---
title: "K2552 Actual localized-source reduction to scalar domain problems"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact source-preserving sufficient scalar reduction and auxiliary radial splitter; remaining response inverses and physical domain open
scripts:
  - tests/channel-swings/k2552_localized_source_domain_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2552
carrier: actual radial-pressure source and original full selected-action fields on the curved seven-plus-seven product LAYER=toy CHIRALITY=N/A
pairing: indefinite tensor/test duality; positive auxiliary radial L2 only for the source decomposition ON=declared_carrier
real_structure: real kappa nonzero and product signature7,7; smooth even radial profiles and arbitrary B distributions where defined
grading: scalar and radial TT source pieces, shifted metric, original metric, displacement and auxiliary grade2 remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion of K2537
target: prescribed-source scalar-domain reduction, cancelling tails and compatibility demand MAP-TYPE=evaluation
```

# K2552 Reduce the actual prescribed source before choosing its domains

## Result and exact remaining debt

The conserved radial-pressure source of K2531, including its arbitrary
seven-dimensional second-factor dependence, admits an exact source-preserving
reduction to FOUR scalar response problems. The auxiliary radial splitter is
constructed with an explicit positive inverse and a quantitative norm bound.
The full tensor and scalar response formulas retain every selected-action row,
including the skew equation and the original-metric shift.

This removes the need to solve an undifferentiated301-component system for
this source class. It does NOT assert existence of the four remaining
indefinite-signature scalar inverses, select physical boundary data or prove
uniqueness. A nonzero operator determinant is not an inverse. The response
class retains the original observer homogeneity and normal SO(3) invariance;
all seven B coordinates, with both signature signs, remain unrestricted.
This is a sufficient construction, not a classification of all full solutions.

SC-ACT-01 ASSERTS its first-order action, SC-GEO-55 ASSERTS displacement from
gauge-rotated Levi-Civita, SC-GEO-03 ASSERTS Met(X), SC-META-53 remains
UNCERTAIN about indefinite spectra. The independent ambient metric and selected
comm/symi/symi completion are repository constructions. Ledger0.263
LT-GR6b/10/11/SM8, source polarities, canon and physical credit remain unchanged.

## 1. Keep the prescribed stress and solve the auxiliary radial split

On the stationary product A×B, each seven-dimensional factor has Ric=lambda G,

    K=lambda/6=35kappa²/3624192, kappa!=0,
    a0=-5kappa/2288, rE=1/(6a0).

Use the actual tube metric on A around the four-observer:

    G_A=dr²+S(r)² dOmega_2²+C(r)² gamma,
    S'=C, C'=-KS, C²+KS²=1,
    alpha=C'/C, beta=S'/S,
    X=Box_A on radial scalars=partial_r²+(4alpha+2beta)partial_r.

The original source is j=j_A rho(B), with eigenvalues A(r)/2 on four
observer directions and P(r)/2 on three normal directions, no B or mixed
components. Here P'+4alpha(P-A)=0 is the actual pressure conservation
condition. rho can be smooth or the original invariant point distribution;
response domains must support whichever is supplied. No replacement TT source
or tangential cutoff is introduced. For the compact-source tail statement below, require A (hence P,t) to be supported strictly inside R=1/|kappa|. Set t=tr_A j_A=(4A+3P)/2.

Define the conserved scalar tensor

    L_A*chi=Hess_A chi-G_A Xchi-lambda G_A chi,
    div_A L_A*chi=0, tr_A L_A*chi=-6Xchi-7lambda chi.

If (6X+7lambda)chi=-t, then

    j_A=L_A*chi+J_TT,
    tr_A J_TT=div_A J_TT=0.                           (1)

Because the source has no B index, multiplying either term by arbitrary
rho(B) preserves full product conservation. This is an equality of the same
prescribed tensor distribution.

The splitter is an actual construction. Put R=1/|kappa|, w_A=C^4 S² and
A_r=-w_A^-1(w_A partial_r)' with regularity at0 and Dirichlet value atR.
For x=sqrt(K)r, sin(x)/x>=1-x²/6 and cos²x>=1-x² on this small interval.
Thus

    w_A/r²=(sin x/x)² cos^4x >=1-(7/3)x²>1/2,
    w_A<=r², KR²=35/3624192.

For f(R)=0, weighted Cauchy--Schwarz gives
|f(r)|²<=(1/r-1/R) integral_r^R s²|f'|² ds.
Integrating against r² and bounding the inner integral by its full value gives
integral r²|f|²<=(R²/6)integral r²|f'|². The weight comparison then yields

    A_r>=3/R²=3kappa².

Its positive inverse is explicit:

    (A_r^-1 F)(r)=integral_r^R w_A(s)^-1
                            integral_0^s w_A(v)F(v)dv ds.    (2)

The regular center and zero outer value follow directly, and differentiating
checks the equation. The associated closed weighted radial Dirichlet form
therefore has this inverse. The energy bound and positive Neumann series give

    chi=(A_r-7K)^-1(t/6),
    ||chi||_w <= ||t||_w/[6(3kappa²-7K)],
    7K/(3kappa²)<1.                                  (3)

Smooth even input gives a smooth even solution at the center: in(2) the inner
integral is O(r³), its quotient by w_A is O(r), and the radial regular equation
can be iterated. These boundaries select the DECOMPOSITION, not physical
fourteen-dimensional response data.

## 2. Released tail and overlap constraints

For K2531's nonzero nonnegative compact A, the actual repaired P is nonnegative
because C'<0, so t>=0 and t is not zero. The kernel in(2) is strictly positive
in the interior against a nonzero nonnegative source. Equation(3) implies
chi>0 throughout0<=r<R, even outside supp(t). In particular no regular chi supported strictly
inside this tube can solve the splitter: it would also satisfy the above boundary problem
and contradict its unique positive solution.

The scalar SOURCE tensor has nonzero tails as well. If L_A*chi vanished on an
open annulus outside the source, its trace would give Xchi=-7Kchi and hence
Hess chi=-Kchi G_A. The observer/angular components then imply
alpha chi'=beta chi'. Since alpha-beta=-1/(SC) never vanishes there,
chi'=0 and Kchi=0, contradicting positivity. The scalar and TT source tails
therefore cancel exactly in(1). Truncating the two split sources to make each compact would change the
prescribed source.

There is also an overlap compatibility condition. A regular homogeneous
psi with (X+7K)psi=0 can be added to chi before choosing its outer condition.
Then L_A*psi is itself TT and the two components of(1) change by opposite
copies of that tensor. The induced original-metric response maps from the separately chosen scalar and TT operators
must agree on this overlap to give a decomposition-independent original
metric. Otherwise their difference is a full homogeneous response. This is
an exact matching obligation, not a proof that no matching domain exists.

## 3. Full radial TT realization, without a Codazzi restriction

Write the three invariant mixed eigenvalues in order observer4, radial1,
angular2. Every radial TT tensor is determined by its radial eigenvalue b:

    R(b)=diag(t_b,b,a_b),
    t_b=-SC b'/4-3b/4+7KS²b/4,
    a_b=SC b'/2+(1-7KS²/2)b.                         (4)

Indeed trace4t_b+b+2a_b=0 and the radial divergence is
b'+4alpha(b-t_b)+2beta(b-a_b)=0. Conversely these two equations solve for
t_b,a_b because alpha-beta=-1/(SC). Smooth even b gives b-a_b=O(r²), the
regularity condition at the center. For the actual splitter,

    b=P/2+(4alpha+2beta)chi'+lambda chi.              (5)

Equation(1) plus conservation proves J_TT=R(b), not just equality of traces.

The full rough Laplacian intertwines as

    Box_A R(b)=R(D5 b-14Kb),
    D5=partial_r²+(6alpha+4beta)partial_r.            (6)

For reproducibility, its observer, radial and angular eigenvalues before
substitution are respectively

    t_b''+(4alpha+2beta)t_b'+2alpha²(b-t_b),
    b''+(4alpha+2beta)b'-8alpha²(b-t_b)-4beta²(b-a_b),
    a_b''+(4alpha+2beta)a_b'+2beta²(b-a_b).

These follow from the warped connection; substituting(4) and C²+KS²=1 proves
all three rows of(6). D5 has radial weight C^6 S^4, distinct from the splitter's
C^4 S². This difference and the-14K term cannot be discarded as flat-space
notation. Multiplication by B-dependent scalar coefficients preserves the
intertwining and the TT constraints.

## 4. Two actual TT scalar response equations

For C supported in the AA block and TT_A, the complete selected operator
has tau=div C=0 and w=11(div C-dtau)+13div Kskew=0 with Kskew=0.
Riem C=-KC, so the K2539 hook and Einstein rows reduce to

    Hook(C)=2(Box-lambda-K)C,
    E(C)=-(Box-2K)C/2.

All skew, mixed and B equations vanish. Codazzi is NOT required. Reusing the
actual coefficients m=158kappa/143, mH=893kappa/858 gives

    L_Q C=[m-4(Box-7K)/mH-rE(Box-2K)]C
          =c[Box+mu-7K]C,
    c=970112/(13395kappa),
    mu=611557655kappa²/39953092608.

With Y=Box_B and(6), any valid common-domain solutions of

    (D5+Y-16K)v=rE b rho,
    c(D5+Y+mu-21K)u=-rE b rho                       (7)

give z_TT=R(v), Q_TT=R(u), satisfying E z_TT=-j_TT/(12a0)
and L_Q Q_TT=-rE j_TT. These are equations on r×B with all B signature modes,
not K2550's one-coordinate positive boundary realization.

## 5. The complete scalar complement

Use K2548's six-potential realization T(f,g,p,q,r,s), scalar operators X,Y,
full six-row polynomial matrix M and d=det M. Its proven identity is
L_Q T(q)=T(Mq), including the skew row. Here X acts on radial functions
in the first factor, while Y retains arbitrary second-factor dependence.
Set phi=chi rho and

    vsrc=(-X-lambda,0,1,0,0,0)^T,
    T(vsrc phi)=L_A*phi=j_scalar.

Define S0(w) by the potentials

    (f,g,p,q,r,s)=(X+5lambda/6,-X-7lambda/6,0,0,1,0)w.

Substitution into ALL five Einstein rows, with the curvature terms retained,
gives the exact identity

    E S0(w)=T[vsrc (X+Y+2lambda)w].                  (8)

Thus if the scalar-domain problems

    (X+Y+2lambda)w=phi, d(X,Y)U=phi                  (9)

have suitable solutions, then

    z_scalar=-S0(w)/(12a0),
    Q_scalar=-rE T[adj(M)vsrc U]                     (10)

answer their full equations. The universal cofactor identity M adj(M)=d I
over commuting scalar X,Y proves the second assertion; no coefficient-matrix
self-adjointness or injectivity of T is assumed. K2548's nonzero d(0,0)
proves d is not the zero polynomial, and proves nothing about its inverse.
The probe checks the new source/Einstein columns and exact cofactor fixtures;
the polynomial cofactor identity itself is the algebraic proof.

## 6. Compose back to the original fields

Whenever(7) and(9) hold on domains permitting the displayed derivatives and
products, require regular smooth-even radial extension at the center (possibly
with distributional B coefficients), or a separately proved distributional
extension for which the intertwinings hold across r=0 without extra center
sources. Solving only on the punctured tube is insufficient: singular radial
homogeneous amplitudes can introduce a delta flux at the center. For example,
q(r)=integral_r^R w_A(s)^-1 ds satisfies Xq=0 for r>0 but has w_A q'=-1,
a nonzero center flux under distributional extension. Then define

    z=z_TT+z_scalar, Q=Q_TT+Q_scalar,
    h=z-rE sym(Q), e2=-A2^-1 BQ.

K2535's grade-preserving auxiliary elimination and K2539's complete equations
then imply the original selected linear system with the SAME source j.
The other grades vanish at that inherited linearized scope. Source factors1/2,
the sign of rE and the original metric h must be retained. The shifted z is
not an observed-metric substitute. A finite gauge-invariant test can be paired
with h only when its resulting distribution and support permit it.

This is a sufficient four-scalar-domain construction plus the solved radial
splitter. It neither closes the nonlinear action nor proves a self-adjoint,
causal, positive or physical realization. It does not even assert that every
full solution has this invariant form. The remaining scalar domains must
accept the noncompact cancelling split, original B delta or justified smoothing,
and overlap compatibility. These are now explicit inputs to the next test.

## Verification and next condition

The probe checks original source trace/conservation algebra, all three radial
rough-Laplacian components, weight/gap constants, TT operator coefficients,
all five Einstein source rows and full six-row cofactor fixtures. Wrong radial
curvature, flat weights, missing source half, dropped skew equation and using
z as h are contrary controls. Universal radial inversion, tail positivity and
conditional reconstruction are the proofs above, not fixture counts.

Next construct a common right-inverse class for(7),(9) that accepts this actual
source and matches the overlap, or find a source-specific obstruction to that
precisely stated class. This is a much smaller explicit domain question than
the previous301-component problem; repeating contact cofactors or replacing
the source with a Codazzi eigenmode cannot answer it.

[Probe](../../tests/channel-swings/k2552_localized_source_domain_probe.py),
[report](../../lab/process/k2552-localized-source-domain.json),
[actual source](k2531-partial-thickness-source-2026-11-04.md),
[full scalar module](k2548-compact-coupled-metric-detectors-2026-11-04.md),
[restricted boundary comparison](k2550-common-domain-tensor-response-2026-11-04.md).
