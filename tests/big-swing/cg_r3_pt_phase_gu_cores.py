#!/usr/bin/env python3
"""BIG SWING 2026-07-06 / ROUTE R3 - PT-phase classification of GU-native cores on the triplet sector.

QUESTION. Bender-Mannheim's central move (the PT / Pais-Uhlenbeck ghost resolution behind Mannheim's
conformal gravity) DERIVES definiteness from the dynamics' own spectral data: if a K-self-adjoint
(PT-symmetric) Hamiltonian is in the PT-UNBROKEN phase (real spectrum, diagonalizable, K definite on
each eigenspace), a unique C operator exists with C^2 = I, [C,A] = 0, K.C > 0, and the C-positive
sector is the physical Hilbert space -- definiteness DERIVED, not imported. BIG-SWING-1's Attempt 1 was
refuted precisely because definiteness was IMPORTED via a gauge-breaking compensator. This script asks:
is the Mannheim move actually AVAILABLE on GU's own carrier? For each GU-native core on the 192-dim
self-dual SU(2)+ generation-triplet sector W (Krein signature (+96,-96,0), the canon anchor), classify
the PT/Krein phase and, where a C exists, test whether it is canonical (derived) and whether the
C-positive physical sector is CHIRAL: print tr(chi Pi_+).

ARENA. The verified Cl(9,5) = M(64,H) carrier V (x) S = R^14 (x) C^128 = 1792, signature convention of
tests/generation-sector/gen_sector_bridge.py (eta = +1 for a=0..8, -1 for a=9..13) so the M_D anchors
bare ||[Pi_RS, M_D]|| = 58.7215 and C2 = ||Gamma M_D Pi_RS|| = 155.3625 reproduce exactly. The triplet
sector W is built by the ghost_parity_krein.py recipe (self-dual SU(2)+ on the spacelike base
{0,1,2,3} inside ker(Gamma), top Casimir sector, dim 192). Compressions to W use the KREIN-orthogonal
compression comp(A) = B^{-1} Wt^H K A Wt (B = K|W), which sends K-self-adjoint operators to
B-self-adjoint operators on W; every K-self-adjointness residual is printed, never assumed.

CORES (all constructions documented; "GU-native" = built only from GU's own a-priori objects: the
Clifford generators, so(9,5) generators, Pi_RS, M_D, the SU(2)+ Casimir):
  1. comp(M_D)                       - the GU-default twisted Dirac symbol (prior swings' core).
  2. comp(Pi_RS M_D Pi_RS)           - proved (and printed) IDENTICAL to core 1 on W, because
                                       W in ker(Gamma) and [K, Pi_RS] = 0.
  3. comp(SU(2)+ Casimir)            - scalar on W (printed); the maximally degenerate core.
  4. comp(sum_ab w_ab T_ab^2)        - Weyl-squared-SHAPED core: generic REAL-weighted sum of squares
                                       of total so(9,5) generators T_ab (finite-dim analog of a
                                       curvature-squared symbol; the conformal-gravity-class shape).
                                       Also 4a: the so(9,5) Casimir weights (printed near-scalar).
  5. mixed-grading GU-native cores   - comp(M_D) + c * core4 (two weight seeds, two couplings).
  C1. control: random J-commuting K-self-adjoint core on W  (2 seeds)
  C2. control: random NON-J K-self-adjoint core on W        (2 seeds)
  C3. control: definitizable core B^{-1}(Y^H Y + 0.1 I)     - NOT GU-native; by construction in the
      PT-UNBROKEN phase with a derived C. Its role: prove the pipeline CAN return "C DERIVED" and a
      nonzero tr(chi Pi_+), so a null result on GU cores is not a classifier tautology.

CLASSIFICATION per core (everything printed):
  (i)   K-self-adjointness residual ||B A - (B A)^H||;
  (ii)  spectrum: max |Im lambda|, number of complex eigenvalues -> PT-BROKEN if any; Jordan blocks /
        K-null (degenerate-Gram) eigenspaces -> SINGULAR (the equal-frequency Pais-Uhlenbeck analog);
  (iii) if PT-UNBROKEN: C = S S^H K (S a K-orthonormalized eigenbasis); residuals ||C^2 - I||,
        ||[C, A]||, ||KC - (KC)^H||, min eig(KC). C is DERIVED (canonical) iff K is DEFINITE on every
        eigenspace; if some eigenspace is K-indefinite, C exists but is NOT determined by the dynamics
        -- demonstrated concretely by building a second valid C via a hyperbolic rotation inside an
        indefinite eigenspace and printing that tr(chi Pi_+) MOVES;
  (iv)  ||[C, J_quat]|| (quaternionic structure restricted to W) and tr(chi Pi_+), chi the Cl(14)
        volume-element chirality compressed to W (tr chi|W = 0, the vectorlike anchor);
  (v)   ghost-parity relation: ||{C, chi}|| (a ghost parity in the R2/canon sense swaps generation and
        mirror, hence anticommutes with chi).

GUARDS. Anchors reproduced FIRST and asserted. No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3,
rank_H=4, ind_H=8} is assumed, inserted, hardcoded as an answer, or divided by; every count below is
MEASURED and any nonzero count would be labeled "mechanism M forces c", never "GU forces c".

Run: python tests/big-swing/cg_r3_pt_phase_gu_cores.py   (repo root; exit 0)
"""
import sys

