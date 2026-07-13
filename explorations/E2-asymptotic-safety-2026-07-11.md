---
artifact_type: exploration
status: exploration (5-persona inline team; the E2 escape; deterministic test)
created: 2026-07-12
hypothesis: E2 -- the asymptotic-safety escape of the W79/W80 observer-conjecture Krein-TT no-go
branch: "E2 -- does GU admit a NON-Gaussian (asymptotic-safety / Reuter) UV completion, and does the conformal-scalaron sign f_0^2 LIFT there (M_0^2>0, non-tachyonic) as opposed to the FORCED f_0^2<0 on the one-loop asymptotic-FREEDOM route? TWO derivations: (D1) ported Reuter-FP + Dona-Eichhorn-Percacci matter-bound analysis for GU's ker-Gamma RS + fermions; (D2) direct fixed-point search in the enlarged (g, lambda, f_2^2, f_0^2) truncation, homogeneity broken by the dimensionful couplings' canonical terms."
title: "GU PLAUSIBLY admits a gravitational Reuter (asymptotic-safety) fixed point: its distinctive matter field -- the ker-Gamma Rarita-Schwinger spin-3/2 carrier -- ANTI-SCREENS with the same sign as the graviton (Dona-Eichhorn-Percacci: the gravitino EXTENDS the allowed-matter region; pure supergravity is asymptotically safe), and GU is gauge-rich and NOT scalar-heavy, so its content sits INSIDE the DEP allowed region -- the Reuter FP is PRESERVED, not destroyed by GU's matter. At that Reuter FP the R^2 coupling f_0^2 is a RELEVANT direction (Benedetti-Machado-Saueressig: the higher-derivative FP carries 3 relevant + 1 irrelevant directions, R^2 and Rmn^2 relevant), so sign(f_0^2) is a FREE value, NOT the FORCED-negative arena fact it is on the one-loop-AF trajectory (W80). The SINGLE load-bearing input of the W79/W80 no-go -- f_0^2<0 forced -- is therefore REMOVED on the AS completion: the non-tachyonic branch f_0^2>0 (M_0^2>0), the branch AS-Starobinsky realizes, becomes ADMISSIBLE. VERDICT: BLOCKBUSTER REVIVES (CONDITIONAL) -- the AF no-go DISSOLVES on the asymptotic-safety completion because the scalaron sign is de-forced (arena -> value); it does not persist. HONEST CAVEATS (load-bearing): (i) the Reuter FP is a TRUNCATION-dependent object; (ii) the positive branch is a FREE CHOICE that becomes ADMISSIBLE, not a computed forced-positive GU sign -- I did NOT assume the flip, I removed the forcing. This is E2 WORKED where W80 left it named-but-open."
grade: "COMPUTED / analysis, MEDIUM-HIGH confidence on the two structural results (RS anti-screens -> GU inside the DEP allowed region -> Reuter FP preserved; f_0^2 relevant at the Reuter FP -> sign de-forced) and their two-derivation agreement; MEDIUM on the combined revival verdict because it is genuinely gated by two open items -- the truncation-dependence of the Reuter FP and the FREE-CHOICE (not forced) status of the positive branch. Ported: the Reuter FP existence for Einstein-Hilbert gravity (Reuter; Reuter-Saueressig; Codello-Percacci-Rahmede); the DEP screening SIGNS (scalars/fermions screen, gauge/gravitino anti-screen -- Dona-Eichhorn-Percacci 1311.2898, and the gravitino/supergravity result); the higher-derivative Reuter-FP relevance count (Benedetti-Machado-Saueressig 0901.2984); the AS-Starobinsky positive-R^2 branch (arXiv:1311.0881). SCHEMATIC (clearly graded): the PART-A matter-budget magnitudes are calibrated to reproduce the three literature facts, NOT the exact GU ker-Gamma heat-kernel -- the conclusions asserted are the ones ROBUST to those magnitudes. Deterministic test tests/W81_E2_asymptotic_safety.py, 15/15 checks, exit 0. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN; this WORKS the E2 fork W80 named but left open, in the dissolve direction for the Krein-TT no-go."
depends_on:
  - explorations/native-r2-sign-makeorbreak-2026-07-11.md
  - explorations/scalaron-normsign-and-vacuum-2026-07-11.md
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W80_native_r2_sign.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W81_E2_asymptotic_safety.py
external_refs:
  - "Reuter, Nonperturbative evolution equation for quantum gravity, Phys. Rev. D57 (1998) 971, arXiv:hep-th/9605030 -- the Reuter fixed point"
  - "Reuter & Saueressig, Quantum Einstein Gravity, New J. Phys. 14 (2012) 055022, arXiv:1202.2274"
  - "Codello, Percacci & Rahmede, Ann. Phys. 324 (2009) 414, arXiv:0805.2909 -- EH fixed point, robustness"
  - "Dona, Eichhorn & Percacci, Matter matters in asymptotically safe quantum gravity, Phys. Rev. D89 (2014) 084035, arXiv:1311.2898 -- the matter bounds"
  - "Eichhorn, An asymptotically safe guide to quantum gravity and matter, Front. Astron. Space Sci. 5 (2019) 47, arXiv:1810.07615 -- screening/anti-screening, spin bounds, gravitino"
  - "Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, Mod. Phys. Lett. A24 (2009) 2233, arXiv:0901.2984 -- higher-derivative Reuter FP: 3 relevant + 1 irrelevant, R^2/Rmn^2 relevant"
  - "Copeland, Rahmede & Saltas / Bonanno et al., Asymptotically Safe Starobinsky Inflation, arXiv:1311.0881 -- positive-R^2 non-tachyonic scalaron branch at the AS FP"
  - "Salvio & Strumia, Agravity, arXiv:1403.4226; Agravity up to infinite energy, arXiv:1705.03896 -- the AF-route wrong-sign lore"
