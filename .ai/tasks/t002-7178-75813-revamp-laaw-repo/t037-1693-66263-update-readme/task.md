# Update README

**ID:** t037-1693-66263       **Status:** done



<!-- TOC -->
<details><summary>Table of Contents</summary>

  - [Description](#description)
  - [TL;DR](#tldr)
  - [Context](#context)
    - [Before](#before)
    - [After](#after)
  - [In scope](#in-scope)
  - [Out of scope](#out-of-scope)
  - [Steps](#steps)
  - [Validations](#validations)

</details>


## Description

Rewrite `LAAW/README.md` to the new design: one context layer (merged),
tasks-with-subtasks instead of phases, two gates, the router skill,
the new id format, and the cross-platform Python sync scripts. The old
README documents the three-layer model (constitution, context,
decisions), five gates, phase-linked tasks, the base-36 id format,
bash sync scripts, and "call the skill explicitly" best practices —
all of which are replaced.

## TL;DR

- Full README rewrite to the new model.
- One context layer, tasks+subtasks, two gates, router skill.
- Cross-platform Python sync scripts (no bash).
- Remove "call the skill explicitly" best practice.
- Update directory structure, bootstrap instructions, and repo layout.

## Context

### Before

- Parent task [t002-7178-75813](../task.md) — the LAAW revamp.
  Depends on t037-1693-16386 (workflow.md rewrite, done).
- Current README (13301 bytes) covers:
  - Three-layer model (constitution, context, decisions folders).
  - Five gates (constitution-review, phase-review, task-review,
    task-completion-review, phase-completion-review, context-update).
  - Phase-linked tasks (`p{NN}-t{NN}-{name}.md`) and orphan tasks.
  - Base-36 8-char id format.
  - Bash sync scripts (`sync-workflow.sh`, `sync-skills.sh`).
  - "Call the skill explicitly" best practice (contradicted by the
    router skill).
  - Old directory structure with six optional layers.
  - `delegated` mode.
- The revamp design collapses to one context layer, two gates,
  tasks-with-subtasks, and the router skill.

### After

<!-- Filled in by implement-task after implementation -->

## In scope

- **`LAAW/README.md`** — full rewrite:
  - **Title/Intro**: "LAAW — Local AI Agents Workflow" — keep the
    title and problem statement (hallucination, wasted context, loss
    of control, unsafe parallel work), update the solution description
    for the new model.
  - **How it works**: Keep "persist knowledge, not reasoning" and
    "separate what from who decides" — update the workflow description
    to the two-gate lifecycle.
  - **One workflow, no profiles**: Remove the "three axes" section
    (presence/granularity/locality with medium/lite/minimal/full
    profiles). Replace with: one workflow, optional layers inferred
    from existence.
  - **Directory structure**: New structure:
    ```
    .ai/
    ├── workflow/              ← this repo's content
    │   ├── workflow.md
    │   ├── skills/            ← one SKILL.md per operation
    │   │   ├── route/         ← router
    │   │   ├── bootstrap/
    │   │   ├── create-constitution/
    │   │   ├── define-task/
    │   │   ├── implement-task/
    │   │   ├── validate-work/
    │   │   ├── review-work/
    │   │   ├── build-context/
    │   │   └── propagate-context/
    │   ├── reference/
    │   ├── templates/
    │   └── tools/             ← generate-id.py, sync-workflow.py,
    │                           ← sync-skills.py, .epoch
    ├── info.md                ← Policy only
    ├── context/               ← optional: context.md + c-{ID}.md
    ├── tasks/                 ← mandatory: tasks.md + t{ID}.md
    └── workbench/             ← optional: scratch space
    ```
  - **Lifecycle & gates**: New two-gate table:
    | Gate | Runs after | Unlocks |
    |---|---|---|
    | `task-review` | task-batch draft | implementation |
    | `task-completion-review` | implementation (mech., then judgment) | task complete |
    Three modes: `manual`, `assisted` (default), `autonomous`. No
    `delegated` mode.
  - **Router skill**: Add a section explaining the router — users
    state what they want in plain terms; the router points to the
    correct skill. No need to name skills explicitly.
  - **Bootstrap section**: Update to the new sync scripts (Python,
    cross-platform). Update the AGENTS.md snippet (no changes needed
    — it already references the correct paths).
  - **Updating the workflow**: Update to `sync-workflow.py` /
    `sync-skills.py` (Python, `tools/` directory).
  - **Best practices**: Remove "Call the skill explicitly" (router
    replaces this). Keep the rest, update for the new model.
  - **What's in this repo**: Update file listing to the new layout
    (skills, templates, tools, reference, workflow.md, README.md).

## Out of scope

- Changes to `workflow.md` — already done by t037-1693-16386.
- Changes to skill files — covered by steps 3–5.
- Changes to reference docs — covered by step 6.
- Changes to templates — covered by step 7.
- Changes to sync scripts — covered by step 9.

## Steps

1. Write the new README structure with all sections.
2. **Title/Intro**: Keep title, update problem/solution for the new
   model (one context, two gates, tasks+subtasks, router).
3. **How it works**: Keep the two core ideas, update workflow
   description to the two-gate lifecycle.
4. **One workflow, no profiles**: Remove three-axes section; replace
   with "one workflow, optional layers inferred from existence."
5. **Directory structure**: New structure with `tools/` (Python scripts
   + `.epoch`), one context folder, tasks-with-subtasks.
6. **Lifecycle & gates**: Two-gate table, three modes (manual,
   assisted, autonomous).
7. **Router skill**: New section explaining the router.
8. **Bootstrap into a project**: Update to Python sync scripts.
9. **Updating the workflow**: Update to `sync-workflow.py` /
   `sync-skills.py` in `tools/`.
10. **Best practices**: Remove "call the skill explicitly"; keep the
    rest, update for the new model.
11. **What's in this repo**: Update file listing.
12. Verify no stale references to phases, constitution folder,
    decisions folder, base-36 ids, bash scripts, or delegated mode.

## Validations

- README is a complete rewrite (not a patch) — every section reflects
  the new model.
- No phase language, no constitution folder, no decisions folder.
- Two gates, three modes (no `delegated`).
- Router skill mentioned in bootstrap and best practices.
- Sync scripts are Python (`sync-workflow.py`, `sync-skills.py` in
  `tools/`), not bash.
- Directory structure matches the new layout.
- Grep for `phase` (as a layer), `constitution` (as a folder),
  `decisions`, `delegated`, `sync-workflow.sh`, `sync-skills.sh`,
  `base-36`, `call the skill explicitly` — all gone or explained.
- File listing in "What's in this repo" matches the actual `LAAW/`
  layout after all steps complete.
