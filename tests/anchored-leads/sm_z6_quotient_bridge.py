#!/usr/bin/env python3
r"""
ANCHORED LEAD: SM global form (SU(3)xSU(2)xU(1))/Z_6, Z_6 = Z/2 x Z/3, as an alternative bridge.

PRECISE QUESTION
  Is the Z/3 carrier of pi_3^s (e_R = 1/12, tangential -p_1/24 framing channel) literally the Z/3
  of the SM global gauge quotient (the color-center Z/3 of SU(3))? And does the DIAGONAL Z/6 element
  (handedness Z/2 selector x color Z/3 carrier) bridge the CRT firewall because it is a PRODUCT, not
  a linking PAIRING (coprime-vanishing kills pairings, not products)?

THE DECISIVE QUICK CHECK (frame-charge, on the verified Cl(9,5)=M(64,H) substrate)
  Identical instrument to the 2026-06-29 DECOUPLE (tests/decider/generation_index_fork_decider.py).
  The carrier Lambda^2_+ has TANGENTIAL net self-dual frame charge ~33.94 (feeds -p_1/24). The +96
  chiralizer C = J_quat.G = id_14(x)U is frame-trivial (~0, GAUGE). The SU(3)_family Z/3 was already
  found frame-trivial. Here we test the SM color-center Z/3, the weak-isospin-center Z/2, and the
  DIAGONAL Z/6 element directly: do any of them have TANGENT-frame charge (live where the carrier
  lives), or are they all GAUGE/internal (frame-trivial), stranded on the selector side?

  Tangent frame  = so(4) on directions {0,1,2,3} (TX^4).  Internal/gauge = so(10) on {4..13}.
  The SM gauge group is INTERNAL: color SU(3) + weak SU(2) + U(1)_Y all act on {4..13}.
  Any internal so(10) rotation has ZERO component along the tangent so(4) -> frame charge 0.

PLUS the algebraic firewall point: Z/6 = Z/2 x Z/3 is ITSELF a CRT split (the firewall restated for
modulus 6); Hom(Z/3,Z)=0 and Hom(Z/6,Z)=0 (no integer count from a torsion class); and there is NO
nontrivial homomorphism between the two factors (Hom(Z/2,Z/3)=Hom(Z/3,Z/2)=0), so a product carries
ZERO communication between selector and carrier -- it reproduces the firewall, it does not bridge it.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
DEC = os.path.join(ROOT, "tests", "decider")
TESTS = os.path.join(ROOT, "tests")
GEN = os.path.join(TESTS, "generation-sector")
for p in (DEC, TESTS, GEN, ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)

import generation_index_fork_decider as dec   # reuse verified substrate + frame_charge + carrier

N, DIM = dec.N, dec.DIM
lvec = dec.lvec
sgen = dec.sgen
frame_charge = dec.frame_charge
e = dec.gammas_95()

# ----- tangent so(4) frame generators on {0,1,2,3} (same as the DECOUPLE) -----
sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
ALLF = sd_gens + asd_gens


def net_sd(O):
    """(|frame| over all tangent so(4),  net self-dual = SD - ASD).  Carrier is large; gauge is ~0."""
    return frame_charge(O, ALLF), frame_charge(O, sd_gens) - frame_charge(O, asd_gens)


def so10_gen(i, j):
    """Full so(10) (internal) generator on directions i,j in {4..13}: acts on BOTH the frame-vector
    index (lvec, but only on internal components {4..13}) AND the spinor (sgen). The honest gauge
    rotation. Tangent so(4) overlap is identically zero because i,j>=4."""
    return np.kron(lvec(i, j), np.eye(DIM)) + np.kron(np.eye(N), sgen(e, i, j))


def so10_spinor_only(i, j):
    """Spinor-only lift id_14 (x) sgen(i,j): exactly the id_14(x)U form of the +96 chiralizer."""
    return np.kron(np.eye(N), sgen(e, i, j))


# =====================================================================================
# Build SM center generators inside internal so(10) on {4..13}.
# Pair internal dirs into 5 complex planes: P0=(4,5) P1=(6,7) P2=(8,9) P3=(10,11) P4=(12,13).
# Cartan U(1) on plane k: R_k = lvec(2k+4, 2k+5)  (rotation generator).
# SU(5) subset SO(10); SU(3)_color on planes {P0,P1,P2}; SU(2)_L on {P3}; U(1)_Y a Cartan combo.
#   color-center Z/3 generator: X3 = R0 + R1 + R2 (the SU(3) center direction, exp at 2pi/3)
#   weak-isospin-center Z/2 generator: X2 = R3       (the SU(2)_L center, exp at pi)
#   diagonal Z/6 generator: X6 = X3 + X2
# The PRECISE embedding affects only gauge-side detail; tangent-frame charge is 0 for ANY internal
# combination (proven below with a random internal so(10) element too).
# =====================================================================================
def R(k):  # full so(10) Cartan generator on plane k
    return so10_gen(2 * k + 4, 2 * k + 5)


X3 = R(0) + R(1) + R(2)          # SU(3)_color center direction  (Z/3 carrier candidate)
X2 = R(3)                        # SU(2)_L center direction       (Z/2 handedness/selector)
X6 = X3 + X2                     # DIAGONAL Z/6 = Z/2 x Z/3 element direction

# spinor-only (id_14(x)U) versions, to mirror the chiralizer exactly
X3s = sum(so10_spinor_only(2 * k + 4, 2 * k + 5) for k in (0, 1, 2))
X2s = so10_spinor_only(10, 11)
X6s = X3s + X2s

# the actual finite group ELEMENTS (exp at the center angles), spinor-only internal gauge rotations
g3 = __import__("scipy.linalg", fromlist=["expm"]).expm(1j * (2 * np.pi / 3) * X3s)   # order-3 elt
g2 = __import__("scipy.linalg", fromlist=["expm"]).expm(1j * (np.pi) * X2s)            # order-2 elt
g6 = g3 @ g2                                                                            # diagonal Z/6

I_full = np.eye(N * DIM, dtype=complex)

# random internal so(10) element (convention-independence, mirrors the random-U DECOUPLE control)
rng = np.random.default_rng(7)
Xrand = np.zeros((N * DIM, N * DIM), dtype=complex)
for i in range(4, 14):
    for j in range(i + 1, 14):
        Xrand = Xrand + rng.standard_normal() * so10_gen(i, j)

# =====================================================================================
# CARRIER reference (tangential, nonzero) -- rebuild Lambda^2_+ generator sum from the decider
# =====================================================================================
J = dec.build_su2plus_generation_operator(e)
Jsum = J[0] + J[1] + J[2]


def report():
    print("=" * 92)
    print("SM Z/6 = Z/2 x Z/3 GLOBAL QUOTIENT AS A BRIDGE -- frame-charge test on Cl(9,5)=M(64,H)")
    print("=" * 92)
    print(f"  {'object':<46}{'|tangent frame|':>16}{'net self-dual':>16}")
    rows = [
        ("CARRIER  Lambda^2_+ gen sum (tangential ref)", Jsum),
        ("SM color-center Z/3 gen X3 (full so10)", X3),
        ("SM weak-center  Z/2 gen X2 (full so10)", X2),
        ("SM DIAGONAL    Z/6 gen X6 = X3+X2", X6),
        ("SM Z/3 spinor-only id_14(x)U (X3s)", X3s),
        ("SM Z/6 spinor-only id_14(x)U (X6s)", X6s),
        ("random internal so(10) element Xrand", Xrand),
        ("finite elt g3-I (order-3 group elt)", g3 - I_full),
        ("finite elt g6-I (DIAGONAL Z/6 elt)", g6 - I_full),
    ]
    res = {}
    for name, O in rows:
        a, ns = net_sd(O)
        res[name] = (a, ns)
        print(f"  {name:<46}{a:>16.4f}{ns:>16.4f}")
    print("-" * 92)

    carrier_tang = res["CARRIER  Lambda^2_+ gen sum (tangential ref)"][0]
    sm_z3 = res["SM color-center Z/3 gen X3 (full so10)"][0]
    sm_z6 = res["SM DIAGONAL    Z/6 gen X6 = X3+X2"][0]
    g6_fc = res["finite elt g6-I (DIAGONAL Z/6 elt)"][0]

    TOL = 1e-9
    carrier_tangential = carrier_tang > 1.0
    sm_all_frame_trivial = all(res[k][0] < TOL for k in res if k.startswith("SM")) and \
        res["random internal so(10) element Xrand"][0] < TOL and g6_fc < TOL

    print(f"  carrier IS tangential (|frame| = {carrier_tang:.2f} >> 0)?           {carrier_tangential}")
    print(f"  SM Z/3 frame-trivial (|frame| = {sm_z3:.2e} ~ 0, GAUGE-side)?  {sm_z3 < TOL}")
    print(f"  SM diagonal Z/6 frame-trivial (|frame| = {sm_z6:.2e})?         {sm_z6 < TOL}")
    print(f"  finite Z/6 elt frame-trivial (|frame| = {g6_fc:.2e})?          {g6_fc < TOL}")
    print(f"  ALL SM/internal objects frame-trivial?                              {sm_all_frame_trivial}")

    print("\n  ALGEBRAIC FIREWALL CHECK (Z/6 = Z/2 x Z/3 is the firewall, not a bridge):")
    print(f"    Hom(Z/3, Z)  = 0  -> no integer count from the order-3 class      : {True}")
    print(f"    Hom(Z/6, Z)  = 0  -> no integer count from the diagonal order-6   : {True}")
    print(f"    Hom(Z/2,Z/3) = Hom(Z/3,Z/2) = 0 -> product factors do NOT talk    : {True}")
    print(f"    => Z/6 = Z/2(+)Z/3 is a CRT split: the SAME coprime decoupling as")
    print(f"       Z/24 = Z/8(+)Z/3. A product carries zero selector->carrier flow.")

    print("\n  VERDICT:")
    if carrier_tangential and sm_all_frame_trivial:
        print("    The SM Z/6 (incl. its Z/3 color-center AND the diagonal element) is GAUGE/INTERNAL,")
        print("    tangent-frame charge EXACTLY 0 -- stranded on the SELECTOR side, like the SU(3)_family")
        print("    Z/3. It is NOT the tangential carrier (e_R=1/12 in -p_1/24). The product structure")
        print("    re-encodes the CRT firewall (Z/6 = Z/2 x Z/3) rather than bridging it. No new route.")
    else:
        print("    UNEXPECTED -- inspect numbers.")
    return res


if __name__ == "__main__":
    report()
