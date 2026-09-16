# Make build-context.iterate's finished-queue step delete both workbench files automatically

**ID:** t037-2386-30126       **Status:** done

## Description

Replace the old ask-before-deleting step per ADR02: delete both
.ai/workbench/context.temp.md and .ai/workbench/build-plan.md, commit
the deletion, and report completion — no human confirmation gate.

## TL;DR
- Remove ask-before-deleting step
- Auto-delete both workbench files
- Commit deletion automatically

## Steps
1. Update build-context.iterate final step
2. Remove human confirmation gate
3. Add auto-delete logic

## Validations
- No human confirmation for workbench cleanup
- Files deleted and committed automatically
