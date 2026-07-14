# H50 (Wave 30) -- The first-prediction test: does `mu_DW` = the dark-energy scale, and what does GU then predict?

**Object.** Everything empirical in GU is gated on ONE scale, `mu_DW` (H49/wave28). H50 asks whether GU's structure *sets* that scale via the O(M^0) DeWitt-Lambda (H24) identified with the observed dark energy (H36), and whether the resulting sub-millimetre gravity deviation is a genuine falsifiable prediction or is already **excluded by its own prediction**. Both outcomes are successes; no preferred result.

**Test:** `tests/wave30/H50_mudw_de_scale_prediction.py` -- deterministic, exit 0.

---

## The four verdicts

### Q1 -- THE ONE-SCALE LINK: **HOLDS** (COMPUTED, structural)

GU's graviton operator symbol (H24 Part 2c) with the O(M^0) term restored is
`P(s) = s^2 + m2_eff*mu_DW^2 * s + c_L*mu_DW^4`, with `s = box` of dimension `[mass^2]`. Dimensional closure forces every monomial to degree `mu_DW^4` (COMPUTED, exact sympy), so a **single** dimensionful scale `mu_DW` governs the whole operator. The two physical outputs are both a single power of `mu_DW` times a *geometric* O(1) factor:

- **DeWitt-Lambda** (the s^0 vacuum term, H15 Part D / H24 Part 2 horizontal-sectional constant): a vacuum energy density `rho_Lambda ~ c_L * mu_DW^4`, `c_L` an O(1) geometric constant (horizontal ambient sectional `~ -3/8`, H24).
- **Massive spin-2** (the s^1/s^2 ratio, H10/H49): `m2 = sqrt(m2_eff) * mu_DW`, `m2_eff in [5/6, 5/4]` (H25).

Eliminating `mu_DW`: **`m2 = (sqrt(m2_eff)/c_L^{1/4}) * (rho_Lambda)^{1/4}`**. The graviton mass is **locked** to the cosmological scale by computed geometric O(1) factors only -- there is **no second free scale**. This is exactly what turns a sub-mm number into a *prediction* rather than a second free parameter. **One `mu_DW` sets both.**

### Q2 -- THE H36 IDENTIFICATION: **CONDITIONAL-ON-H36 (a postulate), NOT GU-forced**

- That an O(M^0) DeWitt-Lambda *exists* is **forced** by GU structure (H15 Part D / H24 Part 2 compute the horizontal-sectional vacuum constant). COMPUTED elsewhere.
- That it *equals the observed dark-energy density* is ranker item **H36**, explicitly tagged **`[wild]`**: "the O(M^0) DeWitt-Lambda = the dark-energy scale = the issuance/non-collapse rate." This is an interpretive **identification, not a theorem**.
- Reinforcing the postulate reading: the H49 **Lambda-magnitude no-go** (COMPUTED) proves a scale-free `g`-vs-`G` action *cannot derive* the `~10^-122` magnitude; the meV scale must be **imported**. `mu_DW = (rho_Lambda)^{1/4} ~ 2.3e-3 eV` is precisely that imported scale.

So the prediction is **GIVEN the H36 identification**, not GU-forced. Under it, `mu_DW ~ 2.3 meV` -- ~31 orders of magnitude **below** the "natural" `mu_DW ~ M_Pl` default of H24/H49. H36 *replaces* the Planck default with the meV DE scale. **Do not overclaim forced.**

### Q3 -- THE PREDICTION + THE EXPERIMENTAL TEST: **EXCLUDED at face value** (make-or-break)

Under `mu_DW = 2.3e-3 eV`, `m2 = sqrt(m2_eff)*mu_DW`, `lambda = hbar_c/m2` (`hbar_c = 197.327 eV*nm`):

| `m2_eff` | `m2` | `lambda = hbar_c/m2` |
|---|---|---|
| 5/6 (longest range) | 2.0996 meV | **93.98 um** |
| 1 | 2.3000 meV | 85.79 um |
| 5/4 (shortest range) | 2.5715 meV | **76.74 um** |

**GU-under-H36 predicts a sub-millimetre Yukawa: `V(r) = -(GM/r)[1 + (1/3) e^{-r/lambda}]`, range `lambda in [76.7, 94.0] um`, strength `alpha = 1/3` (vDVZ trace factor, H10 -- FIXED, not free).** (Unit re-check done two independent ways; agree exactly.)

**Real published bounds (comparison only, cited; no invented numbers):**

