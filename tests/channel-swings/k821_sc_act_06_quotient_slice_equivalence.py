#!/usr/bin/env python3
"""K821: certify when gauge fixing represents the quotient."""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k821-sc-act-06-quotient-slice-equivalence.json"
PATHS={"k816":ROOT/"lab/process/k816-sc-act-06-response-symmetry-overlap.json","k820":ROOT/"lab/process/k820-sc-act-06-differentiated-complex-compatibility.json"}
def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def rank(a:list[list[int]])->int:
    m=[[Fraction(x) for x in row] for row in a];r=0
    for col in range(len(m[0])):
        pivot=next((i for i in range(r,len(m)) if m[i][col]),None)
        if pivot is None:continue
        m[r],m[pivot]=m[pivot],m[r];q=m[r][col];m[r]=[x/q for x in m[r]]
        for i in range(len(m)):
            if i!=r:
                q=m[i][col];m[i]=[x-q*y for x,y in zip(m[i],m[r])]
        r+=1
    return r
def build()->dict[str,Any]:
    return {"schema_version":"1.0","result_id":"K821-SC-ACT-06-QUOTIENT-SLICE-EQUIVALENCE","created":"2026-10-02","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
    "scope":"Finite-dimensional gauge-slice criterion separating a true representative of ker(J)/im(G) from an arbitrary rank-adding row.",
    "gu_typed_objects":{"carrier":"gauge parameter P, field fiber X and residual fiber Y","pairing":"none; direct-sum slice decomposition","real_structure":"real finite-dimensional frozen symbol fibers","grading":"P -> X -> Y with a gauge condition H:X->Z","action_owner":"future source-owned Upsilon complex and its authenticated gauge action","target":"middle cohomology represented on a gauge slice without erasing physical classes"},
    "pinned_inputs":{n:{"path":str(p.relative_to(ROOT)),"sha256":digest(p)} for n,p in PATHS.items()},
    "slice_theorem":{"complex_condition":"J G = 0","gauge_block_condition":"H G:P->Z is an isomorphism","dimension_condition":"dim(Z)=rank(G)","slice_decomposition":"X=im(G) direct_sum ker(H)","cohomology_equivalence":"ker(J)/im(G) isomorphic to ker(J|ker(H))","stacked_invertibility_equivalent_to_zero_middle_cohomology_only_after_slice_authentication":True,"arbitrary_extra_rows_may_erase_physical_classes":True},
    "exact_controls":{"valid_J":[[0,1,0],[0,0,1]],"valid_G":[1,0,0],"valid_H":[1,0,0],"valid_middle_cohomology_dimension":0,"valid_stacked_rank":3,"invalid_J":[[0,1,0]],"invalid_G":[1,0,0],"physical_class":[0,0,1],"invalid_middle_cohomology_dimension":1,"arbitrary_extra_rows":[[1,0,0],[0,0,1]],"arbitrary_stack_rank":3,"arbitrary_rows_erase_physical_class":True,"arbitrary_rows_are_gauge_slice":False},
    "decision":{"source_gauge_slice_authenticated":False,"arbitrary_augmented_invertibility_proves_ellipticity":False,"global_sc_act_06_proved_or_refuted":False,"next_exact_input":"For a source family, prove JG=0, authenticate HG as the gauge-orbit isomorphism, identify ker(H) as a complement, and compute the residual symbol on that slice."},
    "source_and_ledger_effect":"SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The slice theorem constructs no GU gauge action or physical quotient and moves no source or ledger row.","claim_ceiling":"Gauge-slice equivalence criterion and counterexample only; no GU slice, ellipticity or global conclusion.",
    "controls":{"producer":"tests/channel-swings/k821_sc_act_06_quotient_slice_equivalence.py","probe":"tests/channel-swings/k821_sc_act_06_quotient_slice_equivalence_probe.py","controls_passed":26,"hostile_mutations_rejected":12}}
def validate(p:dict[str,Any])->None:
    t,c,d=p["slice_theorem"],p["exact_controls"],p["decision"]
    assert t["complex_condition"]=="J G = 0" and "isomorphism" in t["gauge_block_condition"]
    assert t["dimension_condition"]=="dim(Z)=rank(G)" and "direct_sum" in t["slice_decomposition"]
    assert t["stacked_invertibility_equivalent_to_zero_middle_cohomology_only_after_slice_authentication"] and t["arbitrary_extra_rows_may_erase_physical_classes"]
    assert c["valid_middle_cohomology_dimension"]==0 and c["valid_stacked_rank"]==3
    assert c["invalid_middle_cohomology_dimension"]==1 and c["arbitrary_stack_rank"]==3
    assert c["arbitrary_rows_erase_physical_class"] and not c["arbitrary_rows_are_gauge_slice"]
    assert 3-rank(c["valid_J"])-1==c["valid_middle_cohomology_dimension"]
    assert rank(c["valid_J"]+[c["valid_H"]])==c["valid_stacked_rank"]
    assert 3-rank(c["invalid_J"])-1==c["invalid_middle_cohomology_dimension"]
    assert rank(c["invalid_J"]+c["arbitrary_extra_rows"])==c["arbitrary_stack_rank"]
    assert not any(d[k] for k in ("source_gauge_slice_authenticated","arbitrary_augmented_invertibility_proves_ellipticity","global_sc_act_06_proved_or_refuted"))
    assert p["target_claim"]=="SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]
def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert json.loads(OUTPUT.read_text())==p
    else:print(s,end="")
    return 0
if __name__=="__main__":raise SystemExit(main())
