#!/usr/bin/env python3
"""K238: independent numerical controls for an analytic Andreief comparison.

The proof is in VERIFICATION.md's K238 section. These finite checks are not the
proof and do not enclose a cubature or a signed order-six group.
"""
from __future__ import annotations

import mpmath as mp


mp.mp.dps = 75


def ratio(rows, columns):
    size = len(rows)
    bessel = mp.matrix([[2 * mp.besselk(1, t + u) for u in columns] for t in rows])
    cauchy = mp.matrix([[2 / (t + u) for u in columns] for t in rows])
    return mp.det(bessel) / mp.det(cauchy)


def profiles():
    q = mp.mpf
    # Distinct ordered times, including a strongly asymmetric shape. All
    # arguments are at most 1/4, as in the K186 positive radial core.
    return (
        ([q('0.08'), q('0.05'), q('0.01')], [q('0.07'), q('0.04'), q('0.015')]),
        ([q('0.14'), q('0.11'), q('0.01')], [q('0.09'), q('0.04'), q('0.005')]),
        ([q('0.18'), q('0.07'), q('0.003')], [q('0.06'), q('0.004'), q('0.001')]),
    )


def main():
    for rows, columns in profiles():
        for size in (1, 2, 3):
            r = ratio(rows[:size], columns[:size])
            floor = mp.exp(-sum(rows[:size]) - sum(columns[:size]))
            assert r > floor > mp.exp(-mp.mpf(size) / 4)
    # The K186 energy density is strictly above, not below, shifted
    # Lebesgue density; the sign of this premise is load-bearing.
    for energy in ('1.01', '1.5', '3', '20'):
        z = mp.mpf(energy)
        assert z / mp.sqrt(z*z - 1) > 1
    print('[PASS] K238 exact-scope Bessel/Cauchy lower-bound controls (9 profiles)')


if __name__ == '__main__':
    main()
