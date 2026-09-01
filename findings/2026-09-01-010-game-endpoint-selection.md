# FINDING-2026-09-01-010: Final gameplay endpoint appears after a broader service-discovery/control-plane phase

Status: inferred
Confidence: medium
First observed: 2026-09-01
Session: 2026-09-01-001

## Observation
Before the UE client browses to `GAME_ENDPOINT_01:30925`, the PCAP records DNS activity for multiple Maverick AGA/global/L4 services, server-status and content services, gaming-SDK gateway/latency services, and multiple `*.edgegap.net` names. The exact gameplay endpoint is not itself present as an obvious matching DNS answer in the captured DNS question/answer data.

## Evidence
- `networking/discovery/2026-09-01-001-dns-queries.csv`
- `logs/networking/2026-09-01-001-pcap-summary.txt`
- `archive/2026-09-01-001/snippets/match-entry-and-server.txt`

## Interpretation
The timing is consistent with a control-plane/application-level stage that determines or exposes the final game endpoint before the Unreal connection begins. The exact allocator is unresolved.

## Alternatives
The endpoint may have been supplied through encrypted HTTPS/API data, cached state, or another application-level mechanism. The presence of Edgegap names alone does not prove that the gameplay endpoint is an Edgegap node.

## Next test
Capture a second matchmaking session and correlate every HTTPS/application connection immediately before `SERVER READY` and `Browse` with the eventual endpoint appearance.
