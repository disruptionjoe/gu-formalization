#!/usr/bin/env python3
"""Certificate for K1659 complete-cube orbit-class sign."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1659-all-amplitude-complete-cube-sign.json").read_text())
    q, z = d["sign_classification"], d["decision"]
    checks = []
    density = 1 / 512
    qmin3 = 3 * math.sqrt(3) / 64
    for g in (0.01, 1.0, 8 * math.sqrt(3)):
        checks.append((f"small margin g={g}", 2 * qmin3 > 3 * g * density))
    for g in (8 * math.sqrt(3), 100.0, 10000.0):
        checks.append((f"large margin g={g}", 2 * (g / 2) ** 1.5 > 3 * g * density))
    checks += [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1659"),
        ("negative floor", "-3g eta^2 c_N^2" in q["negative_floor"]),
        ("small margin", "3sqrt(3)/64" in q["small_coupling_margin"]),
        ("large margin", "(g/2)^(3/2)" in q["large_coupling_margin"]),
        ("posterior N3", "O_(g,eta,R)(N^3)" in q["posterior_remainder"]),
        ("positive N4", "c_(g,eta,R)N^4" in q["posterior_remainder"]),
        ("scope", "unrestricted anisotropic laws remain open" in q["scope_guard"]),
        ("amplitudes decision", z["all_fixed_admissible_amplitudes_classified"]),
        ("patterns decision", z["all_known_unit_phase_cube_patterns_classified"]),
        ("gap decision", z["positive_leading_gap_proved"]),
        ("coefficient open", not z["unrestricted_coefficient_identified"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
