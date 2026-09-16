# Non-submodule bootstrap mechanism

**ID:** t037-2386-13289       **Status:** done



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

Converted from P02 — Non-submodule bootstrap mechanism. Shipped the
copy-based bootstrap/re-sync mechanism: `LAAW/sync-workflow.sh`
installs/re-syncs the workflow into a target project's `.ai/workflow/`,
plus a version-stamp file restoring commit traceability.

## TL;DR
- Shipped `LAAW/sync-workflow.sh` script
- Version-stamp convention (ADR04)
- Updated LAAW/README.md, mission.md, techstack.md, ADR01
- Dogfooded against this workspace

## Context

### Before
- P02 phase with 5 tasks (P02-T01 through P02-T05), all complete
- Old task ID format

### After
- Parent task with 5 subtasks, all done
- New task ID format

## In scope
- Converted from P02 phase
- All 5 subtasks completed and shipped

## Out of scope
- Any changes to the LAAW repo itself — that was done in LAAW/ checkout

## Subtasks
| id | name | description | depends on | status |
|----|------|-------------|------------|--------|
| t037-2386-09761 | design-version-stamp | Design and record version-stamp convention (ADR04) | — | done |
| t037-2386-55024 | draft-sync-script | Draft the copy/re-sync script (LAAW/sync-workflow.sh) | t037-2386-09761 | done |
| t037-2386-60598 | update-readme | Update LAAW/README.md bootstrapping/updating sections | t037-2386-55024 | done |
| t037-2386-72751 | update-workspace-docs | Update mission.md, techstack.md, ADR01 | t037-2386-55024, t037-2386-60598 | done |
| t037-2386-07232 | dogfood | Dogfood the script against this workspace | t037-2386-55024 | done |
