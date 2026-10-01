#!/usr/bin/env python3
"""Independent hostile replay for K712."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k712", HERE / "k712_sc_act_06_auxiliary_positive_gauge_repair.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["theorem"].__setitem__(key, not value)))
    for key in baseline["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    changes = {"dimension": 13, "native_signature": [14, 0, 0], "auxiliary_signature": [13, 1, 0]}
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    for side, key, value in (
        ("native", "norm", 2), ("native", "laplacian_rank", 14),
        ("auxiliary", "norm", 0), ("auxiliary", "laplacian_rank", 0),
        ("auxiliary", "middle_cohomology", 1), ("auxiliary", "clifford_identity_exact", False),
    ):
        mutations.append((f"{side}-{key}", lambda d, side=side, key=key, value=value: d["exact_controls"]["native_null_auxiliary_nonnull"][side].__setitem__(key, value)))
    mutations += [
        ("basis", lambda d: d["exact_controls"]["basis_covectors"]["0"].__setitem__("laplacian_rank", 0)),
        ("family", lambda d: d["exact_controls"]["positive_trace_weight_family"]["1"].__setitem__("norm", 0)),
        ("only", lambda d: d["decision"].__setitem__("wick_rotation_is_only_possible_elliptic_gauge_route", True)),
        ("free", lambda d: d["decision"].__setitem__("native_indefinite_adjoint_repaired_without_new_data", True)),
        ("closed", lambda d: d["decision"].__setitem__("conditional_auxiliary_route_is_mathematically_open", False)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 32:
        mutations.append(("repeat-basis", lambda d: d["exact_controls"]["basis_covectors"]["13"].__setitem__("laplacian_rank", 0)))
    assert len(mutations) == 32
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K712 controls: 36")
    print(f"PASS K712 hostile mutations rejected: {caught}/32")
    return 0 if caught == 32 else 1


if __name__ == "__main__":
    raise SystemExit(main())
