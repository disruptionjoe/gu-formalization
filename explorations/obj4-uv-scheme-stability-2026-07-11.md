---
artifact_type: exploration
status: exploration
created: 2026-07-11
objective: "Objective 4 -- upgrade the UV/FRG (Reuter-FP / ker-Gamma-RS) result from truncation/regulator evidence toward CONTROLLED evidence: classify universal vs non-universal, test gauge + field-parametrization sensitivity of the load-bearing conclusions, attach honest uncertainty ranges, and state what is CONTROLLED vs still truncation/scheme-conditional."
hypothesis: "The load-bearing FRG conclusions (Reuter-FP existence; # relevant directions; f_2^2*=0 structural root; f_0^2 relevance) survive gauge + field-parametrization change and are CONTROLLED; the eta_C sign / HORN-K-vs-Q selection does NOT get resolved by gauge or parametrization and remains the sole scheme/truncation-conditional residual."
grade: "computed-proxy + ported. Deterministic test tests/W101_obj4_scheme_stability.py, exit 0. The universal/non-universal ledger and the eta_C-scheme structural facts are re-derived in code; the gauge x parametrization invariance is a reduced 2-coupling Reuter proxy (existence + relevant-count invariant while coordinates move); the full functional gauge+parametrization+combined-f(R)+Weyl^2+ker-Gamma spin-3/2 FRG recomputation is NOT done (paper-scale) and is ported from the literature with explicit citations."
depends_on:
  - tests/W81_E2_asymptotic_safety.py
  - tests/W83_frg_fr_weyl_af_as.py
  - tests/W85_second_regulator_reuter.py
  - tests/W86_regulator_shape_sweep.py
  - tests/W89_eta_c_across_regulators.py
  - explorations/second-regulator-reuter-fp-2026-07-11.md
  - explorations/regulator-shape-parameter-sweep-2026-07-12.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W101_obj4_scheme_stability.py
---

# Objective 4 -- UV/FRG Scheme-Stability Map (Universal vs Non-Universal; Gauge + Parametrization; Controlled vs Conditional)

## Role and prior state

The FRG line established, at successively higher grade:

- **W81/W83** -- a genuine non-Gaussian **Reuter fixed point** for GU's `ker-Gamma`-RS field content, with
  the induced dimensionful `(g, lambda)` breaking the homogeneity of the marginal `(f_2^2, f_0^2)` block; a
  critical surface of dimension **3 relevant `{g, lambda, f_0^2}` + 1 marginal `f_2^2`**; `f_0^2` de-forced
  to a **relevant** direction (which de-forces `sign(f_0^2)` and closes the observer leg).
- **W85** -- **regulator robustness**: a second (exponential) regulator preserves FP existence, the relevant
  count, `f_0^2` relevance, and the RS anti-screening sign; only the non-universal values move.
- **W86** -- a **shape-parameter sweep** over `r_s(y)=s y/(e^y-1)` confirms the same gates across a shape family.
- **W89** -- reduces the type-III Krein-TT horn to `sign(eta_C)`, and finds it is **`Z_h`-SCHEME-dependent**:
  EH-adapted `Z_h=Z_N` gives `eta_C=+2 c_reg>0` (HORN Q, lift); Weyl-adapted `Z_h=1/f_2^2` gives `eta_C=0`
  (HORN K, frontier real). The physically-correct leading-4th-order (Weyl-adapted) scheme -> **HORN K lean**,
  truncation-conditional.

Objective 4 asks for the biggest **controlled-evidence** step now available: a universal/non-universal
classification; a **gauge** and **field-parametrization** sensitivity test of the load-bearing conclusions;
honest uncertainty ranges; and a clean CONTROLLED-vs-conditional map. This document runs a 5-persona team
inline and encodes the result in `tests/W101_obj4_scheme_stability.py`.

## Honesty preface (computed vs ported)

A full gauge + parametrization functional FRG recomputation of the combined `f(R)+Weyl^2 + ker-Gamma`
spin-3/2 object is **paper-scale** and is **not** performed here. What is **computed** (reduced-proxy grade,
in the W85/W86 discipline): the universal/non-universal ledger as a checked structure; the `f_2^2*=0`
structural root and the `eta_C`-sign-rides-the-scheme facts (re-derived in code); and a reduced 2-coupling
Reuter proxy carrying an explicit gauge parameter `alpha` and a linear-vs-exponential split flag, verifying
that the qualitative gates are invariant while the coordinates move. What is **ported** (cited): the known
gauge- and parametrization-(in)dependence of the Reuter FP and of the higher-derivative Weyl AF.

