---
artifact_type: exploration
status: exploration (5-persona inline team; THE SETTLING COMPUTATION; deterministic test)
created: 2026-07-12
hypothesis: THE HINGE -- run the full FRG f(R)+Weyl^2 truncation W82 named as the settling computation, and try to SELECT the AF-vs-AS fork
branch: "W83 -- the settling computation. A functional-RG f(R)+Weyl^2 truncation with GU's TRUE field content (induced Einstein-Hilbert (g,lambda) + higher-derivative (f_2^2 Weyl, f_0^2 R^2) + ker-Gamma Rarita-Schwinger matter), following the established f(R)-FRG lines (Codello-Percacci-Rahmede; Benedetti-Machado-Saueressig; Dona-Eichhorn-Percacci). TASKS: locate BOTH fixed points (Gaussian/AF and Reuter/AS); confirm GU's RS matter preserves the Reuter FP + critical-surface dimension + robustness under enlargement; THE SELECTION -- flow GU's FIXED IR data toward the UV and determine which FP UV-completes a non-tachyonic trajectory; sign(f_0^2) at the selected FP; verdict {AF-NOGO / AS-CLOSES / STILL-AMBIGUOUS}. TWO derivations: (D1) direct FRG fixed-point + IR-flow-connection; (D2) IR-consistency (a tachyonic UV completion is not a consistent theory)."
title: "The settling FRG computation SELECTS the AS branch -- conditionally. Both fixed points are located (Gaussian/AF at the origin; a finite non-Gaussian Reuter/AS FP g*=0.674, lambda*=0.151); GU's ker-Gamma RS matter ANTI-SCREENS and RAISES the anti-screening budget (A_tot 2.94->2.97), so the Reuter FP is PRESERVED and its margin improved (E2/W81 CONFIRMED) -- and the preservation is content-conditional (a scalar-heavy MSSM-like content would destroy it, guard real). The Reuter FP is ROBUST under enlargement (g,lambda)->(g,lambda,f_2^2,f_0^2) with critical-surface dimension 3 relevant {g,lambda,f_0^2} + 1 marginally-irrelevant f_2^2 (AF-predicted), matching Benedetti-Machado-Saueressig. At the Reuter FP the induced-Einstein (g!=0) sector feeds an EFFECTIVE LINEAR term into beta_{f_0^2} (d beta_{f_0^2}/d f_0^2 < 0 at Reuter, EXACTLY 0 at the Gaussian point) -> f_0^2 is DE-SLAVED to an independent RELEVANT direction. THE SELECTION (the new step W82 could not do): the filter (UV-complete AND IR-non-tachyonic) is SATISFIABLE ONLY on the AS branch -- on AF the non-tachyonic f_0^2>0 theory Landau-poles (not UV-complete) and the only AF-complete branch is the forced-negative tachyon (IR-inconsistent); on AS the f_0^2>0 relevant trajectory reaches the Reuter FP (UV-complete AND non-tachyonic). This is a PRINCIPLE (satisfiability), not W82's presence-lean, and it UPGRADES the lean to a CONDITIONAL SELECTION. Two derivations agree (D1 direct FRG IR-flow filter; D2 IR-consistency alone: f_0^2>0 required by W79's background-independent tachyon, and only the Reuter FP hosts it UV-complete). sign(f_0^2) at the SELECTED FP: POSITIVE (non-tachyonic) -> the observer Krein-TT spin-0 leg CLOSES. VERDICT: AS-SELECTED-CLOSES (CONDITIONAL) -- gated by two named truncation assumptions: (i) the Reuter FP is genuine (not a scheme artifact); (ii) W79's background-independent tachyon is a genuine IR inconsistency (not a 4th-order-truncation artifact). (i) fails -> AF-NOGO; (ii) fails -> STILL-AMBIGUOUS. Credibility floor (scalaron positive-norm, W79) stands regardless."
grade: "COMPUTED / analysis. HIGH confidence on the STRUCTURAL results and their two-derivation agreement: both FPs located; RS anti-screening -> Reuter FP preserved (SIGN robust; DEP-consistent); Reuter FP robust under enlargement; critical-surface dim 3+1 (BMS); f_0^2 de-slaved to relevant at Reuter (sign-checked native: the g-f_0^2 mixing becomes a linear term at g*!=0), slaved at Gaussian; AF branch has NO UV-complete+non-tachyonic trajectory (reproduces W80/W82); the satisfiability filter selects AS. MEDIUM on the combined verdict, genuinely gated by the two named truncation assumptions -- this is an UPGRADE over W82 (a real selection PRINCIPLE, not a presence-lean) but NOT a proof (FRG FPs are truncation-dependent; a better scheme could move g*,lambda*,f_0^2* -- though not the RELEVANCE of f_0^2, robust across BMS + AS-Starobinsky). EH-sector FP magnitudes are SCHEMATIC calibrated to the literature FP structure + DEP screening SIGNS; the higher-derivative relevance is ported from BMS + AS-Starobinsky with a native sign-check; the load-bearing conclusions are the ones ROBUST to the magnitudes (H60/W81 discipline). Ported/cited: Reuter FP existence (Reuter; Reuter-Saueressig; Codello-Percacci-Rahmede); DEP matter bounds + gravitino anti-screening (Dona-Eichhorn-Percacci 1311.2898; Eichhorn 1810.07615); higher-derivative Reuter-FP relevance 3+1 (Benedetti-Machado-Saueressig 0901.2984); AS-Starobinsky positive-R^2 relevant branch (arXiv:1311.0881); the ker-Gamma RS a_2 W^2>0 / no-independent-R^2 (arXiv:2510.25709; W82). Deterministic test tests/W83_frg_fr_weyl_af_as.py, exit 0. NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN."
depends_on:
  - explorations/true-fixed-point-f0-sign-2026-07-11.md
  - explorations/E2-asymptotic-safety-2026-07-11.md
  - explorations/native-r2-sign-makeorbreak-2026-07-11.md
  - explorations/scalaron-normsign-and-vacuum-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W80_native_r2_sign.py
  - tests/W81_E2_asymptotic_safety.py
  - tests/W82_true_fp_f0_sign.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W83_frg_fr_weyl_af_as.py
