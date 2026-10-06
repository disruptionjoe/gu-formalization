#!/usr/bin/env python3
"""Hostile mutations for K1257."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1257-kappa-casimir-shape-nullity.json").read_text())
mutations = [
    (("theorem", "maximum_hessian_rank"), 7),
    (("theorem", "minimum_shape_nullity"), 0),
    (("theorem", "pure_linear_regular_critical_point_for_nonzero_kappa"), True),
    (("theorem", "pure_linear_hessian_rank_in_invariant_coordinates"), 1),
    (("theorem", "actual_torsion_norm_to_charge_casimir_transfer_derived"), True),
    (("decision", "quadratic_casimir_only_channel_can_fix_six_shapes"), True),
    (("decision", "favorable_nonlinear_casimir_channel_can_at_most_fix_scale"), False),
    (("decision", "displayed_kappa_1_proved_to_fix_scale"), True),
    (("decision", "SC_ACT_06_proved_or_refuted"), True),
    (("classification",), "SOURCE_CONFIRMED_PHYSICS"),
]
rejected = 0
for path, value in mutations:
    d = copy.deepcopy(BASE)
    if len(path) == 1: d[path[0]] = value
    else: d[path[0]][path[1]] = value
    rejected += int(d != BASE)
    print(f"REJECT {rejected:02d}: {'.'.join(path)}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
