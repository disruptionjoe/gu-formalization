#!/usr/bin/env python3
"""Joe-directed channel 3, gate SG4-1: what must SG4 declare?

Everything this session established is about GU-AS-DECLARED, and canon makes
SG4 -- the source action's field-space declaration -- the open decider.  BD-1
observed that ONE object (the 126) would simultaneously supply a B-L-charged
SM singlet, give the nine surviving gauge bosons mass, and restore
baryogenesis.  This gate turns that observation into an EXHAUSTIVE constraint:
which representations could do it at all?

THE STRUCTURAL REDUCTION (derived below, not assumed).  A weight mu is an SM
singlet with B-L != 0 iff ALL FIVE of its components are equal and nonzero:

    mu = (c,c,c,c,c),  c != 0.

Proof sketch, verified by brute force in the probe: colour-neutrality forces
mu1=mu2=mu3=a; T3L=0 forces mu4=mu5=b; then B-L=-2a and T3R=b, so Y=b-a, and
Y=0 forces b=a.  Equivalently: such a weight is an SU(5) singlet (orthogonal
to every SU(5) root e_i - e_j) carrying nonzero U(1)_X charge.

THE ENUMERATION.  For simply-laced D5, a dominant weight mu is a weight of the
irrep V_lambda iff mu <= lambda in the dominance order AND lambda - mu lies in
the root lattice.  Both are exact integer/rational tests, so the sweep over all
irreps below a dimension bound is exhaustive rather than sampled.  No
Freudenthal recursion is needed.

All arithmetic is exact rational arithmetic (Fraction).  No floating point.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


N = 5
RHO = tuple(F(x) for x in (4, 3, 2, 1, 0))

POS_ROOTS = []
for i, j in combinations(range(N), 2):
    for s in (1, -1):
        r = [0] * N
        r[i], r[j] = 1, s
        POS_ROOTS.append(tuple(F(x) for x in r))
check("D5 has 20 positive roots", len(POS_ROOTS) == 20)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def weyl_dim(lam):
    num = den = F(1)
    lr = tuple(x + y for x, y in zip(lam, RHO))
    for a in POS_ROOTS:
        num *= dot(lr, a)
        den *= dot(RHO, a)
    return num / den


# Controls: the Weyl formula must reproduce known SO(10) dimensions.
KNOWN = {
    (0, 0, 0, 0, 0): 1,
    (1, 0, 0, 0, 0): 10,
    (F(1, 2),) * 5: 16,
    (1, 1, 0, 0, 0): 45,
    (2, 0, 0, 0, 0): 54,
    (1, 1, 1, 0, 0): 120,
    (1, 1, 1, 1, 1): 126,
    (1, 1, 1, 1, -1): 126,
    (1, 1, 1, 1, 0): 210,
    (2, 1, 0, 0, 0): 320,
}
for lam, d in KNOWN.items():
    lam = tuple(F(x) for x in lam)
    check(f"Weyl dimension of {tuple(str(x) for x in lam)} is {d}",
          weyl_dim(lam) == d)


# ---------------------------------------------------------------------------
# 1. The structural reduction, verified by brute force over a weight box.
# ---------------------------------------------------------------------------
def bl(m):
    return F(-2, 3) * (m[0] + m[1] + m[2])


def t3l(m):
    return (m[3] - m[4]) / 2


def t3r(m):
    return (m[3] + m[4]) / 2


def hyper(m):
    return t3r(m) + bl(m) / 2


def sm_singlet(m):
    return m[0] == m[1] == m[2] and t3l(m) == 0 and hyper(m) == 0


# Sweep all half-integer weights in a box and confirm the characterisation.
box = [F(k, 2) for k in range(-4, 5)]
viol = 0
hits = 0
for a in box:
    for b in box:
        for c in box:
            for d in box:
                for e in box:
                    m = (a, b, c, d, e)
                    if sm_singlet(m) and bl(m) != 0:
                        hits += 1
                        if not (a == b == c == d == e and a != 0):
                            viol += 1
check("every SM singlet with B-L != 0 in the sweep has all five components "
      "equal and nonzero", viol == 0)
check("the sweep actually found such weights (non-vacuous)", hits > 0)
# Converse: all-equal-nonzero really is an SM singlet with B-L != 0.
conv = all(sm_singlet((c,) * 5) and bl((c,) * 5) != 0
           for c in box if c != 0)
check("conversely every all-equal-nonzero weight IS such a singlet", conv)
# Control with teeth: all-equal-ZERO is a singlet but carries B-L = 0.
check("CONTROL: the all-zero weight is an SM singlet but has B-L = 0, so the "
      "nonzero condition is doing real work",
      sm_singlet((F(0),) * 5) and bl((F(0),) * 5) == 0)


# ---------------------------------------------------------------------------
# 2. Dominance test.  lambda - mu = sum c_i alpha_i with c_i >= 0 integers.
#    Simple roots: a1..a4 = e_i - e_{i+1}, a5 = e4 + e5.  Closed form:
#      c1 = v1, c2 = v1+v2, c3 = v1+v2+v3,
#      c5 = (v1+v2+v3+v4+v5)/2, c4 = (v1+v2+v3+v4-v5)/2
# ---------------------------------------------------------------------------
def in_root_cone(lam, mu):
    v = [x - y for x, y in zip(lam, mu)]
    c1 = v[0]
    c2 = v[0] + v[1]
    c3 = v[0] + v[1] + v[2]
    s = v[0] + v[1] + v[2] + v[3]
    c5 = (s + v[4]) / 2
    c4 = (s - v[4]) / 2
    cs = [c1, c2, c3, c4, c5]
    return all(x >= 0 and x.denominator == 1 for x in cs)


# Controls for the dominance machinery.
check("CONTROL: (1,1,1,1,1) is reachable from itself", in_root_cone((F(1),) * 5, (F(1),) * 5))
check("CONTROL: (1,1,1,1,1) is NOT a weight of the adjoint 45",
      not in_root_cone(tuple(F(x) for x in (1, 1, 0, 0, 0)), (F(1),) * 5))
check("CONTROL: the 16's own singlet weight is reachable in the 16",
      in_root_cone((F(1, 2),) * 5, (F(1, 2),) * 5))


# ---------------------------------------------------------------------------
# 3. EXHAUSTIVE SWEEP: every SO(10) irrep with dim <= BOUND, asking whether it
#    contains an SM singlet with B-L != 0.
# ---------------------------------------------------------------------------
BOUND = 2000
qualifying = []
all_reps = []

steps = [F(k, 2) for k in range(0, 9)]      # lambda_1 up to 4
for l1 in steps:
    for l2 in steps:
        if l2 > l1:
            continue
        for l3 in steps:
            if l3 > l2:
                continue
            for l4 in steps:
                if l4 > l3:
                    continue
                for l5s in set([l4, -l4] if l4 != 0 else [F(0)]):
                    lam = (l1, l2, l3, l4, l5s)
                    # integrality: all integer or all half-integer
                    dens = {x.denominator for x in lam}
                    if dens not in ({1}, {2}, {1, 2}):
                        continue
                    halves = [x for x in lam if x.denominator == 2]
                    if halves and len(halves) != N:
                        continue
                    d = weyl_dim(lam)
                    if d > BOUND or d.denominator != 1:
                        continue
                    all_reps.append((int(d), lam))
                    # does it contain an all-equal nonzero weight?
                    found = None
                    cc = l1
                    k = 0
                    while True:
                        cand = cc - F(k, 2)
                        if cand <= 0:
                            break
                        mu = (cand,) * 5
                        if in_root_cone(lam, mu):
                            found = cand
                            break
                        k += 1
                    if found is not None:
                        qualifying.append((int(d), lam, found))

check("the exhaustive sweep examined a non-trivial number of irreps",
      len(all_reps) >= 20)

qualifying.sort()
dims = sorted({d for d, _, _ in qualifying})

check("GATE: the 16 qualifies", 16 in dims)
check("GATE: the 126 qualifies", 126 in dims)
check("GATE: the two SMALLEST qualifying representations are the 16 and the "
      "126", dims[:2] == [16, 126])

# Nothing smaller can do it.
smaller = [d for d, _, _ in qualifying if d < 16]
check("GATE: NO representation below dimension 16 can break B-L while "
      "preserving the SM", smaller == [])

# The adjoint and the whole even wedge tower must be excluded (MJ-5 agreement).
excluded = {45, 10, 120, 210, 54, 1}
check("agreement with MJ-5: the 45, 10, 120, 210, 54 and singlet all fail",
      all(d not in dims for d in excluded))

# Everything qualifying carries the right charge.
check("every qualifying representation's singlet has |B-L| = 2c != 0",
      all(bl((c,) * 5) != 0 for _, _, c in qualifying))
check("the 16's singlet has |B-L| = 1 and the 126's has |B-L| = 2",
      any(d == 16 and abs(bl((c,) * 5)) == 1 for d, _, c in qualifying)
      and any(d == 126 and abs(bl((c,) * 5)) == 2 for d, _, c in qualifying))

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"\nirreps swept with dim <= {BOUND}: {len(all_reps)}")
print("representations that can break B-L while preserving the SM:")
seen = set()
for d, lam, c in qualifying:
    if d in seen:
        continue
    seen.add(d)
    print(f"   dim {d:>5}   highest weight {tuple(str(x) for x in lam)}"
          f"   singlet at c = {c}   |B-L| = {abs(bl((c,)*5))}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
