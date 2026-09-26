#!/usr/bin/env python3
"""Execute K511 shards 017--024 through the certified K514/K508 backend."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k515-order-ten-face-shards-017-024.json"
K511_JSON = ROOT / "lab/process/k511-order-ten-face-shard-plan.json"
SHARD_START = 17
SHARD_STOP = 25


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K514 = load("k514_for_k515", "k514_order_ten_face_shards_009_016.py")
K514.SHARD_START = SHARD_START
K514.SHARD_STOP = SHARD_STOP


def build() -> dict:
    payload = K514.build()
    payload["result_id"] = "K515-ORDER-TEN-FACE-SHARDS-017-024"
    payload["decision"] = {
        "shards_017_through_024_released": True,
        "cumulative_K511_shards_executed_including_K512": 25,
        "cumulative_remaining_face_programs_executed": 100,
        "unexecuted_remaining_face_programs": 816,
        "all_916_remaining_faces_executed": False,
        "full_projective_normal_cone_complete": False,
        "recursive_positive_interior_cover_complete": False,
        "analytic_radial_tails_complete": False,
        "complete_hybrid_integrals_emitted": False,
        "next_exact_input": (
            "Continue K511 at shard 025 under serialized resource control, then "
            "construct the normal-projective partition before interior and tail composition."
        ),
    }
    payload["claim_ceiling"] = (
        "Rigorous 180-digit K508-backend evidence for the 32 exact programs in "
        "K511 shards 017 through 024, across 224 positive-width normal cells. "
        "Together with K512--K514 this completes 100 of the 916 K508-omitted "
        "programs. It is not the other 816 programs, a complete face bank, "
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
        raise AssertionError("K515 fixed census changed")
    required = (
        "expected_program_ids_match_exactly",
        "all_32_programs_executed",
        "all_224_cells_finite",
        "every_cell_has_positive_argument_floor",
        "all_32_direct_overlaps_pass",
    )
    if not all(bank[key] for key in required):
        raise AssertionError("K515 backend evidence failed")
    k511 = json.loads(K511_JSON.read_text())
    expected_shards = k511["shards"][SHARD_START:SHARD_STOP]
    expected_program_ids = [
        program_id for shard in expected_shards for program_id in shard["program_ids"]
    ]
    actual_program_ids = [row["program_id"] for row in rows]
    if actual_program_ids != expected_program_ids:
        raise AssertionError("K515 stored program identity changed")
    if bank["bank_sha256"] != K514.K508.digest(rows):
        raise AssertionError("K515 stored bank digest changed")
    stored_uses = sum(
        cell["divided_difference_operation_uses"]
        for row in rows
        for cell in row["cells"]
    )
    if bank["divided_difference_operation_uses"] != stored_uses:
        raise AssertionError("K515 operation census changed")
    direct_ids = [row["program_id"] for row in payload["direct_overlap_controls"]]
    if direct_ids != expected_program_ids:
        raise AssertionError("K515 direct-control identity changed")
    for stored, expected_shard in zip(
        payload["measurement"]["per_shard"], expected_shards, strict=True
    ):
        if (
            stored["shard_id"] != expected_shard["shard_id"]
            or stored["program_digest"] != expected_shard["program_digest"]
        ):
            raise AssertionError("K515 stored shard provenance changed")
        shard_rows = [row for row in rows if row["shard_id"] == stored["shard_id"]]
        if stored["program_rows_sha256"] != K514.K508.digest(shard_rows):
            raise AssertionError("K515 stored shard digest changed")
    if not decision["shards_017_through_024_released"]:
        raise AssertionError("K515 release boundary changed")
    if decision["cumulative_remaining_face_programs_executed"] != 100:
        raise AssertionError("K515 cumulative census changed")
    if decision["unexecuted_remaining_face_programs"] != 816:
        raise AssertionError("K515 remainder census changed")
    forbidden = (
        "all_916_remaining_faces_executed",
        "full_projective_normal_cone_complete",
        "recursive_positive_interior_cover_complete",
        "analytic_radial_tails_complete",
        "complete_hybrid_integrals_emitted",
    )
    if any(decision[key] for key in forbidden):
        raise AssertionError("K515 overclaimed the order-ten cover")
    if payload["source_and_ledger_effect"] != "none":
        raise AssertionError("K515 moved source or ledger state")
    if not all(
        math.isfinite(float(cell["complete_second_derivative_abs_upper"]))
        for row in rows
        for cell in row["cells"]
    ):
        raise AssertionError("K515 stored nonfinite cell")


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
