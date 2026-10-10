#!/usr/bin/env python3
"""Hostile mutations for K1653."""
import copy
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q,z=d.get("localization",{}),d.get("decision",{})
    return all([
        d.get("claim_id")=="K1653",
        "complete d_N=Theta(N^3) cube" in q.get("normalized_channel",""),
        "fixed a>0" in q.get("normalized_channel",""),
        "Disjoint adjacent-pair averages" in q.get("shift_estimator",""),
        "O(N^(-1))" in q.get("phase_estimator",""),
        "O_(g,eta)(N^3)" in q.get("prediction_bound",""),
        "C_(F,N)-O_(g,eta)(N^3)" in q.get("score_saturation",""),
        z.get("unrestricted_coercivity_proved") is False,
        z.get("protected_status_change") is False,
    ])


def main():
    s=json.loads((ROOT/"lab/process/k1653-translation-phase-posterior-localization.json").read_text());assert valid(s)
    changes=[(("claim_id",),"K1652"),(("localization","normalized_channel"),"sparse unknown support"),(("localization","shift_estimator"),"overlapping unbounded pairs"),(("localization","phase_estimator"),"O(1)"),(("localization","prediction_bound"),"O(N^4)"),(("localization","score_saturation"),"upper bound only"),(("decision","unrestricted_coercivity_proved"),True),(("decision","protected_status_change"),True)]
    for i,(path,value) in enumerate(changes,1):
        m=copy.deepcopy(s);cur=m
        for k in path[:-1]:cur=cur[k]
        cur[path[-1]]=value;assert not valid(m),i;print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")
if __name__=="__main__":main()
