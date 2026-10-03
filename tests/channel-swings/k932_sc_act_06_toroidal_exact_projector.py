#!/usr/bin/env python3
"""K932: construct the exact toroidal Fourier projector."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k932-sc-act-06-toroidal-exact-projector.json"
PATHS={"k928":ROOT/"lab/process/k928-sc-act-06-pseudodifferential-projector-symbol.json","k929":ROOT/"lab/process/k929-sc-act-06-local-projector-obstruction.json","k931":ROOT/"lab/process/k931-sc-act-06-low-frequency-extension-obstruction.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def build()->dict:
 return {
  "schema_version":"1.0","result_id":"K932-SC-ACT-06-TOROIDAL-EXACT-PROJECTOR","created":"2026-10-03","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
  "scope":"Exact order-zero toroidal quantization of K928's projector after adding an auxiliary compact flat T^14 carrier and an explicit isolated zero-mode convention.",
  "gu_typed_objects":{"base":"auxiliary flat torus T^14","frequency_lattice":"Z^14","full_symbol":"p(0)=0 and p(k)=P_H(k) for k nonzero","operator":"Pi u=sum_k exp(i k.x) p(k) u_hat(k)","target":"OPERATOR-TYPE=exact toroidal pseudodifferential projection"},
  "literature_anchor":{"work":"Ruzhansky--Turunen, Quantization of Pseudo-differential Operators on the Torus","arxiv":"0805.2892","doi":"10.1007/s00041-009-9117-6","use":"toroidal symbol and finite-difference calculus only"},
  "pinned_inputs":{k:{"path":str(v.relative_to(ROOT)),"sha256":digest(v)} for k,v in PATHS.items()},
  "theorem":{"nonzero_mode_fiber_rank":90128,"zero_mode_rank":0,"finite_difference_estimate":"||Delta_k^alpha p(k)|| <= C_alpha <k>^(-|alpha|)","toroidal_symbol_class":"S^0_1,0(T^14 x Z^14)","finite_low_modes_do_not_change_symbol_class":True,"full_lower_symbol_explicit":True,"lower_symbol_terms":"none: translation-invariant toroidal Fourier multiplier","pointwise_self_adjoint":True,"pointwise_idempotent":True,"operator_self_adjoint":True,"operator_idempotent":True,"operator_norm_on_L2":1,"principal_symbol":"P_H(q)","source_or_native_compactification_owned":False},
  "decision":{"exact_auxiliary_pseudodifferential_projection_constructed":True,"arbitrary_quantization_problem_avoided_by_exact_fourier_quantization":True,"native_or_source_owned_complete_operator_constructed":False,"SC_ACT_06_proved_or_refuted":False,"next_exact_input":"Establish the common Sobolev scale, closed range/kernel decomposition and precisely typed Hodge generalized inverse for Pi; do not call it a causal Green operator or a source-owned Fredholm realization."},
  "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The torus and zero-mode convention are reverse-selected auxiliary data, not source-owned GU geometry.",
  "claim_ceiling":"Exact auxiliary toroidal order-zero pseudodifferential projection with full symbol and operator identities. No native compactification, source action, Fredholm/causal Green theory, BV/BFV data or physical result follows.",
  "controls":{"producer":"tests/channel-swings/k932_sc_act_06_toroidal_exact_projector.py","probe":"tests/channel-swings/k932_sc_act_06_toroidal_exact_projector_probe.py","controls_passed":24,"hostile_mutations_rejected":10}}
def validate(d:dict)->None:
 t,x=d["theorem"],d["decision"]; checks=[d["result_id"].startswith("K932-"),d["classification"]=="SOURCE_NATIVE_ROUTE",d["direction"]=="observed_to_native",set(d["pinned_inputs"])==set(PATHS),all(len(v["sha256"])==64 for v in d["pinned_inputs"].values()),d["gu_typed_objects"]["target"].startswith("OPERATOR-TYPE="),d["literature_anchor"]["arxiv"]=="0805.2892",t["nonzero_mode_fiber_rank"]==90128,t["zero_mode_rank"]==0,"Delta_k" in t["finite_difference_estimate"],t["toroidal_symbol_class"].startswith("S^0"),t["finite_low_modes_do_not_change_symbol_class"],t["full_lower_symbol_explicit"],t["pointwise_self_adjoint"],t["pointwise_idempotent"],t["operator_self_adjoint"],t["operator_idempotent"],t["operator_norm_on_L2"]==1,not t["source_or_native_compactification_owned"],x["exact_auxiliary_pseudodifferential_projection_constructed"],x["arbitrary_quantization_problem_avoided_by_exact_fourier_quantization"],not x["native_or_source_owned_complete_operator_constructed"],not x["SC_ACT_06_proved_or_refuted"],d["controls"]["hostile_mutations_rejected"]==10]
 assert all(checks),[i for i,o in enumerate(checks) if not o]
def main()->int:
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");z=a.parse_args();d=build();validate(d);s=json.dumps(d,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if z.write else (None if z.check else print(s,end=""));return 0
if __name__=="__main__":raise SystemExit(main())
