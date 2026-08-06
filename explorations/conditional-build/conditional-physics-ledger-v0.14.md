---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.14"
machine_source: lab/process/conditional-physics-ledger-v0.14.json
predecessor: lab/process/conditional-physics-ledger-v0.13.json
status: APPEND_ONLY_METRIC_SOLDERING_MOD_GAUGE_EXACT__MASSIVE_TT_PARTNER_SURVIVES_EVEN_BV__FINITE_TREE_KREIN_MAJORANT_POSITIVE__LOCAL_CURVATURE_VEV_TRACKING_EXACT__LOCAL_SCREENING_FAILS__ODD_UV_AND_AMBIENT_GLOBAL_HORNS_OPEN
---

# Conditional physics ledger v0.14

## Progress meter

```text
Ledger v0.14 — 82/82 active target rows mapped (100% of current denominator)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Metric -> gauge-rotated LC derivative: rank 10 modulo connection gauge
Massive partner: >=2 non-exact ordinary even-BV TT classes
Finite TT Krein grading: exact positive majorant for alpha_II > 0
Local curvature/VEV horn: two values controlled by one input
Independent vacuum shift: dR/d rho_vac = 2/a, so no local screening
Residue — 84 continuous real before quotient + >=19 function-valued
          + 9 open discrete forks
Quotients ranked: 3 scoped symbol/defect quotients; odd/global physics open
```

Coverage, verdict counts and global residue are unchanged. Eight row distances
moved. This is real progress because three previously open constructions now
have exact scoped answers, while the cosmology result also kills one tempting
local mechanism rather than disguising it as a success.

## Metric soldering now exists at the first required grade

For the gauge-rotated Levi-Civita connection,

```text
D_g B[h] = Ad_(epsilon^-1) D_g Gamma_LC[h] + D_B chi.
```

The flat symbol is a `64 x 10` map of rank ten on timelike, spacelike and
null covector representatives. Moving `epsilon` changes the derivative only
by the connection-gauge image. Thus the direct-plus-soldered stress/current
chain has an actual metric derivative modulo gauge on the linear observed
defect.

This is not a full nonlinear theorem on the ambient `Y^14` chimeric
connection. The odd super-IG complex and its cohomology remain unbuilt.

## The massive partner survives the ordinary even BV quotient

The null diffeomorphism image has rank four. The plus/cross TT carrier has
rank two and intersects that image trivially. Hence the massive coupled
eigenvector supplies at least two non-exact even-BV TT classes. Ordinary
diffeomorphism gauge does not erase the partner.

This lower bound does not yet decide the full massive multiplet or the odd
super-IG quotient. It does decide that `it is gauge` is no longer an available
answer at this grade.

## The finite Krein system has a canonical positive majorant

With

```text
K = [[alpha_II, 1], [1, 0]],
M = [[0, 0], [0, b]],
L = K^-1 M,
m^2 = alpha_II b,
b = (124/117) kappa_1,
```

the massless and massive eigenvectors have opposite Krein norms. The spectral
involution

```text
P = I + 2 L/m^2 = [[1, 2/alpha_II], [0, -1]]
```

satisfies `P^2=I`, `[P,L]=0` and `P^T K=KP`. Moreover `KP` has determinant
one and is positive for `alpha_II>0`. The partner therefore has an exact
finite tree-level keep-and-grade construction.

This is not loop stability, renormalization-group control, a type-III result,
or a uniform ultraviolet majorant.

## The local dark-energy horn tracks but does not screen

The smallest action-owned scalar horn using only existing coefficients is

```text
I_sc = integral sqrt(-g) [(a + beta theta) R
                          + kappa theta^2/2 - rho_vac].
```

For constant fields its equations give

```text
R     =  2 rho_vac/a,
theta = -2 beta rho_vac/(a kappa).
```

One input amplitude controls both field values. This passes Weinstein's
limited `two problems become one` parameter-count bar on its own terms. It
does not screen an independent vacuum shift:

```text
dR/d rho_vac = 2/a.
```

Eliminating `theta` gives the exact local trace equation

```text
a R + (3 beta^2/kappa) box R = 2 rho_vac.
```

On FLRW backgrounds, `R=6(Hdot+2H^2+k/a_FLRW^2)`. Spatial flatness `k=0`
therefore does not mean four-dimensional scalar curvature `R=0`; flat-slicing
de Sitter is the planted counterexample. The local static horn lies inside the
ordinary Weinberg burden. A genuinely ambient, global or nonlocal GU horn is
still open and is now the correct target.

## Row movements

| row | verdict/kind retained | distance now |
| --- | --- | --- |
| `LT-GR1` | `SAME/DERIVED_CONDITIONAL` | nonlinear ambient soldering and odd cohomology |
| `LT-GR2b` | `SAME/DERIVED_PARTIAL` | full multiplet, interactions and UV majorant |
| `LT-GR2c` | `NEEDS/MISSING_CONSTRUCTION` | ambient/global horn; local two-to-one is exact |
| `LT-GR2d` | `NEEDS/MISSING_CONSTRUCTION` | beat the exact local susceptibility `2/a` |
| `LT-GR2e` | `NEEDS/MISSING_CONSTRUCTION` | matter/radiation perturbations and held-out `w(z)` |
| `LT-GR3` | `DIFFERS/STRUCTURAL_DIFFERENCE` | odd interacting cohomology and UV control |
| `LT-GR5` | `DIFFERS/STRUCTURAL_DIFFERENCE` | nonlinear augmented-torsion spectrum |
| `LT-GR6` | `DIFFERS/STRUCTURAL_DIFFERENCE` | nonlinear chimeric metric/coframe derivative |

All other rows, external `P1/P2/P3`, canon, lane count and public posture remain
unchanged. The new quotient count is three only because the ordinary even-BV
TT quotient is now explicitly ranked; no global residue reduction is booked.

## Next gates

1. Extend the soldering derivative and positive majorant through the full odd
   super-IG interacting complex.
2. Construct the ambient/global or nonlocal curvature/VEV horn and rerun the
   independent vacuum-shift test.
3. Only after that horn survives, derive action-owned FLRW perturbations and
   held-out `w(z)`.

Evidence:

- `selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md`;
- `selected_branch_bv_tt_curvature_vev_flrw_probe.py`;
- `selected_branch_bv_tt_curvature_vev_flrw_independent.sage`;
- `selected-branch-bv-flrw-source-reinspection-2026-08-05.md`; and
- `2026-08-05-selected-branch-bv-flrw-review.md`.
