#!/usr/bin/env python3
"""Exact coefficient certificate for K1726."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def coefficient(a, x):
    return a * a / 120 - F(7, 36) * a + x * x / 5040 - x / 72 + F(71, 48)


def squares(a, x):
    return F(11, 108) + (a - F(35, 3)) ** 2 / 120 + (x - 35) ** 2 / 5040


def main():
    d = json.loads((ROOT / "lab/process/k1726-regular-path-quartic-floor.json").read_text())
    q, z = d["regular_path"], d["decision"]
    checks = [("schema", d["schema_version"] == "1.0"), ("claim", d["claim_id"] == "K1726")]
    for a, x in [(F(0), F(0)), (F(35, 3), F(35)), (F(-2), F(71)), (F(17, 5), F(-9, 2))]:
        checks.append((f"square identity {a} {x}", coefficient(a, x) == squares(a, x)))
    checks += [
        ("floor exact", coefficient(F(35, 3), F(35)) == F(11, 108)),
        ("a defect positive", squares(F(35, 3) + 1, F(35)) - F(11, 108) == F(1, 120)),
        ("x defect positive", squares(F(35, 3), F(36)) - F(11, 108) == F(1, 5040)),
        ("scope bounded", "uniformly bounded" in q["scope"]),
        ("negative defect", "u_0>0" in q["scope"]),
        ("matched law", "q^2/6+q^3/4" in q["matched_law"]),
        ("two squares", "(a-35/3)^2/120" in q["completed_squares"] and "(x-35)^2/5040" in q["completed_squares"]),
        ("equality", q["equality_conditions"] == "a=35/3 and x=35."),
        ("uniform remainder", "O(q^(9/2))" in q["uniformity"]),
        ("decision floor", z["regular_path_quartic_floor_exact"] == "11/108"),
        ("cubic preserved", z["fixed_seed_cubic_floor_preserved"]),
        ("finite strength open", not z["all_seed_nonperturbative_optimizer_identified"]),
        ("scope guard", "growing support" in d["scope_guard"] and "finite channel strength" in d["scope_guard"]),
    ]
    for n, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {n:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
