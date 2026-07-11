---
title: "H24 — The R^Y Normalization / mu_DW: settling H16's two collapsed viability bars (curved-ambient EH sign + ghost scale)"
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 6
depends_on:
  - "tests/wave6/H24_RY_normalization.py"
  - "tests/one-residual/willmore_curved_ambient_term.py"
  - "tests/threads/A_numerical_diffgeo_oracle.py"
  - "tests/wave5/H16_stelle_viability.py"
  - "tests/wave3/H15_gravity_fork_R_term.py"
  - "explorations/wave5/H16-stelle-viability-2026-07-11.md"
  - "explorations/wave3/H15-gravity-fork-2026-07-11.md"
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
verdict: "CONTESTED (sharpened) — the LEADING curved-ambient R^Y correction is a computed Lambda (branch-neutral, sign preserved); the residual EH-sign gate collapses to one number C_RY vs -1/2, requiring the unbuilt |II|^2 first variation; mu_DW is the source-action overall scale (dimensionless ratios geometric, magnitude smuggled). Gravity does NOT upgrade to VIABLE. Confidence: moderate-high on the split; the residual number is not computed."
---

# H24 — The R^Y Normalization / mu_DW

**Discipline.** Exploration-grade. Compute → adversarially verify → honest grade. The
reproducible check is `tests/wave6/H24_RY_normalization.py` (exit 0, 11 PASS). No target
number imported. Where a quantity is not computable without the source action (the residual
sign coefficient `C_RY`, the dimensionful `mu_DW`), it is fenced, not asserted. The loop
`[P,S]=0` is **out of scope**.

---

## The question H24 settles

H16 found **CONTESTED-CORNER**: the wrong-sign antigravity KILL is retired *in the flat
ambient*, and both live viability bars collapse onto ONE unbuilt input — the ambient DeWitt
`R^Y` normalization `mu_DW`:

- **BAR 3 (sign).** The Gauss `−R^X` gives attractive gravity in the flat ambient. The gate:
  does the curved-ambient correction `|II|² = |H|² − R^X + R^Y_tang` **flip** the effective
  Einstein-Hilbert (`R^X`) sign into a KILL?
- **BAR 2 (scale).** `m_ghost² = ½ μ_DW²`, safe iff `μ_DW ~ M_Pl`.

H24's job: compute the `R^Y` correction / `μ_DW` **as far as the gimmel geometry allows**, and
settle both bars **without the full source action**.

## What was computed (exact, reproducible)

The curved-ambient correction `R^Y_tang` is the ambient sectional curvature of the section's
tangent 2-planes. On a near-flat section (small vertical slope `∂g`) it splits into a **leading**
(zero-slope) piece and a **subleading** (slope-quadratic) piece. H24 computes both.

### (1a) LEADING piece — the pure-horizontal ambient curvature is a **Lambda** (branch-neutral)

The section's tangent planes at zero slope are the **horizontal** 2-planes `∂_μ ∧ ∂_ν`. Their
ambient sectional curvature — computed here for the first time — is

```
R^Y(∂_μ, ∂_ν, ∂_ν, ∂_μ) = a single CONSTANT, uniformly negative
    (non-doubled machinery: −3/16; oracle-authoritative honest doubled basis: −3/8; Krein-signed raw)
```

The decisive property is **not** the magnitude but that this curvature is **0-derivative in the
spacetime coordinate `x`**: the gimmel metric `G_{IJ}` and every Christoffel `Γ^A_{BC}` are
functions of the **fiber** coordinate `h_{ab}` only — they contain no base coordinate `x^μ`
(verified directly: `∂_x R^Y_horizontal = 0`). Restricted to the section `g(x)`, the
pure-horizontal `R^Y` is therefore a function of the field **value** `g(x)` carrying **no
spacetime derivative**. It enters the operator symbol at `s⁰` — a **cosmological-constant /
vacuum shift**, *exactly* like H15 Part D's DeWitt Lambda (`η^{ab} B_{mn,ab} = ½ η_{mn}`).

A `s⁰` term leaves the `s²` (Weyl) and `s¹` (Einstein-Hilbert) **kinetic** coefficients
**unchanged** (verified: adding `Λ` to `s(s+m²)` shifts only the `s⁰` coefficient). **Hence the
LEADING curved-ambient correction CANNOT flip the `R^X` sign.** This **retires H16's central
worry** — "a curved-ambient `R^Y` of opposite sign and larger magnitude could flip the effective
EH sign" — for the *dominant* correction: the dominant correction is branch-neutral by
construction, not by magnitude.