| experiment | `alpha=1` reach | `<=> mu_DW` floor (`alpha=1`, `m2_eff=5/6`) |
|---|---|---|
| Kapner et al. 2007, PRL 98 021101 (Eot-Wash) | `lambda > 56 um` | 3.86 meV |
| Tan et al. 2020, PRL 124 051301 (HUST) | `lambda > 48 um`; strongest `alpha` bound over 40-350 um; ~3x improvement at ~70 um | 4.50 meV |
| Lee et al. 2020, PRL 124 101101 (Eot-Wash) | `lambda > 38.6 um` | 5.60 meV |

- GU's `lambda` (76.7-94.0 um) **exceeds every `alpha=1` crossing** by factors 1.4-2.4: the massive-spin-2 Yukawa lives in the experiments' **most-sensitive band**, not below their reach. (COMPUTED)
- The DE-scale `mu_DW = 2.3 meV` is **below all three `alpha=1` floors** -- even at *unit* strength the predicted deviation would already have been seen. This reconciles H49's stated Eot-Wash floor `mu_DW > ~3.8 meV`. (COMPUTED vs cited)
- The fair test is at `alpha=1/3`. Its exclusion reaches a somewhat larger `lambda` / lower `mu_DW` floor than `alpha=1`. We do **not** invent a curve value; we bound it: HUST reports the `alpha` bound already `~3x` below unity at `~70 um`, and it tightens at longer `lambda`, so at 77-94 um the bound is order `1e-2..1e-1` -- **well below 1/3**. The conservative `alpha=1/3` `mu_DW` floor is `~3.0-3.6 meV`, still **above** the DE value 2.3 meV. (ARGUED from the monotone curve + cited HUST factor-3 at 70 um)

**Verdict Q3: EXCLUDED.** The predicted `(alpha=1/3, lambda~77-94 um)` point sits in the excluded region of Lee 2020 / Tan 2020 / Kapner 2007. **Margin (honest):** `mu_DW` would need to be `~1.3x` higher (`>= ~3.0 meV`) to clear the `alpha=1/3` floor; equivalently GU's `alpha=1/3` sits **~3-10x above** the bound at its predicted `lambda`. The exclusion is by an **O(1) factor** -- GU-under-H36 sits *at* the frontier, not deep in the excluded region.

### Q4 -- VERDICT: **SELF-FALSIFIED-AT-FACE-VALUE (conditional-on-H36)**

GU's first parameter-linked prediction, under its own H36 identification, is **excluded by existing short-range gravity** -- a genuine self-falsification of "GU-under-H36". This is a **major honest outcome** (GU handed a falsifiable number and the number is in tension with data), stated without evasion.

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| operator symbol homogeneous of degree `mu_DW^4`; one scale governs the operator | **COMPUTED** | PART 1, exact sympy |
| `m2 = (sqrt(m2_eff)/c_L^{1/4})*(rho_Lambda)^{1/4}` (graviton mass locked to DE scale) | **COMPUTED** | PART 1 |
| DeWitt-Lambda exists / is forced by GU structure | COMPUTED (H15 D / H24) | cited, prior waves |
| "DeWitt-Lambda = observed DE" is a postulate (H36 `[wild]`), scale imported | **ARGUED** | ranker H36 + H49 no-go |
| `lambda in [76.7, 94.0] um`, `alpha=1/3` under `mu_DW=2.3 meV` | **COMPUTED** | PART 3, unit-rechecked |
| `alpha=1` crossings 38.6 / 48 / 56 um; `mu_DW` floors 5.60 / 4.50 / 3.86 meV | COMPUTED vs cited | Lee/Tan/Kapner (comparison only) |
| `alpha=1/3` bound at 77-94 um is `<< 1/3` -> EXCLUDED | **ARGUED** | monotone curve + HUST factor-3 at 70 um |
| exclusion margin is O(1); `c_L` shift -> LIVE at frontier | ARGUED | PART 4 |

## Honest limits

