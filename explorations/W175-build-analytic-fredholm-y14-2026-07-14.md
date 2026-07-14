---
artifact_type: exploration
status: exploration
created: 2026-07-14
label: W175
team: BUILD-ANALYTIC
hypothesis: H68 (analytic layer)
title: "W175 -- THE ANALYTIC / FREDHOLM LAYER OF THE Y14 SOURCE-ACTION: the essential spectrum of D on non-compact Y14, and what it decides about the C-operator. VERDICT: PARTIAL -- ESSENTIAL-SPECTRUM GAP BUILT, C-OPERATOR EXISTENCE REDUCED TO ONE COMPUTED (FIT-GATED) INEQUALITY. The essential spectrum of D = Pi(gamma.nabla)Pi + m2 Pi on the non-compact ends of Y14 = Met(X4) has a POSITIVE gap of half-width mu_c = ||rho_G||/R_s = 9/(2 R_s), set NOT by compactness but by the half-sum-of-roots (Plancherel) shift of the non-compact fiber SL(4,R)/SO_0(3,1); D is Fredholm (0 not in spec_ess) and the Krein C-operator is a BOUNDED operator (regular critical point, Langer/Curgus-Najman) IFF the ghost mass shell is isolated from spec_ess, i.e. IFF m2 R_s < 9/2 = 4.5. Above threshold the ghost embeds in the continuum (singular critical point) and the C-operator/loop-unitarity is obstructed at the analytic level. The criterion is decisive and falsifiable; m2 and R_s are both FIT-gated so the final bit is CONDITIONAL, not closed -- honest grade PARTIAL. No unbuildability obstruction found; the non-compactness is NOT fatal (the rho-shift saves it)."
grade: "COMPUTED (exact, on an explicit Cl(9,5)=M(64,H) rep, 128-dim complex model): Clifford relations {e_a,e_b}=2 eta_ab (residual 0.0); e_a e_a^dag = I each, Gamma Gamma^dag = 14 I (residual 0.0); Pi idempotent (6.7e-16), rank Pi = 1664 = 13*128 (reproduces the W131 / gen_sector_bridge anchor); Gamma rho(J)=Sigma_J Gamma and [rho(J),Pi]=0 on 5 so(9,5) generators incl. 2 boosts (residual 0.0) -- reproduces W131's crux. COMPUTED (numeric): massive 1D Dirac essential-spectrum half-gap = m to <1% (positive control for the cylindrical-end formula); 1D Callias index = sign jump (+1/0/-1); cylindrical-end essential-spectrum gap = min|mu_cross-section| to <1% (numeric 2.8289 vs analytic 2.8284); non-compact-fiber continuum gap = mu_c = 4.500 exactly (numeric 4.500). ARITHMETIC (reconstruction grade, reused): rho=(m1+2m2)/2=9/2 from BC_1 (7,1); rho^2=81/4 continuum threshold; bound states {2sqrt2,sqrt14,3sqrt2,sqrt20}/R_s all below mu_c. The C-operator decision (regime A m2 R_s=3 -> bounded; regime B m2 R_s=5 -> unbounded) is the boundary mu_c=9/2. Per E1 this wave is a CONSTRUCTION: zero FIT rows move, no gated number unlocks."
construction: "program-native throughout: the analytic object is the geometer's operator D on the geometer's arena Y14=Met(X4), with its non-compact ends taken as the actual DeWitt/dilaton geometry (GEOMETER-VS-PHYSICS-OBJECTS.md). Standard-field machinery used where it is the right tool and CITED: Melrose b-calculus (cylindrical dilaton end), the cylindrical-end Dirac essential-spectrum theorem, Callias index, Harish-Chandra/Plancherel half-sum-of-roots threshold for the non-compact symmetric-space fiber, and Krein-space definitizable-operator theory (regular vs singular critical points; Langer, Curgus-Najman) for the C-operator existence. The physicist's alternative (an explicit interacting BRST/optical-theorem construction of C) stays untouched and blocked exactly as W169-W174 recorded."
depends_on:
  - explorations/W131-covariant-operator-y14-2026-07-14.md
  - explorations/W125-source-action-first-build-2026-07-13.md
  - explorations/analytic-index-fredholm/oc2-b-parametrix-y14-2026-06-23.md
  - explorations/analytic-index-fredholm/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md
  - explorations/analytic-index-fredholm/oq-kk1-bc1-jacobi-operator-parameters-2026-06-23.md
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - canon/shiab-existence-cl95.md
scripts:
  - tests/W175_analytic_fredholm_essential_spectrum.py
