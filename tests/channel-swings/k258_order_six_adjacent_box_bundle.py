#!/usr/bin/env python3
"""K258: a signed adjacent-box bundle that consumes positive K218 lobes.

Each constituent box is enclosed independently.  Only the resulting valid
intervals are added, so unequal rational functions are never netted merely
because they share an interval bound.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from math import factorial

from flint import arb, ctx, fmpq

from k225_order_six_diagonal_cancellation import K185, ROOT, terms


K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
K257 = ROOT / "lab/process/k257-order-six-negative-box-cancellation.json"
OUT = ROOT / "lab/process/k258-order-six-adjacent-box-bundle.json"

SELECTED_PAIRS = ((2, 5), (3, 5), (4, 5), (5, 6), (5, 7), (2, 4), (2, 6), (2, 7))
ACTIVE_Q_LO = Q(1792)
ACTIVE_Q_HI = Q(2304)
ACTIVE_Q_STEP = Q(32)
INACTIVE_Q_LO = Q(1)
INACTIVE_Q_HI = Q(13, 5)
GRID_SIDE = int((ACTIVE_Q_HI - ACTIVE_Q_LO) / ACTIVE_Q_STEP)
NEGATIVE_MASS_LOWER = Q(151, 10**22)  # 1.51e-20
PI_UPPER = Q(22, 7)
PRECISION = 192


def rational_row(value: Q) -> dict:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": f"{float(value):.12e}",
    }


def as_arb(value: Q) -> arb:
    return arb(value.numerator) / value.denominator


def cosh_log(q: Q) -> Q:
    return (q + 1 / q) / 2


def sinh_log(q: Q) -> Q:
    return (q - 1 / q) / 2


def interval(lo: Q, hi: Q) -> arb:
    alo, ahi = as_arb(lo), as_arb(hi)
    return (alo + ahi) / 2 + arb(0, (ahi - alo) / 2)


def reduced_groups(items, active_axes: tuple[int, int, int]):
    inactive_axes = tuple(axis for axis in range(8) if axis not in active_axes)
    grouped = defaultdict(lambda: [0, 0])
    for weight, supports in items:
        factors = []
        for row in range(14):
            active_mask = sum(
                1 << local
                for local, axis in enumerate(active_axes)
                if supports[axis] & (1 << row)
            )
            inactive_count = sum(
                1 for axis in inactive_axes if supports[axis] & (1 << row)
            )
            factors.append((active_mask, inactive_count))
        slot = grouped[tuple(sorted(factors))]
        slot[0 if weight > 0 else 1] += abs(weight)
    return {
        factors: (positive, negative)
        for factors, (positive, negative) in grouped.items()
        if positive or negative
    }


def group_digest(groups) -> str:
    payload = [
        {
            "factors": [list(pair) for pair in factors],
            "positive_weight": weights[0],
            "negative_weight": weights[1],
        }
        for factors, weights in sorted(groups.items())
    ]
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def core_interval(groups, active_boxes, inactive_box):
    total = arb(0)
    for factors, (positive_weight, negative_weight) in groups.items():
        product = arb(1)
        for active_mask, inactive_count in factors:
            denominator = arb(256) + inactive_count * inactive_box
            for local in range(3):
                if active_mask & (1 << local):
                    denominator += active_boxes[local]
            product *= denominator
        reciprocal = 1 / product
        total += positive_weight * reciprocal - negative_weight * reciprocal
    return total


def cell_q_bounds(index: int) -> tuple[Q, Q]:
    lo = ACTIVE_Q_LO + index * ACTIVE_Q_STEP
    return lo, lo + ACTIVE_Q_STEP


def cell_measure(lo: Q, hi: Q) -> Q:
    return sinh_log(hi) - sinh_log(lo)


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    assert len(items) == 1864
    assert len(SELECTED_PAIRS) == len(set(SELECTED_PAIRS)) == 8
    assert (3, 5) in SELECTED_PAIRS  # K257's original pair
    assert all(2 <= left < right <= 7 for left, right in SELECTED_PAIRS)
    assert GRID_SIDE == 16 and ACTIVE_Q_LO > INACTIVE_Q_HI

    configs = []
    for pair in SELECTED_PAIRS:
        active_axes = (1,) + pair
        groups = reduced_groups(items, active_axes)
        configs.append((pair, active_axes, groups))

    inactive_c = interval(cosh_log(INACTIVE_Q_LO), cosh_log(INACTIVE_Q_HI))
    inactive_measure = (
        sinh_log(INACTIVE_Q_HI) - sinh_log(INACTIVE_Q_LO)
    ) ** 5
    q_cells = [cell_q_bounds(index) for index in range(GRID_SIDE)]
    c_cells = [interval(cosh_log(lo), cosh_log(hi)) for lo, hi in q_cells]
    measures = [cell_measure(lo, hi) for lo, hi in q_cells]

    component = {
        pair: {
            "strictly_negative_cells": 0,
            "strictly_positive_cells": 0,
            "maximum_core_upper": None,
            "minimum_core_lower": None,
        }
        for pair in SELECTED_PAIRS
    }
    raw_negative_mass = arb(0)
    maximum_upper = None
    minimum_lower = None
    atlas_hash = hashlib.sha256()
    negative_cells = 0
    for i in range(GRID_SIDE):
        for j in range(GRID_SIDE):
            for k in range(GRID_SIDE):
                bundle = arb(0)
                bounds = (c_cells[i], c_cells[j], c_cells[k])
                for pair, _, groups in configs:
                    value = core_interval(groups, bounds, inactive_c)
                    lower, upper = value.lower(), value.upper()
                    row = component[pair]
                    row["strictly_negative_cells"] += int(upper < 0)
                    row["strictly_positive_cells"] += int(lower > 0)
                    if row["maximum_core_upper"] is None or upper > row["maximum_core_upper"]:
                        row["maximum_core_upper"] = upper
                    if row["minimum_core_lower"] is None or lower < row["minimum_core_lower"]:
                        row["minimum_core_lower"] = lower
                    bundle += value
                lower, upper = bundle.lower(), bundle.upper()
                assert upper < 0
                negative_cells += 1
                maximum_upper = upper if maximum_upper is None or upper > maximum_upper else maximum_upper
                minimum_lower = lower if minimum_lower is None or lower < minimum_lower else minimum_lower
                measure = measures[i] * measures[j] * measures[k] * inactive_measure
                raw_negative_mass += (-arb(upper)) * as_arb(measure)
                atlas_hash.update(f"{i},{j},{k}:{lower}:{upper}\n".encode())

    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalized_negative_mass = arb(normalization_lower) * arb(raw_negative_mass.lower())
    assert normalized_negative_mass > as_arb(NEGATIVE_MASS_LOWER)

    k247 = json.loads(K247.read_text())
    prefix_row = k247["certificate"]["complete_upper"]
    prefix_upper = Q(prefix_row["numerator"], prefix_row["denominator"])
    cancellation_margin = NEGATIVE_MASS_LOWER - prefix_upper
    assert cancellation_margin > 0

    component_rows = []
    for pair, active_axes, groups in configs:
        row = component[pair]
        component_rows.append({
            "exceptional_pair": list(pair),
            "active_axes": list(active_axes),
            "sign_separated_bound_classes": len(groups),
            "group_sha256": group_digest(groups),
            "strictly_negative_cells": row["strictly_negative_cells"],
            "strictly_positive_cells": row["strictly_positive_cells"],
            "maximum_core_upper": str(row["maximum_core_upper"]),
            "minimum_core_lower": str(row["minimum_core_lower"]),
        })
    assert any(row["strictly_positive_cells"] == GRID_SIDE**3 for row in component_rows)
    assert any(row["strictly_negative_cells"] == GRID_SIDE**3 for row in component_rows)

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K257)
        },
        "object": (
            "The exact K218 eight-auxiliary signed integrand on a connected union of eight "
            "full-dimensional adjacent pair boxes, including product-cosh density and pi^-8 normalization"
        ),
        "bundle": {
            "selected_exceptional_pairs": [list(pair) for pair in SELECTED_PAIRS],
            "common_active_axis": 1,
            "active_q_interval": [str(ACTIVE_Q_LO), str(ACTIVE_Q_HI)],
            "active_q_step": str(ACTIVE_Q_STEP),
            "inactive_q_interval": [str(INACTIVE_Q_LO), str(INACTIVE_Q_HI)],
            "constituent_boxes": len(SELECTED_PAIRS),
            "pairwise_disjoint_interiors": True,
            "disjointness_reason": (
                "Distinct exceptional pairs disagree on at least one axis assigned to disjoint q-ranges "
                "[1792,2304] and [1,13/5]; overlaps are empty, not merely measure zero."
            ),
            "includes_k257_pair": [3, 5],
            "component_boxes": component_rows,
        },
        "interval_atlas": {
            "precision_bits": PRECISION,
            "matched_grid_shape": [GRID_SIDE] * 3,
            "matched_cells": GRID_SIDE**3,
            "strictly_negative_bundle_cells": negative_cells,
            "maximum_bundle_upper": str(maximum_upper),
            "minimum_bundle_lower": str(minimum_lower),
            "cell_bounds_sha256": atlas_hash.hexdigest(),
            "composition_rule": (
                "Each constituent box is enclosed independently with sign-separated weights. "
                "The eight resulting valid intervals are added only on matched cells of equal measure."
            ),
        },
        "integration": {
            "measure_identity": "integral cosh(t) dt = sinh(t) = (q-q^-1)/2",
            "per_box_inactive_product_measure": str(inactive_measure),
            "raw_bundle_negative_mass_interval_lower": str(raw_negative_mass.lower()),
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "computed_normalized_bundle_negative_mass_lower": str(normalized_negative_mass.lower()),
            "declared_strict_bundle_negative_mass_lower": rational_row(NEGATIVE_MASS_LOWER),
        },
        "composition": {
            "k247_complete_positive_prefix_upper": rational_row(prefix_upper),
            "strict_negative_excess_over_k247_upper": rational_row(cancellation_margin),
            "result": (
                "The eight-box bundle contains positive constituent lobes but has strictly negative "
                "matched-cell sum and enough negative mass to cancel K247's complete positive prefix."
            ),
        },
        "controls": (
            "An independent reverse-order 256-bit replay reconstructs every selected pair from raw allocations, "
            "replays all matched cells, checks exact center signs and pairwise disjointness, and verifies that "
            "adding the omitted pair {4,7} defeats this selected interval certificate rather than being silently absorbed."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "K257's cancellation survives a connected adjacent-region composition that explicitly consumes "
            "positive pair-box lobes. The remaining seven pair boxes and the rest of the complement stay open."
        ),
        "claim_ceiling": (
            "Exact negative integral and mass lower bound on the declared eight-box union, plus a negative union "
            "with K247 q<=15. No sign or bound for the remaining pair boxes or other complement, full K218 integral, "
            "complete original order-six error, K215 impossibility, source/ledger/canon/paper/public change, or physical positivity."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K258 negative bundle cells", result["interval_atlas"]["strictly_negative_bundle_cells"])
    print("[PASS] K258 bundle mass lower", result["integration"]["declared_strict_bundle_negative_mass_lower"]["decimal"])
    print("[PASS] K258 cancellation margin", result["composition"]["strict_negative_excess_over_k247_upper"]["decimal"])
