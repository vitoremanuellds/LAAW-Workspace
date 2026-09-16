# Merge decisions → context

**ID:** t037-2384-22173       **Status:** not-started



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

Convert each ADR file from `decisions/` into a `c-{ID}-{name}.md`
context item in `context/` using the new decision shape (Decision/
Context/Alternatives/Consequences), update `context/context.md` index
table with all decision context items, and delete the `decisions/`
folder.

## TL;DR
- Read each ADR file from decisions/
- Convert each to c-{ID}-{name}.md in context/
- Update context.md index table
- Delete decisions/ folder

## Context

### Before
- `decisions/` folder with 5 ADR files:
  - adr01-plain-copy-bootstrap.md (569 words)
  - adr02-workbench-directory.md (1.1 KB)
  - adr03-single-modular-workflow.md (2.4 KB)
  - adr04-workflow-version-stamp.md (1.8 KB)
  - adr08-id-format.md (478 words)
- `decisions/decisions.md` — index table with 5 rows
- `context/context.md` — index table with 6 items (from constitution merge)

### After
- `context/c037-2384-96156-plain-copy-bootstrap.md`
- `context/c037-2384-22173-workbench-directory.md`
- `context/c037-2384-01677-single-modular-workflow.md`
- `context/c037-2384-76968-workflow-version-stamp.md`
- `context/c037-2384-72444-id-format.md`
- `context/context.md` updated with new index rows
- `decisions/` folder deleted

## In scope
- Read each ADR file from decisions/
- Convert each to c-{ID}-{name}.md format in context/
- Update context.md index table with all 5 decision context items
- Delete decisions/ folder (including decisions.md)

## Out of scope
- Merging phases/ (separate subtask)
- Updating AGENTS.md (separate subtask)
- Any changes to the LAAW repo itself

## Steps

1. **Generate IDs:** Run `python3 LAAW/tools/generate-id.py --prefix c` five times to get new IDs for the 5 ADRs.
2. **Read ADR files:** Read all 5 ADR files from `decisions/`.
3. **Create c-{ID}-{name}.md files:** For each ADR, create a new context item in `context/` using the new decision shape:
   ```markdown
   # c-{ID}-{name}

   ## Decision
   <the decision content, stripped of the ADR header>

   ## Context
   <the context content>

   ## Alternatives Considered
   <the alternatives content>

   ## Consequences
   <the consequences content>
   ```
   Map:
   - adr01 → c037-2384-96156-plain-copy-bootstrap
   - adr02 → c037-2384-22173-workbench-directory
   - adr03 → c037-2384-01677-single-modular-workflow
   - adr04 → c037-2384-76968-workflow-version-stamp
   - adr08 → c037-2384-72444-id-format

4. **Update context.md index:** Add all 5 new context items to the index table in `context/context.md` with proper descriptions and relations.
5. **Delete decisions/:** Remove the entire `decisions/` folder.
6. **Verify:** Confirm all 5 c-{ID}.md files exist in context/, decisions/ is deleted, context.md index is updated.

## Validations
- `decisions/` folder no longer exists
- All 5 c-{ID}-{name}.md files exist in `context/`
- `context/context.md` index table includes all 5 decision context items
- Each c-{ID}.md file has Decision/Context/Alternatives/Consequences sections
