---
title: "K1180 I1B native candidate admission boundary"
status: active_research
doc_type: exact_i1b_native_candidate_admission_boundary
created: "2026-10-05"
claim_ceiling: current K132 candidate admission boundary; no protected verdict change
manifest: lab/process/k1180-i1b-native-candidate-admission-boundary.json
probe: tests/channel-swings/k1180_i1b_native_candidate_admission_boundary_probe.py
target_claim: SC-ACT-06
---

# K1180 I1B native candidate admission boundary

K1176--K1179 reconcile the abstract K132 repair polytope with the strongest
currently serialized nearby native objects.

- One stratum-independent packet needs a shared ceiling of at least `106536`.
- All three-resource allocations at a fixed total are abstractly sharp, so
  dimensions alone do not select a repair kind.
- The strongest single native ceiling leaves `96801/96801/104965` even under
  unproved full independent transport.
- Granting all four ceilings a mutually independent direct sum of rank `4606`
  still leaves `93766/93766/101930`.
- The repository currently contains zero typed K132 couplings and zero measured
  native complement stacks for these four rows.

The next admissible object is therefore exact: supply one source-owned map on
the K132 carrier; compute its causal rank on `ker H` after the rank-98 joint
channel and every earlier admitted map; place those measured complement ranks
inside the repair polytope; then recompute `Qd=0`, negative capture,
propagation, radical equality, domains, closed range, uniform positivity and
maximal generation.

SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains `UNCERTAIN`, and
LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. The producer passes `12/12`; the
hostile probe rejects `12/12`.
