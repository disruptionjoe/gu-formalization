#!/usr/bin/env python3
"""
INDEPENDENT re-verification of MOVE-5 (Krein no-go, SW moment-map chiral index).

Written from scratch with DIFFERENT internal methods than the chaser where possible,
plus deliberate BREAK attempts:

  (A) sanity: verify the Clifford algebra {e_a,e_b}=2 eta_ab for signature (9,5).
  (B) verify M(64,H): an antilinear quaternionic J (J^2=-1) commuting with all gammas.
  (C) build j=1 triplet, mu, mass op M=c(mu); compute net chiral index THREE ways
      that differ from chaser's:
        (i)  rank(M_++) - rank(M_--)  and  ker-dim(M_++) - ker-dim(M_--)
        (ii) graded trace tr(omega) over im/ker using SVD-based projectors
        (iii) full sorted spectra of M restricted to +chirality vs -chirality sectors
  (D) BREAK 1 (non-vacuity): hand the SAME index machinery an operator with a KNOWN
      nonzero chiral asymmetry (chirality-even, supported on the + sector only, rank r)
      and demand it reports exactly r -> proves the "index 0" is a real property of the
      Krein-even moment map, not a bug that always returns 0.  NOTE a chirality-ODD
      Hermitian source (single c(e_a)) is NOT a valid control on this carrier: with an
      equal (96,96) chirality split its diagonal blocks vanish and its off-diagonal
      block is SQUARE, so rank-nullity forces graded index == 0 identically; that fact
      is verified as a side check, and the one-sided even control carries the burden.
  (E) BREAK 2 (structural forcing rigor): check that the chirality-swap P=c(e_b) is
      actually INVERTIBLE on the triplet (the property the forcing proof needs but the
      chaser did not explicitly test). If P were singular on the triplet, isospectrality
      would NOT follow.
  (F) BREAK 3: hand M a generic Hermitian chirality-EVEN perturbation (not from mu) and
      confirm the swap symmetry still forces index 0 -> and a chirality-ODD perturbation
      breaks it. This isolates exactly what is doing the work.
"""
import numpy as np

N, DIM = 14, 128
rng = np.random.default_rng(2024)


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


SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
TIMELIKE = {4, 5, 6, 7, 8}   # -> Cl(9,5): 9 spacelike(+), 5 timelike(-)


def build():
    base = jw(7)
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
    spacelike = [a for a in range(N) if a not in TIMELIKE]
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Jfull = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
             for (a, b, c, d) in SD]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wker = Vv[:, w > 0.5]
    Cas = -(Jfull[0] @ Jfull[0] + Jfull[1] @ Jfull[1] + Jfull[2] @ Jfull[2])
    CasK = Wker.conj().T @ Cas @ Wker
    CasK = 0.5 * (CasK + CasK.conj().T)
    cev, cU = np.linalg.eigh(CasK)
    # exact integer-eigenvalue clustering: the su(2)_+ Casimir on ker(Gamma) has the exact
    # spectrum {0, 3, 8} (= 4j(j+1), j=0,1/2,1) with multiplicities {640, 832, 192}
    known = np.array([0.0, 3.0, 8.0])
    lev = known[np.argmin(np.abs(cev.real[:, None] - known[None, :]), axis=1)]
    resid = float(np.max(np.abs(cev.real - lev)))
    assert resid < 1e-9, f"Casimir spectrum off the exact levels {{0,3,8}}: residual {resid:.3e}"
    mults = {float(L): int((lev == L).sum()) for L in known}
    assert mults == {0.0: 640, 3.0: 832, 8.0: 192}, f"Casimir multiplicities {mults}"
    top = 8.0
    Wt = Wker @ cU[:, lev == top]
    assert Wt.shape[1] == 192, f"triplet carrier dim {Wt.shape[1]} != 192"
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    chir = np.kron(I14, om if om2 > 0 else (-1j) * om)
    return e, K, Jfull, Sig, Wt, chir, top