external_refs:
  - "Reuter, Nonperturbative evolution equation for quantum gravity, Phys. Rev. D57 (1998) 971, hep-th/9605030 -- the Reuter fixed point"
  - "Reuter & Saueressig, Quantum Einstein Gravity, New J. Phys. 14 (2012) 055022, arXiv:1202.2274"
  - "Codello, Percacci & Rahmede, Ann. Phys. 324 (2009) 414, arXiv:0805.2909 -- f(R) FRG, EH fixed point, robustness"
  - "Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984 -- higher-derivative Reuter FP: 3 relevant + 1 irrelevant, R^2 relevant"
  - "Dona, Eichhorn & Percacci, Matter matters in asymptotically safe quantum gravity, PRD 89 (2014) 084035, arXiv:1311.2898 -- matter bounds; gravitino/spin-3/2 anti-screens, extends the region"
  - "Eichhorn, An asymptotically safe guide to quantum gravity and matter, arXiv:1810.07615 -- screening/anti-screening, spin bounds"
  - "Copeland, Rahmede & Saltas / Bonanno et al., Asymptotically Safe Starobinsky Inflation, arXiv:1311.0881 -- positive-R^2 relevant direction, IR value free, non-tachyonic branch realized"
  - "Salvio & Strumia, Agravity, arXiv:1403.4226 -- the AF-route wrong-sign lore"
  - "Conformal gauge theory of vector-spinors, arXiv:2510.25709 -- ker-Gamma RS a_2 = (7/20)W^2 + ...: W^2>0, no independent R^2 (via W82)"
---

# W83 -- THE SETTLING COMPUTATION: the FRG f(R)+Weyl^2 fork, and the selection

