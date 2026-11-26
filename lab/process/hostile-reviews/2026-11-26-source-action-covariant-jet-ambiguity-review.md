---
title: Review of covariant finite-section-jet ambiguity
status: process
doc_type: mathematical-review
created: '2026-11-26'
---

# Internal review: covariant finite-jet ambiguity

**Disposition: accepted at the declared local analytic column scope.** Two independent mathematical reviews and a hostile review checked the concrete proof and relevant operator/source custody. Required notation repairs were integrated and rechecked. This is internal review, not external-expert certification or a full Lean PDE proof.

[Result](../../../explorations/conditional-build/source-action-covariant-jet-ambiguity-2026-11-26.md) · [Finite certificate](../source-action-covariant-jet-ambiguity.json) · [Lean](../../../Lean/GUFormalization/CovariantJetAmbiguity.lean).

## Analysis / PDE review

Accepted the actual variable-coefficient CK recursion. The j-th trace-normal derivative has Q-differential order at most j. Analytic coefficient multiplication and base derivatives do not lower Q-ideal order; lower and moving-frame terms are retained. A seed of degree d therefore has every total normal derivative below d zero for all base spacetime. Restriction back to the seed surface proves exact first visibility.

The covariance proof uses invariance of the trace plane and scalar seed, the actual operator's naturality, the injection's intertwining property and CK uniqueness. It is an identity of local germs under the connected spin cover, not individual-field invariance or a common global boost-invariant box. Scaling regular diagonal points establishes analytic-composition injectivity, not merely polynomial independence.

Strongest controls: imposing the constant-seed image excludes all new witnesses; higher-normal-order equations can violate the filtration; complete infinite analytic normal jets restore uniqueness. Each is correctly outside the exclusion or explicitly preserved as a contrary case.

## Algebra / invariant-filtration review

Accepted the exact Jacobian determinant24192 and epsilon^6 scaling, the trace-invariant subspace and independence of history-valued finite sums. No indefinite diagonalization or full invariant-ring classification is used. The explicit CK-image kernel equals the sum of weighted-degree>N components because lower homogeneous seed components are detected on the seed surface and cannot cancel higher degrees.

The Hilbert coefficient formula, cumulative nested sum and unit-cube bounds are correct. H(N) counts copies of full history spaces in one explicit scalar seed subspace; it is not the full physical dimension or a particle count. The arbitrary analytic G refinement uses convergent analytic data and local image rank, not an unproved convergence of an arbitrary infinite sum.

Required notation correction: Q=S-rI is traceless identically, so `H={r=0}={tr Q=0}` was invalid shorthand. The final report says `H={S:tr S=0}`, identified with the traceless Q-space by S=Q on H. This was checked after correction; no mathematical calculation depended on the shorthand.

## Hostile / source and verification review

Accepted the scoped uniqueness exclusion. The strongest unproved link is the physical/source necessity of the unrestricted analytic column domain. Invisible analytic witnesses need not be physical states; a quotient can be legitimate and visible histories can still obey a selected law. No GU or class-C falsification, ghost result, hidden particle family or new physical completion is inferred.

The existing local gauge-identity lemma removes only unrestricted-parameter finite-order additive column gauge maps on the fixed background. Source BRST, nonlocal or constrained-parameter transformations and background-changing gauge remain outside. The report correctly reuses this lemma without counting it as a new gauge theorem.

The finite probe verifies native trace symbol and leading CK seams, invariant arithmetic and weighted counts. Its variable-coefficient scalar recurrence is explicitly a separate countercontrol, not a substitute for the full equation. The Lean layer formalizes affine-kernel and finite-polynomial algebra, not CK existence, physical domains or Lorentz naturality.

Wording repairs verified: Lorentz-covariant **families**, not invariant individual fields; connected spin-cover/germ action explicit; trace-plane notation corrected. SC-OP-05 now explicitly identifies the uncertain source southeast cell versus the repository SE=-1/2 repair. No remaining required revision.

## Verification and novelty ceiling

- 488 exact finite controls passed, including full15-slot trace symbol inversion, five observed injection slots through degree8, variable-coefficient recurrence and second-order mutation.
- Thirteen Lean theorems compiled without `sorry`: affine measurement-kernel characterization, arbitrary hidden parameter families, selected-right-inverse injectivity, even-polynomial coefficient isolation/independence and finite-cutoff vanishing.
- The written analytic proof remains a separate reviewed obligation.
- Prior repo coverage checked: initial finite-jet delayed visibility, q-only noncovariant whole-history kernel, and covariant constant-seed right inverse. The new theorem combines covariant all-history finite-normal-jet invisibility and exact weighted filtration.
- Novelty is new-to-repository/candidate application of classical tools. Bounded literature inspection does not certify worldwide priority.

**Final ceiling:** uniqueness of the bulk extension from covariance plus a fixed finite section calibration is ruled out in the unrestricted analytic column class. Physical admission, observed law, full gauge quotient, coupling and source identity remain undetermined. No ledger verdict changes.
