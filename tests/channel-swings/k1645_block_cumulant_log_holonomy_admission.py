#!/usr/bin/env python3
"""Certificate for K1645's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1645-block-cumulant-log-holonomy-admission.json").read_text())
    a, z = d["admission"], d["decision"]
    c = a["bridge_census"]
    checks = [
        ("claim", d["claim_id"] == "K1645"),
        ("census sum", c["rows"] == c["satisfied"] + c["conditional"] + c["excluded"] + c["missing"]),
        ("rows", c["rows"] == 360),
        ("satisfied", c["satisfied"] == 281),
        ("source asserts", [a["source_claims"][k] for k in ("SC-ACT-01", "SC-ACT-02", "SC-ACT-06")] == ["ASSERTS"] * 3),
        ("source uncertain", a["source_claims"]["SC-META-53"] == "UNCERTAIN"),
        ("ledger stable", a["physics_ledger"] == {"same": 33, "differs": 22, "needs": 31, "over_determined": 2}),
        ("protected rows", set(a["protected_rows"].values()) == {"0/7"}),
        ("block advance", "submacroscopic" in a["quantum_advance"].lower()),
        ("log advance", "log^(1+epsilon)" in a["holonomy_advance"]),
        ("scope fence", "No source" in a["scope_guard"]),
        ("conditional advance", z["conditional_block_coefficient_advance"]),
        ("log advance decision", z["logarithmic_endpoint_advance"]),
        ("macroscopic open", not z["macroscopic_correlated_endpoint_closed"]),
        ("source open", not z["source_owned_action_supplied"]),
        ("physical open", not z["physical_admission_complete"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
