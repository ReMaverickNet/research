# Research Roadmap

_Last updated: 2026-09-01_

This roadmap is organised around the evidence we have now, rather than treating the project as one linear reverse-engineering task. The **current SGAR investigation is the primary track**; the June 6, 2025 Splitgate 2 build is a separate historical compatibility track.

## Priority order

When the preservation window is limited, prioritise:

**live network capture > game / launcher logs > build metadata > static file inventory > speculative reverse engineering**

The repository remains evidence-first. A plausible architecture is not a confirmed architecture until a reproducible observation supports it.

---

## Phase 0: Final live-service baseline

**Status: active — critical before September 3, 2026**

Capture the production system while the official dedicated-server infrastructure is still operating.

- [ ] Record the current public Steam build ID and relevant depot IDs.
- [ ] Record executable hashes and Unreal build / changelist information.
- [ ] Capture clean launch, launcher and anti-cheat lifecycles.
- [ ] Capture login, account-service, party and lobby flows.
- [ ] Capture matchmaking from queue start through match assignment.
- [ ] Capture the exact transition from `SERVER READY` to Unreal `Browse` / `SendInitialJoin`.
- [ ] Capture gameplay sessions with controlled player counts.
- [ ] Capture match completion, disconnect, timeout and reconnect behaviour.
- [ ] Repeat critical tests on Windows and Linux / Proton where practical.

### Immediate experiment

Run a **narrow matchmaking → `SERVER READY` → `Browse` capture** and correlate, by timestamp and process, every relevant outbound connection immediately before the final gameplay endpoint appears.

The goal is to identify the endpoint-selection handoff, not to guess which production hostname owns it.

---

## Phase 1: Map the live online stack

**Status: active**

Turn the captures into a service and lifecycle map.

- [x] Establish a real official-server Unreal gameplay session.
- [x] Establish that control/service traffic precedes the gameplay connection.
- [x] Establish the observed Unreal gameplay networking stack.
- [ ] Identify which services are involved at each lifecycle stage.
- [ ] Separate Steam / EOS, 1047 services, anti-cheat, telemetry, content and gameplay traffic.
- [ ] Classify endpoints as control-plane, gameplay-plane, relay/intermediary or unresolved.
- [ ] Determine whether the final gameplay endpoint is allocated, relayed or otherwise selected by another service.
- [ ] Repeat endpoint-selection observations across multiple matches.
- [ ] Record ports, directions, timing and transport consistently.

See [NETWORK.md](../NETWORK.md) for the current architecture map and [networking/](../networking/) for the underlying evidence.

---

## Phase 2: Build the central control-plane model

**Status: next engineering track**

Design ReMaverick around the **minimum client-visible control plane**, rather than reproducing the production service count.

- [ ] Define the abstract lifecycle: session → party / lobby → matchmaking → allocation → game endpoint.
- [ ] Define the core domain objects: player, session, party, match, server, build, region, map and game mode.
- [ ] Map observed 1047 service families onto those concepts with confidence labels.
- [ ] Document which components are confirmed, inferred or experimental.
- [ ] Create `ReMaverickNet/central` once the endpoint handoff is sufficiently characterised.
- [ ] Build the server registry and compatibility model first.
- [ ] Add allocation logic independently of the eventual client-facing protocol.
- [ ] Only implement a client-facing compatibility layer once the required behaviour is evidenced.

See [docs/centralisation.md](centralisation.md) for the current design direction.

### Design rule

**Centralise client requirements, not 1047's hostname topology.**

A discovered hostname is not automatically a required service.

---

## Phase 3: Gameplay-server feasibility

**Status: blocked on sufficient protocol evidence**

Treat gameplay as a separate plane from the central service.

- [ ] Determine whether a server target, binary, class or server-oriented code path is shipped or otherwise referenced.
- [ ] Determine the minimum handshake/session requirements for the stock client.
- [ ] Determine which parts of the Unreal networking stack must be reproduced or supplied.
- [ ] Determine the minimum authoritative state required by the client.
- [ ] Establish whether a compatible server can accept the observed connection lifecycle.
- [ ] Prototype a minimal controlled game-server environment only after the protocol boundary is understood.

