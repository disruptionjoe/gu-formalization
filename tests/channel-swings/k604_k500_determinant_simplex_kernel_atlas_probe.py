#!/usr/bin/env python3
"""Probe and hostile self-test for K604."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load():
    path = HERE / "k604_k500_determinant_simplex_kernel_atlas.py"
    spec = importlib.util.spec_from_file_location("k604_probe_target", path)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    return module


def controls(module, payload):
    summary = {row["pair_kind"]: row for row in payload["atlas"]["summary"]}
    return [
        payload["K603_reconciliation"]["all_pair_counts_match"],
        payload["K603_reconciliation"]["all_2958_action_terms_replayed"],
        summary["N"]["surviving_unordered_pairs"] == 2352,
        summary["A_F"]["surviving_unordered_pairs"] == 21344,
        summary["B_F"]["surviving_unordered_pairs"] == 59586,
        all(row["nonzero_signed_kernel_classes"] > 0 for row in summary.values()),
        all(row["distinct_kernel_classes"] <= row["surviving_unordered_pairs"] for row in summary.values()),
        any(row["u"] > 1 for row in payload["atlas"]["classes"]),
        all("b" in row and "l" in row and "r" in row for row in payload["atlas"]["classes"]),
        payload["kernel_theorem"]["determinant_expansion_is_not_replaced_by_occurrencewise_absolute_values"],
        not payload["decision"]["outward_kernel_values_emitted"],
        not payload["decision"]["complete_K500_uniform_leakage_emitted"],
    ]


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--selftest", action="store_true"); args = parser.parse_args()
    module = load(); payload = module.build(); module.validate(payload)
    checks = controls(module, payload)
    if not all(checks):
        raise AssertionError("K604 control failed")
    if args.selftest:
        mutations = []
        for key in ("N", "A_F", "B_F"):
            bad = copy.deepcopy(payload); bad["K603_reconciliation"]["expected_surviving_pairs"][key] += 1; mutations.append(bad)
        for key in ("outward_kernel_values_emitted", "complete_finite_K456_moments_emitted", "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted"):
            bad = copy.deepcopy(payload); bad["decision"][key] = True; mutations.append(bad)
        bad = copy.deepcopy(payload); bad["atlas"]["classes"] = []; mutations.append(bad)
        rejected = 0
        for bad in mutations:
            try: module.validate(bad)
            except AssertionError: rejected += 1
        if rejected != len(mutations):
            raise AssertionError("K604 hostile mutation survived")
        print(f"K604 hostile self-test: {rejected}/{len(mutations)} rejected")
    print(f"K604 probe: {sum(checks)}/{len(checks)} controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
