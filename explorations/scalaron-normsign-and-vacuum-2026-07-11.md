---
artifact_type: exploration
status: exploration
created: 2026-07-12
hypothesis: H59 / H61a (unified UV loop-positivity + observer-conjecture Krein-TT), decisive residual
branch: "W79 -- the two facts W78 left uncomputed: (1) the NORM-SIGN of GU's R^2 scalaron from |II|^2=|H|^2-R^X; (2) GU's TRUE VACUUM and whether the flat-space tachyon lifts there."
title: "GU's induced R^2 scalaron is POSITIVE-NORM (its norm is set by the Gauss-fixed induced Einstein term -R^X, computed positive by H25 -- NOT by the R^2 coefficient), so the two North Stars SPLIT rather than fall together. But its mass M_0^2 = gamma/(6 f_0^2) is BACKGROUND-INDEPENDENT (a pure-R^2 feature: f''=2 f_0^2 is constant), so with f_0^2<0 the scalaron is tachyonic at EVERY constant-curvature background including GU's de Sitter true vacuum R_vac=4Lambda/gamma. Vacuum selection CANNOT lift the obstruction. VERDICT: SPLIT, resolved -- loop-positivity CLOSES (positive-norm); the observer-conjecture Krein-TT leg is the program's FIRST GENUINE NO-GO, located precisely at the scalaron potential."
grade: "exploration / positive-norm derivation: rigorous within the 4th-order truncation (two derivations -- direct f'(0)=gamma and the Einstein-frame no-ghost condition -- agree; the norm is provably beta-independent). Background-independence of M_0^2 and no-lift: rigorous within the truncation (M_0^2=gamma/(6 f_0^2), d/dR=0, exact sympy; de Sitter vacuum R_vac=4Lambda/gamma with beta dropping out; Einstein-frame V_E'' curvature agrees). LOAD-BEARING inputs (each cited, not re-derived here): gamma>0 (H25 C_RY>0), f_0^2<0 (W45-47/W78), the 4th-order landing (H49). Deterministic test tests/W79_scalaron_normsign_and_vacuum.py, exit 0. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN; this RESOLVES the split W78 left conditional."
depends_on:
  - explorations/conformal-factor-mode-gauge-status-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - explorations/wave5/H21-theta-equals-II-2026-07-11.md
  - explorations/wave7/H25-II-first-variation-2026-07-11.md
  - explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md
  - explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W79_scalaron_normsign_and_vacuum.py
---

# W79 -- The scalaron norm-sign and GU's true vacuum (decides both North Stars)

**Role.** W78 proved GU's spin-0 conformal mode is a *physical propagating* R^2 scalaron (not a
gauge artifact) that is a positive-norm **tachyon** around flat space, and reduced the whole UV +
observer-conjecture program to **two uncomputed facts** it explicitly flagged as load-bearing:

1. **Norm-sign** -- is the scalaron positive-norm (legs SPLIT) or a negative-norm ghost-tachyon
   (both North Stars fall together into a no-go)? W78 assumed positive-norm from "standard
   agravity," flagged it as the single fact that decides split-vs-fall-together.
2. **True vacuum** -- the flat-space tachyon `M_0^2 < 0` is an instability of a background, not
   necessarily of the theory. Does GU's effective potential (`|II|^2` + induced Einstein + DeWitt
   `Lambda`) admit a stable non-tachyonic vacuum where `M_0^2 > 0`, lifting the Krein-TT
   obstruction?

W79 computes both, from GU's *actual* induced sign structure, two independent ways each. Test:
`tests/W79_scalaron_normsign_and_vacuum.py` (deterministic, exact sympy, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), stated

