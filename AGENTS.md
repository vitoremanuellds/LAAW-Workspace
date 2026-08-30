# AGENTS.md

## Agent Workflow
This project uses a structured, modular agent workflow — one process,
with optional layers rather than a profile choice:
- `.ai/info.md` exists → open and read in full — not "recall it
  exists," actually read it —
  [.ai/workflow/workflow.md](.ai/workflow/workflow.md).
- `.ai/info.md` doesn't exist → unbootstrapped. Run
  `.ai/workflow/skills/create-constitution/SKILL.md` (or
  `.ai/workflow/skills/bootstrap/SKILL.md` to set up several layers at
  once) to bootstrap it before doing anything else.

Do this before acting, every session — not just once, and not from
memory of a previous read. Gate-skip and scope-overstep bugs have
consistently traced back to this step being skipped.

`.ai/workflow/` here is a **plain copy**, not a git submodule —
deliberate for this repo (see `.ai/decisions/adr01-plain-copy-bootstrap.md`
once it exists). Don't reintroduce a submodule here without checking
that ADR first.
