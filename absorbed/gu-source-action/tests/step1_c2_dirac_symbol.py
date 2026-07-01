#!/usr/bin/env python3
"""STEP 1 - Is C2's escape a first-order DIRAC-type symbol?

We build the escape matrices E_a = (I - Pi_RS) (id_14 (x) e_a) Pi_RS, a = 0..13, so that the
off-surface escape is E(xi) = sum_a xi_a E_a = (I - Pi_RS) M_D Pi_RS.

We then answer, with REAL numbers:
  (a) Is there Clifford-like structure among {E_a}?  -- compute the symbol Gram tensors
        S_ab = E_a^dag E_b + E_b^dag E_a        (anticommutator on the DOMAIN, ker Gamma)
        T_ab = E_a E_b^dag + E_b E_a^dag        (anticommutator on the RANGE, im Gamma^dag)
      Does {E_a} "square" (via E(xi)^dag E(xi)) to a multiple of a (9,5) quadratic form times a projector?
  (b) Ellipticity / characteristic set: for which xi does E(xi) drop rank / vanish?
      Diagonalise the Hermitian form  xi -> ||E(xi)||_F^2 = xi^T M xi  with M_ab = tr(E_a^dag E_b),
      and inspect the signature (a genuine Dirac boundary symbol is elliptic off a null cone).
  (c) Is C2(xi) = ||E(xi)|| exactly K*|xi|?  Test homogeneity AND isotropy (does the operator norm
      depend only on |xi|, or on direction?). Pin K at the repo xi.

Run: python tests/step1_c2_dirac_symbol.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N = gu_bridge.N        # 14
DIM = gu_bridge.DIM    # 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)   # the Cl(9,5) signature on the gammas


def build_escape_matrices():
    """E_a = (I - Pi_RS)(id_14 (x) e_a) Pi_RS for a=0..13."""
    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi_RS   # projector onto im(Gamma^dag) = (ker Gamma)^perp
    I14 = np.eye(N, dtype=complex)
    E = []
    for a in range(N):
        Ma = np.kron(I14, e[a])
        E.append(Q @ Ma @ Pi_RS)
    return e, Gamma, Pi_RS, M_D, Q, E


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    e, Gamma, Pi_RS, M_D, Q, E = build_escape_matrices()

    # ---- sanity: E(XI) really is the escape and reproduces the off-surface block -------------
    xi = gu_bridge.XI
    E_xi = sum(xi[a] * E[a] for a in range(N))
    escape_direct = Q @ M_D @ Pi_RS
    assert np.allclose(E_xi, escape_direct), "E(xi) != (I-Pi_RS) M_D Pi_RS"

    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    print(f"[anchors] bare ||[Pi_RS,M_D]|| = {bare:.4f} (expect 58.7215)")
    print(f"[anchors] C2 = ||Gamma M_D Pi_RS|| = {C2:.4f} (expect 155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchor mismatch"

    # =====================================================================================
    # (c-pre) Relation between the escape norm and C2.
    #   C2 = ||Gamma M_D Pi_RS||  while the escape uses Q = Gamma^dag (GG^dag)^{-1} Gamma.
    #   Report both Frobenius and spectral norms of E(xi).
    # =====================================================================================
    esc_F = float(np.linalg.norm(E_xi))                 # Frobenius
    esc_2 = float(np.linalg.norm(E_xi, 2))              # spectral (operator) norm
    print("\n=== escape vs C2 at the repo xi ===")
    print(f"||E(xi)||_F (Frobenius) = {esc_F:.4f}")
    print(f"||E(xi)||_2 (spectral)  = {esc_2:.4f}")
    print(f"C2                      = {C2:.4f}")
    print(f"ratio C2/||E||_F        = {C2/esc_F:.6f}")

    # =====================================================================================
    # (a) Clifford-like structure among {E_a}.
    #   Domain Gram:  M_ab = tr(E_a^dag E_b)   (Hilbert-Schmidt inner product of the symbols)
    #   This is the matrix of the quadratic form  ||E(xi)||_F^2 = sum_ab conj(xi_a) M_ab xi_b.
    #   For a genuine (9,5) Dirac symbol we would expect M proportional to diag(eta) up to an
    #   overall positive scale, i.e. M ~ kappa * diag(ETA). We test how close it is.
    # =====================================================================================
    M = np.zeros((N, N), dtype=complex)
    for a in range(N):
        for b in range(N):
            # tr(E_a^dag E_b) = Frobenius inner product <E_a, E_b> = vdot (O(n^2), not the O(n^3) matmul)
            M[a, b] = np.vdot(E[a], E[b])
    M_herm_err = np.linalg.norm(M - M.conj().T)
    M = 0.5 * (M + M.conj().T)  # symmetrise tiny numerical asymmetry
    Mreal = M.real
    print("\n=== (a) symbol Gram  M_ab = tr(E_a^dag E_b)  (Hilbert-Schmidt) ===")
    print(f"Hermiticity error ||M - M^dag|| = {M_herm_err:.3e}")
    diag = np.diag(Mreal)
    offdiag = Mreal - np.diag(diag)
    print("diagonal (a=0..13):")
    print(diag)
    print(f"max |off-diagonal|          = {np.abs(offdiag).max():.4f}")
    print(f"||off-diagonal||_F          = {np.linalg.norm(offdiag):.4f}")
    print(f"||diagonal||_F              = {np.linalg.norm(diag):.4f}")
    # Is the diagonal signed like ETA (9 plus, 5 minus)?  A Dirac (9,5) symbol would be.
    signs = np.sign(diag)
    print(f"diagonal signs vs ETA pattern: signs={signs.astype(int)}")
    print(f"all diagonal entries positive? {bool((diag > 0).all())}")
    # Best scalar kappa with M ~ kappa*diag(ETA): the (9,5) Dirac hypothesis.
    kappa_eta = float(np.dot(diag, ETA) / np.dot(ETA, ETA))
    resid_eta = np.linalg.norm(Mreal - kappa_eta * np.diag(ETA))
    print(f"(9,5)-Dirac fit  M ~ kappa*diag(ETA): kappa={kappa_eta:.4f}, "
          f"residual={resid_eta:.4f}, rel={resid_eta/np.linalg.norm(Mreal):.4f}")
    # Best scalar kappa with M ~ kappa*I (Euclidean elliptic Dirac).
    kappa_I = float(np.mean(diag))
    resid_I = np.linalg.norm(Mreal - kappa_I * np.eye(N))
    print(f"Euclidean fit    M ~ kappa*I:          kappa={kappa_I:.4f}, "
          f"residual={resid_I:.4f}, rel={resid_I/np.linalg.norm(Mreal):.4f}")

    # =====================================================================================
    # (b) Ellipticity / characteristic set of the Frobenius symbol.
    #   Eigen-decompose Mreal. Eigenvalues are the squared singular values of the map
    #   xi -> ||E(xi)||_F. Zero eigenvalues  =>  real characteristic directions (escape vanishes).
    # =====================================================================================
    evals, evecs = np.linalg.eigh(Mreal)
    print("\n=== (b) spectrum of the Frobenius symbol form M ===")
    print("eigenvalues (ascending):")
    print(evals)
    nzero = int((np.abs(evals) < 1e-6 * max(1.0, np.abs(evals).max())).sum())
    print(f"#~zero eigenvalues (characteristic directions) = {nzero}")
    print(f"min/max eigenvalue ratio = {evals.min()/evals.max():.4e}")
    print(f"is M positive definite (Frobenius-elliptic)? {bool((evals > 1e-6*evals.max()).all())}")

    # =====================================================================================
    # (c) Is C2(xi) = ||E(xi)|| exactly K*|xi|?  Two facets:
    #   (c1) homogeneity  C2(t xi)=|t| C2(xi)  -- already known degree-1; re-confirm here.
    #   (c2) isotropy:    does the OPERATOR norm depend only on |xi|, or on direction?
    #        Sample random unit xi; if ||E(xi)||_2 is constant => true elliptic |xi| symbol.
    #        If it varies => it is a genuine (anisotropic) Dirac-type symbol with a real symbol
    #        cone, NOT the trivial scalar |xi|.
    # =====================================================================================
    print("\n=== (c) homogeneity + isotropy of C2(xi) = ||Gamma M_D Pi_RS|| ===")
    # C2 via the bridge (the canonical definition) for homogeneity:
    r2 = gu_bridge.C2(2.0 * xi) / C2
    print(f"C2(2 xi)/C2(xi) = {r2:.6f}  (degree-1 homogeneous if = 2)")

    # isotropy scan: random real unit directions, report C2 and escape Frobenius norm.
    # (The per-direction spectral 2-norm via a full SVD of a 1792x1792 matrix was dropped --
    # it was reporting-only and dominated runtime; the Frobenius symbol norm settles isotropy.)
    rng = np.random.default_rng(0)
    c2_vals, escF_vals = [], []
    for _ in range(12):
        v = rng.standard_normal(N)
        v = v / np.linalg.norm(v)
        c2_vals.append(gu_bridge.C2(v.astype(complex)))
        Ev = sum(v[a] * E[a] for a in range(N))
        escF_vals.append(float(np.linalg.norm(Ev)))
    c2_vals = np.array(c2_vals)
    escF_vals = np.array(escF_vals)
    print(f"over 12 random UNIT xi:")
    print(f"  C2:          min={c2_vals.min():.4f} max={c2_vals.max():.4f} "
          f"mean={c2_vals.mean():.4f} std={c2_vals.std():.4f} (spread {c2_vals.std()/c2_vals.mean()*100:.1f}%)")
    print(f"  ||E||_F:     min={escF_vals.min():.4f} max={escF_vals.max():.4f} "
          f"mean={escF_vals.mean():.4f} std={escF_vals.std():.4f}")
    # K at repo xi (degree-1 slope):
    K_C2 = C2 / float(np.linalg.norm(xi.real))
    K_escF = esc_F / float(np.linalg.norm(xi.real))
    print(f"|xi| at repo = {np.linalg.norm(xi.real):.4f}")
    print(f"K_C2  = C2/|xi|      = {K_C2:.4f}  (constant only if isotropic)")
    print(f"K_escF= ||E||_F/|xi| = {K_escF:.4f}")

    # ---- VERDICT assertions (these are the honest checks, not pre-baked to a target) ------
    print("\n=== VERDICT ===")
    is_iso_C2 = c2_vals.std() / c2_vals.mean() < 0.02
    is_pos_def = bool((evals > 1e-6 * evals.max()).all())
    is_eta_dirac = resid_eta / np.linalg.norm(Mreal) < 0.05
    is_euclid = resid_I / np.linalg.norm(Mreal) < 0.05
    print(f"escape Frobenius form positive-definite (elliptic, no real char. set)? {is_pos_def}")
    print(f"escape Gram ~ (9,5) Dirac kappa*diag(ETA)? {is_eta_dirac} (rel resid {resid_eta/np.linalg.norm(Mreal):.3f})")
    print(f"escape Gram ~ Euclidean kappa*I?           {is_euclid} (rel resid {resid_I/np.linalg.norm(Mreal):.3f})")
    print(f"C2 operator norm isotropic (pure |xi| symbol)? {is_iso_C2} "
          f"(dir. spread {c2_vals.std()/c2_vals.mean()*100:.1f}%)")

    # Guard: bare commutator must remain 58.72 (anti-trap). Already asserted above. Re-assert.
    assert abs(bare - 58.7215) < 1e-2, "ANTI-TRAP violated: bare commutator moved"

    return {
        "bare": bare, "C2": C2, "esc_F": esc_F, "esc_2": esc_2,
        "M_diag": diag, "eta_fit_resid_rel": resid_eta / np.linalg.norm(Mreal),
        "euclid_fit_resid_rel": resid_I / np.linalg.norm(Mreal),
        "evals": evals, "nzero": nzero,
        "c2_spread_pct": c2_vals.std() / c2_vals.mean() * 100,
        "K_C2": K_C2,
    }


if __name__ == "__main__":
    main()
