---
title: "K2315 Calibration control cost"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2315_calibration_control_cost_probe.py
---

# K2315 Calibration control cost

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
result: K2315
carrier: two positive bosonic modes at fixed total stock N and retained working pump with independent pilot readout LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product, half trace distance and operator norm ON=declared_carrier
real_structure: ordinary complex conjugation and adjoint
grading: pilot/reference total number N; occupation-neighbor controls conserve total charge
action_owner: repository-construction -- restricted passive or number-selective control alternatives to K2312
target: calibration confidence obstruction and preparation time accounting MAP-TYPE=evaluation
```

## Operational target and control restriction

[K2312](k2312-relational-finite-calibration-2026-10-30.md) prepares a relational sine state in total-number shell N=3*10^27 with an arbitrary shell unitary. It supplies protected reference, readout and inverse phase actuation. Here test whether ordinary **passive two-mode** preparation can replace that unitary, then price a number-selective repair. This is positive-Hilbert apparatus mathematics; SC-META-53 remains UNCERTAIN and ledger0.263 unchanged.

Start |0,N>, allow time-dependent number-conserving quadratic Hamiltonians on the two modes only, encode once exp(-2i phi n_P) on the pilot, then allow arbitrary joint pilot/reference measurement. The working system remains independently prepared with mu=10^28 and full baseline distance delta<9.386e-12. Correction is K2312's estimate-dependent inverse exp(+i theta Q). The theorem excludes extra sensing resources, working-pump interrogation, repeated phase queries, postselection and arbitrary replacement of the working output. Exact inverse actuation is granted, making the preparation obstruction stronger within this task.

The target is **at every phi**, at least95% probability of conditional full retained-output error<=10^-11, phase modulo pi. This is a confidence task, not an average-error lower bound.

## Passive stock obstruction, with arbitrary readout

Every passive preparation has the form

    (u a_P^dagger+v a_R^dagger)^N |vac>/sqrt(N!), |u|²=p, |v|²=1-p.

Thus pilot number has a binomial law. Two encodings separated by d have squared overlap

    F=[1-4p(1-p)sin²d]^N >=cos^(2N)d,
    D²=1-F <=N sin²d <=N d².                       (1)

Time dependence of the quadratic controls does not change this form: their one-particle U(2) evolution induces its symmetric Nth power. No QFI-to-confidence inference is needed.

For residual e, the inherited retained-pump marginal bound is

    D_full>=sqrt(1-exp[-4mu sin²e])-delta.

Therefore success D_full<=10^-11 implies circular |e|<10^-25. A direct conservative verification is enough: at e0=10^-25, sin(e0)>=e0-e0³/6 and1-exp(-x)>=x-x²/2, giving the square-root term>1.99*10^-11, larger than10^-11+delta<1.9386*10^-11. It increases on0<=|e|<=pi/2.

Take two possible phases separated by d=3*10^-25. Their successful-estimate neighborhoods are disjoint. Classifying an estimate by its closer hypothesis gives at least95% binary success under either hypothesis. Helstrom's binary bound (1+D)/2 therefore requires D>=.9. Equation(1) implies

    N>=.81/(3*10^-25)²=9*10^48.                    (2)

At K2312's stock3*10^27, D²<=2.7*10^-22, so the demanded guarantee is impossible in this passive class, even with arbitrary joint calibration readout and perfect correction. This does not refute K2312's sine protocol, whose nonpassive preparation is precisely the premise being tested.

Small-shell controls matter: the sine state equals a balanced binomial state for N=1 AND N=2. For N>=3 it cannot: sine reflection symmetry forces p=1/2, but its first amplitude ratio2cos(pi/(N+2)) differs from sqrt(N). N=3 is checked separately; N>=4 follows because the former is strictly below2 and the latter at least2. This state mismatch alone would not imply(2); the operational overlap argument does.

## Released repair: occupation-neighbor synthesis with a norm budget

Reuse the number-selective Givens idea already constructed in [K2264](k2264-restricted-detector-control-2026-10-29.md), rather than claiming new controllability. For target positive sine coefficients a_0,...,a_N, define r_k=sqrt(sum_{j=k}^N a_j²). Starting at |0,N>, successively apply adjacent rotations on occupation basis slots k,k+1 with cos(theta_k)=a_k/r_k, sin(theta_k)=r_{k+1}/r_k. After rotation k, coefficient k is final and the remaining amplitude r_{k+1} occupies slot k+1. Exactly N such rotations prepare the target. Number-selective coupling is a supplied nonlinear control; adjacency of occupation labels is not spatial finite-range synthesis.

Let H(t)=D(t)+H_off(t) on this hard shell, D diagonal, H_off=A+A^dagger and A only raises occupation by one. Assume ||H_off(t)||<=hbar J, J>0. Conjugation by diag(i^n) shows i[H,n] is unitarily equivalent up to sign to H_off, so

    |d <n>/dt|<=J.

For a final state at half trace distance eta from the sine target, both supported in0..N, the bounded observable n/N in[0,1] gives <n> >=N(1/2-eta). Starting with zero pilot occupation,

    T>=N(1/2-eta)/J.                               (3)

For exact preparation and N=3*10^27, JT>=1.5*10^27. Each selective rotation can be generated with offdiagonal norm hbar J in time theta_k/J; theta_k<=pi/2 gives constructive T<=pi N/(2J), with exact pulse areas and switching granted. Thus the preparation cost is order N/J in this explicitly normalized alphabet. Arbitrarily large diagonal energies cannot evade(3), since they commute n. A bound ||A||<=hbar J instead gives the weaker2J speed; a microscopic beam-splitter coupling g has shell norm of order N hbar|g|, so fixed J is not fixed g.

A positive Hamiltonian can be obtained by adding a sufficiently large identity on the finite shell, affecting only a global phase. That shift and the diagonal/control apparatus are not priced by the offdiagonal budget. For N pulses, operator errors epsilon_k (the norm differences between actual and ideal pulse unitaries) telescope to total state distance at most sum epsilon_k; an eta allowance requires that sum<=eta, not merely each pulse error<=eta. A uniform allocation eta/N at eta=10^-14 and N=3*10^27 is below3.334*10^-42 per pulse. This sufficient compiler precision is not a necessary physical noise bound.

Hard support or an independent energy-tail bound is essential for the eta statement; trace distance alone does not bound occupation on unrestricted Fock space. Charged stock, neutral record reset, protected reference, drift, readout and correction errors remain separate K2312 obligations. This result prices preparation under a chosen control norm; it is not a complete hardware or thermodynamic cost model.

## Evidence and remaining construction

Exact small-shell binomial overlaps, sine exceptions, Givens maps, commutator conjugacy, rational confidence bounds and corrupted-input checks support the implementation. Universal passive U(2), discrimination, synthesis and speed arguments are the proofs above. No novelty claim is made. The next concrete architecture must supply selective nonlinear couplings, norm/time/precision, protected relative encoding and neutral reset in one model. More stock alone or repeated sine minimax does not supply those premises.

For prior context, [Qiu and Li](https://arxiv.org/abs/0812.2378) discuss minimum-error discrimination and the binary Helstrom limit. [Zhou, Guha and Gagatsos](https://arxiv.org/abs/2308.01293) study fixed-photon two-mode Bayesian estimation with an MSE objective; that objective differs from the uniform retained-pump confidence task here. These links are context, not a novelty or experimental claim.
