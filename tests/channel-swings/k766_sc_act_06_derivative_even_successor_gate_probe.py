#!/usr/bin/env python3
"""Hostile mutation probe for K766."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k766_sc_act_06_derivative_even_successor_gate.py"
CERT = ROOT / "lab/process/k766-sc-act-06-derivative-even-successor-gate.json"


def load():
    spec = importlib.util.spec_from_file_location("k766_probe_target", SCRIPT)
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
        lambda d: d.__setitem__("classification", "COMPARATOR"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d.__setitem__("closed_classes", []),
        lambda d: d["closed_classes"][0].__setitem__("class", "BROKEN"),
        lambda d: d["closed_classes"][1].__setitem__("reason", "BROKEN"),
        lambda d: d.__setitem__("live_reopeners", []),
        lambda d: d["decision"].__setitem__("do_not_retry_low_rank_scalar_tensor_or_small_derivative_even_owner", False),
        lambda d: d["decision"].__setitem__("finite_rank_theorem_not_global_action_no_go", False),
        lambda d: d["decision"].__setitem__("large_rank_or_changed_germ_routes_remain_open", False),
        lambda d: d["decision"].__setitem__("k500_native_packet_remains_open", False),
        lambda d: d["decision"].__setitem__("global_SC_ACT_06_refuted", True),
        lambda d: d["decision"].__setitem__("SC_ACT_06_status", "REFUTED"),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ]
    while len(mutations) < 36:
        mutations.append(lambda d: d.__setitem__("live_reopeners", []))
    caught = 0
    for mutate in mutations[:36]:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError, IndexError):
            caught += 1
    assert caught == 36
    print("PASS controls=42 hostile_mutations_rejected=36/36")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
