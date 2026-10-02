#!/usr/bin/env python3
"""Hostile mutations for K798."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k798_k500_current_packet_closure.py"
def load(): s=importlib.util.spec_from_file_location("k798",SCRIPT); assert s and s.loader; m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def main():
 m=load(); b=m.build(); fs=[lambda p:p.__setitem__("result_id","MUTANT"),lambda p:p.__setitem__("pinned_inputs",{})]
 for k in b["composition"]: fs.append(lambda p,k=k:p["composition"].__setitem__(k,not p["composition"][k]))
 for k in b["decision"]:
  if isinstance(b["decision"][k],bool): fs.append(lambda p,k=k:p["decision"].__setitem__(k,not p["decision"][k]))
 fs += [lambda p:p["reranked_frontier"].__setitem__("repeat_prohibition","repeat current packet"),lambda p:p["daily_review"].__setitem__("local_date","2026-10-01"),lambda p:p.__setitem__("source_and_ledger_effect","PROMOTED")]
 while len(fs)<30: fs.append(lambda p:p["decision"].__setitem__("complete_native_K500_route_killed",True))
 caught=0
 for f in fs:
  q=copy.deepcopy(b); f(q)
  try:m.validate(q)
  except (AssertionError,KeyError,ValueError):caught+=1
 assert caught==30; print("K798 probe: 30/30 hostile mutations rejected"); return 0
if __name__=="__main__": raise SystemExit(main())