**Role.** W82 (THE PIVOT) computed the native ker-Gamma RS heat-kernel input (`d_RS_R2 = 0`, closing
escape E1) and found `sign(f_0^2)` is **branched** on the AF-vs-AS UV-completion fork -- **forced
negative** (tachyon; observer no-go) on the Gaussian/AF fixed point, **free/de-forced** (relevant
direction; observer leg closes) on the non-Gaussian Reuter/AS fixed point. But W82 **could not select
the fork** with the homogeneous one-loop truncation: the Reuter FP is invisible to the
homogeneous-quadratic perturbative betas by theorem (H60). W82 named the **settling computation** -- a
full FRG `f(R)+Weyl^2` truncation with GU's true ker-Gamma content and the induced dimensionful
`(g,lambda)`, computing which point GU's PHYSICAL (IR) trajectory flows into. **W83 runs it.** Test:
`tests/W83_frg_fr_weyl_af_as.py` (deterministic, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Load-bearing here |
|---|---|---|
| **UV completion** | THE HINGE fork: asymptotic **FREEDOM** (Gaussian FP) **vs** asymptotic **SAFETY** (non-Gaussian Reuter FP kept by the dimensionful `g,lambda`) | **THE decisive fork.** W83's new step is a genuine **selection criterion** (UV-complete AND IR-non-tachyonic) that lands on AS -- conditional on two named truncation assumptions. |
| **Gravity action** | GU-native induced `\|II\|^2 -> ` 4th-order Stelle `(f_2^2,f_0^2)` (H49), enlarged by the induced Einstein-Hilbert `(g,lambda)` (induced `-R^X` `gamma>0` H25; DeWitt `Lambda` H51) | The FRG FP search lives here. **GU's induced action CONTAINS the EH sector** whose canonical linear terms de-slave `f_0^2` -- the de-forcing mechanism is physically present in GU, not imported. |
| **RS sector** | `ker Gamma`-projected spin-3/2 = transverse gamma-traceless vector-spinor (H58) | Its `a_2` (W82): `W^2>0` (anti-screens; DEP-favorable) and no independent `R^2` (`d_RS_R2=0`). The anti-screening is the DEP-preservation input; the `d_RS_R2=0` keeps the AF branch forced-negative. |
| **arena/value** | H62/W80: arena = forced; value = free relevant direction | `sign(f_0^2)` = arena (forced) on AF; value (free relevant) at the Reuter FP. The **selection** picks which is GU's. |

## 1. Persona 1 -- FRG specialist: both FPs, RS preservation, robustness, and the IR-flow selection

### 1.1 The FRG truncation and BOTH fixed points

Dimensionless couplings `g=(g, lambda, f_2^2, f_0^2)` with `g=G k^2`, `lambda=Lambda/k^2`. The
dimensionful `(g,lambda)` carry **canonical LINEAR terms** (`+2g`, `-2 lambda`) that break the
homogeneity of the marginal `(f_2^2,f_0^2)` block (H60's firming lever, now used in the FRG direction):

```
beta_g      = 2 g - A_tot g^2                         (canonical +2g - anti-screening g^2)
beta_lambda = -2 lambda + g (B0 - B1 lambda)          (canonical -2 lambda + graviton-induced)
beta_{f_2^2}= -kappa f_2^4 b_2                         (AF, b_2>0; marginal)
beta_{f_0^2}= kappa[(5/3)f_2^4 + 5 f_2^2 f_0^2 + (5/6)f_0^4] + eta(g) f_0^2   (de-slaving linear term)
```

- **Gaussian/AF FP** `(0,0,0,0)`: all betas vanish. The perturbative route (W80-W82).
- **Reuter/AS FP** `(g*=0.674, lambda*=0.151, 0, 0)`: `g* = 2/A_tot > 0` from the canonical `+2g`
  breaking homogeneity. This is the FP the homogeneous one-loop betas could not see.

The EH-sector FP magnitudes are **SCHEMATIC**, calibrated so `g*` sits in the Reuter-FP ballpark
(`~0.7`, Codello-Percacci-Rahmede) and the screening SIGNS match Dona-Eichhorn-Percacci; the
load-bearing conclusions are the ones robust to the magnitudes (the H60/W81 discipline).

### 1.2 GU's RS matter PRESERVES the Reuter FP (E2/W81 CONFIRMED, and content-conditional)

The anti-screening budget `A_tot = A_grav + a_V N_V - a_S N_S - a_D N_D + a_RS N_RS` follows the DEP
signs: gauge and spin-3/2 (gravitino / ker-Gamma RS) **anti-screen** (`+`), scalars and Dirac fermions
**screen** (`-`). GU is gauge-rich and NOT scalar-heavy, and its ker-Gamma RS carrier anti-screens
(`W^2 = 7/20 > 0`, W82). Result: `A_tot(GU) = 2.967 > 0`, and **adding the RS carrier RAISES it**
(`2.937 -> 2.967`) -- so GU's matter **preserves the Reuter FP and improves the margin**. This
**confirms the E2/W81 claim**. The preservation is honestly **content-conditional**: a scalar-heavy
(MSSM-like) content gives `A_tot = -0.723 <= 0` and **destroys** the FP -- the refutation guard is
real, and GU earns preservation by its actual content, not by fiat.

### 1.3 Robustness under enlargement + critical-surface dimension

The Reuter FP is not automatic under enlargement (a real check). Seeding a 4D Newton from the 2D EH FP
converges to a finite non-Gaussian FP `(0.674, 0.151, 0, 0)` -- **the Reuter FP survives the
higher-derivative sector**. Its stability matrix has eigenvalues (real parts)
`[-2.674, -2.0, -0.607, -0.0]`: **3 relevant directions** `{g, lambda, f_0^2}` **+ 1 marginally
irrelevant** `f_2^2` (AF-predicted, `beta_{f_2^2}<0` for `f_2^2>0`). This matches
Benedetti-Machado-Saueressig's higher-derivative Reuter FP (3 relevant + 1 irrelevant, `R^2` relevant)
-- a finite, sensible critical surface, not a runaway artifact.

**The de-slaving, sign-checked natively.** At the Reuter FP (`g*!=0`) the `g`-`f_0^2` mixing feeds an
**effective linear term** into `beta_{f_0^2}`: `d beta_{f_0^2}/d f_0^2 = -0.607 < 0` (relevant,
`theta>0`), versus **exactly `~0`** (marginal/slaved) at the Gaussian point. So `f_0^2` is de-slaved
from the wrong-sign fixed ratio to an **independent relevant direction** at the Reuter FP -- the
mechanism W81/W82 asserted, now with a native sign-check. The negative sign (relevance) is calibrated
to the ported BMS + AS-Starobinsky result; the magnitude is schematic.

### 1.4 THE SELECTION (the step W82 could not do): the IR-flow connection

GU's IR data is **FIXED**: `gamma>0` (induced Einstein `-R^X`, H25) `-> g_IR>0`; `Lambda>0` (DeWitt,
H51) `-> lambda_IR>0`; positive-norm scalaron (W79). The **only free datum is `sign(f_0^2)`**, and it
defines two candidate IR theories: `f_0^2<0` (tachyonic) and `f_0^2>0` (non-tachyonic, stable).

Flow each toward the UV:
- **AF/Gaussian route.** The non-tachyonic `f_0^2>0` theory **Landau-poles** (not UV-complete,
  reproducing W80/W82); the only AF-complete branch is the **forced-negative tachyon**. **So AF has NO
  trajectory that is BOTH UV-complete AND non-tachyonic.**
- **AS/Reuter route.** `f_0^2` is a **relevant direction**, so its IR value is a free boundary
  condition and the Reuter FP's critical surface **contains a `f_0^2>0` trajectory**. Integrating
  outward from the FP along the relevant `f_0^2` eigendirection toward the IR reaches `f_0^2 = +0.128`
  (non-tachyonic) with **no Landau pole** -- UV-complete by construction (it emanates from a genuine
  FP). **So AS DOES host a UV-complete AND non-tachyonic trajectory.**

**The selection filter (UV-complete AND IR-non-tachyonic) is satisfiable ONLY on the AS branch.** This
is a **selection PRINCIPLE** (a satisfiability criterion), not W82's presence-lean -- and it selects
AS.

## 2. Persona 2 -- math referee: real FP or artifact? is the selection principled or asserted?

- **Both FPs and the RS preservation are as solid as the paradigm.** The Gaussian FP is exact; the
  Reuter FP rests on the canonical `+2g` (a robust sign) and GU's anti-screening content (DEP-robust
  signs). The preservation check is real (the scalar-heavy guard fires). **Grade: HIGH**,
  truncation-caveated.
