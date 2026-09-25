---
title: "K489--K490 native Neumann-word M-orthogonal complement"
status: active_research
status_axis: operational_state
doc_type: conditional_native_k139_k162_m_orthogonal_projection_and_k168_shape_cross_result
created: 2026-09-25
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K489--K490 native Neumann-word M-orthogonal complement

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

```gu-typed-objects
result: exact native M-orthogonal correction of the first K139 Neumann-word tail, followed by outward q00/q10 bounds for the K168 shape Rayleigh value and trial-to-corrected-tail cross
carrier: K162 q00 and q10 zero-bath seed cyclic subspaces in the fixed K139 positive particle/hole Fock carrier LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: physical Gram M=S* S with S=(1-G_256)^-1 ON=repository_signed_point_control
real_structure: CAR adjoint, momentum conjugation and the q10/q01 signed flavor transport
grading: conserved charge, bath-particle number, Neumann-word order and impurity parity
action_owner: repository-construction; Weinstein's source and a GU action do not select the positive polarization, couplings, extension, scalar center, state or domain
target: corrected first tail line and K168 component cross for a future combined K139/K168 K473 complement estimate MAP-TYPE=not-a-map
```

## Opening comparison and recovered-work correction

The September 25 priority asks for the actual fixed-form complete-complement
attempt, not another abstract acquisition interface. The recovered K485--K487
drafts instead reproduced K413--K415 on the same 936 faces, 13,300 ordered
descriptors and template histograms; K486 even reproduced K414's exact atlas
digest. K488 was a new positive-approach control, but explicitly not a face
interval or recursive cover. Those drafts were preserved under `_local/` and
were not published as new results.

The direct native route starts from K170. For a zero-bath seed `phi`, put

```text
v_n=G^n phi,               S=(1-G)^-1.
```

K170 proves that distinct `v_n` occupy orthogonal bath-number sectors. This
settles the physical Gram geometry of the first two regular-coordinate words
without a finite independent rebuild.

## K489: the free word tail is not M-orthogonal

Write

```text
A=sum_(n>=0)||v_n||^2,       B=sum_(n>=1)||v_n||^2=A-1.
```

Because `S phi=sum_(n>=0)v_n` and `S G phi=sum_(n>=1)v_n`, the exact Gram block
on `(phi,G phi)` is

```text
M_[phi,Gphi] = [[A,B],[B,B]].
```

Thus `<phi,M Gphi>=B>0`: the ordinary bath-number tail is not the
`M=S* S`-orthogonal tail required by K473. The corrected first-tail direction
is

```text
t=G phi-(B/A)phi,
<phi,Mt>=0,
<t,Mt>=B/A.
```

K170's certified first-word integral and untouched word-two-plus bound
`81/3520` give outward `B`, projection-coefficient and corrected-norm intervals
for q00 and q10. This is an actual fixed-operator Gram calculation. It does
not claim that one corrected line is the complete complement.

## K490: the K168 component cross is signed and nonzero

Let `O=sum_(n odd)||v_n||^2`. K168's shape `diag(-2,1,1)` alternates its
eigenvalue with word parity. Direct substitution of the corrected vector gives

```text
q00: DeltaR(phi,t)=+3 O/A,
     theta_t=-2+3 O/(A B),

q10: DeltaR(phi,t)=-3 O/A,
     theta_t= 1-3 O/(A B),

both: |cross|_M^2=9 O^2/(A^2 B).
```

Since the first word is odd, K170 supplies `O>=||G phi||^2`; since every odd
word is in the nonzero tail, `O<=B`. Those relations give rigorous outward
q00/q10 intervals. The component cross is strictly nonzero and flips sign
between the two seeds. A separate absolute estimate of the base and shape
parts would discard that sign and is not a combined-form certificate.

## Decision and boundary

The attempted native split therefore changes method in two ways:

1. a dyadic/free bath-tail decomposition must be Gram-corrected before any
   K473 floor or cross is claimed; and
2. the fixed K168 component already contributes a signed cross on that
   corrected graph, so the next calculation must evaluate the cancellation-
   safe base `R0` form on exactly the same vectors.

The missing base `R0` cross prevents a combined K139/K168 `mu`, a complete
tail floor `gamma`, K473 `beta`, K469 residual budget or K152 interval. A
loose bound on the shape component alone is not a model obstruction. No
source, ledger, canon, paper, public-posture or physical conclusion moves.

## Hostile review

- **Strongest overclaim:** treating the corrected first line as the complete
  K162 complement. It is only the first explicit line in the corrected graph.
- **Strongest contrary route:** a different complete M-orthogonal basis could
  be constructed directly. It must reproduce the same two-vector projection
  on this cyclic slice, so it does not restore the naive tail.
- **Weakest reproducibility seam:** higher-word parity mass is bounded rather
  than evaluated. The intervals use only `a_1<=O<=B` and K170's proved total
  tail; they do not assign unknown word mass to a favorable parity.

## Reproduction

```bash
python3 tests/channel-swings/k489_native_neumann_word_m_orthogonalization.py --write
python3 tests/channel-swings/k489_native_neumann_word_m_orthogonalization_probe.py --selftest
python3 tests/channel-swings/k490_k168_native_shape_cross_estimate.py --write
python3 tests/channel-swings/k490_k168_native_shape_cross_estimate_probe.py --selftest
```
