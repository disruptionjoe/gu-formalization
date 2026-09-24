#!/usr/bin/env python3
"""Replay K401 and reject mutations of its finite overlapping face rows."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k401_order_nine_whole_radial_face_majorants.py"
PUBLISHED = ROOT / "lab/process/k401-order-nine-whole-radial-face-majorants.json"

spec = importlib.util.spec_from_file_location("k401_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K401 producer")
backend = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = backend
spec.loader.exec_module(backend)


def rejected(payload: dict) -> bool:
    try:
        backend.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    rebuilt = backend.build()
    published = json.loads(PUBLISHED.read_text())
    controls = [
        rebuilt == published,
        rebuilt["fixed_control"]["global_determinant_envelopes_consumed"] == 1468,
        rebuilt["fixed_control"]["ordered_descriptors"] == 4480,
        rebuilt["fixed_control"]["face_programs"] == 695,
        rebuilt["fixed_control"]["maximum_nested_transition_depth"] == 19,
        rebuilt["complete_coherent_majorant"]["all_20_coherent_groups_retained_before_final_sum"],
        rebuilt["majorant_summary"]["minimum_radial_power"] == 0,
        rebuilt["majorant_summary"]["v9_v10_have_no_face_rows"],
        rebuilt["whole_radial_contract"]["face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals"],
        not rebuilt["decision"]["complete_hybrid_integrals_emitted"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("global_determinant_envelopes_consumed", 1467),
        lambda p: p["fixed_control"].__setitem__("ordered_descriptors", 4479),
        lambda p: p["fixed_control"].__setitem__("face_programs", 694),
        lambda p: p["fixed_control"].__setitem__("hybrid_axes", 20),
        lambda p: p["fixed_control"].__setitem__("maximum_nested_transition_depth", 18),
        lambda p: p["complete_coherent_majorant"].__setitem__("all_4480_ordered_descriptors_assembled", False),
        lambda p: p["complete_coherent_majorant"].__setitem__("all_20_coherent_groups_retained_before_final_sum", False),
        lambda p: p["whole_radial_face_bank"].pop(),
        lambda p: p["whole_radial_face_bank"][0].__setitem__("K389_radial_power", -1),
        lambda p: p["whole_radial_contract"].__setitem__("face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals", False),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("recursive_owner_cover_not_overclaimed", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K401 probe failed")
    print(f"K401 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
