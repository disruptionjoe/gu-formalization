#!/usr/bin/env python3
"""Hostile mutations for K1245 integrated boundary."""
EXPECTED={"null_gain":2,"jump_reduction":2,"k1150":"0/7","selected":False}
def accepts(x): return x==EXPECTED and not x["selected"]
mut=[]
for key in ("null_gain","jump_reduction"): item=dict(EXPECTED); item[key]+=1; mut.append(item)
item=dict(EXPECTED); item["k1150"]="1/7"; mut.append(item)
item=dict(EXPECTED); item["selected"]=True; mut.append(item)
assert accepts(EXPECTED) and all(not accepts(x) for x in mut)
print(f"PASS hostile mutations {len(mut)}/{len(mut)}")
