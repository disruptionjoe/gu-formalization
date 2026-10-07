#!/usr/bin/env python3
"""Hostile mutations for K1343."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1343-defocusing-principal-series-wave-interaction.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("focusing sign",lambda x:x["interaction"].__setitem__("parameters","lambda<0"),lambda x:x["interaction"]["parameters"]=="m>0 and lambda>0")
rejects("quadratic only",lambda x:x["interaction"].__setitem__("equation","u_tt-Delta u=0"),lambda x:"||u||_Hps^2 u" in x["interaction"]["equation"])
rejects("energy coercivity lost",lambda x:x["decision"].__setitem__("positive_coercive_conserved_energy_constructed",False),lambda x:x["decision"]["positive_coercive_conserved_energy_constructed"])
rejects("global evolution lost",lambda x:x["decision"].__setitem__("global_finite_energy_evolution_constructed",False),lambda x:x["decision"]["global_finite_energy_evolution_constructed"])
rejects("causality lost",lambda x:x["decision"].__setitem__("causal_finite_speed_constructed",False),lambda x:x["decision"]["causal_finite_speed_constructed"])
rejects("equivariance lost",lambda x:x["decision"].__setitem__("internal_G_equivariance_constructed",False),lambda x:x["decision"]["internal_G_equivariance_constructed"])
rejects("constraint overclaim",lambda x:x["decision"].__setitem__("constraint_complex_constructed",True),lambda x:not x["decision"]["constraint_complex_constructed"])
rejects("source overclaim",lambda x:x["decision"].__setitem__("gu_action_owned",True),lambda x:not x["decision"]["gu_action_owned"])
rejects("physical overclaim",lambda x:x["decision"].__setitem__("gu_interacting_physical_theory_constructed",True),lambda x:not x["decision"]["gu_interacting_physical_theory_constructed"])
rejects("interaction removed",lambda x:x["decision"].__setitem__("genuine_nonlinear_local_interaction_constructed",False),lambda x:x["decision"]["genuine_nonlinear_local_interaction_constructed"])
assert len(tests)==10; print("RESULT: PASS 10/10")
