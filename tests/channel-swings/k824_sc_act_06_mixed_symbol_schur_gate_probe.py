#!/usr/bin/env python3
"""Hostile mutations for K824."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
P=Path(__file__).with_name("k824_sc_act_06_mixed_symbol_schur_gate.py")
S=importlib.util.spec_from_file_location("k824",P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main() -> int:
    mutations=[
        ("wrong Schur",lambda x:x["mixed_symbol_schur_theorem"].__setitem__("effective_bosonic_symbol","B")),
        ("zero loses kernel",lambda x:x["mixed_symbol_schur_theorem"].__setitem__("zero_mixed_blocks_preserve_bosonic_kernel",False)),
        ("one-sided repair",lambda x:x["mixed_symbol_schur_theorem"].__setitem__("one_sided_mixed_block_repairs_bosonic_kernel",True)),
        ("two-sided no effect",lambda x:x["mixed_symbol_schur_theorem"].__setitem__("two_sided_mixed_blocks_can_change_bosonic_kernel",False)),
        ("unowned credited",lambda x:x["mixed_symbol_schur_theorem"].__setitem__("unowned_mixed_blocks_are_credited",True)),
        ("Schur global",lambda x:x["mixed_symbol_schur_theorem"].__setitem__("schur_invertibility_alone_proves_a_full_deformation_complex",True)),
        ("wrong one rank",lambda x:x["exact_controls"].__setitem__("one_sided_full_rank",3)),
        ("wrong two rank",lambda x:x["exact_controls"].__setitem__("two_sided_full_rank",2)),
        ("source invented",lambda x:x["decision"].__setitem__("actual_source_mixed_packet_constructed",True)),
        ("current repaired",lambda x:x["decision"].__setitem__("current_zero_fermion_block_repaired",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
        ("ledger moved",lambda x:x.__setitem__("source_and_ledger_effect","MOVED")),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build()); mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(name)
    print("K824 hostile mutations rejected: 12/12"); return 0
if __name__=="__main__": raise SystemExit(main())
