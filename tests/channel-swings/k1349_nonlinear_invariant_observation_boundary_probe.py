#!/usr/bin/env python3
"""Hostile mutations for K1349."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1349-nonlinear-invariant-observation-boundary.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("unbounded map",lambda x:x["observable"].__setitem__("codomain","R"),lambda x:x["observable"]["codomain"]=="the real interval [0,1)")
rejects("gauge invariance removed",lambda x:x["decision"].__setitem__("local_gauge_invariant",False),lambda x:x["decision"]["local_gauge_invariant"])
rejects("G invariance removed",lambda x:x["decision"].__setitem__("full_internal_G_invariant",False),lambda x:x["decision"]["full_internal_G_invariant"])
rejects("covector imported",lambda x:x["decision"].__setitem__("nonzero_without_chosen_internal_covector",False),lambda x:x["decision"]["nonzero_without_chosen_internal_covector"])
rejects("linear theorem misapplied",lambda x:x["decision"].__setitem__("k1344_linear_no_go_evaded_by_changed_map_class",False),lambda x:x["decision"]["k1344_linear_no_go_evaded_by_changed_map_class"])
rejects("source-map overclaim",lambda x:x["decision"].__setitem__("source_owned_observation_map_constructed",True),lambda x:not x["decision"]["source_owned_observation_map_constructed"])
rejects("observed semantics overclaim",lambda x:x["decision"].__setitem__("observed_state_semantics_constructed",True),lambda x:not x["decision"]["observed_state_semantics_constructed"])
rejects("prediction overclaim",lambda x:x["decision"].__setitem__("empirical_export_or_prediction_constructed",True),lambda x:not x["decision"]["empirical_export_or_prediction_constructed"])
rejects("protected movement",lambda x:x["decision"].__setitem__("protected_status_change",True),lambda x:not x["decision"]["protected_status_change"])
rejects("nonlinearity removed",lambda x:x["observable"].__setitem__("nonlinearity","linear"),lambda x:"linear oddness" in x["observable"]["nonlinearity"])
assert len(tests)==10; print("RESULT: PASS 10/10")
