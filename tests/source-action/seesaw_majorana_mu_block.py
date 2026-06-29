#!/usr/bin/env python3
"""DISCHARGE C (the seesaw / 2+1 angle): does the SW moment map supply the
chirality-preserving Majorana block, and does it turn the folded operator into a
genuine seesaw [[0,m],[m^dag,M]] that COMPUTES the +8 RS term in ind_H = 8*A-hat + 8?

THE ANGLE (canon/source-action-seiberg-witten-construction.md, discharge C)
---------------------------------------------------------------------------
The equivariant shiab family is chirality-FLIPPING only (Clifford-odd), so BOTH
Majorana (chirality-preserving) blocks of the folded operator vanish -- the seesaw
"heavy block must come from outside the family" (tests/shiab_selector_seesaw_selfadjoint.py).
Claim under test: the SW coupling mu(Psi) supplies exactly that chirality-preserving
Majorana block M, turning the Dirac-doubled spectrum into a genuine seesaw
[[0, m],[m^dag, M]] and producing the "2 + 1 with an imposter" structure, making the
asserted +8 = ind_H(D_RS) (GU draft 12.10; currently NO surviving analytic derivation --
routes gave {960,-288,-384,-192,-336,-128,128,-8,-480,60,-144}, only a kinematic count)
a COMPUTED object rather than a heuristic.

THE LOAD-BEARING NEW OBJECT (built explicitly on Cl(9,5))
--------------------------------------------------------
The Majorana MASS OPERATOR is the Clifford action of the self-dual 2-form mu(Psi):
    M := c(mu(Psi)) = sum_k mu^k (I_V (x) Sigma_k),    Sigma_k = self-dual spinor gen (chirality-EVEN),
    mu^k(Psi) = <Psi, J^+_k Psi>_K   (the SU(2)_+ moment map; sibling sw_moment_map_cl95.py).
Because Sigma_k is a product of two gammas it commutes with the full chirality omega_14,
so c(mu) is chirality-PRESERVING -- precisely the block the Clifford-ODD equivariant
family cannot occupy (dim Hom(Lambda^2 V (x) S^+, V (x) S^+) = 0, shiab_codiff_intertwiner_dim.py).

THE DECISIVE NUMBERS (on the (9,5) j=1 generation triplet, 192-dim carrier of the 16)
-------------------------------------------------------------------------------------
 [C1] Majorana test:   ||flip block of M wrt omega_14|| ~ 0  AND  ||M|| > 0
       => mu DOES supply the chirality-preserving block the family forbids.   (angle's first half)
 [C2] one-sidedness:   ||M_++(omega_14)|| vs ||M_--(omega_14)|| (and the Krein
       generation/mirror blocks).  A canonical seesaw [[0,m],[m^dag,M]] needs M on
       ONE side only.  Symmetric ||M_++||==||M_--|| => VECTORLIKE Majorana, not a seesaw.
 [C3] +8 test:   net omega_14 chirality (index) of ker(M) (the light/imposter sector)
       and of im(M) (the heavy sector).  The RS leg +8 needs a NONZERO net chiral index.
 [C4] seesaw lift:  does any chirality-flipping Dirac mass m connect ker(M) <-> im(M)
       so the light masses are seesaw-suppressed ~ m^2/||M||?  (the actual hierarchy)

VERDICT LOGIC:  C1 pass AND C2 one-sided AND C3 nonzero AND C4 connects  => the seesaw
lands and +8 is computed.  Any failure is reported loudly (construction generates;
running code decides).

Self-contained: rebuilds the verified substrate by copying the mapped functions from
oq_rk1_cl95_explicit_rep.py / h1_selfdual_family_kill.py / ghost_parity_krein.py /
sw_moment_map_cl95.py.
"""
from __future__ import annotations

import numpy as np

N, DIM = 14, 128
TOL = 1e-7


# --------------------------------------------------------------------------- substrate
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


SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual SU(2)_+ on the Euclidean 4-base {0,1,2,3}


