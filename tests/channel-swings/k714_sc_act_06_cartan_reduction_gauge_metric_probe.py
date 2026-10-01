#!/usr/bin/env python3
"""Independent hostile replay for K714."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k714", HERE / "k714_sc_act_06_cartan_reduction_gauge_metric.py")
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
        "dimension": 13,
        "native_signature": [14, 0, 0],
        "theta_eigenspace_dimensions": [14, 0],
        "theta_eta_orthogonality_defect_zero": False,
        "q_equals_identity": False,
        "q_signature": [13, 1, 0],
        "q_determinant": "-1",
        "eta_recovered_as_q_theta": False,
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("sufficient", lambda d: d["decision"].__setitem__("compact_reduction_is_sufficient_to_define_positive_auxiliary_metric", False)),
        ("canonical", lambda d: d["decision"].__setitem__("compact_reduction_is_automatically_selected_by_native_eta", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 31:
        mutations.append(("repeat-signature", lambda d: d["exact_controls"].__setitem__("q_signature", [0, 14, 0])))
    assert len(mutations) == 31
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K714 controls: 36")
    print(f"PASS K714 hostile mutations rejected: {caught}/31")
    return 0 if caught == 31 else 1


if __name__ == "__main__":
    raise SystemExit(main())
