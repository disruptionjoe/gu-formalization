"""
MP-M4 (MASS TEXTURE / SIGN-BIT ROUTE of the mirror-mechanism swing). The V8+alignment result is:
the aligned condensate phi*Pi_mirror (Pi_mirror = (I - K|_W)/2 = (I + Q5)/2) gaps all 96 mirror
states while keeping all 96 generation states massless, [M,P]=0, as the global minimum of a native
potential on an open region of couplings (A1/A4), down to ONE sign bit (A2). This route EXTRACTS
what the KINEMATICS + that one sign bit FIX about the mirror SPECTRUM, and separates it cleanly
from what needs the unbuilt dynamics.

THE HONEST CONSTRAINT (restated): the ABSOLUTE mirror mass scale mu is NOT determined -- it is the
condensate VEV magnitude, set by the unbuilt source action. NO absolute-mass claim is made. What
this route asks: given the scale, what is the TEXTURE (the pattern of the 96 mirror masses), what
RATIOS are fixed, and does the sign bit leave any observable imprint on the spectrum?

HEADLINE RESULTS (all machine-checked below; (9,5) with (7,7) cross-check):
  (M4-1) EXACT DEGENERACY, NO TEXTURE (THEOREM). The mirror mass matrix M(phi) = phi*Pi_mirror
      has spectrum EXACTLY {0^96 (generations), phi^96 (mirrors)} -- Pi_mirror is a rank-96
      ORTHOGONAL PROJECTOR (eigenvalues in {0,1} identically), so all 96 mirrors sit at ONE mass
      mu = phi with zero spread (band width ~1e-14). The kinematics forces a FLAT mirror spectrum:
      no family splitting, no isospin splitting, no generation hierarchy. Mirror mass scales
      linearly in the condensate amplitude (mu is a free overall multiplier => dynamics-gated).
  (M4-2) THE DEGENERACY IS SYMMETRY-PROTECTED (THEOREM). Pi_mirror = (I - P)/2 commutes with the
      ENTIRE unbroken group on W: both families su(2)+ x su(2)-, and the maximal-compact internal
      so(5)_s x so(5)_t (residuals ~1e-14). It does NOT commute with the internal boosts (the
      non-compact directions Q5 already breaks). Since any compact physical gauge group sits in
      the maximal compact, the mirror mass is GAUGE-INVARIANT: it does not split within gauge
      multiplets and is a vectorlike (Dirac/Majorana-type) mass that needs no electroweak breaking.
      The 96 mirrors are ONE degenerate multiplet 96 = 3 (su(2)+) x 2 (su(2)-) x 16, measured on
      the mirror half W_- (weights {-2,0,2}x32, {-1,+1}x48, uniform so(5)_s Casimir).
  (M4-3) THE QUARTIC ACTIVELY SELECTS DEGENERACY (THEOREM, ties to A1b). Among all mirror-sector
      mass operators of fixed tr(M^2), the uniform (projector) one MINIMIZES tr(M^4) by
      Cauchy-Schwarz: tr(Pi^4) = tr(Pi^2)^2/96 exactly, and any split raises tr(M^4). So the
      l4>0 stable-cone quartic that selects the mirror-hiding vacuum (A1) DRIVES the spectrum to
      the flat/degenerate texture; a mirror texture would cost potential energy. Degeneracy is not
      just the projector ansatz -- it is the minimizer.
  (M4-4) THE SIGN BIT LEAVES NO SPECTRAL IMPRINT (THEOREM). The one undetermined coupling sign
      sign(lq + l4/192) = sign of tr(Q5 Phi^2) selects the ORIENTATION (which K-half gaps). The
      opposite orientation is phi*Pi_generation = phi*(I + P)/2, and chi conjugates one into the
      other (chi Pi_mirror chi = Pi_generation, residual ~1e-14). Its spectrum is the SAME multiset
      {0^96, phi^96} -- only the LABEL (which half is called "physical") swaps. So the orientation
      content of the sign bit is spectrally INVISIBLE (A3, re-confirmed at the spectrum level). The
      sign bit's ONLY physical content is BINARY: gapped-mirror-phase vs mirror-blind-phase; within
      the gapped phase it produces no texture, no ratio, no observable. It is not a spectral knob.
  (M4-5) NO KINEMATIC MASS RATIO IS FIXED beyond the trivial ones (BOUNDARY). Determined: all
      mirror/mirror ratios = 1 (degenerate); m_generation/mu = 0 exactly (aligned limit). The
      Weyl-point relation phi = mu/q (generation branch massless) is the aligned equal-weight
      condition itself, not an independent number. Dynamics-gated: the absolute mu, ANY
      mirror-gap / generation-mass ratio (the generation Yukawa texture is a different, unbuilt
      condensate), and whether the sign is the gapping sign.
  (M4-6) CONTROLS WITH POWER. A generic chi-anticommuting (pure E-) condensate SPLITS the mirror
      band (nonzero texture) but is |m|-blind; a generic mixed P-even condensate splits both bands.
      So the degeneracy checks discriminate: the flat texture is SPECIAL to the aligned projector
      direction the mechanism selects, not automatic for an arbitrary mirror-gapping operator.

DETERMINED (THEOREM):   flat 96-fold degeneracy, symmetry protection, gauge-invariance of the
                        mirror mass, sign-bit spectral invisibility, exact generation masslessness.
DYNAMICS-GATED (CONSISTENT_UNCOMPUTED):  the absolute scale mu, the generation Yukawa texture, any
                        mirror/generation ratio, the gapping sign, radiative/EWSB degeneracy lifts.

TARGET-IMPORT GUARD: no element of {3, 8, 24, chi(K3)=24, rank_H, ind_H} is assumed, inserted, or
divided by. All dimensions (128, 1664, 192, 96, 48, 32) are measured outputs. The mirror count 96
and its 3x2x16 factoring are MEASURED, never forced; no absolute mass is claimed. Anchors first;
controls with discriminating power. From-memory physics (SO(5,5) max compact = SO(5)xSO(5), "a
compact gauge group sits in the maximal compact") is flagged as a structural/group-theory input,
not a numeric import.

Run: python tests/big-swing/mp_m4_mass_texture_sign_bit.py    (exit 0)
"""
import numpy as np
from itertools import combinations

