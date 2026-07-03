#!/usr/bin/env python3
"""OQ-RK1 (internal path #2): INDEPENDENT target-free rank certificate for the
composite  Pi_RS . E_+ . Pi_RS  on ONE common module of the actual Cl(9,5) =
M(64,H) carrier.

This is an independent re-run of the OQ-RK1 decisive test. It does NOT read from
or trust the prior hardening-pass scripts; it rebuilds Cl(9,5) with a DIFFERENT
concrete gamma realization (timelike-first signature placement + reversed
Jordan-Wigner tensor ordering) and computes the composite rank by THREE mutually
independent routes:

  (R1) SVD numerical rank of the Hermitian triple product Pi_RS . E_+ . Pi_RS ;
  (R2) Hermitian eigenvalue count of the same operator (different code path);
  (R3) a PURELY ANALYTIC subspace-dimension derivation
         rank_C( E_+ Pi_RS ) = dim E_+(ker T)
                             = dim(ker T) - dim( ker T  cap  ker E_+ )
       with every dimension read off by matrix_rank, no product formed.

Common module (the actual "1792-dim M(64,H) vector-spinor carrier"):
        V := R^14 (x) S ,   dim_C = 14 * 128 = 1792 .
  * Pi_RS = orthogonal projector onto ker of the gamma-trace map
            T : R^14 (x) S -> S ,  (psi_a) |-> sum_a c(e_a) psi_a  (i.e. gamma^a psi_a = 0).
  * E_+   = I_14 (x) (I + omega)/2 , chirality on the spinor factor.

HARD RULES obeyed (asserts are on STRUCTURE, never on the answer):
  * No division by, or insertion of, any target number (3, 8, 24, chi(K3)=24,
    Ahat(K3)=2, 16+8). The forbidden move rank_eff := 8/2 = 4 is NEVER executed.
  * rank_C -> rank_H halving is licensed ONLY by an executable quaternionic
    structure certificate: an explicit antilinear J with J^2 = -I commuting with
    every e_a (hence with T, Pi_RS, omega, E_+). If that certificate fails, only
    rank_C is reported.
The integer that comes out is whatever it is.
"""
from __future__ import annotations

import json
import numpy as np

TOL = 1e-9


def kron_list(mats):
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


def jw_gammas_reversed(n_pairs: int):
    """2*n_pairs Hermitian gammas, {G_a,G_b}=2 delta_ab, but with the tensor
    factors placed in the REVERSED order relative to oq_rk1_cl95_explicit_rep.py
    (identity factors on the left, s3 tail on the right). Different concrete
    matrices, same abstract algebra -> independent realization."""
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas = []
    for k in range(n_pairs):
        left = [I] * (n_pairs - 1 - k)   # reversed placement
        right = [s3] * k
        gammas.append(kron_list(left + [s1] + right))
        gammas.append(kron_list(left + [s2] + right))
    return gammas


def build_clifford_9_5_timelike_first():
    """Cl(9,5) with the 5 TIMELIKE (square -1) generators listed FIRST, then the
    9 spacelike ones. Signature multiset is identical to (9,5); only the labeling
    and the concrete matrices differ from the prior scripts."""
    n_pairs = 7
    dim = 2 ** n_pairs
    G = jw_gammas_reversed(n_pairs)
    # timelike first: 5 generators square to -1, then 9 square to +1
    eta = [-1] * 5 + [+1] * 9
    e = [1j * G[a] if eta[a] == -1 else G[a] for a in range(14)]
    Iden = np.eye(dim, dtype=complex)
    omega = Iden.copy()
    for a in range(14):
        omega = omega @ e[a]
    return e, eta, omega, dim


def rank_svd(M, tol=TOL):
    return int(np.linalg.matrix_rank(M, tol=tol))


def rank_herm_eig(M, tol=1e-7):
    Mh = 0.5 * (M + M.conj().T)
    w = np.linalg.eigvalsh(Mh)
    return int(np.sum(np.abs(w) > tol))


