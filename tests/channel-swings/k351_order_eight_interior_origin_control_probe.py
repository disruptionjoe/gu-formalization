#!/usr/bin/env python3
"""Deterministic replay, finite-difference check and hostile controls for K351."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

from flint import arb


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k351_order_eight_interior_origin_control.py")
STORED = ROOT / "lab/process/k351-order-eight-interior-origin-control.json"


def load():
    spec = importlib.util.spec_from_file_location("k351_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K351 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K351 replay differs")
    rows = stored["hybrid_interior_reference_bank"]

    raw = {axis: arb(1) / 512 for axis in module.AXES}
    analytic, _ = module.complete_second("s1", raw)
    h = arb("1e-8")
    plus = dict(raw)
    minus = dict(raw)
    plus["s1"] += h
    minus["s1"] -= h
    finite_difference = (module.complete_value(plus) - 2 * module.complete_value(raw) + module.complete_value(minus)) / (h * h)
    finite_difference_relative_error = abs(float((finite_difference / analytic - 1).mid()))

    checks = [
        len(rows) == 18,
        [row["moving_dimension"] for row in rows] == list(range(18, 0, -1)),
        all(float(row["minimum_cumulative_argument_lower"]) > 0 for row in rows),
        all(row["all_23_group_intervals_sha256"].startswith("sha256:") for row in rows),
        stored["composition_contract"]["determinants_assembled_before_group_enclosure"],
        stored["composition_contract"]["complete_coherent_groups_assembled_before_reported_enclosure"],
        stored["composition_contract"]["all_ordered_orientations_retained"],
        not stored["composition_contract"]["raw_Bessel_evaluation_at_zero_used"],
        stored["control_summary"]["K347_s1_node_second_derivative_replayed"],
        finite_difference_relative_error < 2e-8,
        not stored["control_summary"]["complete_hybrid_integrals_emitted"],
    ]
    if not all(checks):
        raise AssertionError(f"K351 control failed; finite-difference relative error={finite_difference_relative_error}")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("hybrid_terms", 17),
        lambda p: p["fixed_control"].__setitem__("ordered_directional_entries_per_axis", 1296),
        lambda p: p["hybrid_interior_reference_bank"].pop(),
        lambda p: p["hybrid_interior_reference_bank"][0].__setitem__("moving_dimension", 17),
        lambda p: p["composition_contract"].__setitem__("all_ordered_orientations_retained", False),
        lambda p: p["composition_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["composition_contract"].__setitem__("reference_bank_is_not_a_projective_cell_cover", False),
        lambda p: p["control_summary"].__setitem__("all_18_hybrid_reference_intervals_finite", False),
        lambda p: p["control_summary"].__setitem__("proper_face_preconditioners_complete", True),
        lambda p: p["control_summary"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["decision"].__setitem__("complete_order_eight_remainder_emitted", True),
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
        raise AssertionError(f"K351 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K351 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
