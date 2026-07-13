---
artifact_type: exploration
status: exploration (5-persona inline team; the make-or-break sign; deterministic test)
created: 2026-07-12
hypothesis: H59 / H61a decisive residual -- the ONE load-bearing input of the W79 no-go
branch: "W80 -- decide the single number the observer-conjecture no-go rests on: sign(f_0^2). TWO ways: (T1) GU's NATIVE R^2 (spin-0) one-loop beta with the RS ker-Gamma contribution -- does it flip the ported agravity value? (T2) is sign(f_0^2) FORCED (arena) or a FREE observer-selected VALUE (H62)?"
title: "GU's native R^2 sign is NEGATIVE at the central estimate and the RS ker-Gamma sector does NOT rescue it (c_RS_weyl over its whole H60 band keeps both fixed ratios negative; only a large, unsupported d_RS_R2 < -5/6 would flip). sign(f_0^2) SPLITS into two questions that H62 conflated: the MAGNITUDE of f_0^2 is a free relevant-direction VALUE (H62, correct), but the SIGN is FORCED negative (arena) on the one-loop asymptotic-FREEDOM UV completion -- because both UV fixed ratios r*=f_0^2/f_2^2 are negative and no trajectory can cross a fixed ratio, so f_0^2 > 0 Landau-poles (is not AF-complete). This is literature-backed agravity lore (Salvio-Strumia), NOT a porting artifact. The sign is FREE only by LEAVING that construction, via two nameable-but-unproven escapes: (E1) an uncomputed ker-Gamma d_RS_R2 < -5/6; (E2) a non-AF UV completion (asymptotic SAFETY / Reuter FP / f_0->inf conformal-Weyl limit) H57/H60/SS keep open. VERDICT: CONDITIONAL -- the no-go is GENUINE within the operative one-loop-AF construction; it dissolves only via E1 or E2, neither established. The credibility floor (scalaron positive-norm, W79 Task 1; loop-positivity leg closes; GU-independent theorems) stands regardless of this sign."
grade: "COMPUTED / analysis, HIGH confidence on the sorting and the two-derivation agreement; MEDIUM on the UV-completion fork (E2 open) and the ker-Gamma number (E1 uncomputed). Two derivations agree (algebraic fixed-ratio roots; numeric RK4 no-sign-crossing flow) that sign(f_0^2) is NEGATIVE and FORCED on the one-loop-AF route. Reuses the H57/H60 flow machinery (mirrors W45 BetaSystem; KNOWN pure-gravity coefficients 133/10, 5/3, 5, 5/6; H60 c_RS_weyl band [1.02,1.82]; W45 d_RS_R2 anchor 0 GUESS). Deterministic test tests/W80_native_r2_sign.py, exit 0. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN; this sharpens H62 (magnitude=value, sign=arena-on-AF) and pins the single input W79 flagged."
depends_on:
  - explorations/scalaron-normsign-and-vacuum-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - explorations/H62-arena-value-partition-firmup-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W80_native_r2_sign.py
---

# W80 -- GU's native R^2 sign, and whether it is forced or free (the make-or-break number)

