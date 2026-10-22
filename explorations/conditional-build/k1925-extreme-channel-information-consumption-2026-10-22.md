---
title: "K1925: Extreme-channel information and catalyst consumption"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite positive Hilbert models; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1925_extreme_channel_information_consumption.py
  - tests/channel-swings/k1925_extreme_channel_information_consumption_probe.py
---

# K1925: Extreme-channel information and catalyst consumption

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
result: exact physical-environment information and thermodynamic consumption identity
carrier: finite n-level system, finite bath and catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace, von Neumann entropy and Gibbs free energy ON=finite_product_input
real_structure: complex adjoint; no source reality map
grading: system population labels only
action_owner: repository-construction -- joint unitary; additive energy conservation only in the thermal consumer
target: exact extreme Schur channel and returned-catalyst resource MAP-TYPE=intertwiner
```

## 1. The physical environment has a fixed information footprint

Let C be an extreme n-by-n correlation matrix of rank k, with unit vectors
v_j spanning C^k and C_ij=<v_j,v_i>. Let a finite environment start in ANY
state rho, independently of the system. Suppose an arbitrary joint unitary
realizes the full Schur channel Phi_C, including every coherence. Set
S=supp(rho), r=rank(rho). The reused K1912 support theorem supplies a SINGLE
isometry T:C^k tensor S -> H_environment such that on the populated support

    U(|j> tensor psi)=|j> tensor T(v_j tensor psi).       (1)

This statement concerns the physical environment, not an inaccessible
purifying reference. For any probability vector pi, put

    mu_pi=sum_j pi_j |v_j><v_j|, chi_pi=S(mu_pi).

The physical output conditioned on input j and its average are exactly

    rho_j=T(|v_j><v_j| tensor rho)T*,
    rho_bar=T(mu_pi tensor rho)T*.                       (2)

Consequently the Holevo information of this label ensemble is

    S(rho_bar)-sum_j pi_j S(rho_j)=chi_pi,                (3)

independent of the initial bath spectrum or size. This is a quantum
information quantity, not a claim that a single measurement extracts all
chi_pi classical nats. Each pair obeys the sharper operational identity

    (1/2)||rho_i-rho_j||_1=sqrt(1-|C_ij|^2).             (4)

Proof transfer: exact preservation of population inputs forces product
system outputs on S by positivity. Each pure vector in S can occur in an
ensemble of rho; extremality in the CORRELATION set forces its Gram matrix
to be C. Polarization gives V_i*V_j=<v_i,v_j>I_S. The tensor Gram isometry
proves(1), and entropy/tensor trace-norm identities prove(2)-(4).
No assumption that U is globally controlled outside S is used.

The entropy exchange of Phi_C on the diagonal input pi equals chi_pi, but
that fact alone would only identify a purified complementary output. The
extreme-support argument is essential for (2) on the physical mixed bath.

## 2. Exact thermodynamic consumption, including correlations

Now environment=B tensor A: B is a finite thermal bath tau_B at beta>0,
A is a finite apparatus/catalyst initially sigma_A, possibly coherent or
rank deficient. Start rho=tau_B tensor sigma_A and require
[U,H_S+H_B+H_A]=0, with H_S diagonal in the target population basis.
Use the input diag(pi). Let bars denote final averaged B,A marginals.
Define F_beta(omega)=Tr(H omega)-S(omega)/beta. Then

    beta [F_beta(sigma_A)-F_beta(sigma_bar_A)]
      = chi_pi + I(B:A)_bar + D(tau_bar_B || tau_B).      (5)

This is an equality, not only a bound. The system populations, hence its
energy, are unchanged. Total energy conservation gives Delta E_B=-Delta E_A.
Equation(2) gives S(rho_bar)=S(tau_B)+S(sigma_A)+chi_pi. Subadditivity with
the definition of mutual information yields
Delta S_B+Delta S_A=chi_pi+I(B:A)_bar. Finally
D(tau_bar_B||tau_B)=beta Delta E_B-Delta S_B proves(5).
Bath/catalyst correlations are included rather than silently excluded.

Therefore unchanged A even just for ONE input diag(pi) with chi_pi>0 is
impossible. It is unnecessary to demand return separately for every basis
input, or to forbid final system-apparatus correlations. A pure catalyst is
not an exception. This excludes the stated exact extreme channel under
exact additive conservation and exact return; it does not exclude arbitrary
catalytic state transitions, initial correlations, work supplies or infinite
environments. Free-energy DECREASE is a consumed resource, not the total
work of preparing, driving, resetting or measuring an apparatus.

## 3. Explicit target, saturation and optimal input

For the four-level target use
v_1=(1,0), v_2=(0,1), v_3=(1,1)/sqrt2, v_4=(1,-i)/sqrt2.
Their projectors span Hermitian(2), certifying extreme rank2. At uniform pi,

    eigenvalues(mu) = 1/2 +/- sqrt2/8,
    chi_uniform = h2(1/2+sqrt2/8) > 0.                  (6)

The prior pi=(1/2,1/2,0,0) gives mu=I2/2 and chi=log2, the maximal possible
value since k=2. Thus any full-channel realization consumes at least log2
dimensionless free energy for that legitimate diagonal input. Uniform-input
return already contradicts the smaller positive(6).

The identity is achievable: take B one-dimensional, H_S=H_A=0, a pure
qubit apparatus, and controlled qubit unitaries with first columns v_j.
They preserve total energy and implement C exactly. The apparatus average
is mu_pi; its entropy increase and beta free-energy decrease are chi_pi.
This consumes the apparatus; it is not a returned catalyst. Adding an
arbitrary spectator gives all initial-rank saturators from(1).

The K1923 initial preparation optimum and (5) answer different questions.
A log2 initial preparation cost does not itself prove a log2 consumption
law; (5) supplies the missing output-state accounting.

## 4. Released repeated-use and approximate-return consumers

For an exact tensor channel Phi_C^(tensor N), the Gram projectors span
Hermitian(k^N), so the tensor target remains extreme. With product prior pi,
chi_N=N chi_pi. Apply(5) to the WHOLE experiment including all finite fresh
Gibbs cells at the same beta and the same finite apparatus. Intermediate
apparatus memory/correlations are allowed. Exact tensor-channel operation
requires

    N chi_pi <= beta(F_initial-F_final)
             <= beta bandwidth(H_A)+log(dim A).         (7)

The upper bound follows from the finite energy range and entropy range.
It does not follow merely from observing correct one-use marginals: the
whole tensor-channel requirement matters. Externally reset cells or
nonthermal ancillary supplies must be included as consumed resources.

For an EXACT channel but approximate average return with trace distance
r=(1/2)||sigma_bar_A-sigma_A||_1, let d_A>=2 and
f_d(r)=h2(r)+r log(d_A-1) for r<=1-1/d_A, and f_d(r)=log d_A otherwise.
The finite entropy continuity inequality and energy range bound give

    chi_pi <= beta r bandwidth(H_A)+f_d(r).             (8)

This includes rank-deficient sigma and energy coherence. It bounds return
accuracy, not channel approximation. There is no dimension-uniform inference
as d_A grows, precisely the loophole exploited by large approximate catalysts.
For a degenerate qubit and the maximizing prior, (8) forces r>=1/2 and the
pure-qubit realization attains r=1/2. Equation(8) is a necessary tradeoff,
not a generally sufficient protocol. Approximate-channel stability is a
separate issue addressed at a spectral-dependent scope in K1926.

## 5. Executed counterexample: vanishing average disturbance at finite cost

The dimension dependence is real even with EXACT channel realization and
zero Hamiltonians. Let r=2m, d_A=2r=4m, and prepare sigma with decreasing
nonzero eigenvalues 1/(i H_r), i=1,...,r, followed by r zeros, where
H_r=sum_(i=1)^r 1/i. Use the optimal prior pi=(1/2,1/2,0,0), so mu_pi=I2/2.
Choose the support isometry T to place the two copies of each eigenvalue
1/(2i H_r) in consecutive output eigenvectors. The K1912 construction
extends every map v_j tensor psi to a unitary on this SAME apparatus,
implements the full target, and conserves H=0. Its average return distance is

    r_return=(H_(2m)-H_m)/H_(2m) -> 0,                 (9)

while the entropy increase is EXACTLY log2. To check(9), at index2i the
initial and final eigenvalues agree; at index2i-1<=2m the initial one is
larger. Their positive differences sum to 1-H_m/H_(2m). Beyond initial
support all differences are negative. Since H_(2m)-H_m<=log2 and H_(2m)
diverges, the distance tends to0. Thus no dimension-free positive bound
on this SINGLE average return distance can follow from exact target
realization and finite energy bandwidth alone.

This is not an all-input approximate catalyst. From(4) and the triangle
inequality, if r_j is the distance of the conditional environment to its
initial state, r_i+r_j>=sqrt(1-|C_ij|^2). In this bath-free construction
r_1+r_2>=1, so at least one basis input disturbs the apparatus by at least1/2
for every m. No claim about the catalyst marginal alone when a separate
bath can hold information follows from this physical-environment bound.
The example distinguishes averaged return, all-input return and reset cost.
The slowly decaying harmonic spectrum is related to the established
[van Dam--Hayden embezzling construction](https://arxiv.org/abs/quant-ph/0201041).
Here the explicit mixed-state calculation is for one channel-input average;
it is not a new entanglement-catalysis theorem or an all-input return protocol.

## 6. Hostile review and literature

The mixed-bath/complementary-channel distinction is load-bearing; the proof
uses physical-support polarization. Dropping extremality is false: a
maximally mixed qubit with I,X,Y,Z implements complete dephasing C=I4 while
every conditional bath state is unchanged and chi_physical=0, although the
pure complementary entropy is positive. This is an explicit countercontrol.
The finite pure-qubit saturator checks the consumption sign and shows that
correlation entropy cannot be booked twice. Bounds are in nats, hbar=1.

Catalytic channel restrictions are established prior art: Lie and Jeong,
[catalytic randomness and factorizability](https://arxiv.org/abs/2104.00300)
and [randomness without information leakage](https://arxiv.org/abs/2010.14795).
These papers prevent claiming the general catalytic obstruction as novel.
The entropy-continuity ingredient is
[Audenaert's finite-dimensional bound](https://arxiv.org/abs/quant-ph/0610146);
the support theorem is reused from K1912. This note supplies a self-contained
target-specific information/thermal accounting and consumers, not a novelty
claim or a full literature survey.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
the southeast rival; SC-MAS-01 and SC-CHI-02 ASSERT a stylized mass toy;
SC-META-53 remains UNCERTAIN about indefinite spectra. None selects this
positive Hilbert channel, bath, catalyst, energy or units. LT-SM8, LT-GR6b
and AC-F1 remain unchanged. The same-background full20 paired injection,
separate K/C, domain and accessible algebra remain construction obligations.
No source-register, physics-ledger or canon verdict changes. Analytic proofs
carry universal scope; exact finite controls, numerical illustrations and
report/pin checks are distinguished. No novelty, external expert acceptance,
native GU prediction, infinite-reservoir or formal-proof claim.
