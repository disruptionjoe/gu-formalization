#!/usr/bin/env python3
"""K460 exact boundary between HVZ membership and a complete complement floor."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


TRIAL = Fraction(-2)
THRESHOLD = TRIAL + Fraction(5, 2)


def completion(name: str, hidden_modes: tuple[Fraction, ...]) -> dict[str, Any]:
    complement_floor = min((*hidden_modes, THRESHOLD))
    count_below = 1 + sum(value < THRESHOLD for value in hidden_modes)
    return {
        "name": name,
        "trial_Rayleigh": qstr(TRIAL),
        "trial_residual_square": "0",
        "essential_spectrum": f"[{qstr(THRESHOLD)},infinity)",
        "named_HVZ_threshold_member": qstr(THRESHOLD),
        "hidden_discrete_complement_modes": [qstr(value) for value in hidden_modes],
        "complete_complement_floor": qstr(complement_floor),
        "spectral_count_strictly_below_named_threshold": count_below,
    }


def demo() -> dict[str, Any]:
    controls = [
        completion("clean_complement", ()),
        completion("hidden_discrete_complement_mode", (Fraction(-1),)),
        completion("two_hidden_complement_modes", (Fraction(-3, 2), Fraction(-1))),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K460-K152-HVZ-MEMBERSHIP-COMPLEMENT-BOUNDARY",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "K169_replay": {
            "reference_ground_symbol": "E_ref(q)",
            "neutral_cluster_cost": "5/2",
            "named_threshold_member": "E_ref(q)+5/2",
            "membership_proves_first_threshold": False,
            "membership_proves_complete_complement_floor": False,
        },
        "exact_controls": controls,
        "independence": {
            "same_trial_data": len({(row["trial_Rayleigh"], row["trial_residual_square"]) for row in controls}) == 1,
            "same_named_HVZ_threshold": len({row["named_HVZ_threshold_member"] for row in controls}) == 1,
            "same_essential_edge": len({row["essential_spectrum"] for row in controls}) == 1,
            "different_complete_complement_floors": len({row["complete_complement_floor"] for row in controls}) > 1,
            "different_counts_below_threshold": len({row["spectral_count_strictly_below_named_threshold"] for row in controls}) > 1,
        },
        "native_boundary": {
            "abstract_controls_are_K162_values": False,
            "K169_membership_may_be_used_as_K162_complement_floor": False,
            "valid_native_routes": [
                "complete M-orthogonal-complement positivity at b",
                "equivalent native flux certificate proving rank 1 below b",
                "independent native spectral-count certificate rank 1 below b",
            ],
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
