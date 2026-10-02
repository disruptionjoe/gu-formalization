#!/usr/bin/env python3
"""Hostile mutations for K797."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k797_k500_current_custody_no_assembly_theorem.py"
def load(): s=importlib.util.spec_from_file_location("k797",SCRIPT); assert s and s.loader; m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def main():
 m=load(); b=m.build(); fs=[lambda p:p.__setitem__("result_id","MUTANT"),lambda p:p.__setitem__("pinned_inputs",{})]
 for k in b["no_assembly_theorem"]: fs.append(lambda p,k=k:p["no_assembly_theorem"].__setitem__(k,not p["no_assembly_theorem"][k]))
 for side in ("A_bundle","B_bundle"):
  for _ in range(3): fs.append(lambda p,s=side:p["minimal_native_reopeners"][s].pop())
 fs += [lambda p:p["minimal_native_reopeners"].__setitem__("either_bundle_alone_suffices_for_complete_K500",True),lambda p:p["minimal_native_reopeners"].__setitem__("both_bundles_on_one_domain_are_sufficient_inputs_for_existing_compilers",False)]
 for k in b["dependency_reconciliation"]: fs.append(lambda p,k=k:p["dependency_reconciliation"].__setitem__(k,not p["dependency_reconciliation"][k]))
 fs += [lambda p:p["decision"].__setitem__("current_serialized_K500_assembly_route_closed",False),lambda p:p["decision"].__setitem__("new_native_data_required",False),lambda p:p.__setitem__("source_and_ledger_effect","PROMOTED")]
 while len(fs)<28: fs.append(lambda p:p["no_assembly_theorem"].__setitem__("therefore_projection_does_not_entail_A_and_B",False))
 caught=0
 for f in fs:
  q=copy.deepcopy(b); f(q)
  try:m.validate(q)
  except (AssertionError,KeyError,ValueError):caught+=1
 assert caught==28; print("K797 probe: 28/28 hostile mutations rejected"); return 0
if __name__=="__main__": raise SystemExit(main())
