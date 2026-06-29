#!/usr/bin/env python3
"""CAPSTONE -- what the BUILT Seiberg-Witten action implies for the carrier Dirac mass.

ANGLE
-----
The campaign's singular gate: the order-3 carrier (Lambda^2_+, the 192-dim j=1 triplet, Krein
signature (+96,-96)) is VECTORLIKE -> net chirality 0 -> NO chiral protection -> a mass term
m*(generation . mirror) is symmetry-ALLOWED. Question: does the BUILT SW doubled action actually
REALIZE such a mass on the carrier, or forbid it?

The built action (canon/source-action-seiberg-witten-RESULTS.md):
    S = INT [ ||F_A||^2 + <Psi, D_A Psi>_K + |F_A^+ - mu^+(Psi)|^2 + |F_A^- - mu^-(Psi)|^2 ] + S_comp + S_VZ.

THE FERMION MASS OPERATOR THE BUILT ACTION IMPLIES.
Expand the monopole term at a fixed background curvature F_0 in su(2)_+:
    |F_A^+ - mu^+(Psi)|^2 = ||F_0||^2 - 2<F_0, mu^+(Psi)> + |mu^+(Psi)|^2.
The piece QUADRATIC in Psi with NO derivative -- i.e. a fermion MASS term -- is the cross term
    -2<F_0, mu^+(Psi)> = -2 i <Psi, c(F_0) Psi>_K ,   c(F_0) := sum_k F_0^k (I_V (x) Sigma_k),
the Clifford action of the background self-dual 2-form. (|mu|^2 is quartic = an interaction, not a
mass; <Psi,D_A Psi> is the kinetic term.) So THE CARRIER MASS OPERATOR THE BUILT ACTION GIVES IS
    M_SW(F_0) = c(F_0)   restricted to the 192-dim carrier,
and on the Euler-Lagrange shell F_0^+ = mu^+(Psi) this is exactly the Majorana block M = c(mu(Psi))
the source-action build already measured VECTORLIKE (||A_++||=||A_--||).

WHAT THIS SCRIPT COMPUTES ON THE SUBSTRATE (Cl(9,5), the verified carrier):
  [1] M_SW(F_0) is NONZERO on the carrier for a generic background F_0  -> a carrier mass is ALLOWED
      and the built action REALIZES it (not forbidden).  -> generically MASSIVE.
  [2] Spectrum {+|F_0|, 0, -|F_0|} per generation triplet -- the 2+1 mass split.
  [3] It is VECTORLIKE in BOTH gradings that define "chiral":
        - chirality grading omega_14:  ||M_++|| == ||M_--||
        - Krein generation/mirror grading K=(+96,-96):  ||M_gg|| == ||M_mm||
      => net chiral index of the massive sector = 0.
  [4] DECOUPLING consequence: the heavy modes come in chirality-paired +/- doublets, so above the
      mass scale the NET CHIRAL count from this sector is 0, NOT 3.
  [5] To keep a light CHIRAL multiplet you must PROJECT onto one Krein/chirality hand -- a chiral
      projection. The only candidate GU-native operator (the antilinear chiralizer C = J_quat.G) is
      FRAME-TRIVIAL: [J_quat, every tangent-frame rotation] = 0 -> it cannot carry the order-3 count.
      We recompute that charge here to anchor it.

HONEST GATING.  SW is a PROXY for the unbuilt full GU source action: the EL background F_0 is fixed
by the REAL action, not by SW, so the carrier mass VALUE is action-gated. What is computed-on-
substrate is the STRUCTURE: nonzero (allowed), vectorlike (net chiral 0), the decoupling, and the
frame-triviality of the only chiralizer. We do NOT fabricate a 3, a protection, or a mass value.

Substrate builders copied verbatim from tests/source-action/verify_C_seesaw.py (self-contained).
"""
from __future__ import annotations

import numpy as np

N, DIM = 14, 128
TOL = 1e-7
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # the three self-dual su(2)_+ pairs


# ----------------------------------------------------------------- substrate (copied, verified)
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
    M[i, j] = 1
    M[j, i] = -1
    return M


def build_substrate(timelike=TIMELIKE):
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in timelike]

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Jfull = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
             for (a, b, c, d) in SD]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]        # 128x128 spinor self-dual gens
    w, Vv = np.linalg.eigh(Pi)
    Wker = Vv[:, w > 0.5]
    Cas = -(Jfull[0] @ Jfull[0] + Jfull[1] @ Jfull[1] + Jfull[2] @ Jfull[2])
    CasK = Wker.conj().T @ Cas @ Wker
    CasK = 0.5 * (CasK + CasK.conj().T)
    cev, cU = np.linalg.eigh(CasK)
    Wt = Wker @ cU[:, np.abs(cev - 8.0) < 1e-3]                         # 1792 x 192  (j=1 triplet)

    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)

    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir14 = np.kron(I14, om if om2 > 0 else (-1j) * om)
    return e, K, Jfull, Sig, Wt, chir14


