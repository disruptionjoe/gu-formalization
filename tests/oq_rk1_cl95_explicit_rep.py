#!/usr/bin/env python3
"""OQ-RK1 anchor: explicit Cl(9,5) = M(64,H) representation.

Purpose
-------
The decisive OQ-RK1 test asks for the TARGET-INDEPENDENT quaternionic rank
    rank_H( Pi_RS . E_+ . Pi_RS )   in M(64,H)
which would return 4 (=> 3 generations) or 8 (=> 4 generations, Candidate B).

This script does NOT claim to compute that decisive number, because the repo
does not pin down Pi_RS (or E_RS^eff) as a concrete operator on S = H^64
(see the spec in explorations/oq-rk1-rs-rank-attempt-2026-06-26.md).

What it DOES do, for the first time in the repo, is build an EXPLICIT complex
128x128 representation of Cl(9,5) (= M(64,H) complexified to M(128,C)) and
verify, by actual matrix computation, the two quantities in the OQ-RK1
expression that ARE algebraically well-defined:

  (1) E_+  : the chirality projector (1+omega)/2, rank_C = 64  -> rank_H = 32.
  (2) Pi_RS^raw : the raw 14D gamma-trace kernel on the positive-chiral
      vector-spinor space, rank_C(ker) = 832 -> rank_H = 416.

Neither 32 nor 416 is 4 or 8. That is the point: the gap between the raw,
well-defined object (416_H) and the desired effective rank (4 or 8) is exactly
the missing physical/BRST quotient + K-theory symbol class + H-trace + ch_2(F)
+ Y14->K3 bridge that the certificate files flag as UNDERDEFINED.

H-rank convention: M(64,H) (x)_R C = M(128,C); an H-linear idempotent of
H-rank r has complex rank 2r. So rank_H = rank_C / 2 for H-linear projectors.
"""

from __future__ import annotations

import numpy as np

TOL = 1e-9


def kron_list(mats):
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


def jordan_wigner_gammas(n_pairs: int):
    """2*n_pairs Hermitian gamma matrices of size 2**n_pairs, {G_a,G_b}=2 delta_ab."""
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas = []
    for k in range(n_pairs):
        # G_{2k+1} = s3^{(x)k} (x) s1 (x) I^{(x)(n-1-k)}
        # G_{2k+2} = s3^{(x)k} (x) s2 (x) I^{(x)(n-1-k)}
        left = [s3] * k
        right = [I] * (n_pairs - 1 - k)
        gammas.append(kron_list(left + [s1] + right))
        gammas.append(kron_list(left + [s2] + right))
    return gammas


