# Repository alignment review — 2026-09-01-001

The current repository was inspected before packaging. Its top level contains `archive/`, `builds/`, `captures/`, `docs/`, `findings/`, `logs/`, `networking/`, `redkard/`, `reverse-engineering/`, `sessions/`, and `tooling/`. Findings are currently stored directly under `findings/` alongside placeholder status directories; session records are under `sessions/linux/`. This bundle follows those live filesystem conventions.

Existing finding IDs at review time ended at `2026-09-01-007`. The new finding series therefore starts at `008`.

The AI guidance requires separating direct observations from inferences, preserving exact evidence references, avoiding unnecessary private IPs/identifiers, and recording AI usage. The final package follows those constraints. It also keeps the raw PCAP and original large Steam/Wine trace out of the repository-facing set.

Updated rather than duplicated:
- `2026-08-31-002-redkard-proton.md`
- `2026-08-31-003-loadout-assets.md`

New:
- `2026-09-01-008` through `2026-09-01-015`

Not added:
- separate locker-badge finding
- separate broad TDM-baseline finding
- separate MVP-flow finding
- P2P finding
