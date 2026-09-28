#!/usr/bin/env python3
"""Deterministically replay K559 and reject reachability mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k559_orders_eleven_twelve_hybrid_face_atlas.py")
STORED = ROOT / "lab/process/k559-orders-eleven-twelve-hybrid-face-atlas.json"


def load():
    spec = importlib.util.spec_from_file_location("k559_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K559 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    rows = stored["order_atlases"]
    checks = [
        rebuilt == stored,
        stored["fixed_control"]["combined_hybrid_terms"] == 50,
        stored["fixed_control"]["combined_ordered_descriptors"] == 94752,
        stored["fixed_control"]["combined_reachable_face_instances"] == 2733,
        [row["fixed_control"]["reachable_face_instances"] for row in rows] == [1198, 1535],
        [row["fixed_control"]["unique_reachable_masks"] for row in rows] == [142, 169],
        all(row["order_summary"]["first_hybrid_reaches_complete_K554_atlas"] for row in rows),
        all(row["order_summary"]["reachable_face_counts_monotone_nonincreasing"] for row in rows),
        all(row["order_summary"]["only_first_hybrid_owns_complete_origin"] for row in rows),
        not stored["decision"]["complete_face_normal_integrability_emitted"],
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_hybrid_terms", 49),
        lambda p: p["fixed_control"].__setitem__("combined_ordered_descriptors", 94751),
        lambda p: p["order_atlases"].pop(),
        lambda p: p["release_test"].__setitem__("moving_dimensions_descend_24_and_26", False),
        lambda p: p["release_test"].__setitem__("first_hybrids_replay_complete_K554_atlases", False),
        lambda p: p["release_test"].__setitem__("only_first_hybrids_own_complete_origins", False),
        lambda p: p["decision"].__setitem__("rank_six_mask_native_preconditioner_emitted", True),
        lambda p: p["decision"].__setitem__("complete_face_normal_integrability_emitted", True),
        lambda p: p["decision"].__setitem__("whole_domain_hybrid_majorants_emitted", True),
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
        raise AssertionError("K559 probe failed")
    print(f"K559 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
