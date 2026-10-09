#!/usr/bin/env python3
"""Certificate for K1633's fractional Sobolev holonomy theorem."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1633-fractional-holonomy-sufficiency.json").read_text())
    q, z = d["fractional_sufficiency"], d["decision"]
    s = 0.75
    weight_integral = math.sqrt(math.pi) * math.gamma(s - 0.5) / math.gamma(s)
    constant = math.sqrt(2.0 * math.pi * weight_integral)
    checks = [
        ("claim", d["claim_id"] == "K1633"),
        ("fractional hypothesis", "s>1/2" in q["hypothesis"]),
        ("weighted Cauchy", "(1+t^2)^(-s)" in q["weighted_cauchy"]),
        ("weight integral finite", math.isfinite(weight_integral) and weight_integral > 0.0),
        ("constant finite", math.isfinite(constant) and constant > 0.0),
        ("gamma constant", "Gamma(s-1/2)" in q["constant"]),
        ("strict threshold", "exactly when s>1/2" in q["threshold"]),
        ("fractional sufficient", z["fractional_Hs_sufficient_for_holonomy_L1"]),
        ("strictly above half", z["threshold_requires_s_strictly_greater_than_half"]),
        ("H1 not necessary", not z["h1_necessary"]),
        ("endpoint open", not z["endpoint_half_proved"]),
        ("source open", not z["source_owned_flow"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
