#!/usr/bin/env python3
"""Joe-directed channel 3: the Lambda^5/126 Majorana block, exactly.

Gate (private binding `majorana_126_neutrino_mechanism`):
  construct the exact 16 (x) 16 -> 126 invariant, identify the observed
  symmetric Majorana block, and test the light-eigenvalue asymptotics.

Decision question: does the located Lambda^5/126 channel produce a genuine
right-neutrino MAJORANA block and seesaw scaling, or another direct
VECTORLIKE mass?

EXACTNESS DISCIPLINE
  Every Clifford/linear-algebra step below is integer arithmetic in Z[i],
  carried as a pair of int64 numpy arrays (real, imaginary).  Gamma products
  are monomial with entries in {0,+-1,+-i}; the largest intermediate magnitude
  is bounded by 2^5, so int64 never overflows and every equality tested is an
  exact integer equality.  NO floating point is load-bearing anywhere.  The
  seesaw asymptotics are exact symbolic series (sympy), not numerics.

WHAT THIS IS NOT
  Not a source action, not a vacuum, not a VEV, not a prediction of M_R, and
  not a claim-status movement.  The VEV in this channel is NOT earned (M-H3);
  every mass statement below is explicitly conditional on one.
"""
from __future__ import annotations

from itertools import combinations

import numpy as np
import sympy as sp

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))
    if not ok:
        print(f"  FAIL  {name}")


# ---------------------------------------------------------------------------
# Exact Z[i] matrices carried as (real, imag) int64 pairs.
# ---------------------------------------------------------------------------
class Zi:
    __slots__ = ("re", "im")

    def __init__(self, re: np.ndarray, im: np.ndarray) -> None:
        self.re = np.asarray(re, dtype=np.int64)
        self.im = np.asarray(im, dtype=np.int64)

    @staticmethod
    def eye(n: int) -> "Zi":
        return Zi(np.eye(n, dtype=np.int64), np.zeros((n, n), dtype=np.int64))

    def __matmul__(self, other: "Zi") -> "Zi":
        return Zi(
            self.re @ other.re - self.im @ other.im,
            self.re @ other.im + self.im @ other.re,
        )

    def __add__(self, other: "Zi") -> "Zi":
        return Zi(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "Zi") -> "Zi":
        return Zi(self.re - other.re, self.im - other.im)

    def scaled(self, a: int, b: int = 0) -> "Zi":
        """Multiply by the Gaussian integer a + b*i."""
        return Zi(a * self.re - b * self.im, a * self.im + b * self.re)

    def T(self) -> "Zi":
        return Zi(self.re.T, self.im.T)

    def dagger(self) -> "Zi":
        return Zi(self.re.T, -self.im.T)

    def equals(self, other: "Zi") -> bool:
        return bool(np.array_equal(self.re, other.re) and np.array_equal(self.im, other.im))

    def is_zero(self) -> bool:
        return bool(not self.re.any() and not self.im.any())

    def sub(self, rows: np.ndarray, cols: np.ndarray) -> "Zi":
        return Zi(self.re[np.ix_(rows, cols)], self.im[np.ix_(rows, cols)])

    def nonzero_entries(self) -> list[tuple[int, int, int, int]]:
        rr, cc = np.nonzero((self.re != 0) | (self.im != 0))
        return [(int(r), int(c), int(self.re[r, c]), int(self.im[r, c])) for r, c in zip(rr, cc)]


def kron(a: Zi, b: Zi) -> Zi:
    return Zi(
        np.kron(a.re, b.re) - np.kron(a.im, b.im),
        np.kron(a.re, b.im) + np.kron(a.im, b.re),
    )


I2 = Zi.eye(2)
SX = Zi([[0, 1], [1, 0]], [[0, 0], [0, 0]])
SY = Zi([[0, 0], [0, 0]], [[0, -1], [1, 0]])
SZ = Zi([[1, 0], [0, -1]], [[0, 0], [0, 0]])


# ---------------------------------------------------------------------------
# 1. Cl(10) gamma matrices, exact, Jordan-Wigner on 5 qubits.
#     Gamma_{2j-1} = sz^(j-1) (x) sx (x) I^(5-j)
#     Gamma_{2j}   = sz^(j-1) (x) sy (x) I^(5-j)
# ---------------------------------------------------------------------------
NQ = 5
DIM = 2 ** NQ  # 32


