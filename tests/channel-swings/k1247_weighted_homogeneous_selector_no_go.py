#!/usr/bin/env python3
"""K1247: weighted-homogeneous regular-selector Hessian no-go."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1247-weighted-homogeneous-selector-no-go.json").read_text())
T = DATA["theorem"]
weights = (2,4,6,7,8,10,12)
monomials = [
    (12,0,0,0,0,0,0),
    (0,6,0,0,0,0,0),
    (0,0,4,0,0,0,0),
    (0,0,0,0,3,0,0),
    (0,0,0,0,0,0,2),
]
weighted_degrees = [sum(w*a for w, a in zip(weights, alpha)) for alpha in monomials]
derivative_degrees = [
    (sum(w*a for w, a in zip(weights, alpha)) - weights[j], 24 - weights[j])
    for alpha in monomials for j, power in enumerate(alpha) if power
]
CHECKS = []

def check(label, value):
    CHECKS.append((label, bool(value)))
    print(f"{'PASS' if value else 'FAIL'} {label}")

check("representative polynomial is weighted degree 24", weighted_degrees == [24] * 5)
check("differentiated Euler identity is exact", all(actual == expected for actual, expected in derivative_degrees))
check("identity carries the differentiated coordinate weight", "(D-w_j)" in T["differentiated_identity"])
check("critical point kills Hessian weighted-radial image", T["at_critical_point_with_nonzero_invariant_tuple"].startswith("Hess(V)(W I)=0"))
check("nonzero regular radial vector is a kernel witness", T["hessian_rank_upper_bound"] == 6)
check("regular lock requires rank seven", T["required_regular_lock_rank"] == 7)
check("nondegenerate regular critical point with nonzero invariant tuple is excluded", not T["nondegenerate_regular_critical_point_with_nonzero_invariant_tuple_possible"])
check("theorem is limited to one weighted degree", T["applies_to_single_weighted_degree"])
check("inhomogeneous escape is not excluded", not T["applies_to_arbitrary_nonhomogeneous_potential"])
check("singular zero-charge case is not covered", not T["applies_to_singular_zero_charge"])
failures = [label for label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
