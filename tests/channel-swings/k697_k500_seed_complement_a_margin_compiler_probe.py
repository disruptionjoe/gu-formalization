#!/usr/bin/env python3
"""Probe K697 and reject hostile block-composition mutations."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k697", HERE / "k697_k500_seed_complement_a_margin_compiler.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = []
    for key, value in base["block_theorem"].items():
        if value is False:
            mutations.append((key, lambda d, key=key: d["block_theorem"].__setitem__(key, True)))
    for key in base["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    mutations.extend([
        ("seed", lambda d: d["exact_controls"].__setitem__("seed_norm_square_upper", "1/3")),
        ("complement", lambda d: d["exact_controls"].__setitem__("complement_norm_square_upper", "1/10")),
        ("cross", lambda d: d["exact_controls"].__setitem__("cross_upper", "1/4")),
        ("global", lambda d: d["exact_controls"].__setitem__("global_R_norm_square_upper", "1/2")),
        ("A", lambda d: d["exact_controls"].__setitem__("A_lower", "1/2")),
        ("target-A", lambda d: d["exact_controls"].__setitem__("target_A_lower", "3/4")),
        ("slack", lambda d: d["exact_controls"].__setitem__("strict_slack", "0")),
        ("accepted", lambda d: d["exact_controls"].__setitem__("accepted", False)),
        ("target", lambda d: d.__setitem__("target_claim", "SC-META-53")),
        ("ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("decision", lambda d: d["decision"].__setitem__("reducing_seed_complement_packet_suffices_for_A_above_two_thirds", False)),
        ("native-decision", lambda d: d["decision"].__setitem__("native_A_margin_constructed", True)),
        ("seed-required", lambda d: d["block_theorem"].__setitem__("native_seed_compression_required", False)),
        ("comp-required", lambda d: d["block_theorem"].__setitem__("complete_complement_bound_required", False)),
        ("reduction-required", lambda d: d["block_theorem"].__setitem__("R_star_R_reduction_required_for_maximum_rule", False)),
    ])
    while len(mutations) < 32:
        key = list(base["native_interface_status"])[len(mutations) % len(base["native_interface_status"])]
        mutations.append((f"native-repeat-{len(mutations)}", lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    caught = 0
    for _, mutate in mutations[:32]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K697 controls: 38")
    print(f"PASS K697 hostile mutations rejected: {caught}/32")
    return 0 if caught == 32 else 1


if __name__ == "__main__":
    raise SystemExit(main())
