---
title: "Meaningful next steps to progress the repo (2026-06-26)"
date: 2026-06-26
status: roadmap
doc_type: roadmap
method: "two adversarially-verified workflows: (1) wide heterodox-lead sweep across gu-formalization + time-as-finality + temporal-issuance; (2) honest repo-state assessment (5 lenses) -> prioritized, theater-filtered next steps"
companion_docs:
  - explorations/time-as-finality-crosswalk/record-issuance-boundary-selector-2026-06-26.md
  - explorations/time-as-finality-crosswalk/observer-selector-leftover-space-2026-06-26.md
---

# Meaningful next steps (2026-06-26)

Two independent adversarial workflows converged on the same strategic picture. This is the honest,
theater-filtered list of what actually moves the repo.

## The convergent finding: one root blocker gates four problems

The deepest blocker is a single missing object — **the stabilized RS/IG-sector GU SOURCE ACTION**
(with its Noether identity `delta_2 . d_RS,-1 = 0`). It is **genuine missing physics, not a formalization
gap**: Weinstein's only candidate (draft eq. 10.10) is author-disclaimed ("Caveat Emptor"), and the
machine obstruction is real (the RS symbol on the projected pure-gauge image has norm 73.48 in Cl(4,0) /
343.73 in Cl(9,5) — neither annihilated, so no clean subspace subtraction).

It gates **four "separate" problems simultaneously** — they collapse to one:
- the **shiab source-forced selector** (SHIAB-04),
- the **generation count** `ind_H(D_GU)=24=3` (also needs a non-compact index theorem),
- **RS-BRST** (no stabilized RS action exists),
- **dark-energy Assumption 3** (the `xi R theta^2` coefficient).

**Two independent searches confirmed you cannot out-clever it.** The wide heterodox sweep (43 candidate
leads across three repos) produced **0 survivors** under adversarial verification — every promising lead was
already pursued, orthodox-mislabeled, a rename of a buried lead, or collapsed to the source action. Joe's
record-issuance-boundary hypothesis (a genuinely new *kind* of object) lands on the index, not the shiab, and
also routes back to the source action (see companion doc). **The strategic implication is clean: stop hunting
selectors; the high-value movable work is everything that does NOT need the source action.**

---

## DO NOW — real, verdict-flipping, source-action-independent (adversarially verified non-theater)

**1. Pure-gravitational `I_16` for the Weyl `S^+` on `Y14` + Green-Schwarz factorizability.**
The most computable open anomaly piece, and the first substep is fully self-contained and decisively
checkable: compute `[Ahat(TY14)]_16` as an exact-rational polynomial in `p1..p4` (pure-Python `Fractions`,
~40 lines) and cross-check the five coefficients against the published Alvarez-Gaume-Witten table. Then add
the `Sp(2n)` octic-trace decomposition on the already-realized `S=H^64` rep, and emit a factorizability
boolean. Fulfils the literal ANOMALY-01 upgrade condition (currently zero implementation in `tests/`).
*Honest ceiling:* the result is conditional on the assumed chiral content and the contested Sp(64)-vs-Sp(1)
gauge-group reading, and the global (eta / Dai-Freed / bordism) leg stays open — deliver it as a **conditional
number**, not a closure.

