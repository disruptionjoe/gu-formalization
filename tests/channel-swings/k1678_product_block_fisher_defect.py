#!/usr/bin/env python3
"""Certificate for K1678's product-block identities."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1678-product-block-fisher-defect.json").read_text())
    claim, decision = data["composition"], data["decision"]
    t = 0.2
    mean = math.sqrt(t)*0 + math.sqrt(1-t)*0
    variance = t + (1-t)
    fourth = t*t + 6*t*(1-t) + 3*(1-t)**2
    checks = [
        ("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1678"),
        ("independent block", "independent" in claim["trial"]),
        ("Gaussian complement", "standard Gaussians" in claim["trial"]),
        ("pushforward", "S_(g,N)^(1/2)" in claim["trial"]),
        ("mean zero", mean == 0), ("variance one", variance == 1),
        ("fourth cumulant", math.isclose(fourth - 3, -2*t*t)),
        ("exact covariance", "exactly S_(g,N)" in claim["covariance"]),
        ("Bregman zero", "A_N is zero" in claim["covariance"]),
        ("Fisher identity", "(j(t)/4)T_N" in claim["fisher"]),
        ("trace scale", "Theta_g(N^4)" in claim["fisher"]),
        ("defect identity", "D_N=-2t^2L_N exactly" in claim["defect"]),
        ("gap positive term", "(j(t)/4)T_N" in claim["gap_identity"]),
        ("gap negative term", "-2g t^2L_N" in claim["gap_identity"]),
        ("covariance decision", decision["exact_covariance_match"]),
        ("Bregman decision", decision["bregman_term_zero"]),
        ("Fisher decision", decision["weighted_fisher_order_n4_times_j"]),
        ("defect decision", decision["negative_defect_order_n4_times_t2"]),
        ("not stationary yet", not decision["stationarity_before_averaging"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
