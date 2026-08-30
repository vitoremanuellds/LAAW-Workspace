# `full`'s `.ai/` directory structure

Snapshot of `LAAW/workflow.md` §3's
directory-structure block, current as of P03. Kept here so P04/P05
(which also touch `workflow.md`'s structural sections) don't have to
re-read the whole submodule just to know what's already there —
re-verify against the actual file if it's been a while, this is a
snapshot, not the source of truth.

```
.ai/workflow/       submodule, never written to — workflow.md, reference/, templates/, skills/
.ai/info.md         Policy + Status, merged
.ai/constitution/   mission, techstack, roadmap
.ai/context/        context.md + whatever fits
.ai/decisions/      decisions.md + adr{NN}-{name}.md
.ai/phases/         p{NN}-{name}.md, own Context + task table
.ai/tasks/          p{NN}-t{NN}-{name}.md, flat
.ai/workbench/      freeform scratch — planning notes, Q&A, prompt drafts; disposable, not part of the permanent record
```

`.ai/workbench/` is P03's addition (see
[ADR02](../decisions/adr02-workbench-directory.md)): the one directory
in the block that isn't schema- or Status-tracked, and that no skill
reads as an input dependency. `build-context-full`'s two ephemeral
outputs (`context.temp.md`, `build-plan.md`) live there now, and get
deleted automatically once `build-context.iterate`'s read queue empties.

New projects get `.ai/workbench/README.md` automatically on first run
via `create-constitution-full` (a template copy, same pattern as
`info.md`/`context.md`/`decisions.md`). This repo's own `.ai/workbench/`
was instantiated by hand (2026-08-29) rather than through a fresh
`create-constitution-full` run — this repo already bootstrapped before
P03 existed.

`.ai/workflow/` here doesn't auto-track `LAAW/` —
there's no `git submodule update --remote` equivalent yet (that's
P02's job). After P03's changes landed in the submodule, `.ai/workflow/`
was manually re-synced (`rsync`, verified identical via `diff -rq`,
2026-08-29) to pick them up. Until P02 automates this, re-check
`.ai/workflow/` for drift after any phase that changes
`LAAW/`'s content.

**Reminder for future phases in this project:** every edit to `full`'s
actual content happens in `LAAW/`'s own
checkout, committed to *its own* git history — never this repo's
`.ai/workflow/` copy above, which is read-only here. See `mission.md`'s
Boundaries.
