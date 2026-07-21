---
title: "PRONG 1 method scope: the numerical establish-or-refute plan for the PRODUCT-UNIFORM NORM-RESOLVENT BOUNDARY-VALUE THEOREM -- a decided method decision-tree (not results). Uniformity object DECIDED (the delta->0 norm-resolvent LIMIT resolvent norm, sup over a z-region, not the sup-mode operator and not the single-z delta-Cauchy increment the factor-4 gate mis-measured); correct gate DECIDED (log U(N) vs log N growth-rate slope on a WALL-ALIGNED grid ladder, replacing the alignment-confounded factor-4-at-z=2i ratio -- the confound demonstrated: min|q_j| is a sawtooth in N, 19 reversals over 21 consecutive N); discretization DECIDED (keep the operator_grade_end central-difference pointwise-lift scheme -- it preserves K-self-adjointness AND deck-oddness EXACTLY and stays block-tridiagonal for the BlockTriLU resolvent; spectral collocation rejected: dense + deck-fragile at Dirichlet ends); z-region DECIDED (wall-aligned off-real strip excluding the crossed-sector imaginary band); minimal decisive computation NAMED (wall-aligned 3-rung imaginary-segment quadruple: one gapped control + one crossing + one 2-block product + two negative controls); planted controls with demonstrated power (gapped-only PASSES, (q+idelta)^{-1} over-singular normalization FAILS, identical-block product must NOT false-fire); top ill-posedness risk NAMED (delta->0 and N->infinity non-commutation -- keep delta in the grid-resolved window); product toy DECIDED (minimal 2-block SUFFICIENT but must be two COMPARABLE CROSSING blocks with DISTINCT walls -- gapped+crossing masks, identical doubles multiplicity)"
status: active_research
doc_type: scoping_decision_tree
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (scope Prong 1: uniformity numerics method)"
claim: none
canon: none
posture: none
inputs:
  - explorations/operator-grade-end-2026-07-20.md
  - explorations/boundary-law-operator-lift-2026-07-20.md
  - explorations/sector-relative-section-theory-2026-07-20.md
  - explorations/n2-end-family-2026-07-20.md
reuses:
  - tests/channel-swings/operator_grade_end_probe.py
  - tests/channel-swings/sector_relative_section_probe.py
  - tests/channel-swings/n2_end_family_probe.py
runnable:
  - tests/channel-swings/prong1_scope_checks.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# Prong 1: the method to establish-or-refute product-uniformity

> **EXECUTION CORRECTION (2026-07-20):** The fixed-delta exponent-one
> negative control cannot test `delta -> 0`, and the implemented 512-block
> product surrogate is not the exact commuting-tensor Stage-1 product (its
> defining algebra fails by order `10^1`). The matched-delta per-object test
> supports boundedness along one joint refinement path. A successor typing
> audit then established that the Lawvere product is Cartesian/Krein-direct-
> sum, so the product clause is algebraic and the coupled tensor is a separate
> monoidal question. The wall-on-node fixed-grid limit is not an ordinary
> operator resolvent. See
> `explorations/product-typing-and-resolvent-pencil-swing-2026-07-20.md`
> before reusing this method plan.

The theorem gating both blockbuster faces (boundary-law Section 1c /
sector Section 7.1): the delta -> 0 norm-resolvent boundary value of the
section operator `N_delta,op = M_op (q_op + i delta)^{-1/2}` exists on a
z-region, is deck-odd, and is BOUNDED UNIFORMLY across the discretization
ladder AND across finite-product carriers `A x A x ...`. operator_grade_end
reached A3: the norm-resolvent mode is the only survivor (delta-Cauchy at
rate ~delta^1.0 per N), deck-oddness is machine-exact, but the factor-4
N-uniformity gate FAILED at 5.4 (non-monotone wobble 0.0066/0.0357/0.0099
at N=64/128/256) and the sup-mode diverges ~N^1.35. This document DECIDES
the method for the next swing. It is a plan; the only computations run here
are the small validating checks in the appendix (`prong1_scope_checks.py`).

## Obligation 1 -- the uniformity object, precisely, and the correct gate

