#!/usr/bin/env python3
"""
Independent re-check of the reviewer-#2 addendum
(tests/antilinear-bound/nonkrein_physical_admissibility.py) on a GENUINELY
different substrate:

  * OWN gamma matrices by RECURSIVE DOUBLING (not the Jordan-Wigner build of the
    main scripts);
  * a DIFFERENT seed;
  * the carrier / K / Gamma_c rebuilt from those gammas and its premises
    re-certified independently;
  * a CROSS-SIGNATURE run on Cl(7,7) (internal so(3,7)) -- the null structure is
    signature-independent;
  * a Euclidean Cl(14,0) PREMISE-FAILURE control -- there W_+/- are K-ALIGNED
    (not K-null), the null hypothesis fails, and a physical subspace DOES carry
    |chi| = 96, proving the isotropy (null-eigenspace) hypothesis is load-bearing,
    not vacuous.

Reproduces, on this independent substrate: P_iso strictly contains S (non-Krein
operators with K-null re-graded eigenspaces), index nullity chi_C(P) = 0 on all of
P_iso (exact integer ranks), and the K-definite re-grading carrying the vectorlike
+-96.  Deterministic, numpy-only.  Any disagreement aborts.
"""
import time
import numpy as np

T0 = time.time()
SEED = 20260705                       # different seed from the addendum (20260704)
np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(SEED)
NASSERT = 0


def check(cond, msg):
    global NASSERT
    NASSERT += 1
    assert cond, msg


