#!/usr/bin/env python3
"""Independent replay and hostile mutations for quotient/slice semantics."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/corrected_observation_quotient_slice_compatibility.py"
STORED = ROOT / "lab/process/corrected-observation-quotient-slice-compatibility.json"

spec = importlib.util.spec_from_file_location("quotient_slice_probe_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load quotient/slice producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    module.validate_payload(stored)

    gamma = module.matrix([[0, 0, 1]])
    insertion = module.matrix([[0], [0], [1]])
    projector = module.subtract(module.identity(3), module.matmul(insertion, gamma))
    quotient_gauge = module.matrix([[1], [0], [0]])
    slice_gauge = module.matrix([[0], [0], [1]])
    parameter = (Q(5),)
    field = (Q(4), Q(-2), Q(9))
    projected = module.matvec(projector, field)

    quotient_delta = module.sub(
        module.matvec(projector, module.add(field, module.matvec(quotient_gauge, parameter))),
        projected,
    )
    slice_delta = module.sub(
        module.matvec(projector, module.add(field, module.matvec(slice_gauge, parameter))),
        projected,
    )
    checks = [
        module.matmul(gamma, insertion) == module.matrix([[1]]),
        module.matmul(projector, quotient_gauge) == quotient_gauge,
        module.matmul(projector, quotient_gauge) != module.zero(3, 1),
        quotient_delta == module.matvec(quotient_gauge, parameter),
        module.matmul(projector, slice_gauge) == module.zero(3, 1),
        module.matmul(projector, slice_gauge) != slice_gauge,
        slice_delta == (Q(0), Q(0), Q(0)),
        stored["owner_audit"]["correction_status"].startswith("semantic reclassification"),
        stored["source_routing"]["polarity_change"] == "none",
        all(stored["release_test"].values()),
    ]
    if not all(checks):
        raise AssertionError("independent quotient/slice replay failed")

    mutations = [
        lambda p: p["theorem_controls"].__setitem__("right_inverse", False),
        lambda p: p["theorem_controls"].pop("projector_idempotent"),
        lambda p: p["theorem_controls"].__setitem__("quotient_fixture_projector_does_not_kill_nonzero_gauge_image", False),
        lambda p: p["theorem_controls"].__setitem__("slice_fixture_projector_kills_gauge_image", False),
        lambda p: p["decision"].__setitem__("august_fixture_reclassified_as_quotient_descent_only", False),
        lambda p: p["decision"].__setitem__("typed_K77_action_observation_bridge_constructed", True),
        lambda p: p["decision"].__setitem__("physical_quotient_constructed", True),
        lambda p: p["decision"].__setitem__("green_domain_closed", True),
        lambda p: p["release_test"].__setitem__("predecessor_quotient_theorem_not_retracted", False),
        lambda p: p["release_test"].__setitem__("physical_claim_not_emitted", False),
        lambda p: p["ledger_effect"].__setitem__("changed", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except (AssertionError, KeyError):
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(
            f"quotient/slice hostile rejection failed: {rejected}/{len(mutations)}"
        )
    print(
        f"quotient/slice probe passed {len(checks)}/{len(checks)} controls "
        f"and rejected {rejected}/{len(mutations)} hostile mutations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
