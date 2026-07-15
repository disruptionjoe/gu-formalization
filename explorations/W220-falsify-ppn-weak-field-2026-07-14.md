---
artifact_type: exploration
status: exploration (FALSIFICATION WAVE, non-naive; LEG = weak-field / PPN gravity with matter; five personas inline, one worker, no sub-agents; deterministic test with Bianchi + linearized-Einstein + Schwarzschild positive controls and a Brans-Dicke teeth control, exit 0)
created: 2026-07-14
wave: W220
label: W220
note: "W219 was already taken (W219-native-good-stable-stabilizer-input-gate); this note takes the next free number W220."
posture: coherence-first (Joe 2026-07-14); exploration grade; truth-seeking (a pass hardens GU, a fail kills the leg; report either honestly); no rooting
leg: WEAK-FIELD, POST-NEWTONIAN (PPN) LIMIT WITH MATTER
method: "ASSUME GU IS CORRECT and GRANT every unbuilt piece (source action, completions) resolving exactly as GU hopes. Then find where GU is NEVERTHELESS WRONG. 'Unbuilt / incomplete / undetermined' is a GAP and does NOT count. Only a WRONG DEFINITE PREDICTION counts."
pre_declared_failure_condition: "GU is FALSIFIED on this leg IF its computed PPN parameters deviate from the measured solar-system values beyond the observational bounds: |gamma-1|>2.3e-5 (Cassini), |beta-1|>1e-4 (LLR/perihelion), or any preferred-frame / preferred-location / conservation parameter (xi, alpha1..3, zeta1..4) beyond its bound. GU SURVIVES (a real pass, not a gap) IF all parameters reduce to the GR values {gamma=beta=1, rest 0} within these bounds."
verdict: "SURVIVES. Granting the shiab-Einstein reduction R_mn-(s/2)g_mn=T_mn (s=R, so exactly G_mn=T_mn), GU's ten PPN parameters are gamma=1, beta=1, xi=alpha1=alpha2=alpha3=zeta1=zeta2=zeta3=zeta4=0 -- the FULL GR signature, zero deviation, within every solar-system bound. The pre-declared failure condition is NOT triggered. The Brans-Dicke negative control (w=100, |gamma-1|=9.8e-3) is correctly reported FALSIFIED, so the pass is not vacuous."
depends_on:
  - explorations/W161-lens-foundational-action-2026-07-14.md
  - canon/schwarzschild-weak-field-rfail.md
scripts:
  - tests/W220_falsify_ppn_weak_field.py
primary_source:
  - "Geometric_UnityDraftApril1st2021.pdf (E. Weinstein), sec 9.1-9.2 (shiab; 1st/2nd-order Bosonic action), eq 9.7-9.10 (reduction to S=T, R_mn-(s/2)g=T)"
external_refs:
  - "C. M. Will, 'The Confrontation between General Relativity and Experiment', Living Rev. Relativity 17 (2014) 4 -- PPN framework, the ten parameters, solar-system bounds"
  - "B. Bertotti, L. Iess, P. Tortora, Nature 425 (2003) 374 -- Cassini gamma: |gamma-1| < 2.3e-5"
  - "C. Brans, R. H. Dicke, Phys. Rev. 124 (1961) 925 -- scalar-tensor gravity, gamma=(1+w)/(2+w) (the teeth control)"
---

# W220 -- FALSIFY the weak-field / PPN leg of Geometric Unity (non-naive)

## 0. The leg, the method, and why it is non-naive

The falsification target is GU's **weak-field, post-Newtonian (PPN) limit in the presence of
matter**. The PPN framework (Will 2014) parametrizes the most general slow-motion, weak-field
metric of a "physically reasonable" gravity theory by ten dimensionless numbers -- gamma, beta,
xi, alpha1, alpha2, alpha3, zeta1, zeta2, zeta3, zeta4 -- each with a measured solar-system
bound. General Relativity predicts `gamma = beta = 1` and all eight others `= 0`, and every
one is confirmed to high precision.

