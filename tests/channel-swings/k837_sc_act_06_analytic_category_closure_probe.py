#!/usr/bin/env python3
"""Hostile mutations for K837."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
P=Path(__file__).with_name("k837_sc_act_06_analytic_category_closure.py");S=importlib.util.spec_from_file_location("k837",P);M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
  muts=[
    ("identity",lambda x:x["analytic_identity_theorem"].__setitem__("all_taylor_coefficients_zero_implies_local_zero_germ",False)),
    ("convergence",lambda x:x["analytic_identity_theorem"].__setitem__("convergent_taylor_series_determines_local_germ",False)),
    ("finite",lambda x:x["analytic_identity_theorem"].__setitem__("finite_jet_order_suffices_without_degree_bound",True)),
    ("orders",lambda x:x["analytic_identity_theorem"]["polynomial_controls"][0].__setitem__("zero_derivative_orders",[])),
    ("first",lambda x:x["analytic_identity_theorem"]["polynomial_controls"][1].__setitem__("first_nonzero_order",2)),
    ("coeff",lambda x:x["analytic_identity_theorem"]["polynomial_controls"][2].__setitem__("first_nonzero_coefficient",1)),
    ("zero germ",lambda x:x["analytic_identity_theorem"]["polynomial_controls"][0].__setitem__("zero_germ",True)),
    ("flat",lambda x:x["category_boundary"].__setitem__("analytic_identity_excludes_smooth_flat_behavior",False)),
    ("category",lambda x:x["category_boundary"].__setitem__("regularity_category_must_be_declared",False)),
    ("formal",lambda x:x["category_boundary"].__setitem__("formal_series_requires_convergence_or_actual_map",False)),
    ("GU category",lambda x:x["decision"].__setitem__("actual_gu_regular_category_declared",True)),
    ("GU germ",lambda x:x["decision"].__setitem__("actual_gu_nonlinear_germ_constructed",True)),
  ]
  for n,m in muts:
    p=copy.deepcopy(M.build());m(p)
    try:M.validate(p)
    except AssertionError:continue
    raise AssertionError(n)
  print("K837 hostile mutations rejected: 12/12");return 0
if __name__=="__main__":raise SystemExit(main())
