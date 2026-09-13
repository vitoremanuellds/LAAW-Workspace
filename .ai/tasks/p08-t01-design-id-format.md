# P08-T01: Design the New ID Format

## Context

See [../phases/p08-feedback-improvements.md](../phases/p08-feedback-improvements.md)
for the phase context, requirements, and plan.

## Implementation

### Objective

Define the complete ID generation specification — epoch, format, naming
convention, and constants file — so that all agents computing IDs
concurrently produce unique, lexicographically sortable identifiers.

### In scope

- Define the custom epoch (start date for minutes-elapsed calculation).
- Define the full ID format string with component widths.
- Define the naming convention for phases, tasks, and decisions.
- Create the constants file that all agents read to compute IDs.
- Document the collision probability analysis.

### Out of scope

- Implementing the ID generation script (that's P08-T02).
- Restructuring task folders (P08-T04).
- Migrating existing IDs to the new format (deferred).
- Updating workflow.md references (P08-T03).

### Files to create

- `LAAW/constants.py` — Python module defining `EPOCH`, `MIN_WIDTH`,
  `RANDOM_WIDTH`, `MIN_MAX`, `FORMAT_STRING`, and helper functions for
  ID generation. This is the single source of truth all agents read.
- `.ai/decisions/adr08-id-format.md` — ADR documenting the ID format
  decision, rationale, and collision analysis.

### Files to modify

- `.ai/decisions/decisions.md` — Add row for ADR08.

### Steps

1. **Define the epoch date** — Choose a fixed past date as the epoch
   (e.g., `2020-01-01T00:00:00Z`). The epoch should be far enough in
   the past that the 7-digit counter won't approach overflow during
   the project's lifetime.

2. **Define the format specification** — Formalize the ID format:
   - Format string: `{prefix}{minutes:07d}{random:05d}-{name}`
   - Prefix: `p` for phases, `t` for tasks, `d` for decisions
   - Minutes component: 7 digits, zero-padded, minutes since epoch
   - Random component: 5 digits, zero-padded, random integer 0–99999
   - Name: lowercase, hyphen-separated, no spaces
   - Full example: `p00525960123456-feedback-improvements`

3. **Create the constants file** — Write `LAAW/constants.py` with:
   - `EPOCH = datetime(2020, 1, 1, 0, 0, 0)` (UTC)
   - `MIN_WIDTH = 7`
   - `RANDOM_WIDTH = 5`
   - `MIN_MAX = 10**MIN_WIDTH` (10,000,000)
   - `RANDOM_MAX = 10**RANDOM_WIDTH` (100,000)
   - `FORMAT_STRING = "{prefix}{minutes:07d}{random:05d}-{name}"`
   - `PREFIX_MAP = {"phase": "p", "task": "t", "decision": "d"}`
   - Helper function `generate_id(prefix, name, random_seed=None)` that
     computes minutes since epoch, generates random component, returns
     formatted string.

4. **Create the ADR** — Write `.ai/decisions/adr08-id-format.md` using
   the template from `.ai/workflow/templates/adr-template.md` with:
   - Title: "Collision-safe ID format with timestamp + random component"
   - Context: Sequential IDs risk collisions in concurrent multi-team use
   - Decision: Adopt `{prefix}{minutes:07d}{random:05d}-{name}` format
   - Consequences: Lexicographic sort = chronological order; ~0.045%
     collision risk for 10 concurrent requests; 19-year lifespan from
     epoch

5. **Update decisions.md** — Add a row for ADR08 in
   `.ai/decisions/decisions.md`:
   | ADR08 | Collision-safe ID format with timestamp + random component | Adopt `{prefix}{minutes:07d}{random:05d}-{name}` format for phases, tasks, decisions | valid | — |

6. **Validate the constants file** — Run:
   ```bash
   cd LAAW && python3 -c "from constants import generate_id; print([generate_id('p', f'test-{i}') for i in range(5)])"
   ```
   Verify output follows the expected format with 7-digit minutes and
   5-digit random components.

### Dependencies

- Requires `.ai/workflow/templates/adr-template.md` to exist (check
  if it does; if not, note in the task that the ADR template needs to
  be created or use the template from the skill file).

### Expected result

- A constants file that any agent can import to generate IDs.
- An ADR documenting the decision for future reference.
- The decisions index updated with ADR08.

### Automatic validations

- Run `cd LAAW && python3 -c "from constants import generate_id; ids = [generate_id('p', f'test-{i}') for i in range(10)]; assert len(set(ids)) == len(ids), 'Collision detected'; print('All IDs unique'); print(ids[0])"` and verify it prints 10 unique IDs matching the format.
- Verify the constants file defines all required constants (`EPOCH`, `MIN_WIDTH`, `RANDOM_WIDTH`, `MIN_MAX`, `RANDOM_MAX`, `FORMAT_STRING`, `PREFIX_MAP`).
- Verify the ADR file exists and contains the required sections (Title, Context, Decision, Consequences).
- Verify the decisions.md row for ADR08 is present with correct description.

### Manual validations

- Does the epoch date feel appropriate (not too recent, not too old)?
- Does the format specification leave no ambiguity for agents?
- Is the ADR sufficiently detailed for future contributors?
