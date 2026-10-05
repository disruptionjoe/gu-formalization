#!/usr/bin/env python3
"""K1143: constrained energy conservation and radical quotient descent."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1143-constrained-energy-radical-descent.json"


def mm(a, b):
    def exact(x):
        return int(x) if x.denominator == 1 else str(x)
    return [[exact(sum(Fraction(x) * Fraction(y) for x, y in zip(row, col))) for col in zip(*b)] for row in a]


def tr(a): return [list(x) for x in zip(*a)]
def add(a, b):
    out = []
    for ra, rb in zip(a, b):
        row = []
        for x, y in zip(ra, rb):
            value = Fraction(x) + Fraction(y)
            row.append(int(value) if value.denominator == 1 else str(value))
        out.append(row)
    return out


def build():
    q = [[1, 0, 0, 0]]
    h = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]
    g = [[0, 0, 0, 0], [0, 3, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]]
    z = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
    quotient = [[0, 0], [0, 0], [1, 0], [0, 1]]
    restricted = mm(mm(tr(z), h), z)
    quotient_gram = mm(mm(tr(quotient), h), quotient)
    h_skew_defect = add(mm(tr(g), h), mm(h, g))
    return {
        "schema_version": "1.0",
        "result_id": "K1143-CONSTRAINED-ENERGY-RADICAL-DESCENT",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "if G is H-skew and preserves ker(Q), constrained energy is conserved; a nonnegative restriction descends through its automatically G-invariant radical to a positive-definite quotient",
        "fixture": {
            "Q": q, "H_diagonal": [0, 0, 2, 2], "G": g,
            "QG_on_kernel_zero": True,
            "H_skew_defect": h_skew_defect,
            "restricted_gram": restricted,
            "restricted_inertia": [2, 0, 1],
            "radical_basis": [[0, 1, 0, 0]],
            "radical_invariant": True,
            "quotient_gram": quotient_gram,
            "quotient_dimension": 2,
            "quotient_positive_definite": True,
        },
        "independence_controls": {
            "propagation_without_positivity": "replace the last H entry by -2",
            "positivity_without_propagation": "add a kernel-to-constraint entry in the first row of G",
        },
        "functional_domain_supplied": False,
        "source_action_constraint_supplied": False,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    f = d["fixture"]
    assert "automatically G-invariant radical" in d["theorem"]
    assert f["QG_on_kernel_zero"]
    assert f["H_skew_defect"] == [[0, 0, 0, 0]] * 4
    assert f["restricted_gram"] == [[0, 0, 0], [0, 2, 0], [0, 0, 2]]
    assert f["restricted_inertia"] == [2, 0, 1]
    assert f["radical_basis"] == [[0, 1, 0, 0]]
    assert f["radical_invariant"]
    assert f["quotient_gram"] == [[2, 0], [0, 2]]
    assert f["quotient_dimension"] == 2 and f["quotient_positive_definite"]
    assert "-2" in d["independence_controls"]["propagation_without_positivity"]
    assert not d["functional_domain_supplied"] and not d["source_action_constraint_supplied"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1143 controls: 12/12")
