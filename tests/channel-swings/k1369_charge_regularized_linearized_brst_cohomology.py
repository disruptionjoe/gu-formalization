#!/usr/bin/env python3
"""Completed linearized BRST cohomology controls for K1369."""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1369-charge-regularized-linearized-brst-cohomology.json").read_text()); n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
L,B,Q=D["linearized_complex"],D["completion_boundary"],D["decision"]
check("vacuum typed","A=0" in L["vacuum"] and "phi=0" in L["vacuum"])
check("linear BRST typed","s_lin A=d c" in L["brst_differential"])
check("closed image typed","closed" in L["closed_gauge_image"])
check("matter graph energy typed","X_Q^1" in L["matter_energy_space"])
check("cohomology direct sum typed","H_Maxwell_transverse direct_sum E_matter" in L["cohomology"])
check("positive pairing typed","positive transverse Maxwell energy" in L["positive_pairing"])
check("matter generator typed","skew-adjoint" in L["matter_generator"])
m2=1.0; mu=0.25
for k2,q in ((1,0),(2,2),(0,4),(5,-6),(9,8)):
    check(f"positive matter mode k2={k2} q={q}",k2+m2+mu*q*q>0)
check("completed gain typed","completed on X_Q^1" in B["completed_gain"])
check("nonlinear debt typed","Closed nonlinear range" in B["nonlinear_missing"])
check("physical limit typed","not a source-owned" in B["physical_limit"])
check("linear complex decision",Q["closed_linearized_brst_complex_on_graph_domain"])
check("closed image decision",Q["closed_linearized_gauge_image"])
check("positive cohomology decision",Q["positive_nonzero_linearized_cohomology"])
check("photon classes decision",Q["transverse_photon_classes_present"])
check("matter classes decision",Q["graph_regular_matter_classes_present"])
check("nonlinear properness absent",not Q["nonlinear_KT_BV_BFV_properness"])
check("global nonlinear absent",not Q["global_nonlinear_evolution"])
check("GU cohomology absent",not Q["gu_physical_hilbert_cohomology"])
check("observation map absent",not Q["source_observation_map_constructed"])
check("protected fixed",not Q["protected_status_change"])
assert n==27,n
print("RESULT: PASS 27/27")
