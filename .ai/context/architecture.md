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

## LAAW workflow structure

The workflow (`LAAW/workflow.md`) is organized into 12 sections:

1. **Principles** — persist knowledge not reasoning, read only what's needed
2. **Starting point** — read `info.md` at every gate, read skill file every time
3. **Directory structure** — `.ai/workflow/` (read-only), `.ai/info.md`, optional layers, tasks (mandatory)
4. **Artifact hierarchy** — Constitution → Context → Decisions → Phases → Tasks
5. **Lifecycle & gates** — gates for missing layers are skipped; modes: manual, assisted (default), autonomous, delegated
6. **Deviations** — recorded inline in task files; lifecycle: OPEN → ADDRESSED → INCORPORATED
7. **Decisions (ADRs)** — written by the owner at the moment of decision
8. **Validation vs Review** — two distinct checks at completion-review
9. **Context propagation** — task → phase Context → phase completion → promote to context/
10. **Operation contracts** — authority always from `info.md`
11. **Status** — the permanent record; `not-planned → awaiting-plan-review → plan-approved → in-progress → validating → reviewing → complete`
12. **Commit discipline** — commit each draft immediately before requesting review

**Path conventions:** All paths are `.ai/`-prefixed, never bare or dot-relative. Cross-references are `.ai/workflow/`-anchored. This prevents silent resolution bugs when files are copied to different depths (e.g., via `sync-skills.sh` to `.agents/skills/`).

## Skills overview

LAAW ships 9 skills under `LAAW/skills/`, each with YAML frontmatter (`name` + `description`) and a Markdown body:

| Skill | Operation | Purpose |
|---|---|---|
| `bootstrap` | Layer setup | Ask which optional layers to enable; delegates to each layer's scaffold-on-first-use; always ensures `.ai/info.md` exists first |
| `create-constitution` | Constitution | Create/update `mission.md` + `techstack.md`; bootstraps `.ai/info.md` on first run |
| `define-phase` | Phase planning | Define new phase or replan after deviation; writes Context+Requirements+Plan+Validations |
| `define-task` | Task planning | Break phase plan into tasks (phase-linked or orphan); writes enough detail for implementation |
| `implement-task` | Implementation | Write/modify/delete project code for approved task |
| `validate-work` | Validation | Run task/phase validation (mechanical checks) before review |
| `review-work` | Review | Check implementation for scope, complexity, architecture issues (judgment) |
| `propagate-context` | Context propagation | Propagate reusable knowledge into `context/` after task/phase completes |
| `build-context` | Context survey | Populate `context/` by surveying existing codebase (assess → plan → iterate) |

**Skill contract pattern:** Each skill states its own Can/Must/Cannot contract right after its frontmatter. Authority always comes from `.ai/info.md`, never self-assigned.

**Skill files in `.agents/skills/`:** `sync-skills.sh` mirrors `LAAW/skills/` to `.agents/skills/` for harnesses that auto-discover skills from that directory. Cross-references use `.ai/workflow/`-anchored paths to survive this depth change.
