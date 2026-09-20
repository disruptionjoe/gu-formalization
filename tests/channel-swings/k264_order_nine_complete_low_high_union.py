#!/usr/bin/env python3
"""K264: certify the complete 64-box K218 low/high union positive."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from math import factorial

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import ROOT, terms
from k242_order_six_third_shell_signed_taylor import orbit_groups
from k262_order_six_low_through_three_high_multiplicity_integral import (
    HIGH_Q,
    K185,
    LOW_Q,
    as_arb,
    box_center_and_radius,
    centered_moments,
    rational_tail,
    sinh_log,
)


K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K261 = ROOT / "lab/process/k261-order-six-all-pair-box-taylor-integral.json"
K262 = ROOT / "lab/process/k262-order-six-low-through-three-high-multiplicity-integral.json"
K263 = ROOT / "lab/process/k263-order-six-four-high-multiplicity-integral.json"
OUT = ROOT / "lab/process/k264-order-nine-complete-low-high-union.json"

ORDER = 9
PRECISION = 256
POSITIVE_LOWER = Q(106, 10**22)  # 1.06e-20


def rational_row(value: Q) -> dict:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": f"{float(value):.12e}",
    }


def coefficient_hash(polynomial) -> str:
    payload = ";".join(
        f"{','.join(map(str, exponents))}:{coefficient}"
        for exponents, coefficient in polynomial.terms()
    )
    return sha256(payload.encode()).hexdigest()


def record_digest(records: list[dict]) -> str:
    payload = json.dumps(records, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode()).hexdigest()


def normalized_interval(raw_lower: arb, raw_upper: arb,
                        normalization_lower: fmpq,
                        normalization_upper: fmpq) -> tuple[arb, arb]:
    lower_scale = normalization_upper if raw_lower < 0 else normalization_lower
    upper_scale = normalization_upper if raw_upper > 0 else normalization_lower
    return arb(lower_scale) * raw_lower, arb(upper_scale) * raw_upper


def compile_box(groups: dict, subset: tuple[int, ...], ring, variables,
                low_center: Q, low_radius: Q, high_center: Q, high_radius: Q,
                low_moments: tuple, high_moments: tuple,
                low_measure: Q, high_measure: Q) -> dict:
    active = frozenset((1,) + subset)
    centers = tuple(high_center if axis in active else low_center for axis in range(8))
    radii = tuple(high_radius if axis in active else low_radius for axis in range(8))
    moments = tuple(high_moments if axis in active else low_moments for axis in range(8))
    polynomials = [ring.constant(0) for _ in range(ORDER + 1)]

    for rows, weight in groups.items():
        pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(ORDER)]
        for row in rows:
            support = tuple(axis for axis in range(8) if row & (1 << axis))
            base = fmpq(256) + sum(
                (fmpq(centers[axis].numerator, centers[axis].denominator)
                 for axis in support),
                fmpq(0),
            )
            linear = sum((variables[axis] for axis in support), ring.constant(0))
            divided = [pieces[0] / base]
            for degree in range(1, ORDER + 1):
                divided.append((pieces[degree] - linear * divided[degree - 1]) / base)
            pieces = divided
        for degree, piece in enumerate(pieces):
            polynomials[degree] += weight * piece

    heads = []
    hashes = []
    monomials = []
    for polynomial in polynomials:
        hashes.append(coefficient_hash(polynomial))
        terms_in_polynomial = list(polynomial.terms())
        monomials.append(len(terms_in_polynomial))
        value = arb(0)
        for exponents, coefficient in terms_in_polynomial:
            term = arb(coefficient)
            for axis, exponent in enumerate(exponents):
                term *= moments[axis][exponent]
            value += term
        heads.append(value)

    tail = sum(
        (Q(abs(weight)) * rational_tail(rows, centers, radii, ORDER + 1)
         for rows, weight in groups.items()),
        Q(),
    )
    multiplicity = len(subset)
    tail *= high_measure ** (1 + multiplicity) * low_measure ** (7 - multiplicity)
    return {
        "high_exceptional_axes": list(subset),
        "coefficient_sha256_by_degree": hashes,
        "monomials_by_degree": monomials,
        "raw_head_by_degree": [str(value) for value in heads],
        "raw_absolute_tail_upper": str(tail),
    }


def summarize_layer(multiplicity: int, boxes: list[dict],
                    normalization_lower: fmpq,
                    normalization_upper: fmpq) -> dict:
    head_by_degree = [arb(0) for _ in range(ORDER + 1)]
    tail = Q()
    for box in boxes:
        for degree, value in enumerate(box["raw_head_by_degree"]):
            head_by_degree[degree] += arb(value)
        tail += Q(box["raw_absolute_tail_upper"])
    head = sum(head_by_degree, arb(0))
    raw_lower = head.lower() - as_arb(tail)
    raw_upper = head.upper() + as_arb(tail)
    lower, upper = normalized_interval(
        raw_lower, raw_upper, normalization_lower, normalization_upper
    )
    return {
        "multiplicity": multiplicity,
        "boxes": len(boxes),
        "box_record_sha256": record_digest(boxes),
        "box_records": boxes,
        "complete_raw_head_by_degree": [str(value) for value in head_by_degree],
        "complete_raw_head": str(head),
        "complete_raw_absolute_tail_upper": str(tail),
        "complete_raw_integral_interval": {"lower": str(raw_lower), "upper": str(raw_upper)},
        "normalized_integral_interval": {"lower": str(lower), "upper": str(upper)},
    }


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    groups = orbit_groups(items)
    projection = json.loads(K230.read_text())
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    orbit_digest = sha256(compact.encode()).hexdigest()
    assert len(items) == 1864 and len(groups) == 307
    assert orbit_digest == projection["orbit_coefficient_manifest_sha256"]

    ring = fmpq_mpoly_ctx.get([f"x{axis}" for axis in range(8)])
    variables = ring.gens()
    low_center, low_radius = box_center_and_radius(LOW_Q)
    high_center, high_radius = box_center_and_radius(HIGH_Q)
    low_moments = centered_moments(LOW_Q, low_center, ORDER)
    high_moments = centered_moments(HIGH_Q, high_center, ORDER)
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])
    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalization_upper = fmpq(2**8 * 256**6, factorial(5)) * fmpq(10, 31) ** 8

    layers = []
    for multiplicity in range(7):
        boxes = [
            compile_box(
                groups, subset, ring, variables,
                low_center, low_radius, high_center, high_radius,
                low_moments, high_moments, low_measure, high_measure,
            )
            for subset in combinations(range(2, 8), multiplicity)
        ]
        layers.append(summarize_layer(
            multiplicity, boxes, normalization_lower, normalization_upper
        ))

    complete_head_by_degree = [arb(0) for _ in range(ORDER + 1)]
    complete_tail = Q()
    for layer in layers:
        for degree, value in enumerate(layer["complete_raw_head_by_degree"]):
            complete_head_by_degree[degree] += arb(value)
        complete_tail += Q(layer["complete_raw_absolute_tail_upper"])
    complete_head = sum(complete_head_by_degree, arb(0))
    complete_raw_lower = complete_head.lower() - as_arb(complete_tail)
    complete_raw_upper = complete_head.upper() + as_arb(complete_tail)
    complete_lower, complete_upper = normalized_interval(
        complete_raw_lower, complete_raw_upper,
        normalization_lower, normalization_upper,
    )
    assert complete_lower > as_arb(POSITIVE_LOWER)

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K261, K262, K263)
        },
        "object": (
            "The exact K218 signed integral on the complete 64-box S6-invariant "
            "low/high union with fixed high axis 1, fixed low axis 0, and all "
            "exceptional-coordinate high multiplicities zero through six"
        ),
        "domain": {
            "fixed_high_axis": 1,
            "fixed_low_axis": 0,
            "exceptional_axes": list(range(2, 8)),
            "included_high_multiplicities": list(range(7)),
            "high_q_interval": list(map(str, HIGH_Q)),
            "low_q_interval": list(map(str, LOW_Q)),
            "boxes": 64,
            "pairwise_disjoint": True,
            "s6_invariant_union": True,
        },
        "projection": {
            "raw_signed_terms": len(items),
            "retained_exact_s6_orbits": len(groups),
            "orbit_manifest_sha256": orbit_digest,
            "rule": (
                "K230 proves integral equality on each complete multiplicity union "
                "and on their complete disjoint union. No projected representative "
                "is asserted equal on one non-invariant box."
            ),
        },
        "expansion": {
            "total_degree_inclusive": ORDER,
            "tail_starts_at_degree": ORDER + 1,
            "compiler": "exact FLINT fmpq multivariate polynomial recurrence",
            "integration": "signed head against exact product-cosh centered moments",
            "tail": "complete-homogeneous geometric majorant per orbit and box",
        },
        "multiplicity_layers": layers,
        "complete_union": {
            "complete_raw_head_by_degree": [str(value) for value in complete_head_by_degree],
            "complete_raw_head": str(complete_head),
            "complete_raw_absolute_tail_upper": str(complete_tail),
            "complete_raw_integral_interval": {
                "lower": str(complete_raw_lower),
                "upper": str(complete_raw_upper),
            },
            "normalized_integral_interval": {
                "lower": str(complete_lower),
                "upper": str(complete_upper),
            },
        },
        "certificate": {
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "normalization_upper_using_pi_greater_than_31_over_10": str(normalization_upper),
            "normalization_direction_rule": (
                "Positive lower endpoints use pi<22/7; positive and absolute upper "
                "endpoints, negative lower endpoints, and tails use pi>31/10."
            ),
            "declared_strict_positive_mass_lower": rational_row(POSITIVE_LOWER),
            "result": "strictly_positive_complete_64_box_low_high_union",
        },
        "controls": (
            "An independent reverse-order raw-allocation probe recompiles every exact "
            "degree polynomial, moment and tail; checks two- and three-point product "
            "quadratures; and applies absolute-weight, wrong-measure, multiplicity-four "
            "deletion and lower-order-certificate controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "Order-nine cross-layer control resolves K263's interval ambiguity: the "
            "complete 64-box low/high union is strictly positive. This is a bounded "
            "far-region sign theorem, not the sign of the remaining K218 complement."
        ),
        "claim_ceiling": (
            "Exact positivity and interval only on the declared complete 64-box union. "
            "No full K218 integral, complete original order-six error, K215 impossibility, "
            "source, ledger, canon, paper, public-posture, or physical conclusion."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K264", result["certificate"]["result"])
    print("[PASS] K264 interval", result["complete_union"]["normalized_integral_interval"])
