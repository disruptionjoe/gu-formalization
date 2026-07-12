# H51 (Wave 31) -- Compute the DeWitt coefficient `c_L`, and settle GU's first prediction

**Object.** H50 (wave30) showed that ONE scale `mu_DW` sets both the O(M^0) DeWitt-Lambda (`rho_Lambda = c_L*mu_DW^4`) and the massive spin-2 mass (`m2 = sqrt(m2_eff)*mu_DW`). Under the H36 identification `rho_Lambda = ` observed dark energy, `mu_DW` **cancels** and the predicted Yukawa range is a convention-independent geometric number,

```
lambda = hbar_c * c_L^{1/4} / (sqrt(m2_eff) * rho_Lambda^{1/4}).
```

H50 left `c_L` **uncomputed** (estimated `~3/8`), naming it the single number that decides EXCLUDED vs LIVE. H51 computes it from the actual gimmel/DeWitt geometry and reads off the verdict. Both outcomes are successes; no preferred result.

**Test:** `tests/wave31/H51_dewitt_coefficient_cL.py` -- deterministic, exit 0.

---

## The four verdicts

### Q1 -- COMPUTE `c_L`: **`c_L = 3/8` (EXACT)** [COMPUTED]

The O(M^0) DeWitt cosmological coefficient is the **pure-horizontal ambient sectional curvature** of the gimmel metric on `Y = Met(X)` -- the leading curved-ambient correction, a 0-derivative constant (H24 Part 2 / H25 Part 0). The DIM=4 machinery gives it exactly:

- pure-horizontal ambient sectional `= -3/16` (non-doubled basis), diagonal mixed sectional `= -1/2` (convention-robust). The A-oracle-authoritative **doubled-basis** value is `-3/8` (a factor 2 above the non-doubled `-3/16`; documented in H24/H25).
- **`c_L = |horizontal ambient sectional (oracle basis)| = 3/8 = 2*(3/16)`.** H50's `~3/8` estimate is **confirmed exact**, not a guess.

**Corroboration (independent object, same functional):** the constant-section trace-reversed Frobenius DeWitt shape energy (thread B) is `|H|^2_V = -1`, `|II|^2_V = 2`, with fiber-trace `= (1/2) eta_mn` -- the O(M^0) vacuum density is Lambda-shaped, a nonzero constant.

**Normalization -- the crux the task demands be shown [COMPUTED].** Extracting all three coefficients of the graviton operator symbol `P(s) = A2 s^2 + A1 s + A0` from the *same* `|II|^2` second-variation machinery as H25 Method 2 (three configs, full curved-ambient), the **TT-graviton s^0 coefficient `A0 = 0` exactly** (with `A2(Weyl) = 1`, `m2_eff = A1/A2 = 5/4`). So the DeWitt Lambda is **not a TT-graviton mass** -- it is a background / trace-sector vacuum energy. `c_L` is therefore the O(M^0) **background** density coefficient, a dimensionless geometric **sectional** in the *same status* as the `-1/2` mixed sectional that fixes `m2_eff`: both are convention-robust coefficients of the one symbol with the overall scale `mu_DW` factored out. This is what makes `c_L^{1/4}/sqrt(m2_eff)` convention-independent.

> **Honest normalization limit.** Because the DeWitt Lambda is a background (not TT-kinetic) object, its normalization against the TT Weyl coefficient carries an O(1) convention freedom. The horizontal sectional gives `c_L = 3/8`; the constant-section full shape density gives `|II|^2_V = 2` as the *upper* end of that O(1) band. The verdict (below) is robust across the whole band.

### Q2 -- THE PREDICTED `lambda`: **`lambda in [60.0, 73.6] um`** (`mu_DW` cancels) [COMPUTED]

Substituting `mu_DW = (rho_Lambda/c_L)^{1/4}` into `m2 = sqrt(m2_eff)*mu_DW` gives `lambda = hbar_c*c_L^{1/4}/(sqrt(m2_eff)*rho_Lambda^{1/4})` -- `mu_DW` **cancels identically** (verified symbolically). With `c_L = 3/8`, `rho_Lambda^{1/4} = 2.3` meV, `hbar_c = 197.327` eV*nm (so `hbar_c/rho^{1/4} = 85.79 um`, `c_L^{1/4} = 0.7825`):

| `m2_eff` | source | `lambda` |
|---|---|---|
| 5/6 (longest) | H25 Method 1 (convention-robust) | **73.6 um** |
| 5/4 (shortest) | H25 Method 2 | **60.0 um** |

Units re-checked two independent ways (`hbar_c[eV*nm]/rho` vs `hbar_c[eV*m]/m2`), agree. **Computing `c_L = 3/8` LOWERED `lambda`** from H50's `c_L=1` band `[76.7, 94.0] um` by `c_L^{1/4} = 0.78`, toward the frontier -- but still firmly sub-millimetre. Strength `alpha = 1/3` (vDVZ trace factor, H10 -- fixed, not free).

### Q3 -- VERDICT vs REAL BOUNDS: **EXCLUDED at alpha=1/3** [COMPUTED vs cited/argued]

Published `|alpha|=1` crossings (comparison only, cited): **Lee 2020** (Eot-Wash) `lambda < 38.6 um`; **Tan 2020** (HUST) to `48 um`, strongest alpha bound over 40-350 um, ~3x improvement near 70 um; **Kapner 2007** (Eot-Wash) `56 um`. The `alpha=1/3` boundary reaches a somewhat *larger* `lambda`; from the monotone alpha-vs-lambda curve it is **argued at `lambda ~ 45-52 um`** (H50).

