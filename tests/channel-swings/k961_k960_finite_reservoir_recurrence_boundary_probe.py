#!/usr/bin/env python3
"""Hostile mutation replay for K961."""
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent; s=importlib.util.spec_from_file_location("k961",H/"k961_k960_finite_reservoir_recurrence_boundary.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def ok(p):
    try: m.validate(p); return True
    except (AssertionError,KeyError): return False
def main():
    p=m.build(); muts=[
      lambda x:x["theorem"].__setitem__("finite_trigonometric_polynomial",False), lambda x:x["theorem"].__setitem__("normalization","f(0)=0"),
      lambda x:x["theorem"].__setitem__("requires_commuting_environment_hamiltonians",True), lambda x:x["exact_controls"].__setitem__("weights_sum","0"),
      lambda x:x["exact_controls"].__setitem__("all_returns_near_one",False), lambda x:x["decision"].__setitem__("finite_closed_recurrence_proved",False),
      lambda x:x["ownership"].__setitem__("finite_hilbert_and_trace_rule_imported",False), lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),
      lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)]
    caught=0
    for f in muts: q=copy.deepcopy(p); f(q); caught += not ok(q)
    print(f"K961 hostile: {caught}/{len(muts)}"); return 0 if caught==len(muts) else 1
if __name__=="__main__": raise SystemExit(main())
