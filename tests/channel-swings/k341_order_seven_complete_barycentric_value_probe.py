#!/usr/bin/env python3
"""Independent replay and hostile controls for K341."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k341_order_seven_complete_barycentric_value.py")
STORED = ROOT / "lab/process/k341-order-seven-complete-barycentric-value.json"


def load():
    spec = importlib.util.spec_from_file_location("k341_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K341 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    replay = module.build()
    module.validate_payload(replay)
    if replay != stored:
        raise AssertionError("deterministic K341 replay differs")
    upper = float(stored["complete_barycentric_value"]["prefactor_free_complete_abs_upper"])
    checks = [
        stored["fixed_control"]["finite_rs_cell_count"] == 12,
        stored["fixed_control"]["analytic_tail_cell_count"] == 3,
        stored["fixed_control"]["terminal_sector_count"] == 2,
        stored["fixed_control"]["coherent_group_count"] == 4,
        stored["deduplicated_radial_projective_cover"]["source_K334_leaf_count"] == 516,
        stored["deduplicated_radial_projective_cover"]["exact_finite_rs_volume_sum"] == "1",
        stored["fixed_control"]["rs_cover_checksum"] == module.EXPECTED_RS_CHECKSUM,
        stored["complete_barycentric_value"]["prefactor_free_complete_abs_upper"] == module.EXPECTED_COMPLETE_UPPER,
        math.isfinite(upper) and upper > 0,
        stored["assembly_contract"]["all_eight_split_variables_retained"],
        not stored["assembly_contract"]["occurrencewise_absolute_sum_used"],
        not stored["complete_barycentric_value"]["K318_y_Peano_mass_applied"],
        not stored["complete_barycentric_value"]["K294_bare_mass_applied_again"],
        not stored["decision"]["native_prefactor_applied"],
    ]
    if not all(checks):
        raise AssertionError("K341 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("finite_rs_cell_count", 516),
        lambda p: p["fixed_control"].__setitem__("terminal_sector_count", 1),
        lambda p: p["deduplicated_radial_projective_cover"].__setitem__("exact_finite_rs_volume_sum", "0"),
        lambda p: p["deduplicated_radial_projective_cover"].__setitem__("gap_refinement_not_integrated_at_fixed_barycenter", False),
        lambda p: p["fixed_control"].__setitem__("rs_cover_checksum", "sha256:0"),
        lambda p: p["complete_barycentric_value"].__setitem__("prefactor_free_complete_abs_upper", "1e-7"),
        lambda p: p["complete_barycentric_value"].__setitem__("prefactor_free_complete_abs_upper", "inf"),
        lambda p: p["complete_barycentric_value"].__setitem__("K318_y_Peano_mass_applied", True),
        lambda p: p["complete_barycentric_value"].__setitem__("K294_bare_mass_applied_again", True),
        lambda p: p["assembly_contract"].__setitem__("all_four_K305_groups_included", False),
        lambda p: p["assembly_contract"].__setitem__("occurrencewise_absolute_sum_used", True),
        lambda p: p["assembly_contract"].__setitem__("detached_terminal_cofactor_used", True),
        lambda p: p["decision"].__setitem__("native_prefactor_applied", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except (AssertionError, ValueError):
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K341 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K341 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
