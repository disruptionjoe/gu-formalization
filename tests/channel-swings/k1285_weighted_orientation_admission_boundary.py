#!/usr/bin/env python3
"""Integrated controls for K1285."""
import json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1285-weighted-orientation-admission-boundary.json").read_text()); n=0
def c(label,x):
    global n; assert x,label; n+=1; print(f"PASS {n:02d}: {label}")
rows=D["certificate"]["rows"]; counts={s:sum(r["state"]==s for r in rows) for s in ("satisfied","excluded","conditional","missing")}
c("id",D["result_id"]=="K1285-WEIGHTED-ORIENTATION-ADMISSION-BOUNDARY")
c("twenty-seven rows",len(rows)==27)
for s in counts: c(s,counts[s]==D["certificate"][s+"_count"])
c("K1145 zero",D["certificate"]["k1145_pass_count"]==0)
c("K1150 zero",D["certificate"]["k1150_pass_count"]==0)
c("internal closed",D["decision"]["internal_homogeneous_spurion_route_closed_in_scope"] is True)
c("external open",D["decision"]["external_nonhomogeneous_boundary_Green_singular_and_component_routes_open"] is True)
assert n==10; print("RESULT: PASS 10/10")
