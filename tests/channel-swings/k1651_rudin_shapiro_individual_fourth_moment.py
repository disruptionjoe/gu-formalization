#!/usr/bin/env python3
"""Certificate for K1651's exact individual Rudin--Shapiro fourth moments."""
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def shift(poly, v, sign=1):
    return {tuple(k[i] + v[i] for i in range(3)): sign * c for k, c in poly.items()}


def add(a, b):
    out = dict(a)
    for k, c in b.items():
        out[k] = out.get(k, 0) + c
    return {k: c for k, c in out.items() if c}


def l4(poly):
    corr = defaultdict(int)
    items = list(poly.items())
    for k, a in items:
        for j, b in items:
            corr[tuple(k[i] - j[i] for i in range(3))] += a * b
    return sum(v * v for v in corr.values())


def main():
    d = json.loads((ROOT / "lab/process/k1651-rudin-shapiro-individual-fourth-moment.json").read_text())
    p = {(0, 0, 0): 1}
    q = {(0, 0, 0): 1}
    side = [1, 1, 1]
    stage_checks = []
    for n in range(1, 10):
        axis = (n - 1) % 3
        v = [0, 0, 0]
        v[axis] = side[axis]
        side[axis] *= 2
        sq = shift(q, tuple(v))
        p, q = add(p, sq), add(p, shift(q, tuple(v), -1))
        expected = len(p) ** 2 * (4 / 3 - (-0.5) ** n / 3)
        stage_checks.append((f"stage {n} equal", l4(p) == l4(q)))
        stage_checks.append((f"stage {n} formula", math.isclose(l4(p), expected)))

    qn, z = d["individual_moment"], d["decision"]
    checks = stage_checks + [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1651"),
        ("difference", "16d_n" in qn["difference_identity"]),
        ("disjoint", "disjoint Fourier supports" in qn["orthogonality"]),
        ("closed form", "4/3-(1/3)(-1/2)^n" in qn["closed_form"]),
        ("cubic coefficient", "(-1/8)^r" in qn["cubic_defect"]),
        ("equality decision", z["individual_fourth_moments_equal"]),
        ("closed decision", z["individual_fourth_moment_closed_form"]),
        ("defect decision", z["cubic_defect_coefficient_exact"]),
        ("descent fence", not z["energy_descent_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