---

## Persona 1 -- FRG / Asymptotic-Safety specialist (the construction)

**The universal / non-universal split is the whole game.** In FRG every dimensionless FP coordinate is a
scheme-dependent number; treating its motion as fragility is a category error. What carries physics is the
**qualitative** content that is invariant. The ledger:

**UNIVERSAL (scheme / gauge / parametrization / regulator-independent):**

1. **Existence of the Reuter (non-Gaussian) FP** for GU's matter-corrected content (inside the
   Dona-Eichhorn-Percacci region). This is the single most robust AS result: it survives all four axes.
2. **Number of relevant directions** = **3 `{g, lambda, f_0^2}` + 1 marginal `f_2^2`** (an integer count;
   it carries zero uncertainty).
3. **Sign of the critical exponents** on the relevant block (`Re(theta)>0`); in the EH sub-block the
   UV-attractive pair is complex with positive real part.
4. **`f_2^2*=0` as a structural Gaussian root** of `beta_{f_2^2} = -kappa f_2^4(b_grav+b_RS) + eta_C f_2^2`.
   Both terms carry a factor `f_2^2`, so `f_2^2=0` is a root for *any* `(kappa, b, eta_C)` -- at every gauge,
   parametrization, regulator, **and** scheme. This is the most invariant object in the whole line.
5. **`f_0^2` relevance** (`R^2` relevant), which de-forces `sign(f_0^2)`.
6. **RS `ker-Gamma` anti-screening SIGN** (heat-kernel spin coefficient x positive-definite threshold).

**NON-UNIVERSAL (moves; motion is expected, not failure):** `g*`, `lambda*`, `f_0^2*` magnitude, `f_2^2*`
magnitude on the lifted HORN-Q branch, `eta_C` **magnitude**, the numerical exponent **values** `theta_i`,
`eta_N*` magnitude (canonically `-2`, with scheme `O(0.3)` spread).

**SEMI (universal in some axes, non-universal in others):** `sign(eta_C)` -> HORN K vs HORN Q, which is
robust across gauge/parametrization/regulator **within a scheme** but flips across the `Z_h` **scheme**; and
`g* lambda*`, which is quasi-universal (a narrow band, not an exact invariant).

## Persona 2 -- Referee grading universal-vs-non-universal (the discipline check)

I accept the six universal entries with one sharpening and one demotion.

- **Sharpening (entry 6).** RS anti-screening is universal only at the level of its **sign**. Its
  **magnitude** and the precise `ker-Gamma` projection are not controlled. Grade it `CONTROLLED(sign)`, and
  do not let the magnitude ride along.
- **Demotion I refuse.** Entry 4 (`f_2^2*=0` structural root) is sometimes waved away as "trivial." It is
  not: it is exactly the object that makes HORN K *always available* regardless of scheme. The horn question
  is never "does a Gaussian root exist" (it always does) but "is there *also* a lifted root `f_2^2*>0`,"
  i.e. `sign(eta_C)`. Keeping `f_2^2*=0` in the universal column is correct and load-bearing.
- **On the counts.** A relevant-direction **count** is an integer and must be reported with **zero**
  uncertainty. Putting error bars on "3" would be a grading error. The uncertainty lives on the exponent
  **values**, not the count. The test enforces this separation (`COUNTS_ZERO_UNCERTAINTY`).

Verdict on the ledger: **sound**, provided `sign(eta_C)` is filed as SEMI (not universal) and RS is filed as
sign-only. Both are encoded.

## Persona 3 -- Adversary: "gauge dependence kills it"

My thesis: FRG results are notoriously gauge- and parametrization-dependent; the "Reuter FP" is an artifact
of the harmonic gauge `alpha` and the linear split, and the HORN-K lean is a gauge choice dressed as physics.

**Where I land after the checks -- three concessions and one score.**

1. **FP existence is not mine to kill.** The `alpha`-dependence of the EH Reuter FP was mapped long ago
   (Lauscher-Reuter): `g*`, `lambda*` move with `alpha`, but the FP persists and the number of UV-attractive
   directions is stable; the product `g* lambda*` is quasi-invariant. Gies-Knorr-Lippoldt then showed the FP
   and exponents survive a *generalized* parametrization + gauge family, and that the **exponential split
   reduces** the gauge dependence. Dona-Eichhorn-Percacci and Ohta-Percacci-Vacca show the FP exists in both
   linear and exponential parametrizations with a stable relevant count. The proxy in `W101` reproduces the
   qualitative behaviour: across a `5 x 2` grid of `(alpha, param)` the FP exists everywhere, the relevant
   count is invariant (`=2` in the reduced EH block), the exponents stay a complex pair with `Re>0`, while
   `g*` and `lambda*` move (`x1.25`, `x1.18`) and `g* lambda*` stays in a `x1.22` band. **Concession: gauge
   and parametrization do not kill FP existence or the count.**

