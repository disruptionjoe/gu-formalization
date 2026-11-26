---
title: A sign-indefinite candidate Hamiltonian survives the connection constraints
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T1
expected_delta: Derive actual coupled constraints before testing a negative-energy claim.
actual_delta: Complete connection time-kernel reduction, exact central elimination and a sign-indefinite constrained quadratic Hamiltonian on the existing sufficiently-large-kappa stationary branch. The two kappa1 backgrounds and physical ghost spectrum remain undetermined.
class_covered: Existing real W2 K95 full-U stationary branch T(1/kappa)=O(1/kappa), sufficiently large positive kappa; autonomous imaginary connection Hessian, compactly supported constrained instantaneous data in a time-adapted local patch. Separately complete pointwise connection symbols and exact nonlinear central elimination for nonzero kappa.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-04
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-GEO-51
- lab/sources/source-claim-register.yaml#SC-META-53
- explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md
- explorations/conditional-build/source-action-physical-dynamics-2026-11-25.md
- explorations/conditional-build/source-action-offsection-metric-2026-11-25.md
source_bridge:
  status: conditional
  reason: Source motivates first-order action and full-U ingredients, but does not select this reconstructed Shiab completion, the tested coupling range, or the unrestricted constrained instantaneous-data category. Physical state selection and observed quotient are open.
kill_condition: Exclude positivity of the canonical quadratic Hamiltonian on INTERNAL-LARGE-KAPPA-CONSTRAINED-DATA only. No exclusion of restricted physical domains, either kappa1 background, source GU, class C or an observed particle spectrum.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-LARGE-KAPPA-CONSTRAINED-DATA
internal_target_verdict: canonical quadratic Hamiltonian has both signs and is unbounded above and below
canon_verdict_change: none
---

