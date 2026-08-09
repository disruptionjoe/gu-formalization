---
title: "Swing (NEGATIVE): the compact-core route to pi_! is closed — killed on degree, self-defeating anyway, and the serious obstruction is non-ellipticity not non-compactness"
artifact_type: exploration_result
created: 2026-08-09
status: ROUTE_CLOSED__COMPACT_CORE_SUBSTITUTION_FAILS_ON_DEGREE__WOULD_BE_3_FREE_REGARDLESS__REAL_BLOCKER_IS_NON_ELLIPTICITY__LIVE_ROUTE_HANDED_OVER_IS_THE_B_CALCULUS_INDICIAL_WINDOW
grade: "NEGATIVE RESULT / triage. No computation was run. Every kill quoted below was already in the
  repository before this swing; the contribution is consolidation plus one owed-sweep finding. Nothing here
  is new mathematics and nothing is resolved."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
follows:
  - canon/single-decider-integer-index-RESULTS.md
  - canon/no-go-class-relative-map.md
  - canon/h2-base-index-chirality.md
  - explorations/five-lens-analytic-council-2026-08-08.md
  - explorations/rational-triviality-lemma-result-2026-08-08.md
  - explorations/analytic-index-fredholm/n5-ind-h-analytic-conditions-2026-06-22.md
---

# The compact-core route to `pi_!` is closed

## What was proposed

The fiber `GL(4,R)/O(3,1)` deformation-retracts to `RP^3`, which is compact, orientable and
parallelizable. `GL(4,R)` retracts to `O(4)` and `O(3,1)` to `O(3) x O(1)`, so the bundle is
fiber-homotopy-equivalent to an `RP^3`-bundle, which admits a pushforward. Proposal: define `pi_!` there.

**It does not work, and it was already tried.**

## Kill 1 — degree mismatch (decisive)

> "The Bismut formula integrates a cohomology class over the *actual* fiber (the 10-manifold), not over the
> homotopy retract (the 3-manifold). The integral of a form over a 10-manifold requires a 10-form; the
> integral of a form over a 3-manifold requires a 3-form."

`pi_!` lowers degree by **10**; the `RP^3` pushforward lowers by **3**. **Different maps into different
groups.** Fiber-homotopy equivalence preserves cohomology; it does **not** preserve the integration map.
There is a standing correction in canon forbidding exactly this substitution — `RP^3` is the
deformation-retract **SPINE** of the metric fiber, and "the link of the non-compact end is `RP^3`" is
explicitly marked WRONG.

## Kill 2 — self-defeating even if it had worked

`H^even(F;Q) = Q`, concentrated in degree 0. **No vertical characteristic class of positive even degree
exists**, so fibre integration of `ch . A-hat` has nothing to integrate. Certified, with a firing negative
control on `CP^1` (where the index does move). The consequence is stated sharply:

> **"the fibre can multiply a base index; it can never create one."**

Consistent with `canon/h2-base-index-chirality.md`: the families index over the `RP^3` fiber is valued in
2-torsion `H^2(RP^3) = Z_2`, hence **3-free**. This is the dual of `canon/two-primary-lemma.md`: the lemma
says a 2-primary obstruction cannot **forbid** an odd count; the dual says a 2-primary index cannot
**supply** one. **Clearing this gate would close the route, not open it.**

## Kill 3 — the serious obstruction is not compactness at all

Four distinct obstructions are filed and have been treated as one:

| | obstruction |
|---|---|
| **A** | non-compact fiber ⇒ no compact vertical supports, no K-orientation |
| **B** | **NON-ELLIPTICITY** — `sigma(D_GU)(xi)^2 = g_Y(xi,xi) Id` in split signature; the symbol degenerates on the null cone |
| **C** | no Fredholm family at all |
| **D** | three GU-native absences filed as theorems: no invariant Riemannian fibre metric (the only invariant trace form is indefinite `(+7,-3)`); no invariant proper exhaustion (homogeneous ⇒ invariant scalars are constant); plus (B) |

> "The blocker is **not** non-compactness… **no** index theory applies to a non-elliptic operator. Callias
> does not rescue this; Callias assumes ellipticity."

**(B) is the one that matters, and no compactification touches it.** Any plan that attacks this gate by
making the fiber compact is attacking (A) while (B) stands.

## Owed sweep (the one actionable finding)

`canon/single-decider-integer-index-RESULTS.md:70` and `canon/no-go-class-relative-map.md:323` both say
`pi_!` fails because the fibre is **non-convex**. Two exploration files already correct this —

> "the reason given elsewhere for `pi_!` failing — 'the fibre is non-convex' — is also wrong: `pi_!` fails
> because the 10-dimensional fibre is **non-compact**, so fibre integration needs compact vertical supports."

— and **canon still carries the wrong phrasing with no correction banner.** `docs/y14-x4-systems-spec.md`
inherited it through v1.4 and is corrected in v1.5. The canon sweep is owed.

**Probable provenance.** "Non-convex" sits in the same file that asserts `Met(X^4)` is *contractible (convex
cone)* — the **Riemannian** fact under the Lorentzian name (filed as D8,
`explorations/canon-met-x4-contractibility-type-defect-2026-08-09.md`). Convexity is the running diagnostic
across that file. In the Riemannian case it genuinely does the work; the Lorentzian case fails, and the
failure was attributed to the property that *would* have carried the Riemannian argument rather than to the
one that actually blocks a pushforward. **One import, two symptoms.**

## Also retracted while checking this

The fiber-end result — limit-point / essentially self-adjoint, "the domain is UNIQUE and FORCED" — was
**REFUTED 2026-08-08**: `moduli dimension = 0` is false, the maximal stratum has real dimension **346,112**,
and "unique and forced" was the output of a **planted bounded-collar coefficient** where the true end model
blows up exponentially. A second gap is named alongside: **Bar-Ballmann does not cover ultrahyperbolic
signature.** So the analytic half is *worse* specified than before this swing, not better.

## The live route, handed over

Not the retract. The **b-calculus indicial-window decider**, currently unattempted:

```
Compute the index in Window 0 vs Window 1 on a cylindrical end -- a finite mechanical count.
  CONSTANT -> a well-defined index exists; GC-FC4 downgrades.
  JUMPS    -> the count is a property of the import, not of the geometry.
```

Estimated days. **Note the honest ceiling:** by Kill 2 this still lands 3-free, so it decides whether an
index *exists*, not whether it can be three. That is worth having and should not be oversold.

## What this swing is worth

It removes a route, consolidates four obstructions that were being counted as one, identifies the serious
one as **(B) non-ellipticity**, and surfaces an owed canon sweep. It resolves nothing and computes nothing.
The proposal that opened it was wrong, and it was wrong in a way the repository had already recorded twice —
which is itself the finding worth carrying: **before proposing a route here, grep the explorations.**
