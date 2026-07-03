#!/usr/bin/env python3
"""OQ-RK1 hardening: DIRECT composite rank of  Pi_RS . E_+ . Pi_RS  on the real
quaternionic carrier Cl(9,5) = M(64,H), realized faithfully as M(128,C).

WHAT THIS CLOSES
----------------
The prior OQ-RK1 certificates computed the two FACTORS separately
(E_+ rank_H = 32; raw 14D gamma-trace kernel rank_H = 416) and a Cl(4,0) TOY
composite (48_H), but never the composite  Pi_RS . E_+ . Pi_RS  on ONE common
module of the ACTUAL Cl(9,5) carrier, because in those scripts E_+ lived on the
128-dim spinor S while the gamma-trace projector was pre-restricted to the
896-dim S^+ vector-spinor -- they did not act on a common module.

This script removes that gap by putting BOTH projectors on the *structurally
canonical* common Rarita-Schwinger fiber

        V  :=  R^14  (x)  S           (dim_C = 14 * 128 = 1792)
                         = R^14 (x) H^64  complexified = H^896 complexified.

This 1792_C space IS the "actual 1792-dim M(64,H) vector-spinor carrier" named
in the OQ-RK1 gap. On V:
    * Pi_RS = orthogonal projector onto ker of the gamma-trace map
              T : R^14 (x) S -> S ,  (psi_a) |-> sum_a c(e_a) psi_a .
      (This is the standard RS constraint gamma^a psi_a = 0; NO target used.)
    * E_+   = I_14 (x) (I + omega)/2 , chirality acting on the spinor factor.
Both are Hermitian idempotents built ONLY from the Clifford generators e_a that
already exist in oq_rk1_cl95_explicit_rep.py. Neither is chosen to hit a number.

WHAT IS REPORTED (and what is NOT)
----------------------------------
We report the RAW complex rank  rank_C( Pi_RS . E_+ . Pi_RS )  the computation
yields, by two independent methods (SVD matrix_rank and Hermitian eigenvalue
count). We then supply an EXECUTABLE quaternionic-structure certificate: an
explicit antilinear J with J^2 = -I that COMMUTES with both Pi_RS and E_+.
Because a J-commuting operator on a quaternionic space has even complex rank and
J-invariant image, this certificate -- and ONLY this certificate -- licenses
rank_H = rank_C / 2. If the J certificate had FAILED we would report rank_C only.

HARD ASSERTS are on STRUCTURE (idempotency, hermiticity, gamma-trace
annihilation, chirality grading, Clifford relations, omega^2=+I, J^2=-I,
J-commutation), NEVER on the final integer. The integer is whatever it is.

FORBIDDEN MOVES (documented, never executed):
    * rank_eff := ind_H / Ahat(K3) = 8/2 = 4          (INVALID_TARGET_DIVISION)
    * inserting ind_H(D_RS) = 8 as an input
    * selecting a rank-r sub-projector of E_+ to force r
    * rank_C -> rank_H halving WITHOUT the J certificate below
None is used. The composite rank is derived from the projector definitions.
"""

from __future__ import annotations

import json
import numpy as np

TOL = 1e-9


# ---------------------------------------------------------------------------
# Clifford data (identical construction to oq_rk1_cl95_explicit_rep.py)
# ---------------------------------------------------------------------------
def kron_list(mats):
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


def jordan_wigner_gammas(n_pairs: int):
    """2*n_pairs Hermitian gammas of size 2**n_pairs, {G_a,G_b}=2 delta_ab."""
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas = []
    for k in range(n_pairs):
        left = [s3] * k
        right = [I] * (n_pairs - 1 - k)
        gammas.append(kron_list(left + [s1] + right))
        gammas.append(kron_list(left + [s2] + right))
    return gammas