# A sign-indefinite candidate Hamiltonian survives the connection constraints

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Reduce the actual connection constraints and test the resulting canonical energy.
actual_delta: Exact constraint reduction yields an indefinite quadratic Hamiltonian on the existing large-kappa branch, in the declared instantaneous-data category; no physical ghost verdict.
```

## Result in plain terms

**A negative-energy warning survives the actual connection constraints on an
already-established stationary branch of the candidate.** It is stronger than
the earlier metric-only coefficient or ambient-signature test: an autonomous
sector of the full coupled quadratic action is identified, every algebraic
constraint in that sector is eliminated for sufficiently large positive kappa,
and its canonical quadratic Hamiltonian still has both signs.

The conclusion concerns **compactly supported constrained instantaneous data**.
We have not proved that every such datum evolves in a well-posed physical
solution space. Nor does indefinite energy alone imply exponentially growing
solutions or a quantum ghost. The two certified kappa=1 backgrounds are not
classified by this theorem, and they are not known to connect to the small-h
branch. No numerical large-kappa threshold is claimed.

This makes the next question much sharper: which of these directions survive
the actual physical state/domain selection? At kappa=1 there is also a concrete
finite-dimensional algebraic constraint matrix to compute; a full differential
inverse of the connection operator is no longer the first prerequisite.

| State | Result or remaining question |
|---|---|
| ESTABLISHED | Complete time-symbol kernel, its derivative-free self-block, exact central elimination, and large-kappa constrained quadratic-energy indefiniteness. |
| RULED OUT under stated premises | Positive canonical quadratic energy on the unrestricted compact constrained-data category of that large-kappa branch. |
| UNDETERMINED | Actual kappa1 constraint-matrix invertibility, propagated physical states, helicity-two/massive spin content, quantum norm, nonlinear energy and source selection. |
| NOT MODELED | A source-selected quantum state/domain or interpretive observer ontology in this calculation. |

**Weakest unproved physical link:** admission of the tested data as observed
physical solution states. **Source-necessary exclusion:** absent.
**Class-C representativeness:** unproved. Internal T1 review concerns the stated
mathematical exclusion only; source, physics ledger, class C, canon and paper
verdicts are unchanged.

```gu-typed-objects
result: actual candidate connection constraints and constrained quadratic energy
carrier: TstarY tensor u64_64; autonomous imaginary-Clifford quadratic sector LAYER=ambient BRIDGE=physical_observation_unproved CHIRALITY=N/A
pairing: native -Re_trace_div128 and K95 one-form contraction with actual volume ON=connection_forms
real_structure: real full U64_64 with real and imaginary Clifford coefficient sectors; no extra Sp restriction
grading: coefficient-conjugation eigenspaces; not generation or physical chirality grading
action_owner: repository-construction fixed W2 I1B-style action with repaired independent-bar matter
target: time-kernel algebraic constraints and canonical quadratic Hamiltonian MAP-TYPE=not-a-map
```

> Classification: `INTERNAL_STRUCTURAL_ONLY`, outside the listed conventional
> particle-comparator families. **GU-COMPARATOR-ROUTING — scope before inference.**
> Read [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> K95 is not K77; full U is not an assumed Sp parent. I1B is not the separate
> residual-square I2B. Literal contraction, source2+1 and independent barred
> fields are retained. A metric amplitude or a connection component is not an
> observed graviton or a physical particle count.

## 1. The actual action and a coupled sector

Reuse the [fixed W2 action](source-action-wave2-construction-2026-11-25.md):

    S_B = <T,Phi F_B> + 1/2<T,Phi D_B T>
          + 1/3<T,Phi(T wedge T)> + kappa/2<T,T>.

Pairings include the native volume. The actual formal adjoint retains density,
frame and coefficient derivatives. On a stationary zero-matter background,

    H_AA = kappa Id + K + 2 N(T0,.),
    K = (Phi D_B + D_B^dagger Phi^dagger)/2.

The source's printed endpoint is not substituted for this action derivative.
The stationary59 Jacobian is not this full operator.

The held geometry, B, Phi and real stationary T0 have real Clifford
coefficients. On the real Lie algebra u(64,64), coefficient conjugation splits
real Clifford grades1,2 mod4 (dimension8128) from i times grades0,3 mod4
(dimension8256). Mixed products have imaginary trace, so the real quadratic
action has no mixed term between these sectors. Metric variations and their
moving Clifford/reference terms are real. Thus the **imaginary sector is
autonomous in the complete coupled quadratic system**, including metric and
real connection variations. Zero-background matter also decouples linearly.

This is an existing background symmetry, not a newly imposed physical quotient.
The small-h analytic branch is also coefficient-conjugation real: the complete
Euler residual and source preserve this conjugation, and the unique analytic
branch through T=0 must equal its conjugate (equivalently its convergent
recursion has real coefficients). Thus sector autonomy applies to that branch,
not only to the two certified kappa1 roots.
Nonlinear imaginary fields can backreact at quadratic order; we do not claim
a fixed-background nonlinear truncation.

## 2. Complete connection time symbol

For a real formal covector xi put

    P_xi=Phi(xi wedge .),  K_xi=(P_xi-P_xi^t)/2.

The transpose uses the native trace/form pairing; the minus is the differential
adjoint sign. K_xi is pairing-skew. The full complexified connection fibre has
dimension14*2^14=229376. A basis entry has exterior one-bit mask e and Clifford
mask c. Phi preserves e XOR c; wedge/contraction with an axis toggles that axis.
For time theta3, labels r and r XOR 2^3 form a28-entry block:

    (e_i,e_i XOR r), (e_i,e_i XOR r XOR 2^3), i=0,...,13.

Choose r without bit3. Complex orthogonal covariance fixing time relates
transverse subsets of equal cardinality s. The even number of Hodge occurrences
in each native Phi term cancels orientation signs. Complex rescaling of orthogonal
axes proves ranks without changing the physical real form. Hence14 exact
representatives with multiplicities binomial(13,s) exhaust all8192 blocks.

| s | rank | kernel | multiplicity |
|---|---:|---:|---:|
|0|26|2|1|
|1|6|22|13|
|2|24|4|78|
|3|6|22|286|
|4|26|2|715|
|5|6|22|1287|
|6|26|2|1716|
|7|6|22|1716|
|8|26|2|1287|
|9|6|22|715|
|10|26|2|286|
|11|6|22|78|
|12|26|2|13|
|13|2|26|1|

Each kernel has nondegenerate mass pairing. Blocks are pairing-orthogonal.
Native commutator/two-i-anticommutator operations preserve u(64,64), whose
complexification is the full matrix algebra. Therefore these complex ranks
are the actual real ranks:

| Real sector | connection components | time rank | time kernel |
|---|---:|---:|---:|
|Real Clifford|113792|64482|49310|
|Imaginary Clifford|115584|66430|49154|
|Full U|229376|130912|98464|

These are derivative ranks and constraint-row counts, **not physical degrees of
freedom or particle multiplicities**. The exact probe reconstructs every
representative matrix, kernel and pairing Gram; this is not numerical sampling.

## 3. The whole kernel self-block is algebraic

Let N=ker K_dt. For every covector zeta and n1,n2 in N,

    <n1,K_zeta n2>=0.                                      (1)

For a transverse axis j, only paired label r XOR 2^j can receive a label r.
Covariance leaves two incidence cases: j inside or outside r. All26 feasible
representatives have zero exact kernel-to-kernel matrix. Other target blocks
are pairing-orthogonal; linearity covers every covector. The time term is zero
by definition. This proves(1) for the entire carrier.

Nondegeneracy of the pairing on N gives a direct orthogonal splitting
V=N+R, with R=N-perp=im K_dt. K_dt is invertible on R. Write a=v+w in moving
R,N bundles, with their pairing-orthogonal projectors P_R,P_N. For
H_AA=sum K^I partial_I+M, the exact compressed operator is

    M_N=P_N H_AA inclusion_N
       =P_N [M P_N + sum K^I(partial_I P_N)]|N.             (2)

It is an **order-zero endomorphism**, by(1). All moving-projector, frame,
density and background terms remain. The exact N equation is

    M_N w + P_N H_AA v + P_N H_Ag p=0.                    (3)

It contains no derivatives of w and no time derivative of v. The remaining R
equation contains no time derivative of w. If M_N is invertible, w is eliminated
pointwise; the connection-only R system is first order in time and at most
second order in other coordinates. Real-sector metric forcing must still be
carried. In the autonomous imaginary sector H_Ag=0.

This replaces the earlier blanket differential-inverse burden with a specific
finite-dimensional lower-matrix question. It does not prove its answer at
kappa1, global Fredholmness, or a well-posed evolution.

## 4. Actual constraint elimination on the existing small-h branch

The [analytic stationary result](source-action-homogeneous-analytic-vacuum-2026-11-25.md)
already supplies T(h)=O(h), h=1/kappa, on the same fixed candidate. Choose a
compact local spatial/normal patch on which base dt is uniformly ambient-
timelike. Such a patch exists around the observation section; it need not
cover the entire metric fibre. Geometry and projectors are independent of
kappa and time on these constant-base backgrounds.

Equation(2) has the exact form

    M_N(h,y)=kappa Id_N+E(h,y).

E and its required derivatives are uniformly bounded on the compact patch
for small h. A fixed auxiliary positive norm is used only to bound an inverse,
not as a physical pairing. For sufficiently large positive kappa the Neumann
series gives M_N^-1=O(1/kappa), uniformly locally. Thus all98464 connection
N components—and all49154 in the autonomous imaginary sector—are algebraically
eliminable on that branch.

This is an actual lower-term result, not replacement of E by zero. It supplies
no numerical threshold, no inverse at kappa1, and no connection of either
certified kappa1 root to this branch. It tests an existing coupling family;
it does not choose a new coupling value or action.

## 5. Energy after the constraints: the internal T1 result

Take fixed smooth compactly supported imaginary R-data v on the patch. The
constraint solution is

    w[v]=-M_N^-1 P_N H_AA v=O(1/kappa).

The leading kappa term in P_N H_AA v vanishes because P_N v=0. The estimate
holds with the finite spatial derivatives used by the action for this fixed v.
Its support remains compact. N and R are orthogonal.

The time-independent quadratic kinetic term is exactly

    1/2 integral rho <v,K_dt partial_t v>.

There is no w time term or mixed w/v time term. Substitution therefore leaves
a nondegenerate time two-form on R. The N constraints are second-class in the
formal local Dirac sense: the eliminated algebraic block is invertible and
the remaining velocity two-form has no radical. No additional formal constraint
is generated there. This accounts for all linearized N equations and primary
momentum constraints in this autonomous block, not nonlinear constraint
integrability or linearization stability. This is not a claim that the resulting PDE has a well-posed
flow on every smooth compact datum.

For the displayed first-order real action, canonical energy is minus the
non-time-derivative part. The actual reduced quadratic Hamiltonian satisfies

    H_red[v]=-kappa/2 integral rho <v,v>+O(1).             (4)

Indeed the w mass term is O(1/kappa), the mass cross term is zero, and the
remaining native geometric, spatial-derivative and T(h) terms are bounded
for fixed v. No density or lower coefficient is discarded.

Both signs of the integral in(4) occur in R. For Z=i Id and a central covector
c perpendicular to the unit normalization of timelike dt, the exact native identity is

    K_dt^2(cZ)=-48 cZ.

Thus cZ lies in im K_dt=R. Its norm is G^-1(c,c). A spatial central covector
has positive norm; a negative normal covector has negative norm. Extend each
smoothly over a sufficiently small patch, project into R if needed, and
multiply by a nonzero compact bump. Their norm signs persist. Equation(4)
then gives negative and positive energies respectively for every sufficiently
large kappa (using one threshold for the two fixed witnesses).

At each such kappa the constraints are linear and H_red quadratic. Scaling
either witness preserves its constraints and makes H_red unbounded in its
respective direction. An overall action-sign convention exchanges the two
directions and cannot make the quadratic form positive.

**Precisely ruled out:** positive canonical quadratic Hamiltonian on this
unrestricted constrained instantaneous-data category. **Not proved:** negative-
energy globally propagated modes, dynamical instability, a quantum ghost,
unbounded full nonlinear energy, an observed wrong-sign graviton, or either
kappa1 background's exclusion. First order in time/second order in space does
not justify a blanket Cauchy–Kowalevski existence claim. A physical domain may
exclude the witnesses; that requires an explicit preserved domain and observed
map, not a relabeling of the constraints already eliminated here.

## 6. Exact central elimination, including nonlinear terms

Independently of the large-kappa theorem, write T=cZ+R0 with coefficientwise
tracefree R0. Centrality gives T wedge T=R0 wedge R0. B is spin-valued,
D_B(cZ)=dc Z, and Phi on scalar two-forms has Clifford grade3. The center
self-derivative and geometric-source terms vanish. The mass cross term vanishes.
After legitimate integration by parts using the actual adjoint,

    S[T]=S[R0]+ integral rho [kappa/2<cZ,cZ>+<cZ,J0>],
    J0=p0[K R0 + (1/3)Phi(R0 wedge R0)+J_F].              (5)

J_F is the action-derived matter current; the held independent-bar fermion
operator is affine in T. The coefficient1/3 is essential: R0 wedge R0 has no
c dependence. For nonzero kappa the exact central equation and reduced action are

    cZ=-J0/kappa,
    S_reduced=S|center=0 - integral rho <J0,J0>/(2kappa).   (6)

This is a nonlinear local auxiliary-field reduction, including metric/matter
variations by the envelope identity. It requires no59-Jacobian or differential
inverse. The equivalence is for compact interior variations or transported
compatible boundary data. Eliminating the center is not discarding a gauge mode:
the earlier fixed-reference active central U1 transformation is not an action
symmetry. Dressing-frame redundancy leaves Ahat unchanged.

This operation differs from eliminating the time-kernel N. Transverse central
components lie in R and can serve as canonical momenta; solving their Euler
equations introduces second-order dynamics for their partners. They are not
fourteen extra primary N constraints. Section5 performs the full N reduction
in the original first-order variables; it does not double-count the two
eliminations or discard its central energy witnesses.

The induced tracefree time-velocity square has rank13 and inertia(4+,9−) at
positive kappa on an ambient-timelike patch. This alone is an **unreduced**
kinetic warning; section5, not this13-dimensional block, supplies the full
imaginary-constraint energy argument. Pointwise causal controls give:

| Covector | central map rank | induced square rank | nonzero inertia |
|---|---:|---:|---|
|timelike|13|13|4+,9−|
|spacelike|13|13|5+,8−|
|null|13|12|4+,8−; one radical direction in the image|

The supporting identity is **p0 Phi^dagger Phi=-48 Id on scalar two-forms**.
The unprojected composite has grade4 terms; removing p0 would be false.
The actual central K_xi squared identity includes its longitudinal projector,
and the native probe checks every central column for all three causal types.

## 7. A tempting false ghost is explicitly rejected

Keeping only K_dt partial_t+kappa would make each span{c,K_dt c} look like a
two-mode oscillator. The actual lower operator does not preserve it. For raw
c=theta0 Id (physical field i c), native K(c)+2N(T0,c) has receivers
(exterior mask1, Clifford masks259 and517), each exactly−1/4, outside that span.
All59 background contributions to those two coefficients vanish identically.
The leakage holds at both certified roots and throughout the held59 family.

These oscillators are not actual modes. No frequency or particle mass is
exported from them. The large-kappa theorem instead retains the full lower
operator and eliminates the complete imaginary constraint block.

For the real sector, the prior metric Q4 remains an unreduced coefficient.
With t=a-b, b=B'[g]p, the leading identity is

    1/2<a,K a>+<a,L b>-1/2<b,K b>
      =1/2<t,K t>+<t,P b>.

The already-completed polynomial principal response does not determine the
remaining real-sector metric equation or cancel Q4 automatically. Fibre
integration, lower metric coupling and physical spin identification remain.

## 8. Choice budget, source relevance and continuation

No action, coupling value, contour, cutoff, physical pairing or state restriction
was added. Coordinate/phase decomposition and elimination of existing fields
are derived operations. The compact bump is a mathematical witness, not an
installed physical domain or reference measure.

The existing assumption view stays at **10 active choice families,4 grouped
compatibility obligations, net6**. Wave delta:0 new choice families,0 additional
successful viability obligations,0 source-selected predictions. The constrained
energy exclusion is recorded as a restriction on an existing completion
category, not credited as a fifth satisfied compatibility bundle. The inherited
arbitrary-dispersion warning remains; this constraint-focused wave adds no such
freedom. These grouped counts are not physical degrees of freedom.

SC-ACT-01/05 motivates the action grammar; SC-ACT-04's separate I2B is not
imported. SC-GEO-51 keeps full U; SC-META-53 explicitly leaves unbounded spectra
and physical shielding unresolved. LT-GR1 still requires the full observed
helicity/massive-spin quotient; LT-GR6b and LT-SM8 require the action-derived
physical domain/quotient. Their verdicts remain NEEDS.

The queued ghost diagnostic has now **run and produced a scoped constraint/
energy result**. The full physical ghost spectrum remains open. The concrete
next discriminator is the actual M_N endomorphism at the two kappa1 roots,
beginning with the autonomous imaginary sector, followed by the admitted
physical domain's treatment of the surviving energy directions. The real
metric/connection and observed spin questions remain separate. No complete
selection theory is made a waiting prerequisite for these calculations.

## Verification

The [native probe](../../tests/program-focus/source_action_coupled_ghost_probe.py)
reconstructs all14 complete representative time blocks, exact kernels and
nondegenerate mass Gram matrices; all26 spatial incidence compressions vanish.
It additionally passes325 exact central/causal/algebra controls, including
native lower leakage and the false unprojected Phi-composite control.
These are finite certificates for stated algebraic seams, not physical counts.

Eight [Lean finite lemmas](../../Lean/GUFormalization/CoupledGhost.lean) check
auxiliary square completion/uniqueness, canonical energy signs, bounded-remainder
dominance and count arithmetic. They do not formalize the Clifford matrices,
analytic branch, moving bundles or PDE domains. The analytic/constraint proof
is written and independently reviewed. Required T1 mathematical and hostile
reviews and native gates are recorded in the [review](../../lab/process/hostile-reviews/2026-11-25-source-action-coupled-ghost-review.md)
and [machine evidence](../../lab/process/source-action-coupled-ghost.json).
