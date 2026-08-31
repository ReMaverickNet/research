# FINDING-2026-08-31-003: Loadout attachment paths report invalid targets while weapons remain usable

Status: observed
Confidence: medium
First observed: 2026-08-31
Session: 2026-08-31-001

## Observation

The player used the AER SMG (Sprinter / Aeros SMG) and applied an extended barrel and recoil grip. The UE log repeatedly reports attachment and item-state errors around loadout changes, including:

- `AttachID_AER_SMG_ExtBarrel` - target component not found
- `AttachID_AER_SMG_RecoilGrip` - target component not found
- `AttachID_MER_BurstPistol_ImpactBullets` - no valid class or override
- `FillInvalidSlot failed to find a parent item in LoadoutSlot.Primary.Weapon.Generic`
- `FillInvalidSlot failed to find a parent item in LoadoutSlot.Skin.Generic`
- `SelectSlot: Failed to find quickbar slot 'None'` on Weapons, Equipment, Utilities and Gadgets

The Sprinter nevertheless remained usable during the test. The burst pistol was present but was not manually edited.

## Evidence

Session: `sessions/linux/2026-08-31-001.md`

Relevant raw-log period: approximately 21:03:29-21:03:39 UTC, during repeated loadout/weapon state changes.

## Interpretation

These messages establish that the loadout/attachment system attempted to resolve item components that were invalid or unavailable in the captured client state. They do not establish that the corresponding weapon was unusable. The successful use of the Sprinter means the errors may concern secondary presentation/attachment paths, stale item data, or intentionally missing backend-provided state.

The burst-pistol warning is particularly useful because the attachment was not edited by the player, indicating that some attachment state can be evaluated during ordinary item creation or loadout refresh.

## Alternatives

- Missing live-service data may leave partial inventory/attachment state.
- Repeated actor registration and recreation may cause stale component references.
- Some attachment definitions may intentionally lack a class or override in this build.
- The errors may be harmless fallback behaviour in this offline/limited-service state.

## Next test

Repeat the same Sprinter + attachment sequence in a server-backed arena match and capture the corresponding item-resolution logs. Compare against a fresh client with a different weapon/loadout to determine which errors are state-dependent.

## AI analysis

ChatGPT was used for initial log triage. Weapon identity and manual actions were supplied by the tester and should be treated as the authoritative observation for this session.
