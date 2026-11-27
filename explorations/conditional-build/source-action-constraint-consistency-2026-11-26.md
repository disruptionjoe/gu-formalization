---
title: First constraint consistency reduces to two existing sources and fibre multiplier data
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T2
expected_delta: Test the actual differentiated auxiliary constraint without an unrestricted inverse
actual_delta: The pure geometric multiplier sandwich is order zero; horizontal kernel derivatives vanish modulo the constraint image. The two tested horizontal spin5 consistency classes are minus census cases8 and17, with all normal and zero-order multiplier repairs retained.
class_covered: Compatible parallel constant-rank connection symbols with an exact non-null time form; horizontal cancellation and source identification additionally require the owned Lorentz-invariant W2/K95 background family, including both real zero-matter kappa1 roots.
premises:
- 'source-action-kappa1-constraints-2026-11-25.md section1: closed-time operator identity, actual M, native nondegenerate N/R splitting'
- 'source-action-homogeneous-analytic-vacuum-2026-11-25.md A1-A3 and source-action-dynamics-and-continuation-2026-11-25.md: complete horizontal Lorentz invariance of the59 family'
- 'source-normal-tensor-class-2026-11-26.md sections6.1-6.4: local transitivity and actual Q primary lift; plus-comparator tensor claims in its earlier sections are not imported'
- 'source-action-q7-propagation-2026-11-26.md: actual remaining range equation and owned coupled quadratic autonomy'
- 'source-action-firstjet-source-census-2026-11-26.md: exact source cases8/17 and receiver coverage'
source_bridge:
  status: conditional
  reason: Consistency is necessary for the named candidate initial jets. W2 and freely initialized Q jets are not source-required physical states; no GU or physical-ghost verdict follows.
kill_condition: Only a native dual annihilating the full M image and every allowed normal/zero-order kernel-multiplier image can obstruct these initial jets. Old-receiver nonmembership and incomplete propagation do not exclude W2, class C or GU.
---

# First constraint consistency: the actual obstruction is smaller than the calculation

program_target: LB-CLASS
tier: T2
expected_delta: Test actual differentiated constraints without an unrestricted inverse
actual_delta: Pure geometry is order zero; horizontal kernel derivatives vanish modulo im M; the two tested spin5 second-jet classes reuse minus census cases8/17. Normal and zero-order multiplier repairs remain.

Basis: freshly fetched `fbc2f6517d61395c8d92db90a254c4db473da7ef`.

## Result in plain terms

The **two tested horizontal spin-5 second-jet components** of the first consistency test can reuse already computed vectors with **56 and 80 terms**, rather than assemble a new large derivative operator. This is a proved connection to the equations of motion; the earlier unrestricted inverse extension remains optional.

Three ordinary spatial derivatives of the undetermined constraint variables cannot change the relevant consistency class. Their **ten metric-fibre derivatives and derivative-free coupling can still change it**. These are existing unknowns, not a new physical completion. Neither vector has been proved to give a nonzero final obstruction.

The result applies inside the autonomous imaginary-connection block of the complete quadratic candidate at both held real zero-matter roots. It does not establish a physical quotient, actual solution propagation, runaway exchange, a small-h continuation path, or a GU falsification. Source2+1, observed/total grading, literal contraction, independent matter fields, primary-minus adjoint, K77/K95 and geometric/physical spin remain distinct.

```gu-typed-objects
result: actual first-time consistency class and multiplier-symbol reduction
carrier: W2 K95 imaginary-U connection forms; N=ker K_dt, R=N-perp, Z=ker M LAYER=ambient BRIDGE=physical_admission_unproved CHIRALITY=N/A
pairing: native indefinite imaginary-U trace/form pairing ON=declared_carrier
real_structure: native real U64_64 coefficients; highest-weight complexification only for exact source arithmetic
grading: geometric SO3 spin and differential order; not physical chirality or family count
action_owner: repository-construction W2 action, actual quadratic Hessian
target: J2(Q) to coker of the full augmented first-consistency map MAP-TYPE=homomorphism
```

## 1. Exact consistency, including every undetermined variable

Use the actual stationary equations

    A partial_t v + Bv + En = 0,
    Dv + Mn = 0,

with A=K_dt invertible on R and G its inverse, zero on N. B,D,E contain the complete spatial and lower terms; M=P C P|N, C=kappa I+2N(T0,.). In this paragraph the polarized cubic map N(T0,.) is distinct from the time-kernel bundle N. P is the native orthogonal projector; positivity is not assumed.

The owned G_tau transitivity and conjugacy theorem makes the rank of the **full M** locally constant at each root, without computing that rank. Thus Z=ker M and coker M are genuine smooth/analytic bundles. No nondegeneracy of the pairing restricted to Z is needed.

