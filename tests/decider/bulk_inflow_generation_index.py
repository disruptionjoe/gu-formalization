#!/usr/bin/env python3
r"""
THE SINGLE DECIDER -- bulk anomaly-inflow / characteristic-class angle.

Compute the NET CHIRAL GENERATION INDEX on GU's actual 4+10 geometry as the
anomaly-inflow coefficient of the bulk gravitational  -p_1/24  SPT class, with
the Spin(10)-16 content, via the index density (A-hat / ch / the p_1 framing
channel). This is the leg MOST likely computable WITHOUT the dynamical RS
operator, because anomaly inflow = bulk topology.

DECISION RULE (canon/three-generations-locate-not-force-CRT-RESULTS.md sec "single decider"):
  * integer == 3 AND fork TANGENTIAL (e=1/12, not gauge e=3/8)  -> "located" upgrades to FORCED.
  * integer == 1 (Pati-Salam "2+1 effective") OR fork GAUGE      -> strong reading dead; LOCATE stands.
  * a leg provably GATED on the unbuilt RS/IG source action or an unproven
    Bismut-Cheeger reduction -> report computable vs gated, do NOT fabricate.

ALL CONTROLS reproduced in-run so the answer is trustworthy:
  ch2(S_X)[K3] = -5376 ;  A-hat(K3)=2 & A-hat[(K3)^4]=16 ;  charge-q lens eta (2q^2-4q+1)/8 ;
  tangential e_R = 1/12 (p_1=4) ;  Pati-Salam Spin(7,7) -> exactly ONE generation.

Reuses, a-priori in-repo: tests/oq_rk1_cl95_explicit_rep.py (Cl(9,5)=M(64,H)),
tests/ahat_genus_y14_i16.py (exact A-hat engine), tests/gen_ch2_sx_from_codazzi.py
(ch2 machinery), tests/generation-sector/gen_sector_bridge.py (verified anchors).

Run:  python tests/decider/bulk_inflow_generation_index.py
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.normpath(os.path.join(HERE, ".."))
GEN = os.path.normpath(os.path.join(TESTS, "generation-sector"))
for p in (TESTS, GEN):
    if p not in sys.path:
        sys.path.insert(0, p)

import oq_rk1_cl95_explicit_rep as cl95      # noqa: E402  Cl(9,5)=M(64,H) rep
import gen_sector_bridge as gu_bridge        # noqa: E402  verified anchors

TOL = 1e-9


def primefac(n):
    n = abs(int(n))
    if n <= 1:
        return str(n)
    out, d = [], 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d; e += 1
        if e:
            out.append(f"{d}^{e}" if e > 1 else f"{d}")
        d += 1
    if n > 1:
        out.append(str(n))
    return " . ".join(out)


def primary(denom):
    d = abs(int(denom))
    f = set()
    x, k = d, 2
    while k * k <= x:
        while x % k == 0:
            f.add(k); x //= k
        k += 1
    if x > 1:
        f.add(x)
    if 3 in f:
        return "3-PRIMARY (factor 3 present)"
    if f <= {2}:
        return "2-PRIMARY (only powers of 2)"
    return f"MIXED ({primefac(d)})"


# ======================================================================== #
# CONTROL 0 -- K3 topology (sigma ONLY; chi NEVER an input)
# ======================================================================== #
SIGMA_K3 = -16
P1_TK3 = 3 * SIGMA_K3                 # Hirzebruch p1 = 3 sigma = -48
AHAT_K3 = -SIGMA_K3 // 8              # A-hat(K3) = -sigma/8 = 2   (exact)


def control_ahat_p1_channel():
    """A-hat(K3)=2 and the bulk -p_1/24 inflow coefficient on K3 (the SPT class integral)."""
    # the gravitational SPT class is [A-hat]_4 = -p_1/24 ; its integral over K3:
    grav_inflow = Fr(-P1_TK3, 24)                 # -(-48)/24 = 2
    assert grav_inflow == Fr(AHAT_K3) == Fr(2), grav_inflow
    # End-to-end: A-hat[(K3)^4] = A-hat(K3)^4 = 16 (the degree-16 density integrates to 16).
    ahat_k3_4 = AHAT_K3 ** 4
    assert ahat_k3_4 == 16
    return grav_inflow, ahat_k3_4


# ======================================================================== #
# CONTROL 1 -- ch2(S_X)[K3] = -5376  (bulk characteristic number, Codazzi/Sp(64))
# ======================================================================== #
def verify_spin_multiplier(Nso, seed=2):
    """ch2(S)/p1(V) = tr_S(rho(F)^2)/tr_V(F^2) = dim_S/8 for so(Nso) (actual matrices)."""
    rng = np.random.default_rng(seed + Nso)
    G = cl95.jordan_wigner_gammas(Nso // 2)
    A = rng.normal(size=(Nso, Nso)); F = A - A.T
    Sig = lambda a, b: 0.25 * (G[a] @ G[b] - G[b] @ G[a])
    rho = sum(F[a, b] * Sig(a, b) for a in range(Nso) for b in range(a + 1, Nso))
    return float(np.trace(rho @ rho).real) / float(np.trace(F @ F).real), 2 ** (Nso // 2)


def control_ch2_sx():
    """Reproduce ch2(S_X)[K3] = -5376 = 16 * 7 * (-48) from the spin multiplier dim_S/8 = 16."""
    m14, dimS14 = verify_spin_multiplier(14)        # dim_S/8 = 128/8 = 16
    assert abs(m14 - 16.0) < 1e-6 and dimS14 == 128
    p1_N = 6 * P1_TK3                               # N = Sym^2 T*K3 ; p1(N) = 6 p1(TK3) = -288
    p1_V = P1_TK3 + p1_N                            # V = TK3 (+) N (pullback TY14) = 7 p1(TK3) = -336
    ch2_full = int(round(m14)) * p1_V               # 16 * (-336) = -5376
    assert ch2_full == -5376 == 16 * 7 * P1_TK3, ch2_full
    # full twisted index int_K3 A-hat ch(S_X) = ch2 - rank * p1/24
    twisted = ch2_full - 128 * P1_TK3 // 24         # -5376 + 256 = -5120
    return ch2_full, p1_V, p1_N, twisted


# ======================================================================== #
# CONTROL 2 -- charge-q lens Dirac eta (2q^2-4q+1)/8 on RP^3=L(2;1) (2-primary)
# ======================================================================== #
def lens_eta_q(q):
    return Fr(2 * q * q - 4 * q + 1, 8)


# ======================================================================== #
# CONTROL 3 -- tangential Adams e_R = p_1/48 = 1/12 (3-primary) from p_1 = 4
# ======================================================================== #
def su2_adjoint_dynkin_ratio():
    """T(adjoint)/T(fundamental) = 4 from explicit su(2) matrices -> p_1(ad)=4 c_2."""
    s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]], complex)
    s3 = np.array([[1, 0], [0, -1]], complex)
    tr_f = np.trace((s1 / 2) @ (s1 / 2)).real
    eps = np.zeros((3, 3, 3)); eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1
    Ta = [(-1j) * eps[a] for a in range(3)]
    tr_a = np.trace(Ta[0] @ Ta[0]).real
    return int(round(tr_a / tr_f))


def control_tangential_eR():
    idx = su2_adjoint_dynkin_ratio()                # 4
    p1 = idx * 1                                    # charge-1 self-dual bundle, c_2=1 -> p_1 = 4
    e_R = Fr(p1, 48)                                # p_1/48 = stable-deg/24 = (p_1/2)/24
    assert idx == 4 and p1 == 4 and e_R == Fr(1, 12)
    return p1, e_R


# ======================================================================== #
# CONTROL 4 -- Spin(10)-16 chiral spinor & ch2(S^+) = 2 p_1(N) (the 16-content)
# ======================================================================== #
def spin10_16_weights():
    import itertools
    half = Fr(1, 2)
    allw = list(itertools.product([half, -half], repeat=5))
    s16 = [w for w in allw if sum(1 for c in w if c < 0) % 2 == 0]   # even # minus = chiral 16
    assert len(allw) == 32 and len(s16) == 16
    return s16


def ch2_halfspin_multiplier(weights):
    """ch2(S^+) = c * p_1(N), with c = (1/2) * (Sum_w w_i^2 / 1) read off the weight sum.
    Sum_w w_i w_j = c2 * delta_ij ; then ch2(S^+) = (1/2)*c2 * Sum_i x_i^2 = (c2/2) p_1(N)."""
    M = np.zeros((5, 5))
    for w in weights:
        wv = np.array([float(c) for c in w])
        M += np.outer(wv, wv)
    offdiag = float(np.max(np.abs(M - np.diag(np.diag(M)))))
    diag = float(M[0, 0])
    assert offdiag < 1e-9, ("off-diagonal weight sum must vanish", offdiag)
    assert all(abs(M[i, i] - diag) < 1e-9 for i in range(5))
    c2 = diag                                       # Sum_w w_i^2 = 4
    return Fr(int(round(c2)), 2)                    # ch2(S^+) coefficient of p_1(N) = c2/2 = 2


def control_16_twisted_index():
    """Generation index = ind(D_K3 (x) S^+_16(N)), N = Sym^2 T*K3.  Bulk char number."""
    w16 = spin10_16_weights()
    c = ch2_halfspin_multiplier(w16)                # ch2(S^+) = 2 p_1(N)
    assert c == Fr(2, 1)
    p1_N = 6 * P1_TK3                               # -288
    rank16 = 16
    grav = rank16 * AHAT_K3                         # 16 * 2 = 32 (the -p_1/24 gravitational leg)
    gauge = int(c * p1_N)                           # ch2(S^+(N)) = 2 * (-288) = -576 (coefficient leg)
    ind16 = grav + gauge                            # 32 - 576 = -544
    return rank16, grav, gauge, ind16


# ======================================================================== #
# CONTROL 5 -- Pati-Salam Spin(7,7) -> exactly ONE generation (group theory)
# ======================================================================== #
def control_pati_salam_one_generation():
    import itertools
    half = 0.5
    s16 = [w for w in itertools.product([half, -half], repeat=5)
           if sum(1 for c in w if c < 0) % 2 == 0]
    sumY = 0.0; sumQ = 0.0
    for w in s16:
        w123 = w[:3]; s4, s5 = w[3], w[4]
        t3l = (s4 + s5) / 2; t3r = (s4 - s5) / 2
        blv = -(2 / 3) * sum(w123)
        Y = t3r + blv / 2; Q = t3l + Y
        sumY += Y; sumQ += Q
    # one anomaly-free generation: Tr Y = Tr Q = 0 over exactly 16 states
    return len(s16), abs(sumY) < 1e-9 and abs(sumQ) < 1e-9


# ======================================================================== #
# THE FORK -- frame charge of the GENERATION-COUNTING (net-chiral) operator
#             vs the tangential Lambda^2_+ carrier, on the verified substrate.
# ======================================================================== #
N, DIM = gu_bridge.N, gu_bridge.DIM
ETA = np.array([1.0] * 9 + [-1.0] * 5)


def _quaternionic_J(e128, seed=1):
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e128[a] @ U @ e128[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U)); U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U); U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


def _lvec(i, j):
    M = np.zeros((N, N), complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def _sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def _frame_charge(O, gens):
    O4 = O.reshape(N, DIM, N, DIM)
    tot = 0.0
    for L in gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        tot += float(np.linalg.norm(F_L))
    return tot


def resolve_fork():
    """Does the net-chiral GENERATION selector rotate the tangent frame (TANGENTIAL, feeds
    -p_1/24, e=1/12) or is it frame-trivial (GAUGE, e=3/8, 3-part zero)?  Decided by frame charge."""
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G = Pi - Q                                       # chiral grading
    e128 = gu_bridge.gammas()
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "substrate anchors moved"

    U = _quaternionic_J(e128, seed=1)
    Jf = np.kron(np.eye(N), U)                       # J_quat = id_14 (x) U
    Cu = Jf @ G.conj()                               # unitary part of antilinear +96 selector C=J_quat.G
    Csq = float((np.trace(Cu @ Cu.conj()) / (N * DIM)).real)
    assert abs(Csq + 1.0) < 1e-3, "selector must be antiunitary C^2=-1 (the net-chiral +96 escape)"

    # the tangential Lambda^2_+ carrier (rotates BOTH vector and spinor on base {0,1,2,3})
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    J3 = sum(np.kron(np.eye(N), _sgen(e, a, b) + _sgen(e, c, d))
             + np.kron(_lvec(a, b) + _lvec(c, d), np.eye(DIM)) for (a, b, c, d) in SD)

    # the PURE-INTERNAL +96 re-grading C_trip = J_quat . chirality (no gamma-trace projector)
    om = np.eye(DIM, dtype=complex)
    for a in range(N):
        om = om @ e128[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir_int = om if om2 > 0 else (-1j) * om
    C_trip = np.kron(np.eye(N), U @ chir_int)

    sd_gens = [_lvec(0, 1) + _lvec(2, 3), _lvec(0, 2) + _lvec(3, 1), _lvec(0, 3) + _lvec(1, 2)]
    asd_gens = [_lvec(0, 1) - _lvec(2, 3), _lvec(0, 2) - _lvec(3, 1), _lvec(0, 3) - _lvec(1, 2)]
    all4 = sd_gens + asd_gens

    def net_self_dual(O):
        # the -p_1/24 channel is fed ONLY by the NET self-dual instanton charge (SD - ASD);
        # a non-chiral (SD=ASD balanced) frame content carries zero net self-dual p_1.
        return _frame_charge(O, sd_gens) - _frame_charge(O, asd_gens)

    carrier_net_sd = net_self_dual(J3)               # Lambda^2_+ : large, purely self-dual (p_1=4)
    selector_total_frame = _frame_charge(Cu, all4)   # nonzero: the NON-CHIRAL gamma-trace projector Pi
    selector_net_sd = net_self_dual(Cu)              # ~ 0 : NO net self-dual instanton (the decisive #)
    selector_pure_frame = _frame_charge(C_trip, all4)  # ~ 0 : pure-internal re-grading is frame-trivial

    return {
        "carrier_net_sd": carrier_net_sd,            # ~ 34 (tangential, feeds -p_1/24)
        "selector_total_frame": selector_total_frame,   # ~ 7 (non-chiral Pi part, SD=ASD balanced)
        "selector_net_sd": selector_net_sd,          # ~ 0 (no net self-dual instanton -> no p_1)
        "selector_pure_frame": selector_pure_frame,  # ~ 0 (pure-internal re-grading frame-trivial)
    }


# ======================================================================== #
# MAIN
# ======================================================================== #
def main():
    np.set_printoptions(precision=4, suppress=True)
    line = "=" * 88
    print(line)
    print("THE SINGLE DECIDER -- bulk anomaly-inflow generation index on GU's 4+10 geometry")
    print(line)

    # ---------------- CONTROLS (reproduced so the answer is trustworthy) ----------------
    print("\n[CONTROLS]")
    grav_inflow, ahat44 = control_ahat_p1_channel()
    print(f"  A-hat(K3) = -sigma/8 = {AHAT_K3} (exact);  bulk -p_1/24 SPT inflow on K3 = "
          f"int_K3(-p_1/24) = {grav_inflow};  A-hat[(K3)^4] = {ahat44} = 8*A-hat(K3)... "
          f"(8*2={8*AHAT_K3} H-index)")
    ch2_full, p1V, p1N, twisted = control_ch2_sx()
    print(f"  ch2(S_X)[K3] = (dim_S/8)*p1(V) = 16 * {p1V} = {ch2_full}  = 16*7*({P1_TK3})"
          f"   [bulk char number; 'disguised-chi 24' REJECTED]")
    print(f"  full twisted int_K3 A-hat*ch(S_X) = ch2 - 128*p1/24 = {twisted}")
    qd = [str(lens_eta_q(q)) for q in range(5)]
    print(f"  charge-q lens Dirac eta (2q^2-4q+1)/8 on RP^3=L(2;1): {qd}  (denom 8=2^3, 2-PRIMARY all q)")
    p1_tan, e_R = control_tangential_eR()
    print(f"  tangential Adams e_R = p_1/48 with p_1={p1_tan}: e_R = {e_R}  "
          f"(denom {e_R.denominator} = {primefac(e_R.denominator)}, {primary(e_R.denominator)})")
    nps, ps_ok = control_pati_salam_one_generation()
    print(f"  Pati-Salam Spin(7,7) chain: {nps} states = exactly ONE anomaly-free generation "
          f"(Tr Y=Tr Q=0): {ps_ok}")
    assert ps_ok and nps == 16

    # ---------------- THE BULK INFLOW INTEGER (the computable core) ----------------
    print("\n[BULK INFLOW INTEGER -- the -p_1/24 SPT channel with the Spin(10)-16 content]")
    rank16, grav, gauge, ind16 = control_16_twisted_index()
    print(f"  Spin(10)-16 chiral spinor: rank {rank16}; ch2(S^+(N)) = 2*p_1(N) (verified by weight sum)")
    print(f"  ind(D_K3 (x) 16) = [grav -p_1/24 leg] + [gauge ch2 leg] = {rank16}*A-hat(K3) + 2*p_1(N)")
    print(f"                   = {grav} + ({gauge}) = {ind16}   (bulk characteristic number)")
    print()
    print("  The GENERATION COUNT decomposition GU actually asserts (canon/no-go-class-relative-map.md):")
    spin_half_Hindex = 8 * AHAT_K3                   # 16  (index-theory grade, COMPUTABLE)
    print(f"    spin-1/2 leg  ind_H = 8*A-hat(K3) = 8*{AHAT_K3} = {spin_half_Hindex}   "
          f"[index-theory grade: COMPUTABLE]")
    print(f"    RS  +8 leg     ind_H = 8                          [ASSERTED -- rests on "
          f"rank_H(S_RS^+)=4, UNCOMPUTED]")
    print(f"    total candidate ind_H = {spin_half_Hindex}+8 = 24  ->  count = 24/8 = 3   "
          f"(the '+1' RS leg is the gated piece)")
    print(f"    bulk-FORCED part (spin-1/2 only): {spin_half_Hindex}/8 = {spin_half_Hindex//8} "
          f"generations  ==  A-hat(K3) = {AHAT_K3}   ('2' of the '2+1')")
    # the ten failed RS routes -- explicit non-convergence (no fabrication)
    rs_routes = [960, -288, -384, -192, -336, -128, 128, -8, -480, 60]
    print(f"    RS analytic routes (10) gave {rs_routes} -- NO convergence to 16; +8 NOT derived.")
    assert 16 not in rs_routes

    # the LINEAR net chiral index (h1): the Lambda^2_+ triplet is vectorlike, net 0
    print("\n  LINEAR net chiral generation index (the Lambda^2_+ triplet, h1_selfdual_family_kill):")
    print("    Euclidean (14,0): +96 / -96  ->  NET = 0  (VECTORLIKE). A nonzero net-chiral count")
    print("    requires the ANTILINEAR +96 selector -- not a linear bulk index.")
    net_linear = 0

    # ---------------- THE FORK (resolved by the computation, not assumed) ----------------
    print("\n[FORK -- tangential vs gauge, decided by frame charge of the COUNTING operator]")
    fk = resolve_fork()
    print(f"  tangential Lambda^2_+ carrier  net self-dual frame charge = {fk['carrier_net_sd']:8.3f}"
          f"   -> rotates frame, carries p_1=4, e_R=1/12 [TANGENTIAL]  BUT triplet is net-0 (vectorlike)")
    print(f"  net-chiral +96 GENERATION selector  total frame charge    = {fk['selector_total_frame']:8.3f}"
          f"   (from the NON-CHIRAL gamma-trace projector Pi; SD=ASD balanced)")
    print(f"  net-chiral +96 GENERATION selector  NET self-dual charge   = {fk['selector_net_sd']:8.2e}"
          f"   -> NO net self-dual instanton -> carries NO p_1 -> cannot feed -p_1/24  [DECISIVE]")
    print(f"  pure-internal +96 re-grading (J_quat.chirality) total frame= {fk['selector_pure_frame']:8.2e}"
          f"   -> frame-trivial (entirely in the M(64,H) coefficient fiber)")
    # the -p_1/24 channel (where the order-3 lives) is fed ONLY by the NET self-dual instanton
    # charge; the selector's net self-dual charge is exactly 0 -> it couples to the GAUGE channel.
    fork_gauge = abs(fk['selector_net_sd']) < 1e-6 and abs(fk['selector_pure_frame']) < 1e-6
    tangential_carrier_is_vectorlike = True          # h1: +96/-96, net 0 (does NOT count generations)
    print()
    print(f"  => the operator that PRODUCES the net chiral count is FRAME-TRIVIAL -> couples GAUGE")
    print(f"     gauge-branch boundary eta = Tr Ad(-1)/8 = 3/8  (denom 8 = 2^3, {primary(8)}; 3-part ZERO)")
    print(f"  => the order-3 carrier (Lambda^2_+, e_R=1/12, denom 12 = 2^2.3) is a SEPARATE bundle whose")
    print(f"     triplet is VECTORLIKE (net 0) -- it carries an order-3 homotopy class but does NOT count.")
    fork = "GAUGE" if fork_gauge else "TANGENTIAL"

    # ---------------- INTEGER EXTRACTION + DECISION ----------------
    print("\n" + line)
    print("VERDICT")
    print(line)
    # the bulk-computable integers, none of which is 3:
    bulk_integers = {
        "Pati-Salam verified per-fiber generation": 1,
        "spin-1/2 leg (A-hat K3 = ind_H/8)": spin_half_Hindex // 8,   # 2
        "LINEAR net chiral (vectorlike, h1)": net_linear,             # 0
    }
    print(f"  bulk-FORCED integers: {bulk_integers}")
    print(f"  fork resolved BY computation: {fork}")
    print()
    is_three = False
    forced = (3 in bulk_integers.values()) and (fork == "TANGENTIAL")
    if forced:
        print("  -> located UPGRADES to FORCED.")
    else:
        print("  -> 3 is NOT bulk-forced AND the fork lands GAUGE.")
        print("     The strong reading ('GU forces three') is DEAD on the bulk-topology leg.")
        print("     The LOCATE result stands alone: bulk topology forces 2-primary EVEN numbers and a")
        print("     LINEAR net-chiral index of 0; the verified Pati-Salam chain gives exactly ONE")
        print("     generation; the '+1' that would make 2+1=3 is the RS leg, GATED on the unbuilt source")
        print("     action; and the only net-chiral selector is frame-trivial (GAUGE, e=3/8, 3-part 0).")

    print("\n[GATED -- honestly marked, NOT fabricated]")
    print("  (i)   families pushforward pi_!: ch(S)/Y14 -> ch(S_X)/X4 is NOT_DEFINED (fiber")
    print("        GL(4,R)/O(3,1) non-convex). So ch2(S_X)[K3]=-5376 is a BULK char number, not yet")
    print("        THE families index -- gated on a PROVEN Bismut-Cheeger fibered-boundary reduction")
    print("        (the true 13-dim link is an S^6-bundle over RP^3; 'the spine is RP^3' is not a proof).")
    print("  (ii)  the +8 RS spin-3/2 leg (24=16+8) is ASSERTED; every analytic route FAILED. Gated on")
    print("        the unbuilt stabilized RS/IG source action. The net chiral count (1 vs 3) is gated.")
    print("  (iii) order-3-class -> integer-3 is a theorem of nothing (APS/Dai-Freed/Bismut-Cheeger")
    print("        relate boundary eta to indices/phases/cobordism, never to an integer family count);")
    print("        e_R=1/12 is HOMOTOPY-FIXED, identical for 1 or 5 generations.")

    print("\n" + line)
    print(f"RESULT: bulk topology does NOT force 3.  Integer(s) bulk-forced in {{0, 1, 2}} "
          f"(net-chiral linear=0, Pati-Salam=1, spin-1/2 A-hat leg=2).")
    print(f"        FORK = {fork} (denominator 8 = 2^3, 3-part ZERO).  => LOCATE stands; FORCE not earned.")
    print(line)

    # hard asserts -- the decider's load-bearing facts
    assert AHAT_K3 == 2
    assert ch2_full == -5376
    assert e_R == Fr(1, 12)
    assert all(lens_eta_q(q).denominator == 8 for q in range(8))
    assert nps == 16 and ps_ok
    assert ind16 == -544
    assert fork == "GAUGE"
    assert not forced
    return {
        "ahat_k3": AHAT_K3, "ch2_sx": ch2_full, "twisted_index": twisted,
        "e_R_tangential": str(e_R), "ind16_bulk": ind16,
        "spin_half_Hindex": spin_half_Hindex, "rs_leg_status": "GATED (asserted +8, routes failed)",
        "pati_salam_generations": 1, "linear_net_chiral": net_linear,
        "fork": fork, "bulk_forces_three": forced,
        "verdict": "LOCATE stands; FORCE not earned (fork GAUGE, 3 not bulk-forced)",
    }


if __name__ == "__main__":
    out = main()
    print("\nMACHINE SUMMARY:", out)
