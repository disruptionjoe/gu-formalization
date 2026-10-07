#!/usr/bin/env python3
"""Data-mutation probe for K1395."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1395-compact-torus-coefficient-integrability-obstruction.json").read_text())
def validate(x):
 f,q=x["integrability_obstruction"],x["decision"];e=[]
 for key,needle in (("baseline","including the vacuum"),("nontrivial_mode","Q-eigenvector"),("reduced_equation","a''+(m^2+mu q^2)a+lambda a^3=0"),("global_periodic_solution","periodic"),("baseline_removed_obstruction","positive period average"),("logical_effect","not a necessary global continuation condition")):
  if needle not in f[key]:e.append(key)
 if q["global_integral_BR_target_viable_on_T3"]:e.append("target overclaim")
 if not q["vacuum_baseline_obstruction_proved"]:e.append("baseline decision")
 if not q["nontrivial_periodic_mode_obstruction_proved"]:e.append("mode decision")
 if q["finite_interval_continuation_criterion_reversed"]:e.append("finite reversal")
 if q["global_large_data_evolution_proved"]:e.append("global overclaim")
 if q["noncompact_dispersive_route_excluded"]:e.append("noncompact overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("baseline",lambda x:x["integrability_obstruction"].__setitem__("baseline","finite")),("mode",lambda x:x["integrability_obstruction"].__setitem__("nontrivial_mode","none")),("ODE",lambda x:x["integrability_obstruction"].__setitem__("reduced_equation","unknown")),("periodic",lambda x:x["integrability_obstruction"].__setitem__("global_periodic_solution","decays")),("average",lambda x:x["integrability_obstruction"].__setitem__("baseline_removed_obstruction","integrable")),("logic",lambda x:x["integrability_obstruction"].__setitem__("logical_effect","necessary")),("target overclaim",lambda x:x["decision"].__setitem__("global_integral_BR_target_viable_on_T3",True)),("baseline decision",lambda x:x["decision"].__setitem__("vacuum_baseline_obstruction_proved",False)),("mode decision",lambda x:x["decision"].__setitem__("nontrivial_periodic_mode_obstruction_proved",False)),("finite reversal",lambda x:x["decision"].__setitem__("finite_interval_continuation_criterion_reversed",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_large_data_evolution_proved",True)),("noncompact overclaim",lambda x:x["decision"].__setitem__("noncompact_dispersive_route_excluded",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 12/12")
