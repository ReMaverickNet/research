# SGAR vs EMPULSE

> **Scope:** CROSS-GAME comparison; each row distinguishes direct evidence from the cross-game interpretation.

| Function | SGAR | EMPULSE | Scope / confidence |
|---|---|---|---|
| Auth/platform | Steam/EOS + Maverick services | Steam/EOS + Maverick services | SHARED / High |
| Maverick global | Observed | Observed | SHARED / High |
| Orion AGA | Observed | Observed; gRPC | SHARED / High |
| L4 AGA | Observed as control service | NATS/TLS :4222 + TCP/60000 | SHARED family; EMPULSE adds protocol detail |
| Server status | Observed | Observed | SHARED / High |
| CMS/content | Observed | Observed; local cache URLs corroborate CMS assets | SHARED family / High |
| Matchmaking | Successful SGAR queue-to-server transition | Ranked attempt stalled before visible endpoint | SHARED architecture; outcome differs |
| Allocation | Endpoint handoff observed indirectly through `SERVER READY` | Not reached/observed | UNKNOWN for EMPULSE |
| Unreal gameplay | Direct official-server UDP session | None in this capture | SGAR-only observation here |
| Practice range | Not used as a control in this experiment | `NetMode=Standalone` | EMPULSE-specific |
| Edgegap | Related hostnames already present in prior research | Related DNS observed | SHARED infrastructure family; exact role unresolved |
| Shutdown teardown | Existing capture evidence | L4/NATS/API teardown correlated to exit | EMPULSE-specific timing; architecture likely shared |

## Main comparison

EMPULSE strengthens the case that Maverick is a common control-plane backend while also exposing a concrete L4 transport detail that the SGAR dataset did not previously resolve. The games should therefore be compared as clients of a shared service architecture, not as two wholly independent backend implementations.

At the same time, the successful SGAR gameplay path must not be projected onto EMPULSE: this Ranked experiment never reached the authoritative gameplay boundary.
