# Task: P07-T02 — Change define-task default to single-task

## Context

See [p07-feedback-implementation-improvements](../phases/p07-feedback-implementation-improvements.md).

Currently, `define-task` drafts **all** tasks in scope by default.
The procedure says: "Steps 1–7 require no prior approval — draft
everything for this invocation before stopping for anything" and
"once every task in scope for this invocation is drafted, ask the
user whether there's more to add."

The feedback says the default should be **one task only**. Drafting
all tasks should require an explicit user request. This prevents
accidentally over-planning and gives the human more control over the
planning cadence.

### In scope

- `define-task`'s default behavior: draft one task per invocation.
- The "draft all" path: only when the user explicitly asks.
- The "ask whether there's more" question: adapts from "more tasks
  this invocation?" to "draft the next task?"

### Out of scope

- Changes to the task file format.
- Changes to phase-linked vs. orphan distinction.
- Changes to the review gate or status transitions.

### Files to modify

- `.ai/workflow/skills/define-task/SKILL.md`

### Steps

1. Read the current `define-task/SKILL.md` in full.
2. Update the **When to use** section:
   - Change: "Scope is whatever was actually asked" paragraph.
   - New default: "plan the first task" or "plan the next task"
     means exactly one task.
   - New explicit request: "plan all remaining tasks" or "break down
     the whole plan" means all tasks.
   - Ambiguity: ask whether to draft one or all.
3. Update the **Procedure — phase-linked** section:
   - Step 1 (stubbing): Keep as-is — stubbing all remaining plan
     steps is still correct (it's cheap, titles only). The change is
     about *drafting* full task detail, not stubbing.
   - Update the "Then, repeat steps 3–6 for each task actually in
     scope this invocation" wording to clarify the default is one
     task unless the user explicitly asked for all.
   - Step 7: Update the "ask whether there's more" question from
     "more tasks to draft this invocation?" to "draft the next task
     now, or stop?"
   - Step 8: Update the commit message guidance to say which single
     task was drafted (unless all were explicitly requested).
4. Update the **Procedure — orphan** section:
   - Orphan tasks are already drafted one at a time by default
     (there's no phase Plan to exhaust). Just clarify the behavior
     in the text — no orphan task has ever been drafted in batch.
   - Step 6: Update the "ask whether there's more" question from
     "more to add" to "draft the next orphan task now, or stop?"
5. Update the **Output** section to reflect that one task file is
   produced per default invocation (unless all were explicitly
   requested).

### Automatic validations

- `grep -r "draft everything" .ai/workflow/skills/define-task/`
  returns zero matches (the phrase "draft everything" should be
  gone).
- `grep -r "each task actually in scope" .ai/workflow/skills/define-task/`
  returns one match (the updated wording that clarifies default is one).
- No other skill file is modified.

### Manual validations

- The new default ("one task") feels natural and gives the human
  control over planning cadence.
- The "draft all" path is clear when the user explicitly requests it.
- The "ask whether there's more" question is appropriate for the
  single-task default.
