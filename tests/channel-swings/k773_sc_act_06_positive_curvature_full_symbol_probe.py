#!/usr/bin/env python3
"""Hostile mutation probe for K773."""
from __future__ import annotations
import copy, runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
K=runpy.run_path(str(ROOT/"tests/channel-swings/k773_sc_act_06_positive_curvature_full_symbol.py"))
p=K["build"](); K["validate"](p)
def row(q,name): return next(x for x in q["exact_controls"]["cases"] if x["case"]==name)
M=[
 lambda q:q.__setitem__("classification","SOURCE_NATIVE_ROUTE"),
 lambda q:q["composition_theorem"].__setitem__("mixed_boson_fermion_principal_blocks_vanish",False),
 lambda q:q["composition_theorem"].__setitem__("displayed_fermion_candidate_is_exact",False),
 lambda q:q["composition_theorem"].__setitem__("middle_cohomology_is_direct_sum",False),
 lambda q:q["composition_theorem"].__setitem__("bosonic_middle_classes_survive_full_symbol",False),
 lambda q:q["composition_theorem"].__setitem__("source_global_SC_ACT_06_refuted",True),
 lambda q:row(q,"native_nonnull").__setitem__("full_symbol_middle_cohomology_dimension",0),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("full_symbol_middle_cohomology_dimension",0),
 lambda q:row(q,"native_nonnull").__setitem__("full_symbol_exact",True),
 lambda q:row(q,"native_null_auxiliary_nonzero").__setitem__("fermion_middle_cohomology_dimension",1),
 lambda q:q["exact_controls"].__setitem__("fermion_two_block_rank",1919),
 lambda q:q["decision"].__setitem__("displayed_full_symbol_comparator_is_elliptic",True),
 lambda q:q.__setitem__("source_and_ledger_effect","MOVED"),
 lambda q:q.__setitem__("target_claim","NONE-NOT-A-KILL"),
]
rejected=0
for mutation in M:
    q=copy.deepcopy(p); mutation(q)
    try: K["validate"](q)
    except AssertionError: rejected+=1
assert rejected==len(M)==14
print("K773 probe: controls=22 mutations=14 rejected=14 failures=0")
