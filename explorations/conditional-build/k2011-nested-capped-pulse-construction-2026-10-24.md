---
title: "K2011: Finite capped moment programs and continuum pulse certificates"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2011_nested_capped_pulse_construction.py
  - tests/channel-swings/k2011_nested_capped_pulse_construction_probe.py
---

# K2011: Finite capped moment programs and continuum pulse certificates

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact-cell finite moment hierarchy, strong limit theorem and actual continuum dual/error certificates
carrier: K1974 actual optimal phase on width9 scalar strip LAYER=toy CHIRALITY=N/A
pairing: Lebesgue marginal moments and real L2 norm ON=actual_characteristic_strip
real_structure: real bounded measurable pulse and algebraic phase integrals
grading: nested row and column partitions, not source chirality
action_owner: repository-construction -- unchanged scalar transport problem
target: finite computable approximation and certified continuum norm bounds MAP-TYPE=intertwiner
```

## 1. Result, exact object and prior work

For D={-3<=u<=3, u<=z<=u+9}, M=23/100, and the ACTUAL K1974
optimal phase phi, the exact feasible pulse set is nonempty. K1980 already
constructs its unique minimum-norm element v_dagger by integral regularization.
This note does not claim first existence, first strong convergence or a closed
wing formula. It supplies a different **finite algebraic quadratic-program
hierarchy**, using exact slanted cell areas and integrated marginals, and proves
that its solutions converge strongly without requiring a cap-preserving
marginal inverse or a Slater point. The executed rational dual witnesses give

    2.3897489868 < ||v_dagger||_2^2 < 2.739952052817663.      (1)

This improves K2007's lower2.361527; its upper is reused unchanged. The
corresponding 96-row clipped witness w has exact cap and certified bounds

    ||row(w)-2phi||_1 < 0.192794705,
    ||column(w)||_1 < 0.050916625,
    ||w-v_dagger||_2^2 < 0.3502030661.                    (2)

These are full continuum integrated errors, not just errors at sample nodes.
They are not zero. No executed array is called a feasible pulse or exact QP
minimizer. The mathematical hierarchy uses exact algebraic forcing; the
reported arrays are floating-scouted, rationalized dual witnesses certified
independently of solver termination. No new Dirichlet phase-energy result or
GU realization follows. Layer0 uses the same independent scalar object.

## 2. Finite programs are exact relaxations, not pointwise collocation

For n=24*2^k use row bins on[-3,3] and column bins on[-3,12], both of width
h=6/n. Let C_ij=D intersect(I_i x J_j), A_ij=area(C_ij), and
G_i=2 integral_(I_i) phi. Omit zero-area cells. Define K_n in L2(D) by

    |v|<=M, integral_(I_i x R intersect D) v=G_i,
    integral_(R x J_j intersect D) v=0 for all i,j.       (3)

Every exactly feasible pulse lies in K_n. The set is closed, convex and
bounded, hence weakly compact, with a unique norm-minimizer v_n. Conditional
expectation on the cells preserves (3), the cap and all bin moments, and
cannot increase norm (Jensen). Equality of norm forces cell constancy.
Thus v_n is exactly the solution of the FINITE strictly convex QP

    minimize sum A_ij x_ij^2,
    sum_j A_ij x_ij=G_i, sum_i A_ij x_ij=0, |x_ij|<=M.   (4)

A_ij is rational and G_i algebraic from the pinned phase. There is no
nonlinear quadrature inside (4). Finite active-set enumeration over algebraic
numbers is a terminating exact method: enumerate free/bound coordinates,
solve the equality-constrained quadratic minimum on each face, and check
feasibility and objective. Redundant equalities can be removed by exact rank.
This establishes computability, not an efficient complexity bound or a claim
that the large exact active-set program was executed.

## 3. Strong convergence and a genuine nested lower hierarchy

K_(2n) is contained in K_n. It is the CONSTRAINT SETS in H that are nested;
the cell arrays of different sizes are not identified coordinatewise.
For m a finer dyadic grid, the projection variational inequality gives

    ||v_m-v_n||^2 <= ||v_m||^2-||v_n||^2.                (5)

The right-hand norms increase and are bounded by ||v_dagger||^2. Hence v_n
is Cauchy in H, with strong limit v. Any fixed bin constraint holds for all
sufficiently fine grids and passes to v. Nested step functions are dense in
the row and column L2 spaces, so vanishing all their marginal moments means
exact marginals almost everywhere. Marginal maps H->L2 are bounded by
Cauchy-Schwarz (row length9 and column length at most6). The cap set is closed.
Thus v is exactly feasible; minimality and uniqueness identify v=v_dagger.
Consequently ||v_n||^2 increases to ||v_dagger||^2.

This direct proof is an application of Hilbert projection and Jensen, not a
new general convergence theorem. It does not transfer monotonicity or the
error bound(5) to arbitrary inexact arrays. A small difference between two
successive numerical arrays is not a certified distance to the limit.

The standard finite polyhedral QP has primal-dual equality even if saturation
precludes strict box feasibility: at its minimizer the polyhedral normal cone
supplies equality multipliers and coordinate bound normals. This follows
by separating the linear tangent cone; no infinite-dimensional Slater
assumption is imported. Thus additive step potentials can approach the
continuum norm arbitrarily closely through these finite programs. This is
asymptotic completeness of the finite witness family, not attainment by one
bounded continuum dual potential.

## 4. Explicit mesh residual bounds, including inexact moment solutions

Let w be ANY cell-constant capped array. Let B_r and B_c be sums of absolute
row-bin and column-bin residual masses. Inside each row bin, row(w) is
Lipschitz with constant2M: only the two moving strip endpoints contribute.
The grid aligns all endpoints shifted by9. Likewise column(w) is Lipschitz
with constant2M within each column bin. The actual phase has
|phi'|<=21/20: its displayed polynomial pieces and0<lambda<7/100 prove this
bound, including the outer derivative1+lambda/2. Phase breaks are continuous.
For an L-Lipschitz function f on a bin of width h,

    integral |f| <= |integral f| + L h^2/3.              (6)

Indeed compare f with its bin average, integrate |f(x)-f(y)|<=L|x-y|,
and use the exact double integral h^3/3. Summing gives

    eta_r <= B_r+2h(2M+21/10),
    eta_c <= B_c+10Mh.                                 (7)

For the exact QP minimizers B_r=B_c=0; this is a computable O(h) marginal
modulus. It is not a modulus for strong H-distance. For executed witnesses
we further integrate the squared row and column residuals exactly. The row
residual is polynomial of degree at most2 after splitting at phase breaks;
its square has degree4. The column residual is affine. Cauchy-Schwarz gives
eta_r<=sqrt(6 integral e_r^2), eta_c<=sqrt(15 integral e_c^2).
The K1983 phase enclosure adds54*DG to the row L1 bound. Rational outward
square roots make(2) rigorous. Using rectangular areas at slanted boundary
cells would invalidate both the QP and its certificates.

## 5. Executed continuum consumer and validation boundaries

For row/column step potentials a,b put zeta=a+b and w=clip(zeta,-M,M).
With psi_M(z)=z^2 for|z|<=M and2M|z|-M^2 otherwise, exact integration gives

    D=2 sum a_i G_i - sum A_ij psi_M(a_i+b_j)
       <= ||v_dagger||^2,
    ||v_dagger-w||^2 <= U-D,                           (8)

where U=2.739952052817663 is the inherited strict feasible norm upper bound.
The second assertion uses pointwise strong Fenchel inequality and EXACT
marginals of v_dagger, not those of w. The forcing surrogate error is bounded
by18*DG*sum |a_i||I_i|, subtracted from D.

The 24,48,96-row exact certificates give lower bounds greater than
2.3494373102,2.3801535831,2.3897489868 respectively. The 96-row floating
optimizer reported unsuccessful line-search termination despite a small
numerical gradient. No conclusion depends on that flag or gradient: every
stored rational potential is re-integrated and checked exactly. The arrays
have nonzero continuum errors even when bin residuals are tiny. These facts
are preserved, not concealed by a success counter.

The producer uses trapezoid cell integration and coefficient polynomial
integration. The separate probe uses polygon clipping/shoelace areas and
exact Boole/Simpson integration, then corrupts actual geometry, cap, forcing
or normalization after a green baseline. Input hashes check provenance
separately. Same-author probes are not independent specialist acceptance.

Next: an effective error-to-limit modulus or a cap-preserving exact marginal
repair would turn the finite approximation into a quantitative primal
construction. K1980's integral method, K2005's local corner and K2007's
uncapped inverse remain distinct reusable results. No global capped wing
formula or exact finite feasible pulse is claimed. Source register, ledger
v0.263 and canon remain unchanged.

Executed: three witness replays; separate polygon/Boole probe30240 cell areas and full continuum residual integrals; four actual mathematical faults and four provenance hashes.
