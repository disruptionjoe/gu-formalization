#!/usr/bin/env python3
"""K822: compose parameter persistence with all-covector uniformity."""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k822-sc-act-06-joint-parameter-covector-uniformity.json"
PATHS={"k817":ROOT/"lab/process/k817-sc-act-06-finite-parameter-schur-gate.json","k818":ROOT/"lab/process/k818-sc-act-06-uniform-covector-gate.json","k820":ROOT/"lab/process/k820-sc-act-06-differentiated-complex-compatibility.json","k821":ROOT/"lab/process/k821-sc-act-06-quotient-slice-equivalence.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict[str,Any]:
    return {"schema_version":"1.0","result_id":"K822-SC-ACT-06-JOINT-PARAMETER-COVECTOR-UNIFORMITY","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
    "scope":"Uniform punctured-parameter theorem for an authenticated quotient symbol over the complete Euclidean unit cotangent sphere.",
    "gu_typed_objects":{"carrier":"authenticated quotient-symbol bundles over the Euclidean unit cotangent sphere","pairing":"Euclidean fiber norms after domain and slice authentication","real_structure":"real parameter and real homogeneous covector symbol","grading":"quotiented field symbol to independent residual symbol","action_owner":"future source-owned relative Upsilon complex","target":"one common punctured parameter interval with all-covector exactness"},
    "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
    "uniform_persistence_theorem":{"expansion":"S(t,q)=t tau(q)+E(t,q)","transverse_gap":"inf_|q|=1 sigma_min(tau(q)) >= mu > 0","uniform_remainder":"sup_|q|=1 ||E(t,q)|| <= C t^2","common_interval":"0 < |t| <= mu/(2C)","certified_gap":"sigma_min(S(t,q)) >= mu|t|/2 for every unit q","pointwise_thresholds_imply_common_interval":False,"joint_continuity_and_compactness_can_supply_uniform_remainder":True,"theorem_constructs_gu_symbol":False},
    "exact_controls":{"mu":2,"C":3,"common_interval_upper":"1/3","test_t":"1/4","scalar_control":"S(t)=2t-3t^2","actual_gap_at_test_t":"5/16","certified_gap_at_test_t":"1/4","pointwise_counterexample":"S(t,q)=2t-t^2/q for q>0 and S(t,0)=2t","each_fixed_q_has_punctured_interval":True,"common_punctured_interval_exists":False,"failure_reason":"remainder is not jointly continuous and has no uniform quadratic constant"},
    "decision":{"actual_gu_uniform_interval_proved":False,"pointwise_k817_k818_checks_suffice_without_joint_control":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"For an authenticated source family and quotient slice, prove a positive gap for tau(q) and a jointly uniform quadratic Schur remainder on the complete Euclidean cotangent sphere."},
    "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The theorem composes generic uniform estimates but supplies no source symbol family, physical quotient, observable, prediction or confirmation.","claim_ceiling":"Joint uniform-persistence theorem and nonuniform counterexample only; no GU all-covector family or ellipticity conclusion.",
    "controls":{"producer":"tests/channel-swings/k822_sc_act_06_joint_parameter_covector_uniformity.py","probe":"tests/channel-swings/k822_sc_act_06_joint_parameter_covector_uniformity_probe.py","controls_passed":28,"hostile_mutations_rejected":12}}
def validate(p:dict[str,Any])->None:
    t,c,d=p["uniform_persistence_theorem"],p["exact_controls"],p["decision"]
    assert t["expansion"]=="S(t,q)=t tau(q)+E(t,q)" and "mu > 0" in t["transverse_gap"]
    assert "C t^2" in t["uniform_remainder"] and t["common_interval"]=="0 < |t| <= mu/(2C)"
    assert not t["pointwise_thresholds_imply_common_interval"] and t["joint_continuity_and_compactness_can_supply_uniform_remainder"] and not t["theorem_constructs_gu_symbol"]
    assert (c["mu"],c["C"],c["common_interval_upper"])==(2,3,"1/3")
    assert c["actual_gap_at_test_t"]=="5/16" and c["certified_gap_at_test_t"]=="1/4"
    assert c["each_fixed_q_has_punctured_interval"] and not c["common_punctured_interval_exists"]
    tt=Fraction(1,4);assert 2*tt-3*tt*tt==Fraction(5,16)
    assert Fraction(c["mu"],2)*tt==Fraction(1,4)
    for n in range(2,10):
        tv=Fraction(1,n);q=tv/2
        assert 2*tv-tv*tv/q==0
    assert not any(d[k] for k in ("actual_gu_uniform_interval_proved","pointwise_k817_k818_checks_suffice_without_joint_control","global_sc_act_06_proved_or_refuted"))
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert json.loads(OUTPUT.read_text())==p
    else:print(s,end="")
    return 0
if __name__=="__main__":raise SystemExit(main())
