#!/usr/bin/env python3
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k976",H/"k976_k975_bounded_dilation_first_jet_obstruction.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ok(p):
    try:m.validate(p);return True
    except (AssertionError,KeyError):return False
def main():
    p=m.build();muts=[lambda x:x["theorem"].__setitem__("hypotheses",[]),lambda x:x["theorem"].__setitem__("first_jet_is_derivation",False),lambda x:x["theorem"].__setitem__("positive_rate_dephasing_is_not_a_commutator",False),lambda x:x["theorem"].__setitem__("exact_semigroup_parent_impossible_under_hypotheses",False),lambda x:x["exact_controls"].__setitem__("dephasing_of_P0_zero",False),lambda x:x["exact_controls"].__setitem__("dephasing_of_P1_zero",False),lambda x:x["exact_controls"].__setitem__("P0_and_P1_force_commuting_hamiltonian_diagonal",False),lambda x:x["exact_controls"].__setitem__("diagonal_commutator_on_Pplus_has_purely_imaginary_offdiagonal",False),lambda x:x["exact_controls"].__setitem__("dephasing_Pplus_has_real_symmetric_nonzero_offdiagonal",False),lambda x:x["exact_controls"].__setitem__("witness_separates_generators",False),lambda x:x["ownership"].__setitem__("bounded_autonomous_parent_only",False),lambda x:x["ownership"].__setitem__("unbounded_or_nondifferentiable_parent_excluded",True),lambda x:x["ownership"].__setitem__("correlated_assignment_or_reset_parent_excluded",True),lambda x:x["ownership"].__setitem__("gu_action_or_physical_quotient_constructed",True),lambda x:x["ownership"].__setitem__("prediction_or_confirmation_credit",True),lambda x:x["decision"].__setitem__("bounded_product_parent_first_jet_excluded",False),lambda x:x.__setitem__("source_and_ledger_effect","changed")];caught=0
    for f in muts:q=copy.deepcopy(p);f(q);caught+=not ok(q)
    print(f"K976 hostile: {caught}/{len(muts)}");return 0 if caught==len(muts) else 1
if __name__=="__main__":raise SystemExit(main())
