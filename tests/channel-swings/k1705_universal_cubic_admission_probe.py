#!/usr/bin/env python3
"""Hostile mutations for K1705."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def valid(d):
    a,o,q=d.get("admission",{}),d.get("open_frontier",{}),d.get("decision",{})
    return all([d.get("claim_id")=="K1705",a.get("new_rows")==["K1701","K1702","K1703","K1704","K1705"],
        "420 rows" in a.get("census",""),"SC-ACT-01/02/06 remain ASSERTS" in a.get("source_claims",""),
        "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in a.get("physics_ledger",""),
        a.get("apparatus")=="K1145/K1150 remain 0/7.","public posture unchanged" in a.get("protected_surfaces",""),
        "exact scalar Fisher/MMSE" in o.get("finite_strength",""),"growing support" in o.get("uncontrolled_seeds",""),
        "cutoff-uniform" in o.get("haar",""),q.get("source_or_ledger_verdict_moved") is False,
        q.get("physical_admission_closed") is False])


def main():
    src=json.loads((ROOT/"lab/process/k1705-universal-cubic-admission.json").read_text())
    muts=[(('claim_id',),'K1704'),(('admission','new_rows'),['K1701']),(('admission','census'),'wrong'),
        (('admission','source_claims'),'promoted'),(('admission','physics_ledger'),'changed'),(('admission','apparatus'),'7/7'),
        (('admission','protected_surfaces'),'moved'),(('open_frontier','finite_strength'),'closed'),
        (('open_frontier','uncontrolled_seeds'),'closed'),(('open_frontier','haar'),'closed'),
        (('decision','source_or_ledger_verdict_moved'),True),(('decision','physical_admission_closed'),True)]
    assert valid(src)
    for n,(path,val) in enumerate(muts,1):
        d=copy.deepcopy(src); cur=d
        for key in path[:-1]: cur=cur[key]
        cur[path[-1]]=val; assert not valid(d),n; print(f"REJECT {n:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__=="__main__": main()
