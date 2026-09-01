# FINDING-2026-09-01-008: Official matchmaking reaches an authoritative Unreal gameplay endpoint

Status: observed
Confidence: high
First observed: 2026-09-01
Session: 2026-09-01-001

## Observation
During normal matchmaking TDM Bot Arena, the client logs a direct `Browse` to `GAME_ENDPOINT_01:30925`, sends `SendInitialJoin`, is `Welcomed by server`, and loads `MAP_Zenith/Zenith_Main` with `PortalWarsGameModeV2_BP_C`. The PCAP independently contains a 34,939-packet bidirectional UDP flow for the same sanitised endpoint/port lasting about 5m36s. The participant confirms this was an official-server matchmaking match with three bot teammates and four bot opponents.

## Evidence
- `sessions/linux/2026-09-01-001.md`
- `logs/game/2026-09-01-001-PortalWars2-sanitized.log`
- `logs/networking/2026-09-01-001-pcap-summary.txt`
- `networking/gameplay/2026-09-01-001-game-udp-packets.csv`

## Interpretation
The capture directly establishes a real server-backed Unreal gameplay session rather than only platform, lobby, discovery, or matchmaking-service traffic. It establishes authoritative server behaviour from the client's perspective, but not the exact implementation/resource type underneath the endpoint.

## Alternatives
The underlying server could be a VM/container/dynamically allocated instance rather than a dedicated physical machine. The capture does not by itself prove which backend service owns or allocates the endpoint.

## Next test
Repeat normal matchmaking TDM and compare the endpoint-selection sequence and game-server handshake across multiple sessions.
