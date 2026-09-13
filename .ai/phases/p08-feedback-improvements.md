# Phase P08: Feedback Implementation Improvements

## Context

This phase implements improvements derived from practical feedback gathered
during active use of the LAAW workflow system. The feedback topics are
documented in [`.ai/workbench/feedback.md`](.ai/workbench/feedback.md).

Key areas of improvement:

- **ID generation format**: Current sequential IDs risk collisions when
  multiple teams work concurrently. A timestamp + random component
  provides safe concurrency.
- **Task folder organization**: The flat `tasks/` folder becomes crowded.
  Moving to phase-folders (with orphan tasks remaining flat) is a
  deliberate tradeoff.
- **Agent discipline around `.gitignore`**: Agents have been committing
  ignored files; the workflow needs to be more emphatic about respecting
  repository boundaries.
- **Task table creation**: The task table should be created automatically
  during phase definition, not deferred until the first task.

Relevant prior decisions: [ADR03](../decisions/adr03-single-modular-workflow.md)
(current workflow structure), [ADR02](../decisions/adr02-workbench-directory.md).

## In scope

- Redesign the ID generation scheme (phases, tasks, ADRs) with timestamp +
  random components for collision avoidance.
- Write a Python script to generate one or N ordered IDs.
- Restructure `tasks/` to use phase subdirectories; orphan tasks remain
  flat in `tasks/`.
- Strengthen `.gitignore` enforcement in the workflow documentation and
  agent instructions.
- Update the `define-phase` skill to always create the task table
  automatically.

## Out of scope

- Migration of existing task IDs to the new format (deferred — existing
  IDs remain valid; new phases use the new format).
- Restructuring existing phase files (only new phases adopt the new
  folder layout).
- Changes to the git history or rewriting of existing commits.

## Requirements

- **R01**: ID generation produces unique identifiers safe for concurrent
  multi-team use — no collisions even when two agents generate IDs at
  the same second.
- **R02**: The ID generation script returns only IDs (not names), accepting
  a count parameter, and outputs them in order.
- **R03**: New task files follow the `p{NN}/t{NN}-{name}.md` path under
  the phase folder; orphan tasks remain `t{NN}-{name}.md` under
  `tasks/`.
- **R04**: The workflow documentation explicitly instructs agents to
  respect `.gitignore` and never commit ignored files.
- **R05**: The `define-phase` skill always creates the task table
  (with header row) as part of phase file creation — no waiting for
  the first task.
- **R06**: All existing `.ai/` directory references in workflow docs
  update to reflect the new task folder structure.

## Plan

1. **Design the new ID format** — define the constant epoch, timestamp
   component (minutes elapsed), random component (4 digits), and full
   naming convention (`{p/t/d}{id}-{name}`).
2. **Implement the ID generation script** — Python script accepting N,
   returning ordered IDs only. Place it under `.ai/workflow/`.
3. **Update workflow.md** — reflect the new ID format in the directory
   structure (§3), ID conventions (§4), and any other references.
4. **Restructure tasks/ folder** — create phase subdirectories; move
   existing phase-linked tasks into their phase folders; orphan tasks
   remain flat. Update all path references.
5. **Strengthen `.gitignore` discipline** — add explicit agent
   instructions to the workflow and AGENTS.md about never committing
   ignored files; make the instruction emphatic.
6. **Update define-phase skill** — ensure the task table is always
   created automatically during phase definition.
7. **Update ADR03** — cross-reference the new ID scheme and folder
   structure as an evolution of the existing design.

## Automatic validations

- Run the ID generation script with N=10 and verify all IDs are unique
  and follow the `{minutes}{random}` format (4-digit random).
- Grep all `.ai/` markdown files for references to task paths and
  verify they use the new `p{NN}/t{NN}-{name}.md` format.
- Verify the `define-phase` skill file always includes the task table
  creation step in its procedure.
- Run `git diff --cached` after an agent session and confirm no
  `.gitignore`d files appear in the staged list.

## Manual validations

- Does the new ID scheme feel natural for concurrent multi-team use?
- Does the phase-folder structure for tasks improve navigability without
  losing the simplicity of flat orphan task files?
- Is the `.gitignore` instruction emphatic enough to prevent agent
  overreach?
- Is the task table creation change sufficient, or does it need
  additional guardrails?

## Tasks

| ID | Title | Purpose | Depends on | Status |
|---|---|---|---|---|
| | | | | |
