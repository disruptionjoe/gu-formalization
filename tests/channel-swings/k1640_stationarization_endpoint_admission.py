#!/usr/bin/env python3
"""Certificate for K1640's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1640-stationarization-endpoint-admission.json").read_text())
    c, p, s = d["census"], d["protected_boundaries"], d["scope_fences"]
    checks = [
        ("claim", d["claim_id"] == "K1640"),
        ("census sum", c["rows"] == c["satisfied"] + c["conditional"] + c["excluded"] + c["missing"]),
        ("rows", c["rows"] == 355),
        ("satisfied", c["satisfied"] == 276),
        ("source asserts", c["source_asserts"] == ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06"]),
        ("source uncertain", c["source_uncertain"] == ["SC-META-53"]),
        ("ledger stable", c["physics_ledger"] == {"SAME": 33, "DIFFERS": 22, "NEEDS": 31, "OVER_DETERMINED": 2}),
        ("scoreability stable", c["k1145_k1150_scorable_rows"] == "0/7"),
        ("all protected", all(value is False for value in p.values())),
        ("stationarization domain", "finite-full-energy finite-Fisher" in s["stationarization_domain"]),
        ("gap moment domain", "finite fourth moment/Wick expectation" in s["gap_domain"]),
        ("fixed positive coupling", s["coupling"] == "fixed g>0 independently of N"),
        ("three wakes", len(d["next_wakes"]) == 3),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