2. **The relevant count is an integer; I cannot move it continuously.** No `alpha` and no split changes 3
   into 4. **Concession.**

3. **The HORN-K lean is where I press -- and I still lose the gauge/param attack, but not the war.** The
   HORN-K lean rests on (a) the universal `f_2^2*=0` root and (b) the **gauge-independent** Weyl one-loop AF
   (`f_2^2 -> 0`; Fradkin-Tseytlin, Avramidi-Barvinsky; the one-loop higher-derivative dimensionless beta
   coefficients are famously gauge- and parametrization-**unique**). Neither `alpha` nor the split touches
   either. **So gauge/parametrization do not flip the horn.** My real lever is the `Z_h` **scheme**
   (EH-adapted vs Weyl-adapted) -- and that is precisely *not* a gauge or parametrization choice. **Score:
   the horn survives my gauge attack; it remains open on the scheme/truncation axis, which is honest, not a
   kill.**

**Adversary's residual, stated fairly:** the one thing I *can* still say is that `eta_C`'s sign is not
CONTROLLED -- it is scheme/truncation-conditional. That is already the line's own admission (W89). I do not
get to upgrade "scheme-conditional" to "gauge-dependent-therefore-artifact"; those are different axes.

## Persona 4 -- Cross-checker + literature (ported robustness, cited)

Porting map (read-only; these stand in for the paper-scale recomputation):

| Load-bearing claim | Ported robustness | Sources |
|---|---|---|
| Reuter FP existence, gauge `alpha` | `g*,lambda*` move; FP + UV-attractive count stable; `g*lambda*` quasi-invariant | Lauscher-Reuter (gauge/`alpha` study of the EH FP) |
| FP + exponents under generalized gauge + parametrization | robust; exponential split **reduces** gauge dependence | Gies-Knorr-Lippoldt, "Generalized parametrization dependence in QG" |
| Exponential vs linear split | FP exists in both; relevant count stable; coords + matter bounds move | Dona-Eichhorn-Percacci; Ohta-Percacci-Vacca; Nink |
| Higher-derivative Weyl one-loop AF (`f_2^2 -> 0`), gauge/param | dimensionless one-loop beta coefficients gauge- & parametrization-unique | Fradkin-Tseytlin; Avramidi-Barvinsky; Benedetti-Machado-Saueressig (essential scheme) |
| `R^2` relevant (`f_0^2` relevance) across regulators/truncation orders | robust | Codello-Percacci-Rahmede; Benedetti-Machado-Saueressig; AS-Starobinsky |
| Matter anti-screening region | GU RS content sits inside the allowed region; sign robust | Dona-Eichhorn-Percacci bounds |

**Two-sidedness kept honest (as W89 already flagged).** The literature genuinely reports both outcomes for
the four-derivative sector: one-loop / several gauge+regulator combinations give Weyl AF (`f_2^2*=0`), while
a nontrivial Newton coupling is reported to **induce** additional four-derivative fixed points (a lift) in
other schemes. This is exactly the EH-adapted vs Weyl-adapted split, and it is a **scheme** two-sidedness,
not a gauge one -- consistent with the cross-check that gauge/parametrization do not decide it.

**Uncertainty ranges (ported spreads across regulator/gauge/param/truncation):**

| Quantity | Honest range | Class |
|---|---|---|
| `g*` | `0.20 - 1.50` | non-universal |
| `lambda*` | `0.05 - 0.40` | non-universal |
| `g* lambda*` | `0.10 - 0.35` | **quasi-universal** (narrow band) |
| `Re(theta)` (relevant block) | `1.0 - 2.4` | value non-universal, **sign universal (>0)** |
| `eta_N*` | `-2.3 - -1.7` (canonical `-2`) | non-universal magnitude |
| `eta_C` (Weyl-adapted, physical) | **exactly `0`** | HORN K (structural) |
| `eta_C` (EH-adapted) | `0 - ~0.2` (`= +2 c_reg`, `c_reg ~ O(0.01-0.1)`) | HORN Q |
| `n_relevant` (`f(R)`) | `3` | **universal count, zero uncertainty** |
| `n_marginal` (`f_2^2`) | `1` | **universal count, zero uncertainty** |
| `f_2^2*` (structural root) | `0` | **universal, zero uncertainty** |

