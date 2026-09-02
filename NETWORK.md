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

## Control plane

Observed service families include Maverick AGA/global/L4 services, server-status, content, client-IP, gaming-SDK services, EOS services and multiple Edgegap-related hostnames.

The exact responsibility of each service is not yet established. The final allocator/session broker remains an open question.

### First-party clarification: Maverick

On September 2, 2026, Ian stated that **Maverick is the backend for both Splitgate: Arena Reloaded and EMPULSE** and that the same backend can dynamically serve either game. He described EMPULSE as having been built from SGAR with additions and removals, explaining the substantial shared backend behaviour.

This is first-party information from an informal developer discussion and should be kept distinct from packet-derived observations. See [Finding 2026-09-02-011](findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md).

The precise division of responsibilities within Maverick remains unknown.

## Gameplay plane

The live SGAR session uses Unreal's GameNetDriver with Iris replication and the logged Oodle, DTLS and StatelessConnect packet handlers.

The capture is therefore useful for endpoint timing, transport metadata and session correlation, but does not expose readable Unreal replication payloads.

## P2P transition

As of this document's September 2, 2026 update, the P2P implementation is not yet live. Ian stated that Arena Royale will use P2P, while the old 64-player BR will not due to the host-resource requirements of supporting that player count through P2P.

Ian also stated that RedKard is disabled when P2P is used. Whether its files/components remain present in the client is not yet known.

See [Finding 2026-09-02-011](findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md) for the source note and open questions.

## Evidence status

- **Observed:** direct official-server Unreal gameplay session.
- **Observed:** distinct control/service traffic exists before gameplay.
- **First-party confirmed:** Maverick is shared by SGAR and EMPULSE.
- **First-party confirmed:** RedKard is disabled for P2P.
- **Inferred:** a control-plane step supplies or determines the final gameplay endpoint.
- **Unknown:** exact allocator and exact application request that provides the endpoint.
- **Unknown:** how much of Maverick remains involved after the P2P transition.

See [findings/](findings/) and [networking/](networking/) for the evidence behind this map.

## Next experiment

Capture the P2P transition from first launch through the new server-browser flow after September 3, correlating process, destination, protocol and timing. Compare the service inventory with the September 1 dedicated-server capture and specifically check what remains of Maverick and RedKard.
