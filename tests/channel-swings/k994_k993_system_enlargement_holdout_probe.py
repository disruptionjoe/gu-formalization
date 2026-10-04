#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k994",H/"k994_k993_system_enlargement_holdout.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("input_ids",[]),lambda x:x["dependency_checks"].__setitem__("named_pair_qutrit_separable",False),lambda x:x["dependency_checks"].__setitem__("finite_probe_not_full_identification",False),lambda x:x["preregistration"].__setitem__("status","scored"),lambda x:x["preregistration"].__setitem__("no_holdout_refit",False),lambda x:x["preregistration"].__setitem__("empirical_score_assigned",True),lambda x:x["preregistration"].__setitem__("absolute_separation",0),lambda x:x["boundary"].__setitem__("same_original_qubit_system",True),lambda x:x["boundary"].__setitem__("microscopic_record_required",True),lambda x:x["boundary"].__setitem__("action_owned_qutrit_charge_sector_required",False),lambda x:x["boundary"].__setitem__("positive_state_effect_and_gap_one_readout_required",False),lambda x:x["boundary"].__setitem__("distinguishes_named_pair_only",False),lambda x:x["boundary"].__setitem__("identifies_general_phase_law",True),lambda x:x["exact_controls"].__setitem__("gap_one_values_strictly_different",False),lambda x:x["ownership"].__setitem__("qutrit_sector_and_readout_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_observable_owner_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("nonrecord_pairwise_holdout_frozen",False),lambda x:x["decision"].__setitem__("k989_record_holdout_remains_distinct",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K994 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
