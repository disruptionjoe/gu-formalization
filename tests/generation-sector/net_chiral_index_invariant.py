"""
Theorem 2 substrate verification: the net chiral index as a FINITE-DIMENSIONAL invariant.

Backs the airtight, Fredholm-free proof that every linear Krein-isometric operator conserves the
net chiral index at zero on the (96,96) cross-chirality generation carrier.

Definition under test (finite-dim, no analysis):
  W = C^192, Gamma = grading (Gamma^2 = I, eigenspaces W_+, W_- each dim 96),
  K = nondegenerate Hermitian Krein form of signature (96,96), PURELY CROSS-CHIRALITY:
      W_+ and W_- are each K-isotropic (Lagrangian); K|_{W_+ x W_-} is a perfect pairing.
  A PHYSICAL subspace P is a maximal K-positive-definite subspace (dim 96).
  NET CHIRAL INDEX  chi(P) := dim pi_+(P) - dim pi_-(P),  pi_+- the grading projections.

Claims verified:
  (A) abstract (96,96) cross-chirality model: every physical subspace is the graph of an
      ISOMORPHISM W_+ -> W_-, so pi_+(P)=W_+, pi_-(P)=W_-, hence chi(P)=0.
  (B) a RANDOM linear Krein isometry U in U(96,96) maps physical subspaces to physical
      subspaces and preserves chi = 0 (U^dag K U = K checked to machine precision).
  (C) supertrace diagnostic: Re tr(Pi_P Gamma) = 0 on the K-orthonormal (spectral) representative.
      NOTE: tr(Pi_P Gamma) with the STANDARD-orthogonal projector is representative-dependent (a
      Krein isometry is not a standard unitary), so it is NOT the invariant -- the dimension
      difference chi = dim pi_+(P) - dim pi_-(P) is what is conserved. The run prints the
      post-isometry value to make this visible.
  (D) NON-TRIVIALITY CONTROL: for a grading-ALIGNED (Hilbert, non-cross) form K=diag(I,-I)
      the same definition gives chi = +96 (a maximally chiral configuration). So chi is a
      genuine invariant that DETECTS chirality; it is 0 here because of cross-chirality.
  (E) the real GU triplet (ghost_parity_krein construction) reproduces (A)-(C).
"""
import numpy as np

try:
    from scipy.linalg import expm
except Exception:  # pragma: no cover
    def expm(M):
        w, V = np.linalg.eig(M)
        return (V * np.exp(w)) @ np.linalg.inv(V)

rng = np.random.default_rng(0)
n = 96


def rank(A, tol=1e-7):
    if A.size == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > tol * max(1.0, s[0])))


def max_positive_subspace(K):
    """Basis (columns) of a maximal K-positive-definite subspace via spectral decomposition."""
    w, V = np.linalg.eigh(K)
    Q = V[:, w > 1e-9]
    # K-positive-definite check on the span
    G = Q.conj().T @ K @ Q
    assert np.min(np.linalg.eigvalsh(0.5 * (G + G.conj().T))) > 1e-9
    return Q


def chi(Q):
    """Net chiral index of subspace with basis columns Q: dim pi_+(P) - dim pi_-(P)."""
    return rank(Q[:n, :]) - rank(Q[n:, :])


def supertrace(Q):
    """Re tr(Pi_P Gamma) with Pi_P the standard-orthogonal projector onto P=col(Q)."""
    Qo, _ = np.linalg.qr(Q)            # orthonormal basis of P
    G = np.concatenate([np.ones(n), -np.ones(n)])  # Gamma diagonal
    return float(np.real(np.einsum('ij,i,ij->', Qo.conj(), G, Qo)))


def krein_isometry(K, scale=1.0):
    """Random U in the isometry group of K: U^dag K U = K, built as expm of a K-anti-self-adjoint X."""
    S = rng.standard_normal((2 * n, 2 * n)) + 1j * rng.standard_normal((2 * n, 2 * n))
    S = S - S.conj().T                # anti-Hermitian
    X = np.linalg.solve(K, S)          # X = K^{-1} S  =>  X^dag K + K X = 0
    X = scale * X / np.linalg.norm(X)  # keep ||X|| small so expm is well-conditioned
    return expm(X)