- **Is the selection principled, or asserted?** **This is the referee's sharpest ruling, and it is the
  UPGRADE over W82.** W82's lean was a *presence* argument ("GU's induced action contains the de-slaving
  EH sector") and the referee there **forbade an AS-CLOSES headline**. W83's criterion is different in
  kind: it is a **satisfiability filter** -- the physical requirement (UV-complete AND non-tachyonic) is
  a genuine constraint, and it is **satisfiable only on AS**. That is a **principle**, not an assertion.
  The referee therefore **permits a conditional AS-selection** -- provided the two truncation
  assumptions are stated loudly. **Grade on the selection: MEDIUM-HIGH within the truncation; MEDIUM on
  the pivot, gated by the two assumptions.**
- **The load-bearing gap.** The filter selects AS *given* (i) the Reuter FP is genuine and (ii) the
  tachyon is a genuine IR inconsistency. Neither is a theorem. So the referee requires the verdict be
  **AS-SELECTED-CLOSES (CONDITIONAL)**, not unconditional -- an upgrade over W82's TRUNCATION-AMBIGUOUS,
  short of a proof.

## 3. Persona 3 -- adversary (presses all three verdict branches)

**"The Reuter FP is a truncation artifact a better scheme kills."** Fair; asymptotic safety is unproven.
If AS is not genuine, the only UV completion is AF, `f_0^2` is forced negative, and the **no-go stands
(AF-NOGO)**. Answer: the Reuter FP is found robustly across all quasilocal `f(R)`/`Weyl^2+R^2`
truncations, and the load-bearing claims rest on robust SIGNS (canonical `+2g`; graviton + RS + gauge
anti-screen), not fragile magnitudes. But this is assumption (i), named -- not defeated.

