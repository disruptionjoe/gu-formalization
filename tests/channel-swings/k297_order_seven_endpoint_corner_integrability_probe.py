#!/usr/bin/env python3
"""Independent replay and hostile mutations for K297."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k297-order-seven-endpoint-corner-integrability.json"


def valid(payload: dict) -> bool:
    rows = {row["old_position"]: row for row in payload["corner_table"]}
    decision = payload["decision"]
    release = payload["release_test"]
    if sorted(rows) != [2, 4, 6]:
        return False
    return all(
        (
            [rows[p]["companion_valuation"] for p in (2, 4, 6)] == [3, 1, 0],
            [rows[p]["cauchy_valuation"] for p in (2, 4, 6)] == [6, 3, 1],
            all(rows[p]["derivative_orders"][4]["absolutely_integrable"] for p in (2, 4)),
            rows[6]["derivative_orders"][4]["radial_integrability_margin"] == 0,
            rows[6]["derivative_orders"][4]["divergence"] == "logarithmic",
            decision["occurrencewise_fourth_order_global_extension_legal"] is False,
            decision["coherent_group_fourth_derivative_divergence_proved"] is False,
            payload["radial_composition"]["k294_low_middle_high_gamma_strata_joined"] is False,
            release["true_complete_integrand_divergence_claimed"] is False,
        )
    )


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    if not valid(payload):
        raise AssertionError("K297 manifest failed independent replay")
    mutations = [
        ("rows", 2), ("companion", 1), ("cauchy", 2), ("position4", False),
        ("margin", 1), ("divergence", "none"), ("global", True),
        ("coherent", True), ("radial", True), ("true", True),
    ]
    rejected = 0
    for name, value in mutations:
        candidate = json.loads(json.dumps(payload))
        rows = {row["old_position"]: row for row in candidate["corner_table"]}
        if name == "rows": candidate["corner_table"] = candidate["corner_table"][:value]
        elif name == "companion": rows[6]["companion_valuation"] = value
        elif name == "cauchy": rows[6]["cauchy_valuation"] = value
        elif name == "position4": rows[4]["derivative_orders"][4]["absolutely_integrable"] = value
        elif name == "margin": rows[6]["derivative_orders"][4]["radial_integrability_margin"] = value
        elif name == "divergence": rows[6]["derivative_orders"][4]["divergence"] = value
        elif name == "global": candidate["decision"]["occurrencewise_fourth_order_global_extension_legal"] = value
        elif name == "coherent": candidate["decision"]["coherent_group_fourth_derivative_divergence_proved"] = value
        elif name == "radial": candidate["radial_composition"]["k294_low_middle_high_gamma_strata_joined"] = value
        else: candidate["release_test"]["true_complete_integrand_divergence_claimed"] = value
        if not valid(candidate): rejected += 1
    if rejected != len(mutations):
        raise AssertionError("hostile mutation escaped K297 probe")
    print(f"K297 independent replay: 10/10 checks passed; hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
