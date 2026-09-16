# Merge constitution → context

**ID:** t037-2379-60933       **Status:** not-started



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

Merge `constitution/mission.md` and `constitution/techstack.md` as
inline sections into `context/context.md`, update the index table to
include all existing context items, and delete the now-empty
`constitution/` folder.

## TL;DR
- Read mission.md and techstack.md
- Rewrite context.md with inline ## Mission and ## Techstack
- Update the index table with all context items
- Delete constitution/

## Context

### Before
- `constitution/mission.md` — 2.5 KB, describes what/why/who/goals/boundaries
- `constitution/techstack.md` — 1 KB, describes content format, bootstrap,
  versioning, target constraint
- `context/context.md` — 2 KB, index table with 6 items (full-directory-structure.md,
  purpose.md, architecture.md, c037-1650-68133, c037-1675-68146, c037-1693-91765)
- `constitution/` folder exists with 2 files

### After
- `context/context.md` contains inline ## Mission and ## Techstack sections
  plus the index table
- `constitution/` folder deleted

## In scope
- Read constitution/mission.md and constitution/techstack.md
- Rewrite context/context.md with inline Mission + Techstack + index table
- Delete constitution/ folder

## Out of scope
- Merging decisions/ (that's a separate subtask)
- Merging phases/ (separate subtask)
- Updating AGENTS.md (separate subtask)
- Any changes to the LAAW repo itself

## Steps

1. **Read constitution files:** Read `constitution/mission.md` and
   `constitution/techstack.md` to get their full content.
2. **Read existing context.md:** Read `context/context.md` to capture
   the existing index table entries and their relations.
3. **Write new context.md:** Create `context/context.md` with this
   structure:
   ```markdown
   # Context

   ## Mission

   <content from mission.md>

   ## Techstack

   <content from techstack.md>

   ## Index

   | File | Description | Status | Relations |
   |---|---|---|---|
   | [full-directory-structure.md](full-directory-structure.md) | ... | active | ... |
   | [purpose.md](purpose.md) | ... | active | |
   | [architecture.md](architecture.md) | ... | active | ... |
   | [c037-1650-68133-revamp-open-decisions.md](c037-1650-68133-revamp-open-decisions.md) | ... | active | ... |
   | [c037-1675-68146-id-name-filenames.md](c037-1675-68146-id-name-filenames.md) | ... | active | ... |
   | [c037-1693-91765-ids-ordered-by-table.md](c037-1693-91765-ids-ordered-by-table.md) | ... | active | ... |
   ```
   Note: The index table includes the existing context items. The
   Mission and Techstack sections are inline (not separate files).
4. **Delete constitution/:** Remove the entire `constitution/` folder
   and all its contents.
5. **Verify:** Confirm `constitution/` is deleted, `context/context.md`
   has inline Mission + Techstack, and the index table is present.

## Validations
- `constitution/` folder no longer exists
- `context/context.md` contains `## Mission` and `## Techstack` sections
- `context/context.md` has an index table with all 6 existing context items
- No orphan files in constitution/
