---
title: "K358--K360 order-eight normal-projective atlas"
status: exploration
claim_verdict: internal_structural_and_numerical_control_only
date: 2026-09-23
claim_ceiling: exact finite maximum-coordinate atlas, measure and recursive boundary routing for every reachable order-eight face, plus one non-equal positive complete-evaluator control per reachable codimension; positive-width projective cells, boundary-strip majorants, global face ownership, interior, tails and complete hybrid integrals remain open
manifests:
  - lab/process/k358-order-eight-normal-projective-atlas.json
  - lab/process/k359-order-eight-projective-measure-and-boundary-routing.json
  - lab/process/k360-order-eight-anisotropic-projective-controls.json
producers:
  - tests/channel-swings/k358_order_eight_normal_projective_atlas.py
  - tests/channel-swings/k359_order_eight_projective_measure_and_boundary_routing.py
  - tests/channel-swings/k360_order_eight_anisotropic_projective_controls.py
probes:
  - tests/channel-swings/k358_order_eight_normal_projective_atlas_probe.py
  - tests/channel-swings/k359_order_eight_projective_measure_and_boundary_routing_probe.py
  - tests/channel-swings/k360_order_eight_anisotropic_projective_controls_probe.py
---

# K358--K360 order-eight normal-projective atlas

Classification: `INTERNAL_STRUCTURAL_AND_NUMERICAL_CONTROL_ONLY`.

K356's equal allocation among zeroed axes is one line through each normal
cone. K358 replaces that line as the coordinate model. For a face with zero
set `Z` and codimension `c`, write `rho=sum(t_i)` and `p_i=t_i/rho`. On chart
`a`, choose `p_a` maximal and set `r_i=p_i/p_a`. Then

```text
p_a = 1 / (1 + sum r_i)
p_i = r_i / (1 + sum r_i)
0 <= r_i <= 1
|d p_nonanchor / d r| = (1 + sum r_i)^(-c).
```

The smallest canonical maximal axis owns ties. Thus `c` charts cover the
complete simplex without a factorial permutation atlas. The `517` face
programs deduplicate to `81` masks, `578` charts and `2,998` program-chart
uses. Exact rational inverse and determinant controls pass at every reachable
codimension. K356's equal-normal point is the all-ratios-one corner shared by
the closed charts; it is not evidence about their interiors.

K359 freezes the measure. One chart has angular mass `1/c!`; all `c` charts
sum to the simplex mass `1/(c-1)!`. Ratio-zero boundaries lower positive
support, and maximum ties move to the smallest canonical owner. The
lexicographic support/owner metric proves both recursions terminate. The
compact contract represents `9,940` unique oriented coordinate boundaries,
`41,588` program uses and `4,740,626` nonempty lower strata without emitting
an exponential table.

K360 exercises the numerical interface off the equal line. At `rho=1/2048`,
one non-equal exact rational projective direction is selected at each of the
thirteen reachable codimensions. All `31,200` ordered descriptor controls
retain the full `23` coherent groups, remain finite with positive cumulative
argument floors and overlap the direct complete evaluator.

## Boundary and continuation

Angular boundaries have measure zero, but an interval cell whose closure
touches `r_i=0` still needs a one-sided zero-safe majorant. K349 closes the
all-zero radial scaling; it does not automatically close every angular
coordinate boundary. The next gate is therefore positive-width ratio cells
paired with boundary-strip decay bounds, followed by a disjoint global owner
rule for overlapping face neighborhoods. Only then can the recursive positive
interior and analytic tails join the eighteen K348 hybrids.

K358 passes `9/9` controls and rejects `11/11` hostile mutations. K359 passes
`9/9` and rejects `10/10`. K360 passes `9/9` and rejects `12/12`.

SC-META-53 remains `UNCERTAIN`; RA-F1, LT-SM8, LT-GR6b and AC-F1 remain
`NEEDS`. No source, ledger, canon, paper, public or physical posture changes.
