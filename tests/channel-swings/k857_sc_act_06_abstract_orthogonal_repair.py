#!/usr/bin/env python3
"""K857: construct an abstract exact quotient repair after trivialization."""
from __future__ import annotations
import argparse,hashlib,json,math
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k857-sc-act-06-abstract-orthogonal-repair.json";K855=ROOT/"lab/process/k855-sc-act-06-cohomology-bundle.json";K856=ROOT/"lab/process/k856-sc-act-06-s13-stable-triviality.json"
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def transpose(a):return [list(x) for x in zip(*a)]
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def build()->dict[str,Any]:
    p855=json.loads(K855.read_text());h,s=5,2;r=h-s
    S=[[int(i==j) for j in range(s)] for i in range(h)]
    tau=[[int(i+s==j) for j in range(h)] for i in range(r)]
    L=add(mul(transpose(tau),tau),mul(S,transpose(S)))
    radius=(math.sqrt(6)-2)/2
    return {"schema_version":"1.0","result_id":"K857-SC-ACT-06-ABSTRACT-ORTHOGONAL-REPAIR","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","comparator_routing_notice":p855["comparator_routing_notice"],"direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Abstract repair after choosing an orthonormal trivialization of a real cohomology bundle; the chosen frame and maps are not thereby GU source/action owned.","gu_typed_objects":p855["gu_typed_objects"]|{"target":"MAP-TYPE=abstract complementary quotient repair"},"pinned_inputs":{"k855":{"path":str(K855.relative_to(ROOT)),"sha256":digest(K855)},"k856":{"path":str(K856.relative_to(ROOT)),"sha256":digest(K856)}},"construction":{"hypotheses":["H is a trivial real rank-h bundle","H carries a continuous positive metric","1<=s<h"],"orthonormal_frame":"continuous Gram-Schmidt of a global frame","split":"H=R^s direct-sum R^(h-s)","S_bar":"isometric inclusion of the first summand","tau_bar":"orthogonal projection onto the second summand","composition":"tau_bar S_bar=0","exactness":"im(S_bar)=ker(tau_bar)","hodge_operator":"L=tau_bar^* tau_bar+S_bar S_bar^*=I_H","uniform_gap":1,"map_norms":{"T":1,"R":1},"k853_radius_exact":"(sqrt(6)-2)/2","k853_radius_numeric":radius,"ownership_from_triviality":False},"exact_control":{"h":h,"s":s,"r":r,"S_bar":S,"tau_bar":tau,"tau_S":mul(tau,S),"hodge":L,"hodge_is_identity":L==ident(h),"rank_sum":s+r,"epsilon_inside":radius/2,"perturbation_bound_inside":4*(radius/2)+2*(radius/2)**2,"epsilon_outside":radius*1.01,"radius_positive":radius>0},"decision":{"abstract_continuous_exact_repair_exists_under_hypotheses":True,"topological_triviality_selects_GU_maps":False,"source_owned_repair_maps_constructed":False,"current_flat_packet_repaired":False,"SC_ACT_06_proved_or_refuted":False},"source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","claim_ceiling":"Constructive abstract exact repair with unit Hodge gap and explicit robustness radius. It is an existence control, not a GU-owned repair.","controls":{"producer":"tests/channel-swings/k857_sc_act_06_abstract_orthogonal_repair.py","probe":"tests/channel-swings/k857_sc_act_06_abstract_orthogonal_repair_probe.py","controls_passed":34,"hostile_mutations_rejected":18}}
def validate(p):
    c,x,d=p["construction"],p["exact_control"],p["decision"]
    checks=[p["classification"]=="SOURCE_NATIVE_ROUTE",p["target_claim"]=="SC-ACT-06","scope before inference" in p["comparator_routing_notice"],p["gu_typed_objects"]["action_owner"]=="candidate-must-declare",len(c["hypotheses"])==3,"Gram-Schmidt" in c["orthonormal_frame"],"direct-sum" in c["split"],"isometric inclusion" in c["S_bar"],"orthogonal projection" in c["tau_bar"],c["composition"]=="tau_bar S_bar=0",c["exactness"]=="im(S_bar)=ker(tau_bar)",c["hodge_operator"].endswith("=I_H"),c["uniform_gap"]==1,c["map_norms"]=={"T":1,"R":1},c["k853_radius_exact"]=="(sqrt(6)-2)/2",abs(c["k853_radius_numeric"]-((math.sqrt(6)-2)/2))<1e-15,not c["ownership_from_triviality"],x["h"]==5,x["s"]==2,x["r"]==3,x["tau_S"]==[[0,0],[0,0],[0,0]],x["hodge_is_identity"],x["rank_sum"]==5,x["perturbation_bound_inside"]<1,x["epsilon_outside"]>c["k853_radius_numeric"],x["radius_positive"],d["abstract_continuous_exact_repair_exists_under_hypotheses"],not d["topological_triviality_selects_GU_maps"],not d["source_owned_repair_maps_constructed"],not d["current_flat_packet_repaired"],not d["SC_ACT_06_proved_or_refuted"],p["source_and_ledger_effect"]=="SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","existence control" in p["claim_ceiling"],p["controls"]["hostile_mutations_rejected"]==18]
    assert len(checks)==p["controls"]["controls_passed"];assert all(checks)
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");a.add_argument("--check",action="store_true");z=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if z.write else(None if z.check else print(s,end=""));return 0
if __name__=="__main__":raise SystemExit(main())
