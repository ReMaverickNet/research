# Tye Windows SGAR evidence bundle — derived archive

Source contributor: Tye Tye / SGLF
Analysis date: 2026-09-03
Game: SPLITGATE: Arena Reloaded (SGAR)
Internal project/log name: PortalWars2
Current supplied build: PortalWars2-CL-600100 / Release-3.1
Steam AppID: 2918300

## Source material

The contributor supplied five filtered PCAPNG exports, eleven `PortalWars2` logs, a contributor README, and one NVIDIA `.nv-gpudmp`. The original wide PCAPs remain private with the contributor.

## Published log copies

The `logs/` directory contains privacy-reviewed copies of all eleven supplied `PortalWars2` logs. These preserve timestamps, build identifiers, authoritative server IP:port values, Unreal networking events, matchmaking/referral events, custom-map events, errors and connection ordering needed for research.

The following contributor/machine identifiers are redacted from the published copies:

- Windows profile names and `C:\Users\...` filesystem paths
- Unreal `MachineId`
- Steam account identifiers
- per-session Unreal crash GUIDs

Public game-service/server addresses are intentionally preserved where they are part of the network evidence. No attempt is made to anonymise the authoritative endpoints used for PCAP/log correlation.

## What is published

Only derived or privacy-reviewed material is intended for the repository: capture times, packet counts, protocol summaries, sanitised log copies/excerpts, endpoint IDs, UDP ports, build identifiers, map names, transfer sizes, hashes and analysis.

## What is not published

Raw PCAPNGs, raw logs, the original NVIDIA dump, contributor account identifiers, personal filesystem paths, machine identifiers and other unrelated private source material are excluded.

## Important interpretation rule

The filtered exports contain no packet to the log-correlated authoritative hosts/ports for 23 overlapping server sessions. That is evidence about the **filtered exports only**. The raw wide captures must be reprocessed before saying the contributor's filter actually deleted those packets.

## Correlation scope

- 102 `SERVER READY` events across the supplied current-build logs.
- 23 of those overlap three gameplay-capable filtered PCAP windows.
- 2 custom-map transfers overlap the September 2 mixed capture; 5 additional transfers occur outside that capture window.
- Solo and Invite-received captures have no overlapping `SERVER READY` event in the supplied log set.
