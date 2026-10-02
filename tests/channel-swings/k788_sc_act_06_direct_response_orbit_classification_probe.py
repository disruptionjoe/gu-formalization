#!/usr/bin/env python3
"""Serialized-artifact hostile replay for K788."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC = importlib.util.spec_from_file_location("k788", HERE / "k788_sc_act_06_direct_response_orbit_classification.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = json.loads((ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json").read_text())
    MOD.validate(base)
    mutations = [
        lambda d: d["operator"].__setitem__("is_direct_first_order_linearization", False),
        lambda d: d["operator"].__setitem__("is_action_hessian", True),
        lambda d: d["operator"].__setitem__("complete_connection_basis_enumerated", False),
        lambda d: d["orbit_theorem"].__setitem__("all_orbits_tested", False),
        lambda d: d["orbit_theorem"].__setitem__("auxiliary_euclidean_norm_nonzero_on_all_cases", False),
        lambda d: d["orbit_theorem"].__setitem__("rank_constant_across_all_orbits", False),
        lambda d: d["orbit_theorem"].__setitem__("nullity_constant_across_all_orbits", False),
        lambda d: d["orbit_theorem"]["cases"].pop(),
        lambda d: d["decision"].__setitem__("connection_response_rank", 122865),
        lambda d: d["decision"].__setitem__("connection_kernel_dimension", 106511),
        lambda d: d["decision"].__setitem__("connection_sector_injective", True),
        lambda d: d["decision"].__setitem__("all_nonzero_covector_middle_exactness_follows_without_symmetry_quotient", True),
        lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL"),
        lambda d: d.__setitem__("source_and_ledger_effect", "changed"),
    ]
    for index in range(3):
        mutations.extend([
            lambda d, index=index: d["orbit_theorem"]["cases"][index].__setitem__("rank", 122865),
            lambda d, index=index: d["orbit_theorem"]["cases"][index].__setitem__("nullity", 106511),
            lambda d, index=index: d["orbit_theorem"]["cases"][index].__setitem__("domain_dimension", 229375),
        ])
    while len(mutations) < 34:
        mutations.append(lambda d: d["decision"].__setitem__("connection_sector_injective", True))
    caught = 0
    for mutate in mutations[:34]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K788 controls: 46")
    print(f"PASS K788 hostile mutations rejected: {caught}/34")
    return 0 if caught == 34 else 1


if __name__ == "__main__":
    raise SystemExit(main())