The computed band `[60.0, 73.6] um` lies **above** the `alpha=1/3` boundary at **both** ends -> the `(alpha=1/3, lambda)` point sits in the **excluded** region.

- **Margin (honest, O(1)):** the closest corner (`m2_eff=5/4`, `60.0 um`) sits `~1.15x` above the conservative 52 um boundary (`~1.33x` above the aggressive 45 um). The convention-robust `m2_eff=5/6` corner (`73.6 um`) clears by `~1.4x`.
- **Robustness to `c_L`:** reaching the allowed window (`lambda < 40 um`) would require `c_L < ~0.03-0.07` (a `~5x` drop from the computed 3/8), far below every geometric estimate (`3/8`; constant-section `2`). At the upper end `c_L=2`, `lambda in [91, 112] um` -- *more* excluded. The verdict does not depend on the `c_L` normalization choice.

### Q4 -- VERDICT: **EXCLUDED -> GU-under-H36 SELF-FALSIFIED** (conditional-on-H36)

GU's first parameter-linked prediction, under its own H36 identification, is in tension with existing short-range gravity. **The exact `c_L` did not rescue it** -- it moved `lambda` toward the frontier but left it excluded by an O(1) factor. This is a major honest outcome: GU handed a falsifiable number, the number is computed, and it is excluded.

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| horizontal ambient sectional `-3/16` (non-doubled), diagonal `-1/2` | **COMPUTED** | Part 1a, exact sympy |
| `c_L = 3/8` (oracle doubled basis) = O(M^0) DeWitt coefficient | **COMPUTED** | Part 1b (`= 2*(3/16)`) |
| constant-section `|H|^2_V=-1`, `|II|^2_V=2`, fiber-trace `(1/2)eta_mn` | **COMPUTED** | Part 1c (thread B) |
| TT-graviton `s^0` coefficient `= 0`; `A2(Weyl)=1`, `m2_eff=5/4` | **COMPUTED** | Part 1d, `|II|^2` 2nd variation |
| `mu_DW` cancels; `lambda = hbar_c c_L^{1/4}/(sqrt(m2_eff) rho^{1/4})` | **COMPUTED** | Part 2a, symbolic |
| `lambda in [60.0, 73.6] um` at `alpha=1/3` | **COMPUTED** | Part 2, units two ways |
| `alpha=1` crossings 38.6 / 48 / 56 um | COMPUTED vs cited | Lee/Tan/Kapner |
| `alpha=1/3` boundary `~45-52 um` | **ARGUED** | monotone curve, not digitized |
| `[60.0,73.6] um` EXCLUDED at `alpha=1/3` | COMPUTED vs ARGUED bound | Part 3 |
| O(1) background-vs-TT normalization of `c_L` | ARGUED | Part 1d limit |

## Honest limits

1. **Forced vs conditional (load-bearing, unchanged from H50).** The exclusion falsifies the **H36 identification**, not GU-gravity per se. Drop H36 and `mu_DW` is free -> the sub-mm distinction decouples (no prediction). H51's bite: you cannot simultaneously identify the DeWitt-Lambda with the observed DE *and* keep GU's graviton-mass link, because together they force an already-excluded sub-mm Yukawa -- and now `c_L` is computed, so this is no longer evadable by the "uncomputed O(1)" escape H50 flagged.
2. **The margin is O(1) and the closest corner is near the boundary.** At `m2_eff=5/4`, `lambda = 60.0 um` sits only `~1.15x` above the conservative `alpha=1/3` boundary (52 um). A digitized `alpha=1/3` curve landing at `~55-60 um` would move that single corner to STILL-BORDERLINE. The convention-robust `m2_eff=5/6` corner (73.6 um) stays excluded.
3. **The `alpha=1/3` boundary is argued, not digitized.** The `alpha=1` crossings (38.6/48/56 um) are citable; the `alpha=1/3` boundary (~45-52 um) is inferred from the monotone curve, not read off a digitized figure. This is now the single largest residual.
4. **`c_L` normalization O(1) band.** The DeWitt Lambda is a background object (TT `s^0 = 0`, computed), so its normalization against the TT Weyl coefficient is O(1)-free (horizontal sectional `3/8` to constant-section `2`). The verdict is robust across the band, but the exact `lambda` within `[60, 112] um` is not pinned better than O(1).
5. **`m2_eff` band is real, not cherry-picked.** Both H25 methods (5/6, 5/4) give `lambda` in the excluded band.

## RE-RANK signal

**EXCLUDED (GU-under-H36 self-falsified at face value; margin O(1) at the frontier).** `c_L` is now **COMPUTED = 3/8**, closing H50's single open number and removing its "uncomputed O(1)" escape hatch. Computing it lowered `lambda` to `[60.0, 73.6] um` -- toward the frontier but still excluded.

**Single next object:** **digitize the published `alpha=1/3` exclusion curve** (Lee 2020 / Tan 2020 alpha-vs-lambda) to convert the argued `~45-52 um` boundary into a cited number. That is the *only* remaining input between EXCLUDED and STILL-BORDERLINE at the 60 um corner. (Secondary: pin the O(1) background-vs-TT normalization of `c_L` via the full higher-codimension Willmore first variation.)

---

*Sources for the published bounds (comparison only): Kapner et al., Phys. Rev. Lett. 98, 021101 (2007); Lee et al., Phys. Rev. Lett. 124, 101101 (2020); Tan et al., Phys. Rev. Lett. 124, 051301 (2020).*
