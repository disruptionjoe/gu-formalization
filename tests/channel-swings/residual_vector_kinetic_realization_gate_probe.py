#!/usr/bin/env python3
"""Independent replay and hostile-mutation probe for the residual-vector gate."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/residual_vector_kinetic_realization_gate.py"
STORED = ROOT / "lab/process/residual-vector-kinetic-realization-gate.json"

spec = importlib.util.spec_from_file_location("residual_vector_gate_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load residual-vector producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        rebuilt["exact_root_trace"]["cartan_tensor"] == [["16" if i == j else "0" for j in range(5)] for i in range(5)],
        rebuilt["declared_cartan_plane"]["B-L_projection_on_Y"] == "4/5",
        rebuilt["declared_cartan_plane"]["pairing_X_Y"] == "0",
        rebuilt["declared_cartan_plane"]["pairing_X_X"] == "16/5",
        rebuilt["decision"]["first_rank_radical_gate_on_fundamental_candidate"] == "passes",
        rebuilt["decision"]["premise_P8_status"] == "supplied_not_derived",
        rebuilt["source_boundary"]["source_claim_effect"] == "none",
        rebuilt["source_boundary"]["physics_ledger_effect"] == "none",
        all(rebuilt["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("residual-vector independent control failed")
    mutations = [
        lambda p: p["exact_root_trace"].__setitem__("root_count", 39),
        lambda p: p["exact_root_trace"].__setitem__("tensor_identity", "8*I_5"),
        lambda p: p["declared_cartan_plane"].__setitem__("gram_determinant", "0"),
        lambda p: p["declared_cartan_plane"].__setitem__("gram_rank", 1),
        lambda p: p["declared_cartan_plane"].__setitem__("pairing_X_Y", "1"),
        lambda p: p["declared_cartan_plane"].__setitem__("pairing_X_X", "0"),
        lambda p: p["horn_disposition"]["packet_fundamental_zeta_F_1"].__setitem__("p8_derived", True),
        lambda p: p["horn_disposition"]["packet_induced_zeta_F_0"].__setitem__("p8_derived", True),
        lambda p: p["decision"].__setitem__("premise_P8_status", "derived"),
        lambda p: p["remaining_p8_owners"].pop(),
        lambda p: p["release_test"].__setitem__("source_two_layer_reading_not_collapsed", False),
        lambda p: p["release_test"].__setitem__("no_physical_or_public_effect", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"residual-vector probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
