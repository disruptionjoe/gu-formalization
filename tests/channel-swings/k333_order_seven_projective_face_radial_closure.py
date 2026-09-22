#!/usr/bin/env python3
"""Extend K332's face bank across the radial annulus and infinite tail."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K312_MODULE = HERE / "k312_order_seven_positive_cell_measure_backend.py"
K332_MODULE = HERE / "k332_order_seven_projective_face_evaluator.py"
K329 = ROOT / "lab/process/k329-order-seven-degree27-origin-evaluator.json"
K330 = ROOT / "lab/process/k330-order-seven-radial-tail-control.json"
K332 = ROOT / "lab/process/k332-order-seven-projective-face-evaluator.json"
OUTPUT = ROOT / "lab/process/k333-order-seven-projective-face-radial-closure.json"

ctx.dps = 180
ctx.threads = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fraction(text: str) -> Fraction:
    return Fraction(text)


def upper(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def build() -> dict[str, Any]:
    k312 = load_module(K312_MODULE, "k333_k312_backend")
    k332_module = load_module(K332_MODULE, "k333_k332_backend")
    k329 = json.loads(K329.read_text())
    k330 = json.loads(K330.read_text())
    k332 = json.loads(K332.read_text())
    if not k330["decision"]["positive_projective_interior_full_radial_half_line_complete"]:
        raise AssertionError("K330 interior half-line unavailable")
    if not k332["decision"]["both_projective_origin_face_cells_bounded"]:
        raise AssertionError("K332 face origin bank unavailable")

    reference = k332_module.face_bank(Fraction(1))
    stored_faces = {row["face"]: row for row in k332["projective_face_bank"]["faces"]}
    annulus_mass = k312.radial_finite_upper(Fraction(1, 16), Fraction(1), 6)
    gap_volume = fraction(reference["six_gap_exact_volume"])
    tail_powers = [35, 36, 37]
    faces = []
    for row in reference["faces"]:
        face = row["face"]
        coefficient = [arb(value) for value in row["sixteen_chart_preconditioned_value_first_second_abs_uppers"]]
        projective_masses = [fraction(value) for value in row["reduced_projective_masses"]]
        annulus = [
            coefficient[order] * arb(str(annulus_mass * projective_masses[order] * gap_volume))
            for order in range(3)
        ]
        tails = [
            coefficient[order] * arb(str(k312.radial_tail_upper(Fraction(1), tail_powers[order]) * projective_masses[order] * gap_volume))
            for order in range(3)
        ]
        origin = [arb(value) for value in stored_faces[face]["origin_integrated_value_first_second_abs_uppers"]]
        totals = [origin[i] + annulus[i] + tails[i] for i in range(3)]
        if any(not math.isfinite(float(value.upper())) or value.upper() <= 0 for value in totals):
            raise AssertionError(f"{face} radial closure is not finite positive")
        faces.append({
            "face": face,
            "radius_one_preconditioned_value_first_second_abs_uppers": [upper(value) for value in coefficient],
            "origin_integrated_value_first_second_abs_uppers": [upper(value) for value in origin],
            "annulus_integrated_value_first_second_abs_uppers": [upper(value) for value in annulus],
            "tail_integrated_value_first_second_abs_uppers": [upper(value) for value in tails],
            "full_radial_half_line_value_first_second_abs_uppers": [upper(value) for value in totals],
            "reduced_projective_powers": row["reduced_projective_powers"],
            "tail_powers": tail_powers,
        })

    interior = [
        arb(k329["origin_measure"]["integrated_value_first_second_abs_uppers"][order])
        + arb(k330["finite_radial_annulus"]["integrated_value_first_second_abs_uppers"][order])
        + arb(k330["exponential_tail"]["integrated_value_first_second_abs_uppers"][order])
        for order in range(3)
    ]
    complete = [
        interior[order] + sum((arb(row["full_radial_half_line_value_first_second_abs_uppers"][order]) for row in faces), arb(0))
        for order in range(3)
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K333-ORDER-SEVEN-PROJECTIVE-FACE-RADIAL-CLOSURE",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k329-order-seven-degree27-origin-evaluator.json",
                "lab/process/k330-order-seven-radial-tail-control.json",
                "lab/process/k332-order-seven-projective-face-evaluator.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "radial_partition": [["0", "1/16"], ["1/16", "1"], ["1", "infinity"]],
            "projective_partition": [["0", "1/4"], ["1/4", "3/4"], ["3/4", "1"]],
            "tail_powers_value_first_second": tail_powers,
        },
        "face_radial_closure": faces,
        "positive_projective_interior_full_radial_value_first_second_abs_uppers": [upper(value) for value in interior],
        "complete_projective_partition_value_first_second_abs_uppers": [upper(value) for value in complete],
        "growth_contract": {
            "D4_normalized_power": 16,
            "bordered_B5_value_first_second_powers": [11, 12, 13],
            "absorbed_endpoint_power": 2,
            "complete_coefficient_powers": [29, 30, 31],
            "positive_radial_measure_power": 6,
            "tail_powers": tail_powers,
            "projective_preconditioners_are_radial_degree_zero": True,
            "tail_finiteness_is_analytic_not_sampled": True,
        },
        "decision": {
            "both_projective_faces_full_radial_half_line_complete": True,
            "complete_three_cell_projective_partition_finite": True,
            "recursive_tolerance_complete": False,
            "complete_y_master_constant_emitted": False,
            "next_exact_input": "turn the K327 exact-cover interior oracle and K333 complete radial/projective boundary bank into one recursive global subdivision with a declared tolerance and an exact coverage checksum; only that accepted sum may be reused on the five gap axes",
        },
        "release_test": {
            "two_faces_closed": [row["face"] for row in faces] == ["s0", "s1"],
            "all_face_tail_uppers_finite_positive": all(
                math.isfinite(float(value)) and float(value) > 0
                for row in faces for value in row["tail_integrated_value_first_second_abs_uppers"]
            ),
            "all_complete_partition_uppers_finite_positive": all(math.isfinite(float(value.upper())) and value.upper() > 0 for value in complete),
            "tail_powers_exactly_35_36_37": tail_powers == [35, 36, 37],
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k332["ledger_effect"],
        "source_routing": k332["source_routing"],
        "claim_ceiling": "Finite analytic radial-annulus and exponential-tail bounds on both preconditioned projective face cells. Together with K329/K330, the three projective cells [0,1/4], [1/4,3/4], [3/4,1] now cover the full radial half-line for the fixed six-gap cell and all sixteen endpoint charts. Projective preconditioning changes no radial degree, so K330's exact tail powers 35/36/37 remain valid. Recursive global subdivision and its declared tolerance remain open; therefore no complete y-master constant, five-gap transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is released.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["radial_partition"] != [["0", "1/16"], ["1/16", "1"], ["1", "infinity"]]:
        raise AssertionError("radial partition changed")
    if fixed["projective_partition"] != [["0", "1/4"], ["1/4", "3/4"], ["3/4", "1"]]:
        raise AssertionError("projective partition changed")
    if fixed["tail_powers_value_first_second"] != [35, 36, 37]:
        raise AssertionError("tail powers changed")
    if [row["face"] for row in payload["face_radial_closure"]] != ["s0", "s1"]:
        raise AssertionError("face closure changed")
    growth = payload["growth_contract"]
    if not growth["projective_preconditioners_are_radial_degree_zero"] or not growth["tail_finiteness_is_analytic_not_sampled"]:
        raise AssertionError("radial growth transfer invalid")
    decision = payload["decision"]
    if not decision["both_projective_faces_full_radial_half_line_complete"] or not decision["complete_three_cell_projective_partition_finite"]:
        raise AssertionError("radial/projective closure not released")
    if decision["complete_y_master_constant_emitted"]:
        raise AssertionError("complete numerical release overclaimed")


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
