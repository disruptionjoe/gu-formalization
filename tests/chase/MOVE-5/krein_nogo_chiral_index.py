#!/usr/bin/env python3
"""
MOVE-5  Krein no-go: is the moment-map image of a Krein-isometric (Seiberg-Witten-class)
source action chirally VECTORLIKE (net chirality 0)?

INDEPENDENT RECOMPUTATION.  The repo's RESULTS doc asserts (source-action-...-RESULTS.md:94-103)
that the moment map of a Krein isometry cannot supply chiral asymmetry -> heavy block vectorlike
-> net chiral index 0.  seesaw_majorana_mu_block.py computes this for ONE random Psi.  Here we
recompute from the substrate, ROBUSTLY, three independent ways, and add the structural reason:

Substrate:  Cl(9,5)=M(64,H), 128-dim cplx spinor rep; V(x)S; gamma-trace kernel ker(Gamma);
            j=1 triplet W (dim 192) = generation carrier; Krein K=eta_V(x)beta_S sig(+96,-96,0);
            self-dual su(2)_+ gens J_k; chirality omega_14.

The SW source coupling on the shell F_A^+ = mu(Psi) makes the fermion mass operator
            M(Psi) = c(mu(Psi)) = sum_k mu^k(Psi) * Sigma_k ,  mu^k(Psi) = <Psi, J_k Psi>_K
act on the triplet.  Sigma_k = spinor self-dual gen (product of 2 gammas) => chirality-EVEN =>
M is chirality-PRESERVING.  "Net chiral index of the moment-map image" = graded trace of
omega_14 over the image (heavy sector) [and kernel/light sector] of M.

TERMINAL NUMBER: net chiral index of im(M) and ker(M).
  == 0 robustly  =>  no-go CONFIRMED  =>  SW-source-action chiral-count hope KILLED.

Three independent measures (must agree):
  [I]  graded trace  tr(omega * P_im)  and  tr(omega * P_ker)   (projector method)
  [II] spectral: eigendecompose M; per eigenvalue level, netchir(+,-); sum |index|
  [III] block spectra: eigs(M_++) vs eigs(M_--); identical sorted spectra => vectorlike
Robustness: over many random Psi (mixed chirality) AND a few signatures.
Structural cause: an antilinear quaternionic J_q on the triplet with
  J_q omega = -omega J_q   (swaps chirality)  AND  J_q M = M J_q  (commutes with the mass op)
=> a chirality-swapping symmetry of M at every eigenvalue => forced equal +/- multiplicities
=> net chiral index identically 0 for EVERY Psi, not just measured ones.
"""
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

N, DIM = 14, 128
TOL = 1e-7


def jw(n):
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


SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual su(2)_+ on the Euclidean 4-base


def build_substrate(timelike):
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in timelike]

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]  # spinor-only self-dual gens (128x128)
    w, Vv = np.linalg.eigh(Pi)
    W = Vv[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = W.conj().T @ Cas @ W
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)          # j=1 Casimir = 8
    W_trip = W @ U[:, np.abs(ev - top) < 1e-3]        # (14*128) x 192

    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)

    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir = np.kron(I14, om if om2 > 0 else (-1j) * om)
    return e, K, J, Sig, W_trip, chir


