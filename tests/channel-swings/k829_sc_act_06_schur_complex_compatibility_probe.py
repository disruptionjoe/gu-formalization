#!/usr/bin/env python3
"""Hostile mutations for K829."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k829_sc_act_06_schur_complex_compatibility.py")
S=importlib.util.spec_from_file_location("k829",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
    mutations=[
        ("wrong Schur",lambda x:x["schur_complex_theorem"].__setitem__("reduced_symbol","S=B")),
        ("wrong factorization",lambda x:x["schur_complex_theorem"].__setitem__("factorization","M=S")),
        ("bad gauge",lambda x:x["schur_complex_theorem"].__setitem__("full_gauge_descends_if","S G=0")),
        ("bad redundancy",lambda x:x["schur_complex_theorem"].__setitem__("full_redundancy_descends_if","R S=0")),
        ("kernel enough",lambda x:x["schur_complex_theorem"].__setitem__("kernel_equivalence_alone_authenticates_reduced_complex",True)),
        ("one side enough",lambda x:x["schur_complex_theorem"].__setitem__("owned_two_sided_mixed_blocks_required",False)),
        ("wrong S",lambda x:x["exact_controls"].__setitem__("S",[[1,0],[0,1]])),
        ("gauge fails",lambda x:x["exact_controls"].__setitem__("M_G",[0,1,0])),
        ("redundancy fails",lambda x:x["exact_controls"].__setitem__("R_M",[0,1,0])),
        ("complex invented",lambda x:x["decision"].__setitem__("actual_gu_mixed_complex_constructed",True)),
        ("maps invented",lambda x:x["decision"].__setitem__("actual_gu_gauge_or_redundancy_authenticated",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build());mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(name)
    print("K829 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())
