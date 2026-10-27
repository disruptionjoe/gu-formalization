---
title: "K2117: Coherent control of quiet-field pulses requires a phase reference"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported operator and apparatus mathematics; no constructed local continuum controller, source selection, GU verdict or novelty
scripts:
  - tests/channel-swings/k2117_coherent_pulse_phase_probe.py
---

# K2117: Coherent control of quiet-field pulses requires a phase reference

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: conditional operational and analytic mathematics
carrier: supplied complex Hilbert CAR, finite code and ordinary external tensor reference LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric ON=declared_complex_completion
real_structure: CAR adjoint; no source-selected reality or barred-field identification
grading: fermion parity; energy sign, charge and source grades remain separate
action_owner: repository-construction -- supplied CAR and free massive Dirac dynamics
target: finite-factor instruments or specified free-Dirac scattering MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and prior-result boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite.
The imported positive CAR/Dirac construction is not source operator9.16.
K2021 local R0/R1 maps do not select its state, algebra or dynamics.
LT-SM8/LT-GR6b retain their action/observation/quotient/positivity debts.
Source register, ledger0.263 and canon verdicts remain unchanged. These results
answer reverse-scaffold coherence and causal-transfer demands; no GU recovery,
new substrate pathway, novelty or external certification is claimed.

## 1. The controlled object and the phase that becomes physical

Reuse the massive Dirac model of [K2115](k2115-exact-pulse-excitation-bound-2026-10-26.md),
with a fixed finite number of identical-mass flavors. Let B be a fixed Hermitian
flavor matrix and

    V_T(t,x)=T^-1 a(t/T) rho(x/T) B,  alpha=integral a,
    R=exp(-i alpha B),  R*=R,  R^2=I.

The matrix B commutes with the free Dirac operator h. For example alpha=1 and
B=pi Pi_- give the reflection R=I-2Pi_-. The compact smooth rho equals1 on
B_A, A>1. The K2115 kernel proof applies with different finite constants; it
already covers fixed Hermitian pulse matrices. Thus J_r(S_T) decays faster
than any inverse power at the endpoint. This is reused, not a new pulse proof.

Fix a finite positive-energy orthonormal frame F whose span L is R-invariant.
The ideal code operation is the exterior second quantization mathcal R=Gamma(R|L),
a reflection on the whole finite Fock code. It is NOT an arbitrary collective
reflection. Without R-invariance this is a transfer between different codes.
Prepare the code by J_F over the fixed sea vacuum Omega, all spectator
excitations absent. All external references are allowed.

The spatially uniform comparison potential has exact scattering R. Finite
propagation and agreement inside the plateau imply, for eta in(0,A-1),

    delta_j=||S_T f_j-Rf_j|| <=2 t_j((A-1-eta)T),
    t_j(r)=||1_{|x|>r} f_j||.                          (1)

Proof: split f_j into its part supported in the smaller ball and its tail.
The supported part remains in the plateau throughout0<=t<=T for both local
Dirac evolutions and has identical evolution. Each unitary maps the tail
with norm t_j, giving2t_j. The cutoff part need not have positive energy;
finite propagation holds on the full one-particle space. No positive-energy
compact-support assumption is made. This bound does not grow with ||B||;
K2115 excitation constants may depend on B.

