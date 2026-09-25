#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from fractions import Fraction
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k502",H/"k502_k172_native_first_level_leakage_bound.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 r=p["native_sector_bounds"];d=p["decision"]
 return [p["result_id"]=="K502-K172-NATIVE-FIRST-LEVEL-LEAKAGE-BOUND",len(r)==2,r[0]["charge"]==[0,0],r[1]["charge"]==[1,0],all(x["bath_level"]==1 for x in r),all(Fraction(x["normal_leakage_norm_upper"])>0 for x in r),r[0]["D_multiplicity"]==1,r[1]["D_multiplicity"]==2,all(x["scalar_256_contributes_to_leakage"] is False for x in r),all(x["uniform_all_level_bound"] is False for x in r),d["actual_native_level_evaluated"] is True,d["complete_K500_uniform_leakage_emitted"] is False,d["noncyclic_floor_emitted"] is False,d["K473_released"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0
 for m in [lambda q:q["native_sector_bounds"][0].__setitem__("bath_level",2),lambda q:q["native_sector_bounds"][0].__setitem__("scalar_256_contributes_to_leakage",True),lambda q:q["native_sector_bounds"][1].__setitem__("D_multiplicity",1),lambda q:q["native_sector_bounds"][0].__setitem__("uniform_all_level_bound",True),lambda q:q["decision"].__setitem__("complete_K500_uniform_leakage_emitted",True),lambda q:q["decision"].__setitem__("K473_released",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==7
if __name__=="__main__":
 p=K.build();c=checks(p);h=selftest();print(f"K502 controls: {sum(c)}/{len(c)}; hostile: {'PASS 7/7' if h else 'FAIL'}");raise SystemExit(0 if all(c) and h else 1)
