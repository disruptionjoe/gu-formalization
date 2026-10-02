#!/usr/bin/env python3
"""Hostile mutations for K827."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
P=Path(__file__).with_name("k827_sc_act_06_regular_parameter_jet_invariance.py")
S=importlib.util.spec_from_file_location("k827",P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main() -> int:
    mutations=[
        ("regular condition",lambda x:x["jet_invariance_theorem"].__setitem__("regular_change_condition","phi'(0)=0")),
        ("order not preserved",lambda x:x["jet_invariance_theorem"].__setitem__("vanishing_order_preserved",False)),
        ("rank not preserved",lambda x:x["jet_invariance_theorem"].__setitem__("first_order_rank_preserved",False)),
        ("absolute scale",lambda x:x["jet_invariance_theorem"].__setitem__("first_order_scale_preserved",True)),
        ("singular harmless",lambda x:x["jet_invariance_theorem"].__setitem__("singular_change_may_raise_vanishing_order",False)),
        ("singular same class",lambda x:x["jet_invariance_theorem"].__setitem__("singular_change_is_same_normalization_class",True)),
        ("wrong regular derivative",lambda x:x["exact_controls"].__setitem__("regular_composite_derivative_at_zero",1)),
        ("wrong regular order",lambda x:x["exact_controls"].__setitem__("regular_composite_vanishing_order",2)),
        ("wrong singular order",lambda x:x["exact_controls"].__setitem__("singular_composite_vanishing_order",1)),
        ("normalization invented",lambda x:x["decision"].__setitem__("actual_source_normalization_constructed",True)),
        ("singular tangent credited",lambda x:x["decision"].__setitem__("singular_reparameterization_credited_as_zero_tangent",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build()); mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(name)
    print("K827 hostile mutations rejected: 12/12"); return 0
if __name__=="__main__": raise SystemExit(main())
