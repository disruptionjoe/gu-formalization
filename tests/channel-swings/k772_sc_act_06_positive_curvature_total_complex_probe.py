#!/usr/bin/env python3
"""Hostile mutation probe for K772."""
from __future__ import annotations
import copy, os, runpy, sys
from pathlib import Path
try:
    import sage.all  # noqa: F401
except ModuleNotFoundError:
    os.execvp("sage", ["sage", "-python", *sys.argv])
ROOT=Path(__file__).resolve().parents[2]
K=runpy.run_path(str(ROOT/"tests/channel-swings/k772_sc_act_06_positive_curvature_total_complex.py"))
p=K["build"](); K["validate"](p)
def row(q, name):
    match = next((x for x in q["exact_controls"]["cases"] if x["case"] == name), None)
    assert match is not None, f"missing exact-control case: {name}"
    return match
M=[
 lambda q:q.__setitem__("classification","SOURCE_NATIVE_ROUTE"),
 lambda q:q["complex_theorem"].__setitem__("curvature_only_gauge_automatically_added",True),
 lambda q:q["complex_theorem"].__setitem__("accidental_candidate_kernel_promoted_to_gauge",True),
 lambda q:row(q,"native_nonnull").__setitem__("internal_candidate_dimension",16383),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("internal_candidate_rank",16383),
 lambda q:row(q,"native_nonnull").__setitem__("combined_on_internal_candidate_rank",8192),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("internal_candidate_kernel_dimension",8192),
 lambda q:row(q,"native_nonnull").__setitem__("candidate_kernel_equals_distortion_kernel",False),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("total_actual_gauge_rank",8197),
 lambda q:row(q,"native_nonnull").__setitem__("summed_euler_rank",221188),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("refined_middle_cohomology_dimension",0),
 lambda q:row(q,"native_nonnull").__setitem__("euler_times_metric_gauge_rank",1),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("middle_exact",True),
 lambda q:q["decision"].__setitem__("source_owned_total_action",True),
 lambda q:q["decision"].__setitem__("all_covector_exactness_proved",True),
 lambda q:q["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted",True),
]
rejected=0
for mutation in M:
    q=copy.deepcopy(p); mutation(q)
    try: K["validate"](q)
    except AssertionError: rejected+=1
assert rejected==len(M)==16
print("K772 probe: controls=28 mutations=16 rejected=16 failures=0")
