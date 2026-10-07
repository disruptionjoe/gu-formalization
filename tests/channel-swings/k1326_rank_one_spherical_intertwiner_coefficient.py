#!/usr/bin/env python3
"""Exact reporting controls for K1326's rank-one spherical coefficient."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1326-rank-one-spherical-intertwiner-coefficient.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
R=D["rank_one_model"]; N=D["normalization"]; Q=D["decision"]
check("multiplicity one",R["split_root_multiplicity"]==1)
check("no double root",R["double_root_multiplicity"]==0)
check("root coordinate",R["spectral_coordinate"]=="z=<lambda,alpha_coroot>")
check("spherical exponent",R["spherical_vector"]=="f_z(x)=(1+x^2)^(-(z+1)/2)")
check("convergence half-plane",R["absolute_convergence_half_plane"]=="Re(z)>0")
check("beta substitution",R["substitution"]=="u=x^2 then Euler beta integral")
check("beta value",R["beta_value"]=="B(1/2,z/2)")
check("gamma coefficient",R["coefficient"]=="m(z)=sqrt(pi)*Gamma(z/2)/Gamma((z+1)/2)")
def spherical_integral(z,steps=4000):
 a=-math.pi/2; b=math.pi/2; h=(b-a)/steps
 total=math.cos(a)**(z-1)+math.cos(b)**(z-1)
 total+=4*sum(math.cos(a+k*h)**(z-1) for k in range(1,steps,2))
 total+=2*sum(math.cos(a+k*h)**(z-1) for k in range(2,steps,2))
 return h*total/3
check("z=1 integral",abs(spherical_integral(1)-math.pi)<1e-10)
check("z=2 integral",abs(spherical_integral(2)-2)<1e-10)
check("z=3 integral",abs(spherical_integral(3)-math.pi/2)<1e-10)
check("raw action",N["raw_spherical_action"].startswith("J_alpha(z)v_z=m(z)"))
check("normalized action",N["normalized_spherical_action"]=="R_alpha(z)v_z=v_s_alpha_z")
check("coefficient constructed",Q["rank_one_spherical_coefficient_constructed"] and Q["coefficient_derived_from_beta_integral"])
check("operator ceiling",not Q["full_knapp_stein_operator_constructed"] and not Q["common_operator_domain_constructed"] and not Q["k_type_spectrum_constructed"])
check("physical ceiling",not Q["physical_intertwiner_constructed"] and not Q["protected_status_change"])
assert n==18; print("RESULT: PASS 18/18")
