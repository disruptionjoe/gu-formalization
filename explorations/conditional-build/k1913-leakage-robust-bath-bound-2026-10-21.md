---
title: "K1913: Finite-temperature bounds survive population leakage"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU identification, novelty or formal proof
scripts:
  - tests/channel-swings/k1913_leakage_robust_bath_bound.py
  - tests/channel-swings/k1913_leakage_robust_bath_bound_probe.py
---

# K1913: Finite-temperature bounds survive population leakage

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
result: joint-unitary leakage versus Choi-error tradeoff and thermal approximation floor
carrier: four-level system and arbitrary finite bath initially in a product state LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=system_tensor_bath
real_structure: ordinary complex conjugation; source K/C not identified
grading: four population labels, not source graded-IG
action_owner: repository-construction -- arbitrary finite joint endpoint unitary
target: full channel approximation to a supplied extreme Schur channel MAP-TYPE=intertwiner
```

## 1. The exact-preservation loophole is removable

[K1912](k1912-faithful-bath-dephasing-boundary-2026-10-21.md) excludes an
exact extreme rank-two endpoint from a faithful finite bath, and bounds
controlled-unitary approximations. Here the joint unitary may mix all system
populations. A dimension-uniform approximation floor still follows.
The constants below are valid lower bounds, not a sharp global optimizer.

Let n=4, bath dimension d, density rho, lambda=lambda_min(rho), and arbitrary
unitary U on C^n tensor C^d. Initial system and bath are independent.
Let E(X)=Tr_b[U(X tensor rho)U*], with no energy-conservation assumption.
The comparison target is K1903/K1912's Schur channel Phi_C. Use their exact
B,H=B*B, delta=6-4sqrt(2), and h=||H||=4+sqrt(2).

For input |j><j| write the observable population leakage

    ell_j=1-<j|E(|j><j|)|j>,  pbar=(sum_j ell_j)/n.

Let J_E=(E tensor Id)(|Omega><Omega|) for normalized
Omega=sum_j |jj>/sqrt(n), and t=||J_E-J_C||_1/2. Then

    sqrt(t)+sqrt(pbar) >= sqrt(d*lambda*delta/(n*h)).       (1)

In particular, for epsilon=||E-Phi_C||_diamond/2,

    epsilon >= d*lambda*delta/(4*n*h)
            = d*lambda*(6-4sqrt(2))/(16*(4+sqrt(2))).      (2)

Thus arbitrarily small population leakage cannot remove the fixed-temperature,
fixed-bandwidth floor by leaving the controlled-unitary class.

## 2. Proof on the actual joint-unitary blocks

Set A_j=U_jj. Each is a contraction and
ell_j=Tr[rho(I-A_j* A_j)]. In finite dimension choose a polar unitary V_j
extending the polar partial isometry, so A_j=V_j |A_j|. Functional calculus
on 0<=|A_j|<=I gives (I-|A_j|)^2<=I-|A_j|^2, hence

    ||(A_j-V_j)sqrt(rho)||_F^2 <= ell_j.                  (3)

This does not commute rho past A_j, and does not claim U itself is controlled.
Regard the weighted matrices as vectors in Hilbert-Schmidt space. K1912's
tracial residual bound, followed by rho>=lambda I, gives

    sum_l ||sum_j B_lj V_j sqrt(rho)||_F^2 >= a,
    a=d*lambda*delta.

The operator norm of B on the direct sum is sqrt(h). By the triangle
inequality and (3), with W_A=sum_l||sum_j B_lj A_j sqrt(rho)||_F^2,

    sqrt(W_A)+sqrt(h*sum_j ell_j) >= sqrt(a).             (4)

Let Q embed C^n into the Choi space by Q|j>=|jj>.
The compression Q* J_E Q is D_A/n, where
(D_A)_jk=Tr(rho A_k* A_j). Therefore

    Tr[(Q H Q*)J_E]=W_A/n,  Tr[(Q H Q*)J_C]=0.

The effect QHQ*/h lies between zero and identity. Since J_E and J_C are
states, operational trace distance bounds its expectation difference:
W_A/(n*h)<=t. Divide (4) by sqrt(n*h) to prove (1).
No discarded off-diagonal system block is assumed absent: its norm is
measured by ell_j. Every ell_j<=epsilon by the population measurement on
basis input, and t<=epsilon by the entangled input. Thus pbar<=epsilon,
and (1) yields (2). The positive-effect estimate is stronger than treating
H as an arbitrary signed observable and inserting an unnecessary factor two.

The argument also proves a more general statement for any supplied positive
witness H=B*B annihilating C, whenever every d-dimensional unitary family has
normalized-trace residual at least delta>0. Replace n,h,delta accordingly.
It does not assert that every extreme correlation admits such a witness.

## 3. Useful resource and experimental consumers

For rho Gibbs with inverse temperature beta>=0 and spectral bandwidth Delta,
d*lambda>=exp(-beta*Delta), so

    epsilon >= exp(-beta*Delta)*delta/(16*h).             (5)

For desired full-channel error epsilon0<delta/(16*h), a necessary condition is
beta*Delta>=log[delta/(16*h*epsilon0)]. This is a resource necessity, not a
sufficient cooling prescription or total-work statement. Enlarging finite d
at fixed beta and bandwidth cannot remove it. At zero minimum eigenvalue,
(2) is zero and imposes no obstruction; the pure-qubit exact realization
is a necessary countercontrol.

A finite sequence with fresh independent faithful cells is one joint unitary
on their product bath, even with intermediate population mixing. Its factor
d_total*lambda_total equals product_l(d_l*lambda_l). For Gibbs cells this
is at least exp(-sum_l beta_l*Delta_l). Adaptive measurement, postselection,
external reset and initially correlated system-bath states are not included.
The bound does not apply unchanged to an unbounded number of cells with
unbounded total thermal bandwidth, or an infinite bath with lambda_min=0.

Equation (1) is also a direct two-measurement test. A Choi-state distance
upper bound t0 and a mean population-leakage upper bound p0 contradict this
bath class if sqrt(t0)+sqrt(p0)<sqrt(a/(4*h)). Choi trace distance is not an
upper bound on diamond distance; the witness test itself needs no such
identification. A one-input output comparison alone cannot certify the
channel-wide hypothesis in (2).

As a constructive upper comparison, K1912's thermal qubit repair obeys
half-diamond error<=q with d*lambda=2q. The ratio between this upper bound
and (2) is at most 8h/delta for that family; no equality or global sharpness
is claimed. To test actual leakage, compose those controlled bath operations
with a system rotation S on labels1,2. Then A_1=cV_1,A_2=cV_2,A_3=V_3,A_4=V_4,
ell_1=ell_2=1-c^2 and ell_3=ell_4=0. The full Kraus/Choi computation in the
probe checks these identities, not a controlled approximation substituted
for the actual channel. A noncommuting bath-state control checks (3).

## 4. Hostile review and known context

Strongest overclaim: a sharp thermal optimizer or exclusion of every reservoir.
Neither follows. Strongest contrary construction: exact pure/nonfaithful
realizations and arbitrarily cold faithful approximations survive. Weakest
seams: Gram conjugation, noncommuting rho and normalized versus unnormalized
Choi states; all are explicit above. Positive Choi witnesses avoid a weaker
square-root continuity loss from first approximating the entire dilation.

[Kretschmann, Schlingemann and Werner](https://arxiv.org/abs/0710.2495)
establish general Stinespring continuity. That theorem is context, not an
unproved replacement for (3)-(4), and it does not by itself retain the fixed
mixed-bath realization resource. The supplied K1912 witness carries the
bath-specific hypothesis. No novelty assertion is made.


## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN
about indefinite spectra. None selects the positive Hilbert pairing, bath,
scalar drive, observable algebra or physical units here. LT-SM8, LT-GR6b
and AC-F1 remain unchanged. Full20 injection, separate K/C, physical domain
and accessible-algebra identification remain independent construction debts.
No source-register, physics-ledger or canon verdict changes. No GU prediction,
novelty, external expert acceptance or formal proof is claimed. Analytic
arguments carry general scope; exact finite probes test the actual algebra
and countercontrols. Report and dependency-pin checks establish only
consistency and provenance, separately from mathematical-input faults.
