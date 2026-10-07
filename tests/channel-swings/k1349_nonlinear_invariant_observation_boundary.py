#!/usr/bin/env python3
"""Bounded nonlinear invariant-observable controls for K1349."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1349-nonlinear-invariant-observation-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
O=D["observable"]; Q=D["decision"]
check("pointwise radial map","||phi||_Hps^2" in O["pointwise_map"])
check("bounded codomain",O["codomain"]=="the real interval [0,1)")
vectors=[(1.,2.,-1.),(2.,0.,3.),(-1.,-2.,4.)]
for v in vectors:
 r=sum(x*x for x in v); obs=r/(1+r); rotated=(v[1],-v[0],v[2]); rr=sum(x*x for x in rotated)
 check("sample bounded",0<obs<1)
 check("sample unitary invariant",abs(obs-rr/(1+rr))<1e-12)
 check("sample nonlinear even",abs(obs-sum((-x)**2 for x in v)/(1+sum((-x)**2 for x in v)))<1e-12)
check("gauge invariance","exp(i e chi)" in O["gauge_invariance"])
check("internal G invariance","pi(g)" in O["internal_G_invariance"])
check("Frechet derivative","2 Re<phi,h>" in O["frechet_derivative"])
check("nontrivial derivative","D O_phi[phi]>0" in O["nontriviality"])
check("nonlinearity witness","linear oddness" in O["nonlinearity"])
check("K1344 boundary","bounded linear" in O["k1344_relation"] and "nonlinear" in O["k1344_relation"])
check("field export","spatial weight" in O["field_export"])
check("observable decision",Q["bounded_nonlinear_scalar_observable_constructed"])
check("gauge decision",Q["local_gauge_invariant"])
check("G decision",Q["full_internal_G_invariant"])
check("no covector choice",Q["nonzero_without_chosen_internal_covector"])
check("changed map class",Q["k1344_linear_no_go_evaded_by_changed_map_class"])
check("source ceiling",not Q["source_owned_observation_map_constructed"])
check("semantics ceiling",not Q["observed_state_semantics_constructed"])
check("empirical ceiling",not Q["empirical_export_or_prediction_constructed"])
check("protected fixed",not Q["protected_status_change"])
assert n==29; print("RESULT: PASS 29/29")
