# Reconstructed EMPULSE architecture

> **Scope:** EMPULSE + SHARED: EMPULSE evidence with SGAR comparison where stated.

```text
EMPULSE launch
   ↓
platform / Steam / EOS initialisation
   ↓
Maverick control plane
   ├─ global AGA :443
   ├─ Orion AGA :443 / gRPC
   ├─ L4 AGA :4222 (NATS/TLS)
   ├─ L4 AGA :60000 (opaque TCP)
   ├─ server-status :443
   ├─ content / CMS
   ├─ client-IP
   └─ Merlin / update services
   ↓
Ranked matchmaking attempt
   ↓
[unknown session / allocator boundary]
   ↓
[no observed SERVER READY or gameplay endpoint in this session]
   ↓
Plaza practice range
   ↓
NetMode = Standalone

Application shutdown
   ↓
L4 / NATS / API teardown
```

The strongest cross-game conclusion is that EMPULSE uses the same Maverick control-plane service family as SGAR. The exact operation that transitions from matchmaking to an authoritative gameplay endpoint remains unknown.
