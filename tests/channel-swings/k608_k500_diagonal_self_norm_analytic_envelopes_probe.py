#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K608."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k608_k500_diagonal_self_norm_analytic_envelopes.py"
ARTIFACT = ROOT / "lab/process/k608-k500-diagonal-self-norm-analytic-envelopes.json"


def load():
    spec = importlib.util.spec_from_file_location("k608_probe_source", SOURCE)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load(); payload = module.build(); module.validate(payload)
    assert payload == json.loads(ARTIFACT.read_text())
    checks = [
        payload["envelope_bank"]["count"] == 1614,
        payload["envelope_bank"]["cyclic_count"] == 291,
        payload["envelope_bank"]["action_count"] == 1323,
        payload["exact_controls"]["all_K606_endpoints_covered"],
        payload["exact_controls"]["all_envelopes_strictly_positive"],
        payload["exact_controls"]["all_action_contractions_precede_last_simplex_coordinate"],
        payload["analytic_theorem"]["normalization_counted_once"].startswith("K604"),
        payload["decision"]["outward_diagonal_upper_envelopes_emitted"],
        not payload["decision"]["complete_K500_uniform_leakage_emitted"],
    ]
    mutations = [
        lambda p: p["envelope_bank"].__setitem__("count", 1613),
        lambda p: p["envelope_bank"].__setitem__("cyclic_count", 290),
        lambda p: p["envelope_bank"].__setitem__("action_count", 1322),
        lambda p: p["exact_controls"].__setitem__("all_K606_endpoints_covered", False),
        lambda p: p["exact_controls"].__setitem__("all_envelopes_strictly_positive", False),
        lambda p: p["exact_controls"].__setitem__("all_action_contractions_precede_last_simplex_coordinate", False),
        lambda p: p["decision"].__setitem__("outward_diagonal_upper_envelopes_emitted", False),
        lambda p: p["decision"].__setitem__("numerical_diagonal_values_claimed", True),
        lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True),
        lambda p: p["decision"].__setitem__("native_noncyclic_floor_emitted", True),
        lambda p: p["decision"].__setitem__("K473_released", True),
    ]
    rejected = 0
    for mutate in mutations:
        changed = copy.deepcopy(payload); mutate(changed)
        try: module.validate(changed)
        except AssertionError: rejected += 1
    assert all(checks) and rejected == len(mutations)
    print(f"K608 exact controls: {sum(checks)}/{len(checks)} passed")
    print(f"K608 hostile mutations: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
