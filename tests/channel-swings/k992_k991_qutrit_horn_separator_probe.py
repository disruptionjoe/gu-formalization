#!/usr/bin/env python3
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k992",H/"k992_k991_qutrit_horn_separator.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["dependency_checks"].__setitem__("charge_gap_theorem_available",False),lambda x:x["construction"].__setitem__("simultaneously_observed_gaps",[2]),lambda x:x["construction"].__setitem__("minimal_dimension_for_simultaneous_gap_one_and_two",2),lambda x:x["construction"].__setitem__("gap_two_matched",False),lambda x:x["construction"].__setitem__("gap_one_strictly_separates_every_finite_nonzero_angle",False),lambda x:x["exact_controls"].__setitem__("rows",[]),lambda x:x["exact_controls"].__setitem__("all_gap_two_identities_replayed",False),lambda x:x["exact_controls"].__setitem__("all_gap_one_closed_forms_replayed",False),lambda x:x["exact_controls"].__setitem__("all_gap_one_separations_positive",False),lambda x:x["ownership"].__setitem__("qutrit_charge_sector_imported",False),lambda x:x["ownership"].__setitem__("gap_one_coherence_access_imported",False),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("named_brownian_and_compound_poisson_horns_system_separable_after_declared_enlargement",False),lambda x:x["decision"].__setitem__("same_qubit_system_remains_nonidentifying",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K992 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
