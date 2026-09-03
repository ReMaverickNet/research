# LocalAppData findings

> **Scope:** EMPULSE: findings from the EMPULSE LocalAppData snapshot.

## Cache manifest

`Saved/PersistentDownloadDir/CacheManifest.json` contains versioned CMS and localisation entries. The most relevant categories are:

### CMS snapshots

- error-codes 0.0.8
- entitlements 0.0.47
- game-encryption 0.0.2
- news-feed 0.0.52 and 0.0.53
- price-tables 0.0.1
- seasons 0.0.3
- stat-system-aggregates 0.0.1
- stat-groups 0.0.3
- regions 0.0.3
- xp-multipliers 0.0.18
- stats-leaderboards 0.0.8

### Localisation/content

- playlist-menus 0.0.42
- playlists 0.0.94
- store-offers 0.0.3
- store-sections 0.0.1
- ranks 0.0.13
- playlist-groups 0.0.39
- regions 0.0.3
- xp-multipliers 0.0.18
- points-events 0.0.9
- challenge-schedule 0.0.23
- team-clash 0.0.1
- challenge-templates 0.0.24
- refer-a-friend 0.0.16
- news-feed 0.0.52 and 0.0.53

The presence of Ranked-related stat/localisation material is stronger evidence for the mode existing in the client than a simple UI screenshot would provide.

## Ranked strings

`CMS/Snapshots/stat-groups-*` contains strings referencing `GameStatsF.Category.Arena`, `Mode.DefaultRanked`, and custom/bot-related stat tagging. This establishes that Ranked is represented in the client-side statistics configuration.

## Shutdown message

The newer news-feed snapshot contains the shutdown transition message describing the move to peer-to-peer hosting with a server browser, with dedicated servers and matchmaking being retired on 3 September 2026. This is consistent with the externally confirmed 1047 announcement and provides a locally cached, first-party game-content copy of the intended lifecycle change.

## CMS asset service

The cache manifest stores URLs under:

`https://cms-assets-game-tools.game-tools.mgmt.1047games.com/orion/...`

The ranked PCAP queries the same hostname. This is a direct local-file → live-network correlation for CMS assets.

## Game runtime configuration

Orion initialisation loads the following relevant modules/components:

- `MaverickSdk`
- `CoreOnline1047`
- `OnlineFramework1047`
- `OnlineNetworkUtils1047`
- `OnlineServices1047`
- `OodleNetwork`
- `EOSShared`
- `OnlineServicesEOSGS`
- `OnlineServicesEOS`
- `OnlineServicesEpicCommon`
- `OnlineServicesOSSAdapter`
- `OnlineSubsystemSteam`
- `OnlineSubsystemUtils`
- `SocketSubsystemEOS`
- `DTLSHandlerComponent`

Runtime reports: Unreal 5.7.4 build family, Orion changelist `638989`, net changelist `638918`, EOS SDK 1.19.0.3-49960398, libcurl 8.12.1 and OpenSSL 1.1.1t. These values are useful reproducibility metadata and do not expose personal account data.

## Sensitive items intentionally excluded

The supplied snapshot includes a Steam account-specific cloud-settings filename, machine identifier values in Orion, crash GUIDs, local/private addresses in PCAPs, and platform/account identifiers. Those are retained only in the private source evidence and not copied into repository-ready files.