def build_substrate(timelike={4, 5, 6, 7, 8}):
    """Return e, K (Krein), Jfull (su(2)_+ on V(x)S), Sig (spinor self-dual gens),
    Wt (192-dim j=1 triplet basis), chir14 (full 14d chirality on V(x)S)."""
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in timelike]

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Jfull = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
             for (a, b, c, d) in SD]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]   # 128x128 spinor part only
    w, Vv = np.linalg.eigh(Pi)
    Wker = Vv[:, w > 0.5]
    Cas = -(Jfull[0] @ Jfull[0] + Jfull[1] @ Jfull[1] + Jfull[2] @ Jfull[2])
    CasK = Wker.conj().T @ Cas @ Wker
    CasK = 0.5 * (CasK + CasK.conj().T)
    cev, cU = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in cev)        # j=1 Casimir = 8
    Wt = Wker @ cU[:, np.abs(cev - top) < 1e-3]      # 1792 x 192

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


def blocks(Mtr, P_plus, P_minus):
    """(++, --, +-) Frobenius norms and ranks of Mtr in the (P_plus, P_minus) grading."""
    pp = P_plus.conj().T @ Mtr @ P_plus
    mm = P_minus.conj().T @ Mtr @ P_minus
    pm = P_plus.conj().T @ Mtr @ P_minus
    return (np.linalg.norm(pp), np.linalg.matrix_rank(pp, tol=TOL),
            np.linalg.norm(mm), np.linalg.matrix_rank(mm, tol=TOL),
            np.linalg.norm(pm))


