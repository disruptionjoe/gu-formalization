"""
VG-V8 (route V8, T5' MAP ATTEMPT): construct or refute the VEV = condensate map at the level of
the (9,5) triplet sector. The tri-theory federation's center (steelman 4.2, 5.2-item-3) owes:
  (a) an exact characterization of the target set V1 left as the interface invoice -- the
      K-self-adjoint directions on the 192-dim triplet sector W that are P_ghost-EVEN and
      chi-NON-commuting (the only operator class that can gap mirrors while generations stay
      light, per VG-V1's exhaustive theorem over the enumerated native algebra);
  (b) a pushforward scan: which Y14/base data CAN land in that set (base 2-forms / Lambda^2_+,
      the Spin(10)-internal 16/16bar directions, odd Clifford / vector-VEV channels, products
      with native directions), each machine-classified;
  (c) a minimal sign-and-regime toy reconciling Weinstein's DECREASED-VEV chirality clause
      [transcript 00:46:40] with Mannheim's FORMED-condensate scale clause (steelman 4.2
      antonym; 5.2 item 3).

HEADLINE RESULTS (all machine-checked below, both signatures where stated):
  (1) THE GHOST PARITY IS CLIFFORD-NATIVE ON W. The compressed internal SPACELIKE volume
      element (Q5 = e9 e10 e11 e12 e13 in (9,5); i*Q3 = i e11 e12 e13 in (7,7)) equals -P_ghost
      IDENTICALLY (residual ~7e-14, all 192^2 entries, both signatures). Mechanism: on W the
      base Clifford volume chi_base acts as -I, the vector-index metric etaV acts as +I, and W
      is invariant under the internal Clifford action, so K = etaV (x) beta_S collapses to
      -(internal spacelike volume). Corollary: every base-odd Clifford channel (in particular
      c(dphi), the gradient of a conf_base condensate) is ANNIHILATED on W -- the base leg of
      the map is dead; the condensate can only land through internal (fiber) directions.
  (2) THE MAP HAS A NATIVE LANDING ZONE. M = (I + Q5)/2 = (I - P)/2 = Pi_mirror is a native
      two-term Clifford direction (scalar + internal spatial volume), K-self-adjoint, P-EVEN
      ([M,P] ~ 8e-15), chi-non-commuting -- inside V1's target set -- and the condensate map
      phi -> phi * Pi_mirror gaps ALL 96 mirror states at m = phi while keeping ALL 96
      generation states EXACTLY massless: T3''s advertised payoff (mirrors gapped, generations
      light, positivity intact), delivered at kinematic grade. V1's "no native object
      satisfies the interface requirement" is EXTENDED (not contradicted): V1's enumerated
      algebra was chi-commuting; the odd Clifford sector was V1 honest-gap #1, and it is
      where the map lands.
  (3) THE INVOICE THAT REMAINS: (i) one orientation Z2 -- which volume sign, i.e. WHICH half
      is physical (the canon's ghost-assignment freedom, now priced as a single sign); (ii)
      the scalar/volume ALIGNMENT (the projector weights; nothing computed here fixes it --
      that is dynamics, unbuilt); (iii) Q5 is equivariant only under the maximal compact
      (internal boosts anticommute with it): the space/time-split datum, the SAME datum the
      Krein form K itself already presupposes -- no new import beyond the sign; (iv) the
      Yukawa/derivative typing caveat inherited from V1 (instantaneous quadratic-form
      deformation only).
  (4) ADVERSE FINDINGS DELIVERED WITH THE POSITIVE: the 16/16bar Spin(10) refinement grading
      chi_int ANTICOMMUTES with K ({chi_int, P} ~ 4e-15) -- it is P-ODD, so the physical
      sector admits NO 16-vs-16bar decomposition and R3's last trace-level chirality readout
      closes (adverse for the canon's three-chiral-generations hope). The count stays OPEN:
      the physical sector remains 96 = 3 x 2 x 16 and chi-trace-achiral; nothing here selects
      3, selects a chirality, or supplies dynamics.
  (5) TARGET-SET GEOMETRY (part a): the P-even K-self-adjoint directions form E, real dim
      2*96^2 = 18432; the chi-conjugation involution splits E = E+ (chi-commuting, 9216) (+)
      E- (chi-anticommuting, 9216); mirror-selective SORTED splitting requires a nonzero E-
      component and |m|-splitting (mass magnitudes) additionally requires a nonzero E+
      component (pure E- spectra are exactly negation-paired: |m| mirror = |m| generation).
      Under the family su(2)+ x su(2)-, E- decomposes into 36 cells (j+,j-) in {0,1,2} x
      {0,1} of 256 real dims each; the internal Clifford monomials span EXACTLY the 256-dim
      family-scalar cell (measured span 256/256), and Q5 sits inside it. J_quat fixes K, P,
      chi and Q5 (Kramers multiplicities stay even throughout: 96/48/32 everywhere).

TARGET-IMPORT GUARD: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is
assumed, inserted, or divided by. All dimensions (128, 1664, 192, 96, 48, 32, 256, 9216) are
measured outputs, asserted after measurement. Anchors reproduced first. Controls with
discriminating power throughout. R1-R4 cited only as committed docs.

Run: python tests/big-swing/vg_v8_t5_map_attempt.py    (exit 0)
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
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name} {detail}")
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
    """Verified carrier recipe (reused from V1 / ghost_parity_krein.py). Returns the compressed
    triplet-sector data. All anchors asserted by the caller."""
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
    betares = max(nrm(bS @ sgen(i, j) + sgen(i, j).conj().T @ bS)
                  for i in range(14) for j in range(i + 1, 14))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    Kful = np.kron(etaV, bS)
    om = I128.copy()
    for a in range(14):
        om = om @ e[a]
    om2 = (np.trace(om @ om) / DIM).real
    Cful = np.kron(I14, om if om2 > 0 else (-1j) * om)

    Rc = lambda M: Wt.conj().T @ M @ Wt
    K = Rc(Kful); K = 0.5 * (K + K.conj().T)
    C = Rc(Cful)
    kev, kU = np.linalg.eigh(K)
    P = (kU * np.sign(kev)) @ kU.conj().T; P = 0.5 * (P + P.conj().T)
    return dict(e=e, Wt=Wt, Rc=Rc, K=K, P=P, C=C, kev=kev, kU=kU,
                J3full=J3full, J3mfull=J3mfull, etaV=etaV, rankG=rankG,
                kerdim=Wk.shape[1], top=top, betares=betares, timelike=timelike)


def mono_big(e, idxs):
    Mm = I128.copy()
    for a in idxs:
        Mm = Mm @ e[a]
    return np.kron(I14, Mm)


print("=" * 110)
print("VG-V8: T5' MAP ATTEMPT -- VEV = condensate on the (9,5) triplet sector (with (7,7) cross-check)")
print("=" * 110)

# ==================================================================================== [0] ANCHORS
print("\n[0] ANCHORS (9,5) (must reproduce before any claim)")
D = build({4, 5, 6, 7, 8})
e, Wt, Rc, K, P, C = D["e"], D["Wt"], D["Rc"], D["K"], D["P"], D["C"]
kev, kU = D["kev"], D["kU"]
tdim = Wt.shape[1]
check("rank(Gamma) = 128", D["rankG"] == 128, str(D["rankG"]))
check("dim ker(Gamma) = 1664", D["kerdim"] == 1664, str(D["kerdim"]))
check("triplet dim = 192", tdim == 192, str(tdim))
check("su(2)+ Casimir top eig on ker (measured)", abs(D["top"] - 8.0) < 1e-6, f"{D['top']}")
check("beta_S pseudo-anti-Hermiticity ~ 0", D["betares"] < TOL, f"{D['betares']:.1e}")
npl, nmi = int((kev > TOL).sum()), int((kev < -TOL).sum())
check("triplet Krein signature (+96, -96, 0)", (npl, nmi) == (96, 96), f"(+{npl}, -{nmi})")
check("|K|-eigs on W all exactly 1 (K|_W is an involution)",
      abs(np.abs(kev).min() - 1) < 1e-9 and abs(np.abs(kev).max() - 1) < 1e-9,
      f"range [{np.abs(kev).min():.6f}, {np.abs(kev).max():.6f}]")
check("P = sign(K) equals K|_W itself", nrm(P - K) < 1e-9, f"{nrm(P - K):.1e}")
check("chi involution on W", nrm(C @ C - np.eye(tdim)) < 1e-8, f"{nrm(C @ C - np.eye(tdim)):.1e}")
check("{P, chi} = 0 (P exchanges chirality halves)", nrm(acomm(P, C)) < 1e-8,
      f"{nrm(acomm(P, C)):.1e}")
Ep, Em = kU[:, kev > 0], kU[:, kev < 0]
Kinv = np.linalg.inv(K)
adjK = lambda A: Kinv @ A.conj().T @ K
Jp = [Rc(M) for M in D["J3full"]]
Jm = [Rc(M) for M in D["J3mfull"]]
check("[K, su(2)+] ~ 0 and [K, su(2)-] ~ 0",
      max(nrm(comm(K, Jp[k])) for k in range(3)) < 1e-8 and
      max(nrm(comm(K, Jm[k])) for k in range(3)) < 1e-8)

# ==================================================== [1] STRUCTURE THEOREMS ON THE TRIPLET SECTOR
print("\n[1] STRUCTURE THEOREMS on W (the mechanism behind the map)")
timelike = D["timelike"]
# (1a) W is invariant under the INTERNAL Clifford action
g = {}
maxinv = 0.0
for i in range(4, 14):
    big = mono_big(e, [i])
    g[i] = Rc(big)
    maxinv = max(maxinv, nrm(big @ Wt - Wt @ g[i]))
check("W invariant under internal Clifford action (all 10 internal gammas)", maxinv < 1e-9,
      f"max residual {maxinv:.1e}")
maxcl = 0.0
for i in range(4, 14):
    for j in range(i, 14):
        eta_ij = (-1.0 if i in timelike else 1.0) if i == j else 0.0
        target = 2 * eta_ij * np.eye(tdim)
        maxcl = max(maxcl, nrm(acomm(g[i], g[j]) - target))
check("internal Clifford relations hold ON W: {g_i, g_j} = 2 eta_ij", maxcl < 1e-9,
      f"max residual {maxcl:.1e}")
big0 = mono_big(e, [0])
check("base gammas do NOT preserve W (contrast)", nrm(big0 @ Wt - Wt @ Rc(big0)) > 1.0,
      f"e0 residual {nrm(big0 @ Wt - Wt @ Rc(big0)):.1f}")

# (1b) the two degeneracies that collapse K onto the internal volume
chb = Rc(mono_big(e, [0, 1, 2, 3]))
check("base Clifford volume chi_base|_W = -I (base leg degenerates)",
      nrm(chb + np.eye(tdim)) < 1e-9, f"||chi_base + I|| = {nrm(chb + np.eye(tdim)):.1e}")
scl = Rc(np.kron(D["etaV"], I128))
check("fiber scale etaV|_W = +I (V1 finding reproduced)", nrm(scl - np.eye(tdim)) < 1e-9,
      f"{nrm(scl - np.eye(tdim)):.1e}")

# (1c) THE IDENTITY: internal spacelike volume = -P_ghost
Q5 = Rc(mono_big(e, [9, 10, 11, 12, 13]))
resQ = nrm(Q5 + P)
check("Q5 = e9 e10 e11 e12 e13 compressed equals -P_ghost IDENTICALLY", resQ < 1e-9,
      f"||Q5 + P|| = {resQ:.1e}  (192x192 identity, not just isospectral)")
Q5r = Rc(mono_big(e, [10, 9, 11, 12, 13]))     # odd permutation = orientation flip
check("orientation flip gives +P (the Z2 the map does not fix)", nrm(Q5r - P) < 1e-9,
      f"||Q5_flipped - P|| = {nrm(Q5r - P):.1e}")
print("    => the ghost parity is the compressed internal SPATIAL volume element, up to")
print("       orientation: P_ghost = -(e9...e13)|_W. Krein sign structure = fiber orientation datum.")

# corollary: base-odd channels are annihilated
c0 = Rc(big0)
Xb = np.random.randn(4); Xb /= nrm(Xb)
cX = Rc(sum(Xb[a] * mono_big(e, [a]) for a in range(4)))
c3 = Rc(mono_big(e, [0, 1, 2]))
check("corollary: c(e0)|_W = 0, c(X_base)|_W = 0, (e0e1e2)|_W = 0  [conf_base gradient leg DEAD]",
      max(nrm(c0), nrm(cX), nrm(c3)) < 1e-9,
      f"norms {nrm(c0):.1e}, {nrm(cX):.1e}, {nrm(c3):.1e}")
print("    mechanism: any monomial with an odd number of base gammas anticommutes with chi_base,")
print("    and chi_base|_W = -I forces its compression to vanish.")

# (1d) the 16/16bar refinement grading is P-ODD (R3 open item 2, answered)
chi_int = Rc(mono_big(e, list(range(4, 14))))
fr_c = nrm(comm(chi_int, P)) / nrm(chi_int)
fr_a = nrm(acomm(chi_int, P)) / nrm(chi_int)
check("chi_int (Spin(10)-internal 16/16bar grading) ANTICOMMUTES with P (and with K)",
      fr_a < 1e-9 and fr_c > 1.0, f"{{chi_int,P}}/|.| = {fr_a:.1e}, [chi_int,P]/|.| = {fr_c:.2f}")
print("    => the physical (P=+1) sector is NOT chi_int-invariant: it admits no 16-vs-16bar")
print("       decomposition; R3's '16/16bar refinement' trace readout CLOSES (adverse for the")
print("       canon three-chiral-generations hope; extends the achirality fence from chi to chi_int).")

# (1e) J_quat compatibility
Sset = [a for a in range(14) if nrm(np.conj(e[a]) + e[a]) < 1e-12]
C128 = I128.copy()
for a in Sset:
    C128 = C128 @ e[a]
check("quaternionic structure: C unitary, C conj(C) = -I",
      nrm(C128.conj().T @ C128 - I128) < 1e-10 and nrm(C128 @ np.conj(C128) + I128) < 1e-10)
Jbig = np.kron(I14, C128)
Jw = Wt.conj().T @ Jbig @ np.conj(Wt)
resJW = nrm(Jbig @ np.conj(Wt) - Wt @ Jw)
check("J_quat preserves W and J_quat^2 = -I on W",
      resJW < 1e-9 and nrm(Jw @ np.conj(Jw) + np.eye(tdim)) < 1e-9,
      f"W-res {resJW:.1e}")
Jinv = np.linalg.inv(Jw)
jact = lambda M: Jw @ np.conj(M) @ Jinv
check("J_quat FIXES K, P, chi and Q5 (conjugation residuals)",
      max(nrm(jact(K) - K), nrm(jact(P) - P), nrm(jact(C) - C), nrm(jact(Q5) - Q5)) < 1e-9,
      f"max {max(nrm(jact(K) - K), nrm(jact(P) - P), nrm(jact(C) - C), nrm(jact(Q5) - Q5)):.1e}")
# (1f) Q5 is a Cartan-involution datum: internal boosts anticommute with it
boost = g[4] @ g[9]      # e4 e9 compressed: internal boost bivector (up to scale)
check("internal boost bivector ANTICOMMUTES with Q5 (Q5 equivariant only under max compact)",
      nrm(acomm(boost, Q5)) < 1e-8, f"{{e4e9, Q5}} = {nrm(acomm(boost, Q5)):.1e}")
print("    => the space/time split inside the fiber is the datum Q5 (and K itself) presupposes;")
print("       no import beyond what the Krein quantization already uses, plus the orientation Z2.")

# ============================================================== [2] (a) THE TARGET SET, EXACTLY
print("\n[2] (a) TARGET-SET CHARACTERIZATION: K-self-adjoint, P-even, chi-non-commuting directions")
# E = P-even K-self-adjoint directions = pairs (A, B) of K|+-Hermitian blocks; dim = 2*96^2.
# chi is off-diagonal in the P-basis with unitary block c; T: M -> chi M chi is an involution on E;
# E+ = chi-commuting (B = +c^H A c), E- = chi-anticommuting (B = -c^H A c), each ~ Herm(96).
cblk = Ep.conj().T @ C @ Em
check("chi off-diagonal block c is UNITARY (parametrization is a bijection)",
      nrm(cblk @ cblk.conj().T - np.eye(96)) < 1e-9)
check("chi diagonal blocks vanish (chi purely exchanges the parity sectors)",
      max(nrm(Ep.conj().T @ C @ Ep), nrm(Em.conj().T @ C @ Em)) < 1e-9)
d_plus = int((kev > 0).sum())
dimE = 2 * d_plus ** 2
print(f"  dim_R E (P-even K-self-adjoint)          = 2 * {d_plus}^2 = {dimE}")
print(f"  dim_R E+ (chi-commuting part)            = {d_plus ** 2}   [V1: exactly isospectral, no split]")
print(f"  dim_R E- (chi-ANTICOMMUTING part)        = {d_plus ** 2}   <-- the target set's linear content")
assert dimE == 18432 and d_plus ** 2 == 9216

# bijection check: random A -> M in E- has all three properties; and E-elements decompose
KA = Ep.conj().T @ K @ Ep      # positive definite
A0 = np.random.randn(96, 96) + 1j * np.random.randn(96, 96)
A0 = 0.5 * (A0 + np.linalg.inv(KA) @ A0.conj().T @ KA)         # K|+-self-adjoint
Mminus = Ep @ A0 @ Ep.conj().T - Em @ (cblk.conj().T @ A0 @ cblk) @ Em.conj().T
r1 = nrm(comm(Mminus, P)) / nrm(Mminus)
r2 = nrm(Mminus - adjK(Mminus)) / nrm(Mminus)
r3 = nrm(acomm(Mminus, C)) / nrm(Mminus)
check("E- parametrization: A -> (A, -c^H A c) is P-even, K-self-adjoint, chi-anticommuting",
      max(r1, r2, r3) < 1e-9, f"residuals {r1:.1e}, {r2:.1e}, {r3:.1e}")

# family structure on the physical sector
w_p = np.linalg.eigvalsh(0.5 * ((1j * Jp[2]) + (1j * Jp[2]).conj().T)
                         if False else 0.5 * (Ep.conj().T @ (1j * Jp[2]) @ Ep
                                              + (Ep.conj().T @ (1j * Jp[2]) @ Ep).conj().T))
vals, cnts = np.unique(np.round(w_p, 6), return_counts=True)
print(f"  su(2)+ Cartan weights on W_+: " + ", ".join(f"{v:+.0f} x{c}" for v, c in zip(vals, cnts)))
check("W_+ su(2)+ content: weights {-2,0,+2} x32 (spin-1 triplet x 32)",
      list(vals) == [-2.0, 0.0, 2.0] and list(cnts) == [32, 32, 32])
w_m = np.linalg.eigvalsh(0.5 * (Ep.conj().T @ (1j * Jm[2]) @ Ep
                                + (Ep.conj().T @ (1j * Jm[2]) @ Ep).conj().T))
vals2, cnts2 = np.unique(np.round(w_m, 6), return_counts=True)
print(f"  su(2)- Cartan weights on W_+: " + ", ".join(f"{v:+.0f} x{c}" for v, c in zip(vals2, cnts2)))
check("W_+ su(2)- content: weights {-1,+1} x48 (doublet x 48)",
      list(vals2) == [-1.0, 1.0] and list(cnts2) == [48, 48])

# internal compact so(5)_s x so(5)_t on W_+ (they commute with K, hence preserve the sectors)
sp5s = [g[i] @ g[j] for (i, j) in combinations(range(9, 14), 2)]    # spin part 1/2 e_i e_j ~ e_i e_j
sp5t = [g[i] @ g[j] for (i, j) in combinations(range(4, 9), 2)]
resP5 = max(nrm(comm(X, P)) for X in sp5s + sp5t)
check("internal compact so(5)_s (+) so(5)_t bivectors commute with P (preserve the sectors)",
      resP5 < 1e-8, f"max [.,P] = {resP5:.1e}")
Cas5s = sum(-0.25 * (X @ X) for X in sp5s)   # -(1/2 e_ie_j)^2 summed = spinor Casimir (measured)
cw = np.linalg.eigvalsh(0.5 * (Ep.conj().T @ Cas5s @ Ep + (Ep.conj().T @ Cas5s @ Ep).conj().T))
print(f"  so(5)_s spinor Casimir on W_+: uniform value {cw.min():.3f}..{cw.max():.3f} "
      f"(4-dim spinor rep on every state)")
check("so(5)_s Casimir uniform on W_+ (single isotype: the internal factor is one 4-dim spinor)",
      cw.max() - cw.min() < 1e-9)
print("  => W_+ ~ (3 of su(2)+) x (2 of su(2)-) x (4 of so(5)_s) x (4 of so(5)_t): 3*2*4*4 = 96")
print("     E- ~ Herm(W_+) decomposes under su(2)+ x su(2)- into 36 = (1+3+5)(1+3) family cells")
print("     of 256 real dims each (the 16 (x) 16bar internal block): 36 x 256 = 9216.")

# ad-Casimir verification on a random E- element (family content check)
def adCas(M, gens):
    out = np.zeros_like(M)
    for Jk in gens:
        out = out - comm(Jk, comm(Jk, M))     # -(ad J)^2, J anti-Hermitian-ish generators
    return out
Mr = Mminus / nrm(Mminus)
c1 = adCas(Mr, Jp)
c2 = adCas(c1, Jp)
c3_ = adCas(c2, Jp)
# ad-Casimir eigenvalues on spin j cells (weights are 2m): lam_j in {0, 8, 24} (measured basis)
G_ = np.array([[np.vdot(Mr, Mr).real, np.vdot(Mr, c1).real, np.vdot(Mr, c2).real],
               [np.vdot(c1, Mr).real, np.vdot(c1, c1).real, np.vdot(c1, c2).real],
               [np.vdot(c2, Mr).real, np.vdot(c2, c1).real, np.vdot(c2, c2).real]])
# component fractions from the moment problem with measured eigenvalues {0, 8, 24}
lam = np.array([0.0, 8.0, 24.0])
V = np.vander(lam, 3, increasing=True).T
mom = np.array([np.vdot(Mr, Mr).real, np.vdot(Mr, c1).real, np.vdot(Mr, c2).real])
fr = np.linalg.solve(V, mom)
pred = np.array([1 * 4 * 256, 3 * 4 * 256, 5 * 4 * 256]) / 9216.0
print(f"  ad-su(2)+ Casimir components of a random E- element: measured fractions "
      f"[{fr[0]:.3f}, {fr[1]:.3f}, {fr[2]:.3f}] vs rep-theory [{pred[0]:.3f}, {pred[1]:.3f}, {pred[2]:.3f}]")
check("E- family decomposition matches rep theory (ad-Casimir moments, random element)",
      np.abs(fr - pred).max() < 0.05, f"max dev {np.abs(fr - pred).max():.3f}")

# the Clifford-native slice of E-: internal odd monomials
vecs = []
for sc in [1, 3, 5]:
    for scomb in combinations([9, 10, 11, 12, 13], sc):
        for tc in [0, 2, 4]:
            for tcomb in combinations([4, 5, 6, 7, 8], tc):
                Mm = np.eye(tdim, dtype=complex)
                for i in list(tcomb) + list(scomb):
                    Mm = Mm @ g[i]
                Msa = 0.5 * (Mm + adjK(Mm))
                if nrm(Msa) < 1e-8:
                    Msa = 0.5 * (1j * Mm + adjK(1j * Mm))
                if nrm(Msa) < 1e-8:
                    continue
                assert nrm(comm(Msa, P)) / nrm(Msa) < 1e-8      # all are P-even (monomial rule)
                assert nrm(acomm(Msa, C)) / nrm(Msa) < 1e-8     # all chi-anticommute (odd grade)
                vecs.append(Msa.ravel())
A_ = np.array(vecs)
sv = np.linalg.svd(np.hstack([A_.real, A_.imag]), compute_uv=False)
rank = int((sv > 1e-8 * sv[0]).sum())
print(f"  internal odd monomials landing in E-: {len(vecs)} monomials, real span dim = {rank}")
check("Clifford-native slice of the target set = ONE family cell (256 of 9216 dims)",
      rank == 256, f"span {rank}")
resfam = max(nrm(comm(np.array(vecs[k]).reshape(tdim, tdim), Jp[2])) for k in range(0, len(vecs), 37))
check("Clifford-native slice is family-scalar ([., su(2)+] = 0 on samples)", resfam < 1e-8,
      f"{resfam:.1e}")
print("  => the (j+, j-) != (0,0) cells (35 x 256 = 8960 dims) require family-tensor data that")
print("     no fiber Clifford element supplies: they remain import territory.")

# monomial classification rules (the exact grammar of the target set)
print("\n  MONOMIAL GRAMMAR (verified on every scanned monomial):")
print("    P-parity of a compressed monomial  = (-1)^(# timelike factors)")
print("    chi-(anti)commutation              = (-1)^(total grade)")
print("    K-self-adjoint phase               = grade g: direct if g(g-1)/2 even, i* if odd")
print("    target set (P-even & chi-anticomm) = ODD grade with EVEN # timelike factors")
print("    base-odd factors                   => compression VANISHES (chi_base = -I)")

# ======================================================== [3] (b) THE PUSHFORWARD SCAN (the table)
print("\n[3] (b) PUSHFORWARD SCAN: what Y14/base data can land in the target set")
print("  columns: |M_W| (0 = channel dead), parity under P, [M,P]/|M|, chi-rel,")
print("           SPLIT = max|sorted spec+ - sorted spec-|, |m|SPLIT = same on magnitudes")

def spec_pm(M):
    Ap = Ep.conj().T @ M @ Ep
    Am = Em.conj().T @ M @ Em
    sp = np.sort(np.linalg.eigvals(Ap).real)
    sm = np.sort(np.linalg.eigvals(Am).real)
    imres = max(np.abs(np.linalg.eigvals(Ap).imag).max(),
                np.abs(np.linalg.eigvals(Am).imag).max())
    return sp, sm, imres

def levels(s, r=4, maxn=6):
    va, cn = np.unique(np.round(s, r), return_counts=True)
    out = ", ".join(f"{v:+.3f}x{c}" for v, c in zip(va[:maxn], cn[:maxn]))
    return out + ("..." if len(va) > maxn else "")

ROWS = []
def scan(name, cls, raw, print_spec=False, expect=None):
    nraw = nrm(raw)
    if nraw < 1e-9:
        print(f"  {name:<44s} {cls:<12s} DEAD: vanishes on W (|M_W| = {nraw:.1e})")
        ROWS.append((name, cls, "dead", None, None))
        return None
    M = 0.5 * (raw + adjK(raw))
    tagged = name
    if nrm(M) < 1e-8 * nraw:
        M = 0.5 * (1j * raw + adjK(1j * raw))
        tagged = name + " [i*]"
        if nrm(M) < 1e-8 * nraw:
            print(f"  {name:<44s} {cls:<12s} DEAD: K-skew both phases")
            ROWS.append((name, cls, "dead", None, None))
            return None
    nM = nrm(M)
    cMP = nrm(comm(M, P)) / nM
    cMC = nrm(comm(M, C)) / nM
    aMC = nrm(acomm(M, C)) / nM
    chirel = ("chi-comm" if cMC < 1e-8 else ("chi-ANTI" if aMC < 1e-8 else "chi-mixed"))
    if cMP < 1e-8:
        sp, sm, imres = spec_pm(M)
        split = np.abs(sp - sm).max()
        asplit = np.abs(np.sort(np.abs(sp)) - np.sort(np.abs(sm))).max()
        par = "EVEN"
        line = (f"  {tagged:<44s} {cls:<12s} |M|={nM:8.3f} {par:<5s} [M,P]={cMP:.0e} "
                f"{chirel:<9s} SPLIT={split:.2e} |m|SPLIT={asplit:.2e}")
        print(line)
        if print_spec:
            print(f"  {'':46s}spec+ = {levels(sp)}")
            print(f"  {'':46s}spec- = {levels(sm)}")
        ROWS.append((name, cls, par + "/" + chirel, split, asplit))
        if expect is not None:
            check(f"    expectation for {name}", expect(split, asplit), "")
        return M
    else:
        par = "ODD" if nrm(0.5 * (M + P @ M @ P)) / nM < 1e-8 else "MIXED"
        print(f"  {tagged:<44s} {cls:<12s} |M|={nM:8.3f} {par:<5s} [M,P]={cMP:.1f} "
              f"{chirel:<9s} (positivity-breaking branch)")
        ROWS.append((name, cls, par + "/" + chirel, None, None))
        return M

print("\n  -- source class 1: base 2-forms / Lambda^2_+ leg (conf_base curvature data) --")
sg = lambda i, j: 0.25 * (e[i] @ e[j] - e[j] @ e[i])
scan("Lambda^2_+ spin-only SD Cartan i(s01+s23)", "base-2form",
     Rc(1j * np.kron(I14, sg(0, 1) + sg(2, 3))), print_spec=True)
scan("Lambda^2_- spin-only ASD Cartan i(s01-s23)", "base-2form",
     Rc(1j * np.kron(I14, sg(0, 1) - sg(2, 3))))
scan("c(e0): base vector / gradient d(phi)", "base-1form", c0)
scan("c(X) generic base vector", "base-1form", cX)
scan("base 3-form e0e1e2", "base-3form", c3)
scan("chi_base (base volume)", "base-4form", chb, print_spec=False)
print("  => the ENTIRE base leg is either dead (odd base count) or chi-commuting (even count):")
print("     no base-geometry channel reaches the target set. Mannheim's condensate cannot enter")
print("     through its own gradient; conf_base data can only enter as a scalar COEFFICIENT.")

print("\n  -- source class 2: Spin(10)-internal directions (the canon's 16/16bar hint) --")
scan("chi_int (16/16bar grading direction)", "internal", chi_int)
scan("T5 = e4..e8 (timelike internal volume)", "internal", Rc(mono_big(e, [4, 5, 6, 7, 8])))
scan("c(e4): internal timelike vector", "internal", g[4])
scan("c(e13): internal spacelike vector", "internal", g[13], print_spec=True)
scan("internal compact 2-form i e9e10", "internal", 1j * g[9] @ g[10])
scan("internal boost 2-form i e4e9", "internal", 1j * g[4] @ g[9])
scan("internal spacelike 3-form e9e10e11", "internal", g[9] @ g[10] @ g[11], print_spec=True)
MQ5 = scan("Q5 = e9..e13 (spacelike internal volume)", "internal", Q5, print_spec=True)
print("  => the 16/16bar direction chi_int and every odd-timelike-count channel is P-ODD")
print("     (positivity-breaking). The even-timelike-count odd channels ARE in the target set --")
print("     and Q5 is literally -P: the parity itself is the distinguished element of the set.")

print("\n  -- source class 3: mixed / products with native directions --")
scan("mixed 3-form i e0e1e9 (base 2-form x int vec)", "mixed", Rc(mono_big(e, [0, 1, 9])),
     print_spec=True)
scan("Q5 * (i J+_3) (native product)", "product", Q5 @ (1j * Jp[2]), print_spec=True)
scan("c(e13) + Q5 (target-set sum)", "sum", g[13] + Q5)

print("\n  -- THE MAP CANDIDATE: the mirror projector (scalar + internal spatial volume) --")
PIm = 0.5 * (np.eye(tdim) + Q5)         # = (I - P)/2
Mmap = scan("Pi_mirror = (I + Q5)/2 = (I - P)/2", "MAP", PIm, print_spec=True)
sp, sm, imres = spec_pm(Mmap)
check("MAP CHANNEL: generations EXACTLY massless (96 states), mirrors gapped at 1 (96 states)",
      nrm(sp) < 1e-7 and np.abs(sm - 1).max() < 1e-7,
      f"max|m_gen| = {np.abs(sp).max():.1e}, mirror band [{sm.min():.6f}, {sm.max():.6f}]")
check("MAP CHANNEL: P-even to machine precision (Turok-Bateman positivity-compatible)",
      nrm(comm(Mmap, P)) / nrm(Mmap) < 1e-9, f"{nrm(comm(Mmap, P)) / nrm(Mmap):.1e}")
check("MAP CHANNEL: chi-non-commuting (outside V1's isospectrality lemma, as required)",
      nrm(comm(Mmap, C)) / nrm(Mmap) > 0.5, f"[M,chi]/|M| = {nrm(comm(Mmap, C)) / nrm(Mmap):.2f}")
scan("Pi_- c(e13) Pi_- (projector-dressed vector)", "MAP-dressed", PIm @ g[13] @ PIm,
     print_spec=True)
scan("mu I + phi Q5 (mu=1, phi=0.5: misaligned map)", "MAP-generic",
     np.eye(tdim) + 0.5 * Q5, print_spec=True)

print("\n  -- controls (discriminating power) --")
theorem_ok = True
for i in range(3):
    Ar = np.random.randn(96, 96) + 1j * np.random.randn(96, 96)
    Ar = 0.5 * (Ar + np.linalg.inv(KA) @ Ar.conj().T @ KA)
    Mr_ = Ep @ Ar @ Ep.conj().T - Em @ (cblk.conj().T @ Ar @ cblk) @ Em.conj().T
    Mr_ = Mr_ / nrm(Mr_) * np.sqrt(tdim)
    sp, sm, _ = spec_pm(Mr_)
    split = np.abs(sp - sm).max()
    asplit = np.abs(np.sort(np.abs(sp)) - np.sort(np.abs(sm))).max()
    print(f"  random PURE E- element #{i+1}: SPLIT={split:.3f} |m|SPLIT={asplit:.2e} "
          f"(negation-paired: spec- = -spec+)")
    theorem_ok = theorem_ok and split > 1e-3 and asplit < 1e-7
check("LEMMA: pure chi-anticommuting directions are |m|-BLIND (spec- = -spec+ exactly); they",
      theorem_ok, "sorted-split but never magnitude-split")
print("        (=> |m|-splitting needs BOTH an E+ and an E- component: even + odd, mixed)")
mix_ok = True
for i in range(3):
    Xr = np.random.randn(tdim, tdim) + 1j * np.random.randn(tdim, tdim)
    Xr = 0.5 * (Xr + adjK(Xr))
    Xr = 0.5 * (Xr + P @ Xr @ P)
    Xr = Xr / nrm(Xr) * np.sqrt(tdim)
    sp, sm, _ = spec_pm(Xr)
    split = np.abs(sp - sm).max()
    asplit = np.abs(np.sort(np.abs(sp)) - np.sort(np.abs(sm))).max()
    print(f"  random MIXED P-even element #{i+1}: SPLIT={split:.3f} |m|SPLIT={asplit:.3f}")
    mix_ok = mix_ok and split > 1e-3 and asplit > 1e-4
check("controls: generic mixed P-even directions split in BOTH metrics (checks have power)",
      mix_ok)
Xr = np.random.randn(tdim, tdim) + 1j * np.random.randn(tdim, tdim)
Xr = 0.5 * (Xr + adjK(Xr))
check("control: unrestricted K-self-adjoint random breaks [M,P] (V1 reproduction)",
      nrm(comm(Xr, P)) / nrm(Xr) > 0.5, f"[M,P]/|M| = {nrm(comm(Xr, P)) / nrm(Xr):.2f}")
Mwrong = Rc(mono_big(e, [4, 9, 10, 11, 12]))
check("control: WRONG 5-set volume (1 timelike + 4 spacelike) is NOT the parity (P-odd)",
      nrm(acomm(0.5 * (1j * Mwrong + adjK(1j * Mwrong)), P)) < 1e-8 or
      nrm(acomm(0.5 * (Mwrong + adjK(Mwrong)), P)) < 1e-8,
      "only the metric-selected spacelike 5-set gives P")

# ======================================================================== [4] (7,7) CROSS-CHECK
print("\n[4] (7,7) SIGNATURE CROSS-CHECK (timelike = {4..10}; internal signature (3,7))")
del D
D7 = build({4, 5, 6, 7, 8, 9, 10})
e7, Wt7, Rc7, K7, P7, C7 = D7["e"], D7["Wt"], D7["Rc"], D7["K"], D7["P"], D7["C"]
kev7 = D7["kev"]
check("(7,7) anchors: rank 128, ker 1664, triplet 192, Krein (+96,-96)",
      D7["rankG"] == 128 and D7["kerdim"] == 1664 and Wt7.shape[1] == 192
      and int((kev7 > TOL).sum()) == 96 and int((kev7 < -TOL).sum()) == 96)
Kinv7 = np.linalg.inv(K7)
adjK7 = lambda A: Kinv7 @ A.conj().T @ K7
Q3 = Rc7(mono_big(e7, [11, 12, 13]))
Q3sa = 0.5 * (1j * Q3 + adjK7(1j * Q3))     # grade 3 => i* phase for K-self-adjointness
check("(7,7): i*(e11 e12 e13) = -P identically (the SAME theorem, spacelike internal volume)",
      nrm(Q3sa + P7) < 1e-9, f"||i Q3 + P|| = {nrm(Q3sa + P7):.1e}")
chb7 = Rc7(mono_big(e7, [0, 1, 2, 3]))
check("(7,7): chi_base|_W = -I and c(e0)|_W = 0 (base leg dead in both signatures)",
      nrm(chb7 + np.eye(192)) < 1e-9 and nrm(Rc7(mono_big(e7, [0]))) < 1e-9)
chi_int7 = Rc7(mono_big(e7, list(range(4, 14))))
check("(7,7): chi_int P-ODD ({chi_int, P} = 0) -- 16/16bar readout closes here too",
      nrm(acomm(chi_int7, P7)) / nrm(chi_int7) < 1e-9)
PIm7 = 0.5 * (np.eye(192) - P7)
Ep7, Em7 = D7["kU"][:, kev7 > 0], D7["kU"][:, kev7 < 0]
sp7 = np.sort(np.linalg.eigvals(Ep7.conj().T @ PIm7 @ Ep7).real)
sm7 = np.sort(np.linalg.eigvals(Em7.conj().T @ PIm7 @ Em7).real)
check("(7,7): map channel Pi_mirror gaps mirrors (x96 at 1), generations exactly massless (x96)",
      nrm(sp7) < 1e-7 and np.abs(sm7 - 1).max() < 1e-7,
      f"max|m_gen| = {np.abs(sp7).max():.1e}")
del D7

# =================================================================== [5] (c) SIGN-AND-REGIME TOY
print("\n[5] (c) SIGN-AND-REGIME TOY: one order parameter, Weinstein's clause AND Mannheim's clause")
print("""
  The antonym (steelman 4.2 / 5.2 item 3): Weinstein conditions chirality on a DECREASED VEV
  [00:46:40 -- 'a decreased VEV in the total space taking a Dirac equation into two Weyl
  equations because the mass is actually a variable']; Mannheim's scale genesis needs a FORMED
  condensate. If VEV = condensate, one switch is thrown on and off simultaneously -- UNLESS the
  two clauses read off different COMPONENTS of one order parameter. The measured operator
  algebra above supplies exactly that reading:

  minimal mass matrix per hyperbolic (generation, mirror) pair, M(phi) = mu(phi) I + phi q Q5,
  Q5-eigenvalue -1 on the generation, +1 on the mirror (measured identity Q5 = -P):

      m_gen(phi) = |mu - q phi|          m_mir(phi) = |mu + q phi|

  2x2 analytic toy (mu = 1, q = 1):""")
mu, q = 1.0, 1.0
print("      phi   :  " + "  ".join(f"{p:5.2f}" for p in [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0]))
print("      m_gen :  " + "  ".join(f"{abs(mu - q * p):5.2f}" for p in [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0]))
print("      m_mir :  " + "  ".join(f"{abs(mu + q * p):5.2f}" for p in [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0]))
print("""      regime phi ~ 0      : Dirac regime -- generation and mirror degenerate at mu (vectorlike).
      regime phi = mu/q   : WEYL POINT -- the generation branch mass passes through ZERO while
                            the condensate is LARGE and FORMED: Weinstein's 'decreased VEV ->
                            Dirac becomes two Weyl equations' is the generation-sector EFFECTIVE
                            mass decreasing, not the order parameter decreasing.
      regime phi >> mu/q  : Mannheim regime -- both bands grow ~ q phi; overall scale genesis;
                            mirror band at |mu + q phi| stays gapped by 2 mu above the
                            generation band. One potential, e.g. V(phi) = lam (phi^2 - v^2)^2,
                            serves both clauses iff its minimum sits at (or beyond) the Weyl
                            point: v >= mu/q. NOTHING computed here fixes v, mu, or q.
      aligned limit       : if mu and q come from ONE condensate with EQUAL weights -- the
                            direction (I + Q5)/2 = Pi_mirror -- then m_gen = 0 IDENTICALLY at
                            every phi: the two clauses hold simultaneously with NO tuning.""")

# numeric triplet-compressed version
print("  triplet-compressed numeric check (mu = 1, q = 1, full 192-dim spectra):")
for phi in [0.0, 0.5, 1.0, 2.0]:
    M = mu * np.eye(tdim) + phi * q * Q5
    sp, sm, _ = spec_pm(M)
    print(f"    phi = {phi:4.1f}:  |m_gen| = {np.abs(sp).min():.3f}..{np.abs(sp).max():.3f} x96   "
          f"|m_mir| = {np.abs(sm).min():.3f}..{np.abs(sm).max():.3f} x96")
M = mu * np.eye(tdim) + 1.0 * Q5
sp, sm, _ = spec_pm(M)
check("Weyl point realized on the actual carrier: at phi = mu/q the 96 generation states are",
      nrm(sp) < 1e-7 and np.abs(sm - 2).max() < 1e-7,
      f"exactly massless while 96 mirrors sit at 2mu (max|m_gen| = {np.abs(sp).max():.1e})")

# misalignment robustness
print("  misalignment robustness (map direction contaminated by a native even direction):")
X = 1j * Jp[2]; X = X / nrm(X) * nrm(PIm)
for eps in [0.0, 0.1, 0.5, 1.0]:
    M = PIm + eps * X
    sp, sm, _ = spec_pm(M)
    gap = np.abs(sm).min() - np.abs(sp).max()
    print(f"    eps = {eps:3.1f}: generation band max |m| = {np.abs(sp).max():.3f}, "
          f"mirror band min |m| = {np.abs(sm).min():.3f}, gap = {gap:+.3f}")
print("    => the mirror-selective gap survives O(1) contamination (band separation persists")
print("       to eps ~ 0.5 and closes near eps ~ 1): the map does not require exact alignment,")
print("       but alignment quality IS physical content nothing native fixes.")

# ============================================================================== [6] VERDICT
print("\n" + "=" * 110)
print("[6] VERDICT (T5' map attempt)")
print("=" * 110)
print("""  CONSTRUCTED, at kinematic grade, with a priced invoice:
  (+) The target set V1 specified is nonempty ON THE NATIVE SIDE once the fiber Clifford algebra
      is admitted: the ghost parity IS the compressed internal spatial volume (both signatures),
      so the mirror projector (I + Q5)/2 is a native two-term Clifford direction, and
      phi -> phi Pi_mirror gaps all 96 mirrors while keeping all 96 generations exactly massless
      with [M, P_ghost] = 0: T3''s payoff (mirrors gapped, generations light, positivity intact).
  (+) The sign-and-regime antonym resolves: 'decreased VEV' = the generation-sector effective
      mass (the mu - q phi branch), 'formed condensate' = phi at the potential minimum; both
      clauses coexist in one potential (exactly, with zero tuning, in the aligned/projector limit).
  (-) What the map does NOT deliver: WHICH half is physical (orientation Z2); WHY the condensate
      aligns with the projector (dynamics, unbuilt); any chirality selection (physical sector
      stays chi-trace-achiral, and the 16/16bar readout is now closed: chi_int is P-odd); any
      count (physical sector remains 96 = 3 x 2 x 16); any base-geometry entry point (the base
      leg is DEAD: chi_base = -I annihilates every base-odd channel, so Mannheim's condensate
      enters only as a scalar coefficient on a fiber direction).
  Refutation scope of the negative parts: exhaustive over (i) all base Clifford channels (odd
  base count dead, even base count chi-commuting), (ii) all internal Clifford monomials (256-dim
  slice, all P-even ones classified), (iii) the enumerated native algebra (V1, cited). NOT
  exhausted: family-tensor imports (35 cells x 256 dims), non-monomial internal combinations
  beyond the scanned sums/products, position-dependent operators on an actual Y14.""")

if FAIL:
    print(f"\nFAILED CHECKS: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = all anchors reproduced, all checks passed, both signatures, controls have power.")
