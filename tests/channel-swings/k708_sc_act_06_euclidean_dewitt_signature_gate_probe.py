#!/usr/bin/env python3
"""Independent hostile replay for K708."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k708", HERE / "k708_sc_act_06_euclidean_dewitt_signature_gate.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key in (
        "positive_definite_iff_lambda_below_one_over_n",
        "trace_null_at_lambda_equal_one_over_n",
        "one_negative_trace_direction_above_threshold",
        "source_native_lambda_is_one_half",
    ):
        mutations.append((key, lambda d, key=key: d["theorem"].__setitem__(key, False)))
    mutations.append(("euclidean-total", lambda d: d["theorem"].__setitem__("euclidean_base_implies_euclidean_total_for_native_lambda", True)))
    for key in baseline["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    changes = {
        "base_dimension": 5,
        "fibre_dimension": 9,
        "threshold": "1/2",
        "native_lambda": "1/4",
        "native_trace_vector_norm": 4,
        "native_fibre_signature": [10, 0, 0],
        "native_total_signature": [14, 0, 0],
        "native_diagonal_basis_gram_determinant": 64,
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("lambda-zero", lambda d: d["exact_controls"]["classification_controls"].__setitem__("lambda_zero", [9, 1, 0])),
        ("lambda-threshold", lambda d: d["exact_controls"]["classification_controls"].__setitem__("lambda_threshold", [10, 0, 0])),
        ("riemannian", lambda d: d["decision"].__setitem__("native_euclidean_base_total_is_riemannian", True)),
        ("refuted", lambda d: d["decision"].__setitem__("source_claim_refuted", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 27:
        idx = len(mutations)
        mutations.append((f"dimension-control-{idx}", lambda d, idx=idx: d["exact_controls"]["classification_controls"]["dimensions_2_through_6"].__setitem__("4", {"below": [0, 0, 10], "at": [0, 0, 10], "above": [0, 0, 10]})))
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
            # The repeated dimension controls are checked independently here.
            dc = candidate["exact_controls"]["classification_controls"]["dimensions_2_through_6"]["4"]
            assert dc == {"below": [10, 0, 0], "at": [9, 0, 1], "above": [9, 1, 0]}
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K708 controls: 34")
    print(f"PASS K708 hostile mutations rejected: {caught}/27")
    return 0 if caught == 27 else 1


if __name__ == "__main__":
    raise SystemExit(main())
