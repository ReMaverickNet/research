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

## Gameplay plane

The live SGAR session uses Unreal's GameNetDriver with Iris replication and the logged Oodle, DTLS and StatelessConnect packet handlers.

The capture is therefore useful for endpoint timing, transport metadata and session correlation, but does not expose readable Unreal replication payloads.

## Evidence status

- **Observed:** direct official-server Unreal gameplay session.
- **Observed:** distinct control/service traffic exists before gameplay.
- **Inferred:** a control-plane step supplies or determines the final gameplay endpoint.
- **Unknown:** exact allocator and exact application request that provides the endpoint.

See [findings/](findings/) and [networking/](networking/) for the evidence behind this map.

## Next experiment

Capture the narrow window from matchmaking through `SERVER READY`, correlating process, destination, protocol and timing immediately before the Unreal connection. The goal is to identify the endpoint-selection handoff without assuming which production service owns it.
