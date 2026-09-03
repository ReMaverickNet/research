#!/usr/bin/env python3
"""Inventory PCAPNG packet counts and capture metadata without modifying the source file."""
from __future__ import annotations

import argparse
import hashlib
import struct
from pathlib import Path

PCAPNG_SHB = 0x0A0D0D0A
PCAPNG_EPB = 0x00000006
PCAPNG_SPB = 0x00000003


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pcapng", type=Path)
    args = parser.parse_args()
    path = args.pcapng
    data = path.read_bytes()
    if len(data) < 12 or struct.unpack_from("<I", data, 0)[0] != PCAPNG_SHB:
        raise SystemExit("not a little-endian PCAPNG section header")
    offset = 0
    blocks = 0
    epb = 0
    spb = 0
    while offset + 12 <= len(data):
        block_type, block_len = struct.unpack_from("<II", data, offset)
        if block_len < 12 or offset + block_len > len(data):
            break
        blocks += 1
        if block_type == PCAPNG_EPB:
            epb += 1
        elif block_type == PCAPNG_SPB:
            spb += 1
        offset += block_len
    print(f"file={path}")
    print(f"size_bytes={len(data)}")
    print(f"sha256={sha256(path)}")
    print(f"blocks={blocks}")
    print(f"enhanced_packet_blocks={epb}")
    print(f"simple_packet_blocks={spb}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
