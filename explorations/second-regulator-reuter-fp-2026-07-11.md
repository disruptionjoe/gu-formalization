---
artifact_type: exploration
status: exploration (5-persona inline team; second-regulator robustness swing; deterministic test)
created: 2026-07-12
hypothesis: "Condition (i) of the W83 AS-SELECTED-CLOSES verdict -- is GU's non-Gaussian Reuter (asymptotic-safety) fixed point GENUINE, or a truncation/scheme ARTIFACT? Test by regulator independence: recompute with a SECOND regulator (exponential vs the W83/W81 Litim/optimized) and check the FP and its load-bearing qualitative features survive."
branch: "SECOND-REGULATOR -- redo the Reuter-FP search with an EXPONENTIAL regulator r(y)=y/(e^y-1) against the W83/W81 Litim/optimized r(y)=(1-y)theta(1-y). Check the regulator-INVARIANTS the W83 verdict actually rests on: (I1) FP EXISTENCE; (I2) the NUMBER and SIGN of the critical exponents (# relevant directions); (I3) the RELEVANCE of f_0^2 (load-bearing -- its relevance de-forces sign(f_0^2) and closes the observer leg); (I4) GU's ker-Gamma RS anti-screening SIGN (magnitude may move, sign must not). Values g*,lambda*,f_0^2* WILL move -- that motion is NOT fragility; only the invariants are the genuine test. Port the known regulator-robustness of the sub-results (EH Reuter FP: Lauscher-Reuter; f(R)/R^2 relevance: Codello-Percacci-Rahmede, Benedetti-Machado-Saueressig) and compute GU's RS-matter contribution's regulator-(in)dependence, being explicit about ported vs computed."
title: "The GU Reuter fixed point SURVIVES the second regulator at first-swing grade -> condition (i) UPGRADES from conditional TOWARD confirmed. A genuinely-different second regulator (exponential r=y/(e^y-1), its threshold functions Phi^p_n(0) COMPUTED here by quadrature and shown to differ from Litim's 1/n! by O(1) factors) moves the FP VALUES g*,lambda* (as it must) but leaves ALL FOUR load-bearing INVARIANTS intact: (I1) the Reuter FP EXISTS under both regulators (g*>0, 0<lambda*<1/2); (I2) the critical exponents stay a complex-conjugate pair with POSITIVE real part -> exactly 2 relevant directions in EH, stable in number and sign across sharp/exponential/optimized while g*lambda* stays in a narrow band (Lauscher-Reuter, ported); (I3) f_0^2 stays RELEVANT -- the de-slaving mechanism needs only g*!=0, which holds in both regulators, and R^2-relevance + the 3-relevant + 1-irrelevant critical surface are regulator- AND truncation-robust (CPR/BMS/AS-Starobinsky, ported); (I4) GU's ker-Gamma RS anti-screening SIGN is regulator-independent because the spin-3/2 budget factorizes as (heat-kernel/spin coefficient, sign-fixed) x (threshold function, positive-definite for any admissible regulator) -- A_tot>0 and RS RAISES it under BOTH regulators (magnitude moves, sign does not; the scalar-heavy refutation guard still fires under the second regulator too). VERDICT: ROBUST (first-swing: ported sub-results + structural RS sign) -> condition (i) upgrades conditional -> toward confirmed; NOT FRAGILE (no invariant failed). RESIDUAL: NEEDS-FULL-COMPUTATION -- a full COMBINED f(R)+Weyl^2 + ker-Gamma spin-3/2 FUNCTIONAL second-regulator run is still outstanding to make the combined object's robustness unconditional. LOAD-BEARING ASSUMPTION: the spin-3/2 budget's (coefficient)x(positive Phi) factorization keeps the anti-screening SIGN in the coefficient -- the ker-Gamma PROJECTION could in principle alter the effective coefficient, which only a full second-regulator ker-Gamma heat-kernel would settle."
grade: "COMPUTED / analysis. HIGH confidence on the regulator-INVARIANTS surviving: I computed two genuinely-different regulator threshold functions (Litim closed-form 1/n! validated against my own quadrature; exponential by quadrature, differing by O(1)); showed FP EXISTENCE + value-MOTION in a transparent reduced EH model; and computed GU's RS anti-screening SIGN invariance via the (coefficient)x(positive-threshold) factorization, with the scalar-heavy refutation guard still firing under the second regulator. MEDIUM-HIGH on the combined condition-(i) upgrade, because the g*lambda*/critical-exponent EH robustness (I2) and the f_0^2/R^2-relevance + critical-surface-dim robustness (I3) are PORTED from the literature (Lauscher-Reuter; Reuter-Saueressig; Codello-Percacci-Rahmede; Benedetti-Machado-Saueressig; AS-Starobinsky), NOT recomputed from a full functional second-regulator run. Ported/cited: EH Reuter-FP cutoff-robustness (weak cutoff/gauge dependence of lambda* and critical exponents -- Lauscher-Reuter; the g*lambda* narrow band + complex-conjugate relevant pair -- Reuter-Saueressig Living Review); f(R) 3-dimensional UV critical surface (Codello-Percacci-Rahmede); higher-derivative 3+1 relevance with R^2 relevant (Benedetti-Machado-Saueressig); positive-R^2 relevant branch (AS-Starobinsky). Computed here: the two regulators' threshold functions; the reduced-EH FP existence+motion under both; the RS anti-screening sign-invariance + refutation guard under the second regulator. Deterministic test tests/W85_second_regulator_reuter.py, exit 0. NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN."
depends_on:
  - explorations/frg-fr-weyl-af-as-fork-2026-07-11.md
  - explorations/E2-asymptotic-safety-2026-07-11.md
  - explorations/true-fixed-point-f0-sign-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W81_E2_asymptotic_safety.py
  - tests/W83_frg_fr_weyl_af_as.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W85_second_regulator_reuter.py
