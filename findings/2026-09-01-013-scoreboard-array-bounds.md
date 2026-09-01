# FINDING-2026-09-01-013: Scoreboard widget accesses missing displayed-entry indices at runtime

Status: observed
Confidence: high
First observed: 2026-09-01
Session: 2026-09-01-001

## Observation
At approximately 02:55:25 UTC, `WBP_ScoreboardPlayer_C:UpdateStatValueWidgets` attempts to access `CurrentDisplayedEntries` indexes 1 and 2 while the array length is 1.

## Evidence
- `archive/2026-09-01-001/snippets/key-evidence-with-source-lines.txt`
- `logs/game/2026-09-01-001-PortalWars2-sanitized.log`

## Interpretation
This establishes a real runtime Blueprint array-bounds condition inside the scoreboard widget. It may be recovered/defensive UI behaviour, or it may have affected one or more displayed values. No visible failure was reported by the participant.

## Alternatives
The widget may intentionally probe optional entries and tolerate the failed accesses, or the warning may correspond to a brief state during scoreboard construction.

## Next test
Record the live scoreboard visually while capturing the same log window and compare each displayed field with the warning timing.
