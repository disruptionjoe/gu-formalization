#!/usr/bin/env python3
"""K260: integrate complete pair-box intervals before subset composition.

K259 required a bundle upper to be negative on every matched active cell.
Here every constituent box remains sign-separated and is integrated first with
the exact product-cosh cell measure.  Only the resulting rigorous box-integral
intervals are composed.  Unequal rational functions are never netted through a
common interval image.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from math import factorial

from flint import arb, ctx, fmpq

from k259_order_six_maximal_pair_box_certificate import (
    ACTIVE_Q_HI,
    ACTIVE_Q_LO,
    ALL_PAIRS,
    GRID_SIDE,
    INACTIVE_Q_HI,
    INACTIVE_Q_LO,
    K185,
    K218,
    K230,
    K247,
    K257,
    K258,
    OUT as K259,
    ROOT,
    as_arb,
    cell_measure,
    cell_q_bounds,
    core_interval,
    cosh_log,
    group_digest,
    interval,
    pair_text,
    rational_row,
    reduced_groups,
    sinh_log,
    terms,
)


OUT = ROOT / "lab/process/k260-order-six-integrated-pair-box-certificate.json"
MIN_SEARCH_SIZE = 10
NEGATIVE_MASS_LOWER = Q(67, 10**22)  # 6.7e-21
PI_UPPER = Q(22, 7)
PRECISION = 192


def normalized_interval(raw_lower: arb, raw_upper: arb, normalization: fmpq) -> tuple[arb, arb]:
    factor = arb(normalization)
    return factor * raw_lower, factor * raw_upper


def subset_upper(boxes: dict[tuple[int, int], dict], subset) -> arb:
    return sum((boxes[pair]["normalized_upper"] for pair in subset), arb(0))


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    assert len(items) == 1864 and len(ALL_PAIRS) == 15

    configs = {
        pair: reduced_groups(items, (1,) + pair)
        for pair in ALL_PAIRS
    }
    inactive_c = interval(cosh_log(INACTIVE_Q_LO), cosh_log(INACTIVE_Q_HI))
    inactive_measure = (
        sinh_log(INACTIVE_Q_HI) - sinh_log(INACTIVE_Q_LO)
    ) ** 5
    q_cells = [cell_q_bounds(index) for index in range(GRID_SIDE)]
    c_cells = [interval(cosh_log(lo), cosh_log(hi)) for lo, hi in q_cells]
    measures = [cell_measure(lo, hi) for lo, hi in q_cells]

    boxes = {
        pair: {
            "raw_lower": arb(0),
            "raw_upper": arb(0),
            "strictly_negative_cells": 0,
            "strictly_positive_cells": 0,
        }
        for pair in ALL_PAIRS
    }
    for i in range(GRID_SIDE):
        for j in range(GRID_SIDE):
            for k in range(GRID_SIDE):
                active_boxes = (c_cells[i], c_cells[j], c_cells[k])
                measure = measures[i] * measures[j] * measures[k] * inactive_measure
                measure_arb = as_arb(measure)
                for pair in ALL_PAIRS:
                    value = core_interval(configs[pair], active_boxes, inactive_c)
                    lower, upper = value.lower(), value.upper()
                    row = boxes[pair]
                    row["raw_lower"] += lower * measure_arb
                    row["raw_upper"] += upper * measure_arb
                    row["strictly_negative_cells"] += int(upper < 0)
                    row["strictly_positive_cells"] += int(lower > 0)

    normalization = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    for pair in ALL_PAIRS:
        lower, upper = normalized_interval(
            boxes[pair]["raw_lower"], boxes[pair]["raw_upper"], normalization
        )
        boxes[pair]["normalized_lower"] = lower
        boxes[pair]["normalized_upper"] = upper

    passing = []
    failing_rows = []
    passing_by_size = {}
    failing_by_size = {}
    minimum_failure_by_size = {}
    checked = 0
    for size in range(MIN_SEARCH_SIZE, len(ALL_PAIRS) + 1):
        size_pass = []
        size_fail = []
        for subset in combinations(ALL_PAIRS, size):
            checked += 1
            upper = subset_upper(boxes, subset)
            if upper < 0:
                size_pass.append((subset, upper))
            else:
                size_fail.append((subset, upper))
                failing_rows.append(f"{size}:{pair_text(subset)}")
        passing_by_size[str(size)] = len(size_pass)
        failing_by_size[str(size)] = len(size_fail)
        if size_fail:
            minimum_failure_by_size[str(size)] = str(min(upper for _, upper in size_fail))
        passing.extend((size, subset, upper) for subset, upper in size_pass)

    maximum_size = max(size for size, _, _ in passing)
    maximal = [(subset, upper) for size, subset, upper in passing if size == maximum_size]
    assert maximum_size == 10
    assert all(count == 0 for size, count in passing_by_size.items() if int(size) > 10)
    selected_pairs, selected_upper = min(maximal, key=lambda row: row[1])
    selected_lower = sum(
        (boxes[pair]["normalized_lower"] for pair in selected_pairs), arb(0)
    )
    computed_negative_mass = -selected_upper
    assert computed_negative_mass > as_arb(NEGATIVE_MASS_LOWER)

    k247 = json.loads(K247.read_text())
    prefix = k247["certificate"]["complete_upper"]
    prefix_upper = Q(prefix["numerator"], prefix["denominator"])
    cancellation_margin = NEGATIVE_MASS_LOWER - prefix_upper
    assert cancellation_margin > 0

    component_rows = []
    for pair in ALL_PAIRS:
        row = boxes[pair]
        component_rows.append({
            "exceptional_pair": list(pair),
            "sign_separated_bound_classes": len(configs[pair]),
            "group_sha256": group_digest(configs[pair]),
            "strictly_negative_cells": row["strictly_negative_cells"],
            "strictly_positive_cells": row["strictly_positive_cells"],
            "normalized_integral_lower": str(row["normalized_lower"]),
            "normalized_integral_upper": str(row["normalized_upper"]),
        })

    maximal_rows = [
        {
            "exceptional_pairs": [list(pair) for pair in subset],
            "normalized_integral_upper": str(upper),
            "selected_for_mass": subset == selected_pairs,
        }
        for subset, upper in sorted(maximal, key=lambda row: pair_text(row[0]))
    ]
    all_pair_lower = sum(
        (boxes[pair]["normalized_lower"] for pair in ALL_PAIRS), arb(0)
    )
    all_pair_upper = sum(
        (boxes[pair]["normalized_upper"] for pair in ALL_PAIRS), arb(0)
    )
    failure_digest = hashlib.sha256(
        ("\n".join(sorted(failing_rows)) + "\n").encode()
    ).hexdigest()

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K257, K258, K259)
        },
        "object": (
            "The fifteen disjoint K259 exceptional-pair boxes of the exact K218 signed "
            "integrand, with every complete sign-separated box interval integrated before composition"
        ),
        "enclosure": {
            "common_active_axis": 1,
            "all_exceptional_pairs": [list(pair) for pair in ALL_PAIRS],
            "active_q_interval": [str(ACTIVE_Q_LO), str(ACTIVE_Q_HI)],
            "inactive_q_interval": [str(INACTIVE_Q_LO), str(INACTIVE_Q_HI)],
            "matched_grid_shape": [GRID_SIDE] * 3,
            "component_boxes": component_rows,
            "composition_rule": (
                "Each complete valid constituent interval is integrated with exact product-cosh "
                "cell measure before subset addition; unequal rational functions are never netted."
            ),
        },
        "integrated_subset_certificate": {
            "minimum_subset_size_checked": MIN_SEARCH_SIZE,
            "subsets_checked": checked,
            "maximum_certifiable_cardinality": maximum_size,
            "maximal_subset_count": len(maximal),
            "maximal_subsets": maximal_rows,
            "passing_subsets_by_size": passing_by_size,
            "failing_subsets_by_size": failing_by_size,
            "minimum_nonnegative_upper_by_size": minimum_failure_by_size,
            "failure_subset_sha256": failure_digest,
            "all_fifteen_normalized_interval": {
                "lower": str(all_pair_lower),
                "upper": str(all_pair_upper),
            },
            "interpretation": (
                "Ten boxes are certifiable after legal per-box integration, but every eleven- "
                "through fifteen-box subset has nonnegative rigorous upper under this coarse enclosure. "
                "Failure is a certificate limit, not a positive-integral theorem."
            ),
        },
        "selected_ten_box_bundle": {
            "selection_rule": "Choose the size-ten subset with the most negative rigorous integrated upper.",
            "exceptional_pairs": [list(pair) for pair in selected_pairs],
            "normalized_integral_lower": str(selected_lower),
            "normalized_integral_upper": str(selected_upper),
            "computed_strict_negative_mass_lower": str(computed_negative_mass),
            "declared_strict_negative_mass_lower": rational_row(NEGATIVE_MASS_LOWER),
        },
        "composition": {
            "k247_complete_positive_prefix_upper": rational_row(prefix_upper),
            "strict_negative_excess_over_k247_upper": rational_row(cancellation_margin),
        },
        "method_comparison": {
            "exact_s6_projection_coarse_enclosure": (
                "Still inconclusive when exact denominator identities are cancelled first and the "
                "remaining unequal functions are sign-separated."
            ),
            "rejected_shortcut": (
                "Netting functions merely because they share an inactive-count interval image is invalid; "
                "equal enclosures do not identify unequal rational functions."
            ),
        },
        "controls": (
            "An independent reverse-order 256-bit raw-allocation replay reconstructs all box integrals, "
            "the complete subset census and failure digest, plus exact center, absolute-weight, "
            "disjointness and K247 composition controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "Integrating valid constituent enclosures before composition raises the certified pair-box "
            "ceiling from nine to ten. Further complement requires a sharper correlated integral, "
            "effective inactive subdivision, or a consuming far-shape derivative atlas."
        ),
        "claim_ceiling": (
            "Exact maximality only for the declared integrated coarse enclosure and an exact negative "
            "integral on the selected ten-box union. No failed-subset sign, remaining-complement, "
            "full-integral, complete-order-six-error, K215, source, ledger, canon, paper, public-posture "
            "or physical-positivity conclusion."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    cert = result["integrated_subset_certificate"]
    print("[PASS] K260 integrated maximum", cert["maximum_certifiable_cardinality"])
    print("[PASS] K260 maximal subset count", cert["maximal_subset_count"])
    print("[PASS] K260 mass lower", result["selected_ten_box_bundle"]["declared_strict_negative_mass_lower"]["decimal"])
