#!/usr/bin/env python3
"""Mutation probe for K1404."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1404-spectral-noether-measure.json").read_text())
def validate(x):
 f,q=x["spectral_noether_measure"],x["decision"];e=[]
 for key,needle in (("symmetry","constant phase"),("charge","C(B)="),("conservation","dC(B)/dt=0"),("countable_additivity","countably additive"),("moments","q^k"),("gauge_invariance","descends"),("boundary","signed")):
  if needle not in f[key]:e.append(key)
 if not q["conserved_spectral_noether_measure_constructed"]:e.append("measure decision")
 if q["measure_positive_or_coercive"]:e.append("positivity overclaim")
 return e
assert not validate(D)
mutations=[("symmetry",lambda x:x["spectral_noether_measure"].__setitem__("symmetry","none")),("charge",lambda x:x["spectral_noether_measure"].__setitem__("charge","none")),("conservation",lambda x:x["spectral_noether_measure"].__setitem__("conservation","none")),("additivity",lambda x:x["spectral_noether_measure"].__setitem__("countable_additivity","finite only")),("moments",lambda x:x["spectral_noether_measure"].__setitem__("moments","none")),("gauge",lambda x:x["spectral_noether_measure"].__setitem__("gauge_invariance","none")),("boundary",lambda x:x["spectral_noether_measure"].__setitem__("boundary","positive")),("decision",lambda x:x["decision"].__setitem__("conserved_spectral_noether_measure_constructed",False)),("positivity",lambda x:x["decision"].__setitem__("measure_positive_or_coercive",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