np.random.seed(20260707)
N, DIM = 14, 128
TOL = 1e-9
nrm = np.linalg.norm
comm = lambda A, B: A @ B - B @ A
acomm = lambda A, B: A @ B + B @ A

FAIL = []
def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        FAIL.append(name)


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


base = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)


def build(timelike):
    """Verified carrier recipe (verbatim from vg_v8_t5_map_attempt.py / ghost_parity_krein.py)."""
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]

    def sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    def lvec(i, j):
        M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M

    def gen(i, j):
        return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)

    Gam = np.hstack(e)
    rankG = np.linalg.matrix_rank(Gam)
    Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    SDp = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    ASDp = [(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1)]
    J3full = [gen(a, b) + gen(c, d) for (a, b, c, d) in SDp]
    J3mfull = [gen(a, b) + gen(c, d) for (a, b, c, d) in ASDp]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]

    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if nrm(bS.conj().T + bS) < TOL:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    Kful = np.kron(etaV, bS)

    Rc = lambda M: Wt.conj().T @ M @ Wt
    K = Rc(Kful); K = 0.5 * (K + K.conj().T)
    om = I128.copy()
    for a in range(14):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    Cful = np.kron(I14, om if om2 > 0 else (-1j) * om)
    C = Rc(Cful)
    kev, kU = np.linalg.eigh(K)
    P = (kU * np.sign(kev)) @ kU.conj().T; P = 0.5 * (P + P.conj().T)
    return dict(e=e, Wt=Wt, Rc=Rc, K=K, P=P, C=C, kev=kev, kU=kU,
                J3full=J3full, J3mfull=J3mfull, etaV=etaV, rankG=rankG,
                kerdim=Wk.shape[1], top=top, timelike=timelike)


def mono_big(e, idxs):
    Mm = I128.copy()
    for a in idxs:
        Mm = Mm @ e[a]
    return np.kron(I14, Mm)


print("=" * 112)
print("MP-M4: MIRROR MASS TEXTURE + SIGN-BIT IMPRINT -- what the kinematics fixes vs what dynamics gates")
print("=" * 112)

