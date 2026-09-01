# FINDING-2026-09-01-009: Live gameplay uses Iris with StatelessConnect, DTLS and Oodle handlers

Status: observed
Confidence: high
First observed: 2026-09-01
Session: 2026-09-01-001

## Observation
The active `GameNetDriver` reports Iris as its replication model and loads `OodleNetworkHandlerComponent`, `DTLSHandlerComponent`, and `StatelessConnectHandlerComponent` during the server-backed gameplay connection.

## Evidence
- `logs/game/2026-09-01-001-PortalWars2-sanitized.log`
- `archive/2026-09-01-001/snippets/match-entry-and-server.txt`

## Interpretation
The live arena connection uses Unreal's Iris replication stack together with the logged Oodle, DTLS and StatelessConnect network handlers. This also explains why raw packet inspection does not expose readily readable gameplay replication/RPC content.

## Alternatives
The published evidence does not independently reconstruct the exact wire ordering or framing of the handler chain beyond what the UE log reports.

## Next test
Compare handler initialisation and packet-length/timing distributions across two or more official-server sessions.
