---
title: "The Observerse Research Program (advanced from Geometric Unity formalization)"
status: canon
doc_type: overview
updated_at: "2026-07-21"
---

# The Observerse Research Program

*This program began as a formalization of Geometric Unity (GU) and has advanced beyond it. Current framing:
`RESEARCH-PROGRAM.md`. Lead result (submission candidate, not yet posted):
`papers/candidates/located-not-forced/`.*

## If you are here from the paper

For readers arriving from "A Diagonal No-Go for Self-Valuations and an Invariance Classification":

- **Lean proof:** `Lean/GUFormalization/ResidualSelection.lean`. Kernel-check it from the repository root with
  `lake env lean Lean/GUFormalization/ResidualSelection.lean` (toolchain pinned in `lean-toolchain`).
- **Finite-instance confirmations:** `tests/W70_path5_D_lawvere.py`, `tests/W73_H62_arena_value_partition.py`,
  and `tests/W99_theorem_finite_instances.py` (run each with `python <file>`).
- **Claim-level honesty map:** `VERIFICATION.md`.
- **Paper source:** `papers/candidates/observer-value-selection-theorem/submission/`.

One caution: this is a large, active research repository. The paper is self-contained and does not depend on
the rest of it.

This program studies a **class of geometry** -- the Clifford-Rarita-Schwinger / chimeric-bundle *observerse* --
as a candidate for the shape of physics. Its established result is a **class-level structural law**: this class
of matter geometry is intrinsically vectorlike and cannot force its own chirality or generation count from
inside (the linear leg is theorem-grade; the antilinear escape is a finite adversarial hunt with no
counterexample found, not yet a closed proof), so on present evidence the count is **external** -- entering as
chirality does in the Standard Model (chiral gauge couplings, instantons, K3 / Calabi-Yau).

That result is not a verdict that GU "does not work." The working question is larger than whether bare GU
kinematics forces the integer three. It is whether GU gives the best, most compressed, most unifying account
of the structures we already know, with the generation count entering as a constrained physical selection
datum rather than as arbitrary numerology. The guiding hypothesis (the program's bet, not yet a result) is that
this class connects the **classical** (general relativity) and the **quantum** (Standard Model), with chirality
as external boundary data; the frontier is **what lies outside the observer universe.** See
`RESEARCH-PROGRAM.md`.

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

**The standard, made precise.** A theory whose subject matter includes the observer's own orientation
cannot, from inside, *derive* the one datum that selects which world it is in — here that is a result, not a
posture: the sector bit is Gödel-independent / oracle-relative, and the program's summit operator provably
does not close from structure without it (the excision that would evade this is anomaly-protected, i.e.
forbidden — proposal grade). So "the program must natively *force* all of physics" is the wrong bar; it
demands the one thing the structure forbids. This class is a **model-schema**, and the external data select
the model. It is therefore held to the standards that actually apply to non-derivable truth:

- **Refutation-survival** — it must survive every kill test we can build. The live one is the dark-energy
  sign (no phantom crossing, `w(z) ≥ −1`), at DESI/Euclid; that prediction is both the external kill test and
  the license for the abduction.
- **Best-arena abduction** — it wins to the degree it leaves the **fewest joints unexplained** and imports
  the **fewest independent knobs** versus stated rivals (SM+QM+GR, ΛCDM+SM, modified gravity) at equal
  empirical coverage — the question this README already refuses to collapse into "does bare GU force three."
  Maintained as an explicit, fair **parsimony ledger**, with wired joints marked *observable* (evidence) vs
  *internal-only* (unification, not yet evidence).

**The irreducible external ledger.** Exactly two data enter from outside: **σ** — one Z/2, the
orientation / time-reversal bit (the spin-cover deck class `w₁`) that fixes the dark-energy sign and the
boundary — and **τ** — one Z/3, which locates the three generations. Both are provably unreadable and
unmintable from inside; the program is complete *modulo* them, never without them. (σ's cardinality = one bit
and its anomaly-protection are proposal grade; the DE-sign prediction is the load-bearing falsifiable.)

**Honest current standing.** Given σ and τ supplied, the construction *hosts* most of physics at
consistency-to-hosting grade and *forces* the dark-energy sign; on the unexplained-joints ledger it is the
better arena than the rivals, but **modestly** (a factor of ~2–3, not orders of magnitude), and native
recovery is gated on one blocked source-action spine. It does not yet *force* physics, and the bit is
imported, not earned — and by the standard above, that is the correct posture, not a deficiency. The
dark-energy no-phantom-crossing measurement is the one observation that turns the modest lean into a verdict.
(Consolidates the 2026-07-21 results: `explorations/lp-lc-deficiency-decisive-…`, `pin-bordism-cardinality-…`,
`per-leg-recovery-state-…`, `parsimony-unexplained-joints-ledger-…`, `council-reframe-arena-abduction-…`.)

## Start Here

- **Research program (current framing):** `RESEARCH-PROGRAM.md`
- **Lead result (submission candidate):** `papers/candidates/located-not-forced/` ("Located, Not Forced")
- **Research posture (truth-seeking method):** `RESEARCH-POSTURE.md`
- **Project canon:** `CANON.md`
- **Current research status:** `RESEARCH-STATUS.md`
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

Load root `LANES.yaml` after this repository's governance and before selecting
work. It is the owner-authoritative source for durable Lane definitions,
admission, and normal control state; authoritative work remains at the paths it
references. Numbered Lanes are Progress, lettered Lanes are Stewardship, and
Discovery is Lane-less. A direct mount uses these local surfaces without
CapacityOS. System observations, health, schedules, and execution history are
not Lane truth.
