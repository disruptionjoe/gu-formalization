#!/usr/bin/env python3
"""K267: certify the first exchangeable-axis middle collar of K218."""
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
from k266_order_nine_first_fixed_axis_middle_collar import (
    MIDDLE_Q,
    coefficient_hash,
    normalized_interval,
    rational_row,
    record_digest,
)

sys.set_int_max_str_digits(0)


K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
K265 = ROOT / "lab/process/k265-order-nine-complete-binary-low-high-union.json"
K266 = ROOT / "lab/process/k266-order-nine-first-fixed-axis-middle-collar.json"
OUT = ROOT / "lab/process/k267-order-nine-exchangeable-axis-middle-collar.json"

ORDER = 9
PRECISION = 256
POSITIVE_LOWER = Q(1, 10**17)
BOUNDS = {"low": LOW_Q, "middle": MIDDLE_Q, "high": HIGH_Q}
BLOCKS = (
    ("fixed_low_low", ("low", "low")),
    ("fixed_high_low", ("high", "low")),
    ("fixed_low_high", ("low", "high")),
    ("fixed_high_high", ("high", "high")),
)


def status_specs(fixed_status: tuple[str, str], high_multiplicity: int):
    """Enumerate every box with exactly one middle exceptional axis."""
    for middle_axis in range(2, 8):
        remaining = tuple(axis for axis in range(2, 8) if axis != middle_axis)
        for high_subset in combinations(remaining, high_multiplicity):
            if fixed_status == ("low", "low") and not high_subset:
                continue
            status = list(fixed_status) + ["low"] * 6
            status[middle_axis] = "middle"
            for axis in high_subset:
                status[axis] = "high"
            yield middle_axis, high_subset, tuple(status)


def compile_box(groups: dict, middle_axis: int, high_subset: tuple[int, ...],
                status: tuple[str, ...], ring, variables,
                geometry: dict[str, dict]) -> dict:
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
        "middle_exceptional_axis": middle_axis,
        "high_exceptional_axes": list(high_subset),
        "axis_status": list(status),
        "coefficient_sha256_by_degree": hashes,
        "monomials_by_degree": monomials,
        "raw_head_by_degree": [str(value) for value in heads],
        "raw_absolute_tail_upper": str(tail),
    }


def summarize(records: list[dict], normalization_lower: fmpq,
              normalization_upper: fmpq) -> dict:
    head_by_degree = [arb(0) for _ in range(ORDER + 1)]
    tail = Q()
    for box in records:
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
        "boxes": len(records),
        "box_record_sha256": record_digest(records),
        "box_records": records,
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
    for block_name, fixed_status in BLOCKS:
        layers = []
        for high_multiplicity in range(6):
            boxes = [
                compile_box(groups, middle_axis, high_subset, status,
                            ring, variables, geometry)
                for middle_axis, high_subset, status
                in status_specs(fixed_status, high_multiplicity)
            ]
            if not boxes:
                continue
            layer = summarize(boxes, normalization_lower, normalization_upper)
            layer["high_exceptional_multiplicity"] = high_multiplicity
            layers.append(layer)
        block_boxes = [box for layer in layers for box in layer["box_records"]]
        block = summarize(block_boxes, normalization_lower, normalization_upper)
        block["block"] = block_name
        block["fixed_axis_status"] = {"0": fixed_status[0], "1": fixed_status[1]}
        block["multiplicity_layers"] = layers
        del block["box_records"]
        blocks.append(block)
        print(f"[CHECKPOINT] K267 {block_name} {block['boxes']} boxes", flush=True)

    all_boxes = [
        box
        for block in blocks
        for layer in block["multiplicity_layers"]
        for box in layer["box_records"]
    ]
    complete = summarize(all_boxes, normalization_lower, normalization_upper)
    del complete["box_records"]
    assert [block["boxes"] for block in blocks] == [186, 192, 192, 192]
    assert complete["boxes"] == 762
    complete_lower = arb(complete["normalized_integral_interval"]["lower"])
    assert complete_lower > as_arb(POSITIVE_LOWER)

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K265, K266)
        },
        "object": (
            "The exact K218 signed integral on the first complete exchangeable-axis "
            "middle collar: exactly one of axes 2..7 is middle, every other axis "
            "is low/high, and at least one non-middle coordinate is high"
        ),
        "domain": {
            "fixed_axis_blocks": [name for name, _ in BLOCKS],
            "exchangeable_axes": list(range(2, 8)),
            "middle_q_interval": list(map(str, MIDDLE_Q)),
            "low_q_interval": list(map(str, LOW_Q)),
            "high_q_interval": list(map(str, HIGH_Q)),
            "boxes": 762,
            "pairwise_disjoint": True,
            "disjoint_from_k247_interior": True,
            "disjoint_from_k265_interior": True,
            "disjoint_from_k266_interior": True,
            "s6_invariant_by_complete_box_enumeration": True,
        },
        "projection": {
            "raw_signed_terms": len(items),
            "retained_exact_s6_orbits": len(groups),
            "orbit_manifest_sha256": orbit_digest,
            "rule": (
                "K230 licenses the retained representative only after integration "
                "over a complete S6-invariant union. Every box is enumerated; no "
                "pointwise representative compression is used."
            ),
        },
        "expansion": {
            "total_degree_inclusive": ORDER,
            "tail_starts_at_degree": ORDER + 1,
            "compiler": "exact FLINT fmpq multivariate polynomial recurrence",
            "integration": "signed head against exact product-cosh centered moments",
            "tail": "complete-homogeneous geometric majorant per orbit and box",
        },
        "fixed_axis_blocks": blocks,
        "complete_collar": complete,
        "certificate": {
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "normalization_upper_using_pi_greater_than_31_over_10": str(normalization_upper),
            "normalization_direction_rule": (
                "Positive lower endpoints use pi<22/7; positive and absolute upper "
                "endpoints, negative lower endpoints, and tails use pi>31/10."
            ),
            "declared_strict_positive_mass_lower": rational_row(POSITIVE_LOWER),
            "result": "strictly_positive_complete_762_box_exchangeable_axis_middle_collar",
        },
        "controls": (
            "An independent reverse-order raw-allocation probe recompiles all 762 "
            "boxes, moments and tails; reconstructs directed normalization; checks "
            "q2/q3 product quadratures; and applies absolute-weight, wrong-measure "
            "and dominant-block deletion controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "The complete adjacent exchangeable-axis middle collar is strictly "
            "positive after signed composition. Farther middle bands and tails stay open."
        ),
        "claim_ceiling": (
            "Exact positivity and interval only on the declared 762-box collar. No "
            "full K218 integral, complete original order-six error, K215 impossibility, "
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
    print("[PASS] K267", result["certificate"]["result"])
    print("[PASS] K267 interval", result["complete_collar"]["normalized_integral_interval"])
