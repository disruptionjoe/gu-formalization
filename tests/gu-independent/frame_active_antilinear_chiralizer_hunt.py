#!/usr/bin/env python3
r"""
GU-INDEPENDENT ESCAPE HUNT: a FRAME-NON-TRIVIAL antilinear chiralizer?

The campaign established (computed-on-substrate, capstone):
  - carrier (192-dim Lambda^2_+ j=1 triplet) is VECTORLIKE: Krein (+96,-96), net chirality 0.
  - net chirality is a LINEAR invariant: no gauge-equivariant linear Krein-unitary breaks +96/-96.
  - the unique net-chiral escape on the substrate is ANTILINEAR: C = J_quat . G, C^2 = -1 (AZ CII).
  - BUT that C is FRAME-TRIVIAL: J_quat = id_14 (x) U (spinor-only); its NET SELF-DUAL frame charge
    (SD-ASD = the p_1 / instanton number) is 0, so it cannot source the tangential -p_1/24 channel
    where the order-3 carrier (frame charge 33.94, e_R=1/12) lives.

Honest open flags from the capstone integrity section that THIS script attacks head-on:
  (#2) "frame charge 0.00 is structural/definitional -- any spinor-only op gives 0."
  (#3) "C = J_quat.G is the unique chiral projector is campaign-ASSERTED, not computed."

So: is the frame-triviality STRUCTURAL or EVADABLE? STEELMAN the escape -- try HARD to construct an
operator that is simultaneously
  (1) ANTILINEAR with C^2 = +-1 (the only index-changing class),
  (2) NET-CHIRAL CAPABLE: chirality-PRESERVING ([C, Gamma_chir] = 0) so it can select a chirality-pure
      Kramers sector (the "+96 reached" mechanism), and C^2 = -1 (CII) -- as opposed to chirality-
      REVERSING ({C,Gamma}=0) which only Dirac-pairs +/- (net 0),
  (3) FRAME-NON-TRIVIAL in the LOAD-BEARING sense: NET SELF-DUAL frame charge (SD - ASD) != 0
      (carries p_1, reaches the tangential framing channel).

A candidate achieving all three is the ESCAPE. We test GU's baseline plus a battery of genuinely
frame-active antilinear constructions (self-dual frame rotation dressings, gamma-soldering reality
structures, frame-reflection CPT, direct frame(x)spinor chiralizer tensors). Be ruthless: report
honestly if every net-chiral candidate collapses to net-SD frame charge 0.

All numbers computed on the verified Cl(9,5)=M(64,H) substrate. Run:
  python tests/gu-independent/frame_active_antilinear_chiralizer_hunt.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM            # 14, 128
ETA_SIG = np.array([1.0] * 9 + [-1.0] * 5)
TIMELIKE = {4, 5, 6, 7, 8}                     # base {0,1,2,3} is EUCLIDEAN (spacelike)
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
ASD = [(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1)]
I14 = np.eye(N, dtype=complex)
I128 = np.eye(DIM, dtype=complex)


# ------------------------------------------------------------------ builders
def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def quaternionic_J(e128, seed=1):
    """Phase-unique quaternionic structure J_quat = id_14 (x) U of M(64,H)."""
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


def frame_charge_split(O, sd_gens, asd_gens):
    """Return (total, SD, ASD, net_SD=SD-ASD): O's coupling to base tangent-frame so(4) gens.
    F_L = Tr_128[(L (x) I_128)^dag O]/||L||^2; charge = sum_L ||F_L||_F. NET self-dual = the p_1 proxy."""
    O4 = O.reshape(N, DIM, N, DIM)

    def charge(gens):
        tot = 0.0
        for L in gens:
            nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
            F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
            tot += float(np.linalg.norm(F_L))
        return tot
    sd, asd = charge(sd_gens), charge(asd_gens)
    allg = sd_gens + asd_gens
    return charge(allg), sd, asd, sd - asd


def build():
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    e128 = gu_bridge.gammas()
    Q = np.eye(N * DIM, dtype=complex) - Pi
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchors moved"

    # carrier = 192-dim j=1 self-dual triplet
    J3full = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d))
              + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = Wk.conj().T @ Cas @ Wk
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uc[:, np.abs(ev - top) < 1e-3]

    # Krein form + chirality grading
    spacelike = [a for a in range(N) if a not in TIMELIKE]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e128[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
    Kful = np.kron(etaV, bS)
    om = I128.copy()
    for a in range(N):
        om = om @ e128[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir_int = om if om2 > 0 else (-1j) * om
    Gamma_chir = np.kron(I14, chir_int)

    sd_gens = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd_gens = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]

    return dict(e=e, e128=e128, Pi=Pi, Q=Q, Gamma=Gamma, M_D=M_D, Wt=Wt, Kful=Kful,
                Gamma_chir=Gamma_chir, chir_int=chir_int, J3full=J3full, bS=bS,
                sd_gens=sd_gens, asd_gens=asd_gens, bare=bare, C2=C2)


# ------------------------------------------------------------------ measurement of a candidate
def analyze(name, M, S, verbose=True):
    """M = the LINEAR (unitary) part of the antilinear operator C = M . K (K = complex conjugation).
    Measures: unitarity, C^2 sign, chirality commutation type on the carrier (net-chiral capable?),
    frame charge split (net-SD = p_1 proxy), carrier preservation. Returns a dict."""
    Wt, G, Gamma_chir = S['Wt'], None, S['Gamma_chir']
    sd_gens, asd_gens = S['sd_gens'], S['asd_gens']

    # unitarity of the linear part
    unit_defect = float(np.linalg.norm(M.conj().T @ M - np.eye(N * DIM)))

    # C = M.K antilinear; C^2 = M conj(M).
    Csq = M @ M.conj()
    csq_p = float(np.linalg.norm(Csq - np.eye(N * DIM)))
    csq_m = float(np.linalg.norm(Csq + np.eye(N * DIM)))
    c2sign = -1 if csq_m < csq_p else +1
    c2defect = min(csq_p, csq_m)

    # frame charge split on the FULL operator (where frame structure lives)
    tot, sd, asd, netsd = frame_charge_split(M, sd_gens, asd_gens)

    # carrier preservation: does C map Wt -> Wt? C(Wt x) = M conj(Wt) conj(x); component outside Wt:
    Pw = Wt @ Wt.conj().T
    MconjW = M @ Wt.conj()
    out_of_carrier = float(np.linalg.norm(MconjW - Pw @ MconjW)) / max(float(np.linalg.norm(MconjW)), 1e-30)

    # chirality commutation type on the carrier (the rigorous net-chiral criterion).
    # carrier rep of antilinear C: x -> A_W conj(x), A_W = Wt^dag M conj(Wt).
    A_W = Wt.conj().T @ M @ Wt.conj()
    Gw = Wt.conj().T @ Gamma_chir @ Wt
    Gw = 0.5 * (Gw + Gw.conj().T)
    # antilinear [C,Gamma]: C Gamma x = A_W conj(Gamma) conj(x); Gamma C x = Gamma A_W conj(x)
    Gw_c = Gw.conj()
    comm = float(np.linalg.norm(A_W @ Gw_c - Gw @ A_W))
    acomm = float(np.linalg.norm(A_W @ Gw_c + Gw @ A_W))
    # normalize by operator size on carrier
    sc = max(float(np.linalg.norm(A_W)), 1e-30)
    chir_type = "PRESERVING (net-chiral capable)" if comm < acomm else "REVERSING (Dirac-pair, net 0)"

    # carrier C^2 sign (the Kramers/CII check on the carrier specifically)
    Csq_W = A_W @ A_W.conj()
    nrmW = max(float(np.linalg.norm(A_W @ A_W.conj())), 1e-30)
    # normalize A_W to unitary-ish before squaring sign read
    # use ratio test
    cW_p = float(np.linalg.norm(Csq_W - np.eye(Csq_W.shape[0]) * (np.trace(Csq_W).real / Csq_W.shape[0])))

    # net-chiral capability flag: chirality-preserving AND genuinely couples within both blocks
    net_chiral_capable = (comm < acomm * 0.5) and (out_of_carrier < 1e-6)

    res = dict(name=name, unit_defect=unit_defect, c2sign=c2sign, c2defect=c2defect,
               frame_total=tot, frame_sd=sd, frame_asd=asd, frame_netSD=netsd,
               out_of_carrier=out_of_carrier, chir_comm=comm / sc, chir_acomm=acomm / sc,
               chir_type=chir_type, net_chiral_capable=bool(net_chiral_capable))
    if verbose:
        print(f"\n  [{name}]")
        print(f"    linear part unitary? defect = {unit_defect:.2e}")
        print(f"    antilinear C^2 = {c2sign:+d}  (defect {c2defect:.2e})")
        print(f"    carrier-preserving? out-of-carrier leakage = {out_of_carrier:.2e}")
        print(f"    chirality commutation on carrier: [C,G]/|C| = {comm/sc:.3e}, "
              f"{{C,G}}/|C| = {acomm/sc:.3e}  -> {chir_type}")
        print(f"    frame charge: total = {tot:.4f}  SD = {sd:.4f}  ASD = {asd:.4f}  "
              f"NET-SD (p_1 proxy) = {netsd:+.4f}")
        verdict = ("ESCAPE CANDIDATE" if (net_chiral_capable and c2sign == -1 and abs(netsd) > 1e-6)
                   else "no escape")
        print(f"    => net-chiral-capable={net_chiral_capable}, C^2=-1={c2sign==-1}, "
              f"|net-SD|>0={abs(netsd)>1e-6}   :: {verdict}")
    return res


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    print("=" * 94)
    print("HUNT: a FRAME-NON-TRIVIAL (net-SD != 0) ANTILINEAR NET-CHIRAL operator -- the escape?")
    print("=" * 94)
    S = build()
    e, e128, Pi, Q = S['e'], S['e128'], S['Pi'], S['Q']
    Wt, Gamma_chir, chir_int = S['Wt'], S['Gamma_chir'], S['chir_int']
    sd_gens, asd_gens, J3full = S['sd_gens'], S['asd_gens'], S['J3full']
    print(f"[anchors] bare = {S['bare']:.4f} (58.7215), C2 = {S['C2']:.4f} (155.3625); carrier dim "
          f"{Wt.shape[1]}")

    # reference: carrier su(2)+ generator net-SD frame charge (the 3-primary target = 33.94)
    su2p = J3full[0] + J3full[1] + J3full[2]
    t, sd, asd, netsd = frame_charge_split(su2p, sd_gens, asd_gens)
    print(f"[reference] carrier su(2)+ (Lambda^2_+) NET-SD frame charge = {netsd:.3f} (target 33.94, "
          f"3-primary, where a count would live)")

    G_bulk = Pi - Q
    U = quaternionic_J(e128, seed=1)
    Jf = np.kron(I14, U)                                   # J_quat = id_14 (x) U

    results = []

    # ---------------- (A) GU baseline: C = J_quat . G  (frame-trivial) ----------------
    print("\n" + "-" * 94)
    print("(A) BASELINE  C = J_quat . G   (GU's actual net-chiral escape; expect net-SD = 0)")
    print("-" * 94)
    M_A = Jf @ G_bulk.conj()       # unitary part of antiunitary C = J_quat.G (acts: C x = M_A conj(x))
    results.append(analyze("A: J_quat.G (GU)", M_A, S))

    # ---------------- (B) self-dual FRAME-ROTATION dressing of the antilinear escape ----------------
    # F = exp(theta * J_+) is a finite tangent-frame self-dual rotation (frame-active, LINEAR, K-unitary).
    # C' = F . C_GU is antilinear. Does it stay net-chiral AND gain net-SD frame charge?
    print("\n" + "-" * 94)
    print("(B) FRAME-DRESSED  C' = F . C_GU,  F = exp(theta * su(2)_+ self-dual frame rotation)")
    print("    (the hardest natural try: graft the carrier's OWN frame-active self-dual content onto the")
    print("     net-chiral antilinear escape)")
    print("-" * 94)
    from scipy.linalg import expm
    for theta in (0.3, 0.7, 1.2):
        F = expm(theta * (su2p - su2p.conj().T) * 0.5)     # unitary frame-active self-dual rotation
        M_B = F @ M_A
        results.append(analyze(f"B: exp({theta}*su2+).C_GU", M_B, S))

    # ---------------- (C) gamma-SOLDERING reality structure (genuinely frame<->spinor mixing) -------
    # R_sol = sum_a (frame shift P_a) (x) gamma_a : the ONE object NOT of id_14(x)U form. Build an
    # antilinear C_sol = R_sol-based reality structure and measure.
    print("\n" + "-" * 94)
    print("(C) GAMMA-SOLDERING reality structure  C_sol from R = sum_a E_a (x) gamma_a")
    print("    (uses the RS field's genuine tangent-VECTOR index via the soldering form -- the only")
    print("     frame<->spinor mixing object; candidate (i) in the brief)")
    print("-" * 94)
    # soldering: R = sum_a |a><a-cyclic| (x) e_a  -- a frame permutation tied to gamma_a.
    # Use a frame self-dual pairing: R = sum over sd pairs (E_{ij}-E_{ji}) (x) (e_i e_j) to stay in so-rep.
    R = np.zeros((N * DIM, N * DIM), dtype=complex)
    for (a, b, c, d) in SD:
        for (i, j) in ((a, b), (c, d)):
            Eij = np.zeros((N, N), dtype=complex)
            Eij[i, j] = 1.0
            Eij[j, i] = -1.0
            R = R + np.kron(Eij, e128[i] @ e128[j])
    # antilinearize via the spinor reality bS (charge-conjugation core)
    Bspin = np.kron(I14, S['bS'])
    M_C = R @ Bspin
    # unitarize the linear part (polar) so C^2 sign is readable
    Uc_, _, Vc_ = np.linalg.svd(M_C)
    M_C = Uc_ @ Vc_
    results.append(analyze("C: gamma-soldering", M_C, S))

    # ---------------- (D) frame-REFLECTION CPT (antiunitary part acts on the 14-frame) -------------
    print("\n" + "-" * 94)
    print("(D) FRAME-REFLECTION CPT  C = (R_frame (x) B_spin) . K,  R_frame flips the 5 timelike axes")
    print("    (candidate (iii): a CT/CPT whose antiunitary part is frame-ACTIVE)")
    print("-" * 94)
    Rframe = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
    M_D2 = np.kron(Rframe, S['bS']) @ Gamma_chir          # frame reflection x spinor charge-conj x chirality
    Uc_, _, Vc_ = np.linalg.svd(M_D2)
    M_D2 = Uc_ @ Vc_
    results.append(analyze("D: frame-reflection CPT", M_D2, S))

    # ---------------- (E) direct frame(x)spinor chiralizer tensor -----------------------------------
    # M = (self-dual frame rotation generator exponential) (x) (U . chirality) -- force BOTH factors active
    print("\n" + "-" * 94)
    print("(E) DIRECT TENSOR  M = exp(t*L_sd^frame) (x) (U.omega),  antilinear via K")
    print("    (force the frame factor self-dual-active AND the spinor factor the chiralizer at once)")
    print("-" * 94)
    Lsd = sd_gens[0]
    for t in (0.5, 1.0):
        Ffac = expm(t * Lsd)                              # 14x14 self-dual frame rotation (real, orthogonal)
        M_E = np.kron(Ffac, U @ chir_int)
        Uc_, _, Vc_ = np.linalg.svd(M_E)
        M_E = Uc_ @ Vc_
        results.append(analyze(f"E: exp({t}Lsd)(x)Uw", M_E, S))

    # ---------------- (F) push HARDEST: antilinear net-chiral with maximal net-SD by construction ----
    # Build C = J_quat.G but replace id_14 with a self-dual frame rotation in the SAME slot, i.e.
    # M = (frame self-dual) (x) U applied to G. This is the most direct attempt to KEEP the proven
    # net-chiral mechanism (J_quat.G) while making the frame factor non-trivial AND self-dual.
    print("\n" + "-" * 94)
    print("(F) HARDEST  M = (exp(L_sd) (x) U) . G   -- the net-chiral mechanism with a self-dual FRAME")
    print("    factor swapped in for id_14 (most direct attempt to keep net-chirality AND get net-SD)")
    print("-" * 94)
    for t in (0.4, 0.9):
        Jframe = np.kron(expm(t * sd_gens[0]), U)
        M_F = Jframe @ G_bulk.conj()
        Uc_, _, Vc_ = np.linalg.svd(M_F)
        M_F = Uc_ @ Vc_
        results.append(analyze(f"F: (exp({t}Lsd)(x)U).G", M_F, S))

    # ---------------- VERDICT ----------------
    print("\n" + "=" * 94)
    print("VERDICT")
    print("=" * 94)
    escapes = [r for r in results if r['net_chiral_capable'] and r['c2sign'] == -1
               and abs(r['frame_netSD']) > 1e-6]
    netchiral = [r for r in results if r['net_chiral_capable'] and r['c2sign'] == -1]
    print(f"  candidates tested: {len(results)}")
    print(f"  net-chiral-capable (chirality-preserving antilinear, C^2=-1): "
          f"{[r['name'] for r in netchiral] or 'NONE'}")
    print(f"  of those, NET-SD frame charge != 0 (the ESCAPE): {[r['name'] for r in escapes] or 'NONE'}")
    print()
    if escapes:
        print("  *** ESCAPE FOUND: a frame-non-trivial antilinear net-chiral operator exists. ***")
        for r in escapes:
            print(f"      {r['name']}: net-SD = {r['frame_netSD']:+.3f}, C^2=-1, chirality-preserving")
    else:
        print("  NO ESCAPE among these candidates.")
        print("  Every operator that is net-chiral-capable (chirality-preserving antilinear, C^2=-1)")
        print("  has NET SELF-DUAL frame charge = 0; every operator with net-SD != 0 either FAILED to")
        print("  preserve the carrier, was chirality-REVERSING (Dirac-pair, net 0), or was not C^2=-1.")
        print("  Tabulating the trade-off below to expose the mechanism:")
    print()
    print(f"  {'candidate':28s} {'C^2':>4} {'netChiral':>9} {'carrier-leak':>12} {'NET-SD':>9}")
    for r in results:
        print(f"  {r['name']:28s} {r['c2sign']:>+4d} {str(r['net_chiral_capable']):>9} "
              f"{r['out_of_carrier']:>12.2e} {r['frame_netSD']:>+9.3f}")

    return dict(n=len(results), escapes=[r['name'] for r in escapes],
                netchiral=[r['name'] for r in netchiral],
                rows=[(r['name'], r['c2sign'], r['net_chiral_capable'],
                       r['out_of_carrier'], r['frame_netSD']) for r in results])


if __name__ == "__main__":
    out = main()
    print("\n[machine-readable]", out)
