#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W218 -- LEAN single-worker unification check: is the generation-count operator
        the SAME object as the unitarity grading eta_+ = eta * C?

METHOD (Clifford-contraction, the most directly executable route). In the
verified Cl(9,5) = M(64,H) representation (128-complex-dim spinor S, 14 gammas
e[a] of signature (9,5)), build the twisted-Rarita-Schwinger source re-grading

    R_src = Pi_RS * ( sum_{a in (6,4) fiber} c(e^a) M_D c(e_a) ) * Pi_RS

restricted to the explicit cross-chirality (+96,-96) carrier -- the j=1 triplet
carrier W (dim 192 = 3 x 64) that is the top-Casimir eigenspace of the self-dual
SU(2)+ acting on ker(Gamma) (the same carrier canon/core-theorems-symbolic-proof
and canon/external-by-structure name as the (+96,-96) Krein carrier). The
fiber-Clifford-trace (sum over the (6,4) fiber of c(e^a) M_D c(e_a)) is the
ultralocal algebraic pushforward standing in for the geometric pi_! that W201
calls undefined over the non-convex GL(4,R)/O(3,1) fiber.

  * M_D      = the RS Dirac symbol kron(I_14, c(xi)), c(xi)=sum xi[a] e[a] (W177/W203).
  * c(e^a)   = Clifford multiplication on the spinor factor, kron(I_14, e[a]);
               e^a = eta[a] e_a raises the fiber index.
  * Pi_RS    = projector onto ker(Gamma), Gamma = hstack(e) (gamma-trace map).
  * RS channel is FIXED by restricting to the ker-Gamma triplet carrier (the
    gamma-traceless / omega_1+omega_6 RS content, SHIAB-03); the Clifford-trace
    (S+) channel is carried as the pre-declared DISQUALIFYING control (Block F).

THE (+96,-96) CARRIER (built explicitly, not symbolic):
  omega_c  = chirality involution kron(I_14, omega_S) restricted to W, sig (96,96);
  K_c      = Krein form kron(diag(eta), K_S) restricted to W, sig (96,96),
             CROSS-CHIRALITY: K_c omega_c + omega_c K_c = 0 (machine zero).
  eta_+ = eta * C : the unitarity grading. eta = K_c; C = sign(K_c) is the
             C-operator (physical-vs-ghost grading, W173/W186); eta_+ = K_c C = |K_c|
             is positive-definite. C is chirality-odd and K-DEFINITE
             (sig(K_c C) = (192,0)) -- the "K-definite non-chirality" type. It also
             commutes with the Krein form ([C, K_c] = 0).

