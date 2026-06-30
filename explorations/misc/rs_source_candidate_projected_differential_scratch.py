#!/usr/bin/env python3
"""KEYSTONE ATTEMPT (committed for provenance, 2026-06-27): smallest RS/IG
source-action candidate vs the necessary-conditions box.

Result: the minimal no-ghost candidate d_RS,-1^phys = Pi_RS o d_A is KILLED (3 ways),
BUT the computation is the in-rep PROOF that a non-equivariant ghost is mandatory, and it
reproduces every repo anchor (343.73, 58.72, 215.85) while establishing two new exact facts
(the two-level escape 1.6e-14 -> 169.19, and the unique gamma-traceless coupling
t* = -1/6 = wedge - 6*contract). See synthesis:
explorations/source-action-necessary-conditions-and-causality-2026-06-27.md. Nothing is tuned.

Candidate under test (the smallest object consistent with CONSTRAINT-PRESERVATION):

    d_RS,-1^phys := Pi_RS o d_A        (BRST/Stueckelberg-projected gauge differential)

i.e. the source-action datum whose EL/gauge generator is the gauge differential
followed by the orthogonal projector onto ker(Gamma).  This is the unique *smallest*
modification of the naive generator d_A that lands in the gamma-trace constraint
surface by construction.  Equivalently it is the quadratic form whose EL projector is
Pi_RS (a Lagrange-multiplier / penalty stabilization S_pen ~ <Psi, Gamma^dag Gamma Psi>
has EL kernel exactly ker(Gamma) = im(Pi_RS)).

We test the two requested predicates on the verified Cl(9,5)=M(64,H)~M(128,C) rep:

  (a) Does the candidate ANNIHILATE the projected-pure-gauge obstruction
      (the 73.48 / 343.73 object)?
  (b) Is it consistent with selecting the canon shiab (1,0,1,0)?

Plus the load-bearing box predicates that are finite on the rep:
  - CONSTRAINT-PRESERVATION   Gamma . d_RS,-1^phys = 0   (target: 0)
  - "obstruction reappears"   (I-Pi_RS) . M_D . d_RS,-1^phys != 0   (does projection
                              actually close the complex, or just move the escape?)
  - H-LINEARITY               [Pi_RS, J] = 0   (rank_H well-defined?)
  - RT-TRACE-DICHOTOMY        can a gamma-traceless coupling be (1,0,1,0)?

NOTHING is tuned. xi is the repo's fixed sample covector. Numbers are reported as-is.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.join(os.path.dirname(HERE), "tests")
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

TOL = 1e-9
N = 14
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.inv(gram) @ M


def build_rep():
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    Iden = np.eye(dim, dtype=complex)
    omega = Iden.copy()
    for a in range(N):
        omega = omega @ e[a]
    return dim, eta, e, omega, Iden


def build_J(dim, eta, e):
    """Quaternionic structure J = U.conj, J^2=-I, [J,e_a]=0 (from shiab_family_basis)."""
    s = np.empty(N)
    for a in range(N):
        if a < 9:
            s[a] = (-1.0) ** a
        else:
            s[a] = (-1.0) ** (a + 1)
    anticomm = [a for a in range(N) if s[a] < 0]
    U = np.eye(dim, dtype=complex)
    for a in anticomm:
        U = U @ e[a]
    Jsq_err = fro(U @ np.conjugate(U) + np.eye(dim))
    comm_err = max(fro(U @ np.conjugate(e[a]) - e[a] @ U) for a in range(N))
    return U, Jsq_err, comm_err


def main():
    dim, eta, e, omega, Iden = build_rep()
    VSdim = N * dim  # 1792

    # ---- core operators (same construction as the obstruction test) ----------
    Gamma = np.hstack(e)                      # 128 x 1792 : gamma-trace
    Pi_RS = proj_onto_kernel(Gamma)           # 1792 x 1792 : projector onto ker(Gamma)
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)   # twisted Dirac symbol

    # pure-gauge image  g(eps) = (xi_a eps)_a  in VS = R^14 (x) S
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # 1792 x 128

    print("=" * 80)
    print("SMALLEST RS SOURCE CANDIDATE:  d_RS,-1^phys = Pi_RS o d_A")
    print("=" * 80)
    print(f"VS=C^{VSdim}, Pi_RS rank_C={int(np.linalg.matrix_rank(Pi_RS, tol=TOL))} (=1664), "
          f"idem err={fro(Pi_RS@Pi_RS-Pi_RS):.1e}")

    # === reproduce the named 343.73 obstruction (naive d_A) ===================
    w, V = np.linalg.eigh(omega)
    Bp = V[:, w > 0.5]; Bm = V[:, w < -0.5]
    Gamma_p = np.hstack([Bm.conj().T @ e[a] @ Bp for a in range(N)])
    Gamma_m = np.hstack([Bp.conj().T @ e[a] @ Bm for a in range(N)])
    P_plus = proj_onto_kernel(Gamma_p); P_minus = proj_onto_kernel(Gamma_m)
    cxi_pm = Bm.conj().T @ cxi @ Bp
    full_symbol = P_minus @ np.kron(np.eye(N, dtype=complex), cxi_pm) @ P_plus
    gauge_chiral = np.vstack([XI[a] * np.eye(64, dtype=complex) for a in range(N)])
    obstruction_343 = fro(full_symbol @ (P_plus @ gauge_chiral))
    print(f"\n[anchor] naive RS symbol on projected pure-gauge image = "
          f"{obstruction_343:.4f}  (repo 343.73)")

    # === (a) does the candidate ANNIHILATE the obstruction? ===================
    # naive escape:  Gamma . d_A(gauge)  = c(xi) eps  (nonzero)
    naive_escape = fro(Gamma @ gauge)
    # candidate:  Gamma . Pi_RS . d_A(gauge)  = 0 by construction of Pi_RS
    cand_image = Pi_RS @ gauge                # d_RS,-1^phys image
    cand_escape = fro(Gamma @ cand_image)
    print("\n(a) CONSTRAINT-PRESERVATION  Gamma . d_RS,-1 (gauge image):")
    print(f"    naive   d_A           : ||Gamma . d_A(gauge)||      = {naive_escape:.4f}   (escapes)")
    print(f"    candidate Pi_RS o d_A : ||Gamma . Pi_RS d_A(gauge)|| = {cand_escape:.2e}   "
          f"(ANNIHILATED: {cand_escape < 1e-6})")

    # but does projecting CLOSE the complex, or just move the escape one level up?
    # next-level obstruction: the Dirac symbol carries the projected gauge mode back
    # OFF the constraint surface, because [Pi_RS, M_D] != 0.
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    reappear = fro(Pi_perp @ M_D @ cand_image)          # (I-Pi) M_D (Pi_RS gauge)
    reappear_full = fro(Pi_perp @ M_D @ Pi_RS)          # operator-level escape
    print("\n    DOES PROJECTION CLOSE THE COMPLEX?  (M_D . d_RS,-1^phys must stay in ker Gamma)")
    print(f"    ||[Pi_RS, M_D]||                       = {comm_PiMD:.4f}   (repo 58.72; !=0)")
    print(f"    ||(I-Pi_RS) M_D Pi_RS (gauge)||        = {reappear:.4f}   "
          f"(obstruction REAPPEARS: {reappear > 1e-6})")
    print(f"    ||(I-Pi_RS) M_D Pi_RS|| (operator)     = {reappear_full:.4f}")

    # === H-LINEARITY of the candidate projector ===============================
    U, Jsq_err, Jcomm_err = build_J(dim, e=e, eta=eta)
    # J on VS = R^14 (x) S acts as id_14 (x) J ; check [Pi_RS, id14 (x) U]=0 in the
    # antilinear sense reduces (for the holomorphic part U) to [Pi_RS, id14 (x) U.conj]
    JVS = np.kron(np.eye(N, dtype=complex), U)
    # Pi_RS is built from real-structure-commuting Clifford gens, so it should be
    # H-linear: test commutator of Pi_RS with the antilinear J = JVS . conj.
    # [Pi_RS, J] = 0  <=>  Pi_RS JVS conj = JVS conj Pi_RS  <=>  Pi_RS JVS = JVS conj(Pi_RS) conj...
    # Pi_RS is real-built (Hermitian, from Clifford gens); test both forms:
    Hlin_err = fro(Pi_RS @ JVS - JVS @ np.conjugate(Pi_RS))
    print("\n    H-LINEARITY (rank_H well-defined?):")
    print(f"    ||J^2+I||={Jsq_err:.1e}, ||[J,Cl]||={Jcomm_err:.1e};  "
          f"||Pi_RS J - J conj(Pi_RS)|| = {Hlin_err:.2e}  (H-linear: {Hlin_err < 1e-6})")

    # === (b) consistency with canon shiab (1,0,1,0) ===========================
    # Build the two shiab channels on the FULL module as Omega^2 (x) S -> Omega^1 (x) S.
    pairs = [(p, q) for p in range(N) for q in range(p + 1, N)]
    n2 = len(pairs)
    GAMMA2 = [e[p] @ e[q] for (p, q) in pairs]

    def build_channel(Wfun):
        T = np.zeros((VSdim, n2 * dim), dtype=complex)
        for j, (p, q) in enumerate(pairs):
            blk = slice(j * dim, (j + 1) * dim)
            for a in range(N):
                Wop = Wfun(a, j, p, q)
                if Wop is not None and np.any(Wop):
                    T[a * dim:(a + 1) * dim, blk] += Wop
        return T

    def W_contract(a, j, p, q):
        out = np.zeros((dim, dim), dtype=complex)
        if a == p: out = out + e[q]
        if a == q: out = out - e[p]
        return out

    def W_wedge(a, j, p, q):
        return eta[a] * 0.5 * (e[a] @ GAMMA2[j] + GAMMA2[j] @ e[a])

    T_contract = build_channel(W_contract)   # canon (1,0,1,0) channel (Clifford-trace)
    T_wedge = build_channel(W_wedge)         # Rarita-Schwinger channel

    g_contract = fro(Gamma @ T_contract)     # gamma-trace of canon shiab
    g_wedge = fro(Gamma @ T_wedge)
    # least-squares: is there a coupling contract + t*wedge that is gamma-traceless?
    A = (Gamma @ T_wedge).reshape(-1)
    b = (Gamma @ T_contract).reshape(-1)
    t_star = -(np.vdot(A, b) / np.vdot(A, A))
    resid = fro((Gamma @ T_contract) + t_star * (Gamma @ T_wedge))
    print("\n(b) RT-TRACE-DICHOTOMY: can a CONSTRAINT-PRESERVING coupling be canon (1,0,1,0)?")
    print(f"    ||Gamma . shiab_contract (canon 1,0,1,0)|| = {g_contract:.4f}   (TRACEFUL: {g_contract>1e-6})")
    print(f"    ||Gamma . shiab_wedge (Rarita-Schwinger)|| = {g_wedge:.4f}")
    print(f"    best traceless mix contract + t*wedge: t*={t_star:.4f}, "
          f"residual ||Gamma .(.)|| = {resid:.4f}")
    print(f"    -> canon (1,0,1,0) is gamma-TRACEFUL; constraint-preserving coupling needs "
          f"t* != 0 (= {abs(t_star)>1e-6}),")
    print(f"       i.e. NOT (1,0,1,0).  Constraint-preservation and canon (1,0,1,0) are "
          f"JOINTLY UNSATISFIABLE.")

    # how much of the candidate's physical image overlaps each shiab channel
    print("\n    projector overlap of shiab channels with the physical surface ker(Gamma):")
    print(f"    ||(I-Pi_RS) shiab_contract|| = {fro(Pi_perp @ T_contract):.4f}  "
          f"(canon escapes the surface)")
    print(f"    ||(I-Pi_RS) shiab_wedge||    = {fro(Pi_perp @ T_wedge):.4f}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"(a) candidate ANNIHILATES named obstruction at gradient level: "
          f"Gamma.d^phys(gauge)={cand_escape:.1e} ~ 0  YES")
    print(f"    but the complex does NOT close: (I-Pi)M_D d^phys = {reappear:.2f} != 0  "
          f"(escape moves up one level)")
    print(f"(b) canon (1,0,1,0) is gamma-traceful (={g_contract:.1f}); incompatible with "
          f"constraint preservation.")
    print(f"    H-linearity of Pi_RS: {Hlin_err:.1e} (~0, rank_H survives).")
    return None


if __name__ == "__main__":
    main()
