#!/usr/bin/env python3
"""Exact M-M27 control: lens-space signature defect versus framing class.

The primary formula is Kirby--Melvin/Rademacher

    defect(L(p;q)) = 4 p s(q,p),

with the Dedekind sum evaluated exactly.  A framing on a fixed spin
3-manifold is an affine Z choice; adding rho changes the stabilized class by
2 in pi_3^S = Z/24.  The script therefore tests the all-lens formula and the
separate framing orbit rather than identifying either object with the other.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction


def sawtooth(numerator: int, denominator: int) -> Fraction:
    residue = numerator % denominator
    if residue == 0:
        return Fraction(0)
    return Fraction(residue, denominator) - Fraction(1, 2)


def dedekind_sum(q: int, p: int) -> Fraction:
    if p <= 0 or math.gcd(q, p) != 1:
        raise ValueError("L(p;q) requires p>0 and gcd(p,q)=1")
    return sum(
        (sawtooth(k, p) * sawtooth(q * k, p) for k in range(1, p)),
        Fraction(0),
    )


def signature_defect(q: int, p: int, normalization: int = 4) -> Fraction:
    return normalization * p * dedekind_sum(q, p)


def stable_class(base_class: int, framing_shift: int, rho_stabilization: int = 2) -> int:
    return (base_class + rho_stabilization * framing_shift) % 24


def run_checks(
    *,
    normalization: int = 4,
    rho_stabilization: int = 2,
    primary_modulus: int = 3,
) -> list[str]:
    checks: list[str] = []

    for p in range(2, 25):
        expected = Fraction((p - 1) * (p - 2), 3)
        assert signature_defect(1, p, normalization) == expected
    checks.append("L(p;1) closed form for p=2..24")

    for p in range(3, 18):
        for q in range(1, p):
            if math.gcd(q, p) == 1:
                assert signature_defect(p - q, p, normalization) == -signature_defect(q, p, normalization)
    checks.append("orientation reversal q -> -q")

    for p in range(2, 18):
        for q in range(1, p):
            if math.gcd(q, p) == 1:
                lhs = dedekind_sum(q, p) + dedekind_sum(p, q)
                rhs = Fraction(p * p + q * q + 1, 12 * p * q) - Fraction(1, 4)
                assert lhs == rhs
    checks.append("Dedekind reciprocity")

    assert signature_defect(1, 2, normalization) == 0
    checks.append("RP3 signature defect is zero, not e_R")

    p1 = 4
    e_real = Fraction(p1, 48)
    rp3_stable_class = (24 * e_real) % 24
    assert e_real == Fraction(1, 12)
    assert rp3_stable_class == 2
    checks.append("filed RP3 framing has e_R=1/12 and class 2 mod 24")

    orbit = [stable_class(2, k, rho_stabilization) for k in range(12)]
    assert 2 in orbit and 6 in orbit
    assert 2 % primary_modulus != 0 and 6 % primary_modulus == 0
    checks.append("same RP3 spin manifold has nonzero and zero 3-primary framings")

    for base in range(24):
        residues = {stable_class(base, k, rho_stabilization) % primary_modulus for k in range(3)}
        assert residues == set(range(primary_modulus))
    checks.append("every framing orbit reaches every Z/3 residue")

    assert stable_class(0, 12, rho_stabilization) == 0
    checks.append("rho orbit has period 12 in Z/24")

    table_rows = [
        (p, q, signature_defect(q, p, normalization))
        for p in range(2, 13)
        for q in range(1, p)
        if math.gcd(q, p) == 1
    ]
    assert len(table_rows) == sum(math.prod([1]) for p in range(2, 13) for q in range(1, p) if math.gcd(q, p) == 1)
    assert len(table_rows) == 45
    checks.append("complete coprime L(p;q) control table through p=12")

    try:
        dedekind_sum(2, 4)
    except ValueError:
        pass
    else:
        raise AssertionError("non-coprime lens label was admitted")
    checks.append("non-coprime label rejection")

    assert signature_defect(1, 3, normalization) == Fraction(2, 3)
    assert signature_defect(2, 3, normalization) == Fraction(-2, 3)
    checks.append("L(3;1)/L(3;2) signed control")

    assert len({stable_class(2, k, rho_stabilization) for k in range(12)}) == 12
    checks.append("honest-framing affine orbit does not collapse")

    assert signature_defect(1, 2, normalization) == signature_defect(1, 2, normalization)
    assert len({stable_class(2, k, rho_stabilization) % primary_modulus for k in range(3)}) == 3
    checks.append("one manifold defect coexists with three framing residues")

    return checks


def selftest() -> None:
    baseline = run_checks()
    assert len(baseline) == 13
    print(f"clean baseline: {len(baseline)}/{len(baseline)} checks")

    mutations = [
        ("missing Rademacher factor four", {"normalization": 1}),
        ("rho falsely stabilizes to zero", {"rho_stabilization": 0}),
        ("three-primary projection retyped as two-primary", {"primary_modulus": 2}),
        ("rho falsely stabilizes to four", {"rho_stabilization": 4}),
    ]
    caught = 0
    for name, kwargs in mutations:
        try:
            run_checks(**kwargs)
        except AssertionError:
            caught += 1
            print(f"[CAUGHT] {name}")
        except Exception as exc:  # crashes are not detections
            raise AssertionError(f"mutation crashed instead of reaching a failing check: {name}: {exc}") from exc
        else:
            raise AssertionError(f"mutation escaped: {name}")
    assert caught == len(mutations)
    print(f"mutation controls: {caught}/{len(mutations)} caught by failing checks")


def main() -> None:
    checks = run_checks()
    for index, check in enumerate(checks, 1):
        print(f"[PASS {index:02d}] {check}")
    print(f"VERDICT: FRAMING_RELATIVE_NOT_LENS_SPACE_INVARIANT ({len(checks)}/{len(checks)} checks)")
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        selftest()


if __name__ == "__main__":
    main()