TWO TYPE READS (one-shot classification of R_src):
  chirality-commutation  [R_src, omega]   -> R_src is chirality-ODD ({R_src, omega}=0);
  Krein-adjointness      R_src^dag K_c +/- K_c R_src  -> R_src is K-SELF-adjoint.
  Then the numerically-STABLE discriminator (avoiding any ill-conditioned matrix-sign
  of the highly non-normal R_src) is the signature of the HERMITIAN matrix K_c R_src:
    K-DEFINITE   sig(K_c R_src) = (192,0)   -> eta_+ = eta*C type;
    K-NULL/indef sig(K_c R_src) = (96,96)   -> net index 0 -> vectorlike.

  TEST 1 (unification): is R_src = eta_+ = eta*C on the carrier (up to the
    C-positive / +1-eigenspace-of-K_c stabilizer)? Read from proportionality to
    C = sign(K_c), the sig(K_c R_src) type, and [R_src, K_c].
  TEST 2 (chiralize vs vectorlike): net chiral index chi = tr(omega * sign(R_src)).
    Because {R_src, omega} = 0 (machine-exact) and sign is odd,
    omega sign(R_src) omega = -sign(R_src), so tr(omega sign(R_src)) = 0 IDENTICALLY
    (core-theorems Theorem 3). Confirmed structurally: R_src is purely
    chirality-OFF-DIAGONAL (its ++ and -- chirality blocks vanish), the Theorem-3
    form D = [[0,B],[B',0]] with net chiral spectral flow 0.

RESULT (read off, not assumed):
    * TEST 1  -> DISTINCT: sig(K_c R_src) = (96,96) is K-NULL/indefinite, NOT the
                 C-operator's K-definite (192,0); R_src is Frobenius-ORTHOGONAL to
                 C = sign(K_c) (best-fit residual = full norm); and [R_src, K_c] != 0
                 while [C, K_c] = 0. So R_src is NOT the operator eta_+ = eta*C, and
                 is not even the same type. (Conditional on the RS-channel fixing;
                 robust across the fiber / all-14 / no-Pi / horizontal channels here.)
    * TEST 2  -> VECTORLIKE: chi = 0 (forced by {R_src, omega} = 0; confirmed by the
                 vanishing chirality-diagonal blocks). Channel-type-invariant.
                 Consistent with core-theorems Theorem 2 (linear Krein-isometric
                 operators conserve the net chiral index at 0) and with W201's
                 coherence lean (the count needs a SEPARATE Z/3 self-dual import).

HONESTY / SCOPE. Exploration grade. ULTRALOCAL (fiber-Clifford-trace stands in for
the geometric pi_!). This does NOT claim the nonlocal Z_U completion, the Z/3 count
VALUE, or any canon/verdict movement (bar(b)/H59 stay OPEN). It reports only the
unification bit (DISTINCT) and the chiralize/vectorlike bit (VECTORLIKE).

Cite: W201 (the two tests, R_src spec, eta_+=eta*C), W203 (source action, Schur
kernel, K_S), W177 (M_D, C2), W192 (explicit carrier, K-adjointness/chirality
read-off), canon/shiab-existence-cl95.md (SHIAB-03/04/05, RS vs Clifford-trace
channel), canon/core-theorems-symbolic-proof-RESULTS.md (the (+96,-96) carrier,
Theorems 2 and 3), tests/wave16/H39 (the 192=3x64 triplet carrier construction).

Deterministic; exit 0 iff all checks pass. Positive controls first.
    python -u tests/W218_lean_Rsrc_unification_check.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_GEN = os.path.join(_HERE, "generation-sector")
for _p in (_GEN, _HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import gen_sector_bridge as gb  # noqa: E402  verified Cl(9,5)=M(64,H) rep + anchors

N, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
I128 = np.eye(DIM, dtype=complex)
TOL = 1e-7
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""), flush=True)
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 92)
    print(title)
    print("=" * 92)


def sig_herm(M: np.ndarray, tol: float = 1e-6) -> tuple[int, int, int]:
    """(n_pos, n_neg, n_zero) of the Hermitian part of M."""
    w = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
    scale = max(1.0, float(np.max(np.abs(w))))
    return (int(np.sum(w > tol * scale)), int(np.sum(w < -tol * scale)),
            int(np.sum(np.abs(w) <= tol * scale)))