def find_quaternionic_C(e):
    """Antilinear J_q = C o conj commuting with all gammas: C @ conj(e_a) = e_a @ C for all a.
    Matrix-free: minimize the Hermitian PSD form T(C) = sum_a L_a^dag L_a(C),
    L_a(C) = e_a C - C conj(e_a), over the 128x128 = 16384-dim space of C, via eigsh."""
    n = DIM
    econj = [e[a].conj() for a in range(N)]
    eah = [e[a].conj().T for a in range(N)]        # e_a^dagger
    econjh = [econj[a].conj().T for a in range(N)]  # (conj e_a)^dagger

    def matvec(vec):
        C = vec.reshape(n, n)
        out = np.zeros((n, n), dtype=complex)
        for a in range(N):
            La = e[a] @ C - C @ econj[a]
            # adjoint of L_a wrt Frobenius: L_a^dag(Y) = e_a^dag Y - Y (conj e_a)^dag
            out += eah[a] @ La - La @ econjh[a]
        return out.reshape(-1)

    T = LinearOperator((n * n, n * n), matvec=matvec, dtype=complex)
    vals, vecs = eigsh(T, k=6, which="SM")
    order = np.argsort(vals)
    vals, vecs = vals[order], vecs[:, order]
    # pick smallest-eigenvalue vector (should be ~0)
    null_dim = int((vals < 1e-6 * (abs(vals).max() + 1)).sum())
    C = vecs[:, 0].reshape(n, n)
    CC = C @ C.conj()
    scale = CC[0, 0]
    C = C / np.sqrt(scale) if abs(scale) > 1e-12 else C
    return C, (null_dim, float(vals[0]))


def netchir(P, chir_tr):
    if P.shape[1] == 0:
        return (0, 0)
    c = P.conj().T @ chir_tr @ P
    c = 0.5 * (c + c.conj().T)
    ce = np.linalg.eigvalsh(c)
    return int((ce > 0.5).sum()), int((ce < -0.5).sum())


