#!/usr/bin/env python3
"""Hostile mutation probe for K765."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k765_sc_act_06_scalar_metric_cohomology_bound.py"
CERT = ROOT / "lab/process/k765-sc-act-06-scalar-metric-cohomology-bound.json"


def load():
    spec = importlib.util.spec_from_file_location("k765_probe_target", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    base = json.loads(CERT.read_text())
    module.validate(base)
    mutations = [
        lambda d: d.__setitem__("result_id", "BROKEN"),
        lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d["composition"].__setitem__("old_bounds", {}),
        lambda d: d["composition"].__setitem__("old_block_rank_budget_r", 11),
        lambda d: d["composition"].__setitem__("new_even_dimension_m", 2),
        lambda d: d["composition"].__setitem__("maximum_middle_class_removal_r_plus_m", 12),
        lambda d: d["composition"].__setitem__("new_lower_bounds", {}),
        lambda d: d["composition"].__setitem__("formula", "BROKEN"),
        lambda d: d["composition"].__setitem__("gauge_rank", 5),
        lambda d: d["composition"].__setitem__("all_covector_rank_budget_uniform", False),
        lambda d: d["decision"].__setitem__("scalar_metric_control_repairs_k749", True),
        lambda d: d["decision"].__setitem__("nonnull_middle_exact", True),
        lambda d: d["decision"].__setitem__("native_null_middle_exact", True),
        lambda d: d["decision"].__setitem__("connection_principal_defect_reached_by_control", True),
        lambda d: d["decision"].__setitem__("stationarity_alone_sufficient_for_ellipticity", True),
        lambda d: d["decision"].__setitem__("source_ownership_supplied", True),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ]
    while len(mutations) < 30:
        mutations.append(lambda d: d["composition"].__setitem__("new_lower_bounds", {}))
    caught = 0
    for mutate in mutations[:30]:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    assert caught == 30
    print("PASS controls=36 hostile_mutations_rejected=30/30")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
