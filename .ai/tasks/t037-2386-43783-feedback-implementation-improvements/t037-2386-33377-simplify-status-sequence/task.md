# Simplify status sequence across workflow and skills

**ID:** t037-2386-33377       **Status:** not-started

## Description

Simplify status sequence: remove plan-approved, merge validating into
reviewing. New enum: not-planned → awaiting-plan-review → in-progress
→ reviewing → complete.

## TL;DR
- Remove plan-approved status
- Merge validating into reviewing
- Update all references

## Steps
1. Update status enum
2. Update workflow.md
3. Update all skill references

## Validations
- No plan-approved references
- No validating status references
- All skills use new enum