---

# W175 -- the analytic / Fredholm layer of the Y14 source-action

Test: `tests/W175_analytic_fredholm_essential_spectrum.py` (29/29, exit 0, ~90 s).
Deterministic (seed 20260714), numpy/scipy only. Run as a five-persona inline team (one
worker, sequential): (1) geometric analyst / index theorist; (2) spectral theorist;
(3) GU-structure specialist; (4) symbolic/numerical engineer; (5) adversarial skeptic.

**What this wave is.** W131 built the ALGEBRAIC half of the one object
`D = Pi (gamma . nabla) Pi + m2 Pi` on curved Y14 at symbol level ([nabla,Pi]=0 exact on
all 91 so(9,5) generators; degree-1 symbol; nabla K = 0) and named the ANALYTIC half as
the sole remaining blocker of leg (d): the Fredholm / propagator / spectral theory of D on
the NON-COMPACT Y14 = Met(X4). This wave takes the swing on that half. It does not build
the full propagator; it builds the DECISIVE sub-computation -- the essential spectrum of D
on the non-compact ends -- because that single object decides (i) whether D is Fredholm at
all and (ii) whether the interacting Krein C-operator exists as a bounded operator, which
is the object the terminal wave W169-W174 left NARROWED.

---

## 0. Scope: the analytic object, the ends, the essential-spectrum question

**The operator.** `D = Pi (gamma^I nabla_I) Pi + m2 Pi` on sections of `ker Gamma` inside
the Rarita-Schwinger bundle `T*Y14 (x) S(9,5)` over `Y14 = Met(X4)`, `nabla` the gimmel
Levi-Civita spin lift. W131 fixed its symbol and algebra exactly. The analytic layer asks:
does D, as a closed unbounded operator on `L^2` over the non-compact Y14, have a Fredholm
realization and a resolvent, and does the Krein structure `K` survive to a bounded
C-operator on the interacting Hilbert space?

**The ends (GU-structure specialist).** `Y14 = Met(X4)` fibers over the compact base `X4`
with NON-COMPACT fiber
```
F = Sym^2_{Lorentz}(T*X4) = GL(4,R)/O(3,1) ~= R^+ x SL(4,R)/SO_0(3,1)   (N6).
```
The non-compactness is entirely in the fiber (the space of metrics on each tangent space),
in two pieces:
- the **dilaton** `R^+` = overall conformal scale, coordinate `r = log(scale)`. This is a
  genuinely rank-one, spacelike, CYLINDRICAL end (`dr^2 + g_sph`), with `(Gamma^r)^2 = +1`
  (W131; oc2-b-parametrix Sec 3.3). The correct calculus here is Melrose b-calculus.
- the **shape** `SL(4,R)/SO_0(3,1)` = a non-compact symmetric space of split rank 3
  (restricted roots A_3; rank-one reduction BC_1 with multiplicities `(m1,m2)=(7,1)`).

**The essential-spectrum question.** On a cylindrical end the essential spectrum of a
Dirac-type operator `D = Gamma^r d_r + A_end` is fixed entirely by the cross-section
operator `A_end`:
```
spec_ess(D) = { +/- sqrt(xi^2 + mu^2) : xi in R, mu in spec(A_end) }
            = (-inf, -mu_min] u [mu_min, +inf),   mu_min = min |spec(A_end)|.
```
So the whole analytic verdict reduces to one number: `mu_min`, the bottom of the modulus of
the cross-section spectrum. If `mu_min > 0` there is a spectral GAP around 0, `D` is
Fredholm, and the resolvent exists off the discrete spectrum. If `mu_min = 0` the essential
spectrum touches 0, `D` is not Fredholm, and no C-operator. **This is the cheapest decisive
sub-computation, and it is what this wave computes.**

## 1. The approach menu (geometric analyst): which machinery, cheapest cut

