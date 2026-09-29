#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K607."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k607_k77_action_symbol_stabilizer_refinement.py"
ARTIFACT = ROOT / "lab/process/k607-k77-action-symbol-stabilizer-refinement.json"


def load():
    spec = importlib.util.spec_from_file_location("k607_probe_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    payload = module.build()
    module.validate(payload)
    assert payload == json.loads(ARTIFACT.read_text())
    checks = [
        payload["actual_action_symbol_replay"]["carrier_rank"] == 512,
        payload["actual_action_symbol_replay"]["spectral_multiplicities"] == [192, 192, 64, 64],
        payload["theorem"]["minimum_nonzero_rank_in_generated_algebra"] == 64,
        not payload["theorem"]["nonzero_rank_one_packet_in_generated_algebra"],
        payload["K590_K605_reconciliation"]["K605_open_nontrivial_carrier_datum_tested"],
        payload["K590_K605_reconciliation"]["action_symbol_reduces_two_block_stabilizer"],
        not payload["K590_K605_reconciliation"]["action_symbol_selects_nonzero_vector_or_covector"],
        not payload["K590_K605_reconciliation"]["action_symbol_selects_nonzero_rank_one_packet"],
        payload["exact_controls"]["sign_polynomial_equals_expected_projector_split"],
        payload["exact_controls"]["D2_tensor_A_square_passes"],
        payload["exact_controls"]["D1_tensor_A_square_passes"],
        payload["exact_controls"]["lifted_nilpotence"],
        not payload["decision"]["K598_released"],
    ]
    mutations = [
        lambda p: p["actual_action_symbol_replay"].__setitem__("carrier_rank", 511),
        lambda p: p["actual_action_symbol_replay"].__setitem__("spectral_multiplicities", [256, 256]),
        lambda p: p["actual_action_symbol_replay"].__setitem__("zero_eigenvalue_absent", False),
        lambda p: p["theorem"].__setitem__("minimum_nonzero_rank_in_generated_algebra", 1),
        lambda p: p["theorem"].__setitem__("nonzero_rank_one_packet_in_generated_algebra", True),
        lambda p: p["K590_K605_reconciliation"].__setitem__("K590_factorized_identity_completion_retracted", True),
        lambda p: p["K590_K605_reconciliation"].__setitem__("K605_factorwise_identity_obstruction_retracted", True),
        lambda p: p["K590_K605_reconciliation"].__setitem__("K605_open_nontrivial_carrier_datum_tested", False),
        lambda p: p["K590_K605_reconciliation"].__setitem__("action_symbol_reduces_two_block_stabilizer", False),
        lambda p: p["K590_K605_reconciliation"].__setitem__("action_symbol_selects_nonzero_vector_or_covector", True),
        lambda p: p["K590_K605_reconciliation"].__setitem__("action_symbol_selects_nonzero_rank_one_packet", True),
        lambda p: p["K590_K605_reconciliation"].__setitem__("K598_actual_action_owned_initial_packet_constructed", True),
        lambda p: p["exact_controls"].__setitem__("sign_polynomial_equals_expected_projector_split", False),
        lambda p: p["exact_controls"].__setitem__("D2_tensor_A_square_passes", False),
        lambda p: p["exact_controls"].__setitem__("D1_tensor_A_square_passes", False),
        lambda p: p["exact_controls"].__setitem__("lifted_nilpotence", False),
        lambda p: p["decision"].__setitem__("actual_K438_action_symbol_tested_against_K605", False),
        lambda p: p["decision"].__setitem__("K605_missing_datum_narrowed", False),
        lambda p: p["decision"].__setitem__("nontrivial_carrier_action_is_not_sufficient_for_selection", False),
        lambda p: p["decision"].__setitem__("K598_released", True),
        lambda p: p["decision"].__setitem__("selected_source_action_rejected", True),
    ]
    rejected = 0
    for mutate in mutations:
        changed = copy.deepcopy(payload)
        mutate(changed)
        try:
            module.validate(changed)
        except AssertionError:
            rejected += 1
    assert all(checks) and rejected == len(mutations)
    print(f"K607 exact controls: {sum(checks)}/{len(checks)} passed")
    print(f"K607 hostile mutations: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
