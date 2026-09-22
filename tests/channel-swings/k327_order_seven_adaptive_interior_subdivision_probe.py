#!/usr/bin/env python3
"""Independent replay and hostile controls for K327."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k327_order_seven_adaptive_interior_subdivision.py")
MANIFEST = ROOT / "lab/process/k327-order-seven-adaptive-interior-subdivision.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k327_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K327 module")
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
    expected = json.loads(MANIFEST.read_text())
    replay = module.build()
    if replay != expected:
        raise AssertionError("K327 deterministic replay failed")
    cover = replay["refined_cover"]
    ratios = [float(value) for value in cover["parent_to_refined_ratios"]]
    checks = {
        "child_count": cover["child_count"] == 256,
        "unique_bits": len({row["bits"] for row in cover["children"]}) == 256,
        "eight_axes": all(len(row["bits"]) == 8 for row in cover["children"]),
        "exact_volume": cover["exact_child_volume_sum"] == replay["parent_control"]["exact_volume"],
        "disjoint": cover["pairwise_disjoint_up_to_shared_boundaries"],
        "three_orders": len(cover["integrated_value_first_second_abs_uppers"]) == 3,
        "finite": all(math.isfinite(float(value)) and float(value) > 0 for value in cover["integrated_value_first_second_abs_uppers"]),
        "strict_contraction": all(0 < value < 1 for value in ratios),
        "nonincreasing": all(cover["refinement_nonincreasing_by_order"]),
        "recomputed": cover["entry_intervals_recomputed_per_child"],
        "post_assembly": cover["post_assembly_enclosure_reused_without_familywise_absolute_sum"],
        "scope": replay["scope_boundary"]["interior_refinement_is_not_global_release"],
        "no_origin_tail": not replay["decision"]["complete_origin_tail_face_sum_emitted"],
        "no_master": not replay["decision"]["complete_y_master_constant_emitted"],
        "no_k152": not replay["release_test"]["native_K152_interval_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K327 independent checks failed: {checks}")
    mutators = (
        lambda p: p["refined_cover"].__setitem__("child_count", 255),
        lambda p: p["refined_cover"]["children"].pop(),
        lambda p: p["refined_cover"]["children"][1].__setitem__("bits", p["refined_cover"]["children"][0]["bits"]),
        lambda p: p["refined_cover"]["children"][0].__setitem__("bits", "000"),
        lambda p: p["refined_cover"].__setitem__("exact_parent_volume_replayed", False),
        lambda p: p["refined_cover"].__setitem__("exact_child_volume_sum", "0"),
        lambda p: p["refined_cover"].__setitem__("pairwise_disjoint_up_to_shared_boundaries", False),
        lambda p: p["refined_cover"].__setitem__("refinement_nonincreasing_by_order", [True, False, True]),
        lambda p: p["refined_cover"].__setitem__("integrated_value_first_second_abs_uppers", ["1", "2"]),
        lambda p: p["refined_cover"]["integrated_value_first_second_abs_uppers"].__setitem__(1, "inf"),
        lambda p: p["refined_cover"].__setitem__("entry_intervals_recomputed_per_child", False),
        lambda p: p["refined_cover"].__setitem__("post_assembly_enclosure_reused_without_familywise_absolute_sum", False),
        lambda p: p["scope_boundary"].__setitem__("interior_refinement_is_not_global_release", False),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    )
    hostile = [rejected(module, expected, mutate) for mutate in mutators]
    if not all(hostile):
        raise AssertionError(f"K327 hostile controls escaped: {hostile}")
    print(f"K327 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
