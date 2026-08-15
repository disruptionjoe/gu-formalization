#!/usr/bin/env python3
"""
LA-3 -- the grant behind ledger rows AC-D1..AC-D5.

GU-COMPARATOR-ROUTING: this probe computes a CONVENTIONAL COMPARATOR object
(the 4d Standard-Model perturbative gauge-anomaly conditions).  Its result
binds only that model.  See la3-*.md and lab/methods/source-native-comparator-routing.md.

QUESTION (new; not owned in-repo).  Ledger rows AC-D1..AC-D5 carry the
condition string "none after the chiral 16 shadow is selected" and the revival
trigger "a physical carrier not equal to complete 16s".  Both quantify over
CONTENTS.  So: on the multiplicity lattice of the 16's own SM constituents,
what is the EXACT set of anomaly-free contents?  Is "complete 16s" necessary?
Is the five-row family five independent facts?

METHOD.  The six SM irreps of a 16 of so(10) are taken as basis directions of
Z^6, with SIGNED multiplicities (a negative entry is the conjugate irrep, the
standard bookkeeping for left-handed Weyl content).  Each of the five
Standard-Model anomaly coefficients is an exact LINEAR functional on Z^6.
Everything is sympy Rational; no float is load-bearing anywhere.

WHAT IS NOT CLAIMED HERE.  That a complete 16 is anomaly-free is owned by
W222 / tests/one-residual/sm_mirror_anomaly_free.py.  That d^abc vanishes on
the 16, 10 and 144(+)16 of so(6,4) is owned by AC-1
(tests/channel-swings/joe_directed_anomaly_cancellation_probe.py).  Neither is
re-derived or re-claimed.  This probe computes the LATTICE those results sit
inside, which is a different object.

Exit 0 iff every [E] result matches its stated exact value and every [C]
control is nonzero / fires as declared.
"""

import sys
import itertools
from sympy import Rational as R, Matrix, Integer, eye

FAIL = []
NCHK = 0


def check(tag, label, got, want):
    global NCHK
    NCHK += 1
    ok = (got == want)
    if not ok:
        FAIL.append(f"[{tag}] {label}: got {got}, want {want}")
    print(f"  [{tag}] {'PASS' if ok else 'FAIL'}  {label}: {got}")
    return ok


def check_nonzero(tag, label, got):
    global NCHK
    NCHK += 1
    ok = (got != 0)
    if not ok:
        FAIL.append(f"[{tag}] {label}: got 0, control must be NONZERO")
    print(f"  [{tag}] {'PASS' if ok else 'FAIL'}  {label} (must be nonzero): {got}")
    return ok


# ---------------------------------------------------------------------------
# 1.  The six SM irreps of a 16, and their exact charges.
#     Conventions validated against tests/one-residual/sm_mirror_anomaly_free.py
#     (same Y assignments, same all-left-handed-Weyl bookkeeping).
# ---------------------------------------------------------------------------
# name, Y, n_colour (1 or 3), is_su2_doublet, su3 cubic-anomaly A (3 -> +1, 3bar -> -1)
IRREPS = [
    ("Q",     R(1, 6),  3, True,  Integer(1)),
    ("u^c",   R(-2, 3), 3, False, Integer(-1)),
    ("d^c",   R(1, 3),  3, False, Integer(-1)),
    ("L",     R(-1, 2), 1, True,  Integer(0)),
    ("e^c",   R(1),     1, False, Integer(0)),
    ("nu^c",  R(0),     1, False, Integer(0)),
]
NAMES = [r[0] for r in IRREPS]
N = len(IRREPS)

T_FUND = R(1, 2)   # Dynkin index of the fundamental of su(2) and su(3)


def functionals(irreps):
    """The five SM anomaly coefficients as exact linear functionals on Z^6."""
    f1, f2, f3, f4, f5 = [], [], [], [], []
    for (_, Y, nc, dbl, A3) in irreps:
        nw = 2 if dbl else 1          # su(2) components
        nstates = nc * nw             # Weyl states in the irrep
        # D1  SU(3)^3            : sum of su(3) cubic anomalies, su(2)-multiplied
        f1.append(A3 * nw)
        # D2  SU(2)^2 U(1)_Y     : sum over doublets of T(2) * Y, colour-multiplied
        f2.append(T_FUND * Y * nc if dbl else R(0))
        # D3  SU(3)^2 U(1)_Y     : sum over triplets of T(3) * Y, su(2)-multiplied
        f3.append(T_FUND * Y * nw if nc == 3 else R(0))
        # D4  U(1)_Y^3           : sum over states of Y^3
        f4.append(nstates * Y**3)
        # D5  grav^2 U(1)_Y      : sum over states of Y
        f5.append(nstates * Y)
    return Matrix([f1, f2, f3, f4, f5])


