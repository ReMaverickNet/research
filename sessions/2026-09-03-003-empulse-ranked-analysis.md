# Session: EMPULSE ranked/practice forensic analysis

**Date:** 3 September 2026  
**Scope:** EMPULSE capture, with explicit SGAR comparison  
**Status:** Derived analysis recorded after cross-checking raw supplied evidence and the public repository baseline.

## Experiment

EMPULSE was launched under Proton and Ranked matchmaking was started. While the queue remained active, the player entered the practice range, exercised weapons and mech interactions, cancelled/left matchmaking, continued running the application briefly, then stopped the first capture. A second capture covered the subsequent application shutdown. No successful Ranked match was obtained.

## Evidence supplied to the analysis

- Raw `EmpulseRankedMM.pcapng`.
- Raw `EmpulseCloseGame.pcapng`.
- Full `Orion.log`.
- Full Proton/Wine `steam-4323990.log`.
- Entire supplied EMPULSE LocalAppData snapshot.
- Current public ReMaverick research documentation and findings, including `NETWORK.md`, navigation/methodology material, the recent SGAR LocalAppData intake archive, and the first-party Maverick shared-backend finding.

## AI disclosure

- **Provider/product:** OpenAI ChatGPT.
- **Model:** GPT-5.6 Luna.
- **Analysis date:** 3 September 2026.
- **Files made available to the AI:** The raw EMPULSE archive and its extracted contents listed above, plus public repository documents.
- **Task:** Perform a deep comparative forensic analysis of EMPULSE against existing ReMaverick SGAR research, correlate PCAP/log/local-file evidence, separate observation from inference, identify new findings, and prepare repository-ready artefacts.
- **Code/tools used:** Local packet/log inspection and a reproducibility inventory script were executed against the supplied evidence. The generated script is included in `tooling/pcapng_inventory.py`.
- **AI contribution:** Evidence triage, cross-source correlation, candidate architectural interpretations, comparison against the existing research model, drafting of findings/documentation, sanitisation review, and packaging.
- **Independent verification:** Important packet-level claims were checked against raw packet bytes, DNS/TLS metadata, timestamped Orion entries and LocalAppData material. Repository claims were checked against the current public repository content and recent SGAR AppData intake structure.
- **Human-review requirement:** NATS/L4 observations are directly evidenced, but the semantic role of the NATS and TCP/60000 channels and the exact allocator/session-broker operation remain hypotheses/unknowns until a successful matchmaking capture correlates them with `SERVER READY` and the authoritative gameplay endpoint.

## Scope notes

- **EMPULSE:** all packet/log/local-file observations in this session.
- **SGAR:** prior architecture and gameplay evidence used as a comparison baseline.
- **SHARED:** the overlap of Maverick hostname/service families, supported by EMPULSE observation plus the existing first-party developer statement that Maverick serves both games.
- **CROSS-GAME INFERENCE:** comparison-based similarities that are not directly proven common.
- **UNKNOWN:** exact matchmaking ticket creation, allocator semantics, NATS subjects, TCP/60000 protocol semantics, and Edgegap's exact role in this unsuccessful Ranked attempt.
