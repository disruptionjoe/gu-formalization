#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util
from decimal import Decimal
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("k495",H/"k495_k176_kernel_l2_outward.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 o=p["outward_evaluation"];a=o["direct_integral_anchor_controls"]
 return [p["result_id"]=="K495-K176-KERNEL-L2-OUTWARD",p["classification"]=="INTERNAL_STRUCTURAL_ONLY",p["analytic_reduction"]["even_positive_and_decreasing_in_abs_p"] is True,o["kernel_positive_and_mesh_monotone"] is True,o["strictly_below_target"] is True,Decimal(o["single_kernel_norm_squared_upper"])<Decimal(1)/Decimal(256),Decimal(o["margin_to_target"])>0,all(x["closed_form_inside_direct_enclosure"] for x in a),p["decision"]["K176_norm_upper_improves_to"]=="1/16",p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0
 for m in [lambda q:q["outward_evaluation"].__setitem__("strictly_below_target",False),lambda q:q["analytic_reduction"].__setitem__("even_positive_and_decreasing_in_abs_p",False),lambda q:q["outward_evaluation"]["direct_integral_anchor_controls"][0].__setitem__("closed_form_inside_direct_enclosure",False),lambda q:q["decision"].__setitem__("K176_norm_upper_improves_to","5/6"),lambda q:q.__setitem__("source_and_ledger_effect","moved"),lambda q:q.__setitem__("classification","PHYSICAL")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==6
if __name__=="__main__":
 p=K.build();c=checks(p);ok=all(c) and selftest();print(f"K495 controls: {sum(c)}/{len(c)}; hostile: {'PASS 6/6' if selftest() else 'FAIL'}");raise SystemExit(0 if ok else 1)
