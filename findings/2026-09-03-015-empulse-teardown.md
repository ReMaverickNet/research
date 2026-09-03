# Finding: EMPULSE L4/control connections persist until application shutdown

> **Scope:** EMPULSE-specific observation.

**Date:** 3 September 2026  
**Confidence:** High  
**Session:** EMPULSE ranked/practice capture + close-game capture

## Observation

The first PCAP ends while EMPULSE remains open. The second PCAP begins before the application exits and captures teardown of the L4 TCP/60000 connection alongside other Maverick/API connections.

Orion records engine shutdown at approximately 01:39:53.743Z, followed by NATS disconnection/close at approximately 01:39:54.575–01:39:54.576Z.

## Interpretation

The L4 control/session channels are persistent application-session resources rather than one-shot matchmaking requests. Their teardown is tied closely to game shutdown.

This does not identify their exact business role, but it strengthens the classification of L4 as stateful control/session infrastructure.

## Why it matters

A successful-match capture should preserve the entire lifespan of these channels and correlate their message bursts with queue creation, match assignment, server readiness and disconnect.
