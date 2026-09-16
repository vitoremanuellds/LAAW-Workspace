# Redesign LAAW as a single modular workflow

**ID:** t037-2386-24191       **Status:** done



<!-- TOC -->
<details><summary>Table of Contents</summary>

  - [Description](#description)
  - [TL;DR](#tldr)
  - [Context](#context)
    - [Before](#before)
    - [After](#after)
  - [In scope](#in-scope)
  - [Out of scope](#out-of-scope)
  - [Subtasks](#subtasks)

</details>
## Description

Converted from P06 — Redesign LAAW as a single modular workflow.
Retired per-profile repos, established one modular workflow with
optional layers (presence/granularity/locality axes).

## TL;DR
- Created bootstrap skill
- Established scaffold-on-first-use convention
- Narrowed constitution skill to mission/techstack only
- Updated phase/task planning skills
- Dropped info.md Status section
- Rewrote workflow.md

## Context

### Before
- P06 phase with 6 tasks (P06-T01 through P06-T06), all complete

### After
- Parent task with 6 subtasks, all done

## In scope
- Converted from P06 phase
- All 6 subtasks completed and shipped

## Out of scope
- Any changes to the LAAW repo itself

## Subtasks
| id | name | description | depends on | status |
|----|------|-------------|------------|--------|
| t037-2386-23102 | scaffold-convention | Scaffold convention + workflow.md rewrite | — | done |
| t037-2386-61135 | constitution-bootstrap-skills | Constitution + bootstrap skills | t037-2386-23102 | done |
| t037-2386-55744 | phase-task-planning-skills | Phase + task planning skills | t037-2386-23102 | done |
| t037-2386-70136 | remaining-renames-propagate | Remaining skill renames + propagate-context | t037-2386-23102 | done |
| t037-2386-16658 | templates-reference | Templates + reference/ updates | t037-2386-23102, t037-2386-61135, t037-2386-55744, t037-2386-70136 | done |
| t037-2386-63379 | validation-size-check | Validation + size check | t037-2386-23102, t037-2386-61135, t037-2386-55744, t037-2386-70136, t037-2386-16658 | done |
