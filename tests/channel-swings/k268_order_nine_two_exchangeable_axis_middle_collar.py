#!/usr/bin/env python3
"""K268: certify the two-exchangeable-axis middle collar of K218."""
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
    K185,
    as_arb,
    box_center_and_radius,
    centered_moments,
    sinh_log,
)
from k267_order_nine_exchangeable_axis_middle_collar import (
    BLOCKS,
    BOUNDS,
    K218,
    K230,
    K247,
    K265,
    K266,
    ORDER,
    PRECISION,
    compile_box,
    summarize,
)


K267 = ROOT / "lab/process/k267-order-nine-exchangeable-axis-middle-collar.json"
OUT = ROOT / "lab/process/k268-order-nine-two-exchangeable-axis-middle-collar.json"
POSITIVE_LOWER = Q(1, 10**16)


def status_specs(fixed_status: tuple[str, str], high_multiplicity: int):
    """Enumerate every box with exactly two middle exchangeable axes."""
    for middle_axes in combinations(range(2, 8), 2):
        remaining = tuple(axis for axis in range(2, 8) if axis not in middle_axes)
        for high_subset in combinations(remaining, high_multiplicity):
            if fixed_status == ("low", "low") and not high_subset:
                continue
            status = list(fixed_status) + ["low"] * 6
            for axis in middle_axes:
                status[axis] = "middle"
            for axis in high_subset:
                status[axis] = "high"
            yield middle_axes, high_subset, tuple(status)


def compile_two_middle_box(groups: dict, middle_axes: tuple[int, int],
                           high_subset: tuple[int, ...],
                           status: tuple[str, ...], ring, variables,
                           geometry: dict[str, dict]) -> dict:
    record = compile_box(
        groups, middle_axes[0], high_subset, status, ring, variables, geometry
    )
    del record["middle_exceptional_axis"]
    record["middle_exceptional_axes"] = list(middle_axes)
    return record


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
        for high_multiplicity in range(5):
            boxes = [
                compile_two_middle_box(
                    groups, middle_axes, high_subset, status,
                    ring, variables, geometry,
                )
                for middle_axes, high_subset, status
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
        print(f"[CHECKPOINT] K268 {block_name} {block['boxes']} boxes", flush=True)

    all_boxes = [
        box
        for block in blocks
        for layer in block["multiplicity_layers"]
        for box in layer["box_records"]
    ]
    complete = summarize(all_boxes, normalization_lower, normalization_upper)
    del complete["box_records"]
    assert [block["boxes"] for block in blocks] == [225, 240, 240, 240]
    assert complete["boxes"] == 945
    complete_lower = arb(complete["normalized_integral_interval"]["lower"])
    assert complete_lower > as_arb(POSITIVE_LOWER)

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K265, K266, K267)
        },
        "object": (
            "The exact K218 signed integral on the second complete exchangeable-axis "
            "middle collar: exactly two of axes 2..7 are middle, every other axis "
            "is low/high, and at least one non-middle coordinate is high"
        ),
        "domain": {
            "fixed_axis_blocks": [name for name, _ in BLOCKS],
            "exchangeable_axes": list(range(2, 8)),
            "middle_axis_count": 2,
            "middle_q_interval": list(map(str, BOUNDS["middle"])),
            "low_q_interval": list(map(str, BOUNDS["low"])),
            "high_q_interval": list(map(str, BOUNDS["high"])),
            "boxes": 945,
            "pairwise_disjoint": True,
            "disjoint_from_k247_interior": True,
            "disjoint_from_k265_interior": True,
            "disjoint_from_k266_interior": True,
            "disjoint_from_k267_interior": True,
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
            "declared_strict_positive_mass_lower": {
                "numerator": POSITIVE_LOWER.numerator,
                "denominator": POSITIVE_LOWER.denominator,
            },
            "result": "strictly_positive_complete_945_box_two_exchangeable_axis_middle_collar",
        },
        "controls": (
            "An independent reverse-order raw-allocation probe recompiles all 945 "
            "boxes, moments and tails; reconstructs directed normalization; checks "
            "q2/q3 product quadratures; and applies absolute-weight, wrong-measure "
            "and dominant-block deletion controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "The complete second adjacent exchangeable-axis middle collar is strictly "
            "positive after signed composition. Farther middle bands and tails stay open."
        ),
        "claim_ceiling": (
            "Exact positivity and interval only on the declared 945-box collar. No "
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
    print("[PASS] K268", result["certificate"]["result"])
    print("[PASS] K268 interval", result["complete_collar"]["normalized_integral_interval"])