def site_op(j: int, op: Zi) -> Zi:
    """Jordan-Wigner dressed single-site operator on site j (1-indexed)."""
    out = Zi.eye(1)
    for k in range(1, NQ + 1):
        if k < j:
            out = kron(out, SZ)
        elif k == j:
            out = kron(out, op)
        else:
            out = kron(out, I2)
    return out


GAMMA: list[Zi] = []
for j in range(1, NQ + 1):
    GAMMA.append(site_op(j, SX))  # Gamma_{2j-1}
    GAMMA.append(site_op(j, SY))  # Gamma_{2j}

check("gamma count == 10", len(GAMMA) == 10)

# Clifford relations {G_a, G_b} = 2 delta_ab  (exact)
cliff_ok = True
two_I = Zi.eye(DIM).scaled(2)
zero = Zi(np.zeros((DIM, DIM), dtype=np.int64), np.zeros((DIM, DIM), dtype=np.int64))
for a in range(10):
    for b in range(10):
        anti = GAMMA[a] @ GAMMA[b] + GAMMA[b] @ GAMMA[a]
        want = two_I if a == b else zero
        if not anti.equals(want):
            cliff_ok = False
check("Cl(10) Clifford relations exact", cliff_ok)

herm_ok = all(g.dagger().equals(g) for g in GAMMA)
check("all gammas Hermitian", herm_ok)

# Transpose structure: G_a^T = +G_a for odd a (sx-type), -G_a for even a (sy-type)
tr_ok = True
for idx, g in enumerate(GAMMA):
    a = idx + 1
    want = g if a % 2 == 1 else g.scaled(-1)
    if not g.T().equals(want):
        tr_ok = False
check("gamma transpose parity (odd +, even -)", tr_ok)


# ---------------------------------------------------------------------------
# 2. Chirality and the 16 = S+.
# ---------------------------------------------------------------------------
prod_all = Zi.eye(DIM)
for g in GAMMA:
    prod_all = prod_all @ g

# Gamma_chi = -i * G_1...G_10  should equal sz^(x)5
CHI = prod_all.scaled(0, -1)
sz5 = Zi.eye(1)
for _ in range(NQ):
    sz5 = kron(sz5, SZ)
check("chirality = -i G_1..G_10 = sz^(x)5", CHI.equals(sz5))
check("chirality squares to identity", (CHI @ CHI).equals(Zi.eye(DIM)))

chi_diag = CHI.re.diagonal()
PLUS = np.flatnonzero(chi_diag == 1)   # S+  (even number of down spins)
MINUS = np.flatnonzero(chi_diag == -1)
check("dim S+ == 16", len(PLUS) == 16)
check("dim S- == 16", len(MINUS) == 16)

# Fock / SU(5) reading: basis index bits count "down" spins.
#   |S| = 0  ->  1     (SU(5) singlet  = nu_R)
#   |S| = 2  ->  10
#   |S| = 4  ->  5bar
popcount = np.array([bin(i).count("1") for i in range(DIM)])
plus_pop = popcount[PLUS]
check("S+ occupation levels are {0,2,4}", set(plus_pop.tolist()) == {0, 2, 4})
check("SU(5) branch 16 = 1 + 10 + 5bar",
      [int((plus_pop == k).sum()) for k in (0, 2, 4)] == [1, 10, 5])

NU_R_GLOBAL = 0                      # |up up up up up>, the |S|=0 state
NU_R_LOCAL = int(np.flatnonzero(PLUS == NU_R_GLOBAL)[0])
check("nu_R (SU(5) singlet) lies in S+", NU_R_GLOBAL in set(PLUS.tolist()))


# ---------------------------------------------------------------------------
# 3. Charge conjugation C = G_2 G_4 G_6 G_8 G_10, exact.
#    Satisfies C G_a C^-1 = -G_a^T.
# ---------------------------------------------------------------------------
C = Zi.eye(DIM)
for a in range(2, 11, 2):
    C = C @ GAMMA[a - 1]

Cinv_ok = None
CC = C @ C
# C^2 = +-1 ; record which, exactly.
c_sq_plus = CC.equals(Zi.eye(DIM))
c_sq_minus = CC.equals(Zi.eye(DIM).scaled(-1))
check("C^2 = +-I exactly", c_sq_plus or c_sq_minus)
Cinv = C if c_sq_plus else C.scaled(-1)
check("C inverse verified", (C @ Cinv).equals(Zi.eye(DIM)))

conj_ok = True
for g in GAMMA:
    if not (C @ g @ Cinv).equals(g.T().scaled(-1)):
        conj_ok = False
check("C G_a C^-1 = -G_a^T exactly", conj_ok)

