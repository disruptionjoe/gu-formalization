#!/usr/bin/env python3
"""Data-mutation probe for K1354."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1354-split-gauge-kinetic-positivity-boundary.json").read_text())
def validate(x):
 c,t,p,q=x["cartan_signature"],x["invariant_form_theorem"],x["positive_controls"],x["decision"]; e=[]
 if "49 positive,42 negative" not in c["signature"]: e.append("signature")
 if "scalar multiple" not in t["classification"]: e.append("classification")
 if "indefinite" not in t["nonzero_case"]: e.append("indefinite")
 if t["zero_case"]!="the zero form is degenerate": e.append("zero case")
 if "extra reduction/selector data" not in p["ownership_boundary"]: e.append("ownership")
 if q["full_split_killing_signature_positive"]!=49: e.append("positive count")
 if q["full_split_killing_signature_negative"]!=42: e.append("negative count")
 if q["positive_full_G_invariant_quadratic_form_exists"]: e.append("positivity overclaim")
 if not q["positive_maximal_compact_control_exists"]: e.append("compact control")
 if q["sc_meta_53_resolved"]: e.append("status overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("signature",lambda x:x["cartan_signature"].__setitem__("signature","positive")),
 ("classification",lambda x:x["invariant_form_theorem"].__setitem__("classification","many arbitrary forms")),
 ("indefinite",lambda x:x["invariant_form_theorem"].__setitem__("nonzero_case","positive")),
 ("zero case",lambda x:x["invariant_form_theorem"].__setitem__("zero_case","nondegenerate")),
 ("ownership",lambda x:x["positive_controls"].__setitem__("ownership_boundary","automatic")),
 ("positive count",lambda x:x["decision"].__setitem__("full_split_killing_signature_positive",91)),
 ("negative count",lambda x:x["decision"].__setitem__("full_split_killing_signature_negative",0)),
 ("positivity overclaim",lambda x:x["decision"].__setitem__("positive_full_G_invariant_quadratic_form_exists",True)),
 ("compact control",lambda x:x["decision"].__setitem__("positive_maximal_compact_control_exists",False)),
 ("status overclaim",lambda x:x["decision"].__setitem__("sc_meta_53_resolved",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); errors=validate(x); assert errors,label; print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
