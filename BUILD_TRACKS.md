# Build tracks

Keep the current SGAR research and historical Splitgate 2 archaeology separate. Evidence from one track must not silently become evidence for the other.

## SGAR: current live build

This is the primary research target for the September 3, 2026 dedicated-server shutdown window.

Current state:

- Official matchmaking reached a real Unreal gameplay endpoint.
- TDM Bot Arena was captured successfully.
- The live UE networking stack is documented in `findings/2026-09-01-*`.

## Splitgate 2: June 6, 2025 build

This is the historical compatibility/archaeology track.

Current state:

- The recovered build launched successfully.
- It reached the loading screen.
- It then stopped with an unknown error before a playable match was reached.

Do not use the successful SGAR gameplay capture as evidence that this June 6 build reached gameplay.

## Why the split matters

The historical build is useful for comparing client assets, manifests, executable metadata, service expectations and protocol evolution. The SGAR build is currently the stronger source for understanding the live production server architecture.

## Navigation

- [Network architecture](NETWORK.md)
- [Research roadmap](docs/roadmap.md)
- [Historical build notes](docs/old-builds.md)
