#!/usr/bin/env python3
"""Replay K563 and reject missing-face, overlap, and overclaim mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k563_orders_eleven_twelve_whole_radial_face_majorants.py")
STORED = ROOT / "lab/process/k563-orders-eleven-twelve-whole-radial-face-majorants.json"


def load():
    spec = importlib.util.spec_from_file_location("k563_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K563 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    faces = [face for row in stored["order_majorants"] for face in row["whole_radial_face_bank"]]
    checks = [
        module.build() == stored,
        stored["fixed_control"]["global_determinant_envelopes_loaded"] == 3540,
        stored["fixed_control"]["combined_ordered_descriptors"] == 94752,
        stored["fixed_control"]["combined_coherent_groups"] == 57,
        len(faces) == 2733,
        all(face["K561_radial_power"] >= 0 for face in faces),
        all(row["order_summary"]["all_reachable_faces_majorized"] for row in stored["order_majorants"]),
        stored["shared_majorant_contract"]["face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals"],
        not stored["decision"]["complete_hybrid_integrals_emitted"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("global_determinant_envelopes_loaded", 3539),
        lambda p: p["fixed_control"].__setitem__("combined_ordered_descriptors", 94751),
        lambda p: p["fixed_control"].__setitem__("combined_coherent_groups", 56),
        lambda p: p["order_majorants"][0]["whole_radial_face_bank"].pop(),
        lambda p: p["order_majorants"][0]["whole_radial_face_bank"][0].__setitem__("K561_radial_power", -1),
        lambda p: p["shared_majorant_contract"].__setitem__("face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals", False),
        lambda p: p["shared_majorant_contract"].__setitem__("symbolic_disjoint_owner_stitching_still_required", False),
        lambda p: p["shared_majorant_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if not all(checks) or rejected != len(mutations):
        raise AssertionError("K563 probe failed")
    print(f"K563 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
