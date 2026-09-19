#!/usr/bin/env python3
"""K259: exhaustive maximality of the fixed K258 pair-box certificate family."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from math import factorial

from flint import arb, ctx, fmpq

from k258_order_six_adjacent_box_bundle import (
    ACTIVE_Q_HI,
    ACTIVE_Q_LO,
    GRID_SIDE,
    INACTIVE_Q_HI,
    INACTIVE_Q_LO,
    K185,
    K218,
    K230,
    K247,
    K257,
    ROOT,
    as_arb,
    cell_measure,
    cell_q_bounds,
    core_interval,
    cosh_log,
    group_digest,
    interval,
    rational_row,
    reduced_groups,
    sinh_log,
    terms,
)


K258 = ROOT / "lab/process/k258-order-six-adjacent-box-bundle.json"
OUT = ROOT / "lab/process/k259-order-six-maximal-pair-box-certificate.json"
ALL_PAIRS = tuple(combinations(range(2, 8), 2))
K258_PAIRS = frozenset(
    ((2, 5), (3, 5), (4, 5), (5, 6), (5, 7), (2, 4), (2, 6), (2, 7))
)
MIN_SEARCH_SIZE = 9
NEGATIVE_MASS_LOWER = Q(133, 10**22)
PI_UPPER = Q(22, 7)
PRECISION = 192


def pair_text(subset: tuple[tuple[int, int], ...]) -> str:
    return ";".join(f"{left}-{right}" for left, right in subset)


def exact_upper(bounds, subset, cell: int) -> arb:
    return sum((bounds[pair][cell].upper() for pair in subset), arb(0))


def exact_bundle(bounds, subset, cell: int) -> arb:
    return sum((bounds[pair][cell] for pair in subset), arb(0))


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    assert len(items) == 1864
    assert len(ALL_PAIRS) == 15

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

    bounds = {pair: [] for pair in ALL_PAIRS}
    upper_float = {pair: [] for pair in ALL_PAIRS}
    component = {
        pair: {"strictly_negative_cells": 0, "strictly_positive_cells": 0}
        for pair in ALL_PAIRS
    }
    cell_measures = []
    for i in range(GRID_SIDE):
        for j in range(GRID_SIDE):
            for k in range(GRID_SIDE):
                active_boxes = (c_cells[i], c_cells[j], c_cells[k])
                for pair in ALL_PAIRS:
                    value = core_interval(configs[pair], active_boxes, inactive_c)
                    bounds[pair].append(value)
                    upper_float[pair].append(float(value.upper()))
                    component[pair]["strictly_negative_cells"] += int(value.upper() < 0)
                    component[pair]["strictly_positive_cells"] += int(value.lower() > 0)
                cell_measures.append(
                    measures[i] * measures[j] * measures[k] * inactive_measure
                )
    assert len(cell_measures) == GRID_SIDE**3

    maximal = []
    witness_rows = []
    failing_by_size = {}
    checked = 0
    for size in range(MIN_SEARCH_SIZE, len(ALL_PAIRS) + 1):
        failures = 0
        for subset in combinations(ALL_PAIRS, size):
            checked += 1
            float_sums = [
                sum(upper_float[pair][cell] for pair in subset)
                for cell in range(GRID_SIDE**3)
            ]
            witness_cell = max(range(GRID_SIDE**3), key=float_sums.__getitem__)
            witness_upper = exact_upper(bounds, subset, witness_cell)
            if witness_upper < 0:
                exact_uppers = [
                    exact_upper(bounds, subset, cell)
                    for cell in range(GRID_SIDE**3)
                ]
                if all(value < 0 for value in exact_uppers):
                    assert size == MIN_SEARCH_SIZE
                    maximal.append({
                        "subset": subset,
                        "maximum_upper": max(exact_uppers),
                    })
                    continue
                witness_cell = max(
                    range(GRID_SIDE**3), key=lambda cell: exact_uppers[cell]
                )
                witness_upper = exact_uppers[witness_cell]
            assert witness_upper >= 0
            failures += 1
            witness_rows.append(
                f"{size}:{pair_text(subset)}:{witness_cell}"
            )
        failing_by_size[str(size)] = failures

    assert len(maximal) == 4
    assert failing_by_size == {
        "9": 5001,
        "10": 3003,
        "11": 1365,
        "12": 455,
        "13": 105,
        "14": 15,
        "15": 1,
    }
    assert checked == 9949
    selected = min(maximal, key=lambda row: row["maximum_upper"])
    selected_pairs = selected["subset"]
    assert len(selected_pairs) == 9
    assert not K258_PAIRS.issubset(selected_pairs)

    selected_negative = 0
    selected_maximum_upper = None
    selected_minimum_lower = None
    raw_negative_mass = arb(0)
    atlas_hash = hashlib.sha256()
    for cell, measure in enumerate(cell_measures):
        value = exact_bundle(bounds, selected_pairs, cell)
        lower, upper = value.lower(), value.upper()
        assert upper < 0
        selected_negative += 1
        selected_maximum_upper = (
            upper if selected_maximum_upper is None or upper > selected_maximum_upper
            else selected_maximum_upper
        )
        selected_minimum_lower = (
            lower if selected_minimum_lower is None or lower < selected_minimum_lower
            else selected_minimum_lower
        )
        raw_negative_mass += (-upper) * as_arb(measure)
        atlas_hash.update(f"{cell}:{lower}:{upper}\n".encode())

    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalized_negative_mass = arb(normalization_lower) * arb(raw_negative_mass.lower())
    assert normalized_negative_mass > as_arb(NEGATIVE_MASS_LOWER)
    k247 = json.loads(K247.read_text())
    prefix = k247["certificate"]["complete_upper"]
    prefix_upper = Q(prefix["numerator"], prefix["denominator"])
    cancellation_margin = NEGATIVE_MASS_LOWER - prefix_upper
    assert cancellation_margin > 0

    maximal_rows = []
    for row in sorted(maximal, key=lambda entry: pair_text(entry["subset"])):
        maximal_rows.append({
            "exceptional_pairs": [list(pair) for pair in row["subset"]],
            "maximum_matched_cell_upper": str(row["maximum_upper"]),
            "selected_for_mass": row["subset"] == selected_pairs,
        })

    component_rows = []
    for pair in ALL_PAIRS:
        component_rows.append({
            "exceptional_pair": list(pair),
            "sign_separated_bound_classes": len(configs[pair]),
            "group_sha256": group_digest(configs[pair]),
            **component[pair],
        })

    witness_digest = hashlib.sha256(
        ("\n".join(sorted(witness_rows)) + "\n").encode()
    ).hexdigest()
    k258_one_step = []
    for pair in ALL_PAIRS:
        if pair in K258_PAIRS:
            continue
        subset = tuple(sorted((*K258_PAIRS, pair)))
        float_sums = [
            sum(upper_float[item][cell] for item in subset)
            for cell in range(GRID_SIDE**3)
        ]
        cell = max(range(GRID_SIDE**3), key=float_sums.__getitem__)
        upper = exact_upper(bounds, subset, cell)
        assert upper >= 0
        k258_one_step.append({
            "added_pair": list(pair),
            "witness_cell_linear_index": cell,
            "witness_upper": str(upper),
        })

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K257, K258)
        },
        "object": (
            "The fixed K258 sign-separated matched-cell certificate family on all fifteen "
            "full-dimensional exceptional-pair boxes of the exact K218 signed integrand"
        ),
        "family": {
            "common_active_axis": 1,
            "all_exceptional_pairs": [list(pair) for pair in ALL_PAIRS],
            "active_q_interval": [str(ACTIVE_Q_LO), str(ACTIVE_Q_HI)],
            "inactive_q_interval": [str(INACTIVE_Q_LO), str(INACTIVE_Q_HI)],
            "matched_grid_shape": [GRID_SIDE] * 3,
            "component_boxes": component_rows,
            "composition_rule": (
                "Every constituent box is enclosed independently with positive and negative weights "
                "kept separate; a subset adds only those complete valid intervals on matched cells."
            ),
        },
        "exhaustive_subset_certificate": {
            "minimum_subset_size_checked": MIN_SEARCH_SIZE,
            "subsets_checked": checked,
            "maximum_uniformly_negative_cardinality": 9,
            "maximal_subsets": maximal_rows,
            "maximal_subset_count": len(maximal_rows),
            "failing_subsets_by_size": failing_by_size,
            "nonnegative_upper_witness_count": len(witness_rows),
            "nonnegative_upper_witness_sha256": witness_digest,
            "k258_one_pair_extensions": k258_one_step,
            "interpretation": (
                "Every subset of size ten through fifteen, and every nonwinning size-nine subset, "
                "has at least one exact matched-cell upper endpoint greater than or equal to zero. "
                "This is maximality only for the declared finite certificate family."
            ),
        },
        "selected_nine_box_bundle": {
            "selection_rule": (
                "Choose the maximal subset with the most negative maximum matched-cell upper."
            ),
            "exceptional_pairs": [list(pair) for pair in selected_pairs],
            "strictly_negative_cells": selected_negative,
            "maximum_bundle_upper": str(selected_maximum_upper),
            "minimum_bundle_lower": str(selected_minimum_lower),
            "cell_bounds_sha256": atlas_hash.hexdigest(),
            "includes_all_positive_components": [
                list(pair) for pair in selected_pairs
                if component[pair]["strictly_positive_cells"] == GRID_SIDE**3
            ],
            "includes_all_negative_components": [
                list(pair) for pair in selected_pairs
                if component[pair]["strictly_negative_cells"] == GRID_SIDE**3
            ],
        },
        "integration": {
            "measure_identity": "integral cosh(t) dt = sinh(t) = (q-q^-1)/2",
            "raw_bundle_negative_mass_interval_lower": str(raw_negative_mass.lower()),
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "computed_normalized_bundle_negative_mass_lower": str(normalized_negative_mass.lower()),
            "declared_strict_bundle_negative_mass_lower": rational_row(NEGATIVE_MASS_LOWER),
            "k247_complete_positive_prefix_upper": rational_row(prefix_upper),
            "strict_negative_excess_over_k247_upper": rational_row(cancellation_margin),
        },
        "controls": (
            "An independent reverse-order 256-bit raw-allocation replay reconstructs all fifteen "
            "components, exhausts the size-nine-through-fifteen subset family, reproduces the four "
            "maximal bundles and canonical witness digest, and checks exact center, disjointness, "
            "absolute-weight and selected-pair mutation controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "Nine boxes are the exact maximum certified by the fixed K258 matched-cell architecture. "
            "Further complement control requires a sharper inactive-coordinate subdivision, grouped "
            "integral, or other correlation-preserving enclosure rather than another subset choice."
        ),
        "claim_ceiling": (
            "Exact maximality only for the declared finite interval certificate family and an exact "
            "negative integral on the selected nine-box union. A failed subset is not proved positive. "
            "No remaining-complement, full-integral, complete-order-six-error, K215, source, ledger, "
            "canon, paper, public-posture or physical-positivity conclusion."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    cert = result["exhaustive_subset_certificate"]
    print("[PASS] K259 maximum pair-box cardinality", cert["maximum_uniformly_negative_cardinality"])
    print("[PASS] K259 maximal subset count", cert["maximal_subset_count"])
    print("[PASS] K259 mass lower", result["integration"]["declared_strict_bundle_negative_mass_lower"]["decimal"])
