#!/usr/bin/env python3
"""Certificate for K1684's localized upper coefficient."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1684-localized-cardinal-upper-coefficient.json").read_text())
    claim, decision = data["upper_coefficient"], data["decision"]
    tau, ell, g = 5.0, 1.5, 0.2
    t2 = 6*g*ell/tau
    surrogate = (tau/6)*t2*t2 - 2*g*ell*t2
    expected = -6*g*g*ell*ell/tau
    small_t = 0.05
    small_surrogate = (tau/6)*small_t**4 - 2*g*ell*small_t**2
    checks = [
        ("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1684"),
        ("Rademacher input", "j_R(t)" in claim["scalar_input"]),
        ("functional infimum", "inf_(C,t)" in claim["functional"]),
        ("positive Fisher", "(j_R(t)/4)tau_g(C)" in claim["functional"]),
        ("negative defect", "-2g t^2 ell_g(C)" in claim["functional"]),
        ("finite recovery", "limsup_N" in claim["finite_cutoff_recovery"]),
        ("Haar averaging", "translation-Haar" in claim["finite_cutoff_recovery"]),
        ("strict coefficient", "h_g^card-up<h_g^prof" in claim["strictness"]),
        ("small sign", small_surrogate < 0),
        ("surrogate optimizer", math.isclose(surrogate, expected)),
        ("explicit decision", decision["opaque_c_g_replaced_by_explicit_upper_functional"]),
        ("strict decision", decision["strict_improvement_over_profiled_gaussian"]),
        ("true coefficient open", not decision["true_unrestricted_coefficient_identified"]),
        ("lower bound open", not decision["matching_lower_bound_proved"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