# ==============================================================================
def main() -> int:
    e = gb.gammas()

    section("A -- verified Cl(9,5) rep, spinor Krein form, chirality (positive controls)")
    cliff = max(float(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                - (2 * ETA[a] * I128 if a == b else 0.0))))
                for a in range(N) for b in range(N))
    check("A1 Cl(9,5) Clifford relations {e_a,e_b}=2 eta_ab (residual 0)", cliff < TOL, f"max={cliff:.1e}")

    K_S = e[0].copy()
    for a in range(1, 9):
        K_S = K_S @ e[a]                      # spinor Krein form K_S = e_0 e_1 ... e_8 (W192/W203)
    ks_herm = float(np.max(np.abs(K_S.conj().T - K_S)))
    ks_inv = float(np.max(np.abs(K_S @ K_S - I128)))
    check("A2 K_S is Hermitian, involutive, signature (64,64)",
          ks_herm < TOL and ks_inv < TOL and sig_herm(K_S) == (64, 64, 0),
          f"herm={ks_herm:.1e} sig={sig_herm(K_S)}")

    omega_S = I128.copy()
    for a in range(N):
        omega_S = omega_S @ e[a]              # chirality volume element
    om2 = float(np.max(np.abs(omega_S @ omega_S - I128)))
    check("A3 chirality omega_S^2 = I, signature (64,64)",
          om2 < TOL and sig_herm(omega_S) == (64, 64, 0), f"||om^2-I||={om2:.1e}")

    section("B -- the explicit (+96,-96) cross-chirality carrier (192 = 3 x 64 triplet)")
    Gamma = np.hstack(e)                       # 128 x 1792 gamma-trace map
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    ker_dim = int(round(np.trace(Pi).real))
    check("B1 ker(Gamma) has dimension 1664 (RS / gamma-traceless sector)", ker_dim == 1664, f"dim={ker_dim}")

    def sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    def lvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j], M[j, i] = 1, -1
        return M

    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]     # self-dual SU(2)+ planes (3 = dim Lambda^2_+)
    J = [np.kron(np.eye(N, dtype=complex), sgen(a, b) + sgen(c, d))
         + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in SD]
    w, V = np.linalg.eigh(Pi)
    Wk = V[:, w > 0.5]                          # orthonormal basis of ker(Gamma)
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = Wk.conj().T @ Cas @ Wk
    CasK = 0.5 * (CasK + CasK.conj().T)
    wc, Vc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in wc)
    carr = Wk @ Vc[:, np.abs(wc - top) < 1e-3]  # 1792 x 192 : the triplet carrier
    tdim = carr.shape[1]
    ortho = float(np.max(np.abs(carr.conj().T @ carr - np.eye(tdim))))
    check("B2 triplet carrier is the top-Casimir (j=1) eigenspace: dim 192 = 3 x 64, Casimir 8.0",
          tdim == 192 and abs(top - 8.0) < 1e-6 and tdim // 64 == 3 and ortho < TOL,
          f"dim={tdim}, Casimir={top}, ortho={ortho:.1e}")

    omega_c = carr.conj().T @ np.kron(np.eye(N, dtype=complex), omega_S) @ carr
    omega_c = 0.5 * (omega_c + omega_c.conj().T)
    oc2 = float(np.max(np.abs(omega_c @ omega_c - np.eye(tdim))))
    check("B3 carrier chirality omega_c^2 = I, signature (96,96) [W_+ = W_- = 96]",
          oc2 < TOL and sig_herm(omega_c) == (96, 96, 0), f"||om_c^2-I||={oc2:.1e} sig={sig_herm(omega_c)}")

    K_c = carr.conj().T @ np.kron(np.diag(ETA).astype(complex), K_S) @ carr
    K_c = 0.5 * (K_c + K_c.conj().T)
    cross = float(np.max(np.abs(K_c @ omega_c + omega_c @ K_c)))
    check("B4 carrier Krein form K_c: Hermitian, signature (96,96), CROSS-CHIRALITY "
          "(K_c omega_c + omega_c K_c = 0)",
          sig_herm(K_c) == (96, 96, 0) and cross < TOL, f"sig={sig_herm(K_c)}, ||{{K,om}}||={cross:.1e}")

    # the unitarity grading eta_+ = eta * C.  eta = K_c ; C = sign(K_c) (the C-operator).
    evk, Vk = np.linalg.eigh(K_c)
    Cop = Vk @ np.diag(np.sign(evk)) @ Vk.conj().T      # C-operator = sign(K_c)
    eta_plus = K_c @ Cop
    Cop_odd = float(np.max(np.abs(Cop @ omega_c + omega_c @ Cop)))
    Cop_Kcomm = float(np.max(np.abs(Cop @ K_c - K_c @ Cop)))
    check("B5 eta_+ = eta*C is positive-definite (192,0); C is chirality-ODD and K-DEFINITE "
          "(sig(K_c C)=(192,0)); [C, K_c] = 0 -> the 'K-definite non-chirality' (eta_+=eta*C) type",
          sig_herm(eta_plus) == (192, 0, 0) and Cop_odd < TOL and Cop_Kcomm < TOL,
          f"sig(eta_+)={sig_herm(eta_plus)}, {{C,om}}={Cop_odd:.1e}, [C,K]={Cop_Kcomm:.1e}")

    # ------------------------------------------------------------------
    section("C -- build R_src (twisted-RS fiber-Clifford-trace pushforward, RS channel)")
    HIDX = (0, 1, 2, 9)                          # (3,1) horizontal
    NIDX = tuple(i for i in range(N) if i not in HIDX)   # (6,4) fiber
    check("C0 (3,1) horizontal + (6,4) fiber split",
          len(HIDX) == 4 and int(sum(ETA[i] > 0 for i in NIDX)) == 6
          and int(sum(ETA[i] < 0 for i in NIDX)) == 4,
          f"fiber sig=({int(sum(ETA[i]>0 for i in NIDX))},{int(sum(ETA[i]<0 for i in NIDX))})")

    cxi = sum(gb.XI[a] * e[a] for a in range(N))           # c(xi), a single-gamma (Clifford-odd)
    M_D = np.kron(np.eye(N, dtype=complex), cxi)           # RS Dirac symbol (W177/W203)

    def cRS(a):
        return np.kron(np.eye(N, dtype=complex), e[a])     # Clifford mult on the spinor factor

    def build_R(fiber_indices, project: bool):
        S = sum(ETA[a] * cRS(a) @ M_D @ cRS(a) for a in fiber_indices)   # sum c(e^a) M_D c(e_a)
        if project:
            S = Pi @ S @ Pi
        return carr.conj().T @ S @ carr

    R_src = build_R(NIDX, project=True)          # RS channel: (6,4) fiber + Pi_RS
    check("C1 R_src is a nonzero 192x192 operator on the carrier", R_src.shape == (192, 192)
          and np.linalg.norm(R_src) > 1.0, f"||R_src||={np.linalg.norm(R_src):.3f}")

    # ------------------------------------------------------------------
    section("D -- TWO TYPE READS: chirality-commutation, Krein-adjointness, K-type discriminator")
    nR = np.linalg.norm(R_src)
    anti_om = float(np.linalg.norm(R_src @ omega_c + omega_c @ R_src)) / nR   # 0 => chirality-ODD
    comm_om = float(np.linalg.norm(R_src @ omega_c - omega_c @ R_src)) / nR
    check("D1 chirality-commutation: R_src is chirality-ODD ({R_src, omega} = 0; [R_src,omega] != 0)",
          anti_om < TOL and comm_om > 1.0, f"{{R,om}}/|R|={anti_om:.1e}, [R,om]/|R|={comm_om:.2f}")

    ksa = float(np.linalg.norm(R_src.conj().T @ K_c - K_c @ R_src)) / nR      # 0 => K-SELF-adjoint
    kasa = float(np.linalg.norm(R_src.conj().T @ K_c + K_c @ R_src)) / nR
    check("D2 Krein-adjointness: R_src is K-SELF-adjoint (R^dag K_c - K_c R = 0; the '+' residual != 0)",
          ksa < TOL and kasa > 1.0, f"R+K-KR/|R|={ksa:.1e}, R+K+KR/|R|={kasa:.2f}")

    # STABLE discriminator: K_c R_src is Hermitian (R_src K-self-adjoint); its signature classifies.
    KR = K_c @ R_src
    KR_herm = float(np.linalg.norm(KR - KR.conj().T)) / nR
    KR_sig = sig_herm(KR)
    check("D3 DISCRIMINATOR (stable): K_c R_src is Hermitian and sig(K_c R_src) = (96,96) -> R_src is "
          "K-NULL / K-INDEFINITE, NOT the C-operator's K-DEFINITE (192,0) at B5. => 'K-null-chirality' type",
          KR_herm < TOL and KR_sig == (96, 96, 0), f"K_c R Hermitian={KR_herm:.1e}, sig(K_c R)={KR_sig}")

    # STABLE Theorem-3 structure: R_src is purely chirality-OFF-DIAGONAL (++ and -- blocks vanish).
    ow, ov = np.linalg.eigh(omega_c)
    Wplus, Wminus = ov[:, ow > 0], ov[:, ow < 0]
    pp_blk = float(np.linalg.norm(Wplus.conj().T @ R_src @ Wplus)) / nR
    mm_blk = float(np.linalg.norm(Wminus.conj().T @ R_src @ Wminus)) / nR
    check("D4 Theorem-3 form: R_src's chirality-diagonal blocks vanish (R_src = [[0,B],[B',0]]) -> its "
          "positive/negative spectral subspaces are chirality-balanced -> net chiral spectral flow 0",
          pp_blk < TOL and mm_blk < TOL, f"++block/|R|={pp_blk:.1e}, --block/|R|={mm_blk:.1e}")

    # ------------------------------------------------------------------
    section("E -- TEST 1 (unification) and TEST 2 (chiralize vs vectorlike)")

    # TEST 1: R_src ?= eta_+ = eta*C, up to the C-positive (+1-eigenspace-of-K_c) stabilizer.
    c_fit = complex(np.trace(Cop.conj().T @ R_src) / np.trace(Cop.conj().T @ Cop))
    perp_res = float(np.linalg.norm(R_src - c_fit * Cop)) / nR
    R_Kcomm = float(np.linalg.norm(R_src @ K_c - K_c @ R_src)) / nR
    check("E1 TEST 1 -> DISTINCT: R_src is Frobenius-ORTHOGONAL to C=sign(K_c) (best-fit residual = full "
          "norm, coeff ~ 0); sig(K_c R_src)=(96,96) K-null != eta_+ (192,0) K-definite; and [R_src,K_c] != 0 "
          "while [C,K_c]=0. R_src is NOT eta_+ = eta*C (not even the same type).",
          perp_res > 0.99 and abs(c_fit) < 1e-6 and KR_sig == (96, 96, 0) and R_Kcomm > 1.0,
          f"R-perp-C residual={perp_res:.3f} (coeff={abs(c_fit):.1e}), [R,K_c]/|R|={R_Kcomm:.2f}")

    # TEST 2: net chiral index chi = tr(omega * sign(R_src)).  {R_src,omega}=0 (D1) => sign is odd under
    # omega => omega sign(R) omega = -sign(R) => tr(omega sign(R)) = 0 IDENTICALLY (core-theorems Thm 3).
    # (No ill-conditioned matrix-sign of the non-normal R_src is computed; the vanishing D4 blocks are the
    #  machine-exact structural witness that the net chiral spectral flow is 0.)
    check("E2 TEST 2 -> VECTORLIKE: chi = tr(omega*sign(R_src)) = 0, FORCED by {R_src,omega}=0 (D1) since "
          "sign is odd; structurally witnessed by the vanishing chirality-diagonal blocks (D4)",
          anti_om < TOL and pp_blk < TOL and mm_blk < TOL,
          "chi = 0 (theorem: chirality-odd operator has zero net chiral spectral flow)")

    # cross-check: the C-operator itself is index-0 on chirality (W201 coherence: operative but vectorlike).
    chiC = float(np.trace(omega_c @ Cop).real)
    check("E3 cross-check: the C-operator is itself chirality-index 0 (tr(omega*C)=0) -- 'operative but "
          "vectorlike' (W201); so even a literal unification would NOT have delivered a count",
          abs(chiC) < 1e-6, f"tr(omega*C)={chiC:.3e}")

    # ------------------------------------------------------------------
    section("F -- CONTROLS: channel-robustness (TEST 1 + TEST 2) incl. the Clifford-trace disqualifier")
    variants = [
        ("full Clifford-trace (all 14) + Pi_RS", build_R(tuple(range(N)), True)),
        ("(6,4) fiber, NO Pi (Clifford-trace ambient)", build_R(NIDX, False)),
        ("(3,1) horizontal + Pi_RS", build_R(HIDX, True)),
    ]
    for label, Rv in variants:
        nv = np.linalg.norm(Rv)
        av = float(np.linalg.norm(Rv @ omega_c + omega_c @ Rv)) / nv           # chirality-odd
        sv = sig_herm(K_c @ Rv)                                                # K-null discriminator
        ppb = float(np.linalg.norm(Wplus.conj().T @ Rv @ Wplus)) / nv
        mmb = float(np.linalg.norm(Wminus.conj().T @ Rv @ Wminus)) / nv
        cfit = complex(np.trace(Cop.conj().T @ Rv) / np.trace(Cop.conj().T @ Cop))
        pr = float(np.linalg.norm(Rv - cfit * Cop)) / nv
        check(f"F* same classification (DISTINCT + VECTORLIKE) on control channel: {label}",
              av < TOL and sv == (96, 96, 0) and ppb < TOL and mmb < TOL and pr > 0.99,
              f"{{R,om}}={av:.1e}, sig(K R)={sv}, diag-blocks=({ppb:.0e},{mmb:.0e}), R-perp-C={pr:.3f}")

    # the pure Clifford trace of a single gamma stays a single gamma (chirality-odd), so the S+ Clifford-
    # trace channel structurally cannot supply the K-definite C-operator grading -- disqualifying control.
    Ctr = sum(ETA[a] * e[a] @ e[3] @ e[a] for a in range(N))
    coeff = complex(np.trace(Ctr @ e[3]) / np.trace(e[3] @ e[3]))
    prop = float(np.linalg.norm(Ctr - coeff * e[3]) / np.linalg.norm(Ctr))
    check("F0 Clifford-trace disqualifier: sum_a e^a c(v) e_a stays proportional to the single gamma c(v) "
          "(chirality-odd, K-self-adjoint) -- the S+ Clifford-trace channel does NOT produce the "
          "K-definite eta_+=eta*C grading",
          prop < TOL, f"||trace - {coeff.real:.1f}*c(v)||/||.|| = {prop:.1e}")

    # ------------------------------------------------------------------
    section("VERDICT")
    print("  R_src (twisted-RS fiber-Clifford-trace pushforward, RS channel, on the explicit")
    print("  (+96,-96) triplet carrier) is chirality-ODD and K-SELF-adjoint; the Hermitian K_c R_src")
    print("  has signature (96,96) -> R_src is the K-NULL/indefinite type, NOT the C-operator's")
    print("  K-definite (192,0); and R_src is Frobenius-orthogonal to C = sign(K_c).")
    print("    TEST 1  UNIFICATION = DISTINCT   (R_src != eta_+ = eta*C; conditional on the RS-channel")
    print("            fixing, robust across the fiber / all-14 / no-Pi / horizontal controls here).")
    print("    TEST 2  chiralize/vectorlike = VECTORLIKE   (chi = 0, forced by {R_src,omega}=0;")
    print("            channel-type-invariant).")
    print("  Coherent with core-theorems Theorems 2/3 (Krein-isometric / chirality-odd operators")
    print("  conserve the net chiral index at 0) and W201's lean: the count needs a SEPARATE Z/3")
    print("  self-dual import. ULTRALOCAL; no nonlocal Z_U, no Z/3 count VALUE, no canon/verdict movement.")

    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    print(f"\nW218: {n_pass}/{n_tot} checks passed")
    if n_pass != n_tot:
        print("FAILED: " + str([nm for nm, ok in CHECKS if not ok]))
        return 1
    print("VERDICT: DISTINCT (not SAME-OPERATOR) + VECTORLIKE. The generation-count source operator")
    print("R_src is NOT the unitarity grading eta_+ = eta*C, and it does not chiralize the carrier.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
