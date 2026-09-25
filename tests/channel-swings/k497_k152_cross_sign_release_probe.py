#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from fractions import Fraction
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k497",H/"k497_k152_cross_sign_release.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 r=p["native_sector_releases"];d=p["decision"];c=p["composition"]
 return [p["result_id"]=="K497-K152-CROSS-SIGN-RELEASE",len(r)==2,r[0]["charge"]==[0,0],r[1]["charge"]==[1,0],all(x["strictly_negative"] for x in r),all(Fraction(x["zero_exclusion_margin"])>0 for x in r),c["finite_orders_2_through_12_evaluated"] is False,d["both_crosses_strictly_negative"] is True,d["signed_orders_2_through_12_retired_for_this_decision"] is True,d["cyclic_complement_floor_emitted"] is False,d["noncyclic_floor_or_cross_emitted"] is False,d["K152_interval_emitted"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0
 for m in [lambda q:q["native_sector_releases"][0].__setitem__("strictly_negative",False),lambda q:q["composition"].__setitem__("finite_orders_2_through_12_evaluated",True),lambda q:q["decision"].__setitem__("both_crosses_strictly_negative",False),lambda q:q["decision"].__setitem__("cyclic_complement_floor_emitted",True),lambda q:q["decision"].__setitem__("K152_interval_emitted",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==6
if __name__=="__main__":
 p=K.build();c=checks(p);h=selftest();print(f"K497 controls: {sum(c)}/{len(c)}; hostile: {'PASS 6/6' if h else 'FAIL'}");raise SystemExit(0 if all(c) and h else 1)
