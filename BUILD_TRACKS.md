# Build tracks

Keep the current SGAR research and historical Splitgate 2 archaeology separate. Evidence from one track must not silently become evidence for the other.

## SGAR: current live build

This is the primary research target for the September 3, 2026 dedicated-server shutdown window.

Current state:

- Official matchmaking reached a real Unreal gameplay endpoint.
- TDM Bot Arena was captured successfully.
- The live UE networking stack is documented in `findings/2026-09-01-*`.
- Current Windows contributor logs (August 29–September 2, 2026) use `PortalWars2-CL-600100` / `++PortalWars2+Release-3.1` and contain 102 `SERVER READY` transitions.

### Arena Reloaded historical checkpoint

A supplied NVIDIA Aftermath crash artifact from March 11, 2026 identifies `PortalWars2-CL-588763` / `++PortalWars2+Release-2.2`. This belongs to the Arena Reloaded Season 1 timeframe and is separate from the September CL-600100 live evidence. See `findings/2026-09-03-018-arena-reloaded-s1-gpu-crash-build.md`.

## Splitgate 2: June 6, 2025 build

This is the historical compatibility/archaeology track.

Current state:

- The recovered build launched successfully.
- It reached the loading screen.
- It then stopped with `Unknown Error: GAME_VERSION_MISMATCH` before a playable match was reached.

![June 6, 2025 build showing GAME_VERSION_MISMATCH](docs/GameVersionMismatch.png)

Do not use the successful SGAR gameplay capture as evidence that this June 6 build reached gameplay.

## Why the split matters

The historical build is useful for comparing client assets, manifests, executable metadata, service expectations and protocol evolution. The SGAR build is currently the stronger source for understanding the live production server architecture.

## Navigation

- [Network architecture](NETWORK.md)
- [Research roadmap](docs/roadmap.md)
- [Historical build notes](docs/old-builds.md)
