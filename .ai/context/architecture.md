# Project Architecture

LAAW-Workspace is a meta-project with a **submodule-based architecture**.
The actual workflow lives inside a git submodule; this repo is the
development/iteration workspace around it.

## Directory structure

```
LAAW-Workspace/
├── README.md              ← Project overview, organization guide
├── AGENTS.md              ← Agent entry point
├── .gitignore             ← Gitignore (ignores .ai/workbench/, .agents/skills/)
├── .gitmodules            ← Submodule config: LAAW/ → vitoremanuellds/LAAW.git
├── LAAW/                  ← Git submodule: the LAAW workflow source
│   ├── README.md          ← User-facing documentation for LAAW
│   ├── workflow.md        ← The full workflow spec (self-contained)
│   ├── sync-skills.sh     ← Copies skills/ to .agents/skills/ in a project
│   ├── sync-workflow.sh   ← Installs/re-syncs workflow into .ai/workflow/
│   ├── reference/         ← Occasional-need detail docs
│   ├── templates/         ← First-run scaffolding templates
│   └── skills/            ← One SKILL.md per operation
├── .ai/                   ← Project management (constitution, phases, tasks, etc.)
│   ├── info.md            ← Policy: gate authority
│   ├── constitution/      ← Mission, techstack
│   ├── context/           ← Context files
│   ├── decisions/         ← ADRs
│   ├── phases/            ← Phases (P01–P06)
│   ├── tasks/             ← Tasks (phase-linked + orphans)
│   ├── workbench/         ← Freeform scratch (gitignored)
│   └── workflow-version   ← Generated: source, commit SHA, date
└── .agents/skills/        ← Generated copy of LAAW/skills/ (gitignored)
```

## Key relationships

- **`LAAW/`** is the source of truth for workflow content. It's a git
  submodule pointing to `https://github.com/vitoremanuellds/LAAW.git`.
  All real content changes happen in `LAAW/`'s own checkout.

- **`.agents/skills/`** is a generated copy of `LAAW/skills/`, created
  by `LAAW/sync-skills.sh`. It's for harnesses that auto-discover skills
  from `.agents/skills/` rather than following `workflow.md`'s lookup
  table. Added/updated on sync, never deleted automatically.

- **`.ai/workbench/`** is gitignored — freeform scratch space,
  disposable, not part of the permanent record.

- **`.ai/workflow/`** is a plain copy from a `LAAW` checkout, managed
  by `LAAW/sync-workflow.sh`. Read-only here; never hand-edited.

## Tech stack

- **Content format:** Markdown only — workflow specs, skill definitions
  (YAML frontmatter + Markdown body), reference docs, templates. No code
  runtime, no build system, no package manager.
- **Bootstrap mechanism:** Shell (bash). `LAAW/sync-skills.sh` copies
  `skills/` to `.agents/skills/`; `LAAW/sync-workflow.sh` copies the
  workflow into a target project's `.ai/workflow/`.
- **Versioning:** Git submodule for `LAAW/`; `sync-workflow.sh` also
  writes a `.ai/workflow-version` file with source URL, commit SHA, and
  date.
