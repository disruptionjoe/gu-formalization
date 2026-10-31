---
title: "K2380 Optimal complete idle erasure recovery"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2380_complete_erasure_recovery_probe.py
---

# K2380 Optimal complete idle erasure recovery

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
result: K2380
carrier: four ternary dual-rail pairs encoding one qubit with arbitrary untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive finite Hilbert pairing and trace norm ON=declared_carrier
real_structure: complex quantum states with real loss probabilities
grading: occupied or vacuum pair sectors and classical erasure flags
action_owner: repository-construction -- independent matched-rail idle amplitude damping
target: optimal final CPTP recovery and complete instrument error consumer MAP-TYPE=evaluation
```

## Exact result

For the code V|b>=(|00bb>+|11,1-b,1-b>)/sqrt(2), idle independent loss with equal rates on the two rails of each pair produces a classical erased-set flag S. Let eta_i be pair i's survival probability and

    w_S = product_(i in S)(1-eta_i) product_(i not in S) eta_i,
    P_j = sum_(|S|=j) w_S.

Among all final CPTP decoders using the surviving record and fresh input-independent ancillas,

    inf_R (1/2)||R E V - id||_diamond = P_2/2 + 3(P_3+P_4)/4. (1)

The arbitrary reference is included in the diamond norm. The decoder has no emitted-environment access, pre-shared reference entanglement or prior knowledge of the logical state. This improves the previous sufficient bad-event bound P_2+P_3+P_4 by recovering the information that actually survives two losses. It does not make those branches quantum-correctable.

## All sixteen erasure branches

Matched rail damping multiplies every occupied bit by the same survival amplitude and every erased bit by the same loss amplitude. Conditional on S the channel is exactly partial trace over S, multiplied by w_S. Orthogonal vacuum flags make the direct sum classical. Time-dependent matched rates are allowed through eta_i=exp(-integral k_i); H=0 during this idle channel.

Label physical pair qubits0,1,2,3 with groups{0,1},{2,3}. Zero/one-loss branches use the existing exact recovery. If S is either complete group, the two survivors carry repetition encoding W of D_X(rho)=(rho+XrhoX)/2, W|b>=|bb>. A CX from first survivor to second extracts D_X on the first. If S removes one from each group, the survivors are

    sum_b rho_bb (|0,b><0,b|+|1,1 xor b><1,1 xor b|)/2.

A CX from the first-group survivor to the second-group survivor extracts D_Z(rho)=(rho+ZrhoZ)/2 on the second. With three erasures the sole survivor is I/2 for every logical input. With four erasures the output is vacuum; prepare I/2 using a Bell pair and discard its partner.

All statements are linear channel identities, checked on E00,E01,E10,E11; basis-state checks alone would miss the X coherence retained by same-group loss. Full all-mask matrix-unit verification is in the companion probe.

## Sharp optimality, not only a fidelity estimate

Let a be the sum of the two same-group weights, b the sum of the four split-group weights, and c=P3+P4. The explicit channel has Pauli weights

    qI=P0+P1+(a+b)/2+c/4,
    qX=a/2+c/4, qY=c/4, qZ=b/2+c/4.

Its half-diamond distance to identity is 1-qI: triangle inequality gives the upper bound and a Bell input gives orthogonal Bell outputs attaining it.

For any decoder, each two-erasure input-reference branch is separable because it is a measure-and-prepare/dephasing channel followed by an isometry. Local recovery preserves separability; overlap with a normalized Bell state is at most1/2 (first check a pure product, then use convexity). Every three/four-loss branch is constant, so the output-reference state is sigma tensor I/2 and its Bell overlap is exactly1/4. Good branches have overlap at most1. The total overlap is therefore at most qI. Measuring Bell versus its complement gives trace distance at least1-qI. This matches the explicit upper bound and proves (1). Mixing flags coherently cannot change the argument: the actual input to recovery is a classical direct sum. Entanglement fidelity alone would not establish the matching upper bound.

## Implemented fallback and finite costs

Reuse the existing supplied X,H,CX and syndrome-measurement alphabet. Eight flag CX gates and four measurements identify erasures. With exactly two losses, four survivor rail-decode gates, one extraction CX and at most three routing CX total at most16 gates including flags. Three losses need at most13. All loss needs10: after measurement syndrome ancilla a1 and output f are zero; H_f then CX(f,a1), discarding a1, prepares I/2. Zero/one loss retains the inherited worst-case21. Thus the worst-case recovery gate count remains21 plus four measurements; no free random coin is assumed.

For identical loss probability p,

    e*=3p^2-3p^3+3p^4/4=3p^2(1-p/2)^2.

At p=1/10, e*=1083/40000=0.027075, while the old bound is0.0523. Nonuniform eta=(9/10,4/5,7/10,3/5) gives e*=1393/10000. Endpoints p=0,1 are channel limits, not strictly positive finite-duration rate fixtures. At high loss the improvement includes a better constant fallback and is not evidence of restored quantum information or hardware advantage.

Use inherited finite gate duration tg and supplied error rates gamma,kappa_g:

    Tenc=12tg,
    Trec=21tg+4tm+tfeedback,
    epsilon_total <= epsilon_pre+e*+(3gamma+8kappa_g)Tenc
                     +(3gamma+12kappa_g)Trec
                     +epsilon_prep+epsilon_measure+epsilon_control. (2)

All terms concern the same stipulated apparatus. The inherited cap/slew fixture G=V=1 has tg=1+pi/2<18/7. With tm=1,tfeedback=0,gamma=0,kappa_g=10^-6, the new idle error plus these gate debts is below0.028018. Preparation, measurement and control-model errors are explicitly separate, not assumed zero or measured. Idle noise already included in e* must not be counted again as a gate-time debt.

## Useful successor: actual unequal rates with the same decoder

[K2377](k2377-time-ordered-rate-robustness-2026-10-31.md) compares complete physical channels with the same Hamiltonian. Set H=0 and choose a matched reference k'. Fix the new decoder R* before seeing actual loss history. Contractivity gives

    e_actual <= min(1,e*_(reference)+min(sqrt(Q),D1)),       (3)

with Q the survival-weighted square-root-rate mismatch and D1 the L1 generator bound defined there. Compose (3) into (2), counting each interval once. This supplies a complete actual-channel certificate, not an optimum for unequal rates. Identical channels give Q=D1=0 and recover (1).

Driven noncommuting X/Z schedules can have history-dependent two-loss dynamics; their optimum is not proved here. An integrated survival substitution cannot transfer (1) to those schedules. Nor does the conditional apparatus construct the source-native GU physical quotient: SC-META-53 remains UNCERTAIN and LT-GR6b remains open.

## Verification and next question

Exact finite matrix-unit enumeration establishes all16 supplied branch channels, including coherences and the implemented all-loss mixture. Separate probability and gate-budget fixtures check the displayed consumers. The universal optimum is the Bell-bound proof, not a pass count. Internal specialist review is not external-expert, proof-assistant or hardware certification. Next characterize the complete driven two-loss channel or evaluate (2)--(3) on one measured complete apparatus. The absent empirical inputs restrict physical credit, not this conditional theorem.