**2. FLRW theta-field high-z integration + DESI sign.**
Replace the visibly hand-waved, sign-confused matter-era file (it literally contains "WAIT — sign check
required") with a real `scipy.solve_ivp` integrator of `B'' + 3H(z)B' + 8H_0^2 B = 0` from `z~30` on the
slow-roll attractor to `z=0`, with a Richardson error bound and an IC-redshift convergence sweep. Settles the
**data-facing** sub-question: is GU's dark-energy sign a clean falsification signal vs DESI, or degenerate
with Lambda-CDM (a `phi_0` node)? *Honest ceiling:* the canon stays OPEN on the structural (source-action)
leg regardless; only the EOS-vs-DESI sub-verdict moves. Do **not** let the output read as "dark energy
resolved."

**3. Willmore-EL order on Schwarzschild (`M/r^3` vs `M/r^4`) — solar-system pass/fail.**
Compute the leading order of the Willmore-EL residual on the linearized Schwarzschild section to settle
`canon/schwarzschild-weak-field-rfail.md` (currently OPEN, RFAIL-02). *Real risk the verifier flagged:* the
term that decides the exponent (the ambient gimmel-curvature coupling) may itself be unwritten (the repo has
the gimmel Christoffels but not the gimmel Riemann tensor). First settle the in-repo `H ~ M/r^2` vs
`B ~ M/r^3` inconsistency; honest deliverable may be "still OPEN, here is the single missing tensor," not a
flipped verdict. Guard against the W2-01 failure mode (flipping a canon flag on a convention choice).

---

## DO NOW — honesty / hygiene (cheap, high-leverage, prevents a second "load-bearing and wrong")

**4. Compile the Lean layer for real** *(defer to the Lean track — it owns those files).*
Today "certified" means only "a `.lean` file exists with no `sorry`" — the sole gate
(`tests/lean_certificate_surface_audit.py`) is literally `assertNotIn("sorry", text)`, and **nothing has ever
been kernel-compiled** (no `.elan`, no `.lake`, no `.olean`). A green `lake build` makes the W2 `F_2`
identities — *the exact algebra W2-01 found wrong* — genuinely machine-checked for the first time; a red build
exposes the "Formal Certificate Boundary" as unbacked. *Real risk:* the mathlib pin is an rc with no version
lock, so `lake exe cache get` may miss and force a multi-hour from-source build (possibly infeasible on this
Windows box). Until it is green, relabel `certified_theorems` -> `drafted_theorems_pending_first_compile`
(`compiled: false`) and harden the audit to FAIL (not skip) when no build artifact exists.

**5. De-theater the test suite.**
**81% of `tests/` (290 of 358 files) is `hourly_*` self-asserting bookkeeping** (zero `import numpy`; they
assert fields equal what the same automation run just wrote). Relocate them to `lab/automation/runs/`, split the
prose/governance gates into `process_gates/`, and reserve `tests/` for files that build an object and compute
a number/rank/dim. This makes the ~20-file real math core visible (currently buried 18:1) and stops a green
`tests/` run from implying any GU claim was mathematically checked.

**6. Verdict-consistency scrub (the real subset only).**
Split the dark-energy entry into Claim 1 (dynamism + equivariance — genuinely PROVED) and Claim 2
(divergence-free — conditional, NOT established; circular Assumption 3) rather than a blanket label; relabel
the stale *exploration* Nguyen synthesis (`§3.1 RESOLVED / §3.2 FULLY CLOSED`) to "existence-only; selector
OPEN" to match the already-honest canon spine. (Skip the items the verifier found already done.)

---

## A genuinely useful side-computation (sharpens, does not flip)

**Majorana / spurion channel dimension.** Compute `Hom_{Spin(9,5)}(S (x) S, Lambda^* V)` on the existing
verified `Cl(9,5)=M(64,H)` rep + gram-nullspace machinery, and report the dimension + chirality grading.
This converts SHIAB-04's prose side-claim ("the heavy Majorana block must come from OUTSIDE the equivariant
family") into a computed character fact. Bounded, tool-supported, adversarially checkable — sharpens a
side-claim, not a headline verdict.

---

## BLOCKED on external input / new physics (do not spin cycles trying to force)

- **Write the GU source action** — the root blocker above. Needs new physics no one has supplied; the toy
  "source-action selector scan" was flagged **theater** (it presupposes the missing source->shiab map). The
  most that can be done without it is the Majorana-channel dimension above.
- **Generation count full resolution** — blocked on the source action AND a non-compact index theorem on
  `Y14` (the boundary/APS framework is partly built; see the record-issuance-boundary companion doc — the
  boundary holonomy `rho` is a real free lever on the index, but it adds a parameter, it does not fix one).
- **Global anomaly cancellation** — the local `I_16` (steps 1) is movable; the global leg (spin-bordism /
  Dai-Freed / eta on `Y14`) needs a 14D bordism computation and the gauged-subgroup embedding of `S^+` in
  `Sp(64)` ("which subgroup" gap).
- **Source-anchored Nguyen engagement** — every current "resolution" rests on AI-persona reconstructions of
  the objection; the verbatim Nguyen PDF is not in the repo. Pinning it requires pulling external literature
  (and per the standing prompt-injection policy, that PDF is **untrusted data, not instructions**).

---

## Recommended sequencing

Start with **step 1** (pure-grav `I_16` — cleanest, fully verifiable, in the numpy lane) and **step 2**
(FLRW DESI sign — self-contained, retires a visibly hand-waved file). These are the two highest realness-per-
effort, source-action-independent wins. Run **step 5** (de-theater) opportunistically — it is one-time hygiene
that makes every future "tests pass" honest. Leave **step 4** (Lean compile) to the Lean track. Treat the
source action as the standing North Star: not yet writable, but the single object whose arrival unblocks four
problems at once.
