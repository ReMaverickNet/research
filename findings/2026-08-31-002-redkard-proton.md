# FINDING-2026-08-31-002: RedKard loads but EOS reports anti-cheat unavailable under Proton

Status: observed
Confidence: high
First observed: 2026-08-31
Session: 2026-08-31-001
Corroborating session: 2026-09-01-001

## Observation
The Proton trace from the original practice-range session records native loading of RedKard/Merlin components, followed by a RedKard driver/service failure and an EOS anti-cheat-unavailable message. The September 1 server-backed TDM session independently reproduces the latter state while the client successfully enters an official matchmaking game.

The September 1 game log records `OS=Wine/11.0`, Merlin feature startup and a Merlin `ReportServerSessionManager` data event. Separately, EOS logs that the anti-cheat client is not available.

## Evidence
- `sessions/linux/2026-08-31-001.md`
- `sessions/linux/2026-09-01-001.md`
- `logs/anticheat/2026-09-01-001-steam-relevant-sanitized.txt`
- `logs/game/2026-09-01-001-PortalWars2-sanitized.log`
- Original practice-range evidence: RedKard executable/driver/client DLL loading, `c0000409`, Wine service-pipe errors, and EOS anti-cheat-unavailable message.

## Interpretation
The September 1 capture strengthens the conclusion that EOS anti-cheat-client availability and Merlin/RedKard-related client activity are separate observable states under Proton. The EOS warning does not imply that all Merlin/RedKard functionality is absent, and the client can still proceed into a real server-backed arena session in this state.

## Alternatives
- EOS anti-cheat availability may be gated separately from local Merlin functionality.
- Steam's launch path may not invoke the exact bootstrap sequence expected by this build.
- Some RedKard failures may be Proton compatibility issues rather than a server-side decision.
- The build may intentionally permit this game mode/session while the EOS anti-cheat interface remains unavailable.

The supplied evidence cannot distinguish these alternatives conclusively.

## Next test
Repeat a server-backed arena capture under native Windows and Proton, comparing only observable process/service/bootstrap timing and EOS/Merlin log state. Do not infer enforcement state beyond what the traces directly establish.

## AI analysis
ChatGPT was used for trace correlation and comparison against the September 1 server-backed session. AI interpretation is not treated as proof of the underlying bootstrap or enforcement design.
