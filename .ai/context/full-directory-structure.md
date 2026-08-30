# LAAW's `.ai/` directory structure

Snapshot of `LAAW/workflow.md` §3's
directory-structure block, current as of P06 (the ADR03 redesign) and
this workspace's own re-bootstrap from it (2026-08-30). Kept here so
future phases touching `workflow.md`'s structural sections don't have
to re-read the whole submodule just to know what's already there —
re-verify against the actual file if it's been a while, this is a
snapshot, not the source of truth.

```
.ai/workflow/       submodule, never written to — workflow.md, reference/, templates/, skills/
.ai/info.md         Policy only — gate authority; always present, not an optional layer
.ai/constitution/   mission.md, techstack.md — optional
.ai/context/        context.md + whatever fits — optional
.ai/decisions/      decisions.md + adr{NN}-{name}.md — optional
.ai/phases/         phases.md (index) + p{NN}-{name}.md, own Context + task table — optional
.ai/tasks/          tasks.md (orphan index) + p{NN}-t{NN}-{name}.md (phase-linked) + t{NN}-{name}.md (orphan) — the one mandatory layer
.ai/workbench/      freeform scratch — planning notes, Q&A, prompt drafts; disposable, not part of the permanent record — optional
```

Presence is inferred from existence — no directory means that layer is
off; `.ai/tasks/` is the only one every project has. How a layer comes
into existence on first use: see `LAAW/reference/scaffold-on-first-use.md`,
or run the `bootstrap` skill to set up several at once.

`info.md` no longer holds a Status section — every status value lives
in `phases.md` (phase-level), a phase file's own task table
(phase-linked task), or `tasks.md` (orphan task). See
[ADR03](../decisions/adr03-single-modular-workflow.md).

`.ai/workbench/` is P03's addition (see
[ADR02](../decisions/adr02-workbench-directory.md), partially
superseded by ADR03's gitignore-locality clause — this workspace's own
`.ai/workbench/` is gitignored, not committed). `build-context`'s
ephemeral outputs (`context.temp.md`, `build-plan.md`) live there, and
get deleted automatically once `build-context.iterate`'s read queue
empties.

New projects get `.ai/workbench/README.md` automatically on first use
via whichever skill writes into it first (today, `build-context`) —
see `scaffold-on-first-use.md`. This repo's own `.ai/workbench/` was
instantiated by hand (2026-08-29), before that convention existed in
its current form.

`.ai/workflow/` here doesn't auto-track `LAAW/` — there's no `git
submodule update --remote` equivalent yet (that's P02's job). This
workspace's own `.ai/workflow/` was manually re-bootstrapped (`cp -r`
from `LAAW/`, `.git` stripped, 2026-08-30) to pick up the full P06
redesign — this repo's own `.ai/constitution/roadmap.md` also moved to
`.ai/phases/phases.md` and `info.md`'s Status section was dropped in
the same pass, matching what `LAAW/workflow.md` now documents. Until
P02 automates this, re-check `.ai/workflow/` for drift after any phase
that changes `LAAW/`'s content.

**Reminder for future phases in this project:** every edit to LAAW's
actual content happens in `LAAW/`'s own checkout, committed to *its
own* git history — never this repo's `.ai/workflow/` copy above, which
is read-only here. See `mission.md`'s Boundaries.
