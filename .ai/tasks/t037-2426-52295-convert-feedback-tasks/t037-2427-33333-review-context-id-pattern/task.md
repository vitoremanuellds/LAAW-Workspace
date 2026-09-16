# review-context-id-pattern
**ID:** t037-2427-33333       **Status:** in-progress

## Description
Review the three context files that don't follow the `c{ID}-{name}.md`
pattern (`architecture.md`, `full-directory-structure.md`, `purpose.md`),
decide whether each is necessary, and either convert to the ID pattern
or delete.

## TL;DR
- Check if architecture.md, full-directory-structure.md, purpose.md are needed
- Convert to `c{ID}-{name}.md` format or delete
- Update context.md index accordingly

## Context
### Before
- `architecture.md` — Project architecture: directory layout, key
  relationships, tech stack, LAAW workflow structure, skills overview
- `full-directory-structure.md` — Snapshot of LAAW's `.ai/` directory
  structure, current as of the ADR03/P06 redesign
- `purpose.md` — Project purpose, mission, goals, and history
- All three are referenced in `context.md` index
- All three don't follow the `c{ID}-{name}.md` pattern

### After
- All context files follow the `c{ID}-{name}.md` pattern, or unnecessary
  ones are deleted
- `context.md` index updated to reflect current state

## In scope
- Read `architecture.md`, `full-directory-structure.md`, `purpose.md`
- Evaluate each file's necessity:
  - If necessary: convert to `c{ID}-{name}.md` format using
    `tools/generate-id.py --prefix c` to generate the ID
  - If not necessary: delete the file and remove from `context.md` index
- Update `context.md` index to reflect changes

## Out of scope
- Changes to task file naming (handled by t037-2427-11111)
- Adding Table of Contents to markdown files (handled by t037-2427-44444)

## Steps
1. Evaluate `architecture.md`
   - Read the file content
   - Determine if it's necessary for project context
   - If necessary:
     - Run `tools/generate-id.py --prefix c` to generate an ID
     - Rename to `c{ID}-architecture.md`
     - Update `context.md` index with the new filename
   - If not necessary:
     - Delete the file
     - Remove its row from `context.md` index

2. Evaluate `full-directory-structure.md`
   - Read the file content
   - Determine if it's necessary for project context
   - If necessary:
     - Run `tools/generate-id.py --prefix c` to generate an ID
     - Rename to `c{ID}-full-directory-structure.md`
     - Update `context.md` index with the new filename
   - If not necessary:
     - Delete the file
     - Remove its row from `context.md` index

3. Evaluate `purpose.md`
   - Read the file content
   - Determine if it's necessary for project context
   - If necessary:
     - Run `tools/generate-id.py --prefix c` to generate an ID
     - Rename to `c{ID}-purpose.md`
     - Update `context.md` index with the new filename
   - If not necessary:
     - Delete the file
     - Remove its row from `context.md` index

4. Commit changes
   - Stage renamed/deleted files and updated `context.md`
   - Commit with message describing context file ID pattern compliance

## Validations
- All context files follow the `c{ID}-{name}.md` pattern, or unnecessary
  ones are deleted
- `context.md` index reflects current state (no references to deleted or
  renamed files)
- All context files that remain are necessary for project context

## Rule
- **Always use `tools/generate-id.py --prefix t` to generate IDs for
  any project file that requires an ID.** Never hardcode, guess, or
  manually construct IDs — the script is the single source of truth
  for ID generation across the entire project.
