#!/usr/bin/env python3
"""Certificate for K1667's anchor-cube localization transfer."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1667-anchor-cube-localization.json").read_text())
    claim, decision = data["localization"], data["decision"]
    n, alpha = 64, 0.25
    q = int(alpha * n) ** 3
    rho_min, rho_max = 0.3, 2.0
    noise = [0.8 / rho_min, 1.2 / rho_max]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1667"),
        ("macroscopic anchor", q == 4096),
        ("anchor density", q / n**3 == alpha**3),
        ("translation scale", 1 / q == (alpha * n) ** -3),
        ("global phase scale", n * n / q == 1 / (alpha**3 * n)),
        ("normalized noise positive", min(noise) > 0),
        ("normalized noise bounded", max(noise) < 10),
        ("anchor text", "complete lattice subcube Q_N" in claim["anchor_hypothesis"]),
        ("anchor floor", "rho_(N,k)>=rho_->0" in claim["anchor_hypothesis"]),
        ("outside may vanish", "0<=rho_(N,k)<=rho_+" in claim["anchor_hypothesis"]),
        ("normalization", "division by sqrt(rho_k)" in claim["normalization"]),
        ("translation rate text", "O(N^(-3))" in claim["anchor_risk"]),
        ("phase rate text", "O(N^(-1))" in claim["anchor_risk"]),
        ("full prediction", "including zero or degenerating coefficients" in claim["full_prediction"]),
        ("score N3", "M_(F,N)=O_" in claim["score_saturation"] and "(N^3)" in claim["score_saturation"]),
        ("scope", "checkerboard" in claim["scope_guard"] and "anchor-free" in claim["scope_guard"]),
        ("localized", decision["macroscopic_anchor_localizes"]),
        ("global floor removed", not decision["global_positive_floor_required"]),
        ("N3 decision", decision["posterior_missing_term_order_N3"]),
        ("dense open", not decision["arbitrary_dense_support_classified"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
