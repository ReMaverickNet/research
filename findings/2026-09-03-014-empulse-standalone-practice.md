# Finding: EMPULSE practice range is a standalone control case

> **Scope:** EMPULSE-specific observation.

**Date:** 3 September 2026  
**Confidence:** High  
**Session:** EMPULSE ranked/practice capture

## Observation

During the live Ranked attempt, the player entered the Plaza practice range and performed weapon, grapple and mech actions. Orion reports the resulting world as `NetMode = Standalone`, with `IsServer=0` and `IsDedicatedServer=0`.

The capture does not show a new dedicated gameplay endpoint appearing around dummy deaths or mech interactions. The Maverick control-plane connections were already established before the practice range was entered.

## Interpretation

The combat actions in this experiment are therefore best treated as local/standalone gameplay rather than evidence of an external authoritative gameplay session.

This is a useful negative control: visible gameplay events in Orion do not, by themselves, imply dedicated-server replication traffic.

## Why it matters

Future packet experiments can use the practice range as a baseline when distinguishing control-plane telemetry/background traffic from authoritative Unreal gameplay. Any new external endpoint coincident with an action should be treated as additional evidence, not assumed to be gameplay traffic automatically.