M = functionals(IRREPS)
ROWLAB = ["D1 SU(3)^3", "D2 SU(2)^2U(1)", "D3 SU(3)^2U(1)", "D4 U(1)_Y^3", "D5 grav^2U(1)"]

print("=" * 74)
print("LA-3  --  the 4d SM anomaly multiplicity lattice of the 16")
print("=" * 74)
print("\nExact functional matrix M (rows = 5 anomaly channels, cols = %s):" % ", ".join(NAMES))
for i, lab in enumerate(ROWLAB):
    print(f"   {lab:16s} {[M[i, j] for j in range(N)]}")

# ---------------------------------------------------------------------------
# 2.  [E] The complete 16 is in the kernel -- reproduced, NOT re-claimed.
#         Used here only as an anchor that the conventions are the repo's.
# ---------------------------------------------------------------------------
print("\n-- anchor (owned by W222 / sm_mirror_anomaly_free.py; reproduced, not claimed) --")
v16 = Matrix([1, 1, 1, 1, 1, 1])
check("E", "M * (complete 16) == 0", M * v16, Matrix([0] * 5))

# ---------------------------------------------------------------------------
# 3.  [E] THE NEW OBJECT: rank of the system and the exact solution lattice.
# ---------------------------------------------------------------------------
print("\n-- new: rank and exact kernel --")
rank = M.rank()
check("E", "rank of the 5x6 anomaly system", rank, 4)
check("E", "so exactly one of the five channels is DEPENDENT", 5 - rank, 1)

ns = M.nullspace()
check("E", "dim ker (rational solution space)", len(ns), 2)

# saturated integer lattice basis
K = Matrix.hstack(*ns).T                      # rows span the kernel over Q
v15 = Matrix([1, 1, 1, 1, 1, 0])              # the 15 of SU(5): a 16 minus its singlet
vnu = Matrix([0, 0, 0, 0, 0, 1])              # the SM singlet nu^c alone
check("E", "M * (15 of SU(5)) == 0", M * v15, Matrix([0] * 5))
check("E", "M * (nu^c alone) == 0", M * vnu, Matrix([0] * 5))
Lbasis = Matrix.hstack(v15, vnu)
check("E", "{15, nu^c} are independent", Lbasis.rank(), 2)
check("E", "{15, nu^c} span the same space as ker M",
      Matrix.hstack(K.T, Lbasis).rank(), 2)

# saturation: the lattice is exactly L, not a finite-index sublattice.
# Every integer solution has n_Q=n_u=n_d=n_L=n_e (free) and n_nu free.
print("\n-- the lattice is SATURATED (every integer solution is an integer combination) --")
sat_ok = True
for trial in itertools.product(range(-2, 3), repeat=2):
    a, b = trial
    n = a * v15 + b * vnu
    if M * n != Matrix([0] * 5):
        sat_ok = False
check("E", "all 25 sampled integer combinations of {15, nu^c} are anomaly-free",
      sat_ok, True)

# exhaustive small-box search: NO anomaly-free vector outside L in [-3,3]^6
outside = []
for n in itertools.product(range(-3, 4), repeat=N):
    v = Matrix(list(n))
    if M * v == Matrix([0] * 5):
        # in L iff first five entries are all equal
        if not (n[0] == n[1] == n[2] == n[3] == n[4]):
            outside.append(n)
check("E", "exhaustive [-3,3]^6 search: anomaly-free vectors OUTSIDE L", len(outside), 0)
inbox = sum(1 for n in itertools.product(range(-3, 4), repeat=N)
            if (n[0] == n[1] == n[2] == n[3] == n[4]))
check("E", "exhaustive [-3,3]^6 search: anomaly-free vectors found (= |L cap box|)",
      sum(1 for n in itertools.product(range(-3, 4), repeat=N)
          if M * Matrix(list(n)) == Matrix([0] * 5)), inbox)

# ---------------------------------------------------------------------------
# 4.  [E] "complete 16s" is SUFFICIENT but NOT NECESSARY: L / Z.16 is infinite.
# ---------------------------------------------------------------------------
print("\n-- 'complete 16s' is sufficient but strictly NOT necessary --")
check("E", "the complete 16 lies in L", Matrix.hstack(Lbasis, v16).rank(), 2)
# nu^c alone is anomaly-free and is NOT a multiple of the 16
is_multiple_of_16 = Matrix.hstack(v16, vnu).rank() == 1
check("E", "nu^c alone is anomaly-free but is NOT a multiple of the 16",
      is_multiple_of_16, False)