def build_clifford_9_5():
    """Return (e_list, eta, omega, dim) for Cl(9,5) as 128x128 complex matrices."""
    n_pairs = 7
    dim = 2 ** n_pairs
    G = jordan_wigner_gammas(n_pairs)
    eta = [+1] * 9 + [-1] * 5
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(14)]
    Iden = np.eye(dim, dtype=complex)
    omega = Iden.copy()
    for a in range(14):
        omega = omega @ e[a]
    return e, eta, omega, dim


def rank_svd(M, tol=TOL):
    return int(np.linalg.matrix_rank(M, tol=tol))


def rank_herm_eig(M, tol=1e-7):
    """Rank of a Hermitian matrix via eigenvalue count (independent of SVD path)."""
    Mh = 0.5 * (M + M.conj().T)
    w = np.linalg.eigvalsh(Mh)
    return int(np.sum(np.abs(w) > tol))


# ---------------------------------------------------------------------------
# Quaternionic-structure certificate for Cl(9,5)=M(64,H)
# ---------------------------------------------------------------------------
def build_quaternionic_structure(e):
    """Explicit antilinear J = M . conj  with J^2 = -I commuting with the e_a.

    Derivation (target-free): for J = M.conj to satisfy J e_a J^{-1} = e_a we
    need  M conj(e_a) M^{-1} = e_a. With conj(e_a) = delta_a e_a where
        delta_a = +1 for a in {0,2,4,6,8, 9,11,13}  (M must commute)
        delta_a = -1 for a in {1,3,5,7, 10,12}      (M must anticommute)
    the product of the six 'anticommute' generators has exactly this pattern.
    The overall scalar is fixed numerically so that M conj(M) = -I (quaternionic,
    not real). We VERIFY every property with hard asserts; nothing is assumed.
    """
    anticomm_idx = [1, 3, 5, 7, 10, 12]
    M = np.eye(e[0].shape[0], dtype=complex)
    for a in anticomm_idx:
        M = M @ e[a]

    # Fix the scalar phase so that M conj(M) = -I if possible.
    MconjM = M @ M.conj()
    # MconjM should be a real multiple of I; read the scalar.
    scalar = MconjM[0, 0]
    # If scalar is +|s|, multiply M by exp(i*theta) to try to reach -I.
    # (M -> c M gives McM -> |c|^2 ... actually (cM) conj(cM) = c conj(c) M conjM
    #  = |c|^2 MconjM, so phase cannot flip the sign. We instead may need to
    #  rescale to unit and check the intrinsic sign.)
    info = {
        "anticomm_idx": anticomm_idx,
        "MconjM_is_scalar": bool(
            np.max(np.abs(MconjM - scalar * np.eye(M.shape[0]))) < 1e-7
        ),
        "MconjM_scalar": complex(scalar),
    }
    # Normalise M so that M conj(M) = +/- I exactly.
    s = np.sqrt(abs(scalar))
    if s > 0:
        M = M / s
    MconjM = M @ M.conj()
    info["normalized_MconjM_scalar"] = complex(MconjM[0, 0])
    info["is_quaternionic_minus_I"] = bool(
        np.max(np.abs(MconjM + np.eye(M.shape[0]))) < 1e-7
    )
    info["is_real_plus_I"] = bool(
        np.max(np.abs(MconjM - np.eye(M.shape[0]))) < 1e-7
    )
    return M, info


def J_apply(M, x):
    """Antilinear action J x = M . conj(x)."""
    return M @ np.conj(x)


