# ReMaverick Research

This repository contains the technical research, evidence, observations, and tooling behind **ReMaverick**.

## Want to help?

You do not need to know reverse engineering, networking, or any other technical wizardry to contribute.

The easiest way to help is to play **SPLITGATE: Arena Reloaded**, pretty much:

If you are comfortable collecting logs or network captures, that's how you can help. The [Windows capture guide](docs/capture/windows.md) and [Linux / Proton capture guide](docs/capture/linux.md) walk you through it step by step, though feel free to reach out to **\_xdan** on discord if you need any help.

**Please do not send passwords, authentication tokens, private messages, or other personal information.** When in doubt, send us (or an AI, though document its usage) the observation first and we can help work out what is useful to preserve.

You can contribute by opening an issue, submitting a pull request, or sharing the relevant files and session details with the project maintainers.

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
- [AI-assisted research guide](docs/ai-assisted-research.md)
- [AI disclosure](docs/ai-disclosure.md)
- [Evidence format](docs/evidence.md)
- [Data handling](docs/data-handling.md)

## AI-assisted research

AI assistance is **strongly encouraged** during this project. The preservation window is short and the amount of material we need to process is large, so tools such as ChatGPT, Claude, and other capable models can be extremely useful for log triage, packet-analysis assistance, pattern finding, documentation, scripting, and forming hypotheses.

The [AI-assisted research guide](docs/ai-assisted-research.md) contains a copy-and-paste prompt, recommended inputs, privacy and sanitisation guidance, and the expected workflow for using AI against ReMaverick research material.

The guide should be used as the default starting point for AI-assisted analysis. AI-generated interpretations are **not evidence by themselves**: claims should be checked against raw captures, logs, binaries, controlled experiments, or another independent source before being recorded as findings.

## Ground rules

Evidence comes first. Keep facts, observations, interpretations, and hypotheses clearly separated.

Do not redistribute proprietary game files. Store hashes and metadata instead.

AI use is welcome, but AI-generated claims are hypotheses until independently verified. Record AI involvement so future researchers can reproduce or challenge the analysis.
