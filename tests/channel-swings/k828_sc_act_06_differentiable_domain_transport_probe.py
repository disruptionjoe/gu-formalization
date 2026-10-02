#!/usr/bin/env python3
"""Hostile mutations for K828."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
P=Path(__file__).with_name("k828_sc_act_06_differentiable_domain_transport.py")
S=importlib.util.spec_from_file_location("k828",P); M=importlib.util.module_from_spec(S); S.loader.exec_module(M)
def main() -> int:
    mutations=[
        ("bijection suffices",lambda x:x["domain_transport_theorem"].__setitem__("domain_bijection_alone_defines_derivative",True)),
        ("drop row",lambda x:x["domain_transport_theorem"].__setitem__("required_rows",x["domain_transport_theorem"]["required_rows"][:-1])),
        ("bad formula",lambda x:x["domain_transport_theorem"].__setitem__("conjugated_derivative_rule","Jdot")),
        ("jump unbounded",lambda x:x["domain_transport_theorem"].__setitem__("jump_transport_has_uniform_bounds",False)),
        ("jump differentiable",lambda x:x["domain_transport_theorem"].__setitem__("jump_transport_is_differentiable",True)),
        ("jump credited",lambda x:x["domain_transport_theorem"].__setitem__("jump_transport_credits_delta",True)),
        ("bad commutator",lambda x:x["exact_controls"].__setitem__("commutator_K_A0",[[0,1],[1,0]])),
        ("rotation nondifferentiable",lambda x:x["exact_controls"].__setitem__("rotation_transport_is_differentiable",False)),
        ("chain mismatch",lambda x:x["exact_controls"].__setitem__("conjugated_derivative_matches_commutator",False)),
        ("domain invented",lambda x:x["decision"].__setitem__("actual_gu_domain_transport_constructed",True)),
        ("derivative invented",lambda x:x["decision"].__setitem__("actual_gu_operator_derivative_constructed",True)),
        ("global verdict",lambda x:x["decision"].__setitem__("global_sc_act_06_proved_or_refuted",True)),
    ]
    for name,mut in mutations:
        q=copy.deepcopy(M.build()); mut(q)
        try:M.validate(q)
        except AssertionError:continue
        raise AssertionError(name)
    print("K828 hostile mutations rejected: 12/12"); return 0
if __name__=="__main__": raise SystemExit(main())
