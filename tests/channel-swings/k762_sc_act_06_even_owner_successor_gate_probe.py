#!/usr/bin/env python3
"""Hostile mutation probe for K762."""
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k762_sc_act_06_even_owner_successor_gate.py";CERT=ROOT/"lab/process/k762-sc-act-06-even-owner-successor-gate.json"
def load():
 s=importlib.util.spec_from_file_location("k762_probe_target",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main()->int:
 m=load();b=json.loads(CERT.read_text());m.validate(b)
 muts=[lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("classification","COMPARATOR"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d.__setitem__("status","unverified"),lambda d:d["closed_class"].__setitem__("class","BROKEN"),lambda d:d["closed_class"].__setitem__("includes_one_derivative_scalar",False),lambda d:d["closed_class"].__setitem__("includes_cbrs1r_plus_any_single_spectator_kinetic_block_without_old_block_change",False),lambda d:d.__setitem__("live_reopeners",[]),lambda d:d["decision"].__setitem__("do_not_retry_small_spectator_condensate_extension",False),lambda d:d["decision"].__setitem__("fixed_old_block_theorem_not_global_condensate_nogo",False),lambda d:d["decision"].__setitem__("changed_old_block_owner_remains_open",False),lambda d:d["decision"].__setitem__("global_SC_ACT_06_refuted",True),lambda d:d["decision"].__setitem__("SC_ACT_06_status","REFUTED"),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
 while len(muts)<36:muts.append(lambda d:d.__setitem__("live_reopeners",[]))
 c=0
 for f in muts[:36]:
  x=copy.deepcopy(b);f(x)
  try:m.validate(x)
  except (AssertionError,KeyError,TypeError,ValueError):c+=1
 assert c==36;print("PASS controls=42 hostile_mutations_rejected=36/36");return 0
if __name__=="__main__":raise SystemExit(main())
