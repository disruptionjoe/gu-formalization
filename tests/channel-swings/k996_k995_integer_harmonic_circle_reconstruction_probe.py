#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k996",H/"k996_k995_integer_harmonic_circle_reconstruction.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[
      lambda x:x["theorem"].__setitem__("all_integer_fourier_coefficients_determine_circle_measure",False),lambda x:x["theorem"].__setitem__("fixed_time_only",False),
      lambda x:x["theorem"].__setitem__("real_line_lift_identified",True),lambda x:x["theorem"].__setitem__("finite_harmonic_sets_remain_nonidentifying",False),
      lambda x:x["exact_controls"].__setitem__("weights_sum_to_one",False),lambda x:x["exact_controls"].__setitem__("all_cyclic_harmonics_used",False),
      lambda x:x["exact_controls"].__setitem__("inverse_dft_reconstructs_measure",False),lambda x:x["exact_controls"].__setitem__("inverse_dft_max_error",1.0),
      lambda x:x["exact_controls"].__setitem__("planted_coefficient_change_detected",False),lambda x:x["ownership"].__setitem__("circle_phase_quotient_imported",False),
      lambda x:x["ownership"].__setitem__("integer_charge_ladder_imported",False),lambda x:x["ownership"].__setitem__("positive_state_effect_pairing_imported",False),
      lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),
      lambda x:x["decision"].__setitem__("k993_finite_ceiling_preserved",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")]
    caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K996 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
