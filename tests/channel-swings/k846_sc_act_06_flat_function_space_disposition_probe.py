#!/usr/bin/env python3
"""Hostile semantic mutations for K846."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("k846_sc_act_06_flat_function_space_disposition.py")
spec = importlib.util.spec_from_file_location("k846", SCRIPT)
assert spec and spec.loader
k846 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k846)


def main() -> int:
    base = k846.build()
    mutations = [
        ("classification", "CONVENTIONAL_COMPARATOR"), ("target_claim", "NONE-NOT-A-KILL"),
        ("gu_typed_objects.action_owner", "repository-construction"),
        ("composition.current_flat_middle_symbol_exact", True),
        ("composition.uniform_middle_symbol_cohomology_lower_bound", 0),
        ("composition.local_elliptic_quotient_estimate", True),
        ("composition.bounded_one_derivative_splitting_on_current_quotient", True),
        ("composition.lower_order_or_same_linearization_repair_available", True),
        ("composition.complete_global_function_space_realization_supplied", True),
        ("composition.all_K842_admission_rows_pass", True),
        ("decision.K717_current_serialized_packet_is_direct_elliptic_realization", True),
        ("decision.K717_background_itself_globally_refuted", True),
        ("decision.every_Upsilon_zero_background_rejected", True),
        ("decision.SC_ACT_06_source_claim_proved_or_refuted", True),
        ("decision.source_register_or_ledger_moves", True),
        ("decision.reopeners.0", "none"), ("decision.reopeners.1", "none"),
        ("decision.reopeners.2", "none"), ("decision.reopeners.3", "none"),
        ("decision.next_exact_input", "Retry lower order."),
        ("source_and_ledger_effect", "SC-ACT-06_REFUTED"), ("claim_ceiling", "Global no-go."),
    ]
    rejected = 0
    for path, value in mutations:
        packet = copy.deepcopy(base)
        cursor = packet
        parts = path.split(".")
        for key in parts[:-1]:
            cursor = cursor[int(key)] if key.isdigit() else cursor[key]
        key = parts[-1]
        if key.isdigit():
            cursor[int(key)] = value
        else:
            cursor[key] = value
        try:
            k846.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K846 probe: rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