# ==================================================================================== [0] ANCHORS
print("\n[0] ANCHORS (9,5), timelike={4..8} (must reproduce before any claim)")
D = build({4, 5, 6, 7, 8})
e, Wt, Rc, K, P, C = D["e"], D["Wt"], D["Rc"], D["K"], D["P"], D["C"]
kev, kU = D["kev"], D["kU"]
tdim = Wt.shape[1]
check("rank(Gamma) = 128", D["rankG"] == 128, str(D["rankG"]))
check("dim ker(Gamma) = 1664", D["kerdim"] == 1664, str(D["kerdim"]))
check("triplet dim = 192", tdim == 192, str(tdim))
npl, nmi = int((kev > TOL).sum()), int((kev < -TOL).sum())
check("triplet Krein signature (+96, -96, 0)", (npl, nmi) == (96, 96), f"(+{npl}, -{nmi})")
check("P = sign(K) equals K|_W itself", nrm(P - K) < 1e-9, f"{nrm(P - K):.1e}")
Q5 = Rc(mono_big(e, [9, 10, 11, 12, 13]))
resQ = nrm(Q5 + P)
check("V8 identity: Q5 = e9..e13 compressed = -P_ghost (~1e-14)", resQ < 1e-9, f"||Q5+P|| = {resQ:.1e}")
check("chi involution on W (chi^2 = I)", nrm(C @ C - np.eye(tdim)) < 1e-8, f"{nrm(C @ C - np.eye(tdim)):.1e}")
check("{P, chi} = 0 (chi exchanges the parity halves)", nrm(acomm(P, C)) < 1e-8, f"{nrm(acomm(P, C)):.1e}")

Ep, Em = kU[:, kev > 0], kU[:, kev < 0]          # W_+ (generation half), W_- (mirror half)
Kinv = np.linalg.inv(K)
adjK = lambda A: Kinv @ A.conj().T @ K
Jp = [Rc(M) for M in D["J3full"]]                # su(2)+  (family / generation triplet)
Jm = [Rc(M) for M in D["J3mfull"]]               # su(2)-  (doublet)
timelike = D["timelike"]
g = {i: Rc(mono_big(e, [i])) for i in range(4, 14)}   # internal gammas on W

def spec_pm(M):
    """masses read on each Krein half: eigenvalues of the compression to W_+ and W_-."""
    Ap = Ep.conj().T @ M @ Ep
    Am = Em.conj().T @ M @ Em
    sp = np.sort(np.linalg.eigvals(Ap).real)
    sm = np.sort(np.linalg.eigvals(Am).real)
    return sp, sm

# =================================================== [1] THE MIRROR MASS MATRIX: FLAT, NO TEXTURE
print("\n[1] MIRROR MASS MATRIX M(phi) = phi * Pi_mirror,  Pi_mirror = (I - P)/2 = (I + Q5)/2")
PIm = 0.5 * (np.eye(tdim) - P)
# Pi_mirror is an orthogonal projector: eigenvalues exactly {0,1}
pev = np.sort(np.linalg.eigvalsh(0.5 * (PIm + PIm.conj().T)).real)
rank_proj = int(np.round(pev.sum()))
check("Pi_mirror is a rank-96 orthogonal projector (eigenvalues exactly {0^96, 1^96})",
      rank_proj == 96 and abs(pev[:96]).max() < 1e-9 and abs(pev[96:] - 1).max() < 1e-9,
      f"rank {rank_proj}, eig range [{pev.min():.2e}, {pev.max():.6f}]")
check("Pi_mirror^2 = Pi_mirror (idempotent)", nrm(PIm @ PIm - PIm) < 1e-9, f"{nrm(PIm @ PIm - PIm):.1e}")

print("  spectrum of M(phi) on each Krein half (mu := phi is a FREE overall scale):")
for phi in [1.0, 0.5, 2.0, 7.3]:
    sp, sm = spec_pm(phi * PIm)
    print(f"    phi = {phi:5.2f}:  generations |m| in [{np.abs(sp).min():.2e}, {np.abs(sp).max():.2e}] x96 "
          f"|  mirrors m in [{sm.min():.6f}, {sm.max():.6f}] x96   (band width {sm.max()-sm.min():.1e})")