# ------------------------------------------------- OWN gammas: recursive doubling (not Jordan-Wigner)
def gammas_recursive(k):
    """2k real-Clifford gammas of dim 2^k by recursive doubling; distinct build from jw()."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = [s1.copy(), s2.copy()]                                  # Cl(2)
    for _ in range(k - 1):
        d = G[0].shape[0]
        G = [np.kron(g, s3) for g in G] + [np.kron(np.eye(d, dtype=complex), s1),
                                           np.kron(np.eye(d, dtype=complex), s2)]
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec4(i, j):
    M = np.zeros((4, 4), dtype=complex)
    M[i, j], M[j, i] = 1, -1
    return M


def build_carrier(timelike):
    """rebuild (Gamma_c, K, W_+, W_-, P_phys, N_phys) from recursive-doubling gammas
    for the signature with the given internal timelike set (frame 0..3 spacelike)."""
    base = gammas_recursive(7)                                  # 14 gammas, dim 128
    N, DIM = 14, 128
    I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    cerr = max(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                             - (2.0 * (-1.0 if a in timelike else 1.0) if a == b else 0.0) * I128))
               for a in range(N) for b in range(N))
    check(cerr < 1e-11, "own recursive-doubling gammas satisfy the Clifford relations")
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    Jk = [np.kron(lvec4(a, b) + lvec4(c, d), I128) + np.kron(I4, S)
          for (a, b, c, d), S in zip(SD, Sig)]
    Cas = -(Jk[0] @ Jk[0] + Jk[1] @ Jk[1] + Jk[2] @ Jk[2])
    Cas = 0.5 * (Cas + Cas.conj().T)
    cw, cV = np.linalg.eigh(Cas)
    W = cV[:, np.abs(cw - cw.max()) < 1e-6]
    check(abs(cw.max() - 8.0) < 1e-9 and W.shape[1] == 192, "carrier j=1 Casimir-8, dim 192")
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    Gc = W.conj().T @ np.kron(I4, om) @ W
    Gc = 0.5 * (Gc + Gc.conj().T)
    gev, gV = np.linalg.eigh(Gc)
    check(int((gev > 0.5).sum()) == 96 and int((gev < -0.5).sum()) == 96, "chirality split 96/96")
    P0, N0 = gV[:, gev > 0.5], gV[:, gev < -0.5]
    spacelike = [a for a in range(N) if a not in timelike]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    Kc = W.conj().T @ np.kron(I4, bS) @ W
    Kc = 0.5 * (Kc + Kc.conj().T)
    kev, kV = np.linalg.eigh(Kc)
    check(int((kev > 1e-8).sum()) == 96 and int((kev < -1e-8).sum()) == 96, "K signature (96,96)")
    check(np.linalg.norm(Kc @ Kc - np.eye(192)) < 1e-9, "K^2 = I")
    Pphys, Nphys = kV[:, kev > 1e-8], kV[:, kev < -1e-8]
    return Gc, Kc, P0, N0, Pphys, Nphys


def rank_gap(A, tol=1e-8):
    s = np.linalg.svd(A, compute_uv=False)
    return int((s > tol * s.max()).sum())


def net_chi(P, Ep, Em):
    return (192 - rank_gap(np.hstack([P, Ep]))) - (192 - rank_gap(np.hstack([P, Em])))


def run_cross_chirality(tag, timelike):
    print("\n" + "=" * 98)
    print(f"{tag}: independent carrier + P_iso index-nullity")
    print("=" * 98)
    Gc, Kc, P0, N0, Pphys, Nphys = build_carrier(timelike)
    cross = np.linalg.norm(Kc @ Gc + Gc @ Kc)
    isoWp = np.linalg.norm(P0.conj().T @ Kc @ P0)
    print(f"  premises: K Gamma_c anticommutator {cross:.2e}, W_+ K-isotropy {isoWp:.2e} "
          f"(cross-chirality / null-graded chirality -- reproduced)")
    check(cross < 1e-9 and isoWp < 1e-9, f"{tag}: cross-chirality premise reproduced")
    # physical subspaces
    def expm(X):
        k = max(0, int(np.ceil(np.log2(max(1e-16, np.linalg.norm(X, 2))))) + 2)
        Y, E, T = X / 2 ** k, np.eye(192, dtype=complex), np.eye(192, dtype=complex)
        for n in range(1, 18):
            T = T @ Y / n
            E = E + T
        for _ in range(k):
            E = E @ E
        return E
    phys = [Pphys]
    for _ in range(2):
        H = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
        phys.append(expm(Kc @ (0.4 * (H - H.conj().T) / np.linalg.norm(H))) @ Pphys)
    for P in phys:
        check(np.linalg.eigvalsh(P.conj().T @ Kc @ P).min() > 1e-6, f"{tag}: physical subspace K-positive")
    # Lagrangian pairing basis -> build non-Krein operators with K-null re-graded eigenspaces
    Gpair = P0.conj().T @ Kc @ N0
    Q = np.hstack([P0, N0 @ np.linalg.inv(Gpair)])
    Qc_inv = np.linalg.inv(np.hstack([P0.conj(), N0.conj()]))
    Kb = Kc.conj()

    def krein_res(M):
        KM = M.conj().T @ Kc @ M
        lam = (np.vdot(Kb, KM) / np.vdot(Kb, Kb)).real
        return np.linalg.norm(KM - lam * Kb) / np.linalg.norm(KM)

    worst = 0
    for j in range(4):
        U1, U2 = (lambda: (lambda A: 0.5 * (A - A.conj().T))(
            rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))))(), \
            (lambda: (lambda A: 0.5 * (A - A.conj().T))(
                rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))))()
        Lp, Lm = Q @ np.vstack([np.eye(96), U1]), Q @ np.vstack([np.eye(96), U2])
        M = np.hstack([Lp, Lm]) @ Qc_inv
        Ep, Em = M @ P0.conj(), M @ N0.conj()
        iso = max(np.linalg.norm(Ep.conj().T @ Kc @ Ep),
                  np.linalg.norm(Em.conj().T @ Kc @ Em)) / (np.linalg.norm(M) ** 2 / 192)
        kr = krein_res(M)
        chis = [net_chi(P, Ep, Em) for P in phys]
        worst = max(worst, max(abs(c) for c in chis))
        check(kr > 0.3, f"{tag}: op {j} non-Krein (residual {kr:.2f})")
        check(iso < 1e-8, f"{tag}: op {j} re-graded eigenspaces K-null (isotropy {iso:.1e})")
        for c in chis:
            check(c == 0, f"{tag}: op {j} chi = {c} != 0 -- FAILURE")
        print(f"  op {j}: Krein residual {kr:.2f} (not in S), eigenspace isotropy {iso:.1e}, "
              f"chi_C(P) = {chis}")
    check(worst == 0, f"{tag}: index nullity holds on P_iso")
    # K-definite re-grading control: carries +-96
    Mdef = np.hstack([Pphys, Nphys]) @ Qc_inv
    Ep, Em = Mdef @ P0.conj(), Mdef @ N0.conj()
    chid = [net_chi(P, Ep, Em) for P in phys]
    print(f"  K-DEFINITE re-grading (eigenspaces = K-positive/K-negative): raw index {chid} "
          f"(vectorlike +-96, non-vacuity)")
    check(max(abs(c) for c in chid) == 96, f"{tag}: K-definite re-grading carries +-96")
    print(f"  => {tag}: P_iso index-nullity reproduced independently.")


run_cross_chirality("Cl(9,5) [internal so(5,5)]", {4, 5, 6, 7, 8})
run_cross_chirality("Cl(7,7) [internal so(3,7)]", {4, 5, 6, 7, 8, 9, 10})

# ---------------------------------------- Euclidean (14,0) premise-FAILURE control
print("\n" + "=" * 98)
print("Cl(14,0) control: null hypothesis FAILS (K aligned with Gamma_c) -> a physical subspace")
print("CAN carry |chi| = 96.  Confirms the isotropy (null-eigenspace) hypothesis is load-bearing.")
print("=" * 98)
Gc, Kc, P0, N0, Pphys, Nphys = build_carrier(set())          # all spacelike
align = min(np.linalg.norm(Kc - Gc), np.linalg.norm(Kc + Gc))
print(f"  min ||K -+ Gamma_c|| = {align:.2e}  (K IS the grading: ALIGNED, not cross-chirality)")
check(align < 1e-8, "(14,0): K is grading-aligned (null premise fails)")
# physical subspace = a K-eigenspace = a chirality eigenspace: net chirality +-96
chi14 = net_chi(Pphys, P0, N0)
print(f"  a physical (K-positive) subspace carries net chiral index = {chi14} (= +-96 != 0):")
print("  without the K-null chirality eigenspaces the count is NOT pinned -- isotropy is the")
print("  real hypothesis, and the theorem is not vacuous.")
check(abs(chi14) == 96, "(14,0) control: physical subspace carries |chi| = 96 (premise load-bearing)")

print("\n" + "#" * 98)
print("# INDEPENDENT RE-CHECK OF THE #2 ADDENDUM -- VERDICT")
print("#" * 98)
print(f"""
  On an independent substrate (own recursive-doubling gammas, different seed):
   - the cross-chirality / null-graded-chirality premises reproduce on Cl(9,5) and Cl(7,7);
   - P_iso strictly contains S (non-Krein operators with K-null re-graded eigenspaces built);
   - index nullity chi_C(P) = 0 holds on all of P_iso (exact integer ranks), both signatures;
   - the K-definite re-grading carries the vectorlike +-96 (non-vacuity);
   - the Euclidean (14,0) control fires |chi| = 96: the null-eigenspace hypothesis is
     load-bearing, and the theorem is not a tautology.
  The reviewer-#2 addendum is INDEPENDENTLY REPRODUCED.

  hard asserts passed: {NASSERT}
  total runtime: {time.time() - T0:.1f}s""")
# EOF
