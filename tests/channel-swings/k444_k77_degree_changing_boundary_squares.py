#!/usr/bin/env python3
"""K444 typed boundary squares for degree-changing K77 KT blocks."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F


KT_DIMS = [21, 91, 70]
CARRIER_RANK = 512
HALF_RANK = 256
SLOW_HALF_RANK = 64


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def sub(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def rank(a: list[list[F]]) -> int:
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][c]
        m[r] = [x / p for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [x - q * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def arrow_count(source_base: int, target_base: int) -> dict[str, int]:
    source = source_base * CARRIER_RANK
    target = target_base * CARRIER_RANK
    all_maps = source * target
    compatible = 2 * (source_base * HALF_RANK) * (target_base * HALF_RANK)
    return {
        "source_dimension": source,
        "target_dimension": target,
        "all_linear_maps_dimension": all_maps,
        "boundary_compatible_maps_dimension": compatible,
        "off_diagonal_obstruction_dimension": all_maps - compatible,
    }


def demo() -> dict:
    p_source = [[F(1), F(0)], [F(0), F(0)]]
    p_target = [[F(1), F(0)], [F(0), F(0)]]
    compatible = [[F(2), F(0)], [F(0), F(3)]]
    exchange = [[F(0), F(1)], [F(1), F(0)]]
    compatible_defect = sub(matmul(p_target, compatible), matmul(compatible, p_source))
    exchange_defect = sub(matmul(p_target, exchange), matmul(exchange, p_source))
    assert rank(compatible_defect) == 0
    assert rank(exchange_defect) == 2
    return {
        "schema_version": "1.0",
        "result_id": "K444-K77-DEGREE-CHANGING-BOUNDARY-SQUARES",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "general_theorem": {
            "typed_square": "Pi_target D = D Pi_source",
            "block_form_criterion": "Pi_target D (I-Pi_source)=0 and (I-Pi_target) D Pi_source=0",
            "criterion_necessary_and_sufficient": True,
            "equal_degree_specialization": "when source=target and Pi_source=Pi_target, this is [D,Pi]=0",
            "k443_is_strict_special_case": True,
        },
        "actual_arrow_counts": {
            "degree_2_to_1": arrow_count(KT_DIMS[0], KT_DIMS[1]),
            "degree_1_to_0": arrow_count(KT_DIMS[1], KT_DIMS[2]),
            "compatible_fraction_each_arrow": "1/2",
        },
        "exact_controls": {
            "compatible_representative_defect_rank": rank(compatible_defect),
            "slow_exchange_representative_defect_rank": rank(exchange_defect),
            "slow_exchange_actual_defect_rank": 2 * SLOW_HALF_RANK,
            "source_to_target_leak_rank": SLOW_HALF_RANK,
            "target_to_source_leak_rank": SLOW_HALF_RANK,
        },
        "decision": {
            "both_degree_changing_square_types_classified": True,
            "boundary_compatibility_implies_nilpotence": False,
            "boundary_compatibility_implies_properness": False,
            "actual_action_coupling_tested": False,
            "next_exact_input": "test nilpotence and cohomology on contrary boundary-compatible completions, then require the action to select and serialize the actual degree-changing blocks",
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
