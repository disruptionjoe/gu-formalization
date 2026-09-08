---
title: "The Observerse Research Program (advanced from Geometric Unity formalization)"
status: canon
doc_type: overview
updated_at: "2026-09-08"
---

# The Observerse Research Program

*This program began as a formalization of Geometric Unity (GU) and has advanced beyond it. Current framing:
`RESEARCH-PROGRAM.md`. Lead result: [*Located, Not Forced* v1.0.0](https://doi.org/10.5281/zenodo.21515143),
published on Zenodo from `papers/candidates/located-not-forced/`.*

## If you are here from the paper

For readers arriving from "A Diagonal No-Go for Self-Valuations and an Invariance Classification":

- **Lean proof:** `Lean/GUFormalization/ResidualSelection.lean`. Kernel-check it from the repository root with
  `lake env lean Lean/GUFormalization/ResidualSelection.lean` (toolchain pinned in `lean-toolchain`).
- **Finite-instance confirmations:** `tests/W70_path5_D_lawvere.py`, `tests/W73_H62_arena_value_partition.py`,
  and `tests/W99_theorem_finite_instances.py` (run each with `python <file>`).
- **Claim-level honesty map:** `VERIFICATION.md`.
- **Paper source:** `papers/published/observer-value-selection-theorem/` (published on Zenodo; the
  previously listed `papers/candidates/observer-value-selection-theorem/submission/` path no longer exists).

## How this repository is produced

This repository is produced by AI agents (Claude- and Codex-class) operating under a single human
director (Joe / Joseph Hernandez). Agents perform the construction, computation, certification, and
canon promotion; the human sets research direction, ratifies governance changes, and owns all
external actions (publication, licensing, distribution). Scientific verdict changes additionally
require a hostile adversarial review by field-relevant specialist agents. All verification reported
here is internal-tier — reproduced and adversarially reviewed within the same AI-directed process
that produced it — unless explicitly marked otherwise. See `VERIFICATION.md` for the claim-level
honesty map.

One caution: this is a large, active research repository. The paper is self-contained and does not depend on
the rest of it.

This program studies a **class of geometry** — the Clifford-Rarita-Schwinger /
chimeric-bundle *observerse* — as a candidate for the shape of physics.
*Located, Not Forced* establishes structural results under its declared
carrier and operator assumptions. The finite antilinear theorem concerns
`intersectionDifference` on a supplied carrier; identifying that carrier with
physical generations and transferring the result to the physical real form
remain separate obligations. See the scope corrections in
`canon/antilinear-bound-RESULTS.md` and the claim-level `VERIFICATION.md`.
These results do not settle the source's distinct `2+1`, graded-IG or observed
chirality mechanisms (SC-GEN-02/03/54; SC-CHI-01/51).

The working question is larger than whether bare GU kinematics forces the
integer three. It is whether this geometry gives a more constrained, unifying
account of the structures we already know. The program's conditional working
model relates classical gravity and quantum matter with chirality/generation
selection entering through additional physical or boundary data. That is a
research hypothesis, not a proved necessity for every source-native mechanism.
See `RESEARCH-PROGRAM.md`, read with the current source and physics caveats below.

This repository optimizes for finding the truth, using Geometric Unity as the generative test case that pointed
here, not as a thesis to defend. GU is a bold, high-information, contested conjecture: the kind of aggressive claim
that, when it pays off, moves science in leaps rather than increments. That makes it an excellent engine
for spawning precise falsifiable hypotheses, which we drive to resolution, keeping only what survives.

The product is true structure (often GU-independent) reported at honest grade, plus a reliable
truth-seeking method. It is not a proof of Geometric Unity, and not an attempt to prove GU true or false,
to vindicate or refute Eric Weinstein, or to make the program look right. The posture is constructive and
verdict-agnostic, while preserving explicit assumptions, rollback conditions, correction logs, no-go
assumption audits, and proof-grade labels. See `RESEARCH-POSTURE.md`.

## Purpose (charter, sharpened 2026-07-21)

This repository exists to establish the **honest truth-status** of the observerse / Geometric Unity
program — force it, falsify it, or place it precisely — and to determine what it would take for this class
of geometry to be the true account of physics. GU is the generative engine, not a thesis to defend; the
product is true structure at honest grade plus a reliable truth-seeking method.

**Current evidential footing (reconciled 2026-09-08).** Keep the source's
claims separate from the repository's conditional constructions. Read
`lab/sources/source-claim-register.yaml` for source identity and polarity;
resolve the current physics ledger through `standing_ledger.ref` and
`human_ref` in `lab/methods/research-evidence-contract-v1.0.json`. Source
adherence is not physical verification, and mapped requirements or SAME rows
are not independent confirmations. Read each row's mapping grade, assumptions,
remaining freedom and evidence, together with later conditional results.

The distinctive questions remain open: two true plus one effective family
(SC-GEN-02/03/51/53/54), observed chirality from a non-chiral total theory
(SC-CHI-01/51), physical positivity despite indefinite geometry (SC-META-53),
and gravity/cosmology from the geometric action and connection distortion
(SC-ACT-01/02; SC-COS-50/51/54). Preserving those questions does not certify
their proposed mechanisms. Representation identities, observation maps,
action equations, physical states and observables require their own bridges.

**Testability.** A specified realization can fail a mathematical consistency
condition or an empirical requirement. Freeze its assumptions and identify
which registered source claim or internal construction the test addresses.
The useful unification question is whether one compatible construction meets
several independent constraints without refitting, and what that common
construction excludes. Conditional matches on different forks are not yet
such a result. Missing action closure does not block conditional reverse-scaffold research
from observed phenomena back to requirements on a future action; it limits
forward derivation and prediction credit.

**Correction to the July overview.** The earlier two-input summary (σ and τ)
and illustrative factor-of-2–3 arena preference are historical conditional
arguments, not a current parameter inventory or calibrated empirical odds.
The live physics ledger records additional unresolved choices and functional
freedom. Nor is no phantom crossing, `w(z) ≥ −1`, currently a derived GU
prediction: LT-GR2d/e retain the sign, magnitude and cosmological-export
burdens. The later conditional result in
`papers/drafts/sigma-dark-energy-sign-nonselection/CLAIM-AND-PREMISE-LEDGER.json`
shows that, with a separately supplied total, nonzero, odd physical sign
bridge, the image across the two σ orientations contains both signs. It supplies neither that bridge
nor a physical orientation selector. Preserve the connection/VEV dark-energy
hypothesis (SC-COS-50/51/54), while withholding the older claim that one
no-phantom measurement settles GU. The July analyses remain available as
historical evidence in `explorations/per-leg-recovery-state-2026-07-21.md` and
`explorations/parsimony-unexplained-joints-ledger-2026-07-21.md`.

## Start Here

Follow `AGENTS.md` and its object/source-routing prerequisites first. For a
compact entry view, run `python3 scripts/research_context.py` after installing
`requirements.txt`. It reads the current question, method ceiling, lead
continuation, and first verification section directly from the existing
files. The view is partial and does not select work: read the full relevant
state, source rules, and exact evidence before choosing or reusing a result.

- **Source claims and attribution:** `lab/sources/source-claim-register.yaml`
- **Current physics recovery/compatibility ledger:** follow `standing_ledger.ref`
  and `human_ref` in `lab/methods/research-evidence-contract-v1.0.json`; use the
  referenced ledger's current accounting and complete row caveats.
- **Current branch-relative state:** `CURRENT-STATE.yaml`
- **Research program (current framing):** `RESEARCH-PROGRAM.md`
- **Reverse-search / forward-certification method contract:**
  `lab/process/reverse-scaffold-method-contract.json`
- **Lead result (published preprint):** `papers/candidates/located-not-forced/`
  ([DOI `10.5281/zenodo.21515143`](https://doi.org/10.5281/zenodo.21515143))
- **Research posture (truth-seeking method):** `RESEARCH-POSTURE.md`
- **Grade and status crosswalk:** `GRADES.md`
- **Project canon:** `CANON.md`
- **Dated research-status chronology:** `RESEARCH-STATUS.md`
- **Tri-repo division of labor (GU leg: boundary content):** `lab/roadmap/tri-repo-division-of-labor-2026-07-02.md`
- **Contributor next steps:** `NEXT-STEPS.md`
- **High-level overview:** `docs/OVERVIEW.md`
- **Six-axis testability white paper:** `papers/candidates/six-axis-testability/`

## Repository Layers

The root is deliberately small. Five things matter at the top level:

- `papers/` — the publication lifecycle: `drafts/` (WIP) -> `candidates/` (staged) -> `published/` (posted).
  The lead result is `papers/candidates/located-not-forced/`.
- `canon/` — the stable project spine: claims safe to cite as the current public framing.
- `tests/` — computational checks; each maps to a claim (see `tests/README.md`). The paper's load-bearing
  files are in `tests/generation-sector/`.
- `explorations/` — the full research lab, grouped into topical subfolders (see `explorations/README.md`).
- `docs/` — second-tier program docs (overview, frontier hypotheses, GU-status deep-dive).

Everything else -- active research, roadmap, process history, deep-research briefs, literature, sources,
specifications, automation, and the archive -- lives under `lab/` (see `lab/README.md`). `Lean/` holds the
Lean formalization scaffold.

## Current Center Of Gravity

The strongest current public posture is:

1. Use GU as the generative engine and candidate unifying fit: take the bold conjecture seriously enough to
   spawn precise falsifiable hypotheses, drive each to a verdict, and reconstruct the missing mathematics
   where that advances a hypothesis.
2. Treat no-go theorems as class-relative until their exact assumptions cover the branch being tested.
3. Require every proposed path to carry explicit assumptions, proof/reconstruction labels, failure
   conditions, and source-to-shadow provenance.
4. Treat the GU-independent results (signed-readout, no-go class-relativity, six-axis specification, the
   generation-multiplicity rep theory) as co-equal products: often the strongest, because they do not
   require anyone to buy GU.
5. Optimize research priority for information gain about what is true, including whether GU supplies a better
   unifying story than competing accounts. Do not collapse that question into the narrower test "does bare GU
   force three generations?"

## Contributing

Start with `RESEARCH-POSTURE.md` and `NEXT-STEPS.md`. The best contributions are
constructive, falsifiable, scoped, and explicit about which GU reconstruction claim they
advance, block, or kill.

## First-Class Lanes

Load root `lab/process/RESEARCH-AGENDA.json` after this repository's governance and before selecting
work. It is the owner-authoritative source for durable Lane definitions,
admission, and normal control state; authoritative work remains at the paths it
references. Numbered Lanes are Progress, lettered Lanes are Stewardship, and
Discovery is Lane-less. A direct mount uses these local surfaces without
private orchestration overlay. System observations, health, schedules, and execution history are
not Lane truth.
