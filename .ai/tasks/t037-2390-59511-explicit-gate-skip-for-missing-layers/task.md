# Explicit gate-skip for missing layers

**ID:** t037-2390-59511       **Status:** not-started



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

Make it explicit in both LAAW/README.md and workflow.md that gates for
non-existent layers are skipped.

## TL;DR
- Add explicit gate-skip statement to LAAW/README.md §5
- Add same statement to LAAW/workflow.md §5

## Context

### Before
- Lifecycle diagram shows linear flow with no conditional branching
- Gate-skipping for optional layers only inferred, never stated

### After
- Explicit statement in both files: gates for missing layers are skipped

## In scope
- Add statement to LAAW/README.md §5
- Add statement to LAAW/workflow.md §5

## Out of scope
- Changing the lifecycle diagram itself
- Adding gating logic to skills or info.md
- Other README or workflow sections beyond §5

## Steps
1. Read LAAW/README.md §5, find insertion point
2. Add explicit gate-skip statement
3. Read LAAW/workflow.md §5, find insertion point
4. Add same statement
5. Verify both additions present and consistent

## Validations
- grep -c "Gates for missing layers" LAAW/README.md returns 1
- grep -c "Gates for missing layers" LAAW/workflow.md returns 1
- Statement appears in both files with consistent meaning
