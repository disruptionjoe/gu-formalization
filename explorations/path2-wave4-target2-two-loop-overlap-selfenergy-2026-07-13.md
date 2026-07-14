---
artifact_type: exploration
status: exploration (W124; 5-persona inline team; two deterministic tests; H59 path-2 Target 2, the named settling object computed at scalar core)
created: 2026-07-13
hypothesis: H59
branch: "Path-2 wave-4 (Team R3 / W124): the two-loop self-energy at s ~ 4M^2 under BOTH prescriptions -- graded fixed-order vs Lee-Wick resummed pair, with the CLOP order-of-limits ambiguity computed explicitly (Stage A sunset, two ghost lines) and the genuinely overlapping kite topology with one ghost line (Stage B)"
title: "W124 VERDICT: PRESCRIPTION-DEPENDENT-AT-GHOST-CUTS / GRADED-UNAMBIGUOUS-AT-FIXED-ORDER / LW-CLOP-AMBIGUITY-WIDTH-EQUALS-THE-GRADED-CUT. At the mixed threshold s ~ 4M^2 the graded fixed-order sunset gives the unique positive two-ghost cut (+ Im S_gg, Krein weight (-1)^2 = +1, regulator-order independent); the Lee-Wick pair gives ZERO in its proper limit order, and the CLOP order-of-limits ambiguity spans { -1/2, 0, +1/2, +1 } x Im S_gg depending on deformation family: the ambiguity WIDTH equals exactly the graded cut. The CLOP band's endpoints (0 and +1) are the only state-space-realizable answers; the intermediates +-1/2 are optical-theorem orphans. Stage B (overlap/kite, one ghost line): no real mixed pinch exists (CLOP needs >= 2 ghost lines in one cut), prescriptions AGREE on ghost-free cuts as Gamma -> 0, the graded theory pays its odd-ghost leak at s > (2m+M)^2 where LW pays nothing, and the heavy-ghost anomalous-threshold hunt comes back EMPTY: the graded prescription develops no ambiguity of its own at two loops. Stage C (spin-2 tensor numerators): OPEN."
grade: "NUMERICAL-CONTROLLED for every integral claim (scipy quadrature, two routes where feasible, positive controls PC1-PC3 / B2a / B4b and negative controls C4 / B3a-parity; tolerances stated in-test); EXACT for the threshold-reality, cut-parity, admissible-cut-weight and spectator-positivity statements; ARGUED where marked (the regulated-convolution definition of the LW absorptive part at finite deformation; the model self-energy in R1; the 't Hooft-Veltman cutting-equation step in B4c). Tests: W124 Stage A 16/16 exit 0, Stage B 11/11 exit 0. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/path2-wave3-target2-graded-clop-and-target3-hardening-2026-07-13.md
  - explorations/path2-wave2-target2-clop-pinch-gate-2026-07-12.md
  - explorations/path2-wave1-synthesis-and-wave2-design-2026-07-11.md
  - explorations/path2-branchA-cutkosky-cut-2026-07-11.md
  - explorations/path2-branchD-leewick-2026-07-11.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - tests/W120_path2_target2_keepgrade_vs_clop.py
  - tests/W55_path2_target2_clop_pinches.py
  - tests/W48_H59_krein_loop_positivity_gate.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W124_stageA_sunset_graded_vs_LW_CLOP.py
  - tests/W124_stageB_overlap_kite_cuts.py
external_refs:
  - "Cutkosky, Landshoff, Olive & Polkinghorne, A non-analytic S-matrix, NPB 12 (1969) 281 -- the CLOP prescription and its order-of-limits ambiguity at the mixed two-loop threshold"
  - "Grinstein, O'Connell & Wise, Causality as an emergent macroscopic phenomenon, PRD 79 (2009) 105019 -- the GOW Lee-Wick cutting rules"
  - "Anselmi & Piva, JHEP 06 (2017) 066 and PRD 96 (2017) 045009 -- CLOP ambiguity localized at >= 2-loop mixed thresholds; the average/fakeon limit"
  - "Lee & Wick, Negative metric and the unitarity of the S-matrix, NPB 9 (1969) 209"
  - "'t Hooft & Veltman, Diagrammar, CERN 73-9 -- cutting equations for real-mass diagrams"
---

# Path-2 Wave-4 (W124) -- the two-loop self-energy at s ~ 4M^2, both prescriptions

**Role.** W120 closed the wave-3 synthesis by naming ONE object as the settler of the remaining
Target-2/family question: the two-loop overlapping self-energy at the mixed threshold `s ~ 4M^2`,
computed once with the resummed complex-pair propagator (removal rules) and once in the graded
fixed-order theory, compared for prescription independence and cut sign. This wave computes that
object at the scalar core (Stage A: the sunset with two ghost lines, masses `(M, M, m)`), does the
genuinely overlapping topology with one ghost line (Stage B: the kite, ghost on the shared line),
and leaves the spin-2 tensor attachment explicitly OPEN (Stage C). Five personas ran inline,
sequentially; their outputs are folded into the sections below.