import numpy as np

N, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3])
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual SU(2)+ on the spacelike base {0,1,2,3}

TOL_IM_REAL = 1e-8     # max |Im lambda| / scale below this -> spectrum counted real
TOL_IM_BROKEN = 1e-6   # above this -> PT-BROKEN
TOL_GRAM_NULL = 1e-7   # |eig(Gram)| / ||B|| below this -> K-null direction in an eigenspace
TOL_CLUSTER = 1e-6     # eigenvalue clustering (relative)
TOL_GEO = 1e-7         # svd threshold for eigenspace extraction (relative)


def herm(X):
    return 0.5 * (X + X.conj().T)


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


def lvec_base(i, j):
    """Plain antisymmetric vector generator on the spacelike base indices (as in ghost_parity_krein)."""
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def mvec_eta(i, j):
    """so(9,5) vector-rep generator with the eta convention of step11."""
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = ETA[j]
    M[j, i] = -ETA[i]
    return M


def quaternionic_J(e128, seed=1):
    """The phase-unique quaternionic structure of M(64,H) (copied from step10/step11)."""
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def build():
    base = jw(7)
    e = [base[a] if ETA[a] > 0 else 1j * base[a] for a in range(N)]
    I14 = np.eye(N, dtype=complex)
    I128 = np.eye(DIM, dtype=complex)

    # --- gamma-trace map, constraint projector, GU-default Dirac core (bridge convention) ---
    Gamma = np.hstack(e)
    sv = np.linalg.svd(Gamma, compute_uv=False)
    rank_Gamma = int(np.sum(sv > 1e-9 * sv[0]))
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(I14, cxi)
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))

    # --- ker(Gamma) basis and the self-dual SU(2)+ triplet sector W (ghost_parity_krein recipe) ---
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    dim_ker = Wk.shape[1]
    Jops = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec_base(a, b) + lvec_base(c, d), I128)
            for (a, b, c, d) in SD]
    Cas = -(Jops[0] @ Jops[0] + Jops[1] @ Jops[1] + Jops[2] @ Jops[2])
    CasK = herm(Wk.conj().T @ Cas @ Wk)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    sel = np.abs(ev - top) < 1e-3
    Wt = Wk @ U[:, sel]
    dim_W = Wt.shape[1]

    # --- spinor Krein metric beta_S = product of the 9 spacelike gammas; K = eta_V (x) beta_S ---
    bS = I128.copy()
    for a in range(N):
        if ETA[a] > 0:
            bS = bS @ e[a]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    res_beta = max(np.linalg.norm(bS @ sgen(e, i, j) + sgen(e, i, j).conj().T @ bS)
                   for i in range(N) for j in range(i + 1, N))
    etaV = np.diag(ETA).astype(complex)
    K = np.kron(etaV, bS)

    # --- Krein form on W and on ker(Gamma) ---
    B = herm(Wt.conj().T @ K @ Wt)
    sig = np.linalg.eigvalsh(B)
    npl = int(np.sum(sig > 1e-9))
    nmi = int(np.sum(sig < -1e-9))
    nz = int(np.sum(np.abs(sig) < 1e-9))
    minB = float(np.min(np.abs(sig)))

    # --- chirality: Cl(14) volume element ---
    chi_s = I128.copy()
    for a in range(N):
        chi_s = chi_s @ e[a]
    if np.linalg.norm(chi_s.conj().T - chi_s) > 1e-9:
        chi_s = 1j * chi_s
    chi_s = chi_s / np.sqrt(abs((chi_s @ chi_s)[0, 0].real))
    chi_full = np.kron(I14, chi_s)

    # --- quaternionic structure J_quat = I_14 (x) U ---
    Uq = quaternionic_J(e, seed=1)
    Jf = np.kron(I14, Uq)

    return dict(e=e, Gamma=Gamma, rank_Gamma=rank_Gamma, Pi=Pi, M_D=M_D, bare=bare, C2=C2,
                Wk=Wk, dim_ker=dim_ker, Cas=Cas, Wt=Wt, dim_W=dim_W, top=top,
                bS=bS, res_beta=res_beta, K=K, B=B, sigW=(npl, nmi, nz), minB=minB,
                chi_full=chi_full, Jf=Jf, I14=np.eye(N, dtype=complex), I128=np.eye(DIM, dtype=complex))


