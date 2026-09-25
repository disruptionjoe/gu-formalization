#!/usr/bin/env python3
"""K455 fail-closed compiler for the native K152 residual packet."""

from __future__ import annotations

import argparse
import json
from typing import Any


REQUIRED_NATIVE = (
    "fixed_limiting_form_ref",
    "cofinal_physical_Gram_ref",
    "complete_continuum_action_column_ref",
    "complete_shifted_form_dual_residual_ref",
    "coercivity_ref",
    "next_distinct_spectrum_ref",
    "native_left_floor_ref",
)


def compile_readiness(**refs: str | None) -> dict[str, Any]:
    missing = [key for key in REQUIRED_NATIVE if not refs.get(key)]
    complete = not missing
    return {
        "same_family_form_transfer_complete": bool(refs.get("fixed_limiting_form_ref")),
        "same_family_physical_Gram_transfer_complete": bool(refs.get("cofinal_physical_Gram_ref")),
        "finite_independent_consumer_audit_complete": bool(refs.get("finite_consumer_audit_ref")),
        "finite_joint_form_Gram_transfer_complete": bool(refs.get("finite_joint_transfer_ref")),
        "complete_continuum_action_column_serialized": bool(refs.get("complete_continuum_action_column_ref")),
        "complete_shifted_form_dual_residual_serialized": bool(refs.get("complete_shifted_form_dual_residual_ref")),
        "coercivity_serialized": bool(refs.get("coercivity_ref")),
        "next_distinct_spectrum_serialized": bool(refs.get("next_distinct_spectrum_ref")),
        "native_left_floor_serialized": bool(refs.get("native_left_floor_ref")),
        "missing_native_fields": missing,
        "native_K152_interface_complete": complete,
        "native_K152_interval_emitted": complete,
    }


def demo() -> dict[str, Any]:
    readiness = compile_readiness(
        fixed_limiting_form_ref="K450#fixed-limiting-form-restriction",
        cofinal_physical_Gram_ref="K450#physical-Gram-restriction",
        finite_consumer_audit_ref="K453#finite-independent-consumer-audit",
        finite_joint_transfer_ref="K454#joint-form-Gram-transfer",
        complete_continuum_action_column_ref=None,
        complete_shifted_form_dual_residual_ref=None,
        coercivity_ref=None,
        next_distinct_spectrum_ref=None,
        native_left_floor_ref=None,
    )
    return {
        "schema_version": "1.0",
        "result_id": "K455-K152-NATIVE-RESIDUAL-READINESS",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "finite_diagnostic_disposition": {
            "K453": "exact finite consumer values for both independent rebuilds",
            "K454": "rigorous joint form/Gram perturbation enclosure",
            "may_substitute_for_fixed_limiting_K139_form": False,
            "may_substitute_for_complete_K162_continuum_action_column": False,
        },
        "native_K152_readiness": readiness,
        "decision": {
            "finite_diagnostics_close_native_residual": False,
            "K450_form_transfer_plus_K453_K454_closes_native_residual": False,
            "next_exact_input": "Serialize the complete K156/K171 continuum action column on the fixed K162 carrier, then evaluate its shifted form-dual residual and prove coercivity, next-distinct separation and a native left floor.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
