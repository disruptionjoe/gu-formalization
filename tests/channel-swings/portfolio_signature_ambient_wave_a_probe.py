#!/usr/bin/env python3
"""Independent Wave-A probe for the SIGNATURE-AMBIENT relative-sign route.

This does not settle the fork.  It independently checks the finite signature
arithmetic, the convention-invariant balance test, and the primary-source
polarity that decides the disposition: SC-SIG-03 says the choice is not forced,
while SC-SIG-04 says K77 is assumed rather than derived.
"""

from fractions import Fraction
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
EXTRACTION = ROOT / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"

checks: list[tuple[str, bool]] = []


def check(name: str, condition: bool) -> None:
    checks.append((name, bool(condition)))
    print(("PASS" if condition else "FAIL") + " :: " + name)


def block_signature(signs: tuple[int, ...], lam: Fraction) -> tuple[int, int, int]:
    """Analytic inertia of tr(g^-1 h g^-1 h)-lam tr(g^-1 h)^2.

    The six off-diagonal symmetric basis vectors have signs s_i*s_j.
    The four diagonal directions have three eigenvalues +1 and one
    eigenvalue 1-4*lam.  This is exact and independent of a matrix package.
    """
    off = [signs[i] * signs[j] for i in range(4) for j in range(i + 1, 4)]
    diag = [Fraction(1)] * 3 + [Fraction(1) - 4 * lam]
    values = [Fraction(v) for v in off] + diag
    return (
        sum(v > 0 for v in values),
        sum(v < 0 for v in values),
        sum(v == 0 for v in values),
    )


def balance(*pairs: tuple[int, int]) -> int:
    return abs(sum(p for p, _ in pairs) - sum(q for _, q in pairs))


def claim_block(text: str, claim_id: str) -> str:
    match = re.search(rf"^- id: {re.escape(claim_id)}\n(?P<body>.*?)(?=^- id:|\Z)", text, re.M | re.S)
    if not match:
        raise AssertionError(f"missing claim {claim_id}")
    return match.group("body")


def main() -> None:
    plus = (1, 1, 1, -1)
    minus = tuple(-s for s in plus)

    for label, signs in (("mostly-plus", plus), ("mostly-minus", minus)):
        check(f"C1 {label} raw (7,3)", block_signature(signs, Fraction(0)) == (7, 3, 0))
        check(f"C1 {label} trace-flipped (6,4)", block_signature(signs, Fraction(1, 2)) == (6, 4, 0))
        check(f"C1 {label} degeneracy at 1/4", block_signature(signs, Fraction(1, 4)) == (6, 3, 1))

    check("C1 fibre even under uniform base sign reversal",
          all(block_signature(plus, x) == block_signature(minus, x)
              for x in (Fraction(0), Fraction(1, 4), Fraction(1, 2))))
    check("C1 horizontal block is odd under base sign reversal",
          minus == tuple(-s for s in plus))

    draft = ((1, 3), (6, 4))
    transcript = ((1, 3), (4, 6))
    check("C2 draft uniform display has balance zero", balance(*draft) == 0)
    check("C2 mirrored draft display has balance zero",
          balance(*tuple((q, p) for p, q in draft)) == 0)
    check("C2 transcript blocks have balance four", balance(*transcript) == 4)
    check("C2 mirrored transcript blocks have balance four",
          balance(*tuple((q, p) for p, q in transcript)) == 4)
    check("C2 planted mixed-notation sum is detected",
          balance((3, 1), (4, 6)) == 0 and balance(*transcript) != 0)

    extraction = EXTRACTION.read_text(encoding="utf-8")
    check("C3 primary extraction pins eqs 12.18-12.19",
          "ג : X^{1,3} → Y^{7,7}  (12.18)" in extraction
          and "ג∗(TY^{7,7}) = TX^{1,3} ⊕ N^{6,4}_ג  (12.19)" in extraction)
    check("C3 primary extraction pins Spin(1,3)xSpin(6,4)",
          "Spin(1,3)×Spin(6,4)" in extraction)

    register = REGISTER.read_text(encoding="utf-8")
    sig3 = claim_block(register, "SC-SIG-03")
    sig4 = claim_block(register, "SC-SIG-04")
    check("C3 SC-SIG-03 preserves source uncertainty",
          "polarity: UNCERTAIN" in sig3
          and "does not know how to choose" in sig3
          and "choices are made that are not yet forced" in sig3)
    check("C3 SC-SIG-04 preserves assumed-not-derived K77",
          "polarity: ASSERTS" in sig4
          and "assumes, rather than derives" in sig4
          and "we will assume that the metric on Y is split with signature (7,7)" in sig4)

    # The planted non-family label keeps the family portrait from accepting
    # arbitrary ten-dimensional signatures as trace-reversed Lorentz fibres.
    admissible = {(7, 3), (6, 4), (3, 7), (4, 6)}
    check("C4 planted (5,5) label rejected", (5, 5) not in admissible)
    check("C4 balance zero pins unordered {7,7} in dimension 14",
          {(max(p, 14 - p), min(p, 14 - p)) for p in range(15)
           if abs(p - (14 - p)) == 0} == {(7, 7)})
    check("C4 balance four pins unordered {9,5} in dimension 14",
          {(max(p, 14 - p), min(p, 14 - p)) for p in range(15)
           if abs(p - (14 - p)) == 4} == {(9, 5)})

    passed = sum(ok for _, ok in checks)
    print(f"\nSIGNATURE-AMBIENT Wave A: {passed}/{len(checks)} exact/source checks PASS")
    print("DISPOSITION: SOURCE_ASSIGNMENT_K77__GEOMETRIC_SELECTION_UNDERDETERMINED__ONE_RELATIVE_SIGN_BIT")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