Deterministic tests: `tests/W124_stageA_sunset_graded_vs_LW_CLOP.py` (16/16, exit 0) and
`tests/W124_stageB_overlap_kite_cuts.py` (11/11, exit 0). Units `M = 1`, normal mass `m = 0.3`
(`m -> 0` sends the sunset threshold `(2M+m)^2 = 5.29` to exactly `4M^2`). Normalizations: all
statements are sign/ratio statements in a fixed positive normalization (subtractions and overall
positive constants dropped; they do not affect Im or any comparison).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **The ghost** | (i) keep-and-grade real-mass Krein-graded state; (ii) Lee-Wick conjugate pair `a_pm = M^2 +- iMGamma` with residual Feynman `eps` | BOTH computed on the same two-loop objects; the comparison is the result |
| **Cutting rules** | (i) real-axis Cutkosky, weight `(-1)^{n_ghost}`; (ii) the pair contour, order of `(Gamma, eps)` limits explicit | the order-of-limits parameter is exhibited, not assumed |
| **The two-loop topology** | (a) sunset (the only cut is the 3-particle cut; two ghosts); (b) kite (overlap; one ghost, shared line) | both; the CLOP locus lives in (a), the overlap structure in (b) |
| **Positivity** | Krein-graded optical theorem only | W48 gate discipline: nothing here is loop positivity |

## 1. Stage A -- the sunset at the mixed threshold (the CLOP object)

The sunset `S(s; M^2, M^2, m^2)` has exactly one cut: the three-particle (ghost, ghost, normal)
cut opening at `s = (2M+m)^2` (`-> 4M^2` as `m -> 0`), with `n_ghost = 2` (EVEN). Its Im part is
computed through the exact sub-bubble nesting `Im S = (1/pi) int dmu^2 Im B(mu^2; a1,a2) Im b0(s;
mu^2, a3)`, controlled by: PC1 (bubble quadrature vs closed form to 1e-6), PC2 (cut formula vs Im
of the analytic continuation `S(s + i delta)`, agreement to < 2 percent -- this is also the
dispersion-consistency check for the graded object), PC3 (all-massive threshold exponent fitted
1.9865 vs the exact 3-body phase-space value 2).

**Graded fixed order (persona 1 + 3).** Ghost residue `(-1)` per line, so the sunset prefactor is
`(-1)^2 = +1`: `Im S_graded = + Im S_ordinary(M,M,m)`, zero below `5.29`, positive above
(`s = 5.5: 0.0063`, `6.0: 0.06874`, `8.0: 0.8356`, `12.0: 3.8498`). Two different regulator routes
(`s + i delta` vs propagator `eps`) and the closed cut formula agree to < 2 percent (G2): **there
is no order-of-limits parameter anywhere in the graded fixed-order amplitude.** W120's P3
(one-loop toy) is hereby confirmed on the true two-loop object: the even two-ghost cut is positive
and Cutkosky-unambiguous in the graded theory.

**Lee-Wick proper (persona 2).** Each ghost line is `-(1/2)[P(a_+) + P(a_-)]`; the two-ghost
channel decomposes with weights `(++): 1/4, (--): 1/4, mixed: 1/2`. The mixed sub-bubble
`b0(mu^2; a_+, a_-)` is REAL on the whole real axis for every width (Schwarz pairing; numerically
`|Im| < 1e-8` at `Gamma/M` from 0.05 to 1.0, L1) even though its branch point `(m_+ + m_-)^2` is
exactly real: at exact conjugacy the mixed threshold carries no real-axis discontinuity. Hence
`Im S_LW = 0` on the entire two-ghost cut (L2: `~ 2e-6` vs graded `0.069` and `1.446`).

