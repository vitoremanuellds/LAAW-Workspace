# Rewrite `workflow.md`

**ID:** t037-1693-16386       **Status:** validating

## Description

Full rewrite of LAAW's `workflow.md` to the two-gate, no-phase,
single-context process. Replaces the current five-gate lifecycle
(constitution → phase → task → …) with the streamlined model: one
mandatory `tasks/` layer, one `context/` folder (merged from
constitution + context + decisions), tasks with optional subtasks, and
exactly two gates (`task-review`, `task-completion-review`).

## TL;DR

Rewrite `LAAW/workflow.md` (~270 lines → ~200 lines) — drop all phase
language, constitution-review, context-update gate, orphan-task
concept; install the recursive task folder rule, the new status list,
decisions-as-context-rows, and the router skill in the operation table.

## Context

### Before

Current `workflow.md` (LAAW `main`, commit `e9e4485`):
- **§3 Directory structure:** `constitution/`, `context/`,
  `decisions/`, `phases/`, `tasks/` — five optional layers + tasks
  mandatory.
- **§4 Artifact hierarchy:** `Constitution → Context → Decisions →
  Phases → Tasks` — five levels of lateral linking.
- **§5 Lifecycle & gates:** five gates (constitution-review,
  phase-review, task-review, task-completion-review,
  phase-completion-review) plus context-update; modes table with
  four columns.
- **§6 Deviations:** task-level, phase-level, project-level —
  three-tier escalation.
- **§7 Decisions (ADRs):** standalone `decisions/` index + `adr{NN}`
  files; owner-based writing (create-constitution, define-phase,
  implement-task).
- **§9 Context propagation:** task → phase file's Context → context/
  (two-hop routing).
- **§11 Status:** five states (`not-planned → awaiting-plan-review →
  in-progress → reviewing → complete`) + `blocked`.

### After

