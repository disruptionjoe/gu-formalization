#!/usr/bin/env python3
"""Hostile mutations for K1029."""
from copy import deepcopy
from k1029_k1028_causal_record_sequential_certificate import build, validate


def main():
    mutations = [
        ("certificate", "w_hat>b+q+R/n"),
        ("pathwise_count_form", "iid only"),
        ("memory_scope", "iid devices"),
        ("record_scope", "average record error"),
        ("controls.q_zero", 1),
        ("controls.q_one", 0.76),
        ("controls.epsilon_quarter", 0.95),
        ("example.mixed_local_ceiling", 0.78),
        ("example.certificate_threshold", 0.7),
        ("audit_boundary", "estimates all inputs"),
        ("ownership.locality_audit_constructed", True),
        ("target_claim", "SC-META-53"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[int(part)] if part.isdigit() else node[part]
        key = parts[-1]
        if key.isdigit(): node[int(key)] = value
        else: node[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1029 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
