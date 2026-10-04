#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k993",H/"k993_k992_finite_harmonic_nonidentifiability.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("pairwise_qutrit_separator_preserved",False),lambda x:x["theorem"].__setitem__("no_zero_angle_atoms",False),lambda x:x["theorem"].__setitem__("fourier_moments_zero_on_S",False),lambda x:x["theorem"].__setitem__("same_rate_gives_identical_exponents_on_S",False),lambda x:x["theorem"].__setitem__("jump_laws_distinct",False),lambda x:x["theorem"].__setitem__("finite_dimensional_charge_tomography_identifies_general_phase_law",True),lambda x:x["exact_controls"].__setitem__("rows",[]),lambda x:x["exact_controls"].__setitem__("orders_exceed_observed_max",False),lambda x:x["exact_controls"].__setitem__("all_moments_numerically_zero",False),lambda x:x["exact_controls"].__setitem__("all_exponents_equal",False),lambda x:x["exact_controls"].__setitem__("support_cardinalities_distinct",False),lambda x:x["ownership"].__setitem__("finite_charge_spectrum_imported",False),lambda x:x["ownership"].__setitem__("jump_laws_and_rate_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_observable_owner_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("qutrit_pairwise_discrimination_not_full_model_identification",False),lambda x:x["decision"].__setitem__("arbitrary_finite_charge_spectrum_leaves_microscopic_horns",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K993 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
