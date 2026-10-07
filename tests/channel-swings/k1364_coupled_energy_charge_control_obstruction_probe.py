#!/usr/bin/env python3
"""Data-mutation probe for K1364."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1364-coupled-energy-charge-control-obstruction.json").read_text())
def validate(x):
 c,r,q=x["counterexample"],x["repair_boundary"],x["decision"];e=[]
 if "Q e_n=4n e_n" not in c["charge_witnesses"]:e.append("witness")
 if "16N" not in c["charge_graph_norm"]:e.append("divergence")
 if "No constant C" not in c["conclusion"]:e.append("conclusion")
 if len(r["admissible_repairs"])!=3:e.append("repairs")
 if q["ordinary_positive_energy_controls_charge_graph_norm"]:e.append("energy overclaim")
 if not q["explicit_uniformly_energy_bounded_divergent_graph_sequence_constructed"]:e.append("sequence")
 if q["seagull_term_supplies_uniform_charge_coercivity"]:e.append("seagull overclaim")
 if q["augmented_action_or_graph_propagation_excluded"]:e.append("repair overclaim")
 if q["source_action_no_go_proved"]:e.append("source no-go overclaim")
 if q["protected_status_change"]:e.append("protected movement")
 return e
assert not validate(D)
mutations=[("witness",lambda x:x["counterexample"].__setitem__("charge_witnesses","bounded Q")),("divergence",lambda x:x["counterexample"].__setitem__("charge_graph_norm","bounded")),("conclusion",lambda x:x["counterexample"].__setitem__("conclusion","coercive")),("repairs",lambda x:x["repair_boundary"].__setitem__("admissible_repairs",[])),("energy overclaim",lambda x:x["decision"].__setitem__("ordinary_positive_energy_controls_charge_graph_norm",True)),("sequence",lambda x:x["decision"].__setitem__("explicit_uniformly_energy_bounded_divergent_graph_sequence_constructed",False)),("seagull overclaim",lambda x:x["decision"].__setitem__("seagull_term_supplies_uniform_charge_coercivity",True)),("repair overclaim",lambda x:x["decision"].__setitem__("augmented_action_or_graph_propagation_excluded",True)),("source no-go overclaim",lambda x:x["decision"].__setitem__("source_action_no_go_proved",True)),("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);e=validate(x);assert e,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {e[0]}")
print("RESULT: PASS 10/10")
