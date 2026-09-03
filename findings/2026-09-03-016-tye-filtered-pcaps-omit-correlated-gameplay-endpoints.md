# FINDING-2026-09-03-016: Filtered Tye exports contain no packets for log-correlated authoritative endpoints

Status: observed
Confidence: high
First observed: 2026-09-03
Sessions: Windows Tye capture set

## Observation

Three filtered PCAPNG exports overlap 23 `SERVER READY` sessions documented by the supplied current-build logs: 2 in the party/invite-sent capture, 8 in the extended Quick Play capture and 13 in the Quick Play/custom capture. For every one of these 23 sessions, the filtered export contains zero packets to the log-reported authoritative host on any transport port and zero packets to the exact `SERVER READY` UDP port.

The exports instead retain substantial 443 traffic plus DNS/broadcast/multicast and other background traffic.

## Evidence

- `captures/pcap/2026-09-03-001.md`
- `logs/networking/2026-09-03-001-tye-pcap-summary.txt`
- `networking/gameplay/2026-09-03-001-windows-server-sessions.csv`
- `archive/2026-09-03-001/event-index.csv`

## Interpretation

The filtered exports are not suitable as standalone evidence for gameplay packet reconstruction. The filtering method is too tight for this purpose, but the exact original Wireshark expression cannot be recovered from the exports.

The contributor's original collection method remains good: capture broadly first and reduce only after the matching log has identified the dynamic gameplay endpoint.

## Limitations

Only the filtered PCAPNG files were supplied. Therefore this finding does **not** claim that the raw wide captures contained the omitted gameplay packets. That question can only be settled by reprocessing the private originals.

The Solo and Invite-received exports have no overlapping `SERVER READY` event in the supplied logs, so they are not used as evidence for either presence or absence of gameplay traffic.

## Next test

Use the raw private captures. For each `SERVER READY` pair, retain both directions from slightly before `Browse` through session teardown.

## AI analysis

AI parsed pcapng timestamps and L3/L4 flows, then joined capture windows to native UE log timestamps. The zero-packet correlation result was independently checked; the causal claim about the original filter remains explicitly unverified until the raw captures are processed.
