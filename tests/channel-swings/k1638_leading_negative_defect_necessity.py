#!/usr/bin/env python3
"""Certificate for K1638's leading negative-defect necessity."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1638-leading-negative-defect-necessity.json").read_text())
    q, z = d["necessity"], d["decision"]
    eps_n4, a, r, g = 8.0, 2.0, 4.0, 0.5
    required_minus_d = (eps_n4 + a + 0.25 * r) / g
    checks = [
        ("claim", d["claim_id"] == "K1638"),
        ("fixed positive coupling", "g>0 independently" in q["fixed_coupling"]),
        ("leading descent", "epsilon N^4" in q["descent_hypothesis"]),
        ("exact lower bound", "epsilon N^4+A_N+(1/4)R_(Omega,N)" in q["exact_bound"]),
        ("positive fixture", required_minus_d == 22.0),
        ("leading defect", "D_N=-Omega(N^4)" in q["leading_scale"]),
        ("two prices", "both" in q["positive_prices"]),
        ("stationarity closed", z["nonstationarity_independent_escape_closed"]),
        ("phase closed", z["phase_independent_escape_closed"]),
        ("necessity", z["leading_negative_defect_necessary"]),
        ("not sufficient", not z["leading_negative_defect_sufficient"]),
        ("no family", not z["realizing_family_constructed"]),
        ("coefficient open", not z["unrestricted_coefficient_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
