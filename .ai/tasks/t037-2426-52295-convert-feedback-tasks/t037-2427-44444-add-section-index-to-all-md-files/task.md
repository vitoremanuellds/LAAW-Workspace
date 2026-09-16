# add-section-index-to-all-md-files
**ID:** t037-2427-44444       **Status:** in-progress

## Description
Add Table of Contents (TOC) to all multi-section markdown files in
`.ai/` and `LAAW/`, and update skills to include TOC requirement as a
creation instruction.

## TL;DR
- Add TOC to all multi-section markdown files in .ai/ and LAAW/
- Update skills to include TOC requirement as creation instruction
- Use internal anchor links (e.g., [Description](#description))

## Context
### Before
- Multi-section markdown files in `.ai/` and `LAAW/` have no Table of
  Contents
- Skills don't mention TOC requirement as a creation instruction

### After
- All multi-section markdown files have a TOC with internal anchor links
- Skills include TOC requirement as a creation instruction

## In scope
- Scan all `.ai/` and `LAAW/` markdown files for 2+ sections
- Add TOC to each file with internal anchor links
- Update LAAW skills to include TOC requirement as creation instruction
- Update `.agents/skills/` and `.ai/workflow/` sync copies

## Out of scope
- Changes to task file naming (handled by t037-2427-11111)
- Reviewing context files for ID pattern compliance (handled by t037-2427-33333)

## Steps
1. Scan `.ai/` and `LAAW/` for multi-section markdown files
   - Find all `.md` files with 2+ `##` headings
   - List them for processing

2. Add TOC to `.ai/` markdown files
   - For each file with 2+ sections:
     - Generate TOC using internal anchor links (e.g., `[Description](#description)`)
     - Insert TOC after the title, before first section
   - Examples: `workflow.md`, `skills/define-task/SKILL.md`, etc.

3. Add TOC to `LAAW/` markdown files
   - For each file with 2+ sections:
     - Generate TOC using internal anchor links
     - Insert TOC after the title, before first section
   - Examples: `workflow.md`, `README.md`, `skills/define-task/SKILL.md`, etc.

4. Update skills to include TOC requirement
   - Add creation instruction to all skills: "Include a Table of Contents
     with internal anchor links for files with 2+ sections"
   - Update: `LAAW/skills/` all SKILL.md files
   - Sync to `.agents/skills/` and `.ai/workflow/skills/`

5. Commit changes
   - Stage all updated markdown files
   - Commit with message describing TOC addition

## Rule
- **Always use `tools/generate-id.py --prefix t` to generate IDs for
  any project file that requires an ID.** Never hardcode, guess, or
  manually construct IDs — the script is the single source of truth
  for ID generation across the entire project.

## Validations
- All multi-section markdown files in `.ai/` have a TOC
- All multi-section markdown files in `LAAW/` have a TOC
- All TOCs use internal anchor links (e.g., `[Description](#description)`)
- All skills include TOC requirement as a creation instruction
- `.agents/skills/` and `.ai/workflow/skills/` synced from LAAW repo
