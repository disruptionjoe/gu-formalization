#!/usr/bin/env python3
"""Data-mutation probe for K1361."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1361-local-gauge-charge-graph-domain.json").read_text())
def validate(x):
 g,l,q=x["graph_domain"],x["local_gauge_theorem"],x["decision"];e=[]
 if "Q phi" not in g["completed_domain"]:e.append("domain")
 if "H_Kfin" not in g["density"]:e.append("core")
 if "partial_j alpha" not in l["weak_derivative"]:e.append("derivative")
 if "not D(Q)" not in l["ordinary_H1_failure"]:e.append("counterexample")
 if not q["minimal_completed_first_order_graph_domain_constructed"]:e.append("construction")
 if not q["local_circle_gauge_action_preserves_graph_domain"]:e.append("gauge preservation")
 if q["ordinary_H1_preserved_for_all_H_ps_fields"]:e.append("H1 overclaim")
 if q["source_selects_domain"]:e.append("source overclaim")
 if q["coupled_global_BV_domain_constructed"]:e.append("BV overclaim")
 if q["protected_status_change"]:e.append("protected movement")
 return e
assert not validate(D)
mutations=[("domain",lambda x:x["graph_domain"].__setitem__("completed_domain","H1 only")),("core",lambda x:x["graph_domain"].__setitem__("density","unknown")),("derivative",lambda x:x["local_gauge_theorem"].__setitem__("weak_derivative","formal")),("counterexample",lambda x:x["local_gauge_theorem"].__setitem__("ordinary_H1_failure","none")),("construction",lambda x:x["decision"].__setitem__("minimal_completed_first_order_graph_domain_constructed",False)),("gauge preservation",lambda x:x["decision"].__setitem__("local_circle_gauge_action_preserves_graph_domain",False)),("H1 overclaim",lambda x:x["decision"].__setitem__("ordinary_H1_preserved_for_all_H_ps_fields",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_selects_domain",True)),("BV overclaim",lambda x:x["decision"].__setitem__("coupled_global_BV_domain_constructed",True)),("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);e=validate(x);assert e,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {e[0]}")
print("RESULT: PASS 10/10")
