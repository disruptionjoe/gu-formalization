#!/usr/bin/env python3
"""Computation B: IS the obstruction the commutator [Pi_RS, c.d*] = 343.73?

World-model claim under test (persona 39, world-model / MMO game-engine):

    "Take Phi := P o c o d*  with  P = Pi_RS (the constraint projector).
     Then d^2 = 0  iff  [Pi_RS, c o d*] = 0,
     and the repo's already-measured 343.73 IS the magnitude of exactly this
     finite, computable commutator on H^64."

This script builds, FROM FIRST PRINCIPLES in the explicit Cl(9,5)=M(64,H)~M(128,C)
representation (the same rep the repo's anchor uses), the objects:

    * Pi_RS  = orthogonal projector onto ker(Gamma), Gamma the 14D gamma-trace
               (the spin-3/2 irreducibility constraint  gamma^a psi_a = 0),
               built on the FULL vector-spinor space VS = R^14 (x) S = C^1792.
    * M_D    = id_14 (x) c(xi)  : the twisted Dirac principal symbol (this is the
               operator the repo's 343.73 code actually contracts with).
    * c.d*   = a literal "Clifford o codifferential" endomorphism of VS:
                 (c.d* psi)_b = c(e_b) ( sum_a xi_a psi_a ),
               i.e. contract the form index (codifferential symbol d*), then
               re-expand by Clifford multiplication.  Endo of VS.
    * shiab  = the canonical Clifford contraction Omega^2 (x) S -> Omega^1 (x) S
               (canon shiab-existence-cl95.md), kept DISTINCT from d* per canon SC1.

and then computes the ACTUAL commutator norms and compares to 343.73. Nothing is
tuned. xi is the repo's fixed sample covector. The decisive outputs are printed.

DISCIPLINE: every operator is built from the verified rep. No quantity is tuned to
hit 343.73, to force [.,.]=0, or to force a dimension. Actual numbers are reported.
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

TOL = 1e-9
# repo's fixed sample covector (same as rs_gu_phys_brst_specification.obstruction_cl95)
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def build_rep():
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = [+1] * 9 + [-1] * 5
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(14)]  # c(e_a), each 128x128
    Iden = np.eye(dim, dtype=complex)
    omega = Iden.copy()
    for a in range(14):
        omega = omega @ e[a]
    return e, omega, Iden, dim


def proj_onto_kernel(M: np.ndarray) -> np.ndarray:
    """Orthogonal projector onto ker(M) for an m x n matrix M (n x n result)."""
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.inv(gram) @ M


def fro(A: np.ndarray) -> float:
    return float(np.linalg.norm(A))


def main() -> dict:
    report = {}
    e, omega, Iden, dim = build_rep()  # dim = 128, S = C^128 (full module)
    n_form = 14
    VSdim = n_form * dim  # 1792 = R^14 (x) S

    # --- Gamma : full 14D gamma-trace on VS = R^14 (x) S  ---------------------
    # Gamma(psi) = sum_a c(e_a) psi_a  in S ;  as a 128 x 1792 matrix = [c(e_0) | ... | c(e_13)]
    Gamma = np.hstack(e)  # 128 x 1792
    rank_Gamma = int(np.linalg.matrix_rank(Gamma, tol=TOL))
    Pi = proj_onto_kernel(Gamma)  # 1792 x 1792, projector onto ker(Gamma) = Pi_RS
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi
    report["VS_dim_C"] = VSdim
    report["gamma_trace_rank_C"] = rank_Gamma
    report["Pi_RS_rank_C"] = int(np.linalg.matrix_rank(Pi, tol=TOL))
    report["Pi_RS_idempotent_err"] = fro(Pi @ Pi - Pi)
    report["Pi_RS_hermitian_err"] = fro(Pi - Pi.conj().T)
    report["Pi_RS_kills_constraint_err"] = fro(Gamma @ Pi)  # should be ~0

    # --- c(xi) : Dirac symbol on S ; M_D = id_14 (x) c(xi) : twisted Dirac symbol on VS
    cxi = np.zeros((dim, dim), dtype=complex)
    for a in range(n_form):
        cxi += XI[a] * e[a]
    M_D = np.kron(np.eye(n_form, dtype=complex), cxi)  # 1792 x 1792

    # --- c.d* : literal "Clifford o codifferential" endo of VS -----------------
    # d* (codifferential symbol): psi -> sum_a xi_a psi_a  in S  (128 x 1792)
    D_star = np.hstack([XI[a] * Iden for a in range(n_form)])  # 128 x 1792
    # c^* (Clifford co-expansion): s -> (c(e_b) s)_b  in VS     (1792 x 128)
    c_coexp = np.vstack([e[b] for b in range(n_form)])         # 1792 x 128
    c_dstar = c_coexp @ D_star                                  # 1792 x 1792 ;  block(b,a)=xi_a c(e_b)

    # --- pure form-sector codifferential-then-gradient (no Clifford), for contrast
    # (grad . div): psi_b -> xi_b ( sum_a xi_a psi_a )
    M_graddiv = np.kron(np.outer(XI, XI), Iden)  # 1792 x 1792, block(b,a)=xi_b xi_a I

    # === COMMUTATORS with Pi_RS ===============================================
    def commutator(M):
        return Pi @ M - M @ Pi

    results_ops = {}
    for name, M in [("M_D = id14 (x) c(xi)  [twisted Dirac symbol]", M_D),
                    ("c.d* = c(e_b)(sum xi_a psi_a)  [Clifford o codiff]", c_dstar),
                    ("grad.div (no Clifford)  [pure form codiff]", M_graddiv)]:
        C = commutator(M)
        D = Pi @ M @ Pi                      # compression to constraint surface
        results_ops[name] = {
            "norm_M": fro(M),
            "commutator_[Pi,M]_fro": fro(C),
            "commutator_is_zero": bool(fro(C) < 1e-6),
            "escape_block_||Pi_perp M Pi||": fro(Pi_perp @ M @ Pi),
            "compression_D=Pi M Pi_fro": fro(D),
            "D_squared_fro": fro(D @ D),     # the 'd^2=0' analog for the compressed op
        }
    report["operators"] = results_ops

    # === REPRODUCE 343.73 and show EXACTLY what it is =========================
    # The repo's number = || (Pi M_D Pi) |_{S+ -> S-}  applied to the gauge image ||.
    # Build it on the full module and confirm it equals the chiral-restricted repo value.
    w, V = np.linalg.eigh(omega)
    Bplus = V[:, w > 0.5]    # 128 x 64  (S^+)
    Bminus = V[:, w < -0.5]  # 128 x 64  (S^-)

    # chiral gamma-traces (as in the repo)
    Gamma_p = np.hstack([Bminus.conj().T @ e[a] @ Bplus for a in range(n_form)])  # 64x896  R14(x)S+ -> S-
    Gamma_m = np.hstack([Bplus.conj().T @ e[a] @ Bminus for a in range(n_form)])  # 64x896  R14(x)S- -> S+
    P_plus = proj_onto_kernel(Gamma_p)
    P_minus = proj_onto_kernel(Gamma_m)
    cxi_pm = Bminus.conj().T @ cxi @ Bplus  # 64x64 S+ -> S-
    full_symbol = P_minus @ np.kron(np.eye(n_form, dtype=complex), cxi_pm) @ P_plus
    gauge = np.vstack([XI[a] * np.eye(64, dtype=complex) for a in range(n_form)])  # 896x64
    symbol_on_gauge = full_symbol @ (P_plus @ gauge)
    repro_343 = fro(symbol_on_gauge)
    report["reproduced_343"] = repro_343

    # The 343.73 operator P_minus (I (x) cxi_pm) P_plus is the (S+ -> S-) block of
    # Pi M_D Pi. Verify the *block norm* (not restricted to gauge) and the
    # gauge-restricted number, to expose that 343.73 is a COMPRESSION-on-gauge,
    # not a commutator.
    block_full = full_symbol                      # the whole S+->S- compressed Dirac block
    report["compression_block_||P- M_D P+||_full"] = fro(block_full)
    report["compression_block_on_gauge_(=343)"] = repro_343
    # commutator restricted to the gauge image, for an apples-to-apples comparison
    Cd = commutator(M_D)
    # embed gauge (896x64 on S+ vector-spinors) into full VS to multiply by Cd:
    # full VS ordering is slot-major over S=C^128; S+ columns live in Bplus.
    # Build embed: R14(x)S+ (896) -> R14(x)S (1792)
    embedSplus = np.kron(np.eye(n_form, dtype=complex), Bplus)  # 1792 x 896
    gauge_full = embedSplus @ gauge                            # 1792 x 64
    report["||[Pi,M_D] . gauge_image||"] = fro(Cd @ (Pi @ gauge_full))

    # === shiab (Clifford contraction Omega^2 (x) S -> Omega^1 (x) S) ==========
    # Distinct from d* (canon SC1). Constraint-compatibility test: does shiab map
    # ker(Gamma^(2)) into ker(Gamma^(1))?  Measured WITHOUT forming the giant
    # Omega^2 projector, by probing random constraint-satisfying 2-form spinors.
    # shiab(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s.
    # On a 2-form alpha = sum_{i<j} alpha_{ij} e^i ^ e^j :
    #   iota_{e_a} alpha = sum_j alpha_{aj} e^j  (a 1-form), so
    #   shiab(alpha (x) s)_b = sum_a [coefficient of e^b in iota? ] ...
    # Implement on basis 2-forms e^i ^ e^j (i<j): iota_{e_a}(e^i^e^j) =
    #   delta_{ai} e^j - delta_{aj} e^i.  Then component b of output 1-form is e^a with a=b:
    #   shiab(e^i^e^j (x) s) = sum_a e^a (x) c(iota_{e_a}(e^i^e^j)) s
    #     = e^i (x) c(e^j) s  -  e^j (x) c(e^i) s.
    # So shiab maps basis (e^i^e^j (x) s) to slot-i: c(e^j)s, slot-j: -c(e^i)s.
    pairs = [(i, j) for i in range(n_form) for j in range(i + 1, n_form)]  # 91
    n2 = len(pairs)
    # Gamma^(2): the gamma-trace on Omega^2 (x) S, same contraction over the single
    # remaining... actually the irreducibility constraint on a 2-form-valued spinor
    # is gamma^a (alpha_{a.})  -> a 1-form-valued spinor; but the relevant
    # constraint-compatibility we test is whether shiab lands in ker(Gamma^(1)).
    rng = np.random.default_rng(0)
    # random 2-form spinor: coefficients alpha_{ij} (x) spinor s  -> represent as
    # vector in C^{n2 * 128}; build shiab as 1792 x (n2*128) sparse-ish matrix.
    Shiab = np.zeros((VSdim, n2 * dim), dtype=complex)
    for col, (i, j) in enumerate(pairs):
        blk = slice(col * dim, (col + 1) * dim)
        Shiab[i * dim:(i + 1) * dim, blk] += e[j]    # slot i gets c(e^j)
        Shiab[j * dim:(j + 1) * dim, blk] += -e[i]   # slot j gets -c(e^i)
    # Constraint-compatibility: norm of Gamma^(1) . shiab on the constraint-respecting
    # 2-form inputs.  Cheap, honest proxy: || Gamma . Shiab || (operator) and the
    # commutator-style quantity || (I-Pi) . Shiab || restricted appropriately.
    GammaShiab = Gamma @ Shiab  # 128 x (n2*128); zero iff shiab always lands in ker(Gamma^1)
    report["shiab"] = {
        "shiab_shape": list(Shiab.shape),
        "||Gamma^(1) . shiab||_fro": fro(GammaShiab),
        "shiab_image_in_ker(Gamma^1)?": bool(fro(GammaShiab) < 1e-6),
        "||(I-Pi).shiab||_fro": fro(Pi_perp @ Shiab),
        "note": ("shiab is the canon Clifford contraction; the projector Pi_RS does NOT "
                 "annihilate its image, so shiab != a constraint-surface endomorphism either."),
    }

    # === The 'd^2=0 iff [Pi,codiff]=0' logical test ===========================
    # Sufficiency: [Pi,M]=0  =>  Pi M = M Pi  =>  D=PiMPi=MPi, D^2 = M^2 Pi (still
    # not auto 0).  Necessity ('iff'): test whether D^2=0 can hold while [Pi,M]!=0.
    report["iff_test"] = {
        name: {
            "[Pi,M]_zero": d["commutator_is_zero"],
            "D^2_zero": bool(d["D_squared_fro"] < 1e-6),
            "iff_would_require_equal": d["commutator_is_zero"] == (d["D_squared_fro"] < 1e-6),
        }
        for name, d in results_ops.items()
    }
    # Machine-checked REFUTATION of the forward direction of the 'iff':
    # take M = Pi itself.  Then [Pi,M] = 0 (commutes exactly), yet the natural
    # constrained operator D = Pi.M.Pi = Pi has D^2 = Pi != 0.  So
    # "[Pi,M]=0  =>  D^2=0" is FALSE, hence the stated 'iff' is not a theorem.
    M_test = Pi
    C_test = commutator(M_test)
    D_test = Pi @ M_test @ Pi
    report["iff_forward_counterexample_M=Pi"] = {
        "||[Pi,Pi]||": fro(C_test),
        "commutes (lhs of iff true)": bool(fro(C_test) < 1e-9),
        "||(Pi.Pi.Pi)^2||": fro(D_test @ D_test),
        "D^2_is_zero (rhs of iff)": bool(fro(D_test @ D_test) < 1e-6),
        "iff_holds_here": bool((fro(C_test) < 1e-9) == (fro(D_test @ D_test) < 1e-6)),
        "verdict": ("[Pi,M]=0 but D^2 != 0  =>  forward direction of 'd^2=0 iff [Pi,codiff]=0' FAILS"),
    }

    # --- print ---------------------------------------------------------------
    print("=" * 84)
    print("Computation B: is the obstruction the commutator [Pi_RS, c.d*] = 343.73 ?")
    print("=" * 84)
    print(f"VS = R^14 (x) S = C^{VSdim};  Gamma rank_C={rank_Gamma} (surjective onto S=C^128)")
    print(f"Pi_RS rank_C={report['Pi_RS_rank_C']} (=1664);  idem err={report['Pi_RS_idempotent_err']:.1e}; "
          f"Gamma.Pi={report['Pi_RS_kills_constraint_err']:.1e}")
    print(f"\nReproduced repo number 343.73 -> {repro_343:.6f}")
    print("\nCOMMUTATORS [Pi_RS, M] (the world-model claim's object), Frobenius norm:")
    for name, d in results_ops.items():
        print(f"  {name}")
        print(f"      ||[Pi,M]||           = {d['commutator_[Pi,M]_fro']:.6f}   "
              f"(zero? {d['commutator_is_zero']})")
        print(f"      ||Pi_perp M Pi||     = {d['escape_block_||Pi_perp M Pi||']:.6f}   (off-surface escape)")
        print(f"      ||Pi M Pi|| (compr.) = {d['compression_D=Pi M Pi_fro']:.6f}")
        print(f"      ||(Pi M Pi)^2||      = {d['D_squared_fro']:.6f}   (the 'd^2=0' analog)")
    print(f"\n343.73 IS:  || (Pi M_D Pi)|_(S+->S-)  applied to gauge image ||")
    print(f"   full S+->S- compressed Dirac block ||P- M_D P+|| = "
          f"{report['compression_block_||P- M_D P+||_full']:.6f}")
    print(f"   ...restricted to the 64-col gauge image          = {repro_343:.6f}  (= 343.73)")
    print(f"   ||[Pi,M_D]||                                     = "
          f"{results_ops[list(results_ops)[0]]['commutator_[Pi,M]_fro']:.6f}  (the ACTUAL commutator)")
    print(f"   ||[Pi,M_D] . gauge_image||                       = {report['||[Pi,M_D] . gauge_image||']:.6f}")
    print("\nSHIAB (canon Clifford contraction, distinct from d*):")
    print(f"   ||Gamma^(1) . shiab||   = {report['shiab']['||Gamma^(1) . shiab||_fro']:.6f}  "
          f"(image in ker(Gamma^1)? {report['shiab']['shiab_image_in_ker(Gamma^1)?']})")
    print("\nMACHINE JSON:")
    print(json.dumps(report, indent=2, default=str))
    return report


if __name__ == "__main__":
    main()
