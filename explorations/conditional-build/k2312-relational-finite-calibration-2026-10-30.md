---
title: "K2312 Relational finite calibration"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2312_relational_finite_calibration_probe.py
---

# K2312 Relational finite calibration

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
result: K2312
carrier: positive Fock pilot/reference shell and neutral finite record with retained working pump LAYER=toy CHIRALITY=N/A
pairing: positive Fock Hilbert inner product and half trace distance ON=declared_carrier
real_structure: ordinary complex conjugation and Hilbert adjoint
grading: total charge 2(K_P+K_R), working Q=N_field+2K_pump and neutral records
action_owner: repository-construction -- supplied total-number-conserving shell control and protected reference, same K2306 working circuit
target: finite relational calibration with charged-stock return and explicit apparatus obligations MAP-TYPE=evaluation
```

## Change the resource class explicitly

[K2309](k2309-nonclassical-pump-calibration-2026-10-30.md) prices an independently prepared asymmetric sine pilot, an external phase readout and correction. Here both arms are retained in one fixed-total-number shell. We construct a finite number-conserving protocol and count its charged stock; protected relative encoding, arbitrary shell control and precise actuation remain supplied. This does not invalidate the coherent-source lower bound for the different independent-pilot task.

Keep mu=10^28 for the working coherent pump and delta<9.386e-12 for its full circuit baseline. Working field starts in vacuum, all gates commute Q=N_field+2K_pump, and phase is modulo pi. The calibration pair is initially independent of the working system and history. SC-META-53 remains UNCERTAIN and ledger0.263 unchanged. Positive Hilbert apparatus mathematics is not a native physical quotient or GU prediction.

## Exact finite preparation and readout

Take integer N>=1 (N=0 has trivial identity preparation and no sensing). Let |n>=|n>_P|N-n>_R, 0<=n<=N, have total charge2N. Start e0=|0,N> and prepare s=sum a_n|n>, where

    a_n=sqrt(2/(N+2)) sin(pi(n+1)/(N+2)).

An explicit unitary is U=I-2|w><w| on this shell, w=(e0-s)/sqrt(2(1-a0)), and identity elsewhere. Ue0=s and U commutes total charge. A positive bounded shell Hamiltonian H=(hbar pi/(2T))(I-U) implements U in duration T. This is an arbitrary high-dimensional control construction; it is not spatially local synthesis or a measured energy/time cost.

Encode unknown phi only on P as exp(-2i phi K_P), keeping R protected. Choose M=N+2 outcomes, theta_j=pi j/M, and

    |v_j>=sum_n exp(-2in theta_j)|n>,
    E_j=|v_j><v_j|/M,
    A_j=|0,N><v_j|/sqrt(M).                          (1)

Fourier orthogonality gives sum E_j=I on the shell. The outcome probabilities are p_j=|sum a_n exp[-2in(phi-theta_j)]|²/M. Since |n-m|<=N and |n-m+-1|<=N+1<M, the discrete sums have no aliases in normalization or the first circular moment. Therefore for EVERY phi,

    sum_j p_j 4sin²(phi-theta_j)
        =2[1-cos(pi/(N+2))]=L.                     (2)

This reuses the sine/path identity; the new construction is its relational, finite-outcome measure-and-return realization.

A_j returns the pair exactly to |0,N>, uncorrelated with its recorded outcome. A finite neutral dilation maps |n>|0> to |0,N> M^-1/2 sum_j exp(+2in theta_j)|j>. Its N+1 Fourier columns are orthonormal, so it extends to a unitary in the fixed total-charge sector. Measuring/dephasing that neutral record realizes(1). The joint state including the working output and actual record has the pair as an exact pure tensor factor.

## Error budgets and the actual resource ledger

Apply exp(+i theta_j Q) to the working system. An explicit positive actuator is H_c=hbar Omega(2I-J/M) tensor Q, where J=sum j|j><j|, with duration pi/Omega. Since Q has integer spectrum, its unitary is exactly the desired controlled correction. It commutes charge, but control resolution M and integrated angle precision remain supplied. The inherited distance bound and Jensen/Cauchy-Schwarz give average error, including the actual classical record marginal,

    D_average<=delta+sqrt(mu L)
             <=delta+pi sqrt(mu)/(N+2).

For N=3*10^27 this is<9.491e-12. The SAME Markov argument with r=3*10^-27 gives bad-outcome probability<2/45 and successful error<9.986e-12. Mean pilot number isN/2, reference numberN/2 during sensing, but total stock is exactly N, not N/2. For equal frequencies its energy is N hbar omega; no frequency or physical energy scale is chosen here. M=N+2 fits a92-qubit neutral record. A classical record can be implemented by copying the coherent register into a second neutral M-state environment before dephasing; this also fits92 qubits. A fresh pure neutral record is consumed on each use; retaining J records costs up to M^J dimensions. Exact charged return is not thermodynamic reset, uncorrelated intermediate-reference catalysis or a complete apparatus return.

A residual reference phase b makes the measured parameter phi-b. A correction angle error u_j adds an error bounded by2sqrt(mu)|u_j|: for the ideal working pure trajectory Var(Q)=4mu because every gate commutes Q, and the pure-state rotation distance is at most |u_j|sqrt(Var Q); contraction covers discarded environments. Compare to that ideal trajectory once, paying delta once. Thus uniform |b|<=b0,|u_j|<=u0 add2sqrt(mu)(b0+u0), also when the actual record is retained. Each allowance1e-14 requires the respective angle<=5e-29. With both allowances the average is<9.511e-12; successful error<1.0006e-11, so the older95%-success threshold1e-11 is NOT certified by both full allowances. To meet it choose b0=u0=1e-29: their combined distance allowance4e-15 yields success<9.990e-12 and average<9.495e-12. Shielding and control precision are substantive supplied conditions.

Exact shell unitaries have zero number leakage. If a preparation trace-error allowance is later used, a hard charge bound/conservation or an independent energy-tail condition is needed to bound energy; trace distance alone cannot do so. General imperfect readout is not silently assigned the previous preparation-only budget. With arbitrary readout channel error xi and comparison to the actual record marginal, a conservative2xi allowance is available; it is not needed for the exact finite construction here.

## Counterconstructions and what was learned

If both arms see the same phi, their encoding is exp(-2iNphi)I: every outcome is phi-independent. Discarding R also destroys the signal because the pilot marginal is number-diagonal. Independent number dephasing has the same effect. Consequently the protocol estimates a phase difference to a protected arm, not an absolute common phase of every charged resource.

The outcome count matters. M=N+1 normalizes the POVM but aliases the loss: for N=1,M=2 the risk is1-cos(4phi), rather than the uniform value1. The extra outcome prevents this error. Operations are covariant under diagonal U(1), not independent arm rotations; the supplied interarm coupling establishes relative coherence. A source-number state can prepare the relational sine state because it has no global U(1) asymmetry; it cannot prepare the independent coherent sine pilot with a phase-free environment. K2309's coherent-stock bound M_coherent>1.575e54 retains its original scope.

This closes finite preparation/readout/charged-return at the mathematical control-alphabet level and quantifies the still required protected-reference and actuator precision. It does not supply a spatial microscopic Hamiltonian, a clock of that precision, shielding apparatus, a low-cost92-qubit reset, or hardware feasibility. Next test a specified physical reference/clock/control architecture against these bounds; repeating sine minimax or claiming charged-stock return eliminates the neutral-resource cost would not answer it.

## Verification

Small-shell exact/algebraic Fourier, Householder and measure-reset checks exercise the actual maps; rational bounds check the large fixture without creating its enormous matrices. Altered readout dimension, charge encoding, preparation, normalization and actuator phase have genuine failed evaluators. General Fourier cancellation/unitary extension and trace-distance arguments are the written proofs above. No novelty, external-expert, proof-assistant, hardware or whole-GU certification is claimed.

For general reference-frame and superselection context, see [Bartlett, Rudolph and Spekkens (2007)](https://arxiv.org/abs/quant-ph/0610030). The finite protocol and error composition above are derived here; no novelty priority is claimed.
