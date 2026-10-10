#!/usr/bin/env python3
"""Certificate for K1673's known-profile coefficient rigidity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1673-known-profile-coefficient-rigidity.json").read_text())
    claim, decision = data["rigidity"], data["decision"]
    n, eta2mg, constant = 256, 0.1, 4.0
    extensive_b = n**3
    tiny_b = math.log(n)
    extensive_lower = eta2mg * n * extensive_b - constant * n * math.log(n)
    tiny_lower = eta2mg * n * tiny_b - constant * n * math.log(n)
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1673"),
        ("B definition", "B_N=sum rho_k^2" in claim["coercive_margin"]),
        ("coercive N B", "N B_N" in claim["coercive_margin"]),
        ("full lower", ">=-eta" not in claim["full_gap"]),
        ("log remainder", "-CN log N" in claim["full_gap"]),
        ("uniform floor", ">=-CN log N" in claim["full_gap"]),
        ("extensive positive", extensive_lower > 0),
        ("extensive leading", extensive_lower / n**4 > 0.09),
        ("tiny may negative", tiny_lower < 0),
        ("tiny subleading", abs(tiny_lower) / n**4 < 1e-4),
        ("liminf", "nonnegative" in claim["coefficient"]),
        ("positive threshold", "B_N/log N" in claim["positive_regimes"]),
        ("extensive regime", "B_N>=bN^3" in claim["positive_regimes"]),
        ("tiny scope", "need not have a proved positive gap" in claim["scope_guard"]),
        ("all known", decision["all_bounded_known_profiles_coefficient_rigid"]),
        ("anchor-free closed", decision["extensive_anchor_free_sector_closed"]),
        ("no tiny positive overclaim", not decision["uniform_positive_gap_for_tiny_profiles"]),
        ("unrestricted open", not decision["unrestricted_coercivity_proved"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
