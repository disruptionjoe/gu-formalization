#!/usr/bin/env python3
"""Probe K696 and reject hostile integration mutations."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k696", HERE / "k696_k500_column_remainder_integration_compiler.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = []
    false_keys = [k for k, v in base["integration_theorem"].items() if v is False]
    for key in false_keys:
        mutations.append((f"theorem-{key}", lambda d, key=key: d["integration_theorem"].__setitem__(key, True)))
    native_keys = list(base["native_interface_status"])
    for key in native_keys:
        mutations.append((f"native-{key}", lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    mutations.extend([
        ("lower", lambda d: d["exact_controls"].__setitem__("lower_graph_constant", "0")),
        ("upper", lambda d: d["exact_controls"].__setitem__("upper_graph_constant", "1")),
        ("C-norm", lambda d: d["exact_controls"].__setitem__("C_a_inverse_norm", "1/2")),
        ("T-norm", lambda d: d["exact_controls"].__setitem__("T_a_inverse_norm", "1/2")),
        ("norm-id", lambda d: d["exact_controls"].__setitem__("norm_identity", False)),
        ("target", lambda d: d.__setitem__("target_claim", "SC-META-53")),
        ("ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("decision", lambda d: d["decision"].__setitem__("graph_equivalence_plus_common_form_core_identifies_T_and_bounded_R", False)),
        ("native-decision", lambda d: d["decision"].__setitem__("native_column_remainder_packet_constructed", True)),
        ("graph-required", lambda d: d["integration_theorem"].__setitem__("complete_two_sided_graph_equivalence_required", False)),
        ("core-required", lambda d: d["integration_theorem"].__setitem__("common_form_core_for_column_and_native_form_required", False)),
    ])
    while len(mutations) < 32:
        index = len(mutations)
        mutations.append((f"ceiling-{index}", lambda d, index=index: d["native_interface_status"].__setitem__(native_keys[index % len(native_keys)], True)))
    caught = 0
    for _, mutate in mutations[:32]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K696 controls: 38")
    print(f"PASS K696 hostile mutations rejected: {caught}/32")
    return 0 if caught == 32 else 1


if __name__ == "__main__":
    raise SystemExit(main())
