---
title: "Observer-Finality Layer"
status: exploration
doc_type: specification
updated_at: "2026-06-25"
---

# Observer-Finality Layer

The six-axis protocol already requires a candidate to specify:

1. L1 substrate,
2. L2 observer,
3. L3 pairing,
4. L4 causal order,
5. L5 emergence class,
6. L6 coordination loop.

This exploration proposes an optional finality sub-protocol for L2 and L6. It should not yet be promoted to canon, because it needs worked examples and falsification tests.

## Proposed Sub-Protocol

For any candidate that uses observerse, rendering, shadow, consensus, or record language, add these fields:

| field | question |
|---|---|
| record-bearing observer class | What systems are allowed to hold records? |
| record type | What physical or mathematical object counts as a record? |
| causal accessibility | Which records can this observer access, and under what causal constraints? |
| finality relation | What makes a record stable enough to build on? |
| readout target | What scalar, semantic, topological, or geometric value is read from finalized records? |
| failure mode | What would show the finality protocol cannot support the claimed shadow? |

## Source-To-Shadow Chain

The refined chain is:

```text
source substrate
  -> observer protocol / pairing
  -> record-bearing network
  -> finality relation
  -> signed or semantic readout
  -> smooth 4D observer-facing shadow
```

This chain prevents a common layer error: a mathematical projection can be defined all at once, but a physical observer-facing world must be recorded, stabilized, and made causally accessible.

## Categorical Refinement

The sheafification bridge note (`sheafification-as-observer-finality-bridge-v0.1.md`) gives one precise implementation target for the finality relation:

```text
presheaf of local observer records F
  -> associated sheaf / descent completion aF
  -> explicit loss profile across eta_F
```

This refinement is admissible only after the candidate declares the site, coverage, target category, restriction maps, observer capability, readout map, and loss object. The point is not that sheafification proves a GU claim; the point is that it prevents "local records become a stable observer-facing shadow" from remaining an untyped slogan.

The S7 legitimacy-monad refinement (`legitimacy-monad-observer-mathematics-v0.1.md`) adds one stricter requirement: if a finality relation is claimed to make observer mathematics buildable, state the idempotent operation or fixed-point condition that makes the record legitimate for that use. Legitimacy here means observer-record usability, not source-side proof.

## Layer Distinctions

The finality layer must not conflate:

- evidence order: the order in which input information is accumulated,
- causal order: the partial order of influence or accessibility,
- finality relation: the stability relation that lets records be built on,
- readout order: the semantic or scalar decoding of accumulated records.

The signed-readout lane already shows why this distinction matters: monotone provenance can feed a non-monotone scalar readout. Time as Finality adds the question of when the record graph becomes observer-final, but it does not make the scalar readout monotone.

## Relativity Guardrail

Any finality model used by GU must be local or domain-relative. A hidden global commit order is incompatible with the relativity-facing discipline of the L4 causal-order axis.

Acceptable:

```text
observer-facing spacetime = locally reconciled causal record interface
```

Not acceptable:

```text
one universal ledger finalizes all observers' records in a single global order
```

## Promotion Condition

This sub-protocol can move toward canon only after at least two worked six-axis examples show that the added fields catch real errors or produce useful falsification tests.
