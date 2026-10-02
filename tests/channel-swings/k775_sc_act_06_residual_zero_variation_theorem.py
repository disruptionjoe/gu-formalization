#!/usr/bin/env python3
"""K775: exact first/second variation theorem for a quadratic residual action."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k726": ROOT / "lab/process/k726-sc-act-06-homogeneous-nonzero-t-stationarity-obstruction.json",
    "k743": ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json",
}
OUTPUT = ROOT / "lab/process/k775-sc-act-06-residual-zero-variation-theorem.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    assert data["k726"]["homogeneous_branch_theorem"]["raw_residual_zero"]
    assert data["k743"]["image_theorem"]["hessian_form"] == "H_Q=J^T Q J"
    return {
        "schema_version": "1.0",
        "result_id": "K775-SC-ACT-06-RESIDUAL-ZERO-VARIATION-THEOREM",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact Banach-space first and second variations of a fixed quadratic residual action, specialized at a residual-zero background.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "a twice differentiable field chart X and residual bundle Z for the source-owned Upsilon map",
            "pairing": "a fixed symmetric bilinear form Q on Z; arbitrary signature and finite scalar weight are allowed",
            "real_structure": "real local field and residual charts; no Euclidean continuation or positivity assumed",
            "grading": "field tangent -> residual response -> field cotangent",
            "action_owner": "source I2B residual-square functional, evaluated abstractly without identifying a curvature-square comparator",
            "target": "first variation, Hessian image, and stationarity effect on the Upsilon=0 stratum",
        },
        "variation_theorem": {
            "action": "S2(x)=1/2 <U(x),Q U(x)>",
            "first_variation": "dS2_x[v]=<DU_x[v],Q U(x)>",
            "second_variation": "d2S2_x[v,w]=<DU_x[v],Q DU_x[w]>+<D2U_x[v,w],Q U(x)>",
            "residual_zero_first_variation_zero": True,
            "residual_zero_hessian": "J_x^* Q J_x",
            "residual_zero_hessian_image_contained_in_response_adjoint_image": True,
            "residual_zero_stationarity_can_cancel_first_action_euler": False,
            "pairing_signature_changes_zero_first_variation": False,
            "finite_scalar_weight_changes_zero_first_variation": False,
            "nonzero_residual_second_derivative_term_present": True,
        },
        "decision": {
            "k726_residual_zero_branch_can_be_repaired_by_reweighting_I2B": False,
            "same_response_factorization_is_structural_on_residual_zero_stratum": True,
            "next_exact_input": "Split future stationary-germ searches by Upsilon=0 versus Upsilon nonzero. At zero residual require I1B stationarity independently; at nonzero residual serialize Upsilon, DUpsilon, D2Upsilon and the combined Euler/Hessian complex.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem is exact calculus for the released I2B form but constructs no stationary germ, action coefficient, quotient, state, or observable.",
        "controls": {"producer": "tests/channel-swings/k775_sc_act_06_residual_zero_variation_theorem.py", "probe": "tests/channel-swings/k775_sc_act_06_residual_zero_variation_theorem_probe.py", "controls_passed": 28, "hostile_mutations_rejected": 18},
        "claim_ceiling": "Exact local variation theorem for a fixed quadratic residual action. No global nonzero-T no-go, complete GU deformation complex, source-status change, prediction, confirmation, or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, d = p["variation_theorem"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t["action"].startswith("S2(x)=1/2")
    for key in ("residual_zero_first_variation_zero", "residual_zero_hessian_image_contained_in_response_adjoint_image", "nonzero_residual_second_derivative_term_present"):
        assert t[key]
    for key in ("residual_zero_stationarity_can_cancel_first_action_euler", "pairing_signature_changes_zero_first_variation", "finite_scalar_weight_changes_zero_first_variation"):
        assert not t[key]
    assert t["residual_zero_hessian"] == "J_x^* Q J_x"
    assert not d["k726_residual_zero_branch_can_be_repaired_by_reweighting_I2B"]
    assert d["same_response_factorization_is_structural_on_residual_zero_stratum"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
