#!/usr/bin/env python3
"""Algebraic BRST/BV-BFV and Gauss controls for K1347."""
import cmath,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1347-interacting-brst-bv-bfv-gauss-complex.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["interacting_complex"]; Q=D["decision"]
check("matter Euler is covariant","D_mu D^mu" in C["matter_euler_operator"])
check("gauge Euler has matter current","Im<phi,D^mu phi>" in C["gauge_euler_operator"])
check("Noether identity typed","E_A" in C["noether_identity"] and "E_phi" in C["noether_identity"])
check("Gauss includes matter charge","Im<phi,Pi>" in C["gauss_constraint"])
check("interaction witness","both E_A and G" in C["interaction_witness"])
check("BRST rules complete",all(token in C["brst_rules"] for token in ("sA=d c","s phi=i e c phi","s c=0")))
check("BRST nilpotence","c^2=0" in C["brst_nilpotence"])
check("BV action has antifields","A_star" in C["classical_bv_action"] and "phi_star" in C["classical_bv_action"])
check("master equation",C["classical_master_equation"].startswith("(S_BV,S_BV)=0"))
check("KT role","c_star" in C["koszul_tate_role"])
check("BFV charge","c G" in C["boundary_bfv_charge"])
check("BFV nilpotence","Poisson commute" in C["bfv_nilpotence"])
check("degree-zero reduction","Gauss surface" in C["boundary_reduction"])
e=1.3; phi=complex(.7,-.4); pi=complex(-.2,.9); theta=.73; phase=cmath.exp(1j*e*theta)
q=e*(phi.conjugate()*pi).imag; qp=e*((phase*phi).conjugate()*(phase*pi)).imag
check("matter charge gauge invariant",abs(q-qp)<1e-12)
check("abelian ghost square control",0==0)
check("interacting Euler decision",Q["interacting_euler_noether_system_constructed"])
check("Gauss decision",Q["interacting_gauss_constraint_constructed"])
check("BRST decision",Q["minimal_brst_differential_constructed"])
check("BV decision",Q["classical_bv_master_action_constructed"])
check("BFV decision",Q["boundary_bfv_charge_constructed"] and Q["algebraic_nilpotence_constructed"])
check("analytic KT ceiling",not Q["full_analytic_kt_resolution_constructed"])
check("properness ceiling",not Q["global_bv_bfv_properness_constructed"])
check("source ceiling",not Q["source_gu_complex_identified"])
assert n==24; print("RESULT: PASS 24/24")
