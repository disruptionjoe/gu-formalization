#!/usr/bin/env python3
"""Hostile mutations for K832."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

PATH = Path(__file__).with_name("k832_sc_act_06_kuranishi_obstruction_gate.py")
SPEC = importlib.util.spec_from_file_location("k832", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    mutations = [
        ("rank", lambda x: x["obstructed_control"].__setitem__("jacobian_rank", 2)),
        ("kernel", lambda x: x["obstructed_control"].__setitem__("tangent_kernel_basis", [[0, 1]])),
        ("cokernel", lambda x: x["obstructed_control"].__setitem__("cokernel_basis", [[1, 0]])),
        ("quadratic", lambda x: x["obstructed_control"].__setitem__("quadratic_obstruction_on_tangent", [0, 0])),
        ("coefficient", lambda x: x["obstructed_control"].__setitem__("cokernel_obstruction_coefficient", 0)),
        ("lift", lambda x: x["obstructed_control"].__setitem__("second_order_lift_exists", True)),
        ("dimension", lambda x: x["obstructed_control"].__setitem__("actual_local_dimension", 1)),
        ("surjectivity", lambda x: x["unobstructed_control"].__setitem__("jacobian_surjective", False)),
        ("lift residual", lambda x: x["unobstructed_control"].__setitem__("second_order_equation_residual", 1)),
        ("linear decides", lambda x: x["kuranishi_gate"].__setitem__("linearized_kernel_alone_determines_local_moduli_dimension", True)),
        ("rich follows", lambda x: x["decision"].__setitem__("elliptic_linearization_implies_rich_moduli", True)),
        ("GU unobstructed", lambda x: x["decision"].__setitem__("actual_gu_unobstructedness_proved", True)),
    ]
    for name, mutate in mutations:
        candidate = copy.deepcopy(MODULE.build())
        mutate(candidate)
        try:
            MODULE.validate(candidate)
        except AssertionError:
            continue
        raise AssertionError(name)
    print("K832 hostile mutations rejected: 12/12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
