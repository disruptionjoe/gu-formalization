---
artifact_type: exploration
status: exploration (5-persona inline team; deterministic test)
created: 2026-07-13
hypothesis: H59 / H61a residual -- the single load-bearing ported number named by W122
branch: "W123 -- SIGN OF GU'S NATIVE R^2 RUNNING: (1) convention audit of the port chain (repo f_0^2 <-> Fradkin-Tseytlin/Avramidi-Barvinsky omega <-> Salvio-Strumia agravity f_0^2, pinned to GU's own induced action via H25's native gamma > 0 and W122's gauge-parameter-free m_0^2), (2) one-loop R^2 beta reassembled from per-field blocks with GU's actual field content across the whole admissible coefficient band, (3) trajectory-existence: is ANY AF trajectory with f_0^2 > 0 possible, including f_0^2 -> 0+ asymptotically?"
title: "VERDICT: the tachyon is NOT a porting artifact. (1) CONVENTION CHAIN PINNED end to end: the repo's ported (f_2^2, f_0^2) system maps EXACTLY (symbolic identity, not notation-matching) onto the Avramidi-Barvinsky (lambda, omega) basis under omega = f_2^2/(2 f_0^2) -- the derived omega beta is -f_2^2(200 w^2 + 1098 w + 25)/60 whose independently published roots -0.0228/-5.4671 are reproduced, and BOTH lineages put the AF trajectory on the same side; the repo's native W122 scalaron mass m_0^2 = gamma/(6c) coincides identically with the published agravity M_0^2 = f_0^2 Mbar_Pl^2/2 under the map, so the tachyon condition is the SAME physical statement at both ends of the port, with physical (not notational) anchors at both ends: gamma > 0 = attractive gravity (H25, computed natively, two methods) and f_0^2 < 0 = tachyonic scalaron (Salvio-Strumia's own reading in their own convention). ONE convention wobble found in the repo -- W45-47/W119 use f_0^2 = the agravity coupling (R^2 coefficient 1/(6 f_0^2)) while W79/W122 use f_0^2 = the direct R^2 coefficient -- and it is verified sign-HARMLESS (reciprocation preserves sign; magnitude formulas differ, flagged). (2) NATIVE CONTENT: the R^2-beta self-coefficient is A = 5/6 + d_RS_R2 + sum of PERFECT SQUARES (scalar non-minimal couplings, w_a(xi_a+1/6)^2 >= 0); with d_RS_R2 = 0 COMPUTED (W82 ker-Gamma heat kernel) no admissible content can reach the flip threshold A < 0 (d < -5/6), so BOTH fixed-ratio roots stay strictly negative (Vieta: product 2/A-scaled > 0, sum < 0) across the entire W47 c_RS_weyl band [1.02, 1.82], far beyond it, and for ANY scalar sector; if A were driven huge the discriminant fails and the outcome is NO AF trajectory at all, never a positive root. FIXED-RATIO SIGN: ROBUST, not FLIPS-IN-BAND, not CONVENTION-ARTIFACT. (3) TRAJECTORY EXISTENCE: FORBIDDEN -- a one-line MONOTONICITY THEOREM (every term of beta_{f_0^2} is nonnegative when f_0^2 > 0, f_2^2 >= 0) makes f_0^2 strictly increasing toward the UV whenever positive, so f_0^2 > 0 Landau-poles in bounded t (Delta t <= (4pi)^2(6/5)/f_0^2) and the escape f_0^2 -> 0+ asymptotically is IMPOSSIBLE, not merely repelled; the AF basin is exactly { f_2^2 > 0, r <= r_1 = -0.0848 } (r_1 the repulsive separatrix, r_2 = -23.575 the UV-attractive ratio; even small-NEGATIVE f_0^2 starts above r_1 Landau-pole), so f_0^2 < 0 at EVERY finite scale on EVERY AF trajectory. TACHYON VERDICT UPDATE: NATIVE-ROBUST on the AF branch; the porting-artifact escape is CLOSED; the surviving escapes are exactly W82's AF-vs-AS fork (E2) and beyond-one-loop caveats, now the ONLY doors."
grade: "DERIVED-on-PORTED-blocks, exploration-grade. DERIVED (exact sympy / deterministic numerics): the omega-map identity, the root and attractivity correspondences, the m_0^2 formula coincidence, the sign-harmlessness of the reciprocal wobble, the Vieta sign theorem for all A > 0 and b_2 > 0, the band sweeps, the monotonicity theorem and Landau bound, the basin characterization. PORTED-KNOWN (cited, reproduced as positive controls, not re-derived): the pure-gravity one-loop coefficients 133/10, 5/3, 5, 5/6 (Fradkin-Tseytlin; Avramidi-Barvinsky; Salvio-Strumia) and the AB omega quadratic 200w^2+1098w+25 with roots -0.0228/-5.4671; the agravity scalaron mass M_0^2 = f_0^2 Mbar_Pl^2/2; the scalar-matter perfect-square structure of the R^2 beta. PORTED-band: c_RS_weyl in [1.02, 1.82] (W47). COMPUTED (imported from W82, literature heat kernel for GU's exact ker-Gamma carrier): d_RS_R2 = 0. IMPORTED-NATIVE (cited): gamma > 0 (H25, two methods); m_0^2 = gamma/(6c) gauge-parameter-free (W122). HONEST RESIDUAL: no GU-native graviton loop is computed here or anywhere in the repo -- the pure-gravity block values remain ported; what W123 closes is the CONVENTION channel (a mis-port would break an exact cross-lineage identity that in fact holds) and the FIELD-CONTENT channel (no admissible content flips the sign). Deterministic test tests/W123_native_r2_sign_convention_audit.py, 34/34 checks, exit 0, with positive controls (AB roots; W46 roots) and a negative control (d = -1 < -5/6 exhibits the flip the admissible band cannot reach). NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN."
depends_on:
  - explorations/W122-spin0-gauge-vs-physical-auxfield-2026-07-13.md
  - explorations/true-fixed-point-f0-sign-2026-07-11.md
  - explorations/native-r2-sign-makeorbreak-2026-07-11.md
  - explorations/h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md
  - explorations/H57-flow-stage1-theory-space-betas-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - explorations/wave7/H25-II-first-variation-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W46_H57_stage2_fixed_point.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W123_native_r2_sign_convention_audit.py
