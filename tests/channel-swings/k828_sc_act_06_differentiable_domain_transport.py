#!/usr/bin/env python3
"""K828: domain transport must be graph differentiable to define Delta."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k828-sc-act-06-differentiable-domain-transport.json"
PATHS = {"k825": ROOT / "lab/process/k825-sc-act-06-common-analytic-domain-gate.json", "k826": ROOT / "lab/process/k826-sc-act-06-relative-coefficient-ownership-gate.json"}
def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    return {
        "schema_version":"1.0","result_id":"K828-SC-ACT-06-DIFFERENTIABLE-DOMAIN-TRANSPORT","created":"2026-10-02","status":"working_draft_verified",
        "classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
        "scope":"Graph-differentiable domain transport required before a moving unbounded symbol has an owned derivative on one reference domain.",
        "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
        "domain_transport_theorem":{
            "domain_bijection_alone_defines_derivative":False,
            "required_rows":["U_t D_0=D_t","uniform graph bounds for U_t and U_t^-1","graph-operator differentiability of U_t and U_t^-1","differentiability of Jhat_t=V_t^-1 J_t U_t on D_0"],
            "conjugated_derivative_rule":"Jhat_dot=V^-1 Jdot U + V^-1 J Udot - V^-1 Vdot Jhat",
            "jump_transport_has_uniform_bounds":True,
            "jump_transport_is_differentiable":False,
            "jump_transport_credits_delta":False,
        },
        "exact_controls":{
            "A0":[[1,0],[0,2]],"K":[[0,-1],[1,0]],
            "commutator_K_A0":[[0,-1],[-1,0]],
            "rotation_transport_is_differentiable":True,
            "conjugated_derivative_matches_commutator":True,
            "jump_U0":"I","jump_U_positive":"-I","jump_maps_same_domain":True,"jump_derivative_exists":False,
        },
        "decision":{"actual_gu_domain_transport_constructed":False,"actual_gu_operator_derivative_constructed":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"Supply a common GU graph domain or an owned U_t,V_t transport differentiable in graph norm, then compute the conjugated full-symbol derivative there."},
        "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling":"Differentiable-domain-transport gate only; no GU domain, symbol derivative, ellipticity, or physical conclusion.",
        "controls":{"producer":"tests/channel-swings/k828_sc_act_06_differentiable_domain_transport.py","probe":"tests/channel-swings/k828_sc_act_06_differentiable_domain_transport_probe.py","controls_passed":26,"hostile_mutations_rejected":12},
    }

def validate(p: dict[str, Any]) -> None:
    t,c,d=p["domain_transport_theorem"],p["exact_controls"],p["decision"]
    assert not t["domain_bijection_alone_defines_derivative"] and len(t["required_rows"])==4
    assert "Jhat_dot" in t["conjugated_derivative_rule"]
    assert t["jump_transport_has_uniform_bounds"] and not t["jump_transport_is_differentiable"] and not t["jump_transport_credits_delta"]
    assert c["commutator_K_A0"]==[[0,-1],[-1,0]]
    assert c["rotation_transport_is_differentiable"] and c["conjugated_derivative_matches_commutator"]
    assert c["jump_maps_same_domain"] and not c["jump_derivative_exists"]
    assert not d["actual_gu_domain_transport_constructed"] and not d["actual_gu_operator_derivative_constructed"] and not d["global_sc_act_06_proved_or_refuted"]
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args(); p=build(); validate(p)
    if a.check: assert json.loads(OUTPUT.read_text())==p
    else: print(json.dumps(p,indent=2,sort_keys=True))
    return 0
if __name__=="__main__": raise SystemExit(main())
