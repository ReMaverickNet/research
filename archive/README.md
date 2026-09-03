# 2026-09-03-002 — Arena Reloaded local-prefix intake

This archive contains **derived, publication-safe metadata only** from a Windows `%LOCALAPPDATA%` prefix supplied as `Local.zip`. The original prefix is **not** included.

## Source

- Source archive: `Local.zip`
- Source SHA-256: `afb49efa29d55679640ba1c29527bcafb6de4ee03b466e73b82199f62d553680`
- Source archive size: `82588081` bytes
- Extracted `PortalWars2` files: `117`
- Extracted bytes: `909,734,848`

## Preserved

- Complete file-level inventory with size, source mtime and SHA-256.
- Complete `CacheManifest.json` metadata with the local path normalised to the game root.
- Snapshot structural probe and hashes.
- Redacted Sentry event metadata.
- Intake summary containing cache category counts, version sets, CMS asset hostnames and build fingerprint.

## Intentionally omitted

- `PortalWars2.log` and backup logs from this bundle (they are already handled by the repository's log/session workflow).
- CMS snapshot/localisation payloads.
- CMS image assets.
- `CloudSettings-V2-prod.sav`.
- Sentry minidump and other crash payloads.
- Any file containing account/player identifiers or authentication material.

These omissions follow the repository's data-handling rules: publish hashes, metadata, observations and reproducible procedures rather than proprietary game files or personal/authentication data.

## Key result

The persistent client cache records **78 objects** across `CMS/Snapshots`, `Localization` and `CMS/Assets`. Multiple revisions of content datasets coexist, providing a local version-history signal. The newest cached `news-feed` revision contains the September 3, 2026 shutdown/P2P/server-browser notice. These observations are recorded in `findings/2026-09-03-019-local-cms-cache.md`.

## Reproduction

Use **XDanfr/PortalWars2-Prefix-Intake v1.0.0** against an extracted private prefix or a Windows `%LOCALAPPDATA%` tree. The reusable tool is maintained separately so the research repository contains the evidence record rather than a one-off intake implementation. Do not point it at a public repository checkout containing proprietary payloads.
