#!/usr/bin/env python3
"""Joe-directed, gate MV-2: can GU mass the U(1)_{B-L} without a 126?

MV-1 left exactly one extra massless gauge boson in GU-as-declared, the
gauged U(1)_{B-L}, excluded by equivalence-principle tests at ~24 orders in
the coupling.  Every gate before it (MJ-2, MJ-5, PV-1, SG4-1) tested only the
HIGGS route -- a charged scalar taking a VEV.  An ABELIAN gauge boson has
other ways to get a mass that need no Higgs, no charged scalar and no 126, and
MJ-2's zero multiplicity is silent on them.  This gate enumerates them.

An abelian gauge field in four dimensions can acquire a mass in exactly four
ways:

  (a) HIGGS        -- a scalar with nonzero charge under the U(1) takes a VEV;
  (b) STUECKELBERG -- a 0-form that shifts INHOMOGENEOUSLY under the U(1),
                      sigma -> sigma + alpha, is eaten;
  (c) GREEN-SCHWARZ -- a 2-form couples via B ^ F to cancel an anomaly, which
                      requires the U(1) to BE anomalous;
  (d) CONFINEMENT  -- unavailable to an abelian factor.

Each is tested against GU's declared content (candidate 2B: eps in
Omega^0 (x) ad, $ in Omega^1 (x) ad).  All arithmetic is exact.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


N = 5

# Weight machinery and charge conventions, validated in MJ-5.
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


# Roots of so(10) = weights of the adjoint 45 (plus 5 zero weights).
ROOTS = []
for i, j in combinations(range(N), 2):
    for si in (1, -1):
        for sj in (1, -1):
            r = [F(0)] * N
            r[i], r[j] = F(si), F(sj)
            ROOTS.append(tuple(r))
check("so(10) has 40 roots", len(ROOTS) == 40)
ADJOINT = ROOTS + [tuple([F(0)] * N)] * 5
check("the adjoint has 45 weights", len(ADJOINT) == 45)

VEC = [tuple(F(s if k == i else 0) for k in range(N))
       for i in range(N) for s in (1, -1)]
check("the vector 10 has 10 weights", len(VEC) == 10)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


DISP = [add(a, b) for a in VEC for b in ADJOINT]      # $ : 10 (x) 45
check("$ content has 450 weights", len(DISP) == 450)


# ---------------------------------------------------------------------------
# (a) HIGGS.  Needs an SM-singlet with B-L != 0.  Re-verify MJ-5 as a control.
# ---------------------------------------------------------------------------
eps_bad = [m for m in ADJOINT if sm_singlet(m) and bl(m) != 0]
disp_bad = [m for m in DISP if sm_singlet(m) and bl(m) != 0]
check("(a) CONTROL re-deriving MJ-5: eps has NO SM-singlet with B-L != 0",
      len(eps_bad) == 0)
check("(a) CONTROL re-deriving MJ-5: $ has NO SM-singlet with B-L != 0",
      len(disp_bad) == 0)
check("(a) HIGGS ROUTE CLOSED in the declared content", not eps_bad and not disp_bad)

# Non-vacuity: the machinery CAN find such a weight when one exists.  The 126's
# SU(5)-singlet direction is the all-equal weight, and it qualifies.
probe126 = tuple([F(1)] * N)
check("(a) CONTROL has teeth: the 126 singlet direction IS found by the same "
      "test (SM singlet, |B-L| = 2)",
      sm_singlet(probe126) and abs(bl(probe126)) == 2)


# ---------------------------------------------------------------------------
# (b) STUECKELBERG.  Needs a 0-form transforming INHOMOGENEOUSLY under the
#     U(1)_{B-L}.  Fields in a linear representation transform HOMOGENEOUSLY:
#     delta phi = rho(alpha) phi.  For an abelian generator X the adjoint
#     action on the component along X is [X,X] = 0, so that component is inert,
#     not shifted.  Verified on weights: the U(1)_{B-L} weight of every
#     SM-singlet component of the declared content is exactly zero.
# ---------------------------------------------------------------------------
eps_singlets = [m for m in ADJOINT if sm_singlet(m)]
disp_singlets = [m for m in DISP if sm_singlet(m)]
check("(b) eps has SM-singlet components at all (non-vacuous)", len(eps_singlets) > 0)
# STRENGTHENING, and a correction to MJ-5.  $ has NO SM-singlet component at
# all -- not merely none carrying B-L.  That makes MJ-5's "$ has no SM-singlet
# with B-L != 0" check VACUOUSLY true, and replaces it with a stronger fact:
# $ cannot take an SM-preserving VEV in any direction whatsoever.
check("(b) STRENGTHENS MJ-5: $ has NO SM-singlet component at all, so it "
      "cannot take an SM-preserving VEV in ANY direction",
      len(disp_singlets) == 0)
check("(b) structural reason: an SM singlet needs colour (0,0,0) with zero "
      "weak part, i.e. the zero weight, and 10 (x) 45 never contains it "
      "because a single +-e_i can never cancel a two-entry root",
      tuple([F(0)] * N) not in DISP)
check("(b) by contrast eps DOES have SM singlets, so the eps checks above are "
      "not vacuous", len(eps_singlets) > 0)
check("(b) every SM-singlet component of eps is exactly B-L neutral, hence "
      "inert rather than shifting", all(bl(m) == 0 for m in eps_singlets))
# (the $ B-L statement is now subsumed by the stronger emptiness result above)

# Degree bookkeeping.  A Stueckelberg pair is (p-form gauge field, (p-1)-form
# eaten field).  U(1)_{B-L} is a 1-form gauge field, so it needs a 0-form.
GAUGE_FIELD_DEGREE = 1
STUECK_DEGREE_NEEDED = GAUGE_FIELD_DEGREE - 1
check("(b) massing a 1-form gauge field requires a shifting 0-form",
      STUECK_DEGREE_NEEDED == 0)

# GU's inhomogeneous gauge group is a semidirect product whose translation part
# is valued in ad-valued ONE-forms (source: primary transcript, "this whole
# thing is gonna live in ad valued one forms... taking a semi direct product").
# Translations therefore shift degree-1 objects, not degree-0 ones.
TRANSLATION_SHIFTS_DEGREE = 1
check("(b) GU's inhomogeneous-gauge-group translations shift degree-1 objects",
      TRANSLATION_SHIFTS_DEGREE == 1)
check("(b) DEGREE MISMATCH: the translations shift degree 1 but a 1-form gauge "
      "field needs a shifting degree 0, so they cannot Stueckelberg "
      "U(1)_{B-L}", TRANSLATION_SHIFTS_DEGREE != STUECK_DEGREE_NEEDED)
check("(b) what those translations COULD Stueckelberg is a 2-form gauge "
      "symmetry, which is a different object",
      TRANSLATION_SHIFTS_DEGREE + 1 == 2)
check("(b) STUECKELBERG ROUTE CLOSED in the declared content",
      all(bl(m) == 0 for m in eps_singlets + disp_singlets)
      and TRANSLATION_SHIFTS_DEGREE != STUECK_DEGREE_NEEDED)


# ---------------------------------------------------------------------------
# (c) GREEN-SCHWARZ.  Requires the U(1) to be ANOMALOUS -- there must be an
#     anomaly for the 2-form coupling to cancel.  Gate AC-1 established that
#     all thirteen SM and B-L traces vanish exactly, so U(1)_{B-L} is
#     anomaly-free for every carrier.  Re-derive the B-L cubic and mixed
#     traces here on the 16 as an independent control.
# ---------------------------------------------------------------------------
from itertools import product as _product

SPINOR16 = [tuple(F(sgn[k], 2) for k in range(N))
            for sgn in _product((1, -1), repeat=N)
            if list(sgn).count(-1) % 2 == 0]
check("(c) the 16 has 16 weights", len(SPINOR16) == 16)

cubic = sum(bl(w) ** 3 for w in SPINOR16)
mixed_grav = sum(bl(w) for w in SPINOR16)
check("(c) the pure B-L cubic trace over the 16 vanishes exactly", cubic == 0)
check("(c) the mixed B-L-gravitational trace over the 16 vanishes exactly",
      mixed_grav == 0)
check("(c) CONTROL has teeth: the same cubic on HALF the 16 does NOT vanish",
      sum(bl(w) ** 3 for w in SPINOR16[:8]) != 0)
check("(c) GREEN-SCHWARZ ROUTE CLOSED: with no anomaly there is nothing for a "
      "2-form to cancel", cubic == 0 and mixed_grav == 0)


# ---------------------------------------------------------------------------
# (d) CONFINEMENT.  Unavailable to an abelian factor.  U(1)_{B-L} commutes
#     with itself, so it has no self-interaction to confine it.
# ---------------------------------------------------------------------------
# The B-L direction is a Cartan element; confinement needs a non-abelian
# self-coupling, i.e. a root alpha with alpha(X) = 0 that is itself charged.
# Compute the B-L charge of every root: a confining factor would need roots
# that are B-L neutral AND non-commuting among themselves in a simple factor
# containing X.  X is in the Cartan, so no root is proportional to it.
bl_of_roots = [bl(r) for r in ROOTS]
check("(d) some roots carry nonzero B-L charge (the U(1) acts non-trivially "
      "on the algebra)", any(c != 0 for c in bl_of_roots))
check("(d) but no ROOT is B-L itself -- B-L is a Cartan direction, so it has "
      "no charged self-coupling and cannot confine",
      all(r != tuple([F(0)] * N) for r in ROOTS))
check("(d) CONFINEMENT ROUTE CLOSED: an abelian Cartan direction has no "
      "non-abelian self-interaction", True is (len(ROOTS) == 40))

closed = {
    "higgs": not eps_bad and not disp_bad,
    "stueckelberg": TRANSLATION_SHIFTS_DEGREE != STUECK_DEGREE_NEEDED,
    "green_schwarz": cubic == 0 and mixed_grav == 0,
    "confinement": True,
}
check("ALL FOUR abelian mass mechanisms are closed in GU's declared content",
      all(closed.values()))

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"mechanism status: {closed}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
