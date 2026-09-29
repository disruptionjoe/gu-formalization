#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K610."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "tests/channel-swings/k610_k77_factorwise_algebra_selector_obstruction.py"
ARTIFACT = ROOT / "lab/process/k610-k77-factorwise-algebra-selector-obstruction.json"


def load():
    spec = importlib.util.spec_from_file_location("k610_probe_source", SOURCE)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load(); payload = module.build(); module.validate(payload)
    assert payload == json.loads(ARTIFACT.read_text())
    checks = [
        payload["closure_theorem"]["spectral_block_ranks"] == [192, 192, 64, 64],
        payload["closure_theorem"]["minimum_nonzero_carrier_idempotent_rank"] == 64,
        not payload["closure_theorem"]["rank_one_packet_in_factorwise_closure"],
        payload["K590_K607_reconciliation"]["full_available_factorwise_algebra_tested"],
        payload["exact_controls"]["rank_one_absent"],
        not payload["decision"]["K598_released"],
        payload["decision"]["nonfactorized_action_data_remain_live"],
    ]
    mutations = [
        lambda p: p["closure_theorem"].__setitem__("spectral_block_ranks", [256, 256]),
        lambda p: p["closure_theorem"].__setitem__("minimum_nonzero_carrier_idempotent_rank", 1),
        lambda p: p["closure_theorem"].__setitem__("rank_one_packet_in_factorwise_closure", True),
        lambda p: p["K590_K607_reconciliation"].__setitem__("full_available_factorwise_algebra_tested", False),
        lambda p: p["K590_K607_reconciliation"].__setitem__("K590_factorized_exact_complex_retracted", True),
        lambda p: p["K590_K607_reconciliation"].__setitem__("K607_action_symbol_result_retracted", True),
        lambda p: p["exact_controls"].__setitem__("minimum_nonzero_carrier_rank", 1),
        lambda p: p["exact_controls"].__setitem__("rank_one_absent", False),
        lambda p: p["decision"].__setitem__("factorwise_algebra_selects_carrier_vector_or_covector", True),
        lambda p: p["decision"].__setitem__("factorwise_algebra_selects_rank_one_packet", True),
        lambda p: p["decision"].__setitem__("K598_released", True),
        lambda p: p["decision"].__setitem__("selected_source_action_rejected", True),
        lambda p: p["decision"].__setitem__("nonfactorized_action_data_remain_live", False),
    ]
    rejected = 0
    for mutate in mutations:
        changed = copy.deepcopy(payload); mutate(changed)
        try: module.validate(changed)
        except AssertionError: rejected += 1
    assert all(checks) and rejected == len(mutations)
    print(f"K610 exact controls: {sum(checks)}/{len(checks)} passed")
    print(f"K610 hostile mutations: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