external_refs:
  - "Fradkin & Tseytlin, Renormalizable asymptotically free quantum theory of gravity, Nucl. Phys. B201, 469 (1982)"
  - "Avramidi & Barvinsky, Asymptotic freedom in higher-derivative quantum gravity, Phys. Lett. B159, 269 (1985) -- the omega beta and its fixed points -0.0228, -5.4671"
  - "Codello & Percacci, Fixed points of higher-derivative gravity, PRL 97 (2006) 221301 -- independent quotation of the AB omega fixed points"
  - "Salvio & Strumia, Agravity, JHEP 06 (2014) 080, arXiv:1403.4226 -- the ported betas; M_0^2 = f_0^2 Mbar_Pl^2/2; the tachyon-vs-AF tension stated in their own convention"
  - "Salvio & Strumia, Agravity up to infinite energy, EPJ C78 (2018) 124, arXiv:1705.03896 -- the f_0 -> infinity conformal resolution of the same tension"
  - "Salvio, Quadratic Gravity, Front. Phys. 6 (2018) 77, arXiv:1804.09944 -- review; conventions; the omega/f_0 dictionary context"
  - "Buccio, Donoghue & Percacci, arXiv:2403.02397 -- physical vs MS-bar running in quadratic gravity (catalogued caveat, not adopted)"
  - "Gibbons, Hawking & Perry, NPB 138 (1978) 141; Mazur & Mottola, NPB 341 (1990) 187 -- Euclidean conformal-factor treatments (catalogued, delineated by W122 as category-inapplicable to the Lorentzian mass sign)"