This leg is **non-naive** precisely because the weak-field limit is computable from GU's
STRUCTURE without the full source action being finished. The council item ("PPN/solar-system
bar, needs no source action") names this. Per the method, I GRANT GU's gravity leg as it hopes
to have it:

- **The reduction (W161, from the April-2021 draft eq 9.7-9.10):** GU's linear-in-curvature,
  shiab-projected Bosonic action reduces to the **second-order Einstein equation**
  `R_mn - (s/2) g_mn = T_mn`, where the shiab is the gauge-covariant Ricci-minus-half-scalar
  projection that "annihilates the Weyl curvature" and `s` is the Ricci scalar. So the granted
  left-hand side is **exactly the Einstein tensor** `G_mn`, and the granted field equation is
  `G_mn = T_mn`.
- **No extra propagating gravitational mode (W161):** the covariant `R^2` coupling `c_R = 0` at
  the fundamental (linear-action) level -- **no scalaron**, tachyonic or otherwise. There is no
  extra long-range scalar in the X4 metric sector to mediate a fifth force.
- **Exact-Schwarzschild vacuum (H1/H21):** the Bach-flat / Ricci-flat vacuum solution of GU's
  reduced gravity is exactly Schwarzschild.

I then compute GU's ten PPN parameters WITH matter and confront the bounds. A GAP (the source
action, the shiab non-uniqueness, the eta-from-gimmel bridge) does NOT count; only a wrong
definite prediction would.

**Pre-declared failure condition (stated before the numbers).** GU is FALSIFIED on this leg IF
any computed PPN parameter deviates from the measured solar-system value beyond its bound:
`|gamma-1| > 2.3e-5` (Cassini), `|beta-1| > 1e-4` (LLR/perihelion), or any of
`xi, alpha1, alpha2, alpha3, zeta1..4` beyond its published bound. GU SURVIVES iff all ten
reduce to the GR values within bounds.

Five personas inline (GR/PPN-framework specialist; weak-field/post-Newtonian-expansion
specialist; solar-system-constraints specialist; shiab-reduction specialist; ruthless skeptic);
one worker, no sub-agents. Deterministic test `tests/W220_falsify_ppn_weak_field.py`,
positive controls first, exit 0.

## 1. The crux: a pure-metric conserved-source theory has GR's trace-reversal (persona 1 + 4)

The single load-bearing computation is that GU's granted reduction is not merely "Einstein-like"
but forced onto the exact Einstein trace-reversal, and PPN is a corollary.

Take the most general Lorentz-covariant, second-order, **pure-metric** field equation sourced by
a symmetric matter tensor:

```
a R_mn + b R g_mn = k T_mn.
```

Matter conservation `div T = 0` (which any minimally-coupled matter sector satisfies) requires
the LHS to be divergence-free. The contracted Bianchi identity `div^m R_mn = (1/2) grad_n R`
gives `div^m(a R_mn + b R g_mn) = (a/2 + b) grad_n R`, which vanishes for generic curvature
**iff** `b = -a/2`. So the LHS is forced proportional to the Einstein tensor `G_mn = R_mn -
(1/2) R g_mn` (test **PC1**). This is exactly GU's stated reduction `R_mn - (s/2) g_mn = T_mn`
with `s = R`. The trace-reversal coefficient is therefore pinned at the Einstein value `f = 1/2`
with no freedom.

**Why this is the whole ballgame for gamma.** gamma measures how much space-curvature a unit
rest mass produces -- equivalently the ratio of the spatial to the temporal metric potential.
Trace-reversing `R_mn = k[T_mn - f T g_mn]` for a static point mass (`T_00 = rho`, `T_ij = 0`,
`T = -rho`) and reading off the linearized harmonic-gauge Ricci `R_mn = -(1/2) laplacian(h_mn)`
gives, per diagonal component,

```
gamma = h_ij / h_00 = f / (1 - f).
```

At the Bianchi-forced `f = 1/2`: **gamma = 1** (test **PC2**). This is a real function of `f`,
not an assertion -- it returns `gamma != 1` the moment an extra field shifts `f` off `1/2`
(that is exactly the Brans-Dicke teeth control in section 3).

## 2. beta from the exact-Schwarzschild vacuum (persona 2)