sp, sm = spec_pm(1.0 * PIm)
check("THEOREM: at unit phi the 96 generations are EXACTLY massless", np.abs(sp).max() < 1e-9,
      f"max|m_gen| = {np.abs(sp).max():.1e}")
check("THEOREM: the 96 mirrors are EXACTLY DEGENERATE at m = phi (band width ~ 0: NO TEXTURE)",
      (sm.max() - sm.min()) < 1e-9 and abs(sm.mean() - 1.0) < 1e-9,
      f"band width = {sm.max()-sm.min():.1e}, level = {sm.mean():.10f}")
# linear scaling => absolute scale is a free multiplier (dynamics-gated)
sp2, sm2 = spec_pm(3.7 * PIm)
check("mirror mass scales LINEARLY in the condensate amplitude (mu = free multiplier => gated)",
      abs(sm2.mean() - 3.7) < 1e-9, f"phi=3.7 -> level {sm2.mean():.6f}")

# ============================================ [2] THE DEGENERACY IS SYMMETRY-PROTECTED (3 x 2 x 16)
print("\n[2] SYMMETRY PROTECTION of the flat texture: [Pi_mirror, unbroken group] = 0")
so5s = [g[i] @ g[j] for (i, j) in combinations(range(9, 14), 2)]   # internal spacelike so(5)_s
so5t = [g[i] @ g[j] for (i, j) in combinations(range(4, 9), 2)]    # internal timelike so(5)_t
unbroken = {"su(2)+ (family)": Jp, "su(2)- (doublet)": Jm,
            "so(5)_s internal": so5s, "so(5)_t internal": so5t}
for label, gens in unbroken.items():
    r = max(nrm(comm(PIm, X)) for X in gens)
    check(f"[Pi_mirror, {label}] = 0 ({len(gens)} generators)", r < 1e-8, f"max residual {r:.1e}")
# the broken directions: internal boosts (non-compact) anticommute with Q5 => move Pi_mirror
boost = g[4] @ g[9]
check("CONTRAST: internal boost e4e9 does NOT commute with Pi_mirror (broken, non-compact)",
      nrm(comm(PIm, boost)) > 0.5, f"[Pi_mirror, e4e9] = {nrm(comm(PIm, boost)):.2f}")
print("  => the mirror mass is invariant under the ENTIRE maximal-compact internal x family group.")
print("     Any physical compact gauge group sits inside the maximal compact (SO(5,5) => SO(5)xSO(5)),")
print("     so the mirror mass is GAUGE-INVARIANT: vectorlike (needs no EWSB), un-split within multiplets.")
print("     [group-theory input flagged: 'compact gauge group <= maximal compact' -- structural, not numeric]")

# measure the mirror half W_- as 3 x 2 x 16 (DERIVED, not imported)
def cartan_weights(gen_on_half, Half):
    A = Half.conj().T @ (1j * gen_on_half) @ Half
    A = 0.5 * (A + A.conj().T)
    v = np.linalg.eigvalsh(A)
    vals, cnts = np.unique(np.round(v, 6), return_counts=True)
    return vals, cnts
vjp, cjp = cartan_weights(Jp[2], Em)
vjm, cjm = cartan_weights(Jm[2], Em)
print(f"  mirror half W_- su(2)+ weights: " + ", ".join(f"{v:+.0f}x{c}" for v, c in zip(vjp, cjp)))
print(f"  mirror half W_- su(2)- weights: " + ", ".join(f"{v:+.0f}x{c}" for v, c in zip(vjm, cjm)))
check("W_- carries su(2)+ TRIPLET (weights {-2,0,+2} x32) x su(2)- DOUBLET (weights {-1,+1} x48)",
      list(vjp) == [-2.0, 0.0, 2.0] and list(cjp) == [32, 32, 32]
      and list(vjm) == [-1.0, 1.0] and list(cjm) == [48, 48])
