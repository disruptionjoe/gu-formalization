---
title: Positive local currents require a state restriction in the tested ambient fermion classes
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-MASS-GAP
tier: T1
expected_delta: Resolve the nonparallel positive-current escape left by the reference-holonomy result
actual_delta: A same-sign normal direction forces every nonnegative zeroth-order local conserved density to vanish in the stated time-regular ambient symbol classes; a visibly observed RS block independently prevents retention of literal observation
class_covered: Existing completed wedge/southeast family with nonzero constant real chiral weights, and scalar-coefficient natural two-channel family with a e g (a+13c) nonzero; full ambient one-form plus scalar spinors, unrestricted equation first jets, arbitrary smooth lower terms, and Hermitian zeroth-order quadratic local currents
premises:
- lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md authenticates draft p46 eq9.16 and independent bars; it does not select a physical current or domain
- explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md section1 owns the completed symbol and coordinate conventions
- explorations/conditional-build/source-natural-symbol-class-2026-11-24.md owns the natural module; nonscalar tensor coefficients are outside this subclass
- Conservation holds on all equation-compatible first jets; analytic noncharacteristic germs realize these jets, but a restricted physical domain need not
source_bridge:
  status: conditional
  reason: SC-OP-04/05 supply candidate grammar and unselected southeast rivals; SC-META-53 is uncertain. The source does not select this completion, unrestricted physical domain or Hermitian local probability current.
kill_condition: A nonzero nonnegative local density compatible with the actual extra-time coefficient invalidates the exclusion; wrong symbol or first-jet admission invalidates transfer, not GU
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-AMBIENT-LOCAL-POSITIVE-CURRENT
internal_target_verdict: Scoped local-current exclusion; physical restricted-domain and observed-balance mechanisms remain open
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# Positive currents: the domain is essential

program_target: BET-MASS-GAP
tier: T1
expected_delta: Test nonparallel and even degenerate positive Cauchy densities on actual ambient fermion symbols.
actual_delta: Every such local density vanishes in the stated unrestricted-jet classes. The observed RS witness cannot acquire positive norm by this construction.

**A positive physical norm need not be a parallel fibre metric. This test allows that freedom.** It allows a moving, hypersurface-dependent Hermitian form, arbitrary mixing of spinor copies and degeneracy on hidden data. The obstruction comes instead from an additional timelike derivative in the actual full ambient symbol.

- **ESTABLISHED:** the symbol/current identities below force the nonnegative density to vanish for the quantified classes. A small observed block independently rules out retaining all literal observation.
- **RULED OUT:** a nonzero positive Cauchy norm supplied by a zeroth-order Hermitian local conserved current on those unrestricted ambient equation jets.
- **NOT MODELED / UNDETERMINED:** source-selected physical state space, interacting nonlocal norm, BRST quotient, quantized fermionic probability, physical energy or mass gap, observed4D balance law, or a GU verdict.

