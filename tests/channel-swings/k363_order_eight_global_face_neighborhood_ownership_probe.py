#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K363."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k363_order_eight_global_face_neighborhood_ownership.py"
STORED = ROOT / "lab/process/k363-order-eight-global-face-neighborhood-ownership.json"
spec = importlib.util.spec_from_file_location("k363_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K363 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    module.validate_payload(stored)
    rebuilt = module.build()
    checks = [
        stored == rebuilt,
        len(stored["hybrid_owner_bank"]) == 18,
        stored["fixed_control"]["reachable_face_programs"] == 517,
        all(row["every_subset_has_exactly_one_owner"] for row in stored["hybrid_owner_bank"]),
        all(row["all_assigned_faces_reachable"] for row in stored["hybrid_owner_bank"]),
        stored["ownership_summary"]["v8_v9_use_only_interior_owner"],
        stored["ownership_contract"]["owner_cells_are_pairwise_disjoint"],
        stored["ownership_contract"]["owner_cells_cover_every_positive_moving_time_vector"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K363 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("hybrid_domains", 17),
        lambda p: p["fixed_control"].__setitem__("reachable_face_programs", 516),
        lambda p: p["hybrid_owner_bank"].pop(),
        lambda p: p["hybrid_owner_bank"][0].__setitem__("every_subset_has_exactly_one_owner", False),
        lambda p: p["hybrid_owner_bank"][0].__setitem__("all_assigned_faces_reachable", False),
        lambda p: p["ownership_contract"].__setitem__("owner_cells_are_pairwise_disjoint", False),
        lambda p: p["ownership_contract"].__setitem__("owner_cells_cover_every_positive_moving_time_vector", False),
        lambda p: p["ownership_contract"].__setitem__("unreachable_faces_are_never_invented", False),
        lambda p: p["decision"].__setitem__("owner_regions_have_uniform_integrand_bounds", True),
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
    if rejected != len(mutations):
        raise AssertionError(f"K363 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K363 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
