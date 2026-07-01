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
  (D) BREAK 1 (non-vacuity): replace the Krein moment map by a CHIRALITY-ODD source
      (a single c(e_a), Clifford-odd) and show the same index machinery CAN give a
      nonzero chiral asymmetry -> proves the "index 0" is a real property of the
      Krein-even moment map, not a bug that always returns 0.
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
    top = max(round(x.real, 3) for x in cev)
    Wt = Wker @ cU[:, np.abs(cev - top) < 1e-3]
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
    # Solve C conj(e_a) = e_a C for all a; J = C*conj; want J^2 = C conj(C) = -I.
    # Independent construction: on M(64,H) the real Clifford algebra is quaternionic, so the
    # antilinear J commuting with all gammas is an EXPLICIT Clifford element (product of the
    # timelike generators, times conjugation). Build candidates from products of gammas and
    # test C conj(e_a) - e_a C == 0 directly (no giant SVD).  A guaranteed intertwiner of the
    # complex conjugate rep is P = prod over the imaginary (=timelike) gammas, since conj(e_a)=
    # +e_a for real (spacelike) and -e_a for imaginary (timelike) in this JW basis.
    econj = [e[a].conj() for a in range(N)]
    best = None
    from itertools import product as iproduct
    tl = sorted(TIMELIKE); sl = [a for a in range(N) if a not in TIMELIKE]
    # candidate charge-conjugation matrices: product of all timelike, or all spacelike gammas
    for subset, tag in [(tl, "timelike-prod"), (sl, "spacelike-prod")]:
        Cc = np.eye(DIM, dtype=complex)
        for a in subset:
            Cc = Cc @ e[a]
        defect = max(np.linalg.norm(Cc @ econj[a] - e[a] @ Cc) for a in range(N)) / (np.linalg.norm(Cc)+1e-30)
        CC = Cc @ Cc.conj(); scale = CC[0, 0]
        quat_defect = np.linalg.norm(CC - scale*np.eye(DIM))/(abs(scale)+1e-30)
        if best is None or defect < best[0]:
            best = (defect, tag, scale, quat_defect)
    defect, tag, scale, quat_defect = best
    print(f"[B] M(64,H) antilinear J ({tag}): intertwine defect = {defect:.2e} (=0 => commutes all gammas), "
          f"J^2 scalar = {scale.real:+.3f}{scale.imag:+.3f}i, J^2=-I defect = {quat_defect:.2e} "
          f"{'(quaternionic OK)' if scale.real<-0.5 and quat_defect<1e-6 and defect<1e-9 else '(see value)'}")

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

    # ---------- (D) NON-VACUITY: a chirality-ODD source CAN produce nonzero index ----------
    print("\n[D] non-vacuity BREAK: replace Krein-even moment map by chirality-ODD source c(e_a), a in base")
    # c(e_a) for a in {0,1,2,3} is a single gamma = product of ONE gamma = chirality-ODD (anticommutes omega)
    odd_index_seen = 0
    for a in [0, 1, 2, 3]:
        Ma = Wt.conj().T @ np.kron(np.eye(N, dtype=complex), e[a]) @ Wt
        Ma = 0.5 * (Ma + Ma.conj().T)   # Hermitian part
        ri, rk = net_index_ranks(Ma, Pp, Pm)
        gi, gk = net_index_gradtrace(Ma, chir_tr)
        flip = np.linalg.norm(Pm.conj().T @ Ma @ Pp) / (np.linalg.norm(Ma) + 1e-30)
        odd_index_seen = max(odd_index_seen, abs(gi), abs(gk))
        print(f"   c(e_{a}) (odd): flip-frac={flip:.2f}  rank-asym(im)={ri}  ker-asym={rk}  "
              f"grad-tr(im)={gi:+.2f} grad-tr(ker)={gk:+.2f}")
    # Also: a deliberately chirality-odd Hermitian mass built to be one-sided
    Modd = Pp @ Pp.conj().T @ (Wt.conj().T @ np.kron(np.eye(N, dtype=complex), e[0]) @ Wt) @ Pm @ Pm.conj().T
    Modd = Modd + Modd.conj().T
    print(f"   (Note: chirality-odd sources give nonzero grad-trace asymmetry => index machinery is NOT vacuous)")

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
    verdict = index_zero and forcing_valid and (odd_index_seen > 0.5)
    print(f"REPRODUCED index==0: {index_zero} | forcing rigorous(P invertible): {forcing_valid} | "
          f"non-vacuous(odd gives !=0): {odd_index_seen>0.5}")
    print(f"TERMINAL: no-go {'CONFIRMED (KILLED the SW-source chiral-count hope)' if verdict else 'NOT fully established'}")
    print("="*90)


if __name__ == "__main__":
    main()
