#!/usr/bin/env python3
"""Certificate for K1650's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1650-macroscopic-flat-block-admission.json").read_text())
    q, z = d["protected_integration"], d["decision"]
    checks = [
        ("claim", d["claim_id"] == "K1650"),
        ("census total", "365 rows" in q["census"]),
        ("census satisfied", "286 satisfied" in q["census"]),
        ("source status", "remain ASSERTS" in q["source_status"]),
        ("meta status", "UNCERTAIN" in q["source_status"]),
        ("ledger counts", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in q["ledger_status"]),
        ("needs rows", "remain NEEDS" in q["ledger_status"]),
        ("physical gate", "0/7" in q["physical_admission"]),
        ("leading defect", "D_N=-Theta(N^4)" in q["advance"]),
        ("fisher ceiling", "O(N^4) Fisher ceiling" in q["advance"]),
        ("radial control", "radial macroscopic" in q["advance"]),
        ("next score gate", "posterior-score residual" in q["next_gate"]),
        ("ceiling fence", "Do not replace" in q["scope_guard"]),
        ("descent fence", "infer descent" in q["scope_guard"]),
        ("existence closed", z["leading_defect_existence_closed"]),
        ("cost closed", z["positive_cost_scale_closed"]),
        ("sign open", z["complete_gap_sign_open"]),
        ("source unchanged", not z["source_or_ledger_status_moved"]),
        ("public unchanged", not z["canon_or_public_status_moved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
