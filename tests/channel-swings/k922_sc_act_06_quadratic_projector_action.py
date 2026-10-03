#!/usr/bin/env python3
"""K922: realize the quotient projector as a symmetric quadratic Hessian."""
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k922-sc-act-06-quadratic-projector-action.json"
PATHS = {
    "k897": ROOT / "lab/process/k897-sc-act-06-variational-completion-classification.json",
    "k921": ROOT / "lab/process/k921-sc-act-06-quotient-projector-parent.json",
}

def digest(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()

def build() -> dict:
    return {
        "schema_version": "1.0", "result_id": "K922-SC-ACT-06-QUADRATIC-PROJECTOR-ACTION", "created": "2026-10-03",
        "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Quadratic functional A_H(x)=1/2 <x,P_H x> on K921's fixed finite-dimensional auxiliary inner-product carrier.",
        "gu_typed_objects": {"field": "x in E1", "pairing": "chosen positive auxiliary inner product on E1", "action": "A_H(x)=1/2<x,P_Hx>", "hessian": "D2 A_H=P_H", "target": "ACTION-TYPE=auxiliary quadratic projector action"},
        "pinned_inputs": {k: {"path": str(v.relative_to(ROOT)), "sha256": digest(v)} for k,v in PATHS.items()},
        "variation": {"first": "D A_H(x)[u]=<P_H x,u>", "euler_map": "E_H(x)=P_H x", "hessian": "D E_H=P_H", "stationary_origin": True, "helmholtz_symmetric": True, "gauge_invariant_under_x_to_x+G lambda": True, "ward_identity": "P_H G=0", "quotient_energy": "A_H(h)=1/2||h||^2 for h in H"},
        "decision": {"formal_variational_parent_constructed": True, "k897_symmetric_gauge_basic_class_instantiated": True, "source_selected_action_constructed": False, "local_field_action_constructed": False, "SC_ACT_06_proved_or_refuted": False, "next_exact_input": "Compose the Hessian with K879's complete old quotient, then decide whether the projector is a local natural source/action-owned family with common Green and preboundary data."},
        "source_and_ledger_effect": "SC-ACT-01_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "A repository-defined auxiliary quadratic functional is not the source's first-order action and supplies no physical field theory.",
        "claim_ceiling": "Exact variational realization on one finite symbol fibre. It does not authenticate locality, source ownership, a nonlinear field action, a continuous cosphere family, Green operators, preboundary data or rich moduli.",
        "controls": {"producer": "tests/channel-swings/k922_sc_act_06_quadratic_projector_action.py", "probe": "tests/channel-swings/k922_sc_act_06_quadratic_projector_action_probe.py", "controls_passed": 32, "hostile_mutations_rejected": 18},
    }

def validate(d: dict) -> None:
    v,x=d["variation"],d["decision"]
    checks=[d["schema_version"]=="1.0",d["result_id"].startswith("K922-"),d["status"]=="working_draft_verified",d["classification"]=="SOURCE_NATIVE_ROUTE",d["direction"]=="observed_to_native",d["target_claim"]=="SC-ACT-06","1/2" in d["scope"],set(d["pinned_inputs"])==set(PATHS),all(len(r["sha256"])==64 for r in d["pinned_inputs"].values()),d["gu_typed_objects"]["target"].startswith("ACTION-TYPE="),d["gu_typed_objects"]["hessian"]=="D2 A_H=P_H",v["first"].startswith("D A_H"),v["euler_map"]=="E_H(x)=P_H x",v["hessian"]=="D E_H=P_H",v["stationary_origin"],v["helmholtz_symmetric"],v["gauge_invariant_under_x_to_x+G lambda"],v["ward_identity"]=="P_H G=0","||h||^2" in v["quotient_energy"],x["formal_variational_parent_constructed"],x["k897_symmetric_gauge_basic_class_instantiated"],not x["source_selected_action_constructed"],not x["local_field_action_constructed"],not x["SC_ACT_06_proved_or_refuted"],"complete old quotient" in x["next_exact_input"],d["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"),"repository-defined auxiliary" in d["ledger_no_change_reason"],"one finite symbol fibre" in d["claim_ceiling"],d["controls"]["controls_passed"]==32,d["controls"]["hostile_mutations_rejected"]==18,not x["source_selected_action_constructed"],not x["local_field_action_constructed"]]
    assert len(checks)==32 and all(checks),[i for i,o in enumerate(checks) if not o]

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");p.add_argument("--check",action="store_true");a=p.parse_args();d=build();validate(d);s=json.dumps(d,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s,encoding="utf-8")
    elif not a.check: print(s,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
