#!/usr/bin/env python3
from __future__ import annotations
import argparse,copy,importlib.util
from fractions import Fraction
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k493",H/"k493_k152_base_cross_prefix_tail_budget.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 d=p["decision"];x=p["decomposition"];r=p["native_sector_budgets"]
 return [p["result_id"]=="K493-K152-BASE-CROSS-PREFIX-TAIL-BUDGET",len(r)==2,r[0]["charge"]==[0,0],r[1]["charge"]==[1,0],x["no_separate_plus_minus_256_bounds"] is True,x["scalar_cross"].startswith("<phi,"),d["actual_native_first_block_used"] is True,d["complete_later_order_tail_used"] is True,d["finite_orders_2_through_12_numerically_evaluated"] is False,all(q["order_12_tail_smaller_than_order_1_tail"] for q in r),all(q["current_order_1_decides_nonzero"] is False for q in r),all(Fraction(q["post_order_12_normal_cross_abs_upper"])>0 for q in r),p["source_and_ledger_effect"]=="none","inconclusive" in p["claim_ceiling"]]
def selftest():
 p=K.build();n=0
 for m in [lambda q:q["decision"].__setitem__("actual_native_first_block_used",False),lambda q:q["decision"].__setitem__("finite_orders_2_through_12_numerically_evaluated",True),lambda q:q["decomposition"].__setitem__("no_separate_plus_minus_256_bounds",False),lambda q:q["native_sector_budgets"][0].__setitem__("current_order_1_decides_nonzero",True),lambda q:q.__setitem__("source_and_ledger_effect","moved"),lambda q:q["native_sector_budgets"][1].__setitem__("order_12_tail_smaller_than_order_1_tail",False),lambda q:q.__setitem__("claim_ceiling",q["claim_ceiling"].replace("inconclusive","decisive")),lambda q:q["decision"].__setitem__("complete_later_order_tail_used",False)]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==8
def main():
 p=argparse.ArgumentParser();p.add_argument("--selftest",action="store_true");a=p.parse_args()
 if a.selftest:ok=selftest();print("K493 SELFTEST", "PASS 8/8" if ok else "FAIL");return 0 if ok else 1
 r=checks(K.build());print(f"K493 controls: {sum(r)}/{len(r)}");return 0 if all(r) else 1
if __name__=="__main__":raise SystemExit(main())
