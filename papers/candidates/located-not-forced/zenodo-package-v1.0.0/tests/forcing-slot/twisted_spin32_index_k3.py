#!/usr/bin/env python3
r"""AGW character-valued spin-3/2 (Rarita-Schwinger) index on K3, twisted by the chiral 16.

ANGLE (forcing-slot campaign)
-----------------------------
Compute the Alvarez-Gaume / Witten character-valued spin-3/2 index density

    I_{3/2}(R) = { A-hat(R) * [ tr_v exp(R/2pi) - 1 ] }                          (AGW)

integrated over K3, then twisted by ch(16) of Spin(10). tr_v is the trace over
the SO(4) VECTOR rep of the tangent frame (this is the "vector index mu" of the
gravitino Psi_mu); the "-1" is the AGW spin-1/2 ghost subtraction. This is the
ONE object whose vector index makes it intrinsically NON-FRAME-TRIVIAL (it is NOT
of the form id_14 (x) U). The question: does its net integer FORCE 3, and is that
integer 3-primary (the count arena) or 2-primary (the selector arena)?

EXACT ARITHMETIC. No numpy/sympy. Fraction only. Everything anchored.

K3 data (homotopy-fixed controls, taken as inputs; chi is NEVER used as an input):
    sigma(K3) = -16
    p1(TK3)   = 3*sigma = -48          (Hirzebruch signature theorem; NOT chi)
    A-hat[K3] = -p1/24 = 2             (Dirac index control)
    chi(K3)   = 24 = 2^3 * 3           (recorded ONLY to test disguised-chi; unused in arithmetic)

On a real 4-manifold the tangent Chern roots are +-x1, +-x2, p1 = x1^2 + x2^2,
and every characteristic form of form-degree > 4 integrates to 0. So:
    A-hat              = 1 - p1/24                 (deg 0 + deg 4 only)
    tr_v exp(R/2pi)    = 4 + p1                    (= 2cosh x1 + 2cosh x2, deg<=4)
    tr_v exp - 1       = 3 + p1
    ch(F) for the 16   = 16 + ch1(F) + ch2(F)      (ch1 = 0: 16 of Spin(10) is traceless)
"""

from __future__ import annotations

from fractions import Fraction as F
from math import gcd


# ----------------------------------------------------------------------------- #
# K3 controls
# ----------------------------------------------------------------------------- #
SIGMA = -16
P1 = 3 * SIGMA                 # = -48, Hirzebruch p1 = 3 sigma. NOT chi.
AHAT = -F(P1, 24)              # = 2
CHI_FORBIDDEN = 24             # 2^3 * 3 ; only used to TEST for disguised chi.

assert AHAT == 2
assert P1 == -48


def factor(n: int) -> dict[int, int]:
    """Prime factorization of |n| (n != 0)."""
    m = abs(n)
    fac = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            fac[d] = fac.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        fac[m] = fac.get(m, 0) + 1
    return fac


def fac_str(n: int) -> str:
    if n == 0:
        return "0"
    sign = "-" if n < 0 else ""
    fac = factor(n)
    if not fac:
        return f"{sign}1"
    parts = [f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(fac.items())]
    return sign + " * ".join(parts)


def two_part(n: int) -> int:
    if n == 0:
        return 0
    f = factor(n)
    return 2 ** f.get(2, 0)


def odd_part(n: int) -> int:
    return abs(n) // two_part(n) if n else 0


def three_part(n: int) -> int:
    if n == 0:
        return 0
    f = factor(n)
    return 3 ** f.get(3, 0)


