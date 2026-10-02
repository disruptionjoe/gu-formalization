#!/usr/bin/env python3
"""Hostile mutations for K841's analytic Hilbert zero accumulation witness."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

PRODUCER = Path(__file__).with_name("k841_sc_act_06_analytic_hilbert_zero_accumulation.py")
SPEC = importlib.util.spec_from_file_location("k841", PRODUCER)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def main() -> int:
    mutations = [
        ("result id", lambda p: p.__setitem__("result_id", "K841-MUTATED")),
        ("classification", lambda p: p.__setitem__("classification", "UNCLASSIFIED")),
        ("governance", lambda p: p["governance"].__setitem__("source_claim_effect", "promotion")),
        ("pinned digest", lambda p: p["pinned_input"].__setitem__("sha256", "0" * 64)),
        ("space", lambda p: p["analytic_hilbert_map"].__setitem__("space", "R^N")),
        ("map", lambda p: p["analytic_hilbert_map"].__setitem__("map", "F(x)=x")),
        ("quadratic bound", lambda p: p["analytic_hilbert_map"].__setitem__("quadratic_bound", "unproved")),
        ("quadratic continuity", lambda p: p["analytic_hilbert_map"].__setitem__("coordinate_square_is_continuous_quadratic_l2_to_l2", False)),
        ("analyticity", lambda p: p["analytic_hilbert_map"].__setitem__("real_analytic", False)),
        ("bounded below", lambda p: p["analytic_hilbert_map"].__setitem__("derivative_bounded_below", True)),
        ("action owner", lambda p: p["gu_typed_objects"].__setitem__("action_owner", "GU")),
        ("cutoff rule", lambda p: p["finite_cutoffs"].__setitem__("coordinate_zero_rule", "x_n=0")),
        ("nearest cutoff zero", lambda p: p["finite_cutoffs"].__setitem__("nearest_nonzero_zero", "e_1")),
        ("finite isolation", lambda p: p["finite_cutoffs"].__setitem__("origin_is_isolated_for_every_finite_cutoff", False)),
        ("enumerated zero count", lambda p: p["finite_cutoffs"]["controls"][2].__setitem__("zero_count", 7)),
        ("full l2 membership", lambda p: p["full_space_zero_set"].__setitem__("all_coordinate_choice_sequences_lie_in_l2", False)),
        ("full norm", lambda p: p["full_space_zero_set"].__setitem__("exact_norm", "||z^[N]||_2=1")),
        ("full isolation", lambda p: p["full_space_zero_set"].__setitem__("origin_is_isolated", True)),
        ("flat conflation", lambda p: p["category_and_limit_boundary"].__setitem__("not_a_smooth_flat_example", False)),
        ("GU overclaim", lambda p: p["decision"].__setitem__("actual_gu_hilbert_kuranishi_map_constructed", True)),
    ]
    for name, mutate in mutations:
        payload = copy.deepcopy(MODULE.build())
        mutate(payload)
        try:
            MODULE.validate(payload)
        except AssertionError:
            continue
        raise AssertionError(f"hostile mutation survived: {name}")
    print("K841 hostile mutations rejected: 20/20")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
