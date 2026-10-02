#!/usr/bin/env python3
"""Hostile mutation probe for K774."""
from __future__ import annotations
import copy, runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
K=runpy.run_path(str(ROOT/"tests/channel-swings/k774_sc_act_06_positive_curvature_successor_gate.py"))
p=K["build"](); K["validate"](p)
M=[
 lambda q:q.__setitem__("classification","INTERNAL_COMPARATOR_ONLY"),
 lambda q:q.__setitem__("closed_classes",q["closed_classes"][:2]),
 lambda q:q.__setitem__("surviving_branches",q["surviving_branches"][:3]),
 lambda q:q["exact_controls"].__setitem__("nonnull_middle_classes",0),
 lambda q:q["exact_controls"].__setitem__("native_null_middle_classes",0),
 lambda q:q["exact_controls"].__setitem__("common_distortion_kernel_inside_curvature_candidate",8192),
 lambda q:q["exact_controls"].__setitem__("native_null_additional_metric_coupled_classes",0),
 lambda q:q["decision"].__setitem__("do_not_retry_fixed_identity_cartan_unit_weight_comparator",False),
 lambda q:q["decision"].__setitem__("do_not_promote_candidate_kernel_to_gauge",False),
 lambda q:q["decision"].__setitem__("do_not_promote_comparator_to_source_I2B",False),
 lambda q:q["decision"].__setitem__("source_owned_positive_family_globally_closed",True),
 lambda q:q["decision"].__setitem__("SC_ACT_06_status","REFUTED"),
 lambda q:q["decision"].__setitem__("global_SC_ACT_06_refuted",True),
 lambda q:q.__setitem__("source_and_ledger_effect","MOVED"),
 lambda q:q.__setitem__("target_claim","NONE-NOT-A-KILL"),
 lambda q:q.__setitem__("status","canon"),
]
rejected=0
for mutation in M:
    q=copy.deepcopy(p); mutation(q)
    try: K["validate"](q)
    except AssertionError: rejected+=1
assert rejected==len(M)==16
print("K774 probe: controls=24 mutations=16 rejected=16 failures=0")
