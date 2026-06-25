---
title: "Dual-Record Section-Retrieval Witness v0.1"
status: exploration
doc_type: observer_finality_witness
updated_at: "2026-06-25"
source_repos:
  - "../temporal-issuance"
  - "../time-as-finality"
verdict: "OBSERVER_FINALITY_CAPABILITY_SPLIT_ONLY_NOT_GU_SOURCE_GEOMETRY"
---

# Dual-Record Section-Retrieval Witness v0.1

## Purpose

Instantiate the dual-record opportunity result as a GU observer-finality stress
witness.

This is not a GU source-geometry claim. It does not derive the GU operator,
select the 4D/14D split, solve Velo-Zwanziger, prove anomaly cancellation, or
change any canon claim.

The useful GU question is narrower:

```text
Can two observer protocols have the same stable signed-readout record while
retaining different opportunity records that change future section/readout
capability?
```

## Inputs

Temporal Issuance verdict:

```text
E094: Project[O] + Finalize[R] + Lose[K], not Issue[S]
```

Time as Finality fixture:

```text
dual-record-opportunity-fixture-v0.1
```

Fixture result:

```text
A  single-record search traps at state 2
B0 limited fixed-latent search traps at state 2
C  growing-adjacency search generates 2 -> 7 and reaches target 10
B1 exact fixed-latent absorber exposes 2 -> 7 and also reaches target 10
```

## Witness Object

Use the shared prefix:

```text
S_n = accepted stable record [(0 -> 1), (1 -> 2)]
stable state = 2
stable score = 3
signed readout = unchanged across compared protocols
```

Compare opportunity records at the same stable record:

```text
O_B0 = decoy opportunity access; no critical 2 -> 7 edge
O_C  = stuckness record plus generated 2 -> 7 edge
O_B1 = exact latent 2 -> 7 edge
```

The section/readout capability is:

```text
Cap_h(S_n, O_n) =
  can retrieve a future admissible section/readout path to target state 10
  within the remaining proposal horizon h
```

With the frozen horizon:

```text
Cap_h(S_n, O_B0) = false
Cap_h(S_n, O_C)  = true
Cap_h(S_n, O_B1) = true
```

## Required GU Fields

```text
observer_class:
  finite observer protocol with stable record and opportunity-edge memory

stable_record_state S_n:
  accepted prefix [(0 -> 1), (1 -> 2)] with stable state 2

opportunity_record O_n:
  B0 decoy access, C generated critical edge, or B1 exact latent edge

move_graph G_n:
  base local graph plus opportunity edges available to the protocol

proposal_kernel K_n:
  deterministic highest-score admissible edge proposal under equal budget

transfer_rule T_n:
  accepted opportunity edge becomes stable provenance; failed probes remain
  opportunity audit data or enter Lose[K]

section_or_readout_capability:
  future retrieval of a target section/readout path within horizon h

fixed_latent_graph_comparator:
  B1 exact latent edge panel

loss_profile:
  stable record forgets failed probes and unused opportunity edges unless audit
  data is retained separately

effect_verdict:
  Project[O] + Finalize[R] + Lose[K], not Issue[S]
```

## GU Reading

The positive observer-finality content is:

```text
Same stable observer-facing record.
Different opportunity-edge record.
Different future section/readout capability.
```

This is useful for GU because observer-facing smooth shadows or signed readouts
may be stable for one task while future retrieval capabilities remain
protocol-dependent.

## Absorber Reading

The source-side reading is absorbed:

```text
O_B1 has the same capability as O_C when the critical edge is supplied as fixed
latent structure.
```

Therefore the witness does not show:

```text
new GU source geometry
new GU physical layer
new no-go evasion
source-side Temporal Issuance
```

## Relation To Signed Readout

The signed-readout lane already separates:

```text
monotone provenance
non-monotone scalar readout
```

This witness adds a third surface:

```text
future opportunity capability
```

The useful separation is:

```text
stable provenance/readout can match while future section retrieval differs.
```

That is an observer-finality stress test, not a source theorem.

## Demotion Conditions

Demote this witness to vocabulary if it is used to claim:

- GU source geometry;
- a physical two-layer GU mechanism;
- evidence against Velo-Zwanziger, anomaly, generation-count, or chirality blockers;
- source-side issuance after the B1 fixed-latent absorber has already fired;
- a hidden global ledger or global time order.

## Verdict

```yaml
witness_complete: true
same_stable_record_split: true
future_capability_split: true
fixed_latent_absorber_fires: true
effect_verdict:
  Issue[S]: false
  Project[O]: true
  Finalize[R]: true
  Lose[K]: true
claim_status_change: none
GU_use: observer_finality_section_retrieval_stress_surface
GU_non_use: source_geometry_or_no_go_evasion
```
