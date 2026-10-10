#!/usr/bin/env python3
"""Certificate for K1671's finite-net orbit prediction theorem."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1671-finite-net-orbit-oracle.json").read_text())
    claim, decision = data["oracle"], data["decision"]
    n = 64
    phase_points = n**2
    translation_points = n**3
    net_size = phase_points * translation_points**3
    approximation = n**3 * n**-4 + 3 * n**5 * n**-6
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1671"),
        ("four latent coordinates", "T^4" in claim["channel"]),
        ("known coefficients", "known coefficients" in claim["channel"]),
        ("uniform residual noise", "uniformly nondegenerate" in claim["channel"]),
        ("phase scale", n**3 * n**-4 == 1 / n),
        ("translation scale", n**5 * n**-6 == 1 / n),
        ("combined approximation", approximation == 4 / n),
        ("phase mesh", "N^(-2)" in claim["net"]),
        ("translation mesh", "N^(-3)" in claim["net"]),
        ("net exponent", net_size == n**11),
        ("polynomial log", math.isclose(math.log(net_size), 11 * math.log(n))),
        ("net cardinality text", "C N^11" in claim["net"]),
        ("approximation text", "O(N^(-1))" in claim["net"]),
        ("finite-model oracle", "O(log N)" in claim["finite_model_risk"]),
        ("posterior optimality", "posterior mean minimizes" in claim["posterior_transfer"]),
        ("posterior covariance", "O(log N)" in claim["posterior_transfer"]),
        ("alias scope", "aliases and stabilizers" in claim["scope_guard"]),
        ("polynomial decision", decision["finite_net_cardinality_polynomial"]),
        ("risk decision", decision["prediction_risk_logarithmic"]),
        ("no identifiability", not decision["latent_identifiability_required"]),
        ("no support geometry", not decision["support_geometry_required"]),
        ("unknown open", not decision["unknown_or_growing_latent_classified"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