1. **Forced vs conditional (the load-bearing caveat).** The exclusion falsifies the **H36 identification**, *not* GU-gravity per se. Drop H36 and `mu_DW` is free again -> the sub-mm distinction is **DECOUPLED** (no prediction), which is exactly the H49 posture. H50's bite is: you *cannot* simultaneously (a) identify the DeWitt-Lambda with the observed DE **and** (b) keep GU's graviton-mass link, because together they force an already-excluded sub-mm Yukawa.
2. **The exact experimental margin is O(1), and the prediction sits on the boundary.** The uncomputed DeWitt coefficient `c_L` (`rho_Lambda = c_L*mu_DW^4`, `c_L ~ 3/8` from the horizontal sectional) enters as `mu_DW = (rho_Lambda/c_L)^{1/4}`. A `~1.5x` upward shift of `mu_DW` (`c_L ~ 0.2`) moves `lambda` to `~55 um` and the `alpha=1/3` point back to the **currently-allowed frontier** (a next-gen target). So the face-value exclusion is **not decisive** -- it is a near-miss self-falsification savable by the one O(1) number GU has not computed.
3. **The `alpha=1/3` floor is argued, not digitized.** The `alpha=1` crossings (38.6 / 48 / 56 um) are citable published numbers; the `alpha=1/3` bound at 77-94 um is inferred from the monotone exclusion curve plus HUST's stated factor-3 improvement at 70 um, not read off a digitized figure. The conclusion (`alpha=1/3` excluded at 77-94 um) is robust to this, but the precise margin is not pinned to better than the stated O(1).
4. **`m2_eff` band is real, not cherry-picked.** Both ends (5/6 and 5/4, the two H25 methods) give `lambda` in the excluded band; the result does not depend on choosing a favourable `m2_eff`.

## RE-RANK signal

**SELF-FALSIFIED-AT-FACE-VALUE (H36 identification excluded; borderline-LIVE within O(1)).** GU's one-scale link is real (Q1 holds), the DE identification is a postulate (Q2 conditional-on-H36), and under it the first prediction is `alpha=1/3` at `lambda~77-94 um`, which existing Eot-Wash/HUST short-range gravity **excludes by an O(1) factor**.

**Single next object:** **compute the DeWitt coefficient `c_L`** in `rho_Lambda = c_L*mu_DW^4` (from the horizontal-sectional constant `~ -3/8` plus the source-action normalization). `c_L` is the one number that decides **EXCLUDED vs LIVE-at-the-frontier**, and it is the same source-action scale that gates all of GU (`mu_DW`, the norm/survival, loop positivity, the count). H50 thus sharpens the entire program's gate onto a single computable O(1) coefficient.

---

*Sources for the published bounds (comparison only): Kapner et al., Phys. Rev. Lett. 98, 021101 (2007); Lee et al., Phys. Rev. Lett. 124, 101101 (2020); Tan et al., Phys. Rev. Lett. 124, 051301 (2020).*

---

## CORRECTION (2026-07-13, wave 32 / H52 -- appended, original text above unchanged)

The `alpha=1/3` boundary is now **CITED, no longer argued** (`explorations/wave32/H52-alpha13-boundary-cited-2026-07-13.md`, test `tests/wave32/H52_alpha13_boundary_cited.py`, exit 0). The n=1 radion benchmark has `alpha = n/(n+2) = 1/3` exactly, so the published radion bounds ARE published `alpha=1/3` crossings via the published fit `lambda = 2.4 (TeV/M*)^2 mm` (Adelberger et al., hep-ph/0611223): Lee 2020 (`M* >= 7.1 TeV`) gives **`lambda_max(alpha=1/3) = 47.6 um`** (band [46.0, 51.2] um); Kapner 2007 gives 73.9 um; Tan 2020 ~59 um (interpolated). Three items in this page are superseded:

1. **The floor.** This page's argued `mu_DW >= ~3.0-3.6 meV` is the **Kapner-2007-only** floor (its 3.0 meV end back-solves to `lambda_max ~= 72 um ~` Kapner's 73.9 um crossing). Against the 2020 frontier the resolved floor is **`mu_DW >= 3.71 meV (m2_eff=5/4) to 4.54 meV (m2_eff=5/6)`**, envelope [3.4, 4.7] meV. Track-2's 3.4-4.8 meV band was the right one.
2. **Kapner-alone scope.** Kapner 2007 alone DOES exclude this page's `c_L=1` window [76.7, 94.0] um (76.7 > 73.9) but does NOT exclude the H51 `c_L=3/8` window [60.0, 73.6] um; that exclusion rests on Lee 2020 / Tan 2020.
3. **Q3/limit-3 wording** ("argued, not digitized"): the boundary is now anchored in PUBLISHED-QUOTED numbers + the published fit function; no figure was digitized. Verdict Q3 (EXCLUDED) STANDS and strengthens: margin at the predicted lambda is now 1.9-9.8x, cited.
