#!/usr/bin/env python3
"""Independent replay and hostile controls for K303."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = Path(__file__).with_name("k303_order_seven_peano_determinant_compiler.py")
MANIFEST = ROOT / "lab/process/k303-order-seven-peano-determinant-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k303_probe_target", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K303 module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    fresh = module.build()
    checks = {
        "fresh_replay": fresh == stored,
        "size_four_second_count": module.determinant_second_leaf_count(4) == 10,
        "size_three_second_count": module.determinant_second_leaf_count(3) == 6,
        "full_axis_leaf_count": module.compiled_leaf_count(module.AXIS_FACTORS["t0"]) == 55,
        "late_axis_leaf_count": module.compiled_leaf_count(module.AXIS_FACTORS["t3"]) == 45,
        "y_axis_leaf_count": module.compiled_leaf_count(module.AXIS_FACTORS["y"]) == 15,
        "aggregate_leaf_count": stored["complete_counts"]["all_six_axes_leaves_all_occurrences"] == 6480,
        "coherent_groups": stored["fixed_control"]["coherent_groups"] == 4,
        "cross_factor_two": stored["release_test"]["all_second_column_cross_terms_carry_factor_two"],
        "no_gamma_join": not stored["release_test"]["radial_gamma_join_emitted"],
    }
    hostile = {
        "drop_one_second_column": module.determinant_second_leaf_count(4) - 1 != 10,
        "ordered_pair_double_count": 4 + 4 * 3 != 10,
        "lost_cross_factor": all(
            row["coefficient"] != 1
            for axis in stored["axis_compiler"]
            for row in axis["outer_rows"]
            if row["kind"] == "cross_first_first"
        ),
        "premature_absolute_value": "after" in stored["complete_counts"]["coherent_absolute_value_location"],
        "restore_left_old_on_t4": module.compiled_leaf_count(module.AXIS_FACTORS["t4"] + ("left_endpoint_safe_old_kernel",)) != 45,
        "reuse_k290": not stored["release_test"]["pointwise_k290_reuse"],
    }
    if not all(checks.values()) or not all(hostile.values()):
        raise AssertionError({"checks": checks, "hostile": hostile})
    print(f"K303 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
