# AGENTS.md

## Project Identity
LAAW-Workspace is a **mirror** of the LAAW repository. It serves as the
workspace for improving LAAW itself — think of it as LAAW being used to
guide the development of LAAW. Any changes made here are intended to
feed back into and improve the LAAW project itself.

## Agent Workflow
This project uses a structured, modular agent workflow — one process,
with optional layers rather than a profile choice:
- `.ai/info.md` exists → open and read in full — not "recall it
  exists," actually read it —
  [LAAW/workflow.md](LAAW/workflow.md).
- `.ai/info.md` doesn't exist → unbootstrapped. Run
  [.agents/skills/route/SKILL.md](.agents/skills/route/SKILL.md) to
  route to the correct bootstrap skill (`bootstrap` or
  `create-constitution`).

Do this before acting, every session — not just once, and not from
memory of a previous read. Gate-skip and scope-overstep bugs have
consistently traced back to this step being skipped.

`.ai/workflow/` here is a **plain copy**, not a git submodule —
deliberate for this repo (see `context/context.md` →
[c037-2384-96156-plain-copy-bootstrap](context/c037-2384-96156-plain-copy-bootstrap.md)).
Don't reintroduce a submodule here without checking that context item first.

## Git Discipline

**NEVER commit files that `.gitignore` excludes.** Before every commit,
run `git diff --cached` and verify no `.gitignore`d files appear in the
staged list. This is a hard rule — see
[LAAW/workflow.md §12](LAAW/workflow.md#12-commit-discipline)
for the detailed procedure.
