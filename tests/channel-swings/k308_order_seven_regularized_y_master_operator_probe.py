#!/usr/bin/env python3
"""Independent replay and hostile controls for K308."""

from __future__ import annotations

import copy
import importlib.util
import math
from pathlib import Path


MODULE = Path(__file__).with_name("k308_order_seven_regularized_y_master_operator.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k308_probe_target", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K308 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    rational = payload["regularized_operator"]["exact_rational_control"]
    arb_rows = payload["regularized_operator"]["arb_scale_controls"]
    constants = payload["outward_positive_cell"]["D4_times_bordered_B5_regularized_y_jet_abs_upper"]
    checks = [
        rational["D4_factorization_exact"],
        rational["bordered_B5_factorization_exact"],
        rational["joint_factorization_exact"],
        all(row["D4_difference_contains_zero"] for row in arb_rows),
        all(row["bordered_B5_difference_contains_zero"] for row in arb_rows),
        len(constants) == 3,
        all(float(value) > 0 and math.isfinite(float(value)) for value in constants),
        payload["outward_positive_cell"]["column_replacement_counts"]["second_cross"] == 10,
        payload["terminal_face_adapter"]["detached_unregularized_cofactor_forbidden"],
        payload["decision"]["complete_y_peano_norm_emitted"] is False,
        payload["decision"]["k294_gamma_join_released"] is False,
        payload["release_test"]["pointwise_K290_bank_reused"] is False,
    ]
    if not all(checks):
        raise AssertionError("K308 independent replay failed")

    hostile = []
    mutations = (
        ("d4_orders", lambda d: d["regularized_operator"].__setitem__("D4_row_column_orders", [0, 1, 2, 2])),
        ("b5_orders", lambda d: d["regularized_operator"].__setitem__("bordered_B5_row_column_orders", [0, 1, 2, 3])),
        ("commutation", lambda d: d["regularized_operator"].__setitem__("y_derivative_commutes_with_regularization", False)),
        ("operator", lambda d: d["decision"].__setitem__("outward_regularized_y_master_operator_implemented", False)),
        ("detached", lambda d: d["terminal_face_adapter"].__setitem__("detached_unregularized_cofactor_forbidden", False)),
        ("norm_overclaim", lambda d: d["decision"].__setitem__("complete_y_peano_norm_emitted", True)),
        ("gamma_overclaim", lambda d: d["decision"].__setitem__("k294_gamma_join_released", True)),
    )
    for name, mutate in mutations:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            hostile.append(name)
    if len(hostile) != len(mutations):
        raise AssertionError(f"K308 hostile controls escaped: {hostile}")
    print(f"K308 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
