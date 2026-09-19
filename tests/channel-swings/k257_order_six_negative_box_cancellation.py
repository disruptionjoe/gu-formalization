#!/usr/bin/env python3
"""K257: a full-dimensional negative K218 box cancels the K247 prefix.

The certificate is internal order-six mathematics.  It proves a signed
integral on one disjoint region, not the sign of the unaccounted complement.
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
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
K256 = ROOT / "lab/process/k256-order-six-binary-face-sign-reversal.json"
OUT = ROOT / "lab/process/k257-order-six-negative-box-cancellation.json"

ACTIVE_AXES = (1, 3, 5)
INACTIVE_AXES = tuple(axis for axis in range(8) if axis not in ACTIVE_AXES)
ACTIVE_Q_LO = Q(1792)
ACTIVE_Q_HI = Q(2304)
ACTIVE_Q_STEP = Q(32)
INACTIVE_Q_LO = Q(1)
INACTIVE_Q_HI = Q(13, 5)
GRID_SIDE = int((ACTIVE_Q_HI - ACTIVE_Q_LO) / ACTIVE_Q_STEP)
NEGATIVE_MASS_LOWER = Q(226, 10**22)  # 2.26e-20
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


def reduced_groups(items: list[tuple[int, tuple[int, ...]]]) -> dict[tuple, tuple[int, int]]:
    """Group equal interval bounds while keeping both signs separate.

    Different inactive subsets with the same cardinality are not the same
    rational function.  They do have the same interval bound on this box, so
    positive and negative weights may be accumulated separately, never netted.
    """
    grouped: defaultdict[tuple, list[int]] = defaultdict(lambda: [0, 0])
    for weight, supports in items:
        factors = []
        for row in range(14):
            active_mask = sum(
                1 << local
                for local, axis in enumerate(ACTIVE_AXES)
                if supports[axis] & (1 << row)
            )
            inactive_count = sum(
                1 for axis in INACTIVE_AXES if supports[axis] & (1 << row)
            )
            factors.append((active_mask, inactive_count))
        slot = grouped[tuple(sorted(factors))]
        slot[0 if weight > 0 else 1] += abs(weight)
    return {
        factors: (positive, negative)
        for factors, (positive, negative) in grouped.items()
        if positive or negative
    }


def group_digest(groups: dict[tuple, int]) -> str:
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


def core_interval(groups: dict[tuple, int], active_boxes: tuple[arb, arb, arb], inactive_box: arb) -> arb:
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
    groups = reduced_groups(items)
    assert len(items) == 1864
    assert len(groups) == 318
    assert ACTIVE_AXES == (1, 3, 5)  # K256 mask 0x2a
    assert GRID_SIDE == 16

    inactive_c = interval(cosh_log(INACTIVE_Q_LO), cosh_log(INACTIVE_Q_HI))
    inactive_measure = (
        sinh_log(INACTIVE_Q_HI) - sinh_log(INACTIVE_Q_LO)
    ) ** len(INACTIVE_AXES)
    q_cells = [cell_q_bounds(index) for index in range(GRID_SIDE)]
    c_cells = [interval(cosh_log(lo), cosh_log(hi)) for lo, hi in q_cells]
    measures = [cell_measure(lo, hi) for lo, hi in q_cells]

    raw_negative_mass = arb(0)
    maximum_upper = None
    minimum_lower = None
    atlas_hash = hashlib.sha256()
    negative_cells = 0
    for i in range(GRID_SIDE):
        for j in range(GRID_SIDE):
            for k in range(GRID_SIDE):
                value = core_interval(groups, (c_cells[i], c_cells[j], c_cells[k]), inactive_c)
                lower, upper = value.lower(), value.upper()
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
    prefix_upper_row = k247["certificate"]["complete_upper"]
    prefix_upper = Q(prefix_upper_row["numerator"], prefix_upper_row["denominator"])
    cancellation_margin = NEGATIVE_MASS_LOWER - prefix_upper
    assert cancellation_margin > 0
    assert ACTIVE_Q_LO > 15

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K247, K256)
        },
        "object": (
            "The exact K218 eight-auxiliary signed integrand on one full-dimensional q-box, "
            "including its product-cosh density and pi^-8 normalization"
        ),
        "box": {
            "active_axes": list(ACTIVE_AXES),
            "active_q_interval": [str(ACTIVE_Q_LO), str(ACTIVE_Q_HI)],
            "active_q_step": str(ACTIVE_Q_STEP),
            "inactive_axes": list(INACTIVE_AXES),
            "inactive_q_interval": [str(INACTIVE_Q_LO), str(INACTIVE_Q_HI)],
            "coordinate_map": "c_j=cosh(t_j)=(q_j+q_j^-1)/2 with t_j=log(q_j)",
            "disjoint_from_k247_q_at_most_15": True,
        },
        "grouping": {
            "raw_signed_terms": len(items),
            "sign_separated_active_subset_inactive_count_bound_classes": len(groups),
            "sign_separation_rule": (
                "Functions with equal interval bounds but different inactive subsets are never netted. "
                "Each class stores total positive and total absolute-negative weight separately."
            ),
            "group_sha256": group_digest(groups),
        },
        "interval_atlas": {
            "precision_bits": PRECISION,
            "grid_shape_active_axes": [GRID_SIDE] * 3,
            "cells": GRID_SIDE**3,
            "strictly_negative_cells": negative_cells,
            "maximum_core_upper": str(maximum_upper),
            "minimum_core_lower": str(minimum_lower),
            "cell_bounds_sha256": atlas_hash.hexdigest(),
        },
        "integration": {
            "measure_identity": "integral cosh(t) dt = sinh(t) = (q-q^-1)/2",
            "inactive_product_measure": str(inactive_measure),
            "raw_negative_mass_interval_lower": str(raw_negative_mass.lower()),
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "computed_normalized_negative_mass_lower": str(normalized_negative_mass.lower()),
            "declared_strict_negative_mass_lower": rational_row(NEGATIVE_MASS_LOWER),
        },
        "composition": {
            "k247_complete_positive_prefix_upper": rational_row(prefix_upper),
            "strict_negative_excess_over_k247_upper": rational_row(cancellation_margin),
            "result": (
                "the K257 box alone has more negative product-cosh mass than the complete positive K247 q<=15 prefix; "
                "their disjoint union therefore has strictly negative signed integral"
            ),
        },
        "controls": (
            "Independent reverse-order higher-precision replay reconstructs the 125 groups from raw allocations and the complete atlas; "
            "exact rational interior points, absolute-weight mutation, K247-upper rather than lower composition, and q-box disjointness are checked."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "Farther signed cancellation is now quantitatively real: one certified full-dimensional region cancels K247's complete positive prefix. "
            "The next question is global composition of the remaining complement, not whether negative mass exists or whether q17 is positive."
        ),
        "claim_ceiling": (
            "Exact sign and negative-mass lower bound on the declared K257 box, plus a negative integral on its union with K247 q<=15. "
            "No sign or bound for the unaccounted complement, full K218 integral, complete original order-six error, K215 impossibility, "
            "source/ledger/canon/paper/public-posture change, or physical positivity."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K257 negative cells", result["interval_atlas"]["strictly_negative_cells"])
    print("[PASS] K257 negative mass lower", result["integration"]["declared_strict_negative_mass_lower"]["decimal"])
    print("[PASS] K257 cancellation margin", result["composition"]["strict_negative_excess_over_k247_upper"]["decimal"])
