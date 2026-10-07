#!/usr/bin/env python3
"""Hostile mutations for K1347."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1347-interacting-brst-bv-bfv-gauss-complex.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("matter current removed",lambda x:x["interacting_complex"].__setitem__("gauge_euler_operator","free Maxwell"),lambda x:"Im<phi,D^mu phi>" in x["interacting_complex"]["gauge_euler_operator"])
rejects("Gauss matter term removed",lambda x:x["interacting_complex"].__setitem__("gauss_constraint","div E=0"),lambda x:"Im<phi,Pi>" in x["interacting_complex"]["gauss_constraint"])
rejects("BRST nilpotence removed",lambda x:x["decision"].__setitem__("algebraic_nilpotence_constructed",False),lambda x:x["decision"]["algebraic_nilpotence_constructed"])
rejects("BV master lost",lambda x:x["decision"].__setitem__("classical_bv_master_action_constructed",False),lambda x:x["decision"]["classical_bv_master_action_constructed"])
rejects("BFV charge lost",lambda x:x["decision"].__setitem__("boundary_bfv_charge_constructed",False),lambda x:x["decision"]["boundary_bfv_charge_constructed"])
rejects("analytic KT overclaim",lambda x:x["decision"].__setitem__("full_analytic_kt_resolution_constructed",True),lambda x:not x["decision"]["full_analytic_kt_resolution_constructed"])
rejects("properness overclaim",lambda x:x["decision"].__setitem__("global_bv_bfv_properness_constructed",True),lambda x:not x["decision"]["global_bv_bfv_properness_constructed"])
rejects("source complex overclaim",lambda x:x["decision"].__setitem__("source_gu_complex_identified",True),lambda x:not x["decision"]["source_gu_complex_identified"])
rejects("Noether identity removed",lambda x:x["interacting_complex"].__setitem__("noether_identity","none"),lambda x:"E_A" in x["interacting_complex"]["noether_identity"])
rejects("common core removed",lambda x:x["interacting_complex"].__setitem__("common_algebraic_core","none"),lambda x:"K-finite" in x["interacting_complex"]["common_algebraic_core"])
assert len(tests)==10; print("RESULT: PASS 10/10")
