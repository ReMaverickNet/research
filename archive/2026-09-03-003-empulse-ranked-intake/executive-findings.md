# Executive findings

> **Scope:** EMPULSE + SHARED: EMPULSE evidence with SGAR comparison where stated.

## 1. EMPULSE independently confirms the shared Maverick control plane

**Observed / Correlated — High confidence.**

The ranked capture resolves and connects to the same production Maverick service families already present in the SGAR research: global AGA, Orion AGA, L4 AGA, server-status, content, client-IP and Merlin update infrastructure. This is especially significant because the separate first-party developer statement already recorded in the repository says Maverick is the backend for both SGAR and EMPULSE.

The EMPULSE capture therefore moves the “shared backend” statement from a repository-only first-party observation to a directly observable network correlation: the EMPULSE client really does talk to the same Maverick hostname families while running a live production build.

## 2. L4 AGA is not just an opaque TCP service: it exposes NATS

**Observed — High confidence.**

`api-l4-aga-prod.maverick-global.prod.1047games.com` is used in two distinct persistent TCP flows during the ranked attempt. One is a TCP/4222 connection whose first server application payload is an unencrypted NATS `INFO` line containing the NATS server identity and capabilities. The banner identifies NATS 2.12.6, `nats-prod-2`, cluster `nats-prod`, authentication required, TLS required and JetStream enabled. The subsequent client payload is a TLS ClientHello.

A second long-lived connection to the same hostname is made on TCP/60000. Its first application bytes form a short binary record beginning with a four-byte little-endian length followed by opaque data. The protocol was not identified.

This narrows the L4 service architecture considerably, but **does not prove that NATS itself or the port-60000 channel is the gameplay allocator**.

## 3. Merlin session-manager traffic lines up with the NATS startup window

**Correlated — Medium/High confidence.**

The L4 NATS connection begins at approximately 01:29:37.868Z. `Orion.log` records `LogMerlin: Data Received: Endpoint: ReportServerSessionManager, Size: 370` at 01:29:43.861Z, only ~6 seconds later. The prior Orion backup also contains the same `ReportServerSessionManager` event and later NATS teardown.

The safest interpretation is that the L4/NATS infrastructure is involved in a session-management or telemetry/reporting path used by the client. The evidence is strong enough to prioritise this relationship for follow-up, but not strong enough to equate `ReportServerSessionManager` with match allocation.

## 4. EMPULSE's ranked attempt does not expose a server endpoint handoff

**Observed / Inferred — High confidence for absence within this capture.**

The capture contains no direct Unreal gameplay endpoint analogous to the successful SGAR session. The client does not log a `SERVER READY` transition, an authoritative-server `Browse`, or `SendInitialJoin` during the ranked/practice session. Instead, the first actual world transition logged is a practice-range map browse at 01:30:05.391Z.

This means the experiment reached the control-plane stage but did not provide evidence of the final matchmaking → allocation → gameplay-server handoff. It is therefore valuable precisely because it bounds the failure/stall point.

## 5. The practice range is explicitly standalone

**Observed — High confidence.**

The practice-range world reports `NetMode = Standalone`, with `IsServer=0` and `IsDedicatedServer=0`. This aligns with the purpose of the experiment: ranked matchmaking and local practice were exercised concurrently, allowing local gameplay actions to be distinguished from dedicated-server traffic.

Dummy deaths and mech ability cues appear in the Orion log as local/standalone activity. No new Maverick gameplay endpoint appears when those actions occur. The persistent L4/global/Orion control connections were already established before the practice range began.

This strongly suggests the dummy/mech interactions in this capture do not require an external authoritative gameplay server.

## 6. The LocalAppData snapshot exposes Ranked and backend-oriented configuration

**Observed — High confidence.**

The cache manifest contains versioned CMS/localisation snapshots for entitlements, game-encryption, regions, seasons, ranks, playlists, playlist-groups, stats/leaderboards, XP multipliers, challenge configuration and other service-driven content. The `stat-groups` payload contains strings referencing `Mode.DefaultRanked`, while localisation/cache material includes dedicated playlist/rank structures.

The client therefore has concrete local data for the Ranked system even though the Orion runtime log does not literally print “Ranked matchmaking” or a queue ticket name.

## 7. Edgegap is present in the discovery layer but is not proven to be the allocator here

**Observed — Medium confidence.**

Multiple `*.pr.edgegap.net` names are queried shortly after Maverick control-plane startup. The candidate hostnames resolve, but the ranked capture does not show a clear corresponding TCP/UDP session to those resolved Edgegap addresses. Consequently, Edgegap should remain an **observed service/discovery dependency**, not an asserted allocation mechanism.

## 8. Shutdown sequencing gives another view of control-plane persistence

**Correlated — High confidence.**

The game remains running after the first PCAP stops. The second close-game capture starts shortly before the application actually exits. Orion logs engine shutdown at ~01:39:53.743Z and NATS disconnection/close almost immediately afterward at ~01:39:54.575–01:39:54.576Z. The second PCAP also catches closure of the port-60000 L4 channel, Orion AGA, global AGA and other residual services, followed by Steam crash/API traffic.

This demonstrates that the Maverick control-plane connections are long-lived application-session resources and are explicitly torn down as the game exits rather than being merely short-lived matchmaking calls.

## 9. EMPULSE strengthens, but does not solve, the backend-boundary question

The most important unresolved question is still the same one identified by the SGAR research: **what exact operation supplies the final gameplay endpoint?** EMPULSE adds a new, narrower clue: there is a real NATS-backed L4 service and a companion binary TCP/60000 path active during the ranked attempt, and both persist independently of the local practice world.

This makes L4 session-management traffic a particularly high-value target for a future successful Quick Play or Custom Game capture. The correct experiment is not merely “find an allocator hostname”; it is to correlate the final `SERVER READY` or equivalent state transition with every active L4/global/orion control channel immediately before the endpoint appears.
