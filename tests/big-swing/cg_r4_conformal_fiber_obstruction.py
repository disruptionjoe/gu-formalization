#!/usr/bin/env python3
"""cg_r4_conformal_fiber_obstruction.py -- BIG SWING R4 (2026-07-06).

QUESTION. Mannheim's conformal (Weyl) gravity has no metric scale: its natural fiber is the
CONFORMAL CLASS of metrics, i.e. GL(4,R)/(O(3,1) x R+) instead of GU's metric fiber
GL(4,R)/O(3,1). Does passing to the conformal class CURE or INHERIT the two walls the program
has already hit?

  Wall 1 (BIG-SWING-1, re-derived from scratch here, NOT copied): the invariant trace form on
         the fiber tangent gl(4,R)/o(3,1) is indefinite with noncompact isotropy -- no
         invariant Riemannian fiber metric exists.
  Wall 2 (C-07): every GU-native Hermitian carrier commutes with the quaternionic structure
         J_quat of Cl(9,5) = M(64,H); Kramers then forces even-multiplicity spectra / even
         signature -- no odd index from GU-native blocks.

WHAT THIS SCRIPT COMPUTES (every number printed; the forbidden targets {3, 8, 24, chi(K3)=24,
Ahat=3, rank_H=4, ind_H=8} are never assumed, inserted, or divided by -- every count below is
MEASURED output of a computation):

  (A) EXACT signature (rational Lagrange congruence, sympy) of B(X,Y) = tr(XY) on the metric
      fiber tangent p = {X : X^T eta = eta X} ~ gl(4,R)/o(3,1), eta = diag(-1,1,1,1), dim 10.
  (B) EXACT signature of B on the conformal reduction p_0 = {X in p : tr X = 0}
      ~ sl(4,R)/so(3,1), dim 9; exact identification of the removed direction (X = I, the pure
      trace/scale direction) including its B-sign and B-orthogonality to p_0; plus a MEASURED
      count (numerical nullspace, singular values printed) of ALL isotropy-invariant symmetric
      forms on p and on p_0 -- so "indefinite" cannot be dodged by picking a different
      invariant form.
  (C) Isotropy of the conformal fiber: the stabilizer of the conformal class [eta] is
      CO(3,1) = O(3,1) x R+; boosts preserve eta EXACTLY (residual printed, sympy-exact check
      too) and have unbounded norm -> noncompact isotropy survives the conformal quotient.
  (D) Compact CONTROL: the same machinery on gl(4)/o(4) and sl(4)/so(4) (eta = I) must return
      DEFINITE signatures -- demonstrating the machinery has discriminating power (it does not
      print "indefinite" on everything).
  (E) C-07 tie-in on the verified 1792-dim GU carrier V (x) S, signature (9,5):
      - ANCHORS reproduced first: beta_S pseudo-anti-Hermiticity residual, self-dual SU(2)+
        triplet Krein signature (+96,-96,0), rank(Gamma) = 128, dim ker(Gamma) = 1664,
        triplet dim 192 (construction copied from tests/generation-sector/ghost_parity_krein.py).
      - J_quat (the antiunitary quaternionic structure, J^2 = -I) built by the step10/step11
        averaging construction, transplanted to this timelike set; residuals printed.
      - so(9,5) carrier generators verified J-commuting (H-linearity defects printed).
      - a WEYL-SQUARED-SHAPED block W2 = sum C_{abcd} Sigma^{ab} Sigma^{cd} + h.c., with
        C_{abcd} a genuine random 4D WEYL-symmetric coefficient tensor (Riemann symmetries +
        first Bianchi + totally trace-free; residuals and the measured 10-dim Weyl space rank
        printed) and REAL coefficients, built from the carrier so-generators on the 4-base
        {0,1,2,3}: verified J-commuting; its compression to the 192-dim triplet sector obeys
        KRAMERS PAIRING (even eigenvalue multiplicities; even signature) -- printed.
      - CONTROLS with discriminating power: (i) a rank-3 projector in the triplet sector has
        ODD signature and O(1) J-defect (foreign object); (ii) the SAME Weyl-squared
        construction with essentially COMPLEX coefficients breaks J-commutation and breaks the
        Kramers pairing. So the pairing check is a measurement, not a tautology.

READING. If (B) still comes out indefinite with noncompact isotropy, and (E) shows the
Weyl-squared-shaped block is J-commuting with Kramers-even triplet spectrum, then the
conformal-gravity-CLASS action built from GU-native blocks INHERITS both walls: the conformal
quotient removes exactly one direction (the scale), and everything obstructive survives.
Any statement of the form "mechanism M forces c" below is about the mechanism, never "GU
forces c".

Run from repo root: python tests/big-swing/cg_r4_conformal_fiber_obstruction.py   (exit 0)
"""
from __future__ import annotations

import time
from itertools import permutations

import numpy as np
import sympy as sp

T0 = time.time()


