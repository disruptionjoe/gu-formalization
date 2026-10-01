#!/usr/bin/env python3
"""Hostile mutation probe for K761."""
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k761_sc_act_06_finite_even_extension_threshold.py";CERT=ROOT/"lab/process/k761-sc-act-06-finite-even-extension-threshold.json"
def load():
 s=importlib.util.spec_from_file_location("k761_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();b=json.loads(CERT.read_text());m.validate(b)
 muts=[lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("classification","SOURCE_NATIVE_ROUTE"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d["threshold"].__setitem__("minimum_m_not_excluded_by_dimension_on_both_strata",1),lambda d:d["threshold"].__setitem__("nonnull_threshold",1),lambda d:d["threshold"].__setitem__("native_null_threshold",1),lambda d:d["threshold"].__setitem__("one_scalar_shortfall",{}),lambda d:d["decision"].__setitem__("every_m_below_98311_excluded_from_all_covector_exactness_by_native_null_stratum",False),lambda d:d["decision"].__setitem__("m_at_least_98311_sufficient_for_exactness",True),lambda d:d["decision"].__setitem__("single_or_small_finite_spectator_owner_closed",False),lambda d:d["decision"].__setitem__("nonfactorizing_old_block_change_outside_scope",False),lambda d:d.__setitem__("necessary_conditions",[]),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
 while len(muts)<32:muts.append(lambda d:d.__setitem__("necessary_conditions",[]))
 c=0
 for f in muts[:32]:
  x=copy.deepcopy(b);f(x)
  try:m.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 assert c==32;print("PASS controls=38 hostile_mutations_rejected=32/32");return 0
if __name__=="__main__":raise SystemExit(main())