For any initial v with an owned primary lift n0, every other primary lift is n0+k, k a section of Z. Set

    L=DGE,
    F0(v)=DG(Bv+E n0(v)).

Differentiating the primary equation gives exactly

    M n_t = F0(v)+Lk.                                      (1)

For the owned first-order Q lift, F0 depends on at most the second spatial jet of v: the naive cubic term cancels by the existing sandwich identity. In a stationary kernel frame let L=L0+sum_a La partial_a. First time-derivative jets at p exist if and only if

    F0(v)(p) is in im [ M | -L0|Z | -L1|Z | ... | -L13|Z ]. (2)

Necessity follows from (1). Conversely, any values and first spatial derivatives in Z are realized by a local analytic kernel germ, since its rank is constant. Choose that germ and n_t(p), and use the range equation to fix v_t. This satisfies precisely the first differentiated constraint at p. It does not solve the multiplier PDE on a neighborhood or the higher consistency chain.

Intrinsically the augmented map is M direct_sum (-ell), where ell:J1(Z)->N is induced by L. Changing kernel frame or the particular primary lift leaves its cokernel class unchanged. With time-dependent coefficients the exact replacements are F0=DG(Bv+E n0)-D_t v-M_t n0 and L=DGE-M_t; those terms cannot be silently omitted outside the stationary category.

## 2. A stronger geometric cancellation

The existing closed-time theorem gives the **operator identity**

    P_tau K P_tau=0

for every closed non-null tau, with K itself independent of the selected time function. Vary tau to dt+epsilon df for an arbitrary local scalar f. The owned projector derivatives give

    dotP P=-G K_df P,       P dotP=-P K_df G.

Differentiate the operator identity and sandwich by P:

    0=P dotP K P+P K dotP P
     =-P K_df G K P-P K G K_df P
     =-[P K G K P,f].

Thus **P K G K P has order zero**: it commutes with every scalar multiplication. This keeps all moving-projector, lapse, frame and density contributions; it does not assume they vanish separately. An independent derivation expands the derivative of G and uses the cubic polarization of the constant-rank symbol pencil.

Consequently the actual first-order symbol of L is only

    L1(xi)=P K_xi G C P+P C G K_xi P
          =-P (delta_xi(P_tau C P_tau)) P.                 (3)

The derivative on the second line varies the time covector while holding C fixed. It is a projected derivative on the moving N bundle, not a derivative in an arbitrary unrecorded trivialization. The zero-order part of L is not shown to vanish.

## 3. What Lorentz symmetry removes, and what it leaves

Every member of the owned59 background family is invariant under the full connected horizontal Lorentz isotropy, including boosts. This is stronger than SO3 invariance. For a horizontal spatial xi choose the boost S with [S,A]=K_xi and put j=P S P. Covariance of C and P gives

    L1(xi)=M j-j M.

For k in Z, therefore, L1(xi)k=M(jk) is in im M. The radial time-covector direction merely rescales A and changes neither P nor M. Thus the ker-M to coker-M principal map vanishes for **all horizontal covectors**.

In (2), the three ordinary spatial derivative blocks may be removed modulo im M. The exact remaining map is

    [ M | -L0|Z | -L_normal,1|Z | ... | -L_normal,10|Z ].    (4)

Kernel-frame derivatives contribute to L0 and remain included. Normal covectors are not generated by the horizontal Lorentz orbit of dt. Normal derivatives can repair a source produced by purely horizontal initial jets; they cannot be discarded because the source was horizontal.

A decisive dual must annihilate every column of (4) and have nonzero pairing with the source. With the native nondegenerate N pairing, its M-annihilating row can be represented by a vector in Z even if Z is degenerate. The ordinary M-cokernel alone is still not the final obstruction.

## 4. Exact bridge to two existing source vectors

For V in the tested Q highest plane take s=P K_xi V and the owned preimage My=s. The matched quadratic source is

    r2=P K_xi G K_xi V-L1(xi)y.

For a unit horizontal xi choose S also satisfying [S,K_xi]=A. From projector covariance,

    P S R=P K_xi G,       R S P=-G K_xi P.

Using (3), P A=0 and P K_xi P=0 gives

    r2=P K_xi R S V-M(jy).                                (5)

Hence its class modulo im M is represented by P K_xi R S V. This equality uses the actual equation and existing horizontal preimage; it requires neither a new M inverse nor new derivative assembly. It holds at both roots. For an approximate y with residual e=My-s, the right side of (5) acquires the explicit correction +j e; a center evaluation must retain it.

