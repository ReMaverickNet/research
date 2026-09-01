# FINDING-2026-09-01-012: Blueprint division-by-zero executes repeatedly during gameplay

Status: observed
Confidence: high
First observed: 2026-09-01
Session: 2026-09-01-001

## Observation
`LogScript` emits `Script Msg: Divide by zero: Divide_DoubleDouble` 128 times. Occurrences span startup, active gameplay, and the post-match/loading phase, with a large cluster during the TDM period.

## Evidence
- `archive/2026-09-01-001/evidence/divide-zero-events.txt`
- `archive/2026-09-01-001/evidence/log-counts.json`
- `logs/game/2026-09-01-001-PortalWars2-sanitized.log`

## Interpretation
This is a genuine runtime Blueprint/script error condition: a division operation executed with a zero denominator. The evidence does not identify the owning Blueprint graph, numerator, resulting value, or user-visible effect. The participant reports no obvious gameplay or UI problem and the match completed successfully.

## Alternatives
The calculation may belong to UI, animation, scoring, telemetry, audio, inventory, ability, or another helper path. Some occurrences may be harmless fallback behaviour.

## Next test
Correlate each warning cluster with nearby widget, score, inventory, ability, animation, and audio logs, then reproduce the smallest isolated action that triggers the same warning.
