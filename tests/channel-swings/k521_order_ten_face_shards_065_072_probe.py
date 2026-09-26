#!/usr/bin/env python3
"""Stored-result probe and hostile mutations for K521."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k521-order-ten-face-shards-065-072.json"
spec = importlib.util.spec_from_file_location(
    "k521_probe_target", HERE / "k521_order_ten_face_shards_065_072.py"
)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K521")
K521 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K521)


def checks(payload):
    fixed = payload["fixed_control"]
    bank = payload["bank_summary"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K521-ORDER-TEN-FACE-SHARDS-065-072",
        fixed["first_shard_id"] == "order10-face-065",
        fixed["last_shard_id"] == "order10-face-072",
        fixed["shard_count"] == 8,
        fixed["program_count"] == 32,
        fixed["complete_positive_width_cells"] == 224,
        fixed["ordered_descriptor_cell_evaluations"] == 2_979_200,
        fixed["coherent_groups_per_cell"] == 28,
        fixed["arb_decimal_digits"] == 180,
        fixed["threads"] == 1,
        bank["expected_program_ids_match_exactly"] is True,
        bank["all_32_programs_executed"] is True,
        bank["all_224_cells_finite"] is True,
        bank["every_cell_has_positive_argument_floor"] is True,
        bank["all_32_direct_overlaps_pass"] is True,
        bank["bank_sha256"]
        == K521.K520.K519.K518.K517.K516.K515.K514.K508.digest(payload["face_cell_bank"]),
        bank["divided_difference_operation_uses"]
        == sum(
            cell["divided_difference_operation_uses"]
            for row in payload["face_cell_bank"]
            for cell in row["cells"]
        ),
        decision["cumulative_remaining_face_programs_executed"] == 292,
        decision["unexecuted_remaining_face_programs"] == 624,
        decision["all_916_remaining_faces_executed"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = json.loads(OUTPUT.read_text())
    controls = checks(payload)
    mutations = [
        lambda row: row["fixed_control"].__setitem__("program_count", 31),
        lambda row: row["fixed_control"].__setitem__("threads", 2),
        lambda row: row["bank_summary"].__setitem__("expected_program_ids_match_exactly", False),
        lambda row: row["bank_summary"].__setitem__("all_224_cells_finite", False),
        lambda row: row["bank_summary"].__setitem__("every_cell_has_positive_argument_floor", False),
        lambda row: row["bank_summary"].__setitem__("all_32_direct_overlaps_pass", False),
        lambda row: row["bank_summary"].__setitem__("bank_sha256", "sha256:0"),
        lambda row: row["bank_summary"].__setitem__("divided_difference_operation_uses", 0),
        lambda row: row["decision"].__setitem__("unexecuted_remaining_face_programs", 623),
        lambda row: row["decision"].__setitem__("all_916_remaining_faces_executed", True),
        lambda row: row["decision"].__setitem__("full_projective_normal_cone_complete", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K521.validate(hostile)
        except AssertionError:
            rejected += 1
    print(
        f"K521 controls: {sum(controls)}/{len(controls)}; "
        f"hostile: {rejected}/{len(mutations)}"
    )
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
