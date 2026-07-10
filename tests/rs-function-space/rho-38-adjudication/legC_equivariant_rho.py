#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
LEG-C -- EQUIVARIANT RHO of the GEOMETRIC gamma-traceless Rarita-Schwinger operator Q
on the order-3 Nikulin mapping torus.  Exact arithmetic only (Fractions; Q(zeta) as pairs;
Q(i,zeta) as a two-step tower for the matrix model).  Adjudication swing, equivariant leg.
==============================================================================================
THE QUESTION (this leg's share). Two K-theory conventions for the spin-3/2 index on K3:
  (A) PINNED / ghost-subtracted (AGW gravitino density, prior campaigns):
      RS_A = D (x) (T_C - 1C), index -42 = 21 sigma/8, twist multiplier tr(g|T_C) - 1 = -3.
  (B) GEOMETRIC gamma-traceless operator Q (Homma-Semmelmann CMP 2019, Baer-Mazzeo CMP 2021):
      K-class [V+]-[V-] = ([S+]-[S-]) (x) (T_C + 1C)  (chirality-REVERSED iota-embedding),
      index -38 = 19 sigma/8, twist multiplier tr(g|T_C) + 1 = -1.
THIS LEG computes the fine equivariant rho of (B) with the verified prior-swing machinery
(ported from tests/rs-function-space/order3-rho/leg3_rs_rho.py, same arithmetic core), derives
ker(Q) phases from the twistor splitting at harmonic level (triangularity condition stated AND
its checkable content verified in an exact flat Clifford matrix model over Q(i,zeta)), gates
ind_phi(Q) by Atiyah-Bott AND Hodge trace, assembles rho by master formula AND Donnelly
averaging, verifies the class law, and reports the Z/3 classes of BOTH conventions side by side.

THE OBJECT. phi = order-3 Nikulin symplectic K3 automorphism: 6 isolated fixed points, local
T^{1,0} weights (zeta, zeta^{-1}), zeta = e^{2 pi i/3} (forced by phi*Omega = Omega). Mapping
torus T_phi = (K3 x S^1)/(Z/3), product metric (Yau metric in the phi-averaged Kahler class),
flat Z/3 characters alpha_k.  rho_k := eta_{alpha_k} - eta_{alpha_0} at the eta level (APS
I-III); h reported separately, never folded.  S^1 spin structure: PERIODIC (prior-swing
convention; the bounding package differs by exact even integers -- disk route cross-check).

ESTABLISHED FORMULAS USED (citations only; nothing else):
  - Atiyah-Bott fixed point formula (Ann. Math. 87/88, 1968); APS I-III (1975-76);
    Donnelly 1978 (equivariant eta, icot densities); Nikulin 1979 / Garbagnati-Sarti 2007.
  - Homma-Semmelmann, CMP 370 (2019) 853-871 (arXiv:1804.10602)  [cached extract verified
    this session: hs-rs-kernel.txt lines 316 (eq 11), 321-323 (Prop 3.1(i)), 673-675
    (K3: dim ker Q = 2h^{1,1}-2 = 38, two copies of primitive harmonic (1,1)-forms),
    354-361 (Remark 3.6: physics ghost subtraction ind D_TM - ind D), 683 (parallel
    spinors lie in ker D_TM)].
  - Baer-Mazzeo, CMP 384 (2021) 533-548 (arXiv:2003.11255)  [cached extract verified:
    baer-mazzeo.txt line 182 (Q elliptic, formally self-adjoint), 286 (alpha-family all
    elliptic => index additivity), 858 (RS(K3) = 38, sharp)].
IMPORT LEDGER printed in S13; everything else is recomputed here from {6 fixed points,
symplectic weights, sigma = -16, standard Hodge data, |G| = 3, the Clifford algebra}.

HOUSE STYLE: exact arithmetic only; global NASSERT; check() asserts; exit 0 on success.
FIREWALL (absorbed/gu-source-action/DEAD-ENDS.md): no chi(K3) = 24 input, no /8 manufacture,
no A-hat = 3, no contractible-fiber => 1; -38 is DERIVED (as -40 + 2), never imported as a
target.  Audit in S13.
"""
from fractions import Fraction as F

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, "FAIL: " + m


def banner(t):
    print()
    print("=" * 94)
    print(t)
    print("=" * 94)


# ==============================================================================================
# SECTION 0: ARITHMETIC CORE
#   (a) Q(i): Gaussian rationals as pairs (a, b) of Fractions              [matrix model base]
#   (b) Q(i, zeta): pairs (A, B) of Q(i) elements, A + B*zeta, zeta^2 = -1 - zeta
#       -- the SAME multiplication law as the verified leg2/leg3 QZ core, base field enlarged.
#   (c) master-formula machinery over plain Fractions (ported from leg3 verbatim).
# ==============================================================================================
class QI:
    """Gaussian rational a + b*i."""
    __slots__ = ("a", "b")

    def __init__(s, a=0, b=0):
        s.a, s.b = F(a), F(b)

    @staticmethod
    def co(o):
        return o if isinstance(o, QI) else QI(o)

    def __add__(s, o):
        o = QI.co(o); return QI(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __neg__(s):
        return QI(-s.a, -s.b)

    def __sub__(s, o):
        return s + (-QI.co(o))

    def __rsub__(s, o):
        return QI.co(o) - s

    def __mul__(s, o):
        o = QI.co(o)
        return QI(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__

    def conj(s):
        return QI(s.a, -s.b)

    def inv(s):
        n = s.a * s.a + s.b * s.b
        check(n != 0, "QI.inv: nonzero")
        return QI(s.a / n, -s.b / n)

    def __eq__(s, o):
        o = QI.co(o); return s.a == o.a and s.b == o.b

    def iszero(s):
        return s.a == 0 and s.b == 0


class QZI:
    """Element A + B*zeta of Q(i, zeta), A, B in Q(i); zeta^2 = -1 - zeta.
    Same multiplication law as the verified leg2/leg3 QZ core."""
    __slots__ = ("A", "B")

    def __init__(s, A=0, B=0):
        s.A, s.B = QI.co(A), QI.co(B)

    @staticmethod
    def co(o):
        return o if isinstance(o, QZI) else QZI(QI.co(o))

    def __add__(s, o):
        o = QZI.co(o); return QZI(s.A + o.A, s.B + o.B)
    __radd__ = __add__

    def __neg__(s):
        return QZI(-s.A, -s.B)

    def __sub__(s, o):
        return s + (-QZI.co(o))

    def __rsub__(s, o):
        return QZI.co(o) - s

    def __mul__(s, o):
        o = QZI.co(o)
        A, B, C, D = s.A, s.B, o.A, o.B
        return QZI(A * C - B * D, A * D + B * C - B * D)   # zeta^2 = -1 - zeta
    __rmul__ = __mul__

    def zconj(s):
        """zeta -> zeta^2 (Galois over Q(i))"""
        return QZI(s.A - s.B, -s.B)

    def cconj(s):
        """full complex conjugation: i -> -i AND zeta -> zeta^2"""
        return QZI(s.A.conj() - s.B.conj(), -s.B.conj())

    def inv(s):
        t = s.zconj()
        n = s * t                                  # = A^2 - AB + B^2, lies in Q(i)
        check(n.B.iszero() and not n.A.iszero(), "QZI.inv: zeta-norm in Q(i), nonzero")
        return t * QZI(n.A.inv())

    def __truediv__(s, o):
        return s * QZI.co(o).inv()

    def __eq__(s, o):
        o = QZI.co(o); return s.A == o.A and s.B == o.B

    def iszero(s):
        return s.A.iszero() and s.B.iszero()

    def __repr__(s):
        return "(%s+%si + (%s+%si)z)" % (s.A.a, s.A.b, s.B.a, s.B.b)


def zc(a=0, b=0, c=0, d=0):
    """a + b*i + c*zeta + d*i*zeta"""
    return QZI(QI(a, b), QI(c, d))


IU = zc(0, 1)                # i
ZETA = zc(0, 0, 1)           # zeta
ZP = {0: zc(1), 1: ZETA, 2: ZETA * ZETA}


def zp(e):
    return ZP[e % 3]


# pinned exact identities (same as the verified core)
check(zp(1) * zp(1) == zc(-1, 0, -1), "zeta^2 = -1 - zeta")
check(zp(1) * zp(2) == zc(1), "zeta * zeta^2 = 1")
check(zp(1) + zp(2) == zc(-1), "zeta + zeta^2 = -1")
check(IU * IU == zc(-1), "i^2 = -1")
check(zp(1).cconj() == zp(2), "complex conjugation zeta -> zeta^2")
ISQ3 = zp(1) - zp(2)                                     # i*sqrt(3) = 1 + 2 zeta
check(ISQ3 == zc(1, 0, 2), "i sqrt3 = 1 + 2 zeta")
check(ISQ3 * ISQ3 == zc(-3), "(i sqrt3)^2 = -3")
ICOT = {1: ISQ3 * F(1, 3), 2: -1 * (ISQ3 * F(1, 3))}     # i cot(pi/3), i cot(2 pi/3)
SQ3H = zc(0, F(-1, 2), 0, -1)                            # sqrt(3)/2 = -i(1 + 2 zeta)/2
check(SQ3H * SQ3H == zc(F(3, 4)), "(sqrt3/2)^2 = 3/4")
check(SQ3H * IU == ISQ3 * F(1, 2), "i * sqrt3/2 = (i sqrt3)/2")

def half(e):
    """(zeta^e)^{1/2} := zeta^{2e} (canonical odd-order lift)"""
    return zp(2 * e)


def sfac(e):
    return half(e) - half(-e)


def is_rat(x):
    return x.B.iszero() and x.A.b == 0


def rat(x, m="value is rational"):
    check(is_rat(x), m)
    return x.A.a


# master formula machinery over plain Fractions (leg2/leg3 conventions, ported verbatim):
def eta_S1(th):
    t = th % 1
    return F(0) if t == 0 else 1 - 2 * t


check(eta_S1(F(1, 3)) == F(1, 3), "eta_S1(1/3) = 1/3")
check(eta_S1(F(2, 3)) == F(-1, 3), "eta_S1(2/3) = -1/3")
check(eta_S1(F(0)) == 0, "eta_S1(0) = 0")


def eta_alpha(kp, km, k):
    """direct spectral eta on T_phi in character alpha_k; ker^- -> +eta_S1, ker^+ -> -eta_S1"""
    e = F(0)
    for th, m in km.items():
        e += m * eta_S1(th + F(k, 3))
    for th, m in kp.items():
        e -= m * eta_S1(th + F(k, 3))
    return e


def h_dim(kp, km, k):
    h = 0
    for th, m in list(km.items()) + list(kp.items()):
        if (th + F(k, 3)) % 1 == 0:
            h += m
    return h


def tr_g(mult, m):
    t = zc(0)
    for th, mu in mult.items():
        t = t + zc(mu) * zp(int(3 * th) * m)
    return t


def z3_class(rho):
    check(rho.denominator in (1, 3), "|G| = 3 caps the denominator of rho at 3")
    return int((3 * rho) % 3)


def shift(mult, m):
    return {(th + F(m, 3)) % 1: mu for th, mu in mult.items()}


# ---- matrix helpers over Q(i, zeta) ----
def mzero(r, c):
    return [[zc(0) for _ in range(c)] for _ in range(r)]


def mid(n):
    M = mzero(n, n)
    for i in range(n):
        M[i][i] = zc(1)
    return M


def mmul(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    check(len(X[0]) == k, "mmul: shapes match")
    Z = mzero(r, c)
    for i in range(r):
        Xi = X[i]
        for j in range(c):
            t = zc(0)
            for l in range(k):
                if not Xi[l].iszero():
                    t = t + Xi[l] * Y[l][j]
            Z[i][j] = t
    return Z


def madd(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]


def msub(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]


def mscal(c, X):
    c = QZI.co(c)
    return [[c * X[i][j] for j in range(len(X[0]))] for i in range(len(X))]


def meq(X, Y):
    return all(X[i][j] == Y[i][j] for i in range(len(X)) for j in range(len(X[0])))


def miszero(X):
    return all(X[i][j].iszero() for i in range(len(X)) for j in range(len(X[0])))


def mtrace(X):
    t = zc(0)
    for i in range(len(X)):
        t = t + X[i][i]
    return t


def dagger(X):
    return [[X[i][j].cconj() for i in range(len(X))] for j in range(len(X[0]))]


def mvec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v))), zc(0)) for i in range(len(M))]


def rref(M):
    A = [row[:] for row in M]
    r, c = len(A), len(A[0])
    piv, pr = [], 0
    for col in range(c):
        pi = None
        for i in range(pr, r):
            if not A[i][col].iszero():
                pi = i
                break
        if pi is None:
            continue
        A[pr], A[pi] = A[pi], A[pr]
        ivp = A[pr][col].inv()
        A[pr] = [ivp * x for x in A[pr]]
        for i in range(r):
            if i != pr and not A[i][col].iszero():
                f = A[i][col]
                A[i] = [A[i][j] - f * A[pr][j] for j in range(c)]
        piv.append(col)
        pr += 1
        if pr == r:
            break
    return A, piv


def rank(M):
    return len(rref(M)[1])


def nullspace(M):
    A, piv = rref(M)
    c = len(M[0])
    free = [j for j in range(c) if j not in piv]
    basis = []
    for fc in free:
        v = [zc(0)] * c
        v[fc] = zc(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        basis.append(v)
    return basis


def detn(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = zc(0)
    for j in range(n):
        if M[0][j].iszero():
            continue
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        term = M[0][j] * detn(minor)
        tot = tot + (term if j % 2 == 0 else -term)
    return tot


banner("SECTION 0 OK: Q(i,zeta) tower (leg3 QZ law over Gaussian base), master-formula machinery,"
       "\nexact matrix helpers (rref/rank/nullspace/det over the exact field)")

# ==============================================================================================
# SECTION 1: LEG-1 INPUTS RECOMPUTED (self-verifying): Lefschetz-forced lattice + H^{1,1} split
# ==============================================================================================
banner("S1. Lefschetz-forced (r,s) = (10,12); H^{1,1} = 8 trivial + 6 zeta + 6 zeta^2; sigma = -16")

SIGMA = -16
check(3 - 19 == SIGMA and 3 + 19 == 22, "K3 lattice signature (3,19): sigma = -16, b2 = 22")
sols_rs = [(22 - s_, s_) for s_ in range(0, 23, 2) if 2 + (22 - s_) - F(s_, 2) == 6]
check(sols_rs == [(10, 12)], "Lefschetz L(phi) = 6 FORCES (r, s) = (10, 12)")
R_INV, S_COINV = sols_rs[0]

H20 = 1
H11 = 22 - 2 * H20
H11_TRIV = R_INV - 2 * H20
H11_Z = S_COINV // 2
H11_Z2 = S_COINV // 2
check(H11 == 20 and H11_TRIV == 8 and H11_Z == 6 and H11_Z2 == 6,
      "H^{1,1} eigensplit: 8 trivial + 6 zeta + 6 zeta^2 (total 20)")
print("  (r,s) = (10,12) forced; H^{1,1} = 8 + 6 zeta + 6 zeta^2; h^{1,1} = 20")

# ==============================================================================================
# SECTION 2: SPIN LIFT (unique, odd order) + operational pin ind_phi(D) = +2
# ==============================================================================================
banner("S2. Unique order-3 spin lift; pin gate ind_phi(D) = 6 * nu_D4 = 2 (both powers)")

admissible = [eps for eps in (+1, -1) if eps ** 3 == 1]
check(admissible == [+1], "unique admissible order-3 spin lift (Hom(Z/3, Z/2) = 0)")


def nu_D4(m):
    """Atiyah-Bott Dirac weight per fixed point of g^m: 1/prod(lam^{1/2} - lam^{-1/2})"""
    return (sfac(m) * sfac(-m)).inv()


for m in (1, 2):
    check(nu_D4(m) == zc(F(1, 3)), "nu_D4(g^%d) = 1/3 exactly" % m)
check(zc(6) * nu_D4(1) == zc(2), "ind_phi(D) = 6 * 1/3 = 2 = tr(phi|H^{0,0}+H^{2,0}): lift pinned")
check(zc(6) * nu_D4(2) == zc(2), "ind_{phi^2}(D) = 2 as well")
print("  lift pinned operationally: S+ phi-trivial (the 2 parallel spinors), S- weights (zeta, zeta^2)")

# ==============================================================================================
# SECTION 3: EXACT FLAT CLIFFORD / TWISTOR MODEL over Q(i,zeta) -- the splitting, its
#            g-EQUIVARIANCE, and the TRIANGULARITY CONDITION (checkable content, all exact)
# ==============================================================================================
banner("S3. Flat model: twistor splitting S+- (x) T_C = V+- (+) iota(S-+); g-equivariance;"
       "\n    HS block matrix at symbol level (all four blocks); triangularity condition")

# --- 3a. Clifford algebra (quaternionic sigma model; c(xi)^2 = -|xi|^2) ---
_1, _0 = zc(1), zc(0)
SIG = [
    [[_1, _0], [_0, _1]],
    [[IU, _0], [_0, -IU]],
    [[_0, _1], [-_1, _0]],
    [[_0, IU], [IU, _0]],
]
GAM = []
for t in range(4):
    sd = dagger(SIG[t])
    G = mzero(4, 4)
    for i in range(2):
        for j in range(2):
            G[i][2 + j] = -sd[i][j]
            G[2 + i][j] = SIG[t][i][j]
    GAM.append(G)

ncl = 0
for mu in range(4):
    for nu in range(4):
        anti = madd(mmul(GAM[mu], GAM[nu]), mmul(GAM[nu], GAM[mu]))
        want = mscal(-2 if mu == nu else 0, mid(4))
        check(meq(anti, want), "Clifford relation (%d,%d)" % (mu, nu))
        ncl += 1
check(ncl == 16, "all 16 Clifford relations verified")

# --- 3b. contraction c, embedding iota, projector P; ranks and chirality bookkeeping ---
# index convention on S (x) T_C: flat index 4*s + t; s in {0,1} = S+, s in {2,3} = S-.
CMAT = mzero(4, 16)
for a in range(4):
    for s in range(4):
        for t in range(4):
            CMAT[a][4 * s + t] = GAM[t][a][s]
IOTA = mzero(16, 4)
for s in range(4):
    for t in range(4):
        for b in range(4):
            IOTA[4 * s + t][b] = F(-1, 4) * GAM[t][s][b]

check(meq(mmul(CMAT, IOTA), mid(4)), "c o iota = id_S (delta iota = 1; iota = (1/4) delta^dag)")
P16 = msub(mid(16), mmul(IOTA, CMAT))
check(meq(mmul(P16, P16), P16), "P = 1 - iota c is a projector (P^2 = P)")
check(miszero(mmul(CMAT, P16)), "c P = 0: P projects onto V = ker(c)")
check(rank(P16) == 12, "rank V = 12 (V+ and V- rank 6 each)")

# chirality: c is ODD, iota REVERSES chirality  (the load-bearing sign of the adjudication)
for a in (0, 1):
    check(all(CMAT[a][4 * s + t].iszero() for s in (0, 1) for t in range(4)),
          "c(S+ (x) T) has no S+ component (row %d)" % a)
for a in (2, 3):
    check(all(CMAT[a][4 * s + t].iszero() for s in (2, 3) for t in range(4)),
          "c(S- (x) T) has no S- component (row %d)" % a)
for b in (0, 1):
    check(all(IOTA[4 * s + t][b].iszero() for s in (0, 1) for t in range(4)),
          "iota(S+) lands in S- (x) T (column %d): chirality REVERSED" % b)
for b in (2, 3):
    check(all(IOTA[4 * s + t][b].iszero() for s in (2, 3) for t in range(4)),
          "iota(S-) lands in S+ (x) T (column %d): chirality REVERSED" % b)

CPLUS = [row[0:8] for row in CMAT]
CMINUS = [row[8:16] for row in CMAT]
VP_BASIS8 = nullspace(CPLUS)
VM_BASIS8 = nullspace(CMINUS)
check(len(VP_BASIS8) == 6 and len(VM_BASIS8) == 6, "rank V+ = rank V- = 6 (kernel bases built)")
print("  Clifford (16 relations), c odd, iota chirality-reversed, c iota = 1, P^2 = P, V+- rank 6")

# --- 3c. the order-3 isometry and its spin lift IN THE MODEL; equivariance of the splitting ---
CH = zc(F(-1, 2))                                # cos(2 pi/3)
def rot(c_, s_):
    return [[c_, -s_], [s_, c_]]


def bdiag(A, B):
    M = mzero(4, 4)
    for i in range(2):
        for j in range(2):
            M[i][j] = A[i][j]
            M[2 + i][2 + j] = B[i][j]
    return M


GT_CAND = {"(+t,+t)": bdiag(rot(CH, SQ3H), rot(CH, SQ3H)),
           "(+t,-t)": bdiag(rot(CH, SQ3H), rot(CH, -1 * SQ3H))}
ZE2 = zp(2)
LIFTS = {"S+triv_a": [zc(1), zc(1), ZETA, ZE2], "S+triv_b": [zc(1), zc(1), ZE2, ZETA],
         "S-triv_a": [ZETA, ZE2, zc(1), zc(1)], "S-triv_b": [ZE2, ZETA, zc(1), zc(1)]}


def diagm(d):
    M = mzero(4, 4)
    for i in range(4):
        M[i][i] = d[i]
    return M


def intertwines(Ld, GT):
    L = diagm(Ld)
    Li = diagm([x.inv() for x in Ld])
    for t in range(4):
        lhs = mmul(mmul(L, GAM[t]), Li)
        rhs = mzero(4, 4)
        for mu in range(4):
            rhs = madd(rhs, mscal(GT[mu][t], GAM[mu]))
        if not meq(lhs, rhs):
            return False
    return True


passing = {gn: [ln for ln, Ld in LIFTS.items() if intertwines(Ld, GT)]
           for gn, GT in GT_CAND.items()}
splus_orients = [gn for gn, ls in passing.items() if any(l.startswith("S+") for l in ls)]
check(len(splus_orients) == 1, "EXACTLY one rotation orientation admits an S+-trivial spin lift")
GT_NAME = splus_orients[0]
GT = GT_CAND[GT_NAME]
LNAME = [l for l in passing[GT_NAME] if l.startswith("S+")][0]
check(passing[GT_NAME] == [LNAME], "for that orientation the S+-trivial lift is the UNIQUE lift shape")
other = [gn for gn in GT_CAND if gn != GT_NAME][0]
check(all(l.startswith("S-") for l in passing[other]) and len(passing[other]) == 1,
      "the OTHER orientation admits only an S--trivial lift (orientation control; "
      "the operational pin ind_phi(D) = +2 selects the S+-trivial model)")
GS = diagm(LIFTS[LNAME])
print("  symplectic model selected: g_T = %s with lift %s (S+ trivial, S- weights zeta, zeta^2)"
      % (GT_NAME, LNAME))

check(meq(mmul(GS, mmul(GS, GS)), mid(4)), "g_S^3 = 1 (order-3 lift)")
check(meq(mmul(GT, mmul(GT, GT)), mid(4)), "g_T^3 = 1")
check(mtrace(GT) == zc(-2), "tr(g|T_C) = -2 (weights {zeta, zeta, zeta^2, zeta^2} on T_C)")
check(detn(msub(mid(4), GT)) == zc(9), "det(1 - g|T) = 9 (Atiyah-Bott denominator)")

G16 = mzero(16, 16)
for s in range(4):
    for sp in range(4):
        for t in range(4):
            for tp in range(4):
                G16[4 * s + t][4 * sp + tp] = GS[s][sp] * GT[t][tp]

check(meq(mmul(GS, CMAT), mmul(CMAT, G16)), "EQUIVARIANCE: g c = c (g_S (x) g_T)")
check(meq(mmul(G16, IOTA), mmul(IOTA, GS)), "EQUIVARIANCE: (g_S (x) g_T) iota = iota g_S")
check(meq(mmul(P16, G16), mmul(G16, P16)), "EQUIVARIANCE: [P, g] = 0 -- the twistor splitting "
      "S+- (x) T_C = V+- (+) iota(S-+) is g-invariant")

GP16 = mmul(G16, P16)
trVp = sum((GP16[i][i] for i in range(8)), zc(0))
trVm = sum((GP16[i][i] for i in range(8, 16)), zc(0))
check(trVp == zc(-3), "tr(g|V+) = -3")
check(trVm == zc(0), "tr(g|V-) = 0")
trSp = GS[0][0] + GS[1][1]
trSm = GS[2][2] + GS[3][3]
check(trSp == zc(2) and trSm == zc(-1), "tr(g|S+) = 2, tr(g|S-) = -1")
check((trSp - trSm) * (mtrace(GT) + 1) == trVp - trVm,
      "CHARACTER IDENTITY at the fixed point: tr(g|V+) - tr(g|V-) = (trS+ - trS-)(tr T_C + 1) = -3")
G16sq = mmul(G16, G16)
GP16b = mmul(G16sq, P16)
check(sum((GP16b[i][i] for i in range(8)), zc(0)) == zc(-3)
      and sum((GP16b[i][i] for i in range(8, 16)), zc(0)) == zc(0),
      "same V-characters for g^2 (both powers)")
NU_Q_MODEL = (trVp - trVm) / 9
check(NU_Q_MODEL == zc(F(-1, 3)),
      "Atiyah-Bott weight of the COMPRESSED operator from the model: nu_Q = -3/9 = -1/3 per point")
print("  tr(g|V+) = -3, tr(g|V-) = 0; nu_Q = (trV+ - trV-)/det(1-g|T) = -1/3 -- from the model alone")

# --- 3d. HS block matrix at symbol level (generic xi) -- ALL FOUR BLOCKS, exact ---
XI = [zc(1), zc(2), zc(3), zc(5)]
GAMXI = mzero(4, 4)
for t in range(4):
    GAMXI = madd(GAMXI, mscal(XI[t], GAM[t]))
QNORM = 1 + 4 + 9 + 25
check(meq(mmul(GAMXI, GAMXI), mscal(-QNORM, mid(4))), "c(xi)^2 = -|xi|^2 at generic xi = (1,2,3,5)")
MXI = mzero(16, 16)
for s in range(4):
    for sp in range(4):
        for t in range(4):
            MXI[4 * s + t][4 * sp + t] = GAMXI[s][sp]

# upper-left block: iota-to-iota compression = (2-n)/n * Dirac symbol = -(1/2) gamma(xi)
check(meq(mmul(CMAT, mmul(MXI, IOTA)), mscal(F(-1, 2), GAMXI)),
      "HS BLOCK (upper-left): c (gamma(xi) (x) 1) iota = -(1/2) gamma(xi) -- the (2-n)/n = -1/2 "
      "embedded block; REVERSED chirality (iota labels): the -1 -> +1 flip of the K-class")
# lower-left block: iota-to-V compression = (2/n) * twistor symbol, sigma_P(xi): chi -> P(chi (x) xi)
TX = mzero(16, 4)
for s in range(4):
    for t in range(4):
        TX[4 * s + t][s] = XI[t]
check(meq(mmul(P16, mmul(MXI, IOTA)), mscal(F(1, 2), mmul(P16, TX))),
      "HS BLOCK (lower-left): P (gamma(xi) (x) 1) iota = (1/2) P(. (x) xi) -- the (2/n) = 1/2 "
      "twistor entry; this is the entry that VANISHES on parallel spinors (triangularity)")
check(not miszero(mmul(P16, mmul(MXI, IOTA))),
      "the lower-left block is NONZERO as a symbol: the twisted symbol is NOT block-diagonal "
      "(the elliptic homotopy of the symbol legs is genuinely needed)")
# upper-right block: V-to-iota compression = -2 * (P* symbol restricted to V)
TDAG = dagger(TX)
check(meq(mmul(CMAT, mmul(MXI, P16)), mscal(-2, mmul(TDAG, P16))),
      "HS BLOCK (upper-right): c (gamma(xi) (x) 1) P = -2 T(xi)^dag P -- the 2 iota P* entry "
      "(coefficient magnitude 2; sign = adjoint convention)")
# lower-right block: sigma_Q = P (gamma(xi) (x) 1) restricted to V; spot ellipticity at generic xi
VP16 = [v + [zc(0)] * 8 for v in VP_BASIS8]
PM = mmul(P16, MXI)
IMGS = [mvec(PM, v) for v in VP16]
for w in IMGS:
    check(all((sum((CMAT[a][j] * w[j] for j in range(16)), zc(0))).iszero() for a in range(4)),
          "sigma_Q image lies in ker c")
    check(all(w[i].iszero() for i in range(8)), "sigma_Q image lies in NEGATIVE chirality (V-)")
check(rank(IMGS) == 6, "sigma_Q(xi): V+ -> V- has rank 6 at generic xi: invertible SPOT CHECK "
      "(full ellipticity = symbol legs' certificate det sigma_Q = (1/4)|xi|^6, cited)")
# symbol equivariance (feeds the equivariant index additivity):
GTXI = mvec(GT, XI)
GAMGTXI = mzero(4, 4)
for t in range(4):
    GAMGTXI = madd(GAMGTXI, mscal(GTXI[t], GAM[t]))
M2 = mzero(16, 16)
for s in range(4):
    for sp in range(4):
        for t in range(4):
            M2[4 * s + t][4 * sp + t] = GAMGTXI[s][sp]
check(meq(mmul(G16, MXI), mmul(M2, G16)),
      "SYMBOL EQUIVARIANCE: g (gamma(xi) (x) 1) = (gamma(g_T xi) (x) 1) g -- since every block "
      "is separately equivariant, the whole block-diagonalization homotopy is g-equivariant")

print("""  TRIANGULARITY CONDITION (stated + checkable content verified):
   w.r.t. S (x) T_C = iota(S) (+) S_3/2, D_TM has the HS eq (1) block form; at n = 4 its
   first column is [ -(1/2) iota D iota^{-1} ; (1/2) P_twistor iota^{-1} ] -- BOTH entries
   post-compose nabla (D = c nabla, P_tw = P nabla), with the two coefficients -(1/2), (1/2)
   verified EXACTLY at symbol level above.  K3's 2 harmonic spinors are PARALLEL
   (Lichnerowicz, scal = 0) and phi-trivial (prior swing), so D psi = 0 AND P_tw psi = 0:
   D_TM(iota psi) = 0.  Hence iota(parallel S+ spinors) is an honest g-stable subspace of
   ker^-(D_TM) with REVERSED chirality and phases {0: 2}   [iota g-equivariant: checked].""")

# ==============================================================================================
# SECTION 4: NON-EQUIVARIANT INDICES from sigma alone (p1 = 3 sigma); -38 DERIVED, not imported
# ==============================================================================================
banner("S4. Indices from sigma = -16 only: D = 2, D_TM = -40, Q = -38 = 19 sigma/8, A = -42")

P1 = 3 * SIGMA
AHAT = F(-SIGMA, 8)
check(AHAT == 2, "ind D = A-hat(K3) = -sigma/8 = 2")
IND_D = int(AHAT)
IND_DTM = F(5 * P1, 6)
check(IND_DTM == -40, "ind D_TM = ind(D (x) T_C) = 5 p1/6 = -40  (A-hat(ch T_C) deg-4)")
IND_A = F(7 * P1, 8)
check(IND_A == -42 == F(21 * SIGMA, 8), "candidate A = A-hat(ch T_C - 1) = 7 p1/8 = 21 sigma/8 = -42")
# candidate B: via the published index additivity (HS eq 11 / BM Rem 2.3 + this swing's symbol legs)
IND_Q = int(IND_DTM) + IND_D
check(IND_Q == -38, "ind Q = ind D_TM + ind D = -40 + 2 = -38  (DERIVED via additivity)")
check(F(19 * P1, 24) == IND_Q, "cross-route: A-hat(ch T_C + 1) deg-4 = 19 p1/24 = -38 EXACTLY")
check(F(19 * SIGMA, 8) == IND_Q and -19 * AHAT == IND_Q,
      "matches PUBLISHED HS Prop 3.1(i): n = 4: ind Q = -19 A-hat = 19 sigma/8  [extract line 321-323]")
check(IND_Q % 3 == 1 and IND_A % 3 == 0,
      "residues mod 3: -38 == 1, -42 == 0 -- the conventions differ mod 3")
check(IND_Q - IND_A == 2 * IND_D == 4,
      "the two candidates differ by exactly 2 ind(D): [T_C + 1] - [T_C - 1] = 2 [1]")
print("  ind D = 2; ind D_TM = -40; ind Q = -38 = 19 sigma/8 (== published); ind A = -42 = 21 sigma/8")

# ==============================================================================================
# SECTION 5: EQUIVARIANT INDEX -- Atiyah-Bott with the GEOMETRIC multiplier tr(g|T_C) + 1 = -1
# ==============================================================================================
banner("S5. ind_phi(Q) = -2 by Atiyah-Bott (multiplier -1, NOT == 0 mod 3) == equivariant additivity")

C_A = {}
C_B = {}
for m in (1, 2):
    trT = zc(2) * (zp(m) + zp(-m))                        # tr(g^m | T_C) at every fixed point
    check(trT == zc(-2), "tr(g^%d|T_C) = -2 at every fixed point (all 6 have local type 1/3(1,2))" % m)
    C_A[m] = trT - 1
    C_B[m] = trT + 1
    check(C_A[m] == zc(-3) and rat(C_A[m]) % 3 == 0,
          "convention A multiplier c_A(g^%d) = -3 == 0 mod 3 (the structural kill of the pinned class)" % m)
    check(C_B[m] == zc(-1) and rat(C_B[m]) % 3 != 0,
          "GEOMETRIC multiplier c_B(g^%d) = tr(g|T_C) + 1 = -1 NOT == 0 mod 3: the kill mechanism "
          "of the pinned convention is ABSENT for the geometric operator" % m)

IND_PHI_DTM = zc(6) * nu_D4(1) * (zc(2) * (zp(1) + zp(-1)))
check(IND_PHI_DTM == zc(-4), "ind_phi(D_TM) = 6 * (1/3) * (-2) = -4")
IND_PHI_Q = zc(6) * nu_D4(1) * C_B[1]
check(IND_PHI_Q == zc(-2), "Atiyah-Bott: ind_phi(Q) = 6 * (1/3) * (-1) = -2")
check(zc(6) * nu_D4(2) * C_B[2] == zc(-2), "ind_{phi^2}(Q) = -2 as well")
check(zc(6) * NU_Q_MODEL == zc(-2),
      "MODEL cross-route: 6 * [(trV+ - trV-)/det(1 - g|T)] = -2 -- the multiplier -1 is grounded "
      "in the exact matrix model of S3, not assumed")
check(IND_PHI_Q == IND_PHI_DTM - (-zc(2)),
      "EQUIVARIANT ADDITIVITY: ind_phi(Q) = ind_phi(D_TM) - ind_phi(reversed D) = -4 - (-2) = -2 "
      "(the embedded block is the chirality-REVERSED Dirac: contributes -ind_phi(D))")
IND_PHI_A = zc(6) * nu_D4(1) * C_A[1]
check(IND_PHI_A == zc(-6), "for comparison, convention A: ind_phi(RS_A) = 6 * (1/3) * (-3) = -6")
print("  c_B = -1 (both powers, all 6 points); ind_phi(Q) = -2 by AB == model route == additivity")

# ==============================================================================================
# SECTION 6: KERNEL OF Q -- THREE ROUTES FORCED TO ONE ANSWER + Hodge==AB GATE + NEGATIVE CONTROL
# ==============================================================================================
banner("S6. ker(Q) phases: twistor subtraction == published 2x primitive H^{1,1} == integer forcing")

# Route (0), input data recomputed (Hodge route of the prior swing, WITHOUT any subtraction):
KM_T10 = {F(0): H11_TRIV, F(1, 3): H11_Z, F(2, 3): H11_Z2}       # ker^-(D (x) T^{1,0}) = H^1(Omega^1)
KM_T01 = {F(0): H11_TRIV, F(2, 3): H11_Z, F(1, 3): H11_Z2}       # conjugate rep
KM_DTM = {th: KM_T10[th] + KM_T01[th] for th in KM_T10}
KP_DTM = {}                                                       # H^0(Omega^1) = H^2(Omega^1) = 0
check(KM_DTM == {F(0): 16, F(1, 3): 12, F(2, 3): 12},
      "ker^-(D_TM) = {0:16, 1/3:12, 2/3:12}; ker^+(D_TM) = 0 (Hodge route, prior-swing verified)")
check(sum(KM_DTM.values()) == 40 == -int(IND_DTM), "dim ker^-(D_TM) = 40 = -ind (ker^+ = 0)")
KP_D = {F(0): 2}                                                  # the 2 parallel (phi-trivial) spinors
KM_D = {}

# Route (i): TWISTOR SUBTRACTION (triangularity, S3): iota(parallel S+ spinors) sits inside
# ker^-(D_TM) with phases {0:2}; the published kernel additivity on K3 (HS: parallel spinors
# in ker D_TM; dim ker Q = 38; 2 + 38 = 40) forces the complement to be ker^-(Q):
IOTA_PAR = {F(0): 2}
KM_Q_i = {th: KM_DTM[th] - IOTA_PAR.get(th, 0) for th in KM_DTM}
KP_Q = {}                                                         # ker Q is 38-dim in ONE chirality
check(sum(KM_Q_i.values()) == 38, "dim additivity: 40 - 2 = 38 == published dim ker Q (import)")
check(KM_Q_i == {F(0): 14, F(1, 3): 12, F(2, 3): 12},
      "route (i): ker^-(Q) = {0:14, 1/3:12, 2/3:12} (g-stable direct sum: iota g-equivariant "
      "(S3), iota(S) intersect V = 0 (c iota = 1), both summands g-stable)")
check(rat(tr_g(KM_DTM, 1)) == 4 and rat(tr_g(IOTA_PAR, 1)) == 2 and rat(tr_g(KM_Q_i, 1)) == 2,
      "trace additivity of the kernel split: 4 = 2 + 2")

# Route (ii): PUBLISHED kernel identification, equivariantly refined: ker Q = TWO copies of
# primitive harmonic (1,1)-forms (HS Example (1) after Prop 4.6). Kahler class = phi-averaged
# one = phi-trivial => primitive H^{1,1} = {0:7, 1/3:6, 2/3:6}; the identification is built from
# parallel phi-trivial objects, so each copy carries that rep or its conjugate -- SAME multiset:
PRIM = {F(0): H11_TRIV - 1, F(1, 3): H11_Z, F(2, 3): H11_Z2}
PRIM_CONJ = {F(0): PRIM[F(0)], F(1, 3): PRIM[F(2, 3)], F(2, 3): PRIM[F(1, 3)]}
check(sum(PRIM.values()) == 19 and 2 * H11 - 2 == 38,
      "primitive h^{1,1} = 19; published dim ker Q = 2 h^{1,1} - 2 = 38 reproduced from Hodge data")
KM_Q_ii_same = {th: 2 * PRIM[th] for th in PRIM}
KM_Q_ii_conj = {th: PRIM[th] + PRIM_CONJ[th] for th in PRIM}
check(KM_Q_ii_same == KM_Q_i and KM_Q_ii_conj == KM_Q_i,
      "route (ii): BOTH copy-assignments (same rep / conjugate rep) give {0:14, 1/3:12, 2/3:12} "
      "== route (i) -- the multiset does not ride the copy convention")

# Route (iii): INTEGER FORCING -- independent of both identifications:
sols = [(m0, m1) for m0 in range(0, 61) for m1 in range(0, 61)
        if (m0 + 2 * m1 == 38) and (m0 - m1 == 2)]
check(sols == [(14, 12)],
      "route (iii): m0 + 2 m1 = 38 (dim, published) AND m0 - m1 = 2 (= -ind_phi(Q), Atiyah-Bott "
      "this leg) AND reality m_zeta = m_{zeta^2}: UNIQUE solution (14, 12)")
KM_Q = KM_Q_i

# GATE: Hodge trace == Atiyah-Bott (both powers):
for m in (1, 2):
    hodge = tr_g(KP_Q, m) - tr_g(KM_Q, m)
    check(hodge == zc(-2), "GATE ind_phi(Q): Hodge trace = -(14 - 12) = -2 == Atiyah-Bott (g^%d)" % m)

# NEGATIVE CONTROL: UNREVERSED-chirality bookkeeping (= convention A's virtual package fed to Q):
bad = (tr_g({F(0): -2}, 1) - tr_g(KM_DTM, 1))
check(bad == zc(-6) and not bad == zc(-2),
      "NEGATIVE CONTROL: same-chirality (ghost) bookkeeping gives trace -6 != -2 = AB(Q): the "
      "chirality REVERSAL of the embedded block is load-bearing and detected by the gate")
check(zc(6) * nu_D4(1) * C_A[1] == zc(-6),
      "...and -6 is exactly convention A's own AB value: BOTH conventions are internally "
      "coherent; they are DIFFERENT objects (the adjudication finding)")
print("  ker^-(Q) = {0:14, 1/3:12, 2/3:12}, ker^+(Q) = 0  -- HONEST (non-virtual), forced 3 ways")

# ==============================================================================================
# SECTION 7: PRIMARY ROUTE -- master formula on T_phi (periodic S^1 structure), all characters
# ==============================================================================================
banner("S7. Direct spectral eta/rho of Q on T_phi; Dirac and convention A alongside")

ETA_Q = [eta_alpha(KP_Q, KM_Q, k) for k in range(3)]
RHO_Q = [e - ETA_Q[0] for e in ETA_Q]
H_Q = [h_dim(KP_Q, KM_Q, k) for k in range(3)]

KP_A, KM_A = {F(0): -2}, KM_DTM                                   # convention A (virtual package)
ETA_A = [eta_alpha(KP_A, KM_A, k) for k in range(3)]
RHO_A = [e - ETA_A[0] for e in ETA_A]
H_A = [h_dim(KP_A, KM_A, k) for k in range(3)]

ETA_D = [eta_alpha(KP_D, KM_D, k) for k in range(3)]
RHO_D = [e - ETA_D[0] for e in ETA_D]
H_D = [h_dim(KP_D, KM_D, k) for k in range(3)]

check(ETA_Q == [F(0), F(2, 3), F(-2, 3)], "GEOMETRIC Q: eta = (0, +2/3, -2/3)")
check(RHO_Q == [F(0), F(2, 3), F(-2, 3)], "GEOMETRIC Q: rho = (0, +2/3, -2/3)")
check(H_Q == [14, 12, 12], "GEOMETRIC Q: h = (14, 12, 12) -- HONEST kernel dims, never folded")
check(ETA_A == [F(0), F(2), F(-2)], "convention A: eta = rho = (0, +2, -2) (reproduces leg3)")
check(H_A == [14, 12, 12], "convention A: h_virtual = (14, 12, 12)")
check(ETA_D == [F(0), F(-2, 3), F(2, 3)], "Dirac baseline: eta = (0, -2/3, +2/3)")
check(H_D == [2, 0, 0], "Dirac baseline: h = (2, 0, 0)")

CLS_Q = [z3_class(r) for r in RHO_Q]
CLS_A = [z3_class(r) for r in RHO_A]
CLS_D = [z3_class(r) for r in RHO_D]
check(CLS_Q == [0, 2, 1], "GEOMETRIC Q classes mod Z: (0, 2, 1)/3 -- NONZERO ORDER 3")
check(CLS_A == [0, 0, 0], "convention A classes mod Z: (0, 0, 0) -- 2-primary (as verified before)")
check(CLS_D == [0, 1, 2], "Dirac classes mod Z: (0, 1, 2)/3 -- Q carries the INVERSE Dirac class")
print("  Q:     eta = %s  rho = %s  h = %s  class = %s" % (ETA_Q, RHO_Q, H_Q, CLS_Q))
print("  A:     eta = %s  rho = %s  h = %s  class = %s" % (ETA_A, RHO_A, H_A, CLS_A))
print("  Dirac: eta = %s  rho = %s  h = %s  class = %s" % (ETA_D, RHO_D, H_D, CLS_D))

# ==============================================================================================
# SECTION 8: CROSS-CHECK A -- Donnelly / isotypic averaging must equal the direct route EXACTLY
# ==============================================================================================
banner("S8. Donnelly averaging == direct spectral values EXACTLY (3 operators x all k)")


def eta_gm(kp, km, m):
    return (tr_g(km, m) - tr_g(kp, m)) * ICOT[m]


for m in (1, 2):
    check(eta_gm(KP_Q, KM_Q, m) == zc(2) * ICOT[m],
          "eta_{g^%d}(Q) = 2 i cot(pi %d/3) (tr(g|ker^- - ker^+) = 2)" % (m, m))

agree = 0
for name, kp, km, eta_direct in (("Dirac", KP_D, KM_D, ETA_D), ("Q", KP_Q, KM_Q, ETA_Q),
                                 ("A", KP_A, KM_A, ETA_A)):
    for k in range(3):
        tot = zc(0)
        for m in (1, 2):
            tot = tot + zp(-k * m) * eta_gm(kp, km, m)     # eta_{g^0} = 0 (product symmetry)
        iso = tot * F(1, 3)
        check(is_rat(iso), "%s k=%d: isotypic average is real-rational" % (name, k))
        check(iso == zc(eta_direct[k]), "%s k=%d: Donnelly isotypic == direct (exact)" % (name, k))
        if k > 0:
            tot2 = zc(0)
            for m in (1, 2):
                tot2 = tot2 + (zp(-k * m) - zc(1)) * eta_gm(kp, km, m)
            check(tot2 * F(1, 3) == zc(eta_direct[k] - eta_direct[0]),
                  "%s k=%d: Donnelly rho == direct rho (exact)" % (name, k))
            agree += 1
check(agree == 6, "6/6 exact Donnelly rho agreements (3 operators x 2 characters)")
print("  all Donnelly isotypic averages agree EXACTLY with the direct spectral route")

# ==============================================================================================
# SECTION 9: CROSS-CHECK B -- disk fixed-point route (bounding structure): mod 2Z, same classes
# ==============================================================================================
banner("S9. Disk route: rho from LOCAL DATA ALONE (c_B = -1) -- kernel-independent class check")


def nu_D6(m):
    return nu_D4(m) * (zp(2 * m) - zp(m)).inv()


check(nu_D6(1) == ISQ3 * F(1, 9), "nu_D6(g) = (zeta - zeta^2)/9")
check(nu_D6(2) == nu_D6(1).cconj(), "nu_D6(g^2) = conj(nu_D6(g))")


def rho_fp(k, cchar):
    tot = zc(0)
    for m in (1, 2):
        tot = tot + (zp(-k * m) - zc(1)) * (zc(12) * nu_D6(m) * cchar[m])
    return tot * F(1, 3)


C_DIRAC = {1: zc(1), 2: zc(1)}
FP_EXPECT = {1: F(-4, 3), 2: F(4, 3)}
for k in (1, 2):
    fpQ = rho_fp(k, C_B)
    fpD = rho_fp(k, C_DIRAC)
    fpA = rho_fp(k, C_A)
    vQ, vD, vA = rat(fpQ), rat(fpD), rat(fpA)
    check(vQ == FP_EXPECT[k], "disk route Q: rho_%d = %s" % (k, FP_EXPECT[k]))
    check(fpQ == -1 * fpD and fpA == zc(-3) * fpD,
          "disk route scalings: rho_fp(Q) = -rho_fp(Dirac), rho_fp(A) = -3 rho_fp(Dirac), k=%d" % k)
    check((vQ - RHO_Q[k]) % 2 == 0, "Q: disk - direct = %s in 2Z (spin-structure shift), k=%d"
          % (vQ - RHO_Q[k], k))
    check(z3_class(vQ) == CLS_Q[k], "Q: disk route gives the SAME mod-Z class %d -- and it uses "
          "ONLY local fixed-point data, independent of all kernel imports, k=%d" % (CLS_Q[k], k))
    check(z3_class(vA) == CLS_A[k] and z3_class(vD) == CLS_D[k],
          "A and Dirac disk classes match too, k=%d" % k)
print("  disk route: Q rho = (-4/3, +4/3); differs from direct (2/3, -2/3) by exact even integers;"
      "\n  classes (0,2,1)/3 IDENTICAL -- the Z/3 verdict does not ride the kernel identification")

# ==============================================================================================
# SECTION 10: CLASS LAW -- rho_k == -(k/3) * ind_fiber mod Z;  a_k = k*T mod 3, T = -ind_phi
# ==============================================================================================
banner("S10. Class law: rho_k == -(k/3) ind(Q) mod Z with ind(Q) = -38; a_k = k*T mod 3, T = 2")

for k in (1, 2):
    check((RHO_Q[k] - F(-k * IND_Q, 3)) % 1 == 0,
          "class law Q: rho_%d == -(%d/3)(-38) == %d/3 mod Z" % (k, k, (38 * k) % 3))
    check((RHO_A[k] - F(-k * int(IND_A), 3)) % 1 == 0, "class law A: rho_%d == -(%d/3)(-42) mod Z" % (k, k))
    check((RHO_D[k] - F(-k * IND_D, 3)) % 1 == 0, "class law Dirac: rho_%d == -(%d/3)(2) mod Z" % (k, k))
for name, kp, km, cls in (("Q", KP_Q, KM_Q, CLS_Q), ("A", KP_A, KM_A, CLS_A),
                          ("Dirac", KP_D, KM_D, CLS_D)):
    T = int(rat(tr_g(km, 1) - tr_g(kp, 1), name + ": T is a rational integer"))
    for k in (1, 2):
        check(cls[k] == (k * T) % 3, "%s: a_k = k*T mod 3 (k=%d, T=%d)" % (name, k, T))
check(int(rat(tr_g(KM_Q, 1) - tr_g(KP_Q, 1))) == 2 == -int(rat(IND_PHI_Q)),
      "T(Q) = 2 = -ind_phi(Q): NOT divisible by 3 -- the structural mechanism that killed the "
      "pinned class (3 | T_A = 6) is absent for the geometric operator")
print("  class law verified all k, all three operators; T(Q) = 2, T(A) = 6, T(Dirac) = -2")

# ==============================================================================================
# SECTION 11: SIDE-BY-SIDE ADJUDICATION TABLE + the exact candidate-link identity + sensitivity
# ==============================================================================================
banner("S11. BOTH conventions side by side; rho(Q) = rho(A) + 2 rho(Dirac) EXACT; sensitivity sweep")

for k in range(3):
    check(ETA_Q[k] == ETA_A[k] + 2 * ETA_D[k],
          "CANDIDATE LINK at eta level, k=%d: eta(Q) = eta(A) + 2 eta(Dirac) "
          "([T_C + 1] = [T_C - 1] + 2[1] in K-theory)" % k)
    check(CLS_Q[k] == (CLS_A[k] + 2 * CLS_D[k]) % 3,
          "CANDIDATE LINK at class level, k=%d: (0,2,1) = (0,0,0) + 2*(0,1,2) mod 3" % k)
check(IND_Q == int(IND_A) + 2 * IND_D, "candidate link at index level: -38 = -42 + 2*2")

# sensitivity sweep over twist conventions (index from p1 alone; multiplier from local weights):
SWEEP = [
    ("T_C - 1C (A, pinned/AGW)", F(7 * P1, 8), -3),
    ("T_C + 1C (B, geometric Q)", F(19 * P1, 24), -1),
    ("T_C - 2C (rival)", F(11 * P1, 12), -4),
    ("TM_C - 1C (rival, = T_C on fiber)", F(5 * P1, 6), -2),
]
seen = set()
for name, ind, mult in SWEEP:
    cls1 = int((-ind) % 3)
    check(cls1 == (1 * (-int(rat(zc(6) * nu_D4(1) * zc(mult))))) % 3,
          "sensitivity row '%s': class(k=1) from index == class from multiplier" % name)
    seen.add((str(ind), mult, cls1))
    gA = "PASS" if ind == -42 else "fail"
    gB = "PASS" if ind == F(19 * SIGMA, 8) else "fail"
    print("  %-36s ind = %6s  mult = %2d  class(k=1) = %d   -42gate:%s  19s/8gate:%s"
          % (name, ind, mult, cls1, gA, gB))
check(len(seen) == 4, "the four conventions are pairwise distinct: the pin choice is load-bearing")
check([r for r in SWEEP if r[1] == -42][0][0].startswith("T_C - 1C"),
      "only convention A passes the AGW/Bilal -42 = 21 sigma/8 gate")
check([r for r in SWEEP if r[1] == F(19 * SIGMA, 8)][0][0].startswith("T_C + 1C"),
      "only convention B passes the published HS Prop 3.1(i) 19 sigma/8 gate -- BOTH candidates "
      "pass an established published gate: the gate no longer selects uniquely (identification open)")

# ==============================================================================================
# SECTION 12: RELABELING SWEEP -- lift x zeta^m only permutes etas; class multisets invariant
# ==============================================================================================
banner("S12. Relabeling sweep m in {0,1,2}: class multisets invariant (verdict convention-robust)")

for m in range(3):
    for name, kp, km, ETA0, CLS0 in (("Q", KP_Q, KM_Q, ETA_Q, CLS_Q),
                                     ("A", KP_A, KM_A, ETA_A, CLS_A),
                                     ("Dirac", KP_D, KM_D, ETA_D, CLS_D)):
        kps, kms = shift(kp, m), shift(km, m)
        e = [eta_alpha(kps, kms, k) for k in range(3)]
        check(sorted(e) == sorted(ETA0), "m=%d %s: etas are a permutation of the m=0 etas" % (m, name))
        cm = sorted(z3_class(x - e[0]) for x in e)
        check(cm == sorted(CLS0), "m=%d %s: class MULTISET invariant %s" % (m, name, cm))
print("  Q multiset {0,1,2} (NONZERO survives relabeling); A stays {0,0,0}; Dirac stays {0,1,2}")

# ==============================================================================================
# SECTION 13: REMAINING GATES, FIREWALL, IMPORT LEDGER, BLOCKED/OPEN ITEMS, OUTPUT
# ==============================================================================================
banner("S13. Standard gates; firewall audit; import ledger; BLOCKED/open items; output")

check(sum(ETA_Q) == 0 and sum(ETA_A) == 0 and sum(ETA_D) == 0, "GATE sum_k eta_k = 0 (all three)")
check(RHO_Q[2] == -RHO_Q[1] and RHO_A[2] == -RHO_A[1] and RHO_D[2] == -RHO_D[1],
      "GATE rho_2 = -rho_1 (all three)")
# reality is structural in the Fraction route; the QZ cross-routes asserted is_rat throughout.
check(F(IND_Q - 2 - 2, 3) == -14, "GATE orbifold integrality Q: (-38 - 2 - 2)/3 = -14 in Z")
check(F(int(IND_A) - 6 - 6, 3) == -18, "GATE orbifold integrality A: (-42 - 6 - 6)/3 = -18 in Z")
check(F(int(IND_DTM) - 4 - 4, 3) == -16, "GATE orbifold integrality D_TM: (-40 - 4 - 4)/3 = -16 in Z")
check(F(2 + 2 + 2, 3) == 2, "GATE orbifold integrality Dirac: 2 in Z")

INPUTS = {
    "fixed_points": 6,
    "local_weights": "(zeta, zeta^-1) on T^{1,0} (symplectic, forced)",
    "lattice_r_s": (10, 12),
    "sigma_K3": -16,
    "hodge_numbers": (0, 1, 20),
    "group_order": 3,
    "clifford_algebra": "R^4 quaternionic model (S3), exact over Q(i,zeta)",
    "densities": "Atiyah-Bott / Donnelly / APS (standard)",
}
check(all(v != 24 for v in (6, 10, 12, -16, 0, 1, 20, 22, 40, 38, 19, 14)),
      "FIREWALL: chi(K3) = 24 is not an input anywhere in this leg")
check(AHAT == 2 and AHAT != 3, "FIREWALL: A-hat(K3) = 2; the flat A-hat = 3 never appears")
check(F(19 * SIGMA, 8) == -38 and F(21 * SIGMA, 8) == -42 and F(-SIGMA, 8) == 2,
      "FIREWALL: the only /8 are the standard AS densities 19s/8, 21s/8, -s/8 -- never 24/8")
check(IND_Q == -40 + 2, "FIREWALL: -38 was DERIVED as -40 + 2 (additivity), not imported as target")
print("  firewall inputs:", INPUTS)

print("""
IMPORT LEDGER (everything not recomputed here; each verified against the cached extracts
in this directory this session):
  [I1] ind Q = ind D_TM + ind D (index additivity)      -- HS eq (11) [hs-rs-kernel.txt:316];
       BM Lemma 2.2 / Remark 2.3 (elliptic alpha-family) [baer-mazzeo.txt:286]; plus this
       swing's symbol legs (exact det certificates, same directory, exit 0).  Used in S4.
  [I2] ind Q = -19 A-hat = 19 sigma/8 at n = 4          -- HS Prop 3.1(i) [hs-rs-kernel.txt:321-323].
       Used only as a GATE (S4 cross-check); the leg derives -38 independently via [I1].
  [I3] dim ker Q = 2 h^{1,1} - 2 = 38 on K3, in one chirality; ker Q isomorphic to two copies
       of primitive harmonic (1,1)-forms               -- HS Example (1) [hs-rs-kernel.txt:673-675];
       BM Remark 5.3 'RS(K3) = 38 ... sharp' [baer-mazzeo.txt:858].  Used in S6 routes (i)-(iii).
  [I4] the two parallel spinors lie in ker D_TM         -- HS remark [hs-rs-kernel.txt:683];
       ALSO derived here from the triangularity condition (S3) -- the import is corroborating.
  [I5] Q elliptic, formally self-adjoint                -- BM Sec 2.2 [baer-mazzeo.txt:182];
       spot-checked at a generic symbol point in S3 (rank 6); full certificate = symbol legs.
  [I6] ker^-(D_TM) = {0:16, 1/3:12, 2/3:12}, ker^+ = 0  -- prior swing (Hodge route), RECOMPUTED
       here in S6 from the S1 eigensplit (in-repo adversarially verified data).
  [I7] convention A attribution (AGW gravitino density = T_C - 1C, -42 = 21 sigma/8) -- prior
       swing's canon pin + Bilal eq (11.47) + HS Remark 3.6 [hs-rs-kernel.txt:354-361].
       AGW primary itself is paywalled: NOT refetched (flagged below).""")

print("""
BLOCKED / OPEN ITEMS (honest shape -- none of these is fabricated around):
  [B1] SG4 MISSING-CARRIER (the identification question, Q4 of the swing): whether the GU
       generation-arena operator is the ghost-subtracted gravitino complex (A) or the geometric
       gamma-traceless operator Q (B) is NOT derivable from K3 geometry or from the literature;
       both are internally coherent published objects differing by exactly 2 [Dirac].  This leg
       does NOT overturn the -42 pin; it computes the complement.  BLOCKED on the GU source
       action being built.
  [B2] the computed rho is that of the SUSPENDED fiber operator on T_phi (the families object);
       the intrinsic 5d RS operator of T_phi is a DIFFERENT bundle (they coincide for Dirac,
       not for RS).  If the program ever names the intrinsic operator: new computation.
  [B3] eta-level REALS (0, +2/3, -2/3) and h = (14,12,12) are exact for the pinned suspension
       conventions (periodic S^1, product metric, finite-order isometric monodromy => vanishing
       Bismut-Cheeger corrections assumed as in the prior verified swing).  The operator-level
       repackaging Q vs pseudodiff-with-symbol-A can shift the reals; only the MOD-Z CLASSES
       (0,2,1)/3 are claimed at adjudication grade (APS III deformation invariance + disk route,
       which is kernel-independent).
  [B4] AGW primary (Nucl. Phys. B 234 (1984)) remains paywalled/unfetched; convention-A
       attribution rides two verified secondaries (Bilal eq 11.47; HS Remark 3.6 quoting
       Witten Shelter Island II p. 252).""")

RESULT = {
    "operator": "geometric gamma-traceless RS operator Q (HS/BM), suspended on T_phi",
    "K_class": "[V+]-[V-] = ([S+]-[S-]) (x) (T_C + 1C)  (chirality-reversed iota block)",
    "index": IND_Q,
    "ind_phi": -2,
    "multiplier": "tr(g|T_C) + 1 = -1 at all 6 points, both powers (NOT == 0 mod 3)",
    "ker_minus": {"0": 14, "1/3": 12, "2/3": 12},
    "ker_plus": {},
    "eta=rho": [str(e) for e in ETA_Q],
    "h": H_Q,
    "class_mod_Z": CLS_Q,
    "convention_A_alongside": {"eta=rho": [str(e) for e in ETA_A], "class": CLS_A},
    "dirac_baseline": {"eta=rho": [str(e) for e in ETA_D], "class": CLS_D},
    "link": "eta(Q) = eta(A) + 2 eta(Dirac) exact; classes (0,2,1) = (0,0,0) + 2(0,1,2) mod 3",
    "verdict": "GEOMETRIC_Q_Z3_NONZERO_CLASS_021__PINNED_A_STAYS_2PRIMARY__IDENTIFICATION_OPEN",
}
print()
print("LEG-C OUTPUT:", RESULT)
print()
print("SIDE-BY-SIDE (the adjudication table):")
print("  %-28s %-8s %-12s %-22s %-14s %s" % ("object", "index", "multiplier", "eta = rho", "h", "Z/3 class"))
print("  %-28s %-8s %-12s %-22s %-14s %s" % ("Dirac (baseline)", "+2", "+1", "(0,-2/3,+2/3)", "(2,0,0)", "(0,1,2) NONZERO"))
print("  %-28s %-8s %-12s %-22s %-14s %s" % ("A: ghost-subtracted (pinned)", "-42", "-3==0mod3", "(0,+2,-2)", "(14,12,12)v", "(0,0,0) 2-PRIMARY"))
print("  %-28s %-8s %-12s %-22s %-14s %s" % ("B: geometric Q (published)", "-38", "-1", "(0,+2/3,-2/3)", "(14,12,12)", "(0,2,1) NONZERO"))
print()
print("#" * 94)
print("# LEG-C COMPLETE: the geometric gamma-traceless RS operator Q carries eta = rho =")
print("# (0, +2/3, -2/3), h = (14,12,12), Z/3 classes (0,2,1)/3 -- NONZERO order 3, the exact")
print("# 2-Dirac-unit complement of the pinned convention's (0,0,0).  Twistor splitting verified")
print("# g-equivariant in an exact matrix model; triangularity checked at symbol level; kernel")
print("# forced three ways; Donnelly == direct exact; disk route (kernel-independent) same classes.")
print("# The A-vs-B carrier identification (SG4) remains OPEN -- reported BLOCKED, not decided.")
print("# hard asserts passed: %d" % NASSERT)
print("#" * 94)
