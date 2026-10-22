---
title: "K1923: Exact preparation cost under energy conservation"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1923_energy_shell_preparation_cost.py
  - tests/channel-swings/k1923_energy_shell_preparation_cost_probe.py
---

# K1923: Exact preparation cost under energy conservation

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
result: shellwise exact support criterion and optimal initial-state resources
carrier: finite system and finite bath with specified additive Hamiltonian LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and quantum relative entropy ON=product_initial_state
real_structure: complex adjoint and positive density matrices
grading: bath energy eigenspaces; target population labels
action_owner: repository-construction -- supplied extreme Schur channel and energy-conserving joint unitary
target: exact channel dilation and preparation-resource minimum MAP-TYPE=intertwiner
```

## 1. Exact endpoint and optimal resource formula

Fix an extreme correlation matrix C of rank k, its Schur channel Phi_C,
and H_S diagonal in the population basis. Let H_B have distinct energies E_e,
eigenspace projections P_e and dimensions d_e. The bath initially has ANY
state rho, including coherences between energies, independently of the system.
The allowed joint unitary obeys [U,H_S+H_B]=0. No catalyst, battery, measurement
or pre-existing system-bath correlation is supplied.

There exists such a U realizing Phi_C exactly if and only if

    k rank(P_e rho P_e) <= d_e for every e.               (1)

Write s_e=floor(d_e/k), tau=exp(-beta H_B)/Z, beta>0, and

    p=sum_e s_e exp(-beta E_e)/Z.                         (2)

If p=0, realization is impossible from ANY preparation. If p>0, the exact
minima over all preparations and conserving unitaries are

    min D(rho||tau) = -log p,
    min [F_beta(rho)-F_beta(tau)] = -log(p)/beta,
    min (1/2)||rho-tau||_1 = 1-p.                         (3)

Choose any rank-s_e projector Q_e inside each shell, Q=sum Q_e. All three
minima are attained by rho_*=Q tau Q/p. Formula(3) concerns an initial state
resource, not total work or an executable cooling protocol. K1916 optimizes
rank globally with unrestricted interactions; (2) instead rounds the allowed
rank SEPARATELY in every energy shell. Cold nondegenerate levels cannot stand
in for the within-shell dimension required by conservation.

## 2. Why energy coherence cannot improve the exact resource optimum

Let Delta_B rho=sum P_e rho P_e. Conservation implies covariance of the
family of induced channels: rotating the bath by exp(-it H_B) conjugates
Phi_rho by the corresponding system time rotations. Phi_C commutes with all
system diagonal rotations. Therefore if Phi_rho=Phi_C, averaging these
rotations gives Phi_(Delta_B rho)=Phi_C with the SAME U. In finite dimension
the infinite Cesaro average is precisely Delta_B, including arbitrary real
energy gaps; commensurability is unnecessary.

The resulting channel is a convex mixture of the channels from nonempty
normalized shell blocks rho_e. Each sends every population input |j><j|
to itself: positive leakage terms cannot cancel in a convex mixture. Every
population-preserving completely positive channel is Schur, since each Kraus
operator must map every |j> into its own line. Extremality of C therefore
forces EACH occupied shell's channel to equal Phi_C.

For vectors in supp(rho_e), population preservation makes U act as
|j> psi -> |j> V_(j,e) psi. Conservation places the bath output back in shell e.
These are isometries from that support into a d_e-dimensional shell. K1912's
extreme-Gram polarization argument now gives k rank(rho_e)<=d_e. No claim
that U is globally controlled on unpopulated directions is needed.

Conversely, if(1) holds, embed C^k tensor supp(rho_e) into shell e and extend
the maps psi -> v_j tensor psi to unitaries U_(j,e) of that shell, where
<v_l,v_j>=C_jl. Put U_j=direct_sum_e U_(j,e) and
U=sum |j><j| tensor U_j. This U conserves energy. Off-energy blocks of rho
contribute zero to Tr(rho U_l* U_j), so the original coherent rho also realizes
C. This proves the stated iff, not merely a sufficient stationary subclass.

Relative entropy obeys

    D(rho||tau)=D(Delta_B rho||tau)+S(Delta_B rho)-S(rho).

Thus coherence cannot reduce this cost; pinching also contracts trace distance
to tau. For pinched rho its support Q' has at most s_e dimensions per shell,
and Gibbs mass q=Tr(Q' tau)<=p. Conditioning tau on Q' gives
D(rho||tau)=D(rho||Q'tau Q'/q)-log q >=-log p.
The support measurement yields distance >=1-q>=1-p. The state rho_* above
attains both. These arguments prove the global optimization even over coherent
states and arbitrary conserving U, not only a controlled-unitary ansatz.

## 3. Released dimension, tensor and low-temperature consequences

Since s_e<=d_e/k, p<=1/k. Every exact realization of an extreme k>1 channel
therefore costs at least log k in relative entropy and at least1-1/k in trace
distance from its Gibbs bath. Equality in these two universal bounds occurs
exactly when every bath shell dimension is divisible by k (finite beta gives
all shell weights positive). A completely nondegenerate bath has p=0 even
when it is arbitrarily large or cold. For k=1, p=1 and no preparation is
needed, as expected for a diagonal-unitary channel.

At low temperature, let E_* be the lowest energy whose d_e>=k, and E_g the
ground energy with degeneracy d_g. Then

    -log p = beta(E_*-E_g)+log(d_g/s_*)+o(1).             (4)

If the ground shell is too small, cooling INCREASES the exact preparation
penalty linearly in beta. If it is large enough, the limiting cost is
log(d_g/floor(d_g/k)), at least log k. This differs from unrestricted
K1916 ground-state preparation, where the interaction can supply energy.

For N copies of an extreme rank-k target, tensor products of the rank-one
Gram projectors span Hermitian(k^N), so C^(tensor N) is extreme of rank k^N.
Replace k by k^N in(1)-(3) for the total bath energy eigenspaces. Thus
D_min>=N log k and at least one shell must have dimension >=k^N. Arbitrary
collective conserving interactions do NOT erase the extensive exact resource
cost. This is not a robust lower bound for vanishing but nonzero errors;
that remains a separate question.

## 4. Exact finite thermal-cell example and asymptotic consumer

Take m identical two-level bath cells with gap Delta>0, excited Gibbs
probability q in(0,1/2) at beta>0, and k=2. The algebraic formula below
also holds for any q in(0,1). The total-energy shell j has dimension
binomial(m,j), each microstate weight q^j(1-q)^(m-j). Hence

    p_m=sum_(j=0)^m floor(binomial(m,j)/2) q^j(1-q)^(m-j)
       =[1-R_m(q)]/2,
    R_m(q)=product_(b: bit b of m is1) [(1-q)^(2^b)+q^(2^b)]. (5)

The product identity follows over F2 from
(1+x)^m=product_(b set)(1+x^(2^b)): odd binomial coefficients occur exactly
at bit-subsets of m. This proves(5) for all m, not by enumeration.
For m=1, p=0. For m=2, p=q(1-q); the single excited shell is a degenerate
qubit and the optimal state is pure within it. At q=1/4, p=3/16 and
D_min=log(16/3), distance13/16. The realizing controlled unitaries act only
inside that shell and preserve energy exactly.

For m=2^b, R_m=(1-q)^m+q^m. Generally, with r=max(q,1-q)<1,
R_m<=2 r^(2^floor(log2 m))<=2 r^(m/2), since every other factor is at most1.
Thus p_m ->1/2 and D_min ->log2, never0. The exact excess is
-log(1-R_m), between R_m and R_m/(1-R_m) when R_m<1. This supplies a finite
exponential convergence estimate. The limits q->0 and m->infinity need not
commute. This analysis concerns changing the initial state to rho_*; it does
not make the original Gibbs bath implement the channel.

## 5. Hostile review, prior art and scope

Strongest overclaim: using global bath rank in place of shell rank, or
assuming stationarity of rho. The covariance/pinching proof and explicit
coherent two-shell realization address both. A scalar shell state remains
subject to K1922's approximation floor. Nonextreme correlation matrices
need not satisfy(1); the tracial Pauli realization of I4 is a countercontrol.
No catalytic, infinite-bath or approximate-channel rank theorem is asserted.
Coherence is useless for this exact covariant target, not for all channels.

K1912's extreme-support theorem and K1916's relative-entropy support optimizer
are the reused dependencies. Tracial Schur factorization is established in
[Haagerup and Musat](https://arxiv.org/abs/1009.0778); thermodynamic coherence
restrictions are studied by [Ćwikliński et al.](https://arxiv.org/abs/1405.5029).
Our shellwise composition does not claim novelty or a full literature census.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
its nonzero southeast rival. SC-MAS-01 and SC-CHI-02 ASSERT a stylized mass
toy; SC-META-53 remains UNCERTAIN about indefinite spectra. None selects
this positive Hilbert channel, bath preparation, Hamiltonian or units.
LT-SM8, LT-GR6b and AC-F1 remain unchanged. Full20 paired injection, separate
K/C, physical domain and accessible algebra remain construction obligations.
No source-register, physics-ledger or canon verdict changes. This is an
independent finite-dimensional mathematical result, with no novelty, native
GU prediction, expert acceptance, infinite-reservoir or formal-proof claim.
Analytic proofs carry universal scope. Finite exact controls test actual
matrices and combinatorics; reporting and dependency checks are separate.
