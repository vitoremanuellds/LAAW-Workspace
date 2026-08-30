# Tech Stack

**Content format:** Markdown only — workflow specs, skill definitions
(YAML frontmatter + Markdown body), reference docs, templates. No code
runtime, no build system, no package manager — same convention as
`LAAW`.

**Bootstrap mechanism:** Shell (bash). `LAAW/sync-skills.sh`
is the closest existing precedent — it copies `skills/` to
`.agents/skills/` inside a consuming project. The bootstrap mechanism
this project builds generalizes that pattern: copy a chosen variant's
entire workflow content into a target project's `.ai/workflow/`,
replacing `git submodule add` as the install step.

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