---

# W123 -- The sign of GU's native R^2 running: convention audit, native content, trajectory existence

**Role.** W122 closed the gauge channel on the scalaron tachyon and left exactly one escape standing:
*"f_0^2 < 0 is PORTED (W45-47 one-loop betas). If GU's native R^2 running has the opposite sign, the
tachyon evaporates. Still the single number the no-go rests on."* W123 attacks that number on the
three axes where a porting error could hide: the CONVENTION channel (was a sign lost in translation
between the literature bases and GU's induced action?), the FIELD-CONTENT channel (does GU's actual
content, anywhere in the admissible coefficient band, flip the beta?), and the TRAJECTORY channel
(does any AF trajectory with f_0^2 > 0 exist, even asymptotically?). Five personas inline, one
context, no sub-agents. Deterministic test: `tests/W123_native_r2_sign_convention_audit.py`
(34/34, exit 0).

Prior art, positioned honestly: W80 showed the fixed-ratio roots are negative and named the escapes
E1/E2; W82 computed the ker-Gamma input (d_RS_R2 = 0, closing E1) and branched the verdict on the
AF-vs-AS fork; W119 closed the regulator-dressing channel (Vieta argument). What no prior wave did:
pin the convention chain END TO END with an exact cross-lineage identity (part 1), prove the
perfect-square structure makes the flip unreachable from the matter side for ANY scalar sector
(part 2 strengthening), and prove the positive-sign exclusion as a monotonicity THEOREM covering the
non-fixed-ratio escape f_0^2 -> 0+ that the root analysis alone does not close (part 3).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| **Gravity functional** | induced `\|II\|^2` -> 4th-order class `gamma R + (R^2, C^2)` (H49/H25); NOT free Lagrangian-building | The port is honest only if GU's induced action is in the ported derivative class (it is, H49) AND its native relative signs match the literature convention the betas were derived in. That match is exactly what part 1 audits, with H25's natively computed `gamma > 0` (attractive gravity, two independent methods) as the GU-side anchor. |
| **Which f_0^2** | BOTH repo usages identified and mapped: W45-47/W119's `f_0^2` = agravity coupling (R^2 coefficient `1/(6 f_0^2)`); W79/W122's `f_0^2` = direct R^2 coefficient | The rule says name the object, not default silently. The two are reciprocal, hence sign-equivalent; the wobble is documented and verified harmless at sign level, flagged at magnitude level (Section 1.3). |
| **RS sector** | `ker Gamma`-projected gamma-traceless carrier (H58); its R^2 heat-kernel input `d_RS_R2 = 0` COMPUTED (W82) | The one native block that could have differed from the standard gravitino; it was computed, not anchored, and it contributes exactly zero to the R^2 beta. |
| **UV completion** | one-loop asymptotic FREEDOM (the branch under audit); the AS/Reuter branch is NOT adjudicated here | W123's verdicts are statements about the AF branch. The AF-vs-AS fork (W82) is untouched and remains the surviving escape. |
| **Krein grading vs loops** | grading acts on norms, not on the one-loop functional determinant | The Stelle 2+5+1 spectrum (graviton + massive spin-2 + scalaron) is exactly what the ported pure-gravity coefficients integrate over; the Krein grading reassigns norms (W119) and does not alter the heat-kernel divergences at this order. Stated, not newly proven. |

## 1. Persona 1 -- higher-derivative-gravity beta-function expert: the convention chain

### 1.1 The two literature bases and the known sign subtleties

The one-loop running of quadratic gravity exists in two main notational lineages:

- **Fradkin-Tseytlin / Avramidi-Barvinsky (lambda, omega):** Weyl coupling `lambda` asymptotically
  free; the R^2 direction carried by `omega`, whose one-loop beta has the famous quadratic numerator
  `200 omega^2 + 1098 omega + 25` with fixed points `omega* = -0.0228` (UV-attractive) and
  `-5.4671` -- BOTH negative. The negativity of the physical `omega*` is the AB lineage's own
  statement of the wrong-sign R^2 direction; it is not an agravity innovation.
