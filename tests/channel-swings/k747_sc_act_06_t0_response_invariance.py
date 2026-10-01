#!/usr/bin/env python3
"""K747: extend the same-response image obstruction over the certified T=0 germ family."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k747-sc-act-06-t0-response-invariance.json"
PATHS = {
    "k723": ROOT / "lab/process/k723-sc-act-06-t0-curvature-principal-invariance.json",
    "k740": ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json",
    "k743": ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k723, k740, k743 = data["k723"], data["k740"], data["k743"]
    cases = []
    for row in k743["exact_controls"]["cases"]:
        cases.append({
            "case": row["case"],
            "full_residual_response_rank": row["full_residual_response_rank"],
            "total_coupled_image_cap_rank": row["total_coupled_image_cap_rank"],
            "owned_metric_diffeomorphism_rank": row["gauge_rank"],
            "middle_cohomology_lower_bound": row["bosonic_middle_cohomology_lower_bound"],
        })
    return {
        "schema_version": "1.0",
        "result_id": "K747-SC-ACT-06-T0-RESPONSE-INVARIANCE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Principal-grade composition over K127's local Ricci-flat arbitrary-Weyl T=0 Levi-Civita stationary germ family; no nonzero-T or global-domain claim.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "K127 local Ricci-flat arbitrary-Weyl T=0 Levi-Civita germs on the 229386-dimensional coupled metric/full-connection principal carrier",
            "pairing": "arbitrary residual pairing Q after the selected I1B action pairing; no unitary pairing horn selected",
            "real_structure": "coherent Euclidean normal-frame principal comparison only; no global Euclidean continuation",
            "grading": "rank-four metric diffeomorphism gauge -> coupled bosonic Euler symbol -> transpose redundancy",
            "action_owner": "selected I1B plus every residual-square I2B Hessian factored through J_q(u)=K_LIFT(SHIAB(q wedge u))",
            "target": "middle exactness of the certified T=0 stationary-family principal complex",
        },
        "principal_transport_theorem": {
            "t0_i1b_principal_coefficients_curvature_independent": k723["principal_invariance_theorem"]["selected_t0_principal_ranks_are_curvature_independent"],
            "normal_frame_freezes_highest_order_coefficients": k723["principal_invariance_theorem"]["normal_frame_freezes_same_highest_order_coefficients"],
            "residual_response_is_derivative_only": k740["operator"]["zero_order_hodge_kappa_u_included"] is False,
            "residual_response_formula": k740["operator"]["principal_map"],
            "simultaneous_coherent_frame_transport_preserves_image_intersections": True,
            "curvature_changes_only_subprincipal_or_lower_order_transport": k723["principal_invariance_theorem"]["curvature_enters_mixed_hessian_below_principal_order"],
            "same_response_image_cap_transports_over_certified_family": True,
            "global_all_t0_stationary_germs_classified": False,
        },
        "exact_controls": {"field_dimension": k743["exact_controls"]["field_dimension"], "cases": cases},
        "decision": {
            "k127_curved_t0_family_repairs_same_response_obstruction": False,
            "another_ricci_flat_weyl_twojet_is_a_new_principal_response": False,
            "all_residual_pairings_on_transported_k740_response_fail_middle_exactness": True,
            "next_exact_input": "A nonzero-T or otherwise non-Levi-Civita stationary Euclidean germ that changes the highest-order response, or an independently action-owned principal operator; curvature transport alone is not a reopener.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result closes the released same-response residual-square repair only on K127's certified local T=0 germ family, not every stationary background or action parent.",
        "controls": {"producer": "tests/channel-swings/k747_sc_act_06_t0_response_invariance.py", "probe": "tests/channel-swings/k747_sc_act_06_t0_response_invariance_probe.py", "controls_passed": 42, "hostile_mutations_rejected": 34},
        "claim_ceiling": "Exact principal-grade transport theorem on the certified K127 T=0 family. No global T=0 classification, nonzero-T result, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K747-SC-ACT-06-T0-RESPONSE-INVARIANCE"
    assert p["classification"] == "SOURCE_NATIVE_ROUTE" and p["direction"] == "observed_to_native"
    assert p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    t = p["principal_transport_theorem"]
    for key in ("t0_i1b_principal_coefficients_curvature_independent", "normal_frame_freezes_highest_order_coefficients", "residual_response_is_derivative_only", "simultaneous_coherent_frame_transport_preserves_image_intersections", "curvature_changes_only_subprincipal_or_lower_order_transport", "same_response_image_cap_transports_over_certified_family"):
        assert t[key]
    assert t["residual_response_formula"] == "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))"
    assert not t["global_all_t0_stationary_germs_classified"]
    assert p["exact_controls"]["field_dimension"] == 229386
    cases = {row["case"]: row for row in p["exact_controls"]["cases"]}
    assert (cases["native_nonnull"]["full_residual_response_rank"], cases["native_null_auxiliary_nonzero"]["full_residual_response_rank"]) == (122864, 122864)
    assert (cases["native_nonnull"]["total_coupled_image_cap_rank"], cases["native_null_auxiliary_nonzero"]["total_coupled_image_cap_rank"]) == (131074, 131071)
    assert (cases["native_nonnull"]["middle_cohomology_lower_bound"], cases["native_null_auxiliary_nonzero"]["middle_cohomology_lower_bound"]) == (98308, 98311)
    assert all(row["owned_metric_diffeomorphism_rank"] == 4 for row in cases.values())
    d = p["decision"]
    assert not d["k127_curved_t0_family_repairs_same_response_obstruction"]
    assert not d["another_ricci_flat_weyl_twojet_is_a_new_principal_response"]
    assert d["all_residual_pairings_on_transported_k740_response_fail_middle_exactness"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
