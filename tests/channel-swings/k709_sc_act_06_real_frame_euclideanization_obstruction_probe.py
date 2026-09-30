#!/usr/bin/env python3
"""Independent hostile replay for K709."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k709", HERE / "k709_sc_act_06_real_frame_euclideanization_obstruction.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["theorem"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["theorem"].__setitem__(key, not value)))
    for key in baseline["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    changes = {
        "source_inertia": [14, 0, 0],
        "target_inertia": [13, 1, 0],
        "real_shear_determinant": 0,
        "real_shear_congruence_determinant": 1,
        "real_shear_inertia": [14, 0, 0],
        "complex_rotation_determinant": "1",
        "complex_bilinear_equals_identity": False,
        "complex_hermitian_equals_source_metric": False,
        "complex_rotation_preserves_standard_real_subspace": True,
        "lambda_half_fibre_inertia": [10, 0, 0],
        "lambda_zero_fibre_inertia": [9, 1, 0],
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("future-transport", lambda d: d["decision"].__setitem__("k706_can_transport_future_euclidean_symbol_after_continuation", False)),
        ("create", lambda d: d["decision"].__setitem__("k706_can_create_the_continuation", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    assert len(mutations) == 27
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K709 controls: 36")
    print(f"PASS K709 hostile mutations rejected: {caught}/27")
    return 0 if caught == 27 else 1


if __name__ == "__main__":
    raise SystemExit(main())
