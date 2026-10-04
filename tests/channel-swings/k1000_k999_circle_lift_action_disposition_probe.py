#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k1000",H/"k1000_k999_circle_lift_action_disposition.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
 try:m.validate(p);return True
 except (AssertionError,KeyError):return False
def main():
 p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("input_ids",[]),lambda x:x["dependency_checks"].__setitem__("all_source_and_ledger_effect_none",False),lambda x:x["dependency_checks"].__setitem__("all_prediction_or_confirmation_withheld",False),lambda x:x["dependency_checks"].__setitem__("holdouts_frozen_not_scored",False),lambda x:x["identification_boundary"].__setitem__("finite_harmonic_set_identifies_unrestricted_circle_law",True),lambda x:x["identification_boundary"].__setitem__("all_integer_harmonics_at_fixed_time_identify_circle_marginal",False),lambda x:x["identification_boundary"].__setitem__("all_time_integer_harmonics_identify_circular_independent_increment_process",False),lambda x:x["identification_boundary"].__setitem__("single_time_marginal_identifies_generator",True),lambda x:x["identification_boundary"].__setitem__("complete_circular_process_identifies_real_lift",True),lambda x:x["identification_boundary"].__setitem__("winding_record_or_noninteger_probe_required_for_lift",False),lambda x:x["demand"].__setitem__("gu_physical_quotient_and_positive_effect_pairing_required",False),lambda x:x["demand"].__setitem__("gu_action_owned_charge_generator_and_integer_spectrum_required",False),lambda x:x["demand"].__setitem__("common_domain_and_locality_theorem_required",False),lambda x:x["demand"].__setitem__("finite_band_regularization_and_error_budget_required_if_access_is_finite",False),lambda x:x["demand"].__setitem__("winding_sensitive_record_required_for_real_lift_claim",False),lambda x:x["ownership"].__setitem__("repository_conditional_models_only",False),lambda x:x["ownership"].__setitem__("gu_action_phase_observable_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("source_claim_or_ledger_verdict_changed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x.__setitem__("source_and_ledger_effect","changed")]
 c=0
 for f in muts:q=copy.deepcopy(p);f(q);c+=not ok(q)
 print(f"K1000 hostile: {c}/{len(muts)}");return 0 if c==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