- **Salvio-Strumia agravity (f_2^2, f_0^2):** `f_2` asymptotically free (`b_2 = 133/10 + matter`);
  `f_0` NOT asymptotically free; and -- their statement, in their convention -- the AF-complete
  branch has `f_0^2 < 0`, which is tachyonic since their scalaron mass is
  `M_0^2 = f_0^2 Mbar_Pl^2/2`. The tachyon-vs-AF tension is a named, published feature of the class
  (1403.4226; resolved in 1705.03896 by the `f_0 -> infinity` conformal limit, i.e. by REMOVING the
  R^2 term in the UV, not by flipping its sign).

The known trap for a porter: the R^2 coefficient appears with different placements
(`omega/(3 lambda)` vs `1/(6 f_0^2)` vs a direct coefficient `c`), different metric signatures, and
different Riemann-sign conventions across these papers. A sign lost at any joint would flip the
repo's conclusion. The audit therefore does not compare notation; it demands an exact identity.

### 1.2 The pin: an exact cross-lineage identity (DERIVED)

Substitute `omega = f_2^2/(2 f_0^2)` into the repo's ported system (W45 coefficients, pure-gravity
content). Symbolic result (test B1, exact):

```
(4pi)^2 d omega/dt = - f_2^2 * (200 omega^2 + 1098 omega + 25) / 60 .
```

This is precisely the published Avramidi-Barvinsky omega beta, and its roots `-0.022864, -5.467136`
(test A1) are the independently published fixed points. The correspondence extends to dynamics: the
repo's pure-gravity ratio roots `r* = -0.0915, -21.8685` equal `1/(2 omega*)` exactly, and the
UV-ATTRACTIVE objects map to each other (`Q'(r_2) < 0` at `r_2 = -21.87` <-> `N'(omega) > 0` at
`omega = -0.0228`; tests B2a-c).

