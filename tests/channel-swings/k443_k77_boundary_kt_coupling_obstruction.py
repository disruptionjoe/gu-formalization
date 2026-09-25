#!/usr/bin/env python3
"""K443 boundary obstruction for degreewise carrier-factor KT couplings."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F


BLOCK_RANKS = [192, 64, 192, 64]


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


def weighted_block_rank(nonzero_rows: list[int]) -> int:
    return sum(BLOCK_RANKS[i] for i in nonzero_rows)


def demo() -> dict:
    pout = [[F(int(i == j and i < 2)) for j in range(4)] for i in range(4)]
    pin = [[F(int(i == j and i >= 2)) for j in range(4)] for i in range(4)]
    compatible = [[F(2), 0, 0, 0], [0, F(3), 0, 0], [0, 0, F(5), 0], [0, 0, 0, F(7)]]
    slow_swap = [[F(0) for _ in range(4)] for _ in range(4)]
    slow_swap[1][3] = F(1)
    slow_swap[3][1] = F(1)
    compatible_defect = sub(matmul(compatible, pout), matmul(pout, compatible))
    swap_defect = sub(matmul(slow_swap, pout), matmul(pout, slow_swap))
    forward_leak = matmul(matmul(pout, slow_swap), pin)
    reverse_leak = matmul(matmul(pin, slow_swap), pout)
    assert rank(compatible_defect) == 0
    assert rank(swap_defect) == 2
    assert rank(forward_leak) == 1
    assert rank(reverse_leak) == 1
    total = 512 * 512
    compatible_dimension = 2 * 256 * 256
    return {
        "schema_version": "1.0",
        "result_id": "K443-K77-BOUNDARY-KT-COUPLING-OBSTRUCTION",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "general_theorem": {
            "coupled_differential": "delta_total=delta_KT tensor I + I_KT tensor Q(t)",
            "boundary_projector": "Pi=I_KT tensor Pi_out(t)",
            "domain_preservation_criterion": "[delta_total,Pi]=0 on boundary traces; after K442 this reduces to [Q,Pi_out]=0",
            "block_form_criterion": "Pi_out Q Pi_in=0 and Pi_in Q Pi_out=0",
            "criterion_necessary_and_sufficient": True,
            "nilpotence_and_properness_separate_obligations": True,
        },
        "actual_rank_count": {
            "corrected_carrier_rank": 512,
            "incoming_rank": 256,
            "outgoing_rank": 256,
            "all_endomorphisms_dimension": total,
            "boundary_compatible_endomorphisms_dimension": compatible_dimension,
            "off_diagonal_obstruction_space_dimension": total - compatible_dimension,
        },
        "exact_controls": {
            "compatible_diagonal_commutator_rank": rank(compatible_defect),
            "slow_swap_representative_commutator_rank": rank(swap_defect),
            "slow_swap_actual_commutator_rank": weighted_block_rank([1, 3]),
            "incoming_to_outgoing_leak_rank": BLOCK_RANKS[1],
            "outgoing_to_incoming_leak_rank": BLOCK_RANKS[3],
            "slow_swap_exchanges_equal_rank_blocks": BLOCK_RANKS[1] == BLOCK_RANKS[3] == 64,
        },
        "decision": {
            "decoupled_k442_product_passes": True,
            "arbitrary_lower_order_coupling_passes": False,
            "slow_sector_exchange_rejected": True,
            "actual_action_coupling_tested": False,
            "full_bv_kt_properness_proved": False,
            "physical_cohomology_constructed": False,
            "next_exact_input": "serialize the actual lower-order K77 field/antifield coupling, verify each degree-changing source/target-projector square and delta_total^2=0 on the closed trace domain, then prove positive-degree acyclicity or identify the exact surviving cohomology",
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