gamma is a first-order (linear-in-mass) quantity; **beta is genuinely nonlinear** (order `U^2`),
so it needs the second-order structure, not just the linearized equation. Granting H1/H21 (the
GU vacuum is exact Schwarzschild), expand Schwarzschild in **isotropic** coordinates,

```
g_00 = -[(1 - M/2r)/(1 + M/2r)]^2,     g_ij = (1 + M/2r)^4 delta_ij,
```

to `O(U^2)` in `U = M/r` and match the standard PPN template `g_00 = -(1 - 2U + 2 beta U^2)`,
`g_ij = (1 + 2 gamma U) delta_ij`. The expansion gives `g_00 = -(1 - 2U + 2U^2 - ...)` and
`g_ij = (1 + 2U + ...) delta_ij`, hence **beta = 1** and **gamma = 1** (test **PC3**), the latter
an independent corroboration of PC2. The linear coefficient `+2` in `g_00` is the Newtonian
normalization (also checked), so the match is not a free rescaling.

## 3. The negative control: this test has teeth (persona 5 + 3)

A SURVIVES verdict is only meaningful if the same machinery can register a FAIL. Brans-Dicke
gravity has an EXTRA propagating scalar, which breaks the pure-metric Bianchi argument of section
1: the scalar carries part of the force, shifting the effective trace-reversal to `f_BD =
(1+w)/(3+2w) != 1/2` and giving `gamma_BD = (1+w)/(2+w)` (test **NC1a**), with the GR limit
`w -> infinity` recovered (**NC1b**). For `w = 100`, `gamma_BD = 0.99020`, so `|gamma-1| =
9.8e-3` -- roughly **400x** the Cassini bound. The confrontation routine correctly returns
**FALSIFIED** for Brans-Dicke `w=100` (**NC1c**). So the routine is not a rubber stamp: it flags
a real deviation when one exists. GU's pass below is therefore not vacuous.

The physical reading of the contrast is the crux of why GU passes: **GU's only extra structure
lives on Y14 / the observerse, not as an additional long-range field in the X4 metric sector.**
W161 already established there is no propagating scalaron (`c_R = 0`). A theory that adds no
propagating gravitational degree of freedom beyond the metric, and whose metric obeys `G_mn =
T_mn`, cannot shift `f` off `1/2`, so it cannot move gamma off 1. This is where the naive
expectation ("a big unified theory surely deforms gamma") fails: the deformation would need a
light extra mode coupled to matter, and GU's reduction has none.

## 4. The other eight parameters (persona 3 + 1)

The remaining PPN parameters test preferred-frame effects (`alpha1, alpha2`), preferred-location
/ Whitehead effects (`xi`), and violations of momentum/energy conservation (`alpha3, zeta1..4`).
Granting the reduction, each is structurally zero:

- **Conservation (`alpha3, zeta1..4 = 0`).** The Bianchi identity `div G = 0` combined with
  `G_mn = T_mn` forces `div T = 0`: GU's reduced gravity is a **fully conservative** theory. All
  five conservation-law parameters vanish (this is the standard PPN theorem for any theory
  derivable from an invariant action with a symmetric conserved source, which the granted
  reduction is).
- **Preferred frame (`alpha1 = alpha2 = 0`).** These require a dynamical long-range vector /
  preferred-frame field coupling to the metric. GU's granted X4 field equation is
  Lorentz-covariant Einstein with no such field; the observerse structure does not deposit a
  preferred timelike vector into the X4 metric sector. So both vanish.
- **Preferred location (`xi = 0`).** No long-range field whose local value would modulate
  gravity; `xi = 0`.

These are the GR values, and each has `0` deviation, within every bound (test block **GU**). They
rest on the granted reduction's Lorentz covariance and single-metric (pure-metric) character; if
a future genuine reduction were to leak a preferred vector from the observerse into X4, this is
the sub-leg where it would show up -- but that is a GAP in the granted object, not a computed
non-zero prediction, so it does not falsify.

## 5. The confrontation table (persona 3)

