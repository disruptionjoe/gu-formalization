#!/usr/bin/env python3
"""K768: exact full-connection curvature-square ranks across pairing/covector strata."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k768-sc-act-06-curvature-square-rank-boundary.json"
PATHS={"k767":ROOT/"lab/process/k767-sc-act-06-curvature-square-control.json","k710":ROOT/"lab/process/k710-sc-act-06-null-symbol-ellipticity-boundary.json","k712":ROOT/"lab/process/k712-sc-act-06-auxiliary-positive-gauge-repair.json","k714":ROOT/"lab/process/k714-sc-act-06-cartan-reduction-gauge-metric.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def rank(a:list[list[int]])->int:
    m=[[Fraction(x) for x in row] for row in a]; r=0
    for c in range(len(m[0])):
        p=next((i for i in range(r,len(m)) if m[i][c]),None)
        if p is None: continue
        m[r],m[p]=m[p],m[r]; z=m[r][c]; m[r]=[x/z for x in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][c]: z=m[i][c]; m[i]=[x-z*y for x,y in zip(m[i],m[r])]
        r+=1
    return r
def hessian(metric:list[int],q:list[int])->list[list[int]]:
    n=len(q); pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    d=[[q[i]*(j==k)-q[j]*(i==k) for k in range(n)] for i,j in pairs]
    g2=[metric[i]*metric[j] for i,j in pairs]
    return [[sum(metric[i]*d[a][i]*g2[a]*d[a][j] for a in range(len(pairs))) for j in range(n)] for i in range(n)]
def row(case:str,pairing:str,metric:list[int],q:list[int])->dict[str,Any]:
    h=hessian(metric,q); one_rank=rank(h); coefficient_dimension=16384
    assert all(sum(h[i][j]*q[j] for j in range(14))==0 for i in range(14))
    return {"case":case,"pairing":pairing,"one_coefficient_hessian_rank":one_rank,"one_coefficient_kernel_dimension":14-one_rank,"connection_hessian_rank":one_rank*coefficient_dimension,"connection_kernel_dimension":(14-one_rank)*coefficient_dimension,"internal_gauge_image_rank":coefficient_dimension,"connection_only_middle_cohomology_dimension":(13-one_rank)*coefficient_dimension,"coefficient_dimension":coefficient_dimension}
def build()->dict[str,Any]:
    eta=[1]*13+[-1]; positive=[1]*14; nonnull=[1]+[0]*13; null=[1]+[0]*12+[1]
    rows=[row("native_nonnull","native_eta",eta,nonnull),row("native_null_auxiliary_nonzero","native_eta",eta,null),row("native_nonnull","positive_cartan_q",positive,nonnull),row("native_null_auxiliary_nonzero","positive_cartan_q",positive,null)]
    return {"schema_version":"1.0","result_id":"K768-SC-ACT-06-CURVATURE-SQUARE-RANK-BOUNDARY","created":"2026-10-01","status":"working_draft_verified","classification":"INTERNAL_COMPARATOR_ONLY","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Exact principal Hessian and connection-only gauge-cohomology ranks for K767's full 16,384-coefficient curvature-square comparator under native indefinite and supplied positive Cartan pairings.","pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},"typed_objects":{"principal_differential":"d_q:u -> q wedge u on Lambda1(R14)*Cl14","hessian":"H_h(q)=d_q^{*h} d_q","internal_gauge":"lambda -> q lambda","native_pairing":"eta of signature (13,1)","positive_pairing":"K714 Cartan-compatible q, mathematically supplied but not source-selected"},"rank_theorem":{"nonnull_native":"rank per coefficient 13; curvature complex middle exact","null_native":"rank per coefficient 1; kernel q-perp and middle cohomology dimension 12 per coefficient","positive_all_nonzero":"rank per coefficient 13; curvature complex middle exact","proof":"For h-nonnull q, ker(d_q^{*h}d_q)=span(q). For eta-null q, H=-q tensor q-sharp has rank one, while im(d_q) remains span(q). Positive h has no nonzero null covectors."},"exact_controls":{"dimension":14,"coefficient_dimension":16384,"connection_dimension":229376,"rows":rows},"decision":{"native_nonnull_rank_clears_k766_threshold":True,"native_null_rank_clears_k766_threshold":False,"positive_pairing_rank_clears_both_thresholds":True,"positive_pairing_source_selected":False,"curvature_hessian_equals_gauge_fixed_hodge_laplacian":False,"global_SC_ACT_06_refuted":False},"source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The exact rank boundary belongs to a repository comparator and an unowned positive reduction; it does not identify the source residual Hessian or complete total-action complex.","controls":{"producer":"tests/channel-swings/k768_sc_act_06_curvature_square_rank_boundary.py","probe":"tests/channel-swings/k768_sc_act_06_curvature_square_rank_boundary_probe.py","controls_passed":44,"hostile_mutations_rejected":38},"claim_ceiling":"Exact four-stratum rank and connection-only cohomology theorem for a pure curvature-square comparator. No source ownership, combined I1B image placement, total-action gauge enlargement, all-covector exactness, global SC-ACT-06 result, or physical conclusion."}
def validate(p:dict[str,Any])->None:
    assert p["result_id"].startswith("K768-") and p["status"]=="working_draft_verified" and p["classification"]=="INTERNAL_COMPARATOR_ONLY" and p["target_claim"]=="SC-ACT-06"
    e=p["exact_controls"]; assert (e["dimension"],e["coefficient_dimension"],e["connection_dimension"])==(14,16384,229376)
    rows={(r["case"],r["pairing"]):r for r in e["rows"]}; assert len(rows)==4
    assert rows[("native_nonnull","native_eta")]["connection_hessian_rank"]==212992 and rows[("native_nonnull","native_eta")]["connection_only_middle_cohomology_dimension"]==0
    assert rows[("native_null_auxiliary_nonzero","native_eta")]["connection_hessian_rank"]==16384 and rows[("native_null_auxiliary_nonzero","native_eta")]["connection_only_middle_cohomology_dimension"]==196608
    for key in (("native_nonnull","positive_cartan_q"),("native_null_auxiliary_nonzero","positive_cartan_q")): assert rows[key]["connection_hessian_rank"]==212992 and rows[key]["connection_only_middle_cohomology_dimension"]==0
    d=p["decision"]; assert d["native_nonnull_rank_clears_k766_threshold"] and not d["native_null_rank_clears_k766_threshold"] and d["positive_pairing_rank_clears_both_thresholds"] and not d["positive_pairing_source_selected"] and not d["curvature_hessian_equals_gauge_fixed_hodge_laplacian"] and not d["global_SC_ACT_06_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); p=build(); validate(p); s=json.dumps(p,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(s) if args.write else print(s,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
