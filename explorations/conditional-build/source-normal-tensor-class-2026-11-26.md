---
title: 'Normal connection tensors: a complete symmetry and observation classification'
status: exploration
doc_type: structural-result
created: '2026-11-26'
program_target: LB-CLASS
tier: T1
expected_delta: Complete the previously excluded normal tensor class and actual observation kernel; distinguish
  source full-U and optional C. Scope actual auxiliary jets.
actual_delta: 'Complete normal tensor class: block symmetry68 real sharp-skew/32 with optionalC; fixed
  endogenous+weak symmetry4 real full-U/zero with optionalC, with exact observation kernels and ranks.
  Existing certificates realize smooth constrained-Q response; full-R jets reach a new spin4 source. No
  GU verdict.'
class_covered: "All pointwise real-linear normal one-form tensors N_real\u2192End_C^odd(S128) on the declared\
  \ K95 split, with source sharp-self Clifford convention and explicitly fixed geometric symmetry actions.\
  \ Separate W2 candidate auxiliary diagnostic; neither every source VEV nor all classC."
premises:
- explorations/conditional-build/source-reality-mixing-class-2026-11-24.md
- explorations/conditional-build/weak-endogenous-grading-2026-11-24.md
- explorations/conditional-build/source-action-weak-response-2026-11-26.md
- lab/sources/source-claim-register.yaml#SC-CHI-51
- lab/sources/source-claim-register.yaml#SC-CHI-52
- lab/sources/source-claim-register.yaml#SC-MAS-02
- lab/sources/source-claim-register.yaml#SC-GEO-51
source_bridge:
  status: conditional
  reason: Source fixes the full-U parent and operator/connection motivation, but does not require fixed
    simultaneous tensor isotropy or optional C-preservation. Physical fluctuation, domain, normalized
    readout and curvature suppression remain unproved.
kill_condition: The zero class excludes only nonzero normal tensors satisfying every stated fixed symmetry,
  source adjoint and optional C condition. Moving reductions, full-U survivors, W2 pairing and GU remain
  outside.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-FIXED-NORMAL-TENSOR-QUATERNIONIC
canon_verdict_change: none
---

program_target: LB-CLASS
tier: T1
expected_delta: Complete the normal tensor and actual observation class; test local auxiliary compatibility.
actual_delta: Fixed full-U four-parameter class survives; optional C intersection zero. Smooth localQ constrained response with nonzero compact test functional; fullR jets reachspin4. No GU verdict.


# Normal tensors: which symmetry assumptions actually survive?

**The source full-U convention retains a four-real-parameter normal tensor class under simultaneous fixed endogenous Lorentz and actual geometric weak symmetry. The additional quaternionic-compatible restriction leaves only zero.** A covariant family whose reduction or VEV transforms is a different category and has explicit nonzero counterexamples. This is a conditional internal exclusion, not a falsification of GU.

