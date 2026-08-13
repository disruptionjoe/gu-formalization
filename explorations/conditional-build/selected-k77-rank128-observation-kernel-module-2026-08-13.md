---
artifact_type: exact_construction_and_composition_result
created: 2026-08-13
status: TEN_DEFECTS_SUM_TO_CANONICAL_NORMAL_COVECTOR_SPINOR_KERNEL__FULL_SO6_4_MODULE_EXACT__SELECTED_GRAPH_ONLY_COMPACT_NATURAL
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ONE_FORM_SPINOR_CARRIER_AND_OBSERVATION_PULLBACK__SOURCE_SILENT_ON_RANK1280_KERNEL_MODULE_AND_GRAPH_SPLITTING
canon_verdict_change: none
---

# Selected K77 rank-128 observation-kernel module

## Result first

The ten transverse rank-128 defects are not ten unrelated repair problems.
They are pairwise-disjoint coordinate pieces whose direct sum is exactly the
1,280-dimensional kernel of observation.  That kernel is the canonical
normal-covector--spinor carrier

```text
ker(R_obs) = N*X tensor S,             dimension 10 x 128 = 1280.
```

Its coordinate inclusion intertwines all 45 generators of `so(6,4)` exactly.
The predecessor's `21/45` result did not show that the carrier lacks full
normal covariance.  It showed that the particular zero-form-seed graph
trivialization, and the selected `H640` graph lift from which it is built,
intertwine only the compact `so(6)+so(4)` stabilizer.  Every one of the 24
mixed boosts detects that non-natural splitting.

This closes the proposed full-module identification.  It does not construct a
physical quotient, repair the selected graph, or show that full `Spin(6,4)`
rather than its compact or `U(3,2)` reduction is the physical symmetry after
observation.

## Adaptive preflight

| lens | basis | confidence | contribution |
|---|---|---:|---|
| Layer-0 semantics | actual math | very high | separated a shared subspace, a direct-sum carrier and a chosen trivialization |
| representation theory | actual math | very high | required all 45 normal generators before naming the module |
| principal-bundle geometry | actual math | high | treated the ten normal lines as frame-dependent summands |
| variational bicomplex | actual math | high | kept graph non-naturality distinct from an action-owned BV differential |
| symplectic geometry | actual math | high | refused to call a configuration kernel a reduced phase space |
| source criticism | actual math | high | checked the one-form-spinor and pullback claims without attributing this theorem to Weinstein |
| exact-computation engineering | actual math | high | reused the exact fixture and made the old attractive misreading a firing control |

The search was wholesale for the finite `so(6,4)` module carried by the ten
filed defects.  It did not assume an action parent, physical carrier, BV
differential, domain or external datum.  Success introduces no new object:
`ker(R_obs)` already exists in the observation exact sequence.

## Exact calculation

On the `GF(1009)` fixture retained from v0.227, let `D_i` be the ten transverse
defect images.  The predecessor proved

```text
rank D_i = 128;
rank(D_i + D_j) = 256 for all 45 pairs;
rank(sum_i D_i) = 1280.
```

The observation map has rank 640 on the 1,920-dimensional carrier, so its
kernel has dimension 1,280.  Every `D_i` lies in that kernel.  Hence equality
of subspaces follows without choosing a basis:

```text
direct_sum_i D_i = ker(R_obs).
```

The coordinate normal inclusion from the ten unobserved one-form slots has
the same image.  With the covector representation on `N*` and the spin
representation on `S`, it obeys

```text
G_ij inclusion = inclusion (G_ij^(N*) tensor 1 + 1 tensor G_ij^S)
```

for all 45 generators: 21 compact rotations and 24 mixed boosts.

By contrast, the selected graph lift `L:H640 -> E1920`, its complementary
projector `1-LR`, and the zero-form-seed defect isomorphism each intertwine
exactly 21 of 45 generators.  All 24 mixed boosts fail.  Their *images* remain
the invariant normal module; their chosen splitting/trivialization does not.

## What the result changes

The previous open phrase "normalization/companion solve for full
`so(6,4)` equivariance" was too broad.  No normalization is needed to prove
the carrier theorem.  A much narrower problem remains:

```text
derive an action- or BV-owned moving graph correction that intertwines the
physical normal symmetry, or prove that observation/action reduces the
physical symmetry to the compact or U(3,2) subgroup already respected.
```

This means future work should not run ten independent rank-128 repairs.  It
should solve one graph-splitting/naturality problem over the already-identified
normal module.

## Source and physics boundary

`SC-GEN-50` and `SC-GEN-56` confirm that the upstairs fermion carrier includes
one-form-valued spinors and that observation pullback is part of the proposed
physics map.  The source does not state this rank-1,280 kernel theorem or own
the selected graph splitting.  Therefore the source return is
`SOURCE-CONFIRMS` for the carrier grammar and `SOURCE-SILENT` for the new exact
identification and its remaining repair.

No ledger verdict, raw residue, quotient, P1/P2/P3, canon or public posture
moves.  This is not the physical carrier `Pi_RS^phys`, a chiral cohomology, a
positive domain, an index, or a generation count.

## Hostile post-review summary

- **Summary outrun:** calling `ker(R_obs)` the physical carrier is rejected;
  it is a configuration-level normal module.
- **Superseded object:** ten scalar normalizations cannot repair a graph map
  whose mixed-boost failure is a full splitting/naturality issue.
- **Downstream:** the module-identification condition closes; graph/BV
  naturality, physical symmetry reduction, global descent and cohomology
  survive.
- **Symplectic charge:** no characteristic quotient or reduced two-form was
  computed, so no phase-space claim is admitted.

Verdict: `SURVIVES_AS_EXACT_SCOPED_MODULE_THEOREM__NO_PHYSICS_VERDICT_MOVE`.

## Receipt and next gate

`tests/channel-swings/portfolio_rank128_observation_kernel_module_probe.py`
passes `27/27` successor checks after replaying the predecessor's exact
pairwise certificate.

Next: construct or kill the action/BV-owned moving graph correction, testing
full `Spin(6,4)`, the source-guided `U(3,2)` reduction and the compact
stabilizer as separately typed symmetry hypotheses.  Do not rebuild the
normal carrier and do not perform ten independent repairs.
