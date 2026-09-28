#!/usr/bin/env python3
"""Deterministic and hostile probe for K599."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k599_k500_sharp_tail_moment_enclosure_interface.py"
ARTIFACT = ROOT / "lab/process/k599-k500-sharp-tail-moment-enclosure-interface.json"


def load():
    spec = importlib.util.spec_from_file_location("k599_probe_producer", PRODUCER)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    return module


def main() -> int:
    m = load(); expected = m.build(); m.validate(expected)
    assert expected == json.loads(ARTIFACT.read_text())
    checks = [
        expected["theorem"]["tail_charged_once"],
        expected["theorem"]["scalar_moment_sign_retained"],
        expected["K574_application"]["same_post_left_adjoint_location"],
        expected["exact_controls"]["all_A_contained"],
        expected["exact_controls"]["all_B_contained"],
        expected["exact_controls"]["all_leakage_contained"],
        expected["exact_controls"]["parallel_orthogonal_and_negative_cross_present"],
        expected["decision"]["sharp_tail_composition_interface_emitted"],
        expected["decision"]["duplicate_tail_charge_forbidden"],
        expected["decision"]["numerical_finite_moment_evaluation_still_required"],
        not expected["decision"]["complete_K500_uniform_leakage_emitted"],
        not expected["non_substitutability"]["K575_residual_substitution_allowed"],
    ]
    mutations = []
    for path in [
        ("theorem", "tail_charged_once"),
        ("theorem", "scalar_moment_sign_retained"),
        ("K574_application", "same_post_left_adjoint_location"),
        ("exact_controls", "all_A_contained"),
        ("exact_controls", "all_B_contained"),
        ("exact_controls", "all_leakage_contained"),
        ("decision", "sharp_tail_composition_interface_emitted"),
        ("decision", "duplicate_tail_charge_forbidden"),
        ("decision", "numerical_finite_moment_evaluation_still_required"),
    ]:
        case = copy.deepcopy(expected); case[path[0]][path[1]] = False; mutations.append(case)
    for path in [
        ("K574_application", "finite_moments_numerically_enclosed"),
        ("K574_application", "complete_uniform_leakage_emitted"),
        ("non_substitutability", "K575_residual_substitution_allowed"),
        ("decision", "complete_K500_uniform_leakage_emitted"),
        ("decision", "native_noncyclic_floor_emitted"),
        ("decision", "K473_released"),
        ("decision", "native_K152_interval_emitted"),
    ]:
        case = copy.deepcopy(expected); case[path[0]][path[1]] = True; mutations.append(case)
    caught = 0
    for case in mutations:
        try: m.validate(case)
        except AssertionError: caught += 1
    print(f"PASS K599 controls: {sum(checks)}/{len(checks)}")
    print(f"PASS K599 hostile mutations: {caught}/{len(mutations)}")
    return 0 if all(checks) and caught == len(mutations) else 1


if __name__ == "__main__": raise SystemExit(main())
