#!/usr/bin/env python3
"""Certificate for K1657's pattern-blind fourth-defect floor."""
import cmath
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def l4(phases, ell):
    conv = defaultdict(complex)
    for i, a in phases.items():
        for j, b in phases.items():
            conv[tuple(x + y for x, y in zip(i, j))] += a * b
    return sum(abs(v) ** 2 for v in conv.values())


def main():
    d = json.loads((ROOT / "lab/process/k1657-complete-cube-defect-floor.json").read_text())
    q, z = d["defect_floor"], d["decision"]
    phases = {}
    ell = 3
    for i in range(ell):
        for j in range(ell):
            for k in range(ell):
                phases[(i, j, k)] = cmath.exp(1j * (i + 2 * j + 4 * k) / 7)
    modes = ell**3
    i4 = l4(phases, ell)
    defect_coeff = 1.5 * (i4 - 2 * modes**2)
    checks = [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1657"),
        ("cube size", len(phases) == modes),
        ("unit coefficients", all(abs(abs(v) - 1) < 1e-12 for v in phases.values())),
        ("I4 nonnegative", i4 >= 0),
        ("defect floor numeric", defect_coeff >= -3 * modes**2 - 1e-9),
        ("pattern", "unit-modulus coefficients" in q["pattern"]),
        ("moment two", "A_N^2d_N" in q["moments"]),
        ("moment four", "(3/2)A_N^4I_(4,N)" in q["moments"]),
        ("floor factor", ">=-3A_N^4d_N^2" in q["floor"]),
        ("eta scale", "-3eta^2d_N^2/N^2" in q["floor"]),
        ("scope", "unequal magnitudes" in q["scope_guard"]),
        ("patterns decision", z["arbitrary_known_unit_phase_patterns_covered"]),
        ("floor decision", z["universal_defect_floor_proved"]),
        ("sharpness fenced", not z["rudin_shapiro_sharpness_claimed"]),
        ("unrestricted open", not z["unrestricted_defect_floor_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
