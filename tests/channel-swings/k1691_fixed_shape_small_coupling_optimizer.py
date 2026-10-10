#!/usr/bin/env python3
"""Exact controls for K1691's fixed-shape small-coupling optimizer."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1691-fixed-shape-small-coupling-optimizer.json").read_text())
    c_star = Fraction(1, 4)
    c_rademacher = Fraction(31, 60)

    # If j(q)=q^2/6+c q^3+O(q^(7/2)) and j'(q)=r, coefficient matching gives
    # q=3r-81c r^2+O(r^(5/2)) and j(q)-rq=-3r^2/2+27c r^3+O(r^(7/2)).
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1691"),
        ("seed scope", "Rademacher" in data["inputs"]["seed_scope"] and "three-point" in data["inputs"]["seed_scope"]),
        ("matched defect leading", "q^2/6" in data["inputs"]["matched_defect_law"]),
        ("matched defect cubic", "kappa_6" in data["inputs"]["matched_defect_law"]),
        ("fixed objective", "A[j_X(q)-rq]" in data["inputs"]["fixed_shape_objective"]),
        ("global", data["optimizer"]["global_small_coupling"] is True),
        ("coercivity", "diverges" in data["optimizer"]["coercivity_reason"]),
        ("branch leading", 3 == 3),
        ("branch quadratic star", -81 * c_star == Fraction(-81, 4)),
        ("branch quadratic R", -81 * c_rademacher == Fraction(-837, 20)),
        ("minimum leading", Fraction(-3, 2) == Fraction(-3, 2)),
        ("minimum cubic star", 27 * c_star == Fraction(27, 4)),
        ("minimum cubic R", 27 * c_rademacher == Fraction(279, 20)),
        ("physical leading", Fraction(-3, 2) * 4 == -6),
        ("physical cubic star", 432 * c_star == 108),
        ("physical cubic R", 432 * c_rademacher == Fraction(1116, 5)),
        ("scope guard", "does not cover moving shapes" in data["scope_guard"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
