# FINDING-2026-09-03-020: EMPULSE Ranked provides a future reference for SGAR Ranked reconstruction

Status: observed / future research use
Confidence: high for the documented availability gap; medium for the future architectural utility
First observed: 2026-09-03
Related session: 2026-09-03-003-empulse-ranked-analysis

## Observation

EMPULSE still exposes a functioning Ranked matchmaking path in the captured production build. The September 3 EMPULSE experiment reached the Ranked matchmaking/control-plane stage and kept persistent Maverick L4 infrastructure active, including a NATS-backed TCP/4222 connection and a companion TCP/60000 channel. The experiment did not reach a final gameplay endpoint.

Current SGAR no longer provides an equivalent Ranked experiment. The repository's live-build SGAR evidence records Ranked as unavailable: the client reports rank `-1` and matchmaking fails immediately, preventing a meaningful Ranked queue/control-plane capture in the current build.

## Interpretation

Because the current SGAR build cannot reproduce the Ranked lifecycle, EMPULSE may become an important **comparative reference** when ReMaverick eventually implements or restores community-run SGAR backend functionality.

The EMPULSE capture provides a surviving example of Maverick handling a Ranked-capable client at the control-plane level. Its L4/session-management observations may help narrow the expected SGAR Ranked architecture when the missing SGAR Ranked logs or live backend traces are no longer obtainable.

This should be treated as a reconstruction aid, not as proof that EMPULSE's Ranked protocol is byte-for-byte identical to SGAR's former Ranked implementation. The first-party developer statement already establishes that Maverick served both games, while EMPULSE-specific behaviour must still be verified against any surviving historical SGAR evidence.

## Why this matters for ReMaverick

SGAR Ranked evidence is unusually difficult to replace once official infrastructure disappears because the current client cannot perform a useful Ranked matchmaking experiment and historical production logs/captures may no longer be fetchable.

EMPULSE therefore preserves a live, same-backend comparison point for questions such as:

- which Maverick L4/session-management services remain active during Ranked;
- whether Ranked uses session/ticket state before a gameplay endpoint exists;
- where `ReportServerSessionManager` activity sits in the lifecycle;
- what control-plane traffic precedes successful server allocation in a Ranked-capable client;
- which parts of the control plane appear common between the two games.

## Evidence

- `archive/2026-09-03-003-empulse-ranked-intake/executive-findings.md`
- `archive/2026-09-03-003-empulse-ranked-intake/sgar-vs-empulse.md`
- `archive/2026-09-03-003-empulse-ranked-intake/proton-log-findings.md`
- `archive/2026-09-03-003-empulse-ranked-intake/pcap-findings.md`
- `findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md`
- Existing SGAR Ranked observations in the current repository, where available.

## Limits

This finding does **not** establish that EMPULSE's Ranked mode is identical to SGAR Ranked, that the observed L4/NATS traffic is the allocator, or that `ReportServerSessionManager` is the matchmaking broker. Those remain open questions for future comparison against preserved SGAR evidence or successful ReMaverick experiments.

## Future use

When ReMaverick begins implementing SGAR Ranked support, use this EMPULSE capture as a comparative reference for the control-plane/session-management layer, while keeping game-specific playlist/rank/ticket semantics separate until independently established.
