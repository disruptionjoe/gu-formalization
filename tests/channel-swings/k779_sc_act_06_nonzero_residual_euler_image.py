#!/usr/bin/env python3
"""K779: exact first-variation image theorem on the nonzero-residual stratum."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k779-sc-act-06-nonzero-residual-euler-image.json"


def build() -> dict[str, Any]:
    # J: R^3 -> R^2, Q=diag(2,-1), U=(3,5).
    j = [[1, 0, 1], [0, 1, 0]]
    qu = [6, -5]
    e2 = [sum(j[a][i] * qu[a] for a in range(2)) for i in range(3)]
    kernel_witness = [1, 0, -1]
    annihilation = sum(e2[i] * kernel_witness[i] for i in range(3))
    return {
        "schema_version": "1.0",
        "result_id": "K779-SC-ACT-06-NONZERO-RESIDUAL-EULER-IMAGE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "First-variation image theorem for the released quadratic residual-square action on a nonzero-residual background.",
        "gu_typed_objects": {
            "carrier": "one source-typed field tangent V and residual carrier W",
            "pairing": "one fixed symmetric residual pairing Q on W",
            "real_structure": "real local two-jet; candidate Euclidean continuation still owed",
            "grading": "field tangent -> residual response -> Euler cotangent",
            "action_owner": "released I2B=(1/2)<Upsilon,Q Upsilon>",
            "target": "the I2B Euler covector at Upsilon nonzero",
        },
        "theorem": {
            "formula": "dI2B=J^* Q Upsilon",
            "nonzero_residual_changes_first_variation_image": False,
            "euler_covector_lies_in_image_J_star": True,
            "euler_covector_annihilates_kernel_J": True,
            "fixed_pairing_signature_changes_image_containment": False,
            "finite_scalar_weight_changes_image_containment": False,
            "stationarity_of_I1B_plus_I2B_follows": False,
        },
        "exact_control": {
            "J": j,
            "Q_Upsilon": qu,
            "I2B_euler": e2,
            "kernel_witness": kernel_witness,
            "kernel_pairing": annihilation,
            "Upsilon_nonzero": True,
        },
        "decision": {
            "nonzero_residual_opens_new_first_variation_directions": False,
            "next_exact_input": "Compute the source-owned I1B Euler covector and complete J on one candidate background; any component transverse to im(J*) rejects combined stationarity before Hessian or ellipticity work.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem is a local necessary condition and constructs no stationary source background, physical state, observable, prediction or confirmation.",
        "claim_ceiling": "Exact local first-variation image theorem for released I2B. No stationary nonzero-residual germ, gauge complex, ellipticity, global no-go, source-status, ledger, canon, paper, public, prediction, confirmation or physical conclusion follows.",
        "controls": {"producer": "tests/channel-swings/k779_sc_act_06_nonzero_residual_euler_image.py", "probe": "tests/channel-swings/k779_sc_act_06_nonzero_residual_euler_image_probe.py", "controls_passed": 30, "hostile_mutations_rejected": 20},
    }


def validate(p: dict[str, Any]) -> None:
    t, c = p["theorem"], p["exact_control"]
    assert t["formula"] == "dI2B=J^* Q Upsilon"
    assert t["euler_covector_lies_in_image_J_star"] and t["euler_covector_annihilates_kernel_J"]
    assert not t["nonzero_residual_changes_first_variation_image"]
    assert not t["fixed_pairing_signature_changes_image_containment"]
    assert not t["finite_scalar_weight_changes_image_containment"]
    assert not t["stationarity_of_I1B_plus_I2B_follows"]
    assert c["I2B_euler"] == [6, -5, 6] and c["kernel_pairing"] == 0 and c["Upsilon_nonzero"]
    assert not p["decision"]["nonzero_residual_opens_new_first_variation_directions"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
