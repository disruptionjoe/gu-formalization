#!/usr/bin/env python3
"""Hostile mutations for K842."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

PATH = Path(__file__).with_name("k842_sc_act_06_infinite_dimensional_admission_compiler.py")
SPEC = importlib.util.spec_from_file_location("k842", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def main() -> int:
    mutations = [
        ("base-count", lambda p: p["compiler"].__setitem__("k838_row_count", 26)),
        ("new-count", lambda p: p["compiler"].__setitem__("new_row_count", 2)),
        ("total-count", lambda p: p["compiler"].__setitem__("total_row_count", 29)),
        ("cutoff-admissible", lambda p: p["compiler"].__setitem__("finite_cutoff_exactness_alone_admissible", True)),
        ("no-splitting", lambda p: p["compiler"].__setitem__("actual_completed_space_and_controlled_splitting_required", False)),
        ("no-uniform-control", lambda p: p["compiler"].__setitem__("cutoff_uniform_nonlinear_control_required", False)),
        ("complete-rejected", lambda p: p["exact_controls"].__setitem__("infinite_dimensional_complete_admitted", False)),
        ("cutoff-passes", lambda p: p["exact_controls"].__setitem__("finite_cutoff_only_admitted", True)),
        ("missing-count", lambda p: p["exact_controls"].__setitem__("current_gu_missing_row_count", 27)),
        ("gu-passes", lambda p: p["exact_controls"].__setitem__("current_gu_admitted", True)),
        ("topology-supplied", lambda p: p["decision"].__setitem__("actual_gu_function_space_topology_declared", True)),
        ("splitting-supplied", lambda p: p["decision"].__setitem__("actual_gu_bounded_or_tame_splitting_constructed", True)),
        ("neighborhood-supplied", lambda p: p["decision"].__setitem__("actual_gu_uniform_nonlinear_neighborhood_constructed", True)),
        ("global", lambda p: p["decision"].__setitem__("global_sc_act_06_proved_or_refuted", True)),
    ]
    for name, mutate in mutations:
        payload = copy.deepcopy(MODULE.build())
        mutate(payload)
        try:
            MODULE.validate(payload)
        except AssertionError:
            continue
        raise AssertionError(name)
    print("K842 hostile mutations rejected: 14/14")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
