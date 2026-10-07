#!/usr/bin/env python3
"""Hostile mutations for K1344."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1344-principal-series-observation-functional-boundary.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("Riesz vector removed",lambda x:x["functional_classification"].__setitem__("riesz_form","unknown"),lambda x:x["functional_classification"]["riesz_form"].startswith("every bounded linear"))
rejects("covariance removed",lambda x:x["functional_classification"].__setitem__("covariance","none"),lambda x:"pi(g)^* eta" in x["functional_classification"]["covariance"])
rejects("nonzero invariant export invented",lambda x:x["functional_classification"].__setitem__("full_G_invariant_scalar_export","nonzero"),lambda x:x["functional_classification"]["full_G_invariant_scalar_export"]=="zero only")
rejects("classification lost",lambda x:x["decision"].__setitem__("bounded_linear_scalar_exports_classified",False),lambda x:x["decision"]["bounded_linear_scalar_exports_classified"])
rejects("invariant boundary lost",lambda x:x["decision"].__setitem__("nonzero_full_G_invariant_bounded_scalar_export_excluded",False),lambda x:x["decision"]["nonzero_full_G_invariant_bounded_scalar_export_excluded"])
rejects("chosen export lost",lambda x:x["decision"].__setitem__("nonzero_symmetry_breaking_bounded_export_exists_after_choice",False),lambda x:x["decision"]["nonzero_symmetry_breaking_bounded_export_exists_after_choice"])
rejects("source overclaim",lambda x:x["decision"].__setitem__("source_owned_observation_covector_selected",True),lambda x:not x["decision"]["source_owned_observation_covector_selected"])
rejects("global no-go overclaim",lambda x:x["decision"].__setitem__("all_observation_maps_excluded",True),lambda x:not x["decision"]["all_observation_maps_excluded"])
rejects("GU map overclaim",lambda x:x["decision"].__setitem__("gu_observed_state_map_constructed",True),lambda x:not x["decision"]["gu_observed_state_map_constructed"])
rejects("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True),lambda x:not x["decision"]["protected_status_change"])
assert len(tests)==10; print("RESULT: PASS 10/10")
