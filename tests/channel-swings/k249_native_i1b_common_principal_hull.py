#!/usr/bin/env python3
"""K249: exact dx0/dx1 I1B hull and the first dx2 carrier obstruction."""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from fractions import Fraction as Q
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
K236 = ROOT / "lab/process/k236-native-i1b-invariant-mixed-grade-symbol.json"
K237 = ROOT / "lab/process/k237-native-i1b-tangential-star-obstruction.json"
OUT = ROOT / "lab/process/k249-native-i1b-common-principal-hull.json"
CHANNELS = ("comm", "symi", "symi")


def calculate():
    with redirect_stdout(StringIO()) as log:
        m = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full, n = m["ONE"], m["ZERO"], m["FULL"], m["N"]

    def direction(mu, blade):
        return {1 << mu: {blade: one}}

    def ordered(left, right, principal):
        image = m["shiab"](
            m["wedge_raw"](direction(principal, 0), right), CHANNELS
        )
        return m["wedge_raw"](left, image).get(full, {}).get(0, zero)

    # A vector is indexed by (label, one-form leg), where
    # Clifford blade = label xor the one-form bit.  The K236/K237 terms all
    # lie in labels 0,1,2,3.  For principal directions 0 and 1 the exact
    # Clifford/form support rule preserves those four labels in both ordered
    # legs, so the full 56-vector block is a genuine two-plane carrier.
    basis = [(label, mu, label ^ (1 << mu)) for label in range(4) for mu in range(n)]
    lookup = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}

    def projected_matrix(principal):
        raw = sp.zeros(len(basis))
        for row, (_, mu_left, blade_left) in enumerate(basis):
            left = direction(mu_left, blade_left)
            for column, (_, mu_right, blade_right) in enumerate(basis):
                value = ordered(left, direction(mu_right, blade_right), principal)
                assert value[1] == 0
                raw[row, column] = sp.Rational(
                    value[0].numerator, value[0].denominator
                )
        euler = (raw - raw.T) / 2
        assert euler.T == -euler
        return raw, euler

    raw0, d0 = projected_matrix(0)
    raw1, d1 = projected_matrix(1)
    assert d0.rank() == d1.rank() == 32

    odd_index = lookup[(3, 0)]
    odd = sp.eye(56)[:, odd_index]
    spoke_indices = tuple(lookup[(2, j)] for j in range(2, 14))
    collective = sum((sp.eye(56)[:, j] for j in spoke_indices), sp.zeros(56, 1))

    # Replay the K236 normal star and K237's named tangential coefficients.
    assert d0 * odd == -collective
    assert d0 * collective == 12 * odd
    assert d1[lookup[(1, 1)], odd_index] == -1
    assert (d1 * collective)[lookup[(0, 0)]] == 12
    assert (d1 * collective)[lookup[(0, 2)]] == 10
    assert (d1 * collective)[lookup[(0, 13)]] == 10

    hull = sp.Matrix.hstack(odd, collective).columnspace()
    growth = [len(hull)]
    while True:
        candidates = hull + [matrix * vector for matrix in (d0, d1) for vector in hull]
        enlarged = sp.Matrix.hstack(*candidates).columnspace()
        growth.append(len(enlarged))
        if len(enlarged) == len(hull):
            break
        hull = enlarged
    hull_matrix = sp.Matrix.hstack(*hull)
    assert growth == [2, 4, 7, 9, 9]
    assert hull_matrix.rank() == 9
    assert all(
        sp.Matrix.hstack(hull_matrix, matrix * hull_matrix).rank() == 9
        for matrix in (d0, d1)
    )

    lam = sp.Symbol("lambda")
    expected_charpoly = lam * (lam**2 + 1) * (lam**2 + 4) * (lam**2 + 12) * (lam**2 + 121)
    restricted = []
    for principal, matrix in ((0, d0), (1, d1)):
        columns = [hull_matrix.gauss_jordan_solve(matrix * vector)[0] for vector in hull]
        action = sp.Matrix.hstack(*columns)
        assert action.rank() == 8
        assert sp.expand(action.charpoly(lam).as_expr()) == sp.expand(expected_charpoly)
        restricted.append({"principal_direction": principal, "rank": 8,
                           "square_factors": [1, 4, 12, 121], "nullity": 1})

    # The next independent principal direction leaves the whole 56-vector
    # carrier.  These two exact ordered contractions are sufficient witnesses;
    # no projected dx2 matrix is silently substituted for the full output.
    odd_out = direction(1, 5)  # label 7: dx1 tensor gamma02
    odd_dir = direction(0, 2)
    odd_forward = ordered(odd_out, odd_dir, 2)
    odd_reverse = ordered(odd_dir, odd_out, 2)
    assert odd_forward == (Q(-2), Q()) and odd_reverse == zero
    odd_euler = (odd_forward[0] - odd_reverse[0]) / 2
    assert odd_euler == -1 and 7 not in range(4)

    spokes = [direction(j, 2 | (1 << j)) for j in range(2, 14)]
    even_out = direction(2, 2)  # label 6: dx2 tensor gamma1
    even_forward = sum((ordered(even_out, spoke, 2)[0] for spoke in spokes), Q())
    even_reverse = sum((ordered(spoke, even_out, 2)[0] for spoke in spokes), Q())
    even_euler = (even_forward - even_reverse) / 2
    assert (even_forward, even_reverse, even_euler) == (Q(-22), Q(), Q(-11))

    return {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__LOCAL_SELECTED_SYMBOL_ONLY",
        "input_sha256": {
            "backend": sha256(BACKEND.read_bytes()).hexdigest(),
            "k236": sha256(K236.read_bytes()).hexdigest(),
            "k237": sha256(K237.read_bytes()).hexdigest(),
        },
        "object": "Selected comm/symi/symi I1B formal Euler principal-symbol plane dx0/dx1 on the flat Ricci-flat T=0 zero-fermion germ",
        "carrier": {
            "basis_rule": "(label,mu,label xor 2^mu) for label in {0,1,2,3}, mu in {0,...,13}",
            "dimension": 56,
            "support_rule": "For principal dx0 and dx1, a nonzero ordered pairing connects labels differing by the corresponding principal bit; labels {0,1,2,3} are therefore closed in both ordered legs.",
            "full_matrix_ranks": {"dx0": int(d0.rank()), "dx1": int(d1.rank())},
        },
        "seed": {
            "odd": "o=dx0 tensor gamma1",
            "collective": "E=sum_(j=2)^13 dxj tensor gamma1 gammaj",
            "normal_actions": ["N0(o)=-E", "N0(E)=12o"],
        },
        "minimal_two_plane_hull": {
            "dimension_growth": growth,
            "dimension": 9,
            "closed_under": ["dx0", "dx1"],
            "minimality": "Successive exact Krylov closure from {o,E} grows 2,4,7,9 and then stabilizes; every retained column is chosen from the preceding hull plus one principal image.",
            "restricted_actions": restricted,
        },
        "dx2_obstruction": {
            "odd_witness": {
                "output": "dx1 tensor gamma02",
                "output_label": 7,
                "ordered_forward_reverse": [str(odd_forward[0]), str(odd_reverse[0])],
                "euler_coefficient": str(odd_euler),
            },
            "collective_witness": {
                "output": "dx2 tensor gamma1",
                "output_label": 6,
                "ordered_forward_reverse": [str(even_forward), str(even_reverse)],
                "euler_coefficient": str(even_euler),
            },
            "theorem": "The natural 56-vector completion containing every K237 escape is not a common carrier for the full principal family: dx2 already maps both K236 generators to nonzero labels outside {0,1,2,3}.",
        },
        "interpretation": "K237's rank-two star has an exact nine-dimensional minimal completion for the dx0/dx1 principal plane. The first independent direction dx2 escapes even the ambient 56-vector two-plane carrier, so the nine-dimensional hull is not a fourteen-direction reduction and a larger ambient construction is required.",
        "claim_ceiling": "Exact selected local dx0/dx1 principal-plane hull and dx2 obstruction only. No all-fourteen-direction minimal hull, source-selected full fermion operator, lower-order invariant domain, quotient, spectrum, positivity, source/physics/ledger/canon/public change, or q17 cancellation result.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = calculate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K249 exact 9D dx0/dx1 hull and dx2 carrier obstruction")