*(filled in at completion — what implementation established that
wasn't obvious before, candidate for promotion to context/)*

## In scope

- `LAAW/workflow.md` — full rewrite.

## Out of scope

- Rewriting skills (step 3–5 of the parent task).
- Rewriting reference/ files (step 6).
- Rewriting templates/ (step 7).
- README rewrite (step 8).
- Sync scripts (step 9).
- Any change to `tools/generate-id.py` or `.epoch`.

## Files to modify

- `LAAW/workflow.md` — entire file rewritten.

## Files to create

None.

## Steps

1. **Rewrite §3 — Directory structure.** Replace the current five-layer
   structure with:
   - `.ai/workflow/` — same (read-only, synced wholesale).
   - `.ai/info.md` — policy only (unchanged).
   - `.ai/context/` — THE one context layer (merged):
     - `context.md` — mission + techstack core inline + index table.
     - `c-{ID}-{name}.md` — individual context items (decisions,
       architecture, invariants).
     - `index-*.md` — optional sub-indexes when the index table would
       grow too big (exempt from ids).
   - `.ai/tasks/` — mandatory:
     - `tasks.md` — root index: one row per top-level task.
     - `t{ID}-{name}.md` — a task with NO subtasks (a leaf).
     - `t{ID}-{name}/` — a task WITH subtasks (a folder):
       - `t{ID}-{name}.md` — the parent task (same stem as folder).
       - Subtask files — each its own `t{ID}-{name}.md`.
   - `.ai/workbench/` — freeform scratch (unchanged).
   - Explain **presence rules collapse**: `tasks/` mandatory; `context/`
     effectively mandatory (one small file suffices); `workbench/`
     optional. No five-axis matrix.
   - Explain the **recursive task folder rule** (same rule applies at
     every nesting level: leaf = file, has-subtasks = folder).
   - Note index/workbench exemption from ids (why).

2. **Rewrite §4 — Artifact hierarchy & context rule.** Replace with:
   ```
   Context → Tasks (own Context)
   ```
   - One optional layer (context) feeding into the mandatory tasks
     layer.
   - No constitution, no decisions, no phases — all context is in
     `context/`.
   - A task can have subtasks (itself a folder) or be a leaf.

3. **Rewrite §5 — Lifecycle & gates.** Replace the five-gate lifecycle
   with the two-gate model:
   ```
   Tasks → Task Plan Review → Implement
     → Task Completion Review (validate, then review)
     → Context Evaluation → Task Complete → (repeat)
   ```
   - **Gates table** (two rows):
     | Gate | Runs after | Unlocks |
     |---|---|---|
     | `task-review` | task-batch draft | implementation |
     | `task-completion-review` | implementation (mech., then judgment) | task complete |
   - Gates block *advancing past* a draft, never *producing* one.
     **Unlocking ≠ starting** — `manual`/`assisted` stops and asks
     before the next step; `delegated`/`autonomous` chains through.
   - **Modes table** (three rows, same columns):
     | Mode | Plan-review | Compl.: mech. | Compl.: judgment |
     |---|---|---|---|
     | `manual` | human | human | human |
     | `assisted` (default) | human | agent | human |
     | `autonomous` | agent | agent | agent |
     (`delegated` removed — no longer needed with two gates; if used,
     defaults to `human` for all).
   - **Task complete:** implementation + `task-completion-review`
     (both checks) + context evaluated.
   - Remove all phase-level gates (phase-review,
     phase-completion-review), constitution-review, context-update.
   - Keep the "starting without every phase planned is normal" note
     — rephrase as "starting without every task planned is normal"
     and link to the updated reference.

4. **Rewrite §6 — Deviations.** Replace three-tier escalation with:
   - Deviation = work materially differs from the approved plan; a
     mismatch against a plan detail marked flexible isn't one.
   - Recorded inline as a `## Deviations` subsection in the task file.
   - Lifecycle `OPEN → ADDRESSED → INCORPORATED`, deleted once the
     fact lives in the plan, implementation, or a context decision row.
   - **Task-level** → back to the implementation loop.
   - **Project-level** → replanned via `create-constitution`, always
     a context decision row.
   - **No phase-level** — phases don't exist anymore.
   - Note: deviations create **context decision rows** (`c-{ID}`),
     not standalone ADR files (see §7 below).
   - Pseudocode is guidance, not contract — deviating from it isn't
     itself a deviation; only the underlying *approach* being wrong
     is.

5. **Rewrite §7 — Decisions.** Replace the ADR section with:
   - Decisions are **context rows** (`c-{ID}-{name}.md`), not standalone
     files.
   - Every decision has: id, name, relation, superseded-by columns
     (same shape as the `context.md` index).
   - **Owner writes it, at the moment of the decision:**
     - `create-constitution` — project-level.
     - `implement-task` — during implementation.
   - No other operation writes one — review flags a missing one back
     to the owning scope.
   - A superseding decision updates both rows' Relations, not a
     deletion — Git keeps history.
   - Remove all references to `decisions/` directory, `adr{NN}` files,
     and `decisions.md` index.

6. **Keep §8 — Validation vs Review.** This section is already
   correct for the two-gate model — no changes needed beyond
   renumbering (it becomes §8).

7. **Rewrite §9 — Context propagation.** Replace the two-hop routing
   (task → phase Context → context/) with the direct path:
   ```
   Task done  → matters beyond this task? → promote to context/
   ```
   - A task writes directly to `context/` (no phase-file routing).
   - Promotion happens at task completion (not phase completion).
   - **Propagate:** architecture facts, invariants, responsibilities,
     dependencies, constraints, domain knowledge.
   - **Never:** task history, temporary details, reasoning, progress
     reports, anything recorded elsewhere.
   - A fact belongs in the task file, or gets promoted to `context/`.
   - An ADR's (context decision's) relevance follows the same cadence
     — writing it doesn't wait.

8. **Keep §10 — Operation contracts.** No changes needed — renumber
   to §10.

9. **Rewrite §11 — Status.** Replace the five-state list with:
   ```
   not-started → planned → in-progress → done
   (blocked from any active state)
   ```
   - `planned` = draft exists, `task-review` gate pending/passed.
   - `in-progress` = approved, implementation underway.
   - `done` = implementation complete + `task-completion-review`
     passed.
   - No separate `awaiting-plan-review` / `reviewing` / `complete`
     states — the two gates are transitions, not states.
   - **One status per fact, one place:** task rows in `tasks.md`,
     subtask rows in the parent task file. `info.md` holds policy
     only.
   - **ID order ≠ execution order** — same reasoning as current.
   - Link to `reference/status-and-info.md` (updated in step 6 of
     the parent task).

10. **Rewrite §12 — Commit discipline.** Keep as-is (it's already
    correct). Renumber to §12.

11. **Update the operation table in §2.** Replace the current nine
    skills with the new set:
    | Operation | Skill |
    |---|---|
    | Route to correct operation | `route` |
    | Bootstrap several layers at once | `bootstrap` |
    | Constitution / context setup | `create-constitution` |
    | Task planning | `define-task` |
    | Implementation | `implement-task` |
    | Validation | `validate-work` |
    | Review | `review-work` |
    | Context — fill items | `build-context` |
    | Context — propagate/finalize | `propagate-context` |

    Changes from current:
    - **Added:** `route` (router skill — plain-language request →
      correct operation).
    - **Removed:** `define-phase` (no phases).
    - **Kept:** `bootstrap`, `create-constitution`, `define-task`,
      `implement-task`, `validate-work`, `review-work`,
      `propagate-context`, `build-context`.
    - Note: `bootstrap` now offers a simplified layer menu (no
      constitution/decisions/phases — just info.md, context, tasks,
      workbench).

