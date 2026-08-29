# Tech Stack

**Content format:** Markdown only — workflow specs, skill definitions
(YAML frontmatter + Markdown body), reference docs, templates. No code
runtime, no build system, no package manager — same convention as
`Full-Local-Model-Agent-Workflow`.

**Bootstrap mechanism:** Shell (bash). `Full-Local-Model-Agent-Workflow/sync-skills.sh`
is the closest existing precedent — it copies `skills/` to
`.agents/skills/` inside a consuming project. The bootstrap mechanism
this project builds generalizes that pattern: copy a chosen variant's
entire workflow content into a target project's `.ai/workflow/`,
replacing `git submodule add` as the install step.

**Versioning:** Git, one repo per variant — `full`'s existing repo
(`Full-Local-Model-Agent-Workflow/`, kept as a git submodule of this
one, since it's this project's actual development checkout, not a
bootstrapped consumer copy) is the pattern any new lighter variant
repo follows. This repo's own `.ai/workflow/`, bootstrapped today, is
itself a plain copy — proof of the target mechanism, not a submodule.

**Target constraint carried over from `full`:** every variant's own
`workflow.md` (and whatever it reads per operation) must stay usable
inside a small local model's context window (7B–35B, 48k–64k, per
`full`'s own design target) — a "lighter" variant should need *less*
of that budget than `full`, not the same amount reorganized.
