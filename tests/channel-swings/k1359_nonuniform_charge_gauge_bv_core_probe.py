#!/usr/bin/env python3
"""Data-mutation probe for K1359."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1359-nonuniform-charge-gauge-bv-core.json").read_text())
def validate(x):
 c,g,b,q=x["common_core"],x["gauge_action"],x["brst_bv_bfv"],x["decision"]; e=[]
 if "H_Kfin" not in c["matter_core"]:e.append("core")
 if "Q phi" not in g["covariant_derivative"]:e.append("covariant derivative")
 if "exp(i alpha Q)" not in g["local_transformation"]:e.append("gauge law")
 if "Q D_mu phi" not in g["nontrivial_interaction"]:e.append("current")
 if "s^2=0" not in b["nilpotence"]:e.append("nilpotence")
 if not q["operator_valued_charge_action_constructed"]:e.append("action")
 if not q["local_gauge_covariance_on_core"]:e.append("covariance")
 if q["completed_common_graph_domain_proved"]:e.append("domain overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 if q["protected_status_change"]:e.append("protected movement")
 return e
assert not validate(D),validate(D)
mutations=[
 ("core",lambda x:x["common_core"].__setitem__("matter_core","all H")),
 ("covariant derivative",lambda x:x["gauge_action"].__setitem__("covariant_derivative","partial phi")),
 ("gauge law",lambda x:x["gauge_action"].__setitem__("local_transformation","uniform phase")),
 ("current",lambda x:x["gauge_action"].__setitem__("nontrivial_interaction","none")),
 ("nilpotence",lambda x:x["brst_bv_bfv"].__setitem__("nilpotence","unknown")),
 ("action",lambda x:x["decision"].__setitem__("operator_valued_charge_action_constructed",False)),
 ("covariance",lambda x:x["decision"].__setitem__("local_gauge_covariance_on_core",False)),
 ("domain overclaim",lambda x:x["decision"].__setitem__("completed_common_graph_domain_proved",True)),
 ("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True)),
 ("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
