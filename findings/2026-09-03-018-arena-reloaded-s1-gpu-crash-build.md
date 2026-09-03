# FINDING-2026-09-03-018: NVIDIA Aftermath dump records an earlier Arena Reloaded Season 1 build

Status: observed
Confidence: high
First observed: 2026-03-11
Session: Windows Tye evidence bundle

## Observation

The supplied `D3D12.2026.03.11-22.04.37.nv-gpudmp` contains an Unreal/NVIDIA Aftermath `GPUCrash` context for:

- executable: `PortalWars2Client-Win64-Shipping`
- engine: `5.5.4-588763+++PortalWars2+Release-2.2`
- build: `PortalWars2-CL-588763`
- RHI: D3D12
- GPU: NVIDIA GeForce RTX 5080
- user driver: 595.71
- timestamp: 2026-03-11 22:04:37 UTC

The repository's current September Windows logs are `PortalWars2-CL-600100` / Release-3.1, so this dump is not evidence of a current-build crash.

## Arena Reloaded track placement

The March 11 crash predates the public Season 2 launch on March 27, 2026, so this dump belongs to the Arena Reloaded Season 1 timeframe rather than the separate June 2025 historical Splitgate 2 track.

## Evidence

- `archive/2026-09-03-001/event-index.csv`
- `docs/old-builds.md`
- NVIDIA Aftermath metadata extracted from the supplied dump

## Interpretation

This is useful build archaeology: it gives a concrete Arena Reloaded Season 1 Unreal changelist and release branch that can anchor future comparisons. It does not establish a GPU root cause or a regression into the September 2026 build.

## Limitations

The supplied dump is only the compact `.nv-gpudmp` artifact. It does not provide enough verified context here to claim a faulting shader, instruction or driver defect. Crash GUIDs and machine-specific identifiers are intentionally excluded from repository-facing evidence.

## Next test

Preserve other S1/S2 build metadata as hashes/strings and, where legally available, compare the CL-588763 and CL-600100 client networking/plugin inventories.

## AI analysis

AI extracted and classified the embedded build/crash metadata. The changelist, branch, timestamp and driver fields were directly checked in the supplied dump; the Season 1 placement is based on the dated March 27 Season 2 launch boundary.
