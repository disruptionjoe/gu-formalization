#!/usr/bin/env python3
import copy,importlib.util,sys
from pathlib import Path
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H));s=importlib.util.spec_from_file_location("k969",H/"k969_k968_explicit_recurrence_holdout.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["theorem"].__setitem__("all_phases_one",False),lambda x:x["theorem"].__setitem__("not_a_minimal_recurrence_claim",False),lambda x:x["exact_controls"].__setitem__("recurrence_after_calibration",False),lambda x:x["exact_controls"].__setitem__("atomic_return_error",1),lambda x:x["exact_controls"].__setitem__("atomic_imag",1),lambda x:x["exact_controls"].__setitem__("late_gap_above_0_999",False),lambda x:x["holdout"].__setitem__("status","scored"),lambda x:x["decision"].__setitem__("bounded_fit_cannot_decide_parent",False),lambda x:x["ownership"].__setitem__("finite_grid_and_holdout_location_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True)];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K969 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