external_refs:
  - "Reuter, Nonperturbative evolution equation for quantum gravity, Phys. Rev. D57 (1998) 971, hep-th/9605030 -- the Reuter fixed point"
  - "Lauscher & Reuter, Ultraviolet fixed point and generalized flow equation of quantum gravity, Phys. Rev. D65 (2002) 025013, hep-th/0108040 -- CUTOFF/GAUGE dependence: lambda* and critical exponents weakly dependent -> not a truncation artifact"
  - "Reuter & Saueressig, Quantum Einstein Gravity, New J. Phys. 14 (2012) 055022, arXiv:1202.2274 -- Living Review: regulator comparison, g*lambda* narrow band, complex-conjugate relevant pair"
  - "Codello, Percacci & Rahmede, Ultraviolet properties of f(R)-gravity, Int. J. Mod. Phys. A23 (2008) 143 / Ann. Phys. 324 (2009) 414, arXiv:0805.2909 -- 3-dimensional UV critical surface, robust"
  - "Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984 -- higher-derivative Reuter FP: 3 relevant + 1 irrelevant, R^2 relevant"
  - "Dona, Eichhorn & Percacci, Matter matters in asymptotically safe quantum gravity, PRD 89 (2014) 084035, arXiv:1311.2898 -- matter bounds; gravitino/spin-3/2 anti-screens, extends the region"
  - "Copeland, Rahmede & Saltas / Bonanno et al., Asymptotically Safe Starobinsky Inflation, arXiv:1311.0881 -- positive-R^2 relevant branch"
  - "Litim, Optimized renormalization group flows, Phys. Rev. D64 (2001) 105007, hep-th/0103195 -- the optimized/Litim regulator; threshold functions"
---

# Second-regulator robustness of GU's Reuter fixed point (condition (i) of the W83 verdict)

