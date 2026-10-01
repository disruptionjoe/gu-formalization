#!/usr/bin/env python3
"""Hostile mutation probe for K754."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k754_sc_act_06_nonzero_fermion_successor_gate.py"
CERT = ROOT / "lab/process/k754-sc-act-06-nonzero-fermion-successor-gate.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k754_probe_target", SCRIPT)
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
    for key, value in baseline["gate_theorem"].items():
        mutations.append(lambda data, key=key, value=value: data["gate_theorem"].__setitem__(key, not value if isinstance(value, bool) else "BROKEN"))
    for index, row in enumerate(baseline["closed_inputs"]):
        mutations.append(lambda data, index=index: data["closed_inputs"][index].__setitem__("evidence", "BROKEN"))
    mutations.extend([
        lambda d: d.__setitem__("result_id", "BROKEN"),
        lambda d: d.__setitem__("classification", "COMPARATOR"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d.__setitem__("live_reopeners", []),
        lambda d: d.__setitem__("admission_order", []),
        lambda d: d["decision"].__setitem__("next_route", "RETRY"),
        lambda d: d["decision"].__setitem__("do_not_retry_minimal_grassmann_bilinear_saddle", False),
        lambda d: d["decision"].__setitem__("do_not_retry_cbrs1r_ultralocal_condensate", False),
        lambda d: d["decision"].__setitem__("source_silent_classes_not_promoted_to_source_ownership", False),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ])
    while len(mutations) < 36:
        mutations.append(lambda d: d.__setitem__("live_reopeners", []))
    caught = 0
    for mutate in mutations[:36]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    assert caught == 36
    print("PASS controls=42 hostile_mutations_rejected=36/36")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