# ----------------------------------------------------------------------------- #
# The AGW spin-3/2 density, integrated on K3.
# I_{3/2 twisted} = int_K3 A-hat * (tr_v exp - 1) * ch(F)
# Keep only form-degree-4 (top) contributions.
#   A-hat        = 1 - p1/24                       [deg0 a0=1, deg4 a4 = -p1/24]
#   (tr_v - 1)   = 3 + p1                          [deg0 v0=3, deg4 v4 = p1]
#   ch(F)        = rankF + ch2F                    [deg0 rankF, deg4 ch2F]  (ch1=0)
# top (deg4) coefficient of the triple product, then integrate (mult by 1; classes
# are already the integrated numbers since p1 -> p1[K3], ch2F -> ch2F[K3]).
# ----------------------------------------------------------------------------- #
def spin32_index(rankF: int, ch2F: int) -> F:
    a0, a4 = F(1), -F(P1, 24)        # A-hat deg0, deg4 (a4 = +2)
    v0, v4 = F(3), F(P1)             # (tr_v exp -1) deg0, deg4
    # deg4 of a*v*ch = a4*v0*rankF + a0*v4*rankF + a0*v0*ch2F
    #               + (a4*v0 etc already) ; ch1=0 so no deg2*deg2 cross terms.
    return a4 * v0 * rankF + a0 * v4 * rankF + a0 * v0 * ch2F


def pure_gravitino_index() -> F:
    """Untwisted RS index: rankF = 1, flat (ch2F = 0)."""
    return spin32_index(rankF=1, ch2F=0)


