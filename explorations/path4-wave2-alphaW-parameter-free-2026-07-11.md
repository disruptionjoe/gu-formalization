---
title: "Path4 wave2 -- is the DE x strong-gravity slope alpha_W(f_0) FORCED PARAMETER-FREE, or GATED on the unbuilt c_W / carrying beta/alpha? The decisive swing settling whether path4's one surviving invariant (the DE-mode / massive-spin-2 co-presence) is a QUANTITATIVE headline or stays QUALITATIVE. VERDICT: GATED (qualitative-only, honest terminus). alpha_W IS the OQ2-A/c_W coefficient; it is welded to f_0 by leading-order Schwarzschild consistency (a genuine shared-theta coupling that Branch A's block-diagonal Jacobian omitted) but that weld (i) IS the unbuilt c_W, (ii) carries beta/alpha, and (iii) terminates in an action coefficient, never reaching the f_0-blind / c_W-blind Yukawa observable. No shared-theta Ward identity pins it: the DE-EOS curvature vertex (lambda_N1) and the gravity-source matter vertex (D_A*F_A) are distinct operators of the one theta, so canonical normalization forces CO-PRESENCE, not a shared number. E's defeater 'show alpha_W is c_W-independent' is NOT met."
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 66
grade: "COMPUTED (deterministic, exit 0): that alpha_W is the c_W coefficient (needs the reconstruction-grade (R^Y.B)^TF input); that the O(M^1) II-class ambient term and the O(M^1) theta-source are the same order (the weld exists) and c_W = f0*K_theta/K_grav (symbolic); that the strong-field OBSERVABLE (Yukawa strength 1/3, range hbar_c/(sqrt(m2_eff) mu_DW)) carries NEITHER f_0 NOR c_W and d(lambda_Y)/d(f_0)=0 (symbolic); that alpha_Y=1/3 and c_L=3/8 are forced ratios while alpha_W is a relative weight between different tensor structures. ARGUED (structural): that the DE-EOS curvature vertex and the gravity-source matter vertex are DISTINCT theta-operators (the load-bearing assumption, = the wave20/H43 light-mode construction plus the Branch-3 source-law); that no DeWitt scale-covariance / Ward identity pins the relative weight; that the indirect beta/alpha-elimination route is gated three ways. Reconstruction-tier, internal. No canon promotion; no verdict/claim-status/RESEARCH-STATUS/posture change; no external action."
depends_on:
  - tests/W66_path4_wave2_alphaW.py
  - explorations/path4-branchA-eos-gravity-correlation-2026-07-11.md
  - explorations/path4-branchE-adversary-arguments-2026-07-11.md
  - explorations/path4-branchB-subtracted-curvature-2026-07-11.md
  - explorations/path4-wave1-synthesis-and-wave2-design-2026-07-11.md
  - tests/one-residual/willmore_el_alpha_w_pin.py
  - tests/one-residual/willmore_oq2a_functional_selection.py
  - tests/one-residual/source_action_intersection.py
  - explorations/wave35/source-action-carve-2026-07-11.md
scripts:
  - tests/W66_path4_wave2_alphaW.py
---

# Path4 wave2 -- is alpha_W(f_0) parameter-free?

Test: `tests/W66_path4_wave2_alphaW.py` (deterministic, no randomness, exit 0). Baselines
`W61` (Branch A) and `W65` (Branch E) both still exit 0.

## The question (the whole probe reduced to this)

Wave 1 established that path 4's one surviving forced-and-novel invariant is a **QUALITATIVE
co-presence**: because the DE scalar mode and the strong-field massive spin-2 are BOTH modes of
the one induced `|II|^2` action, no source-action family member can have a dynamical DE equation
of state without the massive spin-2 companion (LCDM has neither; single-sector scalar-tensor OR
pure-higher-derivative models have exactly one). This co-presence upgrades to a **QUANTITATIVE,
choice-independent, testable correlation -- a genuine headline** IF the coefficient coupling the
two sectors, the slope `alpha_W(f_0)`, is **FORCED PARAMETER-FREE** (independent of the unbuilt
`c_W` and the residual `beta/alpha`). If instead it is **GATED** on the unbuilt `c_W` / carries
`beta/alpha`, the co-presence stays qualitative and the honest H34/H53 accommodation register is
confirmed.

Two prior branches saw the coupling in tension:
- **Branch A (W61)** found the residual->observable map BLOCK-DIAGONAL: DE EOS `<- (lambda_N1,
  f_0)` (mu_DW-blind); Yukawa `<- (mu_DW, m2_eff)` (f_0-blind); masses ~30 orders apart; no scale
  cancels between the sectors -> argued NO quantitative correlation.
