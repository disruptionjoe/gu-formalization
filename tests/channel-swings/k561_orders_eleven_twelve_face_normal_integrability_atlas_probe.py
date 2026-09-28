#!/usr/bin/env python3
"""Replay K561 and reject face-normal integrability mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k561_orders_eleven_twelve_face_normal_integrability_atlas.py")
STORED = ROOT / "lab/process/k561-orders-eleven-twelve-face-normal-integrability-atlas.json"


def load():
    spec = importlib.util.spec_from_file_location("k561_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K561 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    rows = stored["order_atlases"]
    face_rows = [face for row in rows for face in row["face_normal_atlas"]]
    checks = [
        rebuilt == stored,
        stored["fixed_control"]["combined_hybrid_terms"] == 50,
        stored["fixed_control"]["combined_ordered_descriptors"] == 94752,
        stored["fixed_control"]["combined_reachable_face_instances"] == 2733,
        stored["fixed_control"]["logical_descriptor_face_replays"] == 136951920,
        stored["atlas_summary"]["global_minimum_face_normal_power"] == 0,
        [row["order_summary"]["complete_origin_degree"] for row in rows] == [10, 11],
        all(face["minimum_certified_second_derivative_face_normal_power"] == face["codimension"] - 1 - face["maximum_value_singular_power"] for face in face_rows),
        all(face["safe_second_derivative_singular_power_upper"] == face["maximum_value_singular_power"] + face["peano_zero_gain"] for face in face_rows),
        all(face["locally_integrable"] for face in face_rows),
        stored["face_normal_chart_contract"]["raw_Bessel_evaluation_at_zero_used"] is False,
        not stored["decision"]["whole_domain_hybrid_majorants_emitted"],
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_hybrid_terms", 49),
        lambda p: p["fixed_control"].__setitem__("combined_ordered_descriptors", 94751),
        lambda p: p["fixed_control"].__setitem__("combined_reachable_face_instances", 2732),
        lambda p: p["fixed_control"].__setitem__("logical_descriptor_face_replays", 136951919),
        lambda p: p["order_atlases"].pop(),
        lambda p: p["order_atlases"][0]["order_summary"].__setitem__("all_faces_locally_integrable", False),
        lambda p: p["release_test"].__setitem__("complete_origin_degrees_replayed", False),
        lambda p: p["decision"].__setitem__("recursive_positive_interior_cover_complete", True),
        lambda p: p["decision"].__setitem__("analytic_radial_tails_complete", True),
        lambda p: p["decision"].__setitem__("whole_domain_hybrid_majorants_emitted", True),
        lambda p: p["decision"].__setitem__("complete_order_eleven_remainder_emitted", True),
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
        raise AssertionError("K561 probe failed")
    print(f"K561 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
