#!/usr/bin/env python3
r"""
PHI-1 -- CONSTRUCT the 14->4 reduction map phi : Z^15 -> Z^6, and decide
         phi(ker M) subset L.

GU-COMPARATOR-ROUTING.  This probe touches a CONVENTIONAL COMPARATOR object
(the 4D Standard-Model perturbative gauge-anomaly conditions and the lattice
L = Z.(15 of SU(5)) (+) Z.(nu^c), fork 1).  Any result about that object binds
only that model.  See lab/active-research/joe-directed/phi-reduction/*.md and
lab/methods/source-native-comparator-routing.md.

WHAT IS BUILT.  LA-5 typed the unbuilt 14->4 reduction as a lattice
homomorphism phi : Z^15 -> Z^6 and attached a rank bound: AC-D1..D5 are
DERIVED rather than DERIVED_CONDITIONAL iff phi(ker M) subset L, which forces
rank(phi|ker M) <= 2.  Nobody had written phi down.  This probe writes it down
from the observation pullback that MD-1 established, and then decides the
criterion.

THE CONSTRUCTION, in three source-warranted steps.

  (1) GAUGE-BLINDNESS OF THE FORM INDEX -- inherited from M itself, not
      assumed.  CB-C builds the 14D anomaly system as
          D_p  =  [A-hat(TY) ch(Lambda^p T_C)]  *  ch(S_gauge)
      and the gauge Casimir Y occurs ONLY in ch(S).  Verified here over all
      15 columns: the form-leg factor carries Y-exponent 0 and nothing else.
      So in the arena where ker M is defined, the SM quantum numbers live
      entirely in S and the form degree p carries none.  A reduction that
      denies this does not get a different phi; it loses ker M.

  (2) THE PULLBACK TRUNCATES.  MD-1: the source-declared reduction is
      s^* along the observation section s(x) = (x, g_ab(x)), a CONTRACTION.
      On p-forms it is Lambda^p(ds^T) : Lambda^p T*Y -> Lambda^p T*X.  Since
      Lambda^p T*X4 = 0 for p >= 5, s^* ANNIHILATES the ten slots p = 5..14
      outright, and is surjective on p = 0..4.  So phi factors as
          phi  =  psi o T ,     T(x) = (x_0, x_1, x_2, x_3, x_4).

  (3) THE FORM DEGREE ONLY MULTIPLIES.  Lambda^p T*X4 is an internal singlet
      by (1), so the SM content of Lambda^p T*X4 (x) s^*S is k_p * v, where
      v in Z^6 is the internal SM content of the observed 4D spinor and k_p is
      an integer Lorentz multiplicity.  Hence psi_p = k_p * v and

          rank(phi)  <=  1                for EVERY v and EVERY k.

      For the spin-1/2 projection, derived here by exact weight-multiset
      decomposition of Lambda^p V (x) (1/2,0):   k = (+1,-1,+1,-1,+1).

  RESULT:  phi  =  v (x) k,   k = (1,-1,1,-1,1,0,0,0,0,0,0,0,0,0,0) in Z^15.

THE DECISION.  T maps ker M ONTO Z^5 (Smith divisors all 1), so
phi(ker M) = phi(Z^15) = Z.v, and since L is saturated,

          phi(ker M) subset L   <==>   v in L.

The rank-10 14D kernel contributes exactly zero bits.  LA-5's rank bound is
met unconditionally (rank <= 1 <= 2); the residual condition is a single 4D
vector the 14D data provably cannot supply.

NOT CLAIMED HERE.  The 14D rank-5 / kernel-10 system is owned by CB-C and is
IMPORTED from tests/anomaly/cb_c_anomaly_rank.py, never re-derived.  The 4D
rank-4 result and L are owned by LA-3 and are REPRODUCED as anchors.  MD-1's
E1/E2/E3 are REPRODUCED.  Nothing here is a source action, a chirality-
production mechanism, a generation count, a real-form statement, a decision of
the SOLDERED-AD fork, a ledger edit, or a verdict movement.

Exit 0 iff every [E] result matches its stated exact value, every [C] control
fires as declared, and every [R] reproduction matches its filed owner.
Run with --mutate=<name> to exercise the failure path (must exit 1).
"""

from __future__ import annotations

import itertools
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp
from sympy import Integer, Matrix, Rational as R
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tests", "anomaly"))

MUTATE = ""
for _a in sys.argv[1:]:
    if _a.startswith("--mutate="):
        MUTATE = _a.split("=", 1)[1]

FAIL: list[str] = []
NCHK = 0
TAGS: dict[str, int] = {}
RESULTS: dict[str, object] = {}


def check(tag: str, label: str, got, want) -> bool:
    global NCHK
    NCHK += 1
    TAGS[tag] = TAGS.get(tag, 0) + 1
    ok = (got == want)
    if not ok:
        FAIL.append(f"[{tag}] {label}: got {got!r}, want {want!r}")
    print(f"  [{tag}] {'PASS' if ok else 'FAIL'}  {label}: {got}")
    return ok


def check_true(tag: str, label: str, got) -> bool:
    return check(tag, label, bool(got), True)


def assert_no_float(obj, path="result") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"FLOAT found at {path}: {obj!r}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}[{k!r}]")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


print("=" * 78)
print("PHI-1 -- construct phi : Z^15 -> Z^6 and decide phi(ker M) subset L")
print("=" * 78)
if MUTATE:
    print(f"  *** MUTATION ACTIVE: {MUTATE} -- this run MUST exit 1 ***")


# ===========================================================================
# 0.  IMPORT the 14D system from CB-C.  Never re-derived.
# ===========================================================================
print("\n-- 0. the 14D system, IMPORTED from tests/anomaly/cb_c_anomaly_rank.py --")
import cb_c_anomaly_rank as cbc  # noqa: E402