def build_quaternionic_J(e, dim):
    """Explicit antilinear J = M.conj with J^2 = -I commuting with every e_a.
    M = product of the generators e_a whose complex conjugate flips sign
    (i.e. those built from s2, which is pure-imaginary). Verified, not assumed."""
    # e_a conj = e_a  unless the s2 (imaginary) factor participates.
    # Determine sign delta_a with conj(e_a) = delta_a e_a directly from the matrix.
    deltas = []
    for a in range(14):
        ratio = np.conj(e[a])
        # e_a is +/- e_a under conj since each is a real or imaginary tensor word
        num = np.vdot(e[a].reshape(-1), ratio.reshape(-1))
        den = np.vdot(e[a].reshape(-1), e[a].reshape(-1))
        deltas.append(int(np.round((num / den).real)))
    anticomm_idx = [a for a in range(14) if deltas[a] == -1]
    M = np.eye(dim, dtype=complex)
    for a in anticomm_idx:
        M = M @ e[a]
    MconjM = M @ M.conj()
    scalar = MconjM[0, 0]
    s = np.sqrt(abs(scalar))
    if s > 0:
        M = M / s
    MconjM = M @ M.conj()
    info = {
        "deltas": deltas,
        "anticomm_idx": anticomm_idx,
        "normalized_MconjM_scalar": complex(MconjM[0, 0]),
        "is_quaternionic_minus_I": bool(np.max(np.abs(MconjM + np.eye(dim))) < 1e-7),
    }
    return M, info


