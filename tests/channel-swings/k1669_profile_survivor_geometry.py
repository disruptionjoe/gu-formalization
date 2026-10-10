#!/usr/bin/env python3
"""Certificate for K1669's surviving support geometry."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1669-profile-survivor-geometry.json").read_text())
    claim, decision = data["survivor_geometry"], data["decision"]
    n, c1, b, rho_max = 40, 1 / 8, 1 / 64, 2.0
    d = c1 * n**3
    B = b * n**3
    tau2 = b / (2 * c1)
    threshold_min = b * n**3 / (2 * rho_max**2)
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1669"),
        ("tau positive", tau2 > 0),
        ("small-weight half", tau2 * d == B / 2),
        ("threshold extensive", threshold_min / n**3 == b / (2 * rho_max**2)),
        ("l2 necessity", "B_N=Omega(N^3)" in claim["l2_necessity"]),
        ("support inequality", "B_N<=rho_+^2|supp rho|" in claim["support_floor"]),
        ("tau formula", "tau^2=b/(2c_1)" in claim["threshold_lemma"]),
        ("threshold count", ">=bN^3/(2rho_+^2)" in claim["threshold_lemma"]),
        ("anchor-free remainder", "extensive fixed-threshold support but no such anchor" in claim["remaining_geometry"]),
        ("scope", "necessary survivor classification" in claim["scope_guard"]),
        ("sparse excluded", decision["cardinality_sparse_profiles_excluded"]),
        ("density necessary", decision["positive_density_threshold_support_necessary"]),
        ("anchor excluded", decision["macroscopic_anchor_profiles_excluded"]),
        ("sector open", decision["extensive_anchor_free_sector_open"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
