# Sanitisation map

- Game endpoint → `GAME_ENDPOINT_01`
- Local capture host → `LOCAL_CLIENT`
- Local gateway → `LOCAL_GATEWAY`
- Other observed LAN devices → `LAN_DEVICE_01`, `LAN_DEVICE_02`
- Multicast/broadcast addresses → descriptive labels
- Steam account identifier → `STEAM_ID_USER_01` / redacted
- EOS ClientId/ProductId/SandboxId/DeploymentId → `REDACTED`
- Local Windows/Wine username and user path → `REDACTED_USER` / `C:/USERS/REDACTED`

Raw original captures are not included. Game endpoint identity is intentionally retained only as a stable label so packet/log cross-correlation remains possible without publishing the address.
