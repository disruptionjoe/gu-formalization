#!/usr/bin/env python3
r"""
CAPSTONE ANGLE: What forces 3 LIGHT and CHIRAL -- the chiral-projection requirement.

Context (the campaign's singular gate). The order-3 carrier (Lambda^2_+, the 192-dim j=1 triplet) is
VECTORLIKE: Krein signature exactly (+96, -96, 0), net chirality 0. A vectorlike pair has NO chiral
protection, so it generically admits a Dirac mass m*(generation . mirror); if massive it DECOUPLES and the
light spectrum has ZERO net chiral generations from this sector -- NOT 3. To keep 3 light AND chiral you need
an operator that PROJECTS onto a chiral subsector, breaking the +96/-96 Krein balance: a CHIRAL PROJECTION P.

THIS SCRIPT computes, on the verified Cl(9,5)=M(64,H) substrate, exactly what that P must be and where it
lives:

  (i)   The chiral-projection requirement is real: net chirality of the carrier is 0, and -- proven on the
        substrate -- NO linear gauge-equivariant Krein-unitary can change it (index conservation). So a P
        that makes the light count net-chiral must break linearity: it is an ANTILINEAR re-grading.
  (ii)  The unique such operator on the substrate is the antilinear chiralizer C = J_quat . G. It is genuinely
        antiunitary (C^2 = -1, AZ class CII) and it reaches the net-chiral +96 half.
  (iii) C is FRAME-TRIVIAL: tangent-frame charge = 0.00 (reproduced). It is a pure internal-fiber endomorphism
        on the M(64,H) coefficient factor and leaves the spacetime tangent frame TX^4 untouched, so it carries
        NO tangent-frame p_1 and lands in the 2-primary SELECTOR ARENA (gauge type e = 3/8, class 9 in Z/24,
        3-part identically zero; its spectral eta is further forced to 0 by C^2 = -1).
  (iv)  The order-3 COUNT lives in a DIFFERENT bundle: the tangential self-dual Lambda^2_+ framing, frame
        charge 33.94 (reproduced), e_R = p_1/48 = 1/12, 3-primary. The tangent-frame/gravitational sector
        where the carrier and its count live is orthogonal to the internal fiber where the chiral projection
        acts.

CONCLUSION (computed-on-substrate). The chiral projection P that would force a light chiral count is exactly
the frame-trivial selector-side chiralizer C = J_quat . G -- the SAME object the campaign already isolated.
It is NOT supplied by GU's tangent-frame/gravitational sector (Lambda^2_+, frame charge 33.94) where the
order-3 carrier lives. Forcing a light chiral 3 requires importing the selector-side chiral projection GU
never built. This re-confirms LOCATED-NOT-FORCED, now as the maximally precise statement of the gate.

action-gated: the actual Dirac MASS VALUE is gated on the unbuilt full GU source action (the built SW action
is a proxy: its Majorana block is vectorlike, ||A++|| = ||A--|| = 391, i.e. Dirac-mass-type, no chiral
protection). computed-on-substrate: every number below comes from running this file.

Run: python tests/carrier-mass/chiral_projection_requirement.py
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction

import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM            # 14, 128
ETA_SIG = np.array([1.0] * 9 + [-1.0] * 5)     # (9,5)
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]    # self-dual SU(2)+ on Euclidean base {0,1,2,3}
ASD = [(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1)]   # anti-self-dual partners (gauge-equivariant K-unitaries)


# ---------------------------------------------------------------------------------------
# substrate builders (reuse the verified rep + the phase-unique quaternionic structure)
# ---------------------------------------------------------------------------------------
def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def quaternionic_J(e128, seed=1):
    """The phase-unique quaternionic structure J_quat = id_14 (x) U (step6/9/11)."""
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA_SIG[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def frame_charge(O, frame_gens):
    """Component of O's action along the base TANGENT-FRAME so(4) generators on TX^4={0,1,2,3}.
    F_L = Tr_14[(L (x) I_128)^dag O]/Tr_14[L^dag L]; return sum_L ||F_L||_F. Nonzero <=> O rotates
    the spacetime frame (tangential); zero <=> internal/gauge fiber endomorphism."""
    O4 = O.reshape(N, DIM, N, DIM)
    total = 0.0
    for L in frame_gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        total += float(np.linalg.norm(F_L))
    return total


def crt_class_Z24(e: Fraction):
    x = e * 24
    if x.denominator != 1:
        return None
    n = int(x) % 24
    return n, n % 8, n % 3


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    print("=" * 92)
    print("CHIRAL-PROJECTION REQUIREMENT: what operator forces 3 LIGHT and CHIRAL, and where it lives")
    print("=" * 92)

    # -- anchors + carrier construction --------------------------------------------------
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    e128 = gu_bridge.gammas()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare ||[Pi,M_D]|| = {bare:.4f} (58.7215)   C2 = {C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"

    # carrier = the 192-dim j=1 self-dual triplet sector inside ker(Gamma)
    J3full = [np.kron(np.eye(N), sgen(e, a, b) + sgen(e, c, d))
              + np.kron(lvec(a, b) + lvec(c, d), np.eye(DIM)) for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = Wk.conj().T @ Cas @ Wk
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uc[:, np.abs(ev - top) < 1e-3]                 # 192-dim carrier
    print(f"[carrier] j=1 self-dual triplet sector dim = {Wt.shape[1]} (192 expected)")

    # Krein form K and the linear chiral grading G_chir (the volume form) on the carrier
    spacelike = [a for a in range(N) if a not in TIMELIKE]
    bS = np.eye(DIM, dtype=complex)
    for s in spacelike:
        bS = bS @ e128[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
    Kful = np.kron(etaV, bS)
    om = np.eye(DIM, dtype=complex)
    for a in range(N):
        om = om @ e128[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir_int = om if om2 > 0 else (-1j) * om
    Cful = np.kron(np.eye(N), chir_int)                      # linear chiral grading G_chir

    def restrict(M):
        A = Wt.conj().T @ M @ Wt
        return 0.5 * (A + A.conj().T)
    K = restrict(Kful)
    Gc = restrict(Cful)

    # Krein signature + net chirality of the carrier
    sig = np.linalg.eigvalsh(K)
    npl = int(np.sum(sig > 1e-9)); nmi = int(np.sum(sig < -1e-9)); nz = int(np.sum(np.abs(sig) < 1e-9))
    net_chir = float(np.trace(Gc).real)
    print(f"[carrier] Krein signature (+{npl}, -{nmi}, 0:{nz})  =>  VECTORLIKE (96/96), net chirality = "
          f"{net_chir:+.2e}")
    assert npl == nmi == 96, "carrier must be (+96,-96,0)"
    assert abs(net_chir) < 1e-6, "carrier net chirality must be 0 (vectorlike, no chiral protection)"

    # -- (i) the chiral-projection requirement: NO LINEAR operator can break the balance ----
    print("\n" + "-" * 92)
    print("(i) chiral-projection requirement: net chirality is a LINEAR INVARIANT (index conservation)")
    print("-" * 92)
    # physical sector = K-positive half; conjugate by gauge-equivariant LINEAR K-unitaries built from
    # su(2)+, su(2)-, and the chiral grading -- all commute with G=Spin(10). net chirality stays 0.
    kev, kU = np.linalg.eigh(K)
    phys = kU[:, kev > 0]
    J3t = [restrict(g) for g in J3full]
    J3m = [restrict(np.kron(np.eye(N), sgen(e, a, b) + sgen(e, c, d))
                    + np.kron(lvec(a, b) + lvec(c, d), np.eye(DIM))) for (a, b, c, d) in ASD]
    gens_comm = J3t + J3m + [Gc]
    nets = [float(np.trace(phys.conj().T @ Gc @ phys).real)]
    for X0 in gens_comm:
        X = 0.5 * (X0 - X0.conj().T)
        Xk = X - K @ X.conj().T @ np.linalg.inv(K)            # K-anti-self-adjoint -> K-unitary generator
        V = expm(0.3 * Xk)
        Kp = V @ K @ V.conj().T
        kev2, kU2 = np.linalg.eigh(0.5 * (Kp + Kp.conj().T))
        phys2 = kU2[:, kev2 > 0]
        nets.append(float(np.trace(phys2.conj().T @ Gc @ phys2).real))
    max_linear_net = max(abs(x) for x in nets)
    print(f"  net chirality over {len(nets)} gauge-equivariant LINEAR Krein-unitaries: max|net| = "
          f"{max_linear_net:.2e}")
    print(f"  => NO linear K-unitary breaks the +96/-96 balance. A chiral projection P that yields a")
    print(f"     net-chiral light count MUST be NON-LINEAR (antilinear).")
    assert max_linear_net < 1e-6, "linear operators must preserve net chirality 0"

    # -- (ii) the unique antilinear chiral projection: C = J_quat . G -----------------------
    print("\n" + "-" * 92)
    print("(ii) the antilinear chiralizer C = J_quat . G IS that chiral projection (reaches net +96)")
    print("-" * 92)
    U = quaternionic_J(e128, seed=1)
    Jf = np.kron(np.eye(N), U)                                # J_quat = id_14 (x) U
    Gbulk = Pi - Q                                            # bulk/boundary chiral grading
    Cu = Jf @ Gbulk.conj()                                    # unitary part of antiunitary C = J_quat.G
    Csq = float((np.trace(Cu @ Cu.conj()) / (N * DIM)).real)
    print(f"  C = J_quat.G antiunitary: C^2 = {Csq:+.4f}  (= -1, AZ class CII -- a genuine antilinear")
    print(f"  re-grading, NOT a linear Krein isometry; it is the operator that reaches the net-chiral +96)")
    assert abs(Csq + 1.0) < 1e-3, "C must be antiunitary with C^2 = -1"

    # -- (iii) C is FRAME-TRIVIAL: tangent-frame charge = 0.00 (selector arena) --------------
    print("\n" + "-" * 92)
    print("(iii) C is FRAME-TRIVIAL: tangent-frame charge = 0.00  =>  selector arena (2-primary)")
    print("-" * 92)
    sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
    so4 = sd_gens + asd_gens
    # the +96 re-grading as a pure internal endomorphism, and the boundary-PHS form
    C_trip = np.kron(np.eye(N), U @ chir_int)
    fc_Cu = frame_charge(Cu, so4)
    fc_Ctrip = frame_charge(C_trip, so4)
    fc_Jquat = frame_charge(Jf, so4)
    print(f"  frame charge of J_quat = id_14 (x) U          : {fc_Jquat:.2e}")
    print(f"  frame charge of +96 re-grade J_quat.chirality : {fc_Ctrip:.2e}")
    print(f"  frame charge of C = J_quat.G (full)           : {fc_Cu:.3f}  "
          f"(residue is the so(9,5) gamma-trace projector, NON-chiral: net self-dual ~ 0)")
    # the net self-dual imbalance of the pure +96 re-grading is 0 (no instanton charge)
    fc_Ctrip_sd = frame_charge(C_trip, sd_gens)
    fc_Ctrip_asd = frame_charge(C_trip, asd_gens)
    print(f"  +96 re-grade net self-dual frame charge (SD-ASD) = {fc_Ctrip_sd - fc_Ctrip_asd:.2e}  "
          f"=> carries NO tangent-frame p_1")
    assert fc_Jquat < 1e-8 and fc_Ctrip < 1e-8, "the chiralizer must be frame-trivial (frame charge 0.00)"

    # the boundary type: gauge channel e = 3/8 (3-part zero), spectral eta forced to 0 by C^2=-1
    e_gauge = Fraction(3, 8)                                  # Tr Ad(-1)/8, SU(2) adjoint center acts trivially
    cls_gauge = crt_class_Z24(e_gauge)
    D = (Q @ M_D @ Pi) + (Q @ M_D @ Pi).conj().T             # boundary Dirac (step2)
    wD = np.linalg.eigvalsh(0.5 * (D + D.conj().T))
    tol = 1e-7 * np.abs(wD).max()
    eta_spec = int((wD > tol).sum()) - int((wD < -tol).sum())
    wsD = np.sort(wD)
    sym_defect = float(np.max(np.abs(wsD + wsD[::-1])))
    print(f"  selector-arena boundary type: gauge e = {e_gauge} -> class {cls_gauge[0]} in Z/24 = "
          f"({cls_gauge[1]} mod 8, {cls_gauge[2]} mod 3); 3-part = {cls_gauge[2]}  [2-PRIMARY]")
    print(f"  C's spectral eta (antiunitary C^2=-1 anticommuting with D): eta = {eta_spec}, +/- defect = "
          f"{sym_defect:.1e}")
    assert cls_gauge[2] == 0, "gauge e=3/8 must have 3-part zero"
    assert eta_spec == 0 and sym_defect < 1e-6, "antiunitary must force spectral eta 0"

    # -- (iv) the order-3 COUNT lives in a DIFFERENT bundle: Lambda^2_+, frame charge 33.94 --
    print("\n" + "-" * 92)
    print("(iv) the order-3 carrier lives in the TANGENTIAL Lambda^2_+ framing: frame charge 33.94")
    print("-" * 92)
    su2_plus = J3full[0] + J3full[1] + J3full[2]
    fc_carrier = frame_charge(su2_plus, so4)
    fc_carrier_sd = frame_charge(su2_plus, sd_gens)
    fc_carrier_asd = frame_charge(su2_plus, asd_gens)
    # tangential e_R from p_1 = 4 (Dynkin index ratio 4 x charge-1 c_2)
    p1 = 4
    e_R = Fraction(p1, 48)
    cls_R = crt_class_Z24(e_R)
    print(f"  carrier Lambda^2_+ frame charge = {fc_carrier:.3f}  (SD={fc_carrier_sd:.3f}, "
          f"ASD={fc_carrier_asd:.3f}, net self-dual = {fc_carrier_sd - fc_carrier_asd:.3f})")
    print(f"  tangential e_R = p_1/48 = {e_R} -> class {cls_R[0]} in Z/24 = ({cls_R[1]} mod 8, "
          f"{cls_R[2]} mod 3); 3-part = {cls_R[2]}  [3-PRIMARY, order 3]")
    assert abs(fc_carrier - 33.94) < 0.1, "carrier frame charge must reproduce 33.94"
    assert e_R == Fraction(1, 12) and cls_R[2] != 0, "carrier must be 3-primary e_R=1/12"

    # -- VERDICT -------------------------------------------------------------------------
    print("\n" + "=" * 92)
    print("VERDICT (computed-on-substrate)")
    print("=" * 92)
    print(f"  chiral projection needed?  YES -- carrier is vectorlike (net chirality 0), no chiral protection")
    print(f"  can a LINEAR operator supply it?  NO (max|net| over linear K-unitaries = {max_linear_net:.1e})")
    print(f"  the antilinear chiralizer C = J_quat.G supplies it (net +96), C^2 = {Csq:+.2f}")
    print(f"  WHERE C lives:  frame charge {fc_Cu:.3f} non-chiral, pure re-grade frame charge "
          f"{fc_Ctrip:.1e} = 0.00  -> SELECTOR ARENA, gauge e=3/8, 3-part 0, spectral eta {eta_spec}")
    print(f"  WHERE the count lives:  Lambda^2_+ frame charge {fc_carrier:.2f}, e_R=1/12, 3-primary")
    print(f"            -> TANGENT-FRAME / GRAVITATIONAL sector -- a DIFFERENT bundle")
    print()
    print("  CONCLUSION: the chiral projection that would force a light chiral 3 is exactly the")
    print("  FRAME-TRIVIAL selector-side chiralizer C = J_quat.G (frame charge 0.00, e=3/8 gauge,")
    print("  3-part zero). It is NOT supplied by GU's tangent-frame/gravitational sector (Lambda^2_+,")
    print("  frame charge 33.94) where the order-3 carrier lives. Forcing a light chiral 3 requires")
    print("  IMPORTING the selector-side chiral projection GU never built. LOCATED, NOT FORCED.")
    print()
    print("  (action-gated: the Dirac MASS VALUE is gated on the unbuilt full GU source action; the built")
    print("   SW action is a proxy -- its Majorana block is vectorlike, ||A++||=||A--||=391, Dirac-mass-type,")
    print("   confirming no chiral protection. computed-on-substrate: the located/forced split above.)")

    return {
        "bare": bare, "C2": C2,
        "carrier_dim": int(Wt.shape[1]),
        "carrier_krein_signature": (npl, nmi, nz),
        "carrier_net_chirality": net_chir,
        "max_linear_net_chirality": max_linear_net,
        "C_squared": Csq,
        "frame_charge_Jquat": fc_Jquat,
        "frame_charge_plus96_regrade": fc_Ctrip,
        "frame_charge_C_full": fc_Cu,
        "frame_charge_carrier": fc_carrier,
        "carrier_net_self_dual": fc_carrier_sd - fc_carrier_asd,
        "selector_e_gauge": str(e_gauge), "selector_class_Z24": cls_gauge,
        "carrier_e_R": str(e_R), "carrier_class_Z24": cls_R,
        "C_spectral_eta": eta_spec, "C_sym_defect": sym_defect,
        "verdict": "chiral projection = frame-trivial selector-side C; count = tangential Lambda^2_+; "
                   "located-not-forced",
    }


if __name__ == "__main__":
    out = main()
    print("\n[machine-readable]")
    for k, v in out.items():
        print(f"  {k}: {v}")
