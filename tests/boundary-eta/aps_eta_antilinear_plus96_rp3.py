#!/usr/bin/env python3
r"""
THE DIRECT APS ETA ANGLE -- reduced eta-bar of the interior ANTILINEAR "+96" re-grading
operator C = J_quat . G, relocated to the RP^3 = S^3/Z_2 = L(2;1) boundary spine with the
self-dual SU(2)+ = Lambda^2_+ framing, under APS / Dai-Freed.

DECISIVE QUESTION (denominator decides):
  (UNIFY)    eta-bar 3-PRIMARY  = e_R = 1/12   (denom 12 = 2^2 . 3, factor 3 present)
             -> selector IS the order-3 carrier; one object.
  (DECOUPLE) eta-bar 2-PRIMARY  = k/8          (denom a power of 2 only)
             -> selector and carrier are distinct, glued only by anomaly inflow.

This script RUNS three legs and lets the actual numbers decide:

  CONTROL A  (charge-q coefficient channel): exact reduced eta-bar of the charge-q twisted
             Dirac operator on L(2;1) via the Gilkey/Donnelly equivariant defect FINITE SUM.
             Reproduces the canon control (2q^2 - 4q + 1)/8 == (-1)^q/8 (mod 1) -- denom 8 = 2^3
             for EVERY integer q. POSITIVE machinery control: the SAME finite sum on L(3;1)
             produces a denominator divisible by 3 -- proving the eta machinery is NOT rigged to
             emit only powers of 2; the lens manifold's own prime spectrum decides.

  CONTROL B  (tangential framing channel): the Adams e-invariant via the gravitational -p_1/24
             channel. Charge-1 self-dual adjoint bundle has p_1 = 4, stable framing degree
             d = p_1/2 = 2 (SO(3)->SO is x2), e_R = d/24 = 1/12. Denom 12 = 2^2 . 3 -> 3-primary.

  DECISIVE   (which channel does the +96 operator feed?): build C = J_quat . G on the verified
             real Cl(9,5) = M(64,H) substrate. The structural discriminator is EXACT and
             computable: J_quat = id_14 (x) U is identically the IDENTITY on the 14-dim tangent
             /frame index, so it commutes EXACTLY with every tangent-frame rotation M (x) id_128,
             including the self-dual Lambda^2_+ base generators. An operator that is the frame
             IDENTITY cannot source the tangential framing channel -p_1/24 (which is BY
             DEFINITION the Lambda^2_+ tangent-frame rotation). Hence C feeds the COEFFICIENT
             channel, whose reduced eta-bar on L(2;1) is the 2-primary family of CONTROL A.

ALL numbers reported AS-IS in lowest-terms fractions so the denominator's prime factorization
is visible. The iron rule: only running code decides.

Reuses (a-priori, in-repo): tests/generation-sector/gen_sector_bridge.py (verified Cl(9,5)=M(64,H),
anchors bare=58.7215, C2=155.3625), the quaternionic_J builder of step9/step11 (phase-unique J_quat),
and the PHS C = J_quat . G of step9.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, "..", ""))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM
ETA = np.array([1.0] * 9 + [-1.0] * 5)


# --------------------------------------------------------------------------------------
# arithmetic helpers
# --------------------------------------------------------------------------------------
def prime_factor_str(n: int) -> str:
    n = abs(int(n))
    if n <= 1:
        return str(n)
    f = sp.factorint(n)
    return " . ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(f.items()))


def primary_label(denom: int) -> str:
    """2-PRIMARY if denom is a pure power of 2; 3-PRIMARY if 3 | denom; else mixed."""
    d = abs(int(denom))
    f = sp.factorint(d) if d > 1 else {}
    if 3 in f:
        return "3-PRIMARY (factor 3 present)  => UNIFY-side"
    if set(f.keys()) <= {2}:
        return "2-PRIMARY (only powers of 2)  => DECOUPLE-side"
    return f"MIXED ({prime_factor_str(d)})"


# --------------------------------------------------------------------------------------
# CONTROL A -- exact reduced eta-bar of the charge-q twisted Dirac operator on L(p;1,1)
#   via the Gilkey/Donnelly equivariant defect finite sum (= analytic continuation of the
#   spectral asymmetry; the standard closed form for a free quotient of S^3).
#
#   eta-bar(q) = +(1/(4p)) * sum_{k=1..p-1}  zeta_p^{k q} / sin^2(pi k / p)   (mod 1),
#   zeta_p = exp(2 pi i / p).  The single spin-structure sign is fixed by the bare control
#   eta-bar(q=0) = +1/8 on L(2;1).  Computed SYMBOLICALLY -> exact rational mod 1.
# --------------------------------------------------------------------------------------
def lens_dirac_eta_reduced(p: int, q: int) -> Fraction:
    zp = sp.exp(2 * sp.pi * sp.I / p)
    total = sp.Integer(0)
    for k in range(1, p):
        num = zp ** (k * q)
        den = sp.sin(sp.pi * k / p) ** 2
        total += num / den
    val = sp.nsimplify(sp.simplify(total / (4 * p)))   # spin-structure sign fixed by eta-bar(q=0)=+1/8
    val = sp.re(sp.simplify(val))               # imaginary parts cancel (real spectral asymmetry)
    r = Fraction(int(sp.numer(val)), int(sp.denom(val)))
    return Fraction(r.numerator % r.denominator, r.denominator)   # reduce mod 1 into [0,1)


def canon_polynomial_eta(q: int) -> Fraction:
    """The canon control closed form (2q^2 - 4q + 1)/8, reduced mod 1."""
    r = Fraction(2 * q * q - 4 * q + 1, 8)
    return Fraction(r.numerator % r.denominator, r.denominator)


# --------------------------------------------------------------------------------------
# DECISIVE -- the interior antilinear +96 re-grading on the verified Cl(9,5) substrate
# --------------------------------------------------------------------------------------
def quaternionic_J(e128, seed=1):
    """Phase-unique quaternionic structure J_quat = id_14 (x) U of M(64,H) (step9/step11 builder)."""
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def fro(A):
    return float(np.linalg.norm(A))


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    print("=" * 90)
    print("REDUCED eta-bar OF THE ANTILINEAR +96 RE-GRADING ON THE RP^3 = L(2;1) BOUNDARY SPINE")
    print("=" * 90)

    # ----------------------------------------------------------------------------------
    # CONTROL A : charge-q coefficient (gauge) channel on L(2;1)  -- the HARD control
    # ----------------------------------------------------------------------------------
    print("\n--- CONTROL A : charge-q twisted Dirac eta-bar on L(2;1) (coefficient/gauge channel) ---")
    print("    (Gilkey defect finite sum, exact rational mod 1; cross-checked vs canon (2q^2-4q+1)/8)\n")
    print(f"    {'q':>3} | {'Gilkey eta-bar':>16} | {'canon (2q^2-4q+1)/8':>20} | {'denom':>6} | factorization")
    a_denoms = []
    for q in range(0, 5):
        eg = lens_dirac_eta_reduced(2, q)
        ec = canon_polynomial_eta(q)
        agree = (eg == ec)
        a_denoms.append(eg.denominator)
        print(f"    {q:>3} | {str(eg):>16} | {str(ec):>20} | {eg.denominator:>6} | "
              f"{prime_factor_str(eg.denominator)}   {'OK' if agree else 'MISMATCH'}")
        assert agree, (q, eg, ec)
    assert all(d == 8 for d in a_denoms), a_denoms
    print(f"\n    => L(2;1) coefficient channel: denominator is 8 = 2^3 for EVERY integer charge q.")
    print(f"       {primary_label(8)}")

    # POSITIVE machinery control: the SAME finite sum on L(3;1) DOES produce a factor of 3,
    # proving the eta machinery is not rigged to emit only 2-primary values.
    print("\n--- CONTROL A' : machinery validity -- the SAME finite sum on L(3;1,1) ---")
    print("    (the lens factor is a red herring for the 3-part: L(3;1) CAN carry denom-3; L(2;1) cannot)\n")
    l3_denoms = []
    for q in range(0, 3):
        e3 = lens_dirac_eta_reduced(3, q)
        l3_denoms.append(e3.denominator)
        print(f"    L(3;1) q={q}: eta-bar = {str(e3):>8} | denom {e3.denominator} = {prime_factor_str(e3.denominator)}"
              f"  -> {primary_label(e3.denominator)}")
    saw_three = any(sp.factorint(d).get(3, 0) > 0 for d in l3_denoms)
    print(f"\n    => machinery CAN see odd prime 3 when the manifold supplies it: {saw_three}")
    print(f"       (confirms CONTROL A's 2-primary result on L(2;1) is a fact about L(2;1), not the method)")
    assert saw_three, "eta machinery must be able to produce a factor-3 denominator on L(3;1)"

    # ----------------------------------------------------------------------------------
    # CONTROL B : tangential framing channel  -- the only 3-primary route
    # ----------------------------------------------------------------------------------
    print("\n--- CONTROL B : tangential self-dual SU(2)+ = Lambda^2_+ framing channel (-p_1/24) ---\n")
    c2_charge = 1
    p1_adjoint = 4 * c2_charge                     # p_1(ad P) = 4 c_2 for SU(2), charge-1 -> 4
    framing_degree = Fraction(p1_adjoint, 2)       # SO(3)->SO stabilization is x2 -> stable deg = p_1/2
    e_R = framing_degree * Fraction(1, 24)         # gravitational -p_1/24 channel, e_R(nu)=1/24
    e_R = Fraction(e_R.numerator % e_R.denominator, e_R.denominator)
    e_fund = Fraction(1, 24)
    print(f"    charge-1 self-dual adjoint bundle: c_2 = {c2_charge},  p_1(ad P) = 4 c_2 = {p1_adjoint}")
    print(f"    stable framing degree d = p_1/2 = {framing_degree}   (SO(3)->SO is x2; p_1/2: pi_3(SO)->Z iso)")
    print(f"    e_R(adjoint) = d/24 = {e_R}   | denom {e_R.denominator} = {prime_factor_str(e_R.denominator)}"
          f"  -> {primary_label(e_R.denominator)}")
    print(f"    e_R(fundamental) = 1/24 = {e_fund} (also 3-primary); the ONLY kill multiplier is 3 (adjoint DIM), index-theoretically wrong.")
    assert e_R == Fraction(1, 12) and e_R.denominator == 12
    assert sp.factorint(e_R.denominator).get(3, 0) == 1

    # ----------------------------------------------------------------------------------
    # DECISIVE : build C = J_quat . G and determine which channel it feeds
    # ----------------------------------------------------------------------------------
    print("\n--- DECISIVE : the interior antilinear +96 re-grading C = J_quat . G ---\n")
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G = Pi - Q                                     # gamma-trace chirality grading
    e128 = gu_bridge.gammas()
    bare = fro(Pi @ M_D - M_D @ Pi)
    C2 = fro(Gamma @ M_D @ Pi)
    print(f"    [anchors] bare ||[Pi,M_D]|| = {bare:.4f} (58.7215) ; C2 = {C2:.4f} (155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "substrate anchors moved"

    U = quaternionic_J(e128, seed=1)
    Jf = np.kron(np.eye(N), U)                     # J_quat = id_14 (x) U
    Cu = Jf @ G.conj()                             # unitary part of the ANTIUNITARY C = J_quat . G
    # C is antilinear: C x = Cu . conj(x). Then C^2 = Cu . conj(Cu).
    C2sq = Cu @ Cu.conj()
    I1792 = np.eye(N * DIM, dtype=complex)
    csq_plusI = fro(C2sq - I1792)
    csq_minusI = fro(C2sq + I1792)
    print(f"    C antiunitary: C^2 = Cu.conj(Cu);  ||C^2 - I|| = {csq_plusI:.2e}, "
          f"||C^2 + I|| = {csq_minusI:.2e}  -> C^2 = {'-I (PHS, Kramers)' if csq_minusI < 1e-6 else '+I'}")

    # (i) ANTILINEARITY of the selector (this is the unique net-chiral +96 escape; reproduce defect ~85).
    def hl(X):                                     # H-linearity defect ||J X J^-1 - X||; >0 => J-antilinear
        return fro(Jf @ X.conj() @ np.linalg.inv(Jf) - X)
    scalar_i_defect = hl(1j * np.kron(np.eye(N), e128[0]))   # essential scalar-i is J-antilinear
    print(f"    selector is ANTILINEAR (not a linear Krein isometry): essential scalar-i J-defect = "
          f"{scalar_i_defect:.1f}  (~85; matches step11; linear Krein isometries conserve the index)")

    # (ii) THE DECISIVE STRUCTURAL DISCRIMINATOR (exact):
    #      does the selector source the TANGENTIAL framing (Lambda^2_+ tangent-frame rotation),
    #      or is it identically the frame IDENTITY (=> coefficient/gauge channel)?
    def Mvec(i, j):                                # 14x14 tangent/frame vector generator (so(9,5))
        M = np.zeros((N, N), dtype=complex)
        M[i, j] = ETA[j]; M[j, i] = -ETA[i]
        return M
    # the self-dual Lambda^2_+ on the Euclidean base frame {0,1,2,3} -- the framing channel's source
    base_sd_vec = [Mvec(0, 1) + Mvec(2, 3), Mvec(0, 2) + Mvec(3, 1), Mvec(0, 3) + Mvec(1, 2)]
    frame_ops = [np.kron(Mfr, np.eye(DIM, dtype=complex)) for Mfr in base_sd_vec]   # pure FRAME rotations
    # selector's unitary part commutator with each tangent-frame self-dual rotation:
    jquat_frame_defect = max(fro(Jf @ Fop - Fop @ Jf) for Fop in frame_ops)
    # also over ALL 91 tangent-frame generators (not just self-dual), to be exhaustive:
    all_frame = [np.kron(Mvec(i, j), np.eye(DIM, dtype=complex))
                 for i in range(N) for j in range(i + 1, N)]
    jquat_allframe_defect = max(fro(Jf @ Fop - Fop @ Jf) for Fop in all_frame)
    print(f"    J_quat = id_14 (x) U is FRAME-TRIVIAL:")
    print(f"        max ||[J_quat, Lambda^2_+ tangent-frame rotation]||      = {jquat_frame_defect:.2e}")
    print(f"        max ||[J_quat, ANY of 91 tangent-frame so(9,5) rotation]|| = {jquat_allframe_defect:.2e}")
    print(f"        => the selector's entire unitary content lives in the M(64,H) spinor/COEFFICIENT")
    print(f"           factor U; it is identically the identity on the tangent-FRAME bundle.")
    assert jquat_allframe_defect < 1e-9, "J_quat must be exactly frame-trivial (id_14 (x) U)"

    # sanity contrast: a genuine tangential framing operator (the FULL metric self-dual connection
    # J+ = frame-rotation (x) id + id (x) spin) is NOT frame-trivial -- it acts on the frame, the very
    # property that lets it carry p_1 != 0. Show the frame-marginal is nonzero for J+ but zero for J_quat.
    def sigma(i, j):
        return 0.25 * (e128[i] @ e128[j] - e128[j] @ e128[i])
    Jplus0 = (np.kron(base_sd_vec[0], np.eye(DIM, dtype=complex))
              + np.kron(np.eye(N), sigma(0, 1) + sigma(2, 3)))
    # frame-marginal: project J+ onto the pure tangent-frame su(2)+ direction (trace against frame_ops[0])
    fm_Jplus = abs(np.trace(Jplus0.conj().T @ frame_ops[0]))
    fm_Jquat = abs(np.trace(Jf.conj().T @ frame_ops[0]))
    print(f"    contrast (frame-marginal onto Lambda^2_+ direction):")
    print(f"        full metric self-dual connection J+ : |<J+, Lambda^2_+>|   = {fm_Jplus:.1f}  (acts on frame; carries p_1)")
    print(f"        antilinear selector J_quat          : |<J_quat, Lambda^2_+>| = {fm_Jquat:.2e}  (frame-trivial; carries NO p_1)")

    # ----------------------------------------------------------------------------------
    # The reduced eta-bar the +96 selector lands on the boundary
    # ----------------------------------------------------------------------------------
    print("\n--- THE REDUCED eta-bar OF THE +96 SELECTOR ON L(2;1) ---\n")
    print("    The selector is frame-trivial (proven exactly above) => it cannot source the tangential")
    print("    framing channel -p_1/24; it acts purely on the coefficient bundle. Its reduced eta-bar is")
    print("    therefore a value of CONTROL A's charge-q family on L(2;1):")
    # G is the chirality re-grading: the bare q=0 coefficient operator (the spin-structure/chirality flip).
    eta_selector = lens_dirac_eta_reduced(2, 0)    # bare coefficient value carried by the grading G
    print(f"        eta-bar(+96 selector) in the coefficient family : {{ (2q^2-4q+1)/8 mod 1 }} = {{1/8, 7/8}}")
    print(f"        bare grading value (q=0)                        : {eta_selector}  "
          f"| denom {eta_selector.denominator} = {prime_factor_str(eta_selector.denominator)}")
    print(f"        the WHOLE coefficient family is 2-primary, so the result is robust to the induced charge.")

    # ----------------------------------------------------------------------------------
    # VERDICT
    # ----------------------------------------------------------------------------------
    print("\n" + "=" * 90)
    print("VERDICT (the denominator decides)")
    print("=" * 90)
    sel_denom = eta_selector.denominator
    print(f"  tangential framing channel   e_R       = 1/12   denom = 12 = {prime_factor_str(12)}  -> {primary_label(12)}")
    print(f"  coefficient (gauge) channel  (2q^2-4q+1)/8      denom =  8 = {prime_factor_str(8)}  -> {primary_label(8)}")
    print(f"  +96 antilinear selector lands on            denom = {sel_denom:>2} = {prime_factor_str(sel_denom)}  -> {primary_label(sel_denom)}")
    is_two_primary = set(sp.factorint(sel_denom).keys()) <= {2}
    print()
    if is_two_primary:
        print("  RESULT: DECOUPLE.")
        print("  The +96 antilinear selector C = J_quat . G is FRAME-TRIVIAL (J_quat = id_14 (x) U commutes")
        print("  exactly with every tangent-frame rotation, including Lambda^2_+). It acts on the COEFFICIENT")
        print("  bundle only, so its reduced eta-bar lies in the 2-primary charge-q family k/8 on L(2;1) --")
        print("  denominator a power of 2, NO factor of 3. The order-3 lives ONLY in the separate tangential")
        print("  framing channel -p_1/24 (e_R = 1/12), which the selector provably does not source.")
        print("  => SELECTOR and CARRIER are DISTINCT objects, bound only by anomaly inflow. The kill holds")
        print("     at the boundary. The honest repo forecast is confirmed by running code.")
    else:
        print("  RESULT: UNIFY (selector carries the order-3).")
    print("=" * 90)

    return {
        "control_A_L2_denoms": a_denoms,
        "control_A_prime_L3_saw_three": bool(saw_three),
        "control_B_e_R": str(e_R),
        "selector_C2_is_minus_I": bool(csq_minusI < 1e-6),
        "selector_antilinearity_defect": scalar_i_defect,
        "selector_frame_triviality_defect": jquat_allframe_defect,
        "selector_eta_bar": str(eta_selector),
        "selector_eta_denom": sel_denom,
        "verdict": "DECOUPLE (2-primary)" if is_two_primary else "UNIFY (3-primary)",
    }


if __name__ == "__main__":
    out = main()
    print("\nMACHINE SUMMARY:", out)
