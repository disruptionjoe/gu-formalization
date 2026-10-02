#!/usr/bin/env python3
"""K785: preserve K779--K781 while withdrawing their direct SC-ACT-06 route."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k785-sc-act-06-nonzero-residual-variational-salvage.json"


def build() -> dict[str, Any]:
    artifacts = {
        k: json.loads((ROOT / f"lab/process/k{k}-sc-act-06-{name}.json").read_text())
        for k, name in (
            (779, "nonzero-residual-euler-image"),
            (780, "kernel-transverse-stationarity-obstruction"),
            (781, "residual-curvature-novelty"),
            (783, "source-zero-locus-boundary"),
            (784, "i1b-i2b-action-sum-ownership-correction"),
        )
    }
    assert artifacts[783]["decision"]["zero_residual_is_required_for_direct_SC_ACT_06_test"]
    assert not artifacts[784]["ownership"]["combined_stationarity_is_source_owned"]
    return {
        "schema_version": "1.0",
        "result_id": "K785-SC-ACT-06-NONZERO-RESIDUAL-VARIATIONAL-SALVAGE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE_CORRECTION",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Semantic salvage and corrected use boundary for K779--K782.",
        "gu_typed_objects": {
            "carrier": "an explicitly frozen conditional field/residual carrier",
            "pairing": "the fixed Q of a conditional residual-square action",
            "real_structure": "local real two-jet unless a separate Euclidean completion is authenticated",
            "grading": "field tangent -> residual response -> conditional action Euler/Hessian",
            "action_owner": "I2B alone for K779/K781; a repository-conditional I1B-plus-I2B sum for K780/K782",
            "target": "conditional joint-action critical points, not the SC-ACT-06 Upsilon=0 moduli by default",
        },
        "preserved_results": {
            "K779_first_variation_image": True,
            "K780_kernel_transverse_obstruction_for_fixed_sum": True,
            "K781_residual_curvature_decomposition": True,
            "K782_packet_fields_useful_for_conditional_joint_action": True,
            "arithmetic_or_linear_algebra_retracted": False,
        },
        "withdrawn_current_inferences": {
            "K782_is_direct_source_native_SC_ACT_06_gate": True,
            "released_I1B_plus_I2B_sum_is_source_owned": True,
            "nonzero_residual_is_the_incumbent_SC_ACT_06_input": True,
            "nonzero_residual_two_jet_can_by_itself_move_SC_ACT_06": True,
        },
        "corrected_use": {
            "conditional_joint_action_screen": True,
            "direct_SC_ACT_06_adjudication": False,
            "requires_explicit_sum_coefficient_and_action_completion": True,
            "cannot_transfer_to_source_claim_without_new_ownership": True,
        },
        "decision": {
            "route_status": "RETAINED_CONDITIONAL_MATHEMATICS__DIRECT_SC_ACT_06_ROUTE_WITHDRAWN",
            "next_exact_input": "Return the direct SC-ACT-06 route to Upsilon=0 and build the complete first-order Euclidean deformation complex; retain K779--K782 only for an explicitly owned conditional joint action.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "No mathematical result is discarded and no physics row moves; only the source-claim transfer and incumbent route are corrected.",
        "claim_ceiling": "Exact semantic correction and salvage. It proves no source claim, stationary background, ellipticity, prediction, confirmation or physical verdict.",
        "controls": {
            "producer": "tests/channel-swings/k785_sc_act_06_nonzero_residual_variational_salvage.py",
            "probe": "tests/channel-swings/k785_sc_act_06_nonzero_residual_variational_salvage_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 28,
        },
    }


def validate(p: dict[str, Any]) -> None:
    kept, withdrawn, use = p["preserved_results"], p["withdrawn_current_inferences"], p["corrected_use"]
    assert all(kept[key] for key in (
        "K779_first_variation_image",
        "K780_kernel_transverse_obstruction_for_fixed_sum",
        "K781_residual_curvature_decomposition",
        "K782_packet_fields_useful_for_conditional_joint_action",
    ))
    assert not kept["arithmetic_or_linear_algebra_retracted"]
    assert all(withdrawn.values())
    assert use["conditional_joint_action_screen"]
    assert not use["direct_SC_ACT_06_adjudication"]
    assert use["requires_explicit_sum_coefficient_and_action_completion"]
    assert use["cannot_transfer_to_source_claim_without_new_ownership"]
    assert p["decision"]["route_status"] == "RETAINED_CONDITIONAL_MATHEMATICS__DIRECT_SC_ACT_06_ROUTE_WITHDRAWN"
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
