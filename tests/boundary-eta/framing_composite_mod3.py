#!/usr/bin/env python3
r"""M-M9 framing-composite mod-3 decision certificate (audit HB-02 / B6).

THE PROBLEM THIS DECIDES.  The eleven-lens audit (lab/process/
eleven-lens-audit-2026-08-03.md, B6) found that the carrier derivation
conflates two DIFFERENT p1 = 4's:

  (1) the Kirby-Melvin relative Pontrjagin number p1(W, phi_nat) = 4 of the
      NATURAL framing of RP^3 = L(2;1) = SO(3), W the Euler +2 disk bundle
      over S^2 -- a class-of-a-framed-manifold datum; and
  (2) p1(ad P) = -4 c2(P), |p1| = 4, of the charge-1 adjoint clutching --
      a CHANGE-OF-FRAMING degree (stable degree |p1|/2 = 2 via the x2
      stabilization pi_3(SO(3)) -> pi_3(SO)).

Under the twist-on-top-of-the-natural-framing reading the honest object is
the COMPOSITE class

    c = n + t = (natural-framing class) + (change-of-framing degree)
      = (+-2) + (+-2) in Z/24,

which is 0 or +-4 depending on ONE relative sign -- the {0,4} ambiguity of
audit finding B6.  This certificate computes both branches exactly, reduces
them mod 3, proves the arithmetic side of the H^1(RP^3;Z/2) framing-shift
lemma (shifts are strictly 2-primary, so the 3-part of any framing change
is its degree mod 3), and pins the branch selection to a single named
convention datum:

    epsilon = (sign of the natural-framing class) x (sign of the twist
    degree), i.e. whether the charge-1 adjoint clutching is SELF-dual or
    ANTI-self-dual with respect to the same orientation of the spine for
    which the Kirby-Melvin natural framing is the right-handed (h = +1)
    Lie framing.

    epsilon = +1  ==>  composite +-4, 3-part NONZERO  (mod 3 in {1,2})
    epsilon = -1  ==>  composite   0, 3-part ZERO     (mod 3 = 0)

WHAT THIS DOES NOT DO.  It does NOT assert which branch is GU's.  That is
the declared reconstruction-grade premise of the V15-5 certificate
(tests/boundary-eta/v15_framing_convention_sensitivity.py: "Lambda^2_+ is
identified with this exact tangential framing") and of
canon/boundary-einvariant-and-the-tangential-fork.md.  The deliverable is
the DECISION STRUCTURE: the {0,4} set is not a free ambiguity of the
mathematics; it is the two fibers of one binary convention datum.

CONVENTIONS (fixed once, declared):
  C1 orientation: RP^3 = boundary of the Euler +2 disk bundle X_2 over S^2,
     with the boundary orientation (per the canon fork file and V15-5).
  C2 generator labels: e_R(nu) = +1/24 (Adams), class(nu) = +1 in Z/24.
  C3 natural framing: Kirby-Melvin right-handed Lie framing phi_+ on
     SO(3) = L(2;1) (quotient of the right-handed Hopf/Lie framing on S^3),
     Hirzebruch defect h(phi_+) = 3 - m = 1 at m = 2, hence
     p1(X_2, phi_+) = h + 3 sigma(X_2) = 1 + 3 = 4.
     [Kirby-Melvin, "Canonical framings for 3-manifolds", Turk. J. Math 23
     (1999): H(SO_3, phi_{+-}) = (0, +-1); h = p1(W,psi) - 3 sigma(W);
     action p1(W, psi + alpha) = p1 + 4.]
  C4 twist: charge-1 adjoint clutching, p1(ad P) = -4 c2(P), |p1| = 4,
     stable degree |p1|/2 = 2 (x2 stabilization); its SIGN is the
     self-dual / anti-self-dual choice relative to C1 -- the branch picker.
  C5 action convention: composite = class(natural) + degree(twist)
     (framing acted on the right; an inverse convention flips C4's sign and
     must be co-declared with it).

E-INVARIANT FORMULA USED (with its hypothesis made explicit): for a framed
(M^3, psi) = boundary of a compact SPIN W^4 with psi spin-compatible,
e_R[M, psi] = s * p1(W, psi)/48 with a single global sign s fixed by C2
(canon cites Randal-Williams for the formula; audit items B7/P-H26 track
the missing bibliography entry and the W-spin hypothesis for the v1.0.1
correction batch -- this file STATES the hypothesis and CHECKS it).
The formula is well-defined across spin fillings because a closed spin
4-manifold has p1 = 3 sigma with sigma = 0 mod 16 (Rokhlin), so p1 = 0
mod 48; a non-spin filling breaks it (CP^2: p1 = 3), demonstrated below.

HONESTY GUARD.  For RP^3 the exact 2-primary part of the natural-framing
class is NOT pinned (canon fork file section 5, item 3).  Every assert
about RP^3 classes below is therefore either (a) a formula-output statement
labeled with its hypothesis, or (b) a mod-3 statement, which is immune to
2-primary corrections by the framing-shift lemma proven here plus the
rho-invariant immunity lemma (explorations/
rho-invariant-two-primary-immunity-lemma-2026-08-03.md).

Positive controls run FIRST.  Exact integer / Fraction arithmetic only;
standard library only; exits nonzero on any failure.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from math import comb, gcd

MOD = 24  # |pi_3^s| = |Im J_3| = denom(B_2/4)

_CHECKS = 0


def check(cond: bool, msg: str) -> None:
    global _CHECKS
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)
    _CHECKS += 1
    print("  ok  " + msg)


def banner(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def three_part(x: int) -> int:
    """Z/3 CRT coordinate of a class in Z/24."""
    return x % 3


def two_torsion_subgroup(mod: int) -> set[int]:
    """Elements killed by 2 in Z/mod."""
    return {x for x in range(mod) if (2 * x) % mod == 0}


# ===========================================================================
banner("PART 0  --  positive controls: Z/24 arithmetic")
# ===========================================================================

# pi_3^s = Z/24 from the Adams/Bernoulli anchor (firewall: the only 24)
B = [Fraction(0)] * 3
B[0] = Fraction(1)
for k in range(1, 3):
    B[k] = -sum(comb(k + 1, j) * B[j] for j in range(k)) / (k + 1)
check(B[2] == Fraction(1, 6), "B_2 = 1/6 (exact recurrence)")
check((B[2] / 4).denominator == MOD, "|Im J_3| = denom(B_2/4) = 24")

crt = {a: (a % 8, a % 3) for a in range(MOD)}
check(len(set(crt.values())) == MOD, "n -> (n mod 8, n mod 3) is a bijection (CRT)")

tors2 = two_torsion_subgroup(MOD)
check(tors2 == {0, 12}, "2-torsion of Z/24 is {0, 12}")
check(all(three_part(t) == 0 for t in tors2),
      "every 2-torsion element of Z/24 has ZERO Z/3-part")

nonzero3 = [x for x in range(MOD) if three_part(x) != 0]
check(len(nonzero3) == 16,
      "16 of 24 classes have nonzero 3-part (so 'nonzero 3-part' is generic, "
      "not automatic: the lemma below is load-bearing)")

# ===========================================================================
banner("PART 1  --  positive controls: p1 = 3 sigma, Rokhlin, and the S^3 chain")
# ===========================================================================

# closed-manifold normalization controls for (p1, sigma)
closed_manifolds = {          # name: (p1, sigma, spin?)
    "S^4": (0, 0, True),
    "CP^2": (3, 1, False),
    "K3": (-48, -16, True),
}
for name, (p1, sig, spin) in closed_manifolds.items():
    check(p1 == 3 * sig, "closed %s: p1 = 3 sigma  (%d = 3*%d)" % (name, p1, sig))
    if spin:
        check(sig % 16 == 0, "closed spin %s: sigma = 0 mod 16 (Rokhlin)" % name)
        check(p1 % 48 == 0,
              "closed spin %s: p1 = 0 mod 48 -- e_R = s*p1/48 is well-defined "
              "across SPIN fillings" % name)
check(closed_manifolds["CP^2"][0] % 48 == 3,
      "closed NON-spin CP^2: p1 = 3 not in 48Z -- the formula's W-spin "
      "hypothesis is load-bearing (audit B7/P-H26)")

# S^3 Lie-framing anchor: W = B^4 (spin, sigma = 0), p1(B^4, phi_+) = 2 (KM)
p1_B4_lie = 2
eR_lie = Fraction(p1_B4_lie, 48)
check(eR_lie == Fraction(1, 24), "S^3 Lie framing: e_R = p1/48 = 2/48 = 1/24 = e_R(nu)")
check((p1_B4_lie // 2) % MOD == 1, "S^3 Lie framing: class p1/2 = 1 = [nu] in Z/24")

# KM action control: alpha (generator of pi_3(SO(3))) has p1-shift 4, class-shift 2
for k in range(-6, 7):
    p1_shifted = p1_B4_lie + 4 * k
    cls = (p1_shifted // 2) % MOD
    check_needed = (1 + 2 * k) % MOD
    assert cls == check_needed, (k, cls, check_needed)
check(True, "KM Lemma 2.3a sweep k=-6..6: p1 += 4k  <=>  class += 2k "
            "(adding alpha^k; the x2 stabilization in p1/2 form)")

# stabilization control: pi_3(SO(3)) -> pi_3(SO) is x2; p1/2 is the stable degree
p1_adjoint_charge1 = 4          # |p1(ad P)| = |-4 c2| = 4 at charge 1
stable_degree = p1_adjoint_charge1 // 2
check(stable_degree == 2,
      "charge-1 adjoint clutching: |p1(ad P)| = 4  ==>  stable degree p1/2 = 2 "
      "(x2 stabilization; NOT Dynkin index 4, NOT dimension 3)")

# misapplication control: the NON-spin Euler +1 filling of S^3 (CP^2 minus ball)
p1_rel_cp2_minus_ball = 3       # p1(CP^2) - p1(B^4, psi_0) = 3 - 0
bad = Fraction(p1_rel_cp2_minus_ball, 48)
check((MOD * bad).denominator != 1,
      "NON-spin filling of S^3: p1/48 = 3/48 = 1/16 is not a Z/24 class "
      "(24 * 1/16 = 3/2 not integral) -- misapplication is machine-detectable")
check(Fraction(0) != bad, "and it disagrees with the true class 0 of (S^3, psi_0)")

# ===========================================================================
banner("PART 2  --  Kirby-Melvin natural framing of RP^3 = L(2;1) = SO(3)")
# ===========================================================================

m = 2                            # L(2;1)
h_natural = 3 - m                # KM: h(L(m,1), phi_+) = 3 - m
check(h_natural == 1, "KM: Hirzebruch defect h(L(2;1), phi_+) = 3 - m = 1")

sigma_X2 = 1                     # Euler +2 disk bundle over S^2: form (+2)
euler_number = 2
check(euler_number % 2 == 0 and euler_number % 2 == 0,
      "X_2 spin check: w2(X_2) = e mod 2 = 0 (Euler number 2 even) -- "
      "the W-spin hypothesis HOLDS for this filling")
p1_X2_natural = h_natural + 3 * sigma_X2
check(p1_X2_natural == 4,
      "p1(X_2, phi_nat) = h + 3 sigma = 1 + 3 = 4  (the FIRST p1=4: a "
      "class-of-a-framed-manifold datum)")
check(p1_adjoint_charge1 == 4,
      "p1(ad P) magnitude = 4 (the SECOND p1=4: a change-of-framing degree). "
      "Same numeral, different object -- the audit-B6 conflation target")

# natural-framing class via the (spin-hypothesis) formula, both label signs
natural_class = {}
for s1 in (+1, -1):
    e_nat = Fraction(s1 * p1_X2_natural, 48)
    check(abs(e_nat) == Fraction(1, 12),
          "s1=%+d: e_R(RP^3, phi_nat) = s1*p1/48 = %s" % (s1, e_nat))
    n = (s1 * p1_X2_natural // 2) % MOD
    natural_class[s1] = n
    check(n in (2, 22), "s1=%+d: natural-framing class n = %d in Z/24 (i.e. %+d)"
          % (s1, n, s1 * 2))
    check(three_part(n) != 0,
          "s1=%+d: 3-part of n is %d != 0 (the V15-5 identification-premise "
          "reading: NONZERO for both label signs)" % (s1, three_part(n)))
print("  NOTE: only the mod-3 statements about RP^3 classes are convention-robust;")
print("        the exact 2-primary part is unpinned (canon fork file sec. 5 item 3).")

# ===========================================================================
banner("PART 3  --  the H^1(RP^3;Z/2) framing-shift lemma (arithmetic side)")
# ===========================================================================

# Lemma (proved in explorations/framing-composite-mod3-2026-08-03.md):
# a framing change g: M -> SO changes the framed class by  d(g)*nu + t  with
# t killed by 2 (the sub-top-cell contributions factor through composition
# with eta = J(pi_1 SO), and 2*eta = 0).  Arithmetic content certified here:
eta_cubed = 12                   # eta^3 = 12 nu in Z/24 (2-locally 4 nu)
check(crt[eta_cubed] == (4, 0),
      "eta^3 = 12 nu has CRT (4, 0): 2-locally 4 nu, Z/3-part ZERO")
check(eta_cubed in tors2, "eta^3 is 2-torsion (2 eta = 0)")

for d in range(-MOD, MOD + 1):
    for t in tors2:
        shifted = (d + t) % MOD
        assert three_part(shifted) == d % 3, (d, t)
check(True,
      "exhaustive d in -24..24, t in {0,12}: 3-part(d*nu + t) = d mod 3 -- "
      "the 3-part of ANY framing change is its degree mod 3")
check(all(three_part((n + t) % MOD) == three_part(n)
          for n in range(MOD) for t in tors2),
      "no H^1(RP^3;Z/2) shift (image in {0,12}) can create or erase a 3-part")

# ===========================================================================
banner("PART 4  --  the composite, both relative signs: the decision structure")
# ===========================================================================

print("  composite c = n + t,  n = s1*2 (natural framing),  t = s2*2 (twist)")
print()
results = {}
for s1 in (+1, -1):
    for s2 in (+1, -1):
        n = (s1 * 2) % MOD
        t = (s2 * 2) % MOD
        c = (n + t) % MOD
        eps = s1 * s2
        results[(s1, s2)] = (c, eps)
        print("    s1=%+d s2=%+d  eps=%+d :  c = %2d in Z/24,  c mod 3 = %d  (%s)"
              % (s1, s2, eps, c, three_part(c),
                 "ZERO 3-part" if three_part(c) == 0 else "NONZERO 3-part"))
print()

for (s1, s2), (c, eps) in results.items():
    if eps == +1:
        assert c in (4, 20), (s1, s2, c)
        assert three_part(c) in (1, 2), (s1, s2, c)
    else:
        assert c == 0, (s1, s2, c)
        assert three_part(c) == 0, (s1, s2, c)
check(True,
      "eps = +1  ==>  c = +-4 (i.e. 4 or 20), 3-part in {1,2} NONZERO;  "
      "eps = -1  ==>  c = 0, 3-part ZERO -- audit B6's {0,4} is the two "
      "eps-fibers, not a free ambiguity")

# label-independence: global orientation / generator relabeling flips (s1,s2)
# together, preserving eps and the zero/nonzero-3-part decision
for s1 in (+1, -1):
    for s2 in (+1, -1):
        c, eps = results[(s1, s2)]
        c_flip, eps_flip = results[(-s1, -s2)]
        assert eps == eps_flip, (s1, s2)
        assert (three_part(c) == 0) == (three_part(c_flip) == 0), (s1, s2)
check(True,
      "C1/C2 relabelings flip (s1, s2) together: eps and the zero/nonzero "
      "decision are INVARIANT -- eps is a genuine binary about the "
      "construction, not a bookkeeping artifact")

# V15-5 cross-check: in V15-5's coordinates (base object = the twist, d = 2),
# the composite reading enters as a framing shift k = n; V15-5's own rule is
# 'P3 vanishes iff k = 1 mod 3'
for s1 in (+1, -1):
    n_signed = s1 * 2
    composite_zero = (2 + n_signed) % MOD == 0
    v15_erases = (n_signed % 3) == 1
    assert composite_zero == v15_erases, s1
check(True,
      "V15-5 cross-check: composite = 0 exactly when the natural framing "
      "enters as a shift k = -2 = 1 mod 3 -- matching V15-5's erasure rule "
      "'k = 1 mod 3'")

# ===========================================================================
banner("PART 5  --  decision statement (no branch asserted)")
# ===========================================================================

print("""
DECIDED: the {0,4} composite-framing ambiguity (audit HB-02/B6) is the
two fibers of ONE binary convention datum,

    eps = (sign of the KM natural-framing class of RP^3)
        x (sign of the charge-1 adjoint change-of-framing degree),

