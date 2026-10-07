#!/usr/bin/env python3
"""Data-mutation probe for K1392."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1392-completed-triangular-local-flow.json").read_text())
def validate(x):
 f,q=x["completed_flow"],x["decision"];e=[]
 for key,needle in (("phase_space","completion"),("spectral_density","strongly"),("uniform_lifespan","N-independent"),("difference_estimate","one extra triangular tier"),("local_result","completed local strong solution")):
  if needle not in f[key]:e.append(key)
 for key in ("cutoff_uniform_lifespan_proved","one_tier_difference_estimate_proved","completed_local_strong_solution_constructed"):
  if not q[key]:e.append(key)
 for key in ("global_large_data_solution_constructed","physical_quotient_constructed","source_action_identified"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("space",lambda x:x["completed_flow"].__setitem__("phase_space","formal core")),("density",lambda x:x["completed_flow"].__setitem__("spectral_density","weak only")),("lifespan",lambda x:x["completed_flow"].__setitem__("uniform_lifespan","cutoff dependent")),("difference",lambda x:x["completed_flow"].__setitem__("difference_estimate","unclosed")),("result",lambda x:x["completed_flow"].__setitem__("local_result","none")),("uniform decision",lambda x:x["decision"].__setitem__("cutoff_uniform_lifespan_proved",False)),("difference decision",lambda x:x["decision"].__setitem__("one_tier_difference_estimate_proved",False)),("solution decision",lambda x:x["decision"].__setitem__("completed_local_strong_solution_constructed",False)),("global overclaim",lambda x:x["decision"].__setitem__("global_large_data_solution_constructed",True)),("quotient overclaim",lambda x:x["decision"].__setitem__("physical_quotient_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 11/11")
