#!/usr/bin/env python3
"""
One Residual paper -- Section 2.1 (Standard Model gauge group, existence grade).

CLAIM under test
----------------
The Pati-Salam gauge algebra is  g = su(4) (+) su(2)_L (+) su(2)_R  (dim 21, rank 5).
There exists a RANK-ONE breaking vector v_PSB in the Pati-Salam rep (4, 1, 2)
whose stabilizer subalgebra

    stab(v) = { Z in g : rho(Z) v = 0 }

is EXACTLY the Standard Model algebra  su(3) (+) su(2) (+) u(1) :
    - dimension 12,
    - rank 4,
    - exactly ONE u(1) (one-dimensional center),
    - semisimple part of dimension 11  (su(3) dim 8  +  su(2) dim 3).

Control: a GENERIC vector has stabilizer of dimension 3 (only su(2)_L, which
acts trivially on the (4,1,2) rep, survives) -- so the SM-sized stabilizer is a
genuine, non-generic feature of the rank-one direction.  To make the control
faithful, the rep space is two identical copies of (4,1,2): a single copy is
not enough to break all of SU(4) x SU(2)_R generically (it leaves 7), whereas a
generic vector across two copies breaks everything breakable and leaves exactly
the 3-dim trivially-acting su(2)_L.  The rank-one -> SM(12) result is unchanged
by the multiplicity (the second copy is zero in v_PSB), see rho() below.

This is EXISTENCE grade: we exhibit the algebra, the representation, and one
explicit vector, and compute the stabilizer as a null space by real linear
algebra. No claim is inflated to a derivation; representation theory of
Pati-Salam / SO(10) is used for consistency, per the paper's own grading.

Method (real computation, numpy):
    g elements are block-diagonal 8x8 anti-Hermitian matrices diag(X, YL, YR)
    with X in su(4), YL in su(2)_L, YR in su(2)_R (all traceless).
    Rep space is C^4 (x) C^2 with rho(X,YL,YR) = X (x) I2 + I4 (x) YR
    (su(2)_L acts trivially -> the (4,1,2) rep).
    stab(v) is the kernel of  Z |-> rho(Z) v , solved over R as a null space.
    Rank / center / derived-algebra dimensions are computed via the Lie bracket
    (block-wise commutator) decomposed back onto the algebra basis.

Exit 0 iff every check passes.
"""

import numpy as np

np.random.seed(0)
TOL = 1e-9


# --------------------------------------------------------------------------
# Bases for su(n) : traceless anti-Hermitian n x n matrices  (dim n^2 - 1)
# --------------------------------------------------------------------------
def su_basis(n):
    B = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), dtype=complex)
            m[i, j] = 1.0
            m[j, i] = -1.0            # real antisymmetric -> anti-Hermitian
            B.append(m)
            m = np.zeros((n, n), dtype=complex)
            m[i, j] = 1j
            m[j, i] = 1j              # i*(E_ij + E_ji) -> anti-Hermitian
            B.append(m)
    for k in range(1, n):             # traceless diagonal anti-Hermitian
        d = np.zeros(n, dtype=complex)
        for a in range(k):
            d[a] = 1j
        d[k] = -1j * k
        B.append(np.diag(d))
    assert len(B) == n * n - 1
    return B


def embed(X4, Y2L, Y2R):
    """Block-diagonal 8x8 embedding of (X, YL, YR)."""
    M = np.zeros((8, 8), dtype=complex)
    M[0:4, 0:4] = X4
    M[4:6, 4:6] = Y2L
    M[6:8, 6:8] = Y2R
    return M


# Algebra basis: 15 + 3 + 3 = 21 generators as 8x8 blocks
basis = []
for X in su_basis(4):
    basis.append(embed(X, np.zeros((2, 2), complex), np.zeros((2, 2), complex)))
for Y in su_basis(2):
    basis.append(embed(np.zeros((4, 4), complex), Y, np.zeros((2, 2), complex)))
for Y in su_basis(2):
    basis.append(embed(np.zeros((4, 4), complex), np.zeros((2, 2), complex), Y))
DIM_G = len(basis)                     # 21

# indices, for a sanity check that su(2)_L lands in every stabilizer
IDX_SU2L = list(range(15, 18))

# Gram matrix for decomposing bracket results back onto the basis
def ip(A, B):
    return np.real(np.trace(A.conj().T @ B))

G = np.array([[ip(a, b) for b in basis] for a in basis])
G_inv = np.linalg.inv(G)


def coords(M):
    """Coordinates of an 8x8 algebra element M in `basis` (exact if M in span)."""
    b = np.array([ip(a, M) for a in basis])
    return G_inv @ b


def mat(c):
    """Assemble an algebra element from coordinate vector c."""
    M = np.zeros((8, 8), dtype=complex)
    for ck, bk in zip(c, basis):
        M = M + ck * bk
    return M


