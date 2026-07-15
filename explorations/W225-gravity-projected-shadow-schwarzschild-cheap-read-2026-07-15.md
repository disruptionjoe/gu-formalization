---
artifact_type: exploration
label: W225
created: 2026-07-15
status: exploration (GRAVITY LEG, CHEAP HALF; imported exact Schwarzschild; surviving conservative IG branch; Psi=0 gravitational vacuum; personas inline, one worker, no sub-agents; deterministic sympy test with GR-shadow + Willmore positive controls that FIRE on real nonzero-residual falsifiers, exit 0)
posture: coherence-first (Joe 2026-07-14); exploration grade; adversarial, native-object first, truth-seeking (a clear hardens the gravity leg's cheap half, a nonzero linear falsifier would be an EARLY DISPROOF SIGNAL; report either honestly; no rooting)
title: "W225 -- Projected GR-shadow / section-equation residual on imported exact Schwarzschild (cheap half of GU's sole open physics leg)"
leg: GRAVITY -- ELProjectedGRShadowTheorem, imported-metric slice
grade: "GR-shadow proper G^X[Schw]=0 EXACT (sympy, all orders); native mean curvature H^(1)=(M/r)eta and its harmonicity Delta H^(1)=0 COMPUTED (sympy, exact); linear-in-M section residual of every BUILT term of R_s = 0 identically COMPUTED; leading built residual O(M^2/r^4)=Q(B) COMPUTED/SOURCE-AUDIT (reconciled with canon RFAIL-03); E_s^theta operator + coupling alpha_W OPEN (require branch-fixed source action, OQ2-A)"
depends_on:
  - canon/schwarzschild-weak-field-rfail.md
  - explorations/W220-falsify-ppn-weak-field-2026-07-14.md
  - tests/chase/MOVE-3/willmore_el_order.py
  - explorations/disproof-hunt-given-working-action-2026-07-11.md
scripts:
  - tests/W225_gravity_projected_shadow_schwarzschild.py
primary_source:
  - "Geometric_UnityDraftApril1st2021.pdf (E. Weinstein), sec 9 (Bosonic action, shiab, section equation)"
external_refs:
  - "R. M. Wald, General Relativity, U Chicago Press 1984, ch. 4 (Schwarzschild vacuum, Ricci-flat)"
  - "T. J. Willmore, Riemannian Geometry, OUP 1993 (Willmore energy, integral |H|^2, first variation Delta H)"
---

# W225 -- Projected GR-shadow residual on imported exact Schwarzschild (gravity, cheap half)

## Result in one paragraph

Running the BOUNDED CHEAP slice of GU's sole open physics leg on an IMPORTED exact
Schwarzschild solution, in the surviving conservative Inhomogeneous-Gauge (IG) branch, in a
`Psi = 0` gravitational vacuum: **every term of the projected section-equation residual
`R_s = alpha_W W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross` that is COMPUTABLE without the
branch-fixed source action has an IDENTICALLY ZERO linear-in-M residual, and the leading
built contribution is quadratic `O(M^2/r^4)` (the standing `Q(B)` genuine obstruction), which
is safe for `M/r << 1` and is NOT a definite nonzero linear falsifier.** Specifically: the
GR-shadow proper `G^X[g_Schw] = 0` exactly at all orders (sympy full Einstein tensor, though
this is trivial and carries no GU content -- true of any vacuum metric); the program-native
Willmore mean curvature is `H^(1)_ab = (M/r) eta_ab`, which is HARMONIC, so the linear-in-M
Willmore-EL residual `alpha_W W_s^(1) = Delta H^(1) = 0` identically for any finite coupling
`alpha_W`; and in the `Psi = 0` vacuum `E_s^Phi = E_s^cross = 0` exactly while `E_s^YM ~ F_A^2
~ O(M^2/r^4)` is quadratic (zero at linear order, F2 condition). The one term the imported
metric cannot settle is `E_s^theta`: the branch-fixed geometric-theta residual OPERATOR and
the coupling `alpha_W` require the SOURCE ACTION (OQ2-A), so its contribution is GRADED OPEN,
not computed nonzero -- a GAP, hence not a disproof. **VERDICT SIGNAL: the imported-metric
slice is CHEAP-HALF CLEAR at the computable (linear) order -- a genuine-YES SIGNAL for THIS
slice, with NO EARLY DISPROOF.** This does NOT clear the gravity leg (see limits). The
verdict is Joe-gated; canon `schwarzschild-weak-field-rfail.md` stays OPEN.

## Construction fork (stated, not defaulted)

Three GU objects have a native-vs-physics fork here; each is named per
`GEOMETER-VS-PHYSICS-OBJECTS.md`:

1. **Gravity functional -- PROGRAM-NATIVE `|II|^2`.** The section residual `W_s` is the Euler
   -Lagrange residual of the Willmore energy `E[s] = integral |II_s^H|^2` (second
   fundamental form of `X^4 -> Y^14`), NOT a free `R^2 / Weyl^2` Lagrangian. This is the
   construction the table settled toward the native side (row: Gravity functional), and it is
   the object whose linear residual `Delta H^(1)` I compute.
2. **The metric -- STANDARD-physics import, deliberately.** The exact Schwarzschild BASE
   metric `g` is IMPORTED as the vacuum solution. This is the physics-default construction,
   and using it is exactly what makes the slice "cheap" (no source action needed). The GU
   section lives in the fiber `Met(X^4)`; `H^(1)` is the mean curvature of the graph section
   into the fiber. I do not conflate the imported base metric with the gimmel/fiber
   metric-on-metrics (table row: The metric).
3. **Signature `(9,5)` vs `(7,7)` -- fork does NOT bite this slice.** The only datum that
   moves `p-q` is the base metric-sign convention, which is physically vacuous
   (`BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED`). Harmonicity `Delta(M/r) = 0` is
   convention-independent, so the cheap-slice verdict is IDENTICAL on both sides of the
   signature fork. I state this rather than silently defaulting: if a kill had appeared it
   would have had to be checked in the other signature, but no kill appears in either.

Because the load-bearing result (a vanishing linear residual by harmonicity) holds on the
native functional AND is convention-independent, there is no surviving construction in which
this slice produces a linear falsifier. That is the honest reason there is no EARLY DISPROOF.

## The residual, term by term (on imported Schwarzschild, Psi=0, IG branch)

`R_s = alpha_W W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross`.

| term | what it is | linear-in-M part | grade |
|---|---|---|---|
| `alpha_W W_s` | Willmore section EL residual (native `|II|^2`) | `alpha_W * Delta H^(1) = 0` (harmonic) | COMPUTED (sympy) |
| `E_s^YM` | gauge-curvature contribution `~ F_A^2` | `0` (`F_A ~ O(M^2)`, F2) | COMPUTED / SOURCE-AUDIT |
| `E_s^theta` | branch-fixed geometric-theta residual | **OPEN** (needs source action) | OPEN (GAP, not nonzero) |
| `E_s^Phi` | scalar/Higgs source | `0` (`Phi = 0` in vacuum) | EXACT (vacuum) |
| `E_s^cross` | cross terms | `0` (vanishing `Psi/Phi` factor) | EXACT (vacuum) |

Every BUILT term contributes zero at linear order. The leading BUILT contribution is
quadratic `O(M^2/r^4)` -- the standing `Q(B)` genuine obstruction from `W_s` -- which is safe
for `M/r << 1`. The single OPEN term `E_s^theta` is a GAP; under the falsification method a
GAP does not count as a falsification, and an OPEN operator cannot be a "computed nonzero"
disproof.

## Worked computation

**GR-shadow proper (C1).** The full mixed Einstein tensor `G^mu_nu` of exact Schwarzschild
(`f = 1 - 2M/rho`) is computed from the metric via Christoffel -> Ricci -> `G`, giving
`G^mu_nu = 0` in all four diagonal slots at all orders. This is the projected shadow's
Einstein part. It is TRIVIAL (canon warns: true for any vacuum metric, no GU content), so it
is not evidence for GU; it is included only because a nonzero here would be an immediate
inconsistency, and the positive control PC1 shows the detector is not blind to that.

**Native mean curvature and harmonicity (C2, C3).** In isotropic weak field `g = eta + h`,
`phi = M/r`, `h_00 = 2phi`, `h_ij = 2phi delta_ij`, the linearized vertical second
fundamental form of the graph section (literal-graph formula, `ii-s-coordinate-formula` sec
4/6.1, flat reference subtracted) gives the mean-curvature vector

```
H^(1)_ab = (M/r) eta_ab       (sympy: diag = [-M/r, M/r, M/r, M/r])
```

so `H^(1) ~ O(M/r)`, NOT `O(M/r^2)` (the retracted premise). Since `M/r` is harmonic
(`Delta(M/r) = 0`), the flat Willmore-EL leading operator vanishes on every component:

```
Delta H^(1)_ab = 0    (all a,b -- verified exactly)
```

Hence `alpha_W W_s` has NO linear-in-M term for any finite `alpha_W`. This reconfirms canon
RFAIL-03 (`tests/chase/MOVE-3/willmore_el_order.py`) and folds it into the full `R_s`
bookkeeping.

**Leading order (C4).** The curvature-level SFF `d_x d_x h_xx` is homogeneous of degree `-3`
in `(x,y,z)` (sympy scaling check), i.e. `~ M/r^3`; with the linear residual identically zero,
the leading assembled residual is quadratic `a = 2`, leading candidate `(algebraic ~ M/r) x
(Hessian ~ M/r^3) -> M^2/r^4`. Every `a=2` candidate exponent (`n in {4,6}`) is quadratic in
`M`, hence safe. This is the SAME object as the standing `Q(B)` obstruction.

**Vacuum matter/gauge terms (C5).** `Psi = 0` gravitational vacuum: `Phi = 0` so `E_s^Phi = 0`
exactly; every cross term carries a vanishing `Psi/Phi` factor so `E_s^cross = 0`; the gauge
curvature is sourced only through F2 with `F_A ~ O(M/r)^2`, so `E_s^YM ~ F_A^2 ~ O(M^2/r^4)` is
quadratic and zero at linear order.

**Positive controls (PC1, PC2) -- teeth.** PC1: Schwarzschild-de Sitter (`Lambda != 0`) returns
`G^t_t = -Lambda != 0`, an `M`-independent vacuum-Einstein violation -- the GR-shadow detector
FIRES on a non-Ricci-flat metric. PC2: feeding the RETRACTED wrong premise `H = (M/r^2) eta`
returns `Delta(M/r^2) = 2M/r^4 != 0`, a linear-in-M falsifier -- the Willmore linear-residual
detector FIRES when a real linear residual exists. Both controls fire, so the vanishing
results in C2/C3 are not blind spots.

## What this slice can and cannot settle (honest limits)

- **Can settle (imported-metric, computable):** there is NO linear-in-M falsifier from any
  built term of `R_s`; the GR-shadow's Einstein part vanishes exactly; the native Willmore
  linear residual vanishes by harmonicity; the leading built residual is quadratic and safe.
  Combined: **no EARLY DISPROOF** from the cheap slice, and a genuine-YES SIGNAL for THIS
  slice.
- **Cannot settle (needs the full ceiling):**
  1. A genuine YES for the gravity leg. `G^X = 0` is trivial (any vacuum), and `W_s` is
     nonzero at `O(M^2/r^4)`, so exact Schwarzschild is NOT an exact GU (Willmore-critical)
     section. "Cheap-half clear" is not "leg cleared."
  2. `E_s^theta` and the coupling `alpha_W`. These are defined by the branch-fixed SOURCE
     ACTION (OQ2-A), which is unbuilt. The imported metric fixes the geometric theta as a
     datum but not its residual operator. If, when built, `E_s^theta` produced a nonzero
     linear-in-M residual that no gauge transformation removes, THAT would be the disproof --
     this slice does not and cannot foreclose it.
  3. Kerr. Rotation breaks the static-isotropic harmonicity argument; the Kerr section
     residual is a separate computation (OQ2-A).

## Binding

Exploration grade. NO canon / RESEARCH-STATUS / verdict movement:
`canon/schwarzschild-weak-field-rfail.md` stays OPEN; the gravity-leg verdict is Joe-gated.
This note reports a genuine-YES SIGNAL for the imported-metric slice and explicitly does NOT
declare the leg verdict. No Lean/Lake build was run (Python/sympy only). Personas inline
(GR/curvature specialist; Willmore/immersion-variational specialist; IG-branch/theta
specialist; ruthless skeptic); one worker, no sub-agents. Reproducible:
`python -u tests/W225_gravity_projected_shadow_schwarzschild.py` (exit 0; GR-shadow and
Willmore positive controls FIRST, both fire on real falsifiers). Zero em dashes in
paper-facing text.

*Filed 2026-07-15 by the gravity cheap-read wave (W225). Leg: GRAVITY /
ELProjectedGRShadowTheorem, imported-metric slice. VERDICT SIGNAL: CHEAP-HALF CLEAR (no early
disproof); Joe-gated leg verdict untouched.*
