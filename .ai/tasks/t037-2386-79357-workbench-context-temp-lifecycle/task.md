# Workbench directory & context-build temp-file lifecycle

**ID:** t037-2386-79357       **Status:** done



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

Converted from P03 — Workbench directory & context-build temp-file
lifecycle. Established `.ai/workbench/` as a freeform disposable
directory, relocated `build-context-full`'s temp files there, and
added workbench-readme-template.

## TL;DR
- Established `.ai/workbench/` convention
- Relocated build-context-full temp files
- Added workbench-readme-template.md
- Updated workflow.md, reference/, skills

## Context

### Before
- P03 phase with 5 tasks (P03-T01 through P03-T05), all complete

### After
- Parent task with 5 subtasks, all done

## In scope
- Converted from P03 phase
- All 5 subtasks completed and shipped

## Out of scope
- Any changes to the LAAW repo itself

## Subtasks
| id | name | description | depends on | status |
|----|------|-------------|------------|--------|
| t037-2386-51748 | document-workbench | Document .ai/workbench/ in workflow.md and directory-and-links.md | — | done |
| t037-2386-49725 | repoint-templates | Repoint context-temp-template.md/context-build-plan-template.md to .ai/workbench/ | — | done |
| t037-2386-48071 | update-build-context-skill | Update build-context-full/SKILL.md to use .ai/workbench/ | t037-2386-51748, t037-2386-49725 | done |
| t037-2386-30126 | automate-workbench-cleanup | Make build-context.iterate delete workbench files automatically | t037-2386-48071 | done |
| t037-2386-09452 | add-workbench-readme-template | Add workbench-readme-template.md and wire into create-constitution | — | done |
