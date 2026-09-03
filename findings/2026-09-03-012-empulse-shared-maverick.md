# Finding: EMPULSE uses the same Maverick service families as SGAR

> **Scope:** EMPULSE-specific observation/finding; cross-game claims are explicitly attributed to SGAR evidence or first-party confirmation.

**Date:** 3 September 2026  
**Status:** Observed network evidence; corroborates existing first-party statement  
**Confidence:** High  
**Session:** EMPULSE ranked/practice capture, 3 September 2026

## Observation

The EMPULSE ranked capture resolves and connects to the same production Maverick hostname families documented in the SGAR investigation: global AGA, Orion AGA, L4 AGA, server-status, content, client-IP, Merlin update and associated Maverick storage/CMS infrastructure.

The EMPULSE client therefore exposes the same broad production control-plane family rather than a separate backend deployment that merely happens to use similar terminology.

## Evidence

- `EmpulseRankedMM.pcapng`: DNS and TLS/SNI observations for the service families listed in `archive/2026-09-03-003-empulse-ranked-intake/service-inventory.csv`.
- `Orion.log`: explicit `Maverick::Api::GameCms::GetLocalizationManifestPublic` and `GetLocalizationManifestAuthorized` gRPC calls.
- `Orion.log`: `LogMerlin: Data Received: Endpoint: ReportServerSessionManager, Size: 370`.
- Existing ReMaverick finding `2026-09-02-011`, which records first-party developer confirmation that Maverick is shared by SGAR and EMPULSE.

## Interpretation

**Correlated:** EMPULSE independently corroborates the repository's first-party shared-backend statement at the live network level.

This is stronger than a static string match because the hostnames are actively resolved and contacted during a live production run.

## Alternatives

The service families could theoretically represent generic shared platform services rather than every game's complete backend. That alternative does not undermine the finding that EMPULSE uses the same Maverick production service namespace and API infrastructure.

## Why it matters

A compatibility implementation should model the client-visible control-plane contract rather than reproduce separate backend stacks per game. EMPULSE gives a second client that can be used to distinguish truly shared behaviour from game-specific extensions.