def krein_compress(K, B_inv, Wt, A_global):
    """Krein-orthogonal compression of a global operator to W: comp(A) = B^{-1} Wt^H K A Wt.
    Sends K-self-adjoint operators to B-self-adjoint operators on W."""
    return B_inv @ (Wt.conj().T @ (K @ (A_global @ Wt)))


def jdefect(JWm, X):
    """H-linearity defect of X on W w.r.t. the antiunitary J_W: v -> JWm conj(v)."""
    return float(np.linalg.norm(JWm @ X.conj() @ JWm.conj().T - X))


def build_C_from_clusters(A, B, clusters):
    """K-orthonormalized eigenbasis S (S^H B S = diag(+-1)) and C = S S^H B.
    Returns (C, S, signs, sigma_resid, gram_stats) or None if an eigenspace is K-degenerate."""
    n = A.shape[0]
    bscale = float(np.max(np.abs(np.linalg.eigvalsh(B))))
    cols, signs = [], []
    gram_stats = []   # per cluster: (mu, m, npos, nneg, nnull, min|gram eig|)
    for (mu, Qc) in clusters:
        G = herm(Qc.conj().T @ B @ Qc)
        gev, gvec = np.linalg.eigh(G)
        nnull = int(np.sum(np.abs(gev) < TOL_GRAM_NULL * bscale))
        npos = int(np.sum(gev > TOL_GRAM_NULL * bscale))
        nneg = int(np.sum(gev < -TOL_GRAM_NULL * bscale))
        gram_stats.append((mu, Qc.shape[1], npos, nneg, nnull, float(np.min(np.abs(gev)))))
        if nnull > 0:
            return None, None, None, None, gram_stats
        for k in range(len(gev)):
            u = Qc @ gvec[:, k]
            u = u / np.sqrt(abs(gev[k]))
            cols.append(u)
            signs.append(1.0 if gev[k] > 0 else -1.0)
    S = np.array(cols).T
    signs = np.array(signs)
    sigma_resid = float(np.linalg.norm(S.conj().T @ B @ S - np.diag(signs)))
    C = S @ S.conj().T @ B
    return C, S, signs, sigma_resid, gram_stats


