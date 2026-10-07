#!/usr/bin/env python3
"""Exact finite-mode controls for K1336's Hilbert-valued KG domain."""
import hashlib,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1336-hilbert-valued-klein-gordon-domain.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; S=D["spectrum"]; Q=D["decision"]
check("ultrastatic 3+1 control",C["spacetime"].startswith("R_t x T3_x"))
check("internal principal series",C["internal_hilbert_space"].startswith("H_ps=L2(K/M)"))
check("tensor one-particle space",C["one_particle_space"]=="H=L2(T3;H_ps)")
check("positive mass",C["mass_condition"]=="m>0")
check("operator domain",C["operator_domain"]=="D(A_m)=H2(T3;H_ps)")
check("form domain",C["form_domain"]=="D(A_m^(1/2))=H1(T3;H_ps)")
m2=Fraction(9,4); modes=[(a,b,c) for a in range(-3,4) for b in range(-2,3) for c in range(-1,2)]
vals=[Fraction(a*a+b*b+c*c)+m2 for a,b,c in modes]
check("mode census",len(vals)==105)
check("strict modal positivity",all(v>0 for v in vals))
check("sharp lower mode",min(vals)==m2)
check("unique zero momentum minimum",sum(v==m2 for v in vals)==1)
check("declared spectrum",S["eigenvalue"]=="omega_k^2=|k|^2+m^2")
check("self-adjoint declaration",S["self_adjoint"])
check("zero kernel",S["kernel_dimension"]==0)
check("domain constructed",Q["common_local_operator_domain_constructed"] and Q["positive_self_adjoint_spatial_operator_constructed"])
check("physical ceiling",not Q["gu_action_owned"] and not Q["interacting"] and not Q["physical_quotient_constructed"])
assert n==17; print("RESULT: PASS 17/17")
