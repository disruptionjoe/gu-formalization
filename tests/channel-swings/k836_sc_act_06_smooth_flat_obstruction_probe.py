#!/usr/bin/env python3
"""Hostile mutations for K836."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k836_sc_act_06_smooth_flat_obstruction.py"); S=importlib.util.spec_from_file_location("k836",P); M=importlib.util.module_from_spec(S); assert S.loader; S.loader.exec_module(M)
def main()->int:
    muts=[
      ("jacobian",lambda x:x["smooth_control"].__setitem__("jacobian_rank",2)),
      ("kernel",lambda x:x["smooth_control"].__setitem__("tangent_kernel_basis",[[0,1]])),
      ("derivative",lambda x:x["smooth_control"].__setitem__("all_derivatives_of_f_at_origin_zero",False)),
      ("series",lambda x:x["smooth_control"].__setitem__("formal_taylor_series","x^2")),
      ("positive",lambda x:x["smooth_control"].__setitem__("f_strictly_positive_off_origin",False)),
      ("zero locus",lambda x:x["smooth_control"].__setitem__("exact_zero_locus_near_origin",[])),
      ("formal dim",lambda x:x["smooth_control"].__setitem__("formal_zero_set_dimension",0)),
      ("actual dim",lambda x:x["smooth_control"].__setitem__("actual_local_dimension",1)),
      ("finite jets",lambda x:x["theorem"].__setitem__("all_finite_jets_determine_smooth_zero_germ",True)),
      ("formal decides",lambda x:x["theorem"].__setitem__("complete_formal_series_determines_smooth_zero_germ",True)),
      ("formal implies",lambda x:x["theorem"].__setitem__("formal_unobstructedness_implies_smooth_unobstructedness_without_extra_hypotheses",True)),
      ("GU map",lambda x:x["decision"].__setitem__("actual_gu_smooth_kuranishi_map_constructed",True)),
    ]
    for n,m in muts:
      p=copy.deepcopy(M.build());m(p)
      try:M.validate(p)
      except AssertionError:continue
      raise AssertionError(n)
    print("K836 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())
