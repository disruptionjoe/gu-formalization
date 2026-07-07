---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "VG-V8 (route V8, T5' map attempt): CONSTRUCTED AT KINEMATIC GRADE, WITH A PRICED INVOICE. The ghost parity is Clifford-native on the triplet sector — P_ghost = −(internal spacelike volume)|_W identically in (9,5) AND (7,7) (residuals 3.7e-14 / 7.1e-14) — so the mirror projector (I + Q5)/2 is a native two-term direction inside V1's target set, and the condensate map phi ↦ phi·Pi_mirror gaps all 96 mirrors at m = phi while keeping all 96 generations EXACTLY massless with [M, P_ghost] = 0: T3''s advertised payoff (mirrors gapped, generations light, positivity intact), delivered kinematically. The sign-and-regime antonym resolves: 'decreased VEV' is the generation-sector effective mass |mu − q·phi| passing through zero while the condensate is LARGE and formed. What remains imported: one orientation Z2 (which half is physical), the scalar/volume alignment (dynamics, unbuilt), and V1's Yukawa-typing caveat. Adverse findings delivered with the positive: the base leg is DEAD (chi_base|_W = −I annihilates every base-odd channel — Mannheim's own gradient cannot enter; conf_base data enters only as a scalar coefficient), and the Spin(10) 16/16bar refinement grading is P-ODD ({chi_int, P} = 3.8e-15), closing R3's last trace-level chirality readout. The count stays OPEN."
grade: "CONSTRUCTIVE KINEMATIC THEOREM (scope: the 192-dim triplet sector of the (9,5) carrier with full (7,7) cross-check of every headline identity; the target-set characterization is exact given the measured anchors; the negative/refutation statements are exhaustive over (i) all base Clifford channels, (ii) all 256 internal odd Clifford monomials, (iii) V1's enumerated native algebra (cited), and NOT over family-tensor directions (35 cells x 256 dims), non-monomial combinations beyond the scanned sums/products, or position-dependent operators on an actual Y14; no dynamics, no chirality selection, no count). Anchors reproduced first: rank(Gamma) = 128, ker = 1664, triplet 192, Krein (+96, −96, 0), beta_S residual 0.0e+00, |K|-eigs on W exactly 1. Target-import guard clean: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, or divided by — all counts (96, 48, 32, 256, 9216, 18432) are measured outputs. Controls with discriminating power: random pure-E⁻ elements sorted-split at 0.05–0.11 while |m|-splitting at ~2e-14 (the blindness lemma), mixed randoms split both metrics, unrestricted randoms break [M,P] at 1.41, and the wrong-orientation/wrong-subset volume controls fail the parity identity. R1–R4 cited only as committed docs."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - explorations/big-swing-2026-07-06/VG-V1-condensate-ghost-parity-scan.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-06/R3-pt-phase-classification-gu-cores.md
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - papers/drafts/Transcript into the impossible.md
scripts:
  - tests/big-swing/vg_v8_t5_map_attempt.py
---

# VG-V8: the T5' map attempt (VEV = condensate, the federation's center)

**Route V8 of the 2026-07-06/07 gauntlet.** T5' is the tri-theory federation's load-bearing
identification (steelman 4.2): Weinstein's total-space VEV [transcript 00:46:40] = Mannheim's
conf_base condensate. The steelman killed it in three layers (domain, transformation type,
datum class) and Panel B added the antonym: chirality is conditioned on a DECREASED VEV while
scale genesis needs a FORMED condensate — "a single switch simultaneously thrown on and thrown
off" (5.2 item 3). VG-V1 then handed T5' a falsifiable target: the map must deliver, on the
192-dim triplet sector `W`, a K-self-adjoint direction that is **P_ghost-even AND
chi-non-commuting** — such directions exist on the Krein module (V1's random controls split at
~4e-3) but were absent from V1's enumerated native algebra, and the natural Mannheim image (the
fiber scale direction) acts as the identity on `W`.

**Outcome: the map is CONSTRUCTED at kinematic grade — the landing zone V1 demanded turns out
to be native after all, one level below where V1 looked — and the antonym resolves. The price
is stated exactly, and two new adverse findings land with the positive.**

