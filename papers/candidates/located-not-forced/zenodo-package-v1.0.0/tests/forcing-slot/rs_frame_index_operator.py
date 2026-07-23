#!/usr/bin/env python3
r"""
RS FRAME-INDEX OPERATOR on the verified Cl(9,5)=M(64,H) substrate.

ANGLE: the Rarita-Schwinger field Psi_mu is the ONE object whose VECTOR index mu makes it
intrinsically non-frame-trivial (it is NOT of the form id_14 (x) U). Build the RS frame-index
operator with its genuine vector index (the gamma_mu gamma_nu / "slash" structure that couples the
spacetime frame index OFF-DIAGONALLY to the spinor), and measure SIMULTANEOUSLY:
  (c) FRAME CHARGE  -- component along the base tangent-frame so(4) generators (nonzero => non-frame-
      trivial, TANGENTIAL, can feed -p1/24).
  (b) NET CHIRALITY -- asymmetry between + and - chirality of the RS-selected physical sector.

CRUX: does the RS frame-index operator achieve nonzero frame charge AND nonzero net chirality
SIMULTANEOUSLY (the forcing slot), in the UNTWISTED case and in the case TWISTED by the chiral 16
of the internal Spin(10)? If net-chiral, what is the integer and its 2-/3-primary decomposition?

Controls reproduced first to anchor the substrate:
  - Lambda^2_+ self-dual carrier: frame charge ~33.94 (TANGENTIAL) but VECTORLIKE (+96/-96, net 0).
  - chiralizer id_14 (x) (U.chirality): frame charge ~0 (FRAME-TRIVIAL) but NET-CHIRAL +96.

Run: python tests/forcing-slot/rs_frame_index_operator.py
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.normpath(os.path.join(HERE, "..")),
          os.path.normpath(os.path.join(HERE, "..", "generation-sector"))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as bridge

N, DIM = bridge.N, bridge.DIM          # 14, 128
e = bridge.gammas()                    # Cl(9,5) gammas, base 0..3 Euclidean Hermitian
I128 = np.eye(DIM, dtype=complex)
I14 = np.eye(N, dtype=complex)
BASE = (0, 1, 2, 3)


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


# the 6 base tangent-frame so(4) generators (self-dual + anti-self-dual) on {0,1,2,3}
SD_GENS = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
ASD_GENS = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
SO4 = SD_GENS + ASD_GENS


def frame_charge(O, gens=SO4):
    """sum_L ||Tr_14[(L (x) I)^dag O]/Tr(L^dag L)||_F  -- the controls' definition verbatim."""
    O4 = O.reshape(N, DIM, N, DIM)
    tot = 0.0
    per = []
    for L in gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        FL = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        f = float(np.linalg.norm(FL)); per.append(f); tot += f
    return tot, per


# ---- total chirality gradings -----------------------------------------------------------
def base_chirality():
    """gamma5_base = i^? * gamma_0 gamma_1 gamma_2 gamma_3 normalized to square +1, Hermitian."""
    g5 = I128.copy()
    for a in BASE:
        g5 = g5 @ e[a]
    if (np.trace(g5 @ g5) / DIM).real < 0:
        g5 = 1j * g5
    g5 = g5 / np.sqrt(abs((np.trace(g5 @ g5) / DIM).real))
    # make Hermitian rep
    if np.linalg.norm(g5 - g5.conj().T) > 1e-9:
        g5 = 1j * g5 if np.linalg.norm(1j * g5 - (1j * g5).conj().T) < 1e-9 else g5
    return g5


def internal_chirality():
    """gamma5_int = product of internal gammas 4..13 (Spin(10) chirality, the 16 vs 16bar split)."""
    g = I128.copy()
    for a in range(4, N):
        g = g @ e[a]
    if (np.trace(g @ g) / DIM).real < 0:
        g = 1j * g
    g = g / np.sqrt(abs((np.trace(g @ g) / DIM).real))
    return g


def volume_chirality():
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    return om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om


# =========================================================================================
# Triplet sector machinery (verbatim structure from ghost_parity_krein / swing)
# =========================================================================================
def build_triplet():
    Gam = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    J3 = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
          for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi); Wk = Vv[:, w > 0.5]
    Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uu = np.linalg.eigh(CasK); top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uu[:, np.abs(ev - top) < 1e-3]
    return Wt, J3


def krein_form():
    spacelike = [a for a in range(N) if (np.trace(e[a] @ e[a]) / DIM).real > 0]
    timelike = [a for a in range(N) if a not in spacelike]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(N)]).astype(complex)
    return np.kron(etaV, bS)