**The CLOP ambiguity, computed (persona 2's negative control).** The removal prescription retains
a residual Feynman `eps` alongside the pair width `w = M*Gamma`; effective pole masses
`M^2 + i(w - eps)` and `M^2 - i(w + eps)`. The order of the `(Gamma, eps) -> 0` limits changes
the answer:

| Limit order / deformation family | `Im S_LW / Im S_graded` at `s = 6` |
|---|---|
| ORDER L (`eps -> 0` first; LW proper, conjugate pair exact) | `+0.0000` |
| per-line asymmetric, `eta_2 -> 0` first (mixed term, weight 1/2) | `-0.4998` |
| per-line asymmetric, `eta_1 -> 0` first | `+0.4998` |
| ORDER F (`Gamma -> 0` first; Feynman recovered) | `+1.0079 -> 1` (eps-sequence 1.3212, 1.1060, 1.0352, 1.0079 monotone) |

The CLOP difference between the two orders of the eps-family is `Delta = 0.069284` vs
`Im S_graded = 0.068740` (ratio 1.008, C2): **the two-loop ambiguity width equals exactly the
graded two-ghost cut.** Negative control C4: at matched `eps` the order-F pair computation is
bit-identical (1.6e-12) to a real-mass no-pair sunset, whose limit is the graded cut -- the
order-of-limits sensitivity exists only when the complex pair survives the limit. The nonzero
difference REPRODUCES the known ambiguity (Anselmi-Piva's diagnosis), validating the machinery;
the symmetric/proper order (0) is the average/fakeon-like answer.

**The state-space arithmetic (personas 3 + 4, new structural point).** Admissible cut weights
from ANY state-space assignment with Krein signs `+-1` and integer multiplicities are integers in
units of the positive phase-space cut. The CLOP band's endpoints are `0` (removal: no ghost pair
in the spectrum) and `+1` (graded: Krein-even pair), and these are the ONLY state-space-realizable
values; the intermediate `+-1/2` answers are optical-theorem orphans realizable by no Krein-signed
spectrum (K1, exact arithmetic). Reading: **the CLOP ambiguity at the mixed threshold is the
removal prescription failing to decide how much of the graded cut to keep, and the only consistent
resolutions are the two families' own answers.** The graded optical theorem (weight
`(-1)^{n_ghost}`) and the removal optical theorem (ghost-free spectrum) are each internally
consistent; the deformation intermediates are not.

**W48 leak at two loops (persona 3).** The one-ghost sunset `(M, m, m)` has an ODD cut: graded
`Im S(s=4) = -0.4524 < 0` (K2). The parity map `(-1)^{n_ghost}` and the disjoint-loci structure
(odd loci leak, even loci differ-by-ambiguity) are confirmed on true two-loop objects.

