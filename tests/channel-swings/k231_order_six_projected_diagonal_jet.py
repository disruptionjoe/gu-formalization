#!/usr/bin/env python3
"""K231: S6-projected K185 core has no jet below degree four on its diagonal."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json

from k225_order_six_diagonal_cancellation import K185, OUT as K225, ROOT, grouping, terms
from k230_order_six_permutation_projection import OUT as K230

OUT = ROOT / "lab/process/k231-order-six-projected-diagonal-jet.json"


def coefficient(weights, masks, fixed, chosen, degree=4):
    """Exact truncated product of 1/(a_i+h*n_i) at one diagonal point."""
    series = [Q(1)] + [Q() for _ in range(degree)]
    for i in range(14):
        a = 256 + sum(fixed[j] for j in range(8) if masks[j] & (1 << i))
        n = sum(bool(masks[j] & (1 << i)) for j in chosen)
        reciprocal = [Q((-n)**k, a**(k+1)) for k in range(degree + 1)]
        series = [sum((series[k-m]*reciprocal[m] for m in range(k+1)), Q())
                  for k in range(degree + 1)]
    return [weights*s for s in series]


def orbit_jet(items, fixed, size):
    # Each subset of a fixed cardinality occurs equally often under S6.
    subsets = list(combinations(range(2, 8), size))
    total = [Q() for _ in range(5)]
    for weight, masks in items:
        for subset in subsets:
            for k, term in enumerate(coefficient(weight, masks, fixed, subset)):
                total[k] += term
    return [term / len(subsets) for term in total]


def generate():
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864
    assert all(grouping(items, free)[1] == 0 for free in
               ((0, 1), *((0, 1, j) for j in range(2, 8))))
    prior = json.loads(K230.read_text())
    assert prior["retained_orbits"] == 307
    fixed = (Q(5, 4), Q(17, 8)) + (Q(1),)*6
    jets = {str(size): orbit_jet(items, fixed, size) for size in (1, 2, 3)}
    assert all(all(v == 0 for v in values[:4]) for values in jets.values())
    # A nonzero fourth coefficient is a local control, not a uniform bound.
    assert jets["1"][4] == 0 and jets["2"][4] != 0
    assert jets["3"][4] == Q(3, 2)*jets["2"][4]
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"k185": sha256(K185.read_bytes()).hexdigest(),
                         "k225": sha256(K225.read_bytes()).hexdigest(),
                         "k230": sha256(K230.read_bytes()).hexdigest()},
        "object": "S6-projected original signed K185/K218 rational-cosh core Hbar, with c0,c1 fixed",
        "theorem": "For arbitrary positive u,v,b and all multi-indices of total degree at most three in c2..c7, every derivative of Hbar at (u,v,b,b,b,b,b,b) is zero. K225 gives Hbar=0 on the common diagonal and each one-exception slice, so all pure derivatives vanish. Symmetry makes the mixed second derivatives equal; differentiating the diagonal zero twice makes them zero. Differentiating the pure second derivative along the common diagonal kills each repeated-index third derivative; differentiating the mixed second along that diagonal then kills each all-distinct third derivative. The rational denominators are positive there, so the local Taylor expansion exists.",
        "quartic_normal_form": "With x_j=c_j-b for j=2..7 and symmetric monomial sums m22=sum_(j<k)x_j^2*x_k^2, m211=sum_j sum_(k<l; k,l!=j)x_j^2*x_k*x_l, m1111=sum_(j<k<l<m)x_j*x_k*x_l*x_m, the homogeneous degree-four term is A(u,v,b)*(m22-m211/2+m1111). Pure fourth and (3,1) coefficients vanish on every one-exception slice and its common-diagonal derivatives. Differentiating the identically zero pure second jet twice along the common diagonal gives A=-2B for the m22 and m211 coefficients; vanishing on the full diagonal gives the m1111 coefficient A. This one-dimensional normal form is not a uniform sign or bound on Hbar.",
        "exact_jet_point": [str(x) for x in fixed],
        "orbit_direction_controls": {
            key: {"subset_size": int(key), "subsets": [6, 15, 20][int(key)-1],
                  "degrees_zero_through_three": [str(v) for v in vals[:4]],
                  "degree_four_sign": (vals[4] > 0)-(vals[4] < 0),
                  "degree_four_sha256": sha256(str(vals[4]).encode()).hexdigest(),
                  "degree_four_decimal": f"{float(vals[4]):.12e}"}
            for key, vals in jets.items()},
        "projection_control": {"prior_witness_projected_sha256":
                               prior["rational_witness"]["projected_sha256"]},
        "claim_ceiling": "Exact vanishing through cubic order on the six-coordinate common-cosh diagonal and finite nonzero fourth-order rational control for the S6-projected core only. No uniform fourth derivative, cell bound, integrated third shell, K215 finite prefix, coalescent/quotient/reference composition, source/physics/ledger/canon change."
    }


if __name__ == "__main__":
    result = generate()
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K231 projected diagonal jets through degree three vanish")
    print({key: value["degree_four_decimal"] for key, value in
           result["orbit_direction_controls"].items()})
