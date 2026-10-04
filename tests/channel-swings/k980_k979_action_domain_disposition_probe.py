#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k980",H/"k980_k979_action_domain_disposition.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("input_ids",[]),lambda x:x["dependency_checks"].__setitem__("all_source_and_ledger_effect_none",False),lambda x:x["dependency_checks"].__setitem__("all_prediction_or_confirmation_withheld",False),lambda x:x["dependency_checks"].__setitem__("assumption_fork_unselected",False),lambda x:x["decision"].__setitem__("bounded_product_autonomous_parent_excluded",False),lambda x:x["decision"].__setitem__("fresh_collision_family_uniformly_approximates",False),lambda x:x["decision"].__setitem__("fresh_collision_family_imports_singular_resources",False),lambda x:x["demand"].__setitem__("gu_physical_quotient_and_positive_effect_pairing_required",False),lambda x:x["demand"].__setitem__("gu_action_owned_local_coupling_required",False),lambda x:x["demand"].__setitem__("selected_horn_and_common_domain_required",False),lambda x:x["demand"].__setitem__("controlled_limit_or_reset_accounting_required",False),lambda x:x["demand"].__setitem__("remote_marginal_and_locality_theorem_required",False),lambda x:x["demand"].__setitem__("distinct_empirical_holdout_frozen_before_scoring_required",False),lambda x:x["discriminator"].__setitem__("status","scored"),lambda x:x["ownership"].__setitem__("repository_conditional_models_only",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("source_claim_or_ledger_verdict_changed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K980 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