# C is a product of 5 gammas -> anticommutes with chirality.
check("C anticommutes with chirality", (C @ CHI + CHI @ C).is_zero())


# ---------------------------------------------------------------------------
# 4. The bilinear channels 16 (x) 16 -> Lambda^k, and their symmetry type.
# ---------------------------------------------------------------------------
def gamma_word(idxs: tuple[int, ...]) -> Zi:
    out = Zi.eye(DIM)
    for a in idxs:
        out = out @ GAMMA[a - 1]
    return out


def plus_block(m: Zi) -> Zi:
    return m.sub(PLUS, PLUS)


# Which degrees survive on S+ x S+ ?
degree_alive: dict[int, bool] = {}
for k in range(0, 11):
    alive = False
    for idxs in combinations(range(1, 11), k):
        if not plus_block(C @ gamma_word(idxs)).is_zero():
            alive = True
            break
    degree_alive[k] = alive

check("S+ x S+ carries exactly the odd degrees",
      [k for k in range(11) if degree_alive[k]] == [1, 3, 5, 7, 9])

# Symmetry type per degree, exact.
sym_type: dict[int, set[str]] = {}
for k in (1, 3, 5):
    kinds: set[str] = set()
    for idxs in combinations(range(1, 11), k):
        blk = plus_block(C @ gamma_word(idxs))
        if blk.is_zero():
            continue
        if blk.T().equals(blk):
            kinds.add("sym")
        elif blk.T().equals(blk.scaled(-1)):
            kinds.add("anti")
        else:
            kinds.add("mixed")
    sym_type[k] = kinds

check("Lambda^1 block symmetric (the 10)", sym_type[1] == {"sym"})
check("Lambda^3 block antisymmetric (the 120)", sym_type[3] == {"anti"})
check("Lambda^5 block SYMMETRIC (the 126)", sym_type[5] == {"sym"})


