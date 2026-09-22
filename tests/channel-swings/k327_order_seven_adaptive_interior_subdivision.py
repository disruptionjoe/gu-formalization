#!/usr/bin/env python3
"""Exact-cover adaptive refinement of K326's positive interior slab.

The parent slab has two radius coordinates and six projective-gap coordinates.
Bisecting all eight axes gives 256 pairwise interior-disjoint children whose
exact rational volumes sum to the parent volume.  K326 is rerun on every child;
the integrated value/first/second upper is the sum of each child's complete
post-assembly determinant upper times that child's exact measure volume.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K326_MODULE = Path(__file__).with_name("k326_order_seven_signed_entry_jet_chart_bank.py")
K326 = ROOT / "lab/process/k326-order-seven-signed-entry-jet-chart-bank.json"
OUTPUT = ROOT / "lab/process/k327-order-seven-adaptive-interior-subdivision.json"

ctx.dps = 180
ctx.threads = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bisect(interval: tuple[Fraction, Fraction]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    lower, upper = interval
    midpoint = (lower + upper) / 2
    return (lower, midpoint), (midpoint, upper)


def volume(x, b, gaps) -> Fraction:
    result = (x[1] - x[0]) * (b[1] - b[0])
    for lower, upper in gaps:
        result *= upper - lower
    return result


def integrated_chart_sum(cell: dict[str, Any], cell_volume: Fraction) -> list[arb]:
    # Eight left plus eight right K318 charts.  Endpoint chart weights remain
    # inside K326's determinant; only the declared x,b,p cell volume is added.
    totals = []
    for order in range(3):
        left = arb(cell["endpoints"]["left"]["four_group_weighted_abs_uppers"][order])
        right = arb(cell["endpoints"]["right"]["four_group_weighted_abs_uppers"][order])
        totals.append(arb(8) * (left + right) * arb(f"{cell_volume.numerator}/{cell_volume.denominator}"))
    return totals


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(value.upper()), math.inf))


def build() -> dict[str, Any]:
    module = load_module(K326_MODULE, "k327_k326_backend")
    k308 = module.load_module(module.K308_MODULE, "k327_k308_backend")
    k314 = module.load_module(module.K314_MODULE, "k327_k314_backend")
    k326 = json.loads(K326.read_text())
    if not k326["decision"]["adaptive_positive_interior_subdivision_released"]:
        raise AssertionError("K326 did not release adaptive interior work")

    parent_x = module.DEFAULT_X
    parent_b = module.DEFAULT_B
    parent_gaps = module.DEFAULT_P
    parent_volume = volume(parent_x, parent_b, parent_gaps)
    parent_cell = module.complete_cell_bound(k308, k314, parent_x, parent_b, parent_gaps)
    parent_integrated = integrated_chart_sum(parent_cell, parent_volume)

    splits = [bisect(parent_x), bisect(parent_b), *(bisect(interval) for interval in parent_gaps)]
    refined = [arb(0), arb(0), arb(0)]
    child_volumes: list[Fraction] = []
    child_maxima = [arb(0), arb(0), arb(0)]
    child_minima: list[arb | None] = [None, None, None]
    child_rows = []
    for bits in itertools.product((0, 1), repeat=8):
        child_x = splits[0][bits[0]]
        child_b = splits[1][bits[1]]
        child_gaps = [splits[index + 2][bits[index + 2]] for index in range(6)]
        child_volume = volume(child_x, child_b, child_gaps)
        child = module.complete_cell_bound(k308, k314, child_x, child_b, child_gaps)
        integrated = integrated_chart_sum(child, child_volume)
        child_volumes.append(child_volume)
        for order, value in enumerate(integrated):
            refined[order] += value
            if value.upper() > child_maxima[order].upper():
                child_maxima[order] = value
            if child_minima[order] is None or value.upper() < child_minima[order].upper():
                child_minima[order] = value
        child_rows.append({
            "bits": "".join(str(bit) for bit in bits),
            "volume": str(child_volume),
            "integrated_value_first_second_abs_uppers": [upper_text(value) for value in integrated],
        })

    exact_cover = sum(child_volumes, Fraction(0)) == parent_volume
    contraction = [refined[order].upper() <= parent_integrated[order].upper() for order in range(3)]
    ratios = [float(refined[order].upper() / parent_integrated[order].upper()) for order in range(3)]
    if not exact_cover:
        raise AssertionError("child volumes do not exactly cover the parent")
    if not all(contraction):
        raise AssertionError("refinement increased an integrated upper")

    return {
        "schema_version": "1.0",
        "result_id": "K327-ORDER-SEVEN-ADAPTIVE-INTERIOR-SUBDIVISION",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k326-order-seven-signed-entry-jet-chart-bank.json",
            "arb_decimal_digits": 180,
            "threads": 1,
            "split_axes": ["x", "b", "p0", "p1", "p2", "p3", "p4", "p5"],
            "children": len(child_rows),
            "endpoint_charts_per_child": 16,
            "coefficient_orders": [0, 1, 2],
        },
        "parent_control": {
            "x": [str(value) for value in parent_x],
            "b": [str(value) for value in parent_b],
            "projective_gaps": [[str(value) for value in interval] for interval in parent_gaps],
            "exact_volume": str(parent_volume),
            "integrated_value_first_second_abs_uppers": [upper_text(value) for value in parent_integrated],
        },
        "refined_cover": {
            "child_count": len(child_rows),
            "children": child_rows,
            "exact_child_volume_sum": str(sum(child_volumes, Fraction(0))),
            "exact_parent_volume_replayed": exact_cover,
            "pairwise_disjoint_up_to_shared_boundaries": True,
            "integrated_value_first_second_abs_uppers": [upper_text(value) for value in refined],
            "parent_to_refined_ratios": [repr(value) for value in ratios],
            "refinement_nonincreasing_by_order": contraction,
            "minimum_child_integrated_uppers": [upper_text(value) for value in child_minima if value is not None],
            "maximum_child_integrated_uppers": [upper_text(value) for value in child_maxima],
            "entry_intervals_recomputed_per_child": True,
            "post_assembly_enclosure_reused_without_familywise_absolute_sum": True,
        },
        "scope_boundary": {
            "covered": "one exact 256-child refinement of K324's positive x,b and six-gap interior slab across all sixteen K318 endpoint charts",
            "not_covered": ["r=0 origin chart", "exponential radial tail", "s=0 face", "s=1 face", "recursive tolerance closure", "a complete y-master constant"],
            "interior_refinement_is_not_global_release": True,
        },
        "decision": {
            "first_exact_cover_adaptive_interior_oracle_implemented": True,
            "all_three_integrated_uppers_nonincreasing": all(contraction),
            "complete_origin_tail_face_sum_emitted": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "extend the accepted child evaluator to the degree-27 normalized r=0 chart, exponential tail and both projective faces, then recurse to a declared tolerance before any complete y constant",
        },
        "release_test": {
            "two_to_the_eight_children_exact": len(child_rows) == 256,
            "exact_parent_volume_replayed": exact_cover,
            "all_refined_uppers_finite_positive": all(math.isfinite(float(value.upper())) and value.upper() > 0 for value in refined),
            "all_refined_uppers_no_larger_than_parent": all(contraction),
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k326["ledger_effect"],
        "source_routing": k326["source_routing"],
        "claim_ceiling": "First exact-cover adaptive positive-interior subdivision for K326's complete signed value/first/second endpoint-chart bank. All eight x, b and projective-gap axes are bisected, the 256 exact rational child volumes replay the parent, every child's shared entry intervals are recomputed, and all three integrated complete-determinant uppers are nonincreasing. Radial origin, tail, projective faces and recursive tolerance closure remain open, so no complete y-master constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is released.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    cover = payload["refined_cover"]
    if cover["child_count"] != 256 or len(cover["children"]) != 256 or not cover["exact_parent_volume_replayed"]:
        raise AssertionError("exact cover changed")
    if len({row["bits"] for row in cover["children"]}) != 256 or any(len(row["bits"]) != 8 for row in cover["children"]):
        raise AssertionError("child identity census changed")
    if cover["exact_child_volume_sum"] != payload["parent_control"]["exact_volume"]:
        raise AssertionError("child volume sum no longer equals parent")
    if not cover["pairwise_disjoint_up_to_shared_boundaries"]:
        raise AssertionError("child disjointness hidden")
    if not all(cover["refinement_nonincreasing_by_order"]):
        raise AssertionError("adaptive contraction lost")
    if len(cover["integrated_value_first_second_abs_uppers"]) != 3 or any(
        not math.isfinite(float(value)) or float(value) <= 0
        for value in cover["integrated_value_first_second_abs_uppers"]
    ):
        raise AssertionError("refined upper bank invalid")
    if not cover["entry_intervals_recomputed_per_child"] or not cover["post_assembly_enclosure_reused_without_familywise_absolute_sum"]:
        raise AssertionError("K326 evaluator was not honestly reused")
    if not payload["scope_boundary"]["interior_refinement_is_not_global_release"]:
        raise AssertionError("interior-only scope hidden")
    if payload["decision"]["complete_y_master_constant_emitted"]:
        raise AssertionError("complete y-master overclaim")



def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
