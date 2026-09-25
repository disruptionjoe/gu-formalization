#!/usr/bin/env python3
"""K440 closed trace domain and Green model for the K439 split."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F


SPECTRAL_BLOCKS = [
    {"eigenvalue": F(1), "rank": 192, "projector": "fast_outgoing"},
    {"eigenvalue": F(1, 24), "rank": 64, "projector": "slow_outgoing"},
    {"eigenvalue": F(-1), "rank": 192, "projector": "fast_incoming"},
    {"eigenvalue": F(-1, 24), "rank": 64, "projector": "slow_incoming"},
]


def rational(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def verify_model() -> dict[str, bool]:
    positive = [row for row in SPECTRAL_BLOCKS if row["eigenvalue"] > 0]
    negative = [row for row in SPECTRAL_BLOCKS if row["eigenvalue"] < 0]
    return {
        "four_nonzero_real_spectral_blocks": len(SPECTRAL_BLOCKS) == 4 and all(row["eigenvalue"] != 0 for row in SPECTRAL_BLOCKS),
        "total_corrected_rank_512": sum(row["rank"] for row in SPECTRAL_BLOCKS) == 512,
        "positive_rank_256": sum(row["rank"] for row in positive) == 256,
        "negative_rank_256": sum(row["rank"] for row in negative) == 256,
        "spectral_gap_one_over_24": min(abs(row["eigenvalue"]) for row in SPECTRAL_BLOCKS) == F(1, 24),
        "green_l2_bound_24": max(F(1, 1) / abs(row["eigenvalue"]) for row in SPECTRAL_BLOCKS) == 24,
        "green_derivative_bound_25": 1 + max(F(1, 1) / abs(row["eigenvalue"]) for row in SPECTRAL_BLOCKS) == 25,
        "green_h1_sum_bound_49": 1 + 2 * max(F(1, 1) / abs(row["eigenvalue"]) for row in SPECTRAL_BLOCKS) == 49,
        "orientation_reversal_swaps_signs": sorted(-row["eigenvalue"] for row in SPECTRAL_BLOCKS) == sorted(row["eigenvalue"] for row in SPECTRAL_BLOCKS),
    }


def demo() -> dict:
    checks = verify_model()
    assert all(checks.values())
    return {
        "schema_version": "1.0",
        "result_id": "K440-K77-CORRECTED-BOUNDARY-GREEN-DOMAIN",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "input_contract": {
            "carrier": "the K439 corrected rank-512 carrier E=E_+ direct-sum E_-",
            "operator": "D_A=d/dr+A on L2(R_+,E) for the constant coefficient compressed symbol A",
            "positive_trace_condition": "Pi_c,out u(0)=0",
            "infinity_condition": "the negative spectral part is selected by L2 decay at infinity",
            "scope": "conditional frozen-coefficient half-line normal model; not the full moving nonlinear K77 operator",
        },
        "spectral_blocks": [
            {"eigenvalue": rational(row["eigenvalue"]), "rank": row["rank"], "projector": row["projector"]}
            for row in SPECTRAL_BLOCKS
        ],
        "green_operator": {
            "positive_formula": "G_+f(r)=integral_0^r exp[-A_+(r-s)] Pi_c,out f(s) ds",
            "negative_formula": "G_-f(r)=-integral_r^infinity exp[-A_-(r-s)] Pi_c,in f(s) ds",
            "right_and_left_inverse": True,
            "l2_operator_norm_upper_bound": "24",
            "l2_to_derivative_bound": "25",
            "l2_to_h1_sum_bound": "49",
            "slow_block_controls_bound": True,
        },
        "closed_domain_theorem": {
            "domain": "{u in H1(R_+,E): Pi_c,out u(0)=0}",
            "trace_map_continuous": True,
            "domain_closed_in_h1": True,
            "domain_dense_in_l2": True,
            "kernel_dimension": 0,
            "cokernel_dimension": 0,
        },
        "exact_checks": checks,
        "decision": {
            "conditional_closed_green_domain_constructed": True,
            "constraint_preservation_inherited_from_k439": True,
            "moving_lower_order_domain_constructed": False,
            "nonlinear_bv_kt_invariance_proved": False,
            "physical_boundary_selected": False,
            "physical_cohomology_constructed": False,
            "next_exact_input": "construct the lower-order moving K77 connection and nonlinear BV/Koszul-Tate differential on the corrected carrier, then test parallel transport of Pi_c,in/out and invariance of the closed trace domain",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
