---
title: "T27 Bridge Audit Crosswalk"
status: exploration
doc_type: crosswalk
updated_at: "2026-06-17"
sibling_artifact: "time-as-finality/TECHNICAL-REPORT-class-relative-bridge-audit-v0.1.md"
---

# T27 Bridge Audit Crosswalk: GU No-Go Theorems and D1RestrictionSystem

**Purpose.** This document maps GU no-go terminology to Time as Finality (TaF)
T26 vocabulary, records the T27 bridge audit findings per theorem, and notes
what the audit reveals about the GU no-go map's diagnoses.

**Non-goal.** This is not a physics proof.  The audit studies the mathematics of
class-relative abstraction, not the correctness of the underlying physics.

---

## Vocabulary mapping

| GU no-go map term | T26/T27 term | Notes |
| --- | --- | --- |
| Richer substrate datum | Richer D1RestrictionSystem | Sites carry accessible chiral data |
| Forgetful operation / smoothing functor | D1RestrictionMorphism | Morphism maps richer sites to restricted sites |
| Restricted class / projected class | Restricted D1RestrictionSystem | Sites carry no accessible chirality |
| "What gets lost in the smooth-bundle shadow" | `forgotten_structure` field of BridgeCase | Patch data not carried by the morphism |
| Smooth-bundle shadow | scalar/vector projection of the restricted system | Both sites have accessible_support=0 |
| Forgetful image | Restriction morphism image | Sites mapped to in the target system |
| No-go theorem | Gluing obstruction in restricted system | global_witness_count=0 for the chirality attempt |
| Richer object evades the no-go | Global section in richer system | global_witness_count > 0 |

---

## Per-theorem findings

### Witten 1981

GU map diagnosis: analogy_strength = **Strong**.  Every published evasion uses
geometric class exits.  Forgetful operation = smoothing functor
`(X_tilde, S, B) -> (X', trivial-bg)`.

T27 finding:

- Richer system: 2 sites (`smooth_bulk`, `defect_stratum`).  Global section
  exists via `anomaly_inflow` patch (`chiral_bulk != chiral_defect`).
- Restricted system: 2 sites.  Gluing obstruction via `smooth_field` variable
  shared across both patches (forces chiral_A = chiral_B) conflicting with
  `chirality_requirement` (demands chiral_A != chiral_B).
- Morphism `witten_smoothing_functor`: site_map_total=True,
  local_profiles_preserved=False, obstruction_status_preserved=False.
- **Bridge verdict: FAITHFUL (H1).**  The finite abstraction captures the
  Witten class-relative structure.  The forgotten structure is the defect
  stratum profile and the anomaly_inflow patch.

Crosswalk note: the smoothing functor in the GU map maps
`(singular X, brane/flux data) -> (smooth shadow X', trivial-bg)`.
The T27 morphism maps `defect_stratum -> smooth_site_B`, losing the defect
profile `(accessible_support=1, holder_redundancy=2, branch_support=1)` and
the `anomaly_inflow` patch constraint.  These correspond exactly to the
"Net chirality data localized on S; anomaly-inflow contributions; topological
class of the gauge background" listed as forgotten in the GU map (§2.1).

---

### Nielsen-Ninomiya

GU map diagnosis: analogy_strength = **Strong** for modified-symmetry and
bulk-boundary framing.  Forgetful operation = on-site locality functor
`phi_local: (bulk+boundary+modified-symmetry) -> d-dim local on-site lattice`.
GU map prediction for sibling #27: assumption (5) — exact on-site chiral
symmetry — is the protocol-side analog of GW/overlap.

T27 finding:

- Richer system: 3 sites (`bulk_spt`, `boundary_site`, `modified_algebra`).
  Global section exists via `boundary_chiral` (`chiral_left != chiral_right`)
  tied to `algebra_consistency` (`anomaly_in same chiral_left`).
- Restricted system: 3 sites.  Gluing obstruction: `locality_hermitian` forces
  chiral_A = chiral_B, `translation_invariance` forces chiral_B = chiral_C,
  `exact_onsit_ua` forces chiral_A != chiral_C.  Chaining produces a
  contradiction.
- Morphism `nn_onsit_locality_functor`: site_map_total=True,
  local_profiles_preserved=False, obstruction_status_preserved=False.
- **Bridge verdict: FAITHFUL (H1).**

Crosswalk note: the GU map notes that "Lüscher's own framing ('realized in a
different way') is exactly the forgetful-image picture."  The T27 restricted
system encodes Lüscher's no-go condition directly: the `exact_onsit_ua` patch
is the on-site U(1)_A assumption, which creates a finite-arithmetic contradiction
when chained with locality and translation invariance.  The richer system's
`modified_algebra` site (accessible_support=1) is lost in the projection —
this corresponds to the Ginsparg-Wilson algebra structure that Lüscher showed
is the cleanest evasion of assumption (5).

GU map test #1 prediction confirmed at the finite level: assumption (5) (the
`exact_onsit_ua` patch) IS the cleanest drop.  Removing that patch from the
restricted system would resolve the obstruction.

---

### Distler-Garibaldi

GU map diagnosis: analogy_strength = **Weak — stress case**.  Every successful
evasion leaves the single-E8 class entirely.  "The forgetful operation is more
like 'collapse a category' than 'compute a shadow'."  GU map explicitly calls
this "the falsification surface for the whole map."

