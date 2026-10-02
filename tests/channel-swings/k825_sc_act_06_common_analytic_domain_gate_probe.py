#!/usr/bin/env python3
"""Hostile mutations for K825."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
P=Path(__file__).with_name("k825_sc_act_06_common_analytic_domain_gate.py")
S=importlib.util.spec_from_file_location("k825",P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main() -> int:
    mutations=[
        ("pointwise common",lambda x:x["common_domain_theorem"].__setitem__("pointwise_closed_or_self_adjoint_implies_common_domain",True)),
        ("identity allowed",lambda x:x["common_domain_theorem"].__setitem__("identity_comparison_allowed_when_domains_differ",True)),
        ("rank closes domain",lambda x:x["common_domain_theorem"].__setitem__("pointwise_symbol_rank_implies_closed_family_exactness",True)),
        ("drop uniformity",lambda x:x["common_domain_theorem"].__setitem__("uniform_graph_control_needed_for_parameter_uniformity",False)),
        ("equal domains",lambda x:x["exact_controls"].__setitem__("domains_equal",True)),
        ("wrong good exponent",lambda x:x["exact_controls"].__setitem__("witness_integrability_exponent_good","-1")),
        ("wrong bad exponent",lambda x:x["exact_controls"].__setitem__("witness_integrability_exponent_bad","1")),
        ("transport fails",lambda x:x["exact_controls"].__setitem__("reflection_maps_D0_onto_D1",False)),
        ("domain invented",lambda x:x["decision"].__setitem__("actual_gu_common_domain_constructed",True)),
        ("pointwise credited",lambda x:x["decision"].__setitem__("pointwise_closedness_credited_as_common_domain",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
        ("ledger moved",lambda x:x.__setitem__("source_and_ledger_effect","MOVED")),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build()); mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(name)
    print("K825 hostile mutations rejected: 12/12"); return 0
if __name__=="__main__": raise SystemExit(main())