| Object | Construction used | Why it is load-bearing here |
|---|---|---|
| **Gravity functional** | GU-native **induced `|II|^2 = |H|^2 - R^X`** (Gauss), landing (H49/H57-stage1) in the 4th-order class `f(R) = gamma R + beta R^2 - 2 Lambda`. **NOT** a freely chosen `R^2` Lagrangian. | This is THE fork for the norm-sign. On a *free* `R^2` Lagrangian one may tune `gamma < 0` and manufacture a ghost. GU **cannot**: the Gauss identity fixes the `-R^X` Einstein term, and H25 **computed its sign positive**. The positive norm is therefore *forced by the induced construction*, not chosen. |
| **The scalaron mass parameter** | `f'' = 2 beta = 2 f_0^2`, with `f_0^2 < 0` the **induced** (running, `beta_{f_0^2} != 0`) R^2 coefficient of `|H|^2` on the AF trajectory (W45-47, W78). | Fixes the tachyon. `f_0^2 < 0` is the ported one-loop-beta input; it is the single physics-side number the no-go rests on (named below). |
| **The cosmological term** | DeWitt `Lambda`, `rho_Lambda = c_L mu_DW^4`, `c_L = 3/8 > 0` (H50/H51). | Sets the de Sitter true vacuum `R_vac = 4 Lambda/gamma > 0` -- the candidate lift. |

## 1. Persona 1 -- higher-derivative / f(R) specialist: the two computations

### 1.1 The action GU lands in

`|II|^2 = |H|^2 - R^X` decomposes (H49, H57-stage1, W78) into the 4th-order class

```
f(R) = gamma R + beta R^2 - 2 Lambda,
   gamma  = coeff of the INDUCED Einstein term (the Gauss -R^X); sign FIXED by Gauss,
            computed POSITIVE by H25 (C_RY > 0 => m2_eff > 0, attractive gravity);
   beta   = f_0^2, the induced R^2 coefficient (from |H|^2), run NEGATIVE on the AF
            trajectory (W45-47, W78);
   Lambda = DeWitt term, rho_Lambda = c_L mu_DW^4, c_L = 3/8 > 0 (H50/H51).
```

so `f' = gamma + 2 beta R`, `f'' = 2 beta` (constant -- a pure-quadratic feature that turns out
to be decisive).

### 1.2 TASK 1 -- the norm-sign (the crux: it is set by `gamma`, not by `beta`)

The standard, unambiguous spectral facts for `f(R)` gravity (De Felice-Tsujikawa Living Review;
Stelle 1977; Salvio-Strumia agravity):

- **scalaron NORM** `= sign(f'(R_bg))`. No-ghost `<=> f' > 0`. The norm is set by the
  Einstein/graviton (frame) sector -- **not** by the `R^2` coefficient.
- **scalaron MASS^2** `= (1/3)(f'/f'' - R)`. Non-tachyon `<=> f'' > 0`.

These separate cleanly: `beta = f_0^2` sits in `f''` (the mass), never in `f'(0)` (the norm).
Two derivations:

- **(A) Direct.** At the flat background, `f'(0) = gamma`. `d f'(0)/d beta = 0` -- the norm-sign is
  *provably independent* of `f_0^2`. GU's `gamma > 0` (H25) `=>` **positive-norm**.
- **(B) Einstein-frame (scalar-tensor).** `f(R)` is Brans-Dicke `omega=0`; the map `g~ = f' g`,
  canonical scalaron `chi = sqrt(3/2) ln f'`, produces a scalar kinetic term `+(1/2)(d chi)^2` --
  **positive for any `beta`** -- provided the frame map is non-degenerate, i.e. `f' > 0`. So
  positive-norm `<=>` `f' > 0`, which at flat background is `gamma > 0`. Same answer, independent
  route.

> **The wrong-sign `f_0^2 < 0` makes a TACHYON (a mass), not a GHOST (a norm).** Positive-norm is
> forced by the Gauss-fixed `-R^X` Einstein sign (H25), so the two North Stars **SPLIT** and do
> **not** fall together into a ghost-tachyon no-go.

### 1.3 TASK 2 -- the true vacuum and `M_0^2` there (the crux: background-independence)