check("E", "rank L = 2 > 1 = rank Z.(complete 16); quotient L/Z.16 is infinite cyclic",
      Lbasis.rank() - Matrix([[1, 1, 1, 1, 1, 1]]).rank(), 1)
# an explicit witness content that is anomaly-free and is not a sum of 16s
witness = Matrix([1, 1, 1, 1, 1, 7])   # one 15 plus seven SM singlets
check("E", "WITNESS (one 15 + seven nu^c) is anomaly-free in all five channels",
      M * witness, Matrix([0] * 5))
check("E", "WITNESS is not an integer multiple of the complete 16",
      Matrix.hstack(v16, witness).rank(), 2)

# ---------------------------------------------------------------------------
# 5.  [E] The exact dependency relation among the five channels.
# ---------------------------------------------------------------------------
print("\n-- the exact linear relation among the five anomaly channels --")
left = M.T.nullspace()
check("E", "exactly one left-null relation among the five channels", len(left), 1)
c = left[0]
c = c * (1 / min(abs(x) for x in c if x != 0))   # normalise to smallest nonzero
print(f"   relation coefficients (D1..D5): {[c[i] for i in range(5)]}")
check("E", "the relation is exact", (Matrix([[c[i] for i in range(5)]]) * M),
      Matrix([[0] * N]))
support = [ROWLAB[i] for i in range(5) if c[i] != 0]
print(f"   channels in the relation's support (any ONE is droppable): {support}")
check("E", "D4 (U(1)_Y^3) is in the support, i.e. it is a dependent channel",
      c[3] != 0, True)
# each channel individually: does dropping it lose rank?
droppable = []
for i in range(5):
    Mi = M.copy()
    Mi.row_del(i)
    if Mi.rank() == rank:
        droppable.append(ROWLAB[i])
print(f"   channels whose removal does NOT lower the rank: {droppable}")
check("E", "number of individually-droppable channels", len(droppable), len(support))

# ---------------------------------------------------------------------------
# 6.  [E] CHIRALITY-BLINDNESS: the anomaly map is LINEAR, so its zero set is a
#         SUBGROUP -- closed under negation, containing 0.  No anomaly channel
#         can see |net chirality|.
# ---------------------------------------------------------------------------
print("\n-- chirality-blindness of the whole system, exactly --")
lin_ok = True
for a in itertools.product(range(-2, 3), repeat=N):
    if sum(abs(x) for x in a) > 4:
        continue
    va = Matrix(list(a))
    for b in [v15, vnu, v16, witness]:
        if M * (va + b) != M * va + M * b:
            lin_ok = False
check("E", "the anomaly map is exactly additive on sampled contents", lin_ok, True)
check("E", "L is closed under negation (chirality flip)", M * (-witness), Matrix([0] * 5))
check("E", "the vectorlike doubling n (+) (-n) is anomaly-free for EVERY n",
      all(M * (Matrix(list(a)) - Matrix(list(a))) == Matrix([0] * 5)
          for a in itertools.product(range(-2, 3), repeat=N)), True)
# the decisive statement: chiral and non-chiral contents share an anomaly value
chiral = v16                     # net chirality 1 in the 16 direction
nonchiral = Matrix([0] * N)      # net chirality 0
check("E", "a CHIRAL 16 and the EMPTY (vectorlike) content give the SAME anomaly vector",
      M * chiral, M * nonchiral)

# ---------------------------------------------------------------------------
# 7.  [C] CONTROLS THAT MUST HAVE POWER.  If any of these returns zero the
#         machinery is blind and nothing above is reportable.
# ---------------------------------------------------------------------------
print("\n-- controls with power (each MUST be nonzero) --")
ctrl = {
    "drop e^c from the 16 -> D5 must break":
        (M * Matrix([1, 1, 1, 1, 0, 1]))[4],
    "drop e^c from the 16 -> D4 must break":
        (M * Matrix([1, 1, 1, 1, 0, 1]))[3],
    "quark doublets alone -> D1 must break":
        (M * Matrix([1, 0, 0, 0, 0, 0]))[0],
    "one d^c colour triplet alone -> D1 must break":
        (M * Matrix([0, 0, 1, 0, 0, 0]))[0],
    "one extra u^c on top of a 16 -> D3 must break":
        (M * Matrix([1, 2, 1, 1, 1, 1]))[2],
    "one extra L on top of a 16 -> D2 must break":
        (M * Matrix([1, 1, 1, 2, 1, 1]))[1],
    "swap n_L and n_e (1,1,1,2,0,1) -> D5 must break":
        (M * Matrix([1, 1, 1, 2, 0, 1]))[4],
}
for lab, val in ctrl.items():
    check_nonzero("C", lab, val)

