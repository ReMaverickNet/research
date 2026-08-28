# AI disclosure

AI assistance is encouraged because the project has a short preservation window and a large amount of material to process. It is a research accelerator, not an authority.

## Recommended starting point

Before using an AI model to analyse ReMaverick material, follow the [AI-assisted research guide](ai-assisted-research.md). It contains a copy-and-paste research prompt, recommended source material, sanitisation guidance, and a workflow for recording and verifying AI-assisted work.

The guide is intended to be useful to both humans and AI systems, so models can be given the document as context and use its structure directly.

## Record at minimum

- Tool/model used
- Date
- What the AI was asked to do
- Whether source material was provided to it
- Whether generated code was executed
- Which claims or transformations were independently checked

## Example

```yaml
ai:
  used: true
  tools:
    - name: ChatGPT
      task: Categorise 2,000 lines of PortalWars2.log by subsystem
      date: 2026-08-27
  verification:
    - Checked every identified endpoint against the raw log
    - Reproduced the connection sequence in a second capture
```

When an AI proposes a protocol interpretation, label it as a hypothesis until a packet trace, binary observation, or controlled experiment supports it.
