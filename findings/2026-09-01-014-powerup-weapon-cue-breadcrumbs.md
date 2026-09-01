# FINDING-2026-09-01-014: TDM exercises weapon-pickup, power-up Gameplay Cue and weapon-effect paths with identifiable runtime breadcrumbs

Status: observed
Confidence: medium
First observed: 2026-09-01
Session: 2026-09-01-001

## Observation
During the TDM the log references `BP_WeaponPickup_C` actors, `POW_WallHack` Gameplay Cues and weapon-effect activity. It also reports failed posting of the audio event `play_sx_wpn_3p_merpow_prifle_projectile` because the associated AkComponent is invalid. The participant confirms pickups of Borealis and Orion and one Orion secondary-fire use, but the exact mapping between those actions and the logged audio identifier is not established.

## Evidence
- `archive/2026-09-01-001/snippets/match-and-gameplay-errors.txt`
- Participant-confirmed Borealis/Orion actions.

## Interpretation
The capture exposes concrete internal breadcrumbs for weapon pickup, power-up and weapon-effect subsystems during a real server-backed match. The `merpow_prifle` identifier should remain an unresolved asset breadcrumb until independently mapped.

## Alternatives
The audio event may belong to another power weapon, a bot, or an unrelated weapon-effect path occurring near the same time.

## Next test
Repeat one deliberately isolated power-weapon pickup/fire sequence with a video timestamp and compare the surrounding Gameplay Cue, weapon and audio logs.
