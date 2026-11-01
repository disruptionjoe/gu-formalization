---
title: "K2458 The sharp hook-symbol bound forces quadratic bank growth"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "INTERNAL_TARGET: individually ordinary-null scalar hook banks with subquadratic size surject at every degree"
claim_ceiling: "sharp ordinary-symbol rank2 and quadratic necessary bank growth; no full coupled inverse or convergence conclusion"
---

# K2458 The sharp hook-symbol bound forces quadratic bank growth

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
result: K2458
carrier: real cyclic hooks in fourteen dimensions and the original repeated-polar hook bank LAYER=toy CHIRALITY=N/A
pairing: fixed nondegenerate split metric and raw symmetric ordinary Euler symbol ON=declared_carrier
real_structure: characteristic-zero real coefficients with original Q(sqrt2) embedding
grading: tensor slots, ordinary-symbol rank and homogeneous scalar degree
action_owner: repository-construction -- supplied conditional hook model
target: individually ordinary-null hook bank dimension and actual-bank sharpness MAP-TYPE=evaluation
```

## Result

Every nonzero cyclic hook has ordinary-symbol rank at least two. The bound
is sharp even in the original repeated-polar bank, as the exact probe
constructs a rank-two witness satisfying all original polarity constraints.
Thus one ordinary-null scalar coefficient can depend on at most twelve
independent coordinates, improving K2455's universal bound of thirteen.
An unrestricted scalar inverse built from individually ordinary-null terms
requires at least ceil((n+13)(n+1)/156) summands at receiver degree n:
**quadratic growth**, even when the hooks vary with degree.

This excludes a smaller restricted-bank route, not the full mixed inverse.
Ordinary responses may cancel between terms, and the complete K2449 map has
additional linear generators. Analytic convergence and nonlinear closure
remain open. The conditional hooks are not source-selected GU dynamics.
SC-ACT-01/06 and SC-GEO-55 ASSERTS remain at their exact source scopes;
SC-META-53 remains UNCERTAIN. Ledger0.263 and canon are unchanged.
No novelty, external-expert or proof-assistant certification is claimed.

## 1. A cubic identity rules out rank one

Let h_ijk=-h_ikj and h_ijk+h_jki+h_kij=0. Raise an ordinary covector
using the fixed nondegenerate metric to write

    B(v)_ij=h_ivj+h_jvi.

This invertible reparameterization preserves the rank of the original
A_xi h=sum_a eta_a xi_a(h_iaj+h_jai). Antisymmetry in the last slots gives

    B(v)(v,v)=0                                         (1)

as a polynomial identity, for every v. If rank B=1, then
B(v)=ell(v)Q with nonzero linear ell and a nonzero symmetric Q.
Equation (1) says ell(v)Q(v,v)=0. A polynomial ring over a
characteristic-zero field is an integral domain; hence Q(v,v)=0 identically
and polarization gives Q=0, a contradiction.

Rank zero also forces h=0: B=0 and last-slot antisymmetry make h fully
alternating; the cyclic identity then gives3h=0. Therefore nonzero cyclic
hooks have rank at least2, without needing tracefree or polarity constraints.
The argument is signature-independent. A nonzero alternating3-form is a
contrary control if the cyclic condition is improperly dropped: its symbol
vanishes. Null vectors of the metric do not affect the proof because raising
with a nondegenerate indefinite metric is still invertible.

## 2. Sharpness and original-bank verification

On three same-sign coordinate directions, define c_ij=h_iij by

    C=[[0,1,1],[1,0,-1],[-1,-1,0]], h_iji=-c_ij,         (2)

and set all other components zero. Column sums vanish, giving tracefree
contraction; repeated-index antisymmetry also makes the cyclic identity
immediate. Its three nonzero symbol columns satisfy B1-B2+B3=0,
while two are independent. Thus its rank is2, not3.

Membership in the original polar bank does not follow from those generic
identities. The probe reconstructs K and the original pairing from K2437,
then tests same-sign triples and sign variants directly against every original
polar constraint. It records a surviving exact tensor and proves its rank2
and nullity12 by rational elimination in all105 raw symmetric receivers.
The displayed seed (2) describes the family; the report specifies the actual
surviving indices[2,3,10] and signs[1,1,1]. Both the Gram and full
polarization constraints are directly checked. No generic tracefree tensor is silently treated
as original-polar. The original K2452 rank-three hook remains a valid distinct
scalar primitive; its eleven-coordinate ring is not enlarged by this theorem.

## 3. Consequence for the restricted inverse

For a constant nonzero hook h and scalar polynomial f,
D(hf)=A_df h. If S_h=ker(xi->A_xi h), independence of the complementary
symbol columns forces f to depend only on S_h. Conversely any polynomial
on S_h gives ordinary response zero. Thus the allowed homogeneous
coefficients of degree n+1 have dimension at most

    binom(n+12,11).

The arbitrary fourteen-variable scalar receiver of degree n has dimension
binom(n+13,13). With M individually ordinary-null summands, a necessary
condition for scalar surjectivity is

    M >= ceil[binom(n+13,13)/binom(n+12,11)]
      = ceil[(n+13)(n+1)/156].                          (3)

This applies even to a different bank at every degree. Further polar/boundary
restrictions or overlaps only reduce available dimension; the actual nonzero
normalization4/(n+1) cannot increase rank. Dimension sufficiency is not proved.
The rank-two witness alone does not prove its scalar map is nonzero or useful.
K2452's rank-three scalar family retains its sharper individual n-cubed
counting bound where all chosen hooks have that rank.

This is a genuine strengthening of the restricted-bank lower bound, not
progress on the missing norm estimate for the unrestricted mixed inverse.
The next full-inverse question must allow ordinary-response cancellations
and the complete boundary ideal/linear generators. Additional ranks or
larger counts in this excluded route do not supply analytic convergence.
The written proof and an independent internal specialist review establish
the universal statement; finite original-bank computations certify its
particular sharpness witness and contrary controls.

[Probe](../../tests/channel-swings/k2458_hook_symbol_rank_boundary_probe.py) and [report](../../lab/process/k2458-hook-symbol-rank-boundary.json).
