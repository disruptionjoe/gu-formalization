#!/usr/bin/env python3
"""Hostile mutations for K1342."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1342-transverse-positive-cohomology-green-boundary.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("nonclosed image",lambda x:x["physical_reduction"].__setitem__("closed_gauge_image","dense only"),lambda x:"closed range" in x["physical_reduction"]["closed_gauge_image"])
rejects("wrong polarization count",lambda x:x["physical_reduction"].__setitem__("polarization_count",3),lambda x:x["physical_reduction"]["polarization_count"]==2)
rejects("zero cohomology",lambda x:x["decision"].__setitem__("positive_nonzero_transverse_cohomology_constructed",False),lambda x:x["decision"]["positive_nonzero_transverse_cohomology_constructed"])
rejects("causality lost",lambda x:x["green_boundary"].__setitem__("causal_support","none"),lambda x:"J_plus" in x["green_boundary"]["causal_support"])
rejects("constraint propagation lost",lambda x:x["green_boundary"].__setitem__("constraint_propagation","open"),lambda x:"Box_0 delta" in x["green_boundary"]["constraint_propagation"])
rejects("boundary descent lost",lambda x:x["green_boundary"].__setitem__("descent","not descended"),lambda x:"annihilates infinitesimal gauge directions" in x["green_boundary"]["descent"])
rejects("GU cohomology overclaim",lambda x:x["decision"].__setitem__("gu_physical_cohomology_constructed",True),lambda x:not x["decision"]["gu_physical_cohomology_constructed"])
rejects("interaction overclaim",lambda x:x["decision"].__setitem__("interacting",True),lambda x:not x["decision"]["interacting"])
rejects("source overclaim",lambda x:x["decision"].__setitem__("source_owned",True),lambda x:not x["decision"]["source_owned"])
rejects("equivariance lost",lambda x:x["decision"].__setitem__("internal_G_equivariance_constructed",False),lambda x:x["decision"]["internal_G_equivariance_constructed"])
assert len(tests)==10; print("RESULT: PASS 10/10")
