#!/usr/bin/env python3
"""K228: exact anchored third mixed differences of the original K185 core."""
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as Q

from k225_order_six_diagonal_cancellation import K185, ROOT, core, grouping, terms

K227 = ROOT / "lab/process/k227-order-six-two-exception-support.json"
OUT = ROOT / "lab/process/k228-order-six-third-interaction-support.json"
TRIPLE_VALUES = (Q(5, 4), Q(17, 8), Q(3, 2))


def anchored_difference(rows: list, triple: tuple[int, ...], values=TRIPLE_VALUES) -> Q:
    """Boolean third difference, with u=5/4, v=17/8, b=1."""
    answer = Q(0)
    for active in range(8):
        c = [Q(5, 4), Q(17, 8)] + [Q(1)] * 6
        for offset, coordinate in enumerate(triple):
            if active & (1 << offset):
                c[coordinate] = values[offset]
        answer += (-1 if (3 - active.bit_count()) % 2 else 1) * core(rows, tuple(c))
    return answer


def generate() -> dict:
    rows = list(terms(json.loads(K185.read_text())))
    assert len(rows) == 1864
    pairs = json.loads(K227.read_text())
    assert pairs["identically_zero_pair_slices"] == [[2, 3], [6, 7]]
    results = []
    for triple in itertools.combinations(range(2, 8), 3):
        n_groups, n_nonzero = grouping(rows, (0, 1) + triple)
        value = anchored_difference(rows, triple)
        assert n_nonzero and value
        results.append({
            "triple": list(triple),
            "factor_multisets": n_groups,
            "nonzero_coefficient_groups": n_nonzero,
            "third_difference_sign": (value > 0) - (value < 0),
            "third_difference_sha256": hashlib.sha256(str(value).encode()).hexdigest(),
        })
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            "k185": hashlib.sha256(K185.read_bytes()).hexdigest(),
            "k227": hashlib.sha256(K227.read_bytes()).hexdigest(),
        },
        "object": "Original signed K185/K218 1,864-term rational-cosh core H, before positive outer factors",
        "anchor": {"u": "5/4", "v": "17/8", "b": "1", "successive_exception_values": ["5/4", "17/8", "3/2"]},
        "difference_rule": "For S={j,k,l}, Delta_S H=sum_{A subset S}(-1)^(3-|A|) H(u,v,c_2..c_7), with c_i equal to the listed successive exception value when i is in A and equal to b otherwise. All arithmetic is exact rational. A nonzero value is a witness that the pure anchored third interaction is not identically zero; it does not prove a sign elsewhere.",
        "triples": results,
        "decomposition": "For any b and fixed u,v, let D_S H=sum_{A subset S}(-1)^(|S|-|A|) H(c_i=y_i for i in A, c_i=b otherwise). Boolean inversion gives H(u,v,y)=sum_{S subset {2,...,7}}D_S H. K225 kills |S|<=1 and K227 kills the |S|=2 terms S={2,3},{6,7}. The other thirteen pair terms and all |S|>=3 terms remain in the exact identity. Each of the twenty pure |S|=3 terms has an exact nonzero witness at the listed point; hence no universal representation of H as a sum of functions of at most two of y_2..y_7 can hold for every u,v,y at this anchor.",
        "claim_ceiling": "All twenty anchored pure triple interactions are nonzero at one exact rational witness, including triples containing K227 zero pairs. This excludes an exact pair-only pointwise representation on the declared original core but does not lower-bound an integrated signed error, establish nonzero weighted integral, control the third shell or K215, compose coalescent/quotient/reference bounds, or move source, physics, ledger or canon status."
    }


if __name__ == "__main__":
    result = generate()
    assert result == json.loads(OUT.read_text())
    print("[PASS] K228 twenty exact nonzero pure triple interactions and anchored inversion")