- **The scalaron mass is `M_0^2 = gamma/(6 beta)`, and `d M_0^2/dR = 0` -- BACKGROUND-INDEPENDENT.**
  This is special to the pure `R^2` term: `f'' = 2 beta` is constant, so `f'/f'' - R = gamma/(2 beta)`
  is `R`-independent. The tachyon is intrinsic to `sign(f_0^2) < 0`, **not** to the choice of
  background. (Exact sympy.)
- **GU's de Sitter true vacuum exists.** The constant-curvature vacuum condition (trace of the
  `f(R)` vacuum eom) is `R f' - 2 f = 0`, giving `R_vac = 4 Lambda/gamma`. With `Lambda, gamma > 0`
  this is a **de Sitter** background (positive constant curvature). Notably **`beta` drops out of the
  vacuum condition** -- the `R^2` coefficient sets neither the vacuum curvature nor the mass sign
  there.
- **`M_0^2` at the de Sitter vacuum `= gamma/(6 f_0^2) < 0`** -- identical to flat space. **The
  vacuum does not lift the tachyon.** Even inhomogeneous/time-dependent backgrounds give the same
  local `M_0^2` (again because `f'/f'' - R` is `R`-independent), so there is *no background escape at
  all*. For the physical (tiny) `Lambda ~ meV^4` the vacuum is a nearly-flat de Sitter with
  `phi_* = f'(R_vac) = gamma + 8 Lambda beta/gamma \approx gamma > 0`: **positive-norm** graviton and
  scalaron, but **tachyonic**.

**Verdict Task 2: NO stable non-tachyonic vacuum.** The de Sitter vacuum is a tachyonic hilltop
(`V_E'' < 0`, below), not a stable minimum. The obstruction does not lift.

## 2. Persona 2 -- math referee: genuinely from `|II|^2`, or convention-inserted?

- **Norm-sign is genuine, not convention-inserted.** The load-bearing sign is `gamma` = the
  Gauss-fixed `-R^X` Einstein coefficient, which H25 computed **positive by two independent methods**
  (Gauss-ratio and direct `|II|^2` second variation, both `m2_eff > 0`, `C_RY > 0`). We did not
  insert a favorable sign: we *used* the sign the induced construction already forced. The step
  "norm `= sign(f')`" is the standard, convention-robust scalar-tensor result, applicable because
  GU's action lands in the 4th-order class (H49). **Grade: rigorous within the truncation.**
- **Background-independence is exact.** `M_0^2 = gamma/(6 beta)`, `d/dR = 0`, is closed-form exact,
  not a numerical near-zero. The de Sitter vacuum and `beta`'s dropout from `R_vac` are exact. The
  Einstein-frame `V_E''` sign agrees. **Grade: rigorous within the truncation.**
- **What is NOT re-derived here (imported, each cited):** `gamma > 0` (H25); `f_0^2 < 0` on the AF
  trajectory (W45-47/W78); the 4th-order landing (H49). The no-go is only as strong as `f_0^2 < 0`
  (see 5).

## 3. Persona 3 -- adversary (presses both verdicts)

**Against positive-norm ("the sign is convention-dependent"):** the norm is a *relative* sign --
`sign(f')` relative to the metric-signature convention -- and the SAME convention fixes that `-R^X`
is *attractive* (H25's `C_RY > 0`). Flip the convention and both flip together; the ratio (hence
"positive-norm iff gravity is attractive") is convention-independent. The adversary cannot make the
scalaron a ghost without also making GU's gravity repulsive, which H25 excluded. **Positive-norm
holds.**

**Against the no-go ("the de Sitter vacuum is the wrong branch / a rolling background saves it"):**
this is the strongest attack and it **fails on background-independence**. `M_0^2 = gamma/(6 f_0^2)`
does not depend on `R` at all -- no constant-curvature branch, no rolling/inhomogeneous background,
changes its sign. The only way to `M_0^2 > 0` is `f_0^2 > 0`, i.e. a *different sign of the R^2
coefficient*, not a different vacuum. The adversary's "wrong background" move -- which legitimately
rescues generic tachyons (Higgs, Coleman-Weinberg) -- is *defeated here specifically because the
mass is background-independent*. This is the honest reason W78's "liftable by the true vacuum" hope
does **not** materialize.

