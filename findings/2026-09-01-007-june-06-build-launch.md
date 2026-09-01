# FINDING-2026-09-01-007: June 6, 2025 build reaches game-version validation

- Status: observed
- Confidence: high
- First observed: 2026-09-01
- Build: 2025-06-06
- Manifest: `7405019827575083750`
- Depot: `2918301`
- App: `2918300`

## Observation

The June 6, 2025 Arena Reloaded build can be launched locally from its historical depot. On startup:

1. The Battle Royale introductory trailer plays successfully.
2. The client proceeds to the loading screen and plays the associated loading music.
3. The client then displays:
   `Unknown Error: GAME_VERSION_MISMATCH`
4. The available actions are `Retry` and `Quit`.

No playable lobby or match was reached during this test.

## Local content

The Battle Royale introductory trailer is present in the historical game files and plays without requiring the current live service to provide the video. This establishes that this onboarding asset was distributed with the client build rather than being fetched at launch from the current service infrastructure.

## Interpretation

`GAME_VERSION_MISMATCH` indicates that the client reaches a version-validation stage before entering a playable session. The exact service responsible has not yet been established, and this result does not by itself demonstrate that the dedicated game server is the component rejecting the client.

The result is therefore useful primarily as a reproducible historical baseline and as a marker for future packet-capture analysis.

## Alternatives

- The version check may be performed by matchmaking, an API/service layer, EOS-related infrastructure, or another service before a game server is allocated.
- The error may reflect the current state of the live backend rejecting an old client version rather than an intrinsic incompatibility between the historical client and its original server.

## Next test

Capture the June 6 build's launch sequence and correlate the appearance of `GAME_VERSION_MISMATCH` with the preceding network requests and connections. Repeat with another historical build to determine whether the same validation path and failure are shared across versions.

## Scope note

This finding records only the observable launch behaviour and local asset discovery. Anti-cheat implementation details and memory-analysis experiments are intentionally not included here because they are not necessary to establish this observation.
