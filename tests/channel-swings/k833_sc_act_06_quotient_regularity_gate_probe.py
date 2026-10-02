#!/usr/bin/env python3
"""Hostile mutations for K833."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

PATH = Path(__file__).with_name("k833_sc_act_06_quotient_regularity_gate.py")
SPEC = importlib.util.spec_from_file_location("k833", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    mutations = [
        ("ranks", lambda x: x["nonfree_control"].__setitem__("generator_ranks", [1, 1, 1, 1])),
        ("origin stabilizer", lambda x: x["nonfree_control"].__setitem__("origin_stabilizer", "trivial")),
        ("generic stabilizer", lambda x: x["nonfree_control"].__setitem__("nonzero_stabilizer", "SO(2)")),
        ("constant type", lambda x: x["nonfree_control"].__setitem__("orbit_type_constant", True)),
        ("smooth origin", lambda x: x["nonfree_control"].__setitem__("quotient_is_smooth_manifold_without_boundary_near_origin", True)),
        ("free rank", lambda x: x["free_control"].__setitem__("generator_rank_everywhere", 0)),
        ("free stabilizer", lambda x: x["free_control"].__setitem__("stabilizer_everywhere", "SO(2)")),
        ("proper", lambda x: x["free_control"].__setitem__("action_proper", False)),
        ("free quotient", lambda x: x["free_control"].__setitem__("quotient_is_smooth_one_manifold", False)),
        ("false implication", lambda x: x["quotient_gate"].__setitem__("smooth_zero_set_implies_smooth_gauge_quotient", True)),
        ("GU slice", lambda x: x["decision"].__setitem__("actual_gu_local_slice_constructed", True)),
        ("global verdict", lambda x: x["decision"].__setitem__("global_sc_act_06_proved_or_refuted", True)),
    ]
    for name, mutate in mutations:
        candidate = copy.deepcopy(MODULE.build())
        mutate(candidate)
        try:
            MODULE.validate(candidate)
        except AssertionError:
            continue
        raise AssertionError(name)
    print("K833 hostile mutations rejected: 12/12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
