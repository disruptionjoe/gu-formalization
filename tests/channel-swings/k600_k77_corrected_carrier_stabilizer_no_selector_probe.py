#!/usr/bin/env python3
"""Probe and hostile mutations for K600."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "k600_k77_corrected_carrier_stabilizer_no_selector.py"
spec = importlib.util.spec_from_file_location("k600_probe_source", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


payload = module.build()
module.validate(payload)
checks = [
    payload["result_id"] == "K600-K77-CORRECTED-CARRIER-STABILIZER-NO-SELECTOR",
    payload["gu_typed_objects"]["naturality_group"] == "O(E_+) x O(E_-), already preserving the pairing, projector and scalar coefficients",
    payload["theorem"]["dimension_mismatch_alone_used"] is False,
    payload["selected_action_replay"]["D3_t_t_t"] == "8736",
    payload["selected_action_replay"]["D3_t_v_v_over_native_norm"] == "-56/3",
    payload["selected_action_replay"]["field_to_carrier_soldering_map_serialized"] is False,
    payload["selected_action_replay"]["action_Riesz_map_on_K441_pairing_serialized"] is False,
    payload["selected_action_replay"]["K598_conditional_covariant_packet_constructed"] is True,
    payload["selected_action_replay"]["K598_actual_action_owned_packet_constructed"] is False,
    payload["exact_controls"]["invariant_vector_dimension"] == 0,
    payload["exact_controls"]["commutant_dimension"] == 2,
    payload["exact_controls"]["commutant_basis_ranks"] == [3, 3],
    payload["exact_controls"]["block_identity_basis_recovered"] is True,
    payload["exact_controls"]["nonzero_rank_one_commutant_exists"] is False,
    payload["decision"]["scalar_third_jet_selects_nonzero_initial_vector"] is False,
    payload["decision"]["scalar_third_jet_selects_nonzero_Riesz_return"] is False,
    payload["decision"]["nonzero_rank_one_packet_natural_from_current_inputs"] is False,
    payload["decision"]["additional_action_owned_symmetry_breaking_datum_required"] is True,
    payload["decision"]["K598_conditional_transport_preserved"] is True,
    payload["source_and_ledger_effect"] == "none",
]
assert all(checks)


mutations = [
    ("claim vector", lambda p: p["decision"].__setitem__("scalar_third_jet_selects_nonzero_initial_vector", True)),
    ("claim covector", lambda p: p["decision"].__setitem__("scalar_third_jet_selects_nonzero_Riesz_return", True)),
    ("claim rank one", lambda p: p["decision"].__setitem__("nonzero_rank_one_packet_natural_from_current_inputs", True)),
    ("erase extra datum", lambda p: p["decision"].__setitem__("additional_action_owned_symmetry_breaking_datum_required", False)),
    ("erase transport", lambda p: p["decision"].__setitem__("K598_conditional_transport_preserved", False)),
    ("retract factorized", lambda p: p["decision"].__setitem__("K590_factorized_completion_retracted", True)),
    ("reject source", lambda p: p["decision"].__setitem__("selected_source_action_rejected", True)),
    ("use dimension", lambda p: p["theorem"].__setitem__("dimension_mismatch_alone_used", True)),
    ("invent injection", lambda p: p["selected_action_replay"].__setitem__("field_to_carrier_soldering_map_serialized", True)),
    ("invent Riesz", lambda p: p["selected_action_replay"].__setitem__("action_Riesz_map_on_K441_pairing_serialized", True)),
    ("erase conditional", lambda p: p["selected_action_replay"].__setitem__("K598_conditional_covariant_packet_constructed", False)),
    ("invent actual packet", lambda p: p["selected_action_replay"].__setitem__("K598_actual_action_owned_packet_constructed", True)),
    ("move coefficient", lambda p: p["selected_action_replay"].__setitem__("D3_t_t_t", "0")),
    ("move coefficient two", lambda p: p["selected_action_replay"].__setitem__("D3_t_v_v_over_native_norm", "0")),
    ("invent invariant", lambda p: p["exact_controls"].__setitem__("invariant_vector_dimension", 1)),
    ("change commutant", lambda p: p["exact_controls"].__setitem__("commutant_dimension", 3)),
    ("change ranks", lambda p: p["exact_controls"].__setitem__("commutant_basis_ranks", [1, 3])),
    ("erase basis", lambda p: p["exact_controls"].__setitem__("block_identity_basis_recovered", False)),
    ("invent rank one control", lambda p: p["exact_controls"].__setitem__("nonzero_rank_one_commutant_exists", True)),
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
