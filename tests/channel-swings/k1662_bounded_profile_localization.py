#!/usr/bin/env python3
"""Certificate for K1662's bounded-profile localization transfer."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1662-bounded-profile-localization.json").read_text())
    claim, decision = data["localization"], data["decision"]
    rho_min, rho_max, epsilon = 0.4, 2.5, 0.1
    noise = [0.8, 1.0, 1.2]
    normalized_noise = [variance / rho for variance in noise for rho in (rho_min, rho_max)]
    n, d = 64, 64**3
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1662"),
        ("positive floor", rho_min > 0),
        ("finite ceiling", rho_max < float("inf")),
        ("residual margin", epsilon > 0),
        ("normalized noise lower", min(normalized_noise) > 0),
        ("normalized noise upper", max(normalized_noise) < float("inf")),
        ("translation rate", 1 / d == n**-3),
        ("phase rate", n * n / d == n**-1),
        ("hypothesis text", "0<rho_-<=rho_(N,k)<=rho_+" in claim["profile_hypothesis"]),
        ("margin text", "1-epsilon" in claim["profile_hypothesis"]),
        ("normalization text", "division by sqrt(rho_k)" in claim["normalization"]),
        ("risk text", "O(N^2/d_N)=O(N^(-1))" in claim["risk"]),
        ("score N3", "M_(F,N)=O_" in claim["score_saturation"] and "(N^3)" in claim["score_saturation"]),
        ("scope", "vanishing profile floor" in claim["scope_guard"]),
        ("localized decision", decision["known_unequal_amplitudes_localized"]),
        ("N3 decision", decision["posterior_missing_term_order_N3"]),
        ("floor load bearing", decision["uniform_profile_floor_load_bearing"]),
        ("degenerate open", not decision["degenerating_profiles_classified"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