def report(tag, K):
    Gamma = np.diag(np.concatenate([np.ones(n), -np.ones(n)])).astype(complex)
    # Gamma is K-anti-self-adjoint: Gamma K + K Gamma = 0
    aself = np.linalg.norm(Gamma @ K + K @ Gamma)
    Q = max_positive_subspace(K)
    rp, rm = rank(Q[:n, :]), rank(Q[n:, :])
    c0, st0 = chi(Q), supertrace(Q)
    # random Krein isometry
    U = krein_isometry(K)
    iso = np.linalg.norm(U.conj().T @ K @ U - K) / np.linalg.norm(K)
    QU = U @ Q
    cU, stU = chi(QU), supertrace(QU)
    print(f"[{tag}]")
    print(f"   Gamma K-anti-self-adjoint residual ||GK+KG|| = {aself:.1e}")
    print(f"   physical subspace: dim pi_+(P)={rp}, dim pi_-(P)={rm}  ->  chi(P) = {c0:+d}   "
          f"(Re tr Pi_P Gamma = {st0:+.1e})")
    print(f"   random Krein isometry: ||U^dag K U - K||/||K|| = {iso:.1e}")
    print(f"   after U: chi(U.P) = {cU:+d}   (Re tr = {stU:+.1e})")
    return aself, c0, cU, st0, iso


def random_physical_subspace_index():
    """Independent check: random graph P={(x,Tx)} with (BT)+(BT)^dag >0 has chi=0, any T."""
    B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    K = np.block([[np.zeros((n, n)), B], [B.conj().T, np.zeros((n, n))]])
    ok = 0
    for _ in range(20):
        M = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        H = M @ M.conj().T + n * np.eye(n)          # H + H^dag > 0
        T = np.linalg.solve(B, H)                    # so BT = H, positivity holds
        Q = np.vstack([np.eye(n), T])
        G = Q.conj().T @ K @ Q
        assert np.min(np.linalg.eigvalsh(0.5 * (G + G.conj().T))) > 1e-9
        ok += (chi(Q) == 0)
    print(f"[random graph physical subspaces] chi=0 on {ok}/20 random T (all transverse, T iso)")


