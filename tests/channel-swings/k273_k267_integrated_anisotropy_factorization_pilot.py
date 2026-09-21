#!/usr/bin/env python3
"""K273: integrate K225's exact anisotropy majorant on a demanding K267 orbit."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
import sys

from flint import arb, ctx

from k225_order_six_diagonal_cancellation import K185, ROOT, mixed_majorant, terms
from k262_order_six_low_through_three_high_multiplicity_integral import (
    as_arb,
    centered_moments,
    cosh_log,
)
from k267_order_nine_exchangeable_axis_middle_collar import BOUNDS, status_specs

sys.set_int_max_str_digits(0)

K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K225 = ROOT / "lab/process/k225-order-six-diagonal-cancellation.json"
K267 = ROOT / "lab/process/k267-order-nine-exchangeable-axis-middle-collar.json"
K272 = ROOT / "lab/process/k272-k267-s6-invariant-moment-compression-pilot.json"
OUT = ROOT / "lab/process/k273-k267-integrated-anisotropy-factorization-pilot.json"

FIXED_STATUS = ("high", "high")
HIGH_MULTIPLICITY = 5
PRECISION = 256


def rational_row(value: Q) -> dict:
    return {"numerator": value.numerator, "denominator": value.denominator}


def selected_layer(record: dict) -> dict:
    block = next(row for row in record["fixed_axis_blocks"]
                 if row["block"] == "fixed_high_high")
    return next(row for row in block["multiplicity_layers"]
                if row["high_exceptional_multiplicity"] == HIGH_MULTIPLICITY)


def integrated_bound(items: list, pair_majorants: dict[tuple[int, int], Q]):
    anchor = cosh_log(BOUNDS["middle"][0])
    moments = {
        name: centered_moments(bounds, anchor, 1)
        for name, bounds in BOUNDS.items()
    }
    fixed_measure = moments["high"][0] ** 2
    boxes = list(status_specs(FIXED_STATUS, HIGH_MULTIPLICITY))
    assert len(boxes) == 6
    total = arb(0)
    products = 0
    for _, _, status in boxes:
        for j in range(2, 8):
            for k in range(j + 1, 8):
                term = as_arb(pair_majorants[(j, k)]) * fixed_measure
                for axis in range(2, 8):
                    term *= moments[status[axis]][1 if axis in (j, k) else 0]
                    products += 1
                total += term
    return total, boxes, products


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    assert len(items) == 1864
    anchor = cosh_log(BOUNDS["middle"][0])
    fixed_lower = cosh_log(BOUNDS["high"][0])
    lower_corner = (fixed_lower, fixed_lower) + (anchor,) * 6
    pair_majorants = {
        (j, k): mixed_majorant(items, lower_corner, j, k)
        for j in range(2, 8) for k in range(j + 1, 8)
    }
    assert len(pair_majorants) == 15 and all(value > 0 for value in pair_majorants.values())
    bound, boxes, moment_products = integrated_bound(items, pair_majorants)

    record = json.loads(K267.read_text())
    layer = selected_layer(record)
    prior_lower = arb(layer["complete_raw_integral_interval"]["lower"])
    prior_upper = arb(layer["complete_raw_integral_interval"]["upper"])
    prior_width = prior_upper - prior_lower
    factor_width = 2 * bound
    width_ratio = factor_width / prior_width
    assert bound > 0 and width_ratio > arb(10**16)

    derivative_term_evaluations = len(items) * len(pair_majorants)
    current_recurrence_updates = 6 * 307 * 14 * 10
    recurrence_reduction = Q(current_recurrence_updates, derivative_term_evaluations)

    exact_checks = 0
    assert len(boxes) == 6; exact_checks += 1
    assert derivative_term_evaluations == 27960; exact_checks += 1
    assert current_recurrence_updates == 257880; exact_checks += 1
    assert recurrence_reduction == Q(2149, 233); exact_checks += 1
    assert width_ratio > arb(10**16); exact_checks += 1
    assert json.loads(K225.read_text())["mixed_derivative_rule"]; exact_checks += 1
    hostile_checks = 0
    assert factor_width > prior_width; hostile_checks += 1
    assert prior_lower > 0 and -bound < 0 < bound; hostile_checks += 1
    assert json.loads(K272.read_text())["cost_conclusion"]["result"] == "reject_as_total_algebraic_speedup"; hostile_checks += 1

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K225, K267, K272)
        },
        "object": "K225 integrated double-anisotropy majorant on K267 fixed-high/high multiplicity-five six-box orbit",
        "selection": {
            "chosen": "k225_exact_anisotropy_factorization",
            "reason": "K225 is an exact identity for the same original K218 core and has a proved monotone mixed-derivative majorant that can be integrated on K267 immediately.",
            "alternative_not_selected": "determinant_divided_differences",
            "alternative_limit": "No determinant/divided-difference representation with a complete K267 product-cosh remainder is serialized; a slice identity would not satisfy R6.",
        },
        "domain": {
            "fixed_axis_status": list(FIXED_STATUS),
            "high_exceptional_multiplicity": HIGH_MULTIPLICITY,
            "boxes": len(boxes),
            "axis_statuses": [list(status) for _, _, status in boxes],
        },
        "uniform_majorant": {
            "exchangeable_anchor_cosh": str(anchor),
            "fixed_axis_lower_cosh": str(fixed_lower),
            "pair_majorants": {f"{j},{k}": rational_row(value)
                               for (j, k), value in pair_majorants.items()},
            "proof_rule": "K225's exact zero on zero/single-exception strata gives a double integral of mixed derivatives. Every positive denominator, logarithmic derivative and shared-load term decreases coordinatewise, so its lower-corner value uniformly bounds the full box. The two anisotropy factors are integrated against the exact product-cosh measure; there is no omitted Taylor degree.",
            "integrated_absolute_upper": str(bound),
            "raw_interval": {"lower": str(-bound), "upper": str(bound)},
        },
        "comparison": {
            "k267_raw_interval": layer["complete_raw_integral_interval"],
            "k267_raw_width": str(prior_width),
            "factorized_raw_width": str(factor_width),
            "factorized_to_k267_width_ratio": str(width_ratio),
            "current_degree_nine_recurrence_updates": current_recurrence_updates,
            "factorized_derivative_term_evaluations": derivative_term_evaluations,
            "recurrence_reduction_factor": str(recurrence_reduction),
            "factorized_moment_products": moment_products,
        },
        "decision": {
            "result": "reject_integrated_anisotropy_majorant_for_this_case",
            "reason": "The factorization is cheaper but its rigorous symmetric interval is more than 10^16 times wider and loses K267's certified positive sign. It does not beat the current expansion on usable enclosure width.",
            "r6_disposition": "concluded_by_evidenced_rejection",
            "non_implication": "This does not rule out a future signed cancellation-preserving derivative representation with a sharper uniform remainder.",
        },
        "selftests": {"exact_passed": exact_checks, "hostile_passed": hostile_checks},
        "claim_ceiling": "A costed exact rejection of the K225 unsigned integrated majorant on one complete K267 six-box orbit; no universal representation lower bound, new K218 region, full integral, source, ledger, canon, paper, public-posture or physical conclusion.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K273 integrated anisotropy factorization pilot", result["decision"]["result"])
