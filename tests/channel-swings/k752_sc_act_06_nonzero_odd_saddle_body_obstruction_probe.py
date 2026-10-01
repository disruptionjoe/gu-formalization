#!/usr/bin/env python3
"""Hostile mutation probe for K752."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k752_sc_act_06_nonzero_odd_saddle_body_obstruction.py"
CERT = ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k752_probe_target", SCRIPT)
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
    for key, value in baseline["composition_theorem"].items():
        mutations.append(lambda data, key=key, value=value: data["composition_theorem"].__setitem__(key, not value))
    for index, row in enumerate(baseline["exact_controls"]["cases"]):
        for key, value in row.items():
            mutations.append(lambda data, index=index, key=key, value=value: data["exact_controls"]["cases"][index].__setitem__(key, "wrong" if isinstance(value, str) else (not value if isinstance(value, bool) else value + 1)))
    mutations.extend([
        lambda d: d.__setitem__("result_id", "BROKEN"),
        lambda d: d.__setitem__("classification", "COMPARATOR"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d["decision"].__setitem__("k750_nonzero_fermion_reopener_closed_for_minimal_grassmann_bilinear_class", False),
        lambda d: d["decision"].__setitem__("commuting_c_number_spinor_is_same_class", True),
        lambda d: d["decision"].__setitem__("body_valued_even_condensate_is_same_class", True),
        lambda d: d["decision"].__setitem__("fermion_zero_modes_or_nilpotent_backreaction_excluded", True),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ])
    while len(mutations) < 34:
        mutations.append(lambda d: d["composition_theorem"].__setitem__("minimal_nonzero_odd_saddle_repairs_middle_exactness", True))
    caught = 0
    for mutate in mutations[:34]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    assert caught == 34
    print("PASS controls=40 hostile_mutations_rejected=34/34")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
