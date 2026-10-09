#!/usr/bin/env python3
"""Hostile mutations for K1601."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1601-heterogeneous-gaussian-mixture-fisher-sandwich.json").read_text())


def valid(x):
    q, z = x["heterogeneous_mixture"], x["decision"]
    return all([
        x["claim_id"] == "K1601", "arbitrary positive covariances" in q["law"],
        "T=E S_z+C" in q["moments"], "Fisher convexity" in q["convex_upper"],
        "K1533" in q["moment_lower"], "E S_z^(-1)-T^(-1)" in q["exact_width"],
        "Operator convexity" in q["positivity"], "sandwich width" in q["scope_guard"],
        z["heterogeneous_covariances_allowed"], z["arbitrary_mode_translations_allowed"],
        z["exact_precision_jensen_width"], not z["commutation_required"],
        not z["unrestricted_coefficient_identified"], not z["protected_status_change"],
    ])


def main():
    assert valid(D)
    mutations = [(('claim_id',), 'K1600')]
    mutations += [(('heterogeneous_mixture', k), 'changed') for k in ('law', 'moments', 'convex_upper', 'moment_lower', 'exact_width', 'positivity', 'scope_guard')]
    mutations += [(('decision', k), False) for k in ('heterogeneous_covariances_allowed', 'arbitrary_mode_translations_allowed', 'exact_precision_jensen_width')]
    mutations += [(('decision', k), True) for k in ('commutation_required', 'unrestricted_coefficient_identified', 'protected_status_change')]
    for i, (path, value) in enumerate(mutations, 1):
        x, cur = copy.deepcopy(D), None
        cur = x
        for key in path[:-1]: cur = cur[key]
        cur[path[-1]] = value
        assert not valid(x), path
        print(f"PASS {i:02d}: rejected {'/'.join(path)}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