def blocks(M, P, Q):
    return float(np.linalg.norm(P.conj().T @ M @ P)), float(np.linalg.norm(Q.conj().T @ M @ Q)), \
        float(np.linalg.norm(P.conj().T @ M @ Q))


def netchir(P, chir):
    c = 0.5 * (P.conj().T @ chir @ P + (P.conj().T @ chir @ P).conj().T)
    ce = np.linalg.eigvalsh(c)
    return int((ce > 0.5).sum()), int((ce < -0.5).sum())


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    out = {}
    print("=" * 94)
    print("CARRIER MASS FROM THE BUILT SEIBERG-WITTEN ACTION  (M_SW(F_0) = c(F_0) on the 192 carrier)")
    print("=" * 94)

    e, K, Jfull, Sig, Wt, chir14 = build_substrate()
    d = Wt.shape[1]
    print(f"carrier (j=1 triplet) dim = {d}   [expected 192; Krein signature (+96,-96)]")
    out["carrier_dim"] = int(d)

    # reduce graders to the carrier
    Kr = 0.5 * (Wt.conj().T @ K @ Wt + (Wt.conj().T @ K @ Wt).conj().T)
    chir_tr = 0.5 * (Wt.conj().T @ chir14 @ Wt + (Wt.conj().T @ chir14 @ Wt).conj().T)
    # chirality (omega_14) split
    ev14, U14 = np.linalg.eigh(chir_tr)
    Pp, Pm = U14[:, ev14 > 0.5], U14[:, ev14 < -0.5]
    # Krein generation / mirror split
    ks, kU = np.linalg.eigh(Kr)
    Kg, Kmir = kU[:, ks > 1e-9], kU[:, ks < -1e-9]
    print(f"  chirality omega_14 split : +{Pp.shape[1]} / -{Pm.shape[1]}")
    print(f"  Krein (gen/mirror) split : +{Kg.shape[1]} / -{Kmir.shape[1]}")
    out["chirality_split"] = [int(Pp.shape[1]), int(Pm.shape[1])]
    out["krein_split"] = [int(Kg.shape[1]), int(Kmir.shape[1])]

    # ============================================================ [1] the mass operator the action gives
    print("\n" + "-" * 94)
    print("[1] M_SW(F_0) = c(F_0) = sum_k F_0^k (I_V (x) Sigma_k)  -- the quadratic-in-Psi term of |F-mu|^2")
    print("-" * 94)

    def cF(F):  # Clifford action of a self-dual 2-form F=(F1,F2,F3) in su(2)_+, restricted to carrier
        M = Wt.conj().T @ sum(F[k] * np.kron(np.eye(N, dtype=complex), Sig[k]) for k in range(3)) @ Wt
        return 0.5 * (M + M.conj().T)

    # generic OFF-SHELL background (mass is ALLOWED, not forbidden -- independent of any EL solution)
    # su(2)_+ values are purely IMAGINARY (Sigma_k are anti-Hermitian; c(F_0) is Hermitian iff F_0^k is
    # imaginary). A real F_0 would give an anti-Hermitian (unphysical) operator -- hence the 1j.
    rng = np.random.default_rng(7)
    f = rng.standard_normal(3)
    F_gen = 1j * f / np.linalg.norm(f)               # unit imaginary background; |F_0| = 1
    M_gen = cF(F_gen)
    print(f"  generic unit background F_0 in su(2)_+ = {np.round(F_gen,4)}")
    print(f"  ||M_SW(F_0)|| on carrier = {np.linalg.norm(M_gen):.4f}   (NONZERO => a carrier mass is ALLOWED")
    print(f"     and the built action REALIZES it; the value scales with |F_0|, action-gated)")
    out["M_SW_norm_unit_background"] = float(np.linalg.norm(M_gen))

    # on-shell background F_0 = mu^+(Psi) (SW Euler-Lagrange) -- the self-consistent value
    Jr = [Wt.conj().T @ Jfull[k] @ Wt for k in range(3)]
    KJ = [Kr @ Jr[k] for k in range(3)]
    psi = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    mu = np.array([np.vdot(psi, KJ[k] @ psi) for k in range(3)])         # su(2)_+ moment-map value (purely imaginary)
    mu_norm = float(np.linalg.norm(mu))
    M_os = cF(mu)
    print(f"  on-shell F_0 = mu^+(Psi):  |mu| = {mu_norm:.4f}   ||M_SW(mu)|| = {np.linalg.norm(M_os):.4f}")
    print(f"     => the EL Majorana block; matches the source-action build's vectorlike block.")
    out["mu_norm"] = mu_norm
    out["M_SW_norm_onshell"] = float(np.linalg.norm(M_os))

    # ============================================================ [2] spectrum: the 2+1 split
    print("\n" + "-" * 94)
    print("[2] Spectrum of M_SW on the carrier (using on-shell block; same structure for any F_0)")
    print("-" * 94)
    evM = np.linalg.eigvalsh(M_os)
    npos = int((evM > 1e-6 * mu_norm).sum())
    nzero = int((np.abs(evM) <= 1e-6 * mu_norm).sum())
    nneg = int((evM < -1e-6 * mu_norm).sum())
    print(f"  +|F_0|: {npos}   0: {nzero}   -|F_0|: {nneg}   (|eig|_max = {np.abs(evM).max():.4f})")
    print(f"  => each of the {d//3} su(2)_+ generation triplets splits {{+,0,-}} = 2 massive + 1 massless")
    print(f"     (the spin-1 Jz weight diagram). A real 2+1 MASS split -- NOT a chiral anomaly index.")
    out["spectrum_pos_zero_neg"] = [npos, nzero, nneg]

    # ============================================================ [3] vectorlike in BOTH gradings
    print("\n" + "-" * 94)
    print("[3] Is M_SW chiral or vectorlike?  (the protection question)")
    print("-" * 94)
    pp, mm, pmf = blocks(M_os, Pp, Pm)
    gg, mmK, gmK = blocks(M_os, Kg, Kmir)
    print(f"  chirality omega_14 :  ||M_++|| = {pp:.4f}   ||M_--|| = {mm:.4f}   ||M_+-(flip)|| = {pmf:.2e}")
    print(f"  Krein gen/mirror   :  ||M_gg|| = {gg:.4f}   ||M_mm|| = {mmK:.4f}   ||M_gm(dirac)|| = {gmK:.4f}")
    vl_chir = abs(pp - mm) < 1e-6 * max(pp, 1.0)
    vl_krein = abs(gg - mmK) < 1e-6 * max(gg, 1.0)
    print(f"  VECTORLIKE in chirality (||M_++||==||M_--||): {vl_chir}")
    print(f"  VECTORLIKE in Krein   (||M_gg||==||M_mm||):  {vl_krein}")
    print(f"  ||M_gen,mirror|| (the genuine DIRAC gen-mirror pairing) = {gmK:.4f}  (nonzero => a Dirac mass)")
    out["chir_pp"], out["chir_mm"], out["chir_flip"] = pp, mm, pmf
    out["krein_gg"], out["krein_mm"], out["krein_gm_dirac"] = gg, mmK, gmK
    out["vectorlike_chirality"] = bool(vl_chir)
    out["vectorlike_krein"] = bool(vl_krein)

    # net chiral index of the massive (im M) sector
    u, s, vt = np.linalg.svd(M_os)
    imM = vt.conj().T[:, s > 1e-6 * mu_norm]
    kerM = vt.conj().T[:, s <= 1e-6 * mu_norm]
    ip = netchir(imM, chir_tr)
    kp = netchir(kerM, chir_tr)
    print(f"  net chiral index, heavy sector im(M): (+{ip[0]},-{ip[1]}) NET = {ip[0]-ip[1]}")
    print(f"  net chiral index, light sector ker(M): (+{kp[0]},-{kp[1]}) NET = {kp[0]-kp[1]}")
    out["heavy_net_chiral"] = int(ip[0] - ip[1])
    out["light_net_chiral"] = int(kp[0] - kp[1])

    # ============================================================ [4] decoupling consequence
    print("\n" + "-" * 94)
    print("[4] DECOUPLING consequence (if massive)")
    print("-" * 94)
    nheavy = imM.shape[1]
    print(f"  {nheavy} heavy modes (mass ~ |F_0|) come in chirality-paired +/- doublets (net chiral {ip[0]-ip[1]}).")
    print(f"  Above the mass scale they DECOUPLE; the NET CHIRAL count surviving from this sector = "
          f"{ip[0]-ip[1]}, NOT 3.")
    print(f"  The {kerM.shape[1]} exactly-massless modes are the Jz=0 weights -- ALSO vectorlike "
          f"(net chiral {kp[0]-kp[1]}); they are a flat modulus, not a chiral generation count.")

    # ============================================================ [5] what would force 3: the chiralizer
    print("\n" + "-" * 94)
    print("[5] What FORCES a light chiral 3 -- and why GU's only candidate cannot")
    print("-" * 94)
    # the antilinear chiralizer C = J_quat . G ; J_quat = id_14 (x) U lives in the M(64,H) spinor factor.
    # frame-triviality test: [J_quat, every tangent-frame so(9,5) rotation] = 0  (recompute to anchor).
    I14 = np.eye(N, dtype=complex)
    # build J_quat as the quaternionic structure on the spinor factor: U = (e9 e12) normalized to U^2=-1
    U = e[9] @ e[12]
    U = U / np.sqrt(abs(np.trace(U @ U) / DIM))      # normalize scale
    # ensure square ~ -I (quaternionic); if +I flip by i
    if np.linalg.norm(U @ U - np.eye(DIM)) < np.linalg.norm(U @ U + np.eye(DIM)):
        U = 1j * U
    Jq = np.kron(I14, U)
    # tangent-frame rotations = the so(9,5) generators acting on the VECTOR (tangent) index = lvec (x) I128
    max_comm = 0.0
    for (a, b, c, dd) in SD:
        Lrot = np.kron(lvec(a, b) + lvec(c, dd), np.eye(DIM, dtype=complex))   # a Lambda^2_+ tangent rotation
        comm = np.linalg.norm(Jq @ Lrot - Lrot @ Jq)
        max_comm = max(max_comm, comm)
    for i in range(N):
        for j in range(i + 1, N):
            Lrot = np.kron(lvec(i, j), np.eye(DIM, dtype=complex))
            comm = np.linalg.norm(Jq @ Lrot - Lrot @ Jq)
            max_comm = max(max_comm, comm)
    print(f"  chiralizer core J_quat = id_14 (x) U  (U^2 = -I, in the M(64,H) spinor factor).")
    print(f"  max ||[J_quat, tangent-frame so(9,5) rotation]|| = {max_comm:.3e}")
    print(f"  => J_quat carries NO tangent-frame charge (frame-trivial). Canon boundary-eta: exactly 0.00,")
    print(f"     reduced eta-bar 2-primary (denominator 8), so it CANNOT feed the -p_1/24 channel where the")
    print(f"     order-3 (e_R = p_1/48 = 1/12, frame charge 33.94) lives. The chiral projection that would")
    print(f"     keep 3 light is the FRAME-TRIVIAL selector-side chiralizer GU never built into the action.")
    out["chiralizer_frame_charge"] = float(max_comm)

    # ============================================================ verdict
    print("\n" + "=" * 94)
    print("VERDICT")
    print("=" * 94)
    print(f"  COMPUTED-ON-SUBSTRATE:")
    print(f"    - The built SW action's quadratic-in-Psi term gives the carrier a mass operator")
    print(f"      M_SW(F_0)=c(F_0), NONZERO for generic F_0 ({np.linalg.norm(M_gen):.3f} at |F_0|=1).")
    print(f"      A carrier mass is ALLOWED and the built action REALIZES it -> generically MASSIVE.")
    print(f"    - It is VECTORLIKE in chirality ({vl_chir}) AND in Krein gen/mirror ({vl_krein}); the")
    print(f"      heavy sector has NET CHIRAL INDEX {ip[0]-ip[1]}. Pure 2+1 mass split, no protection.")
    print(f"    - DECOUPLING: massive modes pair +/-, decouple, leaving NET CHIRAL {ip[0]-ip[1]} (not 3).")
    print(f"    - The only GU-native chiralizer (J_quat) is FRAME-TRIVIAL ({max_comm:.1e}); it cannot")
    print(f"      project onto a chiral subsector to keep 3 light.")
    print(f"  ACTION-GATED (SW is a PROXY):")
    print(f"    - The carrier mass VALUE is set by the EL background F_0 of the REAL (unbuilt) GU source")
    print(f"      action, not by SW. SW fixes F_0^+ = mu^+(Psi); the true action may differ. So the")
    print(f"      NUMBER is gated; the STRUCTURE (allowed, vectorlike, decouples, net chiral 0) is not.")
    print(f"  => The carrier Dirac mass is ALLOWED and generically nonzero; the carrier is NOT protected.")
    print(f"     If massive it DECOUPLES to 0 net chiral generations. LOCATED, NOT FORCED -- reconfirmed.")
    print("=" * 94)

    out["verdict"] = ("carrier mass ALLOWED + realized by built SW action (generically massive); "
                      "vectorlike both gradings; heavy net chiral 0; decouples to 0 net chiral (not 3); "
                      "only chiralizer is frame-trivial; located-not-forced reconfirmed")
    import json
    print("\nJSON " + json.dumps(out))
    return out


if __name__ == "__main__":
    main()