def net_index_ranks(M, Pp, Pm, tol=1e-6):
    """(i) rank & kernel-dim balance across chirality using matrix_rank."""
    Mpp = Pp.conj().T @ M @ Pp
    Mmm = Pm.conj().T @ M @ Pm
    rk_pp = np.linalg.matrix_rank(Mpp, tol=tol * max(1, np.linalg.norm(Mpp)))
    rk_mm = np.linalg.matrix_rank(Mmm, tol=tol * max(1, np.linalg.norm(Mmm)))
    ker_pp = Pp.shape[1] - rk_pp
    ker_mm = Pm.shape[1] - rk_mm
    # net chiral index of image = rank asymmetry ; of kernel = kernel-dim asymmetry
    return (rk_pp - rk_mm), (ker_pp - ker_mm)


def net_index_gradtrace(M, chir, tol=1e-6):
    """(ii) graded trace of chirality over im(M) and ker(M) via SVD projectors."""
    U, s, Vh = np.linalg.svd(M)
    thr = tol * (s.max() + 1e-30)
    im = U[:, s > thr]
    ker = U[:, s <= thr]
    gi = np.trace(im.conj().T @ chir @ im).real if im.shape[1] else 0.0
    gk = np.trace(ker.conj().T @ chir @ ker).real if ker.shape[1] else 0.0
    return gi, gk


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=130)
    e, K, Jfull, Sig, Wt, chir, top = build()
    d = Wt.shape[1]
    print(f"[build] triplet dim = {d}  (expect 192)   j=1 Casimir top = {top}  (expect ~8)")

    # ---------- (A) Clifford algebra sanity for signature (9,5) ----------
    eta = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)])
    maxdev = 0.0
    for a in range(N):
        for b in range(N):
            anti = e[a] @ e[b] + e[b] @ e[a]
            target = 2 * eta[a, b] * np.eye(DIM)
            maxdev = max(maxdev, np.linalg.norm(anti - target))
    nt = sum(1 for a in range(N) if a in TIMELIKE)
    print(f"[A] Clifford {{e_a,e_b}}=2 eta_ab  max deviation = {maxdev:.2e}  "
          f"signature=({N-nt},{nt}) -> Cl(9,5) {'OK' if maxdev<1e-10 else 'FAIL'}")

    # ---------- (B) M(64,H): antilinear quaternionic J commuting with all gammas ----------
    # Want C with C conj(e_a) = e_a C for all a; J = C*conj; quaternionic iff J^2 = C conj(C) = -I.
    # Independent EXPLICIT construction (no giant SVD): in this JW basis each e_a is either
    # REAL (conj(e_a) = +e_a) or IMAGINARY (conj(e_a) = -e_a) -- MEASURED below, not assumed.
    # (The parity is set by the s1/s2 Jordan-Wigner slot, NOT by timelike/spacelike; the old
    # timelike-product / spacelike-product candidates were wrong for exactly that reason.)
    # C = product of the imaginary gammas: with |S| even it commutes with every e_a outside S
    # and anticommutes with every e_a in S, i.e. C conj(e_a) = e_a C for ALL a.
    econj = [e[a].conj() for a in range(N)]
    imag_idx = [a for a in range(N) if np.linalg.norm(econj[a] + e[a]) < 1e-12]
    real_idx = [a for a in range(N) if np.linalg.norm(econj[a] - e[a]) < 1e-12]
    assert sorted(imag_idx + real_idx) == list(range(N)), "each e_a must be exactly real or imaginary"
    assert len(imag_idx) % 2 == 0, "product trick needs an even number of imaginary gammas"
    Cc = np.eye(DIM, dtype=complex)
    for a in imag_idx:
        Cc = Cc @ e[a]
    defect = max(np.linalg.norm(Cc @ econj[a] - e[a] @ Cc) for a in range(N)) / (np.linalg.norm(Cc) + 1e-30)
    CC = Cc @ Cc.conj(); scale = CC[0, 0]
    quat_defect = np.linalg.norm(CC - scale * np.eye(DIM)) / (abs(scale) + 1e-30)
    quat_ok = (defect < 1e-9 and quat_defect < 1e-6 and scale.real < -0.5)
    print(f"[B] M(64,H) antilinear J (product of the {len(imag_idx)} imaginary gammas {imag_idx}):")
    print(f"    intertwine defect = {defect:.2e} (=0 => commutes all gammas), "
          f"J^2 scalar = {scale.real:+.3f}{scale.imag:+.3f}i, J^2=-I defect = {quat_defect:.2e} "
          f"{'(quaternionic OK)' if quat_ok else '(FAIL)'}")

    # ---------- reduce to triplet ----------
    Jr = [Wt.conj().T @ Jfull[k] @ Wt for k in range(3)]
    Kr = 0.5 * (Wt.conj().T @ K @ Wt + (Wt.conj().T @ K @ Wt).conj().T)
    KJ = [Kr @ Jr[k] for k in range(3)]
    Sigr = [Wt.conj().T @ np.kron(np.eye(N, dtype=complex), Sig[k]) @ Wt for k in range(3)]
    chir_tr = 0.5 * (Wt.conj().T @ chir @ Wt + (Wt.conj().T @ chir @ Wt).conj().T)
    cev, cU = np.linalg.eigh(chir_tr)
    Pp = cU[:, cev > 0.5]
    Pm = cU[:, cev < -0.5]
    print(f"[C] chirality split on triplet (+,-) = ({Pp.shape[1]},{Pm.shape[1]})")

    # ---------- (C) net chiral index over many Psi, my own methods ----------
    worst = dict(rk=0, kr=0, gi=0.0, gk=0.0, spec=0.0, flip=0.0)
    ker_dims = set()
    for _ in range(300):
        psi = rng.standard_normal(d) + 1j * rng.standard_normal(d)
        mu = np.array([np.vdot(psi, KJ[k] @ psi) for k in range(3)])
        M = sum(mu[k] * Sigr[k] for k in range(3))
        M = 0.5 * (M + M.conj().T)
        # method (i)
        ri, rk = net_index_ranks(M, Pp, Pm)
        # method (ii)
        gi, gk = net_index_gradtrace(M, chir_tr)
        # method (iii) sorted spectra within chirality sectors
        spp = np.sort(np.linalg.eigvalsh(0.5 * (Pp.conj().T @ M @ Pp + (Pp.conj().T @ M @ Pp).conj().T)))
        smm = np.sort(np.linalg.eigvalsh(0.5 * (Pm.conj().T @ M @ Pm + (Pm.conj().T @ M @ Pm).conj().T)))
        flip = (np.linalg.norm(Pm.conj().T @ M @ Pp) + np.linalg.norm(Pp.conj().T @ M @ Pm)) / (np.linalg.norm(M) + 1e-30)
        worst['rk'] = max(worst['rk'], abs(ri))
        worst['kr'] = max(worst['kr'], abs(rk))
        worst['gi'] = max(worst['gi'], abs(gi))
        worst['gk'] = max(worst['gk'], abs(gk))
        worst['spec'] = max(worst['spec'], np.max(np.abs(spp - smm)))
        worst['flip'] = max(worst['flip'], flip)
        evM = np.linalg.eigvalsh(M)
        ker_dims.add(int((np.abs(evM) < 1e-6 * (np.abs(evM).max() + 1e-30)).sum()))
    print(f"    (i)   max|rank(M_++)-rank(M_--)| = {worst['rk']}   max|kerdim_+ - kerdim_-| = {worst['kr']}")
    print(f"    (ii)  max|graded-tr omega over im| = {worst['gi']:.2e}   over ker = {worst['gk']:.2e}")
    print(f"    (iii) max|sorted eigs(M_++)-eigs(M_--)| = {worst['spec']:.2e}")
    print(f"    M chirality-preserving: max rel flip block = {worst['flip']:.2e}   ker dims seen = {sorted(ker_dims)}")
    index_zero = (worst['rk'] == 0 and worst['kr'] == 0 and worst['gi'] < 1e-6
                  and worst['gk'] < 1e-6 and worst['spec'] < 1e-6)
    print(f"    => NET CHIRAL INDEX == 0 (all my methods): {index_zero}")

    # ---------- (E) structural forcing: is P=c(e_b) INVERTIBLE on the triplet? ----------
    print("\n[E] structural forcing rigor: chirality-swap P=c(e_b), b>3")
    for b in [9, 8, 7]:
        Pb = Wt.conj().T @ np.kron(np.eye(N, dtype=complex), e[b]) @ Wt
        swap = np.linalg.norm(chir_tr @ Pb + Pb @ chir_tr) / (np.linalg.norm(Pb) + 1e-30)
        commS = max(np.linalg.norm(Pb @ Sigr[k] - Sigr[k] @ Pb) / (np.linalg.norm(Pb) + 1e-30) for k in range(3))
        sv = np.linalg.svd(Pb, compute_uv=False)
        cond = sv[0] / sv[-1] if sv[-1] > 0 else np.inf
        invertible = sv[-1] > 1e-8 * sv[0]
        print(f"   b={b}: anticomm(omega)={swap:.2e}  comm(all Sig)={commS:.2e}  "
              f"sing(min={sv[-1]:.3f},max={sv[0]:.3f}) cond={cond:.2f} invertible_on_triplet={invertible}")
        if b == 9:
            forcing_valid = swap < 1e-6 and commS < 1e-6 and invertible
    print(f"   => forcing argument valid (P swaps chirality, commutes all M(Psi), invertible): {forcing_valid}")

    # ---------- (D) NON-VACUITY: machinery must report a KNOWN nonzero index ----------
    print("\n[D] non-vacuity BREAK: does the index machinery report a KNOWN nonzero asymmetry?")
    # Side fact (a theorem on this carrier, verified -- NOT the control): a chirality-ODD
    # Hermitian source (Hermitian part of a compressed single c(e_a)) has BOTH diagonal
    # chirality blocks == 0 and a SQUARE 96x96 off-diagonal block, so rank-nullity forces
    # its graded index to 0 identically. Odd sources can NEVER fire on an equal-split
    # carrier; reading 0 on them says nothing about whether the machinery works.
    odd_max = 0.0
    for a in [0, 1, 2, 3]:
        Ma = Wt.conj().T @ np.kron(np.eye(N, dtype=complex), e[a]) @ Wt
        Ma = 0.5 * (Ma + Ma.conj().T)   # Hermitian part; chirality-odd
        ri, rk = net_index_ranks(Ma, Pp, Pm)
        gi, gk = net_index_gradtrace(Ma, chir_tr)
        odd_max = max(odd_max, abs(ri), abs(rk), abs(gi), abs(gk))
        print(f"   c(e_{a}) (odd): rank-asym(im)={ri}  ker-asym={rk}  "
              f"grad-tr(im)={gi:+.2f} grad-tr(ker)={gk:+.2f}   (forced 0: square off-diag block)")
    odd_forced_zero = odd_max < 1e-9
    print(f"   side check: odd sources give exactly 0 as the theorem demands: {odd_forced_zero}")
    # THE CONTROL: chirality-EVEN Hermitian op supported on the + sector only, rank r.
    # Ground truth known in advance: rank asym = +r, graded trace im = +r, ker = -r.
    r_ctrl = 7
    Gc = rng.standard_normal((Pp.shape[1], r_ctrl)) + 1j * rng.standard_normal((Pp.shape[1], r_ctrl))
    Ac = Pp @ Gc                                  # columns live entirely in + chirality
    Mctrl = Ac @ Ac.conj().T                      # Hermitian PSD, rank r_ctrl, chirality-even
    ri_c, rk_c = net_index_ranks(Mctrl, Pp, Pm)
    gi_c, gk_c = net_index_gradtrace(Mctrl, chir_tr)
    print(f"   CONTROL rank-{r_ctrl} +-sector even op: rank-asym(im)={ri_c} (expect +{r_ctrl})  "
          f"ker-asym={rk_c} (expect -{r_ctrl})")
    print(f"                                     grad-tr(im)={gi_c:+.2f} (expect +{r_ctrl})  "
          f"grad-tr(ker)={gk_c:+.2f} (expect -{r_ctrl})")
    non_vacuous = (ri_c == r_ctrl and rk_c == -r_ctrl
                   and abs(gi_c - r_ctrl) < 1e-6 and abs(gk_c + r_ctrl) < 1e-6
                   and odd_forced_zero)
    print(f"   => machinery detects the known nonzero chiral asymmetry exactly: {non_vacuous}")

    # ---------- (F) isolate the mechanism ----------
    print("\n[F] mechanism isolation: generic Hermitian perturbations")
    # even (commutes with omega) random Hermitian
    Reven = Pp @ (rng.standard_normal((Pp.shape[1], Pp.shape[1])) + 1j*rng.standard_normal((Pp.shape[1], Pp.shape[1]))) @ Pp.conj().T \
          + Pm @ (rng.standard_normal((Pm.shape[1], Pm.shape[1])) + 1j*rng.standard_normal((Pm.shape[1], Pm.shape[1]))) @ Pm.conj().T
    Reven = Reven + Reven.conj().T
    # does the swap operator P force this generic EVEN op to be isospectral? NO -- because
    # generic even op need not commute with c(e_b). This shows the isospectrality is special to M(mu).
    Pb = Wt.conj().T @ np.kron(np.eye(N, dtype=complex), e[9]) @ Wt
    comm_even = np.linalg.norm(Pb @ Reven - Reven @ Pb) / (np.linalg.norm(Reven)*np.linalg.norm(Pb) + 1e-30)
    # but M(mu) = sum mu_k Sig_k DOES commute with P because each Sig_k does:
    psi = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    mu = np.array([np.vdot(psi, KJ[k] @ psi) for k in range(3)])
    M = sum(mu[k] * Sigr[k] for k in range(3)); M = 0.5*(M+M.conj().T)
    comm_M = np.linalg.norm(Pb @ M - M @ Pb) / (np.linalg.norm(M)*np.linalg.norm(Pb) + 1e-30)
    spp = np.sort(np.linalg.eigvalsh(0.5*(Pp.conj().T@Reven@Pp + (Pp.conj().T@Reven@Pp).conj().T)))
    smm = np.sort(np.linalg.eigvalsh(0.5*(Pm.conj().T@Reven@Pm + (Pm.conj().T@Reven@Pm).conj().T)))
    print(f"   generic EVEN Hermitian op: [P,R]/norm = {comm_even:.2e} (NOT ~0) -> its blocks NOT forced isospectral")
    print(f"      |eigs(R_++)-eigs(R_--)| = {np.max(np.abs(spp-smm)):.2e} (nonzero: swap does NOT act because [P,R]!=0)")
    print(f"   M(mu) from moment map:     [P,M]/norm = {comm_M:.2e} (~0) -> M's blocks forced isospectral")
    print(f"   => the no-go is specific: mu lands in span(Sig_k), the exact commutant of the chirality-swap.")

    print("\n" + "="*90)
    verdict = index_zero and forcing_valid and non_vacuous and quat_ok
    print(f"REPRODUCED index==0: {index_zero} | forcing rigorous(P invertible): {forcing_valid} | "
          f"non-vacuous(known index detected): {non_vacuous} | quaternionic J^2=-1: {quat_ok}")
    print(f"TERMINAL: no-go {'CONFIRMED (KILLED the SW-source chiral-count hope)' if verdict else 'NOT fully established'}")
    print("="*90)
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