Cas5s = sum(-0.25 * (X @ X) for X in so5s)
cw = np.linalg.eigvalsh(0.5 * (Em.conj().T @ Cas5s @ Em + (Em.conj().T @ Cas5s @ Em).conj().T))
check("W_- so(5)_s Casimir UNIFORM (single internal isotype: the 16 of Spin(10))",
      cw.max() - cw.min() < 1e-9, f"spread {cw.max()-cw.min():.1e}")
print("  => the 96 mirrors are ONE degenerate multiplet 96 = 3 x 2 x 16 (all measured). A flat texture:")
print("     no family splitting, no isospin splitting, no hierarchy -- the kinematics fixes this.")

# ================================================= [3] THE QUARTIC ACTIVELY SELECTS THE FLAT TEXTURE
print("\n[3] THE QUARTIC SELECTS DEGENERACY: among fixed-tr(M^2) mirror operators, uniform minimizes tr(M^4)")
print("    (Cauchy-Schwarz: tr(M^4) >= tr(M^2)^2/96, equality iff |eigenvalues| uniform -> ties to A1b)")
def t2t4(vals):
    Mmir = Em @ np.diag(vals.astype(complex)) @ Em.conj().T
    t2 = np.trace(Mmir @ Mmir).real
    t4 = np.trace(Mmir @ Mmir @ Mmir @ Mmir).real
    return t2, t4
uni = np.ones(96)
t2u, t4u = t2t4(uni)
check("projector (uniform) mirror op saturates Cauchy-Schwarz: tr(M^4) = tr(M^2)^2/96",
      abs(t4u - t2u**2 / 96) < 1e-9, f"tr4={t4u:.3f}, tr2^2/96={t2u**2/96:.3f}")
worst = np.inf
for _ in range(300):
    v = np.abs(np.random.randn(96)) + 0.3          # any split, positive levels
    v = v / np.sqrt(np.sum(v**2)) * np.sqrt(96)      # rescale to tr(M^2)=96 (same as uniform)
    t2s, t4s = t2t4(v)
    worst = min(worst, t4s - t4u)                    # should be >= 0 (uniform is the minimizer)
check("EVERY split mirror texture (fixed tr M^2) has tr(M^4) >= projector value (300 draws)",
      worst > -1e-9, f"min excess tr4 over uniform = {worst:.3e} (>= 0)")
# explicit two-level split to exhibit the cost
vsplit = np.concatenate([1.3 * np.ones(48), np.zeros(48)])
vsplit = vsplit / np.sqrt(np.sum(vsplit**2)) * np.sqrt(96)
t2sp, t4sp = t2t4(vsplit)
print(f"    example 48/48 two-level split at fixed tr(M^2)=96: tr(M^4)={t4sp:.1f} > uniform {t4u:.1f} "
      f"(+{100*(t4sp-t4u)/t4u:.0f}% potential cost from l4>0)")
print("  => the l4>0 stable-cone quartic that selects the mirror-hiding vacuum (A1) DRIVES the flat")
print("     spectrum; a mirror texture costs potential energy. Degeneracy is the MINIMIZER, not an ansatz.")

# ===================================================== [4] THE SIGN BIT LEAVES NO SPECTRAL IMPRINT
print("\n[4] THE SIGN BIT: sign(lq + l4/192) = sign of tr(Q5 Phi^2) picks the ORIENTATION (which half gaps)")
PIgen = 0.5 * (np.eye(tdim) + P)     # opposite orientation: gaps the K-positive half instead
# chi conjugates one orientation into the other (A3, at the operator level)
chi_conj = C @ PIm @ C
check("chi conjugates Pi_mirror -> Pi_generation (the two orientations are chi-related, ~1e-14)",
      nrm(chi_conj - PIgen) < 1e-8, f"||chi Pi_mir chi - Pi_gen|| = {nrm(chi_conj - PIgen):.1e}")
sp_p, sm_p = spec_pm(1.0 * PIm)      # +sign orientation
sp_m, sm_m = spec_pm(1.0 * PIgen)    # -sign orientation
# the OBSERVABLE spectrum is the full multiset of 192 masses on the whole triplet, regardless of label
full_plus = np.sort(np.concatenate([np.abs(sp_p), np.abs(sm_p)]))
full_minus = np.sort(np.concatenate([np.abs(sp_m), np.abs(sm_m)]))
check("the two sign choices give the IDENTICAL mass multiset {0^96, phi^96} (only the label swaps)",
      np.abs(full_plus - full_minus).max() < 1e-9,
      f"max multiset diff = {np.abs(full_plus - full_minus).max():.1e}")
