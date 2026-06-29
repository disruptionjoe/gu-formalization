#!/usr/bin/env python3
"""ADVERSARIAL INDEPENDENT VERIFY of sw_action_carrier_mass.py.

Probes the load-bearing claims with fresh seeds + new tests:
  (A) carrier vectorlike: chirality +96/-96 AND Krein +96/-96, and do the two gradings agree?
  (B) c(F_0) for MANY independent + special F_0 directions: always nonzero? always symmetric spectrum?
      ALWAYS gen-mirror BLOCK-DIAGONAL (i.e. NOT a genuine Dirac gen.mirror mass)?
  (C) can ANY F_0 break the +/- chirality balance (force a chiral spectrum)?  scan directions.
  (D) chiralizer commutator: is the 0 a deep result or structurally forced by the tensor split?
      Test [id_14 (x) U, lvec (x) id_128] analytically + an ARBITRARY spinor-only operator.
  (E) does the monopole-term operator pair generation with mirror at all? (the 'Dirac mass' claim)
"""
from __future__ import annotations
import numpy as np

N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


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
    M[i, j] = 1; M[j, i] = -1
    return M


def build():
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in TIMELIKE]
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Jfull = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
             for (a, b, c, d) in SD]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wker = Vv[:, w > 0.5]
    Cas = -(Jfull[0] @ Jfull[0] + Jfull[1] @ Jfull[1] + Jfull[2] @ Jfull[2])
    CasK = Wker.conj().T @ Cas @ Wker
    CasK = 0.5 * (CasK + CasK.conj().T)
    cev, cU = np.linalg.eigh(CasK)
    Wt = Wker @ cU[:, np.abs(cev - 8.0) < 1e-3]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir14 = np.kron(I14, om if om2 > 0 else (-1j) * om)
    return e, K, Jfull, Sig, Wt, chir14


