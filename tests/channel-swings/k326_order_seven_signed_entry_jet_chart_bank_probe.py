#!/usr/bin/env python3
"""Independent replay and hostile controls for K326."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k326_order_seven_signed_entry_jet_chart_bank.py")
MANIFEST = ROOT / "lab/process/k326-order-seven-signed-entry-jet-chart-bank.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k326_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K326 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate_payload(candidate)
    except (AssertionError, ValueError):
        return True
    return False


def main() -> int:
    module = load_module()
    expected = json.loads(MANIFEST.read_text())
    replay = module.build()
    if replay != expected:
        raise AssertionError("K326 deterministic replay failed")
    rows = replay["complete_chart_bank"]["rows"]
    audit = replay["signed_entry_jet_cell"]["entry_jet_audit"]
    checks = {
        "chart_count": len(rows) == 16,
        "unique_chart_ids": len({row["chart_id"] for row in rows}) == 16,
        "left_count": sum(row["endpoint"] == "left" for row in rows) == 8,
        "right_count": sum(row["endpoint"] == "right" for row in rows) == 8,
        "three_orders": all(len(row["complete_value_first_second_abs_uppers"]) == 3 for row in rows),
        "finite": all(math.isfinite(float(value)) and float(value) > 0 for row in rows for value in row["complete_value_first_second_abs_uppers"]),
        "assembly_first": replay["complete_chart_bank"]["shared_interval_substitution_precedes_determinant_coefficient_enclosure"],
        "no_family_abs": not replay["complete_chart_bank"]["familywise_absolute_summation_used"],
        "no_permutation_abs": not replay["complete_chart_bank"]["permutationwise_absolute_summation_used"],
        "literal_zeros": audit["literal_zero_slots"] == [[3, 4], [4, 3], [4, 4]],
        "terminal_orders": len(audit["terminal_scaled_jet_uppers"]) == 3,
        "no_raw_zero": not audit["raw_Bessel_evaluation_at_zero_used"],
        "scope": replay["scope_boundary"]["fixed_slab_bank_is_not_global_release"],
        "no_master": not replay["decision"]["complete_y_master_constant_emitted"],
        "no_k152": not replay["release_test"]["native_K152_interval_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K326 independent checks failed: {checks}")
    mutators = (
        lambda p: p["complete_chart_bank"]["rows"].pop(),
        lambda p: p["complete_chart_bank"]["rows"][1].__setitem__("chart_id", p["complete_chart_bank"]["rows"][0]["chart_id"]),
        lambda p: p["complete_chart_bank"]["rows"][0].__setitem__("endpoint_weight_placement", "border row 4"),
        lambda p: p["complete_chart_bank"]["rows"][8].__setitem__("endpoint_weight_placement", "border column 4"),
        lambda p: p["complete_chart_bank"]["rows"][0].__setitem__("complete_value_first_second_abs_uppers", ["1", "2"]),
        lambda p: p["complete_chart_bank"]["rows"][0]["complete_value_first_second_abs_uppers"].__setitem__(1, "inf"),
        lambda p: p["complete_chart_bank"].__setitem__("shared_interval_substitution_precedes_determinant_coefficient_enclosure", False),
        lambda p: p["complete_chart_bank"].__setitem__("familywise_absolute_summation_used", True),
        lambda p: p["complete_chart_bank"].__setitem__("permutationwise_absolute_summation_used", True),
        lambda p: p["complete_chart_bank"].__setitem__("literal_border_zeros_retained", False),
        lambda p: p["complete_chart_bank"].__setitem__("exact_chart_masses_are_census_not_extra_multiplier", False),
        lambda p: p["signed_entry_jet_cell"]["entry_jet_audit"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["signed_entry_jet_cell"]["entry_jet_audit"].__setitem__("literal_zero_slots", [[4, 4]]),
        lambda p: p["signed_entry_jet_cell"]["entry_jet_audit"].__setitem__("terminal_scaled_jet_uppers", ["4"]),
        lambda p: p["scope_boundary"].__setitem__("fixed_slab_bank_is_not_global_release", False),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    )
    hostile = [rejected(module, expected, mutate) for mutate in mutators]
    if not all(hostile):
        raise AssertionError(f"K326 hostile controls escaped: {hostile}")
    print(f"K326 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
