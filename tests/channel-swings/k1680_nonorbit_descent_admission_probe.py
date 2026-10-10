#!/usr/bin/env python3
"""Hostile mutations for K1680."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("admission", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1680", "c_g N^4 below" in c.get("quantum_result", ""),
        "matching unrestricted lower bound" in c.get("remaining_quantum_gate", ""),
        "K1145/K1150 remain 0/7" in c.get("physical_admission", ""), "395 rows" in c.get("bridge_census", ""),
        "Do not promote" in c.get("scope_guard", ""),
        d.get("profiled_gaussian_unrestricted_leading_minimality_closed_false") is True,
        d.get("true_unrestricted_coefficient_open") is True, d.get("source_status_changed") is False,
        d.get("physics_ledger_changed") is False, d.get("canon_or_public_status_changed") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1680-nonorbit-descent-admission.json").read_text())
    mutations = [
        (("claim_id",), "K1679"), (("admission", "quantum_result"), "no descent"),
        (("admission", "remaining_quantum_gate"), "closed"),
        (("admission", "physical_admission"), "admitted"), (("admission", "bridge_census"), "all satisfied"),
        (("admission", "scope_guard"), "promote"),
        (("decision", "profiled_gaussian_unrestricted_leading_minimality_closed_false"), False),
        (("decision", "true_unrestricted_coefficient_open"), False),
        (("decision", "source_status_changed"), True), (("decision", "physics_ledger_changed"), True),
        (("decision", "canon_or_public_status_changed"), True),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source); cursor = changed
        for key in path[:-1]: cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
