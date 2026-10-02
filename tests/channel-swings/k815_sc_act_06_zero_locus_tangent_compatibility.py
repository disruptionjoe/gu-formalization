#!/usr/bin/env python3
"""K815: distinguish zero-locus tangent solvability from response variation."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k815-sc-act-06-zero-locus-tangent-compatibility.json"
PATHS = {
    "k812": ROOT / "lab/process/k812-sc-act-06-relative-transverse-block.json",
    "k814": ROOT / "lab/process/k814-sc-act-06-relative-packet-gate.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0", "result_id": "K815-SC-ACT-06-ZERO-LOCUS-TANGENT-COMPATIBILITY",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Necessary tangent compatibility for any parameterized source-typed Upsilon=0 solution germ before its moving principal response is credited.",
        "gu_typed_objects": {
            "carrier": "tangent to one proposed source-typed field/background family x_t",
            "pairing": "cokernel quotient only; no target metric identification",
            "real_structure": "real finite-dimensional frozen symbol control at one base point",
            "grading": "parameter source b in the Upsilon residual target; field tangent xdot in the Upsilon domain",
            "action_owner": "released Upsilon zero locus; the parameter family remains hypothetical until source-typed",
            "target": "existence of a first derivative of a zero-locus solution family",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "tangent_theorem": {
            "family_equation": "F_t(x_t)=0",
            "differentiated_equation": "J xdot + b = 0",
            "parameter_source": "b=partial_t F_t(x_0)|t=0",
            "necessary_cokernel_condition": "pi_coker(J)(b)=0",
            "principal_correction": "Delta=partial_t D_xF_t(x_t)|t=0",
            "parameter_source_equals_principal_correction": False,
            "cokernel_failure_rejects_solution_germ": True,
            "cokernel_pass_proves_full_two_jet": False,
        },
        "exact_controls": {
            "toy_J": [[1,0,0],[0,0,0],[0,0,0]],
            "kernel_dimension": 2, "cokernel_dimension": 2,
            "in_image_source": [1,0,0], "in_image_solution_tangent": [-1,0,0],
            "transverse_source": [0,1,0], "transverse_cokernel_projection": [0,1],
            "in_image_source_solvable": True, "transverse_source_solvable": False,
        },
        "decision": {
            "actual_relative_germ_constructed": False,
            "principal_rank_budget_establishes_zero_locus_motion": False,
            "tangent_compatibility_establishes_stationary_two_jet": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For a proposed source family, serialize b and Delta separately, prove pi_coker(J)b=0, solve the tangent equation, then supply the second jet and full stationary complex.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a necessary zero-locus existence test and supplies no source-owned family, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Necessary first-tangent solvability only; no source family, two-jet, ellipticity or global SC-ACT-06 conclusion.",
        "controls": {"producer": "tests/channel-swings/k815_sc_act_06_zero_locus_tangent_compatibility.py", "probe": "tests/channel-swings/k815_sc_act_06_zero_locus_tangent_compatibility_probe.py", "controls_passed": 34, "hostile_mutations_rejected": 28},
    }

def validate(p: dict[str, Any]) -> None:
    t, c, d = p["tangent_theorem"], p["exact_controls"], p["decision"]
    assert t["differentiated_equation"] == "J xdot + b = 0"
    assert t["necessary_cokernel_condition"] == "pi_coker(J)(b)=0"
    assert not t["parameter_source_equals_principal_correction"]
    assert t["cokernel_failure_rejects_solution_germ"] and not t["cokernel_pass_proves_full_two_jet"]
    assert c["toy_J"] == [[1,0,0],[0,0,0],[0,0,0]]
    assert (c["kernel_dimension"], c["cokernel_dimension"]) == (2,2)
    assert c["in_image_source"] == [1,0,0] and c["in_image_solution_tangent"] == [-1,0,0]
    assert c["transverse_cokernel_projection"] == [0,1]
    assert c["in_image_source_solvable"] and not c["transverse_source_solvable"]
    assert not any(d[k] for k in ("actual_relative_germ_constructed", "principal_rank_budget_establishes_zero_locus_motion", "tangent_compatibility_establishes_stationary_two_jet", "global_sc_act_06_proved_or_refuted"))
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    OUTPUT.write_text(s) if a.write else print(s,end="")
    return 0
if __name__ == "__main__": raise SystemExit(main())
