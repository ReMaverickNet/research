# Proton log findings

> **Scope:** EMPULSE-specific analysis with SGAR comparison where noted.

The Proton log is primarily useful as a process/module/timing corroboration source rather than a second complete packet trace.

Relevant runtime components include Steam networking/transport support, Unreal online-subsystem modules, EOS socket support, DTLS and Oodle-related modules. These align with the components reported by Orion during EMPULSE startup.

The log does not expose a trustworthy plaintext allocator request or final gameplay endpoint. Where connection attempts are visible, they were only treated as high-value evidence after temporal correlation with PCAP and Orion.

This supports the repository's evidence-first rule: Proton/Wine module presence explains capability, but does not by itself establish which service performed a particular operation.
