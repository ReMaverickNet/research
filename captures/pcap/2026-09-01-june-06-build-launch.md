# Packet capture metadata: 2026-09-01-june-06-build-launch

- Session: `sessions/linux/2026-09-01-june-06-build-launch.md`
- Evidence record: `sessions/linux/2026-09-01-june-06-build-launch.evidence.yml`

- Source file: `June6.pcapng`
- Format: PCAPNG
- Size: `4,769,164` bytes
- SHA-256: `79a159ca8303ef684e9b84717583ec2fa9327e8e1e697a6ae29647bf8fbc57c9`
- Packet count: `2,295`
- Capture start: `2026-09-01T17:49:15.518383Z`
- Capture end: `2026-09-01T17:49:59.967245Z`
- Duration: approximately `44.449 s`

## Relevant service names observed

The capture contains TLS traffic associated with Maverick production services, including:

- `api-aga-prod.maverick-global.prod.1047games.com`
- `6merlin-prod-updates.maverick-global.prod.1047games.com`
- `server-status-prod.maverick-rooster.prod.1047games.com`
- `client-ip.maverick-global.prod.1047games.com`
- `api.epicgames.dev`

These names establish the presence of the relevant service traffic but do not expose encrypted application payload fields.

## Correlated log sequence

The accompanying game log records:

```text
[2026.09.01-17.49.53:219][882]LogGrpc: Warning: FGrpcRequest - Maverick::Rooster::Api::Metadata::GetErrorCodeConfig - Error:
 Error Code: 7
 Error Message: RBAC: access denied
[2026.09.01-17.49.53:219][883]LogOnlineServices: Warning: [UPortalWarsErrorCodeConfig::QueryConfigInternal] Failed: Result[[1.1.16] unknown]
[2026.09.01-17.49.53:221][883]LogOF1047: Warning: Failed to query config Online.Config.ErrorCodes: [1.1.16] unknown
[2026.09.01-17.49.54:340][949]LogGrpc: Warning: FGrpcRequest - Maverick::FUserClient::Login - Error:
 Error Code: 9
 Error Reason: GAME_VERSION_MISMATCH
[2026.09.01-17.49.54:340][950]LogOnlineServices: Warning: [FAuth1047::Login] Failure: MaverickClient login [2.99.9] GAME_VERSION_MISMATCH - Unknown Error: GAME_VERSION_MISMATCH
[2026.09.01-17.49.54:340][950]LogOF1047: Warning: [FOF1047LoginRequest::MaverickLogin] Failure: Maverick login failed [2.99.9] GAME_VERSION_MISMATCH - Unknown Error: GAME_VERSION_MISMATCH
```

The exact encrypted RPC response contents are not observable from the supplied PCAP.

## Related platform evidence

- Proton metadata extract: `logs/proton/2026-09-01-june-06-build-launch.txt`
- Raw Proton log: `steam-2918300.log` (private)
- Raw Proton log size: `88,839,363` bytes
- Raw Proton log SHA-256: `fab061e36f500db2b24581ddb15e7f9c5468dd991f643b7c9fda82cdc9d8cdfe`

The Proton log confirms that this was a Linux session running the Windows client through Proton.
