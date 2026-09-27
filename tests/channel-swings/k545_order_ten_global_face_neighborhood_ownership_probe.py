#!/usr/bin/env python3
"""Independent replay and hostile mutations for K545."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "k545_order_ten_global_face_neighborhood_ownership.py"
spec = importlib.util.spec_from_file_location("k545_probe_backend", TARGET)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K545 producer")
K545 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K545
spec.loader.exec_module(K545)


def rejected(payload: dict) -> bool:
    try:
        K545.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    committed = json.loads(K545.OUTPUT.read_text())
    rebuilt = K545.build()
    K545.validate_payload(rebuilt)
    controls = [
        committed == rebuilt,
        len(rebuilt["hybrid_owner_bank"]) == 22,
        rebuilt["fixed_control"]["exhausted_low_coordinate_subsets"] == 8_388_606,
        rebuilt["fixed_control"]["reachable_face_programs"] == 936,
        rebuilt["fixed_control"]["unique_zero_masks"] == 121,
        rebuilt["ownership_summary"]["all_subsets_have_exactly_one_owner"],
        rebuilt["ownership_summary"]["all_assigned_faces_are_K411_reachable"],
        rebuilt["ownership_summary"]["v10_v11_use_only_interior_owner"],
        not rebuilt["decision"]["complete_hybrid_integrals_emitted"],
    ]
    mutants = []
    for path, value in [
        (("fixed_control", "hybrid_domains"), 21),
        (("fixed_control", "epsilon"), "1/32"),
        (("fixed_control", "reachable_face_programs"), 935),
        (("fixed_control", "unique_zero_masks"), 120),
        (("fixed_control", "exhausted_low_coordinate_subsets"), 8_388_605),
        (("ownership_contract", "owner_cells_are_pairwise_disjoint"), False),
        (("ownership_contract", "unreachable_faces_are_never_invented"), False),
        (("decision", "owner_regions_have_uniform_integrand_bounds"), True),
        (("decision", "complete_hybrid_integrals_emitted"), True),
        (("release_test", "native_K152_interval_not_emitted"), False),
        (("release_test", "all_8388606_low_coordinate_subsets_exhausted"), False),
    ]:
        mutant = copy.deepcopy(rebuilt)
        mutant[path[0]][path[1]] = value
        mutants.append(rejected(mutant))
    if not all(controls) or not all(mutants):
        raise AssertionError("K545 probe failed")
    print(f"K545 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutants)}/{len(mutants)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