```gu-typed-objects
result: ambient local-current compatibility and visible RS witness
carrier: E=(T*Y tensor S128) direct-sum S128 with all15 spinor copies, q=(literal horizontal one-form, full gamma trace, scalar) LAYER=ambient+observed BRIDGE=held-section-contraction CHIRALITY=S-FULL-DIRAC
pairing: arbitrary proposed positive-semidefinite Hermitian density H, not an identification of independent barred fields or native Krein pairing ON=full_ambient_fermion_carrier
real_structure: complex spinors over separately declared K95 and K77 metric ports; no real-form or adjoint identification
grading: ambient chirality for coefficient weights, not physical chirality or generation count
action_owner: repository-construction -- existing fermion symbol families, no new action or physical-current choice adopted
target: conservation compatibility of a proposed local state current MAP-TYPE=restriction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** A nonnegative classical state current is not a physical quotient, quantum probability or energy. Independent bars are not set equal to Hermitian conjugates. The source's nonchiral2+1 mechanism is not replaced by repeated ordinary families. Read [source-native routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Reuse and source custody

Basis `ea258fc59e0312c2d44ffefa50f4815cad521f3d`; counter115 selects LC-BETS. MASS-GAP and COSMOLOGY each had19 runs remaining. This test uses an already supplied symbol and resolves its immediate current-transfer question. The tied cosmology option needs an unselected normal integral and boundary domain. No new action, connection, state restriction or norm is adopted.

The [reference-holonomy result](bet-mass-gap-reference-holonomy-2026-11-27.md) excludes parallel positive fibre forms, while expressly retaining ordinary Dirac Cauchy norms. The [normalized-time result](bet-2plus1-evolution-complement-2026-11-27.md) classifies tangent evolution/complements, not a normal-direction6S system. [Source quotient work](source-symbol-quotient-membership-2026-11-12.md) owns tangent Jordan/semisimple distinctions; [W2 construction](source-action-wave2-construction-2026-11-25.md) already warns about extra-time frequencies. [K2203](k2203-observed-lower-pairing-compatibility-2026-10-28.md) excludes a different subsystem's local current using its mass terms. These results are reused, not claimed anew.

The new transfer is **all positive-semidefinite local densities for the full normal symbol, including horizontal semisimple survivors, and retention of actual literal observed data**. Symmetrizer theory is standard; see [Métivier §2.3.3](https://www.math.u-bordeaux.fr/~gmetivie/CoursPiseMars08.pdf). We prove the semidefinite version directly. No world-novelty claim.

SC-OP-04 (draft p46 eq9.16) supplies scalar/one-form grammar. SC-OP-05 leaves nonzero southeast rivals unselected. SC-META-53 (TOE2025 01:22:30) leaves indefinite-spectrum handling open and proposes compact shielding. These do not require the tested current/domain. SC-GEO-51's full U(64,64) is not silently narrowed to Sp(32,32). The [primary extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md) and [source-current dictionary](source-prescription-current-2026-11-13.md) retain independent bars.

## 2. Necessary current compatibility

For a noncharacteristic physical-time covector tau normalize the actual system:

    partial_t u + sum_j E_j partial_j u + V u = 0.

Take a real quadratic local current

    j^0=u†H(t,x)u, j^j=u†J_j(t,x)u,
    H=H† >=0, J_j=J_j†.

Absorb smooth density factors into these matrices. Conservation on **every equation-compatible first jet** implies, by comparing independent spatial derivatives,

    J_j = H E_j = E_j† H.                            (1)

The remaining zero-order equation contains derivatives of H,J and V; it cannot alter(1). Moving forms, normal-dependent forms, lower-order connections and scalar integration weights are allowed. This is not an unrestricted smooth Cauchy theorem. Analytic coefficients with invertible time coefficient admit local analytic Cauchy–Kowalevski germs realizing these finite jets; a restricted physical domain requires its own jet-admission proof.

If E_eta²=-I, (1) gives

    E_eta† H E_eta = -H.                              (2)

Both the left side and H are nonnegative, hence H=0. Indefinite conserved pairings are not excluded.

More generally, if E_eta has no real eigenvalues, (1) preserves ker H. The induced map on E/ker H is selfadjoint in its induced positive form, and would have a real eigenvalue if that quotient were nonzero. Its spectrum is contained in the original spectrum. Thus H=0, including Jordan cases and arbitrary copy mixing.

## 3. Completed native wedge/southeast family

Reuse [chiral-weight transport](bet-2plus1-chiral-weight-transport-2026-11-25.md) §1 and [local-complement normalization](bet-2plus1-local-complement-2026-11-27.md). All15S components are retained. q is a tangent quotient, not an autonomous normal-direction operator.

For nonzero real w_+,w_-, set W=w_+P_++w_-P_-, Wsharp=w_-P_++w_+P_-, p=w_+w_-. Sharp exchanges weights, not adjoints. The completed SE weight is cW/p. Probe slot conventions are:

| Port | gamma0² | Same-sign normal | sigma | c |
|---|---:|---|---:|---:|
| K95 | -1 | a negative normal slot | +1 | -11/12 |
| K77 | +1 | a positive normal slot | -1 | +11/12 |

The authenticated simultaneous coordinates give

    R^-1 D_k R = M_k tensor Gamma_k, Gamma_k=gamma_k Wsharp.

For u=(u0,...,u13,h),

    (M_k u)_k=h,
    (M_k u)_i=sum_(j not i,k)u_j (i!=k),
    (M_k u)_h=r u_k+s h,
    r=sigma/p!=0, s=-(11/12)r.

M0 is invertible: its13 spatial slots have all-ones-minus-identity matrix with eigenvalues12,-1; its time/scalar block has determinant-r. For k!=0 put S=sum_(j>0)u_j, B=h-S+u_k and a=11/12. Directly,

    N_k=M0^-1 M_k,
    (N_k u)_0=u_k-aB, (N_k u)_k=u0-aB,
    (N_k u)_i=u_i+B/12 (i>0,i!=k),
    (N_k u)_h=S-u_k.                                 (3)

B maps to-B, so a second application restores all components. Thus N_k²=I for every weight. The spinor factor alpha_k=Gamma0^-1 Gamma_k=gamma0^-1 gamma_k also loses its weights and commutes with N_k. Consequently

    E_k=N_k tensor alpha_k,
    E_k²=-(eta_k/eta_0)I.                             (4)

A same-sign normal has square-I and triggers(2); an opposite-sign direction has square+I. The overall minus convention for evolution does not change the result. Variable invertible state frames transport H by congruence; invertible equation-row changes cancel in normalized evolution. Their derivative terms are lower order. This is not a coordinate artifact.

For arbitrary scalar SE ratio t=s/r, (3)'s first component becomes u_k+tB. Still B'=-B, and

    N_k²-I=(t+11/12)(e_k-e_0) tensor ell_k,
    ell_k(u)=B, (N_k²-I)²=0.

Thus SE0 supplies a Jordan countercontrol, not a positive-current rescue. The next section gives an independent wider scalar-coefficient proof without assuming this factorization.

## 4. Natural scalar family, including uncompleted SE

In the already classified [natural module](source-natural-symbol-class-2026-11-24.md), let a,c,e,g,s be scalar complex coefficients on the full spinor:

    M(xi)(zeta,nu)=(
      a c_xi zeta-a xi Gamma zeta+c J(i_xi zeta-c_xi Gamma zeta)+e xi nu,
      g i_xi zeta+s c_xi nu).

Here c_xi denotes Clifford multiplication, c a coefficient, Gamma J=14, i_xi J=c_xi, q_xi=xi². Assume a e g F!=0, F=a+13c. Independent chiral extension of this entire family is not asserted; the completed chiral family is covered in §3.

For q_xi!=0, uniquely split zeta=xi u+Jv+r0, with Gamma r0=i_xi r0=0. The contraction/trace system has Schur factor13. Substitution yields components

    transverse r0: a c_xi r0,
    xi:             -12a v+e nu,
    J:              -F c_xi v,
    scalar:         g q_xi u+g c_xi v+s c_xi nu.

Vanishing forces r0,v,nu,u successively to zero. M(xi) is invertible for every complex nonnull xi. The same decomposition produces a kernel at nonnull xi whenever a e g F=0; such singular-time members require a constraint analysis and are outside this theorem.

For orthogonal unit real tau,eta with the same sign, (eta-lambda tau)²=eta0(1+lambda²). Every eigenvalue of M(tau)^-1 M(eta) therefore lies in {i,-i}. The quotient proof after(2) gives H=0, including nonsemisimple scalar SE0/rivals. This is not the full18-generator module or arbitrary tensor/derivative-dependent Shiab.

## 5. A visibly observed RS witness

In the raised-form coordinates choose horizontal spatial slots1,2:

    zeta1=psi, zeta2=-gamma2^-1 gamma1 psi,
    other slots=0, nu=0.

This rank128 block W0 has Gamma zeta=0 and i_tau zeta=i_eta zeta=0. Clifford multiplication by tau,eta and chiral weights preserve it: the defining two-gamma relation commutes with them. The contraction/gradient terms vanish and normalized time/eta evolution squares to-I. Literal O0=(zeta_H,nu), hence also augmented q=(zeta_H,Gamma zeta,nu), is injective on W0.

Even this block alone forces H|W0=0 by(2). If H>=0 on the full carrier, W0 is in its radical. Neither ker H subset ker O0 nor the stronger H>=epsilon q†q, epsilon>0, can hold. This is an observed field direction, not a physical-family count.

More general SE arrows leave this witness untouched when full time regularity and W0 invariance survive. This is a conditional test, not automatic coverage of every source-native operator. Removing W0 in a physical quotient requires a bridge explaining how the required observed matter remains; no such quotient is prohibited by assertion.

## 6. Controls and untested escapes

**One-time Dirac:** normalized spatial matrices are Hermitian; H=I gives a positive free current. The diagnostic does not mistake Lorentz boosts/indefinite covariant pairings for negative probability.

**Indefinite current:** E=[[0,1],[-1,0]] and H=diag(1,-1) satisfy HE=E^T H. Positivity, not conservation alone, is at issue.

**Restricted Fourier norm:** set E(k,l)=k diag(1,-1)+l[[0,1],[-1,0]]. E²=(k²-l²)I. On |l|<|k|,

    H(k,l)=I+(l/k)[[0,1],[1,0]]>0,
    HE=diag((k²-l²)/k,-(k²-l²)/k).

This positive conserved norm for the frozen restricted system is frequency-dependent and uniformly positive only away from the cone boundary. It is not a common zeroth-order local density for all normal derivatives. It calibrates an escape, not an interacting GU domain. The [existing polarization gate](selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md) already distinguishes this category.

Other open categories: derivative-valued currents, nonlocal norms, constrained physical jets, changed principal tensors, singular-time constrained systems, and separately derived observed4D balance laws with normal flux. Lower terms cannot change(1) but may help specify restricted states. A positive norm for a homogeneous ODE is not this spatial-jet test; finite-time estimates are not exactly conserved local currents.

## 7. Scientific effect and acceptance ceiling

Compact shielding in these classes requires an explicit **physical state/domain/current bridge**. A compact reduction or arbitrary nonparallel positive local density does not supply one on the unrestricted ambient state space. The result is structural across quantified coefficients/lower terms, conditional on the symbol and jet premises, not source-necessary or exhaustive of class C.

No choice family is added. W2's historical10/4/net6/0 remains its own inventory, not this family's budget. No physical mass gap, ghost, Hamiltonian sign, selected prediction or GU verdict follows.

[Evidence](../../lab/process/bet-mass-gap-local-current.json) records exact controls and independent review. Lean certifies the nonnegative anti-isometry contradiction and finite arithmetic, not the PDE jet argument, natural-symbol module or source interpretation. Internal review is not external validation. Lane-C results do not automatically enter scientific matrix cells or ledger rows.

The current test is consumed; another local positive-matrix search under these premises is redundant. Future shielding work needs a supplied restricted domain/current, its preservation and observed-matter bridge. Joe27r's wedge own-dynamics/energy work remains the ordinary-B continuation with its remaining budget.