### (1b) SUBLEADING piece — the slope-quadratic mixed `R^Y` opposes attraction (**sign fixed, magnitude gated**)

`R^Y_tang` also has a slope-quadratic piece `R^Y_mixed · (∂g)²` (two vertical slope legs). Since
slope `= ∂g = ∂h` at the fluctuation level, this is a **2-derivative** quadratic-in-`h` term — the
**same order** as the `R^X` Einstein-Hilbert quadratic form on a TT graviton — so it **does**
enter the box (`s¹`) coefficient. Its **sign is computable**: the mixed sectional curvatures are
**negative** (`−1/2` diagonal, convention-robust; `−1/8` honest off-diagonal), and they enter the
energy as `+R^Y_tang`, so they contribute a **negative** box coefficient `C_RY < 0` — it
**opposes** the `+1/2` from `−R^X`. The effective mass² is

```
m²_eff = 1/2 + C_RY,   C_RY < 0.
```

The sign **flips** (massless graviton becomes the ghost → repulsive KILL) **iff `C_RY < −1/2`**.
The knife-edge `C_RY = −1/2` gives `m²_eff = 0` — precisely the **degenerate coincident-pole
(Branch B / pure-Bach)** case. So the residual gate is a **single sharp number**, not a vague
worry. The **magnitude** `|C_RY|` requires the full nonlinear `|II|²` first variation contracted
onto TT (H15 caveat 2 — the Simons + normal-bundle-curvature first variation, **not built**), so
whether `|C_RY|` crosses `1/2` is **not decidable here**.

*(A flag, not a claim: the flip threshold `−1/2` numerically equals the mixed **diagonal**
sectional curvature. If the first-variation contraction happened to project onto the diagonal
sector with unit weight, `m²_eff` would land exactly at the degenerate Branch-B edge. This is a
tantalizing coincidence to check when the first variation is built — it is **not** a result.)*

### (2) `μ_DW` — dimensionless ratios are geometric; the overall scale is **not**

The gimmel metric `G((u,k),(v,l)) = h(u,v) + V_h(k,l)` has the horizontal block `h` (the base
metric) and the vertical block `V_h` (trace-reversed Frobenius) each with relative coefficient 1.
The geometry is **scale-covariant**: rescaling `G → tG` leaves every sectional-curvature **ratio**
invariant. So the geometry **fixes all dimensionless invariants** — the `−1/2`, `−1/8`, `−3/8`
sectionals; the flat `m² = 1/2`; and the `C_RY`/threshold ratio — but **does not fix the single
overall dimensionful scale**.

That scale is genuinely dimensionful: the horizontal block `h` is a **metric** (`[length]²`),
while the vertical block `V_h = tr(h⁻¹k h⁻¹l) − …` is **dimensionless**. Joining them in one
metric requires a dimensionful conversion `μ_DW` — the DeWitt normalization — which the
scale-covariant geometry leaves free. **`μ_DW` is set by the source action's overall
normalization (unbuilt).** With `m_ghost² = m²_eff · μ_DW²`, the natural `μ_DW ~ M_Pl` (the
metric-on-metrics scale = the induced `R^X` Planck coefficient) gives a **Planckian ghost →
decouples → BAR 2 SAFE** — but that value is the **natural** one, **smuggled** rather than
derived. This exactly confirms and sharpens H16's BAR 2 read: *plausibly safe, magnitude gated*.

## Adversarial checks

- **Is the `R^Y` contraction the right one for the EH sign?** Yes, with the split made explicit:
  the EH sign is a **linearized-about-flat, 2-derivative** question, so only the pieces of
  `R^Y_tang` that reach `s¹` matter. The pure-horizontal piece is `s⁰` (verified 0-derivative) —
  correctly excluded from the sign. The slope-quadratic mixed piece is `s¹` (verified 2-derivative
  via `∂g = ∂h`) — correctly included. The Lambda-vs-kinetic separation is not assumed; it is the
  computed 0-derivative property.
- **Convention artifact caught.** This file's symbolic (non-doubled) machinery reproduces the
  known `−5/8` off-diagonal mixed sectional and `−3/16` horizontal sectional — the
  **mixed-convention artifacts** the A-oracle (`tests/threads/A_numerical_diffgeo_oracle.py`,
  the authority) corrects to the honest doubled-basis `−1/8` and `−3/8`. The test therefore
  asserts **only** convention-robust content: the diagonal `−1/2`, uniform negativity, Krein
  signs, constancy, and 0-derivative-ness. Every downstream conclusion rests on those, never on a
  convention-dependent magnitude.
