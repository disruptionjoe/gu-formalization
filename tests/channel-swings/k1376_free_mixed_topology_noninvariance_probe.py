#!/usr/bin/env python3
"""Data-mutation probe for K1376."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1376-free-mixed-topology-noninvariance.json").read_text())
def validate(x):
 f,q=x["free_flow"],x["decision"];e=[]
 if "Omega^2=-Delta" not in f["equation"]:e.append("operator")
 if "no Qpi_0" not in f["k1372_phase_data"]:e.append("phase")
 if "Qe_(4N)=4N" not in f["mode"]:e.append("charge")
 if "t_N tends to zero" not in f["test_time"]:e.append("time")
 if "(4N)^2/omega_N" not in f["output"]:e.append("output")
 if not q["initial_k1372_topology_bounded"]:e.append("initial")
 if not q["free_output_k1372_norm_unbounded"]:e.append("unbounded")
 if q["strong_continuity_on_one_sided_topology"]:e.append("continuity overclaim")
 if q["global_nonlinear_evolution_proved"]:e.append("nonlinear overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("operator",lambda x:x["free_flow"].__setitem__("equation","unknown")),
 ("phase",lambda x:x["free_flow"].__setitem__("k1372_phase_data","full lift")),
 ("charge",lambda x:x["free_flow"].__setitem__("mode","neutral")),
 ("time",lambda x:x["free_flow"].__setitem__("test_time","fixed")),
 ("output",lambda x:x["free_flow"].__setitem__("output","bounded")),
 ("initial",lambda x:x["decision"].__setitem__("initial_k1372_topology_bounded",False)),
 ("unbounded",lambda x:x["decision"].__setitem__("free_output_k1372_norm_unbounded",False)),
 ("continuity overclaim",lambda x:x["decision"].__setitem__("strong_continuity_on_one_sided_topology",True)),
 ("nonlinear overclaim",lambda x:x["decision"].__setitem__("global_nonlinear_evolution_proved",True)),
 ("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
