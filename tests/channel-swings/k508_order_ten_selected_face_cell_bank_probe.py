#!/usr/bin/env python3
"""Probe and hostile self-test for the stored K508 selected cell bank."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k508-order-ten-selected-face-cell-bank.json"
spec = importlib.util.spec_from_file_location("k508_probe_target", HERE / "k508_order_ten_selected_face_cell_bank.py")
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K508")
K508 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K508)


def checks(payload):
    f = payload["fixed_control"]
    b = payload["bank_summary"]
    d = payload["decision"]
    return [
        payload["result_id"] == "K508-ORDER-TEN-SELECTED-FACE-CELL-BANK",
        f["selected_reachable_face_programs"] == 20,
        f["complete_positive_width_cells"] == 140,
        f["ordered_descriptor_cell_evaluations"] == 1_862_000,
        f["coherent_groups_per_cell"] == 28,
        b["all_20_selected_reachable_faces_executed"] is True,
        b["all_140_cells_finite"] is True,
        b["every_cell_has_positive_argument_floor"] is True,
        b["all_20_direct_overlap_controls_pass"] is True,
        d["K485_preconditioned_selected_positive_width_face_cells_released"] is True,
        d["selected_20_reachable_faces_numerically_evaluated"] is True,
        d["all_936_reachable_faces_numerically_evaluated"] is False,
        d["full_projective_normal_cone_complete"] is False,
        d["complete_hybrid_integrals_emitted"] is False,
        payload["release_test"]["native_K152_interval_not_emitted"] is True,
    ]


def selftest(payload):
    mutations = [
        lambda p: p["fixed_control"].__setitem__("complete_positive_width_cells", 139),
        lambda p: p["bank_summary"].__setitem__("all_140_cells_finite", False),
        lambda p: p["bank_summary"].__setitem__("every_cell_has_positive_argument_floor", False),
        lambda p: p["direct_overlap_controls"].pop(),
        lambda p: p["decision"].__setitem__("K485_preconditioned_selected_positive_width_face_cells_released", False),
        lambda p: p["decision"].__setitem__("all_936_reachable_faces_numerically_evaluated", True),
        lambda p: p["decision"].__setitem__("full_projective_normal_cone_complete", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K508.validate_payload(hostile)
        except AssertionError:
            rejected += 1
    return rejected, len(mutations)


def main() -> int:
    payload = json.loads(OUTPUT.read_text())
    controls = checks(payload)
    rejected, total = selftest(payload)
    print(f"K508 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{total}")
    return 0 if all(controls) and rejected == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
