---
title: "Signature reality and stabilizer commutants: the split-real horn enlarges the involution candidates but selects none"
status: exploration
doc_type: determination
created: "2026-08-27"
grade: "EXACT FINITE REAL-ALGEBRA TYPING; PHYSICAL STABILIZER AND AMBIENT SIGNATURE SELECTION OPEN"
scripts:
  - tests/channel-swings/signature_reality_stabilizer_commutant_probe.py
target_claim: "M-H4 / DQ2"
target_claim_verdict: "EXECUTED_AT_REALITY_AND_DISCONNECTED-STABILIZER-COMMUTANT_CEILING"
comparator_classification: INTERNAL_STRUCTURAL_ONLY
canon_verdict_change: none
---

# Signature reality and stabilizer commutants

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: real-form and disconnected-stabilizer commutant comparison for the two ambient-signature horns
carrier: finite real Clifford Dirac modules and their chiral pair LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: real Clifford-module endomorphism pairing ON=finite real spinor module
real_structure: quaternionic J^2=-1 on Cl(9,5); split-real J^2=+1 on Cl(7,7)
grading: volume-word chiral grading with two connected-Spin halves
action_owner: repository-construction -- no source action or physical quotient is supplied
target: full-Clifford, connected-Spin and disconnected-parity commutants MAP-TYPE=restriction
```

Scope: this result binds the finite real Clifford modules and their exact
connected/disconnected symmetry actions. It does not bind a physical BRST
quotient, interacting observable algebra, source action or ambient-signature
selector.

## Result

The repeated word “commutant” names three different objects. Keeping them
separate resolves the M-H4/DQ2 fork cleanly:

| horn | real Clifford algebra | irreducible real Dirac module | full-Clifford commutant | connected-Spin chiral commutant | after orientation-reversing exchange |
|---|---|---:|---|---|---|
| `(9,5)` | `M(64,H)` | `H^64`, real dimension `256` | `H`, real dimension `4` | `H + H`, real dimension `8` | diagonal `H`, real dimension `4` |
| `(7,7)` | `M(128,R)` | `R^128`, real dimension `128` | `R`, real dimension `1` | `R + R`, real dimension `2` | diagonal `R`, real dimension `1` |

The probe derives the quaternionic rows as exact commutant null spaces of
integer left-multiplication matrices. It adds the chiral projector and then the
orientation-reversing exchange as separate generators, so the reduction
`D + D -> diagonal D` is computed rather than inferred from a label. The
split-real row is the corresponding one-dimensional control.

The dimension dictionary also fences the surviving `128` homonym:

- the `(9,5)` real Dirac module has dimension `256`, complexification dimension
  `128`, and real chiral halves of dimension `128`;
- the `(7,7)` real Dirac module has dimension `128`, complexification dimension
  `128`, and real chiral halves of dimension `64`.

Those equal-looking `128`s do not denote the same carrier.

## The fork outcome

For the antilinear reality operator, `(cJ)^2=|c|^2J^2`. Therefore no scalar
multiple of the quaternionic `(9,5)` operator with `J^2=-1` is an involution,
whereas the split-real `(7,7)` operator with `J^2=+1` is an involution candidate.
The disconnected parity action reduces the two chiral scalar freedoms to one,
but it does not select the sign of that surviving involution or turn it into a
physical observable.

So DQ2 lands on its first preregistered branch: the split-real horn enlarges the
candidate set relative to the Kramers horn. The conjecture that the real
orthogonal structure itself forces the missing sign does not land at this
finite symmetry grade. This does not select `(9,5)` or `(7,7)` and does not move
the open `SIGNATURE-AMBIENT` fork.

## Verification and ceiling

`python3 tests/channel-swings/signature_reality_stabilizer_commutant_probe.py
--selftest` passes `17/17` checks and catches `4/4` planted reference/machinery
mutations. The result is exact finite real algebra. A physical stabilizer
commutant still requires the source-owned quotient/domain and actual observable
algebra; no canon, source, prediction or public posture moves.
