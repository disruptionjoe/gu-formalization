#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k998",H/"k998_k997_invisible_winding_lift_nonidentifiability.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
 try:m.validate(p);return True
 except (AssertionError,KeyError):return False
def main():
 p=m.build();muts=[lambda x:x["theorem"].__setitem__("all_integer_harmonics_identical",False),lambda x:x["theorem"].__setitem__("all_integer_charge_process_channels_identical",False),lambda x:x["theorem"].__setitem__("circular_path_process_identical",False),lambda x:x["theorem"].__setitem__("real_lift_laws_distinct",False),lambda x:x["theorem"].__setitem__("unwrapped_record_or_noninteger_probe_required",False),lambda x:x["exact_controls"].__setitem__("integer_invisibility_pass",False),lambda x:x["exact_controls"].__setitem__("integer_exponent_max_error",1.0),lambda x:x["exact_controls"].__setitem__("noninteger_probe_separates",False),lambda x:x["exact_controls"].__setitem__("added_jump_quadratic_variation_per_event",0.0),lambda x:x["exact_controls"].__setitem__("terminal_no_added_jump_probability_T2",1.0),lambda x:x["ownership"].__setitem__("real_lift_and_lattice_jump_process_imported",False),lambda x:x["ownership"].__setitem__("winding_record_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_native_record_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("complete_circle_identification_does_not_identify_real_lift",False),lambda x:x["decision"].__setitem__("k997_positive_result_preserved",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")]
 c=0
 for f in muts:q=copy.deepcopy(p);f(q);c+=not ok(q)
 print(f"K998 hostile: {c}/{len(muts)}");return 0 if c==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