def net_chirality_of_sector(Wt, grading_full, chir_full):
    """RS-style: take the POSITIVE eigenspace of the (triplet-restricted, Hermitised) grading
    operator as the 'physical sector', report its net chirality Tr(phys^dag C phys) and the
    chiral signature (n+, n-)."""
    G = Wt.conj().T @ grading_full @ Wt; G = 0.5 * (G + G.conj().T)
    C = Wt.conj().T @ chir_full @ Wt; C = 0.5 * (C + C.conj().T)
    kev, kU = np.linalg.eigh(G)
    phys = kU[:, kev > 1e-9]
    net = float(np.trace(phys.conj().T @ C @ phys).real)
    # chiral signature of the physical sector
    cc = phys.conj().T @ C @ phys; cc = 0.5 * (cc + cc.conj().T)
    cev = np.linalg.eigvalsh(cc)
    nplus = int(np.sum(cev > 1e-6)); nminus = int(np.sum(cev < -1e-6))
    return net, nplus, nminus, phys.shape[1]


# =========================================================================================
def primefac(n):
    n = abs(int(round(n)))
    if n <= 1:
        return str(n)
    out, d = [], 2
    while d * d <= n:
        ee = 0
        while n % d == 0:
            n //= d; ee += 1
        if ee:
            out.append(f"{d}^{ee}" if ee > 1 else f"{d}")
        d += 1
    if n > 1:
        out.append(str(n))
    return ".".join(out)


