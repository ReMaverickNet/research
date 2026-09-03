# Network architecture

Central map of the ReMaverick research model. This document is a navigation layer, not a claim that every stage or service is fully understood.

## Current lifecycle

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

The September 1, 2026 SGAR TDM capture establishes a successful transition from matchmaking/control-plane activity to a direct Unreal gameplay endpoint. The client logs `SERVER READY`, browses the endpoint, sends the initial join, is welcomed by the server, loads Zenith and enters a real gameplay session.

The PCAP independently correlates a large bidirectional UDP flow with that same gameplay session.

The Windows contributor corpus expands the endpoint evidence to 102 current-build server transitions. Every one uses a distinct UDP port in `30005–32760`; the same public host can recur with different ports.

## Control plane

Observed service families include Maverick AGA/global/L4 services, server-status, content, client-IP, gaming-SDK services, EOS services and multiple Edgegap-related hostnames.

The exact responsibility of each service is not yet established. The final allocator/session broker remains an open question.

### First-party clarification: Maverick

On September 2, 2026, Ian stated that **Maverick is the backend for both Splitgate: Arena Reloaded and EMPULSE** and that the same backend can dynamically serve either game. He described EMPULSE as having been built from SGAR with additions and removals, explaining the substantial shared backend behaviour.

This is first-party information from an informal developer discussion and should be kept distinct from packet-derived observations. See [Finding 2026-09-02-011](findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md).

The precise division of responsibilities within Maverick remains unknown.

## Gameplay plane

The live SGAR session uses Unreal's GameNetDriver with Iris replication and the logged Oodle, DTLS and StatelessConnect packet handlers. The Windows Tye corpus independently repeats that same stack across all 102 logged `SERVER READY` sessions.

The current gameplay transport is therefore a dynamic per-session UDP endpoint, not UDP/443 by default. Filtered Windows exports that overlap 23 server sessions contain none of the corresponding server endpoint traffic, so they cannot support wire-level gameplay reconstruction without reprocessing the private raw captures.

The capture is therefore useful for endpoint timing, transport metadata and session correlation, but protected Unreal replication payloads are not expected to be readable directly.

## Custom-map data plane

Windows logs show `CustomMapSupport` requesting map data from the authoritative server, receiving repeated chunks, completing the advertised compressed byte count and then initialising the custom map. Seven such transfers occur across the supplied logs, with repeated compressed/uncompressed size pairs. Two transfer windows overlap the supplied September 2 mixed PCAP, but the filtered export omits the authoritative endpoint.

## P2P transition

As of this document's September 2, 2026 update, the P2P implementation is not yet live. Ian stated that Arena Royale will use P2P, while the old 64-player BR will not due to the host-resource requirements of supporting that player count through P2P.

Ian also stated that RedKard is disabled when P2P is used. Whether its files/components remain present in the client is not yet known.

See [Finding 2026-09-02-011](findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md) for the source note and open questions.

## Evidence status

- **Observed:** direct official-server Unreal gameplay session.
- **Observed:** 102 current-build Windows `SERVER READY` transitions with dynamic UDP ports.
- **Observed:** the same Iris/Oodle/DTLS/StatelessConnect stack across the 102 Windows server transitions.
- **Observed:** server-delivered custom-map data transfers.
- **First-party confirmed:** Maverick is shared by SGAR and EMPULSE.
- **First-party confirmed:** RedKard is disabled for P2P.
- **Inferred:** a control-plane step supplies or determines the final gameplay endpoint.
- **Unknown:** exact allocator and exact application request that provides the endpoint.
- **Unknown:** how much of Maverick remains involved after the P2P transition.

See [findings/](findings/) and [networking/](networking/) for the evidence behind this map.

## Next experiment

Re-filter a private raw Windows capture using the exact `SERVER READY` endpoint before attempting deeper packet reconstruction. Then capture the P2P transition from first launch through the new server-browser flow and compare the service inventory with the September 1 dedicated-server session.
