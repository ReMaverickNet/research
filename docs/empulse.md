# EMPULSE research

> **Scope:** EMPULSE-focused entry point. This page points to EMPULSE-specific evidence while explicitly linking shared Maverick conclusions back to the central cross-game architecture.

EMPULSE was built from the SGAR codebase with additions and removals, and first-party evidence in this repository states that Maverick serves both games. The EMPULSE packet captures therefore belong in the same overall architecture, but EMPULSE-specific observations are kept visibly separate so they are not mistaken for SGAR captures.

## EMPULSE-specific findings

- [2026-09-03-012 — shared Maverick service-family observation](../findings/2026-09-03-012-empulse-shared-maverick.md)
- [2026-09-03-013 — L4 NATS / TCP 60000](../findings/2026-09-03-013-empulse-l4-nats.md)
- [2026-09-03-014 — standalone practice range](../findings/2026-09-03-014-empulse-standalone-practice.md)
- [2026-09-03-015 — teardown sequencing](../findings/2026-09-03-015-empulse-teardown.md)

## Cross-game context

- [Network architecture](../NETWORK.md) — central lifecycle map, with EMPULSE and SGAR scope called out explicitly.
- [EMPULSE service inventory](../networking/empulse-service-inventory.md) — sanitised EMPULSE network endpoint inventory.
- [Maverick shared-backend finding](../findings/2026-09-02-011-maverick-shared-backend-and-p2p-transition.md) — first-party source explaining why the common service family is expected.

## Scope convention

- **EMPULSE** — directly observed in EMPULSE evidence.
- **SGAR** — existing Splitgate: Arena Reloaded evidence used as a baseline.
- **SHARED** — supported as common between the games.
- **CROSS-GAME INFERENCE** — plausible comparison that still needs direct confirmation.
- **UNKNOWN** — evidence does not establish the relationship.

The fact that a hostname or subsystem appears in this EMPULSE index does not by itself make its exact internal role known. Service ownership, allocation semantics and protocol responsibility remain evidence questions.