def main():
    e, K, Jfull, Sig, Wt, chir14 = build()
    I14 = np.eye(N, dtype=complex)
    d = Wt.shape[1]
    print(f"carrier dim = {d}")

    Kr = 0.5 * (Wt.conj().T @ K @ Wt + (Wt.conj().T @ K @ Wt).conj().T)
    chir_tr = 0.5 * (Wt.conj().T @ chir14 @ Wt + (Wt.conj().T @ chir14 @ Wt).conj().T)

    # (A) gradings
    ev14 = np.linalg.eigvalsh(chir_tr)
    evK = np.linalg.eigvalsh(Kr)
    print(f"(A) chirality split  +{int((ev14>0.5).sum())}/-{int((ev14<-0.5).sum())}")
    print(f"    Krein split      +{int((evK>1e-9).sum())}/-{int((evK<-1e-9).sum())}")
    # do chirality and Krein gradings commute? (independent question)
    comm_grad = np.linalg.norm(chir_tr @ Kr - Kr @ chir_tr)
    print(f"    ||[chir, Krein]|| = {comm_grad:.3e}  (0 => simultaneously diagonalizable gradings)")

    # build projectors
    e14, U14 = np.linalg.eigh(chir_tr)
    Pp, Pm = U14[:, e14 > 0.5], U14[:, e14 < -0.5]
    ks, kU = np.linalg.eigh(Kr)
    Kg, Kmir = kU[:, ks > 1e-9], kU[:, ks < -1e-9]

    def cF(F):
        M = Wt.conj().T @ sum(F[k] * np.kron(I14, Sig[k]) for k in range(3)) @ Wt
        return 0.5 * (M + M.conj().T)

    # (B)+(C) many directions
    print("(B/C) scanning F_0 directions (10 random + 3 axis + non-imaginary control):")
    rng = np.random.default_rng(20260629)
    worst_chiral_imbalance = 0.0
    worst_genmirror = 0.0
    min_norm = 1e9
    for trial in range(10):
        f = rng.standard_normal(3); f = 1j * f / np.linalg.norm(f)
        M = cF(f)
        nrm = np.linalg.norm(M); min_norm = min(min_norm, nrm)
        ev = np.linalg.eigvalsh(M)
        npos, nneg = int((ev > 1e-6).sum()), int((ev < -1e-6).sum())
        worst_chiral_imbalance = max(worst_chiral_imbalance, abs(npos - nneg))
        gm = np.linalg.norm(Kg.conj().T @ M @ Kmir)   # genuine Dirac gen-mirror block
        worst_genmirror = max(worst_genmirror, gm)
    # axis directions
    for k in range(3):
        f = np.zeros(3, dtype=complex); f[k] = 1j
        M = cF(f)
        ev = np.linalg.eigvalsh(M)
        gm = np.linalg.norm(Kg.conj().T @ M @ Kmir)
        worst_genmirror = max(worst_genmirror, gm)
        worst_chiral_imbalance = max(worst_chiral_imbalance, abs(int((ev>1e-6).sum())-int((ev<-1e-6).sum())))
    # non-imaginary (real) F_0 control: produces anti-Herm operator -> the bug the construct caught
    f_real = np.array([0.3, 0.5, -0.8])
    M_real = Wt.conj().T @ sum(f_real[k] * np.kron(I14, Sig[k]) for k in range(3)) @ Wt
    herm_defect_real = np.linalg.norm(M_real - M_real.conj().T)
    print(f"    min ||c(F_0)|| over trials = {min_norm:.4f}  (>0 => always nonzero, mass ALLOWED)")
    print(f"    worst |npos-nneg| chiral imbalance = {worst_chiral_imbalance}  (0 => ALWAYS vectorlike, no F_0 forces chirality)")
    print(f"    worst ||gen->mirror block|| of c(F_0) = {worst_genmirror:.3e}  (~0 => c(F_0) is NOT a gen-mirror Dirac mass; it is Krein-DIAGONAL)")
    print(f"    real (non-imaginary) F_0 => anti-Herm defect {herm_defect_real:.3f} (confirms su(2)_+ values must be imaginary; the caught bug)")

    # (D) chiralizer triviality: structural vs deep
    U = e[9] @ e[12]
    U = U / np.sqrt(abs(np.trace(U @ U) / DIM))
    if np.linalg.norm(U @ U - np.eye(DIM)) < np.linalg.norm(U @ U + np.eye(DIM)):
        U = 1j * U
    Jq = np.kron(I14, U)
    # actual chiralizer J_quat vs all 91 so(9,5) tangent rotations
    maxc = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            L = np.kron(lvec(i, j), np.eye(DIM, dtype=complex))
            maxc = max(maxc, np.linalg.norm(Jq @ L - L @ Jq))
    # CONTROL: an ARBITRARY spinor-only operator id_14 (x) R also commutes -> shows 0 is STRUCTURAL
    R = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    Jr = np.kron(I14, R)
    maxc_arb = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            L = np.kron(lvec(i, j), np.eye(DIM, dtype=complex))
            maxc_arb = max(maxc_arb, np.linalg.norm(Jr @ L - L @ Jr))
    print(f"(D) max||[J_quat, tangent rot]|| = {maxc:.3e}")
    print(f"    max||[ARBITRARY id14(x)R, tangent rot]|| = {maxc_arb:.3e}  (also 0 => the vanishing is STRUCTURAL: any spinor-only op carries 0 tangent charge, not special to J_quat)")

    # (E) does the FULL doubled-action quadratic structure ever pair gen<->mirror within c(F)? No.
    # The genuine Dirac gen-mirror leg must come from a Clifford-ODD operator c(e_a) (kinetic D_A), tested in verify_C.
    print("\nSUMMARY")
    print(f"  carrier vectorlike (both gradings +96/-96): {int((ev14>0.5).sum())==96 and int((evK>1e-9).sum())==96}")
    print(f"  c(F_0) always nonzero + always vectorlike: {min_norm>1e-6 and worst_chiral_imbalance==0}")
    print(f"  c(F_0) is gen-mirror DIAGONAL (NOT a Dirac mass; monopole term gives Majorana-type block): {worst_genmirror<1e-6}")
    print(f"  chiralizer frame-trivial is STRUCTURAL (any spinor-only op): {maxc<1e-9 and maxc_arb<1e-9}")


if __name__ == "__main__":
    main()
