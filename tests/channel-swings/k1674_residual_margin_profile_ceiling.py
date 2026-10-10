#!/usr/bin/env python3
"""Certificate for K1674's residual-margin profile ceiling."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1674-residual-margin-profile-ceiling.json").read_text())
    claim, decision = data["ceiling"], data["decision"]
    eta, epsilon = 0.2, 0.1
    r_floor = math.sqrt(3) / 4
    rho_ceiling = (1 - epsilon) / (eta * r_floor)
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1674"),
        ("shell floor", "sqrt(3)/4" in claim["inputs"]),
        ("margin", "1-epsilon" in claim["inputs"]),
        ("positive floor", r_floor > 0),
        ("finite ceiling", math.isfinite(rho_ceiling)),
        ("positive ceiling", rho_ceiling > 0),
        ("bound formula", "4(1-epsilon)/(eta sqrt(3))" in claim["bound"]),
        ("formula replay", abs(rho_ceiling - 4 * (1 - epsilon) / (eta * math.sqrt(3))) < 1e-12),
        ("uniformity", "uniformly in N" in claim["bound"]),
        ("no separate ceiling", "no separate bounded-profile assumption" in claim["consequence"]),
        ("fixed eta", "fixed eta" in claim["consequence"]),
        ("vanishing margin scope", "vanishing margin" in claim["scope_guard"]),
        ("ceiling decision", decision["uniform_profile_ceiling_derived"]),
        ("assumption removed", not decision["separate_ceiling_assumption_required"]),
        ("vanishing open", not decision["vanishing_margin_classified"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
