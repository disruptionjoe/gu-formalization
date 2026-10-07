#!/usr/bin/env python3
"""Hostile mutations for K1335."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1335-operator-intertwiner-admission-boundary.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("bad census",lambda x:x["certificate"].__setitem__("satisfied_count",11),lambda x:sum(x["certificate"][k] for k in ("satisfied_count","excluded_count","conditional_count","missing_count"))==20)
rejects("operator row conditional",lambda x:x["certificate"]["advanced_row"].__setitem__("to","conditional"),lambda x:x["certificate"]["advanced_row"]["to"]=="satisfied")
rejects("operator absent",lambda x:x["decision"].__setitem__("full_rank_one_kernel_and_even_k_spectrum_constructed",False),lambda x:x["decision"]["full_rank_one_kernel_and_even_k_spectrum_constructed"])
rejects("domain absent",lambda x:x["decision"].__setitem__("common_dense_k_finite_domain_constructed",False),lambda x:x["decision"]["common_dense_k_finite_domain_constructed"])
rejects("unitarity absent",lambda x:x["decision"].__setitem__("regular_imaginary_unitarity_and_irreducibility_constructed",False),lambda x:x["decision"]["regular_imaginary_unitarity_and_irreducibility_constructed"])
rejects("Coxeter absent",lambda x:x["decision"].__setitem__("operator_valued_D7_coxeter_relations_constructed",False),lambda x:x["decision"]["operator_valued_D7_coxeter_relations_constructed"])
rejects("descent absent",lambda x:x["decision"].__setitem__("G_equivariant_full_chamber_descent_constructed",False),lambda x:x["decision"]["G_equivariant_full_chamber_descent_constructed"])
rejects("source overclaim",lambda x:x["decision"].__setitem__("source_charge_or_chamber_selected",True),lambda x:not x["decision"]["source_charge_or_chamber_selected"])
rejects("physical overclaim",lambda x:x["decision"].__setitem__("positive_physical_pairing_constructed",True),lambda x:not x["decision"]["positive_physical_pairing_constructed"])
assert len(tests)==9; print("RESULT: PASS 9/9")
