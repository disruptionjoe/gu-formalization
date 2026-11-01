---
title: "K2444 Sharp error transfer through a heralded causal program"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "sharp ideal-operation minimax over unrestricted causal targets; no joint transcript or native GU guarantee"
---

# K2444 Sharp error transfer through a heralded causal program

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
result: K2444
carrier: normalized causal Choi programs and complete Bell success maps LAYER=toy CHIRALITY=N/A
pairing: trace distance with explicit success and failure mass ON=declared_carrier
real_structure: complex Hermitian positive states with explicit classical flag blocks
grading: r ordered slots and retained flags
action_owner: repository-construction -- supplied conditional mathematical model
target: sharp normalized successful output error MAP-TYPE=evaluation
```

## Result

The heralded consumers of [K2441](k2441-heralded-adaptive-batch-2026-11-01.md) and [K2442](k2442-replicated-process-distance-2026-11-01.md) admit a stronger error guarantee. For equal input/output dimension d, r slots, q=d^(-2r) and input trace-distance allowance epsilon,

    D(normalized successful output, ideal output)
        <= min(1, d^(2r-1) epsilon).                         (1)

The constant and the entire capped envelope are sharp over the unrestricted causal target class. The previous epsilon/(q-epsilon) bounds remain valid conservative bounds; no prior result is withdrawn. The same local slope is attained at the original mixed product instruments. Global attainment for every fixed original target is not claimed.

This is conditional quantum-information mathematics, not native GU recovery. SC-META-53 remains UNCERTAIN; source, ledger0.263 and canon are unchanged. The established comb/link-product framework is [Chiribella, D'Ariano and Perinotti](https://arxiv.org/abs/0904.4483); no novelty claim is made.

## 1. Use both output masses

For positive operators A,B of nonzero traces s,q, triangle inequality gives

    2 max(s,q) D(A/s,B/q) <= ||A-B||1+|s-q|.                 (2)

For example if q>=s, write q(A/s-B/q)=(A-B)+(q-s)A/s. The other case interchanges A,B. Thus a completed success/failure distance at most e implies D<=e/max(s,q)<=e/q. The lower denominator q-e is unnecessary. Equal-success orthogonal mass transfer saturates (2), so e/(q+e) is not a valid universal replacement.

K2441 proves P*(I)<=lambda I for the whole success CP map, lambda=1/d_A1, independent of later feedback and flags. The CP map P/lambda is trace-nonincreasing and has a CPTP completion by a failure flag. Contractivity therefore gives

    ||P(rho)-P(sigma)||1+|Tr P(rho)-q| <=2 lambda epsilon.    (3)

Combining(2),(3) yields C epsilon with C=lambda/q=D_in^2/d_A1. This works for arbitrary actual program states; only the target identity P(sigma)=q O uses causality. Success is guaranteed when lambda epsilon<q. When success is independently nonzero, the capped bound still holds beyond that regime.

A completed-operation half-diamond error kappa contributes without lambda scaling:

    theta=lambda epsilon+kappa,
    s>=q-theta,
    D<=min(1,theta/q), provided s>0.                         (4)

The guaranteed nonzero-success regime is theta<q. A desired error tau<1 follows from theta<=tau q. Replacing kappa by lambda kappa would require an additional scaled-operation premise. Storage/controller errors remain real operational costs.

## 2. All-slot causal sharpness

For equal d>=2, let Phi be the normalized maximally entangled vector and

    v=|0>_R1 tensor Phi_(B1,R2) ... tensor Phi_(B[r-1],Rr),
    L=d^(-1/2)(<v| tensor I_Br), alpha=d^(-(2r-1)).

This is the physical success Kraus operator of the pure-input forwarding controller. For H=|v><v| tensor Z with trace-zero Hermitian Z, LHL*=Z/d. The perturbation has zero final-output partial trace, so it changes none of the comb normalization equations. Around I/d^(2r), sufficiently small positive and negative perturbations remain positive causal combs and have output/input trace-distance ratio C=d^(2r-1). The upper bound is consequently sharp on causal differences for every r, not just two slots.

For global attainment choose

    sigma=(I_previous/d^(2r-1)) tensor |0><0|,
    rho_u=sigma+u |v><v| tensor (|1><1|-|0><0|), 0<=u<=alpha.

Both are positive causal combs: the only reduced eigenvalue is alpha-u, and the final-output partial trace of the perturbation vanishes. D(rho_u,sigma)=u; both success probabilities equal q; normalized output distance is u/alpha. Taking u=min(epsilon,alpha) proves the minimax envelope (1) over all such targets.

For the original flagged instruments, the all-plus Choi block is full rank. Embed the same H in that flag history. A product of the original minimum plus-block eigenvalues supplies a strictly positive perturbation window. Flag-independent forwarding retains flags and attains the same local slope. This does not identify an arbitrary error state as causal, or give global attainment at each fixed original target.

## 3. Released consumers and resource comparison

K2442's mean-distance certificate allows history-selected controllers T_t with fresh private initialization. Apply (3) separately before averaging; their target outputs may differ but each target success probability is q. If the mean resource distance over actual used indices is epsilon, the normalized mean actual success subchannel differs from the same-history ideal mean by at most (lambda epsilon+kappa)/q. This is success-weighted normalization, not the mean of individually normalized outputs or an ideal-history trajectory.

For two qubit slots, q=1/16, lambda=1/2. A one-percent output target with kappa=10^-6 permits epsilon<=0.001248. The old sufficient condition epsilon+kappa<=tau*q/(1+tau) permits only about0.000617812. Under a fixed epsilon proportional to n^(-1/2) tomography bound, that allowance ratio would reduce the leading sample requirement by about4.08; it is a conditional scaling comparison, not a full optimized experiment or measured saving. Pair-loss distance bounds scale n^(-1/4) and require their own fourth-power comparison.

Neither improvement reduces ideal success cost d^(2r) or supplies trusted routing, calibration, private initialization or quantum storage. Uniformly random correlated-block use is a separate interface in [K2445](k2445-correlated-block-certificate-2026-11-01.md).
[Exact probe](../../tests/channel-swings/k2444_sharp_heralded_transfer_probe.py), [report](../../lab/process/k2444-sharp-heralded-transfer.json). Written universal proofs and finite exact controls are distinct evidence. Independent internal review is not proof-assistant or external-expert certification.
