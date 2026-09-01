# Control-plane centralisation

This is a proposed implementation direction derived from the evidence collected so far. It is not a reconstruction of 1047 Games' internal architecture.

## Goal

Implement the smallest ReMaverick-controlled control plane capable of handling the lifecycle required by a compatible client, while keeping gameplay-server implementation separate.

## Proposed model

```text
client
  ↓
ReMaverick Central
  ├─ identity / session
  ├─ party / lobby
  ├─ matchmaking
  ├─ server registry
  ├─ endpoint allocation
  └─ content / configuration hooks
           ↓
     ReMaverick game server
```

## Why centralise

The live SGAR capture shows many service families around matchmaking and startup, followed by a separate direct Unreal gameplay endpoint. The exact production ownership of those services is unresolved. ReMaverick does not need to reproduce that distribution internally unless evidence shows a compatibility requirement for it.

## Design rule

Centralisation should follow observed client requirements, not production hostname count.

A discovered hostname is not automatically a required service. Every implementation component should have a corresponding evidence trail or be clearly labelled experimental.

## Initial components

### Identity / session

Represent the client session and any required account or platform association at a structural level. Do not store or publish credentials or tokens.

### Matchmaking

Represent queueing, match formation and the transition to an allocated server. Exact wire/API behaviour remains to be established.

### Server registry

Track available ReMaverick game servers, their build compatibility, mode, map, region and endpoint.

### Allocation

Choose a compatible server and return the endpoint required for the next connection stage. The exact original 1047 allocation mechanism is still under investigation.

## Deliberately deferred

Gameplay replication, historical-version support, stats, inventory, events, progression, anti-cheat compatibility and the old Battle Royale systems should remain separate workstreams until the relevant behaviour is sufficiently understood.

## Current research gate

Before implementing a client-facing compatibility protocol, capture the narrow matchmaking → `SERVER READY` → `Browse` transition and correlate the final control-plane connections with the endpoint delivered to the client.

Related: [Network architecture](../NETWORK.md), [Build tracks](../BUILD_TRACKS.md), [Roadmap](roadmap.md).
