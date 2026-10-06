#!/usr/bin/env python3
"""Hostile mutations for K1178."""
from copy import deepcopy
from k1178_native_response_ceiling_ledger import build, validate


def main():
    mutations = [
        ("inputs", []), ("baseline_deficits", {}), ("candidates", []),
        ("candidates.0.ceiling", 651), ("candidates.1.transport", "owned"),
        ("candidates.2.complement", 1470), ("candidates.0.null", 0),
        ("strongest_single_ceiling", 4606), ("strongest_single_residual", {}),
        ("decision", "candidate passes"), ("ownership_firewall", "dimension proves coupling"),
        ("protected_disposition", "SC-ACT-06 rejected"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build())
        if key == "candidates.0.ceiling": d["candidates"][0]["optimistic_independent_rank_ceiling"] = value
        elif key == "candidates.1.transport": d["candidates"][1]["k132_transport"] = value
        elif key == "candidates.2.complement": d["candidates"][2]["k132_kernel_complement_rank"] = value
        elif key == "candidates.0.null": d["candidates"][0]["residual_if_full_independent_transport"]["null"] = value
        else: d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1178 hostile probes: 12/12")


if __name__ == "__main__": main()
