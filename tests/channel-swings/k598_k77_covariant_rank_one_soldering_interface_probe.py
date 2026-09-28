#!/usr/bin/env python3
"""Deterministic and hostile probe for K598."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k598_k77_covariant_rank_one_soldering_interface.py"
ARTIFACT = ROOT / "lab/process/k598-k77-covariant-rank-one-soldering-interface.json"


def load():
    spec = importlib.util.spec_from_file_location("k598_probe_producer", PRODUCER)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    return module


def main() -> int:
    m = load(); expected = m.build(); m.validate(expected)
    assert expected == json.loads(ARTIFACT.read_text())
    checks = [
        expected["exact_controls"]["matching_half_all_squares_pass"],
        expected["exact_controls"]["matching_half_all_covariantly_parallel"],
        expected["exact_controls"]["fixed_vector_shortcut_fires_at_mixed_points"],
        expected["exact_controls"]["opposite_half_all_squares_fail"],
        expected["exact_controls"]["both_K589_arrows_exercised"],
        expected["ownership_boundary"]["K441_owns_transport_and_moving_projector"],
        expected["ownership_boundary"]["K589_owns_base_degree_arrows"],
        expected["ownership_boundary"]["K596_owns_initial_rank_one_discriminator"],
        expected["ownership_boundary"]["conditional_covariant_packet_constructed"],
        not expected["ownership_boundary"]["actual_action_owned_packet_constructed"],
        expected["decision"]["both_conditional_covariant_K444_squares_emitted"],
        not expected["decision"]["actual_action_owned_soldering_constructed"],
    ]
    mutations = []
    for path in [
        ("exact_controls", "matching_half_all_squares_pass"),
        ("exact_controls", "matching_half_all_covariantly_parallel"),
        ("exact_controls", "fixed_vector_shortcut_fires_at_mixed_points"),
        ("exact_controls", "opposite_half_all_squares_fail"),
        ("ownership_boundary", "conditional_covariant_packet_constructed"),
        ("decision", "both_conditional_covariant_K444_squares_emitted"),
    ]:
        case = copy.deepcopy(expected); case[path[0]][path[1]] = False; mutations.append(case)
    for path in [
        ("ownership_boundary", "actual_action_owned_packet_constructed"),
        ("decision", "actual_action_owned_soldering_constructed"),
        ("decision", "K590_factorized_completion_retracted"),
        ("decision", "selected_source_action_rejected"),
    ]:
        case = copy.deepcopy(expected); case[path[0]][path[1]] = True; mutations.append(case)
    caught = 0
    for case in mutations:
        try: m.validate(case)
        except AssertionError: caught += 1
    print(f"PASS K598 controls: {sum(checks)}/{len(checks)}")
    print(f"PASS K598 hostile mutations: {caught}/{len(mutations)}")
    return 0 if all(checks) and caught == len(mutations) else 1


if __name__ == "__main__": raise SystemExit(main())