**The object (DECIDED).** Not the operator `N_delta,op` itself (that is the
sup-mode; it diverges ~N^1.35 and is the WRONG topology -- the wall's
Jordan-nilpotent normalization is an unbounded sup obstruction). Not the
bare `(D_op - z)^{-1}`. The object is the **delta -> 0 norm-resolvent LIMIT
resolvent** of the section operator,

    R_0,N(z) := lim_{delta->0} (N_delta,N - z)^{-1},

on the discretized L^2 collar at resolution N. The quantity that must be
N-uniform is its operator norm, swept over a z-region Z:

    U(N) := sup_{z in Z} || R_0,N(z) ||   (largest singular value,
                                           deterministic power iteration +
                                           BlockTriLU, as in the probe).

"Product-uniform" (operational): `C_read` closed under finite products in
the norm-resolvent topology means `U_2(N) := sup_z ||R^{(2)}_0,N(z)||` is
ALSO N-bounded, where `R^{(2)}` is the resolvent of the section operator on
the 2-block product carrier. **Minimal 2-block toy is SUFFICIENT**: the
diagonal argument uses only `A x A` (Delta: A -> A x A, T: A x A -> B), and
the finite-product tower closes by the same induction PROVIDED the 2-block
constant is block-content-independent. But the two blocks must be
**comparable crossing blocks with DISTINCT walls** (appendix C3): a gapped
block masks a crossing (no product wall forms), and identical blocks only
double multiplicity (the referee artifact). The full product tower is NOT
needed to decide the theorem (see Obligation 8, step 5, flagged).

**The correct gate (DECIDED), and why factor-4 was wrong.** Replace
"max/min of the smallest-delta resolvent difference across the ladder < 4
at z=2i" with a **growth-rate gate on the limit norm over a wall-aligned
ladder**:

    fit  log U(N)  vs  log N   over  N in {65,129,257,513(,1025)};
    PASS if slope <= tau (tau ~ 0.15: bounded, with finite Richardson
         delta-extrapolant) UNIFORMLY over the z-region;
    FAIL if slope is bounded away from 0 (power-law growth, cf. N^1.35).

The factor-4 gate failed for three separable reasons, each fixed:
1. It thresholded the delta-CAUCHY INCREMENT (a proxy), not the limit norm.
   The increment ~ 1/min_j|q_j|, and (appendix C1) `min_j|q_j|` is a
   SAWTOOTH in N driven by grid-wall alignment -- 19 direction reversals
   across 21 consecutive N. The 5.4 was two unlucky alignments, not a
   trend. Fix: measure the extrapolated LIMIT norm on a WALL-ALIGNED grid
   (appendix C2: wall on the central node at odd N makes the worst point's
   contribution `(i delta)^{-1/2}` identical across N, removing the
   alignment degree of freedom).
2. It sampled a SINGLE z=2i. A theorem needs a z-region (the probe's own
   functional-analyst note). Fix: sup over Z, and map slope(z).
3. It read a two-point ratio. Fix: a >=4-rung log-log slope with a fit
   band (dominates the ~1% power-iteration noise).

**LAP refinement (INGESTED from Prong 2).** The Krein-Mourre limiting-
absorption principle (Georgescu-Gerard-Hafner, JFA 265 (2013)) predicts the
bounded object is a WEIGHTED resolvent, `|| <A>^{-s} (H-z)^{-1} <A>^{-s} ||`
with `s > 1/2` and `<A>` built from the collar conjugate operator (dilation/
translation generator `A ~ s d/ds` or `d/ds`). So measure `U(N)` in BOTH the
plain operator norm AND the `<s>^{-s}`-weighted norm (a diagonal
multiplication weight on the collar, trivial to insert into the power
iteration): the theorem's bounded object may be the WEIGHTED one even where
the plain resolvent is not N-uniform. And the gate has a sharpened meaning:
it is the numerical establish-or-refute of whether the type-changing wall is
a **REGULAR** critical point of the K_S spectral function IN RESOLVENT NORM,
uniformly in N. The sup-mode `N^1.35` is "singular in sup-norm"; a flat
`slope(U)` is "regular in resolvent norm" -- exactly the one missing
ingredient Prong 2 isolates (Section 6 there).

## Obligation 2 -- discretization (KEEP the central-difference lift)