In the native frame xi=theta0 and tau=theta3. Normal connection axis10 is Gamma10=rho(H03), and covectors transform by -H03 transpose. Therefore [Gamma10,K3]=-K0 and [Gamma10,K0]=-K3: **S=-Gamma10**.

The spin7 part of R Gamma10 V cannot reach spin5 under the rank1 horizontal symbol. Only its spin6 part contributes. This identifies the exact spin5 representatives:

| Q highest vector | Existing census case | Source terms | Sign in matched class |
|---|---:|---:|---|
| V5 | 8 | 56 | minus |
| V12 | 17 | 80 | minus |

Both are outside the old certified E5 receiver. That remains a coverage fact, not proof that their classes in coker M, or in the augmented cokernel (4), are nonzero. The other optional firstjet census columns do not become necessary by this argument.

## 5. Verification and inference controls

[Machine evidence](../../lab/process/source-action-constraint-consistency.json) · [exact certificate](../../lab/process/source-action-constraint-consistency-certificates.json) · [probe](../../tests/program-focus/source_action_constraint_consistency_probe.py) · [review](../../lab/process/hostile-reviews/2026-11-26-source-action-constraint-consistency-review.md).

Final exact bridge replay passed in 4.07 seconds. Both complete source fields match the frozen census, all59 backgrounds pass the signed boost check, and the two vectors are independent. The direct root0/V5 diagnostic took 76.76 seconds; its geometric first-order remainder is exactly zero. A separate corrected identity check passed with the nonzero1968-term residual correction retained. The timings concern different verification tasks, not an asserted whole-pipeline speedup.

Reproduce from an empty local cache:

```sh
python3 tests/program-focus/source_action_weak_response_probe.py --repo . --cache _local/constraint-consistency/e5 --unpack
python3 tests/program-focus/source_action_constraint_consistency_probe.py --repo . --cache _local/constraint-consistency --e5 _local/constraint-consistency/e5 --mode bridge --output _local/constraint-consistency/bridge.json
```

The optional `matched` and `center-check` modes retain the direct formula and explicit approximate-response residual. Their output is diagnostic only. The direct root-center calculation is **diagnostic only**: it checks the assembled formula, including the exact geometric first-order cancellation, but its approximate inverse coefficients cannot certify exact-root membership. The new signed boost bridge instead compares exact sparse vectors against the published cases8/17; the proof supplies root-independent interpretation. No full inverse or full propagation is claimed.

An exact two-dimensional algebraic control checks why multiplier columns matter. With G=[[0,1],[-1,0]], M=diag(1,0), E=E1 partial_x+E0, D=-E1^T partial_x+E0^T, E1=[[0,1],[0,0]], E0=[[0,0],[0,1]], one gets L=diag(0,-2)partial_x. The source e2 is outside im M but k=(x/2)e2 repairs it. With E0=0, L=0 and the same source is unrepairable. These are exact inference controls, not GU evidence or execution of the proposed GR/Stelle/Dirac comparator suites. They do not impose the additional native Lorentz-conjugacy hypothesis.

Two independent mathematical derivations and a hostile scope review support the structural reduction. These are internal simulated research roles, not external scientists. The quick20-description reassessment includes category theory and number theory; no separate agent was created per persona. No new Lean theorem is claimed for this T2 result; native premises and operator reasoning remain explicit reviewed mathematics.

## 6. Three-state conclusion and next decisive work

- **ESTABLISHED:** local constant rank of M; exact augmented first-jet criterion; order-zero pure geometric sandwich; horizontal multiplier derivatives absorbed into im M; the signed actual-equation bridge to cases8/17.
- **RULED OUT as an inference:** old E5 nonmembership by itself proves candidate inconsistency. The exact controls show why this inference fails. This is not a source or physical exclusion.
- **NOT MODELED / UNDETERMINED:** values of the remaining augmented normal/zero-order map, a nonzero final obstruction, closure of the full constraint chain, propagated negative-energy physical states, source necessity, or a GU falsification.

Next use the two sparse source representatives against (4): find a genuine augmented dual obstruction or an explicit multiplier/range repair. Native normal derivative blocks can be obtained directly from (3), without geometric derivative assembly. A claimed failure must include the zero-order multiplier term. A positive finite-stage result must retain the separate lower-order and propagation burdens. Do not expand all16 old uncovered sources or build another full-R inverse by default.

No action, norm, boundary condition, physical quotient or choice family is added. Choices remain10 grouped families/4 obligation bundles/net6/zero source-selected predictions. Program policy, schedules, source/physics/canon/class-C verdicts and scientific matrix cells remain unchanged. This is factual research continuation; Nov26(g) counterfactual suites remain proposal-only.
