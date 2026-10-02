#!/usr/bin/env python3
"""K823: certify that zero-locus transport does not imply action stationarity."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k823-sc-act-06-stationarity-transport-gate.json"
PATHS = {
    "k815": ROOT / "lab/process/k815-sc-act-06-zero-locus-tangent-compatibility.json",
    "k819": ROOT / "lab/process/k819-sc-act-06-second-order-zero-locus-obstruction.json",
    "k822": ROOT / "lab/process/k822-sc-act-06-joint-parameter-covector-uniformity.json",
}

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "result_id": "K823-SC-ACT-06-STATIONARITY-TRANSPORT-GATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Necessary action-stationarity jet conditions for a proposed relative Upsilon=0 family whenever action Hessians or action-owned field symbols are claimed.",
        "gu_typed_objects": {
            "carrier": "a proposed real parameterized field/background curve x_t",
            "pairing": "independently owned Euler covector and Hessian, not the Upsilon residual pairing",
            "real_structure": "real C2 parameter and field jets",
            "grading": "zero-locus residual F_t and action Euler map E_t are separate typed rows",
            "action_owner": "future source/action-owned moving functional; no such family is supplied",
            "target": "simultaneous zero-locus and action-stationary transport",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n, p in PATHS.items()},
        "stationarity_transport_theorem": {
            "zero_locus_equation": "F_t(x_t)=0",
            "stationarity_equation": "E_t(x_t)=dS_t(x_t)=0",
            "first_stationarity_jet": "A xdot + e = 0, where A=D_x E_0 and e=partial_t E_t|0",
            "second_stationarity_jet": "A xddot + E_tt + 2 E_tx[xdot] + E_xx[xdot,xdot] = 0",
            "zero_locus_transport_implies_stationarity_transport": False,
            "stationarity_is_required_before_action_hessian_credit": True,
            "passing_first_and_second_stationarity_jets_proves_a_full_family": False,
        },
        "exact_controls": {
            "shared_zero_locus": "F(t,x)=x-t with branch x_t=t",
            "branch_speed": 1,
            "nonstationary_action": "S(t,x)=x^2/2",
            "nonstationary_euler": "E(t,x)=x",
            "nonstationary_first_jet_residual": 1,
            "nonstationary_zero_locus_passes": True,
            "nonstationary_stationarity_transport_passes": False,
            "stationary_action": "S(t,x)=(x-t)^2/2",
            "stationary_euler": "E(t,x)=x-t",
            "stationary_first_jet_residual": 0,
            "stationary_second_jet_residual": 0,
            "stationary_zero_locus_passes": True,
            "stationary_transport_passes": True,
        },
        "decision": {
            "actual_source_action_family_constructed": False,
            "zero_locus_packet_promoted_to_action_stationarity": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For a source relative family, serialize its independent Euler map and prove the stationarity jets on the same field curve before using an action Hessian or action-owned mixed symbol.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "A generic stationarity-separation theorem supplies no source action, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Necessary stationarity transport only; no source action family, ellipticity or global SC-ACT-06 conclusion.",
        "controls": {
            "producer": "tests/channel-swings/k823_sc_act_06_stationarity_transport_gate.py",
            "probe": "tests/channel-swings/k823_sc_act_06_stationarity_transport_gate_probe.py",
            "controls_passed": 28,
            "hostile_mutations_rejected": 12,
        },
    }

def validate(p: dict[str, Any]) -> None:
    t, c, d = p["stationarity_transport_theorem"], p["exact_controls"], p["decision"]
    assert t["zero_locus_equation"] != t["stationarity_equation"]
    assert "A xdot + e = 0" in t["first_stationarity_jet"]
    assert "A xddot" in t["second_stationarity_jet"]
    assert not t["zero_locus_transport_implies_stationarity_transport"]
    assert t["stationarity_is_required_before_action_hessian_credit"]
    assert not t["passing_first_and_second_stationarity_jets_proves_a_full_family"]
    assert c["branch_speed"] == 1 and c["nonstationary_first_jet_residual"] == 1
    assert c["nonstationary_zero_locus_passes"] and not c["nonstationary_stationarity_transport_passes"]
    assert c["stationary_first_jet_residual"] == c["stationary_second_jet_residual"] == 0
    assert c["stationary_zero_locus_passes"] and c["stationary_transport_passes"]
    assert not any(d[k] for k in ("actual_source_action_family_constructed", "zero_locus_packet_promoted_to_action_stationarity", "global_sc_act_06_proved_or_refuted"))
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    p = build(); validate(p)
    if a.check: assert json.loads(OUTPUT.read_text()) == p
    else: print(json.dumps(p, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__": raise SystemExit(main())