**Role.** W79 reduced the entire observer-conjecture Krein-TT no-go to a SINGLE load-bearing input,
`f_0^2 < 0`, which it imported from the ported agravity one-loop betas (W45-47). Everything else in
W79 (positive-norm, background-independence of `M_0^2 = gamma/(6 f_0^2)`, the de Sitter vacuum) is
rigorous within the truncation; the no-go is only as strong as that one sign. W80 decides it two
ways from GU's native content, and asks the deeper H62 question: is the sign a **forced arena fact**
or a **free observer-selected value**? Test: `tests/W80_native_r2_sign.py` (deterministic, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Load-bearing here |
|---|---|---|
| **Gravity action** | GU-native induced `\|II\|^2` -> 4th-order Stelle `(f_2^2, f_0^2)` (H49) | The R^2 (spin-0) beta lives on this side; the ported agravity betas apply because GU's induced action is in the same derivative class. |
| **RS sector** | `ker Gamma`-projected spin-3/2: transverse, gamma-traceless, background-independent, degree-0 projector (H58) | THE native input for T1. It enters the R^2 beta via `d_RS_R2` (anchor 0) and the Weyl beta via `c_RS_weyl` (band [1.02,1.82]). Being transverse-gamma-traceless = *conformal-like*, which is exactly the content that does NOT source `R^2`. |
| **UV completion** | one-loop perturbative asymptotic **FREEDOM** (Gaussian FP), the route H57/H60 realize | THE fork for T2. The negative fixed ratio is a feature of THIS route; H57/H60/SS keep asymptotic **SAFETY** (Reuter FP) and the `f_0 -> inf` conformal-Weyl limit open as alternative UV completions on which the sign question changes. |
| **arena/value** | H62 symmetry characterization (c): arena = symmetry-invariant/fixed-point data; value = requires symmetry-breaking | Used to classify sign(f_0^2). W80 finds H62's `f_0 = value` row is about the **magnitude**; the **sign** is a separate, arena question on the AF route. |

## 1. Persona 1 -- RG / heat-kernel specialist: the native R^2 beta and its sign

### 1.1 The system (mirrors W45 H57-stage1; KNOWN coefficients reused, not re-derived)

With `x = f_2^2`, `y = f_0^2`, `t = ln mu`, `kappa = 1/(4pi)^2`:

```
(4pi)^2 dx/dt = -x^2 b_2 ,              b_2 = 133/10 + c_RS_weyl                 (AF, b_2>0)
(4pi)^2 dy/dt =  (5/3) x^2 + 5 x y + (5/6 + d_RS_R2) y^2
```

The pure-gravity coefficients `133/10, 5/3, 5, 5/6` are KNOWN/ported (Fradkin-Tseytlin;
Avramidi-Barvinsky; Salvio-Strumia). The two native RS inputs:

- **`c_RS_weyl`** -- RS ker-Gamma contribution to the Weyl beta `b_2`. H60 dof-counting band
  `[1.02, 1.82]`, central `~1.32`, POSITIVE (deepens `f_2` AF).
- **`d_RS_R2`** -- RS ker-Gamma contribution to the **R^2 (spin-0)** beta. Anchor **0** (GUESS,
  W45/H60): a pure fermion does not renormalize `R^2`, and the ker-Gamma carrier is transverse
  gamma-traceless (conformal-like), so at leading order it does not source `R^2` either; the ONLY
  native `R^2` source is the small non-minimal `Bbar Sigma.R B` coupling `y_RS`.

### 1.2 The sign lives in the fixed ratio (because `f_2 -> 0` on the AF trajectory)

Since `x = f_2^2 -> 0` in the UV, the physical UV variable is `r = y/x = f_0^2/f_2^2`, and
`sign(f_0^2)_AF = sign(r*)` at a UV fixed ratio. The fixed ratios solve

```
P(r) = (5/6 + d_RS_R2) r^2 + (5 + b_2) r + 5/3 = 0 ,   A := 5/6 + d_RS_R2 .
```

**At the anchor (`d_RS_R2 = 0`), both roots are NEGATIVE.** Exactly: with `A = 5/6 > 0`,

```
product of roots = C/A = (5/3)/(5/6) = 2 > 0    (both same sign)
sum of roots     = -(5 + b_2)/A < 0             (so the shared sign is NEGATIVE).
```

Numerically (anchor `b_2 = 14.7167`): `r* = -0.0848 , -23.575` -- exactly the H57 Stage-2 pair.
**Native `f_0^2 < 0`, the SAME sign as the ported agravity value.**

### 1.3 Does the RS ker-Gamma contribution flip it? -- Only one lever can, and it is not supported

- **Via `c_RS_weyl` (the Weyl beta): NO.** The product `C/A = 2 > 0` and `sum < 0` for **any**
  `b_2 > 0`, so both roots stay negative for the *entire* H60 band `[1.02,1.82]` -- and for any
  plausible `c_RS_weyl`. RS-via-`b_2` cannot flip the sign. (Test 1b.)
- **Via `d_RS_R2` (the R^2 beta): only if `d_RS_R2 < -5/6`.** A positive fixed ratio (a
  non-tachyonic AF branch) appears iff `A < 0` iff `d_RS_R2 < -5/6 ~ -0.833`. That is a **large
  NEGATIVE** contribution to the `R^2` beta. The anchor is 0; a transverse gamma-traceless
  (conformal-like) ker-Gamma carrier does not source `R^2` at leading order, and its only source
  (the non-minimal `y_RS`) is small on the AF trajectory. Reaching `-5/6` is **not supported**.
  (Tests 1c, 1d.)

**T1 verdict: native `f_0^2 < 0` at the central estimate; the RS ker-Gamma sector does NOT rescue
the sign.** The flip requires an uncomputed `d_RS_R2 < -5/6`; nothing supports it.

## 2. Persona 2 -- math referee: native vs ported, forced vs free

- **Native vs ported: same sign, and now the native structure is exhibited, not just imported.**
  W79 imported `f_0^2 < 0`. W80 shows *why* it is negative in GU's native flow: both UV fixed
  ratios are negative for structural reasons (`C/A = 2 > 0`, `sum < 0`) that survive the whole RS
  Weyl-band. The one native lever that could flip it (`d_RS_R2 < -5/6`) is precisely the uncomputed
  ker-Gamma heat-kernel H60 already flagged. **Grade: the negative sign is robust at the central
  native estimate; the flip is a specific, bounded, uncomputed possibility, not a live default.**
- **Forced vs free -- the referee's key ruling.** H62 classifies `f_0` as a **value** (relevant
  direction). That is correct for the **magnitude** but does NOT settle the **sign**. The sign is a
  separate question, adjudicated in Sec 3-4. Do not read "H62 says f_0 is free" as "the sign is
  free" -- that is the conflation W80 must break.

