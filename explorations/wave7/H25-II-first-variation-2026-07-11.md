---
title: "H25 — The |II|^2 first variation / C_RY: gravity's tree-level sign gate, decided CLEAR"
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 7
depends_on:
  - "tests/wave7/H25_II_first_variation_CRY.py"
  - "tests/wave6/H24_RY_normalization.py"
  - "tests/one-residual/willmore_curved_ambient_term.py"
  - "tests/threads/A_numerical_diffgeo_oracle.py"
  - "tests/wave3/H15_gravity_fork_R_term.py"
  - "explorations/wave6/H24-RY-normalization-2026-07-11.md"
  - "explorations/wave3/H15-gravity-fork-2026-07-11.md"
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
verdict: "CLEAR (sign-decided; magnitude normalization-gated). The residual tree-level EH-sign coefficient C_RY is COMPUTED POSITIVE by two independent methods (Gauss-ratio and direct |II|^2 second variation), OVERTURNING H24's hand-waved C_RY<0. m^2_eff = 1/2 + C_RY > 1/2 > 0: gravity's tree-level sign SURVIVES the curved-ambient R^Y correction. The wrong-sign antigravity KILL is excluded BY SIGN (not merely magnitude). Remaining gates: mu_DW absolute scale (H24 BAR 2), OQ2-A functional choice, loop [P,S]=0 — all unchanged. Confidence: HIGH on the sign/verdict (two independent methods + exact H15 flat-calibration match); MODERATE on the absolute magnitude (normalization-dependent)."
---

# H25 — The |II|^2 First Variation / C_RY

**Discipline.** Exploration-grade; compute → adversarially verify → honest grade. The
reproducible check is `tests/wave7/H25_II_first_variation_CRY.py` (exit 0, all PASS). No target
number imported. The one deliverable is **C_RY** — its sign, decisively — and hence the verdict on
`m^2_eff = 1/2 + C_RY`.

---

## The question H25 settles

H24 sharpened H16's curved-ambient EH-sign gate (BAR 3) to a **single number**: `C_RY`, the
coefficient of the slope-quadratic mixed `R^Y` kinetic term, in

```
m^2_eff = 1/2 + C_RY.
```

- **CLEAR** iff `C_RY > -1/2` (`m^2_eff > 0`): gravity's tree-level sign survives — real,
  non-tachyonic massive ghost; attractive massless graviton.
- **KILL** iff `C_RY < -1/2` (`m^2_eff < 0`): tachyonic/wrong-sign → the conformal/Stelle reading
  takes a real hit.

H24 **hand-waved** `C_RY < 0` ("mixed sectional < 0 → opposes attraction") but explicitly branded
it *"a flag, not a claim"* and **deferred** the actual `|II|^2` first variation as too heavy. H25
does that computation.

## What was computed (exact sympy, DIM=4 = the real Y14)

The model is the **full** faithful geometry — 4D base `X^4`, `Sym^2 = 10D` fiber, **14D** ambient
`Y^14 = Met(X^4)` with the gimmel/DeWitt metric — not a reduced-dimension proxy. The graviton is a
genuine transverse-traceless (TT) plane wave `h_{ab} = a·eps_{ab}·cos(k·x)`. Two **independent**
methods, deliberately chosen so a sign error in one would not propagate to the other.

### Method 1 — Gauss decomposition (convention-robust ratio)

