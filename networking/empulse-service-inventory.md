# EMPULSE service inventory (3 September 2026)

This is a sanitised, repository-ready inventory. IP addresses are observed production addresses at capture time; hostname ownership and application purpose should be treated separately.

| Scope | Hostname | Observed transport | Evidence | Purpose assessment | Confidence |
|---|---|---|---|---|---|
| SHARED | `api-aga-prod.maverick-global.prod.1047games.com` | HTTPS/TLS :443 | DNS + persistent/short flows | Global Maverick AGA/control API | High |
| SHARED | `api-l4-aga-prod.maverick-global.prod.1047games.com` | NATS/TLS :4222; binary TCP :60000 | Direct packet bytes | L4 session/control subsystem; exact role unresolved | High protocol / Medium role |
| SHARED | `api-aga-prod.maverick-orion.prod.1047games.com` | TLS :443, ALPN `grpc-exp,h2` | TLS ClientHello + Orion `LogGrpc` | Orion-scoped Maverick gRPC API | High |
| SHARED | `server-status-prod.maverick-orion.prod.1047games.com` | HTTPS/TLS :443 | DNS + TLS flow | Server-status lookup | High |
| SHARED | `client-ip.maverick-global.prod.1047games.com` | HTTPS/TLS :443 | DNS + TLS flow | Public client-IP lookup | High |
| SHARED | `content-prod.maverick-global.prod.1047games.com` | HTTPS/TLS :443 | DNS + TLS flow | Content/config service | High |
| SHARED | `merlin-prod-updates.maverick-global.prod.1047games.com` | HTTPS/TLS :443 | DNS + TLS flow + Orion | Merlin update distribution | High |
| SHARED | `1047games-maverick-user-files-prod.s3.us-west-2.amazonaws.com` | HTTPS/TLS :443 | Repeated transfers | Maverick user-file storage | Medium |
| EMPULSE | `cms-assets-game-tools.game-tools.mgmt.1047games.com` | HTTPS/TLS :443 | CacheManifest URL + PCAP DNS/SNI | First-party CMS asset delivery | High |
| EMPULSE | `b-*.pr.edgegap.net` | DNS observed | Multiple lookups | Possible hosting/edge discovery | Medium |

## Negative evidence

No authoritative Unreal gameplay endpoint was identified in the ranked/practice capture. This should not be rewritten as proof that EMPULSE never allocates a server; it only bounds this unsuccessful experiment.
