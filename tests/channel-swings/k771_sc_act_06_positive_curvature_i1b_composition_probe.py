#!/usr/bin/env python3
"""Hostile mutation probe for K771."""
from __future__ import annotations
import copy, os, runpy, sys
from pathlib import Path
try:
    import sage.all  # noqa: F401
except ModuleNotFoundError:
    os.execvp("sage", ["sage", "-python", *sys.argv])
ROOT=Path(__file__).resolve().parents[2]
K=runpy.run_path(str(ROOT/"tests/channel-swings/k771_sc_act_06_positive_curvature_i1b_composition.py"))
p=K["build"](); K["validate"](p)
def row(q, name):
    match = next((x for x in q["exact_controls"]["cases"] if x["case"] == name), None)
    assert match is not None, f"missing exact-control case: {name}"
    return match
M=[
 lambda q:q.__setitem__("classification","SOURCE_NATIVE_ROUTE"),
 lambda q:q["composition_theorem"].__setitem__("separate_rank_addition_used",True),
 lambda q:q["composition_theorem"].__setitem__("all_invariant_blocks_enumerated",False),
 lambda q:row(q,"native_nonnull").__setitem__("distortion_i1b_rank",130911),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("distortion_i1b_rank",122745),
 lambda q:row(q,"native_nonnull").__setitem__("distortion_positive_curvature_rank",212991),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("distortion_summed_operator_rank",221184),
 lambda q:row(q,"native_nonnull").__setitem__("total_coupled_rank",221190),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("metric_rank_increment",4),
 lambda q:row(q,"native_nonnull").__setitem__("bosonic_middle_cohomology_dimension",0),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("bosonic_middle_cohomology_dimension",0),
 lambda q:row(q,"native_nonnull").__setitem__("euler_times_gauge_rank",1),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("redundancy_times_euler_rank",1),
 lambda q:row(q,"native_nonnull").__setitem__("middle_exact",True),
 lambda q:q["decision"].__setitem__("source_owned_total_action",True),
 lambda q:q["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted",True),
]
rejected=0
for mutation in M:
    q=copy.deepcopy(p); mutation(q)
    try: K["validate"](q)
    except AssertionError: rejected+=1
assert rejected==len(M)==16
print("K771 probe: controls=30 mutations=16 rejected=16 failures=0")
