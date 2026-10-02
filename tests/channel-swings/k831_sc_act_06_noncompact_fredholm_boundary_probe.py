#!/usr/bin/env python3
"""Hostile mutations for K831."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

PATH = Path(__file__).with_name("k831_sc_act_06_noncompact_fredholm_boundary.py")
SPEC = importlib.util.spec_from_file_location("k831", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    mutations = [
        ("symbol", lambda x: x["operator_theorem"].__setitem__("principal_symbol_invertible_for_nonzero_covector", False)),
        ("kernel", lambda x: x["operator_theorem"].__setitem__("l2_kernel_dimension", 1)),
        ("input norm", lambda x: x["operator_theorem"].__setitem__("normalized_input_norm_squared", 2)),
        ("bounded below", lambda x: x["operator_theorem"].__setitem__("bounded_below_modulo_kernel", True)),
        ("closed range", lambda x: x["operator_theorem"].__setitem__("range_closed", True)),
        ("fredholm", lambda x: x["operator_theorem"].__setitem__("fredholm", True)),
        ("norm sequence", lambda x: x["exact_controls"].__setitem__("derivative_norm_squared", ["1/2"] * 4)),
        ("decay", lambda x: x["exact_controls"].__setitem__("strict_decay", False)),
        ("circle kernel", lambda x: x["exact_controls"].__setitem__("compact_control_kernel_dimension", 0)),
        ("circle index", lambda x: x["exact_controls"].__setitem__("compact_control_index", 1)),
        ("false implication", lambda x: x["decision"].__setitem__("pointwise_symbol_exactness_implies_global_fredholmness", True)),
        ("GU domain invented", lambda x: x["decision"].__setitem__("actual_gu_fredholm_domain_constructed", True)),
    ]
    for name, mutate in mutations:
        candidate = copy.deepcopy(MODULE.build())
        mutate(candidate)
        try:
            MODULE.validate(candidate)
        except AssertionError:
            continue
        raise AssertionError(name)
    print("K831 hostile mutations rejected: 12/12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
