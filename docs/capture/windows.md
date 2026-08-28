# Windows capture guide

Windows is the primary capture platform because Arena Reloaded ships as a Windows build.

## Goal

Capture the game's own activity while making it possible to separate:

- the game client
- the launcher
- RedKard / anti-cheat
- Steam and other platform services
- unrelated system traffic

## 1. Prepare a clean session

Before launching the game:

1. Close unrelated games and network-heavy applications.
2. Note the current game build and Steam branch.
3. Start a new Wireshark capture on the active network interface.
4. Start Process Monitor or another process/network observation tool if needed.
5. Create a session folder using the project's [session template](../../SESSION_TEMPLATE.md).

Avoid capturing credentials, cookies, private messages, or other unrelated personal traffic.

## 2. Game log

1047 support documentation identifies the main game log as:

```text
%LOCALAPPDATA%\PortalWars2\Saved\Logs\PortalWars2.log
```

Copy the log after the test, then redact personal or secret data before publishing it.

## 3. Network capture

Wireshark is recommended.

Start the capture before Steam launches the game if you want the full chain. If you only care about the game, start immediately before launch and keep the capture scoped to the test window.

Useful first-pass views include:

```text
ip.addr == <known game endpoint>
tcp
udp
dns
```

Do not assume every connection made by the computer belongs to the game. Correlate packet timestamps with the process and game logs.

## 4. Reduce the capture

After the test:

1. Record the exact start/end time in UTC.
2. Check DNS traffic for domains resolved during the session.
3. Identify remote IPs and ports that appear only during the test.
4. Correlate connection timestamps with `PortalWars2.log`.
5. Separate Steam, anti-cheat, telemetry, CDN, and gameplay/session traffic where the evidence supports doing so.
6. Save the original capture privately and publish only a reviewed copy.

## 5. Suggested test sequence

Run simple, repeatable sessions rather than trying to capture everything at once:

```text
launch
login
wait in menu
join/create party
enter lobby
start matchmaking
enter match
play for several minutes
leave match
return to menu
exit game
```

Repeat with changes to one variable at a time, such as host/client role or player count.

## 6. Record the environment

Always record:

- Windows version
- Steam client version where relevant
- game build/branch
- network type (Ethernet/Wi-Fi)
- VPN/proxy state
- host/client role
- game mode
- player count
- exact test times in UTC

## 7. AI-assisted analysis

AI tools may be used to reduce large logs, suggest Wireshark filters, write parsing scripts, classify endpoints, or propose hypotheses.

Record that use in the session's **AI assistance** section and independently verify important claims against the raw evidence.
