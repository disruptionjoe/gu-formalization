#!/usr/bin/env python3
"""K1253: exact scale/shape data inventory for the two-weight selector."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1253-two-weight-selector-data-inventory.json").read_text())
I = DATA["inventory"]
weights = (2, 4, 6, 7, 8, 10, 12)
r0 = Fraction(3)
shapes = (Fraction(1,2), Fraction(-2,3), Fraction(3,4), Fraction(-4,5), Fraction(5,6), Fraction(-6,7))
selected = (r0**2,) + tuple(r0**d*c for d, c in zip(weights[1:], shapes))
recovered = tuple(value / r0**d for value, d in zip(selected[1:], weights[1:]))
checks = [
    ("one positive scale is explicit", I["selected_scale"] == "r0>0"),
    ("six shape values are explicit", len(I["selected_shapes"]) == 6),
    ("selector family carries seven values", I["independent_selector_data_count"] == 7),
    ("selected invariant list is complete", len(I["selected_invariants"]) == 7),
    ("forward map reconstructs I2", selected[0] == 9),
    ("inverse map recovers all six shapes", recovered == shapes),
    ("parameterization is bijective on the horn", I["parameterization_is_bijective_on_horn"]),
    ("fixed degrees add no tunable selector datum", I["fixed_weight_degrees_add_selector_data"] == 0),
    ("favorable kappa scale grant leaves six shapes", I["favorable_kappa1_as_scale_grant_leaves_shape_data"] == 6),
    ("source displays no shape ratios", not I["source_displays_shape_ratios"]),
    ("source boundary coupling remains absent", not I["source_derives_boundary_coupling_to_chart"]),
    ("construction does not reduce unowned freedom", not DATA["decision"]["construction_reduces_unowned_regular_orbit_freedom"]),
]
for name, item in DATA["pinned_inputs"].items():
    checks.append((f"{name} digest is pinned", hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() == item["sha256"]))
for label, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {label}")
failures = [label for label, ok in checks if not ok]
print(f"TOTAL {len(checks)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
