#!/usr/bin/env python3
"""Independent finite-measure replay and hostile nontranslation/weight controls."""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations, product


def p(xs):
    m22 = sum(xs[i]**2 * xs[j]**2 for i, j in combinations(range(6), 2))
    m211 = sum(xs[i]**2 * xs[j] * xs[k] for i in range(6)
               for j, k in combinations((n for n in range(6) if n != i), 2))
    m1111 = sum(xs[i]*xs[j]*xs[k]*xs[l] for i, j, k, l in combinations(range(6), 4))
    return m22 - m211/2 + m1111


def factor(values, weights):
    m0 = sum(weights, Q())
    m1 = sum((w*c for c, w in zip(values, weights)), Q())
    m2 = sum((w*c*c for c, w in zip(values, weights)), Q())
    return 15*(m0*m2-m1*m1)**2*m0**2


def direct(values, weights, anchor):
    return sum((p(tuple(c-anchor for c in cs)) *
                product_weight(ws) for cs, ws in
                ((tuple(values[i] for i in inds), tuple(weights[i] for i in inds))
                 for inds in product(range(len(values)), repeat=6))), Q())


def product_weight(weights):
    out = Q(1)
    for weight in weights:
        out *= weight
    return out


def main():
    low_c, low_w = (Q(1), Q(2)), (Q(2), Q(3))
    high_c, high_w = (Q(1), Q(2), Q(3)), (Q(2), Q(3), Q(1))
    k4, k5 = factor(low_c, low_w), factor(high_c, high_w)
    assert k5 > k4
    for anchor in (Q(-2), Q(0), Q(5, 3), Q(7)):
        assert direct(low_c, low_w, anchor) == k4
        assert direct(high_c, high_w, anchor) == k5
    # An arbitrary variable A on the two outer coordinates cannot be pulled
    # out as a constant; replay both nested cubes and their disjoint strips.
    anchor = Q(5, 3)
    def a(u, v):
        return Q(1, 256 + u + 2*v + anchor)
    low_a = sum((wu*wv*a(u, v) for u, wu in zip(low_c, low_w)
                 for v, wv in zip(low_c, low_w)), Q())
    high_a = sum((wu*wv*a(u, v) for u, wu in zip(high_c, high_w)
                  for v, wv in zip(high_c, high_w)), Q())
    strip_a = high_a-low_a
    assert k5*high_a-k4*low_a == (k5-k4)*low_a+k5*strip_a
    # Hostile controls: moving just one coordinate is not a common translation;
    # dropping unequal weights is the same measure error caught in K239.
    assert p((Q(1), Q(2), Q(3), Q(4), Q(5), Q(6))) != p(
        (Q(2), Q(2), Q(3), Q(4), Q(5), Q(6)))
    assert k5 != factor(high_c, (Q(1), Q(1), Q(1)))
    print("[PASS] K240 independent non-centered weighted shell replay")


if __name__ == "__main__":
    main()
