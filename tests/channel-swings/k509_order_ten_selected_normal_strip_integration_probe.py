#!/usr/bin/env python3
"""Probe and hostile self-test for stored K509 selected strips."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k509-order-ten-selected-normal-strip-integration.json"
spec = importlib.util.spec_from_file_location("k509_probe_target", HERE / "k509_order_ten_selected_normal_strip_integration.py")
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K509")
K509 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K509)


def checks(payload):
    f = payload["fixed_control"]
    s = payload["strip_summary"]
    d = payload["decision"]
    return [
        payload["result_id"] == "K509-ORDER-TEN-SELECTED-NORMAL-STRIP-INTEGRATION",
        f["selected_reachable_face_programs"] == 20,
        f["integrated_selected_face_cells"] == 140,
        f["exact_partition_width"] == "3/4096",
        s["all_20_selected_face_strips_integrated"] is True,
        s["all_140_cell_contributions_finite_positive"] is True,
        s["minimum_selected_K486_normal_power"] >= 0,
        s["selected_hybrids_without_reachable_faces"] == ["v10", "v11"],
        d["all_selected_equal_normal_near_face_strips_integrated"] is True,
        d["remaining_916_faces_integrated"] is False,
        d["full_projective_normal_cone_complete"] is False,
        d["complete_hybrid_integrals_emitted"] is False,
        payload["release_test"]["native_K152_interval_not_emitted"] is True,
    ]


def selftest(payload):
    mutations = [
        lambda p: p["fixed_control"].__setitem__("integrated_selected_face_cells", 139),
        lambda p: p["selected_face_strip_bank"].pop(),
        lambda p: p["decision"].__setitem__("all_selected_equal_normal_near_face_strips_integrated", False),
        lambda p: p["decision"].__setitem__("remaining_916_faces_integrated", True),
        lambda p: p["decision"].__setitem__("full_projective_normal_cone_complete", True),
        lambda p: p["decision"].__setitem__("recursive_positive_interior_cover_complete", True),
        lambda p: p["decision"].__setitem__("analytic_radial_tails_complete", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K509.validate_payload(hostile)
        except AssertionError:
            rejected += 1
    return rejected, len(mutations)


def main() -> int:
    payload = json.loads(OUTPUT.read_text())
    controls = checks(payload)
    rejected, total = selftest(payload)
    print(f"K509 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{total}")
    return 0 if all(controls) and rejected == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
