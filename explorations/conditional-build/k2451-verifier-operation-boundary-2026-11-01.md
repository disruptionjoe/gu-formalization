---
title: "K2451 A four-register local verifier and its operation boundary"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "conditional four-register local operations with certified gaps; no hardware calibration or native GU identification"
---

# K2451 A four-register local verifier and its operation boundary

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
result: K2451
carrier: the original rank-nine purified flagged qubit programs on F tensor R tensor B tensor E LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and operator norm ON=declared_carrier
real_structure: supplied real exact coefficients or complex positive Hilbert states as explicitly typed below
grading: coherent flag F, reference R, output B and nine-dimensional environment E
action_owner: repository-construction -- supplied conditional mathematical model
target: finite local verifier construction and exact effect limitations MAP-TYPE=evaluation
```

## Result

The original two-setting verifier hides an internal entangled measurement. Its particular conditional effects cannot be implemented with only local R/B/F operations and classical communication. Nevertheless a different finite verifier for the same original purification uses only operations local to F, R, B and E, with classical feedforward, and has a proved positive gap. Thus the resource restriction changes the verifier and its statistical cost; it does not eliminate verification.

This is a specialization of established pure-state verification methods, not a novelty claim; [Wang and Hayashi](https://www.nature.com/articles/s41534-019-0226-z) address optimized bipartite protocols. Their bipartition does not make an operation inside S=FRB local among its three registers. Our four-register construction and conservative gap are proved below. SC-META-53 remains UNCERTAIN. These are supplied positive-Hilbert programs; source, ledger0.263 and canon stay unchanged.

## 1. Why the old effects need extra operations

K2447's Fourier conditional S vector is v_k=sum_i sqrt(lambda_i)omega^(-ik)u_i. Selecting its good flag locally leaves sqrt(1-w)|Phi+> on R,B, up to a phase. Thus the partial transpose of that good block of |v_k><v_k| has a negative eigenvalue -(1-w)/2. A positive separable effect remains separable under local postselection and positive under partial transpose. Therefore this exact conditional effect cannot be implemented by local R/B/F operations, shared randomness and classical communication alone, with no shared entangled ancillary resource. K2447's basis-setting good effect is already a Bell projector. Approximate implementation also has a nonzero distance from this specific effect; no quantitative optimal distance is claimed here.

This statement concerns those effects. It does not forbid a different local verification strategy. It also does not classify locality inside a physical encoding of a logical register.

Coherent flags remain necessary for a pure-extension gap. If an acceptance effect Omega is block diagonal in F and Omega Psi=Psi, then Omega fixes each nonzero flag component separately. There are three orthogonal accepted vectors, hence no unique-target gap. If Omega is diagonal in the original E basis the multiplicity is at least nine. This is not evidence that dephased resources implement the wrong reduced program: K2447 proves the opposite distinction.

## 2. Original ten-string support

Rotate R and B by the same real native-axis basis from K2447. This leaves the Bell vector unchanged and turns every bad Kraus Choi vector into a computational product. In site order(F,R,B,E), the target is Psi=sum_i sqrt(mu_i)|x_i>, with strictly positive weights:

| i | x_i |
|---|---|
|0|(0,0,0,0)|
|1|(0,1,1,0)|
|2|(1,0,0,1)|
|3|(1,0,1,2)|
|4|(1,1,1,3)|
|5|(1,1,0,4)|
|6|(2,1,0,5)|
|7|(2,1,1,6)|
|8|(2,0,1,7)|
|9|(2,0,0,8)|

The weights are mu0=mu1=(1-w)/2, followed by the eight bad lambda values from K2447. They are exact rational numbers for both original laws. The probe reconstructs them directly from the original means and weights and verifies the actual native basis rotation, not only an abstract10-dimensional target.

Choose the tree edges(0,1),(0,2),(2,j) for j=3,...,9. Its diameter is3. For each edge ij, its coordinate cube C_ij contains all strings whose site symbols occur at that site in x_i or x_j. A direct inventory shows that C_ij contains exactly the two selected target-support strings. This condition is essential.

## 3. Explicit local edge test

At each site apply the nondestructive two-outcome projector onto the edge's local coordinate alphabet. Communicate the outcomes. Accept if any site is outside; this accepts the target components outside the selected pair. If all sites are inside, fixed sites require no further action. On differing sites measure all but one in the logical X basis; keep E last when it differs, and B last for the good edge(0,1). For parity s in{+1,-1}, accept the last site iff it passes

    (sqrt(mu_i)|x_i,last>+s sqrt(mu_j)|x_j,last>)/sqrt(mu_i+mu_j).

This is a sequence of local two-outcome filters, local basis measurements, classical feedforward and a local rank-one projection. In particular the filters must not distinguish the two endpoint symbols: destructive computational readout before the phase test destroys their coherence.

For the selected pair, every parity branch accepts its normalized target superposition with certainty and rejects

    eta_ij=(sqrt(mu_j)|i>-sqrt(mu_i)|j>)/sqrt(mu_i+mu_j).

One can check this by projecting the two endpoint amplitudes onto the X outcomes; they acquire exactly the parity sign. Therefore the edge effect has eigenvalue1 on the pair target and0 on eta. Positivity of both the effect and its complement implies these eigenvectors have no coupling to the orthogonal complement. Other target strings are outside the cube and are fixed by the accepted-outside branch. Thus each edge test preserves the target support and has restricted failure |eta_ij><eta_ij|.

Separately P_support is a local computational readout followed by acceptance iff the four outcomes match one of the ten listed strings. This measurement may destroy coherence on test rounds; only its acceptance effect matters. It is not used on retained use rounds.

Choose the support test with probability1/2 and each of the nine edge tests with probability1/18. Then

    I-Omega on support = L_tree/18,
    L_tree=sum_edges |eta_ij><eta_ij|.

Outside support, failure is at least1/2 because of the support test. Connectedness of the tree makes the only support vector annihilated by every eta the target Psi. The gap is at least min(1/2,lambda2(L_tree)/18); equality outside support is not asserted.

## 4. Exact conservative gap without spectral fitting

Let v_i=sqrt(mu_i)f_i be perpendicular to Psi, so sum mu_i f_i=0 and ||v||^2=sum mu_i|f_i|^2. Then

    ||v||^2=sum_(i<j) mu_i mu_j |f_i-f_j|^2,
    <v,L_tree v>=sum_edges a_ij |f_i-f_j|^2,
    a_ij=mu_i mu_j/(mu_i+mu_j).

Bound each difference by the path of at most3 edges and Cauchy-Schwarz. An edge partitions the tree into total masses A_e and1-A_e, so

    ||v||^2 <=3 sum_e A_e(1-A_e)|Delta_e f|^2.

Hence a certified gap is

    nu_lb=min(1/2, (1/54) min_e a_e/[A_e(1-A_e)]).        (1)

Both original laws give their minimum on edge(0,2):

|law|exact nu_lb|
|---|---|
|first|85/10071|
|second|221/27783|

These are lower bounds, not optimal four-party local gaps. The exact probe checks local edge effects, support invariance, every tree cut, original rotation/weights, and the bound using rational algebra. No numerical eigenvalue is used as proof.

Removing any tree edge disconnects the support graph and leaves multiple fixed vectors. Replacing(0,2) by(1,2) puts a third target string into its cube and fails perfect completeness for the actual test. Both are exact negative controls. Local coherence in F and E is still required even though cross-register entangling gates are absent.

## 5. Statistical and operational consequence

K2450 applies with nu equal to the proved gap for the law tested and beta a calibrated conditional error of the complete implemented effect. Each test uses either one computational support setting or one of nine edge-setting families, each with a finite set of local parity outcomes. On use, discard E, dephase the program flag and apply the original declared consumer. No test outcomes or E data are passed to the use controller.

The smaller gap costs actual-use samples. At zero failures the sufficient one-percent threshold for one original qubit slot is

    N_U >= ceil(log(1/alpha)/
      [c_delta*(nu*((.01-kappa/q)/C)^2-delta-beta)]),

with q=1/4,C=2 and positive denominator. The probe computes this prospective cost for both original laws using pi=1/2, alpha=.05, delta=beta=10^-8 and kappa=10^-6. It compares the existing nu=1/2 verifier under the same allowances, preserving that its internal effects have different operation requirements. At those exact prospective allowances, the sufficient actual-use counts are22,647,684 and24,184,903 for the two laws, versus346,586 using the existing nu=1/2 effect under the same allowances. These are hypothetical calibration budgets, not actual device data. No count claims future performance, practical storage feasibility, or physically cheap logical qudit control.

This closes a finite logical operation question: entangled internal effects are avoidable by changing the verifier, at an explicit certified statistical cost. Actual coherent flag/environment custody, trusted local basis changes and filters, conditional calibration, memory/storage and use-operation data remain independent missing inputs. If only recorded flags are available, no pure-extension local verifier can repair that loss; retain the measured-resource tomography or block route.

[Exact probe](../../tests/channel-swings/k2451_verifier_operation_boundary_probe.py), [report](../../lab/process/k2451-verifier-operation-boundary.json). Universal proofs, finite original-object checks and prospective budgets are separate evidence. Internal independent review is not external-expert or proof-assistant certification.
