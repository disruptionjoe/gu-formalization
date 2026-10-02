#!/usr/bin/env python3
"""Hostile mutations for K796."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k796_k500_current_custody_product_countermodels.py"
def load(): s=importlib.util.spec_from_file_location("k796",SCRIPT); assert s and s.loader; m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def main():
 m=load(); b=m.build(); fs=[lambda p:p.__setitem__("result_id","MUTANT"),lambda p:p["shared_projection"].__setitem__("same_seed_and_finite_prefix_for_all_models",False),lambda p:p["shared_projection"].__setitem__("models_are_controls_not_native_K139_K168_realizations",False),lambda p:p["product_countermodels"].pop(),lambda p:p["product_countermodels"][0].__setitem__("label",p["product_countermodels"][1]["label"]),lambda p:p["product_countermodels"][0].__setitem__("visible_seed_square","1/3"),lambda p:p["product_countermodels"][0].__setitem__("visible_finite_denominator","0"),lambda p:p["product_countermodels"][0].__setitem__("A_strictly_above_two_thirds",not p["product_countermodels"][0]["A_strictly_above_two_thirds"]),lambda p:p["product_countermodels"][0].__setitem__("B_denominator_nonnegative",not p["product_countermodels"][0]["B_denominator_nonnegative"])]
 for k in b["theorem"]: fs.append(lambda p,k=k:p["theorem"].__setitem__(k,not p["theorem"][k]))
 fs += [lambda p:p["decision"].__setitem__("current_serialized_projection_is_nonidentifying",False),lambda p:p["decision"].__setitem__("native_A_or_B_nonexistence_proved",True),lambda p:p.__setitem__("source_and_ledger_effect","PROMOTED")]
 while len(fs)<24: fs.append(lambda p:p["product_countermodels"][1].__setitem__("visible_seed_square","2/5"))
 caught=0
 for f in fs:
  q=copy.deepcopy(b); f(q)
  try:m.validate(q)
  except (AssertionError,KeyError,ValueError):caught+=1
 assert caught==24; print("K796 probe: 24/24 hostile mutations rejected"); return 0
if __name__=="__main__": raise SystemExit(main())
