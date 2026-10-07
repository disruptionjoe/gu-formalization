#!/usr/bin/env python3
"""Data-mutation probe for K1382."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1382-diagonal-mode-mixed-norm-obstruction.json").read_text())
def validate(x):
 m,q=x["diagonal_modes"],x["decision"];e=[]
 if "q_N=4N" not in m["mode"]:e.append("mode")
 if "q_N^(-n)" not in m["amplitude"]:e.append("amplitude")
 if "=1" not in m["energy_normalization"]:e.append("energy")
 if "asymptotic to (4N)^sigma/sqrt(2)" not in m["mixed_norm"]:e.append("mixed")
 if "diverges" not in m["finite_p"]:e.append("finite-p")
 if not q["same_lifted_energy_uniformly_bounded"]:e.append("bounded")
 if not q["finite_p_mixed_norm_unbounded"]:e.append("unbounded")
 if q["same_energy_finite_p_bound_exists"]:e.append("bound overclaim")
 if q["all_dispersive_repairs_excluded"]:e.append("repair overclaim")
 if q["global_nonlinear_evolution_proved"]:e.append("global overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("mode",lambda x:x["diagonal_modes"].__setitem__("mode","fixed charge")),("amplitude",lambda x:x["diagonal_modes"].__setitem__("amplitude","one")),("energy",lambda x:x["diagonal_modes"].__setitem__("energy_normalization","diverges")),("mixed",lambda x:x["diagonal_modes"].__setitem__("mixed_norm","bounded")),("finite-p",lambda x:x["diagonal_modes"].__setitem__("finite_p","unknown")),("bounded",lambda x:x["decision"].__setitem__("same_lifted_energy_uniformly_bounded",False)),("unbounded",lambda x:x["decision"].__setitem__("finite_p_mixed_norm_unbounded",False)),("bound overclaim",lambda x:x["decision"].__setitem__("same_energy_finite_p_bound_exists",True)),("repair overclaim",lambda x:x["decision"].__setitem__("all_dispersive_repairs_excluded",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_nonlinear_evolution_proved",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
