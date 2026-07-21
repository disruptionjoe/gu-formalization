---
title: "P-RANK-FOLD: the chain datum cannot carry the generation selector"
status: active_research
doc_type: exploration
created: 2026-07-21
run_ref: RUN-20260721-023512-repository-work-cycle-cai-hourly
portfolio_item: CONSTRUCTION-SPACE-EXPLORATION
outcome: P-RANK-FOLD-DIRECT-FAIL
---

# P-RANK-FOLD: value provenance survives; payload folding fails

## Bounded question

Can the generation datum be folded into CH-SM's already counted finite
subgroup-chain datum, rather than remaining a separate input?

The question has two construction sides and they must not be conflated:

| side | generation object | subgroup-chain object |
|---|---|---|
| conventional Spin(10) physics | a flavor multiplicity space `F` carrying copies of the matter `16` | a breaking-chain/VEV choice acting on the Spin(10) representation |
| program-native GU | the forced `U = Lambda^2_+ T*X4` triplet, `dim U = 3`, inside the gamma-traceless matter module, still paired with an `SU(2)-` doublet and mirrors | the finite internal breaking-path datum and its spinorial rank-drop direction |

The conventional construction is used to test the claimed fold into the GUT
chain. The native construction is used to test whether GU's geometric triplet
evades the conventional flavor-separation wall.

## 1. Conventional side: exact flavor separation

Write a matter sector with flavor multiplicity as

```text
H_matter = F tensor S_16.
```

A Spin(10) subgroup-chain choice, its tensor VEVs, matter parity, and the
rank-drop direction act on `S_16` and the relevant Higgs representations. On
the matter copies their action has the form

```text
1_F tensor A_chain.
```

It therefore commutes with every endomorphism of `F`. Changing among the
finite chain paths can change the intermediate gauge group, D-parity, and
scale-level phenomenology, but it supplies no equation for `dim F` and no
projector on `F`. This is the representation-theoretic content already seen in
the exact A1-A3 receipts: the 45/54/210/126 menu has no flavor index, matter
parity is scalar on each `16`, and ranks 1, 2, and 3 all satisfy the same VEV
constraints.

A lookup table assigning a generation count to one of the 16 (or conditionally
6) chain labels would not be a fold. It would be a target-coded map with no
equivariance, action, or source provenance, forbidden by the target-free
selector contract.

## 2. Native side: the integer is present, the selection is not

GU does evade the premise that the *number* three must be imported:

```text
d = 4 (structural input)
  -> dim Lambda^2_+ = 3
  -> an SU(2)+ triplet in ker(Gamma).
```

That provenance is exact and remains intact. But the native matter factor has
more structure than a bare triplet. Per chirality its 96 states decompose as

```text
3 (SU(2)+) x 2 (SU(2)-) x 16 (Spin(10)).
```

The internal Spin(10) chain acts on the final factor. It does not remove the
`SU(2)-` doubling, choose one member of each generation/mirror hyperbolic pair,
or produce a nonzero chiral index. The theorem-grade fences remain: the native
triplet is vectorlike, the self-dual connection has generation index zero, and
the native quaternionic-commuting carrier algebra cannot supply an odd
mirror-selective projector in the `(9,5)` H-class.

Thus the native route changes the type of the residual demand. It is not a
free integer value; it is a qualitative, source-owned physicalization map:

```text
forced triplet -> mirror selection + SU(2)- factor collapse -> three physical generations.
```

No current finite chain label constructs that map.

## 3. Disposition

- **Direct fold into the subgroup-chain datum:** `FAIL` on both construction
  sides by sector separation.
- **Native value provenance:** `SURVIVES`; `3 = dim Lambda^2_+` conditional on
  the four-dimensional base input.
- **Residual datum:** rename the former rank/count-integer slot as a
  `generation-physicalization selector` (mirror selection plus factor-2
  collapse). It remains distinct from the finite chain datum.
- **Alternative signature:** the `(7,7)` real-class fork removes the simple
  Kramers parity wall but does not create a convention-rigid value or a chain
  action on flavor; its standing `FREE-INTEGER` result therefore does not
  rescue this fold.
- **Claims and posture:** no claim, canon, verdict, or public consequence moves.
- **B.5:** remains parked at `B5-MIDDLE-SOURCE-GAP`. A future source action may
  own the missing physicalization map, but this probe neither constructs it nor
  designs around the unavailable B.5 differential.

The chain datum and generation selector must be counted separately wherever
both remain imported. The next standing construction-space work is the parked
queue (`P-LATTICE-SWEEP` / `P-OBS-LEG`) only after its declared wake conditions
are rechecked; no automatic second probe is taken here.