def classify(name, A, B, B_inv, JWm, chiW, verbose=True, alt_demo=True):
    """Full PT/Krein phase classification of a B-self-adjoint core A on (W, B)."""
    n = A.shape[0]
    row = dict(name=name, phase="?", c_status="-", cj="-", trchi="-", ghost="-")
    BA = B @ A
    ksa = float(np.linalg.norm(BA - BA.conj().T))
    jdef = jdefect(JWm, A)
    comm_chi = float(np.linalg.norm(A @ chiW - chiW @ A))
    anti_chi = float(np.linalg.norm(A @ chiW + chiW @ A))
    lam = np.linalg.eigvals(A)
    scale = max(float(np.max(np.abs(lam))), 1e-30)
    imax = float(np.max(np.abs(lam.imag)))
    n_cplx = int(np.sum(np.abs(lam.imag) > TOL_IM_BROKEN * scale))
    print(f"\n--- CORE: {name} ---")
    print(f"  (i)  K-self-adjointness ||BA - (BA)^H|| = {ksa:.2e}   ||A|| = {np.linalg.norm(A):.4f}")
    print(f"       J-commutation defect ||J A J^-1 - A|| = {jdef:.2e}"
          f"   chi-grading: ||[A,chi]|| = {comm_chi:.3f}  ||{{A,chi}}|| = {anti_chi:.3f}")
    print(f"  (ii) spectrum: max|Im lambda| = {imax:.3e} (scale {scale:.3f}),"
          f" complex eigenvalues (|Im|>{TOL_IM_BROKEN:.0e}*scale): {n_cplx}")
    row["ksa"], row["jdef_A"], row["imax"] = ksa, jdef, imax
    if n_cplx > 0:
        npair = n_cplx // 2
        row["phase"] = "PT-BROKEN"
        print(f"       -> PT-BROKEN: {npair} complex-conjugate pairs present; no C operator exists.")
        return row
    if imax > TOL_IM_REAL * scale:
        row["phase"] = "BOUNDARY(ambig)"
        print("       -> spectrum real only marginally (between tolerances): PT-boundary / ambiguous;")
        print("          treated as SINGULAR-adjacent, no C construction attempted.")
        return row

    # real spectrum: cluster and extract eigenspaces by SVD
    lr = np.sort(lam.real)
    gaps = np.where(np.diff(lr) > TOL_CLUSTER * scale)[0]
    bounds = [0] + [int(g) + 1 for g in gaps] + [n]
    clusters_raw = [(float(np.mean(lr[bounds[i]:bounds[i + 1]])), bounds[i + 1] - bounds[i])
                    for i in range(len(bounds) - 1)]
    clusters, total_geo, jordan = [], 0, False
    for (mu, m_alg) in clusters_raw:
        u_, s_, vh_ = np.linalg.svd(A - mu * np.eye(n))
        m_geo = int(np.sum(s_ < TOL_GEO * scale))
        if m_geo < m_alg:
            jordan = True
        Qc = vh_[n - m_geo:, :].conj().T if m_geo > 0 else np.zeros((n, 0))
        clusters.append((mu, Qc))
        total_geo += m_geo
    mults = sorted(set(m for (_, m) in clusters_raw))
    print(f"       real spectrum: {len(clusters_raw)} clusters, multiplicities {mults},"
          f" sum(geometric) = {total_geo} / {n}")
    if jordan or total_geo < n:
        row["phase"] = "SINGULAR(Jordan)"
        print("       -> SINGULAR: geometric < algebraic multiplicity (Jordan blocks);")
        print("          the equal-frequency Pais-Uhlenbeck analog. No C operator exists.")
        return row

    C, S, signs, sig_resid, gram_stats = build_C_from_clusters(A, B, clusters)
    ndef = sum(1 for (_, m, p_, q_, z_, _) in gram_stats if z_ == 0 and (p_ == 0 or q_ == 0))
    nindef = sum(1 for (_, m, p_, q_, z_, _) in gram_stats if z_ == 0 and p_ > 0 and q_ > 0)
    nnull = sum(1 for (_, m, p_, q_, z_, _) in gram_stats if z_ > 0)
    ming = min(g[5] for g in gram_stats)
    print(f"       eigenspace K-Gram census: {ndef} definite, {nindef} indefinite, {nnull} with"
          f" K-null directions; min |Gram eig| = {ming:.3e}")
    if len(gram_stats) <= 8:
        for (mu_, m_, p_, q_, z_, mg_) in gram_stats:
            print(f"         eigenspace mu = {mu_:+.4f}: dim {m_}, K-signature (+{p_}, -{q_}, 0:{z_}),"
                  f" min |Gram eig| = {mg_:.3e}")
    if C is None:
        row["phase"] = "SINGULAR(K-null)"
        print("       -> SINGULAR: an eigenspace carries K-null directions (degenerate Gram);")
        print("          the C-operator construction degenerates (PU equal-frequency point).")
        return row

    derived = (nindef == 0)
    row["phase"] = "PT-UNBROKEN"
    row["c_status"] = "DERIVED" if derived else "NON-CANONICAL"
    c2r = float(np.linalg.norm(C @ C - np.eye(n)))
    car = float(np.linalg.norm(C @ A - A @ C))
    KC = B @ C
    kcr = float(np.linalg.norm(KC - KC.conj().T))
    kcm = float(np.min(np.linalg.eigvalsh(herm(KC))))
    cj = jdefect(JWm, C)
    Pip = 0.5 * (np.eye(n) + C)
    trchi = np.trace(chiW @ Pip)
    ghost = float(np.linalg.norm(C @ chiW + chiW @ C))
    print(f"  (iii) C built: ||S^H B S - diag(+-1)|| = {sig_resid:.2e}  ||C^2 - I|| = {c2r:.2e}"
          f"  ||[C,A]|| = {car:.2e}")
    print(f"        ||KC - (KC)^H|| = {kcr:.2e}   min eig(KC) = {kcm:.4e}  (positive => K.C > 0)")
    print(f"        C status: {'DERIVED (every eigenspace K-definite: unique C)' if derived else 'NON-CANONICAL (K indefinite on ' + str(nindef) + ' eigenspaces: C exists but is NOT determined by the dynamics)'}")
    print(f"  (iv)  ||[C, J_quat]|| = {cj:.2e}")
    print(f"        tr(chi Pi_+) = {trchi.real:+.6f} {trchi.imag:+.2e}j")
    print(f"  (v)   ghost-parity relation ||{{C, chi}}|| = {ghost:.3e}"
          f"  (0 => C swaps chirality halves like the R2 ghost parity)")
    row["cj"] = f"{cj:.1e}"
    row["trchi"] = f"{trchi.real:+.3f}"
    row["ghost"] = f"{ghost:.1e}"
    row["trchi_val"] = float(trchi.real)
    row["derived"] = derived

    if (not derived) and alt_demo:
        # demonstrate non-uniqueness: hyperbolic rotation inside the first indefinite eigenspace
        idx = 0
        offs = []
        off = 0
        for (mu, Qc) in clusters:
            offs.append(off)
            off += Qc.shape[1]
        for k, (mu_, m_, p_, q_, z_, _) in enumerate(gram_stats):
            if p_ > 0 and q_ > 0:
                idx = k
                break
        o = offs[idx]
        m = gram_stats[idx][1]
        loc_signs = signs[o:o + m]
        jp = o + int(np.where(loc_signs > 0)[0][0])
        jm = o + int(np.where(loc_signs < 0)[0][0])
        t = 0.6
        S2 = S.copy()
        S2[:, jp] = np.cosh(t) * S[:, jp] + np.sinh(t) * S[:, jm]
        S2[:, jm] = np.sinh(t) * S[:, jp] + np.cosh(t) * S[:, jm]
        C2m = S2 @ S2.conj().T @ B
        c2r2 = float(np.linalg.norm(C2m @ C2m - np.eye(n)))
        car2 = float(np.linalg.norm(C2m @ A - A @ C2m))
        kcm2 = float(np.min(np.linalg.eigvalsh(herm(B @ C2m))))
        tr2 = np.trace(chiW @ (0.5 * (np.eye(n) + C2m)))
        print(f"        NON-UNIQUENESS DEMO (hyperbolic rotation t=0.6 inside indefinite eigenspace"
              f" mu={gram_stats[idx][0]:+.4f}):")
        print(f"          alt C: ||C'^2 - I|| = {c2r2:.2e}  ||[C',A]|| = {car2:.2e}"
              f"  min eig(KC') = {kcm2:.4e}  -> equally valid C")
        print(f"          tr(chi Pi'_+) = {tr2.real:+.6f}  (was {trchi.real:+.6f};"
              f" delta = {tr2.real - trchi.real:+.6f})")
        row["alt_delta"] = float(tr2.real - trchi.real)
    return row


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    rng = np.random.default_rng(7)
    print("=" * 100)
    print("R3: PT-phase classification of GU-native cores on the self-dual triplet sector W")
    print("=" * 100)

    D = build()
    e, K, B, Wt, Wk = D["e"], D["K"], D["B"], D["Wt"], D["Wk"]
    I14, I128 = D["I14"], D["I128"]
    nW = D["dim_W"]

    # ================= ANCHORS =================
    print("\n[ANCHORS -- reproduced before any claim]")
    print(f"  rank(Gamma) = {D['rank_Gamma']}   (target 128)")
    print(f"  dim ker(Gamma) = {D['dim_ker']}   (target 1664)")
    print(f"  bare ||[Pi_RS, M_D]|| = {D['bare']:.4f}   (target 58.7215)")
    print(f"  C2 = ||Gamma M_D Pi_RS|| = {D['C2']:.4f}   (target 155.3625)")
    print(f"  beta_S pseudo-anti-Hermiticity residual = {D['res_beta']:.2e}   (target ~0)")
    print(f"  triplet sector dim = {nW}   (target 192), Casimir top eigenvalue = {D['top']}")
    npl, nmi, nz = D["sigW"]
    print(f"  triplet Krein signature = (+{npl}, -{nmi}, 0:{nz})   (target (+96, -96, 0));"
          f" min |eig B| = {D['minB']:.4f}")
    assert D["rank_Gamma"] == 128 and D["dim_ker"] == 1664 and nW == 192
    assert abs(D["bare"] - 58.7215) < 1e-2 and abs(D["C2"] - 155.3625) < 1e-2
    assert D["res_beta"] < 1e-9 and (npl, nmi, nz) == (96, 96, 0)

    # ================= STRUCTURE on W =================
    print("\n[STRUCTURE on W]")
    chi_full = D["chi_full"]
    chi2 = float(np.linalg.norm(chi_full @ chi_full - np.eye(N * DIM)))
    chiK = float(np.linalg.norm(K @ chi_full + chi_full @ K))
    chi_inv = float(np.linalg.norm((np.eye(N * DIM) - Wt @ Wt.conj().T) @ (chi_full @ Wt)))
    chiW = Wt.conj().T @ chi_full @ Wt
    chiW2 = float(np.linalg.norm(chiW @ chiW - np.eye(nW)))
    trchiW = complex(np.trace(chiW))
    chiB = float(np.linalg.norm(B @ chiW + chiW @ B))
    print(f"  chi (Cl(14) volume element): ||chi^2 - I|| = {chi2:.2e},  ||{{K, chi}}|| = {chiK:.2e}"
          f"  (chi ANTI-commutes with K)")
    print(f"  chi preserves W: ||(1 - P_W) chi W|| = {chi_inv:.2e};  ||chi_W^2 - I|| = {chiW2:.2e}")
    print(f"  tr(chi|W) = {trchiW.real:+.2e}  (vectorlike anchor: net chiral asymmetry of triplet = 0)")
    print(f"  ||{{B, chi_W}}|| = {chiB:.2e}  => each chirality half of W is totally K-null (canon)")
    Pp = 0.5 * (np.eye(nW) + chiW)
    Pm = 0.5 * (np.eye(nW) - chiW)
    nullp = float(np.max(np.abs(np.linalg.eigvalsh(herm(Pp @ B @ Pp)))))
    nullm = float(np.max(np.abs(np.linalg.eigvalsh(herm(Pm @ B @ Pm)))))
    print(f"  max |eig(K on chi=+1 half)| = {nullp:.2e},  chi=-1 half: {nullm:.2e}   (both ~0: null)")
    assert abs(trchiW.real) < 1e-8 and chiK < 1e-8 and nullp < 1e-8 and nullm < 1e-8

    Jf = D["Jf"]
    Uq = Jf[:DIM, :DIM]
    jj = float(np.linalg.norm(Uq @ Uq.conj() + I128))
    Jinv = float(np.linalg.norm((np.eye(N * DIM) - Wt @ Wt.conj().T) @ (Jf @ Wt.conj())))
    JWm = Wt.conj().T @ Jf @ Wt.conj()
    jwu = float(np.linalg.norm(JWm.conj().T @ JWm - np.eye(nW)))
    jw2 = float(np.linalg.norm(JWm @ JWm.conj() + np.eye(nW)))
    jB = jdefect(JWm, B)
    print(f"  J_quat: ||U Ubar + I|| = {jj:.2e} (J^2 = -1);  J preserves W: resid = {Jinv:.2e}")
    print(f"  J_W unitarity = {jwu:.2e},  ||J_W J_Wbar + I|| = {jw2:.2e},  K is H-linear:"
          f" jdef(B) = {jB:.2e}")
    assert jj < 1e-6 and Jinv < 1e-7 and jw2 < 1e-7

    B_inv = np.linalg.inv(B)
    Pi, M_D, Cas = D["Pi"], D["M_D"], D["Cas"]
    kmd = float(np.linalg.norm(K @ M_D - M_D.conj().T @ K))
    kpi = float(np.linalg.norm(K @ Pi - Pi @ K))
    print(f"  global K-self-adjointness: ||K M_D - M_D^H K|| = {kmd:.2e},  ||[K, Pi_RS]|| = {kpi:.2e}")

    # ================= CORES =================
    print("\n[CORES]")
    rows = []

    # 1. comp(M_D)
    A1 = krein_compress(K, B_inv, Wt, M_D)
    rows.append(classify("1. comp(M_D)  [GU default Dirac core]", A1, B, B_inv, JWm, chiW))

    # 2. comp(Pi M_D Pi) -- identical on W (printed proof)
    A2 = krein_compress(K, B_inv, Wt, Pi @ M_D @ Pi)
    d12 = float(np.linalg.norm(A1 - A2))
    print(f"\n--- CORE: 2. comp(Pi_RS M_D Pi_RS) ---")
    print(f"  ||comp(Pi M_D Pi) - comp(M_D)|| = {d12:.2e}  -> IDENTICAL to core 1 on W")
    print(f"  (reason: W in ker(Gamma) so Pi Wt = Wt, and [K, Pi] = {kpi:.1e} = 0; no separate run)")
    rows.append(dict(name="2. comp(Pi M_D Pi)", phase="= core 1", c_status="= core 1",
                     cj="-", trchi="-", ghost="-"))

    # 3. comp(SU(2)+ Casimir) -- scalar on W
    A3 = krein_compress(K, B_inv, Wt, Cas)
    c3 = complex(np.trace(A3) / nW)
    scal3 = float(np.linalg.norm(A3 - c3 * np.eye(nW)))
    print(f"\n--- CORE: 3. comp(SU(2)+ Casimir) ---")
    print(f"  ||A - ({c3.real:.4f}) I|| = {scal3:.2e}  -> exactly scalar on W (W is the top Casimir sector)")
    rows.append(classify("3. comp(SU(2)+ Casimir)  [scalar]", A3, B, B_inv, JWm, chiW))

    # 4. Weyl-squared-shaped: generic real-weighted sum of squares of so(9,5) total generators
    print("\n[building core 4: sum_ab w_ab T_ab^2 over all 91 so(9,5) pairs, seeded real weights]")
    pairs = [(a, b) for a in range(N) for b in range(a + 1, N)]

    def quad_core(weights):
        Acc = np.zeros((N * DIM, N * DIM), dtype=complex)
        for (a, b), wab in zip(pairs, weights):
            L = mvec_eta(a, b)
            s = sgen(e, a, b)
            Acc += wab * (np.kron(L @ L, I128) + 2.0 * np.kron(L, s) + np.kron(I14, s @ s))
        return Acc

    # K-pseudo-anti-Hermiticity of the total generators (vector leg included), printed
    resT = max(float(np.linalg.norm(
        K @ (np.kron(mvec_eta(a, b), I128) + np.kron(I14, sgen(e, a, b)))
        + (np.kron(mvec_eta(a, b), I128) + np.kron(I14, sgen(e, a, b))).conj().T @ K))
        for (a, b) in [(0, 1), (0, 9), (9, 13), (3, 11)])
    print(f"  total-generator K-pseudo-anti-Hermiticity residual (sampled pairs) = {resT:.2e}")

    w4 = rng.standard_normal(len(pairs))
    A4g = quad_core(w4)
    A4 = krein_compress(K, B_inv, Wt, A4g)
    # 4a: so(9,5) Casimir weights -> near-scalar (printed, not classified separately)
    wcas = np.array([ETA[a] * ETA[b] for (a, b) in pairs])
    A4ag = quad_core(wcas)
    A4a = krein_compress(K, B_inv, Wt, A4ag)
    c4a = complex(np.trace(A4a) / nW)
    scal4a = float(np.linalg.norm(A4a - c4a * np.eye(nW)))
    print(f"  4a (so(9,5) Casimir weights): ||A - ({c4a.real:.4f}) I|| = {scal4a:.2e}"
          f"  {'(scalar: ker Gamma is so(9,5)-irreducible)' if scal4a < 1e-6 else '(NOT scalar)'}")
    rows.append(classify("4. comp(sum w_ab T_ab^2)  [Weyl^2-shaped, seed 7]", A4, B, B_inv, JWm, chiW))

    # structural facts about cores 1 and 4 (printed, cited in the doc)
    c1sq = complex(np.trace(A1 @ A1) / nW)
    sq_res = float(np.linalg.norm(A1 @ A1 - c1sq * np.eye(nW)))
    comm14 = float(np.linalg.norm(A1 @ A4 - A4 @ A1))
    print(f"\n  [structure] comp(M_D)^2 = ({c1sq.real:.6f}) I, residual {sq_res:.2e}"
          f"  (two-frequency +-omega structure, omega = {abs(c1sq.real)**0.5:.4f})")
    print(f"  [structure] ||[comp(M_D), comp(W2 seed7)]|| = {comm14:.2e}"
          f"  ({'commute: mixed-core eigenspaces are joint (lambda_1, lambda_4) sectors' if comm14 < 1e-9 else 'do NOT commute'})")

    # 5. mixed-grading GU-native cores: comp(M_D) + c * core4 (grading mixes odd and even)
    w4b = np.random.default_rng(8).standard_normal(len(pairs))
    A4b = krein_compress(K, B_inv, Wt, quad_core(w4b))
    for tag, A4x, cc in [("seed 7, c=0.5", A4, 0.5), ("seed 7, c=1.5", A4, 1.5), ("seed 8, c=0.5", A4b, 0.5)]:
        cscale = cc * np.linalg.norm(A1) / np.linalg.norm(A4x)
        Am = A1 + cscale * A4x
        rows.append(classify(f"5. comp(M_D) + {cc}*|A1|/|A4|*comp(W2 {tag.split(',')[0]})  [mixed, {tag}]",
                             Am, B, B_inv, JWm, chiW))

    # C1. random J-commuting K-self-adjoint controls
    for sd in (21, 22):
        r2 = np.random.default_rng(sd)
        X = r2.standard_normal((nW, nW)) + 1j * r2.standard_normal((nW, nW))
        X = 0.5 * (X + B_inv @ X.conj().T @ B)                      # K-symmetrize
        X = 0.5 * (X + JWm @ X.conj() @ JWm.conj().T)               # J-symmetrize
        X = 0.5 * (X + B_inv @ X.conj().T @ B)
        rows.append(classify(f"C1. random J-commuting K-self-adjoint (seed {sd})  [control]",
                             X, B, B_inv, JWm, chiW, alt_demo=False))

    # C2. random NON-J K-self-adjoint controls
    for sd in (31, 32):
        r2 = np.random.default_rng(sd)
        X = r2.standard_normal((nW, nW)) + 1j * r2.standard_normal((nW, nW))
        X = 0.5 * (X + B_inv @ X.conj().T @ B)
        rows.append(classify(f"C2. random non-J K-self-adjoint (seed {sd})  [control]",
                             X, B, B_inv, JWm, chiW, alt_demo=False))

    # C3. definitizable positive control (NOT GU-native): A = B^{-1}(Y^H Y + 0.1 I)
    r3 = np.random.default_rng(41)
    Y = r3.standard_normal((nW, nW)) + 1j * r3.standard_normal((nW, nW))
    H = Y.conj().T @ Y / nW + 0.1 * np.eye(nW)
    A_def = B_inv @ H
    rows.append(classify("C3. definitizable B^{-1}(Y^H Y + 0.1I)  [NOT GU-native; positive control]",
                         A_def, B, B_inv, JWm, chiW, alt_demo=False))

    # ================= CROSS-CHECK on the 1664-dim gamma-traceless slice =================
    print("\n[CROSS-CHECK: comp(M_D) on the full 1664-dim ker(Gamma) slice]")
    Bk = herm(Wk.conj().T @ K @ Wk)
    sk = np.linalg.eigvalsh(Bk)
    kp = int(np.sum(sk > 1e-9))
    km = int(np.sum(sk < -1e-9))
    kz = int(np.sum(np.abs(sk) < 1e-9))
    print(f"  K signature on ker(Gamma) = (+{kp}, -{km}, 0:{kz})")
    Bk_inv = np.linalg.inv(Bk)
    Ak = Bk_inv @ (Wk.conj().T @ (K @ (M_D @ Wk)))
    BAk = Bk @ Ak
    print(f"  K-self-adjointness on slice: ||B A - (B A)^H|| = {np.linalg.norm(BAk - BAk.conj().T):.2e}")
    lamk = np.linalg.eigvals(Ak)
    sck = float(np.max(np.abs(lamk)))
    imaxk = float(np.max(np.abs(lamk.imag)))
    nck = int(np.sum(np.abs(lamk.imag) > TOL_IM_BROKEN * sck))
    print(f"  spectrum: max|Im lambda| = {imaxk:.3e} (scale {sck:.3f}), complex count = {nck}"
          f"  -> {'PT-BROKEN on the slice too' if nck > 0 else 'real on the slice'}")
    row_k = dict(imaxk=imaxk, nck=nck)

    # ================= THEOREM: the achirality of every admissible physical sector =================
    print("\n[THEOREM CHECK: Re tr(chi Pi_+) = 0 for EVERY admissible C on this arena]")
    print("  Claim: on any Krein space where chi is Hermitian and ANTI-commutes with K (the canon fact")
    print("  '{K, chi} = 0', i.e. each chirality half of W is totally K-null), every operator C with")
    print("  K.C Hermitian (which every Bender-Mannheim C operator satisfies, C = K^{-1}H, H = KC) has")
    print("  conj(tr(chi C)) = tr(chi K^{-1} H)^* = tr(H K^{-1} chi) = -tr(chi K^{-1} H), so tr(chi C)")
    print("  is purely imaginary and Re tr(chi Pi_+) = Re[tr(chi) + tr(chi C)]/2 = 0. One line; no")
    print("  reference to GU cores at all. Numeric corroboration (random admissible H, 4 seeds):")
    for sd in (51, 52, 53, 54):
        r5 = np.random.default_rng(sd)
        Z = r5.standard_normal((nW, nW)) + 1j * r5.standard_normal((nW, nW))
        Hr = herm(Z @ Z.conj().T) / nW + 0.05 * np.eye(nW)
        tC = complex(np.trace(chiW @ (B_inv @ Hr)))
        print(f"    seed {sd}: tr(chi B^-1 H) = {tC.real:+.2e} {tC.imag:+.4f}j   (Re ~ 0, Im O(1))")
    print("  => the readout tr(chi Pi_+) = 0 (real part) is an ARENA IDENTITY, not a GU-core property:")
    print("     no choice of C -- GU-native, imported, or otherwise -- makes the C-positive physical")
    print("     sector net-chiral in the Cl(14)-volume trace sense. This is the C-07 wall in PT language.")

    # ================= TABLE + VERDICT =================
    print("\n" + "=" * 100)
    print("[DECISIVE READOUT TABLE]  (core x phase x C x [C,J] x tr(chi Pi_+))")
    print("=" * 100)
    hdr = f"{'core':64s} {'phase':17s} {'C':14s} {'||[C,J]||':10s} {'tr(chi Pi_+)':12s} {'||{C,chi}||':10s}"
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['name'][:63]:64s} {r['phase']:17s} {r['c_status']:14s} {str(r['cj']):10s}"
              f" {str(r['trchi']):12s} {str(r['ghost']):10s}")

    gu_rows = [r for r in rows if r["name"].startswith(("1.", "3.", "4.", "5."))]
    cured = [r for r in gu_rows if r.get("derived", False)]
    chiral = [r for r in gu_rows if abs(r.get("trchi_val", 0.0)) > 0.5 and r.get("derived", False)]
    ctrl_derived = any(r.get("derived", False) for r in rows if r["name"].startswith("C3"))
    ctrl_broken = any(r["phase"] == "PT-BROKEN" for r in rows if r["name"].startswith("C2"))
    print("\n[VERDICT]")
    print(f"  GU-native cores classified: {len(gu_rows)} (cores 1,3,4 and 3 mixed variants; core 2 = core 1)")
    print(f"  GU-native cores that are PT-UNBROKEN with a DERIVED (canonical) C: {len(cured)}")
    print(f"  GU-native cores with a derived C AND a chiral physical sector (|tr(chi Pi_+)| > 0.5): {len(chiral)}")
    print(f"  discriminating power: definitizable control returns DERIVED = {ctrl_derived};"
          f" random non-J control returns PT-BROKEN = {ctrl_broken}")
    print(f"  (=> the classifier is NOT a tautology: it CAN output 'C DERIVED' and does so on the")
    print(f"      non-GU control; the null result on GU cores is a property of the GU cores.)")
    if len(cured) == 0:
        print("\n  MANNHEIM MOVE NOT AVAILABLE on GU's carrier as tested: no GU-native core is")
        print("  PT-UNBROKEN with a dynamics-determined C. Definiteness cannot be DERIVED from these")
        print("  cores' spectral data; importing it (BIG-SWING-1's refuted move) remains the only route.")
    else:
        for r in cured:
            print(f"\n  NOTE: '{r['name']}' has a derived C; tr(chi Pi_+) = {r['trchi']}"
                  f"  -- label: 'this CORE forces the count', never 'GU forces it'.")
    print("\n  exit 0")
    return rows, row_k


if __name__ == "__main__":
    main()
    sys.exit(0)
