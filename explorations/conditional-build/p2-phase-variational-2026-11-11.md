---
title: Phase compatibility with differential and variational structure
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: P2xorder_locality
tier: T2
expected_delta: Derive nontrivial conditional requirements for the remaining P1/P2
  cells
actual_delta: P2 order_locality and variational constrained by full coefficient and
  pairing equations
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Phase compatibility with differential and variational structure

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P2xorder_locality
tier: T2
expected_delta: Conditional constraints for open matrix cells
actual_delta: P2 order_locality and variational constrained by full coefficient and pairing equations

```gu-typed-objects
result: Phase compatibility with differential and variational structure
carrier: smooth complex first-order source and target bundles, canonical RS only where explicitly named LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: fixed nondegenerate Hermitian density, possibly indefinite; independent-bar block separate ON=declared_carrier
real_structure: separately stated real or complex category; K77/K95 never silently identified
grading: coflip and scalar block multipliers are distinct; Grassmann signs not inferred
action_owner: N/A -- structural tests, no guessed action or class-C inhabitant
target: actual observation and declared analytic realization MAP-TYPE=restriction
```

## Layer 0 and source scope

The relevant native datum is P2, phase/orientation of the canonical vertical projected RS symbol on X, presently algebraic-candidate grade. The coflip phase below is an intertwiner phase; it is NOT automatically an overall kinetic-operator multiplier or an observed Weyl chirality. Total GU remains nonchiral; native 2+1 and literal observation contraction remain separate. No positive form, LC connection, source-selected action or physical quotient is assumed. The result is a structural conditional requirement for class-C subfamilies using the named first-order local maps. K77/K95 are separate typed instances. In particular scalar phase in complex multiplicity coordinates is not a new scalar primitive field.

Reusable evidence: x-p1-p2-class-c-lift-2026-11-11.md already separates weighted principal-coefficient existence from connectivity and separates action pairing from Krein K. x-p1-p2-multiplicity-weld-2026-11-11.md supplies the scalar-ratio conclusion only when the complete named diagram is preserved. x-p1-p2-projector-connection-2026-11-11.md supplies exact K95 residual beta*Omega and warns that covariance is not parallelism. K1126 already owns the first-order skew-coefficient correction. We extend these to complete first-order coflip equations and phase-derivative repairs, not rediscover their results.

## 1. Complete anti-linear differential intertwining criterion

Work in local frames with smooth finite-rank complex bundles. Let

 D = sum_mu A^mu partial_mu + B,
 D' = sum_mu A'^mu partial_mu + B',
 C u = U conjugate(u), U pointwise invertible.

Then CD=D'C on all compactly supported test sections iff

 U conjugate(A^mu) = A'^mu U                 (each mu),
 U conjugate(B) = sum_mu A'^mu partial_mu U + B'U.       (1)

Proof: expand both sides and compare independent first jets and values. This is a full differential criterion, not a principal-symbol test. The fixed source/target bundles, vector-covector convention, and connections determine the local coefficients. Smoothness suffices. Frame changes preserve the operator identity.

Suppose U0 solves (1) for fixed D,D'. Let U=pU0 with a smooth nonzero complex scalar p. Then its only residual is

 CD-D'C = -sigma_D'(dp) U0 conjugation.

Thus the complete intertwiner with the SAME lower-order terms exists precisely when sigma_D'(dp)=0. If xi -> sigma_D'(xi) is injective over the complex cotangent space, dp=0, so p is constant on each connected component. Unit p preserves a prescribed antilinear square when U0 defines an endomorphism coflip: (p C0)^2=|p|^2 C0^2. This does not establish existence of U0.

Here injectivity means the linear map covector→operator, not invertibility of the symbol matrix at every nonzero covector; null covectors remain allowed. The injectivity condition holds for the canonical projected geometric RS symbol in dimension n>2 with nondegenerate Clifford metric: the map from the complex vector representation is Spin-equivariant; its kernel is invariant, the vector representation is irreducible for n>=3, and the map is nonzero since its symbol is invertible at non-null covectors (already banked in tests/carrier-bit-decision/leg2_obstruction_hardening.md). Consequently the kernel is zero. For the vertical rank10 symbol the same argument uses its own nondegenerate vertical metric, not an identification of ambient and observed signatures. No assertion is made that every coupled class-C symbol is the canonical isolated RS pencil.

Conversely arbitrary nonzero p preserves first-order locality and intertwining after the unique change in B' with D and U=pU0 fixed:

 B'_p = B' - p^{-1} sigma_D'(dp).                         (2)

Invertibility of U makes the correction unique. This is a zero-order coefficient correction; it does not prove naturality, real-coefficient admissibility, action ownership, BV or source selection. A local phase branch theta with p=exp(i theta) gives correction -i sigma_D'(d theta), but (2) is global without choosing theta. For unit-modulus p its logarithmic derivative may have nonzero integral periods; one should not assert a global theta.

