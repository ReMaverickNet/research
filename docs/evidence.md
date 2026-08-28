# Evidence and finding format

Every useful result should be traceable back to a session or other reproducible source.

## Evidence record

```yaml
id: EV-0001
type: observation
first_observed: 2026-08-27
session: 2026-08-27-001
build_id: <build>
source:
  - logs/game/2026-08-27-001-PortalWars2.log
  - captures/pcap/2026-08-27-001.pcapng
summary: >-
  Example observation about the launch -> lobby -> matchmaking -> gameplay lifecycle
artifacts:
  - logs/game/2026-08-27-001-PortalWars2.log
  - captures/pcap/2026-08-27-001.pcapng
  - logs/network/2026-08-27-001-connections.txt
ai:
  used: true
  tools: ChatGPT
  purpose: Initial log categorisation and filter suggestions
  verification: Manual verification of endpoints and timestamps
```

## Finding format

```text
# FINDING-0001: Example title

Status: observed
Confidence: high
First observed: 2026-08-27

## Observation
What was directly seen in a log, capture, executable, or reproducible test.

## Evidence
Links to session IDs and artifact paths.

## Interpretation
What the observation probably means.

## Alternatives
Other explanations that have not yet been excluded.

## Next test
The smallest experiment that could increase or decrease confidence.
```

Use `observed`, `inferred`, and `hypothesis` labels rather than presenting all conclusions as equally certain.
