#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k975",H/"k975_k974_physical_domain_disposition.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["decision"].__setitem__("exact_exponential_positive_spectral_parent_requires_singular_energy_moments",False),lambda x:x["decision"].__setitem__("finite_energy_approximation_remains_possible",False),lambda x:x["demand"].__setitem__("gu_physical_quotient_and_positive_effect_pairing_required",False),lambda x:x["demand"].__setitem__("gu_action_owned_local_coupling_required",False),lambda x:x["demand"].__setitem__("energy_or_form_domain_owned_required",False),lambda x:x["demand"].__setitem__("spectral_measure_reset_or_resolution_law_owned_required",False),lambda x:x["demand"].__setitem__("remote_marginal_and_locality_theorem_required",False),lambda x:x["demand"].__setitem__("distinct_empirical_holdout_frozen_before_scoring_required",False),lambda x:x["ownership"].__setitem__("exact_and_regularized_models_repository_owned_only",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["ownership"].__setitem__("source_claim_or_ledger_verdict_changed",True),lambda x:x["discriminator"].__setitem__("status","scored")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K975 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
