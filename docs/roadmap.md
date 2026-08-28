# Research Roadmap

_Last updated: 2026-08-27_

## Phase 0: Freeze the baseline

**Urgency: critical, before September 3, 2026**

- [ ] Record the current public Steam build ID and relevant depot IDs.
- [ ] Record game executable hashes.
- [ ] Record Unreal build / changelist values from `PortalWars2.log`.
- [ ] Capture clean-launch logs.
- [ ] Capture launcher / anti-cheat logs.
- [ ] Capture DNS lookups and outbound connections during launch.
- [ ] Capture login and account-service traffic.
- [ ] Capture party creation / invitation / lobby traffic.
- [ ] Capture matchmaking start, queue, assignment, and match entry.
- [ ] Capture gameplay traffic with multiple player counts.
- [ ] Capture host/client differences.
- [ ] Capture match exit, disconnect, timeout, and reconnect behaviour.
- [ ] Repeat selected tests from Windows and Linux/Proton.

## Phase 1: Map the online stack

- [ ] Identify domains and services contacted at each lifecycle stage.
- [ ] Separate Steam/Epic services, 1047 services, anti-cheat services, telemetry, CDN/content services, and game-session traffic.
- [ ] Determine which endpoints are control-plane vs gameplay-plane.
- [ ] Determine whether gameplay transport is UDP, TCP, or a mixture.
- [ ] Record observed ports, connection directions, and session timing.
- [ ] Determine whether players receive a directly reachable game endpoint or an intermediary/relay endpoint.
- [ ] Identify authentication/session tokens at a structural level without publishing secret material.

## Phase 2: Unreal / client architecture

- [ ] Catalogue interesting modules, plugins and subsystem names.
- [ ] Identify OnlineSubsystem integrations visible in logs/files.
- [ ] Identify networking-related log categories.
- [ ] Determine whether the client contains server-oriented code paths or references.
- [ ] Catalogue console/configuration variables related to networking where safely observable.

## Phase 3: Historical build archaeology

- [ ] Build a manifest table for important milestones.
- [ ] Preserve manifest IDs and build IDs rather than game files.
- [ ] Obtain older builds only through legitimate Steam account access.
- [ ] Compare file inventories and hashes across builds.
- [ ] Track changes to networking, online services, RedKard integration and executable metadata.
- [ ] Identify the first build containing relevant server/P2P components.

## Phase 4: RedKard / MerlinAntiCheat

- [ ] Document the launcher lifecycle.
- [ ] Document which files are shipped vs provisioned at runtime.
- [ ] Record process names, service/driver presence, startup/shutdown ordering, and observable IPC/network activity.
- [ ] Catalogue public references to EQU8 integration.
- [ ] Compare RedKard packaging across historical builds.
- [ ] Investigate Proton compatibility at the level of observable behaviour.
- [ ] Avoid bypass, evasion, patching, or disabling research.

## Phase 5: September 3 transition

- [ ] Capture the final dedicated-server session before shutdown.
- [ ] Capture the first P2P/server-browser session after transition.
- [ ] Compare DNS, endpoints, protocol behaviour, session setup, and browser discovery.
- [ ] Determine whether the post-transition server browser is purely in-game discovery or depends on an external directory service.
- [ ] Determine whether custom external servers can be represented by the browser.
- [ ] Document host requirements and connectivity failure modes.

## Phase 6: Dedicated-server feasibility

- [ ] Determine whether a server target/binary is shipped or referenced.
- [ ] Determine whether authoritative simulation is client-hosted or server-hosted.
- [ ] Determine minimum required online services.
- [ ] Identify protocol compatibility requirements.
- [ ] Prototype only after the architecture is understood.

## Evidence priority

When time is limited, prioritise:

**live network capture > game/launcher logs > build metadata > static file inventory > speculative reverse engineering.**