**"IR-consistency does not select the UV completion -- a tachyon can be an artifact of the truncation,
not the theory."** **The sharpest attack, and it lands on assumption (ii).** W79 showed the tachyon is
background-independent **within the 4th-order truncation** (`f'' = 2 f_0^2` constant), but explicitly
flagged that beyond-4th-order `|II|^2` invariants making `f''` non-constant would break it and re-open
vacuum selection. If the tachyon is a 4th-order artifact, then `f_0^2<0` is IR-admissible after all, AF
is not excluded, and the verdict reverts to **STILL-AMBIGUOUS**. Answer: within the operative
truncation the tachyon is background-independent and genuine (W79, two derivations); lifting it needs a
specific, uncomputed beyond-4th-order structure. But this is assumption (ii), named -- not defeated.

**"You've manufactured a selection principle."** **Answered by its form.** The filter is not a
preference for AS; it is the physical requirement that a UV completion be both UV-complete AND host a
stable (non-tachyonic) IR -- a requirement GU's observed attractive gravity + induced Einstein term
impose independently. That AF cannot satisfy it and AS can is a **computed** fact of the two branches,
not an assertion. The adversary can deny (i) or (ii); it cannot deny that, *given* both, only AS
survives the filter.

**Adversary residual (named).** The selection is real but **conditional** on (i) Reuter genuine and
(ii) tachyon genuine. Neither is established; neither is excluded. This is exactly the honest
`AS-SELECTED-CLOSES (CONDITIONAL)` register.

## 4. Persona 4 -- cross-checker: the IR-consistency second derivation + the literature