print(f"    +sign: gap on W_- (mirrors), massless W_+ ; -sign: gap on W_+, massless W_- ; SAME spectrum.")
print("  => the ORIENTATION content of the sign bit is spectrally INVISIBLE (A3 at the spectrum level).")
print("     The sign bit's ONLY physical content is BINARY: gapped-mirror phase vs mirror-blind phase.")
print("     Within the gapped phase it produces NO texture, NO ratio, NO observable. Not a spectral knob.")

# ============================================================= [5] RATIOS: WHAT IS AND ISN'T FIXED
print("\n[5] RATIOS -- kinematically fixed vs dynamics-gated")
check("determined: mirror/mirror mass ratio = 1 exactly (flat, from degeneracy)",
      (sm_p.max() / sm_p.min() - 1.0) < 1e-9, f"max/min = {sm_p.max()/sm_p.min():.12f}")
check("determined: m_generation / mu = 0 exactly (aligned equal-weight limit)",
      np.abs(sp_p).max() < 1e-9, f"max|m_gen|/mu = {np.abs(sp_p).max():.1e}")
# the misaligned generic toy M = mu I + phi q Q5 : the Weyl point phi = mu/q is the alignment condition
print("  misaligned generic toy  M = mu*I + phi*q*Q5  (Q5 = -1 on gen, +1 on mir):")
mu, q = 1.0, 1.0
for phi in [0.0, 0.5, 1.0, 2.0]:
    sp_t, sm_t = spec_pm(mu * np.eye(tdim) + phi * q * Q5)
    print(f"    phi={phi:4.1f}: |m_gen|={np.abs(sp_t).max():.3f} (=|mu-q phi|), "
          f"m_mir={sm_t.mean():.3f} (=|mu+q phi|)")
sp_w, sm_w = spec_pm(mu * np.eye(tdim) + (mu / q) * q * Q5)
check("Weyl point phi = mu/q: generations massless, mirrors at 2mu -- this IS the alignment condition,",
      np.abs(sp_w).max() < 1e-7 and abs(sm_w.mean() - 2.0) < 1e-7,
      f"not an independent number (max|m_gen|={np.abs(sp_w).max():.1e}, m_mir={sm_w.mean():.3f})")
print("  DYNAMICS-GATED (never predicted): absolute mu; any mirror-gap / generation-mass ratio (the")
print("  generation Yukawa texture is a DIFFERENT, unbuilt condensate); whether the sign is the gapping sign.")

# =================================================================== [6] CONTROLS (DISCRIMINATING)
print("\n[6] CONTROLS -- the degeneracy checks have power (a wrong direction fails flatness)")
KA = Ep.conj().T @ K @ Ep
cblk = Ep.conj().T @ C @ Em
tex_ok = True
for i in range(3):
    A0 = np.random.randn(96, 96) + 1j * np.random.randn(96, 96)
    A0 = 0.5 * (A0 + np.linalg.inv(KA) @ A0.conj().T @ KA)      # K|+-self-adjoint block
    # pure chi-anticommuting (E-) element: (A, -c^H A c)
    Mminus = Ep @ A0 @ Ep.conj().T - Em @ (cblk.conj().T @ A0 @ cblk) @ Em.conj().T
    Mminus = Mminus / nrm(Mminus) * np.sqrt(tdim)
    sp_e, sm_e = spec_pm(Mminus)
    band = sm_e.max() - sm_e.min()
    print(f"    random PURE E- direction #{i+1}: mirror band width = {band:.3f} (SPLIT: a texture, not flat)")
    tex_ok = tex_ok and band > 1e-2
check("a GENERIC chi-anticommuting condensate SPLITS the mirror band (texture) -- flatness is special",
      tex_ok, "the aligned projector's zero-width band is not automatic")