**DECIDED: keep the operator_grade_end scheme** -- `P_N = -i d/ds` central
difference with Dirichlet ends, internal space doubled `C^2 x C^128`
(`G_col = sigma2 x I`), section objects lifted POINTWISE as multiplication
operators (`Ku_op`, `q_op`, `M_op = Ku_op D_op`). Rationale: this scheme
preserves EXACTLY, at every N, the two structures whose uniformity we
measure --
- **K-self-adjointness** `K_op D_op K_op = D_op^dag` is exact by
  construction (pointwise K_S-conjugation commutes with the local stencil);
- **deck-oddness** `U_h N_delta,op(t) U_h^{-1} = -N_delta,op(t+1)` is
  ALGEBRAIC (pointwise covariance + collar-term deck-invariance), verified
  1e-12 across the ladder.
A discretization that broke either would make the uniformity test
meaningless. **Spectral collocation is REJECTED**: its dense differentiation
matrix (i) destroys the block-tridiagonal structure the BlockTriLU resolvent
depends on (splu fill was already catastrophic on these dense-block
tridiagonals), and (ii) makes the derivative NONLOCAL, so pointwise deck
covariance no longer commutes cleanly with the Dirichlet-truncated operator
(the deck is a pointwise internal conjugation; a global derivative couples
all nodes and the ends break the exact identity). Finite element is rejected
too: the mass matrix spoils the pointwise `q_op^{-1/2}` normalization. **One
refinement to the scheme**: for the ladder use ODD N with the collar window
CENTERED on the wall `s*` so `s*` lands on the central node (appendix C2) --
this is the "wall-aligned-grid ladder" the A3 receipt named, and it makes
the worst grid point N-independent by construction.

## Obligation 3 -- the z-region parameterization

An indefinite (Krein) operator's resolvent MUST blow up as z approaches the
real spectrum, so the bound can only hold OFF the real axis, in the
resolvent set. **DECIDED region (sharpened by Prong 2)**: NOT a generic
off-real strip -- specifically the **Krein-positive-projection / definite-
type strip over the GAPPED sub-end**. Prong 2 (Section 4) is explicit:
choose z with (i) `Im z >= y_lo > 0` (off the real axis), (ii) z lying over
the DEFINITE-TYPE spectral interval where `1_I(H)` is Krein-positive (the
`P > 0` sector), bounded away from the wall/critical-point images, and
(iii) z OUTSIDE the epsilon-pseudospectral tongue the wall's Jordan nilpotent
opens on the crossed sector. Prong 2's crisp warning, honored: **do NOT
scope z over the crossing sector** -- there the section operator is
effectively non-self-adjoint (K_S-skew involution) and only a pseudospectral,
NON-uniform statement exists. This corrects a generic-strip reading: the
target is the definite-type resolvent set of the sector-restricted operator.
The A3 receipt corroborates from the numerical side -- `z = 2i` RESONATED
with the crossed-sector imaginary band (dgraph 218 > dplain 61 at N=64,
moved to `z = 2+2i`), which is exactly the pseudospectral tongue to avoid.
Cheapest-decisive first: a short IMAGINARY-AXIS segment `z = i y,
y in {0.5, 1, 2}` positioned over the gapped-sub-end definite interval, then
widen to the definite-type strip.

**Wrong-region vs theorem-false (the decisive distinction).** Calibrated by
the controls (Obligation 5) and by mapping `slope(z)`:
- genuine theorem-falsity -> `slope(N)` is bounded away from 0 and roughly
  z-INDEPENDENT across the safe strip;
- wrong region (z too near spectrum) -> `slope(N)` BLOWS UP only as z
  approaches a region boundary, and the positive control diverges THERE
  TOO. If the gapped control is flat where the crossing case diverges, the
  divergence is genuine; if both diverge, the region is wrong.

## Obligation 4 -- the minimal decisive computation

**"The wall-aligned 3-rung imaginary-segment quadruple."** On the
wall-aligned ladder `N in {65, 129, 257}` (wall on central node), at
`z = i y, y in {0.5, 1, 2}` (crossed band excluded), compute the
Richardson-extrapolated limit resolvent norm `U(N)` and fit `slope(log U vs
log N)` for FOUR carriers:
(a) ONE gapped ray (positive control, must give slope ~ 0);
(b) ONE crossing ray + its wall (the minimal open case);
(c) the 2-block PRODUCT of two comparable crossing blocks with distinct
    walls (product-uniformity, the genuinely-new clause);
