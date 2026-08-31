# FINDING-2026-08-31-002: RedKard loads but EOS reports anti-cheat unavailable under Proton

Status: observed
Confidence: high
First observed: 2026-08-31
Session: 2026-08-31-001

## Observation

The Proton trace records native loading of:

- `C:\ProgramData\RedKard\Splitgate 2\bin\anticheat.x64.redkard.exe`
- `C:\ProgramData\RedKard\bin\RedKard.sys`
- `RemappedPlugins\1047\MerlinAntiCheat\ThirdParty\equ8_client\client.x64.redkard.dll`

The RedKard driver path then reports `Unhandled exception code c0000409`, followed by Wine service-pipe errors.

The game later logs:

`LogEOSAntiCheat: [AntiCheatClient] Anti-cheat client not available. Verify that the game was started using the anti-cheat bootstrapper if you intend to use it.`

Later in the same session, Merlin reports receiving data from `ReportServerSessionManager`.

## Evidence

Session: `sessions/linux/2026-08-31-001.md`

Relevant raw Proton-trace timings:

- RedKard anti-cheat executable loaded around trace timestamp 737.540
- `RedKard.sys` loaded around 738.348
- `RedKard.sys` throws `c0000409` around 738.349
- EOS anti-cheat-unavailable message around 743.369
- Merlin client loads around 739.498 and logs its plugin initialisation later
- `ReportServerSessionManager` data received at 21:00:29.346 UTC

## Interpretation

The practice range is not a credible cause of the EOS anti-cheat-unavailable message in this session: the message occurs during early application startup, before `MOD_PracticeRange` is activated and before the training map is entered.

The current stronger hypothesis is that the RedKard bootstrap/service/driver path is not functioning correctly under this Proton environment. The `c0000409` exception and service-pipe errors are especially relevant because the EOS warning explicitly refers to the anti-cheat bootstrapper.

The fact that Merlin subsequently receives `ReportServerSessionManager` data shows that the client-side anti-cheat integration is not simply absent.

## Alternatives

- The game may deliberately operate with anti-cheat disabled for this particular client state or platform.
- EOS anti-cheat availability may be gated separately from the local Merlin client.
- Steam's launch path may not invoke the exact bootstrap sequence expected by this build.
- Some observed RedKard failures may be Wine/Proton compatibility issues rather than a server-side decision.

The current capture cannot distinguish these alternatives conclusively.

## Next test

Repeat the capture in a real server-backed arena match. Record whether the game permits matchmaking and whether the EOS/RedKard messages differ when a server session is created. A Windows comparison would also be highly valuable for establishing whether the `c0000409` and EOS warning are Proton-specific.

## AI analysis

ChatGPT was used for initial trace correlation. No claim here should be considered proof of a bootstrap design or incompatibility mechanism until independently verified against additional captures or binaries.
