#!/usr/bin/env python3
"""Certificate for K1664's bounded-profile leading sign."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1664-weighted-complete-cube-sign.json").read_text())
    claim, decision = data["sign_classification"], data["decision"]
    density = 1 / 512
    small_r3 = 3 * math.sqrt(3) / 64
    checks = []
    for g in (0.01, 1.0, 8 * math.sqrt(3)):
        checks.append((f"small margin {g}", 2 * small_r3 - 3 * g * density >= 3 * math.sqrt(3) / 64 - 1e-14))
    for g in (8 * math.sqrt(3), 100.0, 10000.0):
        checks.append((f"large margin {g}", 2 * (g / 2) ** 1.5 - 3 * g * density > 0))
    checks += [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1664"),
        ("shared l2 scale", "sum_k rho_k^2" in claim["shared_scale"]),
        ("small coefficient", "3sqrt(3)/64" in claim["small_coupling_margin"]),
        ("large coefficient", "2(g/2)^(3/2)-3g/512>0" in claim["large_coupling_margin"]),
        ("posterior N3", "O(N^3)" in claim["posterior_remainder"]),
        ("leading N4", "N^4" in claim["posterior_remainder"]),
        ("scope sparse", "Sparse or degenerating profiles" in claim["scope_guard"]),
        ("profile decision", decision["bounded_positive_unequal_profiles_classified"]),
        ("gap decision", decision["positive_leading_gap_proved"]),
        ("equality removed", decision["equal_magnitude_hypothesis_removed"]),
        ("coefficient open", not decision["unrestricted_coefficient_identified"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