FORM = {p: cbc.AHAT_LAMBDA.get(p, {}) for p in range(15)}       # A-hat ch(Lambda^p T_C)
GAUGE = cbc.CH_S                                                 # ch(S)
Dfull = {p: (cbc.to_p_basis(cbc.pmul(FORM[p], GAUGE)) if FORM[p] else {}) for p in range(15)}
KEYS = sorted({k for p in range(15) for k in Dfull[p]}, key=lambda k: (k[1], -k[0][0], -k[0][1]))
MB = [[Dfull[p].get(k, F(0)) for p in range(15)] for k in KEYS]  # 12 x 15 over Q
KER, PIV, FREE = cbc.kernel_basis(MB, 15)

check("R", "reproduce CB-C: degree-16 monomial basis size", len(KEYS), 12)
check("R", "reproduce CB-C: rank of the 12x15 system", len(PIV), 5)
check("R", "reproduce CB-C: kernel dimension", 15 - len(PIV), 10)


def to_primitive_int(v) -> list[int]:
    den = 1
    for c in v:
        den = den * c.denominator // math.gcd(den, c.denominator)
    w = [int(c * den) for c in v]
    g = 0
    for c in w:
        g = math.gcd(g, abs(c))
    return [c // g for c in w] if g else w


KINT = [to_primitive_int(v) for v in KER]
print("   ker M, integral basis (free coordinates are x_5..x_14, unit vectors):")
for w in KINT:
    print("     ", w)

# The kernel lattice is SATURATED: the free block is the 10x10 identity, so
# every integer point of the rational kernel is an integer combination.
FREEBLOCK = Matrix([[Integer(w[j]) for j in range(5, 15)] for w in KINT])
check("E", "the ker M basis carries the 10x10 identity on slots p=5..14",
      FREEBLOCK == sp.eye(10), True)

# Hodge-antisymmetric directions (CB-C row A7)
ANTI = []
for p in range(7):
    a = [0] * 15
    a[p] = 1
    a[14 - p] = -1
    ANTI.append(a)
anti_ok = all(sum(MB[i][j] * ANTI[p][j] for j in range(15)) == 0
              for p in range(7) for i in range(len(KEYS)))
check("R", "reproduce CB-C A7: all 7 Hodge-antisymmetric directions are admissible",
      anti_ok, True)
check("C", "control: a single chiral slot Omega^0 (x) S^+ is NOT admissible",
      all(MB[i][0] == 0 for i in range(len(KEYS))), False)

# LA-2 anchor: 2189 integer kernel points of height 1
h1 = 0
for freevals in itertools.product((-1, 0, 1), repeat=10):
    x = [0] * 15
    for j, fv in enumerate(freevals):
        if fv:
            for c in range(5):
                x[c] += fv * KINT[j][c]
    if all(abs(c) <= 1 for c in x[:5]):
        h1 += 1
check("R", "reproduce LA-2: integer kernel points of height 1", h1, 2189)


# ===========================================================================
# 1.  GAUGE-BLINDNESS OF THE FORM INDEX -- read off M's OWN construction.
#     Monomial key = (e1,e2,e3,e4,eY); eY is the exponent of Y = y^2, the
#     Sp(1) Cartan square, i.e. the gauge Casimir.
# ===========================================================================
print("\n-- 1. the form index carries NO gauge charge (inherited from M itself) --")
form_Y = sorted({mono[4] for p in range(15) for mono in FORM[p]})
gauge_Y = sorted({mono[4] for mono in GAUGE})
if MUTATE == "gauge-blind":
    form_Y = [0, 1]
check("E", "Y-exponents occurring in the form-leg factor A-hat ch(Lambda^p T_C)",
      form_Y, [0])
check("E", "Y-exponents occurring in the gauge factor ch(S)", gauge_Y, [0, 1, 2, 3, 4])
check("C", "control: ch(S) is NOT Y-free, so the previous check is not trivial",
      gauge_Y == [0], False)
full_Y = sorted({k[1] for p in range(15) for k in Dfull[p]})
check("C", "control: the assembled columns D_p DO carry Y (inherited wholly from ch(S))",
      full_Y, [0, 1, 2, 3, 4])
# the factorisation is exact, column by column
factor_ok = all(cbc.to_p_basis(cbc.pmul(FORM[p], GAUGE)) == Dfull[p] for p in range(15))
check("E", "every column factorises exactly as (form leg) * (gauge leg)", factor_ok, True)
print("   ==> in the arena where ker M is defined, SM quantum numbers live"
      " ENTIRELY in S;\n       the form degree p carries none.  This is M's own assumption,"
      " not a new one.")


# ===========================================================================
# 2.  THE OBSERVATION PULLBACK ON p-FORMS.  MD-1 reproduced, then extended
#     from the 1-form leg to every form degree.
# ===========================================================================
print("\n-- 2. the observation pullback s^* on p-forms (MD-1 reproduced, then extended) --")

PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]          # Sym^2(T*X4), 10 entries
check("E", "the internal fibre Sym^2(T*X4) has dimension 10", len(PAIRS), 10)
check("E", "dim Y14 = 4 + dim Sym^2(T*X4)", 4 + len(PAIRS), 14)

xs = sp.symbols("x0 x1 x2 x3")
gf = [[sp.Function(f"g{min(a, b)}{max(a, b)}")(*xs) for b in range(4)] for a in range(4)]
ds = sp.zeros(14, 4)
for mu in range(4):
    ds[mu, mu] = 1
for i, (a, b) in enumerate(PAIRS):
    for mu in range(4):
        ds[4 + i, mu] = sp.diff(gf[a][b], xs[mu])
check("R", "reproduce MD-1 E1: ds has rank 4 for a general observation section",
      ds.rank(), 4)

sstar = ds.T                                                      # s^* : T*Y (14) -> T*X (4)
omega = sp.Matrix(14, 1, lambda i, j: sp.Symbol(f"w{i}"))
expected = sp.Matrix(4, 1, lambda mu, j: sp.Symbol(f"w{mu}") + sum(
    sp.Symbol(f"w{4 + i}") * sp.diff(gf[a][b], xs[mu]) for i, (a, b) in enumerate(PAIRS)))