```
param     GU value   GR value    |dev|      bound      status
------------------------------------------------------------------
gamma       1.0000      1.0    0.000e+00   2.3e-05     WITHIN   (Cassini)
beta        1.0000      1.0    0.000e+00   1.0e-04     WITHIN   (LLR/perihelion)
xi          0.0000      0.0    0.000e+00   1.0e-03     WITHIN
alpha1      0.0000      0.0    0.000e+00   1.0e-04     WITHIN
alpha2      0.0000      0.0    0.000e+00   4.0e-07     WITHIN
alpha3      0.0000      0.0    0.000e+00   4.0e-20     WITHIN
zeta1       0.0000      0.0    0.000e+00   2.0e-02     WITHIN
zeta2       0.0000      0.0    0.000e+00   4.0e-05     WITHIN
zeta3       0.0000      0.0    0.000e+00   1.0e-08     WITHIN
zeta4       0.0000      0.0    0.000e+00   1.0e-02     WITHIN
```

Every parameter equals its GR value exactly; every deviation is `0`, hence within every bound
regardless of the bound's tightness.

## 6. VERDICT

**SURVIVES.** Granting GU's gravity leg -- the shiab-Einstein reduction `R_mn - (s/2) g_mn =
T_mn` (s = R, i.e. exactly `G_mn = T_mn`), no scalaron (W161), exact-Schwarzschild vacuum
(H1/H21), Lorentz-covariant single-metric X4 with a conserved source -- GU's ten PPN parameters
are

```
gamma = 1,  beta = 1,  xi = alpha1 = alpha2 = alpha3 = zeta1 = zeta2 = zeta3 = zeta4 = 0,
```

the **full GR PPN signature**, with zero deviation and within every solar-system bound. The
pre-declared failure condition (any parameter beyond its bound) is **NOT triggered**. The
Brans-Dicke negative control is correctly reported FALSIFIED, so this is a **real pass, not a
vacuous or gap-driven one**.

This is a genuine hardening of GU's gravity leg: **on the PPN sub-leg GU is observationally
indistinguishable from GR in the solar system**, and the naive kill ("a unified theory must
deform gamma or beta") is defeated by the structural fact that the granted reduction adds no
long-range mode to shift the trace-reversal.

## 7. Honest limits (persona 5)

- **This is granted-reduction PPN, not a fresh derivation from GU's own action.** The whole
  result is conditional on the granted objects: the reduction to `G_mn = T_mn` (W161, itself
  conditional on the shiab and the linear-action reading), no scalaron, and exact-Schwarzschild
  vacuum. The falsification method explicitly grants these; the honest content is "IF the
  gravity leg reduces as GU hopes, PPN does NOT falsify it." It is not "GU is derived to pass."
  This is the exact distinction the repo already flagged: `canon/schwarzschild-weak-field-rfail.md`
  re-downgraded an earlier "GU passes solar-system tests" headline because it was
  compatibility-on-an-imported-metric rather than a GU derivation. This note does NOT repeat that
  overclaim: the derivation is of the PPN parameters FROM the granted field-equation structure
  (Bianchi + linearization + the exact vacuum), and it is labelled granted throughout.
- **The one place a real deviation could still hide** is a preferred-frame vector leaking from
  the observerse into the X4 metric (alpha1, alpha2). Granting a Lorentz-covariant single-metric
  reduction closes it; a genuine reduction that produced such a vector would reopen it. That is a
  GAP in the granted object, not a computed non-zero prediction, so it does not falsify here --
  but it is the honest place to attack next if the granted reduction is ever built and turns out
  NOT to be single-metric.
- **No canon / verdict / posture change.** bar(b) and H59 stay OPEN. This is exploration grade;
  the reduction is treated as GIVEN per the method, not re-derived; nothing here asserts GU,
  asserts a vacuum, or flips a verdict. Zero em dashes in paper-facing text.

*Filed 2026-07-14 by the PPN falsification wave (W220). Leg: WEAK-FIELD / PPN GRAVITY WITH
MATTER. Five personas inline in one worker (GR/PPN-framework; post-Newtonian-expansion;
solar-system-constraints; shiab-reduction; ruthless skeptic); no sub-agents. Reproducible:
`python -u tests/W220_falsify_ppn_weak_field.py` (exit 0; Bianchi + linearized-Einstein +
Schwarzschild positive controls first, Brans-Dicke teeth control). Exploration grade;
truth-seeking; no canon movement. VERDICT: SURVIVES.*
