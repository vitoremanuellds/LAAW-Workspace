# P08-T06: Strengthen .gitignore Discipline

## Context

See [../phases/p08-feedback-improvements/phase.md](../phases/p08-feedback-improvements/phase.md).

## Implementation

### Objective

Prevent agents from committing `.gitignore`d files by adding emphatic,
repeated instructions across the workflow documentation and agent
instructions — not just a passing mention, but a clear, hard rule with
an explicit check step in every commit.

### In scope

- Strengthen the `.ai/workflow/workflow.md` §12 (Commit discipline)
  with an emphatic `.gitignore` rule and a concrete pre-commit check
  step.
- Update `AGENTS.md` with a dedicated `.gitignore` discipline section
  that agents must read.
- Add a `.gitignore` check step to each skill's commit procedure
  (bootstrap, build-context, create-constitution, define-phase,
  define-task, implement-task, propagate-context, review-work,
  validate-work).

### Out of scope

- Changes to the `.gitignore` file contents itself (that's a project
  decision, not an agent discipline issue).
- Modifying the `.agents/` directory structure or skill registration.
- Adding automated enforcement (hooks, CI checks) — this is a
  documentation/instruction change only.

### Files to modify

```
.ai/workflow/workflow.md          — §12 Commit discipline: add emphatic .gitignore rule
AGENTS.md                        — Add .gitignore discipline section
.agents/skills/bootstrap/SKILL.md       — Add .gitignore check to commit step
.agents/skills/build-context/SKILL.md   — Add .gitignore check to commit step
.agents/skills/create-constitution/SKILL.md — Add .gitignore check to commit step
.agents/skills/define-phase/SKILL.md    — Add .gitignore check to commit step
.agents/skills/define-task/SKILL.md     — Add .gitignore check to commit step
.agents/skills/implement-task/SKILL.md  — Add .gitignore check to commit step
.agents/skills/propagate-context/SKILL.md — Add .gitignore check to commit step
.agents/skills/review-work/SKILL.md     — Add .gitignore check to commit step
.agents/skills/validate-work/SKILL.md   — Add .gitignore check to commit step
```

### Steps

1. **Update workflow.md §12 (Commit discipline)**
   - Replace the current single-sentence mention of `.gitignore` with
     a dedicated, emphatic subsection:
     - State clearly: "NEVER commit files that `.gitignore` excludes."
     - Add a concrete pre-commit verification step: "Before every
       commit, run `git diff --cached` and verify no `.gitignore`d
       files appear in the staged list."
     - Make the instruction emphatic (use ALL CAPS for the core rule,
       not just markdown emphasis).
   - Keep existing content about locality and per-layer choices.

2. **Add `.gitignore` discipline section to AGENTS.md**
   - Create a new section `## Git Discipline` (or similar) after
     `Agent Workflow`.
   - State the rule emphatically: agents must check `.gitignore`
     before committing and must never stage ignored files.
   - Reference the workflow.md §12 for the detailed procedure.

3. **Add `.gitignore` check to each skill's commit step**
   - For each of the 9 skill files listed above, find the commit
     procedure step (the one that references workflow.md §12).
   - Add a `.gitignore` pre-commit check sentence to that step, e.g.:
     "Before staging, verify no `.gitignore`d files are included —
     run `git diff --cached` and check the output."
   - Keep the existing content; just add the check as a preceding
     sentence or clause in the same step.

### Automatic validations

- Run `grep -n "\.gitignore\|gitignore" .ai/workflow/workflow.md` and
  verify the commit discipline section contains an emphatic rule
  (ALL CAPS or similar strong language), not just a passing mention.
- Run `grep -n "\.gitignore\|gitignore" AGENTS.md` and verify a
  dedicated section exists with clear instructions.
- For each of the 9 skill files, verify the commit step includes a
  `.gitignore` check instruction.
- Run `git diff --cached` after a dry-run commit of the changed files
  and confirm only the intended files appear.

### Manual validations

- Does the `.gitignore` instruction in workflow.md feel emphatic
  enough to prevent agent overreach?
- Does the AGENTS.md section provide clear, actionable guidance?
- Are the skill updates consistent with each other and with the
  workflow.md rule?
- Is the tone appropriate — firm but not condescending?
