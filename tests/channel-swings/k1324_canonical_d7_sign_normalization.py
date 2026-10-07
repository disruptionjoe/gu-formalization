#!/usr/bin/env python3
"""Exhaustive controls for K1324's canonical D7 sign normalizer."""
import hashlib,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1324-canonical-d7-sign-normalization.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
A=D["algorithm"]; E=[tuple(e) for e in A["edge_order"]]
def normalize(bits):
 eps={A["root"]:A["root_sign"]}
 for (u,v),b in zip(E,bits): eps[v]=b*eps[u]
 return tuple(eps[i] for i in range(1,8)),tuple(b*eps[u]*eps[v] for (u,v),b in zip(E,bits))
rows=[normalize(bits) for bits in itertools.product((-1,1),repeat=6)]
check("root fixed",A["root"]==1 and A["root_sign"]==1)
check("tree edge order",len(E)==6)
check("all 64 inputs",len(rows)==64)
check("every output exact",all(out==(1,)*6 for _,out in rows))
check("unique rooted signs",len({eps for eps,_ in rows})==64)
check("fixed exact input",normalize((1,)*6)==((1,)*7,(1,)*6) and A["already_exact_input_is_fixed"])
replay=normalize((1,1,1,1,-1,1)); K=D["k1319_replay"]
check("K1319 signs",list(replay[0])==K["normalizing_signs"])
check("K1319 exact output",list(replay[1])==K["all_normalized_edge_defects"])
check("generator six restored",K["returns_standard_generator_6_sign"])
check("deterministic linear",A["deterministic"] and A["linear_edge_complexity"])
Q=D["decision"]
check("finite algorithm constructed",Q["finite_sign_normalization_constructed"])
check("not source selection",not Q["normalization_is_source_selected_chamber"])
check("analytic ceiling",not Q["analytic_operator_normalization_constructed"])
assert n==15; print("RESULT: PASS 15/15")