plus the two negative controls of Obligation 5.
This is ~9 operator builds per carrier over a 3-point z-set -- far cheaper
than the full strip x 512-ladder x 53-ray census -- and it establishes-or-
refutes the theorem on the best region BEFORE any full ladder. If (a) is
flat and (b)/(c) are flat: corroborated (A1-shaped, now with uniformity). If
(b) or (c) shows a clean z-independent positive slope while (a) stays flat:
REFUTED, with the divergence rate the deliverable.

**Cheaper complementary instrument (from Prong 2): the Mourre constant
`c_N`.** Prong 2 reduces the whole theorem to a uniform positive-commutator
(Mourre) estimate `Re <u,[H,iA]u> >= c <u,u>` on `Ran 1_I(H)`, with `c`
N-independent and product-stable, for the conjugate operator `A ~ s d/ds`
(collar dilation). `c_N` is the bottom of the positive part of the commutator
compressed to the definite-type range -- an EIGENVALUE computation, NO
resolvent solves -- so it is cheaper than the resolvent sweep and directly
decisive: `c_N` bounded below as N grows => regular critical point (theorem
reachable); `c_N -> 0` => singular (refuted / new-math). Run it FIRST as a
sign-post, then confirm with the resolvent quadruple. Its product analog
`c^{(2)}_N` (commutator of the 2-block generator) tests exactly Prong 2's
open point: the Mourre constant is NOT automatically inherited by products.

## Obligation 5 -- planted controls with demonstrated power

The gate must PASS a known-uniform family and FAIL a known-divergent one, or
it tests nothing.
- **Positive control (must PASS):** the gapped-only family (`q > 0`
  throughout, no wall). Its limit resolvent is the trivial off-wall bounded
  one; the A3 receipt already shows gapped is delta-Cauchy and N-stable to
  3%. On the correct gate: slope ~ 0.
- **Negative control #1 (must FAIL), demonstrated power:** the OVER-SINGULAR
  normalization `(q_op + i delta)^{-1}` (exponent 1, not 1/2) on the SAME
  crossing wall. At the wall it contributes `(i delta)^{-1}`; its limit
  resolvent norm grows with N and has no finite delta-extrapolant -- a
  family with KNOWN divergence. The gate must FAIL it while PASSING the true
  `-1/2` normalization on the gapped control. That split is the gate's
  demonstrated discriminating power.
- **Negative control #2 (must NOT false-fire):** the product of two
  IDENTICAL crossing blocks. This only doubles multiplicity, not norm; a
  gate that flags it as divergence is measuring carrier-doubling artifact,
  not genuine product growth (the referee charge). U_2 here must track U
  (slope ~ same as single block), confirming the gate reads genuine product
  fragility only when the blocks have DISTINCT walls (appendix C3).

## Obligation 6 -- ill-posedness / obstruction modes

- **(TOP RISK) delta -> 0 and N -> infinity NON-COMMUTATION.** The test
  measures `lim_delta` then `trend_N`; if the true object needs the
  continuum (N -> infinity) first, discrete `U(N)` need not track it.
  Mitigation: keep delta in the GRID-RESOLVED window
  `delta in [C h |q'|, q_typ]` so the wall is delta-resolved, not
  h-resolved -- the A3 receipt flagged that at N=256 the smallest delta sat
  BELOW grid wall resolution (`q' h ~ 0.075`), which invalidates those
  rungs; extrapolate only within the commuting window, and verify the
  delta-rate (~1.0) is N-stable at fixed z as evidence of commutation.
- **The limit object not existing.** If some z has no finite
  delta-extrapolant, the "limit" is spurious (resolvent set misidentified).
  Mitigation: wall-on-node makes the worst point `(i delta)^{-1/2}` (clean
  delta -> 0), and off-axis z keeps `N_0 - z` invertible.
- **Product test conflating carrier-doubling with genuine divergence.**
  Guarded by negative control #2 and by using distinct-wall comparable
  crossing blocks (C3). The DEEP obstruction Prong 2 names (Section 5): for
  non-normal / effectively-non-self-adjoint pieces (the crossed sector),
  pseudospectra are NOT the neighborhood-sum and the product's pseudospectrum
  can be far larger than the union (Trefethen-Embree) -- so a uniform
  resolvent bound does NOT pass to products for free. The 2-block test must
  therefore check whether the pseudospectral tongue GROWS under the product
  (equivalently `c^{(2)}_N < c_N` degrading with N), which is the genuine
  content of product-uniformity and has no off-the-shelf precedent.
