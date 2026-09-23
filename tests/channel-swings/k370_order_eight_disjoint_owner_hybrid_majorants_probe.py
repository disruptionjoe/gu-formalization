#!/usr/bin/env python3
"""Replay K370 and reject ownership, overlap, and integrability mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k370_order_eight_disjoint_owner_hybrid_majorants.py"
PUBLISHED = ROOT / "lab/process/k370-order-eight-disjoint-owner-hybrid-majorants.json"
spec = importlib.util.spec_from_file_location("k370_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K370 producer")
backend = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backend)


def rejected(payload: dict) -> bool:
    try:
        backend.validate_payload(payload)
    except (AssertionError, KeyError, ValueError):
        return True
    return False


def main() -> int:
    published = json.loads(PUBLISHED.read_text())
    replay = backend.build()
    controls = [
        replay == published,
        published["fixed_control"]["low_coordinate_subsets_replayed"] == 524286,
        published["majorant_summary"]["all_K363_owner_digests_replayed"],
        published["majorant_summary"]["all_face_owners_resolve_to_K369"],
        published["majorant_summary"]["minimum_interior_radial_power"] >= 0,
        published["disjoint_owner_contract"]["face_and_interior_owner_regions_pairwise_disjoint"],
        not published["disjoint_owner_contract"]["overlapping_K369_rows_summed_directly"],
        published["decision"]["all_eighteen_K348_hybrid_majorants_emitted"],
        not published["decision"]["complete_order_eight_remainder_emitted"],
        all(published["release_test"].values()),
    ]
    mutations = []
    for path, value in [
        (("fixed_control", "low_coordinate_subsets_replayed"), 524285),
        (("fixed_control", "face_programs_available"), 516),
        (("disjoint_owner_contract", "face_and_interior_owner_regions_pairwise_disjoint"), False),
        (("disjoint_owner_contract", "overlapping_K369_rows_summed_directly"), True),
        (("disjoint_owner_contract", "raw_Bessel_evaluation_at_zero_used"), True),
        (("decision", "K363_disjoint_owner_stitching_complete"), False),
        (("decision", "recursive_positive_interior_cover_complete"), False),
        (("decision", "complete_order_eight_remainder_emitted"), True),
        (("release_test", "all_owner_digests_match"), False),
        (("release_test", "native_K152_interval_not_emitted"), False),
    ]:
        mutant = copy.deepcopy(published)
        mutant[path[0]][path[1]] = value
        mutations.append(rejected(mutant))
    mutant = copy.deepcopy(published)
    mutant["hybrid_majorant_bank"][0]["exact_complete_hybrid_abs_upper"] = "0"
    mutations.append(rejected(mutant))
    if not all(controls) or not all(mutations):
        raise AssertionError("K370 probe failed")
    print(f"K370 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
