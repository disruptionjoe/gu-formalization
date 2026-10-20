---
artifact_type: literature_note
created: 2026-08-08
subject: "Ultrahyperbolic well-posedness: what the standard theory does and does not give GU"
status: SUPPORTS_THE_ACTIVE_BUILD_PATH__CONFIRMS_M-S5_GAP_IS_REAL_AND_SEVERE
source_return: EXTERNAL_LITERATURE
---

# Ultrahyperbolic well-posedness — a literature note for the Build path

Written to support the K77 Build line (Ward closure → `K_loc` formal adjoint →
Green identity → action Euler/Noether → presymplectic). A global analytic or
physical realization needs its operator/domain hypotheses checked; formal
identities and local algebra do not themselves require a completed global
well-posedness theorem. The recorded premise gap is `M-S5` (2026-08-08).

**Correction, 2026-10-20:** the original note conflated elliptic/Riemannian
boundary theory with Lorentzian evolution and overstated the transfer of a
scalar ultrahyperbolic result to every ambient system. This correction retains
the missing domain bridge, not a universal ill-posedness verdict. No GU source,
physics-ledger or canon status is changed.

## The gap, confirmed

`M-H10` relies on “Bär–Ballmann does this generically,” but the cited settings
must be separated:

- [Christian Bär and Werner Ballmann, 1101.1196](https://arxiv.org/abs/1101.1196)
  study first-order **elliptic** boundary problems with compact boundary and
  a specified principal-symbol symmetry.
- Their [Dirac boundary guide, 1307.3021](https://arxiv.org/abs/1307.3021)
  concerns complete **Riemannian** manifolds with compact boundary, including
  local elliptic and APS boundary conditions.
- Globally hyperbolic **Lorentzian** Cauchy theory concerns a different
  evolution problem. A boundary-condition name such as APS or MIT is not,
  by itself, a theorem fixing signature, operator or admissible domain.

None automatically supplies the proposed noncompact ambient `(7,7)`/`(9,5)`
realization. A transfer needs matching hypotheses or a justified reduction;
the label “Dirac-type” alone does not provide either.

## What IS known about ultrahyperbolic equations, and it is sharp

[Walter Craig and Steven Weinstein, 0812.0210](https://arxiv.org/abs/0812.0210)
analyze a specified linear ultrahyperbolic wave equation. For their
codimension-one problem, an explicit nonlocal restriction on Cauchy data yields
Sobolev well-posedness; unrestricted data do not inherit that guarantee. For
their higher-codimension problem, prescribing finitely many normal derivatives
still allows nonuniqueness.

This supplies both an obstruction example and a constructive constrained-data
example. It neither supplies GU's first-order domain nor proves that every
multi-time constrained system or observed reduction is ill-posed. Any proposed
use for `U13`/`U14` must identify the equation, data space and transfer map.

## Why this matters to the specific gates now open

- **`U13`/`U14` (the domain question).** `C1` established the deck-fixed
  admissible set is a positive-dimensional moduli (max real dimension 346,112)
  with no canonical selector at filed symmetry. That is a *section-level*
  statement. Deficiency indices for a chosen first-order ambient realization
  are a distinct operator/domain question, not answered by the scalar Cauchy
  theorem or by the section-level moduli count.
- **Green identity and formal adjoint.** A Green identity is an integration-by-
  parts statement on specified test fields or a domain. It can be valid before
  a well-posed evolution is proved; it does not establish that evolution.
- **Presymplectic reduction.** Covariant phase space presupposes a solution
  space. Its global analytic properties need separate justification; a local
  presymplectic calculation does not automatically supply them.

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

The original two targeted searches were **not a systematic review**. The
October 20 primary-source check corrects the theorem taxonomy and limits the
Craig–Steven Weinstein transfer to its stated model. It does not establish the
strongest or newest applicable result. Missing analytic input remains a
construction question, not a GU falsification or a bar to other research.

## Sources

- Boundary Value Problems for Elliptic Differential Operators of First Order
  (Christian Bär and Werner Ballmann): <https://arxiv.org/abs/1101.1196>
- Guide to Boundary Value Problems for Dirac-Type Operators (Christian Bär and
  Werner Ballmann): <https://arxiv.org/abs/1307.3021>
- On determinism and well-posedness in multiple time dimensions (Craig &
  Weinstein): <https://arxiv.org/abs/0812.0210>
- Multiple Time Dimensions (S. Weinstein): <https://arxiv.org/pdf/0812.3869>
- The well-posedness of the Cauchy problem for the Dirac operator on globally
  hyperbolic manifolds with timelike boundary: <https://arxiv.org/pdf/1806.06544>
- On boundary value problems for Dirac type operators I (regularity and
  self-adjointness): <https://arxiv.org/pdf/math/9905181>
- Cauchy problem for the Dirac operator on spatially non-compact spacetimes:
  <https://arxiv.org/pdf/2409.17344>
