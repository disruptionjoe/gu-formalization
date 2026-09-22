#!/usr/bin/env python3
"""Independent replay and hostile mutations for K298."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k298-order-seven-coherent-terminal-corner-obstruction.json"


def valid(payload: dict) -> bool:
    groups = payload["ordered_coherent_groups"]
    theorem = payload["cofactor_theorem"]
    control = payload["exact_cauchy_control"]
    consequence = payload["integrability_consequence"]
    decision = payload["decision"]
    return all(
        (
            len(groups) == 4,
            all(group["old_position_coefficient_vector"] == [1, -1, 1] for group in groups),
            all(group["ordered_entry_count"] == 9 for group in groups),
            all(group["all_coefficient_products_equal_cofactor_signs"] for group in groups),
            theorem["terminal_leading_coefficient_cancels"] is False,
            Fraction(control["terminal_row_replacement_determinant"]) == Fraction(1, 6237),
            control["identity_holds"] is True and control["strictly_positive"] is True,
            consequence["fourth_derivative_absolute_integrability_margin"] == 0,
            consequence["complete_four_group_fourth_derivative_locally_absolutely_integrable"] is False,
            consequence["integrand_itself_locally_integrable"] is True,
            decision["global_fourth_derivative_jacobi_route_legal"] is False,
            payload["release_test"]["complete_integrand_divergence_claimed"] is False,
        )
    )


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    if not valid(payload):
        raise AssertionError("K298 manifest failed independent replay")
    mutations = [
        ("groups", 3), ("coefficients", [1, 1, 1]), ("entries", 6),
        ("signs", False), ("cancels", True), ("determinant", "0"),
        ("identity", False), ("margin", 1), ("four_group", True),
        ("integrand", False), ("route", True), ("divergence", True),
    ]
    rejected = 0
    for name, value in mutations:
        candidate = json.loads(json.dumps(payload))
        if name == "groups": candidate["ordered_coherent_groups"] = candidate["ordered_coherent_groups"][:value]
        elif name == "coefficients": candidate["ordered_coherent_groups"][0]["old_position_coefficient_vector"] = value
        elif name == "entries": candidate["ordered_coherent_groups"][0]["ordered_entry_count"] = value
        elif name == "signs": candidate["ordered_coherent_groups"][0]["all_coefficient_products_equal_cofactor_signs"] = value
        elif name == "cancels": candidate["cofactor_theorem"]["terminal_leading_coefficient_cancels"] = value
        elif name == "determinant": candidate["exact_cauchy_control"]["terminal_row_replacement_determinant"] = value
        elif name == "identity": candidate["exact_cauchy_control"]["identity_holds"] = value
        elif name == "margin": candidate["integrability_consequence"]["fourth_derivative_absolute_integrability_margin"] = value
        elif name == "four_group": candidate["integrability_consequence"]["complete_four_group_fourth_derivative_locally_absolutely_integrable"] = value
        elif name == "integrand": candidate["integrability_consequence"]["integrand_itself_locally_integrable"] = value
        elif name == "route": candidate["decision"]["global_fourth_derivative_jacobi_route_legal"] = value
        else: candidate["release_test"]["complete_integrand_divergence_claimed"] = value
        if not valid(candidate): rejected += 1
    if rejected != len(mutations):
        raise AssertionError("hostile mutation escaped K298 probe")
    print(f"K298 independent replay: 12/12 checks passed; hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
