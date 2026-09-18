#!/usr/bin/env python3
"""K227: exact pair-slice support and a finite mixed-anchor cost pilot."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q

from k225_order_six_diagonal_cancellation import K185, OUT as K225, ROOT, core, grouping, mixed_majorant, terms
from k222_order_six_first_middle_shell_cover import SCALE, cosh, sinh

K224 = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"
K226 = ROOT / "lab/process/k226-order-six-global-anchor-obstruction.json"
OUT = ROOT / "lab/process/k227-order-six-two-exception-support.json"


def anchored_cell_bound(items: list, high: tuple[int, ...], anchor: Q) -> Q:
    """Positive exact upper for one disjoint [1,4]/[4,5] exponential band.

    K225's double telescope permits reversed integrals. At pair (j,k),
    earlier h<j retain their actual values, between/later h remain at b.
    Every reciprocal-load derivative decreases with every coordinate.
    """
    lower_exp = tuple(Q(4) if h in high else Q(1) for h in range(8))
    upper_exp = tuple(Q(5) if h in high else Q(4) for h in range(8))
    lo = tuple(cosh(a) for a in lower_exp)
    hi = tuple(cosh(a) for a in upper_exp)
    volume = Q(1)
    for a, z in zip(lower_exp, upper_exp):
        volume *= sinh(z) - sinh(a)
    total = Q(0)
    for j in range(2, 8):
        for k in range(j + 1, 8):
            base = [lo[0], lo[1]] + [anchor] * 6
            for h in range(2, j):
                base[h] = min(lo[h], anchor)
            base[j] = min(lo[j], anchor)
            base[k] = min(lo[k], anchor)
            dj = max(abs(lo[j] - anchor), abs(hi[j] - anchor))
            dk = max(abs(lo[k] - anchor), abs(hi[k] - anchor))
            total += dj * dk * mixed_majorant(items, tuple(base), j, k)
    return SCALE * volume * total / Q(31, 10)**8


def generate() -> dict:
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864
    pairs = []
    zero = []
    for j in range(2, 8):
        for k in range(j + 1, 8):
            count, residual = grouping(items, (0, 1, j, k))
            point = [Q(5, 4), Q(17, 8)] + [Q(1)] * 6
            point[j], point[k] = Q(5, 4), Q(17, 8)
            witness = core(items, tuple(point))
            assert (residual == 0) == (witness == 0)
            if residual == 0:
                zero.append([j, k])
            pairs.append({"pair": [j, k], "factor_multisets": count,
                          "nonzero_coefficient_groups": residual,
                          "witness_sign": (witness > 0) - (witness < 0),
                          "witness_sha256": hashlib.sha256(str(witness).encode()).hexdigest()})
    assert zero == [[2, 3], [6, 7]]
    headroom = Q(json.loads(K224.read_text())["combined_cube_budget_headroom"])
    bands = []
    for high in ((2, 3), (2, 3, 4, 5), (2, 3, 4, 5, 6, 7)):
        global_upper = anchored_cell_bound(items, high, Q(1))
        reanchored = anchored_cell_bound(items, high, cosh(Q(4)))
        assert reanchored < global_upper
        bands.append({"high_indices": list(high), "anchor_cosh": "17/8",
                      "local_upper_using_pi_gt_31_over_10": str(reanchored),
                      "global_upper_same_cell": str(global_upper),
                      "local_over_k224_headroom": str(reanchored / headroom),
                      "global_over_local": str(global_upper / reanchored)})
    assert Q(bands[0]["local_over_k224_headroom"]) > 1
    assert Q(bands[1]["local_over_k224_headroom"]) < 1
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem.split("-")[0]: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (K185, K225, K224, K226)},
        "object": "Original K185/K218 1,864-term signed rational-cosh core restricted to arbitrary common-b two-exception strata",
        "pair_slice_rule": "For each pair j<k among 2..7, set all other c_2..c_7=b and leave c_0=u,c_1=v,c_j=x,c_k=y. Group the 1,864 signed entries by the unordered multiset of fourteen affine factors 256+n_b*b+n_0*u+n_1*v+n_j*x+n_k*y. Zero coefficients in every group prove an identity for all u,v,b,x,y>=1. A nonzero rational point proves each remaining pair slice is not identically zero.",
        "witness_point": "u=x=5/4, v=y=17/8, b=1",
        "pairs": pairs, "identically_zero_pair_slices": zero,
        "mixed_band_rule": "The K225 double telescope allows reversed integrals about any b>=1. On pair (j,k) earlier coordinates h<j retain y_h, intermediate/later ones equal b. For a rectangular cell the unsigned Hessian decreases coordinatewise, hence evaluate it at c0,c1 lower endpoints, min(cell lower,b) for h<j and j,k, and b elsewhere; multiply by each maximum |c_j-b| and |c_k-b|, the exact product of sinh differences, the K218 scale and pi^-8<(10/31)^8. This is an upper bound, not an integral lower bound.",
        "mixed_bands": bands,
        "claim_ceiling": "Exactly two of fifteen two-exception pair slices vanish coefficientwise and thirteen have nonzero rational witnesses. A finite reanchored positive upper improves three selected third-shell cells; its two-high upper exceeds the allocation, which proves no failure of the signed integral or the method itself. Two-pair sparsity is not a full-core identity, a subtraction from K225's positive bound, a complete shell or K215 certificate, boundary composition, source or physics evidence."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K227 two zero and thirteen nonzero exact pair slices; three mixed anchor pilots")