check("R", "reproduce MD-1 E2: (s^*omega)_mu = omega_mu + omega_(ab) d_mu g_ab",
      sp.simplify(sstar * omega - expected) == sp.zeros(4, 1), True)
check("R", "reproduce MD-1 E3: s^* annihilates a 10-dim space of form legs",
      len(sstar.nullspace()), 10)


def ext_power_rank(A: list[list[F]], p: int) -> int:
    """rank of Lambda^p A for A : (source dim n) -> (target dim m), exact."""
    m, n = len(A), len(A[0])
    if p == 0:
        return 1
    if p > m or p > n:
        return 0
    rows = []
    for I in itertools.combinations(range(m), p):
        row = []
        for J in itertools.combinations(range(n), p):
            sub = [[A[i][j] for j in J] for i in I]
            row.append(_det(sub))
        rows.append(row)
    _, piv = cbc.rref(rows)
    return len(piv)


def _det(M: list[list[F]]) -> F:
    n = len(M)
    M = [r[:] for r in M]
    det = F(1)
    for c in range(n):
        pr = next((i for i in range(c, n) if M[i][c] != 0), None)
        if pr is None:
            return F(0)
        if pr != c:
            M[c], M[pr] = M[pr], M[c]
            det = -det
        det *= M[c][c]
        inv = F(1) / M[c][c]
        M[c] = [v * inv for v in M[c]]
        for i in range(c + 1, n):
            if M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[c][j] for j in range(n)]
    return det


def pullback_matrix(Dv: list[list[int]]) -> list[list[F]]:
    """s^* in adapted coordinates: [ I_4 | d_mu g_ab ], exact rationals."""
    return [[F(1) if j == mu else F(0) for j in range(4)] + [F(Dv[mu][i]) for i in range(10)]
            for mu in range(4)]


# two independent exact rational sections; neither is generic-by-accident
D_A = [[(3 * mu + 5 * i + 1) % 11 - 5 for i in range(10)] for mu in range(4)]
D_B = [[(7 * mu * i + 2 * i * i + mu + 3) % 13 - 6 for i in range(10)] for mu in range(4)]
for tagname, Dv in (("A", D_A), ("B", D_B)):
    A = pullback_matrix(Dv)
    _, pv = cbc.rref(A)
    check("E", f"section {tagname}: s^* : T*Y -> T*X has rank 4 (surjective)", len(pv), 4)
    for p in range(0, 5):
        want = math.comb(4, p)
        check("E", f"section {tagname}: rank(Lambda^{p} s^*) = C(4,{p})",
              ext_power_rank(A, p), want)

# The ten annihilated slots, and their non-vacuity.
for p in range(5, 15):
    check("E", f"dim Lambda^{p} T*X4 = 0, so s^*|_Omega^{p} is identically zero",
          math.comb(4, p), 0)
check("E", "the annihilated source spaces are not small: dim Lambda^p T*Y, p=5..14",
      [math.comb(14, p) for p in range(5, 15)],
      [2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1])
check("E", "number of form slots the observation annihilates outright", 15 - 5, 10)

# CONTROL: a degenerate section (ds of rank 3) must drop the exterior ranks.
D_deg = [[(3 * mu + 5 * i + 1) % 11 - 5 for i in range(10)] for mu in range(3)] + [[0] * 10]
A_deg = [[F(1) if (j == mu and mu < 3) else F(0) for j in range(4)]
         + [F(D_deg[mu][i]) for i in range(10)] for mu in range(4)]
_, pv_deg = cbc.rref(A_deg)
check("C", "control: a rank-3 (degenerate) section is detected", len(pv_deg), 3)
check("C", "control: rank(Lambda^2) drops from 6 to 3 on the degenerate section",
      ext_power_rank(A_deg, 2), 3)
check("C", "control: rank(Lambda^4) drops from 1 to 0 on the degenerate section",
      ext_power_rank(A_deg, 4), 0)

print("   ==> phi factors as psi o T with T(x) = (x_0,...,x_4).  The ten slots"
      " p=5..14 are\n       annihilated by the observation itself, not by a choice.")


# ===========================================================================
# 3.  THE LORENTZ MULTIPLICITIES k_p, by exact weight-multiset decomposition
#     of sl(2,C) x sl(2,C) reps.  Irrep (a,b) <-> (j_+,j_-) = (a/2, b/2).
# ===========================================================================
print("\n-- 3. the Lorentz multiplicities k_p (exact weight-multiset decomposition) --")


def irrep_weights(a: int, b: int) -> list[tuple[int, int]]:
    return [(m, n) for m in range(-a, a + 1, 2) for n in range(-b, b + 1, 2)]