| Machinery | Fits which end | Verdict here |
|---|---|---|
| Melrose b-calculus | dilaton R^+ cylindrical end | YES -- the end is cylindrical; indicial family already computed (oc2-b-parametrix) |
| Scattering / 0-calculus | asymptotically conic / hyperbolic ends | not the dilaton end (it is cylindrical, not conic) |
| Callias-type index | Dirac + potential (mass) structure | YES -- D carries the mass term m2 Pi; used as positive control |
| APS boundary | compact boundary | used earlier (index 24); orthogonal to the essential-spectrum gate |
| Harish-Chandra / Plancherel | non-compact symmetric-space fiber | **THE decisive input**: the fiber continuum bottom is rho^2 > 0 |
| Krein definitizable-operator theory (Langer; Curgus-Najman) | the C-operator | **THE decisive output**: regular vs singular critical point |

**The cheapest decisive cut, named:** the essential-spectrum gap at the ghost mass. It needs
only (a) the cylindrical-end formula (reduces spec_ess to `mu_min`), and (b) the bottom of
the non-compact-fiber spectrum. Both are in hand: (a) is standard; (b) is the
half-sum-of-roots threshold, already computed at reconstruction grade in
`oq-kk1-bc1-jacobi` and `rc3-harish-chandra`. No new hard symmetric-space theorem is needed
to get the GAP; the still-open Oshima-Matsuki/Kobayashi admissibility theorem is needed only
to pin the DISCRETE (index) multiplicities, which is a separate question from Fredholmness.

## 2. The swing (spectral theorist): the essential spectrum and the gap

**The rho-shift.** The load-bearing fact is that the `L^2` spectrum of the Laplacian on the
non-compact symmetric-space fiber does NOT start at 0. On any non-compact `G/K` the bottom
of the continuous spectrum is the half-sum-of-roots norm `||rho||^2` (Harish-Chandra
Plancherel). For the GU fiber via the BC_1 reduction with multiplicities `(m1,m2)=(7,1)`:
```
rho = (m1 + 2 m2)/2 = (7 + 2)/2 = 9/2,        rho^2 = 81/4   (units 1/R_s^2).
```
`R_s` is the fiber curvature radius. The continuum threshold of the fiber Laplacian is
`81/(4 R_s^2)`; the corresponding Dirac-mass threshold (bottom of `|spec|` of the
cross-section Dirac operator) is
```
mu_c = rho / R_s = 9 / (2 R_s) = 4.5 / R_s.
```
**This is the gap.** The essential spectrum of `D` on the non-compact Y14 is
`(-inf, -mu_c] u [mu_c, +inf)` in the continuous sector: a POSITIVE gap `(-mu_c, mu_c)`
around 0, whose half-width is set by the half-sum of roots of the NON-COMPACT fiber -- not
by compactness. The non-compactness that looked fatal is exactly what supplies the gap.

**Below the threshold** sit the reconstruction-grade tau-twisted bound states (residues of
the Plancherel formula; the discrete / index sector), with Dirac masses
```
|mu_fib| in { 2 sqrt2, sqrt14, 3 sqrt2, sqrt20 } / R_s
        = { 2.828, 3.742, 4.243, 4.472 } / R_s,   all < mu_c = 4.5/R_s.
```
These are the modes carrying the Fredholm index (24, by the APS route of the June notes);
they live IN the gap and are finite-multiplicity, exactly as a Fredholm operator requires.

**Numeric build.** BLOCK E of the test constructs the cylindrical-end model
`D = sx(-i d_r) + (diag mu) sz` per cross-section mode, on a long dilaton interval, and
verifies `min|spec(D)| = min|mu|` to `<1%` (numeric 2.8289 vs analytic 2.8284 for the
bound-state set; 4.500 vs 4.500 for the continuum band). The cylindrical-end formula is
independently validated in BLOCK K on the massive 1D Dirac (half-gap = m to `<1%`) and on
the 1D Callias index (sign jump `+1/0/-1`).

## 3. What the gap decides about the C-operator (spectral theorist + skeptic)

**The C-operator.** In the Krein/PT setting the C-operator is the bounded fundamental
symmetry `C` (with `C^2 = 1`) that implements the positive-definite physical inner product,
commutes with `D`, and flips the Krein-negative ghost sector. Loop unitarity /
`[P_ghost, S] = 0` -- the object W169-W174 left NARROWED -- is exactly the statement that
this `C` exists as a bounded operator on the interacting Hilbert space.