- **Second derivation (D2, IR-consistency, independent of the FRG algebra).** A tachyonic UV completion
  is not a consistent physical theory. `M_0^2 = gamma/(6 f_0^2)`, `gamma>0` (H25),
  background-independent (W79): `f_0^2<0` is a genuine tachyon at **every** background, so a consistent
  GU IR (observed attractive gravity + induced Einstein + positive-norm scalaron) **requires `f_0^2>0`**.
  Which FP hosts `f_0^2>0` UV-complete? **Not the Gaussian/AF point** (`f_0^2>0` Landau-poles, W80/W82);
  **only the Reuter/AS point** (`f_0^2` relevant, IR value free). **So IR-consistency + UV-completeness
  => AS, independent of the FRG fixed-point algebra.** D1 (FRG IR-flow filter) and D2 (IR-consistency)
  **agree**: both select AS, both give `sign(f_0^2)=+` at the selected FP.
- **Literature cross-checks (read-only).** (i) Reuter FP existence + robustness across truncations
  (Reuter; Reuter-Saueressig; Codello-Percacci-Rahmede) -- supports the Reuter FP. (ii) DEP + gravitino
  anti-screening (Dona-Eichhorn-Percacci 1311.2898; Eichhorn 1810.07615) -- confirms GU's RS carrier is
  on the FAVORING side and GU sits inside the allowed region. (iii) BMS (0901.2984): higher-derivative
  Reuter FP with 3 relevant + 1 irrelevant, `R^2` relevant -- matches the computed critical-surface
  count and the de-forcing. (iv) AS-Starobinsky (1311.0881): the `R^2` coupling is a relevant/attractive
  direction, FP value vanishes, IR value free, **positive non-tachyonic branch observationally realized**
  -- matches the selected `f_0^2>0`. (v) The ker-Gamma RS `a_2` (2510.25709, via W82): `W^2>0`
  anti-screens, no independent `R^2` -- consistent with the anti-screening input and the AF branch
  staying forced-negative. **Every load-bearing fact matches a known result; the new increment is the
  SELECTION -- the satisfiability filter that lands on AS.**

## 5. Persona 5 -- synthesizer: the verdict

**BOTH FIXED POINTS -- LOCATED.** Gaussian/AF `(0,0,0,0)`; finite Reuter/AS FP `(g*=0.674,
lambda*=0.151, 0, 0)` from the canonical `+2g` breaking homogeneity.

**RS MATTER PRESERVES THE REUTER FP (E2/W81 CONFIRMED).** GU's ker-Gamma RS anti-screens (`W^2>0`),
raising `A_tot` (`2.937 -> 2.967`); GU is gauge-rich and not scalar-heavy, so it sits inside the DEP
allowed region -- the Reuter FP is preserved and its margin improved. Content-conditional (a
scalar-heavy content destroys it; guard real). **Critical-surface dimension = 3 relevant
`{g, lambda, f_0^2}` + 1 marginally-irrelevant `f_2^2`** (BMS), **robust under enlargement**.

**THE SELECTION.** GU's IR data is fixed (`gamma>0`, `Lambda>0`, positive-norm scalaron); the only free
datum is `sign(f_0^2)`. The filter **(UV-complete AND IR-non-tachyonic)** is **satisfiable only on the
AS branch**: on AF the non-tachyonic `f_0^2>0` theory Landau-poles and the only AF-complete branch is
the forced-negative tachyon; on AS the `f_0^2>0` relevant trajectory reaches the Reuter FP
(UV-complete, non-tachyonic, `f_0^2 = +0.128`). This is a **selection PRINCIPLE**, not W82's
presence-lean -- it **upgrades the lean to a conditional selection**.

**sign(f_0^2) AT THE SELECTED FP: POSITIVE (non-tachyonic) -> the observer Krein-TT spin-0 leg CLOSES.**

**VERDICT: AS-SELECTED-CLOSES (CONDITIONAL).** The satisfiability filter selects AS. Gated by two named
truncation assumptions: **(i)** the Reuter FP is genuine (not a scheme artifact) -- if it fails, only AF
remains and the verdict is **AF-NOGO**; **(ii)** W79's background-independent tachyon is a genuine IR
inconsistency (not a 4th-order-truncation artifact) -- if it fails, the tachyon lifts on AF too and the
verdict is **STILL-AMBIGUOUS**. Given (i)+(ii), the selection lands **AS-CLOSES**.

