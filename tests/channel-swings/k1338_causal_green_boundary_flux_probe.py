#!/usr/bin/env python3
"""Hostile mutations for K1338."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1338-causal-green-boundary-flux.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("hyperbolicity removed",lambda x:x["green_system"].__setitem__("global_hyperbolicity","open"),lambda x:"globally hyperbolic" in x["green_system"]["global_hyperbolicity"])
rejects("wrong principal sign",lambda x:x["green_system"].__setitem__("normal_hyperbolicity","elliptic"),lambda x:x["green_system"]["normal_hyperbolicity"].startswith("P=partial_t^2-Delta_T3+m^2"))
rejects("tensor lift removed",lambda x:x["green_system"].__setitem__("tensor_lift","unknown"),lambda x:x["green_system"]["tensor_lift"]=="E_plus_minus=E_plus_minus_scalar tensor I_Hps")
rejects("future support removed",lambda x:x["green_system"].__setitem__("support","global"),lambda x:"J_plus" in x["green_system"]["support"] and "J_minus" in x["green_system"]["support"])
rejects("Green system removed",lambda x:x["decision"].__setitem__("causal_green_system_constructed",False),lambda x:x["decision"]["causal_green_system_constructed"])
rejects("propagation removed",lambda x:x["decision"].__setitem__("finite_propagation_support_constructed",False),lambda x:x["decision"]["finite_propagation_support_constructed"])
rejects("boundary form removed",lambda x:x["decision"].__setitem__("cauchy_boundary_symplectic_form_constructed",False),lambda x:x["decision"]["cauchy_boundary_symplectic_form_constructed"])
rejects("conservation removed",lambda x:x["decision"].__setitem__("boundary_form_conserved",False),lambda x:x["decision"]["boundary_form_conserved"])
rejects("BFV overclaim",lambda x:x["decision"].__setitem__("gu_bfv_boundary_reduction_constructed",True),lambda x:not x["decision"]["gu_bfv_boundary_reduction_constructed"])
rejects("interaction overclaim",lambda x:x["decision"].__setitem__("interacting_green_system_constructed",True),lambda x:not x["decision"]["interacting_green_system_constructed"])
assert len(tests)==10; print("RESULT: PASS 10/10")
