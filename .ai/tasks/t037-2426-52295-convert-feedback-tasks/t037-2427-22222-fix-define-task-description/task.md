# fix-define-task-description
**ID:** t037-2427-22222       **Status:** done



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
  - [Rule](#rule)

</details>
## Description
Fix the broken description in `LAAW/skills/define-task/SKILL.md` that
complains about `"{}"` and `":"` characters. The frontmatter description
contains template variable syntax (`t{ID}-{name}`) that LLMs interpret
literally, causing the skill to generate error messages when encountering
those characters in user input.

## TL;DR
- Fix define-task description in LAAW repo to remove literal complaint
- Sync fixed skill to `.agents/skills/`

## Context
### Before
- `LAAW/skills/define-task/SKILL.md` frontmatter description contains:
  ```
  description: Break a plan into individual tasks (tasks/t{ID}-{name}.md),
    or draft a standalone task with no parent (tasks/t{ID}-{name}.md,
    indexed in tasks/tasks.md).
  ```
- The LLM interprets `{` and `}` and `:` in the description as literal
  characters, causing it to complain when users include those characters
  in their task names or descriptions.

### After
- The description no longer contains template variable syntax that triggers
  literal complaints.
- `.agents/skills/define-task/SKILL.md` is synced from LAAW repo.

## In scope
- Read `LAAW/skills/define-task/SKILL.md`
- Fix the frontmatter description to remove or escape template variable
  syntax that causes the LLM to complain about `"{}"` and `":"`.
- Commit the fix in LAAW repo.
- Sync the fixed skill to `.agents/skills/define-task/SKILL.md`.

## Out of scope
- Updating task file naming convention (handled by
  t037-2427-11111-convert-task-file-naming).
- Adding Table of Contents to markdown files (handled by
  t037-2427-44444-add-section-index-to-all-md-files).
- Reviewing context files for ID pattern compliance (handled by
  t037-2427-33333-review-context-id-pattern).

## Steps
1. Read `LAAW/skills/define-task/SKILL.md` frontmatter
   - Identify the exact description text that causes the LLM to complain
     about `"{}"` and `":"`
2. Fix the description
   - Option A: Remove template variable syntax from the description entirely
     and replace with plain-language equivalents.
   - Option B: Escape or reword the description so the LLM doesn't treat
     `{`, `}`, and `:` as literal characters to complain about.
   - Verify the fix resolves the complaint behavior.
3. Commit the fix in LAAW repo
   - Stage `LAAW/skills/define-task/SKILL.md`
   - Commit with message describing the description fix
4. Sync to `.agents/skills/`
   - Copy `LAAW/skills/define-task/SKILL.md` →
     `.agents/skills/define-task/SKILL.md`

## Validations
- `LAAW/skills/define-task/SKILL.md` description no longer contains
  template variable syntax that triggers literal complaints
- `.agents/skills/define-task/SKILL.md` is synced from LAAW repo
- Description is still accurate and usable for the skill's purpose

## Rule
- **Always use `tools/generate-id.py --prefix t` to generate IDs for
  any project file that requires an ID.** Never hardcode, guess, or
  manually construct IDs — the script is the single source of truth
  for ID generation across the entire project.
