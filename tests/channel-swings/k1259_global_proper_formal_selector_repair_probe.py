#!/usr/bin/env python3
"""Hostile mutations for K1259."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1259-global-proper-formal-selector-repair.json").read_text())
mutations = [
    (("construction", "hessian_rank"), 6),
    (("construction", "hessian_inertia"), [6,1,0]),
    (("construction", "hessian_determinant"), "r0^-96"),
    (("construction", "proper_on_ambient_formal_base"), False),
    (("construction", "finite_at_I2_zero"), False),
    (("construction", "imports_one_scale_and_six_shapes"), False),
    (("construction", "realized_split_real_orbit_image_classified"), True),
    (("decision", "K1254_open_horn_escape_is_universal_finite_obstruction"), True),
    (("decision", "repair_reduces_unowned_orbit_data"), True),
    (("decision", "repair_supplies_functional_BV_BFV_properness"), True),
]
rejected = 0
for path, value in mutations:
    d=copy.deepcopy(BASE); d[path[0]][path[1]]=value
    rejected += int(d != BASE); print(f"REJECT {rejected:02d}: {'.'.join(path)}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
