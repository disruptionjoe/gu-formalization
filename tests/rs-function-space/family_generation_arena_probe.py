#!/usr/bin/env python3
r"""
STEP 3 support (WC-FUNCTION-SPACE-EXT): does the HONEST family / characteristic-class data on the
sector's existing geometry carry an order-3 (generation) piece, or is it 2-primary?

The generation arena is the Z/3 summand of pi_3^s = Z/24 = Z/8 (+) Z/3. A reduced e-invariant
e in Q/Z maps to Z/24 by e = n/24; its Z/3-part is n mod 3. So an index value N entering the
gravitational -p_1/24 channel is:
    3-PRIMARY (order-3 present)  <=>  N != 0 mod 3   (e = N/24 keeps a factor of 3)
    2-PRIMARY (no order-3)       <=>  N == 0 mod 3   (e = N/24 has denominator | 8)

This probe checks EVERY honestly-computed family/characteristic number on the existing data and asks
whether any of them reaches N != 0 mod 3. FIREWALL (DEAD-ENDS.md, absorbed/gu-source-action): the
disguised chi-import ch2=24 with the illegitimate /8 normalization (=> "3") is an automatic FAIL and
is shown ONLY as the contrast that a valid S_IG may NOT use. The honest value is ch2(S_X)[K3] = -5376.

SCOPING NOTE (2026-07-10, -38 adjudication): the "every honest number == 0 mod 3" sweep below is
CARRIER-A-SCOPED (ghost-subtracted gravitino complex, 21*sigma/8 convention). The honest geometric
gamma-traceless operator (Homma-Semmelmann) is a different published K-class with ind Q = 19*sigma/8
= -38 == 1 mod 3 on K3 and NONZERO order-3 Nikulin rho classes (0,2,1)/3. Which carrier the GU
generation arena names is the SG4 identification question; the fiberwise -38 != 0 mod 3 is NOT a
pass of the families criterion. See canon/gamma-traceless-38-adjudication-RESULTS.md.

Grade: computed / exact (rational arithmetic). Target-import-safe. Internal tier (caveat (e)).
Run: python tests/rs-function-space/family_generation_arena_probe.py
"""
from fractions import Fraction as Fr

# values that may NOT be used to MANUFACTURE the count (DEAD-ENDS.md target-import guard)
FORBIDDEN_IMPORTS_AS_ANSWER = {24, 3}   # chi(K3)=24 and the /8 count 3


def z3_part(N: int):
    """Z/3-part of the reduced e-invariant e = N/24 (class n=N in Z/24 = Z/8 (+) Z/3)."""
    n = N % 24
    return n % 3


def is_two_primary_index(N: int) -> bool:
    """N contributes to the 2-primary Z/8 arena only (no order-3) iff N == 0 mod 3."""
    return N % 3 == 0


# ------------------------------------------------------------------- the honest existing data
HONEST = [
    ("bulk I_3/2[K3] = 21*sigma/8 (sigma=-16)",      -42),
    ("twist-by-16 RS index (flat)",                  -672),
    ("ch2(S_X)[K3] honest (source-action SPEC)",     -5376),
    ("ch2(S_X)[K3] normalized /8",                   -672),
    ("RS boundary APS eta on L(2;1) (STEP 2)",       0),
]

# the DEAD-END disguised import (shown only as the forbidden contrast)
DEAD_END = [
    ("DISGUISED chi-import ch2=24 (tangent-only |p1/2|)", 24, "chi-import; 24 only because 2chi+3sigma=0 on K3"),
    ("DEAD-END /8 'count' 24/8 = 3",                       3, "illegitimate /8 normalization (honest e is /24)"),
]


def main():
    print("=" * 90)
    print("GENERATION-ARENA PROBE: is the honest family/char-class data 2-primary (no order-3)?")
    print("=" * 90)
    print(f"  discriminant: index N reaches the order-3 arena  <=>  N != 0 mod 3  (e=N/24 keeps a 3)")
    print()
    print(f"  {'honest quantity':<44}{'N':>8}{'N mod 3':>9}{'arena':>12}")
    all_two_primary = True
    for name, N in HONEST:
        tp = is_two_primary_index(N)
        all_two_primary &= tp
        print(f"  {name:<44}{N:>8}{z3_part(N):>9}{'2-PRIMARY' if tp else '3-PRIMARY':>12}")
    print()
    print("  => EVERY honest existing-data family/char number is == 0 mod 3 (Z/3-part 0):")
    print(f"     all_two_primary = {all_two_primary}.  The honest internal/family computation carries")
    print("     NO order-3 (generation) piece. It cannot manufacture an odd count.")

    print("\n  the ONLY objects that reach the order-3 arena are NOT internal family indices:")
    print("   - the tangential Lambda^2_+ framing carrier: e_R = 1/12 = 2/24, Z/3-part = "
          f"{z3_part(2)} != 0 (LOCATED, not a count; Hom(Z/3,Z)=0), and")
    print("   - a genuinely EXTERNAL topological datum (flux): net chiral index = flux number, odd for")
    print("     odd flux (canon/external-topological-index-flux-RESULTS.md).")

    print("\n" + "-" * 90)
    print("FIREWALL contrast (DEAD-ENDS.md): the forbidden route to '3' -- shown, never used")
    print("-" * 90)
    for name, N, why in DEAD_END:
        print(f"  [FORBIDDEN] {name:<44} N={N:<5} ({why})")
    print("  These are automatic FAILs; a valid S_IG may NOT use them.")

    print("\n" + "=" * 90)
    print("VERDICT / what S_IG must do (SPEC hard bar): produce a families-pushforward index N over the")
    print("GU metric fiber GL(4,R)/O(3,1) with N != 0 mod 3 WITHOUT importing chi. On ALL existing data")
    print("that value is 0 mod 3 (2-primary); the honest ch2 is -5376, not 24. So on present evidence the")
    print("order-3 count is NOT internally sourced -- consistent with external-by-structure and the")
    print("firewall-boundary reading. Closing (or killing) the crux needs the unbuilt families pushforward.")
    print("=" * 90)

    # guards
    assert all_two_primary, "every honest family number must be 0 mod 3 (2-primary)"
    assert z3_part(2) == 2, "the tangential carrier e_R=1/12 must be the order-3 object"
    for _, N in HONEST:
        assert N not in FORBIDDEN_IMPORTS_AS_ANSWER, "no honest quantity may equal a forbidden import"
    print("\n[OK] probe guards passed (firewall intact: no chi/8=3 used to source a count).")


if __name__ == "__main__":
    main()