12. **Add §13 — Teams (many developers).** New section (moved from
    the revamp design):
    - **The file-overlap rule is the coordination unit:** work on the
      same file set should not overlap across two `in-progress` tasks
      — the "touches these files" spec line makes conflicts visible
      before they happen.
    - **Parallelism comes from subtasks:** a task can be approved as
      a whole while subtasks are picked up by different people/agents.
    - **Git is the sync layer:** commit each draft/step; review
      happens via diff. No locks beyond file overlap.
    - **Context (Before/After) matters more in a team:** it is what
      the next person reads before touching the task — and where a
      deviation gets recorded if it isn't a full replan.
    - **No Owner field** — settled as a decision in
      [c037-1650-68133](../../context/c037-1650-68133-revamp-open-decisions.md).

13. **Add §14 — What each principle buys.** New summary table (moved
    from the revamp design):
    | Concern | Mechanism |
    |---|---|
    | Limited context window | small files + index `context.md` + links + "read only this file" rule; Context Before/After instead of session history |
    | Hallucination | narrow task specs (files, done-when, out-of-scope); ask-don't-invent rule |
    | Teams | file-overlap visibility, subtask parallelism, git diff review |
    | Not source of truth | task files are guidance; acceptance is checked against the code/behavior, not the doc |
    | Not PM tool | no roadmap, no progress metrics, no dependency graph — only what an agent needs to do its assigned task |
    | Compressed info | everything small by design; anything long gets split + linked |
    | Lazy reading | index files (`context.md`, `tasks.md`) hold only pointers + status |

14. **Update cross-references.** Ensure all internal links in the
    rewritten file point to the correct paths under the new structure:
    - `reference/status-and-info.md`
    - `reference/directory-and-links.md`
    - `reference/scaffold-on-first-use.md`
    - `reference/starting-without-a-plan.md`
    - `reference/reread-skill-discipline.md`

## Dependencies

- `t037-1693-02727` (new-id-system) — the id format must be settled
  before workflow.md can reference the new id shape.

## Expected result

A clean `workflow.md` that:
- Uses the new directory structure (context/, tasks/ only).
- Expresses the two-gate lifecycle (task-review, task-completion-review).
- Lists the new status set (not-started → planned → in-progress → done).
- References the router skill in the operation table.
- Has no mention of phases, constitution/, decisions/, orphan tasks,
  or the old five-gate model.
- Links to updated reference files (which this task does not create —
  they are updated in a later subtask).

## Automatic validations

- `grep -i 'phase' LAAW/workflow.md` returns **no results** (except
  possibly in the word "reshape" or similar — verify manually).
- `grep -i 'constitution' LAAW/workflow.md` returns **no results**
  (except in the skill name `create-constitution` and the phrase
  "constitution-review" should not appear as a gate).
- `grep -i 'constitution-review\|phase-review\|phase-completion-review\|context-update' LAAW/workflow.md` returns **zero matches**.
- `grep -i 'orphan' LAAW/workflow.md` returns **zero matches**.
- `grep -i 'adr\|decisions' LAAW/workflow.md` — returns matches only
  in the context of "context decision rows" or "c-{ID}" references,
  not as a standalone layer.
- `grep -c 'task-review' LAAW/workflow.md` returns **≥ 2** (the gate
  name should appear in the lifecycle diagram and the gates table).
- `grep -c 'task-completion-review' LAAW/workflow.md` returns **≥ 2**.
- `grep 'route' LAAW/workflow.md` returns **≥ 1** (router skill in
  the operation table).
- `grep -E 'not-started|planned|in-progress|done' LAAW/workflow.md`
  finds the new status list (not the old five-state list).
- `grep -i 'awaiting-plan-review\|reviewing\b' LAAW/workflow.md`
  returns **zero matches** (these old states must be gone).

## Manual validations

- A fresh agent reading only `workflow.md` + `context.md` of a
  freshly synced scratch project can say what's active, what its gate
  is, and what "done" means — without reading `skills/`.
- The two-gate lifecycle is expressible for the minimal case
  (one leaf task, no subtasks) with zero optional layers.
