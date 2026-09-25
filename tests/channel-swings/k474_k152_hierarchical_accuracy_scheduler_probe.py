#!/usr/bin/env python3
"""Independent controls and hostile mutations for K474."""

from __future__ import annotations

import copy
from fractions import Fraction

from k473_k152_recursive_complement_floor import CertificateError
from k474_k152_hierarchical_accuracy_scheduler import demo, schedule


def checks(p):
    t, c, n = p["theorem"], p["exact_composed_control"], p["native_release"]
    return [
        p["result_id"] == "K474-K152-HIERARCHICAL-ACCURACY-SCHEDULER",
        p["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        p["direction"] == "observed_to_native",
        len(t["inputs"]) == 3,
        t["two_fail_closed_tests"] == ["mu^2<(alpha-b)(gamma-b)", "eta^2<=d(beta-rho+d)"],
        "conjunction" in t["release"],
        c["recursive_floor"]["complete_complement_floor_outward_interval"] == ["2", "2"],
        c["K469_residual_square_budget_lower"] == "9/4",
        c["complete_M_dual_residual_square_upper"] == "9/4",
        c["budget_pass"] is True,
        Fraction(c["finite_Gram_sqrt_allowance"]) == Fraction(3, 2) - Fraction(3011499, 838860800),
        c["finite_Gram_entries"] == 59586,
        c["native_accuracy_released"] is False,
        n["native_hierarchical_packet_present"] is False,
        n["native_target_deficit_present"] is False,
        n["K457_evaluation_started"] is False,
        n["native_K152_interval_emitted"] is False,
    ]


def main() -> int:
    p = demo(); base = checks(p)
    muts = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("inputs", []),
        lambda d: d["theorem"].__setitem__("two_fail_closed_tests", ["one"]),
        lambda d: d["exact_composed_control"].__setitem__("K469_residual_square_budget_lower", "0"),
        lambda d: d["exact_composed_control"].__setitem__("budget_pass", False),
        lambda d: d["exact_composed_control"].__setitem__("finite_Gram_entries", 0),
        lambda d: d["exact_composed_control"].__setitem__("native_accuracy_released", True),
        lambda d: d["native_release"].__setitem__("K457_evaluation_started", True),
        lambda d: d["native_release"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for m in muts:
        c=copy.deepcopy(p); m(c); rejected += not all(checks(c))
    common = dict(rho=-2,b=1,alpha=3,gamma=6,mu=2,eta_sq=Fraction(9,4),
                  target_deficit=Fraction(1,2),certified_tail=Fraction(1,250),
                  finite_slice_ref="F",complete_tail_ref="T",complement_cross_ref="X",residual_ref="R")
    invalid=0
    for upd in ({"eta_sq":3},{"target_deficit":0},{"certified_tail":2},{"residual_ref":None},{"rho":1}):
        kw=dict(common); kw.update(upd)
        try: schedule(**kw)
        except CertificateError: invalid+=1
    print(f"K474 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K474 HOSTILE MUTATIONS: {rejected}/{len(muts)} rejected")
    print(f"K474 INVALID INPUTS: {invalid}/5 rejected")
    return 0 if all(base) and rejected==len(muts) and invalid==5 else 1


if __name__ == "__main__": raise SystemExit(main())