- **Is `μ_DW` fixed by geometry or smuggled?** Smuggled as a **dimensionful** scale (source-action
  normalization); **fixed** only as **dimensionless ratios**. The "1/2" and the `C_RY`/threshold
  comparison are geometric and real; the `~ M_Pl` value is natural but not derived.

## VERDICT: CONTESTED (sharpened). Not CLEAR, not KILLED.

| Bar | H16 status | H24 result |
|---|---|---|
| **3 — curved-ambient EH sign** | PASS flat-ambient, gated on unbuilt `R^Y` | **LEADING `R^Y` = computed Lambda → branch-neutral → cannot flip the sign** (retires the "leading `R^Y` flips it" worry). Residual gate = **one number `C_RY` vs `−1/2`** (sign fixed: opposes attraction; magnitude needs the unbuilt `|II|²` first variation). |
| **2 — ghost scale** | plausibly SAFE, magnitude gated | **`μ_DW` = source-action overall scale**: dimensionless ratios (incl. the `1/2`) geometric; dimensionful magnitude not derived. Natural `μ_DW ~ M_Pl` → Planckian → SAFE, but smuggled. |

**Gravity does NOT upgrade to VIABLE.** It stays **CONTESTED**, now with a **precisely localized**
residual gate rather than a diffuse worry:

- **NOT killed.** The *dominant* curved-ambient correction is a computed constant (Lambda) and
  cannot flip the `R^X` sign. The wrong-sign antigravity KILL is **not realized** by the leading
  `R^Y` term. H16's single most valuable next computation — "does the curved-ambient `R^Y`
  overturn the sign?" — is answered *in the negative at leading order*.
- **NOT cleared.** The sign-relevant subleading slope-quadratic `R^Y` **opposes** attraction with a
  magnitude that requires the unbuilt `|II|²` first variation; and `μ_DW`'s dimensionful value
  (BAR 2) is the unbuilt source-action normalization. **Both bars remain gated on the same unbuilt
  object** — the source action (its overall normalization and its first variation).

### Honest caveats — what stays gated on the source action

- **The residual sign number `C_RY` is not computed.** Its *sign* (opposing attraction) and its
  *threshold* (`−1/2`, the Branch-B edge) are pinned; its *magnitude* is the full nonlinear
  `|II|²` first variation contracted onto TT — not built.
- **`μ_DW`'s dimensionful value is not derived** — only its dimensionless partners are.
- **The loop `[P,S]=0` was NOT in scope** and is untouched. It remains GU's long-standing missing
  ghost-parity-preserving source-action dynamics, identical to generic Stelle.
- **Convention.** Magnitudes from this file's symbolic machinery are non-doubled; the
  oracle-authoritative honest values are cited. Conclusions use only convention-robust content.

## RE-RANK signal

- **Does gravity upgrade to VIABLE?** **No.** H24 does not clear the branch. It **sharpens**
  H16's CONTESTED verdict: the curved-ambient sign gate splits into a **settled branch-neutral
  leading piece** and a **single residual number** (`C_RY` vs `−1/2`), and `μ_DW` is pinned as
  the source-action overall scale (ratios geometric, magnitude smuggled). The *risk profile*
  improves — the leading `R^Y` no longer threatens a flip — without a status upgrade.
- **Does H23 (the construction) become the only remaining gravity item?** **Effectively yes, for
  the tree-level geometry leg.** Every remaining tree-level gate — the residual `C_RY` magnitude
  (BAR 3), the `μ_DW` value (BAR 2), and the `|II|²`-vs-`|H|²` OQ2-A selection (H15/H18) —
  collapses onto **the source action**: its overall normalization sets `μ_DW`, its first variation
  sets `C_RY`, and its functional choice sets OQ2-A. The gravity leg is now **one construction
  (the source action) away** from a full tree-level verdict. (The loop `[P,S]=0` remains a
  separate, harder, generic-Stelle-shared frontier, unchanged.)
- **What should the next reflection focus on?** **The source action (H23-class construction), with
  the `|II|²` first variation as the specific deliverable.** It simultaneously (i) computes `C_RY`
  and closes BAR 3, (ii) fixes `μ_DW` and closes BAR 2, and (iii) selects OQ2-A and closes the
  H15/H18 fork. Second priority remains the loop `[P,S]=0`, unchanged and not resolvable without
  the action. The entropic/H5 route does not rise.

---

*Filed 2026-07-11. Wave 6. Reproducible: `python tests/wave6/H24_RY_normalization.py` (exit 0,
11 PASS). Exploration-grade; not promoted to canon.*
