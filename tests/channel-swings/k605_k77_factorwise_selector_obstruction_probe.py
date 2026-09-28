#!/usr/bin/env python3
"""Probe and hostile mutations for K605."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "k605_k77_factorwise_selector_obstruction.py"
spec = importlib.util.spec_from_file_location("k605_probe_source", SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

payload = module.build()
module.validate(payload)
checks = [
    payload["result_id"] == "K605-K77-FACTORWISE-SELECTOR-OBSTRUCTION",
    payload["K590_replay"]["carrier_rank"] == 512,
    payload["K590_replay"]["carrier_half_ranks"] == [256, 256],
    payload["K590_replay"]["lifted_D1_rank"] == 35840,
    payload["K590_replay"]["lifted_D2_rank"] == 10752,
    payload["K590_replay"]["both_K444_squares_hold_for_all_parallel_projectors"] is True,
    payload["K600_replay"]["invariant_vector_dimension"] == 0,
    payload["K600_replay"]["commutant_dimension"] == 2,
    payload["theorem"]["factorwise_action_is_not_stabilizer_reducing"] is True,
    payload["theorem"]["coefficient_nonvanishing_is_irrelevant_to_carrier_naturality"] is True,
    payload["exact_controls"]["equivariance_square_count"] == 20,
    payload["exact_controls"]["maximum_entrywise_equivariance_defect"] == 0,
    payload["exact_controls"]["all_factorwise_lifts_equivariant"] is True,
    payload["exact_controls"]["invariant_vector_dimension_after_adjoining_lifts"] == 0,
    payload["exact_controls"]["carrier_commutant_dimension_after_adjoining_lifts"] == 2,
    payload["exact_controls"]["nonzero_rank_one_carrier_commutant_exists"] is False,
    payload["decision"]["K590_factorized_completion_retracted"] is False,
    payload["decision"]["K600_no_selector_theorem_strengthened"] is True,
    payload["decision"]["K598_conditional_transport_preserved"] is True,
    payload["decision"]["factorwise_base_maps_reduce_carrier_stabilizer"] is False,
    payload["decision"]["factorwise_base_maps_select_nonzero_carrier_data"] is False,
    payload["decision"]["selected_source_action_rejected"] is False,
    payload["source_and_ledger_effect"] == "none",
]
assert all(checks)

mutations = [
    ("retract K590", lambda p: p["decision"].__setitem__("K590_factorized_completion_retracted", True)),
    ("erase strengthening", lambda p: p["decision"].__setitem__("K600_no_selector_theorem_strengthened", False)),
    ("erase K598", lambda p: p["decision"].__setitem__("K598_conditional_transport_preserved", False)),
    ("claim reduction", lambda p: p["decision"].__setitem__("factorwise_base_maps_reduce_carrier_stabilizer", True)),
    ("claim selector", lambda p: p["decision"].__setitem__("factorwise_base_maps_select_nonzero_carrier_data", True)),
    ("reject source", lambda p: p["decision"].__setitem__("selected_source_action_rejected", True)),
    ("erase theorem", lambda p: p["theorem"].__setitem__("factorwise_action_is_not_stabilizer_reducing", False)),
    ("move coefficient", lambda p: p["theorem"].__setitem__("coefficient_nonvanishing_is_irrelevant_to_carrier_naturality", False)),
    ("invent defect", lambda p: p["exact_controls"].__setitem__("maximum_entrywise_equivariance_defect", 1)),
    ("erase equivariance", lambda p: p["exact_controls"].__setitem__("all_factorwise_lifts_equivariant", False)),
    ("invent vector", lambda p: p["exact_controls"].__setitem__("invariant_vector_dimension_after_adjoining_lifts", 1)),
    ("change commutant", lambda p: p["exact_controls"].__setitem__("carrier_commutant_dimension_after_adjoining_lifts", 3)),
    ("invent rank one", lambda p: p["exact_controls"].__setitem__("nonzero_rank_one_carrier_commutant_exists", True)),
]
rejected = 0
for _name, mutate in mutations:
    changed = copy.deepcopy(payload)
    mutate(changed)
    try:
        module.validate(changed)
    except AssertionError:
        rejected += 1
assert rejected == len(mutations)
print(f"{len(checks)}/{len(checks)} exact checks passed; {rejected}/{len(mutations)} hostile mutations rejected")