def main():
    rep = {}
    e, eta, omega, dim = build_clifford_9_5_timelike_first()
    Iden = np.eye(dim, dtype=complex)

    # ---- structural asserts on the independent Clifford data ----
    max_cliff = 0.0
    for a in range(14):
        for b in range(14):
            anti = e[a] @ e[b] + e[b] @ e[a]
            expected = (2 * eta[a] if a == b else 0) * Iden
            max_cliff = max(max_cliff, float(np.max(np.abs(anti - expected))))
    assert max_cliff < TOL, f"Clifford relations failed: {max_cliff}"
    assert float(np.max(np.abs(omega @ omega - Iden))) < TOL, "omega^2 != I"
    assert float(np.max(np.abs(omega - omega.conj().T))) < TOL, "omega not Hermitian"
    rep["realization"] = "timelike-first, reversed Jordan-Wigner (independent of prior scripts)"
    rep["clifford_max_error"] = max_cliff
    rep["omega_sq_is_plus_I"] = True

    d14 = 14
    dV = d14 * dim
    assert dV == 1792
    rep["common_module"] = "V = R^14 (x) S"
    rep["common_module_dim_C"] = dV

    # E_+ on V
    E_plus_spin = 0.5 * (Iden + omega)
    E_plus = np.kron(np.eye(d14, dtype=complex), E_plus_spin)
    assert float(np.max(np.abs(E_plus @ E_plus - E_plus))) < TOL
    assert float(np.max(np.abs(E_plus - E_plus.conj().T))) < TOL
    rep["E_plus_rank_C"] = rank_svd(E_plus)

    # Pi_RS = projector onto ker T
    T = np.hstack([e[a] for a in range(d14)])   # 128 x 1792
    rank_T = rank_svd(T)
    rep["gamma_trace_rank_C"] = rank_T
    gram = T @ T.conj().T
    Pi_RS = np.eye(dV, dtype=complex) - T.conj().T @ np.linalg.inv(gram) @ T
    assert float(np.max(np.abs(Pi_RS @ Pi_RS - Pi_RS))) < TOL
    assert float(np.max(np.abs(Pi_RS - Pi_RS.conj().T))) < TOL
    assert float(np.max(np.abs(T @ Pi_RS))) < 1e-7
    rep["Pi_RS_rank_C"] = rank_svd(Pi_RS)

    # ---- quaternionic-structure certificate ----
    M, jinfo = build_quaternionic_J(e, dim)
    MconjM = M @ M.conj()
    j_sq_is_minus_I = bool(np.max(np.abs(MconjM + np.eye(dim))) < 1e-7)
    rng = np.random.default_rng(12345)
    xr = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
    antilin_err = float(np.max(np.abs((M @ np.conj(1j * xr)) + 1j * (M @ np.conj(xr)))))
    comm_e = max(float(np.max(np.abs(M @ e[a].conj() - e[a] @ M))) for a in range(14))
    comm_omega = float(np.max(np.abs(M @ omega.conj() - omega @ M)))
    halving_certified = bool(
        j_sq_is_minus_I and comm_e < 1e-6 and comm_omega < 1e-6 and antilin_err < 1e-9
    )
    rep["J_certificate"] = {
        "J_squared_is_minus_I": j_sq_is_minus_I,
        "antilinearity_error": antilin_err,
        "commutes_with_e_a_error": comm_e,
        "commutes_with_omega_error": comm_omega,
        "halving_certified": halving_certified,
        **{k: jinfo[k] for k in ("anticomm_idx", "is_quaternionic_minus_I")},
    }

    # ==== THE decisive composite, THREE independent routes ====
    # (R1) SVD rank of the triple product
    composite = Pi_RS @ E_plus @ Pi_RS
    assert float(np.max(np.abs(composite - composite.conj().T))) < TOL
    r_svd = rank_svd(composite)
    # (R2) Hermitian eigenvalue count
    r_eig = rank_herm_eig(composite)
    # (R3) analytic subspace dimensions, no triple product:
    #   rank(E_+ Pi_RS) = dim E_+(ker T) = dim(ker T) - dim(ker T ∩ ker E_+).
    dim_kerT = dV - rank_T
    ker_Eplus = np.kron(np.eye(d14, dtype=complex), 0.5 * (Iden - omega))  # R^14 (x) S^-
    # intersection dim: ker T ∩ range(E_-) = ker( T restricted to range E_- ).
    # Build orthonormal basis of range(E_-) and restrict T to it.
    w, Vv = np.linalg.eigh(ker_Eplus)
    B_minus = Vv[:, w > 0.5]                    # 1792 x 896 basis of R^14 (x) S^-
    T_on_minus = T @ B_minus                    # 128 x 896
    dim_inter = B_minus.shape[1] - rank_svd(T_on_minus)
    r_analytic = dim_kerT - dim_inter

    rep["composite_rank_C_svd"] = r_svd
    rep["composite_rank_C_herm_eig"] = r_eig
    rep["composite_rank_C_analytic"] = r_analytic
    rep["dim_kerT"] = dim_kerT
    rep["dim_kerT_cap_kerEplus"] = dim_inter
    assert r_svd == r_eig == r_analytic, f"routes disagree: {r_svd},{r_eig},{r_analytic}"

    if halving_certified:
        assert r_svd % 2 == 0, "J certified but rank_C odd -- contradiction"
        rep["composite_rank_H"] = r_svd // 2
    else:
        rep["composite_rank_H"] = "NOT_CERTIFIED_report_rank_C_only"

    rep["returns_4_or_8"] = bool(r_svd in (4, 8) or rep["composite_rank_H"] in (4, 8))
    rep["depends_on_target_import"] = False

    print("=" * 78)
    print("OQ-RK1 (internal path #2) INDEPENDENT composite rank on Cl(9,5)=M(64,H)")
    print("=" * 78)
    print(f"realization : {rep['realization']}")
    print(f"common module V = R^14 (x) S, dim_C = {dV}")
    print(f"Clifford ok (err {max_cliff:.1e}); omega^2=+I ok")
    print(f"E_+ rank_C = {rep['E_plus_rank_C']}; T rank_C = {rank_T} (surj={rank_T==128});"
          f" Pi_RS rank_C = {rep['Pi_RS_rank_C']}")
    print("-" * 78)
    print("QUATERNIONIC CERTIFICATE J = M.conj:")
    print(f"  J^2=-I: {j_sq_is_minus_I}; antilin err {antilin_err:.1e};"
          f" [J,e_a] err {comm_e:.1e}; [J,omega] err {comm_omega:.1e}")
    print(f"  halving CERTIFIED: {halving_certified}")
    print("-" * 78)
    print(f"rank_C route R1 (SVD triple product)     = {r_svd}")
    print(f"rank_C route R2 (Hermitian eigen-count)  = {r_eig}")
    print(f"rank_C route R3 (analytic subspace dims) = {r_analytic}"
          f"  (= {dim_kerT} - {dim_inter})")
    print(f"rank_H (= rank_C/2, certified)           = {rep['composite_rank_H']}")
    print("-" * 78)
    print(f"Does composite return 4 or 8? -> {rep['returns_4_or_8']}")
    print("Forbidden 8/Ahat(K3)=4 division: NOT EXECUTED.")
    print("=" * 78)
    print("\nMACHINE JSON:")
    print(json.dumps(rep, indent=2, default=str))
    return rep


if __name__ == "__main__":
    main()
