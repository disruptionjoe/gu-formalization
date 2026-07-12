---
title: "Path4 branch A -- the EOS x strong-gravity correlation (thread C3): is there a FORCED, family-invariant, discriminating correlation between the dark-energy EOS w(z) and the strong-field gravity deviation, because both flow from the one shared theta (the II-class second fundamental form)? VERDICT: NO forced numerical correlation. The two observables depend on DISJOINT residual parameters (EOS shape <- root eigenvalue lambda_N1 + amplitude f0; strong-field Yukawa <- mu_DW + m2_eff); the residual->observable map is BLOCK-DIAGONAL, so no scale cancels between the sectors and the joint image is a rectangle, not a locus. The one genuine scale-cancelling lock is DENSITY x Yukawa (H50/H51), not EOS x Yukawa, and it is conditional on the H36 postulate and reproduced by generic degravitation. What survives is a QUALITATIVE, family-invariant, discriminating CO-PRESENCE of both modes from one |II|^2 action -- not a quantitative correlation."
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 61
grade: "COMPUTED (deterministic, exit 0, 16/16, nothing fit): the DE EOS's exact mu_DW-independence (the KG coefficient M^2/H^2 = lambda_N1 carries no mu_DW) and the Yukawa's exact lambda_N1/f0-independence (symbolic), hence the block-diagonal residual->observable map (Part 3); the mu_DW cancellation in the DENSITY-lock lambda_Y = hbar_c*c_L^{1/4}/(sqrt(m2_eff)*rho_Lambda^{1/4}) (symbolic) and its ~22% prefactor band across the beta/alpha-bounded m2_eff in [5/6,5/4]; the two-point (w0,wa) KG integration reproducing dynamical, root-eigenvalue-dependent EOS. ARGUED (structural/evidence tier): that the DE theta is a curvature-coupled LIGHT mode (M^2 ~ H0^2) not a hard-mass mu_DW mode (the load-bearing assumption, = the wave20/H43 construction); that generic degravitation reproduces the density-lock (Q-disc FAIL for the scale-lock); that the surviving CO-PRESENCE is a genuine discriminator but only qualitative. Reconstruction-tier, internal. No canon promotion; no verdict/claim-status change; no external action."
depends_on:
  - tests/W61_path4_A_eos_gravity.py
  - explorations/wave20/H43-de-shape-falsifier-2026-07-11.md
  - explorations/wave28/H49-bach-weyl-sector-2026-07-11.md
  - explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md
  - explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md
  - explorations/wave35/source-action-carve-2026-07-11.md
scripts:
  - tests/W61_path4_A_eos_gravity.py
---

# Path4 branch A -- the EOS x strong-gravity correlation (thread C3)

Test: `tests/W61_path4_A_eos_gravity.py` (deterministic, no randomness, exit 0, 16/16 PASS).

**The candidate.** The source action of this framework is not unique -- it is a shape-dim-1
FAMILY plus two free scales (the residual gravity ratio `beta/alpha`; the scales `mu_DW`,
`alpha`) (wave35). Instead of building a member (= choosing a model) we hunt a FORCED
FAMILY-INVARIANT. Candidate C3: the dark-energy EOS `w(z)` and the strong-field gravity
deviation (the massive spin-2 / Bach-Yukawa handle) BOTH flow from the SAME shared object
`theta` = the II-class second fundamental form. The hope: tying two observables to ONE object
makes the free scales CANCEL, yielding a family-invariant, discriminating correlation locus in
`(w(z), strong-field-deviation)` space -- a choice-independent prediction (the Weyl precedent).

**Construction used (fork rule, `GEOMETER-VS-PHYSICS-OBJECTS.md`).**
- **Gravity functional = the program-native induced `|II|^2`** (Gauss `|II|^2 = |H|^2 - R^X`),
  NOT a free `R^2/Weyl^2` Lagrangian. Its TT second variation is the Stelle operator
  `box(box + m2^2)` (wave28 H49): a massless graviton + a massive spin-2 of mass
  `m2 = sqrt(m2_eff) mu_DW`, giving a Yukawa of range `lambda_Y = hbar_c/(sqrt(m2_eff) mu_DW)`,
  strength `alpha_Y = 1/3` (vDVZ, H10, fixed).
