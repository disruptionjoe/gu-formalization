#!/usr/bin/env python3
"""K458 exact controls separating trial residual data from spectral floors."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


SHIFT = Fraction(6)
TRIAL_EIGENVALUE = Fraction(-2)


def completion(name: str, orthogonal: tuple[int, int]) -> dict[str, Any]:
    spectrum = [TRIAL_EIGENVALUE, *(Fraction(value) for value in orthogonal)]
    above = sorted(value for value in spectrum if value > TRIAL_EIGENVALUE)
    return {
        "name": name,
        "matrix_diagonal": [str(value) for value in spectrum],
        "trial_Gram": "1",
        "trial_action_column": ("-2", "0", "0"),
        "trial_Rayleigh": "-2",
        "trial_shifted_residual_square": "0",
        "orthogonal_compression_floor": str(min(Fraction(value) for value in orthogonal)),
        "next_distinct_above_trial": str(above[0]) if above else None,
        "shifted_coercivity_floor": str(min(value + SHIFT for value in spectrum)),
        "native_left_floor": str(min(spectrum)),
    }


def demo() -> dict[str, Any]:
    completions = [
        completion("near_complement", (-1, 3)),
        completion("far_complement", (4, 5)),
        completion("lower_hidden_mode", (-5, 4)),
    ]
    common_trial = {
        key: {row[key] for row in completions}
        for key in ("trial_Gram", "trial_action_column", "trial_Rayleigh", "trial_shifted_residual_square")
    }
    return {
        "schema_version": "1.0",
        "result_id": "K458-K152-SPECTRAL-INDEPENDENCE-BOUNDARY",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "exact_controls": completions,
        "shared_trial_data": {
            key: next(iter(values)) for key, values in common_trial.items()
        },
        "independence": {
            "all_trial_data_identical": all(len(values) == 1 for values in common_trial.values()),
            "orthogonal_compression_floor_not_determined": len({row["orthogonal_compression_floor"] for row in completions}) > 1,
            "next_distinct_spectrum_not_determined": len({row["next_distinct_above_trial"] for row in completions}) > 1,
            "shifted_coercivity_not_determined": len({row["shifted_coercivity_floor"] for row in completions}) > 1,
            "native_left_floor_not_determined": len({row["native_left_floor"] for row in completions}) > 1,
        },
        "native_boundary": {
            "abstract_controls_are_K162_values": False,
            "action_column_plus_residual_implies_exterior_floor": False,
            "action_column_plus_residual_implies_coercivity": False,
            "action_column_plus_residual_implies_next_distinct_spectrum": False,
            "action_column_plus_residual_implies_native_left_floor": False,
            "required_next_native_input": "one independently proved complete K162 M-orthogonal complement or flux floor plus a selected-center native left floor",
        },
        "K455_readiness_after_K456_K458": {
            "complete_continuum_action_column_serialized": True,
            "complete_shifted_form_dual_residual_serialized": True,
            "coercivity_serialized": False,
            "next_distinct_spectrum_serialized": False,
            "native_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
