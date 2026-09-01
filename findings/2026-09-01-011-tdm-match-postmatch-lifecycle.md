# FINDING-2026-09-01-011: Normal TDM reaches WinningCircle/MVP presentation before the game connection closes

Status: observed
Confidence: high
First observed: 2026-09-01
Session: 2026-09-01-001

## Observation
The client enters Deathmatch experience state in `MAP_Zenith/Zenith_Main`, completes the match, creates `WBP_PostMatchTransitionStinger`, loads `Default__EXP_PostGame_Generic_C`, adds the `WinningCircle` level instance, starts confetti/fireworks/trail presentation, and only later closes the gameplay `UNetConnection`. The participant confirms the normal MVP screen appeared with their name, statistics/progression, and celebration presentation.

## Evidence
- `sessions/linux/2026-09-01-001.md`
- `archive/2026-09-01-001/snippets/ormatch-and-postmatch.txt`
- `logs/game/2026-09-01-001-PortalWars2-sanitized.log`

## Interpretation
The post-match phase is a real client-side lifecycle stage rather than an immediate disconnect after the final gameplay state. It includes dedicated level/UI/cinematic/VFX systems and provides a useful preservation target for the pre-shutdown official-server baseline.

## Alternatives
The supplied log does not isolate one explicit `MatchEnded` event as the authoritative transition point, so the exact server-side completion moment remains unresolved.

## Next test
Correlate the first post-match state packet, final scoreboard values, and WinningCircle creation timestamp in a fresh capture.
