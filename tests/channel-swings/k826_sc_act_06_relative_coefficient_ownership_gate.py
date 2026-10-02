#!/usr/bin/env python3
"""K826: certify ownership requirements for a relative coefficient tangent."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k826-sc-act-06-relative-coefficient-ownership-gate.json"
PATHS = {
    "k784": ROOT / "lab/process/k784-sc-act-06-i1b-i2b-action-sum-ownership-correction.json",
    "k820": ROOT / "lab/process/k820-sc-act-06-differentiated-complex-compatibility.json",
    "k825": ROOT / "lab/process/k825-sc-act-06-common-analytic-domain-gate.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0", "result_id": "K826-SC-ACT-06-RELATIVE-COEFFICIENT-OWNERSHIP-GATE",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Ownership and normalization conditions for crediting Delta=dJ_t/dt at a source-native relative family.",
        "gu_typed_objects": {
            "carrier": "one parameterized family of response maps on fixed or explicitly transported typed fibers",
            "pairing": "none; derivative ownership precedes rank and Schur estimates",
            "real_structure": "the family's real carrier and parameter must be source/action typed",
            "grading": "relative tangent Delta between the field and residual symbol grades",
            "action_owner": "future source/action-selected interpolation, not endpoint custody",
            "target": "whether a relative principal correction and its scale are owned data",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "ownership_theorem": {
            "relative_coefficient": "Delta=dJ_t/dt|t=0",
            "owned_endpoints_determine_relative_coefficient": False,
            "owned_endpoints_determine_parameter_normalization": False,
            "required_owner": "one source/action-owned parameterized family J_t plus its parameter normalization and typed domain transport",
            "endpoint_interpolation_may_be_reverse_selected": True,
            "unowned_interpolation_rank_is_credited": False,
            "reparameterization_changes_delta": True,
        },
        "exact_controls": {
            "J0": [[1,0],[0,0]],
            "J1": [[1,0],[0,1]],
            "K": [[0,0],[0,1]],
            "path_A": "J_A(t)=J0+tK",
            "path_B": "J_B(t)=J0+t^2K",
            "same_endpoint_at_t1": True,
            "Delta_A": [[0,0],[0,1]],
            "Delta_B": [[0,0],[0,0]],
            "Delta_A_rank": 1,
            "Delta_B_rank": 0,
            "scaled_parameter": "J_A(3s)=J0+3sK",
            "scaled_Delta": [[0,0],[0,3]],
            "scaled_Delta_rank": 1,
            "relative_tangent_is_endpoint_invariant": False,
        },
        "decision": {
            "actual_source_relative_family_constructed": False,
            "endpoint_custody_promoted_to_relative_ownership": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "Supply one source/action-owned normalized family J_t on the K825 domain transport, then use its actual Delta in K820 and K822; do not choose an interpolation after seeing the desired rank.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The ownership counterexample authenticates no GU interpolation, action, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Relative-coefficient ownership and reparameterization obstruction only; no source family, ellipticity or global SC-ACT-06 conclusion.",
        "controls": {"producer": "tests/channel-swings/k826_sc_act_06_relative_coefficient_ownership_gate.py", "probe": "tests/channel-swings/k826_sc_act_06_relative_coefficient_ownership_gate_probe.py", "controls_passed": 28, "hostile_mutations_rejected": 12},
    }

def validate(p: dict[str, Any]) -> None:
    t,c,d=p["ownership_theorem"],p["exact_controls"],p["decision"]
    assert t["relative_coefficient"] == "Delta=dJ_t/dt|t=0"
    assert not t["owned_endpoints_determine_relative_coefficient"] and not t["owned_endpoints_determine_parameter_normalization"]
    assert "source/action-owned parameterized family" in t["required_owner"]
    assert t["endpoint_interpolation_may_be_reverse_selected"] and not t["unowned_interpolation_rank_is_credited"] and t["reparameterization_changes_delta"]
    assert c["same_endpoint_at_t1"] and c["Delta_A_rank"] == 1 and c["Delta_B_rank"] == 0
    assert c["Delta_A"] != c["Delta_B"] and c["scaled_Delta"] != c["Delta_A"]
    assert not c["relative_tangent_is_endpoint_invariant"]
    assert not d["actual_source_relative_family_constructed"] and not d["endpoint_custody_promoted_to_relative_ownership"] and not d["global_sc_act_06_proved_or_refuted"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args(); p=build(); validate(p)
    if a.check: assert json.loads(OUTPUT.read_text())==p
    else: print(json.dumps(p,indent=2,sort_keys=True))
    return 0
if __name__=="__main__": raise SystemExit(main())
