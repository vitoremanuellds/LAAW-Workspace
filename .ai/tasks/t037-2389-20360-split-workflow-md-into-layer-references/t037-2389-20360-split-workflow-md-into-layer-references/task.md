# Split workflow.md's per-layer detail into reference/ files

**ID:** t037-2389-20360       **Status:** not-started

## Description

Reduce workflow.md's own required-reading size by extracting layer-specific
detail into reference/ files, read only by the skills that actually need
them.

## TL;DR
- Extract layer-specific detail from workflow.md
- Move to reference/ files
- Confirm workflow.md is at or below pre-P06 baseline

## Context

### Before
- workflow.md grew ~19% (1206 → 1432 words) post-P06
- Layer-specific detail mixed with universal content

### After
- workflow.md at or below 1206 words
- Per-layer detail in reference/, read only by relevant skills

## In scope
- Identify layer-specific content in workflow.md
- Move to reference/ files
- Update workflow.md with pointers

## Out of scope
- Changing any rule or decision from ADR03/P06
- This outer meta-repo's own .ai/

## Steps
1. Re-read workflow.md and mark layer-specific paragraphs
2. Move to reference/ files
3. Replace with pointers in workflow.md
4. Verify word count ≤ 1206
5. Spot-check skill access

## Validations
- wc -w LAAW/workflow.md ≤ 1206
- workflow.md still coherent
- No skill lost access to needed detail
