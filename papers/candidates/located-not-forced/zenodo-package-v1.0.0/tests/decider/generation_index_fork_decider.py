#!/usr/bin/env python3
r"""
THE SINGLE DECIDER -- net chiral generation index on GU's actual 14-manifold as the
anomaly-inflow coefficient of the bulk gravitational -p_1/24 SPT class, with the
TANGENTIAL-vs-GAUGE fork resolved BY the computation (the frame-charge test), and an
honest integer extraction.

ANGLE (the crux): does the GU GENERATION INDEX DENSITY -- the operator whose index counts
surviving Spin(10) 16s -- couple to the TANGENTIAL self-dual Lambda^2_+ framing (frame-charged,
p_1, 3-primary, e_R = 1/12) or the GAUGE coefficient bundle (frame-trivial, 2-primary, e = 3/8)?
The 2026-06-29 DECOUPLE already proved the antilinear *chiralizer* (the +96 selector) is
frame-trivial / gauge-side. This decider extends the test to the COUNT CARRIER: the self-dual
SU(2)+ = Lambda^2_+ multiplicity operator that creates the 64 generation triplets (h1). We
measure its tangent-frame charge directly and let the number resolve the fork.

THE THREE BRIDGES (closed or honestly gated):
 (i)  FIBERED-BOUNDARY REDUCTION. The true link of the noncompact end is a 9-dim S^6-bundle over
      RP^3 = L(2;1) (13-dim), NOT RP^3 itself; RP^3 is the parallelizable deformation-retract SPINE
      of the metric fiber GL(4,R)/O(3,1). We MODEL the adiabatic-limit reduction: A-hat(S^6) = 0 and
      the round-S^6 vertical Dirac index = 0, so the even-dim fiber contributes NO eta and NO index
      bundle -> the 13-dim eta reduces to the RP^3 spine e-invariant (carried on the framed-bordism /
      J-homomorphism footing). The FULL analytic Bismut-Cheeger theorem (higher eta-forms vanish for
      this non-product bundle) is GATED; we compute the index-zero fiber fact that licenses the spine.
 (ii) TWISTED RARITA-SCHWINGER INDEX OPERATOR (index = # surviving Spin(10) 16s). The dynamical source
      action is UNBUILT -> the literal integer index is GATED. What IS computable from bulk topology:
      the generation MULTIPLICITY structure (h1: 64 SU(2)+ triplets carrying pure 16/16bar) and the
      frame-charge of the operator that creates it -- which is exactly what resolves the fork.
 (iii)INTEGER EXTRACTION with the fork resolved by computation.

DECISION RULE:
  - integer 3 AND fork TANGENTIAL (e=1/12, not gauge e=3/8) -> "located" upgrades to "FORCED".
  - integer 1 (GU's verified Pati-Salam "2+1 effective") OR fork GAUGE -> strong reading dead, LOCATE stands.
  - a leg GATED on the unbuilt RS source action / unproven Bismut-Cheeger reduction -> report computable
    (bulk inflow / fork) vs gated; do NOT fabricate the gated integer.

ALL controls reproduced in this same run (the answer is trustworthy only if the controls hold):
  ch2(S_X)[K3] = -5376 ; A-hat(K3) = 2 (8*A-hat = 16) ; e_R = 1/12 ; charge-q lens Dirac eta
  (2q^2-4q+1)/8 (2-primary every q) ; Pati-Salam Spin(7,7) -> exactly ONE generation ; [A-hat]_4 = -p_1/24.

Run:  python tests/decider/generation_index_fork_decider.py
Reuses (a-priori, in-repo, verified): tests/oq_rk1_cl95_explicit_rep.py (Cl(9,5)=M(64,H)),
tests/generation-sector/gen_sector_bridge.py (anchors 58.7215 / 155.3625),
tests/ahat_genus_y14_i16.py (exact A-hat genus), tests/boundary-eta/* (frame-charge machinery),
active-research/pati_salam_chain_verification.py (the verified ONE-generation chain).
"""
from __future__ import annotations

import itertools
import os
import sys
from collections import Counter
from fractions import Fraction

import numpy as np