def main():
    report = {}
    n_pairs = 7  # 14 generators, dimension 2^7 = 128
    dim = 2 ** n_pairs
    G = jordan_wigner_gammas(n_pairs)
    assert len(G) == 14 and G[0].shape == (dim, dim)

    # Signature (9,5): first 9 square to +1 (e_a = G_a), last 5 square to -1 (e_a = i G_a).
    eta = [+1] * 9 + [-1] * 5
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(14)]

    # Verify Clifford relations {e_a, e_b} = 2 eta_ab I.
    Iden = np.eye(dim, dtype=complex)
    max_cliff_err = 0.0
    for a in range(14):
        for b in range(14):
            anti = e[a] @ e[b] + e[b] @ e[a]
            expected = (2 * eta[a] if a == b else 0) * Iden
            max_cliff_err = max(max_cliff_err, np.max(np.abs(anti - expected)))
    report["clifford_max_error"] = float(max_cliff_err)
    report["clifford_ok"] = bool(max_cliff_err < TOL)

    # Volume form omega = e_0 e_1 ... e_13.
    omega = Iden.copy()
    for a in range(14):
        omega = omega @ e[a]
    omega_sq_err = float(np.max(np.abs(omega @ omega - Iden)))
    report["omega_squared_minus_I_error"] = omega_sq_err
    report["omega_squared_is_plus_I"] = bool(omega_sq_err < TOL)
    report["omega_hermitian_error"] = float(np.max(np.abs(omega - omega.conj().T)))
    report["omega_trace"] = complex(np.trace(omega))

    # Chirality projector E_+ = (I + omega)/2.
    E_plus = 0.5 * (Iden + omega)
    E_minus = 0.5 * (Iden - omega)
    report["E_plus_idempotent_error"] = float(np.max(np.abs(E_plus @ E_plus - E_plus)))
    report["E_plus_rank_C"] = int(np.linalg.matrix_rank(E_plus, tol=TOL))
    report["E_plus_rank_H"] = report["E_plus_rank_C"] / 2.0
    report["E_plus_trace"] = complex(np.trace(E_plus))

    # Orthonormal bases for S^+ and S^- (omega is Hermitian, eigenvalues +/-1).
    w, V = np.linalg.eigh(omega)
    Bplus = V[:, w > 0.5]    # 128 x 64
    Bminus = V[:, w < -0.5]  # 128 x 64
    report["Splus_dim_C"] = int(Bplus.shape[1])
    report["Sminus_dim_C"] = int(Bminus.shape[1])

    # Confirm each c(e_a) maps S^+ -> S^- (anticommutes with omega):
    # B_plus^dag e_a B_plus should vanish.
    max_pp = 0.0
    for a in range(14):
        block_pp = Bplus.conj().T @ e[a] @ Bplus
        max_pp = max(max_pp, float(np.max(np.abs(block_pp))))
    report["c_maps_Splus_to_Sminus_max_diagonal_block"] = max_pp
    report["chirality_flip_ok"] = bool(max_pp < TOL)

    # Raw 14D gamma-trace map on positive-chiral vector-spinors:
    #   Gamma^{14D}|_+ : (R^14) (x) S^+ -> S^-,  (xi_a, psi) |-> sum_a xi_a c(e_a) psi
    # As a 64 x (14*64) complex matrix: blocks B_minus^dag e_a B_plus.
    blocks = [Bminus.conj().T @ e[a] @ Bplus for a in range(14)]  # each 64x64
    Gamma14 = np.hstack(blocks)  # 64 x 896
    rk = int(np.linalg.matrix_rank(Gamma14, tol=TOL))
    report["gamma_trace_domain_dim_C"] = int(Gamma14.shape[1])      # 896
    report["gamma_trace_target_dim_C"] = int(Gamma14.shape[0])      # 64
    report["gamma_trace_rank_C"] = rk                               # expect 64 (surjective)
    report["gamma_trace_surjective"] = bool(rk == 64)
    report["raw_RS_kernel_rank_C"] = int(Gamma14.shape[1] - rk)     # 896 - 64 = 832
    report["raw_RS_kernel_rank_H"] = (Gamma14.shape[1] - rk) / 2.0  # 416

    # --- print ---
    print("=" * 78)
    print("OQ-RK1 anchor: explicit Cl(9,5) = M(64,H) ~ M(128,C) representation")
    print("=" * 78)
    print(f"dimension_C = {dim}  (= 2^7; M(64,H) complexified)")
    print(f"Clifford {{e_a,e_b}}=2 eta_ab : ok={report['clifford_ok']} "
          f"(max err {report['clifford_max_error']:.2e})")
    print(f"omega^2 = +I : {report['omega_squared_is_plus_I']} "
          f"(err {report['omega_squared_minus_I_error']:.2e}); "
          f"tr(omega)={report['omega_trace'].real:.3f}")
    print()
    print("OPERATOR (1) E_+ = (I+omega)/2  [the chirality / E-block projector]:")
    print(f"  idempotent err = {report['E_plus_idempotent_error']:.2e}")
    print(f"  rank_C(E_+) = {report['E_plus_rank_C']}  ->  rank_H(E_+) = {report['E_plus_rank_H']}")
    print(f"  (this is the ONLY pinned-down factor in Pi_RS.E_+.Pi_RS; rank_H = 32, exact)")
    print()
    print("OPERATOR (2) Pi_RS^raw via 14D gamma-trace kernel on S^+ vector-spinors:")
    print(f"  c(e_a): S^+ -> S^- for all a : {report['chirality_flip_ok']} "
          f"(max diag block {report['c_maps_Splus_to_Sminus_max_diagonal_block']:.2e})")
    print(f"  Gamma^14|_+ : C^{report['gamma_trace_domain_dim_C']} -> "
          f"C^{report['gamma_trace_target_dim_C']}, rank_C={report['gamma_trace_rank_C']} "
          f"(surjective={report['gamma_trace_surjective']})")
    print(f"  rank_C(ker) = {report['raw_RS_kernel_rank_C']}  ->  "
          f"rank_H(ker) = {report['raw_RS_kernel_rank_H']}")
    print()
    print("KEY POINT:")
    print("  The raw RS object has rank_H = 416 (on the 896_H vector-spinor space),")
    print("  NOT 4 and NOT 8, and it lives in M(896,H) not M(64,H).")
    print("  The decisive 4-vs-8 number requires an EFFECTIVE/PHYSICAL projector")
    print("  E_RS^eff (gauge/BRST quotient + K-theory symbol + ch_2(F) + H-trace +")
    print("  Y14->K3 bridge) that is NOT specified anywhere in the repo. BLOCKED_NEEDS_SPEC.")
    print("=" * 78)
    return report


if __name__ == "__main__":
    main()