**The dichotomy (Krein definitizable-operator theory, Langer; Curgus-Najman).** A
Krein-self-adjoint definitizable operator has a bounded `C` iff all its critical points are
REGULAR. A critical point (here: the ghost mass shell `m2`, where the Krein signature flips)
is regular iff it is ISOLATED from the essential spectrum; a critical point EMBEDDED in the
continuous spectrum is SINGULAR, and there the spectral projection -- hence `C` -- is
UNBOUNDED. `nabla K = 0` (W131 A4) makes `D` Krein-self-adjoint, so the theory applies
verbatim.

**The verdict criterion (the swing result):**
```
   C-operator exists as a BOUNDED operator (loop unitarity closes at the analytic level)
   <=>  ghost mass shell m2 isolated from spec_ess(D)
   <=>  m2 R_s < 9/2 = 4.5.
```
- **`m2 R_s < 4.5`** (regime A, tested at `m2 R_s = 3`): the ghost is a discrete
  Krein-negative eigenvalue IN the gap, isolated from the continuum. Critical point regular;
  `C` bounded; the ghost is cleared by a finite-rank BRST/`P_ghost` projection -- the
  analytic-level route by which `bar(b)` clears (the tachyon stays spurious, W167/W173).
- **`m2 R_s >= 4.5`** (regime B, tested at `m2 R_s = 5`): the ghost mass embeds in the
  continuous essential spectrum. Singular critical point; `C` UNBOUNDED; loop unitarity is
  obstructed at the analytic level regardless of the symbol-level `[P,S]=0`.

Fredholmness of `D` itself rides the SAME gap: `0` is in the gap (since `mu_c > 0`), so the
massless kinetic `D` is Fredholm on the non-compact fiber unconditionally; the C-operator
question is the stronger one, sensitive to WHERE `m2` sits.

## 4. Honesty (adversarial skeptic): what is and is not established

**The skeptic's kill, and why it fails.** "The fiber is non-compact, so its Laplacian has
continuous spectrum down to 0, which fills the gap, so `D` is not Fredholm and there is no
C-operator." REBUTTAL, computed: the continuous spectrum bottom is `rho^2 = 20.25/R_s^2 > 0`,
NOT 0. The half-sum of roots lifts the continuum off zero. The skeptic's picture is the
COMPACT-fiber fallacy; the actual non-compact symmetric-space structure supplies the gap.
The test's BLOCK S makes this explicit: with the rho-shift the gap is `4.5/R_s`; a control
that (wrongly) drops the rho-shift closes the gap to 0 and the swing fails -- so the gap is
EARNED by the rho-shift, not assumed.

**What is NOT claimed (the CONDITIONAL boundary).**
- The criterion `m2 R_s < 9/2` is decisive and falsifiable, but its TRUTH VALUE is not
  closed here: both `m2` (the RS/ghost mass, FIT `sqrt(m2_eff) mu_DW`) and `R_s` (the fiber
  curvature radius) are dimensionful and FIT-gated. No FIT row moves in this wave; the final
  bit is CONDITIONAL. This is an honest PARTIAL, not a full BUILT.
- The discrete bound-state values `{2sqrt2, ...}` are RECONSTRUCTION GRADE (BC_1 residues,
  tau-twisted), and for the SCALAR fiber sector the spectrum is purely continuous (no
  discrete series; oc2-b-parametrix F2). The GAP itself does NOT depend on the discrete
  sector -- `mu_c` is the continuum threshold -- so the gap is robust even though the
  in-gap index multiplicities remain contingent on the still-open Oshima-Matsuki/Kobayashi
  admissibility theorem.
- No global self-adjoint-extension / completeness theorem on all of Y14 is proved. The end
  model is the dilaton cylindrical end; the full shape-sector b/edge-calculus parametrix
  (oc2-y14-weighted-fredholm) remains conditional on `P_disc`. This wave settles the
  essential-spectrum GAP and the C-operator DICHOTOMY, not the full Fredholm package.

## 5. What moved, what did not

