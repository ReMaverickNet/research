# ReMaverick Research

This repository contains the technical research, evidence, observations, and tooling behind **ReMaverick**.

## Why this exists

1047 Games has announced that SPLITGATE: Arena Reloaded will stop using dedicated servers and matchmaking on **September 3, 2026**, moving to peer-to-peer hosting with a server browser instead.

That gives us a finite window to capture how the production system works while the official infrastructure is still operating.

## Research priorities

1. Establish a reproducible baseline for the current live build.
2. Capture the full lifecycle of launch, login, lobby, matchmaking, server connection, gameplay, and disconnect.
3. Identify the services and protocols involved without relying on assumptions.
4. Catalogue historical builds and determine which versions remain obtainable.
5. Understand the transition to P2P and the post-shutdown server-browser behaviour.
6. Determine whether dedicated or community-hosted infrastructure is technically feasible.
7. Preserve the knowledge needed to maintain the project after official development ends.

## Repository map

```text
sessions/       Reproducible experiments and their metadata
logs/           Redacted game / launcher / anti-cheat / network logs
captures/       Packet and ETW captures
findings/       Small, evidence-backed technical findings
builds/         Build, depot and manifest metadata
redkard/        Anti-cheat architecture and compatibility observations
docs/           Guides, methodology and roadmap
tooling/        Small analysis scripts and helper tools
```

## Core documents

- [Roadmap](docs/roadmap.md)
- [Windows capture guide](docs/capture/windows.md)
- [Linux / Proton capture guide](docs/capture/linux.md)
- [Historical builds](docs/old-builds.md)
- [RedKard research](redkard/README.md)
- [AI disclosure](docs/ai-disclosure.md)
- [Evidence format](docs/evidence.md)
- [Data handling](docs/data-handling.md)

## Ground rules

Evidence comes first. Keep facts, observations, interpretations, and hypotheses clearly separated.

Do not redistribute proprietary game files. Store hashes and metadata instead.

AI use is welcome, but AI-generated claims are hypotheses until independently verified. Record AI involvement so future researchers can reproduce or challenge the analysis.
