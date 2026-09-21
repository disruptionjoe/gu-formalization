#!/usr/bin/env python3
"""Independent replay and hostile controls for K268's second collar."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
import sys

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import ROOT
from k262_order_six_low_through_three_high_multiplicity_integral_probe import (
    K185,
    K230,
    independent_groups,
    raw_terms,
)
from k265_order_nine_complete_binary_low_high_union_probe import (
    as_arb,
    centered_moments_independent,
    center_radius,
    normalized_interval_independent,
    sinh_log,
)
from k267_order_nine_exchangeable_axis_middle_collar_probe import (
    NORMALIZATION_SERIALIZATION_SLACK,
    compile_independent,
    quadrature_box,
)
from k268_order_nine_two_exchangeable_axis_middle_collar import (
    BLOCKS,
    BOUNDS,
    ORDER,
    status_specs,
)

sys.set_int_max_str_digits(0)


RECORD = ROOT / "lab/process/k268-order-nine-two-exchangeable-axis-middle-collar.json"


def quadrature_block(groups: dict, fixed_status: tuple[str, str], order: int,
                     absolute_weights: bool = False,
                     wrong_measure: bool = False) -> float:
    total = 0.0
    for multiplicity in range(5):
        for _, _, status in status_specs(fixed_status, multiplicity):
            total += quadrature_box(
                groups, status, order, absolute_weights, wrong_measure
            )
    return total


def main() -> None:
    ctx.prec = 256
    source = json.loads(K185.read_text())
    record = json.loads(RECORD.read_text())
    items = list(raw_terms(source))
    groups = independent_groups(items)
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    digest = sha256(compact.encode()).hexdigest()
    assert len(items) == 1864 and len(groups) == 307
    assert digest == json.loads(K230.read_text())["orbit_coefficient_manifest_sha256"]
    assert digest == record["projection"]["orbit_manifest_sha256"]

    ring = fmpq_mpoly_ctx.get([f"z{axis}" for axis in range(8)])
    variables = ring.gens()
    geometry = {}
    for name, bounds in BOUNDS.items():
        center, radius = center_radius(bounds)
        geometry[name] = {
            "center": center,
            "radius": radius,
            "moments": centered_moments_independent(bounds, center, ORDER),
            "measure": sinh_log(bounds[1]) - sinh_log(bounds[0]),
        }

    block_specs = dict(BLOCKS)
    independent_head = arb(0)
    independent_tail = Q()
    for block in record["fixed_axis_blocks"]:
        fixed_status = block_specs[block["block"]]
        block_head = arb(0)
        block_tail = Q()
        for layer in block["multiplicity_layers"]:
            multiplicity = layer["high_exceptional_multiplicity"]
            expected = {
                (
                    tuple(box["middle_exceptional_axes"]),
                    tuple(box["high_exceptional_axes"]),
                ): box
                for box in layer["box_records"]
            }
            layer_head = arb(0)
            layer_tail = Q()
            specs = list(status_specs(fixed_status, multiplicity))
            for middle_axes, high_subset, status in reversed(specs):
                hashes, heads, tail = compile_independent(
                    groups, middle_axes[0], high_subset, status,
                    ring, variables, geometry,
                )
                prior = expected[(middle_axes, high_subset)]
                assert hashes == prior["coefficient_sha256_by_degree"]
                assert tail == Q(prior["raw_absolute_tail_upper"])
                for value, prior_value in zip(heads, prior["raw_head_by_degree"]):
                    assert (value - arb(prior_value)).contains(0)
                layer_head += sum(heads, arb(0))
                layer_tail += tail
            assert (layer_head - arb(layer["complete_raw_head"])).contains(0)
            assert layer_tail == Q(layer["complete_raw_absolute_tail_upper"])
            block_head += layer_head
            block_tail += layer_tail
        assert (block_head - arb(block["complete_raw_head"])).contains(0)
        assert block_tail == Q(block["complete_raw_absolute_tail_upper"])
        independent_head += block_head
        independent_tail += block_tail
        print(f"[CHECKPOINT] K268 probe {block['block']}", flush=True)

    complete = record["complete_collar"]
    assert (independent_head - arb(complete["complete_raw_head"])).contains(0)
    assert independent_tail == Q(complete["complete_raw_absolute_tail_upper"])
    independent_lower, independent_upper = normalized_interval_independent(
        independent_head, independent_tail
    )
    interval = complete["normalized_integral_interval"]
    assert abs(independent_lower - arb(interval["lower"])) < as_arb(
        NORMALIZATION_SERIALIZATION_SLACK
    )
    assert abs(independent_upper - arb(interval["upper"])) < as_arb(
        NORMALIZATION_SERIALIZATION_SLACK
    )

    q2_by_block = {
        name: quadrature_block(groups, fixed, 2) for name, fixed in BLOCKS
    }
    q3_by_block = {
        name: quadrature_block(groups, fixed, 3) for name, fixed in BLOCKS
    }
    normalization = float(2**8 * 256**6 / factorial(5)) / float(arb.pi() ** 8)
    normalized_q2 = normalization * sum(q2_by_block.values())
    normalized_q3 = normalization * sum(q3_by_block.values())
    lower = float(arb(interval["lower"]).lower())
    upper = float(arb(interval["upper"]).upper())
    assert 0 < lower < normalized_q2 < upper
    assert 0 < lower < normalized_q3 < upper
    assert abs(normalized_q3 - normalized_q2) < abs(normalized_q3) * 2e-3

    dominant_name = "fixed_high_high"
    dominant_status = block_specs[dominant_name]
    absolute_q2 = quadrature_block(
        groups, dominant_status, 2, absolute_weights=True
    )
    wrong_q2 = quadrature_block(groups, dominant_status, 2, wrong_measure=True)
    assert absolute_q2 > q2_by_block[dominant_name]
    assert wrong_q2 != q2_by_block[dominant_name]
    q3_remainder = sum(
        value for name, value in q3_by_block.items() if name != dominant_name
    )
    assert q3_remainder > 0
    assert q3_by_block[dominant_name] > 10 * q3_remainder

    declared = record["certificate"]["declared_strict_positive_mass_lower"]
    declared_lower = Q(declared["numerator"], declared["denominator"])
    assert declared_lower == Q(1, 10**16)
    assert independent_lower > as_arb(declared_lower)
    assert record["domain"]["boxes"] == 945
    assert record["domain"]["middle_axis_count"] == 2
    assert record["domain"]["disjoint_from_k247_interior"]
    assert record["domain"]["disjoint_from_k265_interior"]
    assert record["domain"]["disjoint_from_k266_interior"]
    assert record["domain"]["disjoint_from_k267_interior"]

    print("[PASS] K268 reverse orbit manifest", digest)
    print("[PASS] K268 independent 945-box polynomial, moment, tail and normalization replay")
    print("[PASS] K268 q2/q3 four-block collar quadratures inside interval")
    print("[PASS] K268 absolute-weight, wrong-measure and dominant-block deletion controls")
    print("[PASS] K268 complete collar lower bound", float(independent_lower.lower()))


if __name__ == "__main__":
    main()