def bracket_coords(c1, c2):
    """Lie bracket of two algebra elements, returned in coordinates."""
    A, B = mat(c1), mat(c2)
    return coords(A @ B - B @ A)


# --------------------------------------------------------------------------
# Representation rho on C^4 (x) C^2  (the Pati-Salam (4,1,2))
# --------------------------------------------------------------------------
I4 = np.eye(4, dtype=complex)
I2 = np.eye(2, dtype=complex)


I2c = np.eye(2, dtype=complex)         # multiplicity space (two copies)


def rho1(M):
    """Action of an 8x8 algebra element on ONE copy of (4,1,2) = C^4 (x) C^2."""
    X = M[0:4, 0:4]
    YR = M[6:8, 6:8]                    # su(2)_R acts; su(2)_L (block YL) does not
    return np.kron(X, I2) + np.kron(I4, YR)


def rho(M):
    """
    Action on the rep space  C^2 (x) (C^4 (x) C^2)  = two identical copies of
    the Pati-Salam (4,1,2), stacked as  I_mult (x) rho1(M).

    Why two copies: a single (4,1,2) is not a faithful enough control -- a
    generic full-rank vev there still leaves a 7-dim stabilizer (su(2)_L plus a
    residual su(2)_R-diagonal freedom that a single 4x2 direction cannot fix).
    With two copies a GENERIC vector breaks all of SU(4) x SU(2)_R and leaves
    ONLY su(2)_L (which acts trivially on (4,1,2) by construction) -> dim 3.
    This makes the control honest: dim 3 is exactly the part of the algebra that
    *cannot* be broken by any vector in this rep, so any stabilizer above 3 is a
    genuine, non-generic feature of the chosen direction.  The load-bearing
    rank-one -> SM(12) computation is INDEPENDENT of the multiplicity: the extra
    copy is zero in v_PSB and contributes no constraint.
    """
    return np.kron(I2c, rho1(M))


def stabilizer_basis(v):
    """
    Real basis (as coordinate vectors, length 21) of { Z in g : rho(Z) v = 0 }.
    Build the real 32 x 21 matrix  A  with columns  rho(basis_i) v ,
    kernel over R is the stabilizer.
    """
    cols = []
    for b in basis:
        w = rho(b) @ v
        cols.append(np.concatenate([w.real, w.imag]))
    A = np.array(cols).T               # (32, 21) real
    # null space via SVD
    _, s, Vt = np.linalg.svd(A)
    rank = int((s > TOL * max(1.0, s[0])).sum())
    ns = Vt[rank:]                      # rows span the kernel, shape (21-rank, 21)
    return [row for row in ns]


# --------------------------------------------------------------------------
# Structural invariants of a subalgebra given by a list of coordinate vectors
# --------------------------------------------------------------------------
def subspace_dim(vectors):
    if not vectors:
        return 0
    M = np.array(vectors)
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > TOL * max(1.0, s[0])).sum())


def orthonormalize(vectors):
    M = np.array(vectors)
    U, s, Vt = np.linalg.svd(M, full_matrices=False)
    r = int((s > TOL * max(1.0, s[0])).sum())
    return [Vt[i] for i in range(r)]


def derived_dim(stab):
    """dim of [stab, stab]."""
    onb = orthonormalize(stab)
    brs = []
    for i in range(len(onb)):
        for j in range(i + 1, len(onb)):
            brs.append(bracket_coords(onb[i], onb[j]))
    return subspace_dim(brs)


def center_dim(stab):
    """
    dim of the center { z in stab : [z, t] = 0 for all t in stab }.
    Solve the linear system: z = sum a_k onb_k with [z, onb_j] = 0 for all j.
    """
    onb = orthonormalize(stab)
    n = len(onb)
    rows = []
    for j in range(n):
        for i in range(n):
            rows.append(bracket_coords(onb[i], onb[j]))   # depends linearly on a_i
    # Build matrix L (len = n*21 stacked per j? simpler: constraint per j is
    # sum_i a_i [onb_i, onb_j] = 0). Stack all (j, component) rows.
    L = []
    for j in range(n):
        block = np.array([bracket_coords(onb[i], onb[j]) for i in range(n)])  # (n,21)
        # each of the 21 components gives one linear eqn in a (length n)
        for comp in range(block.shape[1]):
            L.append(block[:, comp])
    L = np.array(L)                     # (n*21, n)
    s = np.linalg.svd(L, compute_uv=False)
    rank = int((s > TOL * max(1.0, s[0])).sum()) if L.size else 0
    return n - rank