- **Grid-wall alignment sawtooth** (C1) contaminating any fixed-grid
  ladder -- removed by wall-on-node (C2).
- **Power-iteration ~1% norm accuracy** -- fine for slope columns; use >=4
  rungs and report the fit band so the tau=0.15 gate dominates the noise.

## Obligation 7 -- literature-scout coupling (INGESTED)

The sibling scout (`explorations/prong2-krein-resolvent-literature-2026-07-
20.md`) landed during this scope and IS folded in above. Its load-bearing
outputs, and where each went:
- **Best framework = Krein-space positive-commutator (Mourre) LAP**,
  Georgescu-Gerard-Hafner, JFA 265 (2013) 3245-3304 (arXiv:1211.0791) -- the
  only surveyed theorem that is Krein-native, delivers a resolvent BOUNDARY
  VALUE (delta -> 0) on a z-region, and is built for non-compact settings.
  Folded into Obligation 4 (the `c_N` Mourre-constant instrument) and the
  execution plan.
- **The metric is WEIGHTED**: `|| <A>^{-s}(H-z)^{-1}<A>^{-s} ||`, `s > 1/2`.
  Folded into Obligation 1 (measure plain AND weighted `U(N)`).
- **The z-region is the Krein-positive/definite-type strip over the gapped
  sub-end, off the wall image and off the pseudospectral tongue; NOT the
  crossing sector.** Folded into Obligation 3 (corrected the generic-strip
  reading).
- **The reduction to ONE ingredient**: uniform regularity of the wall as a
  Krein critical point (N- and product-stable) == a uniform Mourre estimate
  whose constant does not degrade to 0 at the wall. This IS what the gate
  now tests (Obligation 1 reframing; the `c_N` instrument).
- **Product-uniformity = genuinely novel** (no off-the-shelf), obstructed by
  pseudospectral non-additivity for non-normal pieces. Folded into
  Obligations 1 and 6.
Two caveats carried from Prong 2: its central citation (arXiv:1211.0791) is
at ABSTRACT grade (PDF body did not parse), so the three LAP hypotheses
should be re-read from the paper body before the analytic write-up leans on
them; and Prong 2 ran no computation. Neither blocks the Prong-1 numerics --
the `c_N` and `U(N)` instruments are self-certifying.

## Obligation 8 -- cost-ranked execution plan (value floors)

1. **[~5 min algebra, MUST]** Settle the product construction fork: define
   the section symbol `M_2` on the 2-block carrier with `M_2^2 = q_2 I`
   (the defining section-symbol property) and verify `q_2` has an emergent
   wall for two comparable crossing blocks. Appendix C3 shows the additive
   symbol scalar relocates the wall; confirm the true section symbol does
   too. VALUE FLOOR: if no bounded section-symbol product with `M_2^2=q_2 I`
   exists, product-uniformity is ill-posed as stated -- STOP and report the
   construction gap (that is itself the answer).
2. **[cheapest sign-post, from Prong 2]** Compute the Mourre constant `c_N`
   (bottom of the positive commutator `[H, iA]`, `A ~ s d/ds`, on the
   definite-type range) across the wall-aligned ladder, and its 2-block
   analog `c^{(2)}_N`. No resolvent solves. VALUE FLOOR: if `c_N -> 0` the
   wall is singular and the theorem is refuted-as-stated here -- report and
   stop the resolvent sweep.
3. **[cheap, decisive]** Run the minimal decisive quadruple (Obligation 4)
   with both negative controls, in plain AND weighted norm. VALUE FLOOR: if
   the negative controls do not split from the positive, the gate is
   uncalibrated -- fix before widening.
4. **[moderate]** Widen z from the imaginary segment to the definite-type
   strip over the gapped sub-end; map `slope(z)` to separate wrong-region
   from theorem-false.
5. **[moderate]** Extend the ladder to N=513/1025 on the decisive carriers
   to tighten the slope band and the Richardson extrapolant.