- **theta (DE sector) = the program-native fiber / normal mode of the same embedding**
  `X^4 -> Y^14` (canon `theta-field-flrw-dark-energy-eos`). Its cosmological dynamics is a
  Klein-Gordon field whose EFFECTIVE mass on FLRW is `M^2 = lambda_{N,1}` -- a root-system
  normal-Laplacian eigenvalue (a PURE NUMBER, `{3,7,8,...}`) in units of `H^2`. This is the
  wave20/H43 construction: a curvature-coupled LIGHT mode, not a hard `mu_DW`-mass mode.
- **`mu_DW` = the DeWitt/gimmel scale** (ratio-only, H24): overall scale structurally free.

The five-persona team (cosmology/gravity, referee, adversary, cross-checker, synthesizer) was
run inline in one context. Their combined result follows.

---

## 1. The two sector-dependences (cosmology/gravity specialist)

### DE sector: `w(z) = w(lambda_{N,1}, f0)`, exactly `mu_DW`-independent [COMPUTED]

The theta EOS (wave20/H43) is a constant DeWitt-Lambda (`w=-1`) plus a KG field of mass `M^2`
integrated on an LCDM background:

```
B'' + (3 + H'/H) B' + (M^2/H^2) B = 0 ,   w_DE = (-1 + f wB)/(1+f) ,   f = f0 rhoB(z)/rhoB(0)
```

`M^2 = lambda_{N,1}` in `H0^2` units. The **only** scale-carrying coefficient is `M^2/H^2 =
lambda_{N,1}`, a pure root eigenvalue. **`mu_DW` does not appear in the KG equation.** So the
EOS SHAPE `(w0, wa)` is set by `(lambda_{N,1}, f0)` and is EXACTLY independent of `mu_DW`,
`m2_eff`, and `beta/alpha`. The test reproduces dynamical, eigenvalue-dependent EOS points
(`M2=8, f0=0.125 -> (w0,wa) ~ (-0.84, +0.05)`; `M2=3, f0=0.40 -> (-0.86, -0.16)`), the H43
ballpark.

### Gravity sector: deviation `= (lambda_Y, 1/3)`, exactly EOS-blind [COMPUTED]

`lambda_Y = hbar_c/(sqrt(m2_eff) mu_DW)`, `alpha_Y = 1/3`. Depends on `mu_DW` (free scale) and
`m2_eff in [5/6,5/4]` (the `beta/alpha`-bounded residual). **Neither `lambda_{N,1}` nor `f0`
appears.** The strength `alpha_Y = 1/3` is forced and scale-free -- but it is a
gravity-sector-ALONE fact, not a correlation with the DE sector.

---

## 2. The correlation test (referee + cross-checker)

**The residual -> observable map is BLOCK-DIAGONAL:**

```
(lambda_{N,1}, f0)  ->  (w0, wa)      [DE block]        d(w0,wa)/d(mu_DW)      = 0  (exact)
(mu_DW, m2_eff)     ->  (lambda_Y)    [gravity block]   d(lambda_Y)/d(lam_N1,f0) = 0  (exact)
```

No residual parameter is shared between the sectors, and **no scale cancels between them.**
Consequences, both COMPUTED:
- At FIXED EOS `(M2, f0)`, sweeping `mu_DW` by 10x sweeps `lambda_Y` by 10x -- the strong-field
  observable is UNCONSTRAINED by the EOS.
- At FIXED Yukawa `(mu_DW, m2_eff)`, sweeping `lambda_{N,1}` moves `(w0, wa)` -- the DE
  observable is UNCONSTRAINED by the strong field.

**The joint image `(w0, wa, lambda_Y)` fills a RECTANGLE (two free axes), not a 1-D locus.**
There is NO forced correlation between the EOS shape and the strong-field deviation. **Q-forced
FAILS for the literal C3 candidate.**

**Cross-check (independent limit).** Take `mu_DW -> 0` (or `-> M_Pl`): `lambda_Y` runs from `oo`
to Planckian while `(w0, wa)` never moves. Take `f0 -> 0`: the EOS collapses to `w=-1` while
`lambda_Y` is untouched. Both limits confirm the two observables live on independent axes.

---

## 3. The one genuine scale-cancelling lock -- and what it is NOT (cross-checker)

`mu_DW` DOES cancel, but between the graviton mass and the DeWitt VACUUM DENSITY (H50/H51),
because both are content of the ONE operator symbol `P(s) = s^2 + m2_eff mu_DW^2 s + c_L mu_DW^4`:

```
lambda_Y = hbar_c * c_L^{1/4} / (sqrt(m2_eff) * rho_Lambda^{1/4})      (mu_DW cancels; c_L = 3/8)
```

