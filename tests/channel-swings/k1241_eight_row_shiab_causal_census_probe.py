#!/usr/bin/env python3
"""Hostile mutations for the K1241 eight-row causal census."""
EXPECTED = {"ccc":(122878,122878,114688),"ccs":(131070,131070,122880),"csc":(131070,131070,122748),"css":(130912,130912,122746),"scc":(40956,40956,40956),"scs":(32764,32764,32764),"ssc":(32764,32764,32764),"sss":(32766,32766,32766)}
def accepts(item): return item == EXPECTED and len(item) == 8
mutations=[]
for key in EXPECTED:
    item=dict(EXPECTED); values=list(item[key]); values[len(mutations)%3]+=1; item[key]=tuple(values); mutations.append(item)
item=dict(EXPECTED); del item["sss"]; mutations.append(item)
assert accepts(EXPECTED) and all(not accepts(item) for item in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
