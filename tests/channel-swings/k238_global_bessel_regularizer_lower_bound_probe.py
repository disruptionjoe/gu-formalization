#!/usr/bin/env python3
"""K238 independent integral/determinant replay and hostile measure control."""
from __future__ import annotations

import mpmath as mp


mp.mp.dps = 65


def determinant_kernel(rows, columns, kernel):
    return mp.det(mp.matrix([[kernel(t + u) for u in columns] for t in rows]))


def main():
    # Reconstruct the representation without importing the producer. The
    # p=sinh(s) coordinate avoids the integrable lambda=1 singularity.
    for z_text in ('0.05', '0.125', '0.25'):
        z = mp.mpf(z_text)
        original = 2 * mp.besselk(1, z)
        # The omitted [16,infinity) tail is at most
        # 4/z * exp(-z*exp(16)/2), far below the comparison tolerance.
        energy_integral = 2 * mp.quad(lambda s: mp.exp(-z*mp.cosh(s))*mp.cosh(s), [0, 1, 3, 8, 16])
        shifted_flat = 2 * mp.exp(-z) / z
        assert abs(original - energy_integral) < mp.mpf('1e-48')
        assert original > shifted_flat
        # A false unshifted density domination would assert 2*K1 >= 2/z.
        assert original < 2/z

    rows = [mp.mpf(x) for x in ('0.11', '0.06', '0.01')]
    cols = [mp.mpf(x) for x in ('0.09', '0.035', '0.004')]
    for size in (2, 3):
        t, u = rows[:size], cols[:size]
        numerator = determinant_kernel(t, u, lambda z: 2*mp.besselk(1, z))
        denominator = determinant_kernel(t, u, lambda z: 2/z)
        shifted = determinant_kernel(t, u, lambda z: 2*mp.exp(-z)/z)
        assert numerator > shifted > 0 and denominator > 0
        assert abs(shifted / denominator - mp.exp(-sum(t)-sum(u))) < mp.mpf('1e-48')
    print('[PASS] K238 independent energy integral, determinant, wrong-density controls')


if __name__ == '__main__':
    main()
