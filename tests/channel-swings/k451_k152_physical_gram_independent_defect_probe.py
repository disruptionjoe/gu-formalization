#!/usr/bin/env python3
"""Independent controls and hostile mutations for K451."""

from __future__ import annotations

import copy
from k451_k152_physical_gram_independent_defect import demo


RADII = [
    "23118267391392752342114377141/146346923226707931087360000000",
    "565919717438264971286768741333/5268489236161485519144960000000",
    "565919717438264971286768741333/5268489236161485519144960000000",
]


def checks(packet: dict) -> list[tuple[str, bool]]:
    rows, d = packet["sectors"], packet["decision"]
    return [
        ("result id", packet["result_id"] == "K451-K152-PHYSICAL-GRAM-INDEPENDENT-DEFECT"),
        ("classification", packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("three sectors", [r["charge"] for r in rows] == [[0, 0], [1, 0], [0, 1]]),
        ("dimensions", [r["dimension"] for r in rows] == [8, 7, 7]),
        ("Gram positive", all(r["physical_Gram_positive_definite"] for r in rows)),
        ("relative operator", all(r["relative_operator"] == "M^-1 D" for r in rows)),
        ("rational", all(r["relative_operator_entries_rational"] for r in rows)),
        ("radii", [r["induced_infinity_radius"] for r in rows] == RADII),
        ("radius rows", [r["radius_row"] for r in rows] == [0, 1, 2]),
        ("bound grammar", all(r["two_sided_form_bound"] == "-beta*M <= D <= beta*M" for r in rows)),
        ("plus", all(r["plus_certificate_positive_definite"] for r in rows)),
        ("minus", all(r["minus_certificate_positive_definite"] for r in rows)),
        ("nonzero", all(r["defect_nonzero"] for r in rows)),
        ("finite bound", d["finite_independent_rebuild_has_physical_Gram_relative_bound"] is True),
        ("flavor", d["q10_q01_radii_equal"] is True),
        ("not cofinal", d["bound_is_cofinal_decay_estimate"] is False),
        ("not restriction", d["bound_applies_to_fixed_limiting_form_restriction"] is False),
        ("no interval", d["native_K152_interval_emitted"] is False),
    ]


def main() -> int:
    baseline = demo(); base = checks(baseline)
    if not all(ok for _, ok in base): raise AssertionError([name for name, ok in base if not ok])
    mutations = [
        ("charge", lambda d: d["sectors"][0].__setitem__("charge", [1, 1])),
        ("dimension", lambda d: d["sectors"][0].__setitem__("dimension", 7)),
        ("Gram", lambda d: d["sectors"][0].__setitem__("physical_Gram_positive_definite", False)),
        ("operator", lambda d: d["sectors"][0].__setitem__("relative_operator", "D")),
        ("rational", lambda d: d["sectors"][0].__setitem__("relative_operator_entries_rational", False)),
        ("radius", lambda d: d["sectors"][0].__setitem__("induced_infinity_radius", "0")),
        ("row", lambda d: d["sectors"][0].__setitem__("radius_row", 7)),
        ("grammar", lambda d: d["sectors"][0].__setitem__("two_sided_form_bound", "D<=beta")),
        ("plus", lambda d: d["sectors"][0].__setitem__("plus_certificate_positive_definite", False)),
        ("minus", lambda d: d["sectors"][0].__setitem__("minus_certificate_positive_definite", False)),
        ("zero", lambda d: d["sectors"][0].__setitem__("defect_nonzero", False)),
        ("finite", lambda d: d["decision"].__setitem__("finite_independent_rebuild_has_physical_Gram_relative_bound", False)),
        ("flavor", lambda d: d["decision"].__setitem__("q10_q01_radii_equal", False)),
        ("cofinal", lambda d: d["decision"].__setitem__("bound_is_cofinal_decay_estimate", True)),
        ("restriction", lambda d: d["decision"].__setitem__("bound_applies_to_fixed_limiting_form_restriction", True)),
        ("interval", lambda d: d["decision"].__setitem__("native_K152_interval_emitted", True)),
        ("id", lambda d: d.__setitem__("result_id", "wrong")),
        ("class", lambda d: d.__setitem__("classification", "physical")),
    ]
    rejected = 0
    for _, mutate in mutations:
        trial = copy.deepcopy(baseline); mutate(trial)
        rejected += not all(ok for _, ok in checks(trial))
    if rejected != len(mutations): raise AssertionError("hostile mutation escaped")
    print(f"K451 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K451 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
