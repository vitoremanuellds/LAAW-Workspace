# P08-T08: Update ADR03

## Context

[Phase P08: Feedback Implementation Improvements](../phases/p08-feedback-improvements/phase.md)

## Implementation

### Objective

Update ADR03 to cross-reference the new ID scheme (timestamp + random) and the phase-folder task structure as an evolution of the original design decisions.

### In scope

- Add an "Evolutions" or "Related" section to ADR03 that references the new ID scheme and folder structure introduced in P08.

### Out of scope

- Rewriting the core decision or context sections of ADR03.
- Creating a new ADR for the ID scheme or folder structure (those are P08 decisions, not superseding ADR03's core design).

### Files to modify

- `.ai/decisions/adr03-single-modular-workflow.md` — Add cross-references to the new ID scheme and phase-folder task structure.

### Steps

1. Read `.ai/decisions/adr03-single-modular-workflow.md`.
2. In the **Consequences** section (or add a new **Evolutions** section after Consequences), add entries that document how P08 evolved the design:
   - **ID format evolution:** The original ADR03 described sequential IDs (`p{NN}-t{NN}-{name}.md`). P08 introduced a collision-safe format using `{prefix}{minutes:07d}{random:05d}-{name}` (e.g., `p00525960123456-name`) with a 7-digit zero-padded minutes-elapsed component and 5-digit random component. This format is defined in `LAAW/tools/generate_id.py` and `LAAW/tools/constants.py`. See [Phase P08](../phases/p08-feedback-improvements/phase.md).
   - **Task folder structure evolution:** ADR03 specified flat task files in `.ai/tasks/`. P08 introduced phase-folders: phase-linked tasks now live under `.ai/phases/p{NN}-{name}/t{NN}-{name}.md` alongside their phase file, while orphan tasks remain flat in `.ai/tasks/`. See [Phase P08](../phases/p08-feedback-improvements/phase.md).
3. In the **Alternatives Considered** section, verify the existing entries still hold (they do — the three-axis design remains unchanged).
4. In the **Context** section, add a note that the ID and folder conventions described in the Consequences section were further refined in P08 for concurrency safety and navigability.
5. Update the file's title or add an "Update log" subsection at the top if the project convention requires it (check if other ADRs have update logs; if not, skip this).

### Automatic validations

- Grep `.ai/decisions/adr03-single-modular-workflow.md` and confirm it references `generate_id.py` or the new ID format pattern.
- Grep `.ai/decisions/adr03-single-modular-workflow.md` and confirm it references the phase-folder task path pattern `p{NN}-{name}/t{NN}-{name}.md`.
- Confirm the file still reads coherently — no broken references or contradictory statements.

### Manual validations

- Do the cross-references clearly communicate that P08 is an evolution, not a contradiction, of ADR03?
- Is the ADR still readable for someone who hasn't seen P08's phase file?
- Are the references to P08's phase file and supporting files accurate?
