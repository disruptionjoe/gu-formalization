#!/usr/bin/env python3
"""K219: rational cell enclosure for the K218 signed auxiliary integrand."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
OUT = ROOT / "lab/process/k219-order-six-signed-auxiliary-cell-enclosure.json"
SCALE = Q(2**8 * 256**6, 120)  # multiply every reported rational by pi^-8


def allocation_coefficients(source: dict) -> dict[str, int]:
    """Collect identical denominator products before taking interval bounds."""
    coefficients: Counter[str] = Counter()
    for entry in source["complete_face_hypergraph"]["entries"]:
        weight = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            coefficients[term["allocation_id"]] += weight * term["leibniz_sign"]
    return {key: value for key, value in coefficients.items() if value}


def repetition_certificate(source: dict) -> dict:
    signs: dict[str, set[int]] = {}
    counts: Counter[str] = Counter()
    for entry in source["complete_face_hypergraph"]["entries"]:
        weight = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            key = term["allocation_id"]
            signs.setdefault(key, set()).add(1 if weight * term["leibniz_sign"] > 0 else -1)
            counts[key] += 1
    assert len(signs) == 1276 and all(len(s) == 1 for s in signs.values())
    return {"repeated_allocations": sum(n > 1 for n in counts.values()),
            "largest_repetition": max(counts.values()), "opposite_sign_repetitions": 0,
            "consequence": "Since every repetition has one sign, combining identical products changes evaluation count but not signed corner interval endpoints on any cell."}


def reciprocal_product(masks: tuple[int, ...], coshes: tuple[Q, ...]) -> Q:
    loads = [256] * 14
    for j, mask in enumerate(masks):
        for i in range(14):
            if mask & (1 << i):
                loads[i] += coshes[j]
    product = 1
    for load in loads:
        product *= load
    return Q(1, product)


def signed_core(source: dict, coshes: tuple[Q, ...]) -> Q:
    coefficients = allocation_coefficients(source)
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    return sum((weight * reciprocal_product(tuple(int(v, 16) for v in catalog[key]["support_masks_hex"].split(",")), coshes)
                for key, weight in coefficients.items()), Q(0))


def core_bounds(source: dict, low: tuple[Q, ...], high: tuple[Q, ...], *, aggregate: bool = True) -> tuple[Q, Q]:
    """Signed interval: positive reciprocal factors fall as each cosh grows.

    This is valid on the *entire* rectangular t cell, including shared loads.
    No false assumption of independently attainable corners is needed.
    """
    assert len(low) == len(high) == 8 and all(Q(1) <= a <= b for a, b in zip(low, high))
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    if aggregate:
        terms = allocation_coefficients(source).items()
    else:
        terms = ((term["allocation_id"], entry["coefficient_product"] * term["leibniz_sign"]
                  * (2 if entry["left"] != entry["right"] else 1))
                 for entry in source["complete_face_hypergraph"]["entries"] for term in entry["terms"])
    cache: dict[str, tuple[Q, Q]] = {}
    lower = upper = Q(0)
    for key, weight in terms:
        if key not in cache:
            masks = tuple(int(v, 16) for v in catalog[key]["support_masks_hex"].split(","))
            cache[key] = reciprocal_product(masks, low), reciprocal_product(masks, high)
        q_low, q_high = cache[key]
        lower += weight * (q_high if weight > 0 else q_low)
        upper += weight * (q_low if weight > 0 else q_high)
    assert lower <= upper
    return lower, upper


def cell_bounds(source: dict, low: tuple[Q, ...], high: tuple[Q, ...], measure: Q) -> tuple[Q, Q]:
    """Weighted cell integral bounds in rational units of pi^-8.

    measure is exactly product_j (sinh(t_j^+) - sinh(t_j^-));
    monotonicity cosh(t) on t>=0 yields the core interval.
    """
    assert measure >= 0
    a, b = core_bounds(source, low, high)
    return SCALE * measure * a, SCALE * measure * b


def _pilot(source: dict, lower: tuple[Q, ...], upper: tuple[Q, ...], measure: Q) -> dict:
    bound = cell_bounds(source, lower, upper, measure)
    raw = core_bounds(source, lower, upper, aggregate=False)
    center = tuple((x + y) / 2 for x, y in zip(lower, upper))
    point = SCALE * signed_core(source, center) * _product(center)
    return {
        "cosh_lower": [str(v) for v in lower],
        "cosh_upper": [str(v) for v in upper],
        "exact_product_cosh_measure": str(measure),
        "signed_integral_interval_without_pi8": [str(v) for v in bound],
        "raw_term_core_width_to_aggregated_core_width": str((raw[1] - raw[0]) / (bound[1] - bound[0]) * SCALE * measure),
        "center_integrand_without_pi8": str(point),
        "integral_interval_decimal_without_pi8": [f"{float(v):.8e}" for v in bound],
    }


def _product(items: tuple[Q, ...]) -> Q:
    product = Q(1)
    for item in items:
        product *= item
    return product


def generate() -> dict:
    source = json.loads(K185.read_text())
    previous = json.loads(K218.read_text())
    coefficients = allocation_coefficients(source)
    repetitions = repetition_certificate(source)
    assert len(coefficients) == previous["distinct_allocations"] == 1276
    assert sum(coefficients.values()) == 0
    assert signed_core(source, (Q(1),) * 8) == 0
    equal = _pilot(source, (Q(1),) * 8, (Q(5, 4),) * 8, Q(3, 4)**8)
    shifted = _pilot(source, (Q(5, 4),) + (Q(1),) * 7,
                     (Q(17, 8),) + (Q(5, 4),) * 7, Q(9, 8) * Q(3, 4)**7)
    mixed_low = tuple(Q(1) if j % 2 == 0 else Q(5, 4) for j in range(8))
    mixed_high = tuple(Q(5, 4) if j % 2 == 0 else Q(17, 8) for j in range(8))
    mixed = _pilot(source, mixed_low, mixed_high, Q(3, 4)**4 * Q(9, 8)**4)
    assert Q(mixed["center_integrand_without_pi8"]) != 0
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"k185": hashlib.sha256(K185.read_bytes()).hexdigest(),
                         "k218": hashlib.sha256(K218.read_bytes()).hexdigest()},
        "object": "K218's exact raw signed eight-auxiliary rational-cosh integrand on nonnegative rectangular t cells",
        "theorem": "For 1<=l_j<=cosh(t_j)<=u_j and H(c)=sum_A w_A/prod_i(256+sum_(j:i in A_j)c_j), every denominator reciprocal decreases coordinatewise. Hence L=sum_(w_A>0)w_A q_A(u)+sum_(w_A<0)w_A q_A(l) <= H(c) <= U=sum_(w_A>0)w_A q_A(l)+sum_(w_A<0)w_A q_A(u). Combine identical allocations before bounding. The complete weighted cell integral lies in [L,U]*(2^8*256^6/5!)*prod_j(sinh(t_j^+)-sinh(t_j^-))/pi^8.",
        "exact_signed_coefficients": {"raw_terms": 1864, "ordered_with_off_diagonal": 2928,
                                      "distinct_nonzero_allocations": len(coefficients),
                                      "signed_coefficient_sum": sum(coefficients.values())},
        "repetition_certificate": repetitions,
        "pilot_cells": {"inner_box": equal, "first_shifted_slab": shifted,
                        "alternating_shifted_cell": mixed},
        "interpretation": "These exact intervals preserve signs but discard shared-denominator determinant correlations within a cell. All 480 repeated allocation IDs have a single sign, so compression from 1,864 to 1,276 changes evaluation count but provably never narrows any cell interval. K217's global inner-box cancellation bound is sharper than the naive inner-cell interval (the latter's exact rational endpoint still carries pi^-8). A mixed shifted cell has nonzero center. Neither widths nor midpoint values are a convergence rate, full-box cover, or actual signed integral; determinant-aware correlation is the next discriminator.",
        "source_routing": previous["source_routing"],
        "unchanged_complete_rule_error_upper_rational": previous["unchanged_complete_rule_error_upper_rational"],
        "claim_ceiling": "Certified local signed-cell enclosure for the K218 raw auxiliary expression, not a certified middle-box sum, practical adaptive cost, coalescent/quotient/common-reference boundary composition, accurate complete prefix, or source/physics verdict.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K219 exact signed auxiliary-cell enclosure and rational pilot")
