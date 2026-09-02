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

AI assistance was used during this session and is recorded here for reproducibility.

- Provider/product: OpenAI ChatGPT
- Model: GPT-5.6 Luna
- Date of AI-assisted analysis: 2026-09-03
- Source material provided to the AI: the June 6 capture bundle (`June6.pcapng`, `PortalWars2.log`, and `steam-2918300.log`) and the ReMaverick research repository documentation/current `main` contents.
- GitHub access: repository contents were reviewed from the public `main` branch.
- Tasks: initial log triage; packet-capture metadata/timing interpretation; comparison against existing repository documentation; assessment of the `GAME_VERSION_MISMATCH` launch sequence; and analysis of the popup's SG2 background versus Arena Reloaded dialog colour treatment.
- Generated code executed: no.
- Independent checks: the recorded build identifiers, launch result, `Online.Config.ErrorCodes` RBAC failure, `GAME_VERSION_MISMATCH` log sequence, Linux/Proton environment, and packet timing were checked against the supplied source material and the committed repository records.
- Interpretation boundary: the SG2/Arena Reloaded colour attribution is a visual observation. The conclusion that popup presentation is client-side remains an inference/hypothesis because the login response is TLS-encrypted and its application payload fields were not decoded.

AI-generated interpretation is not treated as independent evidence.
