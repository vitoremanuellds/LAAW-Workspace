# T02 — Fix LAAW's remaining "submodule" mislabel

## Context

See [.ai/phases/p02-non-submodule-bootstrap-mechanism.md](../phases/p02-non-submodule-bootstrap-mechanism.md) for the full P02 context. P02 shipped `sync-workflow.sh` and the version-stamp convention, but two files in `LAAW/`'s own checkout still say "submodule" where they should say "plain copy" — a cosmetic inconsistency that was left intentionally out of scope for P02 (P02-T04 updated this repo's docs, P02-T03 updated `LAAW/README.md`, but `LAAW/workflow.md` §3 itself was not touched).

The `LAAW/workflow.md` §3 directory-structure block is the source-of-truth snapshot that bootstrapped projects inherit. Having it say "submodule" while `sync-workflow.sh` is the actual mechanism is misleading to anyone reading the installed copy.

## Implementation

### Objective

Replace the two remaining "submodule" references in `LAAW/`'s own checkout with accurate "plain copy" language, so that the installed workflow is self-consistent.

### In scope

- `LAAW/workflow.md` §3 directory-structure block: change "submodule, never written to" to "plain copy, managed by sync-workflow.sh (P02), never written to"
- `LAAW/skills/build-context/SKILL.md` line 52: change "(the submodule)" to "(the plain copy)"

### Out of scope

- Any other `.ai/` docs in this outer repo (already updated by P02-T04 and this context propagation)
- Any changes to `LAAW/README.md` (P02-T03 already updated it correctly)
- Any changes to `LAAW/sync-workflow.sh` (its comment references to `git submodule add`/`git submodule update --remote` are explanatory — they state what the script replaces, not what the mechanism is)
- Any changes to `LAAW/sync-skills.sh` (its `git submodule update` reference is about the skills-sync script's own usage pattern, unrelated to the workflow bootstrap mechanism)

### Files to modify

- `LAAW/workflow.md` — line 47: update the `.ai/workflow/` line in the directory-structure code block
- `LAAW/skills/build-context/SKILL.md` — line 52: update the parenthetical reference

### Steps

1. Open `LAAW/workflow.md`.
2. Find the directory-structure code block (line ~47):
   ```
   .ai/workflow/       submodule, never written to — workflow.md, reference/, templates/, skills/
   ```
3. Change it to:
   ```
   .ai/workflow/       plain copy, managed by sync-workflow.sh (P02), never written to — workflow.md, reference/, templates/, skills/
   ```
4. Open `LAAW/skills/build-context/SKILL.md`.
5. Find line 52:
   ```
   .git/, .ai/workflow/ (the submodule), and any build/dependency
   ```
6. Change it to:
   ```
   .git/, .ai/workflow/ (the plain copy), and any build/dependency
   ```
7. Verify no other "submodule" references remain in `LAAW/` that should be updated (the remaining ones in `sync-workflow.sh`, `README.md`, and `sync-skills.sh` are all correct as-is).

### Expected result

- `LAAW/workflow.md` §3 directory-structure block accurately describes `.ai/workflow/` as a plain copy managed by `sync-workflow.sh`
- `LAAW/skills/build-context/SKILL.md` refers to `.ai/workflow/` as "the plain copy"
- No unintended changes to other files in `LAAW/`

### Automatic validations

- `grep -n "submodule" LAAW/workflow.md` returns no results
- `grep -n "submodule" LAAW/skills/build-context/SKILL.md` returns no results
- `grep -rn "submodule" LAAW/` returns only the expected references: `sync-workflow.sh` (comment explaining what it replaces), `README.md` (explicitly says no submodule involved), `sync-skills.sh` (its own usage pattern)

### Manual validations

- Confirm the directory-structure block in `LAAW/workflow.md` §3 reads consistently with the rest of the file's language about the bootstrap mechanism
- Confirm `build-context`'s instruction text still makes sense with "(the plain copy)"