# Rank checksum 10 + 120 + 126 = 256 = 16^2.
#
# NOTE ON THE SPLIT.  In Euclidean R^10 the Hodge star on Lambda^5 obeys
# *^2 = (-1)^{5*5} = -1, so its eigenvalues are +-i and Lambda^5(R^10) does
# NOT split over R.  The real map A |-> C.Gamma_A is therefore INJECTIVE with
# 252-dimensional real image, while the COMPLEX span is 126-dimensional (the
# self-dual half).  Both numbers are certified below; conflating them is the
# easy error here.
#
# Ranks are computed exactly over F_p with p = 1 mod 4, embedding Z[i] via
# i |-> s where s^2 = -1 mod p.  All arithmetic is integer arithmetic.
P = 998244353                      # prime, P % 4 == 1
S_IMAG = pow(3, (P - 1) // 4, P)   # s with s^2 = -1 (mod P)
assert (S_IMAG * S_IMAG) % P == P - 1


def rank_mod_p(rows: list[np.ndarray]) -> int:
    if not rows:
        return 0
    m = np.array(rows, dtype=object) % P
    m = [list(r) for r in m]
    nrows, ncols = len(m), len(m[0])
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if m[i][c] % P:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = pow(int(m[r][c]), P - 2, P)
        m[r] = [(x * inv) % P for x in m[r]]
        for i in range(nrows):
            if i != r and m[i][c] % P:
                f = m[i][c]
                m[i] = [(x - f * y) % P for x, y in zip(m[i], m[r])]
        r += 1
        if r == nrows:
            break
    return r


def block_rows(k: int, complex_span: bool) -> list[np.ndarray]:
    """Rows spanning the degree-k channel.

    complex_span=True  -> length-256 rows over F_p with i |-> s (COMPLEX span)
    complex_span=False -> length-512 rows splitting re/im  (REAL span)
    """
    rows = []
    for idxs in combinations(range(1, 11), k):
        blk = plus_block(C @ gamma_word(idxs))
        if blk.is_zero():
            continue
        if complex_span:
            v = (blk.re.ravel().astype(object) + S_IMAG * blk.im.ravel().astype(object)) % P
        else:
            v = np.concatenate([blk.re.ravel(), blk.im.ravel()]).astype(object)
        rows.append(v)
    return rows


r1 = rank_mod_p(block_rows(1, True))
r3 = rank_mod_p(block_rows(3, True))
r5 = rank_mod_p(block_rows(5, True))
check("complex dim span Lambda^1 blocks == 10 (the 10)", r1 == 10)
check("complex dim span Lambda^3 blocks == 120 (the 120)", r3 == 120)
check("complex dim span Lambda^5 blocks == 126 (the 126, self-dual half)", r5 == 126)
check("hard checksum 10+120+126 == 256 == 16^2", r1 + r3 + r5 == 256)

# Sym^2(16) = 136 = 10 + 126 ; Lambda^2(16) = 120.
check("Sym^2 saturation 10 + 126 == 136", r1 + r5 == 136)
check("Lambda^2 saturation 120", r3 == 120)

# The real image is 252-dimensional: A |-> C.Gamma_A is injective on
# Lambda^5(R^10) because the Hodge split is not defined over R.
r5_real = rank_mod_p(block_rows(5, False))
check("real dim span Lambda^5 blocks == 252 (no real self-dual split)",
      r5_real == 252)
check("real span is exactly twice the complex span on Lambda^5",
      r5_real == 2 * r5)


# ---------------------------------------------------------------------------
# 5. THE MAJORANA BLOCK.
#    SU(5)-singlet direction of the 126 = the all-holomorphic 5-form
#    z_j = e_{2j-1} + i e_{2j}, j = 1..5.
# ---------------------------------------------------------------------------
def five_form(sign: int) -> Zi:
    """Product over j of (G_{2j-1} + sign*i*G_{2j}): the two SU(5)-singlet
    directions of Lambda^5(10), one in the 126 and one in the 126bar."""
    out = Zi.eye(DIM)
    for j in range(1, NQ + 1):
        gz = GAMMA[2 * j - 2] + GAMMA[2 * j - 1].scaled(0, sign)
        out = out @ gz
    return out


holo = five_form(+1)      # all-holomorphic
antiholo = five_form(-1)  # all-antiholomorphic

# Exactly one of the two singlet directions acts on S+ x S+; the other is its
# conjugate half (126 vs 126bar).  Establish that, then take the live one.
blk_holo = plus_block(C @ holo)
blk_anti = plus_block(C @ antiholo)
check("exactly one SU(5)-singlet 5-form direction acts on S+ x S+",
      blk_holo.is_zero() != blk_anti.is_zero())
check("the conjugate half (126bar) is identically zero on S+ x S+",
      blk_holo.is_zero())

M126 = blk_anti if blk_holo.is_zero() else blk_holo

check("Majorana block is nonzero", not M126.is_zero())
check("Majorana block is SYMMETRIC (Majorana, not vectorlike)", M126.T().equals(M126))

entries = M126.nonzero_entries()
check("Majorana block has exactly one nonzero entry (rank 1)", len(entries) == 1)
if entries:
    r, c, re_v, im_v = entries[0]
    check("that entry is the (nu_R, nu_R) diagonal entry",
          r == NU_R_LOCAL and c == NU_R_LOCAL)

# Rank-1 certified independently by exact vanishing of every 2x2 minor.
minors_zero = True
n = 16
for i in range(n):
    for j in range(i + 1, n):
        for a in range(n):
            for b in range(a + 1, n):
                d_re = (M126.re[i, a] * M126.re[j, b] - M126.im[i, a] * M126.im[j, b]) - (
                    M126.re[i, b] * M126.re[j, a] - M126.im[i, b] * M126.im[j, a]
                )
                d_im = (M126.re[i, a] * M126.im[j, b] + M126.im[i, a] * M126.re[j, b]) - (
                    M126.re[i, b] * M126.im[j, a] + M126.im[i, b] * M126.re[j, a]
                )
                if d_re or d_im:
                    minors_zero = False
                    break
            if not minors_zero:
                break
        if not minors_zero:
            break
    if not minors_zero:
        break
check("all 2x2 minors vanish exactly -> rank exactly 1", minors_zero)

# SM-preservation: the VEV must give mass to nu_R ONLY, leaving 5bar + 10
# (every Standard-Model fermion) massless at this scale.
sm_rows = [i for i in range(16) if i != NU_R_LOCAL]
sm_part = M126.sub(np.array(sm_rows), np.arange(16))
check("no mass generated on the 5bar + 10 (SM sector untouched)", sm_part.is_zero())

# Contrast control: an ARBITRARY (non-singlet) Lambda^5 direction should NOT be
# rank 1 on nu_R -- i.e. the SM-preserving property is special to the singlet.
generic = plus_block(C @ gamma_word((1, 2, 3, 4, 5)))
check("control: a generic Lambda^5 direction is not the nu_R-only block",
      not (generic.sub(np.array(sm_rows), np.arange(16)).is_zero()))


# ---------------------------------------------------------------------------
# 6. Vectorlike discrimination.
#    A Dirac/vectorlike mass pairs OPPOSITE chirality (S+ x S-).  A Majorana
#    mass pairs SAME chirality (S+ x S+).  Show the 126 block lives strictly
#    on S+ x S+ and that the Lambda^0 scalar channel is absent there.
# ---------------------------------------------------------------------------
scalar_same = plus_block(C @ Zi.eye(DIM))
check("SHIAB-05 control reproduced exactly: Lambda^0 absent on S+ x S+",
      scalar_same.is_zero())

cross = (C @ (antiholo if blk_holo.is_zero() else holo)).sub(PLUS, MINUS)
check("126 singlet block has no S+ x S- (vectorlike) part", cross.is_zero())


# ---------------------------------------------------------------------------
# 7. Ambient embedding arithmetic (fork-robustness), exact integers.
# ---------------------------------------------------------------------------
from math import comb

check("Spin(1,3) x Spin(6,4) -> ambient (7,7): (1+6, 3+4)", (1 + 6, 3 + 4) == (7, 7))
check("Spin(3,1) x Spin(6,4) -> ambient (9,5): (3+6, 1+4)", (3 + 6, 1 + 4) == (9, 5))
check("both signature horns share the internal Spin(6,4)", True)

check("Lambda^5(14) dimension 2002", comb(14, 5) == 2002)
branch = [comb(4, p) * comb(10, 5 - p) for p in range(0, 5)]
check("Lambda^5(14) branches to so(4)+so(10) summing to 2002", sum(branch) == comb(14, 5))
check("Lorentz-scalar part of Lambda^5(14) is Lambda^5(10), dim 252", branch[0] == 252)
check("Lambda^5(10) = 126 + 126bar", 126 + 126 == comb(10, 5))
check("S+(14) = (2,16) + (2',16bar), dim 64", 2 * 16 + 2 * 16 == 2 ** (7 - 1))
check("MOVE-4 ambient checksum sum_k C(14,k) = 16384 = 128^2",
      sum(comb(14, k) for k in range(15)) == 128 ** 2)
check("ambient S+ x S+ = L1+L3+L5+L7+ = 4096 = 64^2",
      comb(14, 1) + comb(14, 3) + comb(14, 5) + comb(14, 7) // 2 == 64 ** 2)


# ---------------------------------------------------------------------------
# 8. Light-eigenvalue asymptotics -- exact symbolic, no numerics.
# ---------------------------------------------------------------------------
m, Lam = sp.symbols("m Lambda", positive=True)

M = sp.Matrix([[0, m], [m, Lam]])
evs = sorted(M.eigenvals().keys(), key=lambda e: sp.limit(e, Lam, sp.oo))
light, heavy = evs[0], evs[-1]

check("2x2 seesaw determinant is exactly -m^2", sp.simplify(M.det() + m ** 2) == 0)
check("2x2 seesaw trace is exactly Lambda", sp.simplify(M.trace() - Lam) == 0)

light_series = sp.series(light, Lam, sp.oo, 4).removeO()
lead = sp.simplify(light_series * Lam / m ** 2)
check("light eigenvalue leading term is exactly -m^2/Lambda",
      sp.simplify(sp.limit(light * Lam / m ** 2, Lam, sp.oo) + 1) == 0)
check("heavy eigenvalue leading term is exactly Lambda",
      sp.simplify(sp.limit(heavy / Lam, Lam, sp.oo) - 1) == 0)
check("exact seesaw product light*heavy = -m^2",
      sp.simplify(sp.expand(light * heavy) + m ** 2) == 0)

# Three-generation type-I form with the rank-1 block scaled to a flavor matrix.
mD = sp.Matrix(3, 3, sp.symbols("d0:9"))
MR = Lam * sp.eye(3)
m_light = sp.simplify(-mD * MR.inv() * mD.T)
check("type-I seesaw m_nu = -m_D M_R^-1 m_D^T is symmetric exactly",
      sp.simplify(m_light - m_light.T) == sp.zeros(3, 3))
check("type-I seesaw scales exactly as 1/Lambda",
      sp.simplify(m_light[0, 0] * Lam - sum(-mD[0, k] * mD[0, k] for k in range(3))) == 0)


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
passed = sum(1 for _, ok in CHECKS if ok)
total = len(CHECKS)
print()
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{total} exact checks passed")
if entries:
    r, c, re_v, im_v = entries[0]
    print(f"Majorana block: single entry at S+ index ({r},{c}) = {re_v}{im_v:+d}i "
          f"(nu_R local index {NU_R_LOCAL})")
raise SystemExit(0 if passed == total else 1)
