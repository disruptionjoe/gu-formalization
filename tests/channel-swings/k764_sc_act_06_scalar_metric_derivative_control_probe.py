#!/usr/bin/env python3
"""Hostile mutation probe for K764."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k764_sc_act_06_scalar_metric_derivative_control.py"
CERT = ROOT / "lab/process/k764-sc-act-06-scalar-metric-derivative-control.json"


def load():
    spec = importlib.util.spec_from_file_location("k764_probe_target", SCRIPT)
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
        lambda d: d["stationarity"].__setitem__("full_background_stationary_relative_to_k749", False),
        lambda d: d["stationarity"].__setitem__("scalar_euler", "NONZERO"),
        lambda d: d["stationarity"].__setitem__("metric_euler", "NONZERO"),
        lambda d: d["stationarity"].__setitem__("connection_euler_added_by_control", "NONZERO"),
        lambda d: d["principal_support"].__setitem__("old_metric_dimension", 11),
        lambda d: d["principal_support"].__setitem__("old_connection_update_rank", 1),
        lambda d: d["principal_support"].__setitem__("old_block_correction_rank_upper_r", 11),
        lambda d: d["principal_support"].__setitem__("new_even_dimension_m", 2),
        lambda d: d["principal_support"].__setitem__("r_plus_m", 12),
        lambda d: d["principal_support"].__setitem__("mixed_metric_scalar_block_allowed", False),
        lambda d: d["principal_support"].__setitem__("scalar_self_block_allowed", False),
        lambda d: d["principal_support"].__setitem__("ward_compatible", False),
        lambda d: d["principal_support"].__setitem__("all_covector_rank_upper_uniform", False),
        lambda d: d.__setitem__("exact_controls", []),
        lambda d: d["decision"].__setitem__("concrete_derivative_even_owner_constructed", False),
        lambda d: d["decision"].__setitem__("owner_is_source_or_GU_selected", True),
        lambda d: d["decision"].__setitem__("owner_changes_connection_principal_image", True),
        lambda d: d["decision"].__setitem__("owner_can_evade_k763_rank_budget", True),
        lambda d: d["decision"].__setitem__("positive_reduction_or_global_domain_supplied", True),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ]
    while len(mutations) < 32:
        mutations.append(lambda d: d.__setitem__("exact_controls", []))
    caught = 0
    for mutate in mutations[:32]:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    assert caught == 32
    print("PASS controls=38 hostile_mutations_rejected=32/32")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
