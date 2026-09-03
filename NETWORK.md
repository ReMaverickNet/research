# Network architecture

Central map of the ReMaverick research model. This document is a navigation layer, not a claim that every stage or service is fully understood.

## Current lifecycle

> **Scope:** SHARED architecture map. Individual observations below identify EMPULSE, SGAR or shared evidence explicitly.

```text
launch
  ↓
auth / platform services
  ↓
lobby / party
  ↓
matchmaking
  ↓
server allocation / endpoint selection
  ↓
Unreal Browse
  ↓
SendInitialJoin
  ↓
server welcome
  ↓
gameplay
  ↓
post-match / results
```

## Current evidence

> **Scope:** SGAR baseline.

The September 1, 2026 SGAR TDM capture establishes a successful transition from matchmaking/control-plane activity to a direct Unreal gameplay endpoint. The client logs `SERVER READY`, browses the endpoint, sends the initial join, is welcomed by the server, loads Zenith and enters a real gameplay session.

The PCAP independently correlates a large bidirectional UDP flow with that same gameplay session.

The Windows contributor corpus expands the endpoint evidence to 102 current-build server transitions. Every one uses a distinct UDP port in `30005–32760`; the same public host can recur with different ports.

## EMPULSE control-plane corroboration

> **Scope:** SHARED — EMPULSE directly observes the service families; SGAR equivalence comes from existing research and first-party confirmation.

The 3 September 2026 EMPULSE ranked/practice capture independently reaches the same Maverick service family used by SGAR: global AGA, Orion AGA, L4 AGA, server-status, content, client-IP, Merlin update and associated first-party storage/CMS infrastructure. This corroborates the first-party statement that Maverick is shared between SGAR and EMPULSE.

EMPULSE provides new protocol-level detail for L4. `api-l4-aga-prod.maverick-global.prod.1047games.com:4222` presents a NATS 2.12.6 server banner with JetStream enabled, followed by TLS. The same hostname also has a separate long-lived TCP/60000 binary channel. These observations establish transport characteristics, but not the application responsibility of either channel. In particular, they do **not** establish that L4 is the allocator.

The Orion log records `ReportServerSessionManager` data shortly after the NATS connection becomes active. This makes the L4/session-manager relationship a high-value follow-up target, but the exact session/allocator semantics remain unknown.

The EMPULSE ranked attempt does not produce a `SERVER READY`, authoritative `Browse`, `SendInitialJoin` or direct Unreal gameplay endpoint. The actual world transition in this capture is the Plaza practice range, whose world reports `NetMode = Standalone`. Thus the experiment establishes useful control-plane behaviour without crossing the gameplay-plane boundary.

## Control plane

> **Scope:** SHARED architecture; EMPULSE adds the new L4 protocol observations.

Observed service families include Maverick AGA/global/L4 services, server-status, content, client-IP, gaming-SDK services, EOS services and multiple Edgegap-related hostnames.

The exact responsibility of each service is not yet established. The final allocator/session broker remains an open question.

### First-party clarification: Maverick

On September 2, 2026, Ian stated that **Maverick is the backend for both Splitgate: Arena Reloaded and EMPULSE** and that the same backend can dynamically serve either game. He described EMPULSE as having been built from SGAR with additions and removals, explaining the substantial shared backend behaviour.

This is first-party information from an informal developer discussion and should be kept distinct from packet-derived observations. See [Finding 2026-09-02-011](findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md).

The precise division of responsibilities within Maverick remains unknown.

## Gameplay plane

> **Scope:** SGAR evidence baseline.

The live SGAR session uses Unreal's GameNetDriver with Iris replication and the logged Oodle, DTLS and StatelessConnect packet handlers. The Windows Tye corpus independently repeats that same stack across all 102 logged `SERVER READY` sessions.

The current gameplay transport is therefore a dynamic per-session UDP endpoint, not UDP/443 by default. Filtered Windows exports that overlap 23 server sessions contain none of the corresponding server endpoint traffic, so they cannot support wire-level gameplay reconstruction without reprocessing the private raw captures.

The capture is therefore useful for endpoint timing, transport metadata and session correlation, but protected Unreal replication payloads are not expected to be readable directly.

## Custom-map data plane

> **Scope:** SGAR evidence.

Windows logs show `CustomMapSupport` requesting map data from the authoritative server, receiving repeated chunks, completing the advertised compressed byte count and then initialising the custom map. Seven such transfers occur across the supplied logs, with repeated compressed/uncompressed size pairs. Two transfer windows overlap the supplied September 2 mixed PCAP, but the filtered export omits the authoritative endpoint.

## Practice-range control case

> **Scope:** EMPULSE-specific.

EMPULSE's practice range is explicitly standalone in the captured Orion log. Dummy deaths and mech gameplay cues occur while the client remains in this standalone world. No dedicated gameplay endpoint appears around these events. This is useful as a negative control when correlating gameplay actions with future packet captures.

## P2P transition

> **Scope:** SHARED / future-state context; exact EMPULSE post-cutover behaviour remains to be captured.

As of the 3 September 2026 EMPULSE capture, the official transition to P2P/server-browser operation is the time-critical next observation. Ian stated that Arena Royale will use P2P, while the old 64-player BR will not due to host-resource requirements, and also stated that RedKard is disabled when P2P is used.

See [Finding 2026-09-02-011](findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md) for the first-party source note and open questions.

## Evidence status

- **Observed:** direct official-server Unreal gameplay session in SGAR.
- **Observed:** 102 current-build Windows `SERVER READY` transitions with dynamic UDP ports.
- **Observed:** the same Iris/Oodle/DTLS/StatelessConnect stack across those Windows server transitions.
- **Observed:** server-delivered custom-map data transfers in SGAR.
- **Observed:** EMPULSE uses the same Maverick service families in a live production run.
- **Observed:** EMPULSE L4 AGA exposes NATS 2.12.6/JetStream and a separate TCP/60000 channel.
- **Observed:** EMPULSE practice range is standalone.
- **First-party confirmed:** Maverick is shared by SGAR and EMPULSE.
- **First-party confirmed:** RedKard is disabled for P2P.
- **Inferred:** a control-plane step supplies or determines the final gameplay endpoint.
- **Unknown:** exact allocator and exact application request that provides the endpoint.
- **Unknown:** exact semantics of NATS and TCP/60000 in L4 AGA.
- **Unknown:** how much of Maverick remains involved after the P2P transition.

See [findings/](findings/) and [networking/](networking/) for the evidence behind this map.

## Next experiment

Immediately prioritise a successful EMPULSE Quick Play capture while dedicated matchmaking is still available. Preserve the full raw PCAP, and correlate the exact moment of any `SERVER READY`/match-assignment event against NATS/60000, global AGA, Orion AGA, server-status and Edgegap traffic. After the dedicated-service cutoff, capture the first P2P/server-browser session and compare its service inventory and endpoint semantics.
