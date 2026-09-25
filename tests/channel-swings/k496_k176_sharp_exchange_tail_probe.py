#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from fractions import Fraction
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k496",H/"k496_k176_sharp_exchange_tail.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 t=p["sharp_tail"];q=p["premises"];d=p["decision"]
 return [p["result_id"]=="K496-K176-SHARP-EXCHANGE-TAIL",q["kernel_certificate"]=="K495-K176-KERNEL-L2-OUTWARD",q["exchange_monomials"]==16,q["cross_polarity_cancellation_used"] is False,t["coefficient_upper"]=="1",t["after_order_1"]=="312/125",Fraction(t["after_order_12"])>0,t["strictly_improves_K176_coefficient"] is True,t["all_order_tail_convergent"] is True,d["signed_orders_2_through_12_still_required_for_cross_decision"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0
 for m in [lambda q:q["premises"].__setitem__("exchange_monomials",15),lambda q:q["premises"].__setitem__("cross_polarity_cancellation_used",True),lambda q:q["sharp_tail"].__setitem__("coefficient_upper","40/3"),lambda q:q["sharp_tail"].__setitem__("strictly_improves_K176_coefficient",False),lambda q:q["decision"].__setitem__("signed_orders_2_through_12_still_required_for_cross_decision",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==6
if __name__=="__main__":
 p=K.build();c=checks(p);h=selftest();print(f"K496 controls: {sum(c)}/{len(c)}; hostile: {'PASS 6/6' if h else 'FAIL'}");raise SystemExit(0 if all(c) and h else 1)