This is a REAL forced scale-invariant lock. **But:**
1. It ties the Yukawa to the DE **DENSITY** (the vacuum `rho_Lambda`, the `w=-1` component),
   **NOT to the EOS SHAPE** `(w0, wa)`. `lambda_{N,1}` and `f0` are ABSENT from it. The DeWitt-
   Lambda is a background/trace-sector object (TT-graviton `s^0` coeff `A0 = 0`, H51),
   confirming its DE input is the vacuum SCALE, not the dynamical EOS.
2. Reaching a NUMBER (`lambda_Y ~ 60-74 um`, H51) requires the **H36 identification**
   `rho_Lambda = observed DE` -- a POSTULATE (wave30 Q2, `[wild]`), NOT family-forced. Drop H36
   and `mu_DW` is free again -> even this lock DECOUPLES.

So the only surviving scale cancellation is a DENSITY x gravity lock (already H50/H51), not the
C3 EOS x gravity correlation.

---

## 4. Family-invariance (referee)

- The `mu_DW` cancellation in the density-lock is family-invariant **in FORM** (holds for all
  `mu_DW`). But its O(1) prefactor `c_L^{1/4}/sqrt(m2_eff)` drifts ~22% across the
  `beta/alpha`-bounded band `m2_eff in [5/6,5/4]` -> the lock is a BAND, not a sharp point; the
  residual `beta/alpha` does NOT fully cancel.
- The EOS x gravity correlation itself is NOT family-invariant -- it does not exist as a locus
  (Part 2). The invariance question is moot: there is nothing to be invariant.

---

## 5. The adversary's objections (presented; the synthesizer weighs, does not veto)

- **"The correlation depends on `beta/alpha`, so it is not family-invariant."** UPHELD in the
  stronger sense: it does not merely depend on `beta/alpha` -- it does not exist at all as a
  cross-sector locus, because the EOS and the Yukawa share NO residual (block-diagonal). The
  `beta/alpha` dependence only survives as a ~22% band on the DENSITY-lock prefactor.
- **"Any theory linking DE to modified gravity makes a similar correlation."** UPHELD for the
  density-lock: generic degravitation / "graviton-mass = DE-scale" models (Dvali/Deffayet-class)
  ALSO tie a graviton mass to the DE scale, and the `meV = rho_Lambda^{1/4}` coincidence is
  KNOWN numerology. So the density-lock is NOT discriminating and NOT novel.
- **Adversary's residual concession:** the ONE thing generic single-sector models lack is the
  simultaneous presence of BOTH modes from ONE object -- that is where any surviving GU
  discriminator must live (see Part 6).

---

## 6. What survives -- the strongest forced-and-novel statement (synthesizer)

> **Forced CO-PRESENCE (qualitative, family-invariant, discriminating -- but not a quantitative
> correlation).** Because the DE scalar mode and the strong-field massive spin-2 are BOTH modes
> of the single induced `|II|^2` shape action, GU forces their CO-PRESENCE: no family member can
> have a dynamical dark-energy EOS (`w != -1` from rolling theta) while lacking the massive
> spin-2 companion, or vice versa. LCDM has NEITHER (w=-1, GR spin-2); generic quintessence has
> the EOS but no massive graviton; generic massive gravity has the graviton but `w=-1`. Only a
> single-object shape theory forces BOTH. This co-presence is family-invariant (every member
> carries both modes) and discriminates from every single-sector model. It is QUALITATIVE (a
> joint non-vanishing), NOT a quantitative scale-cancelling correlation, because the two modes
> carry masses ~30 orders of magnitude apart (`O(H0)` vs `mu_DW`) set by DIFFERENT mechanisms
> (curvature-coupling vs mass-gap).

GU adds two further SEPARATE forced facts on top of the co-presence -- `alpha_Y = 1/3` (fixed)
and the root-system EOS family `{3,7,8,...}` -- but these are independent sub-facts, not a
joint locus.

---

## Graded verdict

| sub-question | grade | one line |
|---|---|---|
| **Q-forced** | **NO** (for the literal C3) | disjoint residuals; block-diagonal map; no scale cancels between EOS and Yukawa. The only cancellation is DENSITY x Yukawa (H50/H51), conditional on the H36 postulate. |
| **Q-novel** | **LOW** | the surviving lock is the known degravitation / `meV`-coincidence pattern, already wave30/wave31. No NEW forced EOS-shape x strong-field correlation. |
| **Q-disc** | **WEAK** | the density-lock is reproduced by generic massive-gravity-as-DE (not discriminating). The genuine discriminator is a QUALITATIVE co-presence + two separate fixed sub-facts, not a family-invariant correlation. |

