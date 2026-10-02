#!/usr/bin/env python3
"""Hostile mutations for K830."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k830_sc_act_06_relative_family_admission_compiler.py")
S=importlib.util.spec_from_file_location("k830",P);M=importlib.util.module_from_spec(S);S.loader.exec_module(M)
def main()->int:
    mutations=[
        ("row count",lambda x:x["compiler"].__setitem__("row_count",17)),
        ("drop row",lambda x:x["compiler"].__setitem__("required_rows",x["compiler"]["required_rows"][:-1])),
        ("partial ellipticity",lambda x:x["compiler"].__setitem__("partial_pass_implies_ellipticity",True)),
        ("necessary sufficient",lambda x:x["compiler"].__setitem__("necessary_packet_is_sufficient_without_middle_exactness",True)),
        ("synthetic rejected",lambda x:x["exact_controls"].__setitem__("synthetic_candidate_admitted",False)),
        ("missing admitted",lambda x:x["exact_controls"].__setitem__("single_missing_candidate_admitted",True)),
        ("wrong missing row",lambda x:x["exact_controls"].__setitem__("single_missing_row","none")),
        ("GU missing hidden",lambda x:x["exact_controls"].__setitem__("current_gu_missing_row_count",0)),
        ("GU admitted",lambda x:x["exact_controls"].__setitem__("current_gu_admitted",True)),
        ("family invented",lambda x:x["decision"].__setitem__("actual_source_relative_family_constructed",True)),
        ("candidate invented",lambda x:x["decision"].__setitem__("actual_gu_candidate_admitted",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build());mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(name)
    print("K830 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())
