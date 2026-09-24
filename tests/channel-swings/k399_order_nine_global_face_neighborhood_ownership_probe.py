#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K399."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "k399_order_nine_global_face_neighborhood_ownership.py"
spec = importlib.util.spec_from_file_location("k399_probe_backend", TARGET)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K399 producer")
K399 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K399
spec.loader.exec_module(K399)


def rejected(payload: dict) -> bool:
    try:
        K399.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    committed = json.loads(K399.OUTPUT.read_text())
    rebuilt = K399.build()
    K399.validate_payload(rebuilt)
    controls = {
        "deterministic_rebuild": committed == rebuilt,
        "twenty_hybrids": len(rebuilt["hybrid_owner_bank"]) == 20,
        "subset_census": rebuilt["fixed_control"]["exhausted_low_coordinate_subsets"] == 2_097_150,
        "face_census": rebuilt["fixed_control"]["reachable_face_programs"] == 695,
        "mask_census": rebuilt["fixed_control"]["unique_zero_masks"] == 98,
        "unique_owners": rebuilt["ownership_summary"]["all_subsets_have_exactly_one_owner"],
        "reachable_owners": rebuilt["ownership_summary"]["all_assigned_faces_are_K386_reachable"],
        "terminal_interiors": rebuilt["ownership_summary"]["v9_v10_use_only_interior_owner"],
        "ceiling": not rebuilt["decision"]["complete_hybrid_integrals_emitted"],
    }
    mutants = []
    for path, value in [
        (("fixed_control", "hybrid_domains"), 19),
        (("fixed_control", "epsilon"), "1/32"),
        (("fixed_control", "reachable_face_programs"), 694),
        (("fixed_control", "unique_zero_masks"), 97),
        (("fixed_control", "exhausted_low_coordinate_subsets"), 2_097_149),
        (("ownership_contract", "owner_cells_are_pairwise_disjoint"), False),
        (("ownership_contract", "unreachable_faces_are_never_invented"), False),
        (("decision", "owner_regions_have_uniform_integrand_bounds"), True),
        (("decision", "complete_hybrid_integrals_emitted"), True),
        (("release_test", "native_K152_interval_not_emitted"), False),
        (("release_test", "all_2097150_low_coordinate_subsets_exhausted"), False),
    ]:
        mutant = copy.deepcopy(rebuilt)
        mutant[path[0]][path[1]] = value
        mutants.append(mutant)
    if not all(controls.values()) or not all(rejected(mutant) for mutant in mutants):
        raise AssertionError("K399 probe failed")
    print(f"K399 probe: {sum(controls.values())}/{len(controls)} controls passed; {sum(rejected(m) for m in mutants)}/{len(mutants)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
