---
title: "Anchor-scale test of the graded inhomogeneous-gauge-group algebra: it CLOSES on the honest Cl(9,5) = M(64,H) fiber (understanding, not a verdict for a side). The corners campaign's toy super-Jacobi closure is scale-robust for its load-bearing part; the toy's diagonal/RD reading was a small-fiber artifact (sl(128) simple, no 4-dim rep); and the anchor SELECTS the real form the toy left open (sesquilinear Krein pairing on S_R; the u(1) center kills the complex-bilinear channel). A NEW previously-unnamed structural fork surfaces: two distinct complexification-free real forms (u(64,64) with center vs the centerless quaternionic g_H). Which the object 'is' is an SG4 selection this run does not make."
status: staged
doc_type: results
created: 2026-07-10
grade: "COMPUTED / exact (Gaussian-rational; NO float scouts on any assert path). LEG-1 64 checks + crosscheck 9, exit 0; LEG-2 35 checks, exit 0; both re-run in-repo. Adversarially verified: 2 hostile referees, 0 refuted, each independently re-derived load-bearing claims with DIFFERENT machinery (right-tensor vs left-tensor JW gamma construction; different timelike sets {9-13} vs {4-8}; numpy Gaussian-integer vs sparse Gaussian-rational) -- 16/16 and independent re-derivations exit 0. Honesty tiers stated in-doc: (1) exact all-element for the even/module/equivariance classes and the Clifford/Krein/embedding facts; (2) exact but witness-sampled for the cubic/central-balance ansatz closures (bounded-degree polynomial identities on fresh exact witnesses, reproduced on a second codebase); (3) ARGUED via representation theory (weakest, flagged) for ansatz-completeness and RD-impossibility. Posture-audited: both legs passed (no side-framing). Internal tier (caveat (e)). No canon row moves; SG4 remains the sole decider; the generation count stays OPEN."
depends_on:
  - canon/escape-corners-campaign-RESULTS.md
  - tests/escape-corners/legb1_graded_ig_algebra.py
  - absorbed/gu-source-action/DEAD-ENDS.md
scripts:
  - tests/anchor-scale/leg1_anchor_super_jacobi.py
  - tests/anchor-scale/leg1_crosscheck.py
  - tests/anchor-scale/leg2_krein_real_form.py
  - tests/anchor-scale/indep_verify.py
  - tests/anchor-scale/refute_leg2.py
---

# Anchor-scale test of the graded-IG algebra

The escape-corners campaign named three open gaps under corner (b)'s graded-IG door (the "cheapest
kill shot"): does the algebra survive at anchor scale, in the honest real/Krein form, at derivative
level? This run closes the first two and names the third. Framed as understanding about the object:
survival and failure were equally valuable going in.

## What the object does at anchor scale

**It CLOSES.** On the honest `Cl(9,5) = M(64,H)` fiber (128-dim spinor, exact signature-(64,64)
Krein form `beta_S`, `u(64,64)`-type anchor), the graded extension
`s = (u_beta (+) T)_even (+) S_odd` closes every super-Jacobi identity class (complete list
C1a-d, C2a-c, C3a-b, C4 certified). The `so(9,5)` spin generators are `beta_S`-pseudo-anti-Hermitian,
so `so(9,5) < u(64,64)` (all 91, exact). So the corners campaign's toy super-Jacobi closure is NOT a
small-fiber artifact for its load-bearing part -- it is scale-robust.

## The three things understood (equal-value outcomes, no side-framing)

1. **What WAS a toy artifact:** the toy's diagonal / "RD" reading cannot exist at the anchor --
   `sl(128)` is simple with no 4-dimensional representation. That feature was a small-fiber
   coincidence, now exposed. (This is exactly the kind of thing an anchor-scale test exists to
   catch; catching it is a success.)

2. **The honest departure is REALITY, not existence.** The anchor SELECTS a real form the toy left
   unselected. On the semisimple sub-anchor `so(9,5)` the closure is carried by a complex-bilinear
   pairing (the antisymmetric charge conjugation `C_+` makes `C_+ sigma_ab` symmetric); but on the
   full `u(64,64)` anchor the complex channel is KILLED by the `u(1)`-center charge constraint
   (`z = i*Id` acts as `+i` on `S`), leaving only the intrinsically-real sesquilinear Krein pairing
   `M(Q,P) = i(Q P^dag beta + P Q^dag beta)` on the real form `S_R`. The odd-odd bracket is
   pseudo-anti-Hermitian from `beta` Hermitian ALONE (root-caused by the referee: holds for any
   Hermitian `b`, fails for a non-Hermitian control -- no Clifford identity, no complexification).
   **Reality is not just compatible; it is forced.** `so(9,5) < u(64,64)` reconciles the two routes.

3. **A NEW, previously-unnamed structural fork.** The `M(64,H)` quaternionic structure `J` exists
   exactly (`J^2 = -I`), is a genuine symmetry of the `spin(9,5)` sector and the Krein form, but
   ANTICOMMUTES with the central charge and is invisible to `u(64,64)`. So there are TWO distinct,
   each-consistent, each-complexification-free real forms -- `u(64,64)` (with center, complex-type
   odd module `S_R`) and the centerless quaternionic `g_H` (`J`-symmetric, an extra bilinear
   channel) -- that do NOT coincide. Which the object "is" is an SG4 selection this run does not
   make. This is the run's genuinely new datum.

## FORCED-shape and locality

The toy's forced shape transfers: `{odd,odd}` is forced into the translation slot `Omega^1(ad)`
(not the gauge algebra) for the whole gauge algebra in the minimal ansatz (exact kill-witnesses) --
machine-confirming, at anchor scale, the transcript's "the space of four momentum becomes the space
of gauge potentials." Sole anchor-specific loosening: a 1-parameter central-`u(1)` locus
`t* = -128 * sum(w_mu q_mu)` in the extended ansatz, available only because `u(64,64)` has a center
`so(4)` lacked (an `su(n|1)`-type Fierz balance). All structure maps pointwise (toy `R^4` locality
transfers verbatim).

## Still open (honest scoping)

- **Real-form SELECTION** (`u(64,64)` vs quaternionic `g_H`): both close; which is physical is SG4.
- **Derivative-level odd `tau_plus`** (Question 3): BLOCKED at exactly the geometric/curvature layer,
  missing structure named; only the frozen-flat reality shadow is certified.
- **Ansatz-completeness** is argued via representation theory (Schur + `sl(128)`-irreducibility with
  machine-verified premises), NOT exhaustive ranks -- the weakest link, labelled as such (replaces
  the toy's exact-rank certificates).

## What this means for the standing picture (no verdict movement)

The cheapest kill shot did NOT eliminate the graded-IG door: the algebra is real at honest scale,
so corner (b) stays OPEN, and the last purely-algebraic contingency under it is removed (the door's
existence is no longer toy-contingent). This does NOT harden the B-tilt by elimination, and it does
NOT decide the carrier bit: the object now presents a sharper SG4 question -- WHICH real form, whether
GU's action is invariant under the scalar-spinor odd variation, which sub-slot is gauged, and at
which vacuum phase. No claim is made that GU's action is invariant under any of this; no canon row
moves; the generation count stays OPEN (located, not forced). Firewall clean throughout (no
`chi(K3)`, no `/8`, no `A-hat=3`; the bare 58.72 commutator is never formed).
