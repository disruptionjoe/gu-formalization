#!/usr/bin/env python3
"""K266: certify the first fixed-axis middle collar of the K218 integral."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from math import factorial
import sys

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

sys.set_int_max_str_digits(0)


K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
K265 = ROOT / "lab/process/k265-order-nine-complete-binary-low-high-union.json"
OUT = ROOT / "lab/process/k266-order-nine-first-fixed-axis-middle-collar.json"

MIDDLE_Q = (Q(13, 5), Q(15))
ORDER = 9
PRECISION = 256
POSITIVE_LOWER = Q(1, 10**18)
BOUNDS = {"low": LOW_Q, "middle": MIDDLE_Q, "high": HIGH_Q}
BLOCKS = (
    ("axis0_middle_axis1_low", ("middle", "low"), range(1, 7)),
    ("axis0_middle_axis1_high", ("middle", "high"), range(7)),
    ("axis1_middle_axis0_low", ("low", "middle"), range(1, 7)),
    ("axis1_middle_axis0_high", ("high", "middle"), range(7)),
)


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


def compile_box(groups: dict, fixed_status: tuple[str, str],
                high_subset: tuple[int, ...], ring, variables,
                geometry: dict[str, dict]) -> dict:
    status = list(fixed_status) + ["low"] * 6
    for axis in high_subset:
        status[axis] = "high"
    centers = tuple(geometry[name]["center"] for name in status)
    radii = tuple(geometry[name]["radius"] for name in status)
    moments = tuple(geometry[name]["moments"] for name in status)
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
        polynomial_terms = list(polynomial.terms())
        monomials.append(len(polynomial_terms))
        value = arb(0)
        for exponents, coefficient in polynomial_terms:
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
    for name in status:
        tail *= geometry[name]["measure"]
    return {
        "high_exceptional_axes": list(high_subset),
        "axis_status": status,
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
        "high_multiplicity": multiplicity,
        "boxes": len(boxes),
        "box_record_sha256": record_digest(boxes),
        "box_records": boxes,
        "complete_raw_head_by_degree": [str(value) for value in head_by_degree],
        "complete_raw_head": str(head),
        "complete_raw_absolute_tail_upper": str(tail),
        "complete_raw_integral_interval": {"lower": str(raw_lower), "upper": str(raw_upper)},
        "normalized_integral_interval": {"lower": str(lower), "upper": str(upper)},
    }


def summarize_block(name: str, fixed_status: tuple[str, str],
                    layers: list[dict], normalization_lower: fmpq,
                    normalization_upper: fmpq) -> dict:
    head_by_degree = [arb(0) for _ in range(ORDER + 1)]
    tail = Q()
    for layer in layers:
        for degree, value in enumerate(layer["complete_raw_head_by_degree"]):
            head_by_degree[degree] += arb(value)
        tail += Q(layer["complete_raw_absolute_tail_upper"])
    head = sum(head_by_degree, arb(0))
    raw_lower = head.lower() - as_arb(tail)
    raw_upper = head.upper() + as_arb(tail)
    lower, upper = normalized_interval(
        raw_lower, raw_upper, normalization_lower, normalization_upper
    )
    assert lower > 0
    return {
        "block": name,
        "fixed_axis_status": {"0": fixed_status[0], "1": fixed_status[1]},
        "boxes": sum(layer["boxes"] for layer in layers),
        "multiplicity_layers": layers,
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
    geometry = {}
    for name, bounds in BOUNDS.items():
        center, radius = box_center_and_radius(bounds)
        geometry[name] = {
            "center": center,
            "radius": radius,
            "moments": centered_moments(bounds, center, ORDER),
            "measure": sinh_log(bounds[1]) - sinh_log(bounds[0]),
        }
    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalization_upper = fmpq(2**8 * 256**6, factorial(5)) * fmpq(10, 31) ** 8

    blocks = []
    for name, fixed_status, multiplicities in BLOCKS:
        layers = []
        for multiplicity in multiplicities:
            boxes = [
                compile_box(groups, fixed_status, subset, ring, variables, geometry)
                for subset in combinations(range(2, 8), multiplicity)
            ]
            layers.append(summarize_layer(
                multiplicity, boxes, normalization_lower, normalization_upper
            ))
        blocks.append(summarize_block(
            name, fixed_status, layers, normalization_lower, normalization_upper
        ))

    complete_head_by_degree = [arb(0) for _ in range(ORDER + 1)]
    complete_tail = Q()
    for block in blocks:
        for degree, value in enumerate(block["complete_raw_head_by_degree"]):
            complete_head_by_degree[degree] += arb(value)
        complete_tail += Q(block["complete_raw_absolute_tail_upper"])
    complete_head = sum(complete_head_by_degree, arb(0))
    complete_raw_lower = complete_head.lower() - as_arb(complete_tail)
    complete_raw_upper = complete_head.upper() + as_arb(complete_tail)
    complete_lower, complete_upper = normalized_interval(
        complete_raw_lower, complete_raw_upper,
        normalization_lower, normalization_upper,
    )
    assert sum(block["boxes"] for block in blocks) == 254
    assert complete_lower > as_arb(POSITIVE_LOWER)

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K265)
        },
        "object": (
            "The exact K218 signed integral on the first fixed-axis middle collar: "
            "exactly one of axes 0 and 1 is middle, every other axis is low/high, "
            "and at least one non-middle coordinate is high"
        ),
        "domain": {
            "fixed_axis_blocks": [row[0] for row in BLOCKS],
            "exceptional_axes": list(range(2, 8)),
            "middle_q_interval": list(map(str, MIDDLE_Q)),
            "low_q_interval": list(map(str, LOW_Q)),
            "high_q_interval": list(map(str, HIGH_Q)),
            "boxes": 254,
            "pairwise_disjoint": True,
            "disjoint_from_k247_interior": True,
            "disjoint_from_k265_interior": True,
            "s6_invariant_by_complete_box_enumeration": True,
        },
        "projection": {
            "raw_signed_terms": len(items),
            "retained_exact_s6_orbits": len(groups),
            "orbit_manifest_sha256": orbit_digest,
            "rule": (
                "K230 licenses the retained representative only after integration "
                "over each complete S6-invariant multiplicity union. Every box is "
                "therefore enumerated; no pointwise representative compression is used."
            ),
        },
        "expansion": {
            "total_degree_inclusive": ORDER,
            "tail_starts_at_degree": ORDER + 1,
            "compiler": "exact FLINT fmpq multivariate polynomial recurrence",
            "integration": "signed head against exact product-cosh centered moments",
            "tail": "complete-homogeneous geometric majorant per orbit and box",
        },
        "fixed_axis_middle_blocks": blocks,
        "complete_collar": {
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
            "result": "strictly_positive_complete_254_box_first_fixed_axis_middle_collar",
        },
        "controls": (
            "An independent reverse-order raw-allocation probe recompiles all 254 boxes, "
            "moments and tails; reconstructs directed normalization; checks q2/q3 product "
            "quadratures; and applies absolute-weight, wrong-measure and block-deletion controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "All four fixed-axis orientations and their complete disjoint 254-box "
            "collar are strictly positive. The remaining middle region and far tail stay open."
        ),
        "claim_ceiling": (
            "Exact positivity and interval only on the declared 254-box collar. No full "
            "K218 integral, complete original order-six error, K215 impossibility, source, "
            "ledger, canon, paper, public-posture, or physical conclusion."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K266", result["certificate"]["result"])
    print("[PASS] K266 interval", result["complete_collar"]["normalized_integral_interval"])