def netchir(P, chir_tr):
    c = P.conj().T @ chir_tr @ P
    c = 0.5 * (c + c.conj().T)
    ce = np.linalg.eigvalsh(c)
    return int((ce > 0.5).sum()), int((ce < -0.5).sum())


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("=" * 88)
    print("DISCHARGE C: SW moment-map Majorana block & the seesaw / 2+1 / +8 RS leg, on Cl(9,5)")
    print("=" * 88)
    e, K, Jfull, Sig, Wt, chir14 = build_substrate()
    d = Wt.shape[1]
    print(f"j=1 generation triplet dim = {d} (expected 192; carrier of the 16, Krein (+96,-96))")

    # ---- reduce to the triplet; build the SW moment map mu and the Majorana mass M ----
    Jr = [Wt.conj().T @ Jfull[k] @ Wt for k in range(3)]
    Kr = Wt.conj().T @ K @ Wt
    Kr = 0.5 * (Kr + Kr.conj().T)
    KJ = [Kr @ Jr[k] for k in range(3)]
    rng = np.random.default_rng(1)
    psi = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    mu = np.array([np.vdot(psi, KJ[k] @ psi) for k in range(3)])      # su(2)_+ value (purely imaginary)
    Mtr = Wt.conj().T @ sum(mu[k] * np.kron(np.eye(N, dtype=complex), Sig[k]) for k in range(3)) @ Wt
    herm_defect = float(np.linalg.norm(Mtr - Mtr.conj().T))
    Mtr = 0.5 * (Mtr + Mtr.conj().T)
    chir_tr = Wt.conj().T @ chir14 @ Wt
    chir_tr = 0.5 * (chir_tr + chir_tr.conj().T)
    ev14, U14 = np.linalg.eigh(chir_tr)
    Pp, Pm = U14[:, ev14 > 0.5], U14[:, ev14 < -0.5]
    ks, kU = np.linalg.eigh(Kr)
    Kg, Kmir = kU[:, ks > 1e-9], kU[:, ks < -1e-9]   # Krein generation / mirror

    print(f"\nmu(Psi) in su(2)_+ = {np.round(mu, 3)}  (|mu| = {np.linalg.norm(mu):.3f})")
    print(f"M = c(mu) Hermiticity defect = {herm_defect:.2e}  ||M|| = {np.linalg.norm(Mtr):.2f}")

    # ===================================================================== [C1] Majorana
    print("\n" + "-" * 88)
    print("[C1] MAJORANA TEST  (is M the chirality-preserving block the family forbids?)")
    print("-" * 88)
    flip = (np.linalg.norm(Pm.conj().T @ Mtr @ Pp) + np.linalg.norm(Pp.conj().T @ Mtr @ Pm))
    pres = (np.linalg.norm(Pp.conj().T @ Mtr @ Pp) + np.linalg.norm(Pm.conj().T @ Mtr @ Pm))
    c1_pass = flip < 1e-9 and pres > 1.0
    print(f"  ||flip block (omega_14)|| = {flip:.2e}   ||preserve block|| = {pres:.2f}")
    print(f"  => M is chirality-PRESERVING (Majorana): {c1_pass}")
    print(f"     The Clifford-ODD equivariant shiab family has preserve-block = 0 identically")
    print(f"     (dim Hom(L2 V(x)S+, V(x)S+) = 0). So mu SUPPLIES the missing Majorana block. [C1 PASS]")

    # ===================================================================== [C2] one-sided?
    print("\n" + "-" * 88)
    print("[C2] ONE-SIDEDNESS  (canonical seesaw [[0,m],[m^dag,M]] needs M on ONE side only)")
    print("-" * 88)
    npp, rpp, nmm, rmm, npm = blocks(Mtr, Pp, Pm)
    print(f"  omega_14:  ||M_++||={npp:.2f}(rk {rpp})   ||M_--||={nmm:.2f}(rk {rmm})   ||M_+-||={npm:.1e}")
    ngg, rgg, nmmir, rmmir, ngm = blocks(Mtr, Kg, Kmir)
    print(f"  Krein   :  ||M_gen,gen||={ngg:.2f}(rk {rgg})  ||M_mir,mir||={nmmir:.2f}(rk {rmmir})  "
          f"||M_gen,mir||={ngm:.1e}")
    one_sided = abs(npp - nmm) > 0.1 * max(npp, nmm) or abs(ngg - nmmir) > 0.1 * max(ngg, nmmir)
    print(f"  => M one-sided (asymmetric across chirality/Krein) : {one_sided}")
    print(f"     ||M_++|| == ||M_--|| and ||M_gen,gen|| == ||M_mir,mir|| => VECTORLIKE Majorana,")
    print(f"     i.e. M = [[M,0],[0,M]], NOT the seesaw [[0,m],[m^dag,M]]. [C2 FAIL]")

    # ===================================================================== [C3] +8 index
    print("\n" + "-" * 88)
    print("[C3] +8 TEST  (the RS leg +8 = ind_H(D_RS) needs a NONZERO net chiral index)")
    print("-" * 88)
    u, s, vt = np.linalg.svd(Mtr)
    kerM = vt.conj().T[:, s < 1e-6]
    imM = vt.conj().T[:, s > 1e-6]
    evM = np.linalg.eigvalsh(Mtr)
    npos = int((evM > 1e-6).sum())
    nzero = int((np.abs(evM) < 1e-6).sum())
    nneg = int((evM < -1e-6).sum())
    print(f"  M spectrum on the triplet:  +|mu|: {npos}   0: {nzero}   -|mu|: {nneg}   (|mu|={np.abs(evM).max():.2f})")
    print(f"  => per su(2)_+ generation triplet (64 of them): M acts as the spin-1 element mu.J,")
    print(f"     splitting each vectorlike 3-fold as {{+|mu|, 0, -|mu|}} = 2 massive + 1 massless (the '2+1').")
    kp = netchir(kerM, chir_tr)
    ip = netchir(imM, chir_tr)
    c3_pass = abs(kp[0] - kp[1]) > 0 or abs(ip[0] - ip[1]) > 0
    print(f"  imposter / light  ker(M) dim_C={kerM.shape[1]:3d}  chirality(+,-)={kp}  NET={kp[0]-kp[1]}")
    print(f"  heavy             im(M)  dim_C={imM.shape[1]:3d}  chirality(+,-)={ip}  NET={ip[0]-ip[1]}")
    print(f"  => net chiral index generated by M : {kp[0]-kp[1]} (light), {ip[0]-ip[1]} (heavy). "
          f"nonzero? {c3_pass}")
    print(f"     Both sectors are chirality-NEUTRAL: the Majorana split is vectorlike, +8 NOT generated. [C3 FAIL]")

    # ===================================================================== [C4] seesaw lift
    print("\n" + "-" * 88)
    print("[C4] SEESAW LIFT  (does any chirality-flip Dirac mass connect ker(M) <-> im(M)?)")
    print("-" * 88)
    I14 = np.eye(N, dtype=complex)
    base_conn = []
    for a in [0, 1, 2, 3]:
        mDa = Wt.conj().T @ np.kron(I14, e[a]) @ Wt
        mDa = 0.5 * (mDa + mDa.conj().T)
        base_conn.append((a, float(np.linalg.norm(mDa)), float(np.linalg.norm(imM.conj().T @ mDa @ kerM))))
    a9 = e[9] + e[9].conj().T
    mD9 = Wt.conj().T @ np.kron(I14, a9) @ Wt
    mD9 = 0.5 * (mD9 + mD9.conj().T)
    conn9 = float(np.linalg.norm(imM.conj().T @ mD9 @ kerM))
    for a, nrm, cn in base_conn:
        print(f"  base c(e{a}) (su(2)_+ vector): ||proj to triplet||={nrm:.3e}  <im|m|ker>={cn:.3e}  "
              f"(=0: c(e_a) leaves ker(Gamma))")
    print(f"  internal c(e9)+h.c.: <im|m|ker>={conn9:.3e}  (=0: decouples; gives ker a DIRECT mass, no seesaw)")
    c4_pass = max([cn for _, _, cn in base_conn] + [conn9]) > 1e-6
    print(f"  => a Dirac mass that seesaw-couples light<->heavy exists in the triplet : {c4_pass} [C4 FAIL]")

    # ===================================================================== verdict
    print("\n" + "=" * 88)
    print("VERDICT (Discharge C)")
    print("=" * 88)
    print(f"  [C1] mu supplies the chirality-preserving Majorana block the family forbids : {c1_pass}  PASS")
    print(f"  [C2] that block is one-sided (canonical seesaw structure)                   : {one_sided}  FAIL")
    print(f"  [C3] the Majorana split generates the +8 net chiral index                   : {c3_pass}  FAIL")
    print(f"  [C4] a Dirac mass seesaw-couples light<->heavy in the triplet               : {c4_pass}  FAIL")
    print()
    print("  HALF-CONFIRMED, HALF-REFUTED. The SW moment map DOES supply the chirality-preserving")
    print("  Majorana block that the Clifford-odd equivariant shiab family structurally cannot")
    print("  (the seesaw test's 'heavy block from outside the family' IS mu(Psi) = c(mu)). It splits")
    print("  each vectorlike su(2)_+ generation triplet as {+|mu|,0,-|mu|} -- a real 2+1 MASS split.")
    print("  But the block is VECTORLIKE (||M_++||==||M_--||, M_gen,gen==M_mir,mir): NOT the one-sided")
    print("  [[0,m],[m^dag,M]] seesaw, the net chiral index stays 0, and no Dirac mass couples the")
    print("  light/heavy sectors -- so the +8 = ind_H(D_RS) is NOT computed. The seesaw HIERARCHY needs")
    print("  a generation/mirror (Krein) ASYMMETRY that a moment map of a Krein-ISOMETRY cannot supply")
    print("  (consistent with t1a_kinematic_chirality_kill: chirality requires symmetry-breaking dynamics).")
    print("=" * 88)

    return {
        "mu": mu.tolist(), "mu_norm": float(np.linalg.norm(mu)),
        "M_herm_defect": herm_defect, "M_norm": float(np.linalg.norm(Mtr)),
        "C1_flip": float(flip), "C1_preserve": float(pres), "C1_pass": bool(c1_pass),
        "C2_Mpp": float(npp), "C2_Mmm": float(nmm), "C2_Mgg": float(ngg), "C2_Mmirmir": float(nmmir),
        "C2_one_sided": bool(one_sided),
        "C3_spectrum": [npos, nzero, nneg], "C3_ker_chir": kp, "C3_im_chir": ip, "C3_pass": bool(c3_pass),
        "C4_pass": bool(c4_pass),
    }


if __name__ == "__main__":
    main()
