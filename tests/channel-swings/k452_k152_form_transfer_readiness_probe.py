#!/usr/bin/env python3
"""Independent controls and hostile mutations for K452."""

from __future__ import annotations

import copy
from k452_k152_form_transfer_readiness import demo


def checks(packet: dict) -> list[tuple[str, bool]]:
    r, k, e = packet["route_separation"], packet["K152_readiness"], packet["claim_effect"]
    return [
        ("id", packet["result_id"] == "K452-K152-FORM-TRANSFER-READINESS"),
        ("class", packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("zero conforming", r["conforming_relative_defect"] == "0"),
        ("cofinal complete", r["conforming_cofinal_bound_complete"] is True),
        ("three finite radii", len(r["independent_rebuild_relative_radii"]) == 3 and all(x != "0" for x in r["independent_rebuild_relative_radii"])),
        ("not approximation", r["independent_rebuild_is_cofinal_approximation"] is False),
        ("routes distinct", r["routes_may_be_identified"] is False),
        ("Gram ready", k["same_cofinal_family_physical_Gram_transport"] is True),
        ("form ready", k["same_cofinal_family_limiting_regular_form_transport"] is True),
        ("defect ready", k["cofinal_physical_Gram_relative_form_defect_bound_serialized"] is True),
        ("residual open", k["complete_shifted_form_dual_residual_serialized"] is False),
        ("coercivity open", k["coercivity_serialized"] is False),
        ("gap open", k["next_distinct_spectrum_serialized"] is False),
        ("floor open", k["native_left_floor_serialized"] is False),
        ("interface open", k["native_K152_interface_complete"] is False),
        ("interval open", k["native_K152_interval_emitted"] is False),
        ("next input", "complete shifted limiting-form dual residual" in k["next_exact_input"]),
        ("no claim movement", set(e.values()) == {"none"}),
    ]


def main() -> int:
    baseline = demo(); base = checks(baseline)
    if not all(ok for _, ok in base): raise AssertionError([name for name, ok in base if not ok])
    mutations = [
        ("zero", lambda d: d["route_separation"].__setitem__("conforming_relative_defect", "1")),
        ("cofinal", lambda d: d["route_separation"].__setitem__("conforming_cofinal_bound_complete", False)),
        ("radii", lambda d: d["route_separation"].__setitem__("independent_rebuild_relative_radii", ["0"])),
        ("approx", lambda d: d["route_separation"].__setitem__("independent_rebuild_is_cofinal_approximation", True)),
        ("identify", lambda d: d["route_separation"].__setitem__("routes_may_be_identified", True)),
        ("Gram", lambda d: d["K152_readiness"].__setitem__("same_cofinal_family_physical_Gram_transport", False)),
        ("form", lambda d: d["K152_readiness"].__setitem__("same_cofinal_family_limiting_regular_form_transport", False)),
        ("defect", lambda d: d["K152_readiness"].__setitem__("cofinal_physical_Gram_relative_form_defect_bound_serialized", False)),
        ("residual", lambda d: d["K152_readiness"].__setitem__("complete_shifted_form_dual_residual_serialized", True)),
        ("coercivity", lambda d: d["K152_readiness"].__setitem__("coercivity_serialized", True)),
        ("gap", lambda d: d["K152_readiness"].__setitem__("next_distinct_spectrum_serialized", True)),
        ("floor", lambda d: d["K152_readiness"].__setitem__("native_left_floor_serialized", True)),
        ("interface", lambda d: d["K152_readiness"].__setitem__("native_K152_interface_complete", True)),
        ("interval", lambda d: d["K152_readiness"].__setitem__("native_K152_interval_emitted", True)),
        ("next", lambda d: d["K152_readiness"].__setitem__("next_exact_input", "done")),
        ("claim", lambda d: d["claim_effect"].__setitem__("physics_ledger", "moved")),
        ("id", lambda d: d.__setitem__("result_id", "wrong")),
        ("class", lambda d: d.__setitem__("classification", "physical")),
    ]
    rejected = 0
    for _, mutate in mutations:
        trial = copy.deepcopy(baseline); mutate(trial)
        rejected += not all(ok for _, ok in checks(trial))
    if rejected != len(mutations): raise AssertionError("hostile mutation escaped")
    print(f"K452 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K452 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