Script: `tests/big-swing/vg_v8_t5_map_attempt.py` (exit 0; every number below is printed by
it). Machinery reused verbatim from the verified carrier recipe (V1 /
`tests/generation-sector/ghost_parity_krein.py`); quaternionic structure from
`tests/big-swing/c07_kramers_regression.py`.

## 0. Anchors (reproduced before any claim)

(9,5) carrier, timelike = {4..8}: rank(Gamma) = 128, dim ker = 1664, triplet dim 192, su(2)+
Casimir top eigenvalue 8.0 (measured), beta_S pseudo-anti-Hermiticity 0.0e+00, triplet Krein
signature (+96, −96, 0:0), |K|-eigenvalues on `W` all exactly 1.000 (so `K|_W` is an involution
and **P = sign(K) = K|_W itself**, residual 3.7e-14), chi an involution with {P, chi} = 0
(5.3e-14), [K, su(2)±] ~ 1e-13. The (7,7) block reproduces its own anchor set (rank 128, ker
1664, triplet 192, Krein (+96, −96)).

## 1. The structural theorems (why the map has a native landing zone)

Three degeneracies of the triplet sector, all measured at ~1e-13, jointly force the headline
identity:

1. **`W` is invariant under the internal Clifford action.** All 10 internal gammas preserve `W`
   (max residual 1.0e-13) and satisfy the Clifford relations ON `W` ({g_i, g_j} = 2 eta_ij,
   1.0e-13). Base gammas do NOT preserve `W` (residual 13.9 — the contrast control).
2. **The base Clifford volume degenerates: chi_base|_W = −I** (3.7e-14). Corollary (the
   base-leg kill): every monomial with an odd number of base gammas anticommutes with chi_base,
   so its compression to `W` **vanishes** — measured: c(e0), c(X_base), e0e1e2 all ~5e-14.
