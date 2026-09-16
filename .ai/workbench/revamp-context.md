# LAAW Revamp — Core Ideas

Context for the full revamp of LAAW. This captures *what LAAW is and
why* — the abstract ideas, mission, and concepts — deliberately **not**
the current project's structure, naming, or layout. The revamp is free
to redesign how these ideas are realized.



<!-- TOC -->
<details><summary>Table of Contents</summary>

  - [Mission](#mission)
  - [The problem it solves](#the-problem-it-solves)
  - [Core ideas](#core-ideas)
  - [Design values (implicit in everything above)](#design-values-implicit-in-everything-above)

</details>
## Mission

A file-based workflow for developing software with AI coding agents,
designed around its hardest constraint: **small local models with tight
context windows**. The same discipline should hold up on frontier
models with more slack, but it is shaped by the weak end, not the
strong.

## The problem it solves

As models get smaller or context gets tighter, four failure modes get
worse, and LAAW exists to counter each:

1. **Hallucination** — agents invent steps or context when they lose
   track.
2. **Wasted context** — reading everything "just in case" fills the
   window.
3. **Loss of human control** — agents push past gates or make scope
   decisions they weren't authorized to make.
4. **Unsafe parallel work** — multiple agents overwrite each other.

## Core ideas

- **Persist knowledge, not reasoning.** Project knowledge lives in
  small linked text files. Agents reconstruct nothing that can be
  stored cheaply; files carry facts, not conversation.
- **Read only what the current task needs.** No agent reads the whole
  knowledge tree to do bounded work — it enters at the smallest unit
  defining its task and follows links as far as needed.
- **Separate *what happens* from *who decides*.** The process is
  fixed and never changes per project; the policy (who is authorized
  for each gate, and in what mode) is a separate, small, per-project
  decision that can loosen as trust grows without touching the
  process.
- **Gates, not freeform flow.** Work advances through explicit gates
  that block *advancing past* a step — never *producing* it. Completion
  always means two distinct checks: mechanical validation (does it meet
  requirements) and judgment review (is it appropriate and coherent).
  They are never merged or skipped silently.
- **Deviations are first-class, and are decisions.** When work diverges
  from an approved plan, that is a named, recorded state with its own
  lifecycle and owner — not a silent drift. The deviation itself is
  captured *as a decision*: what changed, why, and the approach taken.
  There is no separate deviation artifact; the decision is the durable
  trace, and the plan is replanned to match it.
- **Deliberate decisions leave durable traces (ADRs).** A decision
  written when made, by whoever owned the scope — and superseding
  rather than deleting its predecessor. A deviation's decision
  supersedes the plan it deviated from.
- **Context flows upward, deliberately.** Facts earned in fine-grained
  work are evaluated for promotion to coarser levels only at
  completion boundaries — never written sideways or scattered.
- **Status lives in exactly one place per fact.** The permanent record
  answers "what is active" without cross-checking multiple files.
- **One workflow, scaled by axes — not variants.** Weight scales
  through independent choices, not separately-maintained profile
  forks: *presence* (most layers are optional, inferred from what
  exists rather than declared), *granularity* (work units opt into
  larger planning structures individually), *locality* (one in-repo
  tree; a project keeps whatever layers out of version control it
  chooses). Presets are projections of one design, never parallel
  codebases.
- **Free, disposable scratch space.** A workbench exists where
  human and agent can think together outside the permanent record,
  with no schema and no obligation that anything in it survives.
- **Easy in, easy out.** The workflow installs into a project by plain
  file copy — no special version-control machinery — and re-syncing is
  a reviewed, whole-content replacement, leaving the project's own
  files untouched.

## Design values (implicit in everything above)

- Weak-model ergonomics: explicit, repeated, fresh reads over memory;
  small self-contained units over one giant document.
- Boring and auditable: every fact, decision, and status has exactly
  one owner.
- Opt-in complexity: the minimal case must stay genuinely minimal;
  heavier structure is earned, not required.
- Change is planned: replanning is a supported path, not an
  emergency.
