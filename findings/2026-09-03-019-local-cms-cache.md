# Local prefix preserves a versioned CMS/content cache and shutdown messaging

## Status
Confirmed for cache presence and manifest structure; probable for Unreal Compact Binary interpretation.

## Confidence
High for the observations below. The deeper CMS object schema still requires decoding and independent verification.

## First observed
2026-09-03 — Windows local-prefix intake.

## Observation

A Windows `PortalWars2` local prefix contains `Saved/PersistentDownloadDir/CacheManifest.json` plus persistent CMS snapshot, localisation and asset caches. The manifest contains **78 entries**: 14 `CMS/Snapshots`, 25 `Localization`, and 39 `CMS/Assets`. Each snapshot/localisation manifest ID carries a dataset name, dotted content version and a 64-hex content identifier. CMS asset entries carry source URLs.

The manifest also preserves multiple revisions simultaneously, including multiple versions of challenge schedules/templates, news, playlist groups/playlists, seasons, and store sections. This makes the local cache useful as a historical content-version source even without retaining the original HTTP responses.

The cached CMS asset URLs use the `cms-assets-game-tools.game-tools.mgmt.1047games.com` host, with paths including `/rooster/`, `/playlists/Relaunch/`, `/store/`, and `/Events/`. This is direct evidence of a first-party CMS asset namespace present in the client cache, not by itself evidence that this host performed matchmaking or endpoint allocation.

The newest cached `news-feed` revision contains the production notice that on **September 3, 2026** Arena Reloaded would move to peer-to-peer hosting with a server browser while dedicated servers and matchmaking shut down. The older cached `news-feed` revision is also retained, giving a concrete content-version transition rather than only a current-state screenshot/log observation.

The CMS snapshot blobs begin with the byte prefix `b7 75 63 62` and contain structured field markers such as `resourceId`, `gameNamespace`, `contentType`, `eTag`, and dataset-specific fields in several files. This is strongly consistent with Unreal Compact Binary storage; Epic's API documentation describes Compact Binary as a typed structured serialization system. The exact object schema has not yet been decoded here, so this finding does **not** claim field-level semantics beyond the markers directly observed.

## Evidence

- `archive/2026-09-03-002-local-prefix-intake/artifact-inventory.csv`
- `archive/2026-09-03-002-local-prefix-intake/cache-manifest.csv`
- `archive/2026-09-03-002-local-prefix-intake/snapshot-probe.csv`
- `archive/2026-09-03-002-local-prefix-intake/intake-summary.json`
- Source file: `Saved/PersistentDownloadDir/CacheManifest.json`
- Source directory: `Saved/PersistentDownloadDir/CMS/Snapshots/`
- Source directory: `Saved/PersistentDownloadDir/CMS/Assets/`
- Source directory: `Saved/PersistentDownloadDir/Localization/`

## Interpretation

The client is not merely downloading static web assets. It keeps a persistent, version-addressed content cache spanning gameplay playlists, challenges, news, store data, seasonal data, statistics metadata, region metadata and related localisation. This is evidence for a substantial CMS/content-delivery layer in the live client.

The coexistence of historical versions is especially valuable: it allows researchers to reconstruct client-visible content changes from disk even after the service stops serving the corresponding resources.

This finding should remain separate from the control-plane/allocation findings. The presence of a CMS namespace does not establish that CMS participates in authentication, matchmaking, server allocation or gameplay transport.

## Alternatives / limitations

- The manifest's `SavedTimestamp` values are client cache metadata and are not treated as wall-clock timestamps here.
- A cached URL proves that the client downloaded that resource, not which backend component generated the content.
- The asset host may be fronted by CDN infrastructure; the exact origin service is not established.
- The Compact Binary identification remains a format-level hypothesis until the blobs are parsed with a compatible decoder and field-level semantics are checked.
- The local prefix is a point-in-time client state; absence of an object from it does not prove the production service never exposed that object.

## Follow-up

1. Decode the CMS snapshot blobs into a lossless, local-only representation and extract all resource IDs, hashes, cross-references and status fields.
2. Cold-start the game with the persistent CMS cache removed and capture DNS/TLS/request timing for the resulting CMS downloads.
3. Compare the network request metadata against the cache-manifest entry names and version/content IDs.
4. Correlate CMS resource IDs with `CloudSettings-V2-prod.sav` playlist-filter UUIDs without publishing the account-specific save file.
5. Build semantic diffs for the retained dataset revisions.

## Reproduction tooling

The publication-safe intake metadata was generated with **XDanfr/PortalWars2-Prefix-Intake v1.0.0**, the standalone successor to the one-off research-repository script. The release provides the same inventory/cache-manifest workflow, adds conservative identifier/URL sanitisation, and includes a Windows `%LOCALAPPDATA%` launcher for broader user LocalAppData trees.

The source implementation is intentionally maintained outside this evidence repository; this finding records the tool/version used so the transformation remains reproducible.

## External reference

Epic Games Compact Binary API documentation: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/ECbFieldType
