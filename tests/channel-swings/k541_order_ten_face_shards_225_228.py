#!/usr/bin/env python3
"""Execute final K511 shards 225--228 through the certified K540/K508 backend."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k541-order-ten-face-shards-225-228.json"
K511_JSON = ROOT / "lab/process/k511-order-ten-face-shard-plan.json"
SHARD_START = 225
SHARD_STOP = 229


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K540 = load("k540_for_k541", "k540_order_ten_face_shards_217_224.py")
K540.K539.K538.K537.K536.K535.K534.K533.K532.K531.K530.K529.K528.K527.K526.K525.K524.K523.K522.K521.K520.K519.K518.K517.K516.K515.K514.SHARD_START = SHARD_START
K540.K539.K538.K537.K536.K535.K534.K533.K532.K531.K530.K529.K528.K527.K526.K525.K524.K523.K522.K521.K520.K519.K518.K517.K516.K515.K514.SHARD_STOP = SHARD_STOP


def build() -> dict:
    payload = K540.build()
    payload["result_id"] = "K541-ORDER-TEN-FACE-SHARDS-225-228"
    payload["created"] = "2026-09-27"
    bank = payload["bank_summary"]
    bank["all_16_programs_executed"] = len(payload["face_cell_bank"]) == 16
    bank["all_112_cells_finite"] = bank.pop("all_224_cells_finite")
    bank.pop("all_32_direct_overlaps_pass")
    bank["all_16_direct_overlaps_pass"] = len(payload["direct_overlap_controls"]) == 16 and all(
        row["intervals_overlap"] for row in payload["direct_overlap_controls"]
    )
    bank.pop("all_32_programs_executed")
    payload["decision"] = {
        "shards_225_through_228_released": True,
        "cumulative_K511_shards_executed_including_K512": 229,
        "cumulative_remaining_face_programs_executed": 916,
        "unexecuted_remaining_face_programs": 0,
        "all_916_remaining_faces_executed": True,
        "complete_K508_plus_K511_reachable_face_program_bank": True,
        "full_projective_normal_cone_complete": False,
        "recursive_positive_interior_cover_complete": False,
        "analytic_radial_tails_complete": False,
        "complete_hybrid_integrals_emitted": False,
        "next_exact_input": (
            "Construct the determinant-preserving normal-projective partition over "
            "the complete K508 plus K511 reachable-face program bank before "
            "recursive positive-interior and analytic-tail composition."
        ),
    }
    payload["claim_ceiling"] = (
        "Rigorous 180-digit K508-backend evidence for the final 16 exact programs "
        "in K511 shards 225 through 228, across 112 positive-width normal cells. "
        "Together with K512--K540 this executes all 916 K508-omitted programs, "
        "and their union with K508 covers all 936 fixed reachable-face programs. "
        "It is not a projective/interior/tail cover, hybrid integral, K457 value, "
        "K152 interval, or source/physical result."
    )
    return payload


def validate(payload: dict) -> None:
    fixed = payload["fixed_control"]
    bank = payload["bank_summary"]
    decision = payload["decision"]
    rows = payload["face_cell_bank"]
    expected = (4, 16, 112, 1_489_600, 28, 180, 1)
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
        raise AssertionError("K541 fixed census changed")
    required = (
        "expected_program_ids_match_exactly",
        "all_16_programs_executed",
        "all_112_cells_finite",
        "every_cell_has_positive_argument_floor",
        "all_16_direct_overlaps_pass",
    )
    if not all(bank[key] for key in required):
        raise AssertionError("K541 backend evidence failed")
    if len(rows) != 16 or len(payload["direct_overlap_controls"]) != 16:
        raise AssertionError("K541 final-batch cardinality changed")
    k511 = json.loads(K511_JSON.read_text())
    expected_shards = k511["shards"][SHARD_START:SHARD_STOP]
    expected_program_ids = [
        program_id for shard in expected_shards for program_id in shard["program_ids"]
    ]
    actual_program_ids = [row["program_id"] for row in rows]
    if actual_program_ids != expected_program_ids:
        raise AssertionError("K541 stored program identity changed")
    digest = K540.K539.K538.K537.K536.K535.K534.K533.K532.K531.K530.K529.K528.K527.K526.K525.K524.K523.K522.K521.K520.K519.K518.K517.K516.K515.K514.K508.digest
    if bank["bank_sha256"] != digest(rows):
        raise AssertionError("K541 stored bank digest changed")
    stored_uses = sum(
        cell["divided_difference_operation_uses"]
        for row in rows
        for cell in row["cells"]
    )
    if bank["divided_difference_operation_uses"] != stored_uses:
        raise AssertionError("K541 operation census changed")
    direct_ids = [row["program_id"] for row in payload["direct_overlap_controls"]]
    if direct_ids != expected_program_ids:
        raise AssertionError("K541 direct-control identity changed")
    for stored, expected_shard in zip(
        payload["measurement"]["per_shard"], expected_shards, strict=True
    ):
        if (
            stored["shard_id"] != expected_shard["shard_id"]
            or stored["program_digest"] != expected_shard["program_digest"]
        ):
            raise AssertionError("K541 stored shard provenance changed")
        shard_rows = [row for row in rows if row["shard_id"] == stored["shard_id"]]
        if stored["program_rows_sha256"] != digest(shard_rows):
            raise AssertionError("K541 stored shard digest changed")
    if not decision["shards_225_through_228_released"]:
        raise AssertionError("K541 release boundary changed")
    if decision["cumulative_remaining_face_programs_executed"] != 916:
        raise AssertionError("K541 cumulative census changed")
    if decision["unexecuted_remaining_face_programs"] != 0:
        raise AssertionError("K541 remainder census changed")
    if not decision["all_916_remaining_faces_executed"]:
        raise AssertionError("K541 omitted-bank completion changed")
    if not decision["complete_K508_plus_K511_reachable_face_program_bank"]:
        raise AssertionError("K541 reachable-face union changed")
    forbidden = (
        "full_projective_normal_cone_complete",
        "recursive_positive_interior_cover_complete",
        "analytic_radial_tails_complete",
        "complete_hybrid_integrals_emitted",
    )
    if any(decision[key] for key in forbidden):
        raise AssertionError("K541 overclaimed beyond the fixed face program bank")
    if payload["source_and_ledger_effect"] != "none":
        raise AssertionError("K541 moved source or ledger state")
    if not all(
        math.isfinite(float(cell["complete_second_derivative_abs_upper"]))
        for row in rows
        for cell in row["cells"]
    ):
        raise AssertionError("K541 stored nonfinite cell")


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
