#!/usr/bin/env python3
"""Independent replay and hostile controls for K304."""

from __future__ import annotations

import importlib.util
import json
import sys
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = Path(__file__).with_name("k304_order_seven_peano_norm_sufficiency_audit.py")
MANIFEST = ROOT / "lab/process/k304-order-seven-peano-norm-sufficiency-audit.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k304_probe_target", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K304 module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    fresh = module.build()
    routes = stored["route_audit"]
    checks = {
        "fresh_replay": fresh == stored,
        "template_count": stored["minimal_joint_functional_inventory"]["total_pattern_axis_order_templates"] == 108,
        "instance_count": stored["minimal_joint_functional_inventory"]["four_group_instantiations"] == 432,
        "y_templates": stored["minimal_joint_functional_inventory"]["y_axis_templates"] == 18,
        "gap_templates": stored["minimal_joint_functional_inventory"]["five_gap_axis_templates"] == 90,
        "factorized_rejected": not module.route_is_admissible(routes["factorized_supremum"]),
        "terminal_constant": stored["concrete_enclosure_attempt"]["fixed_x_q_bound"]["constant_C"] == "1/38263752",
        "q_factorial": stored["concrete_enclosure_attempt"]["exact_q_integration"]["factorial"] == 39916800,
        "radial_origin_failure": not stored["concrete_enclosure_attempt"]["exact_q_integration"]["radial_origin_integrable"],
        "joint_route_admissible": module.route_is_admissible(routes["joint_weighted_functionals"]),
        "finiteness_preserved": stored["release_test"]["qualitative_finiteness_preserved"],
        "gamma_not_released": not stored["qx_scaling_audit"]["gamma_join_released"],
        "k290_not_reinstated": not stored["decision"]["k290_pointwise_bank_reinstated"],
    }
    missing_measure = deepcopy(routes["joint_weighted_functionals"])
    missing_measure["same_measure"] = False
    early_absolute = deepcopy(routes["joint_weighted_functionals"])
    early_absolute["coherent_before_absolute"] = False
    lost_split = deepcopy(routes["joint_weighted_functionals"])
    lost_split["split_faces_covered"] = False
    hostile = {
        "wrong_measure_rejected": not module.route_is_admissible(missing_measure),
        "early_absolute_rejected": not module.route_is_admissible(early_absolute),
        "lost_split_rejected": not module.route_is_admissible(lost_split),
        "superseded_input_rejected": not module.route_is_admissible(routes["factorized_supremum"]),
        "marginal_is_not_joint": stored["minimal_joint_functional_inventory"]["k302_supplies_complete_joint_templates"] == 0,
        "candidate_powers_not_gamma_bound": not stored["decision"]["k294_gamma_join_released"],
        "positive_route_not_killed": not stored["decision"]["positive_peano_route_rejected"],
    }
    if not all(checks.values()) or not all(hostile.values()):
        raise AssertionError({"checks": checks, "hostile": hostile})
    print(f"K304 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
