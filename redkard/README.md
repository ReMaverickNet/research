# RedKard / MerlinAntiCheat research

SPLITGATE: Arena Reloaded officially describes RedKard as 1047 Games' kernel-level anti-cheat and states that it runs when the game is launched and closes when the game closes. citehttps://support.splitgate.com/hc/en-us/articles/32048091883031-SPLITGATE-Arena-Reloaded-FAQ

Public SteamDB file inventories show an `1047/MerlinAntiCheat` integration containing RedKard bootstrap components, including an anti-cheat executable bootstrap, client DLL bootstrap and `redkard.sys.bootstrap`, alongside `static-vault.bin`. citehttps://steamdb.info/depot/2918301/subs/

Publicly posted support logs also expose parts of the launcher lifecycle, including a `C:\ProgramData\RedKard` runtime path and the game's `MerlinAntiCheat/ThirdParty/equ8_client` integration. These are useful observations, not proof of the complete internal architecture. citehttps://app.betahub.io/projects/pr-2055671118/issues/908/log_files/14515

EQU8's public documentation describes a client component directory and a server-side session manager, which is relevant when interpreting the `equ8_client` naming in Arena Reloaded. It does **not** by itself establish exactly how 1047 modified or wrapped EQU8. citehttps://equ8.gitbook.io/documentation/integration-guide/client-side-configuration

## Research questions

- What starts first: launcher, RedKard agent, driver, game?
- Which files are shipped with the game and which are provisioned into `ProgramData`?
- What configuration is read at startup?
- What process and service lifetime is observable?
- What local IPC exists between launcher, anti-cheat components and the game?
- What network activity belongs to anti-cheat rather than game services?
- How does this differ under Proton?
- Which parts are 1047-specific and which appear inherited from EQU8?

## Safe methodology

Allowed research includes:

- File inventory and hashes
- Process-tree observation
- Service/driver inventory
- Startup/shutdown timing
- Strings and metadata analysis
- Controlled packet capture
- Comparing historical builds
- Compatibility testing on supported systems
- Documenting publicly observable configuration and error messages

Do **not** publish or develop instructions for disabling the driver, evading detection, modifying anti-cheat checks, hiding processes, patching integrity checks, or cheating in online play.

## First-pass capture targets

```text
launcher start
  -> anti-cheat setup
  -> game launch
  -> game initialisation
  -> login
  -> lobby
  -> match
  -> match exit
  -> game exit
  -> anti-cheat shutdown
```

Capture timestamps and process state at each stage. The objective is to map the lifecycle, not defeat it.