def rank_of(stab):
    """
    Rank = dim of a Cartan = dim of the centralizer in `stab` of a REGULAR
    (generic) element of stab.
    """
    onb = orthonormalize(stab)
    n = len(onb)
    r = np.random.randn(n)
    z = sum(rk * v for rk, v in zip(r, onb))     # generic element (coords)
    # centralizer: { t = sum a_i onb_i : [z, t] = 0 }
    cols = np.array([bracket_coords(z, onb[i]) for i in range(n)]).T   # (21, n)
    s = np.linalg.svd(cols, compute_uv=False)
    rank = int((s > TOL * max(1.0, s[0])).sum())
    return n - rank


# --------------------------------------------------------------------------
# The rank-one Pati-Salam breaking vector  v_PSB
#   Copy 0 carries the canonical PS vev  e_3 (x) f_0  -- the SU(3)-singlet /
#   right-handed-neutrino direction, the textbook (4,1,2) breaking vev.
#   Copy 1 is zero.  "Rank one" = the activated 4x2 vev matrix has matrix rank 1
#   (a pure outer product e_3 f_0^T), and only one copy is switched on.
# --------------------------------------------------------------------------
e3 = np.array([0, 0, 0, 1], dtype=complex)
f0 = np.array([1, 0], dtype=complex)
psb_copy = np.kron(e3, f0)                        # 8-dim, the (4,1,2) vev
v_PSB = np.concatenate([psb_copy, np.zeros(8, dtype=complex)])   # 16-dim

# a generic control vector in the same 16-dim rep (both copies random)
v_gen = (np.random.randn(16) + 1j * np.random.randn(16))


# --------------------------------------------------------------------------
# Run checks
# --------------------------------------------------------------------------
def approx(a, b):
    return abs(a - b) < 0.5            # dims are integers

checks = []

# 0. rank-one sanity: the activated copy of v_PSB, as a 4x2 vev matrix, has
#    matrix rank 1; the second copy is identically zero.
Mv = v_PSB[0:8].reshape(4, 2)
sv = np.linalg.svd(Mv, compute_uv=False)
rk1 = int((sv > TOL).sum())
second_zero = np.allclose(v_PSB[8:16], 0)
checks.append(("v_PSB is rank one (activated 4x2 vev, other copy zero)",
               rk1 == 1 and second_zero, f"matrix-rank={rk1}, copy1_zero={second_zero}"))

# 1. ambient algebra dimension
checks.append(("ambient g = su(4)+su(2)_L+su(2)_R has dim 21", DIM_G == 21, f"dim={DIM_G}"))

# 2. stabilizer of v_PSB
stab = stabilizer_basis(v_PSB)
d_stab = subspace_dim(stab)
checks.append(("dim stab(v_PSB) == 12 (SM algebra)", d_stab == 12, f"dim={d_stab}"))

# 3. su(2)_L fully inside stab(v_PSB)
def in_span(vec, vectors):
    if not vectors:
        return False
    M = np.array(vectors)
    # residual of least-squares projection
    coef, *_ = np.linalg.lstsq(M.T, vec, rcond=None)
    res = np.linalg.norm(M.T @ coef - vec)
    return res < TOL
su2L_in = all(in_span(np.eye(DIM_G)[k], stab) for k in IDX_SU2L)
checks.append(("su(2)_L (3 gens) sits inside stab(v_PSB)", su2L_in, f"all_in={su2L_in}"))

# 4. exactly one u(1): center dimension 1
c_dim = center_dim(stab)
checks.append(("center of stab == 1 (exactly one u(1))", c_dim == 1, f"center_dim={c_dim}"))

# 5. semisimple part dim 11 (= su(3) 8 + su(2) 3)
d_der = derived_dim(stab)
checks.append(("derived [stab,stab] dim == 11 (su(3)+su(2))", d_der == 11, f"derived_dim={d_der}"))

# 6. rank 4
rk = rank_of(stab)
checks.append(("rank(stab) == 4", rk == 4, f"rank={rk}"))

# 7. GENERIC control: stabilizer dim 3 (only su(2)_L survives)
stab_g = stabilizer_basis(v_gen)
d_gen = subspace_dim(stab_g)
checks.append(("control: dim stab(generic v) == 3", d_gen == 3, f"dim={d_gen}"))

# 8. the SM stabilizer is strictly larger than generic (non-generic direction)
checks.append(("stab(v_PSB) strictly larger than generic", d_stab > d_gen, f"{d_stab} > {d_gen}"))


print("=" * 68)
print("One Residual 2.1 -- Pati-Salam rank-one stabilizer = SM  (existence)")
print("=" * 68)
all_pass = True
for name, ok, detail in checks:
    tag = "PASS" if ok else "FAIL"
    all_pass = all_pass and ok
    print(f"[{tag}] {name:<52} {detail}")
print("-" * 68)
print(f"RESULT: {'PASS -- SM stabilizer established (existence grade)' if all_pass else 'FAIL'}")

import sys
sys.exit(0 if all_pass else 1)