Exact contrary controls: D=D'=partial_x, U0=1. Every p satisfies the principal equation; p=exp(ix) fails the complete identity by -i exp(ix). D'_p=partial_x-i repairs it. D=partial_x on R^2 and p=p(y) supplies the noninjective-symbol control: dp can be nonzero while exact intertwining survives. Real p=exp(x) gives the real-coefficient correction -1 and demonstrates that locality alone does not lock scalar normalization.

Matrix wording: For a subfamily realizing P2 by an anti-linear first-order coflip, both principal equations and the lower-order derivative equation (1) must hold. A scalar ratio of complete coflips for a fixed injective covector symbol is locally constant; variable ratios require the precise zero-order correction (2), whose action/source admissibility is separate. Covariant connections and nonparallel arrows remain allowed by C.

## 2. Complete formal-adjoint and scalar-dressing classifier

This is a second, DIFFERENT type of phase test. Let H(x) be a smooth nondegenerate Hermitian density matrix, possibly indefinite. Compact support removes boundary terms; H includes the chosen integration density. Let formal H-adjoint be defined by integration by parts, and fix epsilon=+1 or -1. For L=A^mu partial_mu+B,

 L^sharp=epsilon L

iff

 (A^mu)^dagger H = -epsilon H A^mu,
 H B - epsilon B^dagger H = sum_mu partial_mu(H A^mu).    (3)

Proof: the density-dual formal adjoint is -A^dagger H partial + B^dagger H - partial(A^dagger H); compare to epsilon H L. In particular first-order coefficient adjoint sign is opposite the operator sign. This explicitly retains the K1126 correction.

Assume L obeys (3) and its principal symbol is nonzero at every point. Consider fL+Z with scalar f and zero-order Z. Its principal part has the SAME epsilon-adjoint type iff f is real, since conjugation in the adjoint yields (conjugate(f)-f) A^mu=0. No zero-order term can repair a non-real phase here. A unit-modulus f is therefore +/-1 and locally constant.

For every smooth real f the complete same-type dressing is exactly

 L_f = f L + 1/2 sigma_L(df) + R,    R^sharp=epsilon R,   (4)

where the adjoint on R is pointwise H-adjoint. All solutions differ by such R. Proof: (fL)^sharp=epsilon(fL+sigma(df)); sigma(df)^sharp=-epsilon sigma(df), so the half correction makes (4) have the required adjoint type. Conversely subtract it from any solution. If the zero-order term is held fixed at fB, formal adjointness requires sigma(df)=0; injective symbol then forces df=0. If H varies, equation (3), not coefficient transpose, carries the derivative of H.

Critical contrary control: these restrictions do NOT apply automatically to an independently barred kinetic block. Given ANY first-order L:E->F, the doubled block Hessian [[0,L^dagger],[L,0]] is formally selfadjoint relative to the direct density dual, whether or not L itself is selfadjoint or has the scalar-phase restriction above. This is the formal bilinear/independent-variable control already anticipated by the source, not a guessed C action. Graded Grassmann Hessians additionally require their actual parity conventions. Consequently reality of a full action never licenses applying (3) to a single native block without proving the block/pairing identification.

Exact controls: H=diag(1,-2), J=[[0,1],[-1,0]], A=H^{-1}J, B=0 gives epsilon=+1. For f=x, Z=0 fails; Z=A/2 passes. f=i fails at principal order for every Z. Using K=diag(1,-1) in place of H fails as in the existing weld note. For scalar L=i partial_x under H=1, an independent barred/doubled block remains formally selfadjoint even after arbitrary phase multiplication of its offdiagonal L. Keep pairing sign and coefficient i explicit.

Matrix wording: Any P2 phase claimed to follow from variationality must be checked on the actual density-dual block and grading. In a fixed nondegenerate Hermitian pairing and fixed epsilon-adjoint first-order block, the complete constraints are (3); scalar principal dressings are real, and variable dressings require (4). Independent-bar/coupled blocks do not inherit that scalar restriction without a proved pairing/block bridge. No identification of H with native Krein K follows from Helmholtz symmetry.

## 3. Useful next consumer

For the actual source-ingredient coupled symbols, identify whether P2 is implemented by scalar coflip ratio, an overall block multiplier, or a provenance-mixing map. Then substitute the fixed coefficients, actual action duals and connection terms into (1)/(3). This can reject a proposed P1/P2 weld without completing an early-universe action. It cannot decide all C because C does not yet force either restricted representation of P2.

## Evidence, acceptance and residual

Universal proofs above are separate from finite exact supporting/contrary controls in
[the probe](../../tests/program-focus/matrix_remaining_constraints_probe.py) and
[the report](../../lab/process/matrix-remaining-constraints.json). Independent internal
specialist review checks mathematics and source scope; this is not external review
or a Lean-certified class decision. RA-F1, AC-F1 and LT-SM8 remain NEEDS under physics
ledger0.263. Source register, class C, all canon and physical prediction grades are
unchanged. A constrained matrix entry records a useful necessary condition within
its explicit structural category; it does not establish that C inhabits that
category or settle all possible realizations.
