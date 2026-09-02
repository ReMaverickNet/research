# Finding: Maverick shared backend and P2P transition

**Date:** 2 September 2026  
**Source:** Informal VC discussion with Ian (developer, first-party source)  
**Status:** First-party statements recorded from memory; no recording or transcript exists.

## Summary

An informal discussion with Ian shortly before the planned 3 September 2026 P2P transition provided several first-party clarifications about Maverick, Arena Royale, the removal of the faction system, RedKard, reverse-engineering activity, and the possibility of a future dedicated-server executable.

## Maverick

Ian stated that **Maverick is the backend for both Splitgate: Arena Reloaded and EMPULSE**. The backend is shared rather than being a separate implementation for each title, and it is capable of dynamically serving either game.

Ian explained that EMPULSE was built from SGAR with additions and removals, which accounts for the substantial backend compatibility between the two games.

Ian also said that the team had considered releasing Maverick as a service, and spoke positively about its optimisation.

### Research implications

- Shared Maverick infrastructure helps explain why SGAR and EMPULSE expose closely related backend behaviour.
- The ability to serve either game suggests that at least part of the backend was designed around game-specific content/configuration rather than being intrinsically tied to a single title.
- Whether clients from the two games can actually interoperate with the wrong game-specific service remains **unknown**.

## P2P transition

The P2P implementation is **not yet live as of this finding** and is expected to arrive on **3 September 2026**. Ian said that getting the P2P implementation working well required substantial work.

Ian stated that **Arena Royale will move to P2P**, while the old 64-player battle royale will not. The stated reason is that hosting the 64-player mode through P2P would place excessive demands on the host machine.

Implementation details of the P2P system were not discussed and should be treated as open research questions until the transition is live.

## Factions and equipment

Ian stated that the old faction system is gone, including its faction-specific equipment and abilities. There are no indications from this discussion that those systems remain available in the relaunched game.

Separately, the relaunch reduced the ordinary equipment pool because the developers considered the previous pool too large. This should not be conflated with the removal of the faction system.

The old 64-player BR cannot currently be played following the relaunch.

## RedKard

Ian stated that **RedKard is disabled when P2P is used**.

It is currently unknown whether RedKard files/components are removed from the shipped build, remain present but dormant, or are otherwise bypassed. This should be verified against the post-transition build.

## Reverse engineering / enforcement stance

Ian did **not** give formal approval for reverse engineering. His stated position was effectively that he does not condone it, but that he would not take action against the project's current activity for the time being, with no promise regarding future action.

Quoted from the subsequent Discord discussion, as remembered immediately after the VC:

> "i dont condone reverse engineering but i will not do anything just yet, though no promises"

This should therefore be treated as a **developer enforcement stance, not permission or a licence**.

Ian also appeared receptive to the preservation/community-server concept and indicated that he liked the idea of a dedicated-server executable, although he did not commit to producing one or specify its architecture or the amount of work required.

## Dedicated server

The terminology used in the conversation was **dedicated server executable**. The term "headless" was introduced by the community afterward and was not Ian's wording.

No implementation details were confirmed. It is possible that a future dedicated-server executable could use Maverick or a related backend component, but this is an open question rather than an established fact.

A dedicated server implementation would be particularly significant for preservation because it could potentially provide a foundation for community-hosted matches, custom events and historical-version support. These are research goals, not confirmed capabilities.

## Local movie assets

Ian was surprised to learn that the game ships with `.bk2` movie files in its local files and joked that they represented a bit of wasted space.

This is consistent with the project's existing file investigation showing that the relevant cinematics/trailers are locally bundled rather than necessarily streamed on demand.

## Open questions for post-transition research

- Does P2P use the same or a reduced subset of Maverick services?
- Which Maverick services remain reachable once dedicated hosting is gone?
- Is RedKard still present on disk after the P2P transition, and if so, is it dormant?
- Can the SGAR and EMPULSE clients reach the same Maverick service endpoints interchangeably?
- Which old faction, equipment and BR assets remain in shipped files despite being inaccessible in-game?
- What form would a future dedicated-server executable take, and what parts of Maverick would it depend on?

## Evidence quality

**High confidence:** Statements explicitly attributed to Ian during the VC.  
**Medium confidence:** Details recalled immediately afterward without a recording/transcript.  
**Not established:** Any architectural conclusions or future dedicated-server capabilities not explicitly stated by Ian.
