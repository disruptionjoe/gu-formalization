#!/usr/bin/env python3
"""Independent reverse-allocation replay for K273."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
import sys

from flint import arb, ctx

from k262_order_six_low_through_three_high_multiplicity_integral import as_arb, cosh_log
from k262_order_six_low_through_three_high_multiplicity_integral_probe import (
    K185,
    raw_terms,
)
from k265_order_nine_complete_binary_low_high_union_probe import centered_moments_independent
from k267_order_nine_exchangeable_axis_middle_collar import BOUNDS
from k273_k267_integrated_anisotropy_factorization_pilot import ROOT

sys.set_int_max_str_digits(0)

RECORD = ROOT / "lab/process/k273-k267-integrated-anisotropy-factorization-pilot.json"
K267 = ROOT / "lab/process/k267-order-nine-exchangeable-axis-middle-collar.json"


def independent_majorant(items, corner, j, k):
    total = Q()
    for weight, rows in reversed(items):
        loads = [Q(256) + sum((corner[a] for a in reversed(range(8))
                              if row & (1 << a)), Q()) for row in reversed(rows)]
        product = 1
        for load in loads:
            product *= load
        lj = sum((Q(1, loads[i]) for i, row in enumerate(reversed(rows))
                  if row & (1 << j)), Q())
        lk = sum((Q(1, loads[i]) for i, row in enumerate(reversed(rows))
                  if row & (1 << k)), Q())
        shared = sum((Q(1, loads[i] ** 2) for i, row in enumerate(reversed(rows))
                      if row & (1 << j) and row & (1 << k)), Q())
        total += Q(abs(weight), product) * (lj * lk + shared)
    return total


def transpose_support_masks(masks):
    """Convert eight axis masks to fourteen eight-bit denominator rows."""
    return tuple(
        sum(((masks[axis] >> factor) & 1) << axis for axis in range(8))
        for factor in range(14)
    )


def statuses():
    result = []
    for middle in reversed(range(2, 8)):
        row = ["high"] * 8
        row[middle] = "middle"
        result.append(tuple(row))
    return result


def main() -> None:
    ctx.prec = 256
    record = json.loads(RECORD.read_text())
    source = json.loads(K185.read_text())
    items = [(weight, transpose_support_masks(masks))
             for weight, masks in raw_terms(source)]
    assert len(items) == 1864
    anchor = cosh_log(BOUNDS["middle"][0])
    fixed_lower = cosh_log(BOUNDS["high"][0])
    corner = (fixed_lower, fixed_lower) + (anchor,) * 6
    pair_rows = record["uniform_majorant"]["pair_majorants"]
    majorants = {}
    for j in reversed(range(2, 8)):
        for k in reversed(range(j + 1, 8)):
            value = independent_majorant(items, corner, j, k)
            prior = pair_rows[f"{j},{k}"]
            assert value == Q(prior["numerator"], prior["denominator"])
            majorants[(j, k)] = value

    moments = {name: centered_moments_independent(bounds, anchor, 1)
               for name, bounds in BOUNDS.items()}
    total = arb(0)
    fixed_measure = moments["high"][0] ** 2
    for status in statuses():
        for j, k in reversed(list(majorants)):
            term = as_arb(majorants[(j, k)]) * fixed_measure
            for axis in reversed(range(2, 8)):
                term *= moments[status[axis]][1 if axis in (j, k) else 0]
            total += term
    prior_bound = arb(record["uniform_majorant"]["integrated_absolute_upper"])
    assert (total - prior_bound).contains(0)

    comparison = record["comparison"]
    prior_width = arb(comparison["k267_raw_width"])
    factor_width = 2 * total
    assert (factor_width - arb(comparison["factorized_raw_width"])).contains(0)
    assert (factor_width / prior_width - arb(comparison["factorized_to_k267_width_ratio"])).contains(0)
    assert factor_width / prior_width > arb(10**16)

    exact_checks = 0
    assert len(majorants) == 15; exact_checks += 1
    assert len(statuses()) == 6; exact_checks += 1
    assert comparison["factorized_derivative_term_evaluations"] == 27960; exact_checks += 1
    assert comparison["current_degree_nine_recurrence_updates"] == 257880; exact_checks += 1
    assert comparison["recurrence_reduction_factor"] == "2149/233"; exact_checks += 1
    assert record["decision"]["r6_disposition"] == "concluded_by_evidenced_rejection"; exact_checks += 1

    hostile_checks = 0
    assert record["selection"]["alternative_not_selected"] == "determinant_divided_differences"; hostile_checks += 1
    assert record["uniform_majorant"]["raw_interval"]["lower"].startswith("[-"); hostile_checks += 1
    k267 = json.loads(K267.read_text())
    assert sha256(K267.read_bytes()).hexdigest() == record["input_sha256"]["k267"]; hostile_checks += 1
    assert k267["certificate"]["result"] == "strictly_positive_complete_762_box_exchangeable_axis_middle_collar"; hostile_checks += 1

    print(f"[PASS] K273 independent replay exact={exact_checks} hostile={hostile_checks}")


if __name__ == "__main__":
    main()
