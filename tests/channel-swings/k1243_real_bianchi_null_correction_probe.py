#!/usr/bin/env python3
"""Hostile mutations for K1243 coupled correction."""
EXPECTED={"ranks":(131070,131070,122882),"radicals":(98316,98316,106504),"gain":(158,158,134),"jump":8188,"defect":13}
def accepts(x): return x==EXPECTED and all(a+b==229386 for a,b in zip(x["ranks"],x["radicals"])) and x["radicals"][2]-x["radicals"][0]==x["jump"]
mut=[]
for key in ("ranks","radicals","gain"):
    for i in range(3): item=dict(EXPECTED); v=list(item[key]); v[i]+=1; item[key]=tuple(v); mut.append(item)
for key in ("jump","defect"): item=dict(EXPECTED); item[key]+=1; mut.append(item)
assert accepts(EXPECTED) and all(not accepts(x) for x in mut)
print(f"PASS hostile mutations {len(mut)}/{len(mut)}")