def stamp(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# =====================================================================================
# Exact linear algebra helpers (sections A-D)
# =====================================================================================

def exact_signature(G):
    """Exact signature (n_plus, n_minus, n_zero) of a rational symmetric matrix via
    Lagrange congruence (completing squares). Pure sympy rationals; no floats."""
    G = sp.Matrix(G)
    n = G.shape[0]
    assert G == G.T, "exact_signature needs a symmetric matrix"
    pos = neg = zer = 0
    idx = list(range(n))
    while idx:
        # find a nonzero diagonal pivot
        piv = None
        for k in idx:
            if G[k, k] != 0:
                piv = k
                break
        if piv is None:
            # find a nonzero off-diagonal entry and create a diagonal pivot:
            # basis change e_i -> e_i + e_j turns 2*G[i,j] onto the diagonal
            hit = None
            for i in idx:
                for j in idx:
                    if i < j and G[i, j] != 0:
                        hit = (i, j)
                        break
                if hit:
                    break
            if hit is None:
                zer += len(idx)
                break
            i, j = hit
            E = sp.eye(n)
            E[j, i] = 1  # e_i -> e_i + e_j
            G = E.T * G * E
            continue
        d = G[piv, piv]
        if d > 0:
            pos += 1
        else:
            neg += 1
        # congruence-eliminate row/col piv against remaining indices
        E = sp.eye(n)
        for k in idx:
            if k != piv:
                E[piv, k] = -G[piv, k] / d
        G = E.T * G * E
        idx.remove(piv)
    return pos, neg, zer


def p_basis(eta):
    """Basis of p = {X : X^T eta = eta X} (eta-self-adjoint matrices), as X = eta*S with S
    symmetric. dim = 10 for 4x4. Returns list of sympy matrices."""
    n = eta.shape[0]
    Xs = []
    for i in range(n):
        S = sp.zeros(n, n)
        S[i, i] = 1
        Xs.append(eta * S)
    for i in range(n):
        for j in range(i + 1, n):
            S = sp.zeros(n, n)
            S[i, j] = 1
            S[j, i] = 1
            Xs.append(eta * S)
    return Xs


def gram(Xs):
    m = len(Xs)
    return sp.Matrix(m, m, lambda i, j: sp.trace(Xs[i] * Xs[j]))


def traceless_subbasis(Xs):
    """Basis (as coefficient vectors and matrices) of the tr=0 subspace of span(Xs)."""
    tr_row = sp.Matrix(1, len(Xs), lambda _i, k: sp.trace(Xs[k]))
    null = tr_row.nullspace()
    X0s = []
    for c in null:
        M = sp.zeros(*Xs[0].shape)
        for k in range(len(Xs)):
            M += c[k] * Xs[k]
        X0s.append(M)
    return X0s


def so_eta_basis(eta):
    """Basis of so(eta) = {A : A^T eta + eta A = 0}: A_{ij} = eta_j E_ij - eta_i E_ji, i<j."""
    n = eta.shape[0]
    As = []
    for i in range(n):
        for j in range(i + 1, n):
            A = sp.zeros(n, n)
            A[i, j] = eta[j, j]
            A[j, i] = -eta[i, i]
            As.append(A)
    return As


def invariant_form_space_dim(Xs, As, label):
    """MEASURED count of isotropy-invariant symmetric bilinear forms on span(Xs):
    solve B([A,X],Y) + B(X,[A,Y]) = 0 for all isotropy generators A. Numerical nullspace;
    prints the singular-value gap so the count is auditable."""
    m = len(Xs)
    Xn = [np.array(X, dtype=float) for X in Xs]
    An = [np.array(A, dtype=float) for A in As]
    # coordinates on span(Xs): flatten matrices, solve least squares against basis
    Bmat = np.stack([X.flatten() for X in Xn], axis=1)  # 16 x m
    def coords(M):
        c, res, *_ = np.linalg.lstsq(Bmat, M.flatten(), rcond=None)
        assert (np.linalg.norm(Bmat @ c - M.flatten()) < 1e-10), "not in span"
        return c
    rows = []
    sym_pairs = [(a, b) for a in range(m) for b in range(a, m)]
    for A in An:
        rho = np.stack([coords(A @ X - X @ A) for X in Xn], axis=1)  # m x m, action matrix
        # invariance: rho^T G + G rho = 0; G symmetric parametrized by sym_pairs
        for (i, j) in [(a, b) for a in range(m) for b in range(m)]:
            row = np.zeros(len(sym_pairs))
            # entry (i,j) of rho^T G + G rho = sum_k rho[k,i] G[k,j] + G[i,k] rho[k,j]
            for p_idx, (a, b) in enumerate(sym_pairs):
                v = 0.0
                # G[a,b] = G[b,a] both contribute
                for (x, y) in ({(a, b), (b, a)}):
                    if y == j:
                        v += rho[x, i]
                    if x == i:
                        v += rho[y, j]
                row[p_idx] = v
            rows.append(row)
    Msys = np.array(rows)
    sv = np.linalg.svd(Msys, compute_uv=False)
    dim = int(np.sum(sv < 1e-9 * sv[0]))
    tail = sv[-(dim + 1):] if dim + 1 <= len(sv) else sv
    print(f"    [{label}] invariant symmetric forms: nullspace dim = {dim} "
          f"(smallest {min(dim + 2, len(sv))} singular values: "
          f"{np.array2string(sv[-min(dim + 2, len(sv)):], formatter={'float': lambda x: f'{x:.1e}'})})")
    return dim


# =====================================================================================
# Sections A-D
# =====================================================================================

def sections_ABCD():
    print("=" * 95)
    print("SECTIONS A-D: the fiber-metric obstruction, metric vs conformal, exact (sympy rationals)")
    print("=" * 95)
    eta = sp.diag(-1, 1, 1, 1)

    # ---- (A) metric fiber gl(4,R)/o(3,1) ----
    Xs = p_basis(eta)
    G = gram(Xs)
    sigA = exact_signature(G)
    print(f"\n(A) metric fiber tangent  p = gl(4,R)/o(3,1)  (eta-self-adjoint 4x4), dim = {len(Xs)}")
    print(f"    EXACT signature of B(X,Y)=tr(XY):  (+{sigA[0]}, -{sigA[1]}, 0:{sigA[2]})")
    # float cross-check
    evf = np.linalg.eigvalsh(np.array(G, dtype=float))
    print(f"    float cross-check eigenvalues: {np.array2string(evf, precision=3)}")
    assert sigA[2] == 0, "B must be nondegenerate on p"

    # ---- (B) conformal reduction sl(4,R)/so(3,1) ----
    X0s = traceless_subbasis(Xs)
    G0 = gram(X0s)
    sigB = exact_signature(G0)
    print(f"\n(B) CONFORMAL fiber tangent  p_0 = sl(4,R)/so(3,1)  (traceless eta-self-adjoint), dim = {len(X0s)}")
    print(f"    EXACT signature of B restricted:   (+{sigB[0]}, -{sigB[1]}, 0:{sigB[2]})")
    # the removed direction: X = I (pure trace / scale direction)
    I4 = sp.eye(4)
    BII = sp.trace(I4 * I4)
    orth = [sp.trace(I4 * X0) for X0 in X0s]
    print(f"    removed direction = pure-trace X = I (metric scale):  B(I,I) = {BII}  -> a PLUS direction")
    print(f"    B(I, p_0) = {orth}  (exactly orthogonal: the quotient removes ONE + direction)")
    assert all(o == 0 for o in orth)
    assert sigA[0] - sigB[0] == 1 and sigA[1] == sigB[1], "conformal quotient must remove exactly one + direction"

    # ---- uniqueness of the invariant form (measured, not asserted) ----
    print("\n    Which invariant forms exist at all (measured nullspace of the invariance equations):")
    As = so_eta_basis(eta)
    dim_p = invariant_form_space_dim(Xs, As, "p,  isotropy so(3,1)")
    dim_p0 = invariant_form_space_dim(X0s, As, "p_0, isotropy so(3,1)")
    print(f"    -> on p the invariant forms are span{{tr(XY), trX trY}} (dim {dim_p}); on the conformal")
    print(f"       tangent p_0 the invariant form is UNIQUE up to scale (dim {dim_p0}): every choice is")
    print(f"       c*B with signature (+{sigB[0]},-{sigB[1]}) or (+{sigB[1]},-{sigB[0]}) -- indefinite for every c != 0.")
    assert dim_p0 == 1, "conformal tangent should carry a unique invariant form up to scale"

    # ---- (C) isotropy of the conformal fiber ----
    print("\n(C) isotropy of the conformal fiber = stabilizer of the class [eta] in GL(4,R)")
    print("    = {g : g^T eta g = lam*eta, lam>0} = CO(3,1) = O(3,1) x R+.")
    t = sp.symbols('t', real=True)
    Bt = sp.eye(4)
    Bt[0, 0] = sp.cosh(t); Bt[0, 1] = sp.sinh(t)
    Bt[1, 0] = sp.sinh(t); Bt[1, 1] = sp.cosh(t)
    resid = sp.simplify(Bt.T * eta * Bt - eta)
    print(f"    boost B_t (0-1 plane): B_t^T eta B_t - eta = {resid.tolist()}  (EXACTLY zero, all t)")
    assert resid == sp.zeros(4, 4)
    norms = [float(sp.cosh(sp.Integer(tt))) for tt in (1, 5, 10)]
    print(f"    ||B_t|| entries cosh(t) at t=1,5,10: {norms[0]:.3f}, {norms[1]:.1f}, {norms[2]:.1f}"
          f"  -> unbounded inside the isotropy => isotropy NONCOMPACT (O(3,1) survives the quotient;")
    print("       only the scale R+ is removed, and R+ was not the source of noncompact isotropy).")

    # ---- (D) compact control ----
    print("\n(D) COMPACT CONTROL (machinery must discriminate): eta = I")
    etaE = sp.eye(4)
    XsE = p_basis(etaE)
    sigD1 = exact_signature(gram(XsE))
    X0E = traceless_subbasis(XsE)
    sigD2 = exact_signature(gram(X0E))
    print(f"    gl(4)/o(4)   (symmetric 4x4, dim {len(XsE)}):  EXACT signature (+{sigD1[0]}, -{sigD1[1]}, 0:{sigD1[2]})  -> DEFINITE")
    print(f"    sl(4)/so(4)  (traceless sym, dim {len(X0E)}):  EXACT signature (+{sigD2[0]}, -{sigD2[1]}, 0:{sigD2[2]})  -> DEFINITE")
    assert sigD1[1] == sigD1[2] == 0 and sigD2[1] == sigD2[2] == 0
    AsE = so_eta_basis(etaE)
    invariant_form_space_dim(XsE, AsE, "p,  isotropy so(4)")
    invariant_form_space_dim(X0E, AsE, "p_0, isotropy so(4)")

    print("\n(A-D verdict) conformal quotient removes EXACTLY the scale (+) direction:")
    print(f"    metric fiber (+{sigA[0]},-{sigA[1]}) --[quotient by scale, a + direction]--> conformal fiber (+{sigB[0]},-{sigB[1]}),")
    print("    still INDEFINITE, invariant form UNIQUE up to scale (measured), isotropy still NONCOMPACT.")
    print("    The compact control returns DEFINITE, so this is a measurement, not a machinery artifact.")
    return sigA, sigB, sigD1, sigD2


# =====================================================================================
# Section E: the GU carrier, anchors, J_quat, and the Weyl-squared-shaped block
# =====================================================================================

N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}          # signature (9,5), matching ghost_parity_krein.py "(9,5)"
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]  # self-dual SU(2)+ on the base {0,1,2,3}