def main():
    print("=" * 78)
    print("AGW character-valued SPIN-3/2 (Rarita-Schwinger) index on K3, twist by 16")
    print("=" * 78)
    print(f"  inputs: sigma={SIGMA}  p1=3*sigma={P1}  A-hat=-p1/24={AHAT}  "
          f"chi(K3)={CHI_FORBIDDEN} (UNUSED in arithmetic)")

    # --- analytic closed form ------------------------------------------------ #
    # deg4 of A-hat*(tr_v-1) = (1 - p1/24)(3 + p1) |_deg4 = p1 - 3*p1/24 = 7*p1/8.
    print("\n[closed form] deg4{ A-hat*(tr_v exp -1) } = 7*p1/8")
    seven_p1_over_8 = F(7 * P1, 8)
    print(f"   7*p1/8 = 7*({P1})/8 = {seven_p1_over_8}")

    # --- pure gravitino ------------------------------------------------------ #
    pure = pure_gravitino_index()
    print(f"\n[1] PURE gravitino index (rankF=1, flat):  I_3/2 = {pure}")
    assert pure == seven_p1_over_8, (pure, seven_p1_over_8)
    assert pure == F(-42), pure
    print(f"    = {int(pure)}  = {fac_str(int(pure))}")

    # --- twist by trivial/flat 16 (the only fabrication-free gauge bundle) --- #
    tw16 = spin32_index(rankF=16, ch2F=0)
    print(f"\n[2] TWISTED by flat 16 (rankF=16, ch2F=0):  I_3/2^16 = {tw16}")
    assert tw16 == 16 * pure
    assert tw16 == F(-672), tw16
    print(f"    = {int(tw16)}  = 16 * (pure {int(pure)})  = {fac_str(int(tw16))}")

    # cross-check against the repo's existing rs_k3_symbol_index BRST q=-1 branch
    # index_complex_for_v_plus_q(rank=16,ch2=0,q=-1) = (4+q)*rank*ahat + rank*p1 + (4+q)*ch2
    q = -1
    repo_brst = (4 + q) * 16 * int(AHAT) + 16 * P1 + (4 + q) * 0
    print(f"    cross-check vs repo rs_k3_symbol_index q=-1 branch: {repo_brst} "
          f"(match: {repo_brst == int(tw16)})")
    assert repo_brst == int(tw16)

    # --- controls ------------------------------------------------------------ #
    ahat_k3 = int(AHAT)
    ch2_sx = -5376
    print("\n[3] CONTROLS for primary-decomposition comparison:")
    print(f"    A-hat[K3]      = {ahat_k3}      = {fac_str(ahat_k3)}")
    print(f"    ch2(S_X)[K3]   = {ch2_sx}   = {fac_str(ch2_sx)}")
    print(f"    pure I_3/2     = {int(pure)}      = {fac_str(int(pure))}")
    print(f"    twisted I_3/2  = {int(tw16)}     = {fac_str(int(tw16))}")
    print(f"    ratios: ch2_sx/tw16 = {ch2_sx // int(tw16)} ; tw16/pure = {int(tw16)//int(pure)}")
    print(f"            -> shared ODD part {odd_part(int(pure))} = "
          f"{fac_str(odd_part(int(pure)))} across pure, twisted, ch2(S_X)")

    # --- PRIMARY DECOMPOSITION ----------------------------------------------- #
    for name, val in (("pure I_3/2", int(pure)), ("twisted I_3/2", int(tw16))):
        tp, op = two_part(val), odd_part(val)
        thp = three_part(val)
        print(f"\n[4] PRIMARY DECOMPOSITION of {name} = {val} = {fac_str(val)}")
        print(f"    2-part  = {tp} (= 2^{factor(val).get(2,0)})")
        print(f"    3-part  = {thp} (= 3^{factor(val).get(3,0)})")
        print(f"    odd-part= {op} = {fac_str(op)}   [contains 7 from A-hat ghost 7/8;"
              f" contains 3 from p1=3*sigma]")
        print(f"    is_3_primary (a power of 3)? {op == thp and tp == 1}")
        print(f"    equals 3?  {val == 3}   equals Dirac control 2?  {val == 2}")

    # --- WHERE the 3 and 7 come from (provenance, not a count) ---------------- #
    print("\n[5] PROVENANCE of the odd factors (these are GEOMETRY, not a count):")
    print("    factor 3 : enters ONLY through p1 = 3*sigma (Hirzebruch signature 3).")
    print(f"               sigma={SIGMA}, p1=3*sigma={P1}.  This 3 is HOMOTOPY-FIXED:")
    print("               identical for 1, 3, or 5 generations (like the e_R=p1/48 control).")
    print("    factor 7 : enters through 7*p1/8 = (1 - 1/8)*p1, i.e. the AGW ghost")
    print("               subtraction (3 vector dof) against A-hat = 1 - p1/24. The 7=8-1")
    print("               is a 2-arena coefficient artifact, not a generation number.")
    print("    => NEITHER odd factor is selectable; changing the generation count does")
    print("       NOT move them. They are not a forced count.")

    # --- FOUR FABRICATION CHECKS --------------------------------------------- #
    print("\n[6] FOUR FABRICATION CHECKS (be ruthless about any 3):")

    # (1) DISGUISED chi
    val = int(tw16)
    div_by_24 = (val % 24 == 0)
    chi_used_as_input = False  # chi never entered; only sigma did.
    # the integer's 3 came from p1=3sigma, NOT from chi or 2chi+3sigma=0 or an Euler class.
    print("   (1) DISGUISED chi:")
    print(f"       chi(K3)=24=2^3*3 used as an input anywhere?   {chi_used_as_input}")
    print(f"       does 24 divide twisted {val}?  {div_by_24} ({val} = 24 * {val//24})")
    print("       BUT 24 | twisted is COINCIDENTAL: twisted = 16*7*p1/8 = 14*p1 with")
    print(f"           p1=-48 -> {14*P1}; the 3 is the signature 3 (p1=3sigma), the 2^3")
    print("           is from rank-16 * A-hat. No chi, no 2chi+3sigma, no Euler class e(K3)")
    print("           entered. The integer is NOT chi in disguise (it is a signature/A-hat")
    print("           product). It is also not 24 and not a multiple landing ON 24.")
    is_disguised_chi = False

    # (2) REVERSE-ENGINEERED +8 / fitted backward
    print("   (2) REVERSE-ENGINEERED RS leg (+8 fitted backward):")
    print("       Derived FORWARD: rankF and the (4+q->3) ghost count are AGW-fixed, not")
    print("       chosen to hit a target. No +8 (or any constant) was added to reach 3.")
    print(f"       The result -42 / -672 is what the formula GIVES; it is not 3.")
    reverse_engineered = False

    # (3) CIRCULAR rank-4
    print("   (3) CIRCULAR rank-4:")
    print("       The '4' here is dim(K3)=4 = the SO(4) vector-rep dimension (tr_v over 4),")
    print("       a fixed manifold dimension, NOT an assumed-then-found bundle rank. The")
    print("       ghost subtraction uses 4-1=3 vector dof, also fixed by AGW, not assumed.")
    circular_rank = False

    # (4) FITTED holonomy
    print("   (4) FITTED holonomy / fitted gauge bundle:")
    print("       The flat-16 twist (ch2F=0) uses NO chosen instanton number. A genuinely")
    print("       gauge-CHIRAL 16 needs ch2(V_16)!=0, i.e. a FITTED instanton on K3 -- that")
    print("       would BE the fabrication, so it is refused. With ch2F a free parameter the")
    print("       index is rankF*p1 + 3*ch2F + 3*rankF*ahat; to force exactly 3 you would")
    print("       need ch2F fitted:")
    # solve spin32_index(16, ch2F) == 3
    # -672 + 3*ch2F == 3 -> ch2F = 225
    target = 3
    needed_ch2 = (F(target) - spin32_index(16, 0)) / 3
    print(f"           spin32(16, ch2F) = 3  ->  ch2F = {needed_ch2} (a FITTED instanton;")
    print("           225 is not a forced background -> refused as fabrication).")
    fitted_holonomy = False

    all_clean = not any([is_disguised_chi, reverse_engineered, circular_rank, fitted_holonomy])
    print(f"\n   ALL FOUR CHECKS CLEAN (no fabrication needed to report the result)? {all_clean}")

    # --- VERDICT ON THE FORCING SLOT ----------------------------------------- #
    print("\n[7] FORCING-SLOT VERDICT (a),(b),(c) + 3-primary:")
    tangential = True        # the whole index is 7*p1/8 ; carries p1.
    net_chiral = (int(tw16) != 0)   # genuine index asymmetry; nonzero.
    # non-frame-trivial: the vector index mu (tr_v over SO(4)) is NOT id_14 (x) U.
    non_frame_trivial = True
    integer_is_3 = (int(tw16) == 3) or (int(pure) == 3)
    net_chiral_is_3_primary = (two_part(int(tw16)) == 1)  # i.e. odd integer
    print(f"   (a) TANGENTIAL (carries p1)?            {tangential}")
    print(f"   (b) NET-CHIRAL (nonzero net index)?     {net_chiral}  (= {int(tw16)})")
    print(f"   (c) NON-FRAME-TRIVIAL (vector mu)?      {non_frame_trivial}")
    print(f"   net-chiral integer 3-PRIMARY?           {net_chiral_is_3_primary}"
          f"   (it is 2-primary-DOMINANT: 2-part={two_part(int(tw16))})")
    print(f"   integer_is_3?                           {integer_is_3}")
    fills = all([tangential, net_chiral, non_frame_trivial]) and net_chiral_is_3_primary
    print(f"   FILLS FORCING SLOT (all three AND 3-primary)? {fills}")

    print("\n" + "=" * 78)
    print("RESULT: the twisted spin-3/2 index is NONZERO, NET-CHIRAL, TANGENTIAL, and")
    print("NON-FRAME-TRIVIAL -- Horn A's MECHANISM is real -- but the integer is")
    print(f"{int(tw16)} = {fac_str(int(tw16))} (pure {int(pure)} = {fac_str(int(pure))}),")
    print("2-PRIMARY-DOMINANT with its only 3 a homotopy-fixed signature artifact (p1=3sigma).")
    print("It is NOT 3, NOT 3-primary, and NOT chi in disguise. The trapdoor opens onto the")
    print("SELECTOR (2-primary) arena: A-mechanism / B-ontology. The count is NOT forced.")
    print("=" * 78)

    return {
        "pure": int(pure), "twisted": int(tw16),
        "fills_forcing_slot": fills, "integer_is_3": integer_is_3,
    }


if __name__ == "__main__":
    main()
