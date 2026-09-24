#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K400."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "k400_order_nine_zero_inclusive_determinant_envelope.py"
spec = importlib.util.spec_from_file_location("k400_probe_backend", TARGET)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K400 producer")
K400 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K400
spec.loader.exec_module(K400)


def rejected(payload: dict) -> bool:
    try:
        K400.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    committed = json.loads(K400.OUTPUT.read_text())
    rebuilt = K400.build()
    K400.validate_payload(rebuilt)
    controls = {
        "deterministic_rebuild": committed == rebuilt,
        "singular_census": rebuilt["fixed_control"]["singular_templates"] == 60,
        "confluent_census": rebuilt["fixed_control"]["confluent_templates"] == 75,
        "rank_five": rebuilt["fixed_control"]["maximum_species_determinant_rank"] == 5,
        "orders_through_ten": rebuilt["fixed_control"]["global_scaled_primitive_orders"] == list(range(11)),
        "derivatives_012": all([env["derivative_order"] for env in row["derivative_envelopes"]] == [0, 1, 2] for row in rebuilt["determinant_envelope_bank"]),
        "maximum_order_ten": rebuilt["envelope_summary"]["maximum_primitive_order_used"] == 10,
        "duals": rebuilt["envelope_summary"]["all_assignment_duals_preserved"],
        "determinants": rebuilt["zero_inclusive_determinant_contract"]["complete_determinant_assembled_before_absolute_enclosure"],
        "ceiling": not rebuilt["decision"]["whole_radial_face_program_majorants_complete"],
    }
    mutants = []
    for path, value in [
        (("fixed_control", "singular_templates"), 59),
        (("fixed_control", "confluent_templates"), 74),
        (("fixed_control", "maximum_species_determinant_rank"), 4),
        (("fixed_control", "owned_low_coordinate_subsets"), 2_097_149),
        (("zero_inclusive_determinant_contract", "complete_determinant_assembled_before_absolute_enclosure"), False),
        (("zero_inclusive_determinant_contract", "confluent_factorials_applied_before_absolute_enclosure"), False),
        (("zero_inclusive_determinant_contract", "permutation_singular_exponents_retained"), False),
        (("zero_inclusive_determinant_contract", "active_face_derivative_power_assignment_complete"), True),
        (("zero_inclusive_determinant_contract", "entrywise_cofactor_absolutization_permitted"), True),
        (("zero_inclusive_determinant_contract", "raw_Bessel_evaluation_at_zero_used"), True),
        (("decision", "whole_radial_face_program_majorants_complete"), True),
        (("decision", "complete_hybrid_integrals_emitted"), True),
        (("release_test", "active_face_derivative_power_not_overclaimed"), False),
        (("release_test", "native_K152_interval_not_emitted"), False),
    ]:
        mutant = copy.deepcopy(rebuilt)
        mutant[path[0]][path[1]] = value
        mutants.append(mutant)
    if not all(controls.values()) or not all(rejected(mutant) for mutant in mutants):
        raise AssertionError("K400 probe failed")
    print(f"K400 probe: {sum(controls.values())}/{len(controls)} controls passed; {sum(rejected(m) for m in mutants)}/{len(mutants)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
