# Session: 2026-09-01-june-06-build-launch

- Type: historical build launch / network correlation
- Platform: Linux client under Proton
- OS: CachyOS Linux (x86_64)
- Proton version: `proton-11.0-2-x86_64`
- Game build date: 2025-06-06
- App: `2918300`
- Depot: `2918301`
- Manifest: `7405019827575083750`
- Product version: `PortalWars2-CL-486885`
- Engine version: `5.5.4-486885+++PortalWars2+Release-1.0`
- Net CL: `486885`
- Approximate capture window: `2026-09-01 17:49:15.518Z` to `17:49:59.967Z`
- Result: `GAME_VERSION_MISMATCH`; no playable lobby or match reached

## Procedure

1. Launch the recovered June 6, 2025 build from its historical depot.
2. Allow the client to progress through its normal startup flow.
3. Preserve the game log and packet capture from the same run.
4. Correlate the logged error sequence with the packet-capture timing.
5. Record UI presentation observations without treating visual interpretation as protocol evidence.

## Result

The client reaches the loading screen and then stops at `Unknown Error: GAME_VERSION_MISMATCH` with `Retry` and `Quit` actions.

The log records `Online.Config.ErrorCodes` failing with `RBAC: access denied`, followed approximately one second later by `Maverick::FUserClient::Login` returning `GAME_VERSION_MISMATCH`.

The popup presents SG2-styled surrounding background treatment while the dialog itself uses the red/dark-blue colour scheme associated with Arena Reloaded popup presentation.

## Evidence handling

Raw source files remain private:

- `June6.pcapng`
- `PortalWars2.log`
- `steam-2918300.log` (Proton log)

Only sanitised excerpts and metadata are intended for repository publication.

Published evidence includes the sanitised Proton runtime metadata at `logs/proton/2026-09-01-june-06-build-launch.txt`. The Proton log identifies the execution environment as Linux and the compatibility layer as Proton; the raw log remains private.

## Analysis provenance

AI assistance (ChatGPT) was used for initial log triage, packet-metadata interpretation, and documentation drafting. The recorded claims were checked against the supplied log and PCAP contents. AI interpretation is not treated as independent evidence.