- **Branch E (W65)** located the coupling in the unbuilt `c_W` (OQ2-A) and named the defeater:
  "show the slope `alpha_W(f_0)` is `c_W`- and `beta/alpha`-independent."

## Construction used (fork rule, `GEOMETER-VS-PHYSICS-OBJECTS.md`)

- **Gravity functional = program-native induced `|II|^2`** (II-class). Its curved-ambient
  Willmore-EL carries an ambient-curvature term `~ R^Y . B` whose prefactor **is** `c_W` (the
  OQ2-A functional-choice datum, UNBUILT). Its TT spectrum is Stelle `box(box + m2^2)`: massless
  graviton + massive spin-2 of mass `m2 = sqrt(m2_eff) mu_DW`, strength `alpha_Y = 1/3`.
- **theta (DE sector) = program-native normal mode of `X^4 -> Y^14`.** EOS shape set by the
  CURVATURE-coupling eigenvalue `M^2 = lambda_{N,1}` (root number `{3,7,8,...}`) and amplitude
  `f_0` -- the wave20/H43 light-mode construction.
- **theta (gravity source) = the SAME field's MATTER/mass-response vertex** `D_A*F_A = theta ~
  M/rho^2` (Branch-3 source-law, `source_action_intersection.py`).
- **`mu_DW` = DeWitt/gimmel scale** (ratio-only, H24): free.

Five personas ran inline in one context (specialist computes; adversary attacks the emerging
verdict; referee grades; cross-checker; synthesizer). Combined result follows.

---

## 1. What `alpha_W` IS (definition; specialist)

On the `Psi=0` Schwarzschild section the II-class Willmore-EL leading-order stationarity is a
balance between the ambient-curvature term and the theta-source:

```
alpha_W * (R^Y . B)^TF_{mn}   +   S_{mn}(f_0)   =   0            [both O(M^1)]
```

with `(R^Y.B)^TF` the ambient partner (prefactor `= c_W`) and `S(f_0)` the theta-source
(amplitude `= f_0`). Solving,

```
alpha_W  =  - S(f_0) / (R^Y . B)^TF      ==>   alpha_W IS the c_W coefficient.
```

The pin test (`willmore_el_alpha_w_pin.py`) computes `Q^TF(B)` but states `alpha_W` "needs
exactly ONE further input -- the ambient term `(R^Y.B)^TF` ... still reconstruction-grade." So
**`alpha_W` is identified with the unbuilt `c_W`; it is not a computed pure number** (test P0).
The "slope `alpha_W(f_0)`" is the map DE-amplitude `f_0 -> ` strong-field deviation coefficient.

---

## 2. The shared-theta weld A missed (the real coupling -- and where it terminates)

Branch A's Jacobian was drawn over `(lambda_N1, f_0, mu_DW, m2_eff)` with `c_W` **held fixed**.
But the OQ2-A selection (`willmore_oq2a_functional_selection.py`) shows the II-class ambient term
`R^Y.B` is `O(M^1)` and the theta-source is `O(M^1)` -- the **same order** -- so a leading-order
Schwarzschild weld exists (test P1a). `source_action_intersection.py` states it outright: "`f_0`
and `alpha_W` are **LINKED by the cancellation, not independent**." The weld is

```
c_W * (R^Y.B) = f_0 * (theta-source)   ==>   c_W = f_0 * K_theta / K_grav      (test P1b)
```

with `K_grav, K_theta` computed geometric tensor numbers. **This is a genuine shared-theta
coupling that A's block-diagonal Jacobian did NOT include** -- A's "the sectors share no forcing
coupling" is too strong and is amended here.

BUT the weld relates two ACTION coefficients (`c_W` and the source coefficient), each carrying
reconstruction-grade geometry; it is **not** an observable<->observable relation (test P1c). The
decisive question is whether it reaches an observable.

---

## 3. Derivation 1 (DIRECT): the weld never reaches the strong-field observable

The strong-field OBSERVABLE is the massive-spin-2 Yukawa: strength `alpha_Y = 1/3` (forced,
scale-free), range `lambda_Y = hbar_c/(sqrt(m2_eff) mu_DW)`.

- `alpha_Y = 1/3` carries NEITHER `f_0` NOR `c_W` (test P2a).
- `lambda_Y` carries NO `f_0` and NO `c_W` (only `mu_DW`, `m2_eff`), so `d(lambda_Y)/d(f_0) = 0`
  at fixed `(mu_DW, m2_eff)` (tests P2b, P2c, symbolic). **The weld `c_W(f_0)` does not
  propagate to the observable.** A's block-diagonal OBSERVABLE conclusion STANDS.
- The only indirect route -- taking BOTH `c_W` and `m2_eff` as functions of the ONE residual
  `beta/alpha`, then eliminating `beta/alpha` to tie `f_0 <-> m2_eff` -- is gated **three ways**
  (test P2d): it (i) needs the UNBUILT function `c_W(beta/alpha)`, (ii) CARRIES `beta/alpha`, and
  (iii) still needs the FREE `mu_DW` to reach `lambda_Y`. Not parameter-free on any leg.

**Derivation 1 verdict: GATED.** `alpha_W` is the unbuilt `c_W`, carries `beta/alpha`, and never
reaches the `f_0`-blind / `c_W`-blind observable.

---

## 4. Derivation 2 (STRUCTURAL): no shared-theta Ward identity pins `alpha_W`

For `alpha_W` to be parameter-free it would need to be a forced RATIO of computed invariants,
like the framework's genuine parameter-free numbers:
- `alpha_Y = 1/3` (vDVZ, a representation-theory fact -- massless limit of massive spin-2),
- `c_L = 3/8` (DeWitt horizontal sectional curvature),

each fixed by geometry/representation theory with NO unbuilt input (test P3a). By contrast
`alpha_W = -Q^TF/(R^Y.B)` is a **relative weight between two DIFFERENT tensor structures**
(ambient `R^Y.B` vs intrinsic `Q^TF`). The DeWitt scale-covariance (H24, ratio-only) fixes SCALE
ratios; it does **not** constrain this cross-structure weight (test P3b). So no scaling symmetry
pins it.

**Adversary's strongest attack on this derivation:** "you missed the shared-theta Ward identity
-- canonical normalization of the ONE theta forces the ratio (DE coupling)/(gravity coupling)."
Tested and DEFEATED (test P3c): the DE EOS shape is set by the **curvature-coupling vertex**
(`M^2 = lambda_{N,1}`, theta<->R), while the gravity source is the **matter/mass-response
vertex** (`D_A*F_A = theta ~ M/rho^2`, theta<->stress). These are DIFFERENT operators of the same
field; their coefficients (`lambda_{N,1}` vs the source coupling) are INDEPENDENT data. Canonical
normalization of theta therefore forces **shared PRESENCE (co-presence)**, NOT a **shared NUMBER
(correlation)**. There is no Ward identity relating `lambda_{N,1}` to the source vertex.

**Derivation 2 verdict: GATED.** No symmetry/normalization forces `alpha_W` to a computed number;
the shared theta forces qualitative co-presence, not a quantitative slope.

---

## 5. Adversary's mirror attack on a hypothetical PARAMETER-FREE finding

Had a derivation returned parameter-free, the adversary's rebuttal is decisive: "you assumed a
normalization that is itself the unbuilt `c_W`." Concretely, any `alpha_W` value equals
`-Q^TF/(R^Y.B)^TF`, and `(R^Y.B)^TF` on the Schwarzschild section is the reconstruction-grade
ambient contraction the pin test flags as not-yet-built. So any claimed number would have
smuggled in the unbuilt datum. This attack is **not needed** here (both derivations return
GATED), but it confirms there is no back door to parameter-free.

---

## Graded verdict

| sub-question | grade | one line |
|---|---|---|
| **Is `alpha_W(f_0)` PARAMETER-FREE?** | **NO -- GATED** | `alpha_W` IS the unbuilt `c_W`; welded to `f_0` but the weld carries `beta/alpha` and terminates in an action coefficient, not an observable. |
| **Does E's defeater get met?** | **NO** | "show `alpha_W` is `c_W`-independent" fails -- `alpha_W` is definitionally the `c_W` coefficient. |
| **Does A's block-diagonal OBSERVABLE result survive?** | **YES** | `d(lambda_Y)/d(f_0) = 0`; the weld does not reach the Yukawa. A's conclusion stands; only A's completeness claim ("no shared coupling") is amended. |
| **Two-derivation agreement** | **AGREE** | direct (unbuilt `c_W`, carries `beta/alpha`, no observable reach) and structural (no Ward identity; two distinct theta-vertices) both return GATED. |

**VERDICT: GATED -- qualitative-only, the honest terminus. NOT a quantitative headline.**

**Confidence: HIGH.** The observable-blindness is exact and symbolic (`d lambda_Y/d f_0 = 0`);
the weld's existence and its termination in `c_W` are the repo's own results
(`source_action_intersection.py`, `willmore_oq2a_functional_selection.py`,
`willmore_el_alpha_w_pin.py`); the structural distinctness of the two theta-vertices is
well-supported (curvature-coupling vs matter-coupling are different operators). MEDIUM only on
the load-bearing assumption below, whose negation is itself unbuilt.

**Load-bearing assumption.** That the DE-EOS coupling (curvature vertex, `lambda_{N,1}`) and the
gravity-source coupling (matter/mass vertex, `D_A*F_A`) are INDEPENDENT vertices of the one theta
-- so canonical normalization forces co-presence, not a shared number. This is the same class as
Branch A's load-bearing light-mode assumption (wave20/H43). Its negation (a SINGLE theta-vertex
pinning both couplings) would itself require **building the OQ2-A source action AND exhibiting the
single-vertex normalization** -- currently unbuilt. So GATED is the honest default; a
PARAMETER-FREE outcome would be **CONDITIONAL-ON** that unbuilt single-vertex structure, which no
in-repo result supplies.

---

## Resolution of the A-vs-E tension (was A's block-diagonal analysis complete?)

**Both are right, at different levels -- and the synthesis is decisive.**
- **A's block-diagonal Jacobian was INCOMPLETE in one narrow sense:** drawn over
  `(lambda_N1, f_0, mu_DW, m2_eff)` with `c_W` held fixed, it omitted the `O(M^1)`
  Schwarzschild-consistency weld `c_W <-> f_0` that shares the theta object. So A's phrase "the
  sectors share NO forcing coupling" overstates: there IS one shared coupling.
- **But A's OBSERVABLE conclusion is COMPLETE and correct:** the shared coupling is a weld
  between an action coefficient (`c_W`) and `f_0`; it does not reach the `f_0`-blind / `c_W`-blind
  Yukawa observable, so no quantitative observable correlation exists. A's headline result holds.
- **E correctly located the coupling** in the unbuilt `c_W` and carrying `beta/alpha`. The weld A
  missed IS exactly E's gate. E's named defeater ("show `alpha_W` is `c_W`-independent") is NOT
  met -- indeed it cannot be, since `alpha_W` is definitionally the `c_W` coefficient.

Net: the one shared coupling A missed is real but is precisely the gated `c_W <-> f_0` weld E
located; it does not upgrade the co-presence to a quantitative observable correlation. **Path4's
honest headline is fixed: one surviving QUALITATIVE single-object tie (co-presence); no
quantitative parameter-free slope.**

---

## COMPUTED vs ARGUED ledger

- **COMPUTED (exact/symbolic):** `alpha_W` is the `c_W` coefficient (needs reconstruction-grade
  `(R^Y.B)^TF`); the `O(M^1)==O(M^1)` order-match giving the weld and `c_W = f_0 K_theta/K_grav`;
  `alpha_Y=1/3` and `lambda_Y` carry no `f_0`/`c_W`; `d lambda_Y/d f_0 = 0`; `alpha_Y=1/3`,
  `c_L=3/8` are forced rationals while `alpha_W` is a cross-structure weight.
- **ARGUED (structural):** the two-distinct-theta-vertices assumption (load-bearing); no
  DeWitt-covariance/Ward identity pins the relative weight; the three-way gating of the indirect
  `beta/alpha`-elimination route; the interpretation that the weld terminates in an action
  coefficient not an observable.

## Honest limits

1. `K_grav, K_theta` (the geometric tensor numbers in the weld) are reconstruction-grade -- the
   weld's EXISTENCE and its `f_0`-linkage are established (repo's own tests), but its numeric
   coefficient is not, which only reinforces GATED.
2. The load-bearing two-vertex assumption is not proven at the level of a built source action
   (that is the unbuilt OQ2-A object); its negation would itself require building that action.
3. This swing tests the COUPLING's parameter-freedom, not the construction of the source action.

## RE-RANK signal

**`alpha_W(f_0)` is GATED, not parameter-free.** It is the OQ2-A/`c_W` coefficient itself;
Schwarzschild consistency welds it to `f_0` (the shared-theta coupling A's block-diagonal Jacobian
omitted), but the weld carries `beta/alpha`, IS the unbuilt `c_W`, and never reaches the
`f_0`-blind / `c_W`-blind Yukawa observable -- so it produces no quantitative observable
correlation. No shared-theta Ward identity pins it (two distinct theta-vertices). Path4's one
surviving invariant stays QUALITATIVE (the DE-mode / massive-spin-2 co-presence); the H34/H53
accommodation register is confirmed. Do NOT re-spend effort seeking a parameter-free slope
between these sectors without first BUILDING the OQ2-A source action and exhibiting a single-vertex
theta normalization -- both currently unbuilt; only that would move the verdict to
CONDITIONAL-parameter-free.

---

*Filed 2026-07-11. Path4 wave2 decisive swing. Reproducible: `python -u
tests/W66_path4_wave2_alphaW.py` (exit 0); baselines `W61`, `W65` still exit 0. Exploration-grade;
not promoted to canon; no verdict/claim-status/RESEARCH-STATUS/posture change; tree left dirty (no
commit). Adversarially graded: the parameter-free hope was tested two independent ways and NOT
found; the shared coupling A missed was found, traced, and shown to be exactly E's gate; neither
outcome manufactured.*
