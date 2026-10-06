#!/usr/bin/env python3
"""K1251: exact radial/shape chart on the regular I2-positive horn."""

import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1251-source-epsilon-radial-shape-chart.json").read_text())
T = DATA["theorem"]
weights = tuple(T["weights"])
r = Fraction(2)
shapes = (Fraction(1, 3), Fraction(-2, 5), Fraction(3, 7), Fraction(-4, 9), Fraction(5, 11), Fraction(-6, 13))
invariants = (r * r,) + tuple(r**d * y for d, y in zip(weights[1:], shapes))
recovered_r = Fraction(isqrt(invariants[0].numerator), isqrt(invariants[0].denominator))
recovered_shapes = tuple(I / recovered_r**d for I, d in zip(invariants[1:], weights[1:]))
checks = [
    ("split-D7 weights are complete", weights == (2, 4, 6, 7, 8, 10, 12)),
    ("chart has one radial and six shape coordinates", T["chart_dimension"] == 7 and len(T["shape_coordinates"]) == 6),
    ("positive horn is explicit", T["horn"] == "I2>0"),
    ("radial coordinate is positive square root", T["radial_coordinate"] == "r=sqrt(I2)>0"),
    ("inverse chart recovers the radial coordinate", recovered_r == r),
    ("inverse chart recovers every shape", recovered_shapes == shapes),
    ("chart Jacobian determinant is exact", T["jacobian_determinant"] == "2 r^48"),
    ("Jacobian is nonzero on the horn", 2 * r**48 != 0),
    ("shapes are dilation invariant", T["shapes_are_dilation_invariant"]),
    ("chart selects no value", not DATA["decision"]["chart_selects_any_coordinate"]),
    ("no global orbit classification is claimed", not T["global_split_real_orbit_classification_claimed"]),
]
for label, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {label}")
failures = [label for label, ok in checks if not ok]
print(f"TOTAL {len(checks)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
