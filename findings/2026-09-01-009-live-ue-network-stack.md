# FINDING-2026-09-01-009: Live gameplay uses Iris with StatelessConnect, DTLS and Oodle handlers

Status: observed
Confidence: high
First observed: 2026-09-01
Sessions: `2026-09-01-001`, Windows Tye captures

## Observation

The active `GameNetDriver` reports Iris as its replication model and loads `OodleNetworkHandlerComponent`, `DTLSHandlerComponent`, and `StatelessConnectHandlerComponent` during server-backed gameplay connection setup. The Windows contributor corpus independently repeats the same stack across all 102 logged `SERVER READY` sessions in the supplied current-build logs.

## Evidence

- `logs/game/2026-09-01-001-PortalWars2-sanitized.log`
- `archive/2026-09-01-001/snippets/match-entry-and-server.txt`
- `logs/game/2026-09-03-001-tye-session-excerpts.txt`
- `networking/gameplay/2026-09-03-001-windows-server-sessions.csv`

## Interpretation

The handler stack is not a Linux-only observation. Its repetition across 102 current-build Windows server transitions materially strengthens the repository's live Unreal networking baseline. This still does not reconstruct the exact wire ordering or payload framing.

## Alternatives / limitations

The published evidence reports the handler initialisation from UE logs; it does not independently decode the protected gameplay payload or prove packet-level handler order.

## Next test

Compare packet-length and timing distributions from a raw Windows session against the existing Linux reference while keeping the same build where practical.

## AI analysis

AI assisted the log grouping and cross-platform comparison; the 102/102 count was checked directly against the supplied logs. Human review should confirm any final repository interpretation.
