# Publication and sanitisation notes

> **Scope:** EMPULSE-derived publication guidance.

The raw source set contains identifying and session-sensitive material. Repository-ready artefacts intentionally retain only what is required to reproduce the architectural conclusions.

## Retained

- Hostnames and service family names that materially identify production infrastructure.
- Ports and observable protocol characteristics.
- Public source-archive hash.
- Build/module metadata needed for reproducibility.
- Timing relationships expressed in UTC.
- Evidence classifications and unresolved questions.

## Excluded

- Raw PCAPs.
- Full Proton log.
- Raw Orion log.
- Steam/account identifiers.
- Machine/local identifiers.
- Authentication material, tokens and cookies.
- Private/local IP information where not necessary.
- Proprietary cached payloads or save files.
- Crash dumps and unnecessary Sentry identifiers.

The raw evidence remains the authoritative private source and should not be reconstructed from these public derivatives.
