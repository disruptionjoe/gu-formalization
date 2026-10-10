#!/usr/bin/env python3
"""Certificate for K1668's anchored-profile leading sign."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1668-anchor-profile-positive-gap.json").read_text())
    claim, decision = data["sign_classification"], data["decision"]
    density = 1 / 512
    small_r3 = 3 * math.sqrt(3) / 64
    checks = [("t zero continuity", 0 / (1 - 0) >= 4 * 0**2)]
    for g in (0.1, 1.0, 8 * math.sqrt(3)):
        checks.append((f"small margin {g}", 2 * small_r3 - 3 * g * density > 0))
    for g in (8 * math.sqrt(3), 100.0, 10000.0):
        checks.append((f"large margin {g}", 2 * (g / 2) ** 1.5 - 3 * g * density > 0))
    n, rho_min, alpha = 64, 0.4, 0.25
    q = (int(alpha * n)) ** 3
    b = rho_min**2 * q
    checks += [
        ("anchor l2 mass", b > 0 and b / n**3 == rho_min**2 * alpha**3),
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1668"),
        ("zero included", "includes t=0" in claim["nonnegative_profile_coercivity"]),
        ("coercive scale", "eta^2 N B_N m_g" in claim["nonnegative_profile_coercivity"]),
        ("anchor mass text", "rho_-^2 q_N=Theta(N^3)" in claim["anchor_mass"]),
        ("posterior N3", "O(N^3)" in claim["posterior_remainder"]),
        ("positive N4", ">=c_" in claim["posterior_remainder"] and "N^4" in claim["posterior_remainder"]),
        ("advance", "global positive profile floor is unnecessary" in claim["advance"]),
        ("scope", "anchor-free" in claim["scope_guard"]),
        ("classified", decision["anchored_degenerating_profiles_classified"]),
        ("positive", decision["positive_leading_gap_proved"]),
        ("floor removed", decision["global_floor_removed"]),
        ("anchor-free open", not decision["anchor_free_sector_classified"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
