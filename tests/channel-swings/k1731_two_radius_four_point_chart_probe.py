#!/usr/bin/env python3
"""Hostile mutations for K1731 chart scope and formulas."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

def valid(d):
    c=d.get("chart",{}); s=d.get("scope_guard","")
    return all([d.get("claim_id")=="K1731", "b=(1-pa)/(1-p)" in c.get("parameters",""),
        "E[X^2]" in c.get("variance",""), "p a^r" in c.get("even_moments",""),
        "Every symmetric four-point" in c.get("completeness",""), "continuous" in s, "field-valued" in s])

def main():
    d=json.loads((ROOT/"lab/process/k1731-two-radius-four-point-chart.json").read_text()); assert valid(d)
    muts=[]
    for path,val in [(('claim_id',),'K0000'),(('chart','parameters'),'b=1'),(('chart','variance'),'free'),
                     (('chart','even_moments'),'wrong'),(('chart','completeness'),'all laws'),
                     (('scope_guard',),'global optimizer')]:
        x=copy.deepcopy(d); cur=x
        for k in path[:-1]: cur=cur[k]
        cur[path[-1]]=val; muts.append(x)
    for i,x in enumerate(muts,1): assert not valid(x); print(f"REJECT {i:02d}")
    print(f"RESULT: PASS {len(muts)}/{len(muts)} hostile mutations rejected")
if __name__=="__main__": main()