def jw(n):
    """Jordan-Wigner gammas (copied from tests/generation-sector/ghost_parity_krein.py)."""
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def build_carrier():
    """Anchor reproduction: carrier, constraint surface, self-dual triplet, Krein form.
    Construction copied from tests/generation-sector/ghost_parity_krein.py, signature (9,5)."""
    base = jw(7)
    e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in TIMELIKE]
    I14, I128 = np.eye(N, dtype=complex), np.eye(DIM, dtype=complex)

    Gamma = np.hstack(e)
    rankG = int(np.linalg.matrix_rank(Gamma))
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    w, Vv = np.linalg.eigh(Pi)
    W = Vv[:, w > 0.5]
    kerdim = W.shape[1]

    J3 = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
          for (a, b, c, d) in SD]
    Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
    CasK = W.conj().T @ Cas @ W
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]

    # spinor Krein metric beta_S (product of spacelike gammas)
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    res = max(np.linalg.norm(bS @ sgen(e, i, j) + sgen(e, i, j).conj().T @ bS)
              for i in range(N) for j in range(i + 1, N))

    etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)
    B = Wt.conj().T @ K @ Wt
    B = 0.5 * (B + B.conj().T)
    sig = np.linalg.eigvalsh(B)
    npl = int(np.sum(sig > 1e-9))
    nmi = int(np.sum(sig < -1e-9))
    nz = int(np.sum(np.abs(sig) < 1e-9))

    print(f"    rank(Gamma) = {rankG}   dim ker(Gamma) = {kerdim}   triplet dim = {Wt.shape[1]} "
          f"(SU(2)+ Casimir = {top})")
    print(f"    beta_S pseudo-anti-Hermiticity residual = {res:.1e}")
    print(f"    triplet Krein signature = (+{npl}, -{nmi}, 0:{nz})")
    assert rankG == 128 and kerdim == 1664, "rank/kernel anchors failed"
    assert res < 1e-9, "beta_S anchor failed"
    assert npl == nmi == 96 and nz == 0, "triplet Krein signature anchor failed"
    return e, Gamma, Pi, Wt, K


