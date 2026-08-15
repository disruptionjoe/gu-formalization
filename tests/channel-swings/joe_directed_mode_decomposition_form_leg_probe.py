#!/usr/bin/env python3
"""Joe-directed wave, gate MD-1: what ARE GU's nine non-SM directions, as 4D fields?

Five negative results in this session (PV-1, PV-2, CU-1, MV-1, MV-2) share one
IMPORTED assumption: that GU's ad-valued fields are conventional Yang-Mills
VECTORS on 4D spacetime, so that the nine surviving non-SM directions of
`k subset so(6,4)` are nine 4D massless gauge bosons.  MV-1 names the
assumption in its own limits section and does not derive it.  This probe tests
the joint.

An ad-valued connection on `Y14 = Met(X4)` carries TWO indices:

  * a FORM leg, in `T*Y14`, which splits at a section into horizontal (4) and
    vertical (10) parts;
  * an AD leg, in `Lambda^2` of the 14-dimensional chimeric carrier, whose
    internal block is `Lambda^2(10) = so(6,4)` -- where the nine live.

The source explicitly disavows Kaluza-Klein ("It's not extra dimensions.  It's
not Kaluza Klein.  The space that is four dimensional births its own 14
dimensional ambient space", `papers/drafts/Transcript into the impossible.md`
line 29), and the author-stated correction WG-B06 says "the relevant map is a
CONTRACTION, not a PROJECTION".  So both reduction maps are computed and
separated:

  PROJECTION  (KK-style; disavowed):  split the form leg into H* and V* and
                                      read each as an independent 4D field.
  CONTRACTION (source-declared):      pull back along the observation section
                                      `s = g`, i.e. contract the form leg with
                                      `ds`.

The decisive structural fact is ENDOGENY.  The fibre of `Y14` is
`Sym^2(T*_x X4)` -- built from the SAME tangent space as the base.  So the
physical local Lorentz algebra `so(3,1)_g` acts on the internal 10, hence on
`so(6,4)`, hence on the ad leg.  The internal index is NOT Lorentz-inert the
way a Kaluza-Klein internal index is.  Everything below is exact rational
arithmetic (`fractions.Fraction`) on integer/rational matrices; signatures are
by Sylvester congruence, never by eigenvalue floats.

NOT computed here: any action, kinetic term, propagator, mass, quantization,
source action, or claim-status movement.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import combinations

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))


# --------------------------------------------------------------------------
# exact linear algebra over Q
# --------------------------------------------------------------------------
def zeros(r: int, c: int) -> list[list[F]]:
    return [[F(0)] * c for _ in range(r)]


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = zeros(n, p)
    for i in range(n):
        Ai = A[i]
        oi = out[i]
        for k in range(m):
            a = Ai[k]
            if a:
                Bk = B[k]
                for j in range(p):
                    if Bk[j]:
                        oi[j] += a * Bk[j]
    return out


def madd(A, B, s=F(1)):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def transpose(A):
    return [list(col) for col in zip(*A)]


def bracket(A, B):
    return madd(matmul(A, B), matmul(B, A), F(-1))


def is_zero(A) -> bool:
    return all(x == 0 for row in A for x in row)


def flat(A):
    return [x for row in A for x in row]


def rref(rows):
    """Return (rref rows, pivot columns).  rows: list of list[F]."""
    M = [list(r) for r in rows]
    if not M:
        return [], []
    ncols = len(M[0])
    piv = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        pivval = M[r][c]
        M[r] = [x / pivval for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    M = [row for row in M[:r]]
    return M, piv


def rank(rows) -> int:
    return len(rref(rows)[0])


def nullspace(rows, ncols):
    """Basis of {x : rows . x = 0}."""
    if not rows:
        return [[F(1) if j == i else F(0) for j in range(ncols)] for i in range(ncols)]
    R, piv = rref(rows)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        basis.append(v)
    return basis


def in_span(vec, basis_rref, piv) -> bool:
    v = list(vec)
    for i, pc in enumerate(piv):
        if v[pc] != 0:
            f = v[pc]
            v = [v[j] - f * basis_rref[i][j] for j in range(len(v))]
    return all(x == 0 for x in v)


def signature(M):
    """Exact (n_pos, n_neg, n_zero) of a rational symmetric matrix, by
    Sylvester congruence.  No eigenvalues, no floats."""
    n = len(M)
    A = [list(r) for r in M]
    for i in range(n):
        for j in range(n):
            assert A[i][j] == A[j][i], "signature() requires a symmetric matrix"
    pos = neg = zero = 0
    idx = list(range(n))
    while idx:
        k = idx[0]
        # find a nonzero diagonal entry in the active block
        d = None
        for i in idx:
            if A[i][i] != 0:
                d = i
                break
        if d is None:
            # all diagonal zero: find an off-diagonal nonzero, congruence row+col add
            found = None
            for i in idx:
                for j in idx:
                    if i != j and A[i][j] != 0:
                        found = (i, j)
                        break
                if found:
                    break
            if found is None:
                zero += len(idx)
                break
            i, j = found
            for c in range(n):
                A[i][c] = A[i][c] + A[j][c]
            for r_ in range(n):
                A[r_][i] = A[r_][i] + A[r_][j]
            continue
        if A[d][d] > 0:
            pos += 1
        else:
            neg += 1
        piv = A[d][d]
        for i in idx:
            if i == d:
                continue
            f = A[i][d] / piv
            if f:
                for c in range(n):
                    A[i][c] = A[i][c] - f * A[d][c]
                for r_ in range(n):
                    A[r_][i] = A[r_][i] - f * A[r_][d]
        idx.remove(d)
        k = k  # silence linters
    return pos, neg, zero


# --------------------------------------------------------------------------
# BLOCK A -- the endogenous fibre and its two forms (cross-check vs canon)
# --------------------------------------------------------------------------
G4 = [[F(0)] * 4 for _ in range(4)]
for a, v in enumerate([-1, 1, 1, 1]):
    G4[a][a] = F(v)
G4INV = [[G4[i][j] for j in range(4)] for i in range(4)]  # diag(-1,1,1,1) is its own inverse

PAIRS = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def sym_basis(p):
    a, b = p
    E = zeros(4, 4)
    E[a][b] += F(1)
    if a != b:
        E[b][a] += F(1)
    return E


EBAS = [sym_basis(p) for p in PAIRS]
check("A1  dim Sym^2(T*X4) = 10", len(EBAS) == 10, f"{len(EBAS)}")


def trace_g(H):
    return sum(G4INV[a][b] * H[b][a] for a in range(4) for b in range(4))


def frob(H, K):
    return sum(
        G4INV[a][b] * H[b][c] * G4INV[c][d] * K[d][a]
        for a in range(4)
        for b in range(4)
        for c in range(4)
        for d in range(4)
    )


TVEC = [trace_g(E) for E in EBAS]
GRAM_F = [[frob(EBAS[i], EBAS[j]) for j in range(10)] for i in range(10)]
GRAM_TR = [[GRAM_F[i][j] - F(1, 2) * TVEC[i] * TVEC[j] for j in range(10)] for i in range(10)]

sf = signature(GRAM_F)
check("A2  Frobenius fibre form has signature (7,3)", sf == (7, 3, 0), f"{sf}")
str_ = signature(GRAM_TR)
check("A3  trace-reversed (DeWitt) fibre form has signature (6,4)", str_ == (6, 4, 0), f"{str_}")

# CONTROL: the trace-reversal parameter genuinely discriminates.  lambda = 1/8
# (below the critical 1/n = 1/4) must NOT flip the trace direction.
GRAM_L18 = [[GRAM_F[i][j] - F(1, 8) * TVEC[i] * TVEC[j] for j in range(10)] for i in range(10)]
s18 = signature(GRAM_L18)
check(
    "A4  CONTROL FIRES: lambda=1/8 trace-reversal gives (7,3), not (6,4)",
    s18 == (7, 3, 0),
    f"{s18}",
)
# CONTROL: the critical value lambda = 1/n = 1/4 must make the trace direction null.
GRAM_L14 = [[GRAM_F[i][j] - F(1, 4) * TVEC[i] * TVEC[j] for j in range(10)] for i in range(10)]
s14 = signature(GRAM_L14)
check("A5  CONTROL FIRES: lambda=1/4 is the degenerate value, signature (6,3,1)", s14 == (6, 3, 1), f"{s14}")

sh = signature([[G4INV[i][j] for j in range(4)] for i in range(4)])
check("A6  horizontal T*X4 carries signature (3,1)", sh == (3, 1, 0), f"{sh}")
check(
    "A7  total chimeric carrier (9,5) = vertical (6,4) + horizontal (3,1)",
    (str_[0] + sh[0], str_[1] + sh[1]) == (9, 5),
    f"{(str_[0] + sh[0], str_[1] + sh[1])}",
)

# --------------------------------------------------------------------------
# BLOCK B -- the endogenous Lorentz algebra acting on the fibre
# --------------------------------------------------------------------------
LOR = []
LOR_LABEL = []
for a, b in combinations(range(4), 2):
    L = zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            L[mu][nu] = (F(1) if mu == a else F(0)) * G4[b][nu] - (F(1) if mu == b else F(0)) * G4[a][nu]
    LOR.append(L)
    LOR_LABEL.append(f"L_{a}{b}")

check("B1  so(3,1) has 6 generators", len(LOR) == 6)
ok = all(is_zero(madd(matmul(transpose(L), G4), matmul(G4, L))) for L in LOR)
check("B2  every generator is g-antisymmetric (lies in so(3,1))", ok)


def rho(L):
    """Action of L in so(3,1) on a covariant symmetric 2-tensor: H -> -(L^T H + H L)."""
    out = zeros(10, 10)
    for j, E in enumerate(EBAS):
        img = madd(matmul(transpose(L), E), matmul(E, L))
        img = [[-x for x in row] for row in img]
        # expand img in the E basis: diagonal entries direct, off-diagonal entries once
        for i, (a, b) in enumerate(PAIRS):
            out[i][j] = img[a][b]
    return out


RHO = [rho(L) for L in LOR]

homok = True
for i in range(6):
    for j in range(6):
        if not is_zero(madd(rho(bracket(LOR[i], LOR[j])), bracket(RHO[i], RHO[j]), F(-1))):
            homok = False
check("B3  rho is a Lie algebra homomorphism on all 36 pairs", homok)

antisym_F = all(is_zero(madd(matmul(transpose(R), GRAM_F), matmul(GRAM_F, R))) for R in RHO)
antisym_TR = all(is_zero(madd(matmul(transpose(R), GRAM_TR), matmul(GRAM_TR, R))) for R in RHO)
check("B4  rho(so(3,1)) preserves the Frobenius fibre form", antisym_F)
check("B5  rho(so(3,1)) preserves the trace-reversed fibre form", antisym_TR)
check("B6  the endogenous Lorentz image is exactly 6-dimensional", rank([flat(R) for R in RHO]) == 6)

# the trace direction is the metric itself, v = g
VTRACE = [F(0)] * 10
for i, (a, b) in enumerate(PAIRS):
    if a == b:
        VTRACE[i] = G4[a][b]
kills = all(all(row[0] == 0 for row in matmul(R, [[c] for c in VTRACE])) for R in RHO)
check("B7  the trace direction (h = g) is annihilated by every Lorentz generator", kills)
# CONTROL: a generic fibre direction is NOT annihilated -- B7 is not vacuous.
GENERIC = [F(1), F(2), F(3), F(5), F(7), F(11), F(13), F(17), F(19), F(23)]
moved = any(any(row[0] != 0 for row in matmul(R, [[c] for c in GENERIC])) for R in RHO)
check("B7b CONTROL FIRES: a generic fibre direction IS moved by the Lorentz action", moved)

TRACELESS = nullspace([TVEC], 10)
check("B8  the traceless fibre subspace is 9-dimensional", len(TRACELESS) == 9)


def invariant_subspace_of(gens, basis, dim_total):
    """Largest gens-invariant subspace contained in span(basis)."""
    W = [list(b) for b in basis]
    while True:
        if not W:
            return []
        Wr, Wp = rref(W)
        ann = nullspace(Wr, dim_total)  # functionals vanishing on W
        rowsys = []
        for phi in ann:
            for Gm in gens:
                row = []
                for w in W:
                    img = matmul(Gm, [[x] for x in w])
                    row.append(sum(phi[t] * img[t][0] for t in range(dim_total)))
                rowsys.append(row)
        sol = nullspace(rowsys, len(W)) if rowsys else [
            [F(1) if i == j else F(0) for j in range(len(W))] for i in range(len(W))
        ]
        newW = []
        for c in sol:
            newW.append([sum(c[j] * W[j][t] for j in range(len(W))) for t in range(dim_total)])
        newW = rref(newW)[0]
        if len(newW) == len(W):
            return newW
        W = newW


def generated_submodule(gens, seeds, dim_total):
    """Smallest gens-invariant subspace containing seeds."""
    W = rref([list(s) for s in seeds])[0]
    while True:
        Wr, Wp = rref(W)
        new = list(W)
        for Gm in gens:
            for w in W:
                img = [matmul(Gm, [[x] for x in w])[t][0] for t in range(dim_total)]
                if not in_span(img, Wr, Wp):
                    new.append(img)
        newr = rref(new)[0]
        if len(newr) == len(W):
            return newr
        W = newr
        if len(W) == dim_total:
            return W


commutant_rows = []
for R in RHO:
    for i in range(9):
        for j in range(9):
            pass
# commutant of rho restricted to the traceless 9 (irreducibility test)
TB, TP = rref(TRACELESS)


def restrict(M, basis, basis_rref, basis_piv):
    """Matrix of M restricted to span(basis), in the given basis (assumes invariance)."""
    n = len(basis)
    out = zeros(n, n)
    for j, b in enumerate(basis):
        img = [matmul(M, [[x] for x in b])[t][0] for t in range(len(b))]
        # solve img = sum_i c_i basis[i]
        sysrows = transpose([list(bb) for bb in basis])
        aug = [sysrows[r] + [img[r]] for r in range(len(img))]
        R_, P_ = rref(aug)
        c = [F(0)] * n
        for r_, pc in enumerate(P_):
            if pc == n:
                raise ValueError("not invariant")
            c[pc] = R_[r_][n]
        for i in range(n):
            out[i][j] = c[i]
    return out


RHO9 = [restrict(R, TRACELESS, TB, TP) for R in RHO]
# commutant: {M : M A - A M = 0 for all A in RHO9}
rowsys = []
for A in RHO9:
    for i in range(9):
        for j in range(9):
            row = [F(0)] * 81
            for k in range(9):
                row[i * 9 + k] += A[k][j]
                row[k * 9 + j] -= A[i][k]
            rowsys.append(row)
comm9 = nullspace(rowsys, 81)
check(
    "B9  traceless 9 is REAL-IRREDUCIBLE under so(3,1) (commutant = R, dim 1)",
    len(comm9) == 1,
    f"dim commutant = {len(comm9)}",
)

# CONTROL: the full 10 must NOT be irreducible (it splits 9 + trace)
rowsys10 = []
for A in RHO:
    for i in range(10):
        for j in range(10):
            row = [F(0)] * 100
            for k in range(10):
                row[i * 10 + k] += A[k][j]
                row[k * 10 + j] -= A[i][k]
            rowsys10.append(row)
comm10 = nullspace(rowsys10, 100)
check(
    "B10 CONTROL FIRES: the full fibre 10 is reducible (commutant dim 2, not 1)",
    len(comm10) == 2,
    f"dim commutant = {len(comm10)}",
)

# THE KK REFUTATION: the trivial isotypic component of the fibre is 1-dimensional,
# not 10.  A Kaluza-Klein internal index would give 10.
triv = nullspace([flat_row for R in RHO for flat_row in R], 10)
check(
    "B11 the fibre's Lorentz-TRIVIAL component is exactly 1-dimensional (the trace)",
    len(triv) == 1,
    f"dim = {len(triv)}",
)
INERT = [zeros(10, 10) for _ in range(6)]
triv_inert = nullspace([flat_row for R in INERT for flat_row in R], 10)
check(
    "B12 CONTROL FIRES: a genuine KK (Lorentz-inert) internal 10 would give a "
    "10-dimensional trivial component",
    len(triv_inert) == 10,
    f"dim = {len(triv_inert)}",
)

# --------------------------------------------------------------------------
# BLOCK C -- so(6,4), its Cartan decomposition, and the endogenous Lorentz inside it
# --------------------------------------------------------------------------
# rational basis diagonalising the trace-reversed form, positives first
NEWB_COEF = [
    [F(1), F(1), F(0), F(0)],    # +2
    [F(0), F(0), F(1), F(-1)],   # +2
    [F(1), F(-1), F(1), F(1)],   # +4
]


def coefvec(diag4, offidx=None):
    v = [F(0)] * 10
    for i in range(4):
        v[i] = diag4[i]
    if offidx is not None:
        v[offidx] = F(1)
    return v


NEWBASIS = []
NEWLABEL = []
for c in NEWB_COEF:
    NEWBASIS.append(coefvec(c))
for name, i in [("E12", 7), ("E13", 8), ("E23", 9)]:
    v = [F(0)] * 10
    v[i] = F(1)
    NEWBASIS.append(v)
NEWLABEL = ["w1", "w2", "w3", "E12", "E13", "E23"]
NEWBASIS.append(list(VTRACE))
NEWLABEL.append("v=g (trace)")
for name, i in [("E01", 4), ("E02", 5), ("E03", 6)]:
    v = [F(0)] * 10
    v[i] = F(1)
    NEWBASIS.append(v)
    NEWLABEL.append(name)

T = transpose(NEWBASIS)  # columns = new basis vectors in E-coordinates
check("C1  the proposed diagonalising basis is a basis (rank 10)", rank(NEWBASIS) == 10)

GP = matmul(transpose(T), matmul(GRAM_TR, T))
diagonal = all(GP[i][j] == 0 for i in range(10) for j in range(10) if i != j)
check("C2  it diagonalises the trace-reversed form", diagonal)
signs = [1 if GP[i][i] > 0 else -1 for i in range(10)]
check(
    "C3  sign pattern is six positives then four negatives",
    signs == [1] * 6 + [-1] * 4,
    f"{signs}",
)

# so(G') basis: A = G'^{-1} K with K antisymmetric.  Coordinates = K_{ab}, a<b.
GPINV = [[F(0)] * 10 for _ in range(10)]
for i in range(10):
    GPINV[i][i] = 1 / GP[i][i]
ADPAIRS = list(combinations(range(10), 2))


def so_gen(a, b):
    K = zeros(10, 10)
    K[a][b] = F(1)
    K[b][a] = F(-1)
    return matmul(GPINV, K)


ADBAS = [so_gen(a, b) for a, b in ADPAIRS]
check("C4  dim so(6,4) = 45", len(ADBAS) == 45)
ok = all(is_zero(madd(matmul(transpose(A), GP), matmul(GP, A))) for A in ADBAS)
check("C5  every basis element lies in so(6,4)", ok)


def ad_coords(A):
    K = matmul(GP, A)
    return [K[a][b] for a, b in ADPAIRS]


def ad_from_coords(c):
    M = zeros(10, 10)
    for idx, (a, b) in enumerate(ADPAIRS):
        if c[idx]:
            M = madd(M, ADBAS[idx], c[idx])
    return M


# Cartan involution theta(A) = S A S, S = diag(+1^6, -1^4)
S = zeros(10, 10)
for i in range(10):
    S[i][i] = F(signs[i])
theta_auto = True
for i in range(0, 45, 7):
    for j in range(0, 45, 5):
        A, B = ADBAS[i], ADBAS[j]
        lhs = matmul(S, matmul(bracket(A, B), S))
        rhs = bracket(matmul(S, matmul(A, S)), matmul(S, matmul(B, S)))
        if not is_zero(madd(lhs, rhs, F(-1))):
            theta_auto = False
check("C6  theta(A) = S A S is a Lie algebra automorphism (sampled)", theta_auto)
check(
    "C7  theta is involutive",
    all(is_zero(madd(matmul(S, matmul(matmul(S, matmul(A, S)), S)), A, F(-1))) for A in ADBAS[:10]),
)

KIDX = [i for i, (a, b) in enumerate(ADPAIRS) if signs[a] == signs[b]]
PIDX = [i for i, (a, b) in enumerate(ADPAIRS) if signs[a] != signs[b]]
KBAS = [ADBAS[i] for i in KIDX]
PBAS = [ADBAS[i] for i in PIDX]
check("C8  dim k = 21   (cross-check PV-2)", len(KBAS) == 21, f"{len(KBAS)}")
check("C9  dim p = 24   (cross-check PV-2)", len(PBAS) == 24, f"{len(PBAS)}")
check("C10 k is the theta = +1 eigenspace", all(is_zero(madd(matmul(S, matmul(A, S)), A, F(-1))) for A in KBAS))
check("C11 p is the theta = -1 eigenspace", all(is_zero(madd(matmul(S, matmul(A, S)), A, F(1))) for A in PBAS))
check("C12 k is a subalgebra", all(rank([ad_coords(bracket(X, Y))] + [ad_coords(Z) for Z in KBAS]) == 21 for X in KBAS[:6] for Y in KBAS[:6]))


def killing_gram(basis):
    n = len(basis)
    Gm = zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            t = sum(matmul(basis[i], basis[j])[a][a] for a in range(10))
            Gm[i][j] = Gm[j][i] = F(8) * t  # B(A,B) = (n-2) tr(AB), n = 10
    return Gm


sk = signature(killing_gram(KBAS))
sp = signature(killing_gram(PBAS))
check("C13 Killing form is NEGATIVE definite on k (cross-check PV-2)", sk == (0, 21, 0), f"{sk}")
check("C14 Killing form is POSITIVE definite on p (cross-check PV-2)", sp == (0 + 24, 0, 0), f"{sp}")

# the endogenous Lorentz algebra, in the diagonalising basis
TINV_rows = []
Taug = [list(T[r]) + [F(1) if c == r else F(0) for c in range(10)] for r in range(10)]
Rr, Pp = rref(Taug)
TINV = [[Rr[r][10 + c] for c in range(10)] for r in range(10)]
check("C15 basis change is invertible", is_zero(madd(matmul(TINV, T), [[F(1) if i == j else F(0) for j in range(10)] for i in range(10)], F(-1))))

HGEN = [matmul(TINV, matmul(R, T)) for R in RHO]
check("C16 endogenous Lorentz lies inside so(6,4)", all(is_zero(madd(matmul(transpose(H), GP), matmul(GP, H))) for H in HGEN))
HCO = [ad_coords(H) for H in HGEN]
check("C17 its image in so(6,4) is 6-dimensional", rank(HCO) == 6)

hk = [h for h in HGEN if is_zero(madd(matmul(S, matmul(h, S)), h, F(-1)))]
hp_dim = rank([ad_coords(madd(h, matmul(S, matmul(h, S)), F(-1))) for h in HGEN])
hk_dim = rank([ad_coords(madd(h, matmul(S, matmul(h, S)), F(1))) for h in HGEN])
check(
    "C18 endogenous Lorentz meets BOTH summands: 3 rotations in k, 3 boosts in p",
    (hk_dim, hp_dim) == (3, 3),
    f"(k-part, p-part) = ({hk_dim}, {hp_dim})",
)
check("C19 therefore so(3,1)_endo is NOT contained in k", hp_dim > 0)

# CONTROL: a genuinely compact subalgebra (the 3 rotations alone) DOES sit in k
ROT = [HGEN[i] for i, lab in enumerate(LOR_LABEL) if lab in ("L_12", "L_13", "L_23")]
rot_p = rank([ad_coords(madd(h, matmul(S, matmul(h, S)), F(-1))) for h in ROT])
check(
    "C20 CONTROL FIRES: the rotation subalgebra alone has zero p-part (test is not vacuous)",
    rot_p == 0,
    f"p-part = {rot_p}",
)

# --------------------------------------------------------------------------
# BLOCK D -- the decisive test: is the k / p split Lorentz-covariant?
# --------------------------------------------------------------------------
ADJ = []
for H in HGEN:
    M = zeros(45, 45)
    for j, A in enumerate(ADBAS):
        col = ad_coords(bracket(H, A))
        for i in range(45):
            M[i][j] = col[i]
    ADJ.append(M)

KCO = [ad_coords(A) for A in KBAS]
PCO = [ad_coords(A) for A in PBAS]
KR, KP = rref(KCO)
witness = None
for H_i, M in enumerate(ADJ):
    for j, kc in enumerate(KCO):
        img = [matmul(M, [[x] for x in kc])[t][0] for t in range(45)]
        if not in_span(img, KR, KP):
            witness = (LOR_LABEL[H_i], ADPAIRS[KIDX[j]])
            break
    if witness:
        break
check(
    "D1  k is NOT invariant under the endogenous Lorentz algebra (explicit witness)",
    witness is not None,
    f"witness: [{witness[0]}, K_{witness[1]}] leaves k" if witness else "NONE FOUND",
)

PR, PP_ = rref(PCO)
wit_p = None
for H_i, M in enumerate(ADJ):
    for j, pc in enumerate(PCO):
        img = [matmul(M, [[x] for x in pc])[t][0] for t in range(45)]
        if not in_span(img, PR, PP_):
            wit_p = (LOR_LABEL[H_i], ADPAIRS[PIDX[j]])
            break
    if wit_p:
        break
check("D2  p is NOT invariant under the endogenous Lorentz algebra either", wit_p is not None)

largest_in_k = invariant_subspace_of(ADJ, KCO, 45)
check(
    "D3  the LARGEST Lorentz-invariant subspace inside k is ZERO",
    len(largest_in_k) == 0,
    f"dim = {len(largest_in_k)}",
)
largest_in_p = invariant_subspace_of(ADJ, PCO, 45)
check("D4  the largest Lorentz-invariant subspace inside p is zero", len(largest_in_p) == 0, f"dim = {len(largest_in_p)}")

# CONTROL: the test must be able to FIND an invariant subspace when one exists.
hull_h = invariant_subspace_of(ADJ, HCO, 45)
check(
    "D5  CONTROL FIRES: so(3,1)_endo itself IS Lorentz-invariant, dim 6 (the test is "
    "not trivially returning zero)",
    len(hull_h) == 6,
    f"dim = {len(hull_h)}",
)

gen_by_k = generated_submodule(ADJ, KCO, 45)
check(
    "D6  the smallest Lorentz-invariant subspace CONTAINING k is all of so(6,4)",
    len(gen_by_k) == 45,
    f"dim = {len(gen_by_k)}",
)

# the vierbein-like (1,1) module: v ^ (traceless), 9-dimensional
def wedge(u, w):
    """so(GP) element z -> <u,z> w - <w,z> u, with <,> = GP."""
    M = zeros(10, 10)
    for z in range(10):
        uz = sum(u[i] * GP[i][z] for i in range(10))
        wz = sum(w[i] * GP[i][z] for i in range(10))
        for i in range(10):
            M[i][z] = uz * w[i] - wz * u[i]
    return M


VNEW = [matmul(TINV, [[x] for x in VTRACE])[t][0] for t in range(10)]
TL_NEW = [[matmul(TINV, [[x] for x in w])[t][0] for t in range(10)] for w in TRACELESS]
W11 = [ad_coords(wedge(VNEW, w)) for w in TL_NEW]
check("D7  the trace-direction wedge module (1,1) is 9-dimensional", rank(W11) == 9, f"{rank(W11)}")
W11r, W11p = rref(W11)
inv11 = True
for M in ADJ:
    for w in W11:
        img = [matmul(M, [[x] for x in w])[t][0] for t in range(45)]
        if not in_span(img, W11r, W11p):
            inv11 = False
check("D8  it IS Lorentz-invariant (a genuine 9-dimensional 4D field multiplet)", inv11)
in_k = rank([w for w in W11 if all(w[i] == 0 for i in PIDX)])
d_in_k = len(nullspace([[w[i] for w in W11] for i in PIDX], 9))
check(
    "D9  but only 3 of its 9 directions lie in k -- so it is NOT the nine",
    d_in_k == 3,
    f"dim(W11 ∩ k) = {d_in_k}",
)

# the invariant-subspace dimension spectrum: which dims are even possible?
dims = set()
for i in range(45):
    seed = [F(1) if t == i else F(0) for t in range(45)]
    dims.add(len(generated_submodule(ADJ, [seed], 45)))
check(
    "D10 no cyclic Lorentz-submodule of so(6,4) has dimension 21, 24, 12 or 9-inside-k",
    21 not in dims and 24 not in dims and 12 not in dims,
    f"cyclic submodule dimensions found: {sorted(dims)}",
)

# --------------------------------------------------------------------------
# BLOCK G -- the Lorentz-module decomposition of so(6,4)
# --------------------------------------------------------------------------
M6 = hull_h
M9 = W11r
M30 = None
for i in range(45):
    seed = [F(1) if t == i else F(0) for t in range(45)]
    sub = generated_submodule(ADJ, [seed], 45)
    if len(sub) == 30:
        M30 = sub
        break
check("G1  so(6,4) contains Lorentz submodules of dimension 6, 9 and 30", M30 is not None and (len(M6), len(M9), len(M30)) == (6, 9, 30), f"{(len(M6), len(M9), len(M30) if M30 else None)}")
check("G2  they are independent and exhaust the 45: 6 + 9 + 30 = 45", rank(M6 + M9 + M30) == 45, f"rank = {rank(M6 + M9 + M30)}")


def commutant_dim(gens_restricted, n):
    rows = []
    for A in gens_restricted:
        for i in range(n):
            for j in range(n):
                row = [F(0)] * (n * n)
                for k in range(n):
                    row[i * n + k] += A[k][j]
                    row[k * n + j] -= A[i][k]
                rows.append(row)
    return nullspace(rows, n * n)


M6r, M6p = rref(M6)
M9r, M9p = rref(M9)
ADJ6 = [restrict(M, M6, M6r, M6p) for M in ADJ]
ADJ9 = [restrict(M, M9, M9r, M9p) for M in ADJ]
c9 = commutant_dim(ADJ9, 9)
c6 = commutant_dim(ADJ6, 6)
check("G3  the 9 (symmetric-traceless / vierbein-type) is REAL-irreducible, commutant dim 1", len(c9) == 1, f"dim = {len(c9)}")
check("G4  the 6 (= so(3,1) itself) has commutant dim 2 -- complex type, still R-irreducible", len(c6) == 2, f"dim = {len(c6)}")
Iden6 = [[F(1) if i == j else F(0) for j in range(6)] for i in range(6)]
IDFLAT = flat(Iden6)
NMAT = None
for cvec in c6:
    Mc = [[cvec[i * 6 + j] for j in range(6)] for i in range(6)]
    if rank([flat(Mc), IDFLAT]) == 2:
        NMAT = Mc
        break
disc = None
if NMAT is not None:
    Nsq = matmul(NMAT, NMAT)
    # solve N^2 = alpha I + beta N exactly
    sysrows = [[IDFLAT[t], flat(NMAT)[t], flat(Nsq)[t]] for t in range(36)]
    Rc, Pc = rref(sysrows)
    sol = {}
    consistent = 2 not in Pc
    if consistent:
        for r_, pc in enumerate(Pc):
            sol[pc] = Rc[r_][2]
        alpha, beta = sol.get(0, F(0)), sol.get(1, F(0))
        disc = beta * beta + 4 * alpha
check(
    "G5  the 6's commutant is the DIVISION algebra C (its non-scalar element has "
    "negative discriminant, so no idempotent splits it): the 6 is R-irreducible",
    disc is not None and disc < 0,
    f"discriminant = {disc}",
)
check(
    "G6  21, 24 and 12 are NOT sums of the exhibited submodule dimensions {6,9,30}; "
    "9 is, but the unique 9 meets k in only 3 directions (D9)",
    all(
        d
        not in {
            sum(s)
            for r_ in range(4)
            for s in combinations([6, 9, 30], r_)
        }
        for d in (21, 24, 12)
    ),
)

# --------------------------------------------------------------------------
# BLOCK E -- the FORM leg: projection versus contraction
# --------------------------------------------------------------------------
# Symbolic section s(x) = (x, g_{ab}(x)).  ds has a 4x4 identity horizontal block
# and a 10x4 vertical block d(g_ab)/dx^mu.  Work with symbolic entries as
# independent rationals-in-a-polynomial-ring surrogate: use formal symbols.
import sympy as sp  # noqa: E402

xs = sp.symbols("x0 x1 x2 x3")
gf = [[sp.Function(f"g{min(a,b)}{max(a,b)}")(*xs) for b in range(4)] for a in range(4)]
ds = sp.zeros(14, 4)
for mu in range(4):
    ds[mu, mu] = 1
for i, (a, b) in enumerate(PAIRS):
    for mu in range(4):
        ds[4 + i, mu] = sp.diff(gf[a][b], xs[mu])
check("E1  ds has rank 4 for a general observation section", ds.rank() == 4, f"rank = {ds.rank()}")

pullback = ds.T  # s^* : T*Y (14) -> T*X (4)
omega = sp.Matrix(14, 1, lambda i, j: sp.Symbol(f"w{i}"))
sw = pullback * omega
expected = sp.Matrix(
    4,
    1,
    lambda mu, j: sp.Symbol(f"w{mu}")
    + sum(sp.Symbol(f"w{4+i}") * sp.diff(gf[a][b], xs[mu]) for i, (a, b) in enumerate(PAIRS)),
)
check(
    "E2  (s^*omega)_mu = omega_mu + omega_(ab) d_mu g_ab -- the vertical legs are "
    "CONTRACTED into the 4D one-form, not split off",
    sp.simplify(sw - expected) == sp.zeros(4, 1),
)
check(
    "E3  s^* annihilates a 10-dimensional space of form legs (contraction is lossy, "
    "not a projection onto scalars)",
    len(pullback.nullspace()) == 10,
    f"dim ker = {len(pullback.nullspace())}",
)

# CONTROL: only for a FLAT section does pullback reduce to the horizontal projection.
flatsub = {sp.diff(gf[a][b], xs[mu]): 0 for a in range(4) for b in range(4) for mu in range(4)}
ds_flat = ds.subs(flatsub)
proj = sp.zeros(4, 14)
for mu in range(4):
    proj[mu, mu] = 1
check(
    "E4  CONTROL FIRES: pullback == horizontal projection ONLY when d_mu g = 0 "
    "(the constant-coefficient gauge)",
    sp.simplify(ds_flat.T - proj) == sp.zeros(4, 14) and sp.simplify(ds.T - proj) != sp.zeros(4, 14),
)

# --------------------------------------------------------------------------
# BLOCK F -- assembly, both readings
# --------------------------------------------------------------------------
# the ad leg of the nine lies in the INTERNAL Lambda^2(10) block of Lambda^2(14):
NW2 = len(list(combinations(range(14), 2)))
check("F1  dim Lambda^2(carrier 14) = 91, counted", NW2 == 91, f"{NW2}")
n_int = len([1 for a, b in combinations(range(14), 2) if a < 10 and b < 10])
n_mix = len([1 for a, b in combinations(range(14), 2) if a < 10 <= b])
n_hor = len([1 for a, b in combinations(range(14), 2) if a >= 10 and b >= 10])
check(
    "F2  it splits, by index type, as 45 internal + 40 mixed + 6 horizontal",
    (n_int, n_mix, n_hor, n_int + n_mix + n_hor) == (45, 40, 6, NW2),
    f"{(n_int, n_mix, n_hor)}",
)
# the internal block IS Lorentz-invariant inside Lambda^2(14): built explicitly.
CAR = []
for idx, L in enumerate(LOR):
    M = zeros(14, 14)
    R = RHO[idx]
    for i in range(10):
        for j in range(10):
            M[i][j] = R[i][j]
    LT = transpose(L)
    for i in range(4):
        for j in range(4):
            M[10 + i][10 + j] = -LT[i][j]
    CAR.append(M)
W2 = list(combinations(range(14), 2))
W2IDX = {p: i for i, p in enumerate(W2)}
LAM2 = []
for M in CAR:
    A = zeros(91, 91)
    for col, (a, b) in enumerate(W2):
        for t in range(14):
            if M[t][a]:
                if t == b:
                    continue
                p = (t, b) if t < b else (b, t)
                A[W2IDX[p]][col] += M[t][a] * (F(1) if t < b else F(-1))
            if M[t][b]:
                if t == a:
                    continue
                p = (a, t) if a < t else (t, a)
                A[W2IDX[p]][col] += M[t][b] * (F(1) if a < t else F(-1))
        A[col][col] += M[a][a] + M[b][b]
    LAM2.append(A)
INTBLOCK = [i for i, (a, b) in enumerate(W2) if a < 10 and b < 10]
intvecs = [[F(1) if t == i else F(0) for t in range(91)] for i in INTBLOCK]
IR, IP = rref(intvecs)
f3ok = all(
    in_span([matmul(A, [[x] for x in v])[t][0] for t in range(91)], IR, IP)
    for A in LAM2
    for v in intvecs
)
check(
    "F3  dim Lambda^2(10) block inside Lambda^2(14) is 45 and it IS invariant under the "
    "endogenous Lorentz (so the nine's AD leg is correctly located)",
    len(INTBLOCK) == 45 and f3ok,
    f"dim = {len(INTBLOCK)}",
)
mixed = [i for i, (a, b) in enumerate(W2) if a < 10 <= b][0]
badvecs = intvecs + [[F(1) if t == mixed else F(0) for t in range(91)]]
BR, BP = rref(badvecs)
f3ctrl = not all(
    in_span([matmul(A, [[x] for x in v])[t][0] for t in range(91)], BR, BP)
    for A in LAM2
    for v in badvecs
)
check(
    "F3b CONTROL FIRES: adding one MIXED direction to the internal block destroys "
    "invariance (F3 is not vacuous)",
    f3ctrl,
)
# under CONTRACTION each ad direction yields exactly one 4D one-form:
check(
    "F4  CONTRACTION reading: s^* is SURJECTIVE onto T*X (rank 4), so each ad "
    "direction's 4D form content is one FULL unconstrained one-form",
    pullback.rank() == 4,
    f"rank = {pullback.rank()}",
)
horiz_incl = sp.zeros(14, 4)
for mu in range(4):
    horiz_incl[mu, mu] = 1
check(
    "F4b the horizontal leg alone already saturates it: s^* o (horizontal inclusion) "
    "= id on T*X, so the vertical legs ADD to that one-form rather than making new fields",
    sp.simplify(pullback * horiz_incl - sp.eye(4)) == sp.zeros(4, 4),
)
# under PROJECTION each ad direction yields vector + symmetric-traceless + scalar:
rows4 = []
LOR4 = [[[-transpose(L)[i][j] for j in range(4)] for i in range(4)] for L in LOR]
for A in LOR4:
    for i in range(4):
        for j in range(4):
            row = [F(0)] * 16
            for k in range(4):
                row[i * 4 + k] += A[k][j]
                row[k * 4 + j] -= A[i][k]
            rows4.append(row)
c4 = nullspace(rows4, 16)
check(
    "F5  PROJECTION reading: the form leg gives H*(4, R-irreducible) + V*(9 "
    "symmetric-traceless + 1 trace) -- a VECTOR plus a spin-2-type TENSOR plus ONE "
    "scalar per ad direction, never ten scalars",
    len(c4) == 1 and len(triv) == 1 and len(TRACELESS) == 9,
    f"commutant(H*) = {len(c4)}, trivial component of V* = {len(triv)}",
)

# --------------------------------------------------------------------------
# certificate
# --------------------------------------------------------------------------
print("=" * 78)
print("MD-1  four-dimensional mode decomposition: form leg and ad leg")
print("=" * 78)
npass = 0
for name, ok, detail in CHECKS:
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}" + (f"   ({detail})" if detail else ""))
    npass += 1 if ok else 0
print("-" * 78)
print(f"CERTIFICATE: {npass}/{len(CHECKS)}")
print("-" * 78)
print("RESULT")
print("  FORM LEG   : under the source-declared CONTRACTION (pullback along the")
print("               observation section) every ad direction descends to exactly ONE")
print("               4D one-form.  The nine ARE spin-1 on the form leg.")
print("  FORM LEG   : under the disavowed KK PROJECTION the vertical legs are NOT")
print("               ten 4D scalars -- they are 9 (symmetric traceless) + 1 (trace),")
print("               so the projection reading gives MORE fields, not fewer.")
print("  AD LEG     : the endogenous Lorentz algebra acts on so(6,4), and NO nonzero")
print("               subspace of k is Lorentz-invariant.  Under a SOLDERED ad bundle")
print("               the 12 + 9 split of k is not a Lorentz-covariant labelling at all.")
print("  FORK       : SOLDERED-AD vs INERT-AD is NOT decided by the declared content.")
if npass != len(CHECKS):
    sys.exit(1)