**Confidence: HIGH** that the literal C3 correlation is not forced (the disjointness is exact
and symbolic, and robust to the load-bearing assumption -- see below). **MEDIUM** on the value
of the surviving co-presence as a headline (it is real and discriminating but only qualitative).

**Load-bearing assumption.** That the DE theta is a CURVATURE-COUPLED LIGHT mode
(`M^2 ~ H0^2`, root eigenvalue) rather than a hard `mu_DW`-mass mode. This is what makes the EOS
shape `mu_DW`-blind and thereby BREAKS the hoped-for scale cancellation. It is the wave20/H43
construction. It is ROBUST in the following sense: if instead the theta mass were `mu_DW`-set
(`~meV` or `~M_Pl`), the field would be frozen relative to `H0` (`M/H0 ~ 10^{30}`), giving
`w=-1` exactly and NO dynamical EOS at all -- so there would be nothing to correlate. Either
way the literal EOS x gravity correlation fails: either the EOS is `mu_DW`-blind (disjoint) or
the EOS does not exist (frozen).

---

## COMPUTED vs ARGUED ledger

- **COMPUTED (exact/symbolic):** the KG coefficient `M^2/H^2 = lambda_{N,1}` carries no `mu_DW`
  (EOS `mu_DW`-blind); the Yukawa symbol carries no `lambda_{N,1}`/`f0` (Yukawa EOS-blind);
  hence the block-diagonal map and the fixed-EOS/fixed-Yukawa sweeps; the `mu_DW` cancellation
  in the density-lock and its ~22% prefactor band over `m2_eff in [5/6,5/4]`; the two-point
  `(w0,wa)` KG integration.
- **ARGUED (structural/evidence tier):** the load-bearing light-mode assumption (= H43
  construction); that generic degravitation reproduces the density-lock (Q-disc FAIL for the
  scale-lock); that the surviving co-presence discriminates from single-sector models; the H36
  postulate status (cited from wave30).

## Honest limits

1. The `(w0,wa)` values here are a crude two-point proxy of the H43 integration, used only to
   exhibit that the EOS is dynamical and eigenvalue-dependent; the falsification-grade `(w0,wa)`
   locus is H43's, not recomputed. The STRUCTURAL claims (mu_DW-blindness, block-diagonality)
   are exact and do not depend on the proxy's precision.
2. The co-presence claim assumes the DE theta and the strong-field spin-2 are genuinely both
   modes of the one `|II|^2` action. This is plausible (both are variations of the single
   embedding) but the exact mode decomposition on FLRW vs flat backgrounds is not re-derived
   here; hence co-presence is graded ARGUED-structural, not COMPUTED.
3. No source action is built; the residual `beta/alpha` fork (H45 vs H48) is not resolved. This
   branch tests the CORRELATION, not the construction.

## RE-RANK signal

**The EOS x strong-gravity correlation is NOT a forced family-invariant discriminating locus.**
The DE EOS shape and the strong-field Yukawa depend on DISJOINT residual parameters
(`lambda_{N,1}, f0` vs `mu_DW, m2_eff`); the residual->observable map is block-diagonal, so the
free scales do NOT cancel between the two sectors and there is no correlation locus. The one
genuine scale-cancelling relation is a DENSITY x Yukawa lock (already H50/H51), which is
conditional on the H36 postulate and reproduced by generic degravitation -- neither novel nor
discriminating. What GU genuinely forces is a QUALITATIVE, family-invariant, discriminating
CO-PRESENCE of both modes from the one `|II|^2` action; it is the strongest defensible
statement but is not the hoped-for quantitative headline. Do NOT re-spend effort trying to
cancel scales BETWEEN these two sectors: the disjointness is exact and robust to the light-mode
assumption.

---

*Filed 2026-07-11. Path4 branch A (thread C3), blind multi-team wave. Reproducible:
`python -u tests/W61_path4_A_eos_gravity.py` (exit 0, 16/16 PASS). Exploration-grade; not
promoted to canon; no verdict/claim-status change; tree left dirty (no commit). Adversarially
graded: the hoped correlation was tested for and NOT found (block-diagonal), the surviving lock
was tested for novelty/discrimination and FAILS both, and the co-presence that survives is
stated with its qualitative limit. No forcing manufactured, no kill evaded.*
