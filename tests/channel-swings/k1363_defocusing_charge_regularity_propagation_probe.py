#!/usr/bin/env python3
"""Data-mutation probe for K1363."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1363-defocusing-charge-regularity-propagation.json").read_text())
def validate(x):
 t,q=x["propagation_theorem"],x["decision"];e=[]
 if "every integer r>=1" not in t["charge_commutation"]:e.append("powers")
 if "w_r=Q^r u" not in t["differentiated_equation"]:e.append("equation")
 if "all real times" not in t["global_propagation"]:e.append("global")
 if not q["one_charge_graph_order_propagated_globally"]:e.append("one order")
 if not q["every_finite_charge_graph_order_propagated_for_smooth_data"]:e.append("all orders")
 if q["higher_charge_energy_conserved"]:e.append("conservation overclaim")
 if q["coupled_gauge_matter_global_evolution_proved"]:e.append("coupled overclaim")
 if q["closed_KT_BV_BFV_quotient_proved"]:e.append("BV overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 if q["protected_status_change"]:e.append("protected movement")
 return e
assert not validate(D)
mutations=[("powers",lambda x:x["propagation_theorem"].__setitem__("charge_commutation","r=0 only")),("equation",lambda x:x["propagation_theorem"].__setitem__("differentiated_equation","unknown")),("global",lambda x:x["propagation_theorem"].__setitem__("global_propagation","local")),("one order",lambda x:x["decision"].__setitem__("one_charge_graph_order_propagated_globally",False)),("all orders",lambda x:x["decision"].__setitem__("every_finite_charge_graph_order_propagated_for_smooth_data",False)),("conservation overclaim",lambda x:x["decision"].__setitem__("higher_charge_energy_conserved",True)),("coupled overclaim",lambda x:x["decision"].__setitem__("coupled_gauge_matter_global_evolution_proved",True)),("BV overclaim",lambda x:x["decision"].__setitem__("closed_KT_BV_BFV_quotient_proved",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True)),("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);e=validate(x);assert e,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {e[0]}")
print("RESULT: PASS 10/10")
