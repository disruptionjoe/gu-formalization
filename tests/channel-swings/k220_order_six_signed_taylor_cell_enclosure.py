#!/usr/bin/env python3
"""K220: signed-center Taylor enclosure of the exact K218 auxiliary core."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from k219_order_six_signed_auxiliary_cell_enclosure import (
    K185, K218, ROOT, SCALE, allocation_coefficients, core_bounds,
)

K219 = ROOT / "lab/process/k219-order-six-signed-auxiliary-cell-enclosure.json"
K217 = ROOT / "lab/process/k217-order-six-signed-inner-box.json"
OUT = ROOT / "lab/process/k220-order-six-signed-taylor-cell-enclosure.json"


def term_data(masks: tuple[int, ...], c: tuple[Q, ...]) -> tuple[Q, tuple[Q, ...], tuple[Q, ...]]:
    loads = tuple(256 + sum(c[j] for j in range(8) if masks[j] & (1 << i)) for i in range(14))
    q = Q(1)
    for a in loads:
        q /= a
    slopes = tuple(sum((Q(1, loads[i]) for i in range(14) if masks[j] & (1 << i)), Q(0))
                   for j in range(8))
    return q, slopes, loads


def signed_taylor_bounds(source: dict, low: tuple[Q, ...], high: tuple[Q, ...]) -> dict:
    """Exact Taylor interval, with Hessian controlled at the lower corner.

    q_A=prod_i a_i^-1, a_i=256+sum_j mask_ji c_j. For c>=low,
    |d_jd_k q_A|=q_A (L_j L_k+sum_i mask_ji mask_ki/a_i^2)
    is bounded by replacing every load with its lower-corner value. The
    integral Taylor remainder along the center-to-point segment is <=R2.
    """
    assert len(low) == len(high) == 8 and all(Q(1) <= a <= b for a, b in zip(low, high))
    center = tuple((a + b) / 2 for a, b in zip(low, high))
    radius = tuple((b - a) / 2 for a, b in zip(low, high))
    coefficients = allocation_coefficients(source)
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    value = Q(0)
    gradient = [Q(0)] * 8
    remainder_twice = Q(0)
    for key, w in coefficients.items():
        masks = tuple(int(v, 16) for v in catalog[key]["support_masks_hex"].split(","))
        q_mid, slopes_mid, _ = term_data(masks, center)
        value += w * q_mid
        for j in range(8):
            gradient[j] -= w * q_mid * slopes_mid[j]
        q_low, slopes_low, loads_low = term_data(masks, low)
        combined_slope = sum((radius[j] * slopes_low[j] for j in range(8)), Q(0))
        shared_load = sum((sum((radius[j] for j in range(8) if masks[j] & (1 << i)), Q(0))
                           / loads_low[i]) ** 2 for i in range(14))
        remainder_twice += abs(w) * q_low * (combined_slope**2 + shared_load)
    linear_radius = sum((abs(gradient[j]) * radius[j] for j in range(8)), Q(0))
    remainder = remainder_twice / 2
    raw = (value - linear_radius - remainder, value + linear_radius + remainder)
    corner = core_bounds(source, low, high)
    intersected = (max(raw[0], corner[0]), min(raw[1], corner[1]))
    assert intersected[0] <= intersected[1]
    return {"center": center, "radius": radius, "center_core": value,
            "signed_gradient": tuple(gradient), "linear_radius": linear_radius,
            "hessian_remainder": remainder, "taylor_core": raw,
            "corner_core": corner, "intersection_core": intersected}


def pilot(source: dict, low: tuple[Q, ...], high: tuple[Q, ...], measure: Q) -> dict:
    bound = signed_taylor_bounds(source, low, high)
    def pair(k: str) -> list[str]:
        return [str(SCALE * measure * v) for v in bound[k]]
    old_width = bound["corner_core"][1] - bound["corner_core"][0]
    new_width = bound["intersection_core"][1] - bound["intersection_core"][0]
    return {"cosh_lower": [str(v) for v in low], "cosh_upper": [str(v) for v in high],
            "exact_product_cosh_measure": str(measure), "center_core": str(bound["center_core"]),
            "signed_gradient": [str(v) for v in bound["signed_gradient"]],
            "linear_radius": str(bound["linear_radius"]),
            "hessian_remainder": str(bound["hessian_remainder"]),
            "taylor_integral_interval_without_pi8": pair("taylor_core"),
            "k219_integral_interval_without_pi8": pair("corner_core"),
            "intersection_integral_interval_without_pi8": pair("intersection_core"),
            "intersection_width_to_k219_width": str(new_width / old_width),
            "interval_decimal_without_pi8": [f"{float(SCALE * measure * v):.8e}"
                                              for v in bound["intersection_core"]]}


def generate() -> dict:
    source = json.loads(K185.read_text())
    prior = json.loads(K219.read_text())
    small_cos = Q(41, 40)  # cosh(log(5/4)); sinh(log(5/4))=9/40
    inner = pilot(source, (Q(1),)*8, (small_cos,)*8, Q(9, 40)**8)
    old_inner = pilot(source, (Q(1),)*8, (Q(5, 4),)*8, Q(3, 4)**8)
    mixed_low = tuple(Q(1) if j % 2 == 0 else Q(5, 4) for j in range(8))
    mixed_high = tuple(Q(5, 4) if j % 2 == 0 else Q(17, 8) for j in range(8))
    mixed = pilot(source, mixed_low, mixed_high, Q(3, 4)**4 * Q(9, 8)**4)
    assert Q(inner["intersection_width_to_k219_width"]) < 1
    old_signed = Q(json.loads(K217.read_text())["remainder"]["whole_2928_ordered_term_absolute_ceiling"])
    full_inner_upper = Q(old_inner["intersection_integral_interval_without_pi8"][1])
    assert -Q(old_inner["intersection_integral_interval_without_pi8"][0]) == full_inner_upper
    assert full_inner_upper / 3**8 < old_signed  # pi > 3
    return {"schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
            "input_sha256": {"k185": hashlib.sha256(K185.read_bytes()).hexdigest(),
                             "k217": hashlib.sha256(K217.read_bytes()).hexdigest(),
                             "k218": hashlib.sha256(K218.read_bytes()).hexdigest(),
                             "k219": hashlib.sha256(K219.read_bytes()).hexdigest()},
            "object": prior["object"],
            "theorem": "For signed H(c)=sum_A w_A q_A(c), q_A=prod_i a_i(c)^-1 and a_i=256+sum_j m_Aji c_j, let center m and radii r be a nonnegative rectangular cosh cell. H(m) and its signed gradient are exact. With L_Aj=sum_i m_Aji/a_i(low), Taylor's segment remainder is at most (1/2) sum_A |w_A|q_A(low)[(sum_j r_j L_Aj)^2+sum_i (sum_j r_j m_Aji/a_i(low))^2]. Thus H(c) lies within H(m) plus/minus sum_j r_j|d_j H(m)| plus/minus that remainder. Intersect with K219's exact corner interval and multiply by the positive exact product-cosh cell measure and 2^8*256^6/(5! pi^8). Shared loads are retained in the second Hessian term; no independent-load corner attainability is assumed.",
            "pilot_cells": {"small_inner": inner, "k219_inner": old_inner, "alternating_shifted": mixed},
            "full_inner_comparison": {"pi_lower_bound": 3, "absolute_upper_rational_using_pi_gt_3": str(full_inner_upper/3**8), "k217_absolute_ceiling": str(old_signed), "strictly_sharper": True},
            "interpretation": "Signed-derivative correlation strictly narrows all three local K219 pilots. For the complete [0,log(2)]^8 inner box, pi>3 converts the exact K220 symmetric interval to an absolute bound below K217's previous signed ceiling. No middle-region cover, node-cost floor, coalescent/quotient/reference composition or accurate full prefix follows.",
            "source_routing": prior["source_routing"],
            "unchanged_complete_rule_error_upper_rational": prior["unchanged_complete_rule_error_upper_rational"],
            "claim_ceiling": "Exact local signed Taylor cell enclosure with a finite rational comparison, not a whole-box cubature or GU physics/source verdict."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K220 signed Taylor cell theorem and rational pilots")
