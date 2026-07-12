---
title: "H48 -- The self-dual-square forcing test (the coherence route)"
status: exploration
doc_type: research_note
wave: 27
updated_at: "2026-07-11"
verdict: "PARTIAL, leaning RELABELS -- removes 0 of 4 unforced choices unconditionally, <=1 conditional; source-action postulate stays a postulate"
test: "tests/wave27/H48_self_dual_square_forcing.py (deterministic, exit 0)"
depends_on:
  - "explorations/two-track-persona-sweep-2026-07-11/SYNTHESIS.md"
  - "explorations/two-track-persona-sweep-2026-07-11/B-geometric-structural.md"
  - "explorations/two-track-persona-sweep-2026-07-11/D-wild-frontier.md"
  - "tests/wave24/H45_H2_vs_II2_binary.py"
  - "tests/wave26/H20_unified_even_odd_action.py"
  - "tests/wave16/H39_sourceaction_kclass.py"
  - "tests/wave17/H40_terminal_sourceaction.py"
  - "tests/wave1/H1_bach_flat_exact_vacua.py"
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
---

# H48 -- The self-dual-square forcing test

## The object under test

The full-roster persona sweep (families B geometric + D wild-frontier) converged on ONE genuinely
new forcing candidate: the GU source action may be FORCED as the **self-dual square**, with two
claimed faces of a single principle.

- **(B) Willmore/GJMS uniqueness.** The source action is the UNIQUE conformally-invariant
  Willmore/GJMS functional of the soldering distortion `II_s` (= moment-map norm-square = spectral
  action), pinned up to scale by `{conformal-weight + IG-invariance + derivative-order = 4}`.
- **(D) self-dual L-infinity/BV double copy.** The source action is the double copy of a first-order
  self-dual gauge datum on `Lambda^2_+` (dim 3), whose color-kinematics (kinematic-Jacobi) constraint
  should close ONLY on carrier B's gamma-trace-constrained field space (index-changing, order-3
  `rho=(0,2,1)`, Wave 16).

If it FORCES, the source-action POSTULATE becomes a THEOREM and `{count, norm, K-class}` collapse to
one. The HONEST failure mode is the same as H20: **RELABELS** (removes 0 of the 4 unforced choices).
This test guards hard against cosmetic unification: a forcing claim MUST exhibit a reduction in the
count of independent unforced choices `{signature, |II|^2 norm P2, soldering, K-class SG4}`.

Grounded in Weinstein's "2nd order = square of 1st order" and the machine-checked `box^2 = -4 Bach`.
Test: `tests/wave27/H48_self_dual_square_forcing.py`, deterministic, exit 0.

---

## The four verdicts

### Q1 -- UNIQUENESS (B): 1-dimensional, YES (but conditional and target-revising) [COMPUTED]

- **COEFFICIENT count = 2.** The pointwise IG (`O(4) x O(codim)`)-invariant quadratic functionals of
  the soldering distortion are exactly the two contractions of `Sym^2`: `|II|^2` (full, rank-10 form)
  and `|H|^2` (trace-square, rank-1 form). `Sym^2(R^4) = trace(1) (+) traceless(9)` under `O(4)`, so
  there are exactly two invariant quadratic forms. COMPUTED (rank 10 vs rank 1).
- **CONSTRAINT count = 1.** Conformal-weight covariance forces the traceless combination: the trace
  part `H` acquires an inhomogeneous shift under `g -> e^{2w}g` while the traceless `II_0` is
  covariant, so a conformally covariant density must be proportional to
  `|II_0|^2 = |II|^2 - (1/4)|H|^2` (the single linear condition `beta = -(1/4) alpha`). COMPUTED.
- **dim admissible = 2 - 1 = 1.** UNIQUENESS HOLDS -- the functional is forced up to scale. This is a
  genuine forcing structure, the same universal property that forces Bach as the unique conformal
  4-derivative curvature functional.