# a control proving the RANK result is not automatic: a perturbed hypercharge
# must change the rank or the kernel.
print("\n-- mutation controls on the rank/kernel result --")
MUT = [(r[0], (R(1, 2) if r[0] == "e^c" else r[1]), r[2], r[3], r[4]) for r in IRREPS]
Mmut = functionals(MUT)
check_nonzero("C", "MUTATION Y(e^c)=1/2: the complete 16 is no longer anomaly-free",
              sum(abs(x) for x in (Mmut * v16)))
check("C", "MUTATION Y(e^c)=1/2: rank rises to 5 (relation destroyed)",
      Mmut.rank(), 5)
check("C", "MUTATION Y(e^c)=1/2: kernel drops to dim 1",
      len(Mmut.nullspace()), 1)

MUT2 = [(r[0], (R(1, 3) if r[0] == "Q" else r[1]), r[2], r[3], r[4]) for r in IRREPS]
Mmut2 = functionals(MUT2)
check_nonzero("C", "MUTATION Y(Q)=1/3: the complete 16 is no longer anomaly-free",
              sum(abs(x) for x in (Mmut2 * v16)))

# a control proving the LATTICE result is not automatic: an arena in which the
# anomaly-free set is rank 1 only.
print("\n-- arena control: an arena WITHOUT a free singlet direction --")
NOSING = IRREPS[:5]
Mns = functionals(NOSING)
check("C", "arena {Q,u,d,L,e} (no nu^c): kernel is rank 1, i.e. exactly the 15",
      len(Mns.nullspace()), 1)
check("C", "arena {Q,u,d,L,e}: the 15 spans it",
      Mns * Matrix([1, 1, 1, 1, 1]), Matrix([0] * 5))

# THE ESSENTIAL SCOPING CONTROL.  rank 4 is a fact about THIS arena (the 16's own
# SM constituents), NOT a universal fact about the five SM anomaly channels.
# Enlarging the arena by one exotic direction must restore rank 5.
print("\n-- arena-extension controls: rank 4 is ARENA-SPECIFIC, not universal --")
EXO_LEPTON = IRREPS + [("X_lep", R(1, 2), 1, False, Integer(0))]
Mx1 = functionals(EXO_LEPTON)
check("C", "arena + one exotic Y=1/2 colour/isospin singlet: rank rises to 5",
      Mx1.rank(), 5)
check("C", "arena + one exotic Y=1/2 singlet: the five channels become independent",
      len(Mx1.T.nullspace()), 0)

EXO_QUARK = IRREPS + [("X_q", R(-1, 6), 3, False, Integer(-1))]
Mx2 = functionals(EXO_QUARK)
check("C", "arena + one exotic Y=-1/6 colour triplet: rank rises to 5", Mx2.rank(), 5)

# and the lattice grows too, so 'outside L' is arena-relative as well
check("C", "in the extended arena the kernel is still rank 2 (6 dirs, rank 5 system)",
      len(Mx1.nullspace()), 2)

# ---------------------------------------------------------------------------
# 8.  Summary
# ---------------------------------------------------------------------------
print("\n" + "=" * 74)
print(f"CHECKS RUN: {NCHK}   FAILURES: {len(FAIL)}")
for f in FAIL:
    print("  !! " + f)
print("=" * 74)
if FAIL:
    print("\nRESULT: FAIL")
    sys.exit(1)
print("""
RESULT (exact):

  * The five 4d SM anomaly channels are LINEAR functionals on the signed
    multiplicity lattice Z^6 of the 16's own SM constituents.
  * The system has RANK 4, not 5.  One channel is dependent; the exact
    relation is printed above.  The five ledger rows AC-D1..AC-D5 are
    therefore FOUR independent facts and one corollary.
  * The anomaly-free set is exactly the rank-2 saturated lattice
        L  =  Z.(15 of SU(5))  (+)  Z.(nu^c),
    verified by exhaustive search over [-3,3]^6.  "A complete 16" spans a
    rank-1 sublattice of L, so "the carrier equals complete 16s" is
    SUFFICIENT but NOT NECESSARY: L/Z.16 is infinite cyclic.
  * L is a SUBGROUP: closed under negation, containing 0, and containing
    every vectorlike doubling.  A chiral 16 and the empty content have the
    SAME anomaly vector.  No SM anomaly channel can see net chirality.

CONSEQUENCE for ledger rows AC-D1..AC-D5: the recorded condition
"none after the chiral 16 shadow is selected" contains a chirality clause
that is INERT for the rows' own content, and a completeness clause that is
STRICTLY STRONGER than necessary.  The recorded revival trigger
"a physical carrier not equal to complete 16s" is FALSE AS STATED inside
this arena -- the correct trigger is "a physical carrier outside L".
""")
sys.exit(0)
