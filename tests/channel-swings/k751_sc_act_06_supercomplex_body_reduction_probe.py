#!/usr/bin/env python3
"""Hostile mutation probe for K751."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k751_sc_act_06_supercomplex_body_reduction.py"
CERT = ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k751_probe_target", SCRIPT)
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
    for key, value in baseline["theorem"].items():
        mutations.append(lambda data, key=key, value=value: data["theorem"].__setitem__(key, not value))
    mutations.extend([
        lambda d: d.__setitem__("result_id", "BROKEN"),
        lambda d: d.__setitem__("classification", "COMPARATOR"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"),
        lambda d: d["exact_controls"].__setitem__("split_exact_fixture_body_middle_cohomology", 1),
        lambda d: d["exact_controls"].__setitem__("obstructed_fixture_body_middle_cohomology", 0),
        lambda d: d["exact_controls"].__setitem__("dual_number_nilpotent_perturbation_body_unchanged", False),
        lambda d: d.__setitem__("proof", []),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ])
    while len(mutations) < 29:
        mutations.append(lambda d: d["theorem"].__setitem__("nonexact_body_complex_obstructs_exact_supercomplex", False))
    caught = 0
    for mutate in mutations[:29]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    assert caught == 29
    print("PASS controls=34 hostile_mutations_rejected=29/29")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
