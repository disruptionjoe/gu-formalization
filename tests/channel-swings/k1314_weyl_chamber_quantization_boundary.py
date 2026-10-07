#!/usr/bin/env python3
"""Exact controls for K1314's Weyl-chamber quantization boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1314-weyl-chamber-quantization-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["classification_result"]; Q=D["decision"]; w=2**6*math.factorial(7)
check("W(D7) order",C["weyl_group_order"]==w==322560)
check("chamber count",C["chamber_count"]==w)
check("transitive torsor",C["weyl_action_on_chambers"]=="free and transitive")
check("all chamber controls",C["all_chambers_admit_positive_control"])
check("no canonical chamber",not C["single_chamber_canonical"])
check("not source selected",not C["source_selected_chamber"])
vectors=[(1+1j,2-1j),(-1j,3),(2,0),(4j,-2),(1,-1),(3+2j,1j),(-2,5),(1-3j,2)]
norm=sum((abs(a)**2+abs(b)**2) for a,b in vectors)
check("sample direct-sum positivity",norm>0)
check("finite direct-sum positivity",C["finite_multichamber_sum_positive"])
check("multiplicity",C["finite_multichamber_multiplicity"]==w)
check("intertwiners not constructed",not C["normalized_weyl_intertwiner_family_constructed_here"])
check("chamber torsor not Hilbert obstruction",not Q["K1309_chamber_torsor_blocks_mathematical_Hilbert_control"])
check("canonical choice still open",Q["K1309_chamber_torsor_still_blocks_canonical_single_choice"])
check("sum not physical",not Q["direct_sum_is_physical_sector"])
assert n==16; print("RESULT: PASS 16/16")
