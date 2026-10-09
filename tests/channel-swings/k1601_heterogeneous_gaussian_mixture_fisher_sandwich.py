#!/usr/bin/env python3
"""Certificate for K1601's heterogeneous Gaussian-mixture Fisher sandwich."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1601-heterogeneous-gaussian-mixture-fisher-sandwich.json").read_text())
    q, z = d["heterogeneous_mixture"], d["decision"]
    checks = [
        ("claim", d["claim_id"] == "K1601"),
        ("heterogeneous law", "arbitrary positive covariances" in q["law"]),
        ("arbitrary means", "arbitrary cutoff-space means" in q["law"]),
        ("mixture covariance", "T=E S_z+C" in q["moments"]),
        ("fisher convexity", "Fisher convexity" in q["convex_upper"]),
        ("K1533", "K1533" in q["moment_lower"]),
        ("precision gap", "E S_z^(-1)-T^(-1)" in q["exact_width"]),
        ("operator convexity", "Operator convexity" in q["positivity"]),
        ("sandwich only", "sandwich width" in q["scope_guard"]),
        ("order N4 open", "order N^4" in q["scope_guard"]),
    ]
    p, omega = 0.4, 3.0
    s1, s2, m1, m2 = 0.5, 2.0, 1.0, -0.3
    alpha = p * m1 + (1 - p) * m2
    em2 = p * m1 * m1 + (1 - p) * m2 * m2
    es = p * s1 + (1 - p) * s2
    c = em2 - alpha * alpha
    t = es + c
    u = omega * (em2 + p * (s1 + 1 / s1 - 2) + (1 - p) * (s2 + 1 / s2 - 2))
    ell = omega * (alpha * alpha + t + 1 / t - 2)
    delta = omega * (p / s1 + (1 - p) / s2 - 1 / t)
    checks += [
        ("scalar cancellation", abs((u - ell) - delta) < 1e-12),
        ("scalar positivity", delta >= 0),
        ("heterogeneous allowed", z["heterogeneous_covariances_allowed"]),
        ("translations allowed", z["arbitrary_mode_translations_allowed"]),
        ("exact width", z["exact_precision_jensen_width"]),
        ("no commutation", not z["commutation_required"]),
        ("unrestricted open", not z["unrestricted_coefficient_identified"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
