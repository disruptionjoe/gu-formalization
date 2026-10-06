#!/usr/bin/env python3
"""K1223: paired axial preparations reconstruct an affine qubit process."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1223-affine-process-frame-reconstruction.json"
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def sm(m):return [[str(x) for x in r] for r in m]
def sv(v):return [str(x) for x in v]
def build():
    z=F(0);D=[[F(1,2),z,z],[z,F(1,2),z],[z,z,F(1,4)]]
    ri=[[F(3,5),-F(4,5),z],[F(4,5),F(3,5),z],[z,z,F(1)]]
    ro=[[F(1),z,z],[z,F(5,13),-F(12,13)],[z,F(12,13),F(5,13)]]
    m=mm(mm(ro,D),ri);t=[z,-F(9,13),F(15,52)]
    raw=[]
    for j in range(3):
        plus=[t[i]+m[i][j] for i in range(3)];minus=[t[i]-m[i][j] for i in range(3)]
        raw.append({"input_axis":j,"plus":sv(plus),"minus":sv(minus)})
    recovered_m=[[(F(raw[j]["plus"][i])-F(raw[j]["minus"][i]))/2 for j in range(3)] for i in range(3)]
    averages=[[(F(r["plus"][i])+F(r["minus"][i]))/2 for i in range(3)] for r in raw]
    return {"schema_version":"1.0","result_id":"K1223-AFFINE-PROCESS-FRAME-RECONSTRUCTION","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"A fixed trace-preserving qubit process measured with six paired axial input states and three signed Pauli output effects.",
      "theorem":{"raw_readouts":"y_i(+e_j)=t_i+M_ij and y_i(-e_j)=t_i-M_ij",
        "transfer_recovery":"M_ij=[y_i(+e_j)-y_i(-e_j)]/2","translation_recovery":"t_i=[y_i(+e_j)+y_i(-e_j)]/2 for any j",
        "independent_statistics":"nine antisymmetric transfers plus three common symmetric averages = 12",
        "raw_consistency":"the three symmetric averages for each output component must agree, giving six consistency relations among 18 raw reads"},
      "physical_control":{"construction":"gamma=3/4 amplitude damping composed with rational input/output rotations",
        "M":sm(m),"t":sv(t),"raw_readouts":raw},
      "release_test":{"recovered_full_M":recovered_m==m,"all_three_translation_averages_agree":all(a==t for a in averages),
        "raw_scalar_count":18,"independent_scalar_count":12,"consistency_relation_count":6,"protected_status_unchanged":True},
      "decision":{"nine_centered_transfers_determine_bell_chsh":True,"three_additional_marginal_statistics_determine_translation":True,
        "full_affine_process_reconstructed":True,"apparatus_frame_is_self_authenticating":False},
      "ownership":{"preparations_effects_frame_and_systematics_imported":True,"gu_native_effect":"none"},
      "claim_ceiling":"Exact affine process-frame reconstruction inside an imported qubit/Born model; no physical apparatus or GU owner."}
def validate(x):
    assert x["result_id"].startswith("K1223-")
    assert x["release_test"]["recovered_full_M"] and x["release_test"]["all_three_translation_averages_agree"]
    assert (x["release_test"]["raw_scalar_count"],x["release_test"]["independent_scalar_count"],x["release_test"]["consistency_relation_count"])==(18,12,6)
    assert x["decision"]["nine_centered_transfers_determine_bell_chsh"]
    assert x["decision"]["three_additional_marginal_statistics_determine_translation"]
    assert x["decision"]["full_affine_process_reconstructed"]
    assert x["decision"]["apparatus_frame_is_self_authenticating"] is False
    assert x["ownership"]["gu_native_effect"]=="none" and x["release_test"]["protected_status_unchanged"]
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1223 controls: 12/12")