**Two honest caveats that deflate "forcing" to "conditional, target-revising":**
- (a) The forced element is the TRACELESS conformal `|II_0|^2`, NOT GU's full `|II|^2`. They differ by
  `(1/4)|H|^2` -- the Einstein/trace mode. Conformal uniqueness picks the pure-Bach (conformal) branch,
  which REVISES rather than confirms H45's `|II|^2` (Stelle) favored lean. [COMPUTED]
- (b) "Conformal invariance" is GRANTED from the linearized conformal-Bach identification
  (`box^2 = -4 Bach`, proven only on the spin-2 sector) extended to the full soldering functional.
  That extension is ARGUED, not forced. So the uniqueness forces the norm only CONDITIONAL on the
  grant, not from nothing.

### Q2 -- COLOR-KINEMATICS CLOSURE (D): closes on BOTH -> RELABELS [COMPUTED]

- The self-dual kinematic algebra `su(2)_+` on `Lambda^2_+` (dim 3) CLOSES with Jacobiator EXACTLY
  ZERO. Kinematic-Jacobi is satisfiable in the self-dual sector -- this is why self-dual gravity =
  (self-dual YM)^2 is rigid. COMPUTED (`||Jacobiator|| = 0`, `dim Lambda^2_+ = 3`).
- **The discriminator against the built Wave-16 carrier structure.** The self-dual `so(9,5)`
  generators `J_i` on the actual (9,5) triplet (`192 = 3 x 64`) PRESERVE `ker Gamma` -- carrier B's
  gamma-trace-constrained field space: `||Gamma J_i Pi_RS|| = 8e-15 = 0` on the verified rep
  (`rank Pi_RS = 1664`). So the kinematic algebra closes on carrier B.
- **But it closes on BOTH.** The reason B closes is that `Gamma` is an `so(9,5)`-EQUIVARIANT
  intertwiner (`Gamma J_i = sigma_i Gamma`, residual `0`) and `ker Gamma` is an `so(9,5)`-subrep. By
  the SAME equivariance the FULL field space (carrier A: full space + BRST) is an `so(9,5)`-module
  too, so `J_i` preserves it as well. The kinematic algebra is carrier-BLIND: the A/B distinction is
  the downstream INDEX (`-42` vs `-38`), not whether the self-dual algebra closes. COMPUTED.
- **Removes 0 of the K-class A/B bit.** This is exactly the RELABELS outcome persona 6 pre-registered
  for the "closes on both" branch ("another beautiful non-lever").

### Q3 -- DO B AND D COINCIDE? Same on the spin-2 core, distinct on the trace mode [COMPUTED/cited]

- **Coincide on the spin-2/Bach core.** On the transverse-traceless graviton the difference between
  any two of the norms is a multiple of `|H|^2` (the mean-curvature/trace mode), which VANISHES on
  TT. So B's conformal `|II_0|^2` (EL = Bach), D's self-dual double-copy square (`box^2`), and
  `-4 Bach` all reduce to the SAME operator `box^2` on spin-2 (`box^2 = -4 Bach`, H1 machine-checked;
  the double copy squares the first-order self-dual `box` datum). B and D are the SAME principle here.
- **Diverge on the trace/Einstein mode.** The norm difference is `(1/4)|H|^2`. B EXCLUDES it
  (conformal, pure `box^2`); GU's full `|II|^2` INCLUDES it (Stelle `box(box+m^2)`); the self-dual
  square is SILENT on it. They coincide exactly where both are forced and diverge exactly on the
  residual (`|H|^2` trace mode) that neither forces.

### Q4 -- VERDICT + FREEDOM COUNT: PARTIAL, leaning RELABELS [COMPUTED]

The 4 independent unforced choices `{signature (9,5), |II|^2 norm P2, soldering, K-class SG4}`:

| choice | removed unconditionally | removed conditional (grant conformal inv.) |
| --- | --- | --- |
| signature (9,5) | no (self-dual arena is rep-level) | no |
| `|II|^2` norm P2 | no (uniqueness needs the grant) | **yes** (1-dim), but forces conformal `|II_0|^2` |
| soldering | no (even-sector, independent; H40 Q2) | no |
| K-class SG4 | no (Q2 closes on both A and B) | no |

