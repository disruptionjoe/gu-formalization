---
title: "V15-4 — carrier-faithfulness packet"
status: complete-internal
doc_type: review
paper: "located-not-forced-generation-count-2026-06-29"
date: "2026-07-23"
grade: "computed with independent internal paths; physical transfer remains reconstruction-grade"
---

# V15-4 — carrier-faithfulness packet

## Verdict

The repository consistently supports the compact/complexified carrier packet
used by the bounded theorems:

`Cl(9,5)=M(64,H)`; irreducible real module `H^64` of real dimension `256`;
complex realization dimension `128`; gamma-traceless carrier dimension `1664`;
selected compact self-dual triplet dimension `192`; total-chirality blocks
`96+96`; compact Krein signature `(96,96)`; and compact C1--C5 Hom-space
dimensions `(2,2,2,2,0)`.

The physical-signature audit proves that this packet does not transfer
unchanged to the `(3,1)+(6,4)` real-form split. One Lorentzian Hodge-star half
still has complex dimension `192` and blocks `96+96`, but physical
quaternionic conjugation exchanges it with the opposite half and its Krein
restriction is zero. The conjugation-stable closure has complex dimension
`384`, signature `(192,192)`, and Hom-space dimensions `(4,4,4,4,0)`.

This is a mandatory scope correction, not a central-verdict reversal. The
bounded compact theorem survives; the physical Lorentzian theorem instance
remains reconstruction-grade. No equivariant total-chirality-swapping linear
or antilinear map appears on the computed stable closure.

## Evidence chain

| Link | Value | Evidence role | Primary path | Independent or discriminating path |
|---|---:|---|---|---|
| real Clifford algebra | `M(64,H)` | standard classification instantiated and computed | `reproduce_all.py` LBN-001 | `tests/chase/MOVE-5/verify/indep_check.py` |
| real/complex module | `256_R / 128_C` | classification plus explicit realization | `reproduce_all.py` | size identity `4*64^2=2^14` and explicit quaternionic commutant |
| gamma-trace rank/kernel | `128 / 1664` | computed | `reproduce_all.py` LBN-002/003 | `tests/hardening-pass/verify/oqrk1_indh_rank_indep_check.py` |
| compact selected carrier | `192_C=96+96` | computed | `reproduce_all.py` LBN-006 | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| compact Krein form | `(+96,-96,0)` | computed | `reproduce_all.py` LBN-007 | `tests/antilinear-bound/verify/nonkrein_indep_check.py` |
| compact C1--C5 census | `(2,2,2,2,0)` | computed, encoded in Lean | `tests/enum-completeness/enum_class_c_generators.py` | `tests/enum-completeness/verify/indep_check.py` |
| physical Lorentzian half | `192_C`, K-null, `(2,2,0,0,0)` | direct physical-signature computation | `tests/lorentzian-transfer/physical_signature_transfer_audit.py` | compact and positive-Hilbert discriminating controls in the same audit |
| physical real-form closure | `384_C`, `(192,192)`, `(4,4,4,4,0)` | direct physical-signature computation | `tests/lorentzian-transfer/physical_signature_transfer_audit.py` | machine receipt plus conjugation/covariance/gap checks |

“Independent” here always means an internal methodologically different route,
not an external person or institution.

## Object/type map

| Object | Dimension | Reality closure | Form | Safe use |
|---|---:|---|---|---|
| real irreducible `Cl(9,5)` module | `256_R` | quaternionic | real Clifford module | algebra/module classification |
| computational spinor realization | `128_C` | complex realization of `H^64` | matrix model | gamma and carrier computations |
| compact/complexified selected triplet | `192_C` | closed in the compact baseline | nondegenerate `(96,96)` | current finite Krein theorem instance and `(2,2,2,2,0)` census |
| one physical Lorentzian Hodge half | `192_C` | exchanged with conjugate half | K-null | complex branching and per-half dimension only |
| physical conjugation-stable closure | `384_C` | closed, `J^2=-1` | nondegenerate `(192,192)` | bounded physical-real-form comparison; not yet the true `Y14` carrier |

The words “carrier,” “chirality,” and “physical” must therefore carry one of
these type qualifiers at every load-bearing use.

## Reproduction

From the repository root:

```sh
/Users/joe/Brain/CapacityOS/_local/venvs/research-compute/bin/python \
  papers/candidates/located-not-forced/reproduce_all.py

/Users/joe/Brain/CapacityOS/_local/venvs/research-compute/bin/python \
  tests/lorentzian-transfer/physical_signature_transfer_audit.py
```

Expected terminal lines:

```text
load-bearing checks: 31 passed, 0 failed  (total 31)
AUDIT PASS: 53/53 checks
```

The first command reproduces the compact release packet. The second is the
fork discriminator and must not be described as a second computation of the
same object.

## Formal boundary

Lean consumes the finite block/codomain premises and proves the bounded
deduction and finite transversality implication. It does not construct the
Clifford matrices, prove that the compact packet is the physical Lorentzian
packet, select a `Y14` source-action domain, or build an integer generation
observable.

## Required manuscript wording

1. Scope `192`, `(96,96)`, and `(2,2,2,2,0)` to the compact/complexified
   selected carrier.
2. State the physical half/closure fork where the Lorentzian transfer premise
   first appears.
3. Type antilinear preservation as preservation of total 14-dimensional
   chirality; physical conjugation swaps base and internal chirality
   separately.
4. Keep the finite Krein theorem exact on its compact premise and do not
   advertise it as already instantiated on a physical Lorentzian
   `192`-space.
5. Keep the true-`Y14` source action, physical-state projector, and Fredholm
   index open.
