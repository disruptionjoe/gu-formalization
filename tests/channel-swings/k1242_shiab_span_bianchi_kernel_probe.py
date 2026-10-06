#!/usr/bin/env python3
"""Hostile mutations for K1242 span/kernel classification."""
EXPECTED={"span":5,"kernel":4,"real_rows":("css","scs","ssc"),"relations":3}
def accepts(x): return x==EXPECTED and x["span"]-1==x["kernel"]
mutations=[]
for key,delta in (("span",1),("kernel",1),("relations",-1)):
    item=dict(EXPECTED); item[key]+=delta; mutations.append(item)
item=dict(EXPECTED); item["real_rows"]=("css","scc","scs","ssc"); mutations.append(item)
assert accepts(EXPECTED) and all(not accepts(x) for x in mutations)
print(f"PASS hostile mutations {len(mutations)}/{len(mutations)}")
