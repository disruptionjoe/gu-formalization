---
artifact_type: exploration_result
doc_type: exact_representation_theorem
created: 2026-08-26
status: exploration
claim_verdict: FIXED_ARENA_OBSTRUCTION_DOES_NOT_TRANSFER_AUTOMATICALLY
title: "Bateman--Turok enlarged-arena control: exact doubled commutant and pairing boundary"
grade: "EXACT finite representation theorem at target-blind toy grade. The commutant identity and copy-parity controls are symbolic. No GU action, S-matrix, physical quotient, state space, positivity theorem or source-native enlargement is constructed."
target_claim: M-S4-FIXED-ARENA-TRANSFER
target_claim_verdict: NONTRANSFER_PROVED__PHYSICAL_RESCUE_UNBUILT
canon_verdict_change: none
priority_change: none
row_change: M-S4_EXECUTED_AT_NONTRANSFER_CEILING
scripts:
  - tests/channel-swings/bateman_turok_enlarged_arena_commutant.py
---

# Bateman--Turok enlarged-arena commutant control

## Result

The fixed-arena commutant obstruction does **not** transfer automatically to
an equivalent two-copy enlargement. For any representation of an algebra
`A` on `V`, the diagonal two-copy representation on `V+V` obeys

`End_A(V+V) = M_2(End_A(V))`.

In particular, when the fixed arena is irreducible and has scalar commutant,
the equivalent doubled arena has a four-dimensional commutant containing the
copy swap

`P_copy = [[0,I],[I,0]]`, `P_copy^2=I`.

This proves the narrow point M-S4 required: a result obtained by exhausting a
fixed arena's commutant cannot be exported to an enlarged arena without
recomputing the representation and its owners. It does **not** prove the
Bateman--Turok mechanism exists on GU's carrier. A copy-distinguishing action
term removes the swap, and the swap does not turn the native internal Krein
form positive: with crossed pairing `eta=P_copy tensor K`,
`eta P_copy=I tensor K` retains the internal inertia.

Scope: exact representation theory on a target-blind finite carrier. No
identification with GU ghost parity, chirality, a physical `C` operator,
unitarity, Born rule, action, quotient, domain, S-matrix or phenomenology.

```gu-typed-objects
result: equivalent two-copy enlargement changes the commutant from End_A(V) to M2(End_A(V)) and introduces a copy-swap involution, while positivity remains pairing-dependent
carrier: target-blind finite module V plus V for a diagonally represented algebra A LAYER=toy CHIRALITY=N/A
pairing: crossed form P_copy tensor K and separately declared auxiliary P_copy control ON=V-plus-V
real_structure: exact rational real matrices; no GU real Clifford form is assigned
grading: copy grading Z_copy=diag(1,-1) exchanged by P_copy
action_owner: repository-construction
target: automatic transfer of fixed-arena commutant conclusions to an enlarged representation MAP-TYPE=not-a-map
```

## Preflight bookend

### Object and claim typing

- `A`: an abstract represented algebra, not the GU source action.
- `V`: one finite representation carrier.
- `V+V`: two equivalent copies with diagonal `A` action.
- `End_A`: algebraic commutant.
- `P_copy`: copy-space swap, not a spectral `C`, ghost parity, chirality or
  physical state selector.
- `K`: an internal indefinite form used only to test whether copy parity
  supplies positivity automatically.
- Claim ceiling: nontransfer of a fixed-arena commutant obstruction; no
  physical rescue.

### Retrieval and correction history

The object search found three distinct prior facts:

1. R3 classified several GU-motivated fixed-arena cores and described their
   `C` operators as noncanonical.
2. The later specialist panel corrected the interpretation: a `C` operator is
   generally fixed only after a complete commuting observable set is named,
   and Bateman--Turok changes the arena rather than selecting inside the old
   commutant.
3. The exceptional-point monodromy test already proved that its branch swap is
   not literally the measured diagonal ghost grading. A second “both are
   `Z/2`” identification is therefore forbidden.

No existing artifact computed the doubled-representation commutant or tested
its pairing dependence.

### Routes considered

1. **Build a GU/Turok two-field action.** Rejected by authority and dependency:
   no source-owned action/S-matrix bridge is available.
2. **Duplicate the existing numerical R3 carrier.** Rejected as primary: it
   would obscure a general exact identity with a large floating computation.
3. **Prove the commutant identity symbolically.** Selected: exact, general,
   target-blind, and sufficient to decide automatic transfer.
4. **Identify copy swap with ghost parity.** Rejected as homonymy. The theorem
   supplies a copy involution only.

## Exact theorem and controls

For the irreducible `M_2` module, the symbolic certificate finds:

- fixed commutant dimension `1`;
- equivalent doubled commutant dimension `4`;
- exact commuting copy swap with square `I`;
- exact anticommutation with the copy grading;
- basis-independent survival under a non-block-diagonal similarity transform;
- reduction to dimension `2` and loss of swap commutation after adding one
  copy-distinguishing observable;
- crossed native-indefinite metric inertia `(2,2,0)` after multiplying by
  `P_copy`; and
- auxiliary-pairing positive control inertia `(4,0,0)`.

The last pair is load-bearing: existence of a commuting `Z/2` in the enlarged
commutant and positivity of a physical pairing are different questions.

## Postflight hostile review

### Strongest overclaim

“The Bateman--Turok rescue works for GU” is not licensed. The theorem does not
construct the GU doubling, its action, copy equivalence, observable set,
physical pairing, quotient, domain or S-matrix.

### Strongest contrary construction

Any action-owned term distinguishing the copies removes `P_copy` from the
commutant. The exact discriminator control demonstrates this rather than
merely naming it. Conversely, exact copy equivalence is a sufficient algebraic
condition for the swap but not evidence that GU owns such equivalence.

### Weakest reproducibility seam

The solver could return a spurious commutant dimension or retain a parity only
because the basis stayed block diagonal. The test derives commutants from
linear equations, transports parity through a non-block-diagonal similarity,
and plants four machinery corruptions. Each corruption reaches a failing
assertion rather than a crash.

### Final disposition

M-S4 is executed at the nontransfer ceiling:

- a two-copy enlargement can introduce a new commuting involution even when
  the fixed commutant was scalar;
- the involution is conditional on equivalent copy actions;
- it does not automatically make an internal Krein form positive; and
- no GU/Turok physical mechanism is constructed.

Reopen physical rescue only with an action/source-owned doubled carrier,
copy-action equivalence, typed interacting observable set, physical pairing
or quotient, common domain and S-matrix/state-preservation argument.

## Reproduction

```text
_local/cas-venv/bin/python \
  tests/channel-swings/bateman_turok_enlarged_arena_commutant.py \
  --selftest
```

Result: `12/12` exact checks and `4/4` planted mutations caught; exit `0`.
