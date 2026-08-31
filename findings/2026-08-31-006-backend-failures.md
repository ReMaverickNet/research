# FINDING-2026-08-31-006: Multiple live-service requests fail during an otherwise functional client session

Status: observed
Confidence: high
First observed: 2026-08-31
Session: 2026-08-31-001

## Observation

The client remained usable in the main menu, Locker, and practice range while several online-service requests failed or returned unavailable data.

Notable examples include:

- a localization manifest request reporting `LOCALIZATION_MANIFEST_NOT_FOUND`
- cloud-save activity returning HTTP `401`
- multiple game-service configuration requests reporting unavailable/unknown responses
- a later `FOF1047GameContentResolver` warning for cloud file `[1.1.16] unknown`

The Battle Pass screen failed to load during the manual test because there was no active season, but the UE log does not expose a request named `BattlePass`, so the exact backend request responsible was not identified.

## Evidence

Session: `sessions/linux/2026-08-31-001.md`

Relevant raw-log material occurs across startup, menu navigation and the transition into the practice range.

## Interpretation

The production client can continue executing substantial local gameplay while a number of live services are unavailable. This is important when interpreting other warnings from the same session: a missing asset or invalid inventory entry may be a consequence of incomplete remote state rather than a universally broken client system.

## Alternatives

- Some failures may be intentionally tolerated fallback paths.
- The service responses may be tied to the post-season/post-shutdown state rather than a permanently unavailable backend.
- Different services may have independent failure causes.

## Next test

Capture a server-backed arena game and compare the same service calls before matchmaking, during a match, and after returning to the menu. Record which services become available once a real session exists.

## AI analysis

ChatGPT was used for initial log triage and grouping of the observed backend failures. The Battle Pass cause remains deliberately unassigned because the raw log does not identify its request.
