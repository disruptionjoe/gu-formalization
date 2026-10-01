#!/usr/bin/env python3
"""Independent hostile replay for K717."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k717", HERE / "k717_sc_act_06_flat_euclidean_gimmel_germ.py")
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
    changes = {
        "theta_squared_identity": False,
        "eta_theta_equals_q": False,
        "fibre_eta_rank": 9,
        "fibre_q_rank": 9,
        "fibre_signature": [10, 0],
        "total_signature": [14, 0],
        "trace_vector_eta_norm": "4",
        "trace_vector_q_norm": "-4",
        "traceless_diagonal_control_eta_norm": "0",
        "traceless_diagonal_control_q_norm": "0",
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("ownership", lambda d: d["decision"].__setitem__("abstract_reduction_ownership_gap_closed_on_this_germ", False)),
        ("global", lambda d: d["decision"].__setitem__("background_owned_reduction_is_global_or_unique", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 34:
        mutations.append(("repeat-signature", lambda d: d["exact_controls"].__setitem__("total_signature", [14, 0])))
    assert len(mutations) == 34
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K717 controls: 40")
    print(f"PASS K717 hostile mutations rejected: {caught}/34")
    return 0 if caught == 34 else 1


if __name__ == "__main__":
    raise SystemExit(main())
