# Fix LAAW's remaining "submodule" mislabel

**ID:** t037-2389-40026       **Status:** not-started



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

Replace the two remaining "submodule" references in LAAW/ with accurate
"plain copy" language.

## TL;DR
- Update LAAW/workflow.md §3
- Update LAAW/skills/build-context/SKILL.md

## Context

### Before
- LAAW/workflow.md §3 says "submodule, never written to"
- LAAW/skills/build-context/SKILL.md says "(the submodule)"

### After
- LAAW/workflow.md says "plain copy, managed by sync-workflow.sh"
- LAAW/skills/build-context/SKILL.md says "(the plain copy)"

## In scope
- Update LAAW/workflow.md §3
- Update LAAW/skills/build-context/SKILL.md

## Out of scope
- Other .ai/ docs in this outer repo
- LAAW/README.md (already updated by P02-T03)
- LAAW/sync-workflow.sh (explanatory references correct)

## Steps
1. Update LAAW/workflow.md §3 directory-structure block
2. Update LAAW/skills/build-context/SKILL.md line 52
3. Verify no other "submodule" references remain (expected ones OK)

## Validations
- grep -n "submodule" LAAW/workflow.md returns no results
- grep -n "submodule" LAAW/skills/build-context/SKILL.md returns no results
- Expected references in sync-workflow.sh, README.md, sync-skills.sh remain
