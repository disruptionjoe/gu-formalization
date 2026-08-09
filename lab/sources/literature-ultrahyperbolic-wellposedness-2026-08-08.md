---
artifact_type: literature_note
created: 2026-08-08
subject: "Ultrahyperbolic well-posedness: what the standard theory does and does not give GU"
status: SUPPORTS_THE_ACTIVE_BUILD_PATH__CONFIRMS_M-S5_GAP_IS_REAL_AND_SEVERE
source_return: EXTERNAL_LITERATURE
---

# Ultrahyperbolic well-posedness — a literature note for the Build path

Written to support the active K77 Build line (Ward closure → `K_loc` formal
adjoint → Green identity → action Euler/Noether → presymplectic). **Every one of
those gates presupposes a domain on which the ambient operator is well-posed.**
This note reports what the literature actually provides for that, because the
repository has a filed premise gap here (`M-S5`, 2026-08-08) and the gap is real.

## The gap, confirmed

`M-H10` rests on "Bär–Ballmann does this generically." **Bär–Ballmann is a theory
of boundary value problems for Dirac-type operators in RIEMANNIAN and LORENTZIAN
settings.** A survey of the current well-posedness literature — Cauchy problems
for Dirac operators on globally hyperbolic manifolds, MIT and APS boundary
conditions, spatially non-compact Cauchy hypersurfaces — is uniformly about
**one time direction**.

**GU's ambient is not that.** `(7,7)` and `(9,5)` are ultrahyperbolic: many time
directions. The standard theory does not extend to it, and no amount of
"generically" bridges that.

## What IS known about ultrahyperbolic equations, and it is sharp

**Craig & Weinstein (arXiv:0812.0210, 2009), the load-bearing result:**

> The Cauchy problem for the ultrahyperbolic equation is **ill-posed in general**,
> but **well-posed on Sobolev spaces `H^m` if an explicit NONLOCAL CONSTRAINT is
> imposed on the Cauchy data.**

Two consequences the Build path should absorb:

1. **Ill-posedness is the default, not a pathology to be discovered later.** For
   an ultrahyperbolic operator, generic initial data does not give a
   well-posed evolution. Any GU construction that assumes a domain exists
   "as usual" is assuming something the literature says is false in this
   signature class.
2. **There is a known remedy, and it is NONLOCAL.** Well-posedness is recovered
   on codimension-one hypersurfaces under an explicit nonlocal constraint on the
   data. That is a *specific*, citable object — not a hope — and it is the
   natural thing for `U13`/`U14` to be compared against.

**And a second result that bounds the remedy:** the initial value problem on
**higher-codimension** hypersurfaces remains **ill-posed**, at least when
specifying finitely many derivatives of the data, through failure of uniqueness.
So the nonlocal-constraint rescue does not generalise freely.

## Why this matters to the specific gates now open

- **`U13`/`U14` (the domain question).** `C1` established the deck-fixed
  admissible set is a positive-dimensional moduli (max real dimension 346,112)
  with no canonical selector at filed symmetry. That is a *section-level*
  statement. The **ambient** question — deficiency indices for a first-order
  ultrahyperbolic operator on a non-compact 14-manifold — is the one this
  literature speaks to, and it says the default is ill-posed.
- **Green identity and formal adjoint.** A Green identity is an integration-by-
  parts statement on a domain. If the domain is not well-posed, the identity is
  formal in the pejorative sense.
- **Presymplectic reduction.** Covariant phase space presupposes a solution
  space. Ill-posedness undermines the object being reduced.

**None of this says the Build is wrong.** It says the Build should *declare*
which well-posedness it is assuming, and that "Bär–Ballmann generically" is not
available as that declaration.

## LAYER-0 WARNING — "Weinstein" is now a three-way homonym here

This repository's citation space now contains:

| who | what | relevance |
|---|---|---|
| **Eric Weinstein** | Geometric Unity, the author of the source | the whole programme |
| **Steven Weinstein** | *Multiple Time Dimensions* (arXiv:0812.3869); co-author of Craig & Weinstein above | ultrahyperbolic determinism |
| **Alan Weinstein** | symplectic geometry, Weinstein's creation-annihilation / symplectic category | presymplectic reduction, an active gate |

**All three are relevant to GU, and two of them to the same gate.** On 2026-08-08
this repository was found to have conflated "Curt/Eric" as one source in a
settled fork row, and that conflation let a mixed-notation sum survive four days.
The same failure with three Weinsteins would be worse, because all three are
citable and all three touch the Build path. **Cite by full name and year, never
by surname alone.**

## Method limit

Two targeted web searches. **Not a systematic review.** This note establishes
that (a) the standard Dirac boundary-value theory is Lorentzian, and (b) a
specific, citable ultrahyperbolic well-posedness result exists with a stated
constraint. It does **not** establish that Craig–Weinstein is the strongest or
most recent such result, and a Build step that leans on it should check that.

## Sources

- On determinism and well-posedness in multiple time dimensions (Craig &
  Weinstein): <https://arxiv.org/abs/0812.0210>
- Multiple Time Dimensions (S. Weinstein): <https://arxiv.org/pdf/0812.3869>
- The well-posedness of the Cauchy problem for the Dirac operator on globally
  hyperbolic manifolds with timelike boundary: <https://arxiv.org/pdf/1806.06544>
- On boundary value problems for Dirac type operators I (regularity and
  self-adjointness): <https://arxiv.org/pdf/math/9905181>
- Cauchy problem for the Dirac operator on spatially non-compact spacetimes:
  <https://arxiv.org/pdf/2409.17344>
