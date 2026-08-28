# Historical builds and Steam depot preservation

Historical builds are important because networking and security components can change independently of the visible game version.

## Known Steam identifiers

- Arena Reloaded AppID: `2918300`
- Main game depot: `2918301`
- Current public branch/build should be recorded from SteamDB before every major preservation pass.

SteamDB exposes the game's depot and build history, including historical manifest IDs. It also shows that the depot contains the shipped `MerlinAntiCheat`/RedKard bootstrap components. citehttps://steamdb.info/app/2918300/depots/

## Recommended tool: DepotDownloader

Use the official SteamRE DepotDownloader project. It supports selecting an app, depot, and exact manifest. Older manifests may require an authenticated Steam account, and Steam can restrict historical downloads. citehttps://github.com/SteamRE/DepotDownloader

Example shape:

```text
dotnet DepotDownloader.dll -app 2918300 -depot 2918301 -manifest <MANIFEST_ID> -dir <OUTPUT_DIRECTORY>
```

Do not put a real password into shell history. The tool can prompt for account credentials interactively when authentication is required.

## Finding a manifest

Use SteamDB's history/manifest pages to identify the build you want. Save these identifiers in the repository:

```yaml
appid: 2918300
depot: 2918301
build_id: <steam-build-id>
manifest_id: <steam-manifest-id>
date: <utc date>
source: SteamDB
```

Then download it with DepotDownloader and record the SHA-256 hashes of important files.

## What to preserve

Prefer metadata over redistributed game content:

- Build IDs
- Manifest IDs
- Timestamps
- File inventories
- File sizes
- SHA-256 hashes
- Relevant strings / symbol names
- Observations from running the build

Keep the actual downloaded game files on your own lawful installation/storage. Do not upload them to ReMaverick.

## Version comparison

For each build, compare:

- `PortalWars2Client` executable metadata
- Unreal engine/changelist data
- `anticheat_conf.json`
- RedKard bootstrap filenames and sizes
- Plugins and module names
- Networking-related strings/log categories
- Domains and endpoint behaviour during a clean run
