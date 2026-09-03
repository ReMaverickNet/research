# PCAP findings and packet methodology

> **Scope:** EMPULSE: packet-level observations from the supplied EMPULSE captures.

## Capture statistics

### Ranked matchmaking / practice session

- Capture: `EmpulseRankedMM.pcapng`
- SHA-256: `804a1cbc2f177785fa64901d7a77c8fe27e749d85651894c1317dd74a5cc614b`
- IP packets parsed: 23,653
- Capture window: 2026-09-03 01:28:53.387Z–01:39:30.123Z
- Duration: ~636.736 s
- IPv4 TCP: 22,636 packets
- IPv4 UDP: 1,017 packets

### Shutdown capture

- Capture: `EmpulseCloseGame.pcapng`
- SHA-256: `627d4952c7663784c8d3066561d8684226731f567b6052cfa461d9d4c73b9de2`

## High-signal observations

- DNS resolves the Maverick global, Orion and L4 service families during client startup.
- The L4 hostname exposes a readable NATS `INFO` banner on TCP/4222 before the TLS handshake.
- The same L4 hostname has a separate long-lived TCP/60000 channel with opaque binary application data.
- Orion AGA uses TLS with `grpc-exp,h2` advertised by ALPN, matching the Orion gRPC calls logged by the game.
- Edgegap-related names are queried, but no authoritative gameplay session to a candidate Edgegap endpoint is established in this capture.
- No direct Unreal gameplay endpoint appears around the practice-range actions.
- L4 and other persistent control-plane connections close near application shutdown.

## Method

The PCAPs were treated as raw evidence. Packet counts and flow metadata were derived without modifying the originals. DNS records, TCP handshakes, TLS/SNI, visible plaintext protocol banners and packet timing were prioritised; opaque encrypted/application payloads were not assigned semantics beyond what the observable framing supports.

## Important negative finding

The unsuccessful Ranked attempt is valuable because it establishes that these control-plane connections can remain active for many minutes without a visible `SERVER READY`/authoritative gameplay endpoint. It does not prove that matchmaking failed before ticket creation or that no server allocation object existed server-side.
