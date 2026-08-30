# Tech Stack

**Content format:** Markdown only — workflow specs, skill definitions
(YAML frontmatter + Markdown body), reference docs, templates. No code
runtime, no build system, no package manager — same convention as
`LAAW`.

**Bootstrap mechanism:** Shell (bash). `LAAW/sync-skills.sh`
was the closest existing precedent — it copies `skills/` to
`.agents/skills/` inside a consuming project.
[P02](../phases/p02-non-submodule-bootstrap-mechanism.md) generalized
that pattern into `LAAW/sync-workflow.sh`: it copies
the workflow's content (`workflow.md`, `skills/`, `templates/`,
`reference/`, `README.md`) wholesale into a target project's
`.ai/workflow/`, replacing `git submodule add`/`git submodule update
--remote` as the install/update step. There's no "chosen variant" to
select — ADR03 already collapsed that into one workflow, so the script
always installs it wholesale. Every run also writes a version-stamp
file beside `.ai/workflow/` (see
[ADR04](../decisions/adr04-workflow-version-stamp.md)).

**Versioning:** Git, one repo for the workflow itself —
`LAAW/` (kept as a git submodule of this
one, since it's this project's actual development checkout, not a
bootstrapped consumer copy) holds the single modular workflow's actual
content, per
[`adr03-single-modular-workflow.md`](../decisions/adr03-single-modular-workflow.md).
There is no per-variant repo to keep in sync anymore — weight is a
function of which optional layers a consuming project turns on, not of
which repo it bootstrapped from. This repo's own `.ai/workflow/`,
bootstrapped today, is itself a plain copy — proof of the target
mechanism, not a submodule.

**Target constraint carried over from `full`:** every variant's own
`workflow.md` (and whatever it reads per operation) must stay usable
inside a small local model's context window (7B–35B, 48k–64k, per
`full`'s own design target) — a "lighter" variant should need *less*
of that budget than `full`, not the same amount reorganized.