- **Unconditional removal = 0 of 4.** The uniqueness needs conformal invariance granted; the
  color-kinematics closes on both A and B; signature and soldering are untouched.
- **Conditional removal (granting conformal invariance) <= 1 of 4** -- only the norm, and even that
  forces the conformal `|II_0|^2` (pure Bach), REVISING the full-`|II|^2` lean rather than confirming
  it. The count+norm+K-class do NOT collapse to one.

**This is not a forcing collapse.** A forcing win would require the K-class (A/B) bit removed and the
`{count, norm, K-class}` collapsed to a single algebraic identity. Instead the load-bearing "only-B"
color-kinematics test RELABELS (closes on both), and the uniqueness leg is a conditional,
target-revising partial. **VERDICT: PARTIAL, leaning RELABELS. The source-action postulate does NOT
become a theorem.**

---

## Honest limits

- **The uniqueness (Q1) is real but does the wrong job.** The 1-dimensionality is a genuine
  universal-property forcing structure -- the strongest single result in this test. But it forces the
  traceless conformal `|II_0|^2` (pure Bach), which the repo's own H45 distinguishes from the favored
  full `|II|^2` (Stelle). So the one place H48 "forces" a freedom, it forces a target in TENSION with
  the standing lean, and only after granting conformal invariance (proven linearized on spin-2 only).
  Reporting this as "forces `|II|^2`" would be the cosmetic-unification trap; it forces `|II_0|^2`.
- **The color-kinematics leg is a clean H20-style negative.** The "only-B" closure was the entire
  forcing signal on the D side. It fails for a structural reason (equivariance): the self-dual algebra
  respects every `so(9,5)`-submodule, so it cannot discriminate A from B. The A/B bit is downstream of
  the index, which the kinematic-Jacobi does not see. This is a genuine freedom-reduction test whose
  honest answer is 0 freedoms removed -- exactly as persona 6 designed it to fail-honestly.
- **What stays open is unchanged.** Signature, soldering, and the K-class A/B bit remain exactly the
  freedoms H39/H40 left. The count stays `{1,3}`; the source action stays the terminal unbuilt object
  with its unbuilt causal-cure term (H40 Q4). H48 reorganizes the picture around the self-dual square
  without shrinking it -- the same relationship H20's Clifford grading had to the same object.
- **Scope.** Q1's coefficient/constraint count and Q2's closure are COMPUTED (exact linear algebra /
  sympy on the verified Cl(9,5) rep). Q3's spin-2 coincidence cites `box^2 = -4 Bach` (H1,
  machine-checked). The extension of conformal invariance from the linearized spin-2 identification to
  the full soldering functional is ARGUED, and is the single load-bearing grant behind the conditional
  removal of the norm.

## RE-RANK signal

**PARTIAL, leaning RELABELS. Removes 0 of the 4 unforced choices unconditionally; at most 1 (the
norm) conditional on granting conformal invariance -- and that one forces the conformal `|II_0|^2`,
not GU's `|II|^2`.** The self-dual-square candidate does not collapse `{count, norm, K-class}` to one.
The load-bearing color-kinematics leg (D) RELABELS (closes on both A and B, the H20 trap); the
uniqueness leg (B) is a genuine but conditional and target-revising partial. B and D coincide only on
the spin-2/Bach core (`box^2 = -4 Bach = ` the square of a first-order self-dual object) and diverge
on the trace/Einstein mode neither forces.

Single next object, unchanged: the source action's unbuilt causal-cure term (H40 Q4), built so as not
to p-hack the carrier. H48's contribution is negative-space discipline: it retires the "self-dual
square forces the coherent collapse" hope by showing the color-kinematics closure is `so(9,5)`-blind
to the A/B bit, and it sharpens the norm question by exhibiting that any conformal-uniqueness forcing
delivers the pure-Bach `|II_0|^2`, not the Stelle `|II|^2` the program currently favors.