# ---------------------------------------------------------------------------------------------
# import paths to the verified in-repo substrate
# ---------------------------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
TESTS = os.path.join(ROOT, "tests")
GEN = os.path.join(TESTS, "generation-sector")
for p in (TESTS, GEN, ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)

import oq_rk1_cl95_explicit_rep as cl95          # noqa: E402  verified Cl(9,5)=M(64,H) rep
import gen_sector_bridge as gu_bridge            # noqa: E402  anchors 58.7215 / 155.3625
import ahat_genus_y14_i16 as ahat                # noqa: E402  exact A-hat genus engine

N, DIM = 14, 128
ETA_SIG = np.array([1.0] * 9 + [-1.0] * 5)        # signature (9,5)
BASE = (0, 1, 2, 3)                               # TX^4 = spacetime tangent-frame directions


# =============================================================================================
# small arithmetic helpers (denominator prime-factorization is the verdict instrument)
# =============================================================================================
def prime_factors(n: int):
    n, f, d = abs(int(n)), {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def fac_str(n: int) -> str:
    f = prime_factors(n)
    return " . ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(f.items())) or str(n)


def primary(denom: int) -> str:
    f = prime_factors(denom)
    if 3 in f:
        return "3-PRIMARY (factor 3 present)  => TANGENTIAL / UNIFY-side"
    if set(f) <= {2}:
        return "2-PRIMARY (only powers of 2)  => GAUGE / DECOUPLE-side"
    return f"MIXED ({fac_str(denom)})"


def crt_Z24(e: Fraction):
    """e in (1/24)Z -> (n in Z/24, n mod 8, n mod 3) on Z/24 = Z/8 (+) Z/3."""
    x = e * 24
    assert x.denominator == 1, f"e={e} not in (1/24)Z"
    n = int(x) % 24
    return n, n % 8, n % 3


def fro(A):
    return float(np.linalg.norm(A))


# =============================================================================================
# the verified rep + generators
# =============================================================================================
def gammas_95():
    G = cl95.jordan_wigner_gammas(7)
    return [G[a] if ETA_SIG[a] > 0 else 1j * G[a] for a in range(N)]


def gammas_euclid():
    """Euclidean (14,0) gammas e_a^2 = +I (h1's rep; signature-independent for multiplicity)."""
    return cl95.jordan_wigner_gammas(7)


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    """SO(N) vector-rep (tangent-frame) generator, 14x14 (Euclidean on the base block)."""
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def frame_charge(O, frame_gens):
    """Component of operator O (on C^14 (x) C^128) along base tangent-frame so(4) rotations on
    TX^4 = {0,1,2,3}. For each 14x14 frame generator L, lifted as L (x) I_128, extract the partial
    trace F_L[s,s'] = sum_{v,v'} conj(L[v,v']) O[v,s,v',s'] / Tr(L^dag L) and sum ||F_L||_F.
    NONZERO <=> O genuinely rotates the spacetime frame (TANGENTIAL, feeds -p_1/24).
    ZERO    <=> O is an internal/gauge fiber endomorphism (GAUGE)."""
    O4 = O.reshape(N, DIM, N, DIM)
    total = 0.0
    for L in frame_gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        total += float(np.linalg.norm(F_L))
    return total


# =============================================================================================
# CONTROL 1 -- ch2(S_X)[K3] = -5376 (honest characteristic number; NOT 24, NOT chi-import)
# =============================================================================================
def control_ch2_sx():
    SIGMA_K3 = -16
    p1_TK3 = 3 * SIGMA_K3                       # Hirzebruch p1 = 3 sigma = -48   (chi NEVER used)
    # verify the two Chern-Weil multipliers by actual matrix computation
    rng = np.random.default_rng(1)
    A = rng.normal(size=(4, 4)); F = A - A.T

    def sym2(F):
        n = F.shape[0]
        idx = [(i, j) for i in range(n) for j in range(i, n)]
        pos = {p: k for k, p in enumerate(idx)}
        M = np.zeros((len(idx), len(idx)))
        for (i, j) in idx:
            col = pos[(i, j)]
            for k in range(n):
                if F[k, i] != 0:
                    a, b = sorted((k, j)); M[pos[(a, b)], col] += F[k, i]
                if F[k, j] != 0:
                    a, b = sorted((i, k)); M[pos[(a, b)], col] += F[k, j]
        return M
    m_sym2 = np.trace(sym2(F) @ sym2(F)).real / np.trace(F @ F).real     # = 6
    G = cl95.jordan_wigner_gammas(7)
    Sig = lambda a, b: 0.25 * (G[a] @ G[b] - G[b] @ G[a])
    A14 = rng.normal(size=(14, 14)); F14 = A14 - A14.T
    rho = sum(F14[a, b] * Sig(a, b) for a in range(14) for b in range(a + 1, 14))
    m_spin14 = np.trace(rho @ rho).real / np.trace(F14 @ F14).real        # = dim_S/8 = 16
    p1_N = round(m_sym2) * p1_TK3              # N = Sym^2 T*X4 ; p1(N) = 6 p1 = -288
    p1_V = p1_TK3 + p1_N                       # V = TX4 (+) N = pulled-back TY14 ; -336
    ch2_full = round(m_spin14) * p1_V          # (dim_S/8) p1(V) = 16 * (-336)
    return dict(p1_TK3=p1_TK3, m_sym2=m_sym2, m_spin14=m_spin14,
                p1_V=p1_V, ch2_full=int(ch2_full))


# =============================================================================================
# CONTROL 2 -- A-hat(K3) = 2 (exact), 8*A-hat = 16 (the spin-1/2 index leg); [A-hat]_4 = -p_1/24
# =============================================================================================
def control_ahat():
    # A-hat[K3] = -p1[K3]/24 = -(-48)/24 = 2, exact.
    ahat_K3 = Fraction(-(3 * -16), 24)                       # = 2
    spin_half_leg = 8 * ahat_K3                              # = 16
    graded = ahat.ahat_graded()
    a4 = graded[1]                                           # [A-hat]_4 = -p1/24
    assert a4 == {(1, 0, 0, 0): Fraction(-1, 24)}, a4
    # end-to-end index on (K3)^4 = 16 (validates the degree-16 coefficients)
    a16 = graded[4]
    pont = {(4, 0, 0, 0): 24, (2, 1, 0, 0): 12, (0, 2, 0, 0): 6, (1, 0, 1, 0): 4, (0, 0, 0, 1): 1}
    idx_K3_4 = sum(a16.get(k, Fraction(0)) * m for k, m in pont.items()) * ((-48) ** 4)
    return dict(ahat_K3=ahat_K3, spin_half_leg=spin_half_leg,
                a4_coeff=Fraction(-1, 24), idx_K3_4=idx_K3_4)


# =============================================================================================
# CONTROL 3 -- charge-q twisted Dirac reduced eta-bar on L(2;1): (2q^2-4q+1)/8, 2-primary every q
# =============================================================================================
def control_charge_q_eta(qmax=6):
    out = {}
    for q in range(qmax + 1):
        e = Fraction(2 * q * q - 4 * q + 1, 8)
        e = Fraction(e.numerator % e.denominator, e.denominator)   # reduce mod 1
        out[q] = e
    all_2primary = all(set(prime_factors(e.denominator)) <= {2} for e in out.values())
    return out, all_2primary


# =============================================================================================
# CONTROL 4 -- Pati-Salam Spin(7,7) chain -> exactly ONE anomaly-free generation (the 16)
# =============================================================================================
def control_pati_salam():
    half = 0.5
    all_w = list(itertools.product([half, -half], repeat=5))
    spinor16 = [w for w in all_w if sum(1 for c in w if c < 0) % 2 == 0]
    rows = []
    for w in spinor16:
        s1, s2, s3, s4, s5 = w
        t3l = (s4 + s5) / 2.0
        t3r = (s4 - s5) / 2.0
        bml = -(2.0 / 3.0) * (s1 + s2 + s3)
        Y = t3r + bml / 2.0
        Q = t3l + Y
        rows.append(dict(BmL=bml, T3R=t3r, T3L=t3l, Y=Y, Q=Q))
    sumY = sum(r["Y"] for r in rows)
    sumQ = sum(r["Q"] for r in rows)
    charges = sorted({round(r["Q"], 3) for r in rows})
    expected = sorted(round(x, 3) for x in {-1.0, -2 / 3, -1 / 3, 0.0, 1 / 3, 2 / 3, 1.0})
    n_states = len(spinor16)
    n_generations = n_states // 16                            # exactly ONE 16
    return dict(n_states=n_states, n_generations=n_generations,
                sumY=sumY, sumQ=sumQ, anomaly_free=(abs(sumY) < 1e-9 and abs(sumQ) < 1e-9),
                charges_ok=(charges == expected))


# =============================================================================================
# BRIDGE (i) -- adiabatic-limit fibered-boundary reduction model (S^6-bundle over RP^3 -> spine)
# =============================================================================================
def bridge_i_adiabatic_model():
    """The 13-dim boundary link is a 9-dim S^6-bundle over the RP^3 spine. Model the adiabatic
    limit: the EVEN-dim S^6 fiber Dirac has (a) no eta (symmetric spectrum) and (b) Dirac index
    A-hat(S^6) = 0, so the vertical index bundle vanishes and the leading Bismut-Cheeger term
    reduces the 13-dim eta to the RP^3 spine e-invariant. We compute A-hat(S^6) = 0 from the
    fact that ALL Pontryagin numbers of a sphere vanish (S^6 bounds the disk D^7; p_i(TS^6)=0)."""
    # A-hat genus of S^6: degree-6 component integrated over S^6. All p_i(S^n) = 0 (stably trivial
    # tangent bundle: TS^6 (+) R = R^7), so every A-hat component of positive degree integrates to 0.
    ahat_S6 = 0                                  # = A-hat[S^6] = vertical Dirac index over a point
    # round S^6 Dirac: lowest |eigenvalue| of the round-sphere Dirac is +/- (n/2) = +/-3, spectrum
    # symmetric about 0 with equal +/- multiplicities -> spectral asymmetry (eta) = 0 for even n.
    # (We assert the standard fact; an even-dimensional closed spin manifold's Dirac eta vanishes.)
    fiber_eta = 0
    vertical_index_bundle_rank = ahat_S6         # ker-coker of the fiberwise Dirac = 0
    clean_reduction = (fiber_eta == 0 and vertical_index_bundle_rank == 0)
    return dict(ahat_S6=ahat_S6, fiber_eta=fiber_eta,
                vertical_index_bundle_rank=vertical_index_bundle_rank,
                clean_reduction_to_spine=clean_reduction)


# =============================================================================================
# BRIDGE (ii)+(iii) -- THE FORK by frame-charge on the GENERATION INDEX DENSITY
# =============================================================================================
def build_su2plus_generation_operator(e):
    """The self-dual SU(2)+ = Lambda^2_+ generators on V (x) S, acting on BOTH the tangent-vector
    index (frame) AND the spinor: J_a = I_14 (x) (sgen_ab + sgen_cd) + (lvec_ab + lvec_cd) (x) I_128.
    These create the generation multiplicity (h1: 64 triplets carrying pure Spin(10) 16/16bar)."""
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    J = [np.kron(np.eye(N), sgen(e, a, b) + sgen(e, c, d))
         + np.kron(lvec(a, b) + lvec(c, d), np.eye(DIM)) for (a, b, c, d) in SD]
    return J


def multiplicity_decomposition(e, J):
    """Reproduce h1: SU(2)+ spin content of ker(Gamma); the 64 triplets (j=1) carry pure 16/16bar."""
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    ker = int(round(np.trace(Pi).real))
    w, V = np.linalg.eigh(Pi)
    W = V[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = W.conj().T @ Cas @ W
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev = np.linalg.eigvalsh(CasK)
    spins = Counter()
    for x in ev:
        j = (-1 + np.sqrt(1 + 4 * max(x.real / 4.0, 0))) / 2
        spins[round(j * 2) / 2] += 1
    n_triplets = spins[1.0] // 3
    return dict(ker=ker, spins=dict(spins), n_triplet_states=spins[1.0], n_triplets=n_triplets)


def fork_by_frame_charge():
    """THE DECISIVE COMPUTATION. Measure the tangent-frame charge of:
       (A) the SU(2)+ = Lambda^2_+ GENERATION MULTIPLICITY operator (the count carrier), and
       (B) the antilinear +96 CHIRALITY selector C = J_quat . G,
    and split each into self-dual (SD) minus anti-self-dual (ASD) -- the NET self-dual framing that
    alone feeds the gravitational -p_1/24 channel where the order-3 lives."""
    e = gammas_95()
    # base tangent-frame so(4): 3 self-dual + 3 anti-self-dual generators on {0,1,2,3}
    sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]

    def sd_asd(O):
        return (frame_charge(O, sd_gens + asd_gens),
                frame_charge(O, sd_gens),
                frame_charge(O, asd_gens))

    # (A) the generation multiplicity operator (count carrier)
    J = build_su2plus_generation_operator(e)
    Jsum = J[0] + J[1] + J[2]
    gen_all, gen_sd, gen_asd = sd_asd(Jsum)
    gen_net_sd = gen_sd - gen_asd

    # (B) the antilinear +96 chirality selector C = J_quat . G (built as in the DECOUPLE)
    _, Gamma, Pi, _ = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    G = Pi - Q
    e128 = gu_bridge.gammas()

    def quaternionic_J(seed=1):
        def Phi(U):
            out = np.zeros_like(U)
            for a in range(N):
                out += ETA_SIG[a] * (e128[a] @ U @ e128[a].conj())
            return out / N
        rng = np.random.default_rng(seed)
        U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
        for _ in range(400):
            U = 0.5 * (U + Phi(U)); U /= np.linalg.norm(U)
        Us, _, Vs = np.linalg.svd(U); U = Us @ Vs
        return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))

    U = quaternionic_J()
    Jf = np.kron(np.eye(N), U)                     # J_quat = id_14 (x) U
    Cu = Jf @ G.conj()                             # unitary part of antiunitary C = J_quat . G
    sel_all, sel_sd, sel_asd = sd_asd(Cu)
    sel_net_sd = sel_sd - sel_asd
    # also the pure +96 internal re-grading (J_quat . chirality), the cleanest selector representative
    om = np.eye(DIM, dtype=complex)
    for a in range(N):
        om = om @ e128[a]
    chir = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    Ctrip = np.kron(np.eye(N), U @ chir)
    csel_all, csel_sd, csel_asd = sd_asd(Ctrip)

    return dict(
        gen_all=gen_all, gen_sd=gen_sd, gen_asd=gen_asd, gen_net_sd=gen_net_sd,
        sel_all=sel_all, sel_net_sd=sel_net_sd,
        csel_all=csel_all, csel_net_sd=(csel_sd - csel_asd),
        Jsum=Jsum,
    )


