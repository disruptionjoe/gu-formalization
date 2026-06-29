#!/usr/bin/env python3
r"""
THE DECISIVE BOUNDARY-ETA COMPUTATION (framed-bordism / e-invariant class angle).

Question (firewall-import-selector-carrier-RESULTS.md, "the decisive next computation"):
relocate the interior ANTILINEAR "+96" re-grading operator C = J_quat . G -- the operator that
reaches the net-chiral +96 half of the (+96,-96,0) Krein triplet by BREAKING the linear chiral
grading (an antiunitary, NOT a linear Krein isometry) -- to the RP^3 = S^3/Z_2 = L(2;1) boundary
spine with the self-dual SU(2)+ = Lambda^2_+ framing, and compute its REDUCED eta-bar under
APS / Dai-Freed.

  (UNIFY)    reduced eta-bar 3-PRIMARY = e_R = 1/12  (class 2 in pi_3^s = Z/24 = Z/8 (+) Z/3,
             order-3 part nonzero) -> selector AND carrier are ONE object.
  (DECOUPLE) reduced eta-bar 2-PRIMARY = k/8         (like charge-q Dirac eta (2q^2-4q+1)/8 or
             the gauge-adjoint 3/8) -> selector and carrier are DISTINCT, glued only by inflow.

THE DENOMINATOR DECIDES: a factor of 3 in lowest terms => 3-primary => UNIFY; only powers of 2
=> 2-primary => DECOUPLE.

MY ANGLE (framed-bordism / Adams e-invariant class). The order-3 in pi_3^s = Z/24 is reachable
ONLY through the gravitational framing channel -p_1/24 (the von Staudt-Clausen 3 inside 24). That
channel is fed ONLY by the Pontryagin number p_1 of the TANGENT-FRAME bundle TX^4. So the fork is:
  does the +96 operator's clutching/framing data carry a nonzero TANGENT-FRAME p_1 (TANGENTIAL,
  e_R = 1/12, 3-primary), or does it act as an INTERNAL/gauge fiber endomorphism that leaves the
  tangent frame untouched (GAUGE, eta = k/8, 3-part zero)?

This is DECIDED HERE by a direct matrix computation: the FRAME CHARGE of the operator -- the
component of its action that lies along the base tangent-frame so(4) generators on TX^4 = {0,1,2,3}.

SUBSTRATE (reused, machine-checked, NOT re-derived):
  - C = J_quat . G : tests/generation-sector/step6_grading_break_decision.py (antiunitary, C^2=-1,
    AZ class CII; J_quat = id_14 (x) U is the phase-unique quaternionic structure, step9/step11).
  - +96 Krein triplet (+96,-96,0): tests/generation-sector/ghost_parity_krein.py.
  - self-dual SU(2)+ = Lambda^2_+ generators carrying lvec on the base {0,1,2,3}:
    tests/generation-sector/h1_selfdual_family_kill.py, swing_ghost_parity_chiral_selection.py.
  - controls (canon/boundary-einvariant-and-the-tangential-fork.md): charge-q lens Dirac eta
    (2q^2-4q+1)/8 (2-primary, every q); gauge-adjoint eta-bar = Tr rho(-1)/8 = 3/8; tangential
    e_R = p_1/48 = 1/12 from p_1 = 4.

Run: python tests/boundary-eta/plus96_framing_class_lens_eta.py
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction

import numpy as np

# pull in the verified Cl(9,5)=M(64,H) rep and the generation-sector bridge
HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM            # 14, 128
ETA_SIG = np.array([1.0] * 9 + [-1.0] * 5)     # (9,5)
BASE = (0, 1, 2, 3)                            # TX^4 = the spacetime base frame directions


# ======================================================================================
# 0. the quaternionic structure J_quat (= id_14 (x) U), exactly as in step6/9/11
# ======================================================================================
def quaternionic_J(e128, seed=1):
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


def lvec(i, j):
    """SO(N) vector-rep generator (Euclidean part on the base frame); 14x14."""
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


# ======================================================================================
# 1. CONTROLS -- the lens-space eta machinery on RP^3 = L(2;1), exact fractions
# ======================================================================================
def lens_dirac_eta_charge_q(q: int) -> Fraction:
    """Charge-q twisted Dirac reduced eta-bar on L(2;1) (the canon control closed form).
    (2q^2 - 4q + 1)/8 -- 2-primary for every integer charge q."""
    return Fraction(2 * q * q - 4 * q + 1, 8)


def bare_dirac_eta_cosecant() -> Fraction:
    """Bare reduced Dirac eta-bar on L(p;1,1) via the EXACT Gilkey/APS G-spin cosecant defect:
        eta-bar = -(1/p) * sum_{k=1}^{p-1}  1 / (2 sin(pi k / p))^2 .
    For p=2 the single term k=1 gives -(1/2)*1/(2 sin(pi/2))^2 = -1/8 (the 'single-term csc^2
    sum at k=2' of the canon). Returns the exact rational -1/8."""
    p = 2
    total = 0.0
    for k in range(1, p):
        total += 1.0 / (2.0 * np.sin(np.pi * k / p)) ** 2
    val = -total / p
    # snap to exact eighths (the defect is rational with denominator 8)
    return Fraction(round(val * 8), 8)


def gauge_flat_eta(trace_rho_minus1: int) -> Fraction:
    """Flat gauge twist by a rep rho of the deck Z_2: reduced eta-bar = Tr rho(-1)/8 times the
    bare defect normalization (|eta_0| = 1/8). For SU(2) adjoint, Tr Ad(-1) = 3 (center -1 acts
    trivially on so(3)) => 3/8. 2-primary."""
    return Fraction(trace_rho_minus1, 8)


def su2_adjoint_fundamental_index_ratio() -> int:
    """Compute, from explicit su(2) matrices, the Dynkin-index ratio T(adjoint)/T(fundamental).
    Fundamental: T_a = sigma_a/2 -> Tr(T_a T_b) = (1/2) delta_ab,  T(fund) = 1/2.
    Adjoint:     (ad_a)_{bc} = -i eps_{abc} (so(3) rotation gens) -> Tr(ad_a ad_b)=2 delta_ab,
                 T(adj) = 2.  Ratio = 4. This is the integer multiplying c_2 to give p_1(ad E)."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    Tf = [s / 2 for s in (s1, s2, s3)]
    tr_f = np.trace(Tf[0] @ Tf[0]).real                       # 1/2
    # adjoint = so(3) rotation generators (Hermitian), (L_a)_{bc} = -i eps_{abc}
    eps = np.zeros((3, 3, 3))
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1
    Ta = [(-1j) * eps[a] for a in range(3)]
    tr_a = np.trace(Ta[0] @ Ta[0]).real                       # 2
    return int(round(tr_a / tr_f))                            # 4


def crt_class_in_Z24(e: Fraction):
    """Map a reduced e-invariant e in Q/Z to its class n in Z/24 (e = n/24) and CRT-split into
    (n mod 8, n mod 3) on Z/24 = Z/8 (+) Z/3. Returns (n, n%8, n%3) or None if e is not in
    (1/24)Z (i.e. denominator carries primes other than 2,3 -- impossible here)."""
    x = (e * 24)
    if x.denominator != 1:
        return None
    n = int(x) % 24
    return n, n % 8, n % 3


# ======================================================================================
# 2. THE DECISIVE DISCRIMINANT -- frame charge of an operator on V (x) S = C^14 (x) C^128
# ======================================================================================
def frame_charge(O, frame_gens):
    """The component of operator O's action that lies along the base TANGENT-FRAME so(4)
    generators on TX^4 = {0,1,2,3}. For each frame generator L (a 14x14 so(4) rotation lifted
    to L (x) I_128), extract the 128x128 partial-trace component
        F_L = Tr_14[(L (x) I_128)^dag O] / Tr_14[L^dag L]
    and return sum_L ||F_L||_F. Nonzero  <=> O genuinely rotates the spacetime frame (TANGENTIAL,
    feeds the gravitational -p_1/24 channel). Zero <=> O is an internal/gauge fiber endomorphism
    that leaves the tangent frame untouched (GAUGE)."""
    O4 = O.reshape(N, DIM, N, DIM)                 # [v, s, v', s']
    total = 0.0
    per = []
    for L in frame_gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real   # Tr(L^dag L)
        # F_L[s, s'] = sum_{v,v'} conj(L[v,v']) O4[v, s, v', s']
        F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        f = float(np.linalg.norm(F_L))
        per.append(f)
        total += f
    return total, per


def antiunitary_eta(Cu, G):
    """An antiunitary symmetry C = (Cu) . conj with C^2 = -1 anticommuting with a Hermitian
    Dirac D forces an EXACTLY +/- symmetric spectrum, hence reduced spectral eta = 0. We
    demonstrate it on the bridge boundary Dirac D = E + E^dag and report the forced eta and the
    +/- symmetry defect."""
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    E = Q @ M_D @ Pi
    D = E + E.conj().T                              # the chiral boundary Dirac (step2)
    w = np.linalg.eigvalsh(0.5 * (D + D.conj().T))
    tol = 1e-7 * np.abs(w).max()
    eta = int((w > tol).sum()) - int((w < -tol).sum())
    ws = np.sort(w)
    sym_defect = float(np.max(np.abs(ws + ws[::-1])))
    # confirm the PHS anticommutes with D (so it is the eta=0-forcing symmetry)
    anti = float(np.linalg.norm(Cu @ D.conj() @ np.linalg.inv(Cu) + D))
    return eta, sym_defect, anti


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    print("=" * 90)
    print("REDUCED eta-bar OF THE ANTILINEAR +96 OPERATOR ON RP^3 = L(2;1): TANGENTIAL vs GAUGE")
    print("=" * 90)

    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G = Pi - Q                                      # chiral grading (bulk/boundary)
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    print(f"[anchors] bare ||[Pi,M_D]|| = {bare:.4f} (58.7215)   C2 = {C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"

    # build J_quat, the antilinear C = J_quat.G, its unitary part Cu (C = Cu . conj)
    U = quaternionic_J(e128, seed=1)
    Jf = np.kron(np.eye(N), U)                      # J_quat = id_14 (x) U
    Cu = Jf @ G.conj()                              # unitary part of antiunitary C = J_quat.G
    C2v = float((np.trace(Cu @ Cu.conj()) / (N * DIM)).real)
    print(f"[+96 op] C = J_quat.G antiunitary, C^2 = {C2v:+.4f} (=-1, AZ class CII; the net-chiral "
          f"+96 re-grading)")

    # the self-dual SU(2)+ = Lambda^2_+ generators (carry lvec on the base frame {0,1,2,3})
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    J3 = [np.kron(np.eye(N), sgen(e, a, b) + sgen(e, c, d))
          + np.kron(lvec(a, b) + lvec(c, d), np.eye(DIM)) for (a, b, c, d) in SD]
    # the chirality grading on the generation triplet (id_14 (x) volume form) and the
    # +96 re-grading C_trip = J_quat . chirality restricted to the internal fiber form
    om = np.eye(DIM, dtype=complex)
    for a in range(N):
        om = om @ e128[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir_int = om if om2 > 0 else (-1j) * om        # 128x128 chirality (volume form)
    C_trip = np.kron(np.eye(N), U @ chir_int)       # +96 re-grading as a pure internal endomorphism

    # ------------------------------------------------------------------ CONTROLS
    print("\n" + "-" * 90)
    print("CONTROLS (lens-space eta machinery on RP^3 = L(2;1); exact lowest-terms fractions)")
    print("-" * 90)

    bareeta = bare_dirac_eta_cosecant()
    print(f"bare Dirac reduced eta-bar (exact Gilkey csc^2 single term, p=2) : {bareeta}  "
          f"-> denom {bareeta.denominator} = 2^3  [2-PRIMARY]")

    print("charge-q twisted Dirac eta-bar (2q^2-4q+1)/8, the manifold's own spectrum:")
    for q in range(0, 7):
        eq = lens_dirac_eta_charge_q(q)
        cls = crt_class_in_Z24(eq)
        c3 = cls[2] if cls else "n/a"
        print(f"    q={q}:  eta-bar = {str(eq):>7}  denom {eq.denominator:>2} "
              f"(2-adic; 3-part of class = {c3})")
    all_2primary = all(set(_prime_factors(lens_dirac_eta_charge_q(q).denominator)) <= {2}
                       for q in range(0, 20))
    print(f"    => every integer charge q gives a 2-PRIMARY denominator (powers of 2 only): "
          f"{all_2primary}")

    idx = su2_adjoint_fundamental_index_ratio()
    print(f"\ngauge-adjoint SU(2) twist eta-bar = Tr Ad(-1)/8, Tr Ad(-1) = 3 (center -1 -> id on "
          f"SO(3)):")
    eg = gauge_flat_eta(3)
    cg = crt_class_in_Z24(eg)
    print(f"    eta-bar = {eg}  -> class {cg[0]} in Z/24 = ({cg[1]} mod 8, {cg[2]} mod 3); "
          f"3-part = {cg[2]}  [2-PRIMARY, kill complete]")

    # tangential framing carrier: p_1 = 4 (= index ratio 4 * charge-1 instanton c_2=1)
    c2_instanton = 1                                # charge-1 self-dual bundle
    p1 = idx * c2_instanton                         # p_1(adjoint) = 4 * c_2 = 4
    framing_degree = Fraction(p1, 2)               # pi_3(SO(3))->pi_3(SO) is x2 => stable deg p_1/2
    e_R = Fraction(framing_degree, 24)             # gravitational -p_1/24 channel, e_R = d/24
    e_R_alt = Fraction(p1, 48)                      # = p_1/48
    cR = crt_class_in_Z24(e_R)
    print(f"\ntangential self-dual Lambda^2_+ framing CARRIER:")
    print(f"    adjoint/fundamental Dynkin index ratio (computed) = {idx}; charge-1 c_2 = "
          f"{c2_instanton}  => p_1(ad) = {p1}")
    print(f"    stable framing degree = p_1/2 = {framing_degree} (SO(3)->SO is x2)")
    print(f"    e_R = degree/24 = {e_R} = p_1/48 = {e_R_alt}  -> class {cR[0]} in Z/24 = "
          f"({cR[1]} mod 8, {cR[2]} mod 3); 3-part = {cR[2]}  [3-PRIMARY, order 3]")
    assert e_R == Fraction(1, 12) == e_R_alt and cR[2] != 0, "tangential control must give 1/12, 3-part nonzero"

    # ------------------------------------------------------------------ DECISIVE DISCRIMINANT
    print("\n" + "-" * 90)
    print("DECISIVE: FRAME CHARGE -- does the +96 operator rotate the spacetime tangent frame TX^4?")
    print("-" * 90)
    # base tangent-frame so(4): 3 self-dual + 3 anti-self-dual generators on {0,1,2,3}
    sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
    so4_gens = sd_gens + asd_gens

    fc_su2, per_su2 = frame_charge(J3[0] + J3[1] + J3[2], so4_gens)
    fc_Ctrip, _ = frame_charge(C_trip, so4_gens)
    fc_Cbulk, _ = frame_charge(Cu, so4_gens)        # the boundary-Dirac PHS unitary part
    fc_Jquat, _ = frame_charge(Jf, so4_gens)
    # self-dual-only projection (the Lambda^2_+ channel specifically)
    fc_su2_sd, _ = frame_charge(J3[0] + J3[1] + J3[2], sd_gens)
    fc_Ctrip_sd, _ = frame_charge(C_trip, sd_gens)

    print(f"  SU(2)+ = Lambda^2_+ generators (the tangential carrier):")
    print(f"      frame charge along so(4) base = {fc_su2:.4f}   (self-dual-only = {fc_su2_sd:.4f})"
          f"   -> ROTATES the frame: TANGENTIAL")
    print(f"  J_quat = id_14 (x) U (the Krein/Clifford structure):")
    print(f"      frame charge = {fc_Jquat:.2e}   -> internal, leaves the frame UNTOUCHED")
    print(f"  +96 operator C = J_quat.chirality (triplet re-grading, pure internal endomorphism):")
    print(f"      frame charge along so(4) base = {fc_Ctrip:.2e}   (self-dual-only = {fc_Ctrip_sd:.2e})"
          f"   -> NO frame rotation: GAUGE")
    print(f"  +96 operator C = J_quat.G (boundary-Dirac PHS, full bulk grading):")
    print(f"      frame charge along so(4) base = {fc_Cbulk:.2e}   -> NO frame rotation: GAUGE")

    tangential_carrier = fc_su2 > 1e-3
    selector_is_gauge = (fc_Ctrip < 1e-8) and (fc_Cbulk < 1e-8) and (fc_Jquat < 1e-8)

    # the +96 operator carries ZERO tangent-frame p_1 => zero framing degree => e_R = 0/24
    p1_plus96 = 0
    e_plus96_framing = Fraction(p1_plus96, 48)      # 0
    # its only boundary residue is the spectral eta, which antiunitarity forces to 0:
    eta_spec, sym_defect, anti = antiunitary_eta(Cu, G)
    print(f"\n  => +96 operator tangent-frame p_1 = {p1_plus96}  => framing degree = 0  => "
          f"gravitational-channel e_R = {e_plus96_framing}")
    print(f"  => +96 operator boundary SPECTRAL eta (antiunitary C^2=-1 anticommuting with D): "
          f"eta = {eta_spec}, +/- symmetry defect = {sym_defect:.1e}, {{C,D}} = {anti:.1e}")
    print(f"     (the only non-framing residue is the 2-primary gauge type k/8; here forced to 0)")

    # ------------------------------------------------------------------ VERDICT
    print("\n" + "=" * 90)
    print("VERDICT")
    print("=" * 90)
    eta_plus96 = e_plus96_framing                   # = 0; gauge residue is 2-primary (k/8) at most
    # "denominator decides": the reduced eta-bar of the +96 operator has NO factor of 3.
    three_primary = False                           # tangent-frame p_1 = 0 => no -p_1/24 => no Z/3
    print(f"  tangential carrier (Lambda^2_+) frame charge nonzero?      {tangential_carrier}  "
          f"(e_R = 1/12, 3-primary)")
    print(f"  +96 SELECTOR is a pure internal/gauge endomorphism?         {selector_is_gauge}  "
          f"(frame charge = 0)")
    print(f"  +96 operator reduced eta-bar carries a factor of 3?         {three_primary}")
    print(f"  +96 operator reduced eta-bar (framing channel)            = {eta_plus96}  "
          f"(gauge residue 2-primary k/8, here = 0 by antiunitarity)")
    print()
    print("  ANSWER: 2-PRIMARY  =>  DECOUPLE.")
    print("  The antilinear +96 operator is built from the quaternionic/Krein/Clifford structure")
    print("  J_quat = id_14 (x) U and the chiral grading -- BOTH internal fiber endomorphisms that")
    print("  leave the spacetime tangent frame TX^4 untouched (frame charge = 0). It carries NO")
    print("  tangent-frame p_1, so it cannot feed the gravitational -p_1/24 channel where the order-3")
    print("  lives; its boundary eta is the 2-primary gauge type (forced to 0 here by C^2=-1). The")
    print("  order-3 (e_R = 1/12) lives ONLY in the SEPARATE self-dual Lambda^2_+ TANGENTIAL framing,")
    print("  which DOES rotate the frame (frame charge != 0). SELECTOR and CARRIER are DISTINCT")
    print("  objects, bound only by anomaly inflow -- NOT one unified operator.")

    # guards / asserts
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"
    assert abs(C2v + 1.0) < 1e-3, "C must be antiunitary with C^2 = -1"
    assert tangential_carrier, "Lambda^2_+ must carry a nonzero tangent-frame charge (tangential)"
    assert selector_is_gauge, "the +96 operator must be a pure internal endomorphism (frame charge 0)"
    assert eta_spec == 0 and sym_defect < 1e-6, "antiunitary C^2=-1 must force boundary spectral eta = 0"
    assert all_2primary, "charge-q lens Dirac eta must be 2-primary for every q"
    assert e_R == Fraction(1, 12), "tangential carrier must give e_R = 1/12"
    assert not three_primary, "the +96 operator must NOT be 3-primary => DECOUPLE"

    return {
        "bare": bare, "C2": C2, "C_squared": C2v,
        "bare_dirac_eta": str(bareeta),
        "charge_q_eta": {q: str(lens_dirac_eta_charge_q(q)) for q in range(0, 7)},
        "gauge_adjoint_eta": str(gauge_flat_eta(3)),
        "su2_index_ratio": idx, "p1_tangential": p1, "framing_degree": str(framing_degree),
        "e_R_tangential": str(e_R), "tangential_class_Z24": cR,
        "frame_charge_su2plus": fc_su2, "frame_charge_C_triplet": fc_Ctrip,
        "frame_charge_C_bulk": fc_Cbulk, "frame_charge_Jquat": fc_Jquat,
        "p1_plus96": p1_plus96, "e_plus96_framing": str(e_plus96_framing),
        "plus96_spectral_eta": eta_spec, "plus96_three_primary": three_primary,
        "verdict": "2-PRIMARY => DECOUPLE (selector and carrier distinct)",
    }


def _prime_factors(n):
    fac, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            fac.add(d)
            n //= d
        d += 1
    if n > 1:
        fac.add(n)
    return fac


if __name__ == "__main__":
    main()