**Role.** W83 landed **AS-SELECTED-CLOSES (CONDITIONAL)** on GU's asymptotic-safety UV completion,
explicitly **gated by two named truncation assumptions**. This document works **assumption (i)**: *is the
non-Gaussian Reuter fixed point GENUINE, or a scheme/truncation artifact?* The paradigm's own answer to
"is this FP an artifact?" is **regulator independence** -- recompute with a second regulator and check
the FP and its load-bearing qualitative features survive. W81/W83 used a single (optimized/Litim-type)
scheme. **This swing brings a genuinely different second regulator (exponential) and checks the
invariants.** Test: `tests/W85_second_regulator_reuter.py` (deterministic, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Load-bearing here |
|---|---|---|
| **UV completion** | The AF-vs-AS fork; this document lives entirely on the **AS/Reuter** branch and stress-tests it | Condition (i) is precisely "is the AS branch's FP real?" -- the whole point is to test, not assume it |
| **Gravity action** | GU-native induced `\|II\|^2 -> ` 4th-order Stelle `(f_2^2,f_0^2)` + induced Einstein `(g,lambda)` | The FRG FP and its critical surface live here; the ported EH + f(R) robustness applies because GU's induced action is in the same derivative class |
| **RS sector** | `ker Gamma`-projected spin-3/2 (H58); anti-screens (`W^2>0`, W82) | **The RS-specific regulator check.** Its anti-screening SIGN must survive the second regulator or GU could exit the DEP region. This is the adversary's sharpest demand and is answered structurally |
| **Regulator/scheme** | *(new fork, named)* the FRG cutoff shape function: **optimized/Litim** `r(y)=(1-y)theta(1-y)` (W81/W83) **vs EXPONENTIAL** `r(y)=y/(e^y-1)` (this swing) | The scheme is NOT a physics fork -- it is a **calculational-convention** axis. Physical (universal) content must be scheme-independent; that IS the test of whether the FP is genuine |

## 1. Persona 1 -- FRG specialist: the second regulator, the FP, and the invariants

### 1.1 The discipline, stated first: what moves vs what must not

FRG fixed-point **values are regulator-dependent** and **will move** between schemes. This is not a
weakness of the method; it is a known feature (the effective average action is a scheme-dependent
object; only universal quantities are scheme-invariant in the exact theory, with residual
scheme-dependence in any truncation). So the genuine test of "is the FP an artifact?" is **not** "do
`g*, lambda*, f_0^2*` stay put" (they won't) -- it is whether the **invariants** survive:

- **(I1) EXISTENCE** of the non-Gaussian FP.
- **(I2) the NUMBER and SIGN of the critical exponents** (= number of relevant directions).
- **(I3) the RELEVANCE of `f_0^2`** -- the single load-bearing feature: its *relevance* (not its value)
  is what de-forces `sign(f_0^2)` and closes the observer Krein-TT spin-0 leg (W81/W82/W83).
- **(I4) GU's ker-Gamma RS anti-screening SIGN** -- its magnitude may move, but if its *sign* flipped,
  GU could fall outside the Dona-Eichhorn-Percacci allowed region under the second regulator.

### 1.2 A genuinely different second regulator (COMPUTED)

The two shape functions and their FRG threshold functions
`Phi^p_n(0) = (1/Gamma(n)) INT_0^inf dy y^{n-1} [r - y r']/[y + r]^p`:

- **Litim/optimized** `r(y)=(1-y)theta(1-y)`: numerator supported on `y<1` with `y+r=1` there, so
  `Phi^p_n(0) = 1/Gamma(n+1) = 1/n!` (closed form).
- **Exponential** `r(y)=y/(e^y-1)`: with `r - y r' = y^2 e^y/(e^y-1)^2` and `y+r = y e^y/(e^y-1)`,
  `Phi^p_n(0)` is a convergent integral **computed by quadrature**.

They are **genuinely different** -- e.g. `Phi^1_1(0)`: Litim `1.000` vs exponential `1.645`; `Phi^1_2(0)`:
Litim `0.500` vs exponential `2.404`; `Phi^2_2(0)`: Litim `0.500` vs exponential `1.000`. **These O(1)
differences ARE the mechanism by which `g*, lambda*` move between schemes** -- computed, not asserted.
Both are strictly **positive-definite** (admissible cutoffs) -- the property that makes the
anti-screening sign regulator-independent (Sec. 1.5).

### 1.3 (I1) EXISTENCE + value-motion (COMPUTED, reduced EH model)

A transparent reduced EH Reuter system with the regulator carried by the threshold weights
(`beta_g = 2g - A phi_2 g^2`, `beta_lambda = -2 lambda + g(B_0 phi_1 - B_1 lambda)`) gives a finite
non-Gaussian FP for **both** regulators: Litim `(g*=0.70, lambda*=0.16)`, exponential
`(g*=0.35, lambda*=0.43)` -- **existence is invariant**, and the **values move** (`|dg*|=0.35`,
`|dlambda*|=0.27`) exactly as the discipline expects. (This reduced model demonstrates
existence + motion; it is **not** calibrated to reproduce the product-stability -- that is ported, Sec.
1.4.)

### 1.4 (I2) # relevant directions + the `g*lambda*` band (PORTED)

The EH Reuter-FP regulator-robustness is a well-established literature result. Across sharp /
exponential / optimized cutoffs the individual `g*, lambda*` vary by `O(1)` (`g*` relative spread `~50%`),
but **(a)** the product `g*lambda*` sits in a **narrow band** (`~0.13-0.14`, relative spread `<3%`),
and **(b)** the critical exponents are a **complex-conjugate pair with positive real part** -> exactly
**2 relevant directions** in EH, **stable in number and sign** in every regulator (Lauscher-Reuter
found `lambda*` and the critical exponents only weakly cutoff/gauge dependent -- the canonical
"not-an-artifact" evidence; Reuter-Saueressig Living Review tabulates the regulator comparison).

### 1.5 (I4) GU's RS anti-screening SIGN is regulator-independent (COMPUTED, structural)

A field's contribution to the anti-screening budget factorizes as
`delta A_field = (heat-kernel/spin coefficient b_field) x (threshold function Phi > 0)`. The threshold
function is **positive for both regulators** (Sec. 1.2); the **sign** lives in `b_field`, a heat-kernel/
spin fact (spin-3/2 gravitino / ker-Gamma RS anti-screens `b>0`; scalars/Dirac screen `b<0` -- DEP).
So `sign(A_tot)` and "RS **raises** `A_tot`" are **regulator-independent**; only the magnitude moves.
Computed under both regulators' weights: Litim `A_tot: 2.08 -> 2.11` (RS raises), exponential
`A_tot: 2.16 -> 2.22` (RS raises); both `>0` (FP preserved). And the **refutation guard still fires under
the second regulator**: a scalar-heavy (MSSM-like) content gives `A_tot <= 0` (FP destroyed) even with
RS -- so the preservation is genuinely content-conditional in **both** schemes, earned by GU's content,
not by regulator choice.

### 1.6 (I3) `f_0^2` relevance is regulator-invariant (mechanism COMPUTED, sign PORTED)

The de-slaving that makes `f_0^2` relevant at the Reuter FP requires only `g*!=0` (the induced-Einstein
sector feeds an effective linear term into `beta_{f_0^2}` -- W83 Sec. 1.3). Since `g*>0` holds under
**both** regulators (Sec. 1.3), the **mechanism is present in both schemes** -- not a single-regulator
accident. The relevance **sign** (R^2 relevant) and the **3 relevant + 1 irrelevant** critical-surface
dimension are **regulator- AND truncation-robust** in the literature (Codello-Percacci-Rahmede's
3-dimensional critical surface; Benedetti-Machado-Saueressig's higher-derivative 3+1 with R^2 relevant;
AS-Starobinsky's positive-R^2 relevant branch). This is the regulator-invariance of the load-bearing
feature.

## 2. Persona 2 -- math referee: are these the right invariants? ported vs computed?

- **Are these the right invariants?** **Yes.** The referee affirms that "is the FP an artifact?" is
  correctly operationalized as regulator independence of **existence + universal content**, not of the
  (non-universal) FP coordinates. I1-I4 are exactly the scheme-invariant data the W83 verdict rests on:
  W83 needs the FP to *exist*, `f_0^2` to be *relevant* (to de-force the sign), the critical-surface
  *dimension* to be finite/sensible, and GU's RS matter to keep it *preserved* (anti-screening sign).
  Values `g*, lambda*, f_0^2*` are **not** load-bearing for any W83 conclusion -- W83 itself graded them
  SCHEMATIC. **Grade on invariant-choice: HIGH.**
- **Ported vs computed -- the honest ledger.** COMPUTED here: the two regulators' threshold functions
  (Litim closed form validated against own quadrature; exponential by quadrature); reduced-EH FP
  existence + value-motion under both; RS anti-screening sign-invariance + the refutation guard under
  the second regulator. PORTED (cited): the EH `g*lambda*` band + complex-conjugate relevant pair
  (I2); the f(R)/R^2 relevance + 3+1 critical-surface dim (I3-sign). The referee **requires** this be
  labeled loudly, and it is (the test's PART headers and the grade). **The referee will NOT certify a
  full second-regulator computation of the combined truncation -- that was not done.**
- **The load-bearing gap.** The invariants that were *computed* here (I1 existence-form, I4 RS sign)
  are structural and solid; the invariants that carry the most weight for the observer leg (I2 relevant
  count, I3 f_0^2 relevance) are **ported**. So the referee's ruling: condition (i) is **upgraded toward
  confirmed at first-swing grade**, not proven -- the ported sub-results are individually robust and
  GU's RS-specific contribution's sign is regulator-independent, but the **combined** object's full
  second-regulator functional run remains outstanding. **Grade: MEDIUM-HIGH on the upgrade.**

## 3. Persona 3 -- adversary: presses fragility

**"You PORTED the robustness instead of computing it."** **Conceded, and named as the residual.** The
two invariants that most directly close the observer leg -- I2 (2 relevant directions, stable) and I3
(`f_0^2` relevance) -- are ported from Lauscher-Reuter / CPR / BMS, not recomputed from a full
functional second-regulator run of *GU's combined truncation*. Answer: (a) what a first swing *can*
legitimately do is port the **known** regulator-robustness of the sub-results and check the *new*
GU-specific piece; (b) the ported facts are among the most-checked in the AS literature (the EH FP's
cutoff-robustness and the f(R) critical surface have been recomputed across many regulators, gauges, and
truncation orders); (c) the swing does **not** claim a computed combined result -- the verdict carries an
explicit **NEEDS-FULL-COMPUTATION residual**. But the adversary is right that this is an *import*, not a
*proof*, for I2/I3. **Not defeated -- named.**

**"The spin-3/2 matter contribution's regulator-dependence was NOT checked."** **This is the sharpest
attack and it is answered structurally, not ported.** I4 is *computed* here: the RS budget factorizes as
`(heat-kernel/spin coefficient) x (positive threshold function)`, so the **sign** is carried by the
coefficient (a spin fact) and the threshold function -- positive for any admissible regulator -- cannot
flip it; A_tot stays `>0` and RS still *raises* it under the exponential regulator, and the scalar-heavy
guard still fires. **The residual the adversary can still press:** the **ker-Gamma PROJECTION** could
alter the *effective* coefficient `b_RS` away from the standard massless-gravitino value (the same open
item W45/W81 flagged as the named parameter `C_RS_WEYL`), and only a full ker-Gamma heat-kernel *with
the second regulator* would pin its magnitude. But note: to flip the **sign** would require the
projection to drive `b_RS` negative, which contradicts the computed `a_2 = (7/20) W^2 > 0` (W82) -- so
the sign is doubly protected. **The magnitude is open; the sign is robust.**

**"The reduced EH model is a toy -- it proves nothing."** Partially fair: the reduced model demonstrates
only I1 (existence) + value-motion, and is explicitly **not** used for I2 (that is ported). It is not
load-bearing beyond showing that a genuinely-different threshold function moves the values while keeping
the FP -- which is the qualitatively correct behavior. **The toy is honestly scoped.**

**Adversary residual (named).** Condition (i) is upgraded, not closed: I2/I3 are ported (robust but
imported) and the ker-Gamma `b_RS` *magnitude* under a second regulator is uncomputed. Neither is a
failure of an invariant; both are the "full-computation" residual.

## 4. Persona 4 -- cross-checker: the literature robustness + GU's matter contribution

- **EH Reuter-FP robustness (I1, I2).** Lauscher-Reuter (hep-th/0108040): the dimensionless cosmological
  constant `lambda*` and the critical exponents are only **weakly** dependent on the cutoff and gauge
  parameters -- the canonical evidence that the FP is *not* a truncation artifact. Reuter-Saueressig
  Living Review (1202.2274): across regulators `g*, lambda*` move but `g*lambda*` sits in a narrow band
  and the critical exponents remain a **complex-conjugate pair with positive real part** (2 relevant).
  My PART-C table encodes representative values (optimized/Litim, sharp, exponential) and the invariant
  checks pass on them. **Consistent.**
- **f(R)/R^2 relevance (I3).** Codello-Percacci-Rahmede (0805.2909): the f(R) UV critical surface is
  **3-dimensional**, robust across their polynomial truncations. Benedetti-Machado-Saueressig
  (0901.2984): the higher-derivative FP has **3 relevant + 1 irrelevant** with R^2 relevant.
  AS-Starobinsky (1311.0881): the positive-R^2 direction is relevant/attractive. All regulator- and
  truncation-robust -- **matches I3**.
- **GU's RS matter (I4).** Dona-Eichhorn-Percacci (1311.2898): spin-3/2 anti-screens, extends the
  allowed region; the *sign* is a spin/heat-kernel fact independent of the cutoff shape. GU's ker-Gamma
  RS `a_2 = (7/20) W^2 > 0` (W82) is on the anti-screening side. Factorized against a positive threshold
  function, the sign survives any admissible regulator -- **the computed I4 is consistent with the DEP
  physics and the W82 native `a_2`.**

## 5. Persona 5 -- synthesizer: the verdict

**SECOND REGULATOR BROUGHT.** Exponential `r(y)=y/(e^y-1)` vs the W81/W83 Litim/optimized
`r(y)=(1-y)theta(1-y)`; their threshold functions `Phi^p_n(0)` are **computed** and differ by O(1)
factors -- the genuine source of the FP-value motion.

**DOES THE REUTER FP SURVIVE?** **YES, at first-swing grade, on all four invariants:**
- **(I1) EXISTENCE** -- the non-Gaussian FP exists under both regulators (`g*>0`, `0<lambda*<1/2`)
  [computed, reduced EH].
- **(I2) # RELEVANT DIRECTIONS** -- a complex-conjugate pair with positive real part -> **2 relevant**
  in EH, stable in number and sign across regulators, with `g*lambda*` in a narrow band while `g*`
  varies widely [ported: Lauscher-Reuter, Reuter-Saueressig].
- **(I3) `f_0^2` RELEVANCE** -- the de-slaving needs only `g*!=0` (holds in both regulators); R^2
  relevance + the **3 relevant + 1 irrelevant** critical surface are regulator- and truncation-robust
  [mechanism computed; sign ported: CPR, BMS, AS-Starobinsky].
- **(I4) GU's RS ANTI-SCREENING SIGN** -- factorizes as (sign-fixed heat-kernel coefficient) x (positive
  threshold function), so `A_tot>0` and RS **raises** it under **both** regulators; the scalar-heavy
  refutation guard still fires under the second regulator [computed, structural].

**THE VALUES MOVE** (`g*, lambda*` shift O(1) between regulators) -- and **that motion is NOT fragility**;
it is exactly what an honest FRG computation expects. **No invariant failed.**

**VERDICT: ROBUST (first-swing: ported sub-results + structural RS sign).** Condition (i) -- the Reuter
FP is genuine, not a scheme artifact -- **UPGRADES from conditional TOWARD confirmed**. The invariants
the W83 verdict actually rests on all survive the second regulator. **NOT FRAGILE** (no invariant moved
in a way that weakens the AS selection). **RESIDUAL: NEEDS-FULL-COMPUTATION** -- a full **combined**
`f(R)+Weyl^2 + ker-Gamma spin-3/2` **functional** second-regulator run (not done here; I2/I3 are ported
and the ker-Gamma `b_RS` *magnitude* under a second regulator is uncomputed) is still required to make
the combined object's robustness **unconditional**. This is the honest register: the ported sub-results
are robust and GU's RS-specific sign is regulator-independent, so condition (i) is materially
strengthened, short of a full recomputation.

**Effect on W83.** Condition (i) moves from "named-but-untested" toward "supported": the AF-NOGO escape
(which required the Reuter FP to be a scheme artifact) is **weakened** -- no invariant supports it under
the second regulator. W83's `AS-SELECTED-CLOSES (CONDITIONAL)` becomes **less conditional on (i)**,
though assumption (ii) (W79's tachyon genuine, not a 4th-order artifact) is untouched by this swing.

**Load-bearing assumption (single, named).** The spin-3/2 anti-screening contribution **factorizes** as
`(regulator-independent heat-kernel/spin coefficient) x (positive threshold function)`, so its **sign**
is carried by the coefficient, not the regulator. Standard FRG factorization supports this, and the sign
is doubly protected by W82's computed `a_2 = (7/20)W^2 > 0`; but the ker-Gamma **projection** could alter
the effective coefficient's **magnitude**, which only a full second-regulator ker-Gamma heat-kernel would
settle.

**Confidence.** HIGH on the computed pieces (two distinct regulators; existence + motion; RS sign
invariance + refutation guard under the second regulator). MEDIUM-HIGH on the combined condition-(i)
upgrade, gated by the ported status of I2/I3 and the uncomputed ker-Gamma `b_RS` magnitude. **Credibility
floor (fork-independent):** the scalaron is positive-norm (W79), so the spin-0 loop-positivity leg closes
regardless; the GU-independent observer theorems stand regardless.

## 6. What this does and does not do

**Does:** bring a genuinely different second regulator (exponential), compute its threshold functions and
show they differ from Litim's by O(1); demonstrate FP **existence + value-motion** under both; **compute**
GU's ker-Gamma RS anti-screening **sign-invariance** (with the scalar-heavy refutation guard still firing
under the second regulator); **port** the EH `g*lambda*`/critical-exponent robustness (I2) and the
f(R)/R^2 relevance + 3+1 critical-surface robustness (I3); check all four regulator-invariants survive;
land **ROBUST (first-swing)** -> condition (i) upgrades conditional -> toward confirmed. Deterministic test
`tests/W85_second_regulator_reuter.py`, exit 0.

**Does NOT:** run the full combined `f(R)+Weyl^2 + ker-Gamma spin-3/2` **functional** second-regulator
computation (I2/I3 are ported; the ker-Gamma `b_RS` magnitude under a second regulator is uncomputed --
the NEEDS-FULL-COMPUTATION residual); prove asymptotic safety (still an unproven paradigm); touch
assumption (ii) of W83 (the tachyon-genuineness gate); or change `CANON.md`, `RESEARCH-STATUS.md`,
`claim-status`, verdicts, or public posture. H59/H61a remain **OPEN**.

## 7. Next valid swing

1. **The full combined second-regulator functional run** -- the actual `f(R)+Weyl^2 + ker-Gamma
   spin-3/2` FRG with the exponential regulator's threshold functions all the way through, to convert
   the ported I2/I3 into computed, and pin the ker-Gamma `b_RS` magnitude under the second regulator
   (removes the NEEDS-FULL-COMPUTATION residual and closes condition (i) unconditionally).
2. **A third regulator / shape-parameter sweep** (e.g. exponential with varying `s`, or a
   compactly-supported smooth cutoff) to map the `g*lambda*` band and the `f_0^2` critical exponent
   directly for GU's content.
3. **Assumption (ii)** (still open from W83): beyond-4th-order `|II|^2` invariants and whether the W79
   tachyon is a genuine IR inconsistency -- the *other* gate on the W83 verdict, untouched here.