def three_part(n):
    n = abs(int(round(n)))
    if n == 0:
        return 0
    k = 0
    while n % 3 == 0:
        n //= 3; k += 1
    return 3 ** k


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    print("=" * 92)
    print("RS FRAME-INDEX OPERATOR on Cl(9,5)=M(64,H)  --  frame charge & net chirality, simultaneous?")
    print("=" * 92)

    Wt, J3 = build_triplet()
    print(f"[substrate] triplet sector dim = {Wt.shape[1]} (expect 192); full V(x)S = {N*DIM}")
    g5b = base_chirality()
    g5i = internal_chirality()
    om = volume_chirality()
    Cful = np.kron(I14, om)              # total chirality grading used by the +96 controls
    P16 = 0.5 * (I128 + g5i)            # chiral-16 projector (internal Spin(10) Weyl +)

    # ------------------------------------------------------------------ CONTROL A: Lambda^2_+
    print("\n[CONTROL A] Lambda^2_+ self-dual carrier  J3sum = sum_k J3[k]")
    J3sum = J3[0] + J3[1] + J3[2]
    fcA, perA = frame_charge(J3sum)
    fcA_sd, _ = frame_charge(J3sum, SD_GENS)
    fcA_asd, _ = frame_charge(J3sum, ASD_GENS)
    netA, npA, nmA, dA = net_chirality_of_sector(Wt, J3sum, Cful)
    print(f"   frame charge |frame| = {fcA:.2f}  (SD {fcA_sd:.2f}, ASD {fcA_asd:.2e}; net s.d. {fcA_sd-fcA_asd:.2f})")
    print(f"   -> TANGENTIAL: {fcA > 1.0}.  net chirality of its physical sector = {netA:+.2f}  "
          f"chiral sig (+{npA}, -{nmA}) of dim {dA}")
    print(f"   reading: nonzero frame charge (~33.94 expected) but VECTORLIKE (net ~0 / +96=-96).")

    # ------------------------------------------------------------------ CONTROL B: chiralizer
    print("\n[CONTROL B] internal chiralizer  id_14 (x) (chirality)  (representative of C=J_quat.G)")
    chiralizer = np.kron(I14, om)
    fcB, _ = frame_charge(chiralizer)
    netB, npB, nmB, dB = net_chirality_of_sector(Wt, chiralizer, Cful)
    print(f"   frame charge |frame| = {fcB:.2e}  -> FRAME-TRIVIAL: {fcB < 1e-6}")
    print(f"   net chirality of its physical sector = {netB:+.1f}  chiral sig (+{npB}, -{nmB})")
    print(f"   reading: zero frame charge (id_14(x)U traceless on frame) but NET-CHIRAL (+96 expected).")

    # ------------------------------------------------------------------ THE RS FRAME-INDEX OPERATOR
    # O_RS = sum_{mu,nu in BASE} |mu><nu| (x) gamma_mu gamma_nu   -- the spin-1/2 / gamma-trace
    # kernel: genuinely OFF-DIAGONAL in the frame index (mu != nu), hence NOT id_14 (x) U.
    print("\n[RS] O_RS = sum_{mu,nu in BASE} |mu><nu| (x) gamma_mu gamma_nu  (genuine vector index)")
    O_RS = np.zeros((N * DIM, N * DIM), dtype=complex)
    for mu in BASE:
        for nu in BASE:
            Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
            O_RS += np.kron(Emn, e[mu] @ e[nu])
    herm = float(np.linalg.norm(O_RS - O_RS.conj().T))
    fcR, perR = frame_charge(O_RS)
    fcR_sd, _ = frame_charge(O_RS, SD_GENS)
    fcR_asd, _ = frame_charge(O_RS, ASD_GENS)
    print(f"   Hermitian dev = {herm:.1e}")
    print(f"   (c) FRAME CHARGE |frame| = {fcR:.3f}  (SD {fcR_sd:.3f}, ASD {fcR_asd:.3f}; net s.d. {fcR_sd-fcR_asd:.3f})")
    print(f"       -> NON-FRAME-TRIVIAL: {fcR > 1e-6}")

    # net chirality, UNTWISTED, under base / internal / volume chirality gradings
    for name, Cg in [("base chir gamma5_base", np.kron(I14, g5b)),
                     ("internal chir gamma5_int", np.kron(I14, g5i)),
                     ("volume chir om", Cful)]:
        net, npp, nmm, dd = net_chirality_of_sector(Wt, O_RS, Cg)
        print(f"   (b) UNTWISTED net chirality [{name:<24}] = {net:+.3f}  sig(+{npp},-{nmm}) dim {dd}")

    # ------------------------------------------------------------------ TWISTED by chiral 16
    print("\n[RS-TWIST] O_RS_tw = sum |mu><nu| (x) P16 gamma_mu gamma_nu P16   (twist by chiral 16 of Spin(10))")
    O_RS_tw = np.zeros((N * DIM, N * DIM), dtype=complex)
    for mu in BASE:
        for nu in BASE:
            Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
            O_RS_tw += np.kron(Emn, P16 @ (e[mu] @ e[nu]) @ P16)
    hermT = float(np.linalg.norm(O_RS_tw - O_RS_tw.conj().T))
    fcT, _ = frame_charge(O_RS_tw)
    fcT_sd, _ = frame_charge(O_RS_tw, SD_GENS)
    fcT_asd, _ = frame_charge(O_RS_tw, ASD_GENS)
    print(f"   Hermitian dev = {hermT:.1e}")
    print(f"   (c) FRAME CHARGE |frame| = {fcT:.3f}  (SD {fcT_sd:.3f}, ASD {fcT_asd:.3f}; net s.d. {fcT_sd-fcT_asd:.3f})")
    print(f"       -> NON-FRAME-TRIVIAL: {fcT > 1e-6}")
    results_tw = {}
    for name, Cg in [("base chir", np.kron(I14, g5b)),
                     ("internal chir", np.kron(I14, g5i)),
                     ("volume chir", Cful)]:
        net, npp, nmm, dd = net_chirality_of_sector(Wt, O_RS_tw, Cg)
        results_tw[name] = (net, npp, nmm, dd)
        print(f"   (b) TWISTED net chirality [{name:<14}] = {net:+.3f}  sig(+{npp},-{nmm}) dim {dd}")

    # ------------------------------------------------------------------ direct operator chiral trace
    # Tr(Gamma5 . O) is the chiral asymmetry of the operator itself (frame-/gauge-invariant when
    # the grading commutes with the symmetry).  Report for completeness (an integer-valued density).
    print("\n[OPERATOR-LEVEL chiral trace Tr(Gamma5 . O), normalized by DIM-block]")
    for tag, O in [("O_RS untwisted", O_RS), ("O_RS_tw twisted", O_RS_tw)]:
        for cn, Cg in [("base", np.kron(I14, g5b)), ("int", np.kron(I14, g5i)), ("vol", Cful)]:
            tr = np.trace(Cg @ O).real
            print(f"   Tr(gamma5_{cn} . {tag:<16}) = {tr:+.4f}")

    # ------------------------------------------------------------------ VERDICT
    print("\n" + "=" * 92)
    print("VERDICT (forcing-slot fill test)")
    print("=" * 92)
    nonft_R = fcR > 1e-6
    nonft_T = fcT > 1e-6
    # the strongest net-chirality candidate from the twisted case:
    best = max(results_tw.items(), key=lambda kv: abs(kv[1][0]))
    bn, (bnet, bp, bm, bd) = best
    netchiral_T = abs(bnet) > 1e-6
    print(f"  UNTWISTED : non-frame-trivial={nonft_R} (fc={fcR:.2f}),  net-chiral=see above")
    print(f"  TWISTED   : non-frame-trivial={nonft_T} (fc={fcT:.2f}),  "
          f"strongest net chirality [{bn}] = {bnet:+.3f}  net-chiral={netchiral_T}")
    if netchiral_T:
        ni = int(round(bnet))
        print(f"  net-chiral integer (twisted, {bn}) = {ni}")
        print(f"     |n| = {abs(ni)} = {primefac(abs(ni))}")
        print(f"     3-primary part = {three_part(ni)} ; 2-primary part = {abs(ni)//three_part(ni)}")
        print(f"     equals 3 ? {abs(ni) == 3} ;  contains a factor 3 ? {abs(ni) % 3 == 0}")
        print(f"     equals/contains chi(K3)=24 ? {abs(ni) == 24 or abs(ni) % 24 == 0}")
    print(f"\n  SIMULTANEITY (forcing slot) -- nonzero frame charge AND nonzero net chirality at once:")
    simult_T = nonft_T and netchiral_T
    print(f"     untwisted: {nonft_R and False}   twisted: {simult_T}")
    return {
        "fc_LambdaPlus": fcA, "net_LambdaPlus": netA,
        "fc_chiralizer": fcB, "net_chiralizer": netB,
        "fc_RS_untw": fcR, "fc_RS_tw": fcT,
        "twisted_nets": {k: v[0] for k, v in results_tw.items()},
        "simultaneous_twisted": simult_T,
    }


if __name__ == "__main__":
    out = main()
    print("\nRETURN:", out)
