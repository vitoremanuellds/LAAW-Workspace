# T03 — Explicit gate-skip for missing layers

## Context

LAAW's lifecycle diagram (§5 of `LAAW/README.md` and `.ai/workflow/workflow.md`)
shows a linear flow:

```
Constitution → Constitution Review → Phase → Phase Plan Review
  → Tasks → Task Plan Review → Implement
  → Task Completion Review → Context Evaluation → Task Complete
  → Phase Completion Review → Reconcile Phase/Project Context → Phase Complete
```

Every layer except `tasks/` is optional (`workflow.md` §3: "Presence is
inferred from existence — no directory means that layer is off"), and
the directory structure section notes which layers are optional.
But **nowhere does it explicitly state that gates for non-existent
layers are skipped**. The lifecycle diagram is a flat linear flow
with no conditional branching notation.

A reader (human or agent) has to infer that if `constitution/` doesn't
exist, `constitution-review` doesn't run — from the "optional"
designation and the "presence inferred from existence" statement. The
intent is clear, but the connection between "optional layers" and
"conditional gates" is never drawn explicitly.

This caused a real gap: when I reviewed the workflow, I had to infer
the gate-skipping behavior from two separate statements rather than
finding it written as a rule. The same gap exists in both
`LAAW/README.md` and `.ai/workflow/workflow.md`.

## Implementation

### Objective

Make it explicit in both `LAAW/README.md` and `workflow.md` that gates
for non-existent layers are skipped — so a reader never has to infer
it.

### In scope

- Add explicit gate-skip statement to `LAAW/README.md` §5 (Lifecycle &
  gates), right after the lifecycle diagram and before the gate table.
- Add the same explicit statement to `.ai/workflow/workflow.md` §5
  (Lifecycle & gates).
- No changes to `info.md`, skills, templates, or any other files.

### Out of scope

- Changing the lifecycle diagram itself (it's intentionally the full
  set of gates; conditional skipping is a reader instruction, not a
  diagram change).
- Adding gating logic to any skill or `info.md` — this is purely
  documentation.
- Any other README or workflow sections beyond §5.

### Files to modify

| File | Change |
|---|---|
| `LAAW/README.md` | Add a bullet/paragraph after the lifecycle diagram in §5 stating that gates for missing layers are skipped |
| `LAAW/workflow.md` §5 | Same addition, consistent wording |

### Steps

1. Read `LAAW/README.md` §5 (Lifecycle & gates) to find the right
   insertion point — immediately after the lifecycle diagram block,
   before the gate table.
2. Add an explicit statement such as:

   > **Gates for missing layers are skipped.** The lifecycle above
   > shows the full set — a project never walks through every gate;
   > it only encounters gates for layers that exist. If `constitution/`
   > doesn't exist, `constitution-review` doesn't run. If `phases/`
   > doesn't exist, `phase-review` and `phase-completion-review` don't
   > run. If `context/` doesn't exist, `context-update` and
   > `context-evaluation` don't run.

   (Wording is flexible — mark as `(flexible: exact wording)`.)

3. Read `LAAW/workflow.md` §5 to find the same insertion point
   — after the lifecycle diagram, before the gate table.
4. Add the same explicit statement with consistent wording.
5. Verify both additions are present and consistent.

### Automatic validations

- `grep -c "Gates for missing layers" LAAW/README.md` returns 1
- `grep -c "Gates for missing layers" LAAW/workflow.md` returns 1
- The statement appears in both files with consistent meaning

### Manual validations

- Confirm the added text sits between the lifecycle diagram and the
  gate table in both files.
- Confirm the wording is clear enough that a first-time reader would
  understand that missing layers mean their gates are skipped without
  having to infer it.
