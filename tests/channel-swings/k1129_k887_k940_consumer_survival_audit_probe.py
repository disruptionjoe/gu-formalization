#!/usr/bin/env python3
"""Hostile mutations for K1129."""
from copy import deepcopy
from k1129_k887_k940_consumer_survival_audit import build, validate


def main():
    mutations = [
        ("audited_range", [895, 898]), ("audited_result_count", 4),
        ("audited_result_ids", []), ("directly_corrected_range", [895, 895]),
        ("dependent_action_gate_range", [899, 940]), ("explicit_auxiliary_range", []),
        ("historical_exact_algebra_preserved", False),
        ("preservation_rule", "all objects transfer"),
        ("withdrawn_current_inference", "all source action claims survive"),
        ("auxiliary_disposition", "physical GU quotient"),
        ("independent_successor", "K887"), ("old_completion_gate_current", True),
        ("source_and_ledger_effect", "PROMOTED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1129 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
