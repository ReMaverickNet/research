# EMPULSE ranked/practice timeline

> **Scope:** EMPULSE: correlated PCAP + Orion + LocalAppData observations.

| UTC time | Event | Evidence | Scope |
|---|---|---|---|
| 01:28:53.387 | Ranked capture begins | PCAP | EMPULSE |
| ~01:29 | Maverick/global/orion/L4 service startup burst | PCAP + Orion | SHARED service family; EMPULSE observation |
| 01:29:37.868 | L4 TCP/4222 connection starts | PCAP | EMPULSE |
| 01:29:37+ | NATS server INFO banner / TLS follows | PCAP bytes | EMPULSE |
| 01:29:43.861 | `ReportServerSessionManager`, size 370 | Orion | EMPULSE; correlated with L4 |
| ~01:30 | Ranked/practice activity begins | Session context + Orion | EMPULSE |
| 01:30:05.391 | Plaza practice-range browse/world entry | Orion | EMPULSE |
| shortly after | World reports `NetMode=Standalone` | Orion | EMPULSE |
| during range | Dummy/weapon/grapple/mech events | Orion | EMPULSE |
| during queue | No `SERVER READY` / authoritative gameplay endpoint | Orion + PCAP | EMPULSE negative evidence |
| after cancellation | Control-plane connections remain active | PCAP/Orion | EMPULSE |
| 01:39:30.123 | First PCAP ends while game is still open | PCAP | EMPULSE |
| ~01:39:53.743 | Engine shutdown | Orion | EMPULSE |
| ~01:39:54.575–01:39:54.576 | NATS disconnect/close | Orion | EMPULSE |
| close capture | L4/60000 and other API connections tear down | PCAP | EMPULSE |

The timeline is deliberately phrased so that “no endpoint observed” is not treated as proof that no backend session/ticket existed server-side.
