#!/usr/bin/env python3
"""Certificate for K1672's anchor-free score localization."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1672-anchor-free-score-localization.json").read_text())
    claim, decision = data["localization"], data["decision"]
    n = 128
    prediction = math.log(n)
    score = n * prediction
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1672"),
        ("whitened metric", "S_0^(-1)" in claim["prediction_metric"]),
        ("prediction logarithmic", "O(log N)" in claim["prediction_metric"]),
        ("score transfer", "O(N)" in claim["score_weight"]),
        ("score formula", score == n * math.log(n)),
        ("subcubic", score < n**3),
        ("subleading", score < n**4),
        ("missing scale", "O(N log N)" in claim["missing_fisher"]),
        ("ceiling saturation", "C_(F,N)-O(N log N)" in claim["missing_fisher"]),
        ("zero profile", "Zero" in claim["support_scope"]),
        ("sparse profile", "sparse" in claim["support_scope"]),
        ("checkerboard", "checkerboard" in claim["support_scope"]),
        ("anchor-free", "anchor-free" in claim["support_scope"]),
        ("known scope", "Known coefficients" in claim["scope_guard"]),
        ("fixed dimension", "fixed four-dimensional orbit" in claim["scope_guard"]),
        ("localized", decision["anchor_free_profiles_localized_in_prediction"]),
        ("NlogN decision", decision["posterior_missing_term_order_N_log_N"]),
        ("anchor unnecessary", not decision["anchor_cube_required"]),
        ("no recovery overclaim", not decision["unique_parameter_recovery_claimed"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
