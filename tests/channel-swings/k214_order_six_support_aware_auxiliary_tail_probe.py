#!/usr/bin/env python3
"""Independent K214 integral, rational cutoff and hostile-scope checks."""
from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
mp.mp.dps = 55


def one_factor_tail(s: mp.mpf, t: mp.mpf) -> mp.mpf:
    # Gamma(6,256) expectation of rho * 2 times the truncated K1 kernel.
    # Integrate rho independently first; no producer function is imported.
    c = 2 * 256**6 * 6
    return c * mp.quad(lambda u: (256+s*mp.sqrt(1+u*u))**(-7),
                       [mp.sinh(t), mp.inf])


def independent_bound(supports: tuple[Q, ...], m: int) -> Q:
    u = Q(4**m-1, 2**(m+1))
    prod = Q(1)
    for s in supports:
        prod *= s
    return 256 * sum((Q(256)/(256+s*u))**6 for s in supports) / prod


def main() -> None:
    record = json.loads((P / "k214-order-six-support-aware-auxiliary-tail.json").read_text())
    assert record["input_sha256"]["K213"]
    for s,t in ((mp.mpf("0.2"), mp.mpf("1.5")),
                (mp.mpf("0.01"), mp.mpf("4"))):
        actual = one_factor_tail(s,t)
        upper = 2/s*(256/(256+s*mp.sinh(t)))**6
        assert 0 < actual < upper
        # Omitting the Gamma shape multiplier fails the independent integral.
        assert actual > upper/6
    print("[PASS] independent one-factor Gamma/cosh tail integrals and shape control")

    delta = Q(1, 2**180)
    target = Q(1, 10**21)
    assert independent_bound((delta,)*8, 443) < target
    assert independent_bound((delta,)*8, 442) >= target
    assert independent_bound((delta,)*8, 443) == (
        Q(2048,delta**8) * (Q(256)/(256+delta*Q(4**443-1,2**444)))**6)
    assert record["uniform_core"]["first_integer_m_sufficient_under_this_uniform_bound"] == 443
    print("[PASS] independent integer-rational dyadic cutoff and neighboring failure")

    # A point-specific cutoff cannot be silently reused on the extreme core.
    masks = json.loads((P / "k185-order-six-duffy-face-tail-wave.json").read_text())
    first = masks["complete_face_hypergraph"]["entries"][0]["terms"][0]
    words = masks["exact_allocation_certificate"]["allocation_catalog"][first["allocation_id"]]["support_masks_hex"].split(",")
    supports = tuple(Q(int(word,16).bit_count(),14) for word in words)
    assert len(supports) == 8
    assert independent_bound(supports, 443) < independent_bound((delta,)*8, 443)
    assert independent_bound((delta,)*8, 100) > target
    assert record["barycenter_diagnostic"]["terms"] == 1864
    print("[PASS] support-mask and hostile barycenter-to-uniform transfer checks")


if __name__ == "__main__":
    main()
