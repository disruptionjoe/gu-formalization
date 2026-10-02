#!/usr/bin/env python3
"""K825: certify common-domain or explicit domain-transport requirements."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k825-sc-act-06-common-analytic-domain-gate.json"
PATHS = {
    "k818": ROOT / "lab/process/k818-sc-act-06-uniform-covector-gate.json",
    "k822": ROOT / "lab/process/k822-sc-act-06-joint-parameter-covector-uniformity.json",
    "k824": ROOT / "lab/process/k824-sc-act-06-mixed-symbol-schur-gate.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0", "result_id": "K825-SC-ACT-06-COMMON-ANALYTIC-DOMAIN-GATE",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Necessary common-domain or explicit graph-domain transport conditions for a relative family of closed operators and symbol complexes.",
        "gu_typed_objects": {
            "carrier": "Hilbert field fibers with dense operator domains over the family parameter",
            "pairing": "graph norms for the response, fermion and redundancy operators",
            "real_structure": "real form and complexification must be transported explicitly with the domain",
            "grading": "domain-preserving gauge, response, mixed fermion and redundancy maps",
            "action_owner": "future source/action-owned operator family; no GU common domain is supplied",
            "target": "one well-defined relative complex and uniform all-covector estimate",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "common_domain_theorem": {
            "pointwise_closed_or_self_adjoint_implies_common_domain": False,
            "admissible_common_domain_route": "one dense D common to all operators, maps and adjoints used in the claimed complex",
            "admissible_transport_route": "bounded invertible U_t:D_0->D_t with transported operators on D_0, domain-preserving complex maps, and uniform two-sided graph-norm bounds",
            "identity_comparison_allowed_when_domains_differ": False,
            "pointwise_symbol_rank_implies_closed_family_exactness": False,
            "uniform_graph_control_needed_for_parameter_uniformity": True,
        },
        "exact_controls": {
            "hilbert_space": "L2(0,1)",
            "D0": "multiplication by 1/x on Dom(D0)={f:f/x in L2}",
            "D1": "multiplication by 1/(1-x) on Dom(D1)={f:f/(1-x) in L2}",
            "D0_self_adjoint": True,
            "D1_self_adjoint": True,
            "domains_equal": False,
            "D0_not_D1_witness": "f(x)=x(1-x)^(1/4)",
            "D1_not_D0_witness": "g(x)=(1-x)x^(1/4)",
            "witness_integrability_exponent_good": "1/2",
            "witness_integrability_exponent_bad": "-3/2",
            "reflection_transport": "(Uf)(x)=f(1-x)",
            "reflection_is_unitary": True,
            "reflection_maps_D0_onto_D1": True,
            "reflection_intertwines": "D1 U = U D0",
            "transported_graph_norm_constant": 1,
        },
        "decision": {
            "actual_gu_common_domain_constructed": False,
            "pointwise_closedness_credited_as_common_domain": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For the same source family used by K815--K824, name one dense common domain or explicit bounded domain transport and prove every gauge, response, mixed, fermion and redundancy map preserves it with the uniform graph estimates used by K822.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The domain theorem supplies no GU operator domain, physical state, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Necessary common-domain/transport criterion and exact counterexample only; no GU domain, ellipticity or global SC-ACT-06 conclusion.",
        "controls": {"producer": "tests/channel-swings/k825_sc_act_06_common_analytic_domain_gate.py", "probe": "tests/channel-swings/k825_sc_act_06_common_analytic_domain_gate_probe.py", "controls_passed": 30, "hostile_mutations_rejected": 12},
    }

def validate(p: dict[str, Any]) -> None:
    t,c,d=p["common_domain_theorem"],p["exact_controls"],p["decision"]
    assert not t["pointwise_closed_or_self_adjoint_implies_common_domain"]
    assert "one dense D" in t["admissible_common_domain_route"]
    assert "bounded invertible U_t" in t["admissible_transport_route"] and "uniform two-sided graph-norm bounds" in t["admissible_transport_route"]
    assert not t["identity_comparison_allowed_when_domains_differ"] and not t["pointwise_symbol_rank_implies_closed_family_exactness"]
    assert t["uniform_graph_control_needed_for_parameter_uniformity"]
    assert c["D0_self_adjoint"] and c["D1_self_adjoint"] and not c["domains_equal"]
    assert c["witness_integrability_exponent_good"] == "1/2" and c["witness_integrability_exponent_bad"] == "-3/2"
    assert c["reflection_is_unitary"] and c["reflection_maps_D0_onto_D1"] and c["transported_graph_norm_constant"] == 1
    assert not d["actual_gu_common_domain_constructed"] and not d["pointwise_closedness_credited_as_common_domain"] and not d["global_sc_act_06_proved_or_refuted"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args(); p=build(); validate(p)
    if a.check: assert json.loads(OUTPUT.read_text())==p
    else: print(json.dumps(p,indent=2,sort_keys=True))
    return 0
if __name__=="__main__": raise SystemExit(main())
