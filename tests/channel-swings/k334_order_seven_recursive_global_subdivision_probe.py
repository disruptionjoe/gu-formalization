#!/usr/bin/env python3
"""Independent replay and hostile controls for K334."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k334_order_seven_recursive_global_subdivision.py")
MANIFEST = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k334_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K334 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate_payload(candidate)
    except (AssertionError, ValueError):
        return True
    return False


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    if replay != stored:
        raise AssertionError("K334 deterministic replay failed")
    module.validate_payload(replay)
    cover = stored["recursive_cover"]
    master = stored["complete_y_master"]
    checks = {
        "eight_axes": stored["fixed_control"]["finite_axes"] == ["r", "s", "p0", "p1", "p2", "p3", "p4", "p5"],
        "recursive": cover["split_count"] > 0 and cover["finite_leaf_count"] > cover["finite_root_count"],
        "exact_volume": cover["exact_finite_geometric_volume_sum"] == cover["exact_finite_parent_volume"],
        "tail_cover": cover["analytic_tail_leaf_count"] == 3 and cover["tail_projective_width_sum"] == "1",
        "checksum": module.checksum(cover["finite_leaves"]) == cover["coverage_checksum"],
        "contraction": cover["all_splits_nonincreasing_by_order"],
        "tolerance": cover["declared_tolerance_met"],
        "three_constants": len(master["complete_value_first_second_abs_uppers"]) == 3,
        "finite": all(math.isfinite(float(value)) and float(value) > 0 for value in master["complete_value_first_second_abs_uppers"]),
        "release": stored["decision"]["complete_y_master_constant_emitted"],
        "no_six_axis": not stored["decision"]["complete_six_axis_peano_norm_emitted"],
        "no_k152": not stored["release_test"]["native_K152_interval_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K334 independent checks failed: {checks}")
    mutations = (
        lambda p: p["fixed_control"].__setitem__("finite_axes", ["r", "s"]),
        lambda p: p["fixed_control"].__setitem__("relative_leaf_contribution_tolerance", "1/8"),
        lambda p: p["fixed_control"].__setitem__("maximum_recursion_depth", 2),
        lambda p: p["recursive_cover"].__setitem__("exact_finite_geometric_volume_sum", "0"),
        lambda p: p["recursive_cover"].__setitem__("tail_projective_width_sum", "3/4"),
        lambda p: p["recursive_cover"].__setitem__("pairwise_disjoint_up_to_shared_boundaries", False),
        lambda p: p["recursive_cover"].__setitem__("all_finite_leaf_bounds_recomputed", False),
        lambda p: p["recursive_cover"].__setitem__("all_splits_nonincreasing_by_order", False),
        lambda p: p["recursive_cover"].__setitem__("declared_tolerance_met", False),
        lambda p: p["recursive_cover"].__setitem__("coverage_checksum", "sha256:" + "0" * 64),
        lambda p: p["recursive_cover"]["finite_leaves"][0].__setitem__("exact_geometric_volume", "0"),
        lambda p: p["recursive_cover"]["analytic_tail_leaves"][0].__setitem__("projective", ["0", "1/8"]),
        lambda p: p["complete_y_master"].__setitem__("complete_value_first_second_abs_uppers", ["1", "2"]),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", False),
        lambda p: p["decision"].__setitem__("complete_six_axis_peano_norm_emitted", True),
        lambda p: p["decision"].__setitem__("k294_gamma_join_released", True),
    )
    hostile = [rejected(module, stored, mutate) for mutate in mutations]
    if not all(hostile):
        raise AssertionError(f"K334 hostile controls escaped: {hostile}")
    print(f"K334 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