The phase issue is the known distinction between controlling an operation and
knowing its channel. See [Araújo, Feix, Costa and Brukner](https://arxiv.org/abs/1309.7976).
We apply that distinction to the actual endpoint estimate; no novelty is claimed.

## 2. Calibrated controlled endpoint theorem

Let Uhat implement S_T on polarized Fock space. For J0=J_0(S_T)<1 set

    <Omega,Uhat Omega>=q exp(i theta), q>0,
    Ucal=exp(-i theta)Uhat,
    epsilon_T=sqrt(2J0)+(pi/2)sum_j delta_j.             (2)

The lower bound q^2>=1-J0 follows from K2115. Its auxiliary-memory proof gives
an OPERATOR-NORM isometry estimate, not merely agreement of reduced channels:

    ||Ucal J_F-J_F mathcal R||
       <=sqrt(2(1-q))+(pi/2)sum_j delta_j <=epsilon_T.  (3)

Indeed the calibrated vacuum distance is sqrt(2(1-q)); the finite CAR
encoding swaps differ by at most(pi/2)sum delta_j. Invariance of L identifies
the output-frame encoding J_(RF) with J_F Gamma(R|L), in the same ordered
creation convention. Equation(3) reuses the explicit sign-corrected K2115
intertwiner. Arbitrary excited spectators are not included.

For ancilla projectors P0,P1 define preparation isometries

    C_T=P0 tensor J_F+P1 tensor Ucal J_F,
    C_id=P0 tensor J_F+P1 tensor J_F mathcal R.

The difference has only the control1 block, so ||C_T-C_id||<=epsilon_T.
Tensoring an external reference leaves the norm unchanged. The pure-output
trace distance is at most the vector difference, and purification plus
contraction handles mixed inputs. Therefore

    (1/2)||Ad_C_T-Ad_C_id||diamond <=min(1,epsilon_T).  (4)

This keeps the ancilla and ENTIRE field output. The relative correction in(2)
is a physical ancilla phase gate, not permission to change the actual
implementer's phase for free. If only theta_est is supplied and
nu=theta-theta_est, channel telescoping gives the sharper bound

    error <= min(1,epsilon_T+|sin(nu/2)|).              (5)

The second term is exact: the eigenvalues of the ancilla phase gate are1 and
exp(i nu); its unitary-channel half-diamond distance to identity is
|sin(nu/2)|. A balanced control superposition attains it; minimization of
|1-p+p exp(i nu)| over p in[0,1] gives the matching upper bound, including
arbitrary references. Using vector distance without optimizing channel phase
would give the unnecessarily large2|sin(nu/2)|.

## 3. Sharp phase blindness and the noise channel

Replace a perfect implementer by its negative. Its one-particle CAR action,
J_r and all delta_j are unchanged and zero. But controlled action on
|+> tensor Omega produces |-> tensor Omega instead of |+> tensor Omega.
The full error is1. Thus none of the unconditioned field estimates can infer
a vanishing coherent-control error without a phase reference.

More generally classical independent phase noise with gamma=E exp(i nu)
acts on control block matrices by

    D_gamma([[A,B],[B*,D]])=[[A,conj(gamma) B],[gamma B*,D]],
    (1/2)||D_gamma-Id||diamond=|1-gamma|/2.             (6)

For an arbitrary input state including references, positivity implies
||B||1<=sqrt(Tr A Tr D)<=1/2. The difference is an offdiagonal block matrix
with trace norm2|1-gamma| ||B||1. A balanced pure control achieves equality.
The noise must be independent of the input and the field dynamics; a fluctuating
Hamiltonian correlated with phase is not represented solely by gamma.
For fixed nu, (6) recovers(5); complete uniform phase uncertainty gives1/2.

There is also a minimax statement. An implementation strategy with access only
to the unconditioned operation cannot distinguish lifts U and -U. The two
ideal controlled channels have half-diamond distance1, so by the triangle
inequality its worst error is at least1/2. Completely dephasing the control
and applying the branch channel attains1/2 against every phase lift. This is
a phase-information limitation under the stated access model, not impossibility
of controlling a supplied calibrated Hamiltonian.

## 4. Released readout consequence and remaining construction

For X readout of |+> control and a perfect reflection, the actual system Kraus
operators are M_x=(I+x exp(i nu) mathcal R)/2. Eigenvalue readout has error
sin^2(nu/2), while, when mathcal R has BOTH eigenvalues, the COMPLETE recorded instrument
has exactly error |sin(nu/2)|. Scalar reflections need not attain this value.
The nonscalar result is derived in [K2119](k2119-distributed-controller-errors-2026-10-26.md).
At nu=pi records swap; at nu=pi/2 the probabilities alone lose the eigenvalue
information. Preserve full instrument coherence, not only its probabilities.

The attempted promotion to a physically local controller stops at two exact
missing interfaces. First [K2118](k2118-controller-locality-2026-10-26.md)
shows why one qubit multiplying an extended potential is not a local apparatus.
Second common-H1 one-particle dynamics and endpoint Shale implementation do
not provide a phase-fixed selfadjoint instantaneous Fock Hamiltonian.
[K1896](k1896-local-phase-vacuum-boundary-2026-10-21.md) already supplies the
UV warning: for nonconstant compact rho and nonzero flavor B,
||P_+ rho B P_-||HS diverges, so the naive quadratic pair-creation term need
not even act on Omega. [K1897](k1897-smooth-pulse-energy-2026-10-21.md) is
explicitly endpoint-only. No new ultraviolet theorem is claimed here.
A renormalized local controller field, its domain, calibration and energy
budget remain to be built. This result advances the exact controlled-endpoint
requirement and rejects an unsupported transfer; it is not that construction.
