#!/usr/bin/env python3
"""Independent controls and hostile mutations for K450."""

from __future__ import annotations

import copy
from k450_k152_limiting_form_cofinal_restriction import demo


def checks(packet: dict) -> list[tuple[str, bool]]:
    t, c, b = packet["theorem"], packet["exact_control"], packet["scope_boundary"]
    return [
        ("result id", packet["result_id"] == "K450-K152-LIMITING-FORM-COFINAL-RESTRICTION"),
        ("classification", packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet["direction"] == "observed_to_native"),
        ("physical Gram identity", t["physical_gram_identity"].startswith("M_j=")),
        ("regular form identity", t["regular_form_identity"].startswith("A_j=")),
        ("zero defect", t["generalized_defect"] == "D_j=J_j^* A_(j+1) J_j-A_j=0"),
        ("zero radius", t["physical_Gram_relative_radius"] == "0"),
        ("uniform levels", t["uniform_on_every_level"] is True),
        ("cofinal", t["cofinal_limit_bound"] is True),
        ("no rebuild premise", t["requires_independent_rediscretization"] is False),
        ("non diagonal control", c["non_diagonal_fine_form"] is True),
        ("Gram control", c["gram_isometry"] is True),
        ("form control", c["form_congruence"] is True),
        ("defect control", c["defect_is_zero"] is True),
        ("restriction scope", b["applies_to_exact_restrictions_of_one_fixed_limiting_form"] is True),
        ("rebuild fenced", b["applies_to_independently_rebuilt_cutoff_forms"] is False),
        ("K447 preserved", b["K447_independent_defect_erased"] is False),
        ("K152 fenced", all(b[key] is False for key in ("complete_shifted_form_dual_residual_serialized", "coercivity_serialized", "next_distinct_spectrum_serialized", "native_left_floor_serialized", "native_K152_interval_emitted"))),
    ]


def main() -> int:
    baseline = demo(); base = checks(baseline)
    if not all(ok for _, ok in base): raise AssertionError([name for name, ok in base if not ok])
    mutations = [
        ("radius", lambda d: d["theorem"].__setitem__("physical_Gram_relative_radius", "1")),
        ("cofinal", lambda d: d["theorem"].__setitem__("cofinal_limit_bound", False)),
        ("uniform", lambda d: d["theorem"].__setitem__("uniform_on_every_level", False)),
        ("rebuild premise", lambda d: d["theorem"].__setitem__("requires_independent_rediscretization", True)),
        ("gram identity", lambda d: d["theorem"].__setitem__("physical_gram_identity", "missing")),
        ("form identity", lambda d: d["theorem"].__setitem__("regular_form_identity", "missing")),
        ("defect", lambda d: d["theorem"].__setitem__("generalized_defect", "D!=0")),
        ("gram control", lambda d: d["exact_control"].__setitem__("gram_isometry", False)),
        ("form control", lambda d: d["exact_control"].__setitem__("form_congruence", False)),
        ("zero control", lambda d: d["exact_control"].__setitem__("defect_is_zero", False)),
        ("diagonal shortcut", lambda d: d["exact_control"].__setitem__("non_diagonal_fine_form", False)),
        ("restriction", lambda d: d["scope_boundary"].__setitem__("applies_to_exact_restrictions_of_one_fixed_limiting_form", False)),
        ("rebuild overclaim", lambda d: d["scope_boundary"].__setitem__("applies_to_independently_rebuilt_cutoff_forms", True)),
        ("erase K447", lambda d: d["scope_boundary"].__setitem__("K447_independent_defect_erased", True)),
        ("invent residual", lambda d: d["scope_boundary"].__setitem__("complete_shifted_form_dual_residual_serialized", True)),
        ("invent coercivity", lambda d: d["scope_boundary"].__setitem__("coercivity_serialized", True)),
        ("invent gap", lambda d: d["scope_boundary"].__setitem__("next_distinct_spectrum_serialized", True)),
        ("invent interval", lambda d: d["scope_boundary"].__setitem__("native_K152_interval_emitted", True)),
    ]
    rejected = 0
    for _, mutate in mutations:
        trial = copy.deepcopy(baseline); mutate(trial)
        rejected += not all(ok for _, ok in checks(trial))
    if rejected != len(mutations): raise AssertionError("hostile mutation escaped")
    print(f"K450 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K450 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