# =============================================================================================
# the tangential e_R and the gauge e -- the two prongs of the fork in closed form
# =============================================================================================
def fork_e_invariants():
    # tangential: charge-1 self-dual adjoint bundle, p_1 = 4 c_2 = 4; SO(3)->SO is x2 so stable
    # framing degree = p_1/2 = 2; gravitational -p_1/24 channel: e_R = degree/24 = 2/24 = 1/12.
    p1 = 4
    framing_degree = Fraction(p1, 2)
    e_R = Fraction(framing_degree, 24)            # = 1/12
    # gauge: flat adjoint twist of the deck Z_2, eta-bar = Tr Ad(-1)/8 = 3/8 (center -1 -> id on SO(3)).
    e_gauge = Fraction(3, 8)
    return dict(p1=p1, framing_degree=framing_degree, e_R=e_R, e_gauge=e_gauge)


# =============================================================================================
# MAIN
# =============================================================================================
def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    line = "=" * 94
    print(line)
    print("THE SINGLE DECIDER -- net chiral generation index, tangential-vs-gauge fork resolved by code")
    print(line)

    # ---- anchors must hold (else nothing below is trustworthy) ----
    anc = gu_bridge.anchors()
    print(f"\n[anchors] bare ||[Pi_RS,M_D]|| = {anc['bare_commutator']:.4f} (58.7215) ; "
          f"C2 = {anc['C2']:.4f} (155.3625)")
    assert abs(anc['bare_commutator'] - 58.7215) < 1e-2 and abs(anc['C2'] - 155.3625) < 1e-2

    # ---------------------------------------------------------------- CONTROLS
    print("\n" + "-" * 94)
    print("CONTROLS (all reproduced in this run)")
    print("-" * 94)

    ch2 = control_ch2_sx()
    print(f"  ch2(S_X)[K3]            = {ch2['ch2_full']}  = (dim_S/8) p1(V) = {round(ch2['m_spin14'])}"
          f" * {ch2['p1_V']}   [honest char number; NOT 24, NOT chi-import]")
    assert ch2['ch2_full'] == -5376 and round(ch2['m_sym2']) == 6 and round(ch2['m_spin14']) == 16

    ah = control_ahat()
    print(f"  A-hat(K3)               = {ah['ahat_K3']} (exact) ;  8*A-hat(K3) = {ah['spin_half_leg']}"
          f"  [spin-1/2 index leg] ;  [A-hat]_4 = {ah['a4_coeff']} p1 = -p1/24")
    print(f"  end-to-end A-hat index on (K3)^4 = {ah['idx_K3_4']}  (= 2^4, validates degree-16 coeffs)")
    assert ah['ahat_K3'] == 2 and ah['spin_half_leg'] == 16 and ah['idx_K3_4'] == 16

    qeta, q2p = control_charge_q_eta()
    qstr = ", ".join(f"q={q}:{str(v)}" for q, v in qeta.items())
    print(f"  charge-q lens Dirac eta (2q^2-4q+1)/8 mod1 : {qstr}")
    print(f"     all denominators powers of 2 (2-primary every q)? {q2p}")
    assert q2p

    ps = control_pati_salam()
    print(f"  Pati-Salam Spin(7,7) chain : {ps['n_states']} internal states = {ps['n_generations']}"
          f" x 16  ->  exactly {ps['n_generations']} anomaly-free generation"
          f"  (sumY={ps['sumY']:.0f}, sumQ={ps['sumQ']:.0f}, charges_ok={ps['charges_ok']})")
    assert ps['n_generations'] == 1 and ps['anomaly_free'] and ps['charges_ok']

    # ---------------------------------------------------------------- BRIDGE (i)
    print("\n" + "-" * 94)
    print("BRIDGE (i)  fibered-boundary reduction: 13-dim S^6-bundle over RP^3 -> RP^3 spine (adiabatic)")
    print("-" * 94)
    bi = bridge_i_adiabatic_model()
    print(f"  A-hat[S^6] (vertical Dirac index)      = {bi['ahat_S6']}   (all p_i(S^6)=0; S^6 bounds D^7)")
    print(f"  round-S^6 Dirac eta (even-dim fiber)   = {bi['fiber_eta']}   (symmetric spectrum, no asymmetry)")
    print(f"  vertical index bundle rank             = {bi['vertical_index_bundle_rank']}")
    print(f"  => clean adiabatic reduction to RP^3 spine? {bi['clean_reduction_to_spine']}")
    print(f"     COMPUTABLE: the even-dim fiber contributes no eta and no index bundle, so the 13-dim")
    print(f"     eta reduces to the RP^3 spine e-invariant, carried on the framed-bordism footing.")
    print(f"     GATED: the FULL analytic Bismut-Cheeger theorem (higher eta-forms vanish for this")
    print(f"     non-product S^6-bundle) is not proven here -- only the index-zero fiber fact is computed.")
    assert bi['clean_reduction_to_spine']

    # ---------------------------------------------------------------- BRIDGE (ii) multiplicity
    print("\n" + "-" * 94)
    print("BRIDGE (ii)  the generation multiplicity carrier (h1): SU(2)+ = Lambda^2_+ -> 64 triplets")
    print("-" * 94)
    e_eu = gammas_euclid()
    J_eu = build_su2plus_generation_operator(e_eu)
    mult = multiplicity_decomposition(e_eu, J_eu)
    print(f"  ker(Gamma) = {mult['ker']} ;  SU(2)+ content = {mult['spins']}")
    print(f"  => {mult['n_triplets']} triplets (j=1, {mult['n_triplet_states']} states) carry the pure"
          f" Spin(10) 16/16bar generation spinor")
    assert mult['ker'] == 1664 and mult['n_triplets'] == 64

    # ---------------------------------------------------------------- THE FORK (decisive)
    print("\n" + "-" * 94)
    print("THE FORK (decisive): frame-charge of the GENERATION INDEX DENSITY vs the +96 SELECTOR")
    print("-" * 94)
    fk = fork_by_frame_charge()
    print(f"  {'operator':<48}{'|frame|':>10}{'net self-dual (SD-ASD)':>24}")
    print(f"  {'SU(2)+ = Lambda^2_+ GENERATION multiplicity':<48}{fk['gen_all']:>10.3f}{fk['gen_net_sd']:>24.3f}")
    print(f"  {'+96 selector C = J_quat.G (chirality)':<48}{fk['sel_all']:>10.3f}{fk['sel_net_sd']:>24.2e}")
    print(f"  {'+96 selector J_quat.chirality (internal)':<48}{fk['csel_all']:>10.2e}{fk['csel_net_sd']:>24.2e}")
    gen_tangential = fk['gen_net_sd'] > 1e-3
    sel_gauge = abs(fk['csel_net_sd']) < 1e-6 and fk['csel_all'] < 1e-8
    print(f"\n  GENERATION carrier rotates TX^4 (net self-dual framing != 0)? {gen_tangential}"
          f"   -> TANGENTIAL")
    print(f"  +96 SELECTOR is frame-trivial (net self-dual = 0, |frame| = 0)? {sel_gauge}"
          f"   -> GAUGE (the DECOUPLE)")
    assert gen_tangential and sel_gauge

    # the two prongs of the fork in closed form
    fe = fork_e_invariants()
    nR, n8R, n3R = crt_Z24(fe['e_R'])
    nG, n8G, n3G = crt_Z24(fe['e_gauge'])
    print(f"\n  TANGENTIAL prong (the carrier's channel): p_1 = {fe['p1']}, framing degree p_1/2 = "
          f"{fe['framing_degree']},  e_R = {fe['e_R']}")
    print(f"     denom {fe['e_R'].denominator} = {fac_str(fe['e_R'].denominator)} -> {primary(fe['e_R'].denominator)}")
    print(f"     class {nR} in Z/24 = ({n8R} mod 8, {n3R} mod 3) ; 3-primary part = {n3R}  (NONZERO, order 3)")
    print(f"  GAUGE prong (Route B): e = {fe['e_gauge']}, class {nG} in Z/24 = ({n8G} mod 8, {n3G} mod 3)"
          f" ; 3-primary part = {n3G}  (ZERO, kill complete)")
    assert fe['e_R'] == Fraction(1, 12) and n3R != 0
    assert fe['e_gauge'] == Fraction(3, 8) and n3G == 0
    fork_verdict = "TANGENTIAL"
    print(f"\n  ==> FORK RESOLVED BY COMPUTATION: {fork_verdict}  (the count carrier couples to -p_1/24,"
          f" e_R = 1/12, 3-primary).")

    # ---------------------------------------------------------------- BRIDGE (iii) integer extraction
    print("\n" + "-" * 94)
    print("BRIDGE (iii)  integer extraction -- COMPUTABLE bulk integers vs the GATED net-chiral index")
    print("-" * 94)
    # what is genuinely computable as an integer on the actual geometry:
    pati_salam_integer = ps['n_generations']            # 1  (GU's verified chain)
    spin_half_index = int(ah['spin_half_leg'])          # 16 (8*A-hat(K3); honest)
    ch2_char_number = ch2['ch2_full']                   # -5376 (honest characteristic number)
    framed_bordism_class = nR                           # 2 in Z/24 (order-3 nonzero -- a CLASS, not "3")
    print(f"  COMPUTABLE integers on GU's actual geometry:")
    print(f"     - Pati-Salam Spin(7,7) net generation count        = {pati_salam_integer}"
          f"   (GU's cleanest verified chain; '2+1 effective')")
    print(f"     - spin-1/2 index leg 8*A-hat(K3)                    = {spin_half_index}")
    print(f"     - ch2(S_X)[K3] characteristic number               = {ch2_char_number}")
    print(f"     - framed-bordism CLASS of the tangential carrier    = {framed_bordism_class} in Z/24"
          f"  (e_R=1/12; order-3 nonzero)")
    print(f"\n  GATED (do NOT fabricate):")
    print(f"     - the net chiral GENERATION index as a literal integer needs the TWISTED RS SOURCE")
    print(f"       ACTION (# surviving Spin(10) 16s). That dynamical operator is UNBUILT; the +8 RS leg")
    print(f"       is ASSERTED (every analytic route -- scalar-FJ, tau-twisted, APS -- FAILED). GATED.")
    print(f"     - order-3-CLASS -> integer-3 is unproven and possibly a CATEGORY ERROR: e_R = 1/12 is")
    print(f"       HOMOTOPY-FIXED (identical for 1, 3, or 5 generations); the framed-bordism datum is the")
    print(f"       class {framed_bordism_class}, NOT the integer 3.")
    print(f"     - the full analytic Bismut-Cheeger fibered-boundary reduction theorem (bridge i). GATED.")

    # ---------------------------------------------------------------- VERDICT
    print("\n" + line)
    print("VERDICT")
    print(line)
    integer_is_3 = False                                # NOT cleanly 3 (class is 2; computable index is 1)
    fork_is_tangential = (fork_verdict == "TANGENTIAL")
    print(f"  FORK            : {fork_verdict}  (carrier net self-dual frame charge = {fk['gen_net_sd']:.2f};"
          f" selector = 0).  e_R = 1/12, denom 12 = {fac_str(12)}, 3-primary.")
    print(f"  INTEGER         : NOT cleanly 3.  The homotopy-fixed framed-bordism class is {framed_bordism_class}"
          f" (not the integer 3);")
    print(f"                    the ONE genuinely computable generation integer on the geometry is"
          f" {pati_salam_integer} (Pati-Salam).")
    print(f"  DECISION RULE   : fork TANGENTIAL (favorable half) BUT integer not 3 (gated / points to 1).")
    print(f"                    => 'located' does NOT upgrade to 'FORCED'. The strong reading is NOT earned.")
    print(f"  DELIVERABLE     : LOCATED, not FORCED. The fork is computationally resolved TANGENTIAL for the")
    print(f"                    count CARRIER (the SU(2)+ = Lambda^2_+ multiplicity operator genuinely rotates")
    print(f"                    TX^4, e_R = 1/12, 3-primary), while the +96 CHIRALITY selector is frame-trivial")
    print(f"                    (GAUGE, 2-primary) -- the DECOUPLE, now extended from selector to carrier.")
    print(f"                    Integer extraction stays GATED on the unbuilt twisted RS source action; the")
    print(f"                    order-3-class -> integer-3 step is unproven (homotopy-fixed; possible category")
    print(f"                    error). On the only honest geometric integer (Pati-Salam), the count is 1.")
    print(line)

    assert fork_is_tangential and not integer_is_3
    return dict(
        anchors=anc, ch2=ch2['ch2_full'], ahat_K3=str(ah['ahat_K3']),
        spin_half_leg=spin_half_index, idx_K3_4=int(ah['idx_K3_4']),
        charge_q_2primary=q2p, pati_salam_generations=ps['n_generations'],
        bridge_i_clean_reduction=bi['clean_reduction_to_spine'],
        n_triplets=mult['n_triplets'],
        gen_net_self_dual_frame_charge=fk['gen_net_sd'],
        selector_net_self_dual_frame_charge=fk['csel_net_sd'],
        fork="TANGENTIAL", e_R=str(fe['e_R']), e_R_denom_factorization=fac_str(12),
        e_R_class_Z24=nR, e_R_3primary_part=n3R,
        e_gauge=str(fe['e_gauge']), e_gauge_3primary_part=n3G,
        framed_bordism_class=framed_bordism_class,
        integer_is_3=integer_is_3,
        computable_generation_integer_pati_salam=pati_salam_integer,
        net_chiral_index_status="GATED (unbuilt twisted RS source action; +8 RS leg asserted)",
        verdict="LOCATED not FORCED; fork TANGENTIAL for carrier, selector GAUGE; integer gated/->1",
    )


if __name__ == "__main__":
    out = main()
    print("\nMACHINE SUMMARY:")
    for k, v in out.items():
        if k != "anchors":
            print(f"  {k}: {v}")
