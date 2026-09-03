#!/usr/bin/env python3
"""Safely inventory a private PortalWars2 local prefix for ReMaverick research.

The tool deliberately emits metadata and hashes rather than copying proprietary
payloads. Run it against an extracted private prefix; never point it at a public
checkout containing game assets.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def mtime_utc(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def public_relpath(relative: str) -> str:
    """Remove account/session identifiers that are unnecessary for public metadata."""
    relative = relative.replace("\\", "/")
    relative = re.sub(r"(^|/)Steam_[0-9]{8,}(?=/|$)", r"\1Steam_<redacted>", relative)
    relative = re.sub(
        r"(^|/)([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})(?=/|$)",
        r"\1<uuid>",
        relative,
    )
    return relative


def classify(relative: str) -> str:
    path = relative.replace("\\", "/")
    if "/Saved/Logs/" in path:
        return "game-log"
    if "/Saved/PersistentDownloadDir/CMS/Snapshots/" in path:
        return "cms-snapshot"
    if "/Saved/PersistentDownloadDir/CMS/Assets/" in path:
        return "cms-asset"
    if "/Saved/PersistentDownloadDir/Localization/" in path:
        return "localization"
    if "/Saved/Cloud/" in path:
        return "cloud-save"
    if "/.sentry-native/reports/" in path:
        return "crash-dump"
    if "/.sentry-native/" in path:
        return "sentry-runtime"
    if path.endswith("GameUserSettings.ini"):
        return "user-settings"
    if "/ImGui/" in path:
        return "imgui-config"
    if path.endswith("upipelinecache") or path.endswith(".shaderCacheVersion"):
        return "render-cache"
    if "/UnrealEngine/" in path:
        return "engine-config"
    return "other"


def normalise_manifest_path(raw_path: str) -> str:
    marker = "AppData/Local/PortalWars2/"
    if marker in raw_path:
        return "PortalWars2/" + raw_path.split(marker, 1)[1]
    return raw_path


def cache_rows(prefix: Path):
    manifest_path = prefix / "Saved/PersistentDownloadDir/CacheManifest.json"
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = payload.get("Entries")
    if not isinstance(entries, list):
        raise ValueError("CacheManifest.json has no list-valued 'Entries' field")
    for entry in entries:
        category = entry.get("Category", "")
        ident = entry.get("Id", "")
        dataset = version = content_id = ""
        source_url = ""
        if category == "CMS/Assets":
            dataset = "asset"
            source_url = ident
        else:
            match = re.match(r"^(.*)-(\d+\.\d+\.\d+)-([0-9A-Fa-f]{64})$", ident)
            if match:
                dataset, version, content_id = match.groups()
            else:
                dataset = ident
        yield {
            "category": category,
            "dataset": dataset,
            "version": version,
            "content_id": content_id,
            "local_path": normalise_manifest_path(entry.get("FilePath", "")),
            "saved_timestamp": entry.get("SavedTimestamp", ""),
            "expiration_seconds": entry.get("DiskExpirationTimeSeconds", ""),
            "source_url": source_url,
        }


def write_csv(path: Path, headers, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prefix", type=Path, help="Extracted PortalWars2 directory or a Local directory containing it")
    parser.add_argument("output", type=Path, help="Output directory for derived metadata")
    parser.add_argument("--no-hash", action="store_true", help="Skip file SHA-256 calculation for a faster triage pass")
    args = parser.parse_args()

    prefix = args.prefix
    if prefix.name != "PortalWars2":
        candidate = prefix / "Local/PortalWars2"
        if candidate.is_dir():
            prefix = candidate
        else:
            candidate = prefix / "PortalWars2"
            if candidate.is_dir():
                prefix = candidate
    if not prefix.is_dir():
        raise SystemExit(f"PortalWars2 directory not found below {args.prefix}")

    out = args.output
    out.mkdir(parents=True, exist_ok=True)

    files = sorted((p for p in prefix.rglob("*") if p.is_file()), key=lambda p: str(p).lower())
    inventory = []
    for path in files:
        relative_raw = path.relative_to(prefix).as_posix()
        inventory.append([
            public_relpath(relative_raw),
            classify("PortalWars2/" + relative_raw),
            path.stat().st_size,
            mtime_utc(path),
            "" if args.no_hash else sha256(path),
        ])
    write_csv(out / "artifact-inventory.csv", ["relative_path", "category", "size_bytes", "mtime_utc", "sha256"], inventory)

    manifest_entries = list(cache_rows(prefix))
    cache_output = []
    for row in manifest_entries:
        local = prefix.parent / row["local_path"]
        if not local.exists():
            local = prefix / row["local_path"].removeprefix("PortalWars2/")
        cache_output.append([
            row["category"], row["dataset"], row["version"], row["content_id"],
            row["local_path"], local.stat().st_size if local.exists() else "",
            row["saved_timestamp"], row["expiration_seconds"], row["source_url"],
        ])
    write_csv(out / "cache-manifest.csv", [
        "category", "dataset", "version", "content_id", "local_path", "size_bytes",
        "saved_timestamp", "expiration_seconds", "source_url"
    ], cache_output)

    summary = {
        "files": len(files),
        "bytes": sum(p.stat().st_size for p in files),
        "categories": dict(sorted(Counter(row[1] for row in inventory).items())),
        "cache_entries": len(manifest_entries),
        "cache_categories": dict(Counter(row["category"] for row in manifest_entries)),
        "versioned_datasets": {},
    }
    versions = defaultdict(set)
    for row in manifest_entries:
        if row["version"]:
            versions[row["dataset"]].add(row["version"])
    for dataset, values in sorted(versions.items()):
        summary["versioned_datasets"][dataset] = sorted(values, key=lambda item: tuple(map(int, item.split("."))))
    (out / "intake-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(f"Inventoried {len(files)} files ({summary['bytes']:,} bytes)")
    print(f"Cache manifest: {len(manifest_entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
