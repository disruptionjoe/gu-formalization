#!/usr/bin/env python3
"""Recursive exact-cover y-master subdivision for the K333 global bank.

The finite radial strip ``0 <= r <= 1`` is partitioned by the three K333
projective charts and the six positive gap cells.  Every leaf recomputes the
complete shared-entry determinant enclosure.  A leaf is recursively split on
all eight finite axes whenever any of its three integrated coefficients
exceeds the declared contribution tolerance.  The analytic ``r >= 1`` tails
remain separate proved leaves.  Exact rational box volumes and projective tail
widths provide a coverage checksum independent of floating-point arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K312_MODULE = HERE / "k312_order_seven_positive_cell_measure_backend.py"
K314_MODULE = HERE / "k314_order_seven_projective_face_oracle.py"
K326_MODULE = HERE / "k326_order_seven_signed_entry_jet_chart_bank.py"
K328_MODULE = HERE / "k328_order_seven_scaled_derivative_envelope_bank.py"
K329_MODULE = HERE / "k329_order_seven_degree27_origin_evaluator.py"
K332_MODULE = HERE / "k332_order_seven_projective_face_evaluator.py"
K327 = ROOT / "lab/process/k327-order-seven-adaptive-interior-subdivision.json"
K330 = ROOT / "lab/process/k330-order-seven-radial-tail-control.json"
K333 = ROOT / "lab/process/k333-order-seven-projective-face-radial-closure.json"
OUTPUT = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"

ctx.dps = 180
ctx.threads = 1

RADIAL_CELLS = ((Fraction(0), Fraction(1, 16)), (Fraction(1, 16), Fraction(1)))
PROJECTIVE_CELLS = (
    ("s0", (Fraction(0), Fraction(1, 4))),
    ("interior", (Fraction(1, 4), Fraction(3, 4))),
    ("s1", (Fraction(3, 4), Fraction(1))),
)
GAPS = tuple((Fraction(1, 8), Fraction(5, 24)) for _ in range(6))
RELATIVE_LEAF_TOLERANCE = Fraction(1, 16)
MAXIMUM_RECURSION_DEPTH = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def upper(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def bisect(interval: tuple[Fraction, Fraction]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    midpoint = (interval[0] + interval[1]) / 2
    return (interval[0], midpoint), (midpoint, interval[1])


def geometric_volume(
    radial: tuple[Fraction, Fraction],
    projective: tuple[Fraction, Fraction],
    gaps: tuple[tuple[Fraction, Fraction], ...],
) -> Fraction:
    result = (radial[1] - radial[0]) * (projective[1] - projective[0])
    for left, right in gaps:
        result *= right - left
    return result


def finite_cell_bound(
    modules: dict[str, Any],
    region: str,
    radial: tuple[Fraction, Fraction],
    projective: tuple[Fraction, Fraction],
    gaps: tuple[tuple[Fraction, Fraction], ...],
) -> list[arb]:
    k312 = modules["k312"]
    k314 = modules["k314"]
    k326 = modules["k326"]
    k328 = modules["k328"]
    gap_list = list(gaps)
    projective_polynomial = k314.projective_polynomial_upper(
        {name: interval for name, interval in zip(k314.GAPS, gap_list, strict=True)}
    )
    gap_volume = math.prod((right - left for left, right in gaps), start=Fraction(1))
    radial_mass = k312.radial_finite_upper(radial[0], radial[1], 6)

    if region == "interior":
        k329 = modules["k329"]
        saved = k329.RADIUS, k329.S, k329.GAPS
        try:
            k329.RADIUS = (Fraction(0), radial[1])
            k329.S = projective
            k329.GAPS = gap_list
            jets, _, d4 = k329.normalized_entry_jets(k326, k328)
        finally:
            k329.RADIUS, k329.S, k329.GAPS = saved
        b5 = k326.determinant_taylor(jets)
        scalar = Fraction(4, 120) * (radial[1] * projective[1]) ** 2 * Fraction(1, 16) * projective_polynomial
        coefficients = [arb(16) * d4 * value * arb(q(scalar)) for value in b5]
        projective_masses = [k312.polynomial_cell_moment(projective[0], projective[1], 3, 29)] * 3
    elif region in ("s0", "s1"):
        k332 = modules["k332"]
        d4, _ = k332.d4_bound(k328, radial[1], region, projective, gap_list)
        b5, _ = k332.b5_jets(k326, k328, radial[1], region, projective, gap_list)
        scalar = Fraction(4, 120) * radial[1] ** 2 * projective[1] ** 2 * Fraction(1, 16) * projective_polynomial
        coefficients = [arb(16) * d4 * value * arb(q(scalar)) for value in b5]
        reduced = [1, 1, 1] if region == "s0" else [26, 25, 24]
        projective_masses = [
            k312.polynomial_cell_moment(projective[0], projective[1], power, 29)
            if region == "s0"
            else k312.polynomial_cell_moment(projective[0], projective[1], 3, power)
            for power in reduced
        ]
    else:
        raise AssertionError("unknown projective region")

    result = [
        coefficients[order] * arb(q(radial_mass * projective_masses[order] * gap_volume))
        for order in range(3)
    ]
    if any(not math.isfinite(float(value.upper())) or value.upper() <= 0 for value in result):
        raise AssertionError("finite cell did not produce three finite positive bounds")
    return result


def split_cell(cell: dict[str, Any]) -> list[dict[str, Any]]:
    splits = [bisect(cell["radial"]), bisect(cell["projective"])]
    splits.extend(bisect(interval) for interval in cell["gaps"])
    children = []
    for bits in itertools.product((0, 1), repeat=8):
        children.append({
            "region": cell["region"],
            "radial": splits[0][bits[0]],
            "projective": splits[1][bits[1]],
            "gaps": tuple(splits[index + 2][bits[index + 2]] for index in range(6)),
            "depth": cell["depth"] + 1,
            "path": f'{cell["path"]}/{"".join(str(bit) for bit in bits)}',
        })
    return children


def row(cell: dict[str, Any], bounds: list[arb]) -> dict[str, Any]:
    return {
        "path": cell["path"],
        "region": cell["region"],
        "depth": cell["depth"],
        "exact_geometric_volume": q(geometric_volume(cell["radial"], cell["projective"], cell["gaps"])),
        "integrated_value_first_second_abs_uppers": [upper(value) for value in bounds],
    }


def checksum(rows: list[dict[str, Any]]) -> str:
    payload = [
        {
            "path": item["path"],
            "volume": item["exact_geometric_volume"],
        }
        for item in rows
    ]
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def stored_row_volume(item: dict[str, Any]) -> Fraction:
    root, *suffix = item["path"].split("/")
    region, radial_text = root.rsplit("-r", 1)
    radial = RADIAL_CELLS[int(radial_text)]
    projective = dict(PROJECTIVE_CELLS)[region]
    gaps = GAPS
    if suffix:
        if len(suffix) != 1 or len(suffix[0]) != 8 or set(suffix[0]) - {"0", "1"}:
            raise AssertionError("invalid recursive leaf path")
        bits = [int(bit) for bit in suffix[0]]
        radial = bisect(radial)[bits[0]]
        projective = bisect(projective)[bits[1]]
        gaps = tuple(bisect(interval)[bits[index + 2]] for index, interval in enumerate(gaps))
    if item["depth"] != len(suffix) or item["region"] != region:
        raise AssertionError("leaf path metadata changed")
    return geometric_volume(radial, projective, gaps)


def build() -> dict[str, Any]:
    modules = {
        "k312": load_module(K312_MODULE, "k334_k312_backend"),
        "k314": load_module(K314_MODULE, "k334_k314_backend"),
        "k326": load_module(K326_MODULE, "k334_k326_backend"),
        "k328": load_module(K328_MODULE, "k334_k328_backend"),
        "k329": load_module(K329_MODULE, "k334_k329_backend"),
        "k332": load_module(K332_MODULE, "k334_k332_backend"),
    }
    k327 = json.loads(K327.read_text())
    k330 = json.loads(K330.read_text())
    k333 = json.loads(K333.read_text())
    if not k327["decision"]["first_exact_cover_adaptive_interior_oracle_implemented"]:
        raise AssertionError("K327 exact-cover oracle unavailable")
    if not k333["decision"]["complete_three_cell_projective_partition_finite"]:
        raise AssertionError("K333 boundary bank unavailable")

    coarse_total = [arb(value) for value in k333["complete_projective_partition_value_first_second_abs_uppers"]]
    tolerances = [value * arb(q(RELATIVE_LEAF_TOLERANCE)) for value in coarse_total]
    queue = [
        {
            "region": region,
            "radial": radial,
            "projective": projective,
            "gaps": GAPS,
            "depth": 0,
            "path": f"{region}-r{radial_index}",
        }
        for radial_index, radial in enumerate(RADIAL_CELLS)
        for region, projective in PROJECTIVE_CELLS
    ]
    leaves: list[dict[str, Any]] = []
    split_records: list[dict[str, Any]] = []
    while queue:
        cell = queue.pop(0)
        bounds = finite_cell_bound(modules, cell["region"], cell["radial"], cell["projective"], cell["gaps"])
        exceeds = [bounds[order].upper() > tolerances[order].upper() for order in range(3)]
        if any(exceeds) and cell["depth"] < MAXIMUM_RECURSION_DEPTH:
            children = split_cell(cell)
            child_bounds = [
                finite_cell_bound(modules, child["region"], child["radial"], child["projective"], child["gaps"])
                for child in children
            ]
            child_sums = [sum((values[order] for values in child_bounds), arb(0)) for order in range(3)]
            nonincreasing = [child_sums[order].upper() <= bounds[order].upper() for order in range(3)]
            if not all(nonincreasing):
                raise AssertionError(f"recursive split increased a bound on {cell['path']}")
            split_records.append({
                "path": cell["path"],
                "parent_uppers": [upper(value) for value in bounds],
                "child_sum_uppers": [upper(value) for value in child_sums],
                "nonincreasing_by_order": nonincreasing,
            })
            for child, child_bound in zip(children, child_bounds, strict=True):
                child["cached_bounds"] = child_bound
                queue.append(child)
            continue
        leaves.append(row(cell, bounds))

    # The queue caches child bounds only to make the split proof explicit; the
    # accepted leaf evaluator is replayed above on every dequeued child.
    finite_totals = [
        sum((arb(item["integrated_value_first_second_abs_uppers"][order]) for item in leaves), arb(0))
        for order in range(3)
    ]
    interior_tail = [arb(value) for value in k330["exponential_tail"]["integrated_value_first_second_abs_uppers"]]
    face_tails = {
        item["face"]: [arb(value) for value in item["tail_integrated_value_first_second_abs_uppers"]]
        for item in k333["face_radial_closure"]
    }
    tail_rows = [
        {"region": "s0", "projective": ["0", "1/4"], "integrated_value_first_second_abs_uppers": [upper(value) for value in face_tails["s0"]]},
        {"region": "interior", "projective": ["1/4", "3/4"], "integrated_value_first_second_abs_uppers": [upper(value) for value in interior_tail]},
        {"region": "s1", "projective": ["3/4", "1"], "integrated_value_first_second_abs_uppers": [upper(value) for value in face_tails["s1"]]},
    ]
    tail_totals = [
        sum((arb(item["integrated_value_first_second_abs_uppers"][order]) for item in tail_rows), arb(0))
        for order in range(3)
    ]
    complete = [finite_totals[order] + tail_totals[order] for order in range(3)]
    gap_volume = math.prod((right - left for left, right in GAPS), start=Fraction(1))
    finite_volume_sum = sum((Fraction(item["exact_geometric_volume"]) for item in leaves), Fraction(0))
    tolerance_pass = all(
        arb(item["integrated_value_first_second_abs_uppers"][order]).upper() <= tolerances[order].upper()
        for item in leaves for order in range(3)
    ) and all(
        arb(item["integrated_value_first_second_abs_uppers"][order]).upper() <= tolerances[order].upper()
        for item in tail_rows for order in range(3)
    )
    exact_cover = finite_volume_sum == gap_volume
    if not exact_cover:
        raise AssertionError("finite recursive leaves do not exactly cover [0,1]^2 times the gap cube")

    return {
        "schema_version": "1.0",
        "result_id": "K334-ORDER-SEVEN-RECURSIVE-GLOBAL-SUBDIVISION",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k327-order-seven-adaptive-interior-subdivision.json",
                "lab/process/k330-order-seven-radial-tail-control.json",
                "lab/process/k333-order-seven-projective-face-radial-closure.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "finite_axes": ["r", "s", "p0", "p1", "p2", "p3", "p4", "p5"],
            "radial_partition": [[q(a), q(b)] for a, b in RADIAL_CELLS] + [["1", "infinity"]],
            "projective_partition": [[q(a), q(b)] for _, (a, b) in PROJECTIVE_CELLS],
            "relative_leaf_contribution_tolerance": q(RELATIVE_LEAF_TOLERANCE),
            "absolute_value_first_second_tolerances": [upper(value) for value in tolerances],
            "maximum_recursion_depth": MAXIMUM_RECURSION_DEPTH,
        },
        "recursive_cover": {
            "finite_root_count": 6,
            "split_count": len(split_records),
            "finite_leaf_count": len(leaves),
            "analytic_tail_leaf_count": len(tail_rows),
            "finite_leaves": leaves,
            "analytic_tail_leaves": tail_rows,
            "split_records": split_records,
            "exact_finite_geometric_volume_sum": q(finite_volume_sum),
            "exact_finite_parent_volume": q(gap_volume),
            "finite_parent_volume_replayed": exact_cover,
            "tail_projective_width_sum": "1",
            "pairwise_disjoint_up_to_shared_boundaries": True,
            "coverage_checksum": checksum(leaves),
            "all_finite_leaf_bounds_recomputed": True,
            "all_splits_nonincreasing_by_order": all(all(item["nonincreasing_by_order"]) for item in split_records),
            "declared_tolerance_met": tolerance_pass,
        },
        "complete_y_master": {
            "finite_value_first_second_abs_uppers": [upper(value) for value in finite_totals],
            "analytic_tail_value_first_second_abs_uppers": [upper(value) for value in tail_totals],
            "complete_value_first_second_abs_uppers": [upper(value) for value in complete],
            "coarse_K333_to_recursive_ratios": [
                repr(float(complete[order].upper() / coarse_total[order].upper())) for order in range(3)
            ],
        },
        "decision": {
            "recursive_global_subdivision_implemented": True,
            "exact_coverage_checksum_accepted": exact_cover,
            "declared_tolerance_complete": tolerance_pass,
            "complete_y_master_constant_emitted": exact_cover and tolerance_pass,
            "five_gap_axis_transfer_released": exact_cover and tolerance_pass,
            "complete_six_axis_peano_norm_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "reuse this exact accepted subdivision with each K309 axis-native directional operator; the y value/first/second bank is not itself a gap-axis constant",
        },
        "release_test": {
            "finite_domain_exactly_covered": exact_cover,
            "tail_domain_analytically_covered": True,
            "all_leaf_uppers_finite_positive": all(
                math.isfinite(float(value)) and float(value) > 0
                for item in leaves + tail_rows
                for value in item["integrated_value_first_second_abs_uppers"]
            ),
            "all_leaf_contributions_below_declared_tolerance": tolerance_pass,
            "raw_zero_evaluation_used": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k333["ledger_effect"],
        "source_routing": k333["source_routing"],
        "claim_ceiling": "Recursive exact-cover complete y-master enclosure for the fixed K309 six-gap cell across the full radial half-line and all three projective charts. Every finite accepted leaf recomputes the shared-entry complete determinant enclosure; analytic r>=1 tails remain exact proved leaves. The rational finite-volume checksum and declared per-leaf contribution tolerance both govern release. This emits only the complete y value/first/second upper bank and subdivision geometry. The five gap-axis operators, six-axis Peano norm, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public and physical claims remain separate.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    cover = payload["recursive_cover"]
    if fixed["finite_axes"] != ["r", "s", "p0", "p1", "p2", "p3", "p4", "p5"]:
        raise AssertionError("recursive axis census changed")
    if fixed["relative_leaf_contribution_tolerance"] != "1/16" or fixed["maximum_recursion_depth"] != 1:
        raise AssertionError("declared tolerance contract changed")
    if cover["exact_finite_geometric_volume_sum"] != cover["exact_finite_parent_volume"] or not cover["finite_parent_volume_replayed"]:
        raise AssertionError("finite exact cover changed")
    if cover["tail_projective_width_sum"] != "1" or cover["analytic_tail_leaf_count"] != 3:
        raise AssertionError("analytic tail cover changed")
    if not cover["pairwise_disjoint_up_to_shared_boundaries"] or not cover["all_finite_leaf_bounds_recomputed"]:
        raise AssertionError("leaf construction contract changed")
    if not cover["all_splits_nonincreasing_by_order"] or not cover["declared_tolerance_met"]:
        raise AssertionError("recursive tolerance closure lost")
    leaves = cover["finite_leaves"]
    if cover["finite_leaf_count"] != len(leaves) or checksum(leaves) != cover["coverage_checksum"]:
        raise AssertionError("coverage checksum changed")
    if len({item["path"] for item in leaves}) != len(leaves):
        raise AssertionError("finite leaf identities are not unique")
    recomputed_volume = sum((stored_row_volume(item) for item in leaves), Fraction(0))
    if q(recomputed_volume) != cover["exact_finite_geometric_volume_sum"] or any(
        q(stored_row_volume(item)) != item["exact_geometric_volume"] for item in leaves
    ):
        raise AssertionError("stored leaf domains do not replay the exact volume")
    tail_width = sum(
        (Fraction(item["projective"][1]) - Fraction(item["projective"][0]) for item in cover["analytic_tail_leaves"]),
        Fraction(0),
    )
    if q(tail_width) != cover["tail_projective_width_sum"]:
        raise AssertionError("analytic tail projective cells do not replay the unit interval")
    if len(payload["complete_y_master"]["complete_value_first_second_abs_uppers"]) != 3:
        raise AssertionError("complete y bank changed")
    decision = payload["decision"]
    if not decision["complete_y_master_constant_emitted"] or not decision["five_gap_axis_transfer_released"]:
        raise AssertionError("accepted y release lost")
    if decision["complete_six_axis_peano_norm_emitted"] or decision["k294_gamma_join_released"]:
        raise AssertionError("downstream result overclaimed")


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