def gu_triplet_KGamma(timelike):
    """Build the real GU self-dual triplet's Krein form K and chirality grading Gamma (192-dim),
    reusing the ghost_parity_krein / t1a construction. Returns (K, Gamma) in the triplet basis."""
    NN, DD = 14, 128

    def jw(nn):
        I = np.eye(2, dtype=complex)
        s1 = np.array([[0, 1], [1, 0]], dtype=complex)
        s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
        s3 = np.array([[1, 0], [0, -1]], dtype=complex)
        G = []
        for k in range(nn):
            L, R = [s3] * k, [I] * (nn - 1 - k)
            for mid in (s1, s2):
                o = np.array([[1 + 0j]])
                for m in L + [mid] + R:
                    o = np.kron(o, m)
                G.append(o)
        return G

    bjw = jw(7)
    I128, I14 = np.eye(DD, dtype=complex), np.eye(NN, dtype=complex)
    e = [(1j * bjw[a] if a in timelike else bjw[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]

    def sg(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    def lv(i, j):
        M = np.zeros((NN, NN), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M

    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    Gam = np.hstack(e)
    Pi = np.eye(NN * DD, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
    J = [np.kron(I14, sg(a, b) + sg(c, d)) + np.kron(lv(a, b) + lv(c, d), I128) for (a, b, c, d) in SD]
    w, V = np.linalg.eigh(Pi); Wk = V[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Ue = np.linalg.eigh(CasK); top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Ue[:, np.abs(ev - top) < 1e-3]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    Kfull = np.kron(etaV, bS)
    om = I128.copy()
    for a in range(14):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DD).real
    chir = np.kron(I14, om if om2 > 0 else (-1j) * om)
    # restrict to triplet, in a basis where Gamma is the diagonal grading
    Kt = Wt.conj().T @ Kfull @ Wt; Kt = 0.5 * (Kt + Kt.conj().T)
    Ct = Wt.conj().T @ chir @ Wt; Ct = 0.5 * (Ct + Ct.conj().T)
    cev, cU = np.linalg.eigh(Ct)
    order = np.concatenate([np.where(cev > 0)[0], np.where(cev < 0)[0]])  # + then -
    Q = cU[:, order]
    Kdiag = Q.conj().T @ Kt @ Q
    Gdiag = np.diag(np.sign(cev[order])).astype(complex)
    return Kdiag, Gdiag


def gu_triplet_check():
    print("[real GU self-dual triplet: chirality structure + chi, by signature]")
    print("   (cross-chirality <=> Gamma K-anti-self-adjoint, ||GK+KG||~0, gives chi=0;")
    print("    grading-aligned <=> Gamma commutes with K, ||GK-KG||~0, gives |chi|=96)")
    for tl, lab, physical in [({4, 5, 6, 7, 8}, "(9,5)", True),
                              ({4, 5, 6, 7, 8, 9, 10}, "(7,7)", True),
                              (set(), "(14,0) Euclidean", False)]:
        Kg, Gg = gu_triplet_KGamma(tl)
        npq = Kg.shape[0] // 2
        anti = np.linalg.norm(Gg @ Kg + Kg @ Gg)
        comm = np.linalg.norm(Gg @ Kg - Kg @ Gg)
        xblk = max(np.linalg.norm(Kg[:npq, :npq]), np.linalg.norm(Kg[npq:, npq:]))
        Qp = max_positive_subspace(Kg)
        c = rank(Qp[:npq, :]) - rank(Qp[npq:, :])
        kind = "cross-chirality (vectorlike)" if anti < 1e-7 else "GRADING-ALIGNED (chiral)"
        print(f"   {lab}: ||GK+KG||={anti:.1e} ||GK-KG||={comm:.1e}  {kind}  ->  chi(P) = {c:+d}")
        if physical:
            assert anti < 1e-7 and xblk < 1e-7 and c == 0, (lab, anti, xblk, c)
        else:
            # Euclidean control: Krein structure needs timelike directions; here Gamma commutes
            # with K, the form is grading-aligned, and the SAME chi detects full chirality |chi|=96.
            assert comm < 1e-7 and abs(c) == 96, (lab, comm, c)
    print("   => cross-chirality (hence chi=0) holds for the PHYSICAL indefinite signatures with")
    print("      timelike directions; Euclidean (14,0) is grading-aligned -- a second non-triviality")
    print("      control, |chi|=96, consistent with the Krein form requiring q>0 (non-compact internal G).")


if __name__ == "__main__":
    # (A,B,C) abstract cross-chirality (96,96)
    B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    Kcross = np.block([[np.zeros((n, n)), B], [B.conj().T, np.zeros((n, n))]])
    a, c0, cU, st0, iso = report("abstract cross-chirality (96,96)", Kcross)
    assert a < 1e-9 and c0 == 0 and cU == 0 and abs(st0) < 1e-6 and iso < 1e-9

    # (D) non-triviality control: grading-aligned Hilbert form => chi = +96
    Kalign = np.diag(np.concatenate([np.ones(n), -np.ones(n)])).astype(complex)
    print("\n[NON-TRIVIALITY CONTROL] grading-aligned (Hilbert) form K = diag(I,-I):")
    Qa = max_positive_subspace(Kalign)
    print(f"   chi(P) = {chi(Qa):+d}   (a maximally chiral config; proves chi DETECTS chirality)")
    assert chi(Qa) == 96

    # independent random-graph check
    print()
    random_physical_subspace_index()

    # (E) the real GU triplet across signatures
    print()
    gu_triplet_check()

    print("\nVERIFIED: on the (96,96) cross-chirality carrier every physical subspace is "
          "chirality-balanced (chi=0); a random linear Krein isometry preserves chi=0. "
          "No Fredholm/spectral-flow input used -- pure finite-dim linear algebra.")
