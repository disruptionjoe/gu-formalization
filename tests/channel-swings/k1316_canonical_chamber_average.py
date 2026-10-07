#!/usr/bin/env python3
"""Exact controls for K1316's finite chamber-average projection."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1316-canonical-chamber-average.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; Q=D["decision"]; N=8; d=3
x=[[float((c+1)*(j+2)%7-3) for j in range(d)] for c in range(N)]
avg=[sum(x[c][j] for c in range(N))/N for j in range(d)]; px=[avg[:] for _ in range(N)]
avg2=[sum(px[c][j] for c in range(N))/N for j in range(d)]; ppx=[avg2[:] for _ in range(N)]
inner=lambda a,b:sum(a[c][j]*b[c][j] for c in range(N) for j in range(d))
y=[[float((2*c+3*j)%5-2) for j in range(d)] for c in range(N)]
ay=[sum(y[c][j] for c in range(N))/N for j in range(d)]; py=[ay[:] for _ in range(N)]
check("D7 chamber count",C["chamber_count"]==2**6*math.factorial(7)==322560)
check("idempotence fixture",ppx==px and C["idempotent"])
check("self adjoint fixture",abs(inner(px,y)-inner(x,py))<1e-12 and C["self_adjoint"])
check("positive fixture",inner(x,px)>=-1e-12 and C["positive_contraction"])
check("contraction fixture",inner(px,px)<=inner(x,x)+1e-12)
const=[[2.0,-1.0,3.0] for _ in range(N)]
check("norm one fixture",abs(inner(const,const)-inner([[sum(const[c][j] for c in range(N))/N for j in range(d)] for _ in range(N)],const))<1e-12 and C["operator_norm"]==1)
check("chamber rank one",C["chamber_factor_rank"]==1)
check("raw multiplicity source",C["raw_multiplicity_reduced_from"]==322560)
check("raw multiplicity target",C["raw_multiplicity_reduced_to"]==1)
check("average exists",Q["canonical_finite_Hilbert_average_exists_after_identifications"])
check("not automatic G descent",not Q["average_is_automatically_G_equivariant"])
check("no chamber selection",not Q["average_selects_one_chamber"])
check("no physical selection",not Q["average_selects_charge_or_physical_sector"] and not Q["source_or_physical_status_moves"])
assert n==15; print("RESULT: PASS 15/15")