6. **[expensive, FLAGGED not scheduled]** The full finite-product tower
   (3+ blocks) and the 53-ray census. Flagged: the induction closes at the
   2-block case, so this costs more than it can resolve once steps 1-5
   decide the theorem; schedule ONLY if the 2-block passes and a referee
   demands the tower.

**Recommended execution swing (one paragraph).** Keep the
operator_grade_end central-difference pointwise-lift discretization
unchanged (it alone preserves K-self-adjointness and deck-oddness exactly
and stays block-tridiagonal); rebuild the collar on an ODD-N wall-centered
grid so the wall sits on the central node at every rung; define the object
as the delta-extrapolated norm-resolvent LIMIT resolvent norm `U(N)` (plain
AND `<s>`-weighted, per the Krein-Mourre LAP) swept over a short off-real
imaginary-axis z-segment positioned over the gapped sub-end's definite-type
interval and off the pseudospectral tongue; first settle the `M_2^2 = q_2 I`
product construction in five minutes of algebra and compute the Mourre
constant `c_N` (and `c^{(2)}_N`) as the cheapest regular-vs-singular
sign-post, then run the wall-aligned 3-rung quadruple (gapped positive
control, one crossing, one distinct-wall 2-block product, plus the
`(q+idelta)^{-1}` and identical-block negative controls) and gate on the
log U vs log N slope against tau ~ 0.15; only if that passes, widen to the
definite-type strip and the N=513/1025 rungs, and leave the full product
tower and 53-ray census unscheduled behind their value floor.

## Appendix -- validating checks run (prong1_scope_checks.py)

Reuses the operator_grade_end geometry verbatim (t_op=0.4100, s*=0.5694,
window [0.169,0.969], dq/ds|wall=-24.12 -- reproduced on import). Command:
`python tests/channel-swings/prong1_scope_checks.py`. Outputs:

- **C1 (factor-4 confound).** Fixed interior-node grid, N scanned 120..140:
  `min_j|q_j|` ranges 0.0000 (N=121, a node lands on the wall) .. 0.0795
  (N=120), with **19 direction reversals across 21 consecutive N** -- a
  sawtooth in N from grid-wall alignment. The resolvent last-pair difference
  ~1/min|q| inherits it; the factor-4 ratio (failed 5.4) reads alignment,
  not a divergence trend. Substantiates Obligation 1, fix #1.
- **C2 (wall-aligned remedy).** Window centered on s*, odd N in
  {65,129,257,513}: the central node lands on s* exactly (dist = 0), so
  `min_j|q_j| = 0` at EVERY N -- the worst node contributes `(i delta)^{-1/2}`
  identically across the ladder. The alignment degree of freedom is removed
  and a log-log growth-rate gate on the limit norm becomes well posed.
  Substantiates Obligations 1 (correct gate) and 2 (odd-N refinement).
- **C3 (product carrier has its own walls).** Named finding first: a
  strongly-gapped block (`q_A in [17.4, 87.2]`) plus a weak crossing block
  (`min q_B = -18.10`) gives `q_A + q_B` with NO zero -- the gap MASKS the
  crossing. Two comparable crossing blocks with distinct walls (s=0.5694 at
  t=0.410; s=0.4482 at t=0.414) give a combined wall RELOCATED to s=0.4981,
  absent from either factor there. Substantiates Obligation 1 (2-block toy
  must be distinct-wall comparable crossing blocks) and Obligation 5
  (negative control #2). Note: the additive scalar `q_A+q_B` is a heuristic
  stand-in; execution step 1 must confirm the true `M_2^2=q_2 I` section
  symbol carries the same emergent wall.

## Boundary

Scoping tier: a method decision-tree, not results. No claim, canon,
scorecard, or posture moves; no external actions; no commits or pushes; no
edits to any existing file (only this document and
`tests/channel-swings/prong1_scope_checks.py`, both new). The validating
checks are minutes-bounded symbol-scalar computations (no operator builds,
no resolvent solves); every operator-grade number cited is
operator_grade_end's, reused not re-run. The theorem itself remains OPEN;
this document decides only HOW the next swing should attack it. The Prong-2
Krein-resolvent literature scout arrived during this scope and is INGESTED
(Obligation 7): best framework Krein-Mourre LAP, weighted metric,
definite-type z-region over the gapped sub-end, product-uniformity novel,
crux = uniform regularity of the wall as a Krein critical point.
