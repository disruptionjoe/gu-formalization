#!/usr/bin/env python3
"""Independent replay and hostile controls for K305."""

from __future__ import annotations

import importlib.util
import json
import sys
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = Path(__file__).with_name("k305_order_seven_coherent_bordered_functional_compiler.py")
MANIFEST = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k305_probe_target", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K305 module")
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
        "groups": stored["fixed_control"]["coherent_groups"] == 4,
        "patterns": all(len(group["stored_upper_triangle_pairs"]) == 6 for group in stored["coherent_groups"]),
        "ordered_terms": all(group["ordered_terms"] == 9 for group in stored["coherent_groups"]),
        "bordered_identity": stored["bordered_determinant_theorem"]["rational_control"]["identity_holds"],
        "master_templates": stored["template_compression"]["new_group_axis_order_master_functionals"] == 72,
        "y_masters": stored["template_compression"]["y_group_order_masters_after"] == 12,
        "gap_masters": stored["template_compression"]["gap_group_axis_order_masters_after"] == 60,
        "master_slots": stored["complete_counts"]["coherent_master_column_replacement_slots"] == 1160,
        "coupling_retained": all(stored["coupling_preservation"][key] for key in ("size_four_determinant_kept_joint", "companion_matrix_and_old_kernels_kept_joint", "split_variables_kept_inside_bordered_determinant", "coherent_sum_precedes_absolute_value")),
        "gamma_not_released": not stored["decision"]["k294_gamma_join_released"],
    }
    def rejected(change) -> bool:
        candidate = deepcopy(stored)
        change(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            return True
        return False

    hostile = {
        "lost_off_diagonal_multiplicity_rejected": rejected(lambda p: p["coherent_groups"][0]["stored_weights"].__setitem__(1, -1)),
        "nonzero_terminal_component_rejected": rejected(lambda p: p["bordered_determinant_theorem"]["rational_control"]["left"].__setitem__(-1, "1")),
        "early_absolute_rejected": rejected(lambda p: p["coupling_preservation"].__setitem__("coherent_sum_precedes_absolute_value", False)),
        "detached_d4_rejected": rejected(lambda p: p["coupling_preservation"].__setitem__("size_four_determinant_kept_joint", False)),
        "numerical_overclaim_rejected": rejected(lambda p: p["decision"].__setitem__("complete_numerical_norms_emitted", True)),
        "gamma_overclaim_rejected": rejected(lambda p: p["decision"].__setitem__("k294_gamma_join_released", True)),
    }
    if not all(checks.values()) or not all(hostile.values()):
        raise AssertionError({"checks": checks, "hostile": hostile})
    print(f"K305 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
