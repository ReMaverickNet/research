# FINDING-2026-08-31-006: Multiple live-service requests fail during an otherwise functional client session

Status: observed
Confidence: high
First observed: 2026-08-31
Sessions: `2026-08-31-001`, Windows Tye logs

## Observation

The client remained usable while several online-service requests failed or returned unavailable data. Existing evidence includes localization manifest failure, cloud-save HTTP 401 responses, game-service configuration failures and a cloud-file resolver warning.

The Windows log corpus adds repeated `rooster-referral-service` failures with `ResponseCode: 9` / `REFERRAL_FAILED`. These occur in multiple September logs that nevertheless contain successful `SERVER READY` → `Browse` → welcome transitions.

## Evidence

- `sessions/linux/2026-08-31-001.md`
- `logs/game/2026-09-03-001-tye-session-excerpts.txt`
- `archive/2026-09-03-001/event-index.csv`

## Interpretation

The new Windows evidence strengthens the existing conclusion that some auxiliary live-service requests can fail without universally blocking a server-backed arena session. `REFERRAL_FAILED` should therefore not be treated as equivalent to matchmaking or gameplay failure.

## Alternatives

The referral service may be optional for the tested path, may be retried/fallbacked, or may be failing because of the live-service state around the shutdown window. The logs do not establish its exact functional dependency graph.

## Next test

Compare referral-service state before matchmaking, after successful server entry, and after returning to the menu on another current-build session.

## AI analysis

AI assisted grouping of repeated error signatures. The presence of the errors and coexistence with successful authoritative sessions were checked directly against the supplied logs.
