#!/usr/bin/env python3
"""Independent exact/hostile replay for K294."""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k294-order-seven-global-radial-simplex-atlas.json"


def valid(payload: dict) -> bool:
    chart = payload["global_chart"]
    norm = payload["normalization_replay"]
    release = payload["release_test"]
    return all(
        (
            chart["jacobian"] == "q^5",
            chart["native_projective_product"] == "product_i g_i=q^6*product_i p_i",
            "q^11" in chart["transformed_native_density"],
            Fraction(norm["simplex_integral"]) == Fraction(1, factorial(11)),
            norm["q_integral"] == "39916800/(256*x)^12",
            Fraction(norm["complete_bare_mass"]) == Fraction(1, 256**16),
            payload["radial_atlas"]["strata"]["directed_sum_contains_one"] is True,
            release["complete_exterior_integrand_bound_emitted"] is False,
            release["complete_base_action_column_evaluated"] is False,
        )
    )


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    if not valid(payload):
        raise AssertionError("K294 manifest failed independent replay")
    mutations = [
        ("jacobian", "q^6"),
        ("native_projective_product", "product_i g_i=q^5*product_i p_i"),
        ("density", "q^10"),
        ("simplex", "1/10"),
        ("q_integral", "3628800/(256*x)^11"),
        ("mass", "1/256"),
        ("sum", False),
        ("exterior", True),
    ]
    rejected = 0
    for name, value in mutations:
        candidate = json.loads(json.dumps(payload))
        if name in {"jacobian", "native_projective_product"}:
            candidate["global_chart"][name] = value
        elif name == "density":
            candidate["global_chart"]["transformed_native_density"] = value
        elif name == "simplex":
            candidate["normalization_replay"]["simplex_integral"] = value
        elif name == "q_integral":
            candidate["normalization_replay"]["q_integral"] = value
        elif name == "mass":
            candidate["normalization_replay"]["complete_bare_mass"] = value
        elif name == "sum":
            candidate["radial_atlas"]["strata"]["directed_sum_contains_one"] = value
        else:
            candidate["release_test"]["complete_exterior_integrand_bound_emitted"] = value
        if not valid(candidate):
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError("hostile mutation escaped K294 probe")
    print(f"K294 independent replay: 9/9 checks passed; hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
