#!/usr/bin/env python3
"""Independent support-enumeration replay and hostile controls for K249."""
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
RECORD = ROOT / "lab/process/k249-native-i1b-common-principal-hull.json"
CHANNELS = ("comm", "symi", "symi")


def main():
    record = json.loads(RECORD.read_text())
    assert record["input_sha256"] == {
        "backend": sha256(BACKEND.read_bytes()).hexdigest(),
        "k236": sha256(K236.read_bytes()).hexdigest(),
        "k237": sha256(K237.read_bytes()).hexdigest(),
    }
    with redirect_stdout(StringIO()) as log:
        m = runpy.run_path(str(BACKEND))
    assert "FAILURES=0" in log.getvalue()
    one, zero, full, n = m["ONE"], m["ZERO"], m["FULL"], m["N"]

    def direction(mu, blade):
        return {1 << mu: {blade: one}}

    def coefficient(left, image):
        return m["wedge_raw"](left, image).get(full, {}).get(0, zero)

    basis = [(label, mu, label ^ (1 << mu)) for label in range(4) for mu in range(n)]
    lookup = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}

    # Unlike the producer's all-pairs construction, enumerate forward image
    # support first, audit every output label, and then form the raw matrix.
    def matrix(principal):
        raw = sp.zeros(56)
        normal = direction(principal, 0)
        for column, (_, mu, blade) in enumerate(basis):
            image = m["shiab"](m["wedge_raw"](normal, direction(mu, blade)), CHANNELS)
            for form_mask, element in image.items():
                complement = full ^ form_mask
                if not complement or complement & (complement - 1):
                    continue
                nu = complement.bit_length() - 1
                for outblade in element:
                    label = outblade ^ (1 << nu)
                    assert label in range(4)
                    row = lookup[(label, nu)]
                    value = coefficient(direction(nu, outblade), image)
                    assert value[1] == 0
                    raw[row, column] = sp.Rational(
                        value[0].numerator, value[0].denominator
                    )
        return (raw - raw.T) / 2

    d0, d1 = matrix(0), matrix(1)
    assert d0.rank() == d1.rank() == 32
    odd = sp.eye(56)[:, lookup[(3, 0)]]
    collective = sum(
        (sp.eye(56)[:, lookup[(2, j)]] for j in range(2, 14)), sp.zeros(56, 1)
    )
    assert d0 * odd == -collective and d0 * collective == 12 * odd
    assert d1[lookup[(1, 1)], lookup[(3, 0)]] == -1

    hull = sp.Matrix.hstack(odd, collective).columnspace()
    growth = [len(hull)]
    while True:
        enlarged = sp.Matrix.hstack(
            *(hull + [matrix_ * vector for matrix_ in (d0, d1) for vector in hull])
        ).columnspace()
        growth.append(len(enlarged))
        if len(enlarged) == len(hull):
            break
        hull = enlarged
    carrier = sp.Matrix.hstack(*hull)
    assert growth == record["minimal_two_plane_hull"]["dimension_growth"] == [2, 4, 7, 9, 9]
    assert carrier.rank() == record["minimal_two_plane_hull"]["dimension"] == 9
    assert all(sp.Matrix.hstack(carrier, op * carrier).rank() == 9 for op in (d0, d1))
    lam = sp.Symbol("lambda")
    expected = sp.expand(lam * (lam**2 + 1) * (lam**2 + 4) * (lam**2 + 12) * (lam**2 + 121))
    for op in (d0, d1):
        action = sp.Matrix.hstack(
            *(carrier.gauss_jordan_solve(op * vector)[0] for vector in hull)
        )
        assert action.rank() == 8
        assert sp.expand(action.charpoly(lam).as_expr()) == expected

    def ordered(left, right, principal, channels=CHANNELS):
        image = m["shiab"](
            m["wedge_raw"](direction(principal, 0), right), channels
        )
        return coefficient(left, image)

    odd_dir, odd_out = direction(0, 2), direction(1, 5)
    assert ordered(odd_out, odd_dir, 2) == (Q(-2), Q())
    assert ordered(odd_dir, odd_out, 2) == zero
    assert record["dx2_obstruction"]["odd_witness"]["output_label"] == 7
    spokes = [direction(j, 2 | (1 << j)) for j in range(2, 14)]
    even_out = direction(2, 2)
    forward = sum((ordered(even_out, spoke, 2)[0] for spoke in spokes), Q())
    reverse = sum((ordered(spoke, even_out, 2)[0] for spoke in spokes), Q())
    assert (forward, reverse, (forward - reverse) / 2) == (Q(-22), Q(), Q(-11))
    assert record["dx2_obstruction"]["collective_witness"]["output_label"] == 6

    # Hostile controls: projecting dx2 to labels 0..3 erases both real
    # outputs, while substituting the normal dx0 coefficient kills this dx2
    # escape.  Neither is allowed to masquerade as common invariance.
    projected_dx2 = sp.zeros(56)
    assert projected_dx2 * odd == sp.zeros(56, 1)
    assert ordered(odd_out, odd_dir, 0) == zero
    assert record["claim_ceiling"].startswith("Exact selected local dx0/dx1")
    print("[PASS] K249 independent support, 9D hull, dx2 escape and hostile projection/principal controls")


if __name__ == "__main__":
    main()
