#!/usr/bin/env python3
"""Replay K570 and reject inward roots, tail loss, metric substitution, and overclaims."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k570_complete_m_dual_residual_enclosure.py")
STORED = ROOT / "lab/process/k570-complete-m-dual-residual-enclosure.json"


def load():
    spec = importlib.util.spec_from_file_location("k570_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K570 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    checks = [
        module.build() == stored,
        stored["fixed_control"]["resolved_vectors"] == 2958,
        stored["fixed_control"]["coherent_groups"] == 201,
        stored["fixed_control"]["self_and_cross_entries"] == 59586,
        stored["fixed_control"]["post_order_twelve_tail_epsilon"] == "3011499/838860800",
        stored["finite_square_input"]["sqrt_lower_is_outward"],
        stored["finite_square_input"]["sqrt_upper_is_outward"],
        stored["tail_composition"]["tail_applied_once"],
        stored["decision"]["complete_M_dual_residual_numerically_enclosed"],
        not stored["decision"]["K152_shifted_form_dual_residual_serialized"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("resolved_vectors", 2957),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 200),
        lambda p: p["fixed_control"].__setitem__("self_and_cross_entries", 59585),
        lambda p: p["fixed_control"].__setitem__("post_order_twelve_tail_epsilon", "0"),
        lambda p: p["finite_square_input"].__setitem__("sqrt_interval_exact", ["1", "1"]),
        lambda p: p["tail_composition"].__setitem__("tail_is_post_left_adjoint", False),
        lambda p: p["tail_composition"].__setitem__("tail_applied_once", False),
        lambda p: p["complete_M_dual_residual_norm_square"].__setitem__("interval_exact", ["1", "0"]),
        lambda p: p["decision"].__setitem__("useful_downstream_spectral_margin_emitted", True),
        lambda p: p["decision"].__setitem__("K152_shifted_form_dual_residual_serialized", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
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
        raise AssertionError("K570 probe failed")
    print(f"K570 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