**Adversary's residual (lands, and is named as the escape):** the no-go rests on `f_0^2 < 0`. If
GU's *native* R^2 running differs in sign from the ported physics-default betas (W45-47), or if
terms beyond the 4th-order truncation give a non-constant `f''`, the background-independence breaks
and a vacuum could lift it. This is the load-bearing assumption, not a defeated one.

## 4. Persona 4 -- cross-checker: second derivation + Starobinsky/agravity literature

- **Einstein-frame potential (independent of the `M^2 = (1/3)(f'/f''-R)` formula).**
  `phi = f' = gamma + 2 beta R`, `V_E(phi) = (beta R^2 + 2 Lambda)/(2 phi^2)`. Its unique extremum is
  `phi_* = gamma + 8 Lambda beta/gamma` (`=> R_vac = 4 Lambda/gamma`, matching the trace condition),
  and `sign(V_E''(phi_*)) = sign(gamma/beta)`. So the extremum is a **stable minimum for
  `beta > 0`** and a **tachyonic maximum for `beta < 0`** -- reproducing `M_0^2 = gamma/(6 beta)`
  from the potential-curvature side. **Two derivations agree** (the discipline that caught the
  `M^2/r^2` bug).
- **Numeric contrast (test):** `gamma=1, Lambda=0.01`:
  - `beta = +1` (Starobinsky-type): `phi_* = 1.08`, `V_E'' = +0.198` (stable min), `M_0^2 = +1/6 > 0`.
  - `beta = f_0^2 = -1` (GU): `phi_* = 0.92`, `V_E'' = -0.321` (tachyonic max), `M_0^2 = -1/6 < 0`.
- **Literature (read-only).** **Starobinsky** `R + R^2/(6M^2)`: the scalaron is the inflaton, mass
  `M^2 > 0`, because the `R^2` coefficient is **positive**. **Agravity (Salvio-Strumia 2014):** the
  `R^2` scalaron is a *physical, positive-norm* scalar; non-tachyonic requires the `R^2` coefficient
  `> 0`; the ghost is *only* the spin-2 mode. **GU has the opposite `R^2` sign (`f_0^2 < 0`)** -- so
  it is a **"wrong-sign Starobinsky": positive-norm (like Starobinsky) but tachyonic (unlike it)**,
  and the tachyon is background-independent. This is exactly W78's assumed reading, now *derived*
  from the induced sign structure rather than assumed.

## 5. Persona 5 -- synthesizer: combined verdict, the split resolved, the no-go located

**TASK 1 -- NORM-SIGN: POSITIVE.** GU's `R^2` scalaron is positive-norm. The norm is set by
`f'(0) = gamma` = the induced `-R^X` Einstein coefficient, which the Gauss identity fixes and H25
computed positive; it is provably independent of `f_0^2`. Two derivations (direct `f'`, Einstein-
frame no-ghost) agree. `f_0^2 < 0` makes a **tachyon (mass)**, not a **ghost (norm)**. *=> the two
North Stars SPLIT; they do not fall together into a ghost-tachyon no-go.*

**TASK 2 -- TRUE VACUUM: no non-tachyonic vacuum.** `M_0^2 = gamma/(6 f_0^2)` is
**background-independent** (pure-`R^2`, `f'' = 2 f_0^2` constant). GU's de Sitter vacuum
`R_vac = 4 Lambda/gamma` exists (positive-norm for the physical tiny `Lambda`) but has the *same*
`M_0^2 < 0`; it is a tachyonic hilltop (`V_E'' < 0`), not a stable minimum. No constant-curvature
(or rolling) background lifts the tachyon. *=> vacuum selection cannot rescue the Krein-TT leg.*

**COMBINED VERDICT: SPLIT -- and now RESOLVED on both sides.**

- **North Star 1 (GU UV loop-POSITIVITY -- a NORM statement): CLOSES (plausibly).** The scalaron is
  positive-norm, so it does not make the inner product indefinite; the spin-2 sector is
  PT-unbroken across the interacting regime (W53). The positive inner product survives.
