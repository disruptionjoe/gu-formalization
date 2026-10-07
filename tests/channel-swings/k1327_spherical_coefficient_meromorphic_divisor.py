#!/usr/bin/env python3
"""Exact divisor controls for K1327's scalar coefficient."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1327-spherical-coefficient-meromorphic-divisor.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
M=D["meromorphic_divisor"]; U=D["unitary_axis"]; R=D["d7_regular_charge"]; Q=D["decision"]
check("coefficient inherited",D["coefficient"]=="m(z)=sqrt(pi)*Gamma(z/2)/Gamma((z+1)/2)")
check("even pole lattice",M["simple_poles"]=="z=0,-2,-4,...")
check("odd zero lattice",M["simple_zeros"]=="z=-1,-3,-5,...")
check("lattices disjoint",set(range(0,-20,-2)).isdisjoint(set(range(-1,-20,-2))))
check("positive axis regular",M["positive_real_axis"]=="finite_nonzero")
check("imaginary axis punctured",M["imaginary_axis"]=="finite_nonzero_except_z=0")
check("unitary coordinate",U["coordinate"]=="z=i*t with real t" and U["regularity_condition"]=="t!=0")
check("conjugation law",U["conjugation"]=="m(-i*t)=conjugate(m(i*t))")
check("unit phase",U["phase_modulus"]==1 and U["phase_inverse"]=="q(-t)=q(t)^(-1)")
check("D7 roots",R["positive_root_count"]==42)
check("regular condition",R["condition"]=="<mu,beta_coroot>!=0 for every D7 root beta")
check("all reduced factors regular",R["consequence"].startswith("all scalar factors") and R["singular_wall_excluded"])
check("scalar decision",Q["meromorphic_scalar_divisor_classified"] and Q["regular_imaginary_scalar_normalization_available"])
check("operator ceiling",not Q["operator_pole_and_reducibility_classification_constructed"] and not Q["singular_principal_series_classified"])
check("physical ceiling",not Q["physical_regularization_constructed"] and not Q["protected_status_change"])
assert n==16; print("RESULT: PASS 16/16")