def decompose(ws: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    """Decompose a weight multiset of sl2 x sl2 into irreps (a,b). Exact."""
    pool: dict[tuple[int, int], int] = {}
    for w in ws:
        pool[w] = pool.get(w, 0) + 1
    out: dict[tuple[int, int], int] = {}
    while any(v > 0 for v in pool.values()):
        hw = max(k for k, v in pool.items() if v > 0)
        a, b = hw
        assert a >= 0 and b >= 0, f"non-dominant highest weight {hw}"
        out[(a, b)] = out.get((a, b), 0) + 1
        for w in irrep_weights(a, b):
            pool[w] = pool.get(w, 0) - 1
            assert pool[w] >= 0, "decomposition failed: negative multiplicity"
    return {k: v for k, v in out.items() if v}


def tensor(u: dict[tuple[int, int], int], v: dict[tuple[int, int], int]) -> dict:
    ws = []
    for (a1, b1), m1 in u.items():
        for (a2, b2), m2 in v.items():
            for w1 in irrep_weights(a1, b1):
                for w2 in irrep_weights(a2, b2):
                    ws += [(w1[0] + w2[0], w1[1] + w2[1])] * (m1 * m2)
    return decompose(ws)


VEC = {(1, 1): 1}                      # the 4D vector rep (1/2,1/2)
SPIN_L = {(1, 0): 1}                   # a left-handed Weyl spinor (1/2,0)
vec_w = irrep_weights(1, 1)
check("E", "the vector rep (1/2,1/2) has 4 weights", len(vec_w), 4)

LAM: dict[int, dict] = {}
for p in range(5):
    ws = [tuple(map(sum, zip(*sub))) if p else (0, 0)
          for sub in itertools.combinations(vec_w, p)] if p else [(0, 0)]
    LAM[p] = decompose(list(ws))
    print(f"     Lambda^{p} T*X4 = " + " + ".join(
        f"({sp.Rational(a, 2)},{sp.Rational(b, 2)})" + (f"x{m}" if m > 1 else "")
        for (a, b), m in sorted(LAM[p].items())))

check("E", "Lambda^0 T*X4 = (0,0)", LAM[0], {(0, 0): 1})
check("E", "Lambda^1 T*X4 = (1/2,1/2)", LAM[1], {(1, 1): 1})
check("E", "Lambda^2 T*X4 = (1,0) + (0,1)", LAM[2], {(2, 0): 1, (0, 2): 1})
check("E", "Lambda^3 T*X4 = (1/2,1/2)", LAM[3], {(1, 1): 1})
check("E", "Lambda^4 T*X4 = (0,0)", LAM[4], {(0, 0): 1})
check("E", "dimensions of Lambda^p T*X4",
      [sum(m * (a + 1) * (b + 1) for (a, b), m in LAM[p].items()) for p in range(5)],
      [1, 4, 6, 4, 1])
check("C", "control: the decomposition rejects a planted wrong answer",
      LAM[2] == {(2, 0): 1, (0, 2): 1, (1, 1): 1}, False)

TENS: dict[int, dict] = {}
for p in range(5):
    TENS[p] = tensor(LAM[p], SPIN_L)
    print(f"     Lambda^{p} (x) (1/2,0) = " + " + ".join(
        f"({sp.Rational(a, 2)},{sp.Rational(b, 2)})" + (f"x{m}" if m > 1 else "")
        for (a, b), m in sorted(TENS[p].items())))

check("E", "Lambda^1 (x) (1/2,0) = (1,1/2) + (0,1/2)", TENS[1], {(2, 1): 1, (0, 1): 1})
check("E", "Lambda^2 (x) (1/2,0) = (3/2,0) + (1/2,0) + (1/2,1)",
      TENS[2], {(3, 0): 1, (1, 0): 1, (1, 2): 1})

LTYPES = sorted({t for p in range(5) for t in TENS[p]})
check("E", "distinct Lorentz types occurring across p = 0..4", len(LTYPES), 5)
check("C", "control: higher-spin pieces DO occur, so keeping spin-1/2 is a strict projection",
      sorted(t for t in LTYPES if t not in {(1, 0), (0, 1)}), [(1, 2), (2, 1), (3, 0)])

# signed spin-1/2 multiplicity: (1/2,0) counts +1, its conjugate (0,1/2) counts -1
KVEC = [TENS[p].get((1, 0), 0) - TENS[p].get((0, 1), 0) for p in range(5)]
if MUTATE == "k-sign":
    KVEC[2] = -KVEC[2]
check("E", "signed spin-1/2 multiplicities k_p, p = 0..4", KVEC, [1, -1, 1, -1, 1])
check("E", "k_p = (-1)^p exactly", KVEC, [(-1) ** p for p in range(5)])
check("E", "gcd(k_0..k_4) = 1", math.gcd(*[abs(c) for c in KVEC]), 1)
check("C", "control: k is not the naive dimension count C(4,p)",
      KVEC == [math.comb(4, p) for p in range(5)], False)

K15 = KVEC + [0] * 10
check("E", "k as a functional on Z^15 (supported on the observed slots only)",
      K15, [1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


# ===========================================================================
# 4.  THE TRUNCATION T ON ker M.
# ===========================================================================
print("\n-- 4. T(ker M): the observation sees the whole of Z^5 --")
NOBS = 4 if MUTATE == "truncate" else 5
TK = Matrix([[Integer(w[c]) for c in range(NOBS)] for w in KINT])
check("E", "M's pivot columns are exactly the observed slots p = 0..4", PIV, [0, 1, 2, 3, 4])
check("E", "M's free columns are exactly the annihilated slots p = 5..14",
      FREE, list(range(5, 15)))
check("E", "rank T(ker M)", TK.rank(), 5)
snfT = smith_normal_form(TK)
divsT = [int(snfT[i, i]) for i in range(min(snfT.shape)) if snfT[i, i] != 0]
check("E", "Smith elementary divisors of T(ker M) are all 1 => T(ker M) = Z^5",
      divsT, [1, 1, 1, 1, 1])
check("E", "so T(ker M) = T(Z^15) = Z^5 exactly", divsT == [1] * 5 and TK.rank() == 5, True)
check("E", "ker M meets ker T in rank 10 - 5 = 5", 10 - TK.rank(), 5)
TK3 = Matrix([[Integer(w[c]) for c in range(4)] for w in KINT])
check("C", "control: truncating one slot earlier (p<=3) gives rank 4, not 5", TK3.rank(), 4)
check("C", "control: T(ker M) is not zero", TK.rank() == 0, False)

# T on the named Hodge-antisymmetric directions
Tanti = [[ANTI[p][c] for c in range(5)] for p in range(7)]
check("E", "T(a_p) = e_p for p = 0..4 and 0 for p = 5,6",
      Tanti, [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0] * 5, [0] * 5])


# ===========================================================================
# 5.  phi ITSELF, and the ZERO-BIT theorem.
# ===========================================================================
print("\n-- 5. phi = v (x) k, and what it does to ker M --")


def PHI(v: list[int]) -> Matrix:
    """The 6 x 15 integer matrix phi = v (x) k."""
    return Matrix([[Integer(v[r] * K15[c]) for c in range(15)] for r in range(6)])


V16 = [1, 1, 1, 1, 1, 1]
PHI16 = PHI(V16)
print("   phi (for v = the complete 16), 6 x 15:")
for r in range(6):
    print("     " + str([int(PHI16[r, c]) for c in range(15)]))

check("E", "rank(phi) = 1 for v = 16", PHI16.rank(), 1)
for vtest in ([1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [2, -3, 5, 7, -11, 13]):
    check("E", f"rank(phi) <= 1 for v = {vtest}", PHI(vtest).rank() <= 1, True)
check("C", "control: rank(phi) = 0 exactly when v = 0", PHI([0] * 6).rank(), 0)

# k evaluated on the kernel basis: the image is Z.v, not a proper sublattice
kvals = [sum(K15[c] * w[c] for c in range(15)) for w in KINT]
print(f"   k applied to the ker M basis: {kvals}")
check("E", "gcd of k over the ker M basis is 1 => phi(ker M) = Z.v",
      math.gcd(*[abs(t) for t in kvals]), 1)
kvals_all = [sum(K15[c] * (1 if c == j else 0) for c in range(15)) for j in range(15)]
check("E", "gcd of k over all of Z^15 is also 1 => phi(Z^15) = Z.v",
      math.gcd(*[abs(t) for t in kvals_all if t]), 1)
check("E", "ZERO-BIT: phi(ker M) = phi(Z^15) = Z.v",
      math.gcd(*[abs(t) for t in kvals]) == math.gcd(*[abs(t) for t in kvals_all if t]), True)

# The zero-bit result holds for EVERY map factoring through T, not just rank-1
# ones: T(ker M) = Z^5 already, so psi(T(ker M)) = psi(Z^5) = psi(T(Z^15)) as
# LATTICES, for every psi.  Verified by canonical Hermite normal form on three
# independent psi, including a rank-5 one.
def row_lattice_hnf(gen: Matrix) -> Matrix:
    """Canonical form of the lattice generated by the ROWS of gen."""
    return hermite_normal_form(Matrix([[Integer(gen[i, j]) for i in range(gen.rows)]
                                       for j in range(gen.cols)]))


NC = TK.cols
PSI_TESTS = {
    "rank-5 generic": Matrix(6, NC, lambda i, j: Integer((5 * i + 3 * j + 1) % 7 - 3)),
    "rank-1 derived": Matrix(6, NC, lambda i, j: Integer(V16[i] * KVEC[j])),
    "rank-2 into L": Matrix(6, NC, lambda i, j: Integer(
        ([1, 1, 1, 1, 1, 0][i] if j % 2 == 0 else [0, 0, 0, 0, 0, 1][i]) * (j + 1))),
}
for pname, psi_t in PSI_TESTS.items():
    latA = row_lattice_hnf(TK * psi_t.T)             # psi(T(ker M))
    latB = row_lattice_hnf(Matrix.eye(NC) * psi_t.T)  # psi(T(Z^15)) = psi(Z^5)
    check("E", f"psi(T(ker M)) = psi(T(Z^15)) as LATTICES [{pname}]", latA, latB)
check("C", "control: the HNF comparison has power (a proper sublattice is detected)",
      row_lattice_hnf(Matrix.eye(5)) == row_lattice_hnf(2 * Matrix.eye(5)), False)

# CONTROL: the 14D system is NOT invisible to every functional -- only to those
# that factor through the observation.
row0 = to_primitive_int(MB[0])
f_ker = sorted({sum(row0[c] * w[c] for c in range(15)) for w in KINT})
f_all = sorted({row0[j] for j in range(15)})
check("C", "control: a row of M itself annihilates ker M (so M is visible to something)",
      f_ker, [0])
check("C", "control: ...but not all of Z^15 -- the control has power",
      all(t == 0 for t in f_all), False)

# LA-5's stated requirement, tested against the constructed phi
kerdim_on_kerM = 10 - PHI16.rank()
check("E", "LA-5 requirement: dim ker(phi|ker M) >= 8 -- constructed phi gives",
      kerdim_on_kerM, 9)
check("E", "LA-5 requirement satisfied (9 >= 8)", kerdim_on_kerM >= 8, True)
ANTIM = Matrix([[Integer(a[c]) for c in range(15)] for a in ANTI])
rank_on_anti = (PHI16 * ANTIM.T).rank()
check("E", "rank(phi restricted to the 7-dim Hodge-antisymmetric span)", rank_on_anti, 1)
check("E", "LA-5 requirement: >= 5 antisymmetric directions annihilated -- rank reading",
      7 - rank_on_anti >= 5, True)
named_annihilated = [p for p in range(7) if all(
    (PHI16 * Matrix([[Integer(c)] for c in ANTI[p]]))[r, 0] == 0 for r in range(6))]
check("E", "CORRECTION: NAMED antisymmetric basis directions a_p that phi annihilates",
      named_annihilated, [5, 6])
check("E", "so the named-basis reading of LA-5's prose ('>= 5 of the 7') is FALSE",
      len(named_annihilated) >= 5, False)
check("C", "control: the rank reading and the named-basis reading genuinely differ",
      (7 - rank_on_anti >= 5) == (len(named_annihilated) >= 5), False)

# CONTROL: a phi that VIOLATES internal-blindness can reach rank 5 -- so the
# rank-1 result is bought by gauge-blindness, not by the shape of ker M.
PHI_bad = Matrix(6, 15, lambda i, j: Integer(1 if (j < 5 and i == j) else 0))
check("C", "control: an internal-blindness-VIOLATING phi reaches rank 5 (> 2)",
      PHI_bad.rank(), 5)
check("C", "control: ...and it breaks the LA-5 bound", 10 - PHI_bad.rank() >= 8, False)


# ===========================================================================
# 5b. THE CONTRARY HORN.  Reject the pullback and take the DISAVOWED KK-style
#     projection instead: split Omega^p(Y) into Lambda^a T*X (x) Lambda^b(fibre)
#     with a + b = p, a <= 4.  Now every slot p = 0..14 reaches 4D.  The fibre
#     Sym^2(T*X4) is ENDOGENOUS (MD-1), so Lambda^b of it still carries NO SM
#     charge -- the rank-1 result survives, but k changes completely.
# ===========================================================================
print("\n-- 5b. the contrary horn: the disavowed KK projection --")
KKFIB = 9 if MUTATE == "kk-fibre" else 10
KKV = [sum(KVEC[a] * math.comb(KKFIB, p - a) for a in range(0, min(4, p) + 1) if p - a >= 0)
       for p in range(15)]
check("E", "KK multiplicities k''_p = C(9,p) + C(9,p-5) (closed form (1+t^5)(1+t)^9)",
      KKV, [math.comb(9, p) + (math.comb(9, p - 5) if p >= 5 else 0) for p in range(15)])
check("E", "k'' explicitly", KKV,
      [1, 9, 36, 84, 126, 127, 93, 72, 93, 127, 126, 84, 36, 9, 1])
check("E", "sum of k'' = 2^10", sum(KKV), 1024)
check("E", "k'' is supported on ALL 15 slots, unlike the pullback k",
      sum(1 for c in KKV if c), 15)
PHI_KK = Matrix([[Integer(V16[r] * KKV[c]) for c in range(15)] for r in range(6)])
check("E", "the KK horn ALSO has rank 1 (the fibre carries no SM charge either)",
      PHI_KK.rank(), 1)
kk_named = [p for p in range(7) if KKV[p] - KKV[14 - p] == 0]
check("E", "KK horn: k'' is Hodge-SYMMETRIC, so it annihilates ALL 7 named "
           "antisymmetric directions", kk_named, [0, 1, 2, 3, 4, 5, 6])
check("C", "control: the pullback horn annihilates only 2 of the same 7 -- "
           "the two horns are genuinely different maps",
      named_annihilated == kk_named, False)

# The decisive separation: is the reduction functional itself an anomaly condition?
kk_ker = [sum(KKV[c] * w[c] for c in range(15)) for w in KINT]
check("E", "KK horn: k'' evaluates to ZERO on EVERY ker M basis vector", kk_ker, [0] * 10)
_, piv_kk = cbc.rref(MB + [[F(c) for c in KKV]])
check("E", "so k'' lies IN the row space of M: rank(M | k'') = rank(M) = 5", len(piv_kk), 5)
_, piv_pb = cbc.rref(MB + [[F(c) for c in K15]])
check("E", "the PULLBACK functional k is NOT in the row space: rank(M | k) = 6",
      len(piv_pb), 6)
check("C", "control: the two horns are separated by exactly this test",
      len(piv_kk) == len(piv_pb), False)
check("E", "KK horn consequence: phi_KK(ker M) = {0}, so phi_KK(ker M) subset L "
           "holds UNCONDITIONALLY -- because the 4D content is IDENTICALLY EMPTY",
      all(t == 0 for t in kk_ker), True)

# This is the same phenomenon CB-C already banked for the net-chirality functional
# W = sum_p x_p C(14,p): W is in the row space, so W = 0 on ker M.  Reproduced,
# not re-claimed; k'' is a second instance of it.
WVEC = [math.comb(14, p) for p in range(15)]
_, piv_W = cbc.rref(MB + [[F(c) for c in WVEC]])
check("R", "reproduce CB-C: W = sum_p x_p C(14,p) IS in the row space of M",
      len(piv_W), 5)
FAMILY = []
for a in range(5):
    fv = [0] * 15
    for b in range(11):
        fv[a + b] += math.comb(10, b)
    FAMILY.append(fv)
ann = []
for c in itertools.product((-1, 0, 1), repeat=5):
    fv = [sum(c[a] * FAMILY[a][j] for a in range(5)) for j in range(15)]
    if all(sum(fv[j] * w[j] for j in range(15)) == 0 for w in KINT):
        ann.append(c)
pal = [c for c in itertools.product((-1, 0, 1), repeat=5) if c[0] == c[4] and c[1] == c[3]]
check("E", "characterisation: c(t).(1+t)^10 annihilates ker M IFF c is palindromic",
      sorted(ann), sorted(pal))
check("E", "both W (c = (1,4,6,4,1)) and k'' (c = (1,-1,1,-1,1)) are palindromic",
      ((1, 4, 6, 4, 1)[0] == (1, 4, 6, 4, 1)[4], tuple(KVEC)[0] == tuple(KVEC)[4]),
      (True, True))
check("C", "control: a NON-palindromic c is not annihilating", (0, 0, 0, 0, 1) in ann, False)
print("   ==> the KK horn 'derives' AC-D1..D5 by producing an IDENTICALLY EMPTY 4D"
      "\n       fermion content.  That is a vacuous derivation and a kill of the horn,"
      "\n       not a win.  The source-native pullback horn is the one with content.")


# ===========================================================================
# 6.  ROBUSTNESS: the rank bound survives EVERY internal-blind weighting.
#     The Lorentz read-off (which components of Lambda^p (x) S count as 4D
#     chiral fermions) is NOT settled by the source.  It does not matter.
# ===========================================================================
print("\n-- 6. robustness: rank <= 1 for every internal-blind Lorentz weighting --")
ranks_seen = set()
gcds_seen = set()
worst = 0
for w in itertools.product(range(-2, 3), repeat=len(LTYPES)):
    wmap = dict(zip(LTYPES, w))
    kw = [sum(wmap[t] * m for t, m in TENS[p].items()) for p in range(5)]
    psi = Matrix([[Integer(V16[r] * kw[c]) for c in range(5)] for r in range(6)])
    rk = psi.rank()
    ranks_seen.add(rk)
    worst = max(worst, rk)
    nz = [abs(t) for t in kw if t]
    gcds_seen.add(math.gcd(*nz) if nz else 0)
check("E", "weightings swept exhaustively over {-2..2}^5", 5 ** len(LTYPES), 3125)
check("E", "maximum rank(psi) over ALL internal-blind weightings", worst, 1)
check("E", "ranks attained", sorted(ranks_seen), [0, 1])
check("C", "control: rank 0 is attained (so the sweep is not saturated at 1)",
      0 in ranks_seen, True)
check("C", "control: rank 1 is attained (so the sweep is not vacuous)", 1 in ranks_seen, True)
check("E", "so the LA-5 bound rank <= 2 is met by EVERY candidate, not just the derived one",
      worst <= 2, True)
print(f"   image indices gcd(k^w) attained over the sweep: {sorted(gcds_seen)}")

# CONTROL: allow the weight to depend on the INTERNAL irrep -- rank 5 returns.
psi_int = Matrix(6, 5, lambda i, j: Integer(1 if i == j else 0))
check("C", "control: letting the weight depend on the internal irrep restores rank 5",
      psi_int.rank(), 5)
print("   ==> the rank bound is bought by GAUGE-BLINDNESS of the form index,"
      " which is M's\n       own assumption.  Denying it does not give a"
      " different phi; it destroys ker M.")


# ===========================================================================
# 7.  THE 4D SIDE: L, reproduced from LA-3, then the criterion.
# ===========================================================================
print("\n-- 7. the criterion: phi(ker M) subset L  <==>  v in L --")
IRREPS = [("Q", R(1, 6), 3, True, Integer(1)),
          ("u^c", R(-2, 3), 3, False, Integer(-1)),
          ("d^c", R(1, 3), 3, False, Integer(-1)),
          ("L", R(-1, 2), 1, True, Integer(0)),
          ("e^c", R(1), 1, False, Integer(0)),
          ("nu^c", R(0), 1, False, Integer(0))]
T_FUND = R(1, 2)


def functionals(irreps):
    f1, f2, f3, f4, f5 = [], [], [], [], []
    for (_, Y, nc, dbl, A3) in irreps:
        nw = 2 if dbl else 1
        nstates = nc * nw
        f1.append(A3 * nw)
        f2.append(T_FUND * Y * nc if dbl else R(0))
        f3.append(T_FUND * Y * nw if nc == 3 else R(0))
        f4.append(nstates * Y ** 3)
        f5.append(nstates * Y)
    return Matrix([f1, f2, f3, f4, f5])


M4 = functionals(IRREPS)
check("R", "reproduce LA-3: rank of the 5x6 anomaly system", M4.rank(), 4)
check("R", "reproduce LA-3: dim ker M4 = 2", len(M4.nullspace()), 2)
V15 = Matrix([1, 1, 1, 1, 1, 0])
VNU = Matrix([0, 0, 0, 0, 0, 1])
check("R", "reproduce LA-3: M4 * (15 of SU(5)) = 0", M4 * V15, Matrix([0] * 5))
check("R", "reproduce LA-3: M4 * (nu^c) = 0", M4 * VNU, Matrix([0] * 5))
check("R", "reproduce LA-3: witness (1,1,1,1,1,7) cancels",
      M4 * Matrix([1, 1, 1, 1, 1, 7]), Matrix([0] * 5))
rel = 2 * M4[0, :] - 27 * M4[1, :] - 36 * M4[2, :] - 9 * M4[3, :] + 9 * M4[4, :]
check("R", "reproduce LA-3: 2 D1 - 27 D2 - 36 D3 - 9 D4 + 9 D5 = 0",
      rel, sp.zeros(1, 6))
LB = Matrix.hstack(V15, VNU)
snfL = smith_normal_form(LB.T)
check("R", "reproduce LA-3: L is SATURATED (Smith divisors all 1)",
      [int(snfL[i, i]) for i in range(min(snfL.shape)) if snfL[i, i] != 0], [1, 1])
check("C", "control: a single Q is NOT anomaly-free",
      M4 * Matrix([1, 0, 0, 0, 0, 0]) == Matrix([0] * 5), False)


def in_L(v: list[int]) -> bool:
    """v in L iff n_Q = n_u = n_d = n_L = n_e (n_nu free). Decided exactly."""
    return len(set(v[:5])) == 1


check("E", "v in L <=> the five charged constituents have EQUAL multiplicity",
      all(in_L(list(x)) == (M4 * Matrix(list(x)) == Matrix([0] * 5))
          for x in itertools.product(range(-3, 4), repeat=6)), True)


def phi_kerM_in_L(v: list[int]) -> bool:
    """phi(ker M) = Z.v, and L is saturated, so this is exactly v in L."""
    g = math.gcd(*[abs(t) for t in kvals])
    gens = [[g * c for c in v]]
    return all(M4 * Matrix(gen) == Matrix([0] * 5) for gen in gens)


WITNESS = [1, 0, 0, 0, 0, 0] if MUTATE == "L-wrong" else V16
check("E", "v = the complete 16: phi(ker M) subset L", phi_kerM_in_L(WITNESS), True)
check("E", "v = the 15 of SU(5): phi(ker M) subset L", phi_kerM_in_L([1, 1, 1, 1, 1, 0]), True)
check("E", "v = 15 + 7 nu^c: phi(ker M) subset L", phi_kerM_in_L([1, 1, 1, 1, 1, 7]), True)
check("E", "v = 4 x 16: phi(ker M) subset L", phi_kerM_in_L([4, 4, 4, 4, 4, 4]), True)
check("C", "control FIRES: v = one Q alone -- phi(ker M) NOT subset L",
      phi_kerM_in_L([1, 0, 0, 0, 0, 0]), False)
check("C", "control FIRES: v = (1,1,1,1,0,0) -- phi(ker M) NOT subset L",
      phi_kerM_in_L([1, 1, 1, 1, 0, 0]), False)
check("C", "control FIRES: v = a 16 minus one d^c -- NOT subset L",
      phi_kerM_in_L([1, 1, 0, 1, 1, 1]), False)
check("E", "phi(ker M) subset L  <==>  v in L, over all v in [-3,3]^6",
      all(phi_kerM_in_L(list(x)) == in_L(list(x))
          for x in itertools.product(range(-3, 4), repeat=6)), True)

# Saturation of L is load-bearing.  The step "Z.v subset L  =>  v in L" uses it.
# On the NON-saturated rank-2 sublattice 2L the same step fails, by witness.
def in_2L(v: list[int]) -> bool:
    return all(c % 2 == 0 for c in v) and in_L([c // 2 for c in v])


check("C", "control: saturation is load-bearing -- 2.(15) lies in 2L but (15) does not",
      (in_2L([2, 2, 2, 2, 2, 0]), in_2L([1, 1, 1, 1, 1, 0])), (True, False))
check("E", "L saturated: g.v in L <=> v in L, over [-3,3]^6 and every g in 1..12",
      all(in_L([g * c for c in x]) == in_L(list(x))
          for g in range(1, 13) for x in itertools.product(range(-3, 4), repeat=6)), True)

# THE FORK IS LOAD-BEARING, and it decides the seven rows.
check("E", "PULLBACK horn: phi(ker M) = Z.v (g = 1), verdict = (v in L)",
      math.gcd(*[abs(t) for t in kvals]), 1)
check("E", "KK horn: phi(ker M) = {0}, verdict = TRUE unconditionally but with "
           "an empty 4D spectrum", all(t == 0 for t in kk_ker), True)
check("E", "so the pullback-vs-projection fork is EXACTLY the bit that decides "
           "DERIVED vs DERIVED_CONDITIONAL for AC-D1..D5",
      (math.gcd(*[abs(t) for t in kvals]) != 0, all(t == 0 for t in kk_ker)), (True, True))
check("C", "control: the two horns really do give different verdicts for some v",
      phi_kerM_in_L([1, 0, 0, 0, 0, 0]) == all(t == 0 for t in kk_ker), False)

# AC-C2: the 4D SU(2)_L doublet count, on the constructed reduction.
DOUBLETS = [3, 0, 0, 1, 0, 0]     # colour-weighted SU(2) doublet count per constituent
for m in (-3, -1, 0, 1, 2, 5):
    nd = sum(DOUBLETS[i] * m * V16[i] for i in range(6))
    check("E", f"AC-C2: doublet count at 14D multiplicity m={m} is divisible by 4",
          nd % 4, 0)
check("C", "control: AC-C2's divisibility fails for a v OUTSIDE L",
      all(sum(DOUBLETS[i] * m * [1, 1, 1, 0, 1, 1][i] for i in range(6)) % 4 == 0
          for m in (1, 2, 3)), False)

# the 14D content is irrelevant: every admissible x gives the SAME 4D verdict
verdicts = set()
for freevals in itertools.product((-1, 0, 1), repeat=10):
    x = [0] * 15
    for j, fv in enumerate(freevals):
        if fv:
            for c in range(15):
                x[c] += fv * KINT[j][c]
    val = sum(K15[c] * x[c] for c in range(15))
    img = [val * c for c in V16]
    verdicts.add(M4 * Matrix(img) == Matrix([0] * 5))
check("E", "over all 59049 integer points of ker M with free coords in {-1,0,1}, "
           "the 4D anomaly verdict is CONSTANT", sorted(verdicts), [True])
verdicts_bad = set()
for freevals in itertools.product((-1, 0, 1), repeat=10):
    x = [0] * 15
    for j, fv in enumerate(freevals):
        if fv:
            for c in range(15):
                x[c] += fv * KINT[j][c]
    val = sum(K15[c] * x[c] for c in range(15))
    img = [val * c for c in [1, 0, 0, 0, 0, 0]]
    verdicts_bad.add(M4 * Matrix(img) == Matrix([0] * 5))
check("C", "control: with v = Q alone the same sweep is NOT constantly True",
      sorted(verdicts_bad), [False, True])


# ===========================================================================
# 8.  CERTIFICATE
# ===========================================================================
RESULTS.update({
    "k": KVEC, "K15": K15, "pivots": PIV, "free": FREE,
    "T_smith": divsT, "rank_phi": int(PHI16.rank()),
    "kerdim_on_kerM": kerdim_on_kerM, "rank_on_anti": int(rank_on_anti),
    "named_annihilated": named_annihilated, "max_rank_over_weightings": worst,
    "kvals": kvals, "h1": h1,
})
assert_no_float(RESULTS)

print("\n" + "=" * 78)
print(f"  checks: {NCHK}   tags: " + "  ".join(f"[{t}]x{n}" for t, n in sorted(TAGS.items())))
if FAIL:
    print(f"  FAILURES: {len(FAIL)}")
    for f in FAIL:
        print("    " + f)
    print("=" * 78)
    sys.exit(1)
print(f"  ALL {NCHK}/{NCHK} PASS -- exact rational/integer arithmetic, no float load-bearing")
print("=" * 78)
print("""
  CONSTRUCTED:  phi = v (x) k,  k = (1,-1,1,-1,1, 0,0,0,0,0,0,0,0,0,0)
                rank(phi) <= 1 for every v and every internal-blind weighting
  DECIDED:      phi(ker M) = phi(Z^15) = Z.v   (T maps ker M ONTO Z^5)
                phi(ker M) subset L  <==>  v in L  (L saturated)
  CONSEQUENCE:  LA-5's rank bound is met unconditionally and is NOT a constraint
                on any candidate.  14D anomaly cancellation contributes EXACTLY
                ZERO bits to the 4D anomaly verdict through the observation.
                The residual condition is one 6-component vector v that the 14D
                data provably cannot supply -- and v is the REPRESENTATION axis's
                own unknown, not a new one.
  CONTRARY:     on the disavowed KK horn the reduction functional k'' lies IN the
                row space of M, so phi_KK(ker M) = {0}: the criterion holds
                unconditionally by producing an IDENTICALLY EMPTY 4D spectrum.
                That kills the horn; it does not derive the rows.
""")
sys.exit(0)
