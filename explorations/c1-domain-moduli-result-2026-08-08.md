---
artifact_type: exploration_result
created: 2026-08-08
status: NO_CANONICAL_DOMAIN_SELECTOR_AT_FILED_SYMMETRY__MODULI_DIMENSION_346112__U13_U14_RECLASSIFIABLE
grade: "EXACT. tests/c1_domain_moduli_no_canonical_selector.py is green. The
  dimension count is integer arithmetic on a Grassmannian stratification; the
  supporting structural facts (graph classification, deck-fixed continuity) are
  checked numerically at small rank. Both INPUTS are filed elsewhere and are not
  re-derived here."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/five-lens-analytic-council-2026-08-08.md
---

# C1: the domain choice is a positive-dimensional moduli, not a bit

## Result

```text
deck-fixed admissible set at n = 832
  = disjoint union over k of Gr(k,832) = U(832)/(U(k) x U(832-k))
  dim_R Gr(k,832) = 2k(832-k)

  0-dimensional strata : k = 0 and k = 832 only -- the two definite sectors
  maximal stratum      : k = 416, dim_R = 346,112

VERDICT: NO-CANONICAL-SELECTOR__DOMAIN-MODULI-DIMENSION-346112
```

Canonicity would require the deck-fixed admissible set to be a **single point**.
It is not. And the only two isolated strata are precisely the definite sectors
that ECW3D-A already showed are **both** admissible and right-`H` invariant, so
even those do not select.

## Inputs, both filed, neither re-derived

- `inertia(B_n) = (832, 832, 0)` on the rank-1664 `ker Gamma` section trace —
  `explorations/eric-curt-wave3d-section-green-domain-2026-07-31.md:44`
- for `H = diag(I_n, -I_n)`, maximal `H`-isotropic trace spaces are exactly the
  graphs `L_U = {(x, Ux)}` with `U in U(n)`, and deck-fixing forces `U* = U`,
  `U^2 = I` — `tests/channel-swings/operator_domain_w1_bridge_audit.py`

The certificate re-checks both structurally at small rank rather than trusting
them: the graph of a random unitary is verified maximal isotropic at `n = 2,3,5`,
and the deck-fixed family `U(theta) = cos(theta) sigma_z + sin(theta) sigma_x` is
verified to be nine distinct, deck-fixed, maximal-isotropic points — a
**continuum, not a `Z/2`**. That rank-2 family embeds block-diagonally in every
`n >= 2`, which is why the conclusion is not an artefact of the large rank.

## What it answers

**Register `M-M23`, verbatim.** That row asks whether the `Z/2` orientation datum
is a `w1` obstruction or a choice in a connected Lagrangian Grassmannian. It is
the latter, and the Grassmannian's dimension is now computed.

**`U13`/`U14` are reclassifiable.** From "no domain yet" — which reads as an
unfinished construction — to:

> **the domain is a positive-dimensional extension moduli; the choice is
> irreducibly external; no canonical selector exists at filed symmetry.**

That is a different kind of statement. "No domain yet" invites more construction.
"Positive-dimensional moduli, choice external" says the construction is finished
and the answer is that a choice must be supplied. In standard BVP theory this is
the *expected* outcome — self-adjoint extensions are classified by unitaries
between deficiency subspaces and the choice is never canonical — so GU is not
anomalous here; it is normal, and the repository can stop treating it as a gap.

## What it does not show

- **"At filed symmetry" is load-bearing.** The result holds with Krein, right-`H`
  and deck. A **larger supplied symmetry group could shrink the fixed set**, and
  the deck action on trace data is itself one of the six fields recorded missing.
  So this is a closure at the stated grade, not a theorem about GU.
- It says nothing about `Y^14`. The `(832,832)` trace is the section-level object;
  the ambient question — deficiency indices of a first-order **ultrahyperbolic**
  operator on a non-compact `(9,5)` manifold — is not this computation, and is not
  standard. Note `M-H10` rests on "Bär-Ballmann does this generically", and
  **Bär-Ballmann does not cover ultrahyperbolic signature.** That gap is named
  nowhere in the repository and is now named here.
- It does not decide `U14`'s weight window. Lens 2's b-calculus indicial roots
  carve `delta` into windows and that remains the separate, days-long computation.

## Relation to what was already written

This quantifies rather than overturns. The source file's own §4 heading reads
*"Existence is cheap; canonical selection is not"*, and ECW3D-A already recorded
that the principal/Krein/right-`H` algebra does not select a unique boundary
sector. Three independent demonstrations existed; none was written as a closure
and none carried a number. **346,112 is the number.**

## Adjacent defect, unfixed here

`explorations/decision-tree-Q1a-fiber-end-classification-2026-07-21.md` still
asserts *"the domain is **unique and forced** ... Moduli dimension = 0"*. It was
refuted by hostile verify — the win planted bounded collar coefficients where the
true end model blows up exponentially — but it **carries no in-file correction
banner**, while every sibling retraction in that chain does. This result
contradicts it directly and with a computed number. Bannering it is owed and is
not done here.