- **North Star 2 (observer-conjecture Krein-TT -- a real-positive-spectrum / STABILITY statement):
  FIRST GENUINE NO-GO.** The physical positive-norm scalaron has `M_0^2 < 0` at *every* background,
  so the modular/`Delta` spectrum is non-real (PT-broken) in the spin-0 sector and no vacuum lifts
  it. This is the program's **first genuine no-go, located precisely at the scalaron potential** --
  not a gauge artifact, not a wrong-background artifact, but the wrong *sign* of the induced `R^2`
  coefficient `f_0^2 < 0`, whose effect is background-independent.

**Load-bearing assumption (named, single).** `f_0^2 < 0` on GU's asymptotically-free trajectory
(ported one-loop betas, W45-47/W78). This is the ONE number the no-go rests on. If GU's *native*
`R^2` running has the opposite sign, or if beyond-4th-order terms make `f''` non-constant, the
background-independence breaks and a vacuum could lift the obstruction. Everything else
(positive-norm; background-independence *given* `f_0^2 < 0`; the de Sitter vacuum) is rigorous
within the 4th-order truncation.

**Construction-fork used (named).** Gravity functional = GU-native induced `|II|^2 = |H|^2 - R^X`
(Gauss), NOT a free `R^2` Lagrangian. This fork is *decisive and lands on the geometric side for the
norm*: the positive norm is **forced** by the Gauss-fixed `-R^X` (a free Lagrangian would leave it
tunable). The same induced construction supplies `f_0^2 < 0` (its running), which is what makes the
tachyon -- so the fork gives *both* the split (good, norm) *and* the no-go (bad, mass), honestly.

**Confidence.** Positive-norm: **rigorous** within the truncation (two derivations; provably
`f_0^2`-independent; H25 supplies `gamma > 0`). No-lift/no-go: **rigorous within the truncation**
(background-independence is exact; both derivations agree), **conditional on `f_0^2 < 0`** (the one
named input). Overall grade: **SPLIT resolved -- loop-positivity closes; Krein-TT first genuine
no-go, conditional only on the `f_0^2 < 0` sign.**

## 6. What this does and does not do

**Does:** derive the scalaron norm-sign (POSITIVE) from GU's induced `|II|^2 = |H|^2 - R^X` sign
structure (not convention-inserted), resolving W78's split; compute GU's true de Sitter vacuum
`R_vac = 4 Lambda/gamma` and show `M_0^2 = gamma/(6 f_0^2) < 0` there and at *every* background
(background-independent), so no vacuum lifts the tachyon; and thereby resolve the combined verdict
to **SPLIT**: loop-positivity closes, the observer-conjecture Krein-TT leg is the program's **first
genuine no-go**, located at the scalaron potential and conditional only on `f_0^2 < 0`.

**Does NOT:** re-derive `f_0^2 < 0` (imported from W45-47/W78 -- the one load-bearing input);
re-derive `gamma > 0` (H25) or `c_L = 3/8` (H51); go beyond the 4th-order truncation (H49); compute
a GU/Stelle loop amplitude; or change `CANON.md`, `RESEARCH-STATUS.md`, `claim-status`, verdicts, or
public posture. H59/H61a remain **OPEN** (this resolves the split they were conditional on, in the
no-go direction for the Krein-TT leg).

## 7. Next valid swing

1. **Verify GU's NATIVE `R^2` running sign** (the single load-bearing input): is `f_0^2 < 0` a
   genuine feature of GU's induced/geometric flow, or an artifact of the ported physics-default
   one-loop betas (W45-47)? This is now the ONE number standing between "first genuine no-go" and
   "the tachyon was a porting artifact."
2. **Check beyond-4th-order terms** in the full `|II|^2` (higher Willmore/`II` invariants): if any
   contribute a non-constant `f''(R)`, the background-independence that makes the no-go airtight
   would break, re-opening vacuum selection.
