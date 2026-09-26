#!/usr/bin/env python3
"""Execute K511 shards 001--008 through K508's true interval backend."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
import time
from collections import Counter
from pathlib import Path

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k513-order-ten-face-shards-001-008.json"
K485_JSON = ROOT / "lab/process/k485-order-ten-mask-native-preconditioner-compiler.json"
K487_JSON = ROOT / "lab/process/k487-order-ten-face-program-compiler.json"
K511_JSON = ROOT / "lab/process/k511-order-ten-face-shard-plan.json"
SHARD_START = 1
SHARD_STOP = 9

ctx.dps = 180
ctx.threads = 1


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K508 = load("k508_for_k513", "k508_order_ten_selected_face_cell_bank.py")


def execute_program(program, singular_templates, confluent_templates):
    cells = []
    singular_counts = Counter()
    confluent_counts = Counter()
    operation_uses = 0
    direct_overlap = False
    for cell_index, (left, right) in enumerate(K508.NORMAL_CELLS):
        rho = K508.BASE.interval(left, right)
        second, groups, singular, confluent, uses = K508.BASE.complete_second(
            program, rho, singular_templates, confluent_templates
        )
        if len(groups) != 28:
            raise AssertionError("K513 coherent-group census changed")
        operation_uses += uses
        if not math.isfinite(float(abs(second).upper())):
            raise AssertionError("K513 nonfinite cell")
        raw_times = K508.BASE.raw_times(program, rho)
        cumulative_s, cumulative_v = K508.K412.cumulative(raw_times)
        minimum = min(
            [value.lower() for value in cumulative_s.values()]
            + [value.lower() for value in cumulative_v.values()]
        )
        if minimum <= 0:
            raise AssertionError("K513 zero cumulative argument")
        power = int(program["maximum_value_first_second_singular_powers"][2])
        scaled = abs(second) * rho**power
        groups = [
            {**row, "group_id": str(row["group_id"]).replace("order9:", "order10:")}
            for row in groups
        ]
        cells.append(
            {
                "normal_interval": [K508.q(left), K508.q(right)],
                "minimum_cumulative_argument_lower": K508.lower_text(arb(minimum)),
                "complete_second_derivative_abs_upper": K508.abs_upper_text(second),
                "rho_to_K486_second_singular_power_abs_upper": K508.abs_upper_text(scaled),
                "coherent_group_count": len(groups),
                "all_28_group_intervals_sha256": K508.digest(groups),
                "singular_template_ids": sorted(singular),
                "confluent_template_ids": sorted(confluent),
                "divided_difference_operation_uses": uses,
            }
        )
        singular_counts.update(singular)
        confluent_counts.update(confluent)
        if cell_index == 0:
            direct, _ = K508.K412.complete_second(program["axis"], raw_times)
            direct_overlap = not (
                second.upper() < direct.lower() or second.lower() > direct.upper()
            )
            if not direct_overlap:
                raise AssertionError("K513 direct overlap failed")
    return (
        {
            "program_id": program["program_id"],
            "face_id": program["face_id"],
            "axis": program["axis"],
            "codimension": program["codimension"],
            "face_kind": program["face_kind"],
            "zeroed_axes": program["zeroed_axes"],
            "cells": cells,
        },
        direct_overlap,
        singular_counts,
        confluent_counts,
        operation_uses,
    )


def build() -> dict:
    started = time.perf_counter()
    k485 = json.loads(K485_JSON.read_text())
    k487 = json.loads(K487_JSON.read_text())
    k511 = json.loads(K511_JSON.read_text())
    selected_shards = k511["shards"][SHARD_START:SHARD_STOP]
    expected_ids = [f"order10-face-{index:03d}" for index in range(SHARD_START, SHARD_STOP)]
    if [row["shard_id"] for row in selected_shards] != expected_ids:
        raise AssertionError("K513 shard identity changed")
    if any(row["program_count"] != 4 for row in selected_shards):
        raise AssertionError("K513 shard size changed")

    programs = {row["program_id"]: row for row in k487["face_programs"]}
    singular_templates, confluent_templates = K508.BASE.template_maps(k485)
    shard_rows = []
    all_rows = []
    direct_controls = []
    singular_counts = Counter()
    confluent_counts = Counter()
    total_operation_uses = 0

    for shard in selected_shards:
        shard_started = time.perf_counter()
        rows = []
        for program_id in shard["program_ids"]:
            row, overlap, singular, confluent, uses = execute_program(
                programs[program_id], singular_templates, confluent_templates
            )
            row["shard_id"] = shard["shard_id"]
            rows.append(row)
            all_rows.append(row)
            direct_controls.append(
                {
                    "shard_id": shard["shard_id"],
                    "program_id": program_id,
                    "intervals_overlap": overlap,
                }
            )
            singular_counts.update(singular)
            confluent_counts.update(confluent)
            total_operation_uses += uses
        shard_rows.append(
            {
                "shard_id": shard["shard_id"],
                "program_digest": shard["program_digest"],
                "program_ids": shard["program_ids"],
                "program_count": len(rows),
                "cell_count": sum(len(row["cells"]) for row in rows),
                "wall_seconds_observed": round(time.perf_counter() - shard_started, 6),
                "program_rows_sha256": K508.digest(rows),
            }
        )

    wall_seconds = time.perf_counter() - started
    expected_program_ids = [program_id for shard in selected_shards for program_id in shard["program_ids"]]
    actual_program_ids = [row["program_id"] for row in all_rows]
    return {
        "schema_version": "1.0",
        "result_id": "K513-ORDER-TEN-FACE-SHARDS-001-008",
        "created": "2026-09-25",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "first_shard_id": expected_ids[0],
            "last_shard_id": expected_ids[-1],
            "K511_plan_digest": k511["partition_contract"]["plan_digest"],
            "shard_count": len(selected_shards),
            "program_count": len(all_rows),
            "cells_per_program": 7,
            "complete_positive_width_cells": sum(len(row["cells"]) for row in all_rows),
            "ordered_descriptors_per_cell": 13300,
            "ordered_descriptor_cell_evaluations": len(all_rows) * 7 * 13300,
            "coherent_groups_per_cell": 28,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "measurement": {
            "wall_seconds_observed": round(wall_seconds, 6),
            "program_seconds_observed": round(wall_seconds / len(all_rows), 6),
            "measurement_is_host_evidence_not_a_runtime_bound": True,
            "per_shard": shard_rows,
        },
        "face_cell_bank": all_rows,
        "direct_overlap_controls": direct_controls,
        "bank_summary": {
            "expected_program_ids_match_exactly": actual_program_ids == expected_program_ids,
            "all_32_programs_executed": len(all_rows) == 32,
            "all_224_cells_finite": all(
                math.isfinite(float(cell["complete_second_derivative_abs_upper"]))
                for row in all_rows
                for cell in row["cells"]
            ),
            "every_cell_has_positive_argument_floor": all(
                float(cell["minimum_cumulative_argument_lower"]) > 0
                for row in all_rows
                for cell in row["cells"]
            ),
            "all_32_direct_overlaps_pass": len(direct_controls) == 32
            and all(row["intervals_overlap"] for row in direct_controls),
            "executed_singular_template_ids": sorted(singular_counts),
            "executed_confluent_template_ids": sorted(confluent_counts),
            "divided_difference_operation_uses": total_operation_uses,
            "bank_sha256": K508.digest(all_rows),
        },
        "decision": {
            "shards_001_through_008_released": True,
            "cumulative_K511_shards_executed_including_K512": 9,
            "cumulative_remaining_face_programs_executed": 36,
            "unexecuted_remaining_face_programs": 880,
            "all_916_remaining_faces_executed": False,
            "full_projective_normal_cone_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "Continue K511 at shard 009 under serialized resource control, then construct the normal-projective partition before interior and tail composition.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Rigorous 180-digit K508-backend evidence for the 32 exact programs in K511 shards 001 through 008, across 224 positive-width normal cells. Together with K512 this completes 36 of the 916 K508-omitted programs. It is not the other 880 programs, a complete face bank, projective/interior/tail cover, hybrid integral, K457 value, K152 interval, or source/physical result.",
    }


def validate(payload: dict) -> None:
    fixed = payload["fixed_control"]
    bank = payload["bank_summary"]
    decision = payload["decision"]
    rows = payload["face_cell_bank"]
    expected = (8, 32, 224, 2_979_200, 28, 180, 1)
    actual = (
        fixed["shard_count"],
        fixed["program_count"],
        fixed["complete_positive_width_cells"],
        fixed["ordered_descriptor_cell_evaluations"],
        fixed["coherent_groups_per_cell"],
        fixed["arb_decimal_digits"],
        fixed["threads"],
    )
    if actual != expected:
        raise AssertionError("K513 fixed census changed")
    required = (
        "expected_program_ids_match_exactly",
        "all_32_programs_executed",
        "all_224_cells_finite",
        "every_cell_has_positive_argument_floor",
        "all_32_direct_overlaps_pass",
    )
    if not all(bank[key] for key in required):
        raise AssertionError("K513 backend evidence failed")
    k511 = json.loads(K511_JSON.read_text())
    expected_shards = k511["shards"][SHARD_START:SHARD_STOP]
    expected_program_ids = [
        program_id for shard in expected_shards for program_id in shard["program_ids"]
    ]
    actual_program_ids = [row["program_id"] for row in rows]
    if actual_program_ids != expected_program_ids:
        raise AssertionError("K513 stored program identity changed")
    if bank["bank_sha256"] != K508.digest(rows):
        raise AssertionError("K513 stored bank digest changed")
    stored_uses = sum(
        cell["divided_difference_operation_uses"]
        for row in rows
        for cell in row["cells"]
    )
    if bank["divided_difference_operation_uses"] != stored_uses:
        raise AssertionError("K513 operation census changed")
    direct_ids = [row["program_id"] for row in payload["direct_overlap_controls"]]
    if direct_ids != expected_program_ids:
        raise AssertionError("K513 direct-control identity changed")
    for stored, expected_shard in zip(
        payload["measurement"]["per_shard"], expected_shards, strict=True
    ):
        if (
            stored["shard_id"] != expected_shard["shard_id"]
            or stored["program_digest"] != expected_shard["program_digest"]
        ):
            raise AssertionError("K513 stored shard provenance changed")
        shard_rows = [row for row in rows if row["shard_id"] == stored["shard_id"]]
        if stored["program_rows_sha256"] != K508.digest(shard_rows):
            raise AssertionError("K513 stored shard digest changed")
    if not decision["shards_001_through_008_released"]:
        raise AssertionError("K513 release boundary changed")
    if decision["unexecuted_remaining_face_programs"] != 880:
        raise AssertionError("K513 remainder census changed")
    forbidden = (
        "all_916_remaining_faces_executed",
        "full_projective_normal_cone_complete",
        "recursive_positive_interior_cover_complete",
        "analytic_radial_tails_complete",
        "complete_hybrid_integrals_emitted",
    )
    if any(decision[key] for key in forbidden):
        raise AssertionError("K513 overclaimed the order-ten cover")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
