#!/usr/bin/env python3
"""Execute K511 shards 065--072 through the certified K520/K508 backend."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k521-order-ten-face-shards-065-072.json"
K511_JSON = ROOT / "lab/process/k511-order-ten-face-shard-plan.json"
SHARD_START = 65
SHARD_STOP = 73


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K520 = load("k520_for_k521", "k520_order_ten_face_shards_057_064.py")
K520.K519.K518.K517.K516.K515.K514.SHARD_START = SHARD_START
K520.K519.K518.K517.K516.K515.K514.SHARD_STOP = SHARD_STOP


def build() -> dict:
    payload = K520.build()
    payload["result_id"] = "K521-ORDER-TEN-FACE-SHARDS-065-072"
    payload["created"] = "2026-09-26"
    payload["decision"] = {
        "shards_065_through_072_released": True,
        "cumulative_K511_shards_executed_including_K512": 73,
        "cumulative_remaining_face_programs_executed": 292,
        "unexecuted_remaining_face_programs": 624,
        "all_916_remaining_faces_executed": False,
        "full_projective_normal_cone_complete": False,
        "recursive_positive_interior_cover_complete": False,
        "analytic_radial_tails_complete": False,
        "complete_hybrid_integrals_emitted": False,
        "next_exact_input": (
            "Continue K511 at shard 073 under serialized resource control, then "
            "construct the normal-projective partition before interior and tail composition."
        ),
    }
    payload["claim_ceiling"] = (
        "Rigorous 180-digit K508-backend evidence for the 32 exact programs in "
        "K511 shards 065 through 072, across 224 positive-width normal cells. "
        "Together with K512--K520 this completes 292 of the 916 K508-omitted "
        "programs. It is not the other 624 programs, a complete face bank, "
        "projective/interior/tail cover, hybrid integral, K457 value, K152 "
        "interval, or source/physical result."
    )
    return payload


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
        raise AssertionError("K521 fixed census changed")
    required = (
        "expected_program_ids_match_exactly",
        "all_32_programs_executed",
        "all_224_cells_finite",
        "every_cell_has_positive_argument_floor",
        "all_32_direct_overlaps_pass",
    )
    if not all(bank[key] for key in required):
        raise AssertionError("K521 backend evidence failed")
    k511 = json.loads(K511_JSON.read_text())
    expected_shards = k511["shards"][SHARD_START:SHARD_STOP]
    expected_program_ids = [
        program_id for shard in expected_shards for program_id in shard["program_ids"]
    ]
    actual_program_ids = [row["program_id"] for row in rows]
    if actual_program_ids != expected_program_ids:
        raise AssertionError("K521 stored program identity changed")
    if bank["bank_sha256"] != K520.K519.K518.K517.K516.K515.K514.K508.digest(rows):
        raise AssertionError("K521 stored bank digest changed")
    stored_uses = sum(
        cell["divided_difference_operation_uses"]
        for row in rows
        for cell in row["cells"]
    )
    if bank["divided_difference_operation_uses"] != stored_uses:
        raise AssertionError("K521 operation census changed")
    direct_ids = [row["program_id"] for row in payload["direct_overlap_controls"]]
    if direct_ids != expected_program_ids:
        raise AssertionError("K521 direct-control identity changed")
    for stored, expected_shard in zip(
        payload["measurement"]["per_shard"], expected_shards, strict=True
    ):
        if (
            stored["shard_id"] != expected_shard["shard_id"]
            or stored["program_digest"] != expected_shard["program_digest"]
        ):
            raise AssertionError("K521 stored shard provenance changed")
        shard_rows = [row for row in rows if row["shard_id"] == stored["shard_id"]]
        if stored["program_rows_sha256"] != K520.K519.K518.K517.K516.K515.K514.K508.digest(shard_rows):
            raise AssertionError("K521 stored shard digest changed")
    if not decision["shards_065_through_072_released"]:
        raise AssertionError("K521 release boundary changed")
    if decision["cumulative_remaining_face_programs_executed"] != 292:
        raise AssertionError("K521 cumulative census changed")
    if decision["unexecuted_remaining_face_programs"] != 624:
        raise AssertionError("K521 remainder census changed")
    forbidden = (
        "all_916_remaining_faces_executed",
        "full_projective_normal_cone_complete",
        "recursive_positive_interior_cover_complete",
        "analytic_radial_tails_complete",
        "complete_hybrid_integrals_emitted",
    )
    if any(decision[key] for key in forbidden):
        raise AssertionError("K521 overclaimed the order-ten cover")
    if payload["source_and_ledger_effect"] != "none":
        raise AssertionError("K521 moved source or ledger state")
    if not all(
        math.isfinite(float(cell["complete_second_derivative_abs_upper"]))
        for row in rows
        for cell in row["cells"]
    ):
        raise AssertionError("K521 stored nonfinite cell")


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
