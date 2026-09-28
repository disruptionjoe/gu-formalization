#!/usr/bin/env python3
"""Replay K569 and reject dropped orders, entries, metric drift, and tail overclaims."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k569_complete_finite_gram_square_enclosure.py")
STORED = ROOT / "lab/process/k569-complete-finite-gram-square-enclosure.json"


def load():
    spec = importlib.util.spec_from_file_location("k569_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K569 producer")
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
        [row["order"] for row in stored["order_enclosures"]] == list(range(2, 13)),
        stored["finite_square_Q_12"]["all_59586_entries_numerically_enclosed"],
        stored["finite_square_Q_12"]["orthogonal_order_sum"],
        stored["composition_contract"]["finite_square_is_M_dual_metric"],
        stored["composition_contract"]["finite_square_is_not_K152_shifted_form_dual_metric"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("resolved_vectors", 2957),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 200),
        lambda p: p["fixed_control"].__setitem__("self_and_cross_entries", 59585),
        lambda p: p["fixed_control"].__setitem__("orders", list(range(2, 12))),
        lambda p: p["order_enclosures"].pop(),
        lambda p: p["order_enclosures"][0].__setitem__("norm_square_interval_exact", ["1", "0"]),
        lambda p: p["finite_square_Q_12"].__setitem__("orthogonal_order_sum", False),
        lambda p: p["composition_contract"].__setitem__("no_native_prefactor_reapplied", False),
        lambda p: p["composition_contract"].__setitem__("finite_square_is_M_dual_metric", False),
        lambda p: p["decision"].__setitem__("complete_M_dual_residual_with_tail_emitted", True),
        lambda p: p["decision"].__setitem__("K152_shifted_form_dual_residual_emitted", True),
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
        raise AssertionError("K569 probe failed")
    print(f"K569 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