3. **The fiber scale degenerates: etaV|_W = +I** (V1's finding, reproduced).

Since `K = etaV (x) beta_S` and `beta_S` is the product of the nine spacelike gammas =
(base volume)·(internal spacelike volume), the three degeneracies collapse `K` on `W` to minus
the internal spacelike volume. Machine-checked as an operator identity, not an isospectrality:

> **THE IDENTITY.** `Q5 = (e9 e10 e11 e12 e13)|_W = −P_ghost` — all 192x192 entries, residual
> **3.7e-14** in (9,5); the same statement `i·(e11 e12 e13)|_W = −P_ghost` holds in (7,7),
> residual **7.1e-14**. An odd permutation of the factors (orientation flip) gives +P (measured).
> **The ghost parity is the compressed internal SPATIAL volume element, up to orientation.**

Status of the datum: `Q5` commutes with the internal compact so(5)_s ⊕ so(5)_t and with both
family su(2)± actions, but internal **boosts anticommute with it** (7.3e-14) — `Q5` is
equivariant only under the maximal compact subgroup. It is a Cartan-involution datum: exactly
the space/time-split choice that `K` itself (product of spacelike gammas) already presupposes.
So calling `Q5` native imports nothing the repo's Krein quantization has not already imported —
except the **orientation Z2**. This refines VG-V2 (K implements the Cartan involution; K = the
ghost parity): the Cartan involution now has an explicit Clifford-monomial realization on `W`.

`J_quat` (the C-07 quaternionic structure) preserves `W` (1.0e-13), squares to −I on `W`, and
**fixes K, P, chi, and Q5** under conjugation (1.3e-13): the whole apparatus is
quaternionically real, all spectra below have even multiplicities (96/48/32 everywhere — the
C-07 Kramers wall persists inside the target set), and the orientation sign cannot be rotated
away quaternionically.

**Adverse finding (R3's open item 2, answered).** The Spin(10)-internal 16/16bar grading
`chi_int` **anticommutes with P and with K** ({chi_int, P}/|·| = 3.8e-15; [chi_int, P]/|·| =
2.00; same in (7,7)). The physical (P = +1) sector is therefore not chi_int-invariant: physical
states are maximally entangled 16 + 16bar combinations, no 16-vs-16bar decomposition of the
physical sector exists, and the "16/16bar refinement" — flagged by
`R3-pt-phase-classification-gu-cores.md` and `BIG-SWING-CONFORMAL-CLASS-BLOCKED.md` as the
canon hope's last untested trace-level chirality readout — **closes, adversely**: the
achirality fence extends from chi to chi_int.

## 2. (a) The target set, characterized exactly

On `W`, with P-blocks `W_±` (96 each, `K|_{W_+}` positive definite) and chi purely
off-diagonal with unitary block `c` (measured):

| space | real dim | content |
|---|---|---|
| E = K-self-adjoint ∩ P-even | 2·96² = **18432** | pairs (A, B) of K-Hermitian blocks |
| E⁺ = chi-commuting part | **9216** | B = +c†Ac; V1's lemma: exactly isospectral, no split, ever |
| E⁻ = chi-ANTICOMMUTING part | **9216** | B = −c†Ac; **the target set's linear content** |

Bijection verified numerically (parametrization residuals ~1e-14). A direction is in V1's
target set iff its E⁻ component is nonzero.

**The splitting refinement (new lemma, machine-verified).** For pure E⁻ elements, spec(M|₋) =
−spec(M|₊) exactly: they sorted-split (controls: 0.113, 0.067, 0.051) but are **|m|-BLIND**
(|m|-splits ~2e-14) — mirror and generation mass magnitudes coincide. **Genuine
mirror-selective gapping (|m| splitting) requires BOTH an E⁺ and an E⁻ component** — an
even+odd mix (mixed random controls split both metrics at ~0.05–0.09). V1's necessary condition
is thereby sharpened to a necessary-and-sufficient shape: nonzero E⁻ component for signed
splitting, nonzero E⁺·E⁻ mix for magnitude splitting.

**Orbit/decomposition under the structures GU carries.** Measured: W₊ carries su(2)+ weights
{−2, 0, +2}×32 (triplet × 32), su(2)− weights {±1}×48 (doublet × 48), and a uniform so(5)_s
(and so(5)_t) spinor Casimir (value 2.500, single isotype):

> W₊ ≅ (3 of su(2)+) ⊗ (2 of su(2)−) ⊗ (4 of so(5)_s) ⊗ (4 of so(5)_t), 3·2·4·4 = 96.
> E⁻ ≅ Herm(W₊) decomposes under su(2)+ × su(2)− into **36 = (1+3+5)(1+3) family cells of 256
> real dims each** (the internal 16 ⊗ 16bar block); ad-Casimir moment fractions of a random E⁻
> element: measured [0.111, 0.337, 0.551] vs rep theory [0.111, 0.333, 0.556].

**The Clifford-native slice.** All 256 internal odd Clifford monomials with even timelike count
land in E⁻ (each verified P-even and chi-anticommuting), and their real span is **exactly 256 =
one family cell** — the family-scalar (j₊, j₋) = (0,0) cell, verified by [·, su(2)+] ~ 2e-13.
`Q5` sits inside it. The other 35 cells (8960 dims) require family-tensor data no fiber
Clifford element supplies: they remain import territory.

**The monomial grammar** (verified on every scanned monomial, both signatures):

| property | rule |
|---|---|
| P-parity of a compressed monomial | (−1)^(# timelike factors) |
| chi-(anti)commutation | (−1)^(total grade) |
| K-self-adjoint phase | direct if g(g−1)/2 even, i· if odd |
| target-set membership | ODD grade with EVEN # timelike factors |
| any odd # of base factors | compression VANISHES (chi_base = −I) |

## 3. (b) The pushforward scan

| channel | class | on W | parity | chi-rel | SPLIT | \|m\|SPLIT |
|---|---|---|---|---|---|---|
| Lambda²₊ spin-only SD Cartan | base-2form | {−1,0,+1}×32 | EVEN | comm | 3e-15 | 3e-15 |
| Lambda²₋ spin-only ASD | base-2form | **DEAD** (1e-28) | — | — | — | — |
| c(e0) = gradient d(phi) direction | base-1form | **DEAD** (5e-14) | — | — | — | — |
| c(X) generic base vector | base-1form | **DEAD** | — | — | — | — |
| base 3-form e0e1e2 | base-3form | **DEAD** | — | — | — | — |
| chi_base (base volume) | base-4form | = −I | EVEN | comm | 0 | 0 |
| chi_int (16/16bar direction) | internal | nonzero | **ODD** | comm | n/a | n/a |
| T5 = e4..e8 (timelike volume) | internal | nonzero | **ODD** | ANTI | n/a | n/a |
| c(e4) internal timelike vector | internal | nonzero | **ODD** | ANTI | n/a | n/a |
| c(e13) internal spacelike vector | internal | {±1}×48 both | EVEN | ANTI | 4e-15 | 3e-15 |
| internal compact 2-form i·e9e10 | internal | nonzero | EVEN | comm | 3e-15 | 2e-15 |
| internal boost 2-form i·e4e9 | internal | nonzero | **ODD** | comm | n/a | n/a |
| internal spacelike 3-form (i·)e9e10e11 | internal | {±1}×48 both | EVEN | ANTI | 3e-15 | 3e-15 |
| **Q5 = e9..e13** | internal | **= −P** | EVEN | ANTI | **2.00** | 1e-15 |
| mixed 3-form i·e0e1e9 | mixed | {−1,0,+1}×32 both | EVEN | ANTI | 5e-15 | 4e-15 |
| Q5·(iJ₊₃) native product | product | ±{−2,0,2}×32 | EVEN | ANTI | 2e-14 | 2e-14 |
| c(e13) + Q5 | sum | {−2,0} vs {0,2} | EVEN | ANTI | 2.00 | 3e-15 |
| **Pi_mirror = (I + Q5)/2 = (I − P)/2** | **MAP** | **0×96 vs 1×96** | EVEN | mixed | **1.00** | **1.00** |
| Pi₋ c(e13) Pi₋ (dressed vector) | MAP-dressed | 0×96 vs ±1×48 | EVEN | mixed | 1.00 | 1.00 |
| mu·I + phi·Q5 (mu=1, phi=0.5) | MAP-generic | 0.5×96 vs 1.5×96 | EVEN | mixed | 1.00 | 1.00 |

Controls: random pure E⁻ ×3 (sorted-split 0.05–0.11, |m|-split ~2e-14 — the blindness lemma
has teeth), random mixed P-even ×3 (split both metrics, 0.05–0.09), unrestricted K-self-adjoint
random ([M,P]/|M| = 1.41 — V1 reproduction), wrong 5-set volume (1 timelike + 4 spacelike:
P-ODD — only the metric-selected spacelike set gives the parity).

**Source-class verdicts:**

1. **Base 2-forms / Lambda²₊ leg: CANNOT reach the target set.** Every base channel is either
   dead (odd base count — including the gradient of Mannheim's condensate) or chi-commuting
   (even base count — isospectral by V1's lemma). Exhaustive over base Clifford data.
   **Mannheim's condensate cannot enter through any base-geometric operator direction;
   conf_base data enters only as a scalar coefficient on a fiber direction.**
2. **Spin(10)-internal directions: the canon's 16/16bar hint fails, but the internal spacelike
   sector delivers.** chi_int itself is P-odd (positivity-breaking as a channel; readout-closing
   as a grading). Odd-timelike-count channels are all P-odd. Even-timelike-count odd channels
   land IN the target set — and the distinguished one, `Q5`, IS the parity: single vectors and
   3-forms give quantized symmetric spectra (no split alone), but the volume gives the maximal
   signed split.
3. **Products with native directions: stay inside the target set, add no splitting by
   themselves** (Q5·family products isospectral) — the native algebra acts on the target set as
   a module; one odd seed is what it cannot generate. The seed is `Q5`, and GU has it.

**The GU-derivable channel that lands and splits — triple-checked:** `Pi_mirror = (I + Q5)/2`:
both signatures ((9,5) max|m_gen| = 1.9e-15, mirrors exactly 1.000×96; (7,7) max|m_gen| =
1.8e-15), [M, P] = 6.3e-15 (Turok–Bateman-compatible), [M, chi]/|M| = 1.41 (outside V1's
isospectrality lemma, as required), controls discriminate, no target-integer import anywhere.

## 4. The map, stated

> **T5' (kinematic form, constructed).** Mannheim's conf_base order parameter phi(x) maps to
> the quadratic-form deformation `M(phi) = phi · Pi_mirror`, where `Pi_mirror = (I + Q5)/2` is
> assembled from the Clifford scalar and the internal spacelike volume — both fiber-native
> given the space/time-split datum the Krein form already uses, up to one orientation Z2.
> Result: all 96 mirror states gap at m = phi, all 96 generation states stay exactly massless,
> [M, P_ghost] = 0 at machine precision. Mirrors gapped, generations light, positivity intact —
> T3''s advertised payoff, and precisely the interface requirement V1 ended on.

What is native: the direction (both terms), the parity-compatibility, the split. What is
imported: **(i)** the orientation Z2 — which volume sign, i.e. WHICH half is physical (canon's
ghost-assignment freedom, now priced at exactly one sign); **(ii)** the alignment — WHY the
condensate couples with equal scalar and volume weights (the projector direction). Nothing
kinematic fixes (ii); it is the map's central physical hypothesis and the natural next
falsifiable statement for any built dynamics. **(iii)** V1's typing caveat: M(phi) is the
instantaneous quadratic-form deformation; a Yukawa-bilinear or derivative-coupled realization
could differ. Note what V1 asked for is delivered in a displaced form: V1 demanded "a conf_base
order parameter whose lift to W fails to commute with chi while commuting with sign(K)" — the
lift's operator part turns out to be necessarily fiber-supplied (the base leg is dead); the
conf_base datum supplies the coefficient field, not the direction.

## 5. (c) The sign-and-regime toy (the antonym, resolved)

Minimal 1-parameter family per hyperbolic (generation, mirror) pair, with the measured
Q5-eigenvalues (−1 on generation, +1 on mirror):

```
M(phi) = mu·I + phi·q·Q5        =>       m_gen(phi) = |mu − q·phi|,   m_mir(phi) = |mu + q·phi|

phi   :   0.00   0.25   0.50   0.75   1.00   1.50   2.00      (mu = q = 1)
m_gen :   1.00   0.75   0.50   0.25   0.00   0.50   1.00
m_mir :   1.00   1.25   1.50   1.75   2.00   2.50   3.00
```

- **phi ~ 0 — Dirac regime:** generation and mirror degenerate at mu; vectorlike.
- **phi = mu/q — the WEYL POINT:** the generation branch passes through zero — "a decreased VEV
  ... taking a Dirac equation into two Weyl equations because the mass is actually a variable"
  [00:46:40, 00:46:02] — while the condensate is LARGE and formed. Verified on the actual
  carrier: at phi = mu/q the 96 generation states are massless to 3.8e-15 while the 96 mirrors
  sit at exactly 2mu.
- **phi >> mu/q — Mannheim regime:** both bands grow ~ q·phi (scale genesis), mirrors gapped by
  2mu above generations.

**Resolution of the antonym:** the two clauses read different COMPONENTS of one order
parameter, not two values of one magnitude. "Decreased VEV" = the generation-sector effective
mass (the mu − q·phi branch) decreasing through zero; "formed condensate" = phi at the potential
minimum. One potential — e.g. V(phi) = lam(phi² − v²)² — serves both clauses iff v ≥ mu/q;
nothing computed here fixes v, mu, or q (that is a tuning condition, stated honestly). In the
**aligned limit** (mu and q from ONE condensate with equal weights — the direction Pi_mirror)
m_gen = 0 identically at every phi: both clauses hold simultaneously with **zero tuning**.

Misalignment robustness (map direction contaminated by a native even direction at relative
weight eps): gap = +1.000 (eps = 0), +0.827 (0.1), +0.134 (0.5), −0.732 (1.0) — the
mirror-selective gap survives O(1) contamination and closes near eps ~ 1. Alignment quality is
physical content nothing native fixes.

**Interpretation required, and primary-source support (flagged):** the condensate must carry an
internal-orientation (volume) component, not a scale component — sharply consistent with V1's
adverse finding that the scale direction acts trivially on `W`: *the condensate lands on the
fiber's spatial orientation, not its scale*. Weinstein's transcript supports mass-as-variable
and a total-space (fiber) VEV [00:46:02–00:46:40, transcript-exact]; nothing in the transcript
names the orientation direction. Mannheim's conformal symmetry forbids a bare v² term (the
potential is scale-free lambda·phi⁴ and any v is dynamically generated — from memory, flagged;
primary-source verification belongs to the VG-SA lane). Neither primary specifies the
alignment; that is the map's invoice, not its content.

## 6. What this buys (and costs) the federation

- **T5' (the center):** upgraded from "no map, and nowhere native to land" (V1's closing) to
  **"landing zone constructed; map = scalar coefficient × native fiber direction; invoice =
  orientation Z2 + alignment dynamics + typing."** The federation keeps its center at kinematic
  grade. No kill condition fires; the steelman's Layer-1 (domain) attack is answered in
  displaced form (the base-to-fiber pushforward exists but is a coefficient map, not an
  operator-direction map); Layer-2 (Weyl action) and Layer-3 (integer invoice) are untouched.
- **T3':** the interface requirement is met by a native direction — ghost-parity-compatible,
  mirror-selective breaking EXISTS on GU's own carrier. The sub-threshold/loop scoping and
  [P_ghost, S] = 0 through actual dynamics remain open (no S exists; unchanged).
- **The antonym (5.2 item 3):** carried obligation discharged at toy grade — sign-and-regime
  story delivered with an exact aligned limit.
- **Costs / adverse:** the 16/16bar refinement readout closes (chi_int P-odd, both signatures)
  — the canon's three-chiral-generations hope loses its last trace-level readout, as R3
  anticipated in its "if the refined grading also anticommutes with K" branch. The base
  geometric leg is dead. **The count stays OPEN**: the physical sector remains 96 = 3 × 2 × 16,
  chi-trace-achiral (canon fence intact); gapping ghosts is not selecting 3, and nothing here
  touches the 3-vs-6 extraction or the C-07 even wall (all multiplicities here are even:
  96/48/32 — Kramers persists inside the target set).
- **Relation to V1:** extended, not contradicted. V1's "the native algebra contains none" was
  proved over the chi-commuting algebra generated by {scalar, fiber scale, su(2)±,
  pseudoscalar}; its honest gap #1 named Clifford-odd elements as out of scope. V8 scanned that
  sector: the target-set members are exactly the odd-grade/even-timelike monomials, and the
  distinguished one is the parity itself. V1's headline "the mirror-selective datum is an
  import" should now be read: *the datum is native up to one orientation sign and one alignment
  hypothesis.* (Canon update candidate for `ghost-parity-krein-synthesis.md` — flagged for
  Joe's review, not applied here.)

## 7. Honest gaps

1. **Kinematic only.** No source action, no S, no dynamics: the map is an operator-direction
   identification plus a toy potential, not a derivation that Mannheim's dynamics flows the
   condensate into the Pi_mirror direction. The alignment (projector weights) is the map's
   central unproven hypothesis, and [P_ghost, S] = 0 remains uncomputable (canon's standing gap,
   sharpened by R1's non-uniqueness at degeneracies).
2. **The orientation Z2 is a genuine residual import** — it IS canon's "physical/ghost
   assignment is not canonical without dynamics," now minimized to one sign but not removed.
3. **"Native" is Cartan-relative.** Q5 is equivariant under the maximal compact only; boosts
   anticommute with it. It presupposes the same space/time-split datum as K itself — no NEW
   import, but a purist reading of "Spin(9,5)-equivariant native" excludes it (this is exactly
   the C-07 "GU-native class" boundary; the map lives on the Krein side of that boundary).
4. **Typing caveat inherited from V1:** instantaneous quadratic-form deformation; Yukawa or
   derivative realizations unprobed. A pure c(d phi) coupling is additionally suspect of being
   removable on-shell (current-coupling integration by parts — from memory, flagged) — moot
   here since that channel died kinematically anyway.
5. **Exhaustiveness limits:** family-tensor directions (35 cells × 256 dims of E⁻) unexplored;
   non-monomial internal combinations beyond the scanned sums/products not exhausted;
   everything is frozen-fiber (no position dependence, no actual Y14 geometry; base data enters
   only as a coefficient by the base-leg kill).
6. **(14,0) not run.** The monomial grammar predicts that in the Riemannian signature the
   ghost parity and the 16/16bar grading would coincide (chi_int has zero timelike factors
   there) — an interesting untested prediction, left open.
7. **The toy potential is a toy.** V(phi) = lam(phi² − v²)² is not Mannheim's potential;
   Mannheim's conformal invariance forbids the bare v (from memory, flagged); the two-regime
   reading survives in the aligned limit without any potential shape, which is the honest core
   of the resolution.
8. **The count question is not advanced.** 96 physical states with 3 × 2 × 16 structure and
   zero chi-trace; extracting 3 (not 6, not 48) remains exactly as open as canon states, and
   the closure of the 16/16bar readout makes one previously hoped route strictly harder.
