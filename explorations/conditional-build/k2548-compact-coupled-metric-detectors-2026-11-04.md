---
title: "K2548 Compact coupled metric detectors for the full selected system"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: compact source-determined metric contact observations for all full solutions if they exist; no arbitrary-source existence, source-disjoint response, physical detector or native GU claim
scripts:
  - tests/channel-swings/k2548_compact_coupled_metric_detectors_probe.py
---

# K2548 Solve the coupled compact-adjoint condition

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
result: K2548
carrier: original ambient metric and full End(V) displacement on the stationary Einstein product; compact six-potential test fields LAYER=toy CHIRALITY=N/A
pairing: invariant distribution/test duality and inherited indefinite tensor contraction; auxiliary positive chart norm only for error bounds ON=declared_carrier
real_structure: real nonzero kappa; product signature (7,7); smooth local space forms and distributions
grading: symmetric metric, symmetric displacement, mixed skew displacement, shifted Einstein variable and scalar potentials remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion inherited from K2537
target: compact full-system adjoint cancellation and actual localized-source contact sensitivity MAP-TYPE=evaluation
```

## Result and boundary

[K2546](k2546-source-determined-metric-detectors-2026-11-04.md) left the
compact coupled-adjoint problem open after showing that its scalar Weyl
annihilation repair was impossible. A six-potential module on the ACTUAL
curved product closes the complete symmetric and skew displacement operator.
Its polynomial cofactor identity constructs compact adjoint fields that
cancel displacement from a metric observation. The resulting identity holds
for EVERY full solution, including solutions outside this module, whenever
the prescribed source admits such a solution. It uses no Green operator.

The class is nonempty: a full-chart parallel particular solution gives a
nonzero metric observation. More substantially, the actual conserved
radial-pressure source of K2531 has a nonzero contact functional in this
class. Its full-thickness approximations retain a nonzero fixed-detector
signal. These are on-shell necessary identities; they do not prove those
localized sources admit full solutions. All the constructed observations
vanish when detector support is disjoint from source support. A boundary-free
long-range gravitational response has therefore NOT been constructed.

SC-ACT-01 ASSERTS its first-order action; SC-GEO-55 ASSERTS displacement from
gauge-rotated Levi-Civita; SC-GEO-03 ASSERTS Met(X); SC-META-53 remains
UNCERTAIN about indefinite spectra. This independent ambient metric and
selected action completion remain conditional repository objects. Source
polarities and ledger0.263 LT-GR6b/10/11 are unchanged. No physical detector
coupling, positivity, native metric-on-metrics, prediction, external
certification or novelty claim follows.

## 1. Close an actual curved module, not a componentwise symbol

Let the seed be A×B, each a seven-dimensional space form with

    Ric=lambda G, lambda=35 kappa²/604032, Ksec=lambda/6,
    a0=-5 kappa/2288, m=158 kappa/143, beta=-15 kappa/143,
    m0=-4 kappa/11, mK=148 kappa/143,
    mV=503 kappa/858, mH=893 kappa/858, kappa!=0.

Use compact smooth scalar potentials (f,g,p,q,r,s) on a product coordinate
rectangle. Define the realization T by

    C_AA=f G_A+Hess_A p, C_BB=g G_B+Hess_B q,
    C_AB=C_BA=d_A d_B r,
    K_AB=d_A d_B s, K_BA=-d_A d_B s,
    Q=C+K.                                                   (1)

The mixed entries here are the actual tensor components; there is no hidden
factor1/2. Define X=Box_A and Y=Box_B on SCALARS, Z=X+Y. The scalar operators
X and Y commute because the connection and metric are a product. This does
not say that a tensor rough Laplacian commutes with Hessian. T is not asserted
injective, and these potentials do not exhaust all full-system fields.

Write

    tau=7f+7g+Xp+Yq,
    BA=f+(X+lambda)p+Yr, BB=g+(Y+lambda)q+Xr,
    VA=BA-tau, VB=BB-tau,
    WA=11VA-13Ys, WB=11VB+13Xs,
    U=XVA+YVB, V=XWA+YWB.                                    (2)

Then div C=(d_A BA,d_B BB), v=div C-dtau=(d_A VA,d_B VB),
div K=(-d_A Ys,d_B Xs), and w=11v+13div K=(d_A WA,d_B WB).
These follow by div Hess_A p=d_A Xp+lambda d_A p, the analogous B
identity, and the absence of mixed product connection terms.

In the five symmetric realization slots (G_A,G_B,Hess_A,Hess_B,mixed),
the tensor G divw-sym nabla w has coefficient vector

    Vstar=(V,V,-WA,-WB,-(WA+WB)/2).                            (3)

The hook divergence S from K2539 has vector

    S_f=2Zf-2Ksec Xp+2U/13,
    S_g=2Zg-2Ksec Yq+2U/13,
    S_p=2(Z+lambda+Ksec)p-2BA-2VA/13,
    S_q=2(Z+lambda+Ksec)q-2BB-2VB/13,
    S_r=2(Z+lambda)r-BA-BB-(VA+VB)/13.                        (4)

Here is the curvature calculation underlying (4). Reuse the full identity

    S=2Box C-2sym nabla(div C)-2lambda C+2Riem C
      +(2/13)(G divv-sym nabla v).

On the A Hessian column,

    Box Hess_A p=Hess_A[(Z+2lambda+2Ksec)p]-2Ksec G_A Xp,
    Riem(Hess_A p)=Ksec[G_A Xp-Hess_A p].

The B column is analogous. On the mixed column,
Box(d_A d_B r)=d_A d_B[(Z+2lambda)r] and Riem has no mixed
component. Volume columns have Riem(f G_A)=lambda f G_A and similarly
for B. Substituting these four identities gives (4), with the full product
Weyl contribution retained. Replacing the product by a14-dimensional space
form, or commuting Box through Hess without curvature, changes this matrix.

For R_C=delta R[C] and the actual cosmological Einstein linearization E,

    R_C=XBA+YBB-(Z+lambda)tau,
    E_f=-(Z/2+lambda)f-R_C/2,
    E_g=-(Z/2+lambda)g-R_C/2,
    E_p=BA-(Z/2+lambda)p-tau/2,
    E_q=BB-(Z/2+lambda)q-tau/2,
    E_r=(BA+BB-tau-(Z+2lambda)r)/2.                            (5)

This follows independently from

    E C=sym nabla(div C)-Box C/2-Hess(tau)/2-Riem C-G R_C/2.

As controls, (5) annihilates the two actual gradient diffeomorphism columns
(p,r)=(2chi,chi) and (q,r)=(2chi,chi), and its divergence vanishes. Restricting
to X=0,p=r=s=0 recovers all three K2541 coefficients, including its curved
Hessian column. Thus that earlier one-factor calculation is reused and
checked, not confused with this new full-support test class.

## 2. An explicit polynomial matrix with nonzero determinant

Define M(X,Y) by the following six output coefficients, in the same order as
the potentials in (1):

    first five rows:
      F=m(f,g,p,q,r)+beta tau(1,1,0,0,0)
        +11 Vstar/(13mV)-2S/mH+E/(3a0),
    sixth row:
      FK=mK s-(WB-WA)/(2mV).                                 (6)

Equations (2)--(6) are an explicit finite specification of every matrix
entry; all are polynomials in X,Y with fixed real rational coefficients in
kappa. The full K2539 equations prove the intertwining identity

    L_Q T(u)=T(Mu).                                          (7)

In particular the sixth row is not discarded. Dropping it for a generic
volume potential already leaves the nonzero coefficient
-11(VB-VA)/(2mV). The total alternation of the mixed skew field vanishes, but
closedness alone is weaker than its full equation.

Let d(X,Y)=det M(X,Y). To prove that this is not the zero polynomial, evaluate
at X=Y=0. The first two rows have zero entries in columns3--6. Their block
has eigenvalues m0+2lambda/a0 and m-lambda/(3a0). The remaining diagonal
entries are zeta,zeta,eta,mK, with no above-diagonal entries in that lower
4×4 block, where

    zeta=m-121lambda/(13mV)-14lambda/(39mH)
        =13614702109 kappa/12332658624,
    eta=m-4lambda/mH-lambda/(3a0)
        =20475967 kappa/18388656.

Consequently

    d0=d(0,0)
      =(m0+2lambda/a0)(m-lambda/(3a0))zeta² eta mK
      =-8051601064527887918824634287658165 kappa^6
        /12353477676102405846624738231189504 !=0.             (8)

The derivative realization is degenerate on constant potentials, but this
does not invalidate the polynomial identity or its nonzero determinant.
Neither injectivity of T nor a faithful symbol representation is needed in
(7). We never infer an inverse for L_Q from (8).

The matrix M is generally NOT self-adjoint in the Euclidean pairing on six
scalar coefficients. The realization has a differential Gram operator and
may be redundant. Formal self-adjointness below belongs to the actual field
operator L_Q from its action, not to the coefficient matrix.

## 3. Execute compact adjoint cancellation for all solutions

Let e_A=(1,0,0,0,0,0) and let e(X,Y) be the six coefficients of E(G_A phi):

    e=((5X+6Y+5lambda)/2,(6X+7Y+7lambda)/2,
       -5/2,-7/2,-3,0)^T.

Put b=adj(M)e. Cofactor expansion over the commutative ring of polynomials
in X,Y gives M b=d e identically. This elementary identity, together with
(7), is the universal proof; exact sample evaluations are merely arithmetic
controls. No division by d and no Fourier or Green inverse occur.

For ANY phi in C_c^infinity(A×B), set

    psi=G_A d(X,Y)phi,
    chi=-T(b(X,Y)phi)/(6a0).                                 (9)

Every component is smooth and compact inside supp(phi). Equation(7) gives

    L_Q chi=-P* E psi/(6a0),                                 (10)

where P projects Q to its symmetric lowered tensor. This is the explicit
coupled-adjoint problem left open by K2546. Both compact test fields can
have derivatives in BOTH factors, unlike an A-homogeneous field extended
from B.

For any full distributional solution of the selected system,

    E z=-j/(12a0), L_Q Q=-P*j/(6a0), h=z-PQ/(6a0),

formal self-adjointness and compact integration by parts give

    O_phi=<h,E psi>
         =-<j,psi/(12a0)+Pchi/(6a0)>.                        (11)

Indeed the Q coefficient in K2546's exact adjoint identity is
P*Epsi/(6a0)+L_Qchi, zero by (10). No ansatz has been imposed on the
solution h,Q or on the conserved source j. Restriction of the TEST fields
to a closed module is sufficient. This is how (11) applies to the actual
localized source without pretending that source belongs to the TT sector.

E annihilates infinitesimal diffeomorphisms at this stationary Einstein seed,
so O_phi is gauge invariant. Every distributional h can act on its compact
smooth covector Epsi. The equality is a necessary identity conditional on
existence, rather than a prediction for a source whose solvability is unknown.

## 4. A nonzero full-chart witness

Nonempty tests do not alone prove a nonempty source/solution pair. Use the
constant conserved source j=G_A on the whole product chart. For parallel
volume tensors the Einstein and tensor matrices are

    Ec=(lambda/2)[[5,7],[7,5]],
    Mc=m I+7beta [[1,1],[1,1]]+Ec/(3a0).

The explicit particular solution is

    z=-Ec^(-1)(1,0)^T/(12a0),
    C=(-16420976,-36052016)^T/(286675 kappa²), K=0,
    h=z-C/(6a0), e2=-A2^(-1)BQ=0.

Both constant matrices are invertible; this is finite algebra, not a
differential inverse. The full forced equations hold throughout the chart,
and other reduced grades remain zero as licensed by K2535. Directly,

    E h=(10192832,-652288)^T/(286675 kappa).                   (12)

For a compact phi with nonzero invariant-volume integral,

    O_phi=7[10192832/(286675 kappa)]d0 integral(phi) !=0.      (13)

Here integral Xphi=integral Yphi=0, so integral dphi=d0 integral(phi).
The factor7 is tr_A G_A; it is independent of metric signature. This is an
actual original-metric readout; substituting the shifted z changes (12).
The source is constant, not compact; all integrations are legitimate because
the detector is compact. This witness does not claim localized-source
existence or physical detector realizability.

## 5. Follow through to the actual radial-pressure source

Use K2531's conserved first-factor stress, including its required normal
pressure, and K2543's conventions:

    j=j_A tensor rho_B, div_A j_A=0,
    t_A=tr_A j_A=(4A_epsilon+3P_epsilon)/2,
    rho_B=delta_q for partial thickness,
    P'+4(Cwarp'/Cwarp)(P-A)=0.

All B and mixed tensor components of j vanish. In the source pairing in
(11), the only additional A component beyond a volume multiple is a partial
A Hessian. Its pairing vanishes by div_A j_A=0 and compact integration by
parts, including B-dependent tests. Thus define the EXPLICIT polynomial

    F(X,Y)=d(X,Y)/(12a0)-b_f(X,Y)/(36a0²).                    (14)

The actual-source observation is exactly

    O_phi=-<t_A rho_B,F(X,Y)phi>
         =-<F(X,Y)(t_A rho_B),phi>.                          (15)

The final equality uses formal self-adjointness of scalar X,Y. It does not
assert formal self-adjointness of M. The sign and the original shift are
independently tested on (12):

    F(0,0)=-[10192832/(286675 kappa)]d0 !=0.                  (16)

Therefore F is a nonzero polynomial. Constant-source nontriviality alone
would not prove that (15) detects a given localized source; the following
argument supplies that missing step.

Write F(X,Y)=sum from n=0 to N of f_n(X)Y^n, with f_N a nonzero
polynomial. Take a nonzero nonnegative smooth radial A_epsilon of compact
normal support as in K2531, with its conserved P_epsilon. On the actual
positive-curvature branch, P has the same sign as A, so t_A is nonzero,
smooth, radial and compact in the three positive normal directions.
Even for a signed nonzero compact A, t_A cannot vanish identically: that
would give A=-3P/4 and P'+7(Cwarp'/Cwarp)P=0; the compact outer condition
then forces P=A=0. Thus the same argument applies to such signed profiles.
For tangentially homogeneous radial functions on A, the actual scalar X is

    X_radial=partial_r²+
      [2 S'(r)/S(r)+4 Cwarp'(r)/Cwarp(r)]partial_r.           (17)

Its coefficients are smooth on every interval away from r=0 and below the
first focal point. The equation f_N(X_radial)t_A=0, if it held, would be a
regular linear ODE of order twice deg(f_N), with nonzero constant leading
coefficient. For a degree-zero nonzero polynomial it already forces t_A=0.
For positive degree, compact support provides zero Cauchy jets on an outer
open interval; ODE uniqueness propagates zero through the connected r>0
tube. Smoothness then gives zero at r=0. This contradicts the nonzero t_A.
Hence f_N(X)t_A is nonzero somewhere in the tube.

For partial thickness, the highest B derivative in
F(t_A tensor delta_q) has order2N with that nonzero coefficient. In B
normal coordinates its leading polynomial is the nonzero Nth power of the
nondegenerate quadratic principal symbol of Y. Lower powers of Y cannot
cancel this leading derivative of delta. Therefore

    F(X,Y)(t_A tensor delta_q) !=0.                          (18)

There exists a compact full-product phi with nonzero O_phi for this ACTUAL
prescribed source, if a full solution exists. The proof selects a detector
where the resulting distribution is nonzero; it does not claim every
detector detects it.
No tangential cutoff is imposed on the source. Compact tests may be chosen
away from tangential edges, exactly as in K2531. Equation(17) uses the
warped volume density; flat normal differentiation is not substituted.

The full-thickness repair rho_delta converges distributionally to delta_q.
Differential continuity gives
F(t_A rho_delta) -> F(t_A delta_q). Choose a SINGLE compact phi detecting
(18). The same fixed-detector value is nonzero for all sufficiently small
positive delta, by convergence to a nonzero real number. This follows the
actual conserved smooth-source family without choosing source-dependent
new detectors. It is still conditional on solutions existing for those
sources and does not assert convergence of any sourced fields.

## 6. Locality and order: what the construction cannot deliver

Both sides of (11) have test support inside supp(phi). If that support is
disjoint from supp(j), O_phi=0 for every admitted solution. The new coupled
construction repairs the scalar-filter limitation, but it remains a contact
observation. A physical source-disjoint response needs selected homogeneous
or boundary data, or a different observation/domain construction. No
noncompact inverse or boundary term has been hidden in a cofactor.

There is a rigorous conservative differential-order bound without expanding
the full determinant. Give the six realization slots weights
w=(0,0,2,2,2,2). Each M_ij has scalar differential order at most
2+w_j-w_i. Summing along a determinant permutation cancels the weights,
so d has order at most12. The adjugate entry (i,j) has order at most
10+w_j-w_i, while e_j has order at most2-w_j. Thus b_i has order at
most12-w_i, and realization T restores at most order12. Consequently

    order(psi)<=12, order(chi)<=12,
    order(Epsi)<=14, order(source test)<=12.                 (19)

These are upper bounds, not minimality or sharp leading-order assertions.
They also give N<=6 in section5. Algebraic cancellations may improve them.

On a fixed relatively compact chart use an auxiliary positive component L2
norm, solely for error control. For an error eta in h,

    |<eta,Epsi>|<=||eta||_2 ||Epsi||_2.

For a fixed profile normalized at fourteen-dimensional scale delta, smooth
coefficient bounds and (19) give ||Epsi_delta||_2=O(delta^-21) and a source
test bound O(delta^-19). These are conservative mathematical upper bounds,
not Theta estimates, observed noise, physical energy, or experimental
sensitivity. At fixed phi every distributional observation is finite. A
shrinking-detector limit on the singular actual source requires its separate
distributional analysis; (18) is not a promise of a finite pointwise metric.

## Evidence, contrary constructions and remaining decision

The exact probe checks the curved coefficients, actual diffeomorphism
columns and divergence, factor exchange including skew orientation, complete
K2541 restriction, zero-frequency determinant, explicit full-chart solution,
original shift/sign, cofactor arithmetic and weighted-order bounds. Its
rational cofactor evaluations do not replace the universal cofactor identity.
The curved intertwining, compact adjoints, radial ODE uniqueness and
distributional approximation are the analytic proofs above. No independent
physical or proof-assistant certification is claimed.

Contrary controls retain the missing skew row, the curved Hessian terms,
the sign of adjoint cancellation and the distinction between h and z.
K2546's no-nonzero-compact-scalar-Weyl-annihilator result survives: this
construction solves a DIFFERENT coupled tensor/skew cancellation problem.
K2544's source-fixed homogeneous ambiguity also survives for general
unfiltered observations; the special Epsi annihilates the complete
homogeneous solution space by its exact adjoint representation.

The compact adjoint criterion and its actual-source contact question are
now settled constructively in this scalar-generated test class. The next
physical question is a source-compatible common boundary/domain realization
with a nonzero source-disjoint original-metric observation, or an action-owned
detector coupling that justifies this particular contact observation. Further
cofactor expansion alone does not supply either. The actual arbitrary-source
inverse, native Met(X), interacting physical quotient and empirical
calibration remain separate debts.

[Probe](../../tests/channel-swings/k2548_compact_coupled_metric_detectors_probe.py),
[report](../../lab/process/k2548-compact-coupled-metric-detectors.json),
[full constraints](k2539-covariant-tensor-constraints-2026-11-04.md),
[localized source](k2531-partial-thickness-source-2026-11-04.md),
[full-thickness repair](k2543-localized-source-readout-2026-11-04.md).
