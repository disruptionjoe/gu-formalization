#!/usr/bin/env python3
"""Hostile mutations for K819."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path

P=Path(__file__).with_name("k819_sc_act_06_second_order_zero_locus_obstruction.py")
S=importlib.util.spec_from_file_location("k819",P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)

def main() -> int:
    mutations=[
        ("first implies second",lambda x:x["second_order_theorem"].__setitem__("first_order_pass_implies_second_order_pass",True)),
        ("kernel ignored",lambda x:x["second_order_theorem"].__setitem__("kernel_choice_must_be_solved",False)),
        ("full family",lambda x:x["second_order_theorem"].__setitem__("second_order_pass_proves_full_family",True)),
        ("obstructed branch",lambda x:x["exact_controls"].__setitem__("obstructed_real_second_order_solution_exists",True)),
        ("repair lost",lambda x:x["exact_controls"].__setitem__("repairable_second_order_solution_exists",False)),
        ("wrong speeds",lambda x:x["exact_controls"].__setitem__("repairable_kernel_speeds",[0])),
        ("source invented",lambda x:x["decision"].__setitem__("actual_source_two_jet_constructed",True)),
        ("k815 promoted",lambda x:x["decision"].__setitem__("k815_alone_certifies_solution_family",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
        ("wrong target",lambda x:x.__setitem__("target_claim","NONE")),
        ("ledger moved",lambda x:x.__setitem__("source_and_ledger_effect","MOVED")),
        ("lost formula",lambda x:x["second_order_theorem"].__setitem__("obstruction","none")),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build()); mut(q)
        try: M.validate(q)
        except AssertionError: continue
        raise AssertionError(name)
    print("K819 hostile mutations rejected: 12/12"); return 0
if __name__ == "__main__": raise SystemExit(main())
