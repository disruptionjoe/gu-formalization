#!/usr/bin/env python3
"""Classify endpoint-corner integrability after exact K296 face zeros."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K296 = ROOT / "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json"
OUTPUT = ROOT / "lab/process/k297-order-seven-endpoint-corner-integrability.json"

CORNER = {
    2: {"scaled_gap_count": 3, "cauchy_valuation": 6, "companion_valuation": 3, "variables": 4},
    4: {"scaled_gap_count": 2, "cauchy_valuation": 3, "companion_valuation": 1, "variables": 3},
    6: {"scaled_gap_count": 1, "cauchy_valuation": 1, "companion_valuation": 0, "variables": 2},
}


def corner_rows() -> list[dict[str, Any]]:
    rows = []
    for old_position, data in CORNER.items():
        derivatives = []
        for order in range(5):
            degree = data["scaled_gap_count"] + data["cauchy_valuation"] + data["companion_valuation"] - order
            margin = degree + data["variables"]
            derivatives.append(
                {
                    "derivative_order": order,
                    "homogeneous_degree": degree,
                    "radial_integrability_margin": margin,
                    "absolutely_integrable": margin > 0,
                    "divergence": "none" if margin > 0 else "logarithmic" if margin == 0 else "power",
                }
            )
        rows.append({"old_position": old_position, **data, "derivative_orders": derivatives})
    return rows


def build() -> dict[str, Any]:
    k296 = json.loads(K296.read_text())
    occurrences = k296["occurrence_census"]
    rows = corner_rows()
    left = Counter(int(row["left_old_position"]) for row in occurrences)
    right = Counter(int(row["right_old_position"]) for row in occurrences)
    fourth = {row["old_position"]: row["derivative_orders"][4] for row in rows}
    return {
        "schema_version": "1.0",
        "result_id": "K297-ORDER-SEVEN-ENDPOINT-CORNER-INTEGRABILITY",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k296-order-seven-coalescent-face-valuation-atlas.json",
            "occurrences": len(occurrences),
            "old_positions": [2, 4, 6],
            "maximum_derivative_order": 4,
            "left_old_position_histogram": {str(k): v for k, v in sorted(left.items())},
            "right_old_position_histogram": {str(k): v for k, v in sorted(right.items())},
        },
        "corner_model": {
            "left_coordinates": "old position 2 scales (r0,r1,r2,y), position 4 scales (r1,r2,y), position 6 scales (r2,y)",
            "right_coordinates": "replace (r,y) by (c,w) with w=1-y",
            "endpoint_paired_kernel": "y*2*K1(x*(y+a*g)) or w*2*K1(x*(w+a*g)), with a in (0,1] on an interior split subbox",
            "leading_rational_model": "g^2*y/(y+a*g)=y*g/a-y^2/a^2+y^3/(a^2*(y+a*g))",
            "fourth_derivative": "d_g^4[g^2*y/(y+a*g)]=24*a^2*y^3/(y+a*g)^5",
            "homogeneity_rule": "the endpoint-paired kernel contributes degree -m; add native scaled gaps, common Cauchy Vandermonde order and companion Vandermonde order",
            "integrability_rule": "a homogeneous degree beta function in n positive corner variables is locally absolutely integrable when beta+n>0; equality is logarithmic",
        },
        "corner_table": rows,
        "decision": {
            "old_positions_two_and_four_integrable_through_order_four": fourth[2]["absolutely_integrable"] and fourth[4]["absolutely_integrable"],
            "old_position_six_fourth_derivative_occurrencewise_integrable": fourth[6]["absolutely_integrable"],
            "old_position_six_fourth_derivative_divergence": fourth[6]["divergence"],
            "occurrencewise_fourth_order_global_extension_legal": False,
            "coherent_group_fourth_derivative_divergence_proved": False,
            "reason": "When the terminal old position is 6, native gap weight times the common Cauchy zero gives g^2 but the companion minor omits position 6 and supplies no (6,8) zero. The exact leading fourth derivative is homogeneous of degree -2 in (g,endpoint), hence logarithmically nonintegrable occurrencewise. The ordered coherent Gram sum may cancel this leading corner and has not yet been restored pointwise.",
            "next_exact_input": "restore the complete ordered 3-by-3 old-position coherent Gram sum before symmetry compression, extract its terminal-corner leading coefficient, and test whether the coefficient cancels in each of the four groups",
        },
        "radial_composition": {
            "k294_low_middle_high_gamma_strata_joined": False,
            "reason": "The angular endpoint corner remains logarithmically nonintegrable for the occurrencewise fourth-order rule at every fixed positive x; the K294 radial gamma weight cannot repair that angular divergence.",
        },
        "release_test": {
            "all_24_occurrences_replayed": len(occurrences) == 24,
            "all_three_old_positions_classified": len(rows) == 3,
            "orders_zero_through_four_classified": all(len(row["derivative_orders"]) == 5 for row in rows),
            "only_terminal_old_position_fails_at_order_four": [position for position, result in fourth.items() if not result["absolutely_integrable"]] == [6],
            "true_complete_integrand_divergence_claimed": False,
            "complete_exterior_integrand_bound_emitted": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k296["ledger_effect"],
        "claim_ceiling": "Exact endpoint-corner homogeneity and absolute-integrability classification for the K288 occurrencewise fourth-derivative route after retaining the native gap weight, common size-four Cauchy zero and companion size-three zero. Positions two and four are integrable through order four; the terminal old-position-six occurrence is logarithmically nonintegrable because its companion omits the needed (6,8) zero. This rejects occurrencewise fourth-order global composition, but proves no divergence of the complete ordered coherent sum or true integrand and supplies no exterior bound, action-column value, residual, native K152 interval, source/ledger move, canon, paper or public claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
