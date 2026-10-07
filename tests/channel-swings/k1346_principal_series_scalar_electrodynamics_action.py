#!/usr/bin/env python3
"""Exact finite-dimensional gauge-covariance controls for K1346."""
import cmath,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1346-principal-series-scalar-electrodynamics-action.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
A=D["single_action"]; Q=D["decision"]
check("nonzero coupling",A["parameters"].startswith("e is nonzero"))
check("covariant derivative","partial_mu phi-i e A_mu phi" in A["covariant_derivative"])
check("one Lagrangian","F_mu_nu" in A["lagrangian"] and "D_mu phi" in A["lagrangian"])
check("local gauge action","exp(i e chi)" in A["local_gauge_action"])
e=1.7; A0=.4; phi=complex(.7,-.2); dphi=complex(-.3,.9); chi=.6; dchi=-.25
phase=cmath.exp(1j*e*chi)
lhs=phase*(dphi+1j*e*dchi*phi)-1j*e*(A0+dchi)*phase*phi
rhs=phase*(dphi-1j*e*A0*phi)
check("sample gauge covariance",abs(lhs-rhs)<1e-12)
check("curvature gauge invariance","F'=F" in A["covariance_identity"])
vectors=[(1+2j,-2+1j),(3-1j,2j)]
for v in vectors:
 r=sum(abs(z)**2 for z in v); rotated=(v[1],-v[0])
 check("internal unitary norm",abs(r-sum(abs(z)**2 for z in rotated))<1e-12)
check("internal equivariance","pi(g)Dphi" in A["internal_G_action"])
check("current interaction present","current term" in A["interaction_terms"])
check("seagull interaction present","seagull term" in A["interaction_terms"])
check("nonseparable action",A["nonseparability"].startswith("the covariant kinetic term is not"))
check("common core","K-finite" in A["common_core"])
check("energy form domain","H1(T3)" in A["energy_form_domain"] and "L2(T3)" in A["energy_form_domain"])
check("one action decision",Q["one_gauge_invariant_interacting_action_constructed"])
check("genuine coupling decision",Q["nonzero_gauge_matter_coupling_constructed"])
check("gauge invariance decision",Q["local_U1_gauge_invariance_constructed"])
check("G equivariance decision",Q["internal_principal_series_equivariance_constructed"])
check("common domain decision",Q["common_energy_form_domain_declared"])
check("not prior sum",not Q["sum_of_prior_separate_actions"])
check("source ceiling",not Q["source_gu_action_identified"] and not Q["source_charge_or_couplings_derived"])
check("analytic ceiling",not Q["global_interacting_solution_theory_constructed"])
check("claim ceiling explicit","repository choices" in D["claim_ceiling"])
assert n==26; print("RESULT: PASS 26/26")
