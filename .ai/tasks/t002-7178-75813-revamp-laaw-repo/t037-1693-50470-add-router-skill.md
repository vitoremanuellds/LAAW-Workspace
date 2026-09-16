# Add router skill

**ID:** t037-1693-50470       **Status:** done

## Description

Create the router skill (`LAAW/skills/route/SKILL.md`) — a plain-language
request parser that maps user intents to the correct operation skill.
The router does no operation work itself; it only reads the user's
request, decides which skill to delegate to, and points the agent at
that skill's file. First router in the two-gate lifecycle, replacing
the old "call the skill explicitly" pattern with "state what you want
in plain terms."

## TL;DR

- New `LAAW/skills/route/SKILL.md` — routing only, no operation work.
- Maps plain-language requests to the eight operation skills.
- Listed in `workflow.md`'s operation table (already done by t037-1693-16386).
- Referenced by `reference/reread-skill-discipline.md` (step 6 of this task).

## Context

### Before

- Parent task [t002-7178-75813](t002-7178-75813-revamp-laaw-repo.md) — the LAAW revamp.
  Depends on t037-1693-16386 (workflow.md rewrite, done), which already
  lists `route` in the operation table.
- Decision [c037-1650-68133](../../context/c037-1650-68133-revamp-open-decisions.md)
  settles the router skill name as `route`.
- `workflow.md` (§2) already has the operation table with `route` as
  the first row — no further workflow.md changes needed for this skill.
- The revamp design says: *"In front of them sits a router skill: the
  user states what they want in plain terms, and the router points the
  agent to the correct operation skill — the user does not have to name
  a skill. This is routing, not a fourth skill doing the operation's
  work."*
- The old README best-practices section said "Call the skill explicitly"
  — this is the reason the router exists; the README rewrite (step 8)
  will remove that advice.

### After

<!-- Filled in by implement-task after implementation -->

## In scope

- `LAAW/skills/route/SKILL.md` — new file, full skill following the
  standard format: frontmatter, Can/Must/Cannot, procedure, output.
- The skill maps these user intents to the correct skill:
  - "bootstrap" → `bootstrap/SKILL.md`
  - "constitution", "mission", "techstack", "context setup" →
    `create-constitution/SKILL.md`
  - "plan", "task", "break down" → `define-task/SKILL.md`
  - "implement", "write", "code" → `implement-task/SKILL.md`
  - "validate", "check", "test" → `validate-work/SKILL.md`
  - "review", "check quality", "judgment" → `review-work/SKILL.md`
  - "build context", "survey", "fill context" → `build-context/SKILL.md`
  - "propagate", "finalize", "mark done" → `propagate-context/SKILL.md`
- The skill states clearly: it does no operation work itself; it only
  points at the correct skill file.
- The skill's procedure: (1) read `../info.md` fresh; (2) read the
  matched skill file in full; (3) delegate to that skill's procedure.

## Out of scope

- Any changes to the operation skills themselves — those are covered by
  their own subtasks (steps 3–4).
- Changes to `workflow.md` — already done by t037-1693-16386.
- Changes to the README — covered by step 8.
- Changes to reference docs — covered by step 6 (this skill is
  referenced by `reread-skill-discipline.md`).

## Steps

1. Create `LAAW/skills/route/` directory.
2. Write `LAAW/skills/route/SKILL.md` with the standard skill format:
   - Frontmatter: `name: route`, description stating it routes plain-language
     requests to the correct operation skill.
   - Can/Must/Cannot contract: Can read user request + workflow.md,
     point to the correct skill file; Must read `info.md` fresh, read
     the matched skill file in full; Cannot do operation work itself.
   - Procedure: (a) read `../info.md` for gate authority; (b) parse
     user request to determine intent; (c) read the matched skill file
     in full; (d) delegate to that skill's procedure.
   - Operation table mapping (same as workflow.md §2): bootstrap,
     create-constitution, define-task, implement-task, validate-work,
     review-work, build-context, propagate-context.
   - Output: the matched skill file is now loaded; agent proceeds with
     that skill's procedure.
3. Verify the skill's operation table matches `workflow.md`'s table
   exactly (same eight entries, same order).
4. Verify no other files in `skills/` need updating — this is a new
   file only; the other skills are unchanged by this subtask.

## Validations

- `LAAW/skills/route/SKILL.md` exists and follows the standard skill
  format (frontmatter, Can/Must/Cannot, procedure, output).
- The operation table in the router matches `workflow.md`'s table
  (§2) exactly: eight entries, same order.
- The skill explicitly states it does no operation work — it only
  points at the correct skill file.
- The skill's procedure includes reading `info.md` fresh and reading
  the matched skill file in full (same discipline as all other skills).
- No stale "call the skill explicitly" references elsewhere in this
  subtask's scope (the README change is step 8).
