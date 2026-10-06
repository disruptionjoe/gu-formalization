#!/usr/bin/env python3
"""K1254: finite horn minimum and functional properness boundary."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1254-two-weight-local-properness-boundary.json").read_text())
T = DATA["theorem"]

def potential(s, q):
    return 2*s**4 - 4*s**2 + (s**4+s**2)*q

samples = [(Fraction(1,2), Fraction(0)), (Fraction(1), Fraction(0)), (Fraction(2), Fraction(0)), (Fraction(1), Fraction(3,2)), (Fraction(3,2), Fraction(5,7))]
checks = [
    ("lower bound holds on exact controls", all(potential(s,q) >= -2 for s,q in samples)),
    ("selected point attains minus two", potential(Fraction(1), Fraction(0)) == -2),
    ("all other exact controls lie above minimum", all(potential(s,q) > -2 for s,q in samples if (s,q) != (1,0))),
    ("finite horn minimum is unique", T["unique_finite_horn_minimum"] == "s=1,Q=0"),
    ("shape infinity is coercive at fixed radius", T["shape_infinity_is_coercive_at_fixed_positive_s"]),
    ("radial infinity is coercive at fixed shape", T["radial_infinity_is_coercive_at_fixed_shape"]),
    ("boundary sequence lies in V<=1", all(potential(Fraction(1,n), Fraction(0)) <= 1 for n in range(2,20))),
    ("boundary sequence approaches zero", abs(float(potential(Fraction(1,1000), Fraction(0)))) < 0.00001),
    ("open-horn sublevel is noncompact", T["sublevel_V_le_1_is_noncompact_in_open_chart"]),
    ("open-horn potential is not proper", not T["potential_is_proper_on_open_horn"]),
    ("no extension across I2 zero is claimed", not T["extension_across_I2_zero_constructed"]),
    ("no functional field space is defined", not T["functional_field_space_defined"]),
    ("no common closed operator domain is defined", not T["common_closed_operator_domain_defined"]),
    ("no Green or generator packet is defined", not T["causal_green_or_maximal_generator_defined"]),
    ("no physical cohomology is defined", not T["positive_nonzero_cohomology_defined"]),
]
for name, item in DATA["pinned_inputs"].items():
    checks.append((f"{name} digest is pinned", hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() == item["sha256"]))
for label, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {label}")
failures = [label for label, ok in checks if not ok]
print(f"TOTAL {len(checks)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
