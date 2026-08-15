---
title: "Selected-K81 RSAP A3 relative-placement ownership gate"
status: active_research
doc_type: exact_owner_inventory_root_type_and_cross_form_routing_gate
created: "2026-08-15"
registry: lab/process/selected-k81-rsap-a3-relative-placement-ownership-gate.json
probe: tests/channel-swings/selected_k81_rsap_a3_relative_placement_ownership_gate_probe.py
grade: "NO SELECTED JOINT A3 EMBEDDING IS OWNED; CROSS-FORM INCIDENCE TYPE-MISSING; REAL-FORM FACTORS ROUTED AS ALTERNATIVE LOCAL HORNS"
canon_verdict_change: none
---

# Selected-K81 RSAP `A3` relative-placement ownership gate

## Result first

The requested relative six-plane orbit cannot be derived from the current
selected `D7` data because the repository and inspected source return do not
own a joint embedding to derive it from.

The predecessor chain owns three different things:

1. an abstract `D7` root census using the vectors `+-e_i +-e_j`;
2. independently constructed real-`A3` principal factors, including the split
   and `SU(2,2)` factors; and
3. one exact regular endpoint whose Cartan type is split rank five plus compact
   rank two.

None of those objects supplies maps

```text
i_split : R^(3,3) -> R^(7,7),
i_22    : R^(4,2) -> R^(7,7)
```

for the selected endpoint, or an equivalent pair of ambient support
projections. The abstract root vectors contain no real-form involution,
six-plane support, or source-owned edge carrier. The endpoint's `5+2` Cartan
type classifies its seven spectral two-planes; it does not identify either
six-plane with a sum of those planes. The inspected source return is explicit
that no coadjoint-orbit edge field or global symplectic realization is owned.

Therefore the k80 transverse, `A1 x A1`, and `B2` controls remain genuinely
contrary completions of the same present data. There is no selected relative
orbit to compute. The correct state is stronger and cleaner than “choose one
later”: cross-real-form incidence is currently **type-missing**.

At current ownership grade the five real-`A3` factors are alternative local
carrier horns, not charts already known to belong to one common atlas. Generic
full-support split/`SU(2,2)` loci remain disjoint by k80. Special lower-rank
incidence remains possible, but only a new joint-embedding datum can activate
one such bridge. No cross-form moment comparison, primitive transition or
triple cocycle is licensed.

## Layer 0

This is an ownership and classical real-Lie-theory gate. It asks which maps
are actually present in the selected construction. It is not a Higgs,
particle-family, ordinary index, chirality or quantization calculation. Those
comparators do not type the missing six-plane maps and must not be imported.

## What the `D7` root census does and does not say

The wall probe enumerates the `84` roots

```text
{+-e_i +-e_j : 1 <= i < j <= 7}.
```

For example,

```text
e1-e2, e2-e3, e3-e4
```

has the `A3` Cartan matrix and spans the twelve roots `e_i-e_j` on the first
four coordinates. This proves an abstract `A3` root subsystem. It does not
select a real form: that requires a real structure or Satake/Cartan-involution
datum. It also does not produce a six-dimensional orthogonal module inside
the ambient fourteen-dimensional vector representation.

The later split factor adds a signature-`(2,2)` symmetric-pair construction.
The real-form census separately adds `SU(2,2)/SO(2,2)`. Those are valid local
Hamiltonian factors, but neither construction is serialized as the source's
chosen ambient subalgebra at the selected endpoint.

## Why the endpoint Cartan does not repair the missing type

The exact endpoint has five real eigenvalue pairs and two imaginary pairs.
That fixes a regular real Cartan of type `(5,2)` and supports the earlier KKS
period argument. It does not answer which three spectral two-planes, if any,
form the split support; which three form the `SU(2,2)` support; or how two such
supports intersect.

Supplying only the integers `5` and `2` cannot distinguish k80's explicit
relative controls. A derivation would need, at minimum:

| required datum | present status |
|---|---|
| rank-six split support map with pullback signature `(3,3)` | not provided |
| rank-six `SU(2,2)` support map with pullback signature `(4,2)` | not provided |
| proof both maps belong to the same selected endpoint/source construction | not provided |
| common-support dimension and signature, or an equivalent joint-orbit invariant | not provided |

The absence asserted here is repository-scoped and source-return-scoped. It is
not a theorem that no future reading of the source, or no extension of the
model, can supply the maps.

## Routing consequence

The if-and-only-if incidence gate now has a definite procedural answer:

```text
individual real-form factor construction
    does not imply
selected cross-real-form transition data.
```

Consequently:

- keep every completed real-`A3` factor;
- treat distinct real forms as alternative local horns at present;
- do not add a cross-form edge to the atlas nerve;
- reopen incidence only with an explicit pair of selected ambient embeddings
  or equivalent support projections;
- when reopened, compute the common-support dimension and signature first and
  reject the k80 contrary controls before choosing a bridge.

This is not a global RSAP no-go and not a proof that special intersections are
empty. It is a precise refusal to manufacture a transition from data that do
not type one.

## Claim ceiling and next gate

- The abstract `D7` root census selects root-subsystem combinatorics, not a
  real-form six-plane embedding.
- The endpoint owns Cartan type `(5,2)`, not a relative pair of `A3` supports.
- The inspected source return owns no edge carrier or global symplectic
  realization from which such supports could be read.
- Cross-form incidence is `TYPE_MISSING`; no common refinement is constructed.
- All individual real-`A3` principal factors remain constructed at factor
  grade.
- Complete nonsplit singular atlases, deeper `so(7,7)` strata, zero charge and
  global all-strata RSAP remain open. The `182D` cotangent parent remains the
  all-charge fallback.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

The next productive swing is internal rather than cross-form: complete the
`SU(2,2)/SO(2,2)` singular transition atlas across all nine compatible
canonical configurations, with exact degeneration paths, ranks and
within-factor cotangent cocycles. Reopen split/`SU(2,2)` gluing only if a new
source/action-owned joint embedding appears.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k81_rsap_a3_relative_placement_ownership_gate_probe.py
```

The certificate uses the Python standard library and exact integer arithmetic.
