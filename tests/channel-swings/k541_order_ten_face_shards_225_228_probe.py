#!/usr/bin/env python3
"""Stored-result probe and hostile mutations for K541."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k541-order-ten-face-shards-225-228.json"
spec = importlib.util.spec_from_file_location(
    "k541_probe_target", HERE / "k541_order_ten_face_shards_225_228.py"
)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K541")
K541 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K541)


def checks(payload):
    fixed = payload["fixed_control"]
    bank = payload["bank_summary"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K541-ORDER-TEN-FACE-SHARDS-225-228",
        fixed["first_shard_id"] == "order10-face-225",
        fixed["last_shard_id"] == "order10-face-228",
        fixed["shard_count"] == 4,
        fixed["program_count"] == 16,
        fixed["complete_positive_width_cells"] == 112,
        fixed["ordered_descriptor_cell_evaluations"] == 1_489_600,
        fixed["coherent_groups_per_cell"] == 28,
        fixed["arb_decimal_digits"] == 180,
        fixed["threads"] == 1,
        bank["expected_program_ids_match_exactly"] is True,
        bank["all_16_programs_executed"] is True,
        bank["all_112_cells_finite"] is True,
        bank["every_cell_has_positive_argument_floor"] is True,
        bank["all_16_direct_overlaps_pass"] is True,
        bank["bank_sha256"]
        == K541.K540.K539.K538.K537.K536.K535.K534.K533.K532.K531.K530.K529.K528.K527.K526.K525.K524.K523.K522.K521.K520.K519.K518.K517.K516.K515.K514.K508.digest(payload["face_cell_bank"]),
        bank["divided_difference_operation_uses"]
        == sum(
            cell["divided_difference_operation_uses"]
            for row in payload["face_cell_bank"]
            for cell in row["cells"]
        ),
        decision["cumulative_remaining_face_programs_executed"] == 916,
        decision["unexecuted_remaining_face_programs"] == 0,
        decision["all_916_remaining_faces_executed"] is True,
        decision["complete_K508_plus_K511_reachable_face_program_bank"] is True,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = json.loads(OUTPUT.read_text())
    controls = checks(payload)
    mutations = [
        lambda row: row["fixed_control"].__setitem__("program_count", 15),
        lambda row: row["fixed_control"].__setitem__("threads", 2),
        lambda row: row["bank_summary"].__setitem__("expected_program_ids_match_exactly", False),
        lambda row: row["bank_summary"].__setitem__("all_112_cells_finite", False),
        lambda row: row["bank_summary"].__setitem__("every_cell_has_positive_argument_floor", False),
        lambda row: row["bank_summary"].__setitem__("all_16_direct_overlaps_pass", False),
        lambda row: row["bank_summary"].__setitem__("bank_sha256", "sha256:0"),
        lambda row: row["bank_summary"].__setitem__("divided_difference_operation_uses", 0),
        lambda row: row["decision"].__setitem__("unexecuted_remaining_face_programs", 1),
        lambda row: row["decision"].__setitem__("all_916_remaining_faces_executed", False),
        lambda row: row["decision"].__setitem__("full_projective_normal_cone_complete", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K541.validate(hostile)
        except AssertionError:
            rejected += 1
    print(
        f"K541 controls: {sum(controls)}/{len(controls)}; "
        f"hostile: {rejected}/{len(mutations)}"
    )
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
