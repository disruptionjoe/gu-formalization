#!/usr/bin/env python3
"""K461 fail-closed compiler for the remaining native K152 spectral packet."""

from __future__ import annotations

import argparse
import json
from typing import Any


COMMON_REFS = (
    "fixed_limiting_form_ref",
    "cofinal_physical_Gram_ref",
    "complete_continuum_action_column_ref",
    "complete_shifted_form_dual_residual_ref",
    "center_zero_coercivity_ref",
)


def compile_readiness(**refs: str | int | None) -> dict[str, Any]:
    missing_common = [key for key in COMMON_REFS if not refs.get(key)]
    route = None
    if refs.get("complete_M_orthogonal_complement_ref"):
        route = "complete_M_orthogonal_complement"
    elif refs.get("native_flux_count_ref") and refs.get("spectral_count_below_b") == 1:
        route = "native_flux_rank_one_count"
    elif refs.get("native_spectral_count_ref") and refs.get("spectral_count_below_b") == 1:
        route = "native_rank_one_count"
    relative_ready = not missing_common and route is not None
    absolute_ready = relative_ready and bool(refs.get("selected_extension_center_ref"))
    return {
        "missing_common_references": missing_common,
        "spectral_route": route,
        "rank_one_count_below_b": refs.get("spectral_count_below_b") == 1,
        "next_distinct_floor_b_released": route is not None,
        "relative_coordinate_family_ready": relative_ready,
        "absolute_physical_axis_ready": absolute_ready,
        "selected_extension_center_required_for_relative_family": False,
        "selected_extension_center_required_for_absolute_axis": True,
        "native_K152_relative_interval_emitted": False,
        "native_K152_absolute_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    current = compile_readiness(
        fixed_limiting_form_ref="K450#fixed-limiting-form",
        cofinal_physical_Gram_ref="K450#physical-Gram",
        complete_continuum_action_column_ref="K456#complete-column",
        complete_shifted_form_dual_residual_ref="K457#finite-Gram-plus-tail",
        center_zero_coercivity_ref=None,
        complete_M_orthogonal_complement_ref=None,
        native_flux_count_ref=None,
        native_spectral_count_ref=None,
        spectral_count_below_b=None,
        selected_extension_center_ref=None,
    )
    positive_control = compile_readiness(
        fixed_limiting_form_ref="control#form",
        cofinal_physical_Gram_ref="control#Gram",
        complete_continuum_action_column_ref="control#column",
        complete_shifted_form_dual_residual_ref="control#residual",
        center_zero_coercivity_ref="control#H0-plus-s0-positive",
        native_flux_count_ref="control#equal-rank-flux",
        spectral_count_below_b=1,
        selected_extension_center_ref=None,
    )
    return {
        "schema_version": "1.0",
        "result_id": "K461-K152-NATIVE-SPECTRAL-READINESS",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "accepted_spectral_routes": [
            "complete M-orthogonal-complement positivity at b",
            "native flux certificate proving rank one below b",
            "independent native spectral-count certificate proving rank one below b",
        ],
        "current_native_readiness": current,
        "exact_positive_control": positive_control,
        "decision": {
            "K456_column_released": True,
            "K457_residual_released": True,
            "K169_HVZ_membership_released_as_complement_floor": False,
            "selected_center_removed_from_relative_readiness": True,
            "next_exact_input": "Prove center-zero shifted coercivity and one complete K162 rank-one-below-b certificate by M-orthogonal complement positivity, native flux, or independent spectral count; then evaluate K457 only to the accuracy that packet requires.",
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
