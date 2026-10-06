#!/usr/bin/env python3
"""Hostile mutations for K1244 admission audit."""
EXPECTED={"k1145":0,"k1150":0,"owned":False,"defect":13}
def accepts(x): return x==EXPECTED and not x["owned"]
mut=[]
for key in ("k1145","k1150","defect"): item=dict(EXPECTED); item[key]+=1; mut.append(item)
item=dict(EXPECTED); item["owned"]=True; mut.append(item)
assert accepts(EXPECTED) and all(not accepts(x) for x in mut)
print(f"PASS hostile mutations {len(mut)}/{len(mut)}")