The calculation covers every complex endomorphism, not a Clifford-degree ansatz. In the weaker block-Lorentz category, observation has a nontrivial coefficient kernel. In the stronger fixed category it is injective. Tensor coefficient dimensions, spinor ranks and physical family counts are different quantities throughout.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: complete pointwise normal tensor classes and actual NE contraction
carrier: geometry-derived K95 branch H3_1 plus N6_4; complex Dirac S128; normal one-form End tensors LAYER=ambient+observed BRIDGE=actual-NE-contraction CHIRALITY=S-FULL-DIRAC
pairing: source-side indefinite Krein form with c(v)-sharp=plus-c(v); W2 opposite convention separate ON=declared_carrier
real_structure: optional quaternionic C square minus1, commuting real source Clifford vectors; fullU does not require C preservation
grading: ambient Clifford oddness and horizontal/normal volumes; no physical family identification
action_owner: source-action primitive NE connection variation; no new action or physical VEV selected
target: q(alpha nu,0)=(0,GammaN(alpha)nu,0) MAP-TYPE=contraction
```

## Selection and source custody

Fresh evidence basis `736d965e076a82608cc8f2d1ca2016612de4142c`. Joe directed the continuing falsification wave and a quick20-lens mathematical reassessment, expressly including category theory and number theory. Target LB-CLASS; internal T1 optional-restriction exclusion and T2 classification/auxiliary analysis. The normal tensor class was explicitly outside the earlier horizontal theorem. Reusing the already-proved weak/endogenous Lie-generation theorem gives greater class coverage than a further neighboring candidate calculation.

Source relevance is narrower than mathematical breadth. SC-CHI-51/52 motivate operator VEV/effective decoupling; SC-MAS-02 identifies a spinless gauge-potential subspace; SC-GEO-51 supplies fullU. None supplies fixed simultaneous tensor isotropy, mandatory C, normalized physical readout or an on-shell suppression law. These are the weakest source links. Class-C representativeness/width remain unproved; no source-necessary exclusion, class-C change, physical prediction or ledger movement follows. Strongest executable alternative was actual auxiliary-jet compatibility; its bounded geometric diagnostic is included below.

## 1. Carriers and exact symmetry action

Use the geometry-derived K95 branch, not an identification with the source-asserted K77. The signature bridge remains open; this calculation does not settle it. At a point fix H(3,1)+N(6,4), S complex128, Omega the real ambient involution, and the nondegenerate K95 source-side Krein pairing. Let C be the fixed quaternionic antilinear structure. Alpha:N_R→End_C(S) is real-linear and ambient-odd: {alpha(n),Omega}=0.

A geometric group element acts on the tensor by

    (g.alpha)(n)=rho_S(g) alpha(rho_N(g)^(-1)n) rho_S(g)^(-1).

Thus the normal leg transforms. Pointwise commutation with SM while leaving n fixed is the wrong class.

Category B: block Lorentz L acts trivially on N and through its ordinary horizontal spin action on S; fixed geometric normal SM G acts on N and S together. N_C=(3,1,-2)+(3bar,1,2)+(1,2,3)+(1,2,-3), hypercharge integer6Y. Equivalently N_C=U+U*, U=C3_-2+C2_3. Normal S_N=Lambda*U.

Category E: require the SAME alpha fixed under endogenous graph Lorentz (X,delta X) and geometric fixed SM (0,W). On N, delta(X)h=-X^T h-hX for N=Sym²H*, actual lambda-half metric. On S use the spin lift of both blocks. The existing trace-motion theorem then proves the generated algebra is so(H)+so(N). This is not assumed independence and not an identification of block and endogenous Lorentz. A covariant family alpha(J) under moving reduction J does not satisfy fixed-alpha invariance merely by covariance.

## 2. Category B: complete all-End coefficients

Clifford identifies the complete complex endomorphism algebra. Horizontal Lorentz scalar tensors have horizontal Clifford degrees0 or4, spanned by 1 and real omega_H. Ambient oddness then selects odd normal degrees:

    T_B,C = span_C{1,omega_H} tensor
            direct_sum_(k=1,3,5,7,9) Hom_G(N_C,Lambda^k N_C).

This includes all Clifford degrees and all End_C(S), not an ansatz.

Exact multiplicities and invariant even-form dimensions:

| k | 1 | 3 | 5 | 7 | 9 |
|---|---:|---:|---:|---:|---:|
| m_k = dim Hom_G(N,Lambda^kN) | 4 | 8 | 10 | 8 | 4 |
| m_k-I_(k-1)-I_(k+1) | 1 | 3 | 4 | 3 | 1 |

| l | 0 | 2 | 4 | 6 | 8 | 10 |
|---|---:|---:|---:|---:|---:|---:|
| I_l = dim (Lambda^l N)^G | 1 | 2 | 3 | 3 | 2 | 1 |

Hence dim_C T_B=68. The real invariant tensor spaces complexify to these modules, so the displayed numbers are also dimensions of the corresponding real coefficient spaces before multiplying by i.

Source pairing: on a real normal k-word, sharp sign is (-1)^(k(k-1)/2). Real omega_H is sharp-self and commutes with normal words. Thus sharp-skew tensors comprise:

- imaginary coefficients for k1,5,9;
- real coefficients for k3,7.

This gives real dimension68. C fixes every real Clifford word and conjugates scalars. Optional C-compatibility retains exactly k3,7, giving real dimension2*(8+8)=32, NOT34. C is a real involution on the sharp-real space; there is no general reason to halve68.

## 3. Actual normal NE contraction: exact kernel and image

Hold the observation split, Clifford contraction q and spinor input fixed in this primitive NE variation; no delta-q term or full reduced-action variation is asserted. For pure normal alpha, P_H(alpha nu)=0. Consequently

    q delta D_NE[alpha] nu = (0, Gamma_N(alpha)nu,0),
    Gamma_N(alpha)=sum_i eta_i c(n_i) alpha(n_i).

Although alpha is ambient-odd, Gamma_N(alpha) is ambient-even. In the retained correlated field grades G=diag(Omega,-Omega) and observed G_o=diag(Omega,-Omega,-Omega), this NE vertex is grade-even; it is not a physical Weyl-decoupling theorem. Independent density-dual bars, source2+1 provenance and the unresolved physical half-label identification remain separate. No repeated-three-family interpretation is imported.

The sigma=tau-Gamma_H b coordinates give the same result because b=0. An arbitrary projection or scalar reduction is not substituted. A nonzero tensor in kerGamma_N remains a nonzero primitive NE coefficient; observation invisibility does not make every current vanish.

On degree k Clifford forms this contraction maps to degrees k-1 and k+1. Both outputs are independently onto invariant forms. For invariant psi of degree k-1 and theta of degree k+1, take

    alpha_psi(v)=v^flat wedge psi,
    alpha_theta(v)=iota_v theta.

Then

    Gamma_N(alpha_psi)=(10-k+1)psi,
    Gamma_N(alpha_theta)=(k+1)theta.

(The identification of forms and Clifford words is the metric Chevalley identification, and the indefinite signature cancels through the contracted inverse metric.) The opposite-degree term vanishes for each construction. All coefficients are nonzero in the admitted odd degrees; these are right inverses up to the shown integer factors.

Thus:

| category | coefficient dimension | image dimension | kernel dimension |
|---|---:|---:|---:|
| complex all-End block-Lorentz×SM | 68 complex | 24 complex | 44 complex |
| source sharp-skew | 68 real | 44 real | 24 real |
| source sharp-skew and C-compatible | 32 real | 20 real | 12 real |

Reason for real counts: adjoining odd degrees have opposite coefficient phases (real versus imaginary), so their common even-degree outputs cannot cancel over R. The only kernels in the sharp-real class are the degreewise kernels, total2*(1+3+4+3+1)=24. C restriction retains k3,7 with disjoint even-degree output supports, total kernel2*(3+3)=12, image2*(I2+I4+I6+I8)=20. The C-compatible image consists exactly of real invariant normal degrees2,4,6,8, times1 or omega_H. It excludes scalar and normal-volume output terms. These dimensions concern tensor-coefficient maps, not spinor rank, family counts or physical modes.

## 4. Category E: endogenous plus fixed geometric SM

Apply the already-owned trace-motion theorem to the honest representation N* tensor End_C(S). Fixed tensors for graph Lorentz and fixed weak are fixed for the generated product, so all-End completeness reduces to the normal vector multiplicity in the Spin(N) Clifford algebra: one each in degrees1 and9, times horizontal degrees0/4.

Therefore complex dimension4, uniquely

    alpha(n)=c_N(n) A,
    A in span_C{1,omega_H,omega_N,Omega}.

Fix the orientation convention Omega=omega_H omega_N. Here omega_H²=omega_N²=-I and omega_N^sharp=-omega_N. Reversing this ambient orientation relabels d and the ambient halves; the rank formulas below use the pinned plus convention. Each REAL tensor c_N(n), c_N(n)omega_H, c_N(n)omega_N, c_N(n)Omega is nevertheless sharp-self: c_N anticommutes with omega_N/Omega and commutes with omega_H. Each is C-even.

Consequences (coefficient equations are also checked in the finite Lean core):

    sharp-skew: A=i(a+b omega_H+c omega_N+d Omega), a,b,c,d real;
    additional [alpha,C]=0: alpha=0.

Thus Category E has4 real source-full-U coefficients; optional C intersection is zero. This zero is a conditional internal tensor-class exclusion, not a source kill. In W2's gamma^sharp=-gamma convention all odd-degree sharp signs reverse, so this zero cannot be transferred there; with the same real Clifford/C laws the four real product tensors survive instead.

The actual contraction is

    Gamma_N(alpha)=10 A,

so it has no coefficient kernel and image dimension4 real. The spinor rank strata are0,64,128. The four joint horizontal/normal chiral blocks have complex dimension32. The fixed quaternionic conjugation C flips both horizontal and normal complex chirality labels and preserves the ambient half. Although C-compatibility is not imposed in this full-U class, A is C-odd: C A C^-1=-A. Thus opposite joint blocks have eigenvalues lambda and -conjugate(lambda); a nonzero pair contributes64. Sharp instead flips the horizontal label while preserving the normal one, so it is not the reason for this same-ambient pairing. Each ambient input half therefore has either rank0 or64. Generic A has full128 support.

## 5. Source spinless subspace and the scope ceiling

SC-MAS-02 specifically points to Lambda1 tensor Lambda1, not all oriented-Spin-invariant all-End tensors. The normal grade1 scalar line is alpha(n)=i a c_N(n) in this sharp convention. Its contraction is10ia I, full spinor rank128 for a nonzero. It is C-odd and therefore absent if the additional C-compatible restriction is imposed.

For comparison, truly FULL ambient Spin(9,5)-equivariant V14→End^-(S) has the two complex tensors c(v),c(v)Omega. Sharp-skew gives two real imaginary directions, optional C again zero. The source's specifically grade1 scalar is only the c(v) line; the c(v)Omega partner is an oriented pseudoscalar Clifford-degree13 tensor, not automatically SC-MAS-02's selected piece. This distinction avoids silently replacing a named source subspace by a larger all-End class.

A normal-only tensor extended by zero on H is not itself an ambient Spin14-equivariant one-form. The normal scalar is a split component; the full ambient scalar pairs it with the corresponding horizontal component.


### Countercontrol: moving reductions survive

Let J select the fixed compact normal color/weak splitting, let omega_c(J) be its real color Kahler2-form, and set theta(J)=omega_c(J) wedge omega_c(J). Then alpha_J(n)=iota_n theta(J) is a nonzero real normal degree3 tensor. It is source-sharp-skew, C-compatible, block-Lorentz scalar and geometricSM-equivariant. Its contraction is4theta(J), not zero. The family transforms covariantly when J transforms; its value at fixed J is not invariant under all endogenous Lorentz transformations. Thus the optional-C zero cannot be applied to a moving-reduction family merely by citing covariance. No such family is adopted as a physical completion here.

For the four-parameter fixed full-U class, rank64 occurs precisely when exactly one of (a+d,b-c) and (a-d,b+c) vanishes. Both vanish only at a=b=c=d=0. Otherwise rank128. Each pair corresponds to an entire ambient half, not a selected physical chirality or generation. The exact probe also retains the excluded even-normal vector multiplicities at degrees4/6 and the invariant degree5 volume forms; dropping them is justified by ambient parity, not by claiming they do not exist.

## 6. Auxiliary response: actual connections matter

This section uses the held W2/K95/full-U candidate and its own **opposite Clifford-adjoint convention**, never the source tensor convention used in sections1–5. Both certified kappa1 homogeneous roots are included. No physical state space is added. The restricted variations below are diagnostic test fields; no source superselection rule is imposed.

Inputs: [affine homogeneous geometry](source-action-homogeneous-analytic-vacuum-2026-11-25.md), [all59 full-Lorentz invariant tensors](source-action-dynamics-and-continuation-2026-11-25.md), [actual closed-time constraints](source-action-kappa1-constraints-2026-11-25.md), [complete6/7 certificates](source-action-reduced-evolution-2026-11-26.md) and [exact120-envelope/scalar response](source-action-weak-response-2026-11-26.md). Their inverses are reused, not recomputed or silently extended.

### 6.1. Time-line stabilizer is locally transitive

Let p=(0,eta), tau=dt, and let `G_tau` consist of the connected affine
transformations with `A^T tau=lambda tau`, lambda>0. Translations are unrestricted.
On the open metric-bundle patch where dt remains timelike, G_tau is locally
transitive. One explicit construction begins with the existing analytic section
`g(S)=exp(S)`, `y=g(S)^(-T) eta g(S)^(-1)`. The timelike row `tau g(S)` can be
sent analytically to `lambda tau` by a local Lorentz matrix h(S), with h(0)=I.
Set A(S)=g(S)h(S). It still represents y and now preserves the time line. This
is a local smooth/analytic boost choice near eta, not a global gauge choice.
The connected stabilizer of p inside G_tau is SO3: a Lorentz A preserving the
time line has lambda=1, and fixes the future unit time vector.

The symbol kernel P depends only on the line of tau. Scaling tau by a nonzero
lapse does not change P or R. The closed-time cancellation remains the theorem
for the actual closed dt; no nonclosed normalized one-form is substituted into
that theorem. The actual constraint M then depends on P,T and natural algebraic
operations, so it transforms by conjugation under G_tau. Every59 coefficient
tensor is invariant under the full connected Lorentz isotropy, hence defines
the already-owned affine invariant T section. This is not merely SO3 covariance.

### 6.2. Q and its induced connection are defined without an arbitrary complement

At p take `V_5=K_dt b_5` and `V_12=K_dt b_12`, using the native36-vector
highest7 basis in the owned probe. Let Q_p be the real SO3 module generated by
these two vectors and their realifications. Each is one spin7 copy. The sparse
check below verifies that rotation diag(1,-1,-1,1) sends each V to its complex
conjugate, so each copy is stable under the native reality operation (the
overall physical-i convention changes no nondegeneracy conclusion).

The exact highest-weight Hermitian Gram is

    [ 3145728        0 ]
    [       0 -9437184 ].

Invariant pairing and the nonzero standard lowering factors imply that the full
two-copy real Q_p (dimension30) is nondegenerate. Distinct copies remain
orthogonal. Thus `R=Q direct_sum Q_perp` supplies the native orthogonal projector
Pi_Q and actual induced connection `nabla^Q=Pi_Q nabla^R`, without selecting a
positive physical metric. Transport Q_p with G_tau to obtain a local analytic
subbundle Q of R. SO3 invariance makes this independent of the chosen adapted
frame, and native nondegeneracy persists under the isometries.

### 6.3. Known inverse on the principal source bundle

Let `L_Q^a=P K^a i_Q`. At p, Q has spin7, while tangent/cotangent types have
spin at most2. The ambient carrier has no spin above7. Therefore these sources
have only spins5,6,7. The existing complete6/7 inverses cover those components.
For spin5, the normal spin2 tensor product has multiplicity one in
`Hom_SO3(V2 tensor V7,V5)`; the two highest5 source vectors already checked in E
determine the entire source map on both Q copies by equivariance. Horizontal
spin1 sources cannot reach spin5.

Generate U_p by the SO3 orbit of the certified highest5 E plus its conjugate,
and the complete N6 and N7 sectors. Each M(T_j) commutes with SO3 and reality.
Consequently U_p is invariant, and the existing E and6/7 inverse certificates
give its inverse. Adding conjugate invariant subspaces cannot introduce a
kernel: inverses agree on their invariant intersections, so the sum is
invertible. No new numerical inversion is needed. Transport U_p to U_y with
G_tau. `M|U` is analytically conjugate to its certified value at p for each held
root. In particular

    Y_Q^a=(M|U)^(-1) L_Q^a

is an actual analytic tensor in Hom(Q,N) with its vector/covector index, not a
formally assigned jet. Pointwise it agrees with the held particular responses.

### 6.4. Include the second fundamental lower source

Write the actual Hessian covariantly as `H=K^a nabla_a+J`,
`J=I+2N(T,.)`. For v in Q, decompose its R derivative as

    nabla^R_a(i_Q v)=i_Q nabla^Q_a v+B_a v,
    B_a:Q -> R intersection Q_perp.

The N part of the full derivative of i_Q is annihilated in the projected
principal term by `P K^a P=0`. Therefore exactly

    P H(i_Q v)=L_Q^a nabla^Q_a v+C_Q v,
    C_Q=P J i_Q+sum_a P K^a B_a.

There is no license to discard B_a: the exact diagnostics below show it is
nonzero. All operations in C_Q are natural under G_tau. At p, C_Q is an SO3
intertwiner Q7 -> N and consequently lands in the COMPLETE N7 sector. The
existing N7 inverse defines the actual smooth lower response

    Z_Q=(M|N7)^(-1) C_Q.

The zero time-principal source `P K_dt=0` permits the same spatial/normal
decomposition used in the owned weak formula. For every smooth local section v
of Q, including compactly supported test sections, set

    n=-Y_Q^a nabla^Q_a v-Z_Q v.

The owned closed-dt identity `P H n=M n` then gives

    P H(i_Q v+n)=0

as an exact local equation. This is constrained test-field elimination. It does
not solve the remaining R equation or the nonlinear coupled field equations.

Differentiating the genuine identity `M Y_Q^b=L_Q^b` now gives every individual
equation

    M nabla_a^(N,HomQ) Y_Q^b
      =nabla_a^(N,HomQ) L_Q^b-(nabla_a^N M)Y_Q^b,

with actual induced N/Q connections and the tangent-index connection. The frame
derivatives and density enter the formal adjoint as usual; they are not frozen.
These are Hom(Q,N), not Hom(R,N), equations.

### 6.5. Consequence for the existing matched coefficient

The correct restricted weak current is

    j_eff,Q=j_R i_Q-j_N Z_Q+div_(native density,nabla^Q)(j_N Y_Q).

At p the derivative-free seed-current map annihilates the complete spin7
carrier. The term `j_R i_Q`, the lower response Z_Q, and the contracted
current-independent derivative/frame/density correction are all spin7 by SO3
equivariance, so their seed-current values vanish. Separate the product rule into (partial_a j_raw) with ambient-frame test coefficients held fixed, evaluated on the same pointwise Y_Q^a V, and j_seed applied to every derivative of Y, i_Q, Pi_Q, the actual connections, frame and density. The first part agrees with the old coefficient because only the same point values enter. Every new fully contracted geometric term, including the second fundamental lower correction, is an SO3 map Q7 into the complete geometric-spin7 carrier and is seed-current blind. No individual derivative is discarded. The surviving terms are therefore the same fixed-frame matter-current derivatives evaluated on the same pointwise Y responses as the four existing certified coefficients. Thus the restricted
local weak coefficient inherits those nonzero intervals. This supplies a route
from the former formal coefficient to a local constrained-Q coefficient.

This argument does not establish full-R auxiliary realizability, arbitrary
matrix-entry/kernel independence, all-Gram normalization, a specified globally
admitted support/domain, the reduced dynamical equations, a physical ghost,
candidate necessity, or a GU verdict. It does not adopt Q as a physical
superselection rule. Its purpose is to realize the already-chosen diagnostic
variation family. This analytic upgrade is subject to the independent review linked below; it is not a formal Lean proof.

### 6.6. A genuine compactly supported local test

There is also a support consequence. Choose one of the certified real Q directions and local analytic independent matter row/column germs whose Hermitian polarization makes the restricted weak coefficient nonzero at p. Its real coefficient keeps its sign on a smaller chart. Extend that Q direction smoothly and multiply it by a nonnegative smooth compact bump to obtain v. Set n=-Y_Q^a nabla_a^Q v-Z_Q v. Both i_Q v and n are compactly supported and satisfy the homogeneous linearized auxiliary constraint P H(i_Q v+n)=0 exactly. Native-density integration by parts, with no boundary term, gives

    integral j(i_Q v+n) = integral j_eff,Q(v) != 0.

Only the test perturbation is cut off; the matter solutions are not. Thus the earlier nonzero formal coefficient is realized as a nonzero **local matter-current first-variation functional on compact constraint-satisfying test connection perturbations**. This is not the full remaining R-Euler equation, a sourced nonlinear constraint solution, a propagated response, an all-Gram claim or a source-admitted physical state. Q is a diagnostic test family, not an adopted physical restriction.

### 6.7. Why full-R jets remain a genuinely new finite burden

Use the adapted frame from A1. In this frame M and principal source tensors have
constant pointwise matrices. If Gamma_N,Gamma_R are the actual induced
connection matrices, differentiating an operator `Y:R->N` gives schematically

    r_ab = M Gamma_N,a Y_b - L_b Gamma_R,a + Gamma^b_ac L_c.

Hence, after the terms manifestly in range(M) are removed, the cokernel test is
the class of `L_b Gamma_R,a V`. For an adjoint kernel vector k the exact witness
is `<k,L_b Gamma_R,a V>`. A nonzero value proves incompatibility of that stated
full-range jet; it is NOT furnished by merely finding a component outside U.

In the homogeneous normal frame Lambda_a=0 for normal a. To time-adapt at
normal axis10 requires the Lorentz boost H03 (up to the passive/active sign),
because `A[10-4][3,0]=-1`. Thus Gamma_R,10 contains `R rho(H03) R`. Let

    W6 = (56-Casimir)/14 * R rho(H03) V,
    L4 = product_(j=5,6,7)(Casimir-j(j+1))/(20-j(j+1)) * P K^5 W6.

The exact sparse probe finds:

| V | W6 support | nonzero W6 coefficient | L4 support | nonzero L4 coefficient |
|---|---:|---|---:|---|
| K_dt b5 |128|(form32,Clifford757)=-4/3|344|(form1,Clifford759)=-i/18|
| K_dt b12|192|(form32,Clifford5733)=-48i/7|472|(form1,Clifford5735)=4/15|

Casimir identities verify eigenvalues42 and20 exactly. The H13 boost gives the
corresponding i-related spin6 direction; H23 gives zero spin6 on these highest
vectors. Normal axis8 gives i times the displayed spin4 source. This proves
that full-R induced derivatives leave the already-inverted5/6/7 source sector.
It is NOT a cokernel obstruction: M may invert the reached spin4 source.

The cheapest full-R successor is to use these exact reached spin4 sources
(and any additional spin5 remainder outside the certified E orbit), reduce only
their M-generated receiver module, or exhibit an actual adjoint kernel vector
paired nontrivially with one. No need to rebuild all49154 dimensions. Cost is
not yet known: the initial sparse vectors are inexpensive, but their invariant
closure and exact root-ball inverse may grow. Do not predeclare a huge inverse
mandatory, and do not call it blocked on new source input. All coefficients are
already owned candidate geometry.



## 7. Epistemic status and continuation

- **ESTABLISHED:** the complete fixed tensor spaces, coefficient contraction kernels/images and native finite Clifford controls above, subject to the listed review record. The four full-U survivors are algebraic tensors, not physical states.
- **RULED OUT:** a nonzero tensor satisfying all fixed endogenous/weak, source-sharp-skew and optional-C conditions simultaneously. It is an internal class exclusion. No source claim is falsified by it.
- **NOT MODELED / UNDETERMINED:** source selection of fixed versus moving reductions, mandatory C, physical VEV/domain/readout, curvature suppression, and all GU-level consequences. Interpretive architectures remain not modeled, not absent.

The normal finite classification is consumed. Do not restart it as a larger matrix solve, an ordinary Higgs no-go, or a repeated generation count. For the candidate response, the natural moving-Q construction resolves local auxiliary compatibility for the already-tested diagnostic family; full-R jets now have explicit reachedspin4 sources. A new on-shell claim must supply its actual transforming VEV/reduction, operator and observation map. Full-U, moving-reduction and opposite-pairing cases survive with the distinctions above. Existing source-custody and anomaly applicability audits are not reopened without new evidence.

Choice inventory remains10 grouped families /4 viability bundles /bookkeeping net6 /zero source-selected predictions. This is not a GU necessity lower bound. No new physical family, schedule, governance, source/canon/physics verdict or paper release.

## 8. Verification boundary

[Exact probe](../../tests/program-focus/source_normal_tensor_class_probe.py) independently enumerates1024 exterior weights with integer6Y and Weyl-denominator extraction, passes438 exact controls, checks all1800 native normal vector equations, native sharp/C and actual contraction identities, and joint-block rank fixtures without floating rank tests. The written representation proof establishes completeness and arbitrary-parameter rank strata; fixtures alone do not. [Lean finite core](../../Lean/GUFormalization/NormalTensorClass.lean) checks coefficient incompatibility, injective10-factor contraction and arithmetic, not Clifford completeness, Lie generation, analytic domains or source relevance.

[Evidence](../../lab/process/source-normal-tensor-class.json) preserves exact controls, input hashes and the compact20-lens delta pass. [Independent reviews](../../lab/process/hostile-reviews/2026-11-26-source-normal-tensor-class-review.md) distinguish mathematical verification from construction/source validation. Native gates and replay are reported there.
