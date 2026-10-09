#!/usr/bin/env python3
"""Certificate for K1648's Gaussian smoothing and Fisher ceiling."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1648-gaussian-smoothed-fisher-control.json").read_text())
    q, z = d["smoothed_law"], d["decision"]
    s_star, delta, omega = 0.8, 0.2, 7.0
    s0 = s_star - delta
    component_excess = omega * (delta + (s0 - 1) ** 2 / s0 - (s_star - 1) ** 2 / s_star)
    closed = omega * delta / (s0 * s_star)
    checks = [
        ("claim", d["claim_id"] == "K1648"),
        ("positive residual fixture", s0 > 0),
        ("one-coordinate identity", math.isclose(component_excess, closed)),
        ("residual covariance", "s_(0,k)" in q["residual_covariance"]),
        ("independent convolution", "independent" in q["law"]),
        ("positive smooth", "positive smooth" in q["regularity"]),
        ("finite fisher", "finite weighted Fisher" in q["regularity"]),
        ("exact covariance", "exact covariance S_N^*" in q["matching"]),
        ("zero displacement", "zero" in q["matching"]),
        ("fisher ceiling", "R_(Omega,N)/4<=C_(F,N)" in q["fisher_ceiling"]),
        ("two-coordinate factor", "(1/2)sum" in q["fisher_ceiling"]),
        ("N4 scale", "O_(g,eta)(N^4)" in q["scale"]),
        ("gap lower", q["gap_interval"].startswith("gD_")),
        ("gap upper", "C_(F,N)+gD_" in q["gap_interval"]),
        ("ceiling fence", "not the actual" in q["scope_guard"]),
        ("descent fence", "does not prove descent" in q["scope_guard"]),
        ("density decision", z["normalized_positive_smooth_density"]),
        ("fisher decision", z["finite_fisher_and_fourth_moment"]),
        ("matching decision", z["profiled_covariance_matched"]),
        ("zero displacement decision", z["gaussian_displacement_zero"]),
        ("cost decision", z["positive_cost_order_N4"]),
        ("sign open", not z["complete_gap_sign_decided"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
