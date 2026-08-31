# FINDING-2026-08-31-005: Practice Range route and practice-dummy lifecycle observed

Status: observed
Confidence: high
First observed: 2026-08-31
Session: 2026-08-31-001

## Observation

The client entered the practice range by browsing to:

`/MAP_Training/TrainingGrounds_Main?Variant=PortalWarsGameVariant:GV_PracticeRange_Default`

The `MOD_PracticeRange` game feature was activated during startup.

Practice targets use the Blueprint class `BP_PracticeDummy_C`. Killing a practice dummy causes `GF1047HealthComponent` to emit a standalone death event for the dummy owner.

## Evidence

Session: `sessions/linux/2026-08-31-001.md`

Relevant raw-log timestamps:

- Practice-range browse: 21:02:51.433 UTC
- First observed dummy death event after weapon testing: 21:03:49.504 UTC
- Additional dummy death events occur throughout the shooting sequence.

## Interpretation

The practice range has a stable, directly observable map route and variant. Practice-dummy deaths are handled through the `GF1047HealthComponent` attribute/health system and can therefore be used as a clean marker when correlating weapon actions with gameplay logs.

## Alternatives

The log does not establish whether practice-dummy death events are replicated over a network session or are exclusively local in the practice range.

## Next test

Use a server-backed arena match and compare player damage/death messages against the practice-dummy lifecycle. This should help separate standalone gameplay logic from server-authoritative gameplay paths.

## AI analysis

ChatGPT was used for initial log triage and extraction of the reproducible map route and dummy event markers.
