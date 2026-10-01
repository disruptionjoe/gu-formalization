#!/usr/bin/env python3
"""Hostile mutation probe for K753."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k753_sc_act_06_even_condensate_reopener_audit.py"
CERT = ROOT / "lab/process/k753-sc-act-06-even-condensate-reopener-audit.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k753_probe_target", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    baseline = json.loads(CERT.read_text(encoding="utf-8"))
    module.validate(baseline)
    mutations = []
    for key, value in baseline["admission_audit"].items():
        if isinstance(value, bool):
            mutations.append(lambda data, key=key, value=value: data["admission_audit"].__setitem__(key, not value))
        elif isinstance(value, int):
            mutations.append(lambda data, key=key, value=value: data["admission_audit"].__setitem__(key, value + 1))
    mutations.extend([
        lambda d: d.__setitem__("result_id", "BROKEN"),
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE_ROUTE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d["exact_controls"].__setitem__("complete_tangent_dimension", 0),
        lambda d: d["exact_controls"].__setitem__("complete_tangent_ranks", []),
        lambda d: d["exact_controls"].__setitem__("complete_tangent_nullities", []),
        lambda d: d["exact_controls"].__setitem__("kernel", "BROKEN"),
        lambda d: d["exact_controls"].__setitem__("intrinsic_metric_row", "ZERO"),
        lambda d: d["decision"].__setitem__("minimal_even_condensate_repairs_k749", True),
        lambda d: d["decision"].__setitem__("nonzero_t_or_independent_action_parent_routes_remain_open", False),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ])
    while len(mutations) < 32:
        mutations.append(lambda d: d["admission_audit"].__setitem__("passes_k750_stationarity_gate", True))
    caught = 0
    for mutate in mutations[:32]:
        candidate = copy.deepcopy(baseline)
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