Note the `eta_C` band **never goes negative**: `eta_C in [0, +]`. So "`eta_C <= 0` physically" means
`eta_C = 0` *exactly* (the structural root), and the horn is decided by *which scheme is physical*, not by
any continuous parameter sliding through zero.

## Persona 5 -- Synthesizer (the controlled-vs-conditional map)

A conclusion is **CONTROLLED** iff it survives **all four** axes `{gauge, parametrization, regulator,
truncation}`. Applying that bar:

**CONTROLLED (survive gauge + parametrization + regulator + truncation; ported-with-proxy):**

1. **Reuter-FP existence** (matter-corrected, inside DEP).
2. **# relevant directions** = 3 `{g, lambda, f_0^2}` + 1 marginal `f_2^2`.
3. **`f_2^2*=0` structural Gaussian root** (also survives the scheme axis -- the strongest entry).
4. **`f_0^2` relevance** (`R^2` relevant -> de-forces `sign(f_0^2)`).

**CONTROLLED at sign level only:** RS `ker-Gamma` anti-screening **sign** (magnitude / projection open).

**STILL SCHEME / TRUNCATION-CONDITIONAL (the sole load-bearing residual):**

- **`sign(eta_C)` -> HORN K vs HORN Q.** Survives gauge + parametrization + regulator, but is **not** decided
  by them; the decider is the `Z_h` scheme (EH-adapted vs Weyl-adapted) and the named higher truncation
  (single self-consistent `Z_h` from the leading 4th-order kinetic term / BMS essential-scheme Weyl-coupling
  FP for GU's exact `ker-Gamma` `(N_S, N_D, N_V, N_RS)` content). The **HORN-K lean itself** (`eta_C = 0`
  physical) **survives gauge + parametrization** -- its structural support (universal `f_2^2*=0` root +
  gauge-independent Weyl one-loop AF) is untouched by `alpha` and the split choice.

**Verdict: `CONTROLLED-EXCEPT-ETAC`.** Four load-bearing FRG conclusions are now controlled across all four
axes (ported robustness, proxy-confirmed). The one open horn is `eta_C`'s sign, which is provably **not**
gauge- or parametrization-decidable and remains scheme/truncation-conditional -- exactly where W89 left it,
now with the additional, honestly-earned statement that gauge and parametrization **do not** move it.

---

## What changed vs the prior state (the genuine step)

- W85/W86 controlled the **regulator** axis. **This module adds the gauge and field-parametrization axes**
  for the load-bearing conclusions (computed proxy for existence + count; ported robustness for the rest),
  and adds the **`Z_h`-scheme structural facts** (`f_2^2*=0` universal; `sign(eta_C)` rides the scheme, not
  the positive threshold) as re-derived-in-code rather than asserted.
- It produces the first explicit **universal / non-universal ledger** and **uncertainty-range table** for the
  whole FRG line, and the first explicit **CONTROLLED-vs-conditional** partition against the four-axis bar.
- It pins the residual precisely: the horn is a **scheme/truncation** question, not a gauge/parametrization
  one. This narrows what the next paper-scale computation must actually do (compute `eta_h` from the leading
  4th-order kinetic term / BMS essential scheme), and rules out "just try another gauge/regulator" as a route
  to closing it.

## Residual (named, honest)

1. **The `eta_C` horn** -- the full off-diagonal `EH x Weyl` TT Hessian with a single self-consistent `Z_h`
   whose anomalous dimension is computed from the leading (4th-order) kinetic term. Scheme/truncation-decided.
2. **Combined-object full functional run** -- a full gauge + parametrization functional FRG of the combined
   `f(R)+Weyl^2 + ker-Gamma` spin-3/2 object (paper-scale) would upgrade the four CONTROLLED conclusions from
   "ported-with-proxy" to "computed." Not done here.
3. **RS magnitude / projection** -- only the sign is controlled.

## Deliverables

- This exploration: `explorations/obj4-uv-scheme-stability-2026-07-11.md`.
- Test: `tests/W101_obj4_scheme_stability.py` -- encodes the ledger, the `f_2^2*=0` and `eta_C`-scheme
  structural re-derivations, the gauge x parametrization invariance proxy, the uncertainty bands, and the
  CONTROLLED-vs-conditional partition. Deterministic, numpy-only, **exit 0** confirmed.

No canon / `RESEARCH-STATUS` / claim-status / verdict / public-posture / absorbed-source file is touched.
Not committed.