`|II|^2 = |H|^2 - R^X + R^Y_tang`. The `s^1` (2-derivative, box) coefficient gets contributions from
`-R^X` (the induced Einstein-Hilbert, H15's `+1/2`) and from the slope-quadratic part of
`R^Y_tang` (which **is** `C_RY`). Both are computed on the same TT graviton via **one identical**
trace operation `ScalTang(R) = Σ η η R(i,j,j,i)` and the **same** Levi-Civita Riemann convention, so
their **ratio is convention-independent**:

- `R^X`: intrinsic scalar of `g = η + h`, `O(a^2)`, box (`t^2`) coefficient. (Verified `R^{(1)} = 0`
  on TT, matching H15.)
- `R^Y_tang`: the **ambient** gimmel Riemann contracted with the section tangent vectors
  `T_μ = ∂_μ + (∂_μ h)^fiber`, slope-quadratic `O(a^2)` box coefficient. (The pure-horizontal `s^0`
  Lambda is separated out at `t^0` — H24's leading branch-neutral piece, correctly excluded.)

```
r = (R^Y_tang box)/(R^X box) = -2/3   — IDENTICAL across 3 polarizations and spacelike/timelike k
C_RY = -(1/2) r = +1/3      m^2_eff = 1/2 + 1/3 = 5/6  > 0
```

The ratio `-2/3` is exactly stable over `{pol(1,2), pol(2,3), pol(1,3)} × {spacelike, timelike}` —
a strong Lorentz/rotation-consistency check.

### Method 2 — direct |II|^2 second variation (self-contained)

Build `B^V` directly from the `ii-s-coordinate-formula` sec 4 (graph Hessian − `Γ̄·∂g` − algebraic
slice term − slope-quadratic), the normal-lift inner product, and the DeWitt vertical metric `V`;
expand `|II|^2` to `O(a^2)`; read the `box^2` (`t^4`, from `|H|^2`) and `box` (`t^2`) coefficients.
With `s = box eigenvalue = -k·k`, the symbol is `P(s) = box2·s^2 + boxc·s`, so
`m^2_eff = boxc/box2 = -(k·k)·(t^2 coeff)/(t^4 coeff)`.

- **Calibration match (decisive).** The `-R^X`-dominant "crude" variant returns
  `m^2 = +1/2` **exactly**, reproducing H15's independently-derived flat-ambient value across all
  three configs — validating the direct machinery *and* the sign convention.
- **Full curved ambient:** `box^2 = +9` (positive Weyl, unchanged by `R^X/R^Y` as required),
  `m^2_eff = +5/4 > 0`, so `C_RY = +3/4 > 0`.

### The result

```
C_RY > 0  (POSITIVE)   — both methods.
m^2_eff = 1/2 + C_RY > 1/2 > 0   — both methods.
```

The curved-ambient `R^Y` correction **REINFORCES** attraction; it does **not** oppose it. This
**overturns** H24's hand-waved sign (which H24 itself flagged as provisional). The intuition H24
used ("sectional < 0 → opposes") conflated the sign of the sectional with the sign of the box
*coefficient*: the actual contraction runs the mixed `R^Y` through the indefinite horizontal trace
and compares it to `-R^X` (which is itself the source of the attractive `+1/2` via a chain of sign
flips). Done honestly, `R^Y_tang` lands on the **same** side as `-R^X`.

## Adversarial checks

- **Two independent methods agree in SIGN.** Method 1 (bare scalar-curvature ratio) and Method 2
  (full DeWitt vertical-norm `|II|^2`) are structurally different computations; both give `C_RY > 0`.
- **Exact H15 recovery.** Method 2's crude variant equals `+1/2` exactly in three configs — the
  machinery reproduces the known flat-ambient Einstein-Hilbert graviton mass, calibrating the sign.
- **Config-independence.** Method 1's ratio is exactly `-2/3` over 3 polarizations × 2 causal types;
  Method 2's full `m^2_eff` is exactly `+5/4` over the same. No accidental-degeneracy artifact.
- **Convention robustness.** The ambient `R^Y` uses the willmore non-doubled basis, but **every**
  polarization used is **diagonal-fiber** (`h_11, h_22, …`), where the doubled/non-doubled bases
  **agree** (A-oracle: diagonal sectional `-1/2` convention-robust). No off-diagonal `-5/8`-vs-`-1/8`
  artifact enters the number.
- **`s^0` Lambda correctly excluded.** The pure-horizontal `R^Y` sits at `t^0` (H24's 0-derivative
  branch-neutral Lambda) and is separated from the `t^2` box coefficient — re-verified here.
- **Weyl coefficient invariant.** `box^2` (`t^4`) is unchanged between flat and full (`R^X, R^Y`
  only touch `s^1`) — an internal consistency the direct method passes.

## VERDICT: CLEAR (sign-decided; magnitude normalization-gated)

| Bar | H24 status | H25 result |
|---|---|---|
| **3 — curved-ambient EH sign** | one residual number `C_RY` vs `-1/2`; sign *hand-waved* `<0`, magnitude gated | **`C_RY > 0` COMPUTED** (two independent methods). `m^2_eff = 1/2 + C_RY > 1/2 > 0`. **CLOSED in the CLEAR direction.** The KILL is excluded **by sign**, not merely by `|C_RY| < 1/2`. |

**Gravity's tree-level sign SURVIVES the curved ambient.** The wrong-sign antigravity KILL is not
realized — and cannot be, at this order, because `C_RY` has the wrong sign to ever produce a
tachyon. This is a **stronger** outcome than "sign-pinned, magnitude-gated": the sign itself
forecloses the kill.

### Honest caveats — what stays gated

- **Absolute `C_RY` magnitude is normalization-dependent** (`+1/3 → m^2_eff = 5/6` in Method 1;
  `+3/4 → m^2_eff = 5/4` in Method 2). The two methods weight the `R^Y` pieces differently (bare
  scalar-curvature ratio vs full DeWitt vertical-norm + normal-lift). **Only the SIGN (hence CLEAR)
  is claimed robust.** The absolute number ultimately needs the source-action normalization.
- **`mu_DW`'s dimensionful value is NOT derived** (H24 BAR 2 — the source-action overall scale;
  unchanged). With `C_RY > 0` and `m^2_eff > 0`, the natural `mu_DW ~ M_Pl` still gives a Planckian,
  decoupled ghost (SAFE), but the magnitude is smuggled, not derived.
- **The loop `[P,S]=0` is OUT OF SCOPE** (unchanged, generic-Stelle-shared).
- **OQ2-A** (`|II|^2` vs `|H|^2` functional choice) is unchanged — H25 assumes the II-class branch
  (the one that carries `-R^X`), consistent with H15's structural lean.

## RE-RANK signal

- **Does gravity upgrade to VIABLE?** **Yes on the tree-level geometry leg.** H25 **closes** H24's
  BAR 3 in the CLEAR direction: the last tree-level *sign* gate is decided, and decided favorably.
  Gravity moves from **CONTESTED (sharpened)** toward **VIABLE**, modulo only (i) the absolute scale
  `mu_DW` / OQ2-A normalization (source action) and (ii) the loop `[P,S]=0`. The tree-level *sign*
  is no longer a live risk.
- **Does H23 (the construction) become the only remaining gravity item?** **Effectively yes for the
  tree-level leg.** Every remaining tree-level gate (`mu_DW`, OQ2-A) collapses onto the **source
  action** — its overall normalization and functional choice. Gravity's tree-level verdict is now
  **one construction (the source action) away**, and the geometry no longer threatens a sign flip.
  The loop `[P,S]=0` remains the separate, harder, generic-Stelle-shared frontier.
- **Do H5/H19 rise?** **No.** The entropic/H5 route does not rise — gravity's sign survived, so the
  Stelle reading is *strengthened*, not weakened. H5/H19 stay where they were.
- **What should the next reflection focus on?** **The source action (H23-class construction).** It
  now has a single job for the tree-level leg: fix the overall normalization (`mu_DW`) and the OQ2-A
  functional choice. The *sign* question that gated everything is settled. Second priority remains
  the loop `[P,S]=0`, unchanged.

---

*Filed 2026-07-11. Wave 7. Reproducible: `python -u tests/wave7/H25_II_first_variation_CRY.py`
(exit 0). Exploration-grade; not promoted to canon. Overturns the provisional-and-flagged sign in
H24; the surviving H24 content (leading Lambda branch-neutral; `mu_DW` = source-action scale) is
unaffected.*