which is fixed by naming, in the SAME orientation of the spine (C1):
  (a) the Kirby-Melvin right-handed natural framing datum
      (h(X_2, phi_+) = +1, p1(X_2, phi_+) = +4), and
  (b) whether the GU charge-1 twist is SELF-dual or ANTI-self-dual with
      respect to that orientation (the +- in Lambda^2_{+-}), under the
      declared composition convention (C5).

  eps = +1 : composite class +-4, 3-part NONZERO (mod 3 in {1,2}).
  eps = -1 : composite class   0, 3-part ZERO.

NOT DECIDED HERE: which value of eps -- equivalently which reading
(identification vs composite) -- the GU construction instantiates.  That is
the declared reconstruction-grade premise of the V15-5 certificate
("Lambda^2_+ is identified with this exact tangential framing") and of
canon/boundary-einvariant-and-the-tangential-fork.md.  Under the V15-5
identification premise the object is the natural framing itself and the
3-part is nonzero for BOTH label signs (Part 2).  This certificate asserts
no GU branch.
""")

check(True, "no GU branch asserted (decision structure only)")

print("-" * 78)
print("ALL CHECKS PASSED: %d assertions" % _CHECKS)
print("VERDICT: DECISION_STRUCTURE_FIXED__BRANCH_PICKED_BY_NAMED_CONVENTION_DATUM")
print("-" * 78)
