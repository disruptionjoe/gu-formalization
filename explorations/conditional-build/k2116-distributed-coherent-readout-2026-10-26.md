---
title: "K2116: Distributed coherent readout and its entanglement resource"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported mathematics; no source selection, continuum readout implementation, GU verdict or novelty
scripts:
  - tests/channel-swings/k2116_distributed_coherent_readout_probe.py
---

# K2116: Distributed coherent readout and its entanglement resource

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

## 1. Exact distributed recorded instrument

Take nontrivial finite local Hermitian involutions R_A,R_B and R=R_A tensor R_B.
Write P_q=(I+q R)/2, q=+1,-1. A supplied pair of ordinary ancilla qubits starts
in the Bell state (|00>+|11>)/sqrt2. Alice and Bob locally apply ancilla-controlled
R_A and R_B, respectively, and then measure each ancilla in its X basis.
For local outcomes x,y=+1,-1 the system Kraus operator is exactly

    K_xy=(I+xy R)/(2sqrt2)=P_(xy)/sqrt2.               (1)

This follows by contracting the two ancilla bras with |00>I+|11>R; the
normalizations include both local X overlaps and the Bell amplitude.
Grouping the two pairs having q=xy gives

    I_q(rho)=P_q rho P_q.                              (2)

Every fine pair with the same q has the SAME Kraus operator, so keeping or
discarding the individual labels creates no extra within-sector disturbance.
Equations(1)--(2) hold on all system matrix units and after adjoining any
external reference. In particular vacuum/pair or logical |00>/|11> coherence
inside a parity sector survives. Independent local occupation readouts fail
this condition, as K2113 already demonstrates.

Each individual local label is uniform: summing its partner gives probability1/2.
The informative parity is distributed; a single observer obtains it only after
causal classical collection. This is compatible with K2114's unread-channel
classification. Both local controlled reflections, their physical support,
energy cost, ancilla preparation and transmission resources are supplied.
No finite-duration massive-field implementation is inferred from abstract
local gates; noncompact positive-energy code modes do not automatically define
spatially local reflections. This construction settles the finite-factor
interface, not all of K2113's continuum readout debt.

Entangled-ancilla stabilizer measurement is established prior art; see
[Beckman et al. (2001), sectionII](https://preskill.caltech.edu/pubs/preskill-2001-causal.pdf).
We use its mechanism as an explicit consumer with exact errors below, without
claiming novelty. K2081/2082's Givens funnel is a different supplied finite
transport construction and is not repeated here.

## 2. Exact imperfect-entanglement error, not only a continuity bound

Replace the Bell pair by c|00>+s|11>, c,s>=0, c^2+s^2=1. The same operations
and parity grouping give the complete instrument with Kraus operators

    A_q=(c I+q s R)/sqrt2.                              (3)

The map includes the classical q record and postmeasurement system. This is
the error of THIS specified protocol, not the optimum over all protocols
allowed to use the same partially entangled resource. If R has
both eigenspaces, its half-diamond distance from(2) is EXACTLY

    e(c,s)=|c-s|/sqrt2=sqrt((1-2cs)/2).                 (4)

Upper bound: the trace distance between the two pure resource states is the
right side. Tensor any input/reference and apply the SAME apparatus channel;
contractivity gives the bound uniformly.

Lower bound: choose normalized vectors u_+,u_- of R eigenvalues+1,-1 and
input (u_++u_-)/sqrt2. Set a=(c+s)/sqrt2, b=(c-s)/sqrt2; a^2+b^2=1.
In the ordered two-dimensional eigenbasis, the record+ difference from the
ideal block is

    (1/2) [[-b^2, ab],[ab,b^2]],

and the record- block has the reversed diagonal signs. Each block has trace
norm |b|, so the total half trace norm is |b|. This saturates the resource
bound without an external reference. If R is scalar, this witness is absent
and(4) is not asserted as equality. Negative/complex Schmidt phases require
calibration; c,s>=0 is part of the construction.

On an R eigenstate the wrong-label probability is b^2; it is strictly smaller
than the coherent instrument error b when0<b<1. Probability-only validation
therefore misses the stronger requirement.

This gives a direct preparation demand: desired e requires2cs>=1-2e^2.
Local gate implementation errors and K2113 transfer errors add by channel
contraction/telescoping only when established uniformly on their full code and
spectator domains. A record-only probability estimate cannot replace that norm.

## 3. Why an entangled resource is necessary in this local implementation model

Suppose both R_A and R_B have both signs. Choose one vector of each sign in
each factor, and locally prepare their equal superpositions. Under(2), each
outcome has probability1/2 and its normalized system state is a maximally
entangled two-qubit Bell state in those chosen eigenspaces. Local corrections
conditioned on the collected parity turn either into the same Bell state.
Thus an exact implementation by local operations and classical communication,
with initially product system input and no quantum communication, converts its
shared resource to one ebit deterministically (possibly discarding other systems).
A separable resource is impossible. More precisely, a finite PURE shared
resource admits an exact implementation under unrestricted local operations
and classical communication iff its largest squared Schmidt coefficient is
at most1/2. Necessity follows by the deterministic Bell conversion just given;
sufficiency follows by converting the resource to a Bell pair in advance.
[Nielsen's pure-state conversion theorem](https://arxiv.org/abs/quant-ph/9811053)
states that the input Schmidt probability vector must be majorized by the
output vector. For output(1/2,1/2,0,...) this is exactly lambda_max<=1/2.
Entanglement entropy at least one bit is necessary, but not sufficient:
(.6,.2,.2) has entropy greater than one bit while lambda_max>.5.
The supplied Bell pair attains the minimum one-bit entropy. Preparation
communication must occur causally, for example in the common past. No borrowed
entanglement or quantum communication is included in this resource statement. This is a resource lower bound for the
stated implementation class, not for apparatuses permitted to send quantum
systems or create entanglement during later causal interaction. It is distinct
from the classical shared randomness sufficient for the unread channel.

The witness uses admissible coherent superpositions in each local factor.
For a CAR application realize them in same-parity dual-rail corners as in
K2114. An even reflection whose signs lie only in different local superselection
sectors does not automatically permit that preparation or inherit this lower bound.

## 4. Verification and remaining continuum demand

The exact probe derives the Kraus operators from the actual joint ancilla and
gates, checks all system matrix units, checks local record uniformity and
sector coherence, and tests(4) with a rational3/5,4/5 Schmidt pair. It includes
wrong control, wrong measurement basis, omitted coherence and incorrectly
coarse-grained branches as genuine machinery faults. These finite controls
are separate from the all-reference proof and entanglement monotonicity.

Next physical work must build local controlled reflections on the distributed
captured massive code with an actual domain, energy bound and collection time,
or select a different readout class. [K2115](k2115-exact-pulse-excitation-bound-2026-10-26.md)
addresses the independent field-pulse resource; it does not pay for these gates.
