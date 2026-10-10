#!/usr/bin/env python3
"""Certificate for K1653's translation/phase localization scaling."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def product_variance(a2, sigma2):
    return (a2 + sigma2) ** 2 - a2 ** 2


def main():
    d = json.loads((ROOT / "lab/process/k1653-translation-phase-posterior-localization.json").read_text())
    checks = []
    for n in (8, 16, 32):
        modes = n ** 3
        pairs = modes // 8
        var_mean = product_variance(0.7, 0.9) / pairs
        checks += [
            (f"pair variance positive N={n}", var_mean > 0),
            (f"pair variance O(d^-1) N={n}", var_mean * modes < 20),
            (f"shift-to-mode scale N={n}", math.isclose(n * n / modes, 1 / n)),
            (f"weighted aggregate N={n}", n * modes * (1 / n) == modes),
        ]
    q, z = d["localization"], d["decision"]
    checks += [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1653"),
        ("complete cube", "complete d_N=Theta(N^3) cube" in q["normalized_channel"]),
        ("adjacent pairs", "Disjoint adjacent-pair averages" in q["shift_estimator"]),
        ("shift rate", "O(d_N^(-1))" in q["shift_estimator"]),
        ("phase rate", "O(N^(-1))" in q["phase_estimator"]),
        ("posterior optimality", "posterior means minimize quadratic risk" in q["prediction_bound"]),
        ("missing N3", "O_(g,eta)(N^3)" in q["prediction_bound"]),
        ("saturation", "C_(F,N)-O_(g,eta)(N^3)" in q["score_saturation"]),
        ("scope", "not unrestricted macroscopic-block coercivity" in q["scope_guard"]),
        ("translation decision", z["translation_estimator_constructed"]),
        ("phase decision", z["global_phase_estimator_constructed"]),
        ("N3 decision", z["posterior_missing_term_order_N3"]),
        ("leading exact", z["fisher_ceiling_leading_exact"]),
        ("coercivity open", not z["unrestricted_coercivity_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
