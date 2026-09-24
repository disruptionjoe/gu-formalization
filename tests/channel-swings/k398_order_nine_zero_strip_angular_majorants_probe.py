#!/usr/bin/env python3
"""Independent replay and hostile mutation probe for K398."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "k398_order_nine_zero_strip_angular_majorants.py"
spec = importlib.util.spec_from_file_location("k398_probe_backend", TARGET)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K398 producer")
K398 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = K398
spec.loader.exec_module(K398)


def rejected(payload: dict) -> bool:
    try:
        K398.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    committed = json.loads(K398.OUTPUT.read_text())
    rebuilt = K398.build()
    K398.validate_payload(rebuilt)
    controls = {
        "deterministic_rebuild": committed == rebuilt,
        "fourteen_rows": len(rebuilt["codimension_strip_bank"]) == 14,
        "epsilon": rebuilt["fixed_control"]["epsilon"] == "1/64",
        "chart_census": rebuilt["fixed_control"]["unique_maximum_charts"] == 758,
        "use_census": rebuilt["fixed_control"]["program_chart_uses"] == 4320,
        "recursive_depths": all(len(row["recursive_intersection_majorants"]) == row["ratio_coordinates"] for row in rebuilt["codimension_strip_bank"]),
        "measure_only": rebuilt["majorant_contract"]["majorants_control_angular_measure_only"],
        "integrand_open": rebuilt["majorant_contract"]["uniform_integrand_weighted_boundary_envelope_still_required"],
        "ceiling": not rebuilt["decision"]["complete_hybrid_integrals_emitted"],
    }
    mutants = []
    for path, value in [
        (("fixed_control", "epsilon"), "1/32"),
        (("fixed_control", "codimension_rows"), 13),
        (("fixed_control", "unique_maximum_charts"), 757),
        (("fixed_control", "program_chart_uses"), 4319),
        (("majorant_contract", "majorants_control_angular_measure_only"), False),
        (("majorant_contract", "uniform_integrand_weighted_boundary_envelope_still_required"), False),
        (("decision", "complete_hybrid_integrals_emitted"), True),
        (("release_test", "native_K152_interval_not_emitted"), False),
        (("release_test", "integrand_weighted_boundary_not_overclaimed"), False),
        (("release_test", "exactly_14_codimension_rows"), False),
    ]:
        mutant = copy.deepcopy(rebuilt)
        mutant[path[0]][path[1]] = value
        mutants.append(mutant)
    if not all(controls.values()) or not all(rejected(mutant) for mutant in mutants):
        raise AssertionError("K398 probe failed")
    print(f"K398 probe: {sum(controls.values())}/{len(controls)} controls passed; {sum(rejected(m) for m in mutants)}/{len(mutants)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