The goal is not to reproduce 1047's infrastructure. It is to establish the smallest viable ReMaverick gameplay endpoint.

---

## Phase 4: September 3, 2026 transition

**Status: time-critical observation track**

Capture the production transition from dedicated servers / matchmaking to P2P and server-browser behaviour.

### Before shutdown

- [ ] Capture a final dedicated-server matchmaking session.
- [ ] Capture server selection, match entry and exit.
- [ ] Record relevant DNS, endpoint and service changes.

### After transition

- [ ] Capture the first P2P session.
- [ ] Capture server-browser discovery and refresh behaviour.
- [ ] Capture host setup and client join behaviour.
- [ ] Determine whether browser entries come from a directory service, in-game discovery or another mechanism.
- [ ] Determine whether externally hosted servers can be represented by the client.
- [ ] Record connectivity and failure modes.

### Comparison

- [ ] Compare lifecycle, transport, discovery and endpoint semantics before and after the transition.
- [ ] Update [NETWORK.md](../NETWORK.md) with confirmed post-transition architecture.

---

## Phase 5: Historical Splitgate 2 archaeology

**Status: active secondary track**

Keep historical SG2 work separate from SGAR evidence.

The current known June 6, 2025 test reached the loading screen but failed with an unknown error before a playable match. It must not inherit conclusions from the successful SGAR capture.

- [ ] Preserve the recovered June 6 build and Steam manifest metadata.
- [ ] Record build, depot and manifest IDs.
- [ ] Record executable hashes and Unreal metadata.
- [ ] Diagnose the loading-screen unknown error.
- [ ] Determine which online services the historical client expects.
- [ ] Compare historical and SGAR service, configuration and networking expectations.
- [ ] Compare file inventories and hashes across important milestones.
- [ ] Identify the first historical build containing relevant server / P2P components.
- [ ] Investigate old BR, faction, attachment and ability systems only where a preserved build and evidence make the comparison worthwhile.

See [BUILD_TRACKS.md](../BUILD_TRACKS.md) and [docs/old-builds.md](old-builds.md).

---

## Phase 6: RedKard / MerlinAntiCheat compatibility

**Status: separate workstream**

- [ ] Document launcher → anti-cheat → game startup ordering.
- [ ] Document shipped vs runtime-provisioned components.
- [ ] Record observable process, driver, service and IPC behaviour.
- [ ] Compare RedKard packaging across historical builds.
- [ ] Investigate Proton compatibility through observable behaviour.
- [ ] Keep anti-cheat research architectural and compatibility-focused.
- [ ] Do not pursue bypass, evasion, integrity-patching or disabling research.

See [redkard/README.md](../redkard/README.md).

---

## Phase 7: Higher-level services

**Status: deferred**

Only pursue these after the core session and server lifecycle are understood.

- [ ] Profiles / account state
- [ ] Stats
- [ ] Progression / battle pass
- [ ] Inventory / loadouts
- [ ] Events
- [ ] Historical game modes and BR systems
- [ ] Server browser metadata
- [ ] Other live-service functionality

These should be modelled as capabilities rather than assumed to be one monolithic backend.

---

## Research and contribution workflow

Every new capture should ideally produce:

```text
session record
    ↓
relevant evidence / logs / capture summaries
    ↓
candidate observations
    ↓
finding(s) with confidence
    ↓
updated central map where justified
```

Do not skip directly from a raw capture to an architectural claim.

For community contributions, prefer the existing capture guides and GitHub Issues. Contributors do not need to understand the repository structure before submitting useful evidence.

## Long-term documentation

The Git repository remains the **evidence, provenance and source-of-truth layer**.

Once enough repeated observations exist, the stable human-facing architecture and reference material can move into the GitHub wiki. The wiki should explain conclusions and workflows while linking back to the repository evidence that supports them.
