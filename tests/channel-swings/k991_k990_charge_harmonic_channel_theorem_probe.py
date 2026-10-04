#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k991",H/"k991_k990_charge_harmonic_channel_theorem.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build(); muts=[
        lambda x:x["theorem"].__setitem__("observable_harmonics_are_charge_differences",False),
        lambda x:x["theorem"].__setitem__("qubit_fixes_only_psi_2",False),
        lambda x:x["theorem"].__setitem__("qubit_nonzero_gap",1),
        lambda x:x["theorem"].__setitem__("qutrit_nonzero_gaps",[2]),
        lambda x:x["exact_controls"].__setitem__("weights_sum_to_one",False),
        lambda x:x["exact_controls"].__setitem__("all_matrix_units_checked",False),
        lambda x:x["exact_controls"].__setitem__("all_matrix_unit_identities_exact",False),
        lambda x:x["exact_controls"].__setitem__("diagonal_units_fixed",False),
        lambda x:x["exact_controls"].__setitem__("observed_gap_set",[2]),
        lambda x:x["ownership"].__setitem__("finite_charge_operator_imported",False),
        lambda x:x["ownership"].__setitem__("positive_matrix_pairing_imported",False),
        lambda x:x["ownership"].__setitem__("phase_law_and_characteristic_exponent_imported",False),
        lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),
        lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),
        lambda x:x["decision"].__setitem__("k956_qubit_samples_one_nonzero_harmonic",False),
        lambda x:x.__setitem__("source_and_ledger_effect","changed")]
    caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K991 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
