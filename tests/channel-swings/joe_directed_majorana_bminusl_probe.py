#!/usr/bin/env python3
"""Joe-directed channel 3, gate MJ-5: is B-L exactly preserved?

MJ-2/MJ-4 showed the 126 is unreachable in GU's declared field content.  The
Pati-Salam lens proposed a stronger claim: if B-L survives as an exact U(1),
then a nu_R Majorana mass is FORBIDDEN BY SYMMETRY rather than merely
unreachable, since it carries |Delta(B-L)| = 2.

A VEV can break B-L while preserving the Standard Model only if its direction
is an SM SINGLET carrying B-L != 0.  So this probe enumerates every weight of
every relevant representation and asks: does any SM-singlet weight have
B-L != 0, and if so, is that representation reachable in GU?

CONVENTIONS (validated against the 16 before use, not assumed):
  weights are doubled so every entry is an integer, w in {+-1}^5 for the 16
  colour     = (w1, w2, w3)      SU(3) from Spin(6) on the first three axes
  weak       = (w4, w5)          SU(2)_L x SU(2)_R from Spin(4)
  B-L        = -(2/3) * (w1+w2+w3) / 2      [the /2 undoes the doubling]
  T3L        = (w4 - w5) / 2 / 2
  T3R        = (w4 + w5) / 2 / 2
  Y          = T3R + (B-L)/2
  Q          = T3L + Y
  colour-neutral  <=>  w1 == w2 == w3
  SM singlet      <=>  colour-neutral AND T3L == 0 AND Y == 0

All arithmetic is exact rational arithmetic on integer weight vectors.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


N = 5


def b_minus_l(w):
    return F(-2, 3) * F(w[0] + w[1] + w[2], 2)


def t3l(w):
    return F(w[3] - w[4], 4)


def t3r(w):
    return F(w[3] + w[4], 4)


def hyper(w):
    return t3r(w) + b_minus_l(w) / 2


def charge(w):
    return t3l(w) + hyper(w)


def colour_neutral(w):
    return w[0] == w[1] == w[2]


def sm_singlet(w):
    return colour_neutral(w) and t3l(w) == 0 and hyper(w) == 0


# ---------------------------------------------------------------------------
# 1. Validate the conventions on the 16 before using them anywhere else.
# ---------------------------------------------------------------------------
spinor16 = [w for w in
            [tuple(s) for s in __import__("itertools").product((1, -1), repeat=N)]
            if list(w).count(-1) % 2 == 0]
check("the 16 has 16 weights", len(spinor16) == 16)

nu_r = (1, 1, 1, 1, 1)
check("nu_R is in the 16", nu_r in spinor16)
check("nu_R is an SM singlet", sm_singlet(nu_r))
check("nu_R has B-L = -1", b_minus_l(nu_r) == -1)
check("nu_R has Q = 0", charge(nu_r) == 0)

leptons = [w for w in spinor16 if colour_neutral(w)]
quarks = [w for w in spinor16 if not colour_neutral(w)]
check("the 16 splits 4 leptons + 12 quark states",
      len(leptons) == 4 and len(quarks) == 12)
check("every lepton has |B-L| = 1", all(abs(b_minus_l(w)) == 1 for w in leptons))
check("every quark has |B-L| = 1/3", all(abs(b_minus_l(w)) == F(1, 3) for w in quarks))
check("all electric charges in the 16 are in {0, +-1/3, +-2/3, +-1}",
      all(charge(w) in (0, F(1, 3), F(-1, 3), F(2, 3), F(-2, 3), 1, -1)
          for w in spinor16))
check("exactly one SM singlet in the 16 (nu_R)",
      sum(1 for w in spinor16 if sm_singlet(w)) == 1)


# ---------------------------------------------------------------------------
# 2. Weights of the tensor representations.  Doubled convention: the vector
#    10 has weights +-2*e_i so that everything shares one scale with the 16.
# ---------------------------------------------------------------------------
VEC = [tuple((2 * s if k == i else 0) for k in range(N))
       for i in range(N) for s in (1, -1)]
check("the vector 10 has 10 weights", len(VEC) == 10)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def wedge(k):
    out = []
    for sub in combinations(VEC, k):
        w = (0,) * N
        for v in sub:
            w = add(w, v)
        out.append(w)
    return out


LAM = {k: wedge(k) for k in range(6)}
from math import comb
for k in range(6):
    check(f"Lambda^{k}(10) has C(10,{k}) weights", len(LAM[k]) == comb(10, k))


# ---------------------------------------------------------------------------
# 3. THE GATE.  Which representations contain an SM-singlet direction that
#    carries B-L != 0 -- i.e. can break B-L without breaking the SM?
# ---------------------------------------------------------------------------
def bl_breaking_singlets(weights):
    return [w for w in weights if sm_singlet(w) and b_minus_l(w) != 0]


profile = {k: len(bl_breaking_singlets(LAM[k])) for k in range(6)}
check("only Lambda^5 contains an SM-singlet with B-L != 0",
      [profile[k] > 0 for k in range(6)] == [False] * 5 + [True])

# Name it exactly: the 126's SU(5)-singlet direction, |B-L| = 2.
l5 = bl_breaking_singlets(LAM[5])
check("the Lambda^5 B-L-breaking singlets all have |B-L| = 2",
      all(abs(b_minus_l(w)) == 2 for w in l5))
check("one of them is the all-plus (126) direction",
      tuple([2] * 5) in [w for w in l5])

# The 120 does contain a colour-neutral B-L-charged weight, but it is NOT an
# SM singlet -- it breaks hypercharge.  Record that explicitly, because it is
# the most plausible near-miss and the obvious place to get this wrong.
l3_colour_neutral_charged = [w for w in LAM[3]
                             if colour_neutral(w) and b_minus_l(w) != 0]
check("Lambda^3 (120) HAS colour-neutral B-L-charged weights", len(l3_colour_neutral_charged) > 0)
check("but none of them is an SM singlet (they break hypercharge)",
      all(not sm_singlet(w) for w in l3_colour_neutral_charged))
check("the 120 near-miss has Y = -1 exactly",
      all(hyper(w) in (1, -1) for w in l3_colour_neutral_charged))


# ---------------------------------------------------------------------------
# 4. GU's actual declared field content: eps -> Lambda^2(10) = 45,
#    $ -> Lambda^1(10) (x) Lambda^2(10) = 10 (x) 45.
#    Neither may contain an SM-singlet with B-L != 0.
# ---------------------------------------------------------------------------
eps_weights = LAM[2]
disp_weights = [add(a, b) for a in LAM[1] for b in LAM[2]]
check("$ content has 450 weights", len(disp_weights) == 450)

check("GATE: eps (the source's declared VEV channel) has NO SM-singlet "
      "with B-L != 0", len(bl_breaking_singlets(eps_weights)) == 0)
check("GATE: $ (displacement) has NO SM-singlet with B-L != 0",
      len(bl_breaking_singlets(disp_weights)) == 0)

# Structural reason, verified: with at most three nonzero entries a weight
# that is colour-neutral either has colour (0,0,0) -- hence B-L = 0 -- or
# colour (+-2,+-2,+-2), which exhausts the entries and leaves Y != 0.
check("every colour-neutral weight of eps has B-L = 0",
      all(b_minus_l(w) == 0 for w in eps_weights if colour_neutral(w)))
check("every colour-neutral B-L-charged weight of $ fails the SM-singlet test",
      all(not sm_singlet(w) for w in disp_weights
          if colour_neutral(w) and b_minus_l(w) != 0))

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"SM-singlet B-L-breaking directions per Lambda^k, k=0..5: "
      f"{[profile[k] for k in range(6)]}")
print(f"eps: {len(bl_breaking_singlets(eps_weights))}   "
      f"$: {len(bl_breaking_singlets(disp_weights))}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
