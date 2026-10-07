#!/usr/bin/env python3
"""Hostile mutations for K1346."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1346-principal-series-scalar-electrodynamics-action.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("zero coupling",lambda x:x["single_action"].__setitem__("parameters","e=0"),lambda x:x["single_action"]["parameters"].startswith("e is nonzero"))
rejects("covariant derivative removed",lambda x:x["single_action"].__setitem__("covariant_derivative","partial phi"),lambda x:"i e A" in x["single_action"]["covariant_derivative"])
rejects("gauge covariance removed",lambda x:x["single_action"].__setitem__("covariance_identity","none"),lambda x:"exp(i e chi) D phi" in x["single_action"]["covariance_identity"])
rejects("interaction removed",lambda x:x["decision"].__setitem__("nonzero_gauge_matter_coupling_constructed",False),lambda x:x["decision"]["nonzero_gauge_matter_coupling_constructed"])
rejects("prior-sum relabel",lambda x:x["decision"].__setitem__("sum_of_prior_separate_actions",True),lambda x:not x["decision"]["sum_of_prior_separate_actions"])
rejects("source-action overclaim",lambda x:x["decision"].__setitem__("source_gu_action_identified",True),lambda x:not x["decision"]["source_gu_action_identified"])
rejects("source-charge overclaim",lambda x:x["decision"].__setitem__("source_charge_or_couplings_derived",True),lambda x:not x["decision"]["source_charge_or_couplings_derived"])
rejects("global-solution overclaim",lambda x:x["decision"].__setitem__("global_interacting_solution_theory_constructed",True),lambda x:not x["decision"]["global_interacting_solution_theory_constructed"])
rejects("internal equivariance lost",lambda x:x["decision"].__setitem__("internal_principal_series_equivariance_constructed",False),lambda x:x["decision"]["internal_principal_series_equivariance_constructed"])
rejects("common domain lost",lambda x:x["decision"].__setitem__("common_energy_form_domain_declared",False),lambda x:x["decision"]["common_energy_form_domain_declared"])
assert len(tests)==10; print("RESULT: PASS 10/10")
