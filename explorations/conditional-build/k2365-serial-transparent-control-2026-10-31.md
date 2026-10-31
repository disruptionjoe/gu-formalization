---
title: "K2365 Serial transparent control with unknown loss time"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical or numerical result; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2365_serial_transparent_control_probe.py
---

# K2365 Serial transparent control with unknown loss time

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
result: K2365
carrier: eight neutral physical qubits encoding four dual rails LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and reference-aware half-diamond distance ON=declared_carrier
real_structure: complex amplitudes and real Hermitian Pauli controls
grading: pair number, physical locality, syndrome and logical qubit differ
action_owner: repository-construction -- K2356 code with K2362 diagonal Z and supplied matched loss
target: finite switching and noise cost of a complete logical Z gate MAP-TYPE=evaluation
```

## Scope and reuse

K2362's Z_ET has32 mutually commuting Pauli strings. Serializing them gives an EXACT loss-free endpoint, yet an unknown-time loss can record the unfinished phase schedule. We bound that error and price pulse caps/slew. This is supplied positive-Hilbert control mathematics, not device realization or GU physical positivity. SC-META-53 UNCERTAIN and LT-SM8 remain unchanged. Preparation, encoding, recovery, readout, other noise and clock errors remain additional debts.

## 1. Carrier and normalized jump instrument

Reuse K2356's code V|b>=(|00bb>+|11,(1 xor b),(1 xor b)>)/sqrt2 on occupied dual pairs |b,1-b>. With N=sum N_i and z_i=(Z_qi-Z_ri)/2,

    Z_ET=(5-N)(z1+z2)(z3+z4)/4=sum_l c_l P_l.

K2362 proves32 coefficients c_l=±1/16, sum|c_l|=2, norm1 on the full256-state carrier, and Z_ET V=VZ and Z_ET A_js=A_js Z for each one-pair erasure. Individual A_js have norm1/sqrt2; the stacked logical error map A_j=(A_j0,A_j1), retaining the lost-rail environment, is an isometry. Write J_j for the physical pair-loss instrument on the occupied-pair sector, so A_j=J_j V. Using separate unnormalized maps as normalized trajectories would lose a factor.

## 2. Cumulative serial bound, exact endpoints

For theta>=0, execute n cycles, each32 pulses of signed area c_l theta/n in any fixed order. Each pulse has fixed sign and monotone cumulative signed area, with no overshoot, as in the triangular/trapezoidal implementation below. A net-area condition alone is insufficient. All strings commute, so the final unitary is exactly exp(-i theta Z_ET). Let delta=theta/n, F(t)=integral_0^t H_serial. During a cycle, choose the nearer completed/next cycle boundary in coefficient l1 arc length. The completed plus remaining l1 length is2delta, hence for one of a=kdelta,(k+1)delta,

    ||F(t)-a Z_ET|| <= delta.

Diagonal strings commute with pair number and all phase primitives. For a loss at time t,

    W_j(t)=exp[-i(theta Z_ET-F(t))] J_j exp[-iF(t)] V.

The output exponential acts trivially on the lost-rail environment. Replace F(t) by aZ_ET on either side. Intertwining then makes the reference map A_j exp(-i theta Z), independent of t. The unitary perturbation bound ||exp(-iK)-exp(-iL)||<=||K-L|| for these Hermitian commuting differences and the isometry give ||W_j-Wideal||<=2delta. The associated reference-aware half-diamond distance is at most min(1,2delta); no unobserved jump-time label is available to recovery.

For matched constant rail damping within each pair, serial diagonal controls preserve occupations, so no-jump attenuation and jump probabilities are logical-state independent. With eta_i=exp(-gamma_i T),

    P0=product eta_i,
    P1=sum_i (1-eta_i) product_(k!=i) eta_k,
    B=1-P0-P1,
    E <= B+P1 min(1,2theta/n).

For equal p=1-exp(-gamma T), B=6p²-8p³+3p⁴ and P1=4p(1-p)^3. Zero-loss error is exactly zero, which is why the serial debt is multiplied by P1 rather than P0+P1. This assumes ideal recovery; unequal rates inside a pair, dephasing, heating or correlated common resets are not covered by these probabilities.

## 3. Explicit physical phase counterexample

Put P=Z_q1 Z_q3, coefficient+1/16, first. A loss of pair1 after accumulated first-pulse area x, 0<x<=theta/(16n), yields recovered logical unitaries U_theta and U_(theta+2x) in its two equally weighted lost-bit environments. On |+>, after removing the intended gate the half trace distance is |sin(2x)|/2. Thus every positive interval of such jump times contains errors although the final no-loss gate is exact. The probe enumerates actual code strings, erased rail bits and physical Pauli eigenvalues to test this statement; it does not mutate an asserted verdict.

## 4. Finite pulse resource follow-through

Each one-string pulse begins/ends at zero, has capG and slewV, and area a=theta/(16n). Its minimum duration is2sqrt(a/V) if a<=G²/V, otherwise a/G+G/V. Therefore

    T_n=16sqrt(n theta/V)                 (triangular),
    T_n=2theta/G+32nG/V                   (plateau).

These are whole-Hamiltonian caps because exactly one norm1 Pauli is driven at a time. A gap-free ideal switching model is already included by zero endpoints; added settling gaps increase T. Fast-cycle transparency and low damping compete: n→infinity at fixed finite slew drives T→infinity, and the displayed upper certificate tends to1. In this model all-four-erased probability p^4 tends to1; the reused K2356 input-independent final recovery floor p^4/2 also rules out a zero-error limit.

A rational sufficient witness uses theta=1/2,G=V=1,gamma=1/6400. n=32 gives T64 and p<=gamma T=1/100. Using B<=6p²,P1<=4p gives E<=37/20000=.00185. n8,T32 yields53/20000=.00265; n128,T128 yields121/40000=.003025. These compare conservative upper certificates, not actual optimal errors or measured device rates. The full instrument adds initialization/recovery/readout and all omitted noise costs.

## 5. General covariance-defect extension

For a pair-number-preserving H and logical h(t), define d0=||HV-Vh|| and dj=||(H tensor I_env)A_j-A_j h||. Duhamel yields zero-jump error<=integral d0 and one-jump-at-t error<=integral_0^t d0+integral_t^T dj, with matched scalar attenuation removed. Integrate over the state-independent trajectory law and add B. This prices continuous coefficient errors, but its instantaneous norm bound generally does not shrink for increasingly fast serial switching. The stronger cumulative commuting-Z proof above is required for the stated1/n result. Noncommuting logical gates require another argument.

Error-transparent evolution and locality are prior art: [Vy, Wang and Jacobs](https://arxiv.org/abs/1210.8007). No novelty, hardware or native-GU certification.
