#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K362."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k362_order_eight_zero_strip_angular_majorants.py"
STORED = ROOT / "lab/process/k362-order-eight-zero-strip-angular-majorants.json"
spec = importlib.util.spec_from_file_location("k362_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K362 producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    module.validate_payload(stored)
    rebuilt = module.build()
    checks = [
        stored == rebuilt,
        len(stored["codimension_strip_bank"]) == 13,
        stored["fixed_control"]["epsilon"] == "1/64",
        all(len(row["recursive_intersection_majorants"]) == row["ratio_coordinates"] for row in stored["codimension_strip_bank"]),
        stored["majorant_contract"]["majorants_control_angular_measure_only"],
        stored["majorant_contract"]["majorants_do_not_bound_the_K352_preconditioned_integrand"],
        stored["majorant_contract"]["uniform_integrand_weighted_boundary_envelope_still_required"],
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("K362 independent control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("epsilon", "1/32"),
        lambda p: p["fixed_control"].__setitem__("codimension_rows", 12),
        lambda p: p["codimension_strip_bank"].pop(),
        lambda p: p["codimension_strip_bank"][0]["recursive_intersection_majorants"].pop(),
        lambda p: p["majorant_contract"].__setitem__("majorants_control_angular_measure_only", False),
        lambda p: p["majorant_contract"].__setitem__("majorants_do_not_bound_the_K352_preconditioned_integrand", False),
        lambda p: p["majorant_contract"].__setitem__("uniform_integrand_weighted_boundary_envelope_still_required", False),
        lambda p: p["decision"].__setitem__("zero_inclusive_integrand_weighted_boundary_majorants_complete", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
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
        raise AssertionError(f"K362 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K362 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