## 3. Persona 3 -- adversary (presses both, and lands the harder blow)

**Against "the sign is free" (adversary wins this one on the AF route):** `f_0^2` being a relevant
direction lets you dial its **magnitude** (which trajectory, where on it), but a trajectory
**cannot cross a fixed ratio** (ODE uniqueness). Both fixed ratios are negative, and the
UV-attractive one is `r_2 = -23.575`. Any start with `f_0^2 > 0` (i.e. `r > r_1 = -0.0848`)
flows to a **Landau pole** in the UV -- it is **not AF-complete** -- while every AF-complete
trajectory sits in the basin `r in (r_2, r_1)` with `f_0^2 < 0` at **all** scales. So on the
one-loop-AF UV completion the sign is **forced negative**; the "stable branch `f_0^2 > 0`" is
exactly the branch that is **not selectable** because it is not AF-complete. This is the adversary's
lasting mark, and it is **literature-backed agravity lore** (Salvio-Strumia: the non-tachyonic
`f_0^2 > 0` region tends to a Landau pole; AF-completeness prefers the wrong-sign branch or the
`f_0 -> inf` conformal limit) -- **NOT a porting artifact**.

**Against "the sign is forced" (adversary's own counter, honestly stated):** the whole argument
assumes the operative UV completion is the **one-loop perturbative-AF** trajectory. H57/H60 *and*
Salvio-Strumia keep two alternatives explicitly open -- asymptotic **safety** (a Reuter FP the
perturbative betas do not capture) and the **`f_0 -> inf` conformal-Weyl limit** (where the `R^2`
term, hence the scalaron and its tachyon, is absent). On either, the negative-fixed-ratio argument
does not apply and `f_0^2 > 0` (or "no scalaron at all") can be admissible. Plus the T1 lever:
`d_RS_R2 < -5/6` would manufacture a positive-`f_0^2` AF branch outright. So the forcing is
**construction-conditional**, not absolute.

**Adversary residual (named as the escape set):** the sign is forced negative **on the operative
one-loop-AF construction**; it becomes free only via (E1) `d_RS_R2 < -5/6` or (E2) a non-AF UV
completion. Neither is established; neither is excluded.

## 4. Persona 4 -- cross-checker: second derivation + literature

- **Second derivation (numeric RK4 flow, independent of the algebraic root analysis).** Integrating
  `dg/dt` toward the UV: a start with `f_0^2 = +0.3` **Landau-poles** (`y ~ 1e31` at finite `t`) --
  not AF-complete; a basin start `f_0^2 < 0` (`r_0 = -1`) flows to the **Gaussian FP** (`x,y -> 0`)
  with `f_0^2 < 0` at **every** step (it never crosses to positive). The two derivations
  (fixed-ratio roots; no-sign-crossing flow) **agree**: sign is negative and forced on the AF route.
- **Literature (read-only).** Salvio-Strumia agravity (1403.4226; 1705.03896): the `R^2` scalar
  coupling `f_0^2` is **not** asymptotically free the way `f_2^2` is; the non-tachyonic sign region
  is prone to a Landau pole, and the clean UV completions are the wrong-sign branch or `f_0 -> inf`
  (conformal/Weyl gravity, no `R^2`). This is exactly the structure W80 reproduces -- the negative
  sign for AF-completeness is a **known feature of the class**, which is *why* it is not a GU
  porting artifact and *why* the honest escape is the UV-completion fork, not a convention flip.
- **Heat-kernel cross-check on T1.** A conformally-coupled field contributes only `C^2` and `E_4`
  (no `R^2`) to the one-loop divergence; the `R^2` beta is fed by **deviation from conformality**
  (the scalar `(xi - 1/6)^2` structure). The ker-Gamma spin-3/2 is transverse gamma-traceless =
  maximally conformal-like, so its leading `R^2` contribution is `~0` (anchor), consistent with
  `d_RS_R2 = 0` and with the `-5/6` flip threshold being far out of reach.

## 5. Persona 5 -- synthesizer: verdict

**TASK 1 -- NATIVE SIGN: NEGATIVE (central estimate); RS does NOT flip it.** GU's native R^2 beta
gives both UV fixed ratios negative (`C/A = 2 > 0`, `sum < 0`) for the entire H60 `c_RS_weyl` band;
the RS ker-Gamma sector changes the sign only through `d_RS_R2`, and only if `d_RS_R2 < -5/6` -- a
large negative `R^2`-beta contribution unsupported for a conformal-like transverse-traceless
carrier. So the native sign equals the ported sign: `f_0^2 < 0`.

**TASK 2 -- FORCED or FREE: SPLIT.** The **magnitude** of `f_0^2` is a free relevant-direction
**VALUE** (H62, correct). The **SIGN** is **FORCED negative (arena)** on the one-loop-AF UV
completion -- both derivations agree, and it is literature-backed, because `f_0^2 > 0` is not
AF-complete (Landau pole) and no trajectory crosses a fixed ratio. The sign is **FREE only off that
route**, via two nameable-but-unproven escapes: **E1** `d_RS_R2 < -5/6` (uncomputed ker-Gamma
heat-kernel); **E2** a non-AF UV completion (asymptotic safety / Reuter FP / `f_0 -> inf` conformal
limit) kept open by H57/H60/SS. This **sharpens H62**: `f_0` magnitude = value, `f_0` sign =
arena-on-the-AF-route (no canon change).

**COMBINED VERDICT: CONDITIONAL -- the no-go is GENUINE within the operative one-loop-AF
construction.** Native `f_0^2 < 0` (T1) and the sign forced on the AF route (T2) mean the W79
Krein-TT no-go stands *as a fact of the one-loop-AF UV completion GU actually realizes* (H57/H60).
It is **not** an unconditional blockbuster-killer, because it dissolves under either unproven
escape (E1 or E2); and it is **not** a dissolved no-go, because neither escape is established and
the negative-for-AF-completeness structure is real agravity physics, not a porting artifact. So the
honest headline is **CONDITIONAL, defaulting to genuine-within-the-construction** -- I do not
manufacture a "free value" rescue (the sign is genuinely forced on the operative route) and I do
not overstate the no-go as absolute (two real escapes remain).

**Two-derivation agreement.** (i) algebraic: both fixed ratios negative + no ratio-crossing =>
forced negative; (ii) numeric RK4: `f_0^2>0` Landau-poles, `f_0^2<0` reaches Gaussian without
sign-crossing. Agree on **sign = negative** and on **forced (arena) on the AF route**.

**Load-bearing assumption (single, named).** The operative UV completion is the **one-loop
perturbative asymptotic-FREEDOM** trajectory. *Given* that, sign(f_0^2) is forced negative (arena)
and the no-go is genuine. The assumption's two failure modes are exactly E1 (native `d_RS_R2 <
-5/6`) and E2 (a non-AF UV completion) -- the construction-fork below.

**Construction-fork (decisive, unresolved).** UV completion = one-loop perturbative-AF (sign forced
negative -> no-go genuine) **vs** asymptotic-safety / conformal `f_0 -> inf` limit (sign free / no
scalaron -> no-go dissolves). Per GEOMETER-VS-PHYSICS discipline this fork is **not settled** --
H57/H60/SS keep both UV routes open -- so the no-go is conditional on the fork landing on the AF
side, which is the side GU's perturbative flow actually realizes.

**Confidence.** HIGH on the two-derivation agreement (native sign negative; forced on the AF route);
MEDIUM on the combined verdict, because it is genuinely gated by the two open items (E1 uncomputed
ker-Gamma `d_RS_R2`; E2 the UV-completion fork). **Credibility floor (independent of this sign):**
the scalaron is positive-norm (W79 Task 1), so the loop-positivity leg closes regardless; the
GU-independent theorems stand regardless. This holds whether the no-go is genuine or dissolves.

## 6. What this does and does not do

**Does:** exhibit GU's native R^2 sign (`f_0^2 < 0`) from the fixed-ratio structure rather than
importing it; show the RS ker-Gamma sector does not flip it (whole `c_RS_weyl` band; flip needs
`d_RS_R2 < -5/6`, unsupported); split sign(f_0^2) into a free magnitude (value, H62) and a
forced sign (arena, on the AF route), with two agreeing derivations; name the two escapes (E1, E2)
and the decisive UV-completion construction-fork; land the verdict CONDITIONAL (no-go genuine
within the operative construction). Deterministic test `tests/W80_native_r2_sign.py`, exit 0.

**Does NOT:** compute the true ker-Gamma heat-kernel `d_RS_R2` (E1 stays uncomputed); settle the
UV-completion fork (E2 stays open -- no FRG/Reuter computation performed); re-derive `gamma > 0`
(H25) or the KNOWN pure-gravity coefficients; go beyond one loop / the 4th-order truncation; or
change `CANON.md`, `RESEARCH-STATUS.md`, `claim-status`, verdicts, or public posture. H59/H61a
remain **OPEN**; this pins the single input W79 flagged and sharpens H62.

## 7. Next valid swing

1. **Compute the ker-Gamma `d_RS_R2` heat-kernel** on the `Spin(9,5)`-equivariant subspace -- the
   one number that decides E1 (is `d_RS_R2 < -5/6`? almost certainly not, but it is uncomputed).
2. **Test the E2 fork** with an FRG/Reuter truncation of GU's induced action: does a non-Gaussian
   UV completion admit `f_0^2 > 0` (or remove the `R^2` scalaron via the `f_0 -> inf` conformal
   limit)? This is where "genuine no-go" vs "dissolved" is actually decided.
