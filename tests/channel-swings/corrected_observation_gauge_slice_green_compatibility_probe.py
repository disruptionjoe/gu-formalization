#!/usr/bin/env python3
"""Independent replay and hostile mutations for the corrected-observation gate."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/corrected_observation_gauge_slice_green_compatibility.py"
STORED = ROOT / "lab/process/corrected-observation-gauge-slice-green-compatibility.json"

spec = importlib.util.spec_from_file_location("corrected_observation_gate_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load corrected-observation producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    checks = [
        stored == rebuilt,
        stored["exact_fixture"]["right_inverse_laws"]["orthogonal"],
        stored["exact_fixture"]["right_inverse_laws"]["oblique"],
        stored["exact_fixture"]["projector_laws"]["both_land_in_gamma_kernel"],
        stored["exact_fixture"]["projector_laws"]["unrelated_gauge_image_is_not_killed"],
        stored["exact_fixture"]["green_laws"]["oblique_projector_is_not_self_adjoint"],
        stored["owner_audit"]["k77_bfv_image"]["carrier"] != stored["owner_audit"]["corrected_clifford_projector"]["carrier"],
        stored["owner_audit"]["typed_composition_result"].startswith("no current artifact"),
        not stored["decision"]["physical_gauge_slice_derived"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("corrected-observation independent control failed")
    mutations = [
        lambda p: p["theorem"].__setitem__("image", "im(P)=B"),
        lambda p: p["theorem"].__setitem__("kernel", "ker(P)=0"),
        lambda p: p["exact_fixture"]["projector_laws"].__setitem__("orthogonal_idempotent", False),
        lambda p: p["exact_fixture"]["projector_laws"].__setitem__("oblique_idempotent", False),
        lambda p: p["exact_fixture"]["projector_laws"].__setitem__("unrelated_gauge_image_is_not_killed", False),
        lambda p: p["exact_fixture"]["green_laws"].__setitem__("orthogonal_projector_is_self_adjoint", False),
        lambda p: p["exact_fixture"]["green_laws"].__setitem__("oblique_projector_is_not_self_adjoint", False),
        lambda p: p["owner_audit"].pop("k77_green_form"),
        lambda p: p["owner_audit"].__setitem__("typed_composition_result", "composed"),
        lambda p: p["decision"].__setitem__("physical_gauge_slice_derived", True),
        lambda p: p["decision"].__setitem__("green_compatible_right_inverse_derived", True),
        lambda p: p["decision"].__setitem__("same_named_projectors_composed", True),
        lambda p: p["release_test"].__setitem__("owner_carriers_remain_distinct", False),
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
    print(f"corrected-observation probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