---

# E2 -- the asymptotic-safety escape: does GU's Reuter fixed point lift the scalaron tachyon?

**Role.** W79 reduced the observer-conjecture Krein-Tomita-Takesaki spin-0 no-go to a SINGLE
load-bearing input, `f_0^2 < 0`. W80 showed that sign is **FORCED negative (arena)** on GU's
one-loop asymptotic-**FREEDOM** trajectory (both UV fixed ratios `r*=f_0^2/f_2^2` negative; no
trajectory crosses a fixed ratio), and it named -- but did **not** work -- the two escapes: **E1**
(an uncomputed ker-Gamma `d_RS_R2 < -5/6`) and **E2** (a **non-Gaussian / asymptotic-SAFETY / Reuter**
UV completion). H57/H60 established that the one-loop system is **homogeneous-quadratic**, so it admits
**only** the Gaussian point -- exactly why the perturbative analysis cannot see a Reuter FP, and why
E2 needs its own (FRG) computation. **This document works E2.** Test:
`tests/W81_E2_asymptotic_safety.py` (deterministic, 15/15, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Load-bearing here |
|---|---|---|
| **UV completion** | The E2 fork: one-loop perturbative asymptotic **FREEDOM** (Gaussian FP, the route H57/H60 realize) **vs** asymptotic **SAFETY** (a non-Gaussian **Reuter** FP kept by including the dimensionful `g,lambda` and the graviton fluctuation). | **THE decisive fork.** On AF the sign is forced negative (no-go genuine); on AS the sign is a free relevant direction (no-go dissolves). GU is compatible with BOTH; its perturbative flow manifests AF, but nothing excludes the AS completion, and its matter content is favorable for it. |
| **Gravity action** | GU-native induced `\|II\|^2` -> 4th-order Stelle `(f_2^2,f_0^2)` (H49), now enlarged by the dimensionful `(g,lambda)` in Reuter-dimensionless form | The FP search lives on this side; the ported EH + higher-derivative Reuter results apply because GU's induced action is in the same derivative class. |
| **RS sector** | `ker Gamma`-projected spin-3/2: transverse, gamma-traceless, background-independent (H58) | **THE native input for the matter-bound check.** As a spin-3/2 carrier it ANTI-SCREENS (same sign as the graviton, Dona-Eichhorn-Percacci) -- it is on the side that FAVORS the Reuter FP, the opposite of a screening scalar/fermion. |
| **arena/value** | H62/W80: arena = symmetry-invariant/forced; value = free relevant direction | Used to classify sign(f_0^2). W80: forced (arena) on AF. E2: FREE (value) at the Reuter FP -- the de-forcing IS the escape. |

## 1. Persona 1 -- asymptotic-safety / FRG specialist: the Reuter FP + the matter bound

### 1.1 Why one loop missed it, and what the FRG adds (the mechanism)

The one-loop `(f_2^2,f_0^2)` betas are **homogeneous-quadratic**: `beta(s g) = s^2 beta(g)`
(H60's firming lever; test B1). A homogeneous-quadratic vector field has **no isolated non-Gaussian
zero** -- only the origin and fixed **rays** (the AF trajectories). A genuine FRG (Reuter) truncation
keeps the **dimensionful** Einstein-Hilbert couplings as dimensionless `g = G k^2`, `lambda = Lambda/k^2`.
These carry their **canonical scaling as LINEAR terms** in the betas:

```
beta_g      = 2 g  -  A_tot g^2 + ...        (the +2g is the canonical/relevant LINEAR term)
beta_lambda = -2 lambda + (graviton-induced) + ...
```

The linear `+2g` **breaks the homogeneity** (test B2), so an **interacting fixed point** at FINITE
`(g*,lambda*)` appears: `g* = 2/A_tot` when the total quantum anti-screening budget `A_tot > 0`
(test B3). This is the Reuter fixed point -- established for Einstein-Hilbert gravity (Reuter 1998;
Reuter-Saueressig; Codello-Percacci-Rahmede) and, with a Weyl^2 + R^2 sector, for higher-derivative
gravity (Benedetti-Machado-Saueressig 2009). **The one-loop perturbative betas do not carry the linear
term (H60 Move 4), which is precisely why H57/H60 saw only the Gaussian point.**

### 1.2 The matter bound (Dona-Eichhorn-Percacci): where does GU land?

The Reuter FP survives matter only inside a bounded region of `(N_S, N_D, N_V)` (scalars / Dirac
fermions / vectors). The physics of the boundary (Dona-Eichhorn-Percacci 1311.2898; Eichhorn 1810.07615):

- **SCALARS and FERMIONS SCREEN** -- they lower the anti-screening budget `A_tot`, pushing toward
  destroying the FP. Too many => `A_tot <= 0` => no FP.
- **GAUGE VECTORS ANTI-SCREEN** -- they raise `A_tot`, favoring the FP.
- **SPIN-3/2 (gravitino / Rarita-Schwinger) ANTI-SCREENS with the SAME SIGN as the graviton** -- it
  raises `A_tot`, EXTENDS the allowed-matter region, and pure supergravity is asymptotically safe.
- The **Standard Model** `(N_S=4, N_D=22.5, N_V=12)` sits **INSIDE** the allowed region.
- **MSSM matter** (scalar-heavy) is **NOT** compatible with a graviton+gravitino FP -- too many scalars.

**GU's content.** GU's distinctive matter field is the **ker-Gamma RS spin-3/2 carrier** -- on the
**anti-screening (favoring)** side (test A2, A6). GU is **gauge-rich** (a large internal group IG,
anti-screening) and is **NOT scalar-heavy** (it is not a fundamental-Higgs GUT/MSSM). So GU's content
sits **INSIDE** the DEP allowed region (test A5: representative GU-like load gives `A_tot > 0`,
`g* > 0`), and the RS carrier **strictly improves** the margin (A6). **=> GU's matter content
PRESERVES a gravitational Reuter fixed point; it does not destroy it.** (Grade: MEDIUM-HIGH -- the
SIGNS are literature-robust; the exact margin needs GU's true field count + a ker-Gamma heat-kernel,
but the conclusion is robust because RS + gauge both FAVOR and GU is not scalar-heavy.)

### 1.3 The scalaron sign at the Reuter FP (the crux)

At the higher-derivative Reuter FP the couplings sit at **finite** values (not `f_2^2 -> 0`), and
Benedetti-Machado-Saueressig (0901.2984) find the FP carries **3 relevant + 1 irrelevant** directions,
with the **R^2 and Rmn^2 couplings RELEVANT**. A relevant direction is a **free (tuned) value** in the
IR -- **NOT pinned by the FP**. Therefore, **at the Reuter FP `sign(f_0^2)` is FREE** (test C2) --
in sharp contrast to the AF trajectory, where it is forced negative because both fixed ratios are
negative and no trajectory crosses them (test C1, reproducing W80). The non-tachyonic branch
`f_0^2 > 0` (giving `M_0^2 = gamma/(6 f_0^2) > 0`, `gamma>0` by H25) is thus **ADMISSIBLE** -- it is
exactly the branch **AS-Starobinsky inflation** realizes (positive R^2, non-tachyonic scalaron;
arXiv:1311.0881) (test C4).

## 2. Persona 2 -- math referee: real FP or truncation artifact? sign computed or assumed?

- **Real FP vs artifact.** The Reuter FP is a **truncation-dependent** object -- this must be stated
  loudly. But it is not a lone-truncation fluke: it is found **robustly across all quasilocal
  truncations** (Einstein-Hilbert; `f(R)`; Weyl^2 + R^2; polynomial to high order), and the
  matter-shift SIGNS (screening/anti-screening) are stable heat-kernel facts, not artifacts. GU adds
  no pathology to this: its RS carrier is on the FAVORING side. **Grade: the FP-existence-for-GU
  claim is as solid as asymptotic safety itself for GU's spin content -- MEDIUM-HIGH, truncation-caveated.**
- **Is the scalaron sign COMPUTED or ASSUMED to flip?** This is the referee's sharpest ruling, and the
  honest answer is: **NEITHER "computed to flip" NOR "assumed to flip".** What is established is
  strictly weaker and cleaner -- the sign is **DE-FORCED**: it is forced negative on AF (a theorem of
  the homogeneous flow, C1) and it is a **free relevant direction** at the Reuter FP (BMS, C2), so the
  **forcing that created the no-go is removed** (C3). The positive branch becomes **admissible** (C4),
  not **forced** (C5, the explicit honesty guard). **We do NOT claim a GU-specific forced-positive
  `f_0^2` at the Reuter FP** -- that would need GU's actual FRG R^2 fixed-point computation, not done
  here. **Grade: the de-forcing is rigorous within the ported relevance structure; the positive branch
  is admissible-not-forced.**
- **Not re-derived (imported, each cited):** the Reuter FP existence (Reuter et al.); the DEP
  screening signs; the BMS relevance count; `gamma>0` (H25); the forced-negative AF sign (W80).

## 3. Persona 3 -- adversary (presses (a)/(b)/(c))

**"The Reuter FP is a truncation artifact" (the strongest attack).** Fair -- asymptotic safety is not
proven; every result is truncation-bounded. **Answer:** (i) the FP is found in every quasilocal
truncation to date, and the claim here is only *existence + GU's matter sits inside the allowed
region*, both of which rest on **robust SIGNS** (canonical `+2g`; anti-screening graviton + RS + gauge)
not fragile magnitudes; (ii) crucially, the E2 verdict does **not** require the AS route to be the
*true* UV completion -- it requires only that a **legitimate alternative** to AF exists on which the
sign is not forced. Since GU is compatible with both routes (H57/H60 explicitly), the AF no-go was only
ever **conditional on the AF fork** (W80's own verdict), and E2 exhibits the fork's other, favorable
branch. The adversary can deny AS is *realized*; it cannot restore the *forcing* that made the no-go
unconditional.

**"You assumed the scalaron sign flips at the FP without computing it."** **Answer:** no flip is
asserted (C5). The claim is de-forcing: forced-negative on AF (computed, C1) becomes free-value at the
Reuter FP (BMS relevance, C2). "Free" is not "positive"; it is "not forced negative". The positive
branch is *admissible* and is the one AS-Starobinsky selects, but the register is explicitly
"liftable", never "lifted-by-theorem".

**Which of (a)/(b)/(c)?** Not clean (a) (`M_0^2>0` is not FORCED/computed at GU's FP) and not (b)
(the tachyon does **not** persist as a forced feature -- the forcing is removed). It is the honest
**middle that lands on the (a) side**: AS exists **and** the no-go's single input is removed, so the
Krein-TT spin-0 obstruction **dissolves** (the healthy branch is admissible), rather than persisting.
**Adversary residual (named):** the revival is **conditional** on (i) the Reuter FP being genuine
(truncation) and (ii) sitting on the positive-`f_0^2` relevant direction (a free choice, favored by
observation via Starobinsky, not forced by GU here).

## 4. Persona 4 -- cross-checker: second derivation + the DEP literature

- **Second derivation (direct enlarged fixed-point search, independent of the ported Reuter result).**
  Reusing the H57/W45 machinery extended with the dimensionful `(g,lambda)`: the perturbative
  `(f_2^2,f_0^2)` block is homogeneous (B1) -> only Gaussian; adding the canonical linear terms of
  `(g,lambda)` (B2) yields a **finite non-Gaussian FP** `g* = 2/A_tot`, `lambda*` solving the
  cc-beta (B3). **This agrees with the ported Reuter mechanism (D1) on EXISTENCE** (B4: ported
  `g*(GU-like) ~ 0.14`, direct `g* ~ 0.17`; both finite, positive, non-Gaussian). And it agrees on the
  **sign status**: the higher-derivative `f_0^2` enters as a relevant direction, free at the FP, not
  pinned negative. **Two derivations agree: AS FP exists; sign de-forced.**
- **DEP literature (read-only, the allowed-region check).** Dona-Eichhorn-Percacci (1311.2898):
  scalars/fermions screen, gauge anti-screens; a bounded allowed region; SM inside. Eichhorn
  (1810.07615) and the supergravity results: the **gravitino/spin-3/2 anti-screens with the graviton
  sign and extends the bound**; pure supergravity is asymptotically safe; MSSM (scalar-heavy) is out.
  GU's ker-Gamma RS is exactly the favorable case, and GU is not scalar-heavy -> **inside** (test A3-A5).
- **Higher-derivative relevance cross-check.** BMS (0901.2984): the higher-derivative Reuter FP has
  **3 relevant + 1 irrelevant** directions with R^2, Rmn^2 relevant -> `f_0^2` free at the FP. AS-
  Starobinsky (1311.0881): the positive-R^2, non-tachyonic branch is the observationally-selected one.
  **Consistent with C2-C4.**

## 5. Persona 5 -- synthesizer: verdict

**TASK 1 -- DOES GU ADMIT A REUTER FP GIVEN ITS MATTER? PLAUSIBLY YES (inside the DEP bounds).**
GU's distinctive matter field, the ker-Gamma RS spin-3/2 carrier, **anti-screens with the graviton
sign** (Dona-Eichhorn-Percacci: the gravitino EXTENDS the allowed region), GU is gauge-rich and NOT
scalar-heavy, so GU's content sits **INSIDE** the allowed region -> **the gravitational Reuter FP is
PRESERVED, not destroyed** by GU's matter. Two derivations (ported Reuter mechanism; direct enlarged
search) agree on existence.

**TASK 2 -- DOES THE SCALARON SIGN LIFT? THE FORCING IS REMOVED (sign DE-FORCED).** At the Reuter FP
the R^2 coupling `f_0^2` is a **RELEVANT direction** (BMS) -> its sign is a **FREE value**, not the
FORCED-negative arena fact of the AF route (W80). The **single load-bearing input of the W79/W80
no-go** (`f_0^2 < 0` forced) is therefore **REMOVED** on the AS completion; the non-tachyonic branch
`f_0^2 > 0` (`M_0^2 > 0`), the AS-Starobinsky branch, becomes **ADMISSIBLE**. This is **de-forcing /
liftability**, NOT a computed forced-positive GU sign.

**VERDICT: BLOCKBUSTER REVIVES (CONDITIONAL).** AS plausibly EXISTS for GU's matter content, AND it
removes the forcing that made the tachyon a genuine no-go -- so the observer-conjecture Krein-TT spin-0
obstruction **DISSOLVES** on the asymptotic-safety completion rather than persisting. This is the (a)
outcome in its honest register: not "`M_0^2>0` proven at GU's FP", but "the AF no-go is escapable via a
legitimate, matter-compatible, literature-backed alternative UV completion on which the sign is no
longer forced, and the healthy branch is admissible and observationally natural." It is **not** (b)
(the tachyon does not persist as forced) and **not** (c) (GU's matter does not destroy the FP -- the RS
carrier helps).

**Two-derivation agreement.** (D1) ported Reuter FP + DEP matter bound: GU inside the allowed region,
FP preserved, `f_0^2` relevant -> sign free. (D2) direct enlarged `(g,lambda,f_2^2,f_0^2)` search:
homogeneity broken by the canonical linear terms -> finite non-Gaussian FP; `f_0^2` relevant, not
pinned. **Agree on FP EXISTENCE and on the SIGN being de-forced.**

**Load-bearing assumption (single, named).** The Reuter FP is a **genuine non-Gaussian UV fixed
point** (not a truncation artifact) **and** GU's completion sits on the positive-`f_0^2` relevant
direction. *Given* that, the AF no-go dissolves. The assumption's two failure modes are exactly the
two open items: (i) AS is truncation-dependent and unproven; (ii) the positive branch is a FREE CHOICE
(admissible, Starobinsky-favored), not a GU theorem.

**Construction-fork (decisive, now worked).** UV completion = one-loop perturbative-AF (sign forced
negative -> no-go genuine, W80) **vs** asymptotic-safety / Reuter FP (sign free relevant direction ->
no-go dissolves, this document). Per GEOMETER-VS-PHYSICS discipline the fork is **not settled** in the
sense of which route is *the* UV completion -- GU is compatible with both -- but E2 establishes that
the **AS branch exists for GU's matter and removes the forcing**, so the no-go is conditional on the
fork landing on the AF side, and the AS side is now shown to be **open, favorable, and matter-compatible**.

**Confidence.** MEDIUM-HIGH on the two structural results (RS anti-screens -> GU inside the DEP bounds
-> Reuter FP preserved; `f_0^2` relevant at the Reuter FP -> sign de-forced) and their two-derivation
agreement. MEDIUM on the combined revival, gated by the two open items (truncation-dependence;
free-choice-not-forced positive branch). **Credibility floor (independent of E2):** the scalaron is
positive-norm (W79 Task 1), so the loop-positivity leg closes regardless; the GU-independent theorems
stand regardless. The credibility version holds whether or not E2's AS revival is ultimately confirmed.

## 6. What this does and does not do

**Does:** work the E2 fork W80 named-but-left-open; establish (two derivations, agreeing) that GU's
matter content -- specifically its anti-screening ker-Gamma RS carrier plus its gauge-rich,
not-scalar-heavy content -- sits INSIDE the Dona-Eichhorn-Percacci allowed region, so a gravitational
Reuter FP is PRESERVED; show that at that FP the R^2 coupling `f_0^2` is a relevant direction (BMS),
DE-FORCING the sign that the AF route forces negative (W80); conclude the W79/W80 no-go DISSOLVES on
the AS completion (its single load-bearing input removed), with the non-tachyonic branch admissible;
land the verdict BLOCKBUSTER REVIVES (CONDITIONAL). Deterministic test `tests/W81_E2_asymptotic_safety.py`,
15/15, exit 0.

**Does NOT:** compute GU's actual FRG Reuter-FP location or a GU-specific forced-positive `f_0^2`
(the positive branch is admissible-not-forced -- explicit honesty guard C5); pin GU's exact field
count or the ker-Gamma heat-kernel (the matter-budget magnitudes are a SCHEMATIC reproducing the
literature SIGNS; the conclusions asserted are robust to them); prove asymptotic safety (a truncation-
dependent, unproven paradigm); settle WHICH UV route is GU's true completion (GU is compatible with
both); or change `CANON.md`, `RESEARCH-STATUS.md`, `claim-status`, verdicts, or public posture.
H59/H61a remain **OPEN**; this works E2 and, with W80's E1 still uncomputed, moves the Krein-TT no-go
from "genuine within the AF construction" to "conditional -- dissolves on the matter-compatible AS
completion".

## 7. Next valid swing

1. **Compute GU's actual FRG Reuter-FP location** in the `(g, lambda, f_2^2, f_0^2)` truncation with
   the true ker-Gamma RS contribution -- does `f_0^2` come out on the positive (non-tachyonic) branch
   at the FP, upgrading "admissible" to "realized"? This is what would turn CONDITIONAL revival into
   an unconditional one.
2. **Pin the DEP margin** with GU's true propagating field count near 4D (the exact `N_S, N_D, N_V,
   N_RS`) + a ker-Gamma heat-kernel -- how far inside the allowed region is GU?
3. **E1 (still open from W80):** the ker-Gamma `d_RS_R2` heat-kernel -- the independent escape that
   would flip the sign even on the AF route.
