# FINDING-2026-08-31-004: Locker badge widget accesses empty texture array

Status: observed
Confidence: high
First observed: 2026-08-31
Session: 2026-08-31-001

## Observation

While the Locker/player-card UI was active, `WBP_PlayerCard_C:UpdateBadges` repeatedly attempted to access indices 0, 1, and 2 of an array named `Textures` when the array length was 0.

The same sequence contains repeated `RequestAsyncLoad() called with empty or only null assets!` messages.

## Evidence

Session: `sessions/linux/2026-08-31-001.md`

Relevant raw-log timestamps:

- 21:00:01.250-21:00:01.253 UTC
- 21:00:34.798 UTC
- 21:03:04.165-21:03:04.166 UTC
- 21:04:24.790-21:04:24.794 UTC

## Interpretation

The badge UI expects texture entries that are absent in the captured runtime state. This is a concrete client-side UI/data error and is not merely a generic Unreal warning.

## Alternatives

- Badge texture data may be intentionally absent when backend services are unavailable.
- The client may be carrying stale or incomplete player-card data.
- The widget may simply fail to guard against an empty badge-texture array.

## Next test

Capture the Locker immediately before and after a successful server-backed match, and compare badge/player-card data and texture-load behaviour.

## AI analysis

ChatGPT was used for initial log triage and extraction of the repeated `UpdateBadges` failure pattern.
