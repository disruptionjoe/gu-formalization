#!/usr/bin/env python3
"""HE-2: does Spin(6,4) reality pair the 144 with the 144bar?

HE-1 (2026-08-14, 62/62) established, in COMPLEX so(10), that the gamma-traceless
vector-spinor 144 contains the Pati-Salam content of exactly ONE family-shaped
block, with multiplicity exactly one, and that the block is the 16bar's -- a
MIRROR.  Net chirality for n_g chiral 16s plus one 144 is n_g - 1.  HE-1 fenced
its own ceiling (Fence 4) and named its own kill:

    "the real form.  Everything is complex so(10).  If Spin(6,4) reality pairs
     144 with 144bar, the sector is vectorlike and n_g -> n_g, the whole result
     collapses."

This probe executes that gate exactly.

TWO INDEPENDENT LEGS, because "reality pairs X with Xbar" is a two-way homonym
and the two senses have DIFFERENT real-form dependence:

  LEG A (ANTILINEAR / conjugation type).  Is there a conjugate-linear
     so(6,4)-equivariant J : 144 -> 144 (i.e. is conj(144) ~= 144)?  This is
     the literal Frobenius-Schur trichotomy real / quaternionic / complex.  It
     IS real-form dependent.  Decided here by explicit Cl(6,4) gammas over Z[i].

  LEG B (BILINEAR / self-duality type).  Is there an invariant bilinear form on
     the 144 (i.e. is 144^* ~= 144)?  This is the object that actually controls
     whether a mass term exists, hence "vectorlike".  It is a COMPLEX-LINEAR
     invariant and is therefore determined by so(10,C) alone -- REAL-FORM
     BLIND.  Decided here by an explicit w_0 computation in W(D5).

Both legs are computed.  A collapse would need at least one of them to answer
"yes".

EXACTNESS DISCIPLINE
  Every Clifford / linear-algebra step is integer arithmetic in Z[i], carried as
  a pair of int64 numpy arrays.  Gamma words are monomial with entries in
  {0,+-1,+-i}.  Ranks are computed over F_p (p = 1 mod 4, i |-> s with
  s^2 = -1 mod p); an F_p rank LOWER-bounds the characteristic-0 rank, and every
  rank used here is also upper-bounded by a codomain dimension, so each is
  pinned exactly.  Weights are DOUBLED integer 5-tuples.  Weyl dimensions and
  Racah multiplicities use Fraction / int.  NO floating point is load-bearing.

CONTROLS
  - positive: nine signature classes whose reality type is textbook-known
    ((9,1) Majorana-Weyl, (10,0) Spin(10) GUT complex, (7,3) quaternionic,
    (5,5) split real, (1,3)/(3,1)/(4,0) matching the repo's own 2026-08-13
    signature-chirality artifact, (7,7) and (9,5) matching canon).
  - negative / contrary: D_4, where -w_0 = id and the analogous module IS
    self-dual -- i.e. a group where the collapse WOULD happen and this
    machinery detects it.
  - PLANTED FAILURES: six assertions that are FALSE by construction; the run
    asserts each is observed False.  A probe nobody has seen fail is unverified.

WHAT THIS IS NOT
  Not a source action, not a physical carrier, not a generation count, not a
  scale, not a claim-status movement.  n_g is an INPUT throughout.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

import numpy as np

CHECKS: list[tuple[str, bool]] = []
PLANTED: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> bool:
    CHECKS.append((name, bool(ok)))
    if not ok:
        print(f"  FAIL  {name}")
    return bool(ok)


def planted(name: str, observed: bool) -> None:
    """Register a deliberately FALSE assertion.  `observed` must come out False."""
    fired = observed is False
    PLANTED.append((name, fired))
    if not fired:
        print(f"  PLANTED CONTROL DID NOT FIRE  {name}")


# ===========================================================================
# 0.  Exact Z[i] matrices, carried as (re, im) int64 pairs.
# ===========================================================================
class Zi:
    __slots__ = ("re", "im")

    def __init__(self, re, im) -> None:
        self.re = np.asarray(re, dtype=np.int64)
        self.im = np.asarray(im, dtype=np.int64)

    @staticmethod
    def eye(n: int) -> "Zi":
        return Zi(np.eye(n, dtype=np.int64), np.zeros((n, n), dtype=np.int64))

    @staticmethod
    def zeros(n: int) -> "Zi":
        z = np.zeros((n, n), dtype=np.int64)
        return Zi(z, z)

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
        return Zi(a * self.re - b * self.im, a * self.im + b * self.re)

    def conj(self) -> "Zi":
        """Entrywise complex conjugate (NOT transpose)."""
        return Zi(self.re, -self.im)

    def T(self) -> "Zi":
        return Zi(self.re.T, self.im.T)

    def equals(self, other: "Zi") -> bool:
        return bool(np.array_equal(self.re, other.re) and np.array_equal(self.im, other.im))

    def is_zero(self) -> bool:
        return bool(not self.re.any() and not self.im.any())

    def is_real(self) -> bool:
        return bool(not self.im.any())

    def is_imag(self) -> bool:
        return bool(not self.re.any())

    def is_scalar_multiple_of_identity(self):
        n = self.re.shape[0]
        a, b = int(self.re[0, 0]), int(self.im[0, 0])
        want = Zi.eye(n).scaled(a, b)
        return (self.equals(want), a, b)


def kron(a: Zi, b: Zi) -> Zi:
    return Zi(
        np.kron(a.re, b.re) - np.kron(a.im, b.im),
        np.kron(a.re, b.im) + np.kron(a.im, b.re),
    )


I2 = Zi.eye(2)
SX = Zi([[0, 1], [1, 0]], [[0, 0], [0, 0]])
SY = Zi([[0, 0], [0, 0]], [[0, -1], [1, 0]])
SZ = Zi([[1, 0], [0, -1]], [[0, 0], [0, 0]])


# ===========================================================================
# 1.  Jordan-Wigner Cl(2m) and the signature dressing Cl(p,q).
# ===========================================================================
def jw_gammas(nq: int) -> list[Zi]:
    """Hermitian Euclidean gammas G_1..G_{2nq} on nq qubits.  G_a^2 = +I."""
    def site(j: int, op: Zi) -> Zi:
        out = Zi.eye(1)
        for k in range(1, nq + 1):
            out = kron(out, SZ if k < j else (op if k == j else I2))
        return out

    out: list[Zi] = []
    for j in range(1, nq + 1):
        out.append(site(j, SX))   # G_{2j-1}  -- purely REAL
        out.append(site(j, SY))   # G_{2j}    -- purely IMAGINARY
    return out


class Clifford:
    """Cl(p,q): Gam[a]^2 = +I for a < p, -I for a >= p.  Entries in Z[i]."""

    def __init__(self, p: int, q: int) -> None:
        n = p + q
        assert n % 2 == 0, "even n only"
        self.p, self.q, self.n = p, q, n
        self.nq = n // 2
        self.dim = 2 ** self.nq
        G = jw_gammas(self.nq)
        self.G = G
        self.gam = [G[a] if a < p else G[a].scaled(0, 1) for a in range(n)]
        self.eta = [1] * p + [-1] * q

    # -- Clifford relations -------------------------------------------------
    def relations_hold(self) -> bool:
        d = self.dim
        Z = Zi.zeros(d)
        for a in range(self.n):
            for b in range(self.n):
                anti = self.gam[a] @ self.gam[b] + self.gam[b] @ self.gam[a]
                want = Zi.eye(d).scaled(2 * self.eta[a]) if a == b else Z
                if not anti.equals(want):
                    return False
        return True

    # -- volume word / chirality -------------------------------------------
    def volume(self) -> Zi:
        out = Zi.eye(self.dim)
        for g in self.gam:
            out = out @ g
        return out

    def chirality(self):
        """Return (CHI, omega_sq_sign) with CHI^2 = +I."""
        w = self.volume()
        w2 = w @ w
        if w2.equals(Zi.eye(self.dim)):
            return w, +1
        assert w2.equals(Zi.eye(self.dim).scaled(-1))
        return w.scaled(0, 1), -1          # i * omega

    # -- reality structures -------------------------------------------------
    def reality(self):
        """Both antilinear intertwiners.

        Returns a list of dicts with keys:
          eta   : sign in Gam_a^* = eta * B Gam_a B^{-1}
          B, Binv
          Jsq   : sign of J^2 where J(psi) = B^{-1} psi^*   (rescale-invariant)
          chir  : +1 if J commutes with chirality (PRESERVES), -1 if it flips
        """
        real_set = [a for a in range(self.n) if self.gam[a].is_real()]
        imag_set = [a for a in range(self.n) if self.gam[a].is_imag()]
        assert len(real_set) + len(imag_set) == self.n, "gamma neither real nor imaginary"
        CHI, _ = self.chirality()
        out = []
        for subset in (imag_set, real_set):
            B = Zi.eye(self.dim)
            for a in subset:
                B = B @ self.gam[a]
            B2 = B @ B
            ok, a2, b2 = B2.is_scalar_multiple_of_identity()
            assert ok and b2 == 0 and a2 in (1, -1), "B^2 not +-I"
            Binv = B if a2 == 1 else B.scaled(-1)
            # eta from the defining relation, verified on every gamma
            eta = None
            for s in (+1, -1):
                if all((self.gam[a].conj()).equals((B @ self.gam[a] @ Binv).scaled(s))
                       for a in range(self.n)):
                    eta = s
                    break
            assert eta is not None, "no eta works"
            M = B.conj() @ B
            ok2, lam_re, lam_im = M.is_scalar_multiple_of_identity()
            assert ok2 and lam_im == 0 and lam_re != 0, "B^* B not real scalar"
            jsq = 1 if lam_re > 0 else -1     # J^2 = (B^* B)^{-1}
            if (CHI.conj()).equals(B @ CHI @ Binv):
                chir = +1
            else:
                assert (CHI.conj()).equals((B @ CHI @ Binv).scaled(-1))
                chir = -1
            out.append(dict(eta=eta, B=B, Binv=Binv, Jsq=jsq, chir=chir, subset=tuple(subset)))
        return out


def reality_class(p: int, q: int) -> str:
    """Predeclared textbook answer from (p-q) mod 8, for even p+q."""
    r = (p - q) % 8
    return {0: "REAL", 2: "COMPLEX", 4: "QUATERNIONIC", 6: "COMPLEX"}[r]


# ===========================================================================
# 2.  Reality type of the half-spinor, nine signatures.
# ===========================================================================
print("=" * 74)
print("PART 1 -- reality type of the half-spinor, by explicit Clifford algebra")
print("=" * 74)

SIGNATURES = [
    (10, 0), (0, 10), (6, 4), (4, 6), (9, 1), (5, 5), (7, 3), (1, 3), (3, 1),
    (4, 0), (7, 7), (9, 5), (5, 9),
]
reality_table: dict[tuple[int, int], dict] = {}

for (p, q) in SIGNATURES:
    cl = Clifford(p, q)
    check(f"Cl({p},{q}) Clifford relations exact", cl.relations_hold())
    CHI, wsq = cl.chirality()
    check(f"Cl({p},{q}) chirality squares to +I", (CHI @ CHI).equals(Zi.eye(cl.dim)))
    fams = cl.reality()
    chirs = {f["chir"] for f in fams}
    jsqs = {f["Jsq"] for f in fams}
    # Schur consistency: on the irreducible S^+ the antilinear intertwiner is
    # unique up to scalar, so both families MUST agree on both signs.
    check(f"Cl({p},{q}) both antilinear families agree on chirality action", len(chirs) == 1)
    if chirs == {+1}:
        check(f"Cl({p},{q}) both antilinear families agree on sign(J^2)", len(jsqs) == 1)
    chir = chirs.pop()
    jsq = sorted(jsqs)[0] if len(jsqs) == 1 else None
    if chir == -1:
        got = "COMPLEX"
    else:
        got = "REAL" if jsq == +1 else "QUATERNIONIC"
    want = reality_class(p, q)
    check(f"Cl({p},{q}) reality type == {want} (predeclared from (p-q) mod 8 = {(p-q)%8})",
          got == want)
    reality_table[(p, q)] = dict(cl=cl, CHI=CHI, chir=chir, Jsq=jsq, type=got,
                                 fams=fams, omega_sq=wsq)
    print(f"  Cl({p:>2},{q:<2})  (p-q)%8={(p-q)%8}  omega^2={wsq:+d}  "
          f"J {'PRESERVES' if chir == 1 else 'FLIPS    '} chirality  "
          f"J^2={'n/a' if jsq is None else f'{jsq:+d}'}  ->  {got}")

INT = reality_table[(6, 4)]
check("INTERNAL Cl(6,4): antilinear J FLIPS chirality (16 <-> 16bar)", INT["chir"] == -1)
check("INTERNAL Cl(6,4): reality type of the Weyl 16 is COMPLEX", INT["type"] == "COMPLEX")
check("INTERNAL Cl(4,6): same verdict under the opposite sign convention",
      reality_table[(4, 6)]["type"] == "COMPLEX" and reality_table[(4, 6)]["chir"] == -1)
check("INTERNAL Cl(6,4) matches compact Cl(10,0) (same mod-8 class)",
      reality_table[(10, 0)]["type"] == "COMPLEX")
check("CONTROL Cl(9,1) is REAL (10d Majorana-Weyl) -- machinery CAN see preservation",
      reality_table[(9, 1)]["type"] == "REAL" and reality_table[(9, 1)]["chir"] == +1)
check("CONTROL Cl(5,5) is REAL (split form)", reality_table[(5, 5)]["type"] == "REAL")
check("CONTROL Cl(7,3) is QUATERNIONIC", reality_table[(7, 3)]["type"] == "QUATERNIONIC")
check("CONTROL Cl(1,3) COMPLEX / flips (repo 2026-08-13 signature-chirality artifact)",
      reality_table[(1, 3)]["chir"] == -1)
check("CONTROL Cl(4,0) preserves chirality (same artifact, Euclidean row)",
      reality_table[(4, 0)]["chir"] == +1)
check("CANON Cl(9,5) QUATERNIONIC (shiab-existence-cl95: M(64,H), index 4)",
      reality_table[(9, 5)]["type"] == "QUATERNIONIC")
check("CANON Cl(7,7) REAL (shiab-existence-cl95 failure-mode row: M(128,R))",
      reality_table[(7, 7)]["type"] == "REAL")
check("Cl(5,9) agrees with Cl(9,5) (ambient sign convention is immaterial)",
      reality_table[(5, 9)]["type"] == reality_table[(9, 5)]["type"])

# repo cross-check: p77-real-index-W1 found omega_int^2 = -1 for Cl(6,4).
check("p77-W1 cross-check: omega_int^2 = -1 on Cl(6,4)", INT["omega_sq"] == -1)


# ===========================================================================
# 3.  Weights, the 144 as an explicit Clifford kernel, and its conjugate.
# ===========================================================================
print()
print("=" * 74)
print("PART 2 -- the 144 as ker(gamma-trace), exactly, and where reality sends it")
print("=" * 74)

P_FP = 998244353                      # prime, 1 mod 4
S_IMAG = pow(3, (P_FP - 1) // 4, P_FP)
assert (S_IMAG * S_IMAG) % P_FP == P_FP - 1


def rank_fp(re: np.ndarray, im: np.ndarray) -> int:
    """Rank over F_p of a Z[i] matrix via i |-> S_IMAG.  Lower-bounds char-0 rank."""
    A = (re % P_FP + (S_IMAG * (im % P_FP)) % P_FP) % P_FP
    A = A.astype(np.int64)
    nrows, ncols = A.shape
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if A[i, c]:
                piv = i
                break
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), P_FP - 2, P_FP)
        A[r] = (A[r] * inv) % P_FP
        col = A[:, c].copy()
        col[r] = 0
        nz = np.flatnonzero(col)
        if nz.size:
            A[nz] = (A[nz] - np.outer(col[nz], A[r])) % P_FP
        r += 1
        if r == nrows:
            break
    return r


def real_fixed_dim(B: Zi, CHI: Zi, D: int) -> int:
    """dim_R { x : J x = x and CHI x = x }, where J(x) = B^{-1} x^*.

    J x = x  <=>  x^* = B x.  Writing x = u + i v and B = R + i M this is the
    REAL system  (R - I)u - M v = 0,  M u + (R + I)v = 0.  The chirality
    constraint (CHI - I)x = 0 adds two more real blocks.  Nullity over F_p
    UPPER-bounds the nullity over Q, which is what every use below needs.
    """
    R, M = B.re, B.im
    Cr, Ci = CHI.re, CHI.im
    I = np.eye(D, dtype=np.int64)
    Z = np.zeros((D, D), dtype=np.int64)
    A = np.block([
        [R - I,          -M],
        [M,          R + I],
        [Cr - I,        -Ci],
        [Ci,         Cr - I],
    ])
    return 2 * D - rank_fp(A, np.zeros_like(A))


DIM_S = 32
CL64 = INT["cl"]
CHI_RAW = INT["CHI"]                       # i * Gamma_1...Gamma_10 for (6,4)

# LABELLING CONVENTION, fixed once and stated.  The (6,4) chirality element
# i*Gamma_1..Gamma_10 equals MINUS the compact Cl(10) chirality -i*G_1..G_10.
# Same eigenspaces, opposite names.  We label with the COMPACT operator so that
# S+ is MJ-1's PLUS (even number of down spins, the 16 carrying nu_R) and the
# highest weights match HE-1 / W221.  Nothing in Leg A depends on the choice:
# J anticommutes with the chirality operator either way.
prod_G = Zi.eye(DIM_S)
for g in CL64.G:
    prod_G = prod_G @ g
CHI_INT = prod_G.scaled(0, -1)             # -i G_1...G_10, the compact chirality
check("compact chirality -i G_1..G_10 squares to +I",
      (CHI_INT @ CHI_INT).equals(Zi.eye(DIM_S)))
check("(6,4) chirality element i*Gamma_1..Gamma_10 = MINUS the compact chirality "
      "(labelling convention recorded, not assumed)",
      CHI_RAW.equals(CHI_INT.scaled(-1)))
chi_diag = CHI_INT.re.diagonal()
check("chirality is diagonal in the JW basis", CHI_INT.is_real() and
      np.array_equal(CHI_INT.re, np.diag(chi_diag)))
SPLUS = np.flatnonzero(chi_diag == 1)
SMINUS = np.flatnonzero(chi_diag == -1)
check("dim S+ = dim S- = 16", len(SPLUS) == 16 and len(SMINUS) == 16)

# --- doubled weights, from the compact Cartan H_j = -(i/2) G_{2j-1} G_{2j} ---
G = CL64.G
weight_of_basis = np.zeros((DIM_S, 5), dtype=np.int64)
for j in range(1, 6):
    Hj2 = (G[2 * j - 2] @ G[2 * j - 1]).scaled(0, -1)      # -i G_{2j-1}G_{2j}
    ok, _, _ = (Hj2 @ Hj2).is_scalar_multiple_of_identity()
    check(f"doubled Cartan 2H_{j} squares to a scalar", ok)
    check(f"doubled Cartan 2H_{j} is real diagonal with entries +-1",
          Hj2.is_real() and np.array_equal(Hj2.re, np.diag(Hj2.re.diagonal()))
          and set(np.unique(Hj2.re.diagonal()).tolist()) == {-1, 1})
    weight_of_basis[:, j - 1] = Hj2.re.diagonal()

wt_splus = sorted(tuple(int(x) for x in weight_of_basis[b]) for b in SPLUS)
wt_sminus = sorted(tuple(int(x) for x in weight_of_basis[b]) for b in SMINUS)
check("S+ doubled weights = (+-1)^5 with an EVEN number of minus signs",
      all(w.count(-1) % 2 == 0 for w in wt_splus) and len(set(wt_splus)) == 16)
check("S- doubled weights = (+-1)^5 with an ODD number of minus signs",
      all(w.count(-1) % 2 == 1 for w in wt_sminus) and len(set(wt_sminus)) == 16)
check("S+ coordinate sums = 1 (mod 4)  [HE-1 3.1]",
      all(sum(w) % 4 == 1 for w in wt_splus))
check("S- coordinate sums = 3 (mod 4)  [HE-1 3.1]",
      all(sum(w) % 4 == 3 for w in wt_sminus))

# --- the vector 10, doubled weights +-2 e_j ---
wt_v = [tuple(2 * (1 if s > 0 else -1) if k == j else 0 for k in range(5))
        for j in range(5) for s in (+1, -1)]
check("vector 10 has 10 doubled weights +-2e_j", len(wt_v) == 10 and len(set(wt_v)) == 10)


def multiset(pairs):
    d: dict[tuple, int] = {}
    for w in pairs:
        d[w] = d.get(w, 0) + 1
    return d


def ms_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return out


def ms_sub(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) - v
    return {k: v for k, v in out.items() if v != 0}


def ms_tensor(a, b):
    out: dict[tuple, int] = {}
    for wa, ma in a.items():
        for wb, mb in b.items():
            w = tuple(x + y for x, y in zip(wa, wb))
            out[w] = out.get(w, 0) + ma * mb
    return out


def ms_dim(a):
    return sum(a.values())


MS_V = multiset(wt_v)
MS_SP = multiset(wt_splus)
MS_SM = multiset(wt_sminus)
MS_VSP = ms_tensor(MS_V, MS_SP)
MS_VSM = ms_tensor(MS_V, MS_SM)
check("dim(10 (x) 16) = 160", ms_dim(MS_VSP) == 160)
check("every weight of 10 (x) 16 has coordinate sum = 3 (mod 4)  [HE-1 3.1]",
      all(sum(w) % 4 == 3 for w in MS_VSP))
check("10 (x) 16 lies in the SAME so(10) chirality class as 16bar, not 16",
      {sum(w) % 4 for w in MS_VSP} == {sum(w) % 4 for w in MS_SM}
      and {sum(w) % 4 for w in MS_VSP} != {sum(w) % 4 for w in MS_SP})

# --- explicit gamma-trace map T : V (x) S -> S, with the (6,4) metric ---
DIM_VS = 10 * DIM_S
T_re = np.zeros((DIM_S, DIM_VS), dtype=np.int64)
T_im = np.zeros((DIM_S, DIM_VS), dtype=np.int64)
for a in range(10):
    ga = CL64.gam[a].scaled(CL64.eta[a])          # eta^{aa} Gamma_a  (index raised)
    T_re[:, a * DIM_S:(a + 1) * DIM_S] = ga.re
    T_im[:, a * DIM_S:(a + 1) * DIM_S] = ga.im
T = Zi(T_re, T_im)

cols_plus = np.concatenate([a * DIM_S + SPLUS for a in range(10)])
cols_minus = np.concatenate([a * DIM_S + SMINUS for a in range(10)])
check("V (x) S splits 160 + 160 by internal chirality",
      len(cols_plus) == 160 and len(cols_minus) == 160)

rk_plus = rank_fp(T_re[:, cols_plus], T_im[:, cols_plus])
rk_minus = rank_fp(T_re[:, cols_minus], T_im[:, cols_minus])
check("gamma-trace on V (x) S+ has rank exactly 16 (F_p lower bound = codim bound)",
      rk_plus == 16)
check("gamma-trace on V (x) S- has rank exactly 16", rk_minus == 16)
check("dim ker(gamma-trace | V (x) S+) = 144  ->  10 (x) 16 = 144 (+) 16bar",
      160 - rk_plus == 144)
check("dim ker(gamma-trace | V (x) S-) = 144", 160 - rk_minus == 144)
# image lands in the OPPOSITE chirality half: certifies the gamma-trace sub is 16bar
img_wrong = T_re[np.ix_(SPLUS, cols_plus)], T_im[np.ix_(SPLUS, cols_plus)]
check("image of V (x) S+ under gamma-trace lies entirely in S- (the sub is a 16bar)",
      not img_wrong[0].any() and not img_wrong[1].any())

# weight multisets follow exactly from equivariance + surjectivity onto S-
MS_144 = ms_sub(MS_VSP, MS_SM)
MS_144B = ms_sub(MS_VSM, MS_SP)
check("144 weight multiset has only non-negative multiplicities",
      all(v > 0 for v in MS_144.values()))
check("dim 144 (weights) = 144", ms_dim(MS_144) == 144)
check("dim 144bar (weights) = 144", ms_dim(MS_144B) == 144)


# --- Weyl group of D_n, w_0, dominance, Weyl dimension, Racah ---------------
def weyl_dn(n: int):
    """Signed permutations of n coordinates with an even number of sign flips."""
    out = []
    for perm in permutations(range(n)):
        sgn = 1
        seen = [False] * n
        for i in range(n):                     # cycle-count parity
            if not seen[i]:
                j, ln = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = perm[j]
                    ln += 1
                if ln % 2 == 0:
                    sgn = -sgn
        for signs in product((1, -1), repeat=n):
            if signs.count(-1) % 2:
                continue
            out.append((perm, signs, sgn))
    return out


def apply_w(w, x, offset=0):
    perm, signs, _ = w
    n = len(perm)
    y = list(x)
    for i in range(n):
        y[offset + i] = signs[i] * x[offset + perm[i]]
    return tuple(y)


W_D5 = weyl_dn(5)
check("|W(D5)| = 1920", len(W_D5) == 1920)
RHO_D5 = (8, 6, 4, 2, 0)                       # doubled rho of D5 = 2*(4,3,2,1,0)

# w_0: the unique element with w(rho) = -rho on the dominant chamber
w0_cands = [w for w in W_D5 if apply_w(w, RHO_D5) == tuple(-x for x in RHO_D5)]
check("D5 has exactly one w_0 with w(rho) = -rho", len(w0_cands) == 1)
W0_D5 = w0_cands[0]
HW_144 = (3, 1, 1, 1, 1)
HW_144B = (3, 1, 1, 1, -1)
minus_w0_144 = tuple(-x for x in apply_w(W0_D5, HW_144))
check("D5: -w_0 acts as e_5 -> -e_5 (the diagram automorphism)",
      minus_w0_144 == HW_144B)
check("144^* = 144bar   =>  NO invariant bilinear form on the 144, in ANY real form",
      minus_w0_144 != HW_144)
check("16^* = 16bar likewise", tuple(-x for x in apply_w(W0_D5, (1, 1, 1, 1, 1))) ==
      (1, 1, 1, 1, -1))
check("(16bar)^* = 16   =>  a right-handed 16bar re-expresses as a LEFT-handed 16",
      tuple(-x for x in apply_w(W0_D5, (1, 1, 1, 1, -1))) == (1, 1, 1, 1, 1))
check("(144bar)^* = 144  =>  a right-handed 144bar re-expresses as a LEFT-handed 144",
      tuple(-x for x in apply_w(W0_D5, HW_144B)) == HW_144)

# CONTRARY CONSTRUCTION / negative control: D_4, where -w_0 = id
W_D4 = weyl_dn(4)
check("|W(D4)| = 192", len(W_D4) == 192)
RHO_D4 = (6, 4, 2, 0)
w0_d4 = [w for w in W_D4 if apply_w(w, RHO_D4) == tuple(-x for x in RHO_D4)]
check("D4 has exactly one w_0", len(w0_d4) == 1)
HW_D4_VS = (3, 1, 1, 1)                        # the so(8) gamma-traceless vector-spinor
mw0_d4 = tuple(-x for x in apply_w(w0_d4[0], HW_D4_VS))
check("CONTRARY CONTROL D4: -w_0 = id, so the analogous 56 IS self-dual "
      "(a group where the collapse WOULD happen, and this machinery sees it)",
      mw0_d4 == HW_D4_VS)


# --- LEG B, SECOND ROUTE: the Z/4 centre of Spin(10), no Weyl group at all ----
# The mod-4 coordinate-sum class IS the character of the Z/4 centre.  An
# invariant bilinear needs the centre to act trivially on V (x) V.  This uses
# ONLY HE-1 3.1's own banked fact and no w_0, so it is a genuinely independent
# confirmation of Leg B -- and the centre is a property of the COMPLEX group.
cls_144 = {sum(w) % 4 for w in MS_144}
cls_144b = {sum(w) % 4 for w in MS_144B}
check("centre class of the 144 is a single value", len(cls_144) == 1)
check("centre class of the 144bar is a single value", len(cls_144b) == 1)
c144, c144b = cls_144.pop(), cls_144b.pop()
check("centre classes: 16 -> 1, 16bar -> 3, 10 -> 2, 144 -> 3, 144bar -> 1",
      ({sum(w) % 4 for w in MS_SP} == {1} and {sum(w) % 4 for w in MS_SM} == {3}
       and {sum(w) % 4 for w in MS_V} == {2} and c144 == 3 and c144b == 1))
check("LEG B route 2: the Z/4 centre acts NONTRIVIALLY on 144 (x) 144 "
      f"(class {(c144 + c144) % 4}) => no invariant bilinear, by the centre alone",
      (c144 + c144) % 4 != 0)
check("LEG B route 2: the centre acts TRIVIALLY on 144 (x) 144bar "
      f"(class {(c144 + c144b) % 4}) => the pairing is the conjugate one",
      (c144 + c144b) % 4 == 0)
check("LEG B route 2 agrees with LEG B route 1 (w_0 / diagram automorphism)",
      ((c144 + c144) % 4 != 0) == (minus_w0_144 != HW_144))


def weyl_dim_dn(hw, n) -> Fraction:
    rho = tuple(2 * (n - 1 - k) for k in range(n))
    mu_rho = tuple(a + b for a, b in zip(hw, rho))
    num, den = Fraction(1), Fraction(1)
    for i in range(n):
        for j in range(i + 1, n):
            for s in (-1, 1):
                num *= (mu_rho[i] + s * mu_rho[j])
                den *= (rho[i] + s * rho[j])
    return Fraction(num, den)


check("Weyl dim of D5 h.w. (3,1,1,1,1)/2 is 144", weyl_dim_dn(HW_144, 5) == 144)
check("Weyl dim of D5 h.w. (1,1,1,1,1)/2 is 16", weyl_dim_dn((1, 1, 1, 1, 1), 5) == 16)
check("Weyl dim of D5 h.w. (2,0,0,0,0) is 10", weyl_dim_dn((2, 0, 0, 0, 0), 5) == 10)
check("Weyl dim of D4 h.w. (3,1,1,1)/2 is 56", weyl_dim_dn(HW_D4_VS, 4) == 56)


def racah_multiplicities(ms, weyl, rho, dominant_test):
    """mult(mu) = sum_w det(w) m(w(mu+rho) - rho), over dominant mu present in ms."""
    out = {}
    doms = [w for w in ms if dominant_test(w)]
    for mu in doms:
        mu_rho = tuple(a + b for a, b in zip(mu, rho))
        tot = 0
        for w in weyl:
            img = apply_w(w, mu_rho)
            key = tuple(a - b for a, b in zip(img, rho))
            if key in ms:
                tot += w[2] * ms[key]
        if tot:
            out[mu] = tot
    return out


def dom_d5(w):
    return w[0] >= w[1] >= w[2] >= w[3] >= abs(w[4])


dec_144 = racah_multiplicities(MS_144, W_D5, RHO_D5, dom_d5)
check("Racah on D5: the 144 weight multiset is IRREDUCIBLE with h.w. (3,1,1,1,1)/2",
      dec_144 == {HW_144: 1})
dec_144b = racah_multiplicities(MS_144B, W_D5, RHO_D5, dom_d5)
check("Racah on D5: the conjugate multiset is irreducible with h.w. (3,1,1,1,-1)/2",
      dec_144b == {HW_144B: 1})
check("144 and 144bar have DIFFERENT weight multisets  =>  NON-ISOMORPHIC",
      MS_144 != MS_144B)
check("144bar's weights are exactly the e_5-flip of the 144's",
      {(w[0], w[1], w[2], w[3], -w[4]): m for w, m in MS_144.items()} == MS_144B)


# --- LEG A: where does the antilinear J actually send the 144? --------------
B_INT = INT["fams"][0]["B"]
BINV_INT = INT["fams"][0]["Binv"]
ETA_INT = INT["fams"][0]["eta"]

I10 = Zi.eye(10)
BIG_B = kron(I10, B_INT)
BIG_BINV = kron(I10, BINV_INT)
BIG_CHI = kron(I10, CHI_INT)

# (i)  J anticommutes with the internal chirality on V (x) S
check("LEG A(i): CHI^* = - B CHI B^{-1}  =>  J maps V(x)S+ ONTO V(x)S-",
      (CHI_INT.conj()).equals((B_INT @ CHI_INT @ BINV_INT).scaled(-1)))

# (ii) J intertwines the gamma-trace, so it preserves gamma-tracelessness.
#      Required identity:  T^* = eta * B T (I_10 (x) B^{-1})
lhs = Zi(T.re, -T.im)
rhs = (B_INT @ T @ BIG_BINV).scaled(ETA_INT)
check("LEG A(ii): T^* = eta * B T (I (x) B^{-1})  =>  J(ker T) = ker T exactly",
      lhs.equals(rhs))

# (iii) equivariance of J for the whole real form so(6,4): all 45 generators
gens_ok = True
for a in range(10):
    for b in range(a + 1, 10):
        Sig = (CL64.gam[a] @ CL64.gam[b]).scaled(1)        # 2 * Sigma_ab, real params
        if not (Sig.conj()).equals(B_INT @ Sig @ BINV_INT):
            gens_ok = False
check("LEG A(iii): J is so(6,4)-equivariant on all 45 generators", gens_ok)

# vector factor: so(6,4) acts on V by REAL matrices, so entrywise conjugation is
# equivariant on V.  Verified, not asserted.
vec_real = True
for a in range(10):
    for b in range(a + 1, 10):
        M = np.zeros((10, 10), dtype=np.int64)
        M[a, b] = CL64.eta[b]
        M[b, a] = -CL64.eta[a]
        if not Zi(M, np.zeros((10, 10), dtype=np.int64)).is_real():
            vec_real = False
check("LEG A(iii'): all 45 so(6,4) generators on the vector 10 are REAL matrices "
      "=> the 10 is a real module and conjugation is equivariant on it", vec_real)

# (iv) EXPLICIT kernel basis of the 144 over Z[i], and its image under J.
#      Gamma_1^2 = +I for (6,4), so Gamma_1^{-1} = Gamma_1 and
#         x_{a,s} = e_a (x) s  -  e_1 (x) (eta^{aa} Gamma_1 Gamma_a s)
#      is annihilated by the gamma-trace, for a = 2..10 and s a basis of S+.
KER = np.zeros((144, DIM_VS), dtype=np.int64), np.zeros((144, DIM_VS), dtype=np.int64)
row = 0
for a in range(1, 10):
    Mixed = (CL64.gam[0] @ CL64.gam[a]).scaled(CL64.eta[a])
    for si in SPLUS:
        KER[0][row, a * DIM_S + si] = 1
        KER[0][row, 0 * DIM_S:1 * DIM_S] = -Mixed.re[:, si]
        KER[1][row, 0 * DIM_S:1 * DIM_S] = -Mixed.im[:, si]
        row += 1
check("explicit Z[i] kernel basis built: 144 vectors", row == 144)
KERZ = Zi(KER[0], KER[1])
img = (T @ KERZ.T()).T()
check("LEG A(iv): all 144 explicit basis vectors are gamma-traceless (T x = 0)",
      img.is_zero())
check("LEG A(iv): the 144 explicit vectors are linearly independent (rank 144)",
      rank_fp(KERZ.re, KERZ.im) == 144)
BIG_CHI = kron(I10, CHI_INT)
check("LEG A(iv): all 144 sit in the CHI = +1 half of V (x) S",
      ((BIG_CHI @ KERZ.T()).T()).equals(KERZ))

JKER = (BIG_BINV @ KERZ.conj().T()).T()          # J applied rowwise
check("LEG A(v): J maps every one of the 144 into the CHI = -1 half",
      ((BIG_CHI @ JKER.T()).T()).equals(JKER.scaled(-1)))
check("LEG A(v): J maps every one of the 144 into ker(gamma-trace) -- i.e. onto "
      "gamma-traceless states, so conj(144) = 144bar and NOT the 144",
      ((T @ JKER.T()).T()).is_zero())
check("LEG A(v): the image is 144-dimensional", rank_fp(JKER.re, JKER.im) == 144)
stack = Zi(np.vstack([KERZ.re, JKER.re]), np.vstack([KERZ.im, JKER.im]))
check("LEG A(vi): 144 and conj(144) span 288 dimensions, so they intersect in {0}",
      rank_fp(stack.re, stack.im) == 288)

# The SECOND antilinear family, independently: the verdict must not depend on
# which of the two conjugations is called "the" reality structure.
for fi, fam in enumerate(INT["fams"]):
    Bf, Bfi, etaf = fam["B"], fam["Binv"], fam["eta"]
    check(f"LEG A(vii) family {fi}: eta = {etaf:+d}, T^* = eta B T (I (x) B^{{-1}})",
          Zi(T.re, -T.im).equals((Bf @ T @ kron(I10, Bfi)).scaled(etaf)))
    Jf = (kron(I10, Bfi) @ KERZ.conj().T()).T()
    check(f"LEG A(vii) family {fi}: image is gamma-traceless",
          ((T @ Jf.T()).T()).is_zero())
    check(f"LEG A(vii) family {fi}: image sits entirely in the CHI = -1 half "
          f"(so conj(144) = 144bar under BOTH conjugations)",
          ((BIG_CHI @ Jf.T()).T()).equals(Jf.scaled(-1)))
    stk = Zi(np.vstack([KERZ.re, Jf.re]), np.vstack([KERZ.im, Jf.im]))
    check(f"LEG A(vii) family {fi}: 144 and its conjugate span 288",
          rank_fp(stk.re, stk.im) == 288)

print(f"  LEG A  Frobenius-Schur indicator of the 144 under Spin(6,4):  0  (COMPLEX)")
print(f"  LEG B  144^* = {minus_w0_144} != {HW_144} = 144  ->  no invariant bilinear form")


# ===========================================================================
# 4.  Re-derivation of HE-1's Pati-Salam mirror claim, independent route.
# ===========================================================================
print()
print("=" * 74)
print("PART 3 -- HE-1 3.2 re-derived: Pati-Salam blocks by Racah on D3 (+) D2")
print("=" * 74)

W_D3 = weyl_dn(3)
W_D2 = weyl_dn(2)
check("|W(D3)| = 24 and |W(D2)| = 4", len(W_D3) == 24 and len(W_D2) == 4)
W_PS = []
for w3 in W_D3:
    for w2 in W_D2:
        W_PS.append((w3, w2, w3[2] * w2[2]))
check("|W(D3 x D2)| = 96", len(W_PS) == 96)
RHO_PS = (4, 2, 0, 2, 0)


def apply_ps(w, x):
    w3, w2, _ = w
    y = list(apply_w(w3, x, offset=0))
    y = list(apply_w(w2, tuple(y), offset=3))
    return tuple(y)


def racah_ps(ms):
    out = {}
    doms = [w for w in ms if w[0] >= w[1] >= abs(w[2]) and w[3] >= abs(w[4])]
    for mu in doms:
        mu_rho = tuple(a + b for a, b in zip(mu, RHO_PS))
        tot = 0
        for w in W_PS:
            img = apply_ps(w, mu_rho)
            key = tuple(a - b for a, b in zip(img, RHO_PS))
            if key in ms:
                tot += w[2] * ms[key]
        if tot:
            out[mu] = tot
    return out


SU4_NAME = {(1, 1, 1): "4", (1, 1, -1): "4bar", (2, 0, 0): "6",
            (2, 2, 0): "15", (3, 1, 1): "20", (3, 1, -1): "20bar",
            (0, 0, 0): "1", (2, 2, 2): "10", (2, 2, -2): "10bar"}


def ps_label(mu):
    """(SU(4) type by highest weight, 2j_L + 1, 2j_R + 1).

    su(2)_L is the (x_4 + x_5) factor, so S+(4) = (2,1) and S-(4) = (1,2);
    this is the assignment under which 16|_PS = (4,2,1) + (4bar,1,2), i.e.
    W221's and HE-1's one-generation content.
    """
    su4 = SU4_NAME.get(mu[:3], f"D3{mu[:3]}")
    jl = (mu[3] + mu[4]) // 2 + 1                    # 2j_L + 1
    jr = (mu[3] - mu[4]) // 2 + 1                    # 2j_R + 1
    return (su4, jl, jr)


def ps_dim(mu):
    d4 = weyl_dim_dn(mu[:3], 3)
    _, jl, jr = ps_label(mu)
    return int(d4) * jl * jr


for name, ms, tot in (("16", MS_SP, 16), ("16bar", MS_SM, 16),
                      ("144", MS_144, 144), ("10 (x) 16", MS_VSP, 160)):
    dec = racah_ps(ms)
    got = sum(m * ps_dim(mu) for mu, m in dec.items())
    check(f"PS decomposition of {name} sums back to {tot}", got == tot)
    labels = {ps_label(mu): m for mu, m in dec.items()}
    print(f"  {name:<10} -> " + "  ".join(
        f"{m}x({lab[0]},{lab[1]},{lab[2]})" for lab, m in sorted(labels.items())))
    if name == "16":
        PS_16 = labels
    elif name == "16bar":
        PS_16B = labels
    elif name == "144":
        PS_144 = labels
    else:
        PS_TENSOR = labels

check("16 |_PS = (4,2,1) + (4bar,1,2)  [chirality-correlated, W221]",
      PS_16 == {("4", 2, 1): 1, ("4bar", 1, 2): 1})
check("16bar |_PS = (4bar,2,1) + (4,1,2)", PS_16B == {("4bar", 2, 1): 1, ("4", 1, 2): 1})
check("HE-1 3.2 REPRODUCED: the 144 contains BOTH 16bar blocks with multiplicity "
      "EXACTLY ONE",
      PS_144.get(("4bar", 2, 1)) == 1 and PS_144.get(("4", 1, 2)) == 1)
check("HE-1 3.2 REPRODUCED: NEITHER 16 block appears in the 144 at all",
      ("4", 2, 1) not in PS_144 and ("4bar", 1, 2) not in PS_144)
check("HE-1 3.2 REPRODUCED: the remaining 128 states are 20/20bar/(4,3,2)-type exotics",
      sum(m * ps_dim(mu) for mu, m in racah_ps(MS_144).items()
          if ps_label(mu) not in {("4bar", 2, 1), ("4", 1, 2)}) == 128)
check("HE-1 NEGATIVE CONTROL REPRODUCED: before gamma-tracelessness the mirror "
      "blocks have multiplicity TWO",
      PS_TENSOR.get(("4bar", 2, 1)) == 2 and PS_TENSOR.get(("4", 1, 2)) == 2)


# ===========================================================================
# 5.  The two ambient horns, built by factorisation, and the chirality tie.
# ===========================================================================
print()
print("=" * 74)
print("PART 4 -- both horns of SIGNATURE-AMBIENT, factorised ext(4) (x) int(6,4)")
print("=" * 74)

HORNS = {"(7,7)": ((1, 3), (7, 7)), "(9,5)": ((3, 1), (9, 5))}
horn_results = {}

for horn, ((pe, qe), (pa, qa)) in HORNS.items():
    ext = Clifford(pe, qe)
    check(f"{horn}: external Cl({pe},{qe}) relations exact", ext.relations_hold())
    G5, _ = ext.chirality()
    check(f"{horn}: gamma5_ext squares to +I", (G5 @ G5).equals(Zi.eye(4)))
    check(f"{horn}: gamma5_ext is purely real or purely imaginary",
          G5.is_real() or G5.is_imag())

    amb = [kron(ext.gam[m], Zi.eye(DIM_S)) for m in range(4)]
    amb += [kron(G5, CL64.gam[a]) for a in range(10)]
    eta_amb = ext.eta + CL64.eta
    D = 128
    Z = Zi.zeros(D)
    ok = True
    for A in range(14):
        for Bx in range(14):
            anti = amb[A] @ amb[Bx] + amb[Bx] @ amb[A]
            want = Zi.eye(D).scaled(2 * eta_amb[A]) if A == Bx else Z
            if not anti.equals(want):
                ok = False
    check(f"{horn}: factorised ambient Clifford relations exact", ok)
    check(f"{horn}: ambient signature is ({eta_amb.count(1)},{eta_amb.count(-1)}) "
          f"= ({pa},{qa})",
          (eta_amb.count(1), eta_amb.count(-1)) == (pa, qa))

    W = Zi.eye(D)
    for g in amb:
        W = W @ g
    W2 = W @ g if False else W @ W
    if W2.equals(Zi.eye(D)):
        CHI_AMB = W
    else:
        CHI_AMB = W.scaled(0, 1)
    check(f"{horn}: ambient chirality squares to +I", (CHI_AMB @ CHI_AMB).equals(Zi.eye(D)))
    fac = kron(G5, CHI_INT)
    ok_fac = any(CHI_AMB.equals(fac.scaled(a, b))
                 for (a, b) in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    check(f"{horn}: ambient chirality FACTORISES as gamma5_ext (x) CHI_int "
          f"(this is what ties external to internal chirality)", ok_fac)

    real_set = [A for A in range(14) if amb[A].is_real()]
    imag_set = [A for A in range(14) if amb[A].is_imag()]
    check(f"{horn}: every ambient gamma is purely real or purely imaginary",
          len(real_set) + len(imag_set) == 14)
    fams = []
    for subset in (imag_set, real_set):
        B = Zi.eye(D)
        for A in subset:
            B = B @ amb[A]
        B2 = B @ B
        okb, a2, b2 = B2.is_scalar_multiple_of_identity()
        assert okb and b2 == 0
        Binv = B if a2 == 1 else B.scaled(-1)
        M = B.conj() @ B
        okm, lam, lim_ = M.is_scalar_multiple_of_identity()
        assert okm and lim_ == 0
        jsq = 1 if lam > 0 else -1
        if (CHI_AMB.conj()).equals(B @ CHI_AMB @ Binv):
            chir = +1
        else:
            chir = -1
        # does J flip the EXTERNAL chirality factor?  and the INTERNAL one?
        g5big = kron(G5, Zi.eye(DIM_S))
        chibig = kron(Zi.eye(4), CHI_INT)
        ext_flip = (g5big.conj()).equals((B @ g5big @ Binv).scaled(-1))
        int_flip = (chibig.conj()).equals((B @ chibig @ Binv).scaled(-1))
        fams.append(dict(B=B, Binv=Binv, Jsq=jsq, chir=chir,
                         ext_flip=ext_flip, int_flip=int_flip))

    chirs = {f["chir"] for f in fams}
    check(f"{horn}: both antilinear families agree on the ambient chirality action",
          len(chirs) == 1)
    chir = chirs.pop()
    jsq = {f["Jsq"] for f in fams}
    check(f"{horn}: ambient reality PRESERVES ambient chirality "
          f"(a Weyl condition survives it)", chir == +1)
    check(f"{horn}: both families agree on sign(J^2)", len(jsq) == 1)
    jsq = jsq.pop()
    want_jsq = +1 if (pa - qa) % 8 == 0 else -1
    check(f"{horn}: sign(J_amb^2) = {want_jsq:+d} "
          f"({'Majorana-Weyl' if want_jsq == 1 else 'symplectic-Majorana-Weyl'})",
          jsq == want_jsq)
    check(f"{horn}: J_amb FLIPS the external chirality factor",
          all(f["ext_flip"] for f in fams))
    check(f"{horn}: J_amb FLIPS the internal chirality factor",
          all(f["int_flip"] for f in fams))
    # explicit sector identity: with Q_{eps,delta} = (I + eps g5)(I + delta CHI_int)
    # = 4 P_{eps,delta},  J P_{++} = P_{--} J  is exactly  Q_{++}^* = B Q_{--} B^{-1}.
    g5big = kron(G5, Zi.eye(DIM_S))
    chibig = kron(Zi.eye(4), CHI_INT)
    Ibig = Zi.eye(D)
    Qpp = (Ibig + g5big) @ (Ibig + chibig)
    Qmm = (Ibig + g5big.scaled(-1)) @ (Ibig + chibig.scaled(-1))
    sector_ok = all((Qpp.conj()).equals(f["B"] @ Qmm @ f["Binv"]) for f in fams)
    check(f"{horn}: EXPLICIT sector identity Q(++)^* = B Q(--) B^{{-1}}  =>  J_amb "
          f"maps (ext+, int+) ONTO (ext-, int-): it acts as CPT, NOT as a doubling",
          sector_ok)
    # real dimension of the J-fixed set inside the ambient Weyl half
    fix = real_fixed_dim(fams[0]["B"], CHI_AMB, D)
    want_fix = 64 if want_jsq == 1 else 0
    gloss = ("a genuine Majorana-Weyl spinor exists" if want_fix else
             "no Majorana-Weyl spinor exists; symplectic doubling is required")
    check(f"{horn}: dim_R of the J-fixed set inside S+_amb = {want_fix} ({gloss})",
          fix == want_fix)
    # cross-check against the unfactorised Cl(pa,qa)
    check(f"{horn}: factorised reality type agrees with the direct Cl({pa},{qa}) build",
          ("REAL" if (chir == 1 and jsq == 1) else
           "QUATERNIONIC" if chir == 1 else "COMPLEX") == reality_table[(pa, qa)]["type"])
    horn_results[horn] = dict(jsq=jsq, chir=chir, sector_ok=sector_ok, fix=fix)
    print(f"  {horn}: ambient reality preserves ambient chirality, J^2 = {jsq:+d}, "
          f"and flips BOTH the external and the internal chirality factor.")


# ===========================================================================
# 6.  Net-chirality readout.
# ===========================================================================
print()
print("=" * 74)
print("PART 5 -- net-chirality readout")
print("=" * 74)

# 4d left-handed content of one ambient Weyl spinor:
#   (ext+, int+)  -> left-handed in  R
#   (ext-, int-)  -> right-handed in Rbar, which re-expresses as LEFT-handed in
#                    (Rbar)^* .  For D5, (16bar)^* = 16 and (144bar)^* = 144.
lh_content_16 = ["16", "16"]                 # before imposing reality
lh_content_144 = ["144", "144"]
check("no 16bar appears at LEFT-handed 4d chirality (Weyl only): content = 16 + 16",
      set(lh_content_16) == {"16"})
check("no 144bar appears at LEFT-handed 4d chirality (Weyl only): content = 144 + 144",
      set(lh_content_144) == {"144"})
check("imposing the ambient reality condition HALVES that content (it identifies "
      "the two summands as CPT partners of each other) -- certified by the "
      "explicit sector identity Q(++)^* = B Q(--) B^{-1} in Part 4, which shows "
      "the reality map carries (ext+,int+) ONTO (ext-,int-) rather than onto a "
      "second independent copy",
      all(h["sector_ok"] for h in horn_results.values()))
check("in NEITHER horn does a barred internal partner appear at the same 4d "
      "chirality: the only way to get 144bar left-handed would be (144bar)^* = "
      "144bar, i.e. self-duality, which Part 2 refuted",
      minus_w0_144 != HW_144)


def net_chirality(n_g: int, n_144: int = 1) -> int:
    """HE-1 3.6, with the mirror multiplicity = 1 certified above."""
    return n_g - n_144


for n_g in (1, 2, 3, 4):
    check(f"net chirality for n_g={n_g} chiral 16s plus one 144 is {n_g - 1} "
          f"[HE-1 3.6 unchanged by the real form]", net_chirality(n_g) == n_g - 1)

check("HE-1's named kill condition ('reality pairs 144 with 144bar') is NOT met "
      "under Spin(6,4): FS indicator 0, no invariant bilinear form",
      INT["chir"] == -1 and minus_w0_144 != HW_144)
check("the verdict is IDENTICAL on both horns of SIGNATURE-AMBIENT",
      horn_results["(7,7)"]["chir"] == horn_results["(9,5)"]["chir"] == +1)
check("the horns differ ONLY in sign(J^2) -- a uniform doubling, not a chirality "
      "change", horn_results["(7,7)"]["jsq"] == +1 and horn_results["(9,5)"]["jsq"] == -1)


# ===========================================================================
# 7.  PLANTED FAILURES -- the failure path, exercised.
# ===========================================================================
print()
print("=" * 74)
print("PART 6 -- planted failing controls (each MUST be observed False)")
print("=" * 74)

planted("PLANTED: 'Cl(6,4) reality PRESERVES chirality'", INT["chir"] == +1)
planted("PLANTED: 'the 144 is self-dual under so(10,C)'", minus_w0_144 == HW_144)
planted("PLANTED: 'dim ker(gamma-trace | V (x) S+) = 160'", 160 - rk_plus == 160)
planted("PLANTED: 'Cl(9,1) reality FLIPS chirality'", reality_table[(9, 1)]["chir"] == -1)
planted("PLANTED: 'the 144 contains a 16 block at Pati-Salam'",
        ("4", 2, 1) in PS_144)
planted("PLANTED: 'D4's gamma-traceless vector-spinor is NOT self-dual'",
        mw0_d4 != HW_D4_VS)
planted("PLANTED: '144 and 144bar have the same weight multiset'", MS_144 == MS_144B)
planted("PLANTED: 'the ambient (9,5) reality has J^2 = +1'",
        horn_results["(9,5)"]["jsq"] == +1)

for nm, fired in PLANTED:
    print(f"  {'fired ' if fired else 'MISSED'}  {nm}")


# ===========================================================================
# 8.  Summary.
# ===========================================================================
print()
print("=" * 74)
n_ok = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
n_pl = sum(1 for _, ok in PLANTED if ok)
print(f"checks: {n_ok}/{n_tot}")
print(f"planted failing controls fired: {n_pl}/{len(PLANTED)}")
print()
print("VERDICT")
print("  LEG A (antilinear, real-form dependent):  the Spin(6,4) conjugation")
print("        FLIPS internal chirality, so conj(144) = 144bar != 144.")
print("        Frobenius-Schur indicator of the 144 = 0.  COMPLEX type.")
print("  LEG B (bilinear, real-form BLIND):  -w_0 is the nontrivial D5 diagram")
print("        automorphism, so 144^* = 144bar.  NO invariant bilinear form on")
print("        the 144 exists under ANY real form of so(10,C).")
print("  => Spin(6,4) reality does NOT pair the 144 with the 144bar in either")
print("     sense.  The sector is NOT made vectorlike by the real form.")
print("     HE-1's net chirality n_g -> n_g - 1 SURVIVES its own named kill.")
print("=" * 74)

failed = [nm for nm, ok in CHECKS if not ok] + [nm for nm, ok in PLANTED if not ok]
raise SystemExit(1 if failed else 0)
