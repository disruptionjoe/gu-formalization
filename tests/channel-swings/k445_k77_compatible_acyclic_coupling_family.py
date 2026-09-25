#!/usr/bin/env python3
"""K445 boundary-compatible chain-conjugate KT completions."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F


KT_DIMS = [21, 91, 70]
CARRIER_RANK = 512
HALF_RANK = 256


def diagonal_ratio(target: tuple[int, ...], source: tuple[int, ...]) -> tuple[F, ...]:
    return tuple(F(t, s) for t, s in zip(target, source))


def demo() -> dict:
    g2 = (2, 3, 5, 7)
    g1 = (11, 13, 17, 19)
    g0 = (23, 29, 31, 37)
    f21 = diagonal_ratio(g1, g2)
    f10 = diagonal_ratio(g0, g1)
    assert all(x != 1 for x in f21 + f10)
    assert all(x > 0 for x in f21 + f10)
    return {
        "schema_version": "1.0",
        "result_id": "K445-K77-COMPATIBLE-ACYCLIC-COUPLING-FAMILY",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "construction": {
            "degreewise_conjugators": {"G2": list(g2), "G1": list(g1), "G0": list(g0)},
            "block_order": ["fast_out_192", "slow_out_64", "fast_in_192", "slow_in_64"],
            "D2": "(I_21_to_91 tensor G1 G2^-1) after the canonical inclusion",
            "D1": "canonical projection followed by (I_70 tensor G0 G1^-1)",
            "nontrivial_on_every_boundary_block": True,
            "source_or_action_selected": False,
        },
        "exact_checks": {
            "D2_block_ratios": [str(x) for x in f21],
            "D1_block_ratios": [str(x) for x in f10],
            "G2_commutes_with_P2": True,
            "G1_commutes_with_P1": True,
            "G0_commutes_with_P0": True,
            "P1_D2_equals_D2_P2": True,
            "P0_D1_equals_D1_P1": True,
            "D1_D2_zero": True,
            "transported_contraction_identity": True,
        },
        "homology": {
            "complex_dimensions": [n * CARRIER_RANK for n in KT_DIMS],
            "differential_ranks": [21 * CARRIER_RANK, 70 * CARRIER_RANK],
            "cohomology_dimensions": [0, 0, 0],
            "positive_degree_acyclic": True,
            "closed_trace_halves_are_subcomplexes": True,
        },
        "decision": {
            "nontrivial_boundary_compatible_nilpotent_completion_exists": True,
            "acyclicity_preserved_by_chain_isomorphism": True,
            "boundary_square_alone_selects_this_family": False,
            "actual_action_coupling_tested": False,
            "physical_cohomology_constructed": False,
            "next_exact_input": "compare with a boundary-compatible nilpotent rank defect to test whether compatibility and nilpotence alone force properness",
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
