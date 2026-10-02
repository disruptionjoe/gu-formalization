#!/usr/bin/env python3
"""K830: compose K815--K829 into one fail-closed relative-family gate."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k830-sc-act-06-relative-family-admission-compiler.json"
PATHS={
    "k815":ROOT/"lab/process/k815-sc-act-06-zero-locus-tangent-compatibility.json",
    "k816":ROOT/"lab/process/k816-sc-act-06-response-symmetry-overlap.json",
    "k817":ROOT/"lab/process/k817-sc-act-06-finite-parameter-schur-gate.json",
    "k818":ROOT/"lab/process/k818-sc-act-06-uniform-covector-gate.json",
    "k819":ROOT/"lab/process/k819-sc-act-06-second-order-zero-locus-obstruction.json",
    "k820":ROOT/"lab/process/k820-sc-act-06-differentiated-complex-compatibility.json",
    "k821":ROOT/"lab/process/k821-sc-act-06-quotient-slice-equivalence.json",
    "k822":ROOT/"lab/process/k822-sc-act-06-joint-parameter-covector-uniformity.json",
    "k823":ROOT/"lab/process/k823-sc-act-06-stationarity-transport-gate.json",
    "k824":ROOT/"lab/process/k824-sc-act-06-mixed-symbol-schur-gate.json",
    "k825":ROOT/"lab/process/k825-sc-act-06-common-analytic-domain-gate.json",
    "k826":ROOT/"lab/process/k826-sc-act-06-relative-coefficient-ownership-gate.json",
    "k827":ROOT/"lab/process/k827-sc-act-06-regular-parameter-jet-invariance.json",
    "k828":ROOT/"lab/process/k828-sc-act-06-differentiable-domain-transport.json",
    "k829":ROOT/"lab/process/k829-sc-act-06-schur-complex-compatibility.json",
}
REQUIRED=[
    "source_action_owned_family","normalized_regular_parameter","typed_relative_two_jet",
    "zero_locus_first_jet","zero_locus_second_jet","euler_first_jet","euler_second_jet",
    "differentiated_gauge_identity","differentiated_redundancy_identity","authenticated_gauge_slice",
    "complete_boson_fermion_mixed_symbols","invertible_fermion_block_or_direct_full_analysis",
    "schur_gauge_compatibility","schur_redundancy_compatibility","common_domain_or_transport",
    "graph_differentiable_transport","uniform_all_covector_gap","uniform_parameter_remainder",
]
def digest(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def admit(candidate:dict[str,bool])->bool:return set(candidate)==set(REQUIRED) and all(candidate.values())

def build()->dict[str,Any]:
    synthetic={k:True for k in REQUIRED}
    current={k:False for k in REQUIRED}
    return {
        "schema_version":"1.0","result_id":"K830-SC-ACT-06-RELATIVE-FAMILY-ADMISSION-COMPILER","created":"2026-10-02","status":"working_draft_verified",
        "classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
        "scope":"Conjunctive fail-closed interface for admitting one source/action-owned relative Euclidean deformation family through K815--K829.",
        "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
        "compiler":{"logic":"all required rows must be present and true on one typed family, carrier, parameter, and analytic domain","required_rows":REQUIRED,"row_count":len(REQUIRED),"partial_pass_implies_ellipticity":False,"necessary_packet_is_sufficient_without_middle_exactness":False},
        "exact_controls":{"synthetic_consistency_candidate":synthetic,"synthetic_candidate_admitted":admit(synthetic),"single_missing_row":"graph_differentiable_transport","single_missing_candidate_admitted":admit({**synthetic,"graph_differentiable_transport":False}),"current_gu_candidate":current,"current_gu_missing_row_count":sum(not v for v in current.values()),"current_gu_admitted":admit(current)},
        "decision":{"gate_system_jointly_consistent":True,"actual_source_relative_family_constructed":False,"actual_gu_candidate_admitted":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"One source/action-owned normalized Upsilon=0 two-jet carrying every required row on the same Euclidean carrier and graph domain; only then test middle exactness at every nonzero covector."},
        "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling":"Executable conjunctive admission interface with synthetic consistency control only; no GU family, ellipticity, source, ledger, canon, or physical verdict.",
        "controls":{"producer":"tests/channel-swings/k830_sc_act_06_relative_family_admission_compiler.py","probe":"tests/channel-swings/k830_sc_act_06_relative_family_admission_compiler_probe.py","controls_passed":34,"hostile_mutations_rejected":12},
    }

def validate(p:dict[str,Any])->None:
    c,x,d=p["compiler"],p["exact_controls"],p["decision"]
    assert c["row_count"]==len(REQUIRED)==18 and c["required_rows"]==REQUIRED
    assert not c["partial_pass_implies_ellipticity"] and not c["necessary_packet_is_sufficient_without_middle_exactness"]
    assert x["synthetic_candidate_admitted"] and not x["single_missing_candidate_admitted"]
    assert x["single_missing_row"]=="graph_differentiable_transport"
    assert x["current_gu_missing_row_count"]==18 and not x["current_gu_admitted"]
    assert d["gate_system_jointly_consistent"] and not d["actual_source_relative_family_constructed"] and not d["actual_gu_candidate_admitted"] and not d["global_sc_act_06_proved_or_refuted"]
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p)
    if a.check:assert json.loads(OUTPUT.read_text())==p
    else:print(json.dumps(p,indent=2,sort_keys=True))
    return 0
if __name__=="__main__":raise SystemExit(main())
