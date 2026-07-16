---
title: "ADAPTER2-01 correction: the sign is an untransported fiber, not a proved finality-axis polarity"
status: exploration
doc_type: correction
created: 2026-07-15
claim: "bar(b) = finality-axis polarity"
prior_status: "Joe-ratified structural identity, based on the adapter #2 hardening certificate"
current_status: "OPEN conjectural bridge; ratification withdrawn as a scientific result"
verdict: "MONOTONE FORGETFUL FUNCTOR SURVIVES; BRANCH-PRESERVING ADAPTER FAILS; POLARITY IDENTITY OPEN"
runnable:
  - explorations/time-as-finality-crosswalk/adapter2_repair_audit.py
  - explorations/time-as-finality-crosswalk/adapter2_hardening_functor.py
---

# ADAPTER2-01 correction

## Decision

The same-day ratification of

```text
bar(b) = polarity of the finality axis
```

is withdrawn as a scientific result. Joe's governance decision was based on a
certificate that claimed to preserve the polarity fork. The certificate does
not do that. The cross-repo identification returns to `OPEN` as a precise
conjectural bridge. `bar(b)` and `H59` remain `OPEN`.

## The simple implementation mistake

The superseded hardening script mapped a consistent constraint state `S` to

```text
(|S|, number of distinct propositions, |S|).
```

It then considered the source fork

```text
{(p,+1)}    versus    {(p,-1)}
```

and tested that the two source states have no common consistent successor. It
reported that result as if the two images were incomparable in the TaF target.
But both images are exactly

```text
(1,1,1).
```

They are equal, not incomparable. The script tested source incompatibility and
labeled it target fork preservation.

The second control was also mislabeled. Its purported non-functorial
composition comparison constructed the same endpoint pair on both sides and
then tested only whether a random object map happened to be monotone.

## The target mismatch

TaF's actual local D1 profile has four coordinates:

```text
(accessible support, holder redundancy, branch support, reversal cost).
```

The superseded script used three cardinality proxies and called them the real
TaF dimensions. Replacing the proxy with a four-coordinate counting tuple does
not repair the decisive problem. Opposite proposition values still have the
same D1 profile.

TaF also explicitly grades T18's direction as a conditional constructor
theorem. Its physical-arrow reading is weakened, and T57 leaves arrow-direction
circularity open. Therefore T18 cannot currently serve as an independently
derived physical direction that anchors the GU sign.

## The smallest honest repairs

`adapter2_repair_audit.py` checks three candidates.

### 1. Profile-only repair

The map from extension states to monotone count profiles is a functor on the
finite inclusion model. This survives. It is a forgetful functor and collapses
the polarity fork.

### 2. D1Field-style repair

TaF's field-valued vocabulary can carry proposition values in addition to the
local D1 profile. Enriching the target with those values preserves the two fork
states and preserves composition in the finite model.

This does not rescue the identity. The sign is now a discrete fiber label over
one common D1 profile. Forgetting proposition values collapses the two branches
again. The finality order does not choose which fiber point is positive norm.

### 3. Polarity-decorated repair

Adding an explicit `positive` label to the target would make the desired map
possible, but it inserts the datum the bridge was supposed to identify. The
global sign flip preserves every profile and exchanges two equally admissible
anchors. Selecting one requires extra symmetry-breaking data.

## Correct mathematical shape

At the current finite structural grade, the best-supported picture is

```text
polarity fiber  Z/2
        |
        v
finality profile / partial order
```

not

```text
polarity = direction of the finality axis.
```

The profile and extension order can coexist with the sign, but neither derives
nor canonically identifies it. A future positive result needs a source-owned,
non-constant, branch-preserving map between the actual native categories, plus
an independent physical anchor connecting one branch to positive norm.

## What remains valid

- XOR satisfiability, signed-graph balance, and `Z/2` cocycle exactness are the
  same Harary-balance predicate on a shared signed-graph encoding.
- A monotone profile map exists in the finite inclusion toy.
- The profile forgets proposition polarity.
- A field-valued enrichment can retain the polarity as additional data.
- There are two globally flipped anchors unless extra data selects one.

## What is downgraded

- Agreement of three algorithms on one shared graph is not an isomorphism of
  the complete native GU, TI, and TaF objects.
- The second adapter is not proved at branch-preserving functor grade.
- The two-adapter precondition for the cross-repo identity is not met.
- The Krein sign is not presently identified with finality-axis polarity.
- "One posit, everything else forced" is not earned by these adapters.

## Reopen burden

Reopen the identity only when one frozen construction supplies:

1. the native source and target categories;
2. a non-constant, branch-preserving functor on their actual morphisms;
3. proof that the relevant target polarity is not an imported label;
4. a physical rather than merely conditional finality direction;
5. a non-circular map from that direction to the GU positive-norm branch; and
6. independent checks against global sign relabeling and constant-functor
   controls.

## Claim-status consistency receipt

| claim | prior status | current status | weakest dependency | stale wording searched | files updated |
|---|---|---|---|---|---|
| `bar(b) = finality-axis polarity` | ratified structural identity at exploration tier | `OPEN` conjectural bridge | no native branch-preserving adapter or physical polarity anchor | `RESEARCH-STATUS.md`, `CANON.md`, `DERIVATION-PROGRESS.md`, `NEXT-STEPS.md`, `canon/`, `papers/`, `explorations/`, `lab/`, `tests/` | owner adapter documents, gate-pipeline conclusion, open-question note, runnable scripts, `RESEARCH-STATUS.md` |

No canon file, paper, `CANON.md`, `DERIVATION-PROGRESS.md`, or current
`NEXT-STEPS.md` block asserted the ratified identity. They require no claim
patch. The current operational surfaces already keep `bar(b)` and `H59` open.