mix_ok = True
for i in range(2):
    Xr = np.random.randn(tdim, tdim) + 1j * np.random.randn(tdim, tdim)
    Xr = 0.5 * (Xr + adjK(Xr)); Xr = 0.5 * (Xr + P @ Xr @ P)     # generic P-even
    Xr = Xr / nrm(Xr) * np.sqrt(tdim)
    sp_x, sm_x = spec_pm(Xr)
    mix_ok = mix_ok and (sm_x.max() - sm_x.min()) > 1e-2 and (sp_x.max() - sp_x.min()) > 1e-2
check("a GENERIC mixed P-even condensate splits BOTH bands (checks discriminate)", mix_ok)

# =============================================================== [7] (7,7) SIGNATURE CROSS-CHECK
print("\n[7] (7,7) SIGNATURE CROSS-CHECK (timelike = {4..10}; the flat texture is signature-independent)")
D7 = build({4, 5, 6, 7, 8, 9, 10})
Wt7, Rc7, K7, P7 = D7["Wt"], D7["Rc"], D7["K"], D7["P"]
kev7, kU7 = D7["kev"], D7["kU"]
Ep7, Em7 = kU7[:, kev7 > 0], kU7[:, kev7 < 0]
Kinv7 = np.linalg.inv(K7); adjK7 = lambda A: Kinv7 @ A.conj().T @ K7
Q3 = Rc7(mono_big(D7["e"], [11, 12, 13]))
Q3sa = 0.5 * (1j * Q3 + adjK7(1j * Q3))
check("(7,7): i*(e11e12e13) = -P (same spacelike-internal-volume theorem)", nrm(Q3sa + P7) < 1e-9,
      f"{nrm(Q3sa + P7):.1e}")
PIm7 = 0.5 * (np.eye(192) - P7)
sm7 = np.sort(np.linalg.eigvals(Em7.conj().T @ PIm7 @ Em7).real)
sp7 = np.sort(np.linalg.eigvals(Ep7.conj().T @ PIm7 @ Ep7).real)
check("(7,7): flat 96-fold mirror degeneracy at phi, generations exactly massless -- texture holds",
      (sm7.max() - sm7.min()) < 1e-7 and np.abs(sp7).max() < 1e-7,
      f"mirror band width = {sm7.max()-sm7.min():.1e}, max|m_gen| = {np.abs(sp7).max():.1e}")

# ==================================================================================== [8] VERDICT
print("\n" + "=" * 112)
print("[8] VERDICT (M4 mass texture / sign bit)")
print("=" * 112)
print("""  DETERMINED (THEOREM, kinematic + stable-cone quartic):
   - The mirror sector is EXACTLY DEGENERATE: one mass mu, 96-fold, zero texture (Pi_mirror is a
     projector; the l4>0 quartic drives uniform magnitude). No family/isospin splitting, no hierarchy.
   - The degeneracy is SYMMETRY-PROTECTED by the full maximal-compact internal x family group; the
     mirror mass is GAUGE-INVARIANT (vectorlike, no EWSB needed), one multiplet 96 = 3 x 2 x 16.
   - The generation half is EXACTLY massless under the mechanism (m_gen/mu = 0).
   - The one sign bit is spectrally INVISIBLE as orientation (A3), and BINARY as phase selection
     (gapped vs blind). It is not a texture knob: it leaves no observable imprint on the spectrum.
  DYNAMICS-GATED (CONSISTENT_UNCOMPUTED -- NOT predicted):
   - The absolute scale mu (condensate VEV magnitude, a free linear multiplier).
   - The generation Yukawa texture (SM masses: a different, unbuilt condensate) and hence ANY
     mirror-gap / generation-mass ratio.
   - Whether GU's unbuilt source action supplies the gapping sign.
   - Radiative / EWSB lifts of the flat degeneracy (their existence is expected once dynamics is built;
     their SIZE is gated).
  HONEST BOUNDARY: the mechanism fixes the SHAPE of the mirror spectrum (flat, gauge-invariant,
  one degenerate 3x2x16 multiplet) but not its POSITION (mu) -- exactly the determined/gated split
  the swing demands. No absolute mass is claimed anywhere.""")

if FAIL:
    print(f"\nFAILED CHECKS: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = all anchors reproduced, flat-texture + sign-bit theorems checked, controls have power.")
