#!/usr/bin/env python3
"""Hostile mutations for K1687."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("expansion", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1687",
        "bounded, symmetric" in claim.get("seed_class", ""),
        "kappa_6/720" in claim.get("hermite_ratio", ""),
        "H_4 H_3^2 phi=216" in claim.get("hermite_integrals", ""),
        "kappa_6^2/120-kappa_4^3/4" in claim.get("fisher_law", ""),
        "t^5 coefficient vanishes" in claim.get("fisher_law", ""),
        "kappa_6^2/(120u^3)" in claim.get("matched_defect", ""),
        "not a uniform optimization" in claim.get("scope_guard", ""),
        decision.get("fifth_order_coefficient_zero") is True,
        decision.get("sixth_order_coefficient_explicit") is True,
        decision.get("finite_t_global_ordering_proved") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1687-symmetric-sixth-order-fisher-law.json").read_text())
    mutations = [
        (("claim_id",), "K1686"),
        (("expansion", "seed_class"), "asymmetric"),
        (("expansion", "hermite_ratio"), "wrong H6"),
        (("expansion", "hermite_integrals"), "wrong integral"),
        (("expansion", "fisher_law"), "nonzero t5"),
        (("expansion", "matched_defect"), "seed independent"),
        (("expansion", "scope_guard"), "uniform global theorem"),
        (("decision", "fifth_order_coefficient_zero"), False),
        (("decision", "sixth_order_coefficient_explicit"), False),
        (("decision", "finite_t_global_ordering_proved"), True),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