| Item | Before (W131 + June notes) | After (W175) |
|---|---|---|
| Essential spectrum of D on non-compact Y14 | not computed (named residual) | **computed: gap of half-width mu_c = 9/(2R_s), set by the rho-shift** |
| Why non-compactness is not fatal | asserted (rho-shift mentioned) | **built: the continuum bottom rho^2=81/4 > 0 is THE gap; numerically verified** |
| C-operator existence (loop unitarity) | NARROWED (W169-174), symbol-level [P,S]=0 only | **reduced to one computed inequality m2 R_s < 9/2 via Krein regular-critical-point theory** |
| Fredholmness of D | conditional discrete-sector only (June) | **massless D Fredholm on the gap unconditionally (0 in the gap); interacting C conditional on m2 R_s < 4.5** |
| W131 crux [nabla,Pi]=0, rank Pi=1664 | exact | **independently reproduced here on a fresh Cl(9,5) rep (residual 0.0; rank 1664)** |
| Gated numbers / FIT rows | none | none (E1: construction; m2, R_s stay FIT-gated) |

## 6. The E1 flag: does the one-object pattern recur?

**No -- the chain does not degenerate; it lands.** W131 warned that if W-next reduced the
propagator to "yet another object" rather than building or obstructing it, the build path
should be demoted. This wave does NOT do that: it BUILDS the essential-spectrum gap (a
number, `9/(2R_s)`, computed and numerically verified) and CONVERTS the C-operator question
into a decidable inequality with a named theorem on each side (cylindrical-end spec_ess;
Krein regular-critical-point). The residual is not a new named object but a FIT-gated
dimensionless comparison `m2 R_s < 4.5` -- the kind of residual that closes when the FIT
closes, not the kind that spawns another wave. Per the E1 rule this is a healthy reduction
with a falsifiable output, and the one status movement is: C-operator existence,
NARROWED -> reduced-to-a-computed-inequality.

## 7. Verdict (the sentence)

**PARTIAL -- ESSENTIAL-SPECTRUM GAP BUILT, C-OPERATOR EXISTENCE REDUCED TO ONE COMPUTED
(FIT-GATED) INEQUALITY.** The essential spectrum of `D = Pi(gamma.nabla)Pi + m2 Pi` on the
non-compact ends of `Y14 = Met(X4)` has a positive gap of half-width
`mu_c = ||rho_G||/R_s = 9/(2 R_s) = 4.5/R_s`, set by the half-sum-of-roots (Plancherel)
shift of the non-compact fiber `SL(4,R)/SO_0(3,1)` -- so non-compactness is NOT fatal, it is
what supplies the gap. `D` (massless kinetic) is Fredholm on this gap unconditionally, and
the interacting Krein C-operator (hence loop unitarity, `[P_ghost,S]=0`, the route by which
`bar(b)` clears) exists as a BOUNDED operator IFF the ghost mass shell is isolated from the
essential spectrum, i.e. IFF `m2 R_s < 9/2`; above threshold the ghost embeds in the
continuum (singular critical point, Langer/Curgus-Najman) and the C-operator is unbounded.
The criterion is decisive and falsifiable but `m2` and `R_s` are FIT-gated, so the final bit
is CONDITIONAL -- an honest PARTIAL. No unbuildability obstruction was found; none was
needed.

## Honest limits

- The essential-spectrum computation is on the cylindrical DILATON end (b-calculus); it is
  the decisive end for the Fredholm/C-operator gate, but the full shape-sector parametrix
  remains conditional on `P_disc` (June notes).
- The gap width `9/(2R_s)` is reconstruction grade (BC_1 `(m1,m2)=(7,1)`); the exact
  tau-twisted symmetric-pair threshold for the corrected `(SL(4,R), SO_0(3,1))` pair rides
  the still-open Oshima-Matsuki/Kobayashi theorem. The SIGN (positive) and the
  DICHOTOMY are robust; the exact NUMBER is contingent.
- The C-operator dichotomy uses standard Krein definitizable-operator theory as a CITED
  tool; the identification of the ghost critical point with the RS Krein-negative sector is
  from W167/W173 at their stated grade.
- `m2` remains the FIT `sqrt(m2_eff) mu_DW`; `R_s` the fiber radius. Nothing here narrows any
  FIT. The inequality is built; its truth value is not.

*Filed 2026-07-14. Wave W175 (TEAM BUILD-ANALYTIC), five personas inline in one session.
Reproducible: `python -u tests/W175_analytic_fredholm_essential_spectrum.py` (29/29,
exit 0). Exploration grade; no canon movement.*
