#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k999",H/"k999_k998_operational_circle_lift_holdouts.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
 try:m.validate(p);return True
 except (AssertionError,KeyError):return False
def main():
 p=m.build();muts=[lambda x:x["finite_band_theorem"].__setitem__("declared_regularity_budget_required",False),lambda x:x["finite_band_theorem"].__setitem__("unrestricted_finite_band_identification",True),lambda x:x["finite_band_theorem"].__setitem__("k993_ceiling_preserved",False),lambda x:x["exact_controls"].__setitem__("tail_bound_pass",False),lambda x:x["exact_controls"].__setitem__("positive_tail_present",False),lambda x:x["exact_controls"].__setitem__("sampled_tail_squared",1e9),lambda x:x["frozen_holdout"].__setitem__("calibration","different"),lambda x:x["frozen_holdout"].__setitem__("base_lift_event_probability",0.1),lambda x:x["frozen_holdout"].__setitem__("jump_lift_event_probability",0.1),lambda x:x["frozen_holdout"].__setitem__("frozen_not_scored",False),lambda x:x["ownership"].__setitem__("sobolev_class_and_budget_imported",False),lambda x:x["ownership"].__setitem__("unwrapped_record_and_apparatus_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_observable_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("finite_band_data_give_conditional_approximation_not_unrestricted_identification",False),lambda x:x["decision"].__setitem__("complete_integer_harmonics_still_do_not_resolve_winding_lift",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")]
 c=0
 for f in muts:q=copy.deepcopy(p);f(q);c+=not ok(q)
 print(f"K999 hostile: {c}/{len(muts)}");return 0 if c==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
