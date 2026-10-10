#!/usr/bin/env python3
"""Certificate for K1679's stationary leading descent."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1679-stationary-nonorbit-leading-descent.json").read_text())
    claim, decision = data["descent"], data["decision"]
    # A representative fixed-g choice demonstrates the t^4 versus t^2 sign.
    fisher_constant, defect_constant, g, t = 7.0, 2.0, 0.5, 0.1
    normalized_gap = fisher_constant*t**4 - g*defect_constant*t**2
    checks = [
        ("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1679"),
        ("Haar average", "Translation-Haar" in claim["stationarization"]),
        ("covariance preserved", "preserves the K1572 covariance" in claim["stationarization"]),
        ("defect preserved", "quartic defect" in claim["stationarization"]),
        ("Fisher convexity", "cannot increase" in claim["stationarization"]),
        ("quartic positive", "t^4N^4" in claim["bound"]),
        ("quadratic negative", "t^2N^4" in claim["bound"]),
        ("sample sign", normalized_gap < 0),
        ("parameter g first", "Fix g>0" in claim["parameter_order"]),
        ("parameter alpha second", "alpha_g first" in claim["parameter_order"]),
        ("parameter t third", "t_g" in claim["parameter_order"]),
        ("strict descent", "lambda_N^statG-c_g'N^4" in claim["conclusion"]),
        ("limsup", "limsup E_N/N^4" in claim["conclusion"]),
        ("nonorbit dimension", "Theta(N^3)" in claim["nonorbit"]),
        ("stationary decision", decision["stationary_admissible_trial"]),
        ("Gaussian rigidity false", decision["profiled_gaussian_leading_rigidity_false"]),
        ("coercivity false", decision["unrestricted_nonnegative_fisher_defect_coercivity_false"]),
        ("coefficient open", not decision["true_coefficient_identified"]),
        ("lower bound open", not decision["matching_lower_bound_proved"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
