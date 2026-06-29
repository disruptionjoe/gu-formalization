#!/usr/bin/env python3
r"""
ADVERSARIAL PROBE of the STRUCTURAL no-go claim in minimal_forcing_ingredient.py.

The construct claims: net chirality = Tr_carrier(Gc . Delta) factorizes as Tr_V(Vpart).Tr_S(...)
so every traceless-so(4) (frame-active) V-part gives net_chir = 0 EXACTLY. It tested only 6 simple
product probes.

But net_chirality(O) = Re Tr(G_P . O) where G_P = P.(id_14 (x) omega).P and P = Wt Wt^dag is the
projector onto the 192-dim carrier. P is NOT a product projector (the carrier ENTANGLES V and S via
J3 = id(x)sgen + lvec(x)id). So the factorization the construct asserts need not hold on the carrier.

DECISIVE TEST: compute M_V = Tr_S(G_P), the 14x14 V-marginal of the carrier-projected grading.
  - If M_V is proportional to id_14  => net_chir of any (frame-active V) (x) I_S is 0 => structural holds
    against I_S spinor probes.
  - More generally, search for ANY operator O that is simultaneously net-chiral AND net-self-dual-
    frame-active, by projecting G_P onto the frame-active subspace so(4)_SD (x) End(S) and reading the
    norm. If that projection is non-zero, an escape operator EXISTS (take O = that projection).

We compute the exact overlap of the net-chirality functional with the frame-active sector, the cleanest
refutation/confirmation of the orthogonality claim.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)
import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def main():
    np.set_printoptions(precision=5, suppress=True, linewidth=170)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare={bare:.4f} (58.7215)  C2={C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2

    # ---- build carrier exactly as construct does ----
    J3full = [np.kron(np.eye(N), sgen(e, a, b) + sgen(e, c, d))
              + np.kron(lvec(a, b) + lvec(c, d), np.eye(DIM)) for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = Wk.conj().T @ Cas @ Wk
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uc[:, np.abs(ev - top) < 1e-3]
    dC = Wt.shape[1]
    print(f"[carrier] dim={dC}")

    om = np.eye(DIM, dtype=complex)
    for a in range(N):
        om = om @ e128[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir_int = om if om2 > 0 else (-1j) * om
    Gamma_full = np.kron(np.eye(N), chir_int)               # id_14 (x) omega
    # Hermitize the grading (should already be Hermitian up to numerics)
    Gh = 0.5 * (Gamma_full + Gamma_full.conj().T)
    print(f"[grading] ||Gamma - Gamma^dag|| = {np.linalg.norm(Gamma_full - Gamma_full.conj().T):.2e}")

    P = Wt @ Wt.conj().T                                    # projector onto carrier (1792x1792)
    G_P = P @ Gh @ P                                        # carrier-projected grading
    G_P = 0.5 * (G_P + G_P.conj().T)

    # net_chirality(O) used by the construct == Re Tr(G_P . O_herm). Confirm via id_V(x)omega:
    test = np.kron(np.eye(N), chir_int)
    val = np.trace(G_P @ test).real
    print(f"[check] Re Tr(G_P . [id_V(x)omega]) = {val:.3f}  (construct's +192 for id_V grading probe)")

    # ===================== DECISIVE TEST 1: V-marginal of G_P =====================
    # M_V = Tr_S(G_P): 14x14. If M_V ∝ id_14 then net_chir of (frameActiveV)(x)I_S = 0.
    G4 = G_P.reshape(N, DIM, N, DIM)
    M_V = np.einsum('vsws->vw', G4)                         # partial trace over S
    print("\n[Test 1] V-marginal M_V = Tr_S(G_P):")
    diag = np.diag(M_V).real
    offnorm = np.linalg.norm(M_V - np.diag(np.diag(M_V)))
    print(f"  diag(M_V) = {diag}")
    print(f"  ||off-diagonal(M_V)|| = {offnorm:.3e}")
    # decompose M_V into id_14 part + traceless part
    tr = np.trace(M_V) / N
    M_V_traceless = M_V - tr * np.eye(N)
    print(f"  trace(M_V)/14 (id_V coeff) = {tr.real:.4f}")
    print(f"  ||traceless part of M_V|| = {np.linalg.norm(M_V_traceless):.3e}")

    # so(4) self-dual + anti-self-dual generators on base {0,1,2,3}
    sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
    print("\n  overlap of M_V with so(4) frame generators  <L, M_V> = Tr(L^dag M_V):")
    for nm, L in ([("SD%d" % i, g) for i, g in enumerate(sd_gens)] +
                  [("ASD%d" % i, g) for i, g in enumerate(asd_gens)]):
        ov = np.trace(L.conj().T @ M_V)
        print(f"    {nm}: <L,M_V> = {ov:.3e}")

    # ===================== DECISIVE TEST 2: does net-chir functional hit frame-active sector =====
    # Project G_P onto the subspace  span{ so(4)_SD generator (x) End(S) }. If nonzero, the operator
    # O* = that projection is BOTH frame-active (lives on so(4)_SD) AND net-chiral (Tr(G_P O*) = ||proj||^2 > 0).
    # Compute, for each SD/ASD frame generator L, the S-side operator  X_L = <L, G_P>_V  (DIMxDIM),
    # i.e. X_L[s,t] = sum_{v,w} conj(L[v,w]) G4[v,s,w,t] / ||L||^2 . Then net_chir reachable through L is
    # Tr(G_P . (L (x) X_L^dag-normalized)). The relevant quantity: ||X_L|| (is the grading's frame-L content nonzero?).
    print("\n[Test 2] S-side content X_L of the grading along each frame generator L (||X_L|| > 0 => escape exists):")
    G4c = G_P.reshape(N, DIM, N, DIM)
    escape_norm = 0.0
    for nm, L in ([("SD%d" % i, g) for i, g in enumerate(sd_gens)] +
                  [("ASD%d" % i, g) for i, g in enumerate(asd_gens)]):
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        X_L = np.einsum('vw,vswt->st', L.conj(), G4c) / nrm      # DIM x DIM
        nX = np.linalg.norm(X_L)
        # net chirality actually reachable: build O = L (x) X_L (frame-active), measure Re Tr(G_P O_herm) and its frame charge
        O = np.kron(L, X_L)
        Oh = 0.5 * (O + O.conj().T)
        ncr = np.trace(G_P @ Oh).real
        print(f"    {nm}: ||X_L (grading's S-content along L)|| = {nX:.3e}   "
              f"net_chir of O=L(x)X_L = {ncr:+.3e}")
        escape_norm = max(escape_norm, nX)

    print("\n[verdict]")
    print(f"  max ||X_L|| over all frame generators = {escape_norm:.3e}")
    if escape_norm < 1e-8:
        print("  STRUCTURAL CONFIRMED: the carrier-projected grading G_P has ZERO content along every")
        print("  frame (so(4)) generator on V. net-chirality functional and frame-charge functional are")
        print("  genuinely orthogonal -- NOT an artifact of the 6-probe sample. Factorization holds")
        print("  because Tr_S(G_P) is exactly proportional to id_14 (frame-trivial). No escape operator.")
    else:
        print("  *** ESCAPE: G_P has nonzero frame content. An operator O = L (x) X_L is BOTH frame-active")
        print("  AND net-chiral. The construct's orthogonality claim is FALSE in general. ***")

    return dict(carrier_dim=dC, idV_coeff=float(tr.real),
                traceless_MV_norm=float(np.linalg.norm(M_V_traceless)),
                max_frame_content=float(escape_norm))


if __name__ == "__main__":
    out = main()
    print("\n[machine-readable]", out)
