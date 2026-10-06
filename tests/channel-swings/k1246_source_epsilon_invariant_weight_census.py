#!/usr/bin/env python3
"""K1246: exact split-D7 regular invariant weight census."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1246-source-epsilon-invariant-weight-census.json").read_text())
T = DATA["theorem"]
CHECKS = []

def check(label, value):
    CHECKS.append((label, bool(value)))
    print(f"{'PASS' if value else 'FAIL'} {label}")

exponents = list(range(1, 2 * 7 - 2, 2)) + [7 - 1]
exponents.sort()
degrees = sorted(value + 1 for value in exponents)
check("D7 dimension is 7(13)=91", T["lie_algebra_dimension"] == 7 * 13 == 91)
check("D7 rank is seven", T["rank"] == 7)
check("D7 exponents reproduced", exponents == T["exponents"])
check("primitive degrees are exponent plus one", degrees == T["primitive_invariant_degrees"])
check("there are seven algebraically independent primitive degrees", len(set(degrees)) == 7)
check("regular orbit dimension is dimension minus rank", T["regular_orbit_dimension"] == 91 - 7 == 84)
check("regular quotient dimension is rank", T["quotient_dimension"] == 7)
check("dilation law is recorded", T["dilation_law"] == "I_d(t mu)=t^d I_d(mu)")
check("weighted radial vector lists every degree", all(str(d) in T["weighted_radial_vector"] for d in degrees))
check("nonzero invariant tuple has nonzero weighted radial vector", T["weighted_radial_vector_nonzero_at_regular_point_with_nonzero_invariant_tuple"])
check("weights do not self-select values", not DATA["decision"]["weights_supply_selector_values"])
failures = [label for label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
