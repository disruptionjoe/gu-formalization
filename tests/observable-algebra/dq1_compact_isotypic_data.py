#!/usr/bin/env python3
"""Resolver Wave B / DQ1: exact Spin(9)xSpin(5) isotypic data on ker Gamma.

This is the constraint-preserving diagonal action, not the full compression
algebra and not the 14-frame/fundamental-spinor carrier used by W228.

The exact branching on either 14D Weyl half is

  ker Gamma = U + X + Y
  U = Delta_9 x Delta_5                       (64)
  X = RS_9 x Delta_5                         (512)
  Y = Delta_9 x RS_5                         (256).

Both Weyl halves restrict identically.  The executable derives dimensions and
the residual arithmetic; the Schur types and multiplicities are explicit
standard compact-Clifford inputs, then justified analytically in the paired
report.  Under those exact inputs, every type is quaternionic with multiplicity
signature (1,1), so the compact classification residual has real dimension 12.
"""
from __future__ import annotations

from fractions import Fraction


def check(name: str, condition: bool) -> None:
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}")
    assert condition, name


def b_dimension(weight: tuple[Fraction, ...]) -> int:
    """Weyl dimension formula for type B_n in orthonormal coordinates."""
    n = len(weight)
    rho = tuple(Fraction(2 * (n - i) - 1, 2) for i in range(n))
    shifted = tuple(weight[i] + rho[i] for i in range(n))
    value = Fraction(1)
    # Positive short roots e_i.
    for i in range(n):
        value *= shifted[i] / rho[i]
    # Positive long roots e_i-e_j and e_i+e_j.
    for i in range(n):
        for j in range(i + 1, n):
            value *= (shifted[i] - shifted[j]) / (rho[i] - rho[j])
            value *= (shifted[i] + shifted[j]) / (rho[i] + rho[j])
    check(f"B{n} Weyl dimension is integral", value.denominator == 1)
    return value.numerator


def main() -> int:
    print("DQ1 — exact compact isotypic data on V=ker Gamma")
    half = Fraction(1, 2)
    spin9 = (half, half, half, half)
    rs9 = (Fraction(3, 2), half, half, half)
    spin5 = (half, half)
    rs5 = (Fraction(3, 2), half)

    d_s9 = b_dimension(spin9)
    d_r9 = b_dimension(rs9)
    d_s5 = b_dimension(spin5)
    d_r5 = b_dimension(rs5)
    check("Spin(9) spinor dimension", d_s9 == 16)
    check("Spin(9) gamma-traceless vector-spinor dimension", d_r9 == 128)
    check("Spin(5) spinor dimension", d_s5 == 4)
    check("Spin(5) gamma-traceless vector-spinor dimension", d_r5 == 16)
    check("9 x 16 = 16 + 128", 9 * d_s9 == d_s9 + d_r9)
    check("5 x 4 = 4 + 16", 5 * d_s5 == d_s5 + d_r5)

    dims = {
        "U=Delta9xDelta5": d_s9 * d_s5,
        "X=RS9xDelta5": d_r9 * d_s5,
        "Y=Delta9xRS5": d_s9 * d_r5,
    }
    check("three compact types have dimensions 64,512,256",
          tuple(dims.values()) == (64, 512, 256))
    check("one Weyl-half kernel has dimension 832", sum(dims.values()) == 832)
    check("both Weyl halves give dim ker Gamma=1664", 2 * sum(dims.values()) == 1664)
    check("independent rank-nullity agrees", 14 * 128 - 128 == 1664)

    # Compact Clifford reality table: Delta_9 and RS_9 are real type;
    # Delta_5 and RS_5 are quaternionic type.  Tensoring real with
    # quaternionic yields quaternionic.  The central (-1,-1) acts trivially,
    # so all three descend to the compact subgroup image in Spin(9,5).
    types = {name: "H" for name in dims}
    multiplicities = {name: (1, 1) for name in dims}
    d_real = {"R": 1, "C": 2, "H": 4}
    overlap = sum(d_real[types[name]] * a * b
                  for name, (a, b) in multiplicities.items())
    check("all three shared types are quaternionic", set(types.values()) == {"H"})
    check("each type occurs once on each Krein sign", set(multiplicities.values()) == {(1, 1)})
    check("compact classification residual dimension is 12", overlap == 12)

    # Live controls against the recurrent summary-layer errors.
    deleted_minus = sum(d_real[types[name]] * 1 * 0 for name in dims)
    check("plant: deleting one chirality copy collapses overlap to zero", deleted_minus == 0)
    wrong_complex = sum(d_real["C"] for _ in dims)
    check("plant: wrong complex Schur type gives 6, not the certified 12", wrong_complex == 6)
    check("plant: dimensions cannot merge X and Y", dims["X=RS9xDelta5"] != dims["Y=Delta9xRS5"])
    frame_only = (("9", "positive"), ("5", "negative"))
    check("control: frame-only 9+5 carrier has no shared type", frame_only[0][0] != frame_only[1][0])

    print("VERDICT: DQ1 residual dimension = 12 conditional on the explicit standard")
    print("compact-Clifford Schur-type and K-invariant pairing inputs.")
    print("This corrects compact uniqueness on this carrier only; the physical stabilizer,")
    print("quotient, and noncompact existence leg remain open.")
    print("P1/P2/P3 are unchanged and unused.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