**The resonance window (persona 5's guard, R1/R2).** On a Schwarz-real model self-energy with
`Im Sigma(s + i0) = + g s` (the W51 ghost sign), the dressed ghost inverse propagator has a
physical-sheet (principal-branch) complex pole pair (`z = 0.933 + 0.257 i` at `g = 0.3`), while
the normal-sign case has no principal-branch root in the resonance region (grid minimum
`|f| = 0.31`): inside the window the graded theory's own resummed propagator IS a Lee-Wick-type
pair, and the contour question returns (W120's verdict, now at the object level). Window
smearing at `Gamma/M = 0.5`: the Breit-Wigner-dressed graded two-ghost spectral weight is
`0.34 / 0.61 / 0.92` at `mu^2 = 3.2 / 4.0 / 4.8` vs fixed-order `0 / 0 / 1.28` vs LW proper
`0 / 0 / 0` -- all three prescriptions visibly split inside `|s - 4M^2| <~ 4 M Gamma`. Fixed-order
statements are trusted only outside it; for the broad gravitational ghost that window is `O(M^2)`.

## 2. Stage B -- the genuinely overlapping topology (kite, one ghost line)

Kite with the ghost on the SHARED line (mass `M`, heavy: `M > 2m`, the gravity-relevant pattern),
four normal lines of mass `m`. Cuts and parity (exact): `{1,2}`, `{3,4}` two-particle, ghost-free,
weight `+1`, threshold `(2m)^2`; `{1,4,5}`, `{2,3,5}` three-particle, one ghost, weight `-1`,
threshold `(2m+M)^2`.

- **B1 (EXACT): no CLOP locus with one ghost line.** Under the LW pair every ghost-containing
  threshold is an off-axis conjugate pair (`Im thr = +-0.08` at `Gamma/M = 0.05` up to `+-1.55`
  at `1.0`); a real mixed pinch needs `m_+` and `m_-` in the SAME cut, i.e. at least two ghost
  lines. The CLOP danger is confined to Stage A's sunset-type channels.
- **B2 (NUMERICAL-CONTROLLED): prescriptions agree on the ghost-free cuts.** The even-cut
  sub-amplitude is the triangle with the ghost virtual. `Re tau_LW -> Re tau_graded` as
  `Gamma -> 0`, monotonically, `O(Gamma)` above thresholds and `O(Gamma^2)` below, with
  extrapolated residuals `~ 1e-3` at all sampled `s` (0.2, 1.0, 3.0, 6.0 -- below and above the
  odd threshold). The residual difference is the internal-mass discontinuity
  `tau_LW - tau_graded -> -(1/2) disc_a T`, purely imaginary; two routes (pair difference at
  `w = 5e-3` vs the direct delta-slice integral) agree to 3 percent (`1.3984 i` vs `1.4391 i`,
  B2c). It feeds the odd-cut bookkeeping, not the even cuts.
- **B3: the odd-ghost leak at the overlap topology.** The three-particle ghost cut is a
  manifestly positive Dalitz integral (spectator denominators bounded below by
  `(m+M)^2 - m^2 > 0`, exact): at `s = 1.3 (2m+M)^2`, `I_odd = 0.0424`, graded contribution
  `-0.0849 < 0` (Krein `-1`, two mirror cuts), normal-line control `+0.0849 > 0`. LW: zero (B1).
  The one-loop W48 pattern -- differ on ghost cuts, agree elsewhere -- reproduces at the
  genuinely overlapping two-loop topology.
- **B4 (skeptic's hunt, came back empty): no graded own-ambiguity.** The candidate failure mode
  was the triangle anomalous threshold (leading Landau singularity) with the heavy shared ghost.
  For internal `(m, M, m)` and light legs, no `det Q = 0` root carries an all-positive alpha
  vector (roots at `s = -0.64` and `0`, both sign-indefinite), while the classic heavy-leg
  control configuration IS detected by the same machinery (`s = 3.64`, all-positive alpha):
  the anomalous threshold is absent from the graded physical region for the heavy-ghost mass
  pattern. Combined with regulator-order independence (Stage A G2) and the standard cutting
  equations for real-mass diagrams (ARGUED, 't Hooft-Veltman), the graded prescription develops
  NO ambiguity of its own at two loops; its remaining exposure is the resonance window, which is
  a domain-of-validity bound, not a contour ambiguity.

## 3. Stage C -- spin-2 tensor numerators: OPEN

Not computed. What would be needed: the massive spin-2 polarization sum inserted on the two cut
ghost lines of the sunset (and the shared line of the kite), decomposed on the spin projectors
with the normalization the repo's `m2_eff` band fixes for the spin-2 sector. Structural
expectation, stated as ARGUED only: on-shell polarization sums are positive-definite kinematic
factors, so tensor numerators multiply each cut by a positive form factor and cannot flip the
`(-1)^{n_ghost}` parity structure; the derivative vertices grow with `s` (W55's proxy) and can
change magnitudes and UV behavior but not the sign/ambiguity pattern established here. Stage C is
left OPEN; nothing in this file's verdict depends on it.

## 4. Verdict and what it does to the trade map

**VERDICT: PRESCRIPTION-DEPENDENT-AT-GHOST-CUTS / GRADED-UNAMBIGUOUS-AT-FIXED-ORDER /
LW-CLOP-AMBIGUITY-WIDTH-EQUALS-THE-GRADED-CUT / AGREE-ON-GHOST-FREE-CUTS.** In detail: the two
prescriptions agree (as `Gamma -> 0`) on every ghost-free cut, at both two-loop topologies; they
differ on every ghost-containing cut -- at odd loci by the graded leak (graded negative vs LW
zero), at the even mixed locus `s ~ 4M^2` by the full cut (graded `+Im S_gg` vs LW `0`), with the
LW side additionally CLOP-ambiguous there by exactly one graded-cut's width. This SHARPENS W120's
disjoint-loci map in three ways:

1. W120's "the two families pay at disjoint thresholds" survives, but with a refinement: the even
   locus is not merely "where removal risks ambiguity" -- it is also a locus of genuine
   inter-family disagreement (`+1` vs `0`), even before the ambiguity.
2. The CLOP ambiguity is quantified and reinterpreted: its width equals the graded cut, its
   endpoints are the two families' own answers, and its intermediate values are realizable by no
   state space. The ambiguity is the removal contour failing to decide between the families,
   not an independent third pathology.
3. The graded side's fixed-order cleanliness is now verified at two loops on both topologies,
   including the overlap structure and the anomalous-threshold hunt; the only graded exposure
   remains the resonance window, where its own resummed propagator becomes a physical-sheet
   complex pair (verified on a model) and the two families' constructions converge structurally
   while their fixed-order answers still differ.

For H59 the settling object of W120 section 7 is now computed at scalar core: what remains of it
is Stage C (tensor numerators) and the finite-width LW boundary value by full Euclidean
continuation (the one ARGUED step on the LW side). The physical-subspace optical-theorem sign
(the W48 gate) is untouched and remains the frontier blocker.

## 5. What this does NOT do

No spin-2 tensor numerators (Stage C OPEN). No full renormalized kite amplitude (per-cut objects
only). No finite-width LW boundary value via Euclidean continuation (the regulated-convolution
definition of the LW absorptive part is the named ARGUED step). No claim that keep-and-grade loop
positivity holds; the W48 leak stands and is reproduced at two loops (K2, B3a). No resolution of
the resummed-contour question inside the window. No canon / RESEARCH-STATUS / claim-status /
verdict / posture change. **H59 remains OPEN.**

**Artifacts:** this file + `tests/W124_stageA_sunset_graded_vs_LW_CLOP.py` (16/16, exit 0) +
`tests/W124_stageB_overlap_kite_cuts.py` (11/11, exit 0).
