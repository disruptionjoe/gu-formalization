#!/usr/bin/env python3
"""K269: certify the complete three-plus exchangeable-middle collar of K218."""
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
    K185, as_arb, box_center_and_radius, centered_moments, sinh_log,
)
from k267_order_nine_exchangeable_axis_middle_collar import (
    BLOCKS, BOUNDS, K218, K230, K247, K265, K266, ORDER, PRECISION,
    compile_box, summarize,
)

K267 = ROOT / "lab/process/k267-order-nine-exchangeable-axis-middle-collar.json"
K268 = ROOT / "lab/process/k268-order-nine-two-exchangeable-axis-middle-collar.json"
OUT = ROOT / "lab/process/k269-order-nine-three-plus-exchangeable-axis-middle-collar.json"
POSITIVE_LOWER = Q(1, 10**15)
MIDDLE_COUNTS = tuple(range(3, 7))


def status_specs(fixed_status: tuple[str, str], middle_count: int,
                 high_multiplicity: int):
    for middle_axes in combinations(range(2, 8), middle_count):
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


def compile_middle_box(groups, middle_axes, high_subset, status,
                       ring, variables, geometry):
    record = compile_box(
        groups, middle_axes[0], high_subset, status, ring, variables, geometry
    )
    del record["middle_exceptional_axis"]
    record["middle_exceptional_axes"] = list(middle_axes)
    return record


def generate() -> dict:
    ctx.prec = PRECISION
    items = list(terms(json.loads(K185.read_text())))
    groups = orbit_groups(items)
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    orbit_digest = sha256(compact.encode()).hexdigest()
    assert len(items) == 1864 and len(groups) == 307
    assert orbit_digest == json.loads(K230.read_text())["orbit_coefficient_manifest_sha256"]

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
    norm_lo = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    norm_hi = fmpq(2**8 * 256**6, factorial(5)) * fmpq(10, 31) ** 8

    count_strata = []
    for middle_count in MIDDLE_COUNTS:
        blocks = []
        for block_name, fixed_status in BLOCKS:
            layers = []
            for high_multiplicity in range(7 - middle_count):
                boxes = [
                    compile_middle_box(
                        groups, middle_axes, high_subset, status,
                        ring, variables, geometry,
                    )
                    for middle_axes, high_subset, status
                    in status_specs(fixed_status, middle_count, high_multiplicity)
                ]
                if not boxes:
                    continue
                layer = summarize(boxes, norm_lo, norm_hi)
                layer["high_exceptional_multiplicity"] = high_multiplicity
                layers.append(layer)
            block_boxes = [b for layer in layers for b in layer["box_records"]]
            if not block_boxes:
                continue
            block = summarize(block_boxes, norm_lo, norm_hi)
            block["block"] = block_name
            block["fixed_axis_status"] = {"0": fixed_status[0], "1": fixed_status[1]}
            block["multiplicity_layers"] = layers
            del block["box_records"]
            blocks.append(block)
            print(f"[CHECKPOINT] K269 count {middle_count} {block_name} {block['boxes']} boxes", flush=True)
        stratum_boxes = [
            b for block in blocks for layer in block["multiplicity_layers"]
            for b in layer["box_records"]
        ]
        stratum = summarize(stratum_boxes, norm_lo, norm_hi)
        stratum["middle_axis_count"] = middle_count
        stratum["fixed_axis_blocks"] = blocks
        del stratum["box_records"]
        count_strata.append(stratum)

    all_boxes = [
        b for stratum in count_strata for block in stratum["fixed_axis_blocks"]
        for layer in block["multiplicity_layers"] for b in layer["box_records"]
    ]
    complete = summarize(all_boxes, norm_lo, norm_hi)
    del complete["box_records"]
    assert [s["boxes"] for s in count_strata] == [620, 225, 42, 3]
    assert complete["boxes"] == 890
    assert arb(complete["normalized_integral_interval"]["lower"]) > as_arb(POSITIVE_LOWER)

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            p.stem.split("-")[0]: sha256(p.read_bytes()).hexdigest()
            for p in (K185, K218, K230, K247, K265, K266, K267, K268)
        },
        "object": "The exact K218 signed integral on the complete remaining exchangeable-axis middle collar",
        "domain": {
            "middle_axis_counts": list(MIDDLE_COUNTS),
            "exchangeable_axes": list(range(2, 8)),
            "middle_q_interval": list(map(str, BOUNDS["middle"])),
            "low_q_interval": list(map(str, BOUNDS["low"])),
            "high_q_interval": list(map(str, BOUNDS["high"])),
            "boxes": 890,
            "boxes_by_middle_axis_count": [620, 225, 42, 3],
            "pairwise_disjoint": True,
            "disjoint_from_k247_k265_k266_k267_k268_interiors": True,
            "s6_invariant_by_complete_box_enumeration": True,
        },
        "projection": {
            "raw_signed_terms": len(items),
            "retained_exact_s6_orbits": len(groups),
            "orbit_manifest_sha256": orbit_digest,
            "rule": "Every box is enumerated; K230 symmetry is used only after complete-union integration.",
        },
        "expansion": {
            "total_degree_inclusive": ORDER,
            "tail_starts_at_degree": ORDER + 1,
            "compiler": "exact FLINT fmpq multivariate polynomial recurrence",
            "integration": "signed head against exact product-cosh centered moments",
            "tail": "complete-homogeneous geometric majorant per orbit and box",
        },
        "middle_count_strata": count_strata,
        "complete_collar": complete,
        "certificate": {
            "normalization_lower_using_pi_less_than_22_over_7": str(norm_lo),
            "normalization_upper_using_pi_greater_than_31_over_10": str(norm_hi),
            "declared_strict_positive_mass_lower": {
                "numerator": POSITIVE_LOWER.numerator,
                "denominator": POSITIVE_LOWER.denominator,
            },
            "result": "strictly_positive_complete_890_box_three_plus_exchangeable_axis_middle_collar",
        },
        "controls": "Independent reverse-order recompilation, moments, tails, normalization, q2/q3, absolute-weight, wrong-measure and dominant-stratum deletion controls.",
        "source_routing": "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS.",
        "decision": "The complete remaining adjacent exchangeable-middle collar is strictly positive after signed composition.",
        "claim_ceiling": "Exact positivity only on the declared 890-box collar; no full K218, complete error, K215, source, ledger, canon, paper, public-posture, or physical conclusion.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K269", result["certificate"]["result"])
    print("[PASS] K269 interval", result["complete_collar"]["normalized_integral_interval"])
