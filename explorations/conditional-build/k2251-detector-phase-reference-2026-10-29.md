---
title: "K2251 Number-conserving detector controls need a phase reference"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional apparatus mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2251_detector_phase_reference_probe.py
---

# K2251 Number-conserving detector controls need a phase reference

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2251 Number-conserving detector controls need a phase reference
carrier: two oscillator detector modes, charge-graded apparatus and finite binary record LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: excitation number and explicit tensor or CAR ordering; not physical families
action_owner: repository-construction -- supplied operational models
target: conservation bound for the actual mode-vacuum effect and finite-reference repair MAP-TYPE=intertwiner
```

## Question, target and prior work

[K2247](k2247-coupled-drift-cutoff-control-2026-10-29.md) allows general local spectral controls, including number-changing ones. Consider the restricted apparatus whose unitary U preserves total number N_S+N_A, whose initial apparatus sigma_A is independent of S, and whose binary pointer effect Z commutes with N_A. Strength, duration and spatial locality are otherwise unrestricted. This is a concrete control class, not a claim about all fixed-cap control.

[K2241](k2241-local-mode-detector-network-2026-10-29.md) supplies the actual mode b=(5/3)a1+(4/3)a2* and arbitrary number-profile effects e1(n_b). Select its allowed profile e1(k)=1_(k=0). The target effect is E=1_(b*b=0). It is not invariant under the PHYSICAL total number N_S=n1+n2. Conserving N_S is not the same as conserving n_b.

The sine-packet and path-adjacency mathematics is reused from [K2240](k2240-finite-battery-gate-2026-10-29.md), not counted as a new general translation theorem. The new measurement result is the actual spectral-effect witness, apparatus charge-mode requirement and finite-effect realization.

The standard background is symmetry-constrained measurement and quantum reference frames: [Bartlett, Rudolph and Spekkens](https://arxiv.org/abs/quant-ph/0610030) and [Marvian and Spekkens](https://arxiv.org/abs/1212.3378). The arguments below are direct applications with an explicit detector witness, not a new general conservation theorem. K2117's controlled-CAR phase convention is a different question. No repeatability assumption is used.

This is GU-independent supplied apparatus mathematics. Layer0 distinguishes physical oscillator charge, measured canonical-mode number, invariant pointer and supplied coherence. SC-META-53/LT-SM8 and ledger0.263 retain their existing scope; no GU physical quotient, source constraint or empirical test is provided.

## 1. Invariant apparatus implies invariant effect

Let M=U*(I tensor Z)U. Then0<=M<=I and M commutes with total number. The induced effect is determined by

    Tr(F rho)=Tr[M(rho tensor sigma_A)].

If sigma_A commutes with N_A, conjugate both factors by the same phase rotation and use total invariance. It follows that F commutes with N_S. This proof holds for unbounded number generators by their bounded unitary phase groups; no manipulation of an unbounded commutator on an unspecified domain is needed. It also holds with degeneracies, arbitrary diagonal thermal stocks, classical mixtures and neutral pointer registers.

For any normalized system vectors |m>,|n> of different charges, all invariant effects give the same probability on |psi_+>=(|m>+exp(i alpha)|n>)/sqrt2 and |psi_->=(|m>-exp(i alpha)|n>)/sqrt2. Choose alpha to align the target offdiagonal entry. The target probabilities differ by2|E_mn|. At least one absolute probability error is therefore at least|E_mn|. Discarding the field from a recorded instrument contracts trace distance, so this is also a lower bound on the worst half trace distance of the FULL recorded instrument from any implementation in this class.

## 2. A mean-number-one witness from the actual detector

The two-mode squeeze T in K2241 has tanh(t)=4/5 and sech(t)=3/5. It preserves n1-n2. In the difference-zero sector the kernel of b is the one-dimensional normalized vector

    |Omega_b>=(3/5) sum_(j>=0) (-4/5)^j |j,j>.

The recurrence follows directly by applying b; the norm is a geometric series. Thus the restriction of E to this sector is its rank-one projector, and on C=span{|00>,|11>},

    E_C=[[9/25, -36/125],[-36/125,144/625]],
    spectrum(E_C)={0,369/625}.

For |psi_±>=(|00>±|11>)/sqrt2, each has mean N_S=1. The E probabilities are9/1250 and729/1250, separated by72/125. Hence any invariant apparatus above has worst error at least36/125=0.288, already on this low-energy pair. Allowing larger number-diagonal reservoirs, stronger conserving controls or longer time does not remove this particular obstruction. For K2247's specific coupled h=[[2,1],[1,2]], the balanced witnesses have mean energy2. To fit its mean-energy1 input ball, use sqrt(3)/2|00> plus/minus (1/2)|11>, giving the still-positive error floor18sqrt(3)/125. Number-changing controls, an asymmetric apparatus or a noninvariant pointer leave the stated class.

## 3. Quantifying supplied charge coherence

Allow sigma_A to be asymmetric. Write P_q for its integer-charge projections and

    sigma_A^(d)=sum_q P_(q+d) sigma_A P_q,
    C_d(sigma_A)=||sigma_A^(d)||_1.

This trace-class Fourier mode is defined equivalently by a circle integral; orthogonal blocks give the sum of the block trace norms. For distinct system charge eigenvectors m,n with d=|n-m|,

    |F_mn| <= C_d(sigma_A)/2.                      (1)

Proof: total invariance forces the apparatus block M_mn to shift charge by the opposite gap. Only the matching Fourier mode of sigma contributes to Tr(sigma M_mn). Since0<=M<=I, ||M-I/2||<=1/2; the offdiagonal system compression M_mn therefore has norm<=1/2. Trace duality proves(1), including apparatus degeneracies.

On the two witness states, the probability separation that F can produce is at most C_2. The target separation is72/125, so the worst error obeys

    epsilon >= max(0,36/125-C_2/2).                (2)

To reach epsilon<delta on this pair one needs C_2>72/125-2delta. This is necessary, not sufficient for the full target detector or for instrument backaction. In particular the finite-density number-diagonal reservoir of K2249/K2250 has C_2=0, irrespective of its entropy capacity. Reset stock and phase reference are distinct resources.

## 4. Finite-reference repair on the declared compression

For L>=2, take a nondegenerate reference |j> with charge2j, j=0,...,L-1. Let

    r_j=sqrt(2/(L+1)) sin((j+1)pi/(L+1)).

In each total-charge sector2j,1<=j<=L-1, the pair {|00,j>,|11,j-1>} receives the exact2x2 effect E_C. The unmatched bottom |00,0> receives E_C,00; the unmatched top |11,L-1> receives E_C,11. These blocks define an invariant positive contraction M on C tensor A. The endpoint diagonals are essential. With reference |r>, its induced effect F_L has the SAME diagonals as E_C and

    (F_L)_01=(E_C)_01 sum_(j=1)^(L-1) r_j r_(j-1)
             =-(36/125) cos(pi/(L+1)).

Thus the worst binary record-probability error over every state on C is exactly

    ||F_L-E_C||=(36/125)[1-cos(pi/(L+1))]
                <=(18/125)pi²/(L+1)².             (3)

The binary classical-output channel has the same half-diamond distance: its difference is a signed scalar functional with representing operator F_L-E_C, whose completely bounded trace norm is its operator norm after the binary half-distance convention. A direct proof uses -eI<=F_L-E_C<=eI on every positive reference block and the trace-norm dual characterization. This assertion concerns the binary record only; it does NOT approximate the target field postmeasurement instrument.

An invariant measurement dilation exists sectorwise: the isometry |v> maps to sqrt(M)|v> tensor|1>+sqrt(I-M)|v> tensor|0>, with a neutral record, extends to a unitary separately in every total-charge sector. The choice of extension, its Hamiltonian, spatial locality, strength and duration remain supplied. The reference may be consumed or correlated; no catalytic restoration is claimed.

## 5. Sharp reference coherence and a concrete resource price

For ANY reference state on the L specified nondegenerate levels,

    C_2=sum_(j=0)^(L-2)|sigma_(j+1,j)|
        <=cos(pi/(L+1)).                           (4)

For a pure state, replace amplitudes by their absolute values. The sum is its Rayleigh quotient for half the path adjacency matrix. The normalized sine vector has its largest eigenvalue cos(pi/(L+1)); the elementary sine recurrence and complete discrete sine basis prove maximality. A mixed state obeys the same result by convexity and pure-state decomposition. Our real sine profile attains(4). Reflection symmetry gives mean reference charge L-1.

This optimizes C_2 at fixed dimension and the error in the stated block-copy construction. It does not prove globally optimal approximation of E_C over all invariant effects: the universal bound(2) is weaker and permits other block choices.

For L=100 the maximum reference number is198 and mean99. Using pi<22/7, equation(3) gives error<1/7000 on C. This is a finite constructive escape from the reference-free0.288 floor with its imported asymmetry explicitly priced. The two-state construction alone does not supply an energy-ball guarantee. Section6 supplies that guarantee for binary record statistics; correct field backaction, repeat-use reference renewal and fixed-cap local implementation remain separate obligations.

## 6. Finite reference for the FULL binary effect on an energy ball

The compression result releases a stronger construction for binary record statistics. Let S be any finite number M of physical oscillator modes, let N be total physical number, and let E be ANY positive contraction on their full Fock space, including the actual E=1_(b*b=0). Assume only Tr(N rho_S)<=B. This is a photon-number budget; converting an energy budget requires a positive spectral gap such as K2247's h_min>0.

For integer Q>=0, P=1_(N<=Q) has finite rank binomial(M+Q,M). Let E_Q=PEP, extended by zero on its complement. Take a reference with L consecutive integer charges0,...,L-1 and the same sine amplitudes as above. For each total charge t, put a copy of the principal compression of E_Q on the available states |n,alpha,t-n>, where0<=n<=Q,0<=t-n<L and alpha labels charge degeneracy. Outside P tensor A the effect is zero. Every block is a compression of a positive contraction, so this defines a finite-dimensional, total-charge-invariant effect with an invariant neutral-record dilation. Unlike a full gate translation, this measurement effect requires NO reference padding: incomplete edge sectors are principal compressions, not truncated unitaries.

Its induced effect on P is E_Q with charge-block entries multiplied by the autocorrelation

    c_d=sum_j r_(j+d)r_j,

where amplitudes outside0,...,L-1 are zero. Denote the corresponding dephasing channel by D_r. To bound it, use BILATERAL shifts S only as a mathematical dilation on an auxiliary l2(Z), embedding r by zero. The isometry maps |n,alpha> to |n,alpha> tensor S^n r. Compare with the identity isometry tensored with r. System charge sectors are orthogonal, including all degeneracies and an arbitrary external reference. Thus the vector error is at most

    max_(0<=n<=Q)||S^n r-r||
    <=Q||Sr-r||=2Q sin(pi/(2(L+1)))<=Qpi/(L+1).

Partial trace and binary measurement contract distance. These bilateral shifts are a proof device, not a supplied infinite physical battery. The actual apparatus effect is the finite block construction above.

For unrestricted inputs in the mean-number ball, eta=Tr[(I-P)rho]<=B/(Q+1). The gentle subnormalized projection bound gives ||rho-P rho P||_1<=2sqrt(eta), including any reference. The difference between the E and E_Q binary channels has half trace norm at most this quantity: their first outcome is the trace-nonincreasing map Tr_S[E(rho-P rho P)] and the second difference is its negative. On the low-charge part, the dephasing bound just proved applies. Therefore the actual finite reference effect approximates the FULL target binary record channel with arbitrary reference at error

    epsilon_record <= min(1, 2sqrt(B/(Q+1))+Qpi/(L+1)).       (5)

This is an energy-constrained complete record-channel bound, not an unconstrained diamond bound or a full field postmeasurement-instrument theorem. It holds on every input in the specified number ball, not just the two witness states. In particular it does not require computing the target's high-number matrix elements numerically to establish existence of the effect; finite block synthesis and precision remain supplied.

Concrete consumer: B=1,Q=159999,L=199999999. The tail term is1/200, and pi<22/7 yields total error<0.007515. The reference has maximum charge199999998 and mean99999999. For two modes the system cutoff rank is (Q+1)(Q+2)/2. These very large finite resources prove a mathematical repair, not practical hardware or an optimum. The same construction works for any finite B and requested positive error by choosing Q then L; the estimate supplies no uniform guarantee over unbounded-energy inputs.

The resulting apparatus need not restore its reference, preserve target field backaction, satisfy a given local control cap or implement its exact spectral blocks efficiently. Those require separate dynamics and repeat-use analysis. The full binary-statistics repair advances beyond the two-state witness while preserving these distinctions.

## Scientific effect and strongest alternatives

The number-conserving restricted alphabet with invariant preparation/readout cannot reproduce this concrete phase-sensitive detector, even with unlimited time. A finite phase reference repairs the explicit two-state input compression and, by positive total-charge block compression and a tail estimate, the full binary record channel on any fixed mean-number ball. Its charge-coherence optimum is known, but the general resource bound is not optimal. This removes pointless stronger-number-conserving control searches for that target, while identifying a precise missing resource. The source-compatible normal-constraint route, broader-contrast optimizer and real all-ten adapter remain separate scientific alternatives; no result here selects among GU actions or changes a physics ledger verdict.

## Reproduction

Run `python tests/channel-swings/k2251_detector_phase_reference_probe.py`. `--write` refreshes the exact-control report. Default execution recomputes the controls, rejects genuine changed-input faults after a green baseline, and checks note/code/dependency hashes. Finite controls do not certify the universal written proofs. Independent internal review is distinct from external-expert, proof-assistant, novelty or remote-CI certification.
