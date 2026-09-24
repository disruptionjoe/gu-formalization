#!/usr/bin/env python3
"""Independent replay and hostile controls for K152 consumer identifiability."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k152_consumer_gap_sensitivity_identifiability_obstruction.py"
STORED = ROOT / "lab/process/k152-consumer-gap-sensitivity-identifiability-obstruction.json"

spec = importlib.util.spec_from_file_location("k152_identifiability_target", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K152 identifiability producer")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def main() -> int:
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    module.validate_payload(stored)
    gap_samples = stored["gap_collapse_family"]["samples"]
    sensitivity_samples = stored["sensitivity_scaling_family"]["samples"]
    gap_values = [Fraction(row["sharp_energy_budget"]) for row in gap_samples]
    tolerance_squares = [Fraction(row["maximum_uncertainty_squared"]) for row in sensitivity_samples]
    checks = [
        ("byte-content rebuild", stored == rebuilt),
        ("fixed K270 control", module.energy_budget(Fraction(3), Fraction(2), Fraction(1)) == Fraction(3, 5)),
        ("gap formula", all(value == Fraction(3, 2 * (3 * row["n"] + 1)) for value, row in zip(gap_values, gap_samples))),
        ("gap samples positive", all(value > 0 for value in gap_values)),
        ("gap samples decrease", all(x > y for x, y in zip(gap_values, gap_values[1:]))),
        ("K168 oscillation unchanged", all(row["K168_shape_oscillation"] == "3" for row in gap_samples)),
        ("sensitivity formula", all(value == Fraction(3, 5 * row["N"] * row["N"]) for value, row in zip(tolerance_squares, sensitivity_samples))),
        ("tolerance samples decrease", all(x > y for x, y in zip(tolerance_squares, tolerance_squares[1:]))),
        ("uniform budget denied", stored["identifiability_decision"]["positive_uniform_K270_energy_budget_from_serialized_inputs"] is False),
        ("uniform tolerance denied", stored["identifiability_decision"]["positive_uniform_integral_uncertainty_tolerance_from_serialized_inputs"] is False),
        ("theorems retained", not any(stored["retained_scope"].values())),
        ("all release controls", all(stored["release_test"].values())),
    ]
    failed = [name for name, ok in checks if not ok]
    if failed:
        raise AssertionError(f"K152 independent controls failed: {failed}")

    mutations = [
        lambda p: p.__setitem__("classification", "PHYSICAL_RESULT"),
        lambda p: p["gap_collapse_family"].__setitem__("budget_formula", "B_n=3/5"),
        lambda p: p["gap_collapse_family"].__setitem__("all_budgets_positive", False),
        lambda p: p["gap_collapse_family"].__setitem__("sample_budgets_strictly_decrease", False),
        lambda p: p["gap_collapse_family"].__setitem__("infimum", "1/100"),
        lambda p: p["gap_collapse_family"].__setitem__("uniform_positive_budget_identified", True),
        lambda p: p["gap_collapse_family"].__setitem__("samples", []),
        lambda p: p["sensitivity_scaling_family"].__setitem__("fixed_energy_budget", "1"),
        lambda p: p["sensitivity_scaling_family"].__setitem__("sample_tolerance_squares_strictly_decrease", False),
        lambda p: p["sensitivity_scaling_family"].__setitem__("infimum_of_tolerance_squared", "1/100"),
        lambda p: p["sensitivity_scaling_family"].__setitem__("uniform_positive_integral_tolerance_identified", True),
        lambda p: p["identifiability_decision"].__setitem__("positive_uniform_K270_energy_budget_from_serialized_inputs", True),
        lambda p: p["identifiability_decision"].__setitem__("further_enclosure_has_decision_defined_target", True),
        lambda p: p["retained_scope"].__setitem__("K152_theorem_falsified", True),
        lambda p: p["release_test"].__setitem__("no_source_ledger_canon_paper_public_or_physical_effect", False),
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
    print(f"K152 identifiability probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
