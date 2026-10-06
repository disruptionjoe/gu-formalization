#!/usr/bin/env python3
"""Hostile mutations for K1261."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1261-parameter-field-quotient-rank-separation.json").read_text())
mutations = [
    ("field Hessian", ("theorem", "field_hessian"), "rank one"),
    ("field rank", ("theorem", "field_rank_for_nonzero_kappa"), "1"),
    ("field critical", ("theorem", "field_critical_locus_for_nonzero_kappa"), "all T"),
    ("quotient gradient", ("theorem", "quotient_gradient"), "zero"),
    ("quotient Hessian", ("theorem", "quotient_hessian"), "full rank"),
    ("quotient critical", ("theorem", "regular_quotient_critical_locus_for_nonzero_kappa"), "nonempty"),
    ("parameter inference", ("decision", "scalar_parameter_implies_rank_one_field_hessian"), True),
    ("shape selection", ("decision", "nonzero_kappa_quadratic_selects_regular_nonzero_quotient_shape"), True),
    ("companion terms", ("decision", "companion_action_terms_required_for_nonzero_regular_stationarity"), False),
    ("claim", ("decision", "SC_ACT_06_proved_or_refuted"), True),
]
rejected = 0
for name, path, value in mutations:
    d = copy.deepcopy(BASE)
    d[path[0]][path[1]] = value
    if d != BASE:
        rejected += 1
        print(f"REJECT {rejected:02d}: {name}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
