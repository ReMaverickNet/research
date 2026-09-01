# FINDING-2026-08-31-003: Loadout attachment paths report invalid targets while weapons remain usable

Status: observed
Confidence: medium
First observed: 2026-08-31
Session: 2026-08-31-001
Corroborating session: 2026-09-01-001

## Observation
The original capture recorded `TargetComponent Not Found` and related attachment/loadout warnings while the affected weapon remained usable. In the September 1 server-backed TDM session, similar component-resolution and invalid/default loadout-slot warnings recur across inventory epochs. The participant explicitly reports that the extended barrel and recoil grip worked normally during the TDM.

## Evidence
- `sessions/linux/2026-08-31-001.md`
- `sessions/linux/2026-09-01-001.md`
- `archive/2026-09-01-001/snippets/match-and-gameplay-errors.txt`
- `archive/2026-09-01-001/evidence/epoch-events.txt`

## Interpretation
The additional server-backed observation strengthens the conservative interpretation that these messages do not prove visible attachment failure. They may represent transient component-resolution, actor re-registration, inventory reconciliation, or stale/default item state while the final visible attachment state still functions.

## Alternatives
- Missing or delayed live-service inventory data may leave partial attachment state.
- Repeated actor registration and recreation may produce stale component references.
- Some definitions may intentionally omit classes or overrides while using fallback behaviour.
- Warnings may be emitted during intermediate loadout epochs even when the final assembled weapon is correct.

## Next test
Record exact screenshots/video after each loadout change in a server-backed session and correlate them with attachment warning bursts to determine whether individual warnings predict any visible state difference.

## AI analysis
ChatGPT was used for initial log triage and cross-session comparison. Weapon identity and the successful visible attachment behaviour were supplied by the tester and should be treated as the authoritative session observation.