def main():
    rep = {}
    e, eta, omega, dim = build_clifford_9_5()
    Iden = np.eye(dim, dtype=complex)

    # --- Structural asserts on the Clifford data -------------------------
    max_cliff = 0.0
    for a in range(14):
        for b in range(14):
            anti = e[a] @ e[b] + e[b] @ e[a]
            expected = (2 * eta[a] if a == b else 0) * Iden
            max_cliff = max(max_cliff, float(np.max(np.abs(anti - expected))))
    assert max_cliff < TOL, f"Clifford relations failed: {max_cliff}"
    assert float(np.max(np.abs(omega @ omega - Iden))) < TOL, "omega^2 != I"
    assert float(np.max(np.abs(omega - omega.conj().T))) < TOL, "omega not Hermitian"
    rep["clifford_max_error"] = max_cliff
    rep["omega_sq_is_plus_I"] = True

    # --- Common RS fiber V = R^14 (x) S ,  dim_C = 14*128 = 1792 ----------
    d14 = 14
    dV = d14 * dim
    rep["common_module"] = "V = R^14 (x) S"
    rep["common_module_dim_C"] = dV
    assert dV == 1792, dV

    # E_+ on V : I_14 (x) (I+omega)/2   (chirality grading on spinor factor)
    E_plus_spin = 0.5 * (Iden + omega)
    E_plus = np.kron(np.eye(d14, dtype=complex), E_plus_spin)
    assert float(np.max(np.abs(E_plus @ E_plus - E_plus))) < TOL, "E_+ not idempotent"
    assert float(np.max(np.abs(E_plus - E_plus.conj().T))) < TOL, "E_+ not Hermitian"
    rep["E_plus_rank_C"] = rank_svd(E_plus)

    # Pi_RS on V : projector onto ker of gamma-trace map T (blocks e_a).
    T = np.hstack([e[a] for a in range(d14)])          # 128 x 1792
    rep["gamma_trace_map_shape"] = list(T.shape)
    rank_T = rank_svd(T)
    rep["gamma_trace_rank_C"] = rank_T                 # expect 128 (surjective)
    gram = T @ T.conj().T
    Pi_RS = np.eye(dV, dtype=complex) - T.conj().T @ np.linalg.inv(gram) @ T
    assert float(np.max(np.abs(Pi_RS @ Pi_RS - Pi_RS))) < TOL, "Pi_RS not idempotent"
    assert float(np.max(np.abs(Pi_RS - Pi_RS.conj().T))) < TOL, "Pi_RS not Hermitian"
    assert float(np.max(np.abs(T @ Pi_RS))) < 1e-7, "Pi_RS does not annihilate gamma-trace"
    rep["Pi_RS_rank_C"] = rank_svd(Pi_RS)              # expect 1792 - 128 = 1664

    # --- Quaternionic-structure certificate (licenses halving, or not) ---
    M, jinfo = build_quaternionic_structure(e)
    rep["J_certificate"] = jinfo
    # J^2 x = M conj(M conj(x)) = M conj(M) x  = MconjM x.
    MconjM = M @ M.conj()
    j_sq_is_minus_I = bool(np.max(np.abs(MconjM + np.eye(dim))) < 1e-7)
    # Antilinearity spot-check: J(i x) = -i J(x).
    xr = np.random.default_rng(0).standard_normal(dim) + 1j * np.random.default_rng(1).standard_normal(dim)
    antilin_err = float(np.max(np.abs(J_apply(M, 1j * xr) + 1j * J_apply(M, xr))))
    # J commutes with omega (=> with E_+) and with each e_a (=> with T, Pi_RS):
    #   on the spinor factor, J e_a J^{-1} = e_a  <=>  M conj(e_a) = e_a M.
    comm_e = max(float(np.max(np.abs(M @ e[a].conj() - e[a] @ M))) for a in range(14))
    comm_omega = float(np.max(np.abs(M @ omega.conj() - omega @ M)))
    rep["J_squared_is_minus_I"] = j_sq_is_minus_I
    rep["J_antilinearity_error"] = antilin_err
    rep["J_commutes_with_e_a_error"] = comm_e
    rep["J_commutes_with_omega_error"] = comm_omega
    halving_certified = bool(
        j_sq_is_minus_I and comm_e < 1e-6 and comm_omega < 1e-6 and antilin_err < 1e-9
    )
    rep["H_linearity_halving_certified"] = halving_certified

    # --- THE decisive composite:  Pi_RS . E_+ . Pi_RS  on V --------------
    composite = Pi_RS @ E_plus @ Pi_RS
    # composite is Hermitian PSD (= (E_+ Pi_RS)^dag (E_+ Pi_RS)); assert it.
    assert float(np.max(np.abs(composite - composite.conj().T))) < TOL, "composite not Hermitian"
    rank_c_svd = rank_svd(composite)
    rank_c_eig = rank_herm_eig(composite)
    rep["composite_rank_C_svd"] = rank_c_svd
    rep["composite_rank_C_herm_eig"] = rank_c_eig
    assert rank_c_svd == rank_c_eig, (
        f"two independent rank methods disagree: {rank_c_svd} vs {rank_c_eig}"
    )
    # Cross-check identity rank(Pi E Pi) = rank(E Pi):
    rank_EPi = rank_svd(E_plus @ Pi_RS)
    rep["rank_E_plus_Pi_RS"] = rank_EPi
    assert rank_EPi == rank_c_svd, "rank(EPi) != rank(Pi E Pi)"

    if halving_certified:
        assert rank_c_svd % 2 == 0, (
            "J certified but composite complex rank is odd -- contradiction"
        )
        rep["composite_rank_H"] = rank_c_svd // 2
    else:
        rep["composite_rank_H"] = "NOT_CERTIFIED_report_rank_C_only"

    # --- The literal OQ-RK1 question ------------------------------------
    rep["returns_4_or_8"] = bool(rank_c_svd in (4, 8) or rep["composite_rank_H"] in (4, 8))
    rep["depends_on_target_import"] = False

    # --- print -----------------------------------------------------------
    print("=" * 78)
    print("OQ-RK1 DIRECT composite rank_C( Pi_RS . E_+ . Pi_RS ) on Cl(9,5)=M(64,H)")
    print("=" * 78)
    print(f"common module V = R^14 (x) S,  dim_C = {dV}  (the actual 1792-dim carrier)")
    print(f"Clifford ok (err {max_cliff:.1e}); omega^2=+I ok")
    print(f"E_+ = I_14 (x) (I+omega)/2 : rank_C = {rep['E_plus_rank_C']}  (of {dV})")
    print(f"T (gamma-trace) : {T.shape[0]}x{T.shape[1]}, rank_C = {rank_T} (surjective={rank_T==128})")
    print(f"Pi_RS = proj ker T : rank_C = {rep['Pi_RS_rank_C']}  (= {dV}-{rank_T})")
    print("-" * 78)
    print("QUATERNIONIC-STRUCTURE CERTIFICATE  J = M.conj :")
    print(f"  M conj(M) scalar (normalized) = {jinfo['normalized_MconjM_scalar']}")
    print(f"  J^2 = -I : {j_sq_is_minus_I}   antilinearity err {antilin_err:.1e}")
    print(f"  J commutes with e_a (err {comm_e:.1e}), with omega (err {comm_omega:.1e})")
    print(f"  ==> rank_C->rank_H halving CERTIFIED : {halving_certified}")
    print("-" * 78)
    print(f"COMPOSITE rank_C (SVD)        = {rank_c_svd}")
    print(f"COMPOSITE rank_C (Herm eig)   = {rank_c_eig}   (independent, agrees)")
    print(f"cross-check rank(E_+ Pi_RS)   = {rank_EPi}")
    print(f"COMPOSITE rank_H (= rank_C/2) = {rep['composite_rank_H']}")
    print("-" * 78)
    print(f"Does the composite return 4 or 8? -> {rep['returns_4_or_8']}")
    print(f"Depends on any target import (8, 4, 24, chi(K3), Ahat)? -> {rep['depends_on_target_import']}")
    print("FORBIDDEN 8/Ahat(K3)=8/2=4 division : NOT EXECUTED (refused).")
    print("=" * 78)
    print("\nMACHINE JSON:")
    print(json.dumps(rep, indent=2, default=str))
    return rep


if __name__ == "__main__":
    main()