T27 finding:

- Richer system: 4 sites.  The `sm_chirality` site has no counterpart in
  single-E8 representation theory.
- Restricted system: 3 sites.  Obstructed.
- Morphism `dg_single_e8_adjoint_functor`: **site_map_total=False** (incomplete
  site map).
- **Bridge verdict: FAILS — CATEGORY CHANGE (H3).**

Crosswalk note: the T27 finding confirms the GU map's diagnosis exactly.  The
site_map_incomplete failure is the finite-arithmetic equivalent of "the
forgetful operation is more like 'collapse a category'."  In restriction-system
terms: there is no way to define a total site map from the richer 4-site
structure to the restricted 3-site structure because the `sm_chirality` site
carries content (SM chiral generations from bundle data) that has no
single-E8-adjoint analog.

The GU map states: "If no honest functor exists from bundle data to single-E8-
adjoint data that captures the chirality content as a shadow, the unified frame
should explicitly carve out Distler-Garibaldi as outside the synthesis."

T27 confirms: no such functor exists as a D1RestrictionSystem morphism.  DG is
correctly outside the Projection-Obstruction Pattern.

---

## Common pattern: Projection-Obstruction Schema

The T27 audit detects a common finite structure across the two H1 cases:

```
Richer system: global section EXISTS (chiral data consistently assignable)
    |
    |  D1RestrictionMorphism (forgetful functor)
    |  - site_map_total = True
    |  - local_profiles_preserved = False
    |  - obstruction_status_preserved = False
    v
Restricted system: global section OBSTRUCTED (no consistent chiral assignment)
```

**Candidate theorem (Finite Projection-Obstruction Schema):**

> A theorem proved within a projected class corresponds to a gluing obstruction
> in the restricted D1RestrictionSystem.  The richer object resolves this
> obstruction by supplying extra patch data — specifically, the patch constraints
> that allow a consistent global assignment.  The forgetful morphism is
> site-map-complete but loses exactly that patch data, producing two simultaneous
> failures: local_profile_mismatch (site-level data is coarsened) and
> obstruction_status_preserved=False (an obstruction is introduced that did not
> exist in the richer system).

This theorem is about the mathematics of class-relative abstraction.  It is
consistent with the GU map's statement (§3.3): "what the smooth-bundle shadow
forgets is consistently the mechanism (where chirality enters: defect, boundary,
bulk, enriched bordism) while preserving the relation (a smooth 4d EFT-shaped
object)."  In T27 terms: the mechanism is the extra patch data; the relation is
the site structure and transport graph.

---

## GU map diagnoses confirmed by T27

| GU map item | T27 finding |
| --- | --- |
| Witten analogy = Strong | Faithful finite bridge confirmed (H1) |
| NN analogy = Strong for bulk/boundary framing | Faithful finite bridge confirmed (H1) |
| DG analogy = Weak — stress case | Bridge fails with site_map_incomplete (H3) — confirms GU map |
| "What gets lost is the mechanism" | T27: forgotten structure = patch data (anomaly_inflow, boundary_chiral) |
| DG is a category change, not an enrichment | T27: site_map_total=False confirms this at the finite level |
| NN assumption (5) = cleanest drop | T27: removing exact_onsit_ua resolves the restricted obstruction |
| Partial topological unification for Witten/NN | T27: both share the Projection-Obstruction Pattern |
| DG resists unification | T27: DG excluded from the pattern by site_map_incomplete |

---

## Open questions raised by T27

1. **DG richer morphism machinery.** Can the DG bridge be represented in a
   presheaf or functor-category extension of D1RestrictionSystem?  The site
   map incompleteness suggests that a presheaf over the richer site category
   (4-site E8xE8 structure) would need a different restriction map than a
   projection to the 3-site single-E8 structure.

2. **Freed-Hopkins.** T27 did not construct a bridge case for Freed-Hopkins
   (classified as an anomaly classification rather than a no-go).  The GU map
   suggests an enriched bordism category as the richer object.  If the enriched
   bordism forgets the observer/QRF data via an underlying-bordism functor, the
   T27 pattern predicts: if the Freed-Hopkins anomaly class is unchanged by the
   enrichment, the restricted obstruction would persist.  This is consistent with
   the Córdova-Ohmori-Shao persistence pattern cited in the GU map.

3. **Non-geometric Witten evasions.** The GU map notes (I12) that no Witten
   evasion using observer/stochastic/causal-set language is published.  T27's
   Witten bridge assumes the geometric exit (defect stratum).  A T27 extension
   could test whether a non-geometric richer system (observer-site-indexed
   chirality) also produces a faithful bridge, or whether it requires richer
   morphism machinery.

---

## Artifacts

- Primary technical report: `time-as-finality/TECHNICAL-REPORT-class-relative-bridge-audit-v0.1.md`
- Executable bridge models: `time-as-finality/models/gu_class_relative_bridge.py`
- JSON results: `time-as-finality/results/gu-class-relative-bridge-v0.1.json`
- Test suite: `time-as-finality/tests/test_gu_class_relative_bridge.py`
- Source GU map: `canon/no-go-class-relative-map.md`
