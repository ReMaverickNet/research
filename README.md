<h1 align="center">
  <img src="https://raw.githubusercontent.com/ReMaverickNet/.github/main/assets/remaverick-icon.svg" alt="ReMaverick icon" width="72" height="72" valign="middle">
  ReMaverick Research
</h1>

This repository contains the technical research, evidence, observations, and tooling behind **ReMaverick**.

## Start here

The project is intentionally **evidence-first**. The central documents explain what we currently know; the deeper folders contain the evidence and source material behind those conclusions.

- [Network architecture](NETWORK.md) — central launch → auth → matchmaking → allocation → game → results map
- [Build tracks](BUILD_TRACKS.md) — keeps current SGAR research separate from June 6, 2025 SG2 archaeology
- [Research roadmap](docs/roadmap.md) — current investigation priorities
- [Centralisation direction](docs/centralisation.md) — proposed ReMaverick control-plane architecture
- [Repository navigation](docs/navigation.md) — where to find evidence, sessions, captures and tooling

## Want to help?

You do not need to know reverse engineering, networking, or any other technical wizardry to contribute.

The easiest way to help is to play **SPLITGATE: Arena Reloaded**, pretty much:

If you are comfortable collecting logs or network captures, that's how you can help. The [Windows capture guide](docs/capture/windows.md) and [Linux / Proton capture guide](docs/capture/linux.md) walk you through it step by step, though feel free to reach out to **_xdan** on discord if you need any help.

**Please do not send passwords, authentication tokens, private messages, or other personal information.** When in doubt, send us (or an AI, though document its usage) the observation first and we can help work out what is useful to preserve.

You can contribute by opening an issue, submitting a pull request, or sharing the relevant files and session details with the project maintainers.

## How to contribute

The easiest way to contribute is through **GitHub Issues**. You do not need to know Git or make a pull request.

1. Run a test using one of the [capture guides](docs/capture/).
2. Keep the files from that session.
3. Open the **Issues** tab and create a new issue.
4. Describe what you did and what happened.
5. Attach your logs or other relevant files to the issue by dragging them into the message box.

A useful submission can be very simple:

> **What I did:** Started the game, joined a party, played one matchmaking game and left normally.
> **What happened:** Everything worked normally.
> **Platform:** Windows
> **Approx. time:** 29 August 2026, around 20:00 UTC

Please **do not upload passwords, authentication tokens, private messages, personal information, or proprietary game files**.

### Comfortable with Git?

You're also welcome to contribute directly with a **pull request**. This is useful for adding cleaned logs, session records, findings, documentation, analysis tools, or other structured research.

If you're unsure which route to use, **just open an Issue**. We'd rather receive useful evidence in an Issue than lose it because contributing seemed complicated.

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
NETWORK.md      Central network / lifecycle architecture map
BUILD_TRACKS.md Current SGAR vs historical SG2 build boundary
sessions/       Reproducible experiments and their metadata
logs/           Redacted game / launcher / anti-cheat / network logs
captures/       Packet and ETW captures
findings/       Small, evidence-backed technical findings
builds/         Build, depot and manifest metadata
redkard/        Anti-cheat architecture and compatibility observations
docs/           Guides, methodology, roadmap and architecture notes
tooling/        Small analysis scripts and helper tools
networking/     Network-specific evidence and protocol notes
reverse-engineering/ Static-analysis and binary research
archive/        Preserved analysed session bundles
```

Each major area has a local `README.md` where navigation or handling rules are useful. The long-term plan is to move the human-facing architecture/reference material into a wiki once the dataset is mature, while keeping this repository as the evidence and source-of-truth archive.

## Core documents

- [Network architecture](NETWORK.md)
- [Build tracks](BUILD_TRACKS.md)
- [Roadmap](docs/roadmap.md)
- [Centralisation direction](docs/centralisation.md)
- [Repository navigation](docs/navigation.md)
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

Evidence comes first, so keep facts, observations, interpretations, and hypotheses clearly separated please.

Do not redistribute any proprietary game files. Store hashes and metadata instead.

AI use is welcome, but AI-generated claims are hypotheses until independently verified. Record AI involvement so future researchers can reproduce or challenge the analysis.

## Contact & legal

ReMaverick is an independent community research and preservation project and is not affiliated with, endorsed by, or operated by 1047 Games, Inc.

**SPLITGATE** and related names, logos, and other trademarks are the property of their respective owners, including 1047 Games, Inc.

For questions, corrections, takedown requests, legal concerns, or other matters relating to the project, contact **[maverick@xdan.me](mailto:maverick@xdan.me)**.

Please do not send passwords, authentication tokens, personal information, private communications, or proprietary game files.