Why this pins the convention: the SS-lineage numbers (133/10, 5/3, 5, 5/6) and the AB-lineage
quadratic (200, 1098, 25) were derived in DIFFERENT conventions by different groups two decades
apart. If the repo's port had dropped a sign anywhere in the (f_2^2, f_0^2) system, the derived
omega beta would NOT land on the published AB polynomial (the map `omega = f_2^2/(2 f_0^2)` has no
free sign to absorb an error in the mixed `5 x y` or inhomogeneous `5/3 x^2` terms; a flipped term
changes the numerator's coefficients, not just its overall sign). The identity holding exactly means
the two lineages agree, through the repo's encoding, on the invariant content.

### 1.3 The GU end of the chain, and the one wobble found

The literature end being internally consistent is not yet the audit; the chain must terminate on
GU's OWN action. Two joints:

1. **The Einstein coefficient.** The tachyon condition is `sign(m_0^2) = sign(gamma / c)` where
   `gamma` multiplies the induced Einstein term and `c` the R^2 term. `gamma > 0` is NOT ported: H25
   computed it natively on the induced `|II|^2` (the Gauss `-R^X` term), two independent methods,
   with the physically anchored meaning "attractive massless graviton" (the antigravity kill was
   excluded BY SIGN). A convention flip cannot fake a physical anchor.
2. **The scalaron mass formula.** W122 derived `m_0^2 = gamma/(6c)` natively (exact Legendre map, no
   gauge parameter anywhere). Test B3: under the convention map `c = 1/(6 f_0^2)`,
   `gamma = Mbar_Pl^2/2`, this coincides IDENTICALLY with the published agravity
   `M_0^2 = f_0^2 Mbar_Pl^2/2`. So the tachyon condition is the SAME physical statement at both ends
   of the port: the repo did not port a sign convention, it ported a physical condition whose GU-side
   ingredients (`gamma`, the Legendre route) are native.

**The wobble (found, documented, harmless).** The repo uses the symbol `f_0^2` for two DIFFERENT
objects: W45-47/W119 use the agravity coupling (R^2 coefficient `= 1/(6 f_0^2)`, per the W45
THEORY_SPACE table), while W79/W122 use `f_0^2` as the DIRECT R^2 coefficient (`m_0^2 =
gamma/(6 f_0^2)` is the direct-coefficient formula). The two are reciprocal up to a positive factor,
so every SIGN statement transfers (tests B4a-b: reciprocation preserves sign; the tachyon verdict is
identical in both readings). Magnitude formulas do NOT transfer between the readings (in the SS
reading the same mass is `gamma f_0^2 * 2/Mbar^2`-normalized); any future MAGNITUDE claim about
`m_0^2` must first name which object `f_0^2` denotes. Flagged for the repo; nothing standing on it
today is magnitude-level.

**Convention-audit verdict: CHAIN PINNED.** Physical anchors at both ends (H25 attractive gravity;
SS tachyon condition), exact identities at both joints (the omega map; the mass-formula
coincidence), one sign-harmless documented wobble.

### 1.4 Honest literature caveats (catalogued, not adopted)

- **Physical vs MS-bar running.** Buccio-Donoghue-Percacci (2403.02397) argue the physical
  (momentum-space) running of quadratic-gravity couplings can differ from the MS-bar running the
  whole arc uses. If the physical R^2 running differed in SIGN, the conclusion would move; nothing
  currently supports that, but it is a genuine beyond-scope channel, named here so it is not
  mistaken for closed.
- **Living-with-it proposals in the literature** (for the skeptic's ledger, Section 5): the
  `f_0 -> infinity` conformal limit (SS 1705.03896: the R^2 term, hence the scalaron, is absent in
  the UV); accepting a sub-Planckian-safe Landau pole with `f_0^2 > 0` (the SS phenomenological
  branch: non-AF, scalaron = inflaton); Euclidean contour/measure treatments (GHP, Mazur-Mottola --
  W122 delineated these as category-inapplicable to the Lorentzian mass sign); tachyon condensation
  (the mean-field version closed by W79; a qualitatively non-perturbative version remains
  hypothetical). None is adopted; each is a distinct research program, not a rescue in hand.

## 2. Persona 2 -- GU rep-theory specialist: the field content, block by block, graded

The one-loop R^2 beta in the pinned convention, assembled from per-field blocks:

| Block | Contribution to `(4pi)^2 beta_{f_0^2}` | Grade |
|---|---|---|
| 4th-order gravity multiplet = Stelle 2+5+1 (graviton + Krein-graded massive spin-2 + scalaron) | `(5/3) f_2^4 + 5 f_2^2 f_0^2 + (5/6) f_0^4` | PORTED-KNOWN (FT/AB/SS). This IS GU's gravity spectrum in the 4th-order landing (W78/W122 count); the Krein grading reassigns norms, not the one-loop determinant. |
| ker-Gamma RS (gamma-traceless vector-spinor) | `d_RS_R2 * f_0^4` with `d_RS_R2 = 0` | COMPUTED (W82; literature `a_2 = (7/20)W^2 + (31/120)E_4 + 4m^2R + 36m^4` has NO R^2 term -- re-asserted symbolically, test C1a). |
| massless fermions, gauge vectors (Sp-sector) | `0` | PORTED-KNOWN (one-loop conformal; only the Weyl beta `b_2` feels them, positively). |
| scalars with non-minimal `xi_a` | `+ sum_a w_a (xi_a + 1/6)^2 f_0^4`, `w_a > 0` | PORTED-structure (SS). A PERFECT SQUARE: cannot be negative for any multiplicity or any `xi` (test C2a). |
| RS Weyl-side | enters only `b_2` via `c_RS_weyl` in `[1.02, 1.82]` | PORTED-band (W47), sign COMPUTED positive (W82 `W^2` coefficient `7/20 > 0`). |

Where derived vs ported, honestly: the ONLY block ever at risk of being GU-different was the
ker-Gamma RS (the one genuinely program-native carrier), and it was COMPUTED (W82), landing on
exactly zero. The gravity block is ported and remains ported -- but it is not "extra matter": it is
the loop of GU's own 2+5+1 spectrum, and any claim that GU's native graviton loop differs from the
literature's is a claim that the literature computation of the SAME spectrum is wrong, not that a
different theory was ported. That reclassification is the real yield of the audit: the escape is no
longer "maybe the port garbled GU"; it would have to be "maybe FT/AB/SS is wrong about quadratic
gravity itself" (or the truncation/physical-running caveats of 1.4).

## 3. Persona 3 -- FRG/flow analyst: the phase portrait (part 3 as a computation)

Variables `x = f_2^2`, `y = f_0^2`, ratio `r = y/x`, rescaled time `ds = kappa x dt` (monotone
whenever `x > 0`; `s -> infinity` along AF trajectories since `x ~ 1/(kappa b_2 t)`).

1. **Monotonicity theorem (the new closure).** For `y > 0` and `x >= 0`, every term of `beta_y =
   kappa[(5/3)x^2 + 5xy + A y^2]` is nonnegative and `beta_y >= (5/6) kappa y^2 > 0` (test D1a). So
   toward the UV a positive `f_0^2` STRICTLY INCREASES: it can never approach `0+`, and the
   comparison ODE gives a hard Landau bound `Delta t <= (4pi)^2 (6/5)/y_0` (verified numerically,
   pole at `t = 292 < 632` for `y_0 = 0.3`, test D1c). This closes the one escape the fixed-ratio
   root analysis (W80/W82) did not by itself close: a hypothetical non-fixed-ratio AF trajectory
   with `f_0^2 -> 0+`. There is none; positivity of `f_0^2` is self-terminating.
2. **The `y = 0` line is not invariant** (`beta_y(x,0) = (5/3) kappa x^2 > 0`, test D1d): the
   gravity-induced R^2 generation term pushes any zero crossing INTO the doomed positive region
   toward the UV. Even starting exactly at `f_0^2 = 0` is not AF-completable.
3. **`x < 0` excluded** (`beta_x = -kappa b_2 x^2 < 0` always): a negative `f_2^2` runs to
   `-infinity` in finite `t` (test D2). AF requires `f_2^2 > 0` -- which is also the sign on which
   the massive spin-2 has a real mass (W119's Krein-gradable branch); the C^2-side convention is
   thereby anchored by the flow itself, not by notation.
4. **Basin characterization** (anchor `b_2 = 14.7167`; conclusions band-swept in Section 4):
   `dr/ds = Q(r) = A r^2 + (5 + b_2) r + 5/3` with roots `r_1 = -0.0848` (`Q'(r_1) > 0`, REPULSIVE
   separatrix) and `r_2 = -23.575` (`Q'(r_2) < 0`, UV-ATTRACTIVE). The AF basin is EXACTLY
   `{ x > 0, r <= r_1 }`: every start with `r < r_1` flows to `r_2` and reaches the Gaussian FP with
   `y < 0` at every step (`y/x -> r_2`, verified, test D3b); every start with `r > r_1` -- including
   small-NEGATIVE `y` (`r_0 = -0.05`) -- Landau-poles (test D3c). The exact fixed-ratio trajectory
   `r = r_1` is the measure-zero separatrix, also negative-`y`. A tiny-positive start `r_0 = +2e-6`
   diverges in finite rescaled time (test D1e).

**Trajectory-existence verdict: `f_0^2 > 0` is FORBIDDEN on every AF trajectory, at every finite
scale, including asymptotically.** Not "disfavored", not "repelled": positivity is incompatible with
AF-completeness by monotonicity, and the boundary cases (`y = 0` axis, `x = 0` axis, `r = r_1`
separatrix) are each individually closed.

## 4. Persona 4 -- symbolic/numerical engineer: what the test proves and how

`tests/W123_native_r2_sign_convention_audit.py`, 34 checks, exit 0, sympy + numpy, deterministic
(no RNG). Positive controls FIRST (per the brief): the AB omega roots `-0.0228/-5.4671` and the W46
roots `-0.0848/-23.575` are reproduced before any new claim (tests A1-A2). Then:

- **B1** the omega-map identity, EXACT symbolic (`sp.simplify(...) == 0`), pure gravity.
- **B2** root and attractivity correspondence between the two lineages (numeric to 1e-6).
- **B3** the mass-formula coincidence, exact symbolic.
- **B4** the reciprocal wobble: sign-preservation exact symbolic; tachyon verdict identical in both
  readings under `gamma > 0, f_0^2 < 0` assumptions.
- **C1** the W82 `a_2` has zero R^2 coefficient (symbolic Poly extraction); `W^2` coefficient
  positive.
- **C2-C3** the perfect-square structure and the Vieta sign theorem for symbolic `A > 0`,
  `b_2 > 0` (assumption-checked, not numeric).
- **C4** grid sweep: `c_RS_weyl` over the W47 band [1.02, 1.82] (81 points, binding check: two real
  roots, both negative, throughout) and wide `[-13.2, 20]`; `d_RS_R2` in `(-5/6, 2]`; scalar square
  in `[0, 3]`; max root over the whole admissible grid `= -0.0435 < 0`; where the discriminant goes
  negative (large A) there is NO fixed ratio (loss of AF), never a positive root.
- **C5** negative control: `d = -1 < -5/6` DOES produce a positive root -- the flip lever is real
  and the test can see it; the admissible band simply cannot reach it (W82: `d = 0` computed).
- **D1-D4** the monotonicity theorem (symbolic nonnegativity), the Landau bound (numeric RK4 beats
  the analytic bound), the non-invariance of `y = 0`, the finite-`s` divergence of the tiny-positive
  start via the exact 1D ratio flow, the `x < 0` exclusion, the basin runs with ratio-convergence
  detection (`y/x -> r_2` to 0.5 absolute at `t = 2e5`), and the pure-R^2 axis.

Numerical honesty notes: the AF-detection threshold accounts for the logarithmic decay
(`|y| ~ |r_2| x`, so the `y` cutoff carries the factor 23.6); blow-up declared at `1e9` with RK4
step 0.2-0.5, far from stiffness until the pole; the 1D `s`-integration uses explicit Euler with
step `1e-3` on a monotone blow-up, where overshoot only accelerates the (correct) divergence
verdict.

## 5. Persona 5 -- adversarial skeptic: steelman "the tachyon is native and robust"

**The steelman now stands stronger than before this wave, and I state it at full strength.** On the
asymptotically-free branch of GU's UV completion, the scalaron tachyon is: not gauge (W78/W122,
three legs); not norm-negative (W79: positive-norm, so the Krein machine has nothing to grade); not
background-liftable (W79); not regulator-liftable (W119); not field-content-liftable (W82 + Section
2: the only native block is computed zero, and all matter blocks are perfect squares); not
convention-borne (Section 1: the chain is pinned by exact identities with physical anchors at both
ends); and not trajectory-avoidable (Section 3: positivity of `f_0^2` is self-terminating, and even
`f_0^2 -> 0+` is impossible). Within one-loop quadratic gravity, GU's AF branch carries a genuine,
propagating, positive-norm tachyonic scalaron on EVERY trajectory. That is the honest reading, and
"the ported number might be a porting artifact" is no longer an available escape: W123 checked the
port and the port is faithful.

**What it kills:** the hope that GU's native computation would quietly differ in sign from the
higher-derivative-gravity literature. The AF branch's tachyon is a theorem of the class GU's induced
action lands in (H49), with GU's own content plugged in across its full uncertainty band.

**What it does NOT kill (the surviving doors, each named, none adopted):**
1. **The AF-vs-AS fork (W82's E2) -- the principal door.** On a Reuter-type completion the R^2
   direction is relevant and its sign is a free boundary condition; W82's verdict
   TRUNCATION-AMBIGUOUS stands. W123 says nothing new about which fork GU realizes; it says the AF
   fork's tachyon is native, not an artifact.
2. **Beyond-one-loop / physical-running** (Buccio-Donoghue-Percacci-type): a computation, not a
   hope; currently no evidence it flips anything.
3. **The `f_0 -> infinity` conformal limit** (SS 1705.03896): removes the scalaron rather than
   healing it; a different UV completion with its own costs (the conformal-mode dynamics returns in
   other guises).
4. **Beyond-4th-order `|II|^2` invariants** (W122's item 2): non-constant `f''(R)` would re-open
   vacuum lifting; not computed.
5. **Qualitatively non-perturbative condensation:** hypothetical; mean-field version closed (W79).

**Where the skeptic must stop.** The class-theorem status cuts both ways: because the tachyon is a
feature of quadratic gravity's AF branch generally (AB's own `omega* < 0`; SS's own tension), it is
not a GU-SPECIFIC defect -- every AF quadratic-gravity program faces it, and the literature's
survival strategies (door 3, and AS itself) are exactly the doors left open above. GU's exposure is
that its induced action FORCES it into this class (H49); GU's asset is that its induced EH sector is
also precisely the de-slaving mechanism on the AS branch (W82). The fork, not the sign, is now the
whole question.

## 6. Verdict (the brief's return fields)

- **Convention-audit: CHAIN PINNED.** Exact omega-map identity; AB roots reproduced; mass-formula
  coincidence; physical anchors at both ends (H25 native `gamma > 0`; SS tachyon condition). One
  documented sign-harmless wobble (coupling vs direct coefficient), flagged for magnitude-level
  future work.
- **Native R^2 beta sign across the band: NEGATIVE-ROBUST.** `A = 5/6 + 0 + (perfect squares) > 0`
  for the entire W47 band, far beyond it, and any scalar sector; both fixed-ratio roots strictly
  negative everywhere admissible.
- **Fixed-ratio sign survival: ROBUST** (not FLIPS-IN-BAND, not CONVENTION-ARTIFACT).
- **Positive-f_0^2 AF trajectory: FORBIDDEN** (monotonicity theorem; includes the asymptotic
  `f_0^2 -> 0+` escape; basin = `{f_2^2 > 0, r <= r_1}`, negative at every finite scale).
- **Tachyon verdict update: NATIVE-ROBUST on the AF branch; NARROWED-TO the AF-vs-AS fork (E2) plus
  the named beyond-one-loop caveats.** The porting-artifact escape W122 named is CLOSED. The no-go
  remains conditional on the AF fork exactly as W82 left it; nothing here selects the fork.

## 7. What would settle the remainder

1. **The fork selection** (unchanged, now the unique principal door): a full FRG `f(R) + Weyl^2`
   truncation with GU's ker-Gamma content and induced `(g, lambda)`, asking which fixed point GU's
   physical trajectory enters (W82 item 1).
2. **A GU-native graviton loop** would upgrade the pure-gravity block from PORTED-KNOWN to DERIVED;
   after this audit the expected yield is confirmation (a sign difference would now mean the
   literature is wrong about quadratic gravity, not that the port was unfaithful) -- honest but low
   marginal value relative to item 1.
3. **Physical-vs-MS-bar running** in the R^2 direction (catalogued caveat): a real computation in
   the recent literature's spirit, if item 1 lands on the AF side.

## What this does NOT do

No canon / RESEARCH-STATUS / claim-status / verdict / posture change. No AF-vs-AS fork selection.
No GU-native loop amplitude (W48 gate). No edit to any prior wave's file. H59/H61a remain **OPEN**.
The W79/W122 no-go remains conditional on the AF branch of the UV-completion fork; W123 removes the
porting-artifact escape from that conditionality and proves the positive-sign exclusion
trajectory-complete.
