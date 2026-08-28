# Linux / Proton capture guide

Arena Reloaded's official PC requirements currently list Windows 10 as the minimum OS while 1047 describes Linux support as experimental through Proton 10.0-1 and above. SteamDB also lists Linux support and SteamOS compatibility metadata. citehttps://support.splitgate.com/hc/en-us/articles/32057144530071-Minimum-Specs

Linux captures are valuable because the Proton compatibility layer exposes some additional information about how the Windows client interacts with the host system.

## 1. Enable Proton logging

Add this Steam launch option:

```text
PROTON_LOG=1 %command%
```

Valve documents that this produces a per-game log named `steam-$APPID.log`; for Arena Reloaded the AppID is `2918300`.

You can redirect Proton logs with `PROTON_LOG_DIR` when you want them grouped with ReMaverick session data.

## 2. Game log

The Windows game log is still useful under Proton. It is normally exposed inside the Proton prefix under the game's Windows-compatible `AppData/Local` path. Search for:

```text
PortalWars2/Saved/Logs/PortalWars2.log
```

Record the exact location from your prefix rather than assuming all Proton setups use the same Steam library path.

## 3. Capture network traffic

Wireshark can capture the same host interface used by the Proton process. `tcpdump` is also useful when you prefer a lightweight CLI capture:

```text
sudo tcpdump -i <interface> -w arena-reloaded.pcapng
```

Start before the test and stop afterwards. Identify the interface with `ip link` or `ip route`.

## 4. Keep Proton and game activity correlated

Record:

- Proton version
- Steam launch options
- game build
- UTC test window
- Linux distribution/kernel
- network interface
- game mode and host/client role

Where possible, correlate Proton log timestamps with `PortalWars2.log` and packet timestamps.

## 5. Reduce unrelated traffic

A Linux host may have substantially more background network activity than the game itself. For a useful research capture:

1. Close unrelated applications.
2. Stop background downloads and update jobs.
3. Record which network interface was captured.
4. Use DNS and endpoint timing to identify candidate game connections.
5. Treat every candidate as unverified until correlated with the game log or process activity.

## 6. AI-assisted analysis

AI can help parse large Proton logs, generate shell/awk/Python filters, cluster endpoints, or compare Windows and Linux captures. Document the model/tool, task, and verification in the session record.
