# Highest-value next experiments

> **Scope:** EMPULSE-specific experimental recommendations informed by SGAR comparison.

## 1. Quick Play successful match — highest value

Capture a complete successful Quick Play match and bracket the exact moment of match assignment / `SERVER READY`. Correlate the preceding 5–10 seconds of NATS/4222 and TCP/60000 traffic with global/orion/server-status/Edgegap activity and the first authoritative UDP endpoint.

**Why:** this is the most likely route to identifying the missing matchmaking → allocation → endpoint boundary.

## 2. Custom Game

Capture creation, invitation/join and start of a Custom Game if another client is available. Compare control-plane messages and endpoint selection with Quick Play.

**Why:** it can help distinguish party/session management from public matchmaking.

## 3. Post-cutover P2P/server-browser capture

Immediately after the dedicated-service cutoff, capture the first available P2P/server-browser flow. Compare which Maverick services remain, which disappear, and whether the server browser uses direct public endpoint exchange.

**Why:** EMPULSE's shutdown transition is itself an architecture change and may reveal the minimum control plane required without official dedicated servers.
