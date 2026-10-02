#!/usr/bin/env python3
"""Hostile mutations for K826."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
P=Path(__file__).with_name("k826_sc_act_06_relative_coefficient_ownership_gate.py")
S=importlib.util.spec_from_file_location("k826",P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main() -> int:
    mutations=[
        ("endpoint determines tangent",lambda x:x["ownership_theorem"].__setitem__("owned_endpoints_determine_relative_coefficient",True)),
        ("endpoint normalizes",lambda x:x["ownership_theorem"].__setitem__("owned_endpoints_determine_parameter_normalization",True)),
        ("interpolation harmless",lambda x:x["ownership_theorem"].__setitem__("endpoint_interpolation_may_be_reverse_selected",False)),
        ("unowned rank",lambda x:x["ownership_theorem"].__setitem__("unowned_interpolation_rank_is_credited",True)),
        ("reparam invariant",lambda x:x["ownership_theorem"].__setitem__("reparameterization_changes_delta",False)),
        ("different endpoint",lambda x:x["exact_controls"].__setitem__("same_endpoint_at_t1",False)),
        ("wrong A rank",lambda x:x["exact_controls"].__setitem__("Delta_A_rank",0)),
        ("wrong B rank",lambda x:x["exact_controls"].__setitem__("Delta_B_rank",1)),
        ("family invented",lambda x:x["decision"].__setitem__("actual_source_relative_family_constructed",True)),
        ("endpoint promoted",lambda x:x["decision"].__setitem__("endpoint_custody_promoted_to_relative_ownership",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
        ("ledger moved",lambda x:x.__setitem__("source_and_ledger_effect","MOVED")),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build()); mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(name)
    print("K826 hostile mutations rejected: 12/12"); return 0
if __name__=="__main__": raise SystemExit(main())
