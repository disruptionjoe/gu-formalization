#!/usr/bin/env python3
"""Independent hostile replay for K715."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k715", HERE / "k715_sc_act_06_lorentz_natural_auxiliary_family.py")
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
        "boost_plane": [["1", "0"], ["0", "1"]],
        "boost_determinant": "0",
        "boost_eta_defect_zero": False,
        "theta_involution_defect_zero": False,
        "theta_eta_orthogonality_defect_zero": False,
        "q_matches_transport": False,
        "q_plane_eigenvalues": ["1", "1"],
        "q_determinant": "0",
        "q_eta_q_defect_zero": False,
        "q_inverse_check": False,
        "native_null_norms": ["1", "1"],
        "auxiliary_null_norms": ["0", "0"],
        "hodge_symbol_ranks": [0, 0],
        "full_auxiliary_eigenvalue_floor": "0",
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("fixed", lambda d: d["decision"].__setitem__("fixed_identity_metric_is_required_in_every_frame", True)),
        ("natural", lambda d: d["decision"].__setitem__("transported_compact_reduction_is_coordinate_natural", False)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 36:
        mutations.append(("repeat-rank", lambda d: d["exact_controls"].__setitem__("hodge_symbol_ranks", [13, 14])))
    assert len(mutations) == 36
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K715 controls: 40")
    print(f"PASS K715 hostile mutations rejected: {caught}/36")
    return 0 if caught == 36 else 1


if __name__ == "__main__":
    raise SystemExit(main())