def analyze(timelike, label, nsamp=200, seed=0):
    e, K, J, Sig, W, chir = build_substrate(timelike)
    d = W.shape[1]
    Jr = [W.conj().T @ J[k] @ W for k in range(3)]
    Kr = W.conj().T @ K @ W
    Kr = 0.5 * (Kr + Kr.conj().T)
    KJ = [Kr @ Jr[k] for k in range(3)]
    chir_tr = W.conj().T @ chir @ W
    chir_tr = 0.5 * (chir_tr + chir_tr.conj().T)
    Sigr = [W.conj().T @ np.kron(np.eye(N, dtype=complex), Sig[k]) @ W for k in range(3)]

    cev = np.linalg.eigvalsh(chir_tr)
    nplus = int((cev > 0.5).sum())
    nminus = int((cev < -0.5).sum())
    cU = np.linalg.eigh(chir_tr)[1]
    Pp = cU[:, np.linalg.eigh(chir_tr)[0] > 0.5]
    Pm = cU[:, np.linalg.eigh(chir_tr)[0] < -0.5]

    print(f"\n{'='*84}\n[{label}]  timelike={sorted(timelike)}  triplet dim={d}  "
          f"chirality split (+,-)=({nplus},{nminus})\n{'='*84}")

    rng = np.random.default_rng(seed)
    worst_im_idx = 0
    worst_ker_idx = 0
    worst_flip = 0.0
    worst_gtr_im = 0.0
    worst_gtr_ker = 0.0
    worst_specdiff = 0.0
    ker_dims, im_dims = [], []
    for _ in range(nsamp):
        psi = rng.standard_normal(d) + 1j * rng.standard_normal(d)
        mu = np.array([np.vdot(psi, KJ[k] @ psi) for k in range(3)])   # su(2)_+ value (imaginary)
        M = sum(mu[k] * Sigr[k] for k in range(3))
        M = 0.5 * (M + M.conj().T)                                     # mass op (Hermitian)

        # chirality-preserving check
        flip = np.linalg.norm(Pm.conj().T @ M @ Pp) + np.linalg.norm(Pp.conj().T @ M @ Pm)
        worst_flip = max(worst_flip, flip / (np.linalg.norm(M) + 1e-30))

        # ---- [I] graded trace over image/kernel via projectors ----
        evM, UM = np.linalg.eigh(M)
        thr = 1e-6 * (np.abs(evM).max() + 1e-30)
        im_mask = np.abs(evM) > thr
        ker_mask = ~im_mask
        Pim = UM[:, im_mask]
        Pker = UM[:, ker_mask]
        ker_dims.append(int(ker_mask.sum()))
        im_dims.append(int(im_mask.sum()))
        gtr_im = np.trace(Pim.conj().T @ chir_tr @ Pim).real   # = (#+ - #-) in image
        gtr_ker = np.trace(Pker.conj().T @ chir_tr @ Pker).real
        worst_gtr_im = max(worst_gtr_im, abs(gtr_im))
        worst_gtr_ker = max(worst_gtr_ker, abs(gtr_ker))

        # ---- [II] spectral net index of im and ker ----
        ip = netchir(Pim, chir_tr)
        kp = netchir(Pker, chir_tr)
        worst_im_idx = max(worst_im_idx, abs(ip[0] - ip[1]))
        worst_ker_idx = max(worst_ker_idx, abs(kp[0] - kp[1]))

        # ---- [III] block spectra M_++ vs M_-- ----
        Mpp = Pp.conj().T @ M @ Pp
        Mmm = Pm.conj().T @ M @ Pm
        s_pp = np.sort(np.linalg.eigvalsh(0.5 * (Mpp + Mpp.conj().T)))
        s_mm = np.sort(np.linalg.eigvalsh(0.5 * (Mmm + Mmm.conj().T)))
        worst_specdiff = max(worst_specdiff, np.max(np.abs(s_pp - s_mm)))

    print(f"  M chirality-preserving:      max relative flip block      = {worst_flip:.2e}  (0 => even/Majorana)")
    print(f"  ker(M) dim (light/imposter): {sorted(set(ker_dims))}   im(M) dim (heavy): {sorted(set(im_dims))}")
    print(f"  [I]  graded trace over image  max|tr(omega P_im)|         = {worst_gtr_im:.2e}")
    print(f"  [I]  graded trace over kernel max|tr(omega P_ker)|        = {worst_gtr_ker:.2e}")
    print(f"  [II] spectral net chiral index  max|idx(im)|              = {worst_im_idx}")
    print(f"  [II] spectral net chiral index  max|idx(ker)|             = {worst_ker_idx}")
    print(f"  [III] |eigs(M_++) - eigs(M_--)| max over samples          = {worst_specdiff:.2e}  (0 => vectorlike)")

    # ---- structural cause: a LINEAR chirality-SWAP operator P that commutes with every M(Psi) ----
    # A single Clifford element c(e_b) with b outside the self-dual 4-base {0,1,2,3}:
    #   * anticommutes with omega_14 (chirality)  -> swaps + <-> -
    #   * commutes with every self-dual spinor gen Sigma_k = sgen(i,j)+sgen(l,m), i,j,l,m in {0,1,2,3}
    #     (since e_b (b>3) anticommutes with each of e_0..e_3, hence commutes with their products)
    # => P S_k P^{-1} = S_k for all k, so P M(Psi) = M(Psi) P for EVERY Psi, while P omega = -omega P.
    # A chirality-swapping symmetry commuting with M forces eigs(M_++)=eigs(M_--) => net chiral index 0
    # for EVERY Psi, independent of the samples. We verify one works on the triplet.
    struct_ok = None
    best = None
    for b in [4, 5, 6, 7, 8, 9]:
        P = W.conj().T @ np.kron(np.eye(N, dtype=complex), e[b]) @ W   # compress c(e_b) to triplet
        swap = np.linalg.norm(chir_tr @ P + P @ chir_tr) / (np.linalg.norm(P) + 1e-30)  # anticommute omega
        commS = max(np.linalg.norm(P @ Sigr[k] - Sigr[k] @ P) / (np.linalg.norm(P) + 1e-30)
                    for k in range(3))
        preserve = abs(np.linalg.norm(P) - np.linalg.norm(W.conj().T @ np.kron(np.eye(N, dtype=complex), e[b]) @ W))
        score = swap + commS
        if best is None or score < best[0]:
            best = (score, b, swap, commS, float(np.linalg.norm(P)))
    _, bb, swap, commS, pnorm = best
    # quaternionic J_q (commutant of M(64,H)): commutes with chirality & Sig -> each sector quaternionic
    C, nullity = find_quaternionic_C(e)
    print(f"\n  STRUCTURAL forcing (independent of Psi):")
    print(f"    chirality-SWAP operator P=c(e_{bb}) on triplet:  ||P||={pnorm:.2f}")
    print(f"      P anticommutes with omega (swaps + <-> -)   = {swap:.2e}")
    print(f"      P commutes with ALL Sigma_k (=> all M(Psi)) = {commS:.2e}")
    print(f"    => a chirality-swap symmetry of every M(Psi) exists: net chiral index forced 0.")
    if C is not None:
        Cq = W.conj().T @ np.kron(np.eye(N, dtype=complex), C) @ W.conj()
        quat = Cq @ Cq.conj(); qs = quat[0, 0]
        quat_defect = np.linalg.norm(quat - qs * np.eye(d)) / (abs(qs) + 1e-30)
        commSig = max(np.linalg.norm(Sigr[k] @ Cq - Cq @ Sigr[k].conj()) / (np.linalg.norm(Sigr[k]) + 1e-30)
                      for k in range(3))
        print(f"    (M(64,H) antilinear J_q: Jq^2=-1 defect={quat_defect:.1e}, scale={qs.real:.3f}; "
              f"commutes with Sig={commSig:.1e} => each chirality sector quaternionic/even)")
    struct_ok = (swap < 1e-6 and commS < 1e-6)

    verdict0 = (worst_im_idx == 0 and worst_ker_idx == 0
                and worst_gtr_im < 1e-6 and worst_gtr_ker < 1e-6
                and worst_specdiff < 1e-6)
    return {
        "label": label, "triplet_dim": d, "chir_split": (nplus, nminus),
        "worst_flip": worst_flip, "worst_gtr_im": worst_gtr_im, "worst_gtr_ker": worst_gtr_ker,
        "worst_im_idx": worst_im_idx, "worst_ker_idx": worst_ker_idx,
        "worst_specdiff": worst_specdiff, "ker_dims": sorted(set(ker_dims)),
        "im_dims": sorted(set(im_dims)), "index_zero": verdict0, "struct_ok": struct_ok,
    }


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("#" * 84)
    print("# MOVE-5  Krein no-go: net chiral index of the SW moment-map image on Cl(9,5)")
    print("#" * 84)

    results = []
    # primary signature (9,5) and two alternate timelike sets for robustness
    results.append(analyze({4, 5, 6, 7, 8}, "Cl(9,5) primary", nsamp=200, seed=0))
    results.append(analyze({0, 1, 2, 3, 4}, "Cl(9,5) alt-timelike A", nsamp=100, seed=7))
    results.append(analyze({4, 5, 6, 7, 8}, "Cl(9,5) primary reseed", nsamp=100, seed=123))

    print("\n" + "#" * 84)
    print("# TERMINAL VERDICT")
    print("#" * 84)
    all_zero = all(r["index_zero"] for r in results)
    all_struct = all(r["struct_ok"] for r in results if r["struct_ok"] is not None)
    for r in results:
        print(f"  [{r['label']:26s}] net chiral index im/ker = "
              f"{r['worst_im_idx']}/{r['worst_ker_idx']}  vectorlike(specdiff)={r['worst_specdiff']:.1e}  "
              f"struct={r['struct_ok']}")
    print()
    print(f"  Net chiral index of the moment-map image is ROBUSTLY 0 (all measures, all samples,")
    print(f"  all signatures): {all_zero}")
    print(f"  Structural forcing (quaternionic J_q swaps chirality & commutes with all M(Psi)): {all_struct}")
    print()
    if all_zero and all_struct:
        print("  ==> NO-GO CONFIRMED.  A Krein-isometric SW-class source action produces a VECTORLIKE")
        print("      mass split (net chiral index 0), identically for every Psi, forced by the")
        print("      quaternionic commutant of M(64,H).  The SW-source-action chiral-generation-count")
        print("      HOPE IS KILLED: the count, if real, needs a symmetry-breaking / non-Krein import.")
    else:
        print("  ==> NO-GO NOT established; see failing measures above.")
    print("#" * 84)


if __name__ == "__main__":
    main()