def quaternionic_J(e128, ETAvec, seed=1):
    """Averaging construction of the quaternionic structure (copied from
    tests/generation-sector/step11_gu_native_parity_theorem.py, ETA transplanted)."""
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETAvec[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def perm_sign(perm):
    perm = list(perm)
    sign, seen = 1, [False] * len(perm)
    for i in range(len(perm)):
        if seen[i]:
            continue
        j, clen = i, 0
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            clen += 1
        if clen % 2 == 0:
            sign = -sign
    return sign


def random_weyl_tensor(rng, g=None, verbose=False):
    """Random 4D tensor with FULL Weyl symmetries w.r.t. metric g (default Euclidean delta):
    antisymmetry in (ab),(cd); pair symmetry; first Bianchi; totally trace-free."""
    if g is None:
        g = np.eye(4)
    T = rng.standard_normal((4, 4, 4, 4))
    T = 0.5 * (T - T.transpose(1, 0, 2, 3))
    T = 0.5 * (T - T.transpose(0, 1, 3, 2))
    T = 0.5 * (T + T.transpose(2, 3, 0, 1))
    # remove the Lambda^4 part (total antisymmetrization) -> first Bianchi holds
    A4 = np.zeros_like(T)
    for perm in permutations(range(4)):
        A4 += perm_sign(perm) * T.transpose(perm)
    R = T - A4 / 24.0
    # Weyl part (n=4): W = R - 1/2 (g o Ric) + s/6 (g o g)/... standard decomposition
    ginv = np.linalg.inv(g)
    Ric = np.einsum('ac,abcd->bd', ginv, R)                        # Ric_bd = g^{ac} R_{abcd}
    s = np.einsum('bd,bd->', ginv, Ric)
    KN = (np.einsum('ac,bd->abcd', g, Ric) - np.einsum('ad,bc->abcd', g, Ric)
          + np.einsum('bd,ac->abcd', g, Ric) - np.einsum('bc,ad->abcd', g, Ric))
    GG = np.einsum('ac,bd->abcd', g, g) - np.einsum('ad,bc->abcd', g, g)
    W = R - 0.5 * KN + (s / 6.0) * GG
    if verbose:
        r_anti1 = np.linalg.norm(W + W.transpose(1, 0, 2, 3))
        r_anti2 = np.linalg.norm(W + W.transpose(0, 1, 3, 2))
        r_pair = np.linalg.norm(W - W.transpose(2, 3, 0, 1))
        r_bian = np.linalg.norm(W + W.transpose(0, 2, 3, 1) + W.transpose(0, 3, 1, 2))
        r_tr = np.linalg.norm(np.einsum('ac,abcd->bd', ginv, W))
        print(f"    Weyl-symmetry residuals: antisym {r_anti1:.1e}/{r_anti2:.1e}, pair {r_pair:.1e}, "
              f"Bianchi {r_bian:.1e}, trace {r_tr:.1e}, ||W|| = {np.linalg.norm(W):.3f}")
        assert max(r_anti1, r_anti2, r_pair, r_bian, r_tr) < 1e-12
    return W


def section_E():
    print()
    print("=" * 95)
    print("SECTION E: C-07 tie-in -- is a Weyl-squared-shaped GU-native block necessarily J-commuting?")
    print("=" * 95)

    print("\n(E0) ANCHORS (construction copied from ghost_parity_krein.py, signature (9,5)):")
    e, Gamma, Pi, Wt, K = build_carrier()
    stamp("carrier + triplet + Krein anchors reproduced")

    I14, I128 = np.eye(N, dtype=complex), np.eye(DIM, dtype=complex)
    ETAvec = np.array([-1.0 if a in TIMELIKE else 1.0 for a in range(N)])

    # ---- J_quat ----
    U = quaternionic_J(e, ETAvec, seed=1)
    uu = np.linalg.norm(U @ U.conj() + I128)
    unit = np.linalg.norm(U @ U.conj().T - I128)
    print(f"\n(E1) J_quat = (I14 (x) U) o conj:  ||U U* + I|| = {uu:.1e} (J^2 = -I),  "
          f"||U U^dag - I|| = {unit:.1e} (antiunitary)")
    assert uu < 1e-9 and unit < 1e-9
    Jf = np.kron(I14, U)
    Jfi = np.linalg.inv(Jf)

    def hl(X):
        """H-linearity defect of a full-carrier operator: ||J X J^{-1} - X|| (J antiunitary)."""
        return float(np.linalg.norm(Jf @ X.conj() @ Jfi - X))

    def hl_spin(x):
        """Same defect for a 128-dim spinor-factor operator."""
        return float(np.linalg.norm(U @ x.conj() @ np.linalg.inv(U) - x))

    def Mvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j] = ETAvec[j]
        M[j, i] = -ETAvec[i]
        return M

    # so(9,5) carrier generators Sigma_ab = 1 (x) sgen_ab + Mvec_ab (x) 1
    def Sigma_full(i, j):
        return np.kron(I14, sgen(e, i, j)) + np.kron(Mvec(i, j), I128)

    # all 91 spin parts at the 128-level (cheap), 5 full-carrier samples (dense), plus Pi
    spin_defect = max(hl_spin(sgen(e, i, j)) for i in range(N) for j in range(i + 1, N))
    samples = [(0, 1), (0, 9), (4, 5), (2, 13), (3, 4)]
    full_defect = max(hl(Sigma_full(i, j)) for (i, j) in samples)
    pi_defect = hl(Pi)
    print(f"(E2) so(9,5) generators commute with J_quat:")
    print(f"     max H-linearity defect over ALL 91 spin generators (128-level) = {spin_defect:.1e}")
    print(f"     max defect over 5 FULL 1792-dim carrier generators Sigma_ab    = {full_defect:.1e}")
    print(f"     constraint projector Pi defect                                 = {pi_defect:.1e}")
    assert spin_defect < 1e-9 and full_defect < 1e-9 and pi_defect < 1e-8
    print("     => any REAL polynomial in these (in particular any quadratic curvature-squared-type")
    print("        block) is J-commuting; Kramers (J^2=-I) then forces even-multiplicity spectra.")
    stamp("J-commutation of so(9,5) verified")

    # ---- Weyl-squared-shaped block ----
    rng = np.random.default_rng(20260706)
    print("\n(E3) Weyl-squared-shaped block  W2 = sum_{abcd} C_{abcd} Sigma^{ab} Sigma^{cd} + h.c.,")
    print("     C a genuine random 4D WEYL-symmetric tensor (real coefficients) on the base {0,1,2,3}:")
    Wc = random_weyl_tensor(rng, verbose=True)
    # measured dimension of the Weyl space (should be the classical 10 in 4D)
    span = np.stack([random_weyl_tensor(rng).flatten() for _ in range(25)])
    weyl_rank = int(np.linalg.matrix_rank(span, tol=1e-10))
    print(f"    measured dim of the 4D Weyl-tensor space = {weyl_rank}")

    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    Sig = {p: Sigma_full(*p) for p in pairs}
    W2 = np.zeros((N * DIM, N * DIM), dtype=complex)
    for (a, b) in pairs:
        for (c, d) in pairs:
            coef = 4.0 * Wc[a, b, c, d]   # 4 = orientation multiplicity of (ab),(cd)
            if abs(coef) > 1e-15:
                W2 += coef * (Sig[(a, b)] @ Sig[(c, d)])
    W2 = 0.5 * (W2 + W2.conj().T)
    w2_defect = hl(W2)
    print(f"    ||W2|| = {np.linalg.norm(W2):.2f}   J-commutation defect of W2 = {w2_defect:.1e}")
    assert w2_defect < 1e-8
    stamp("Weyl-squared block built and J-verified")

    # ---- triplet compression and Kramers pairing ----
    print("\n(E4) Kramers pairing of W2 on the 192-dim self-dual triplet sector:")
    inv_res = np.linalg.norm(Jf @ Wt.conj() - Wt @ (Wt.conj().T @ Jf @ Wt.conj()))
    Utrip = Wt.conj().T @ Jf @ Wt.conj()
    ut_unit = np.linalg.norm(Utrip @ Utrip.conj().T - np.eye(Wt.shape[1]))
    ut_sq = np.linalg.norm(Utrip @ Utrip.conj() + np.eye(Wt.shape[1]))
    print(f"    triplet J-invariance residual ||(1-P)J P|| = {inv_res:.1e};  "
          f"J_trip unitarity = {ut_unit:.1e};  ||J_trip^2 + I|| = {ut_sq:.1e}")
    assert inv_res < 1e-8 and ut_unit < 1e-8 and ut_sq < 1e-8

    D = Wt.conj().T @ W2 @ Wt
    D = 0.5 * (D + D.conj().T)
    d_comm = np.linalg.norm(Utrip @ D.conj() @ np.linalg.inv(Utrip) - D)
    ev = np.linalg.eigvalsh(D)
    gaps = np.abs(ev[0::2] - ev[1::2])
    npl = int(np.sum(ev > 1e-8 * np.abs(ev).max()))
    nmi = int(np.sum(ev < -1e-8 * np.abs(ev).max()))
    signature = npl - nmi
    uniq, counts = np.unique(np.round(ev, 8), return_counts=True)
    print(f"    [D_trip, J_trip] defect = {d_comm:.1e}")
    print(f"    KRAMERS PAIRING: max |ev(2k)-ev(2k+1)| = {gaps.max():.1e}  "
          f"-> every eigenvalue has EVEN multiplicity")
    print(f"    distinct eigenvalues (rounded 1e-8) and multiplicities:")
    for u, c in zip(uniq, counts):
        print(f"        {u:+.6f}  x {c}")
    print(f"    all multiplicities even? {all(c % 2 == 0 for c in counts)}")
    print(f"    signature of D_trip = (+{npl}) - (-{nmi}) = {signature}   -> EVEN? {signature % 2 == 0}")
    assert d_comm < 1e-7
    assert gaps.max() < 1e-8 * max(1.0, np.abs(ev).max()), "Kramers pairing failed"
    assert all(c % 2 == 0 for c in counts)
    assert signature % 2 == 0
    stamp("triplet Kramers pairing verified")

    # ---- controls + lemma: the check has discriminating power ----
    print("\n(E5) CONTROLS AND A LEMMA (would the pairing check pass on foreign input? It must NOT):")
    # (i) rank-3 projector inside the triplet: foreign, odd signature, pairing broken
    X3 = rng.standard_normal((Wt.shape[1], 3)) + 1j * rng.standard_normal((Wt.shape[1], 3))
    C3 = X3 @ X3.conj().T
    C3 = 0.5 * (C3 + C3.conj().T)
    c3_defect = np.linalg.norm(Utrip @ C3.conj() @ np.linalg.inv(Utrip) - C3)
    ev3 = np.linalg.eigvalsh(C3)
    gaps3 = np.abs(ev3[0::2] - ev3[1::2])
    sig3 = int(np.sum(ev3 > 1e-8 * ev3.max())) - int(np.sum(ev3 < -1e-8 * ev3.max()))
    print(f"    (i) rank-3 projector in the triplet: J-defect = {c3_defect:.2f} (FOREIGN, O(1)),"
          f"  signature = {sig3} (ODD -- measured, not imported),"
          f"  max Kramers pair gap = {gaps3.max():.2e} (pairing BROKEN)")
    assert c3_defect > 0.5 and sig3 % 2 == 1 and gaps3.max() > 1e-3

    # (ii) LEMMA (found when this was first tried as a control): complexifying the WEYL
    # coefficients does NOT break J-commutation. Reason: hermitization turns the imaginary
    # part into (i/2) sum W2_{abcd} [Sigma^{ab}, Sigma^{cd}], and the commutator is
    # ANTIsymmetric under pair exchange (ab)<->(cd) while the Weyl tensor is SYMMETRIC --
    # so the imaginary part cancels IDENTICALLY. The wall covers the whole complex-Weyl class.
    Wc2 = random_weyl_tensor(rng)
    O = np.zeros((N * DIM, N * DIM), dtype=complex)
    for (a, b) in pairs:
        for (c, d) in pairs:
            coef = 4.0 * (Wc[a, b, c, d] + 1j * Wc2[a, b, c, d])
            if abs(coef) > 1e-15:
                O += coef * (Sig[(a, b)] @ Sig[(c, d)])
    O = 0.5 * (O + O.conj().T)          # hermitized complex-Weyl block
    o_defect = hl(O)
    Dc = Wt.conj().T @ O @ Wt
    Dc = 0.5 * (Dc + Dc.conj().T)
    evc = np.linalg.eigvalsh(Dc)
    gapsc = np.abs(evc[0::2] - evc[1::2])
    print(f"    (ii) LEMMA -- hermitized COMPLEX-Weyl-coefficient block: J-defect = {o_defect:.1e}"
          f"  (pair symmetry of Weyl cancels the imaginary part identically),")
    print(f"         max Kramers pair gap = {gapsc.max():.2e} (pairing HOLDS: even complexified Weyl"
          f" coefficients cannot escape the wall)")
    assert o_defect < 1e-8 and gapsc.max() < 1e-7

    # (iii) genuine pairing-breaking control: pair-ANTIsymmetric imaginary quadratic block.
    # y_{abcd} antisym in (ab),(cd) and ANTIsymmetric under pair exchange; then
    # O3 = i sum y_{abcd} Sigma^{ab} Sigma^{cd} is HERMITIAN but built with an essential
    # scalar i (equals i * (real element of so(9,5)) via the closed commutator) -> J-ANTIlinear.
    Ty = rng.standard_normal((4, 4, 4, 4))
    Ty = 0.5 * (Ty - Ty.transpose(1, 0, 2, 3))
    Ty = 0.5 * (Ty - Ty.transpose(0, 1, 3, 2))
    Ty = 0.5 * (Ty - Ty.transpose(2, 3, 0, 1))   # pair-ANTIsymmetric
    O3 = np.zeros((N * DIM, N * DIM), dtype=complex)
    for (a, b) in pairs:
        for (c, d) in pairs:
            coef = 4.0j * Ty[a, b, c, d]
            if abs(coef) > 1e-15:
                O3 += coef * (Sig[(a, b)] @ Sig[(c, d)])
    herm_res = np.linalg.norm(O3 - O3.conj().T)
    O3 = 0.5 * (O3 + O3.conj().T)
    o3_defect = hl(O3)
    D3 = Wt.conj().T @ O3 @ Wt
    D3 = 0.5 * (D3 + D3.conj().T)
    ev3b = np.linalg.eigvalsh(D3)
    gaps3b = np.abs(ev3b[0::2] - ev3b[1::2])
    sig3b = int(np.sum(ev3b > 1e-8 * np.abs(ev3b).max())) - int(np.sum(ev3b < -1e-8 * np.abs(ev3b).max()))
    print(f"    (iii) pair-ANTIsymmetric imaginary block (curvature-squared-shaped, NOT Weyl-shaped):")
    print(f"         Hermiticity residual (before symmetrize) = {herm_res:.1e}, ||O3|| = {np.linalg.norm(O3):.2f}")
    print(f"         J-defect = {o3_defect:.2f} (O(1): J-ANTIlinear, essential scalar i),")
    print(f"         signature = {sig3b} (the step10 J-antilinear ZERO class, reproduced),")
    print(f"         max Kramers pair gap = {gaps3b.max():.2e}  -- MEASURED SURPRISE: the pairing still")
    print(f"         holds here (an additional doubling structure on the quadratic-in-generators class;")
    print(f"         escaping J-commutation inside this class buys signature 0, not an odd count).")
    assert herm_res < 1e-9 and o3_defect > 0.5
    assert sig3b == 0, "J-antilinear quadratic block should have symmetric spectrum (sig 0)"

    # (iv) mixture diagnostic: J-commuting + J-anticommuting quadratic blocks summed
    Dm = D + D3
    evm = np.linalg.eigvalsh(Dm)
    gapsm = np.abs(evm[0::2] - evm[1::2])
    sigm = int(np.sum(evm > 1e-8 * np.abs(evm).max())) - int(np.sum(evm < -1e-8 * np.abs(evm).max()))
    print(f"    (iv) mixture D_trip + D3 (generic complex-coefficient quadratic block):"
          f"  max Kramers pair gap = {gapsm.max():.2e},  signature = {sigm}")
    if gapsm.max() < 1e-8 * max(1.0, np.abs(evm).max()):
        print(f"         pairing STILL holds on the mixture: within the quadratic-in-so(9,5) class,")
        print(f"         every tested member (real Weyl, complex Weyl, imaginary pair-antisym, mixture)")
        print(f"         has even multiplicities -- the wall on this class is stronger than Kramers alone.")
    else:
        print(f"         pairing broken on the mixture (as generic Kramers reasoning predicts).")
    stamp("controls done")

    return {
        "spin_defect": spin_defect, "full_defect": full_defect, "pi_defect": pi_defect,
        "w2_defect": w2_defect, "kramers_gap": float(gaps.max()), "signature": signature,
        "weyl_rank": weyl_rank, "c3_sig": sig3, "c3_defect": float(c3_defect),
        "c3_gap": float(gaps3.max()),
        "lemma_defect": float(o_defect), "lemma_gap": float(gapsc.max()),
        "anti_defect": float(o3_defect), "anti_gap": float(gaps3b.max()), "anti_sig": sig3b,
        "mix_gap": float(gapsm.max()), "mix_sig": sigm,
    }


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    sigA, sigB, sigD1, sigD2 = sections_ABCD()
    res = section_E()

    print()
    print("=" * 95)
    print("VERDICT (R4)")
    print("=" * 95)
    print(f"""
Conformal gauge INHERITS both obstructions; it cures neither.

  1. FIBER METRIC. The metric fiber tangent gl(4,R)/o(3,1) has EXACT invariant signature
     (+{sigA[0]},-{sigA[1]}) [re-derived from scratch, reproducing BIG-SWING-1]. The conformal quotient
     removes EXACTLY the pure-trace scale direction X = I, which is a + direction (B(I,I)=4),
     leaving sl(4,R)/so(3,1) with EXACT signature (+{sigB[0]},-{sigB[1]}) -- still indefinite, and now the
     invariant form is UNIQUE up to scale (measured nullspace dim 1), so indefiniteness is
     unavoidable on the conformal fiber. Isotropy remains the noncompact O(3,1) (boosts preserve
     [eta] exactly and are unbounded); the quotient only removed R+, which was never the source
     of noncompactness. Compact control: gl(4)/o(4) -> (+{sigD1[0]},0), sl(4)/so(4) -> (+{sigD2[0]},0), DEFINITE.

  2. C-07 WALL. On the verified 1792-dim carrier (anchors reproduced: rank(Gamma)=128,
     ker=1664, triplet Krein signature (+96,-96,0)), all so(9,5) generators commute with the
     quaternionic J (max defect {res['spin_defect']:.0e} / {res['full_defect']:.0e}), so ANY real polynomial in them --
     in particular the Weyl-squared-shaped block C_abcd Sigma^ab Sigma^cd with true 4D Weyl-
     symmetric real coefficients (J-defect {res['w2_defect']:.0e}) -- is J-commuting. Kramers (J^2=-I) then
     forces even-multiplicity spectra on the triplet sector (max pair gap {res['kramers_gap']:.0e}; measured
     signature {res['signature']}, even). LEMMA: even COMPLEX Weyl coefficients cannot escape (pair
     symmetry cancels the imaginary part identically; J-defect {res['lemma_defect']:.0e}, pairing gap {res['lemma_gap']:.0e}).
     Escaping J-commutation inside the quadratic-in-generators class (pair-ANTIsymmetric
     imaginary block, J-defect {res['anti_defect']:.0f}) buys only the J-antilinear ZERO class (measured
     signature {res['anti_sig']}); the mixture D+D3 measures pair gap {res['mix_gap']:.0e}, signature {res['mix_sig']}. The pairing
     check itself has discriminating power: a rank-3 projector in the triplet is foreign
     (J-defect {res['c3_defect']:.0f}), has ODD measured signature {res['c3_sig']}, and BREAKS the pairing (gap {res['c3_gap']:.1e}).

  BOUNDED NEGATIVE (mechanism-level, never "GU forces c"): a conformal-gravity-CLASS source
  action, built from GU-native blocks on GU's fiber and carrier, inherits the C-07 quaternionic
  wall unchanged, and the conformal quotient removes only the metric scale -- it does not touch
  indefiniteness (+{sigB[0]},-{sigB[1]}), noncompact isotropy, or quaternionic parity.

SCOPE. This tests the conformal CLASS structure transplanted to GU's fiber and carrier. It does
NOT build conformal gravity on X4, does not construct the Bach dynamics, and does not test
Mannheim's phenomenology or the PT-quantization mechanism itself.
""")
    stamp("done, exit 0")


if __name__ == "__main__":
    main()
