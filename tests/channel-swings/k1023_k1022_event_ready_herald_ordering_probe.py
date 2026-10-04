#!/usr/bin/env python3
"""Hostile mutations for K1023."""
from copy import deepcopy
from k1023_k1022_event_ready_herald_ordering import build, validate


def main():
    muts = [("safe_order", "herald after settings"), ("safe_consequence", "always uniform"),
            ("post_settings_countermodel.wins_by_pair", [1]*4),
            ("post_settings_countermodel.herald_accepts_by_pair", [1]*4),
            ("post_settings_countermodel.acceptance_rate", 1),
            ("post_settings_countermodel.retained_win_rate", .75),
            ("ordering_boundary", "ordering irrelevant"), ("memory_scope", "iid only"),
            ("unowned_assumptions", []), ("ownership.gu_herald_constructed", True),
            ("ownership.causal_order_proved", True), ("target_claim", "CONFIRMED")]
    caught = 0
    for path, value in muts:
        d=deepcopy(build()); node=d; parts=path.split(".")
        for p in parts[:-1]: node=node[p]
        node[parts[-1]]=value
        try: validate(d)
        except AssertionError: caught += 1
    assert caught == len(muts)
    print(f"K1023 hostile probes: {caught}/{len(muts)}")


if __name__ == "__main__": main()