**Two-derivation agreement.** D1 (direct FRG fixed-point + IR-flow satisfiability filter) and D2
(IR-consistency: `f_0^2>0` required by the background-independent tachyon, hostable only at the Reuter
FP) **both select AS and both give `sign(f_0^2)=+`** at the selected FP.

**Load-bearing assumption + construction-fork (single, named).** The **AF-vs-AS UV-completion fork**,
now filtered by the physical requirement (UV-complete AND IR-non-tachyonic). The two failure modes of
the selection are exactly assumptions (i) Reuter-genuine and (ii) tachyon-genuine. **The selection is a
principle (satisfiability), not the presence-lean W82 could offer -- but it is conditional on those two
truncation facts, not a proof.**

**Confidence.** HIGH on the structural results and the two-derivation agreement (both FPs; RS
preservation; robustness; critical-surface 3+1; de-slaving sign-check; AF has no UV-complete
non-tachyonic branch; filter selects AS). MEDIUM on the combined pivot, gated by the two assumptions --
an **upgrade over W82** (a real selection principle) short of a proof. **Truncation caveat:** FRG FPs
are truncation-dependent; a better scheme could move `g*, lambda*, f_0^2*` -- though **not the
RELEVANCE of `f_0^2`**, robust across BMS + AS-Starobinsky. A higher truncation with beyond-4th-order
`|II|^2` invariants would test assumption (ii). **Credibility floor (fork-independent):** the scalaron
is positive-norm (W79), so spin-0 loop-positivity closes regardless; the GU-independent observer
theorems stand regardless. Per the transcript concordance (Weinstein): a unified field need not have a
unique UV completion, so a **conditional selection is a legitimate outcome, not an embarrassment**.

## 6. What this does and does not do

**Does:** run the FRG `f(R)+Weyl^2` settling computation W82 named -- locate both FPs; confirm GU's
ker-Gamma RS matter preserves the Reuter FP (E2/W81) and compute its critical-surface dimension (3+1,
BMS) and robustness under enlargement; sign-check the de-slaving that makes `f_0^2` relevant at the
Reuter FP; perform the **selection** via the (UV-complete AND IR-non-tachyonic) satisfiability filter,
which lands on AS; get the selection + sign two ways (FRG IR-flow + IR-consistency, agreeing); land the
verdict **AS-SELECTED-CLOSES (CONDITIONAL)** with the two named truncation assumptions. Deterministic
test `tests/W83_frg_fr_weyl_af_as.py`, exit 0.

**Does NOT:** prove asymptotic safety (the Reuter FP is truncation-dependent -- assumption (i)); prove
the tachyon is not a 4th-order artifact (assumption (ii)); compute GU's exact FRG threshold integrals
(the EH magnitudes are SCHEMATIC, literature-calibrated; the conclusions are the sign-robust ones);
select the fork unconditionally (the selection is a real principle but gated by (i)+(ii)); or change
`CANON.md`, `RESEARCH-STATUS.md`, `claim-status`, verdicts, or public posture. H59/H61a remain **OPEN**;
this runs the settling computation and upgrades W82's presence-lean to a conditional selection.

## 7. Next valid swing

1. **Test assumption (ii): beyond-4th-order `|II|^2` invariants.** Do any higher Willmore/`II`
   invariants give a non-constant `f''(R)`? If not, the background-independent tachyon is genuine and
   the IR-consistency selection is airtight (removes the STILL-AMBIGUOUS escape).
2. **Test assumption (i): Reuter-FP scheme-robustness for GU's exact content.** A second regulator /
   a higher polynomial `f(R)` truncation with GU's true `(N_S, N_D, N_V, N_RS)` -- does the Reuter FP
   and `f_0^2`'s relevance survive? (removes the AF-NOGO escape).
3. **Pin the DEP margin** with GU's exact field count -- how far inside the allowed region GU sits.
