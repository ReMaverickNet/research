# FINDING-2026-09-01-010: Final gameplay endpoints are dynamically allocated across high UDP ports

Status: observed / inferred
Confidence: high
First observed: 2026-09-01
Sessions: `2026-09-01-001`, Windows Tye captures

## Observation

The September 1 Linux reference showed an authoritative endpoint on UDP/30925 after a broader service-discovery phase. The Windows corpus provides 102 additional current-build `SERVER READY` observations. All 102 use unique UDP ports spanning `30005–32760`; 44 fall in the 31000 range, 31 in the 30000 range and 27 in the 32000 range.

The same public server host can be reused with different ports: the busiest observed host accounts for 19 sessions across 19 distinct ports, and 18 of the 24 observed hosts appear in more than one session. No port is reused across different server hosts in this 102-session sample.

## Capture correlation

Twenty-three Windows server transitions overlap the three supplied gameplay-capable filtered captures (2 + 8 + 13). Every one of those 23 logged authoritative hosts is absent from the filtered PCAP on any transport port, and the exact logged UDP port is likewise absent. This establishes that the **filtered exports cannot preserve the correlated gameplay endpoint**. It does not prove whether the original wide captures contained the packets because the originals were not supplied.

## Evidence

- `networking/gameplay/2026-09-03-001-windows-server-sessions.csv`
- `logs/game/2026-09-03-001-tye-session-excerpts.txt`
- `logs/networking/2026-09-03-001-tye-pcap-summary.txt`
- `archive/2026-09-03-001/event-index.csv`
- `captures/pcap/2026-09-03-001.md`
- Existing Linux reference: `networking/gameplay/2026-09-01-001-game-udp-packets.csv`

## Interpretation

The production arena transport should be modelled as a per-session high-UDP endpoint, not as a fixed destination port or a synonym for UDP/443. Reuse of the same public host with changing ports is consistent with multiple sessions/allocations sharing an address, although the supplied evidence does not establish whether each port maps one-to-one to an individual server process.

The next capture should derive the filter directly from the log's `SERVER READY` endpoint and preserve a small pre-Browse window rather than filtering by service port.

## Alternatives / limitations

`SERVER READY` is a client log breadcrumb and not by itself proof of which backend service allocated the address. The allocator remains unresolved. The supplied filtered PCAPs cannot tell us whether the gameplay traffic was discarded by the contributor's filter or never made it into the export.

## Next test

Re-filter one of the contributor's private raw wide captures using the exact `SERVER READY` IP:port pair, both directions, and a short pre/post connection window. Then compare the packet stream with the corresponding `Browse`/welcome timestamps.

## AI analysis

AI was used to parse and aggregate the 102 log records and correlate their timestamps with the five filtered captures. The counts and absence results were independently checked from the supplied files; the allocator interpretation remains an inference.
