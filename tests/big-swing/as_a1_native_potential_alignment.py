"""
AS-A1 (route A1, ALIGNMENT ATTACK): the native invariant potential scan on the P-even condensate
channel space of the (9,5) triplet sector.

V8 (tests/big-swing/vg_v8_t5_map_attempt.py) constructed the mirror-hiding direction
Pi_mirror = (I + Q5)/2 = (I - P_ghost)/2 at kinematic grade and named its central unproven
hypothesis: ALIGNMENT -- nothing shows any dynamics flows the condensate INTO that direction.
This route builds GU-native invariant potentials up to quartic order on the channel space and
asks where the minima sit.

DESIGN. Channel space V_ch = 34 native P-even K-self-adjoint directions (Clifford scalar, Q5,
family su(2)+/su(2)- triplets, Q5-dressed family, internal spacelike vectors / 3-forms / 4-forms).
Invariants = trace polynomials tr(w Phi^n) with native weights w. Weight-collapse measurement:
every scanned native weight either collapses to a scalar on W (all four group Casimirs) or is
P-odd (chi, chi_int, T5, wrong-volume) so its weighted traces VANISH identically on P-even
channels -- the only parity-sensitive native weight is Q5 = -P = -K|_W itself (V8's identity),
i.e. the weighted invariants are the KREIN SUPERTRACES q_n = Str(Phi^n) = tr(sign(K) Phi^n).
Basics: t_n = tr(Phi^n), q_n = Str(Phi^n), n = 1..4. Quartic monomials in the basics: 20
(11 flip-even + 9 flip-odd under the orientation flip, which is implemented on the channel
space by CHI conjugation -- machine-checked). All 20 Gram-independent (printed).

HEADLINE (machine-checked below; mechanism language only, never "GU forces"):
 (1) REDUCED-FAMILY PHASE THEOREM (analytic over the FULL 18432-dim P-even space E, verified
     numerically on the channel): for V = -t2 + l0*t2^2 + lq*q2^2 + l4*t4 (all native, l4 > 0),
     with a = l0 + lq + l4/96 and b = l0 - lq, the stable cone is a > 0 and the global minima are
       * lq < -l4/192 (b > a):  EXACTLY the mirror-hiding corner -- one parity sector's 96
         states uniformly gapped, the other 96 EXACTLY massless (V8's Pi_mirror payoff, as a
         potential MINIMUM), on an OPEN coupling region;
       * lq > -l4/192 (b < a):  the mirror-blind uniform-|m| vacuum (both sectors gapped alike).
     The boundary lq = -l4/192 uses only measured multiplicities (96, 192). Verified including a
     boundary-straddling pair at |shift| = 0.01/192.
 (2) Sign-texture moduli and their lift: the reduced-family corner minimum set contains
     sign-textured one-sector gappings (A = 0, B^2 = m^2 I) exactly degenerate with Pi_mirror;
     the flip-even native quartic t3*t1 lifts them to the exact projector pair {Pi_+, Pi_-}
     (spontaneous orientation); a flip-odd native coupling (q2*t2) selects ONE projector.
     Orientation = spontaneous choice or one native coupling sign -- no import beyond K.
 (3) Random stable draws over the full 11-dim flip-even family: both phases realized; aligned
     minima survive 5% perturbations of every coupling (openness in the full family).
 (4) CONTROLS: scrambled weight R (non-native balanced involution) destroys the parity-aligned
     vacuum; random quartic polynomials of matched scale give ZERO aligned minima; P-odd native
     weights give identically-zero invariants.

WHAT THIS DOES NOT DO: nothing computes the coupling signs from GU (no source action exists);
alignment is an open-region PHASE, not a cone-wide theorem; enumerated (not exhausted) weights
and channel; quartic truncation; frozen fiber; single signature (9,5). The alignment hypothesis
is reduced from a direction-import to ONE coupling-sign bit, not proved.

TARGET-IMPORT GUARD: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed,
inserted, or divided by. All counts (96, 192, 34, ranks) are measured outputs; the Casimir
scalars printed in [2] (8.0, 3.0, 2.5, 2.5) are eigenvalue measurements used in no formula.
Anchors reproduced first.

Run: python tests/big-swing/as_a1_native_potential_alignment.py   (exit 0)
"""
import numpy as np
from itertools import combinations, combinations_with_replacement
from scipy.optimize import minimize as spmin
from scipy.linalg import expm

np.random.seed(20260708)
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
    """Verified carrier recipe, reused verbatim from V8/V1/ghost_parity_krein.py."""
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]
    def sgen(i, j): return 0.25 * (e[i] @ e[j] - e[j] @ e[i])
    def lvec(i, j):
        M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M
    def gen(i, j): return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)
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
    return dict(e=e, Rc=Rc, K=K, P=P, C=C, kev=kev, kU=kU,
                J3full=J3full, J3mfull=J3mfull, rankG=rankG,
                kerdim=Wk.shape[1], top=top, betares=betares, timelike=timelike)

def mono_big(e, idxs):
    Mm = I128.copy()
    for a in idxs:
        Mm = Mm @ e[a]
    return np.kron(I14, Mm)

print("=" * 108)
print("AS-A1: NATIVE INVARIANT POTENTIAL SCAN -- does anything GU-native ALIGN the condensate with Pi_mirror?")
print("=" * 108)

# ============================================================================== [0] ANCHORS
print("\n[0] ANCHORS (9,5), timelike = {4..8} (must reproduce before any claim)")
D = build({4, 5, 6, 7, 8})
e, Rc, K, P, C = D["e"], D["Rc"], D["K"], D["P"], D["C"]
kev, kU = D["kev"], D["kU"]
tdim = 192
check("rank(Gamma) = 128", D["rankG"] == 128, str(D["rankG"]))
check("dim ker(Gamma) = 1664", D["kerdim"] == 1664, str(D["kerdim"]))
check("triplet dim = 192", kU.shape[0] == 192, str(kU.shape[0]))
npl, nmi = int((kev > TOL).sum()), int((kev < -TOL).sum())
check("triplet Krein signature (+96, -96, 0)", (npl, nmi) == (96, 96), f"(+{npl}, -{nmi}, 0:{192-npl-nmi})")
check("beta_S pseudo-anti-Hermiticity ~ 0", D["betares"] < TOL, f"{D['betares']:.1e}")
check("|K|-eigs on W all exactly 1", abs(np.abs(kev).min()-1) < 1e-9 and abs(np.abs(kev).max()-1) < 1e-9,
      f"range [{np.abs(kev).min():.6f}, {np.abs(kev).max():.6f}]")
check("P = sign(K) = K|_W", nrm(P - K) < 1e-9, f"{nrm(P-K):.1e}")
Q5 = Rc(mono_big(e, [9, 10, 11, 12, 13]))
check("V8 identity: Q5 = e9..e13 compressed = -P_ghost", nrm(Q5 + P) < 1e-9, f"||Q5+P|| = {nrm(Q5+P):.1e}")
check("{P, chi} = 0", nrm(acomm(P, C)) < 1e-8, f"{nrm(acomm(P,C)):.1e}")
Kinv = np.linalg.inv(K)
adjK = lambda A: Kinv @ A.conj().T @ K
Jp = [Rc(M) for M in D["J3full"]]
Jm = [Rc(M) for M in D["J3mfull"]]
g = {i: Rc(mono_big(e, [i])) for i in range(4, 14)}
Ep, Em = kU[:, kev > 0], kU[:, kev < 0]

# ============================================================== [1] THE CHANNEL BASIS (34 native directions)
print("\n[1] CHANNEL BASIS: native P-even K-self-adjoint directions on W")
def ksym(raw):
    M = 0.5 * (raw + adjK(raw))
    if nrm(M) < 1e-8 * max(nrm(raw), 1e-30):
        M = 0.5 * (1j * raw + adjK(1j * raw))
    return M

basis, names, tags = [], [], []
def add(name, raw, tag):
    M = ksym(raw)
    if nrm(M) < 1e-9:
        print(f"    dropped (K-skew both phases): {name}"); return
    rP = nrm(comm(M, P)) / nrm(M)
    if rP > 1e-8:
        print(f"    dropped (not P-even, [M,P]/|M| = {rP:.1e}): {name}"); return
    basis.append(M); names.append(name); tags.append(tag)

add("I", np.eye(tdim, dtype=complex), "scalar")
add("Q5", Q5, "volume")
for k in range(3):
    add(f"iJ+_{k+1}", 1j * Jp[k], "family+")
for k in range(3):
    add(f"iJ-_{k+1}", 1j * Jm[k], "family-")
for k in range(3):
    add(f"Q5*iJ+_{k+1}", Q5 @ (1j * Jp[k]), "q5fam+")
for k in range(3):
    add(f"Q5*iJ-_{k+1}", Q5 @ (1j * Jm[k]), "q5fam-")
for i in range(9, 14):
    add(f"vec_e{i}", g[i], "vector")
for (i, j, k) in combinations(range(9, 14), 3):
    add(f"3form_e{i}{j}{k}", g[i] @ g[j] @ g[k], "3form")
for (i, j, k, l) in combinations(range(9, 14), 4):
    add(f"4form_e{i}{j}{k}{l}", g[i] @ g[j] @ g[k] @ g[l], "4form")
d = len(basis)
print(f"  channel dimension d = {d} (every candidate admitted: all P-even, K-self-adjoint)")
check("channel dimension = 34", d == 34, str(d))

Ablk = np.array([Ep.conj().T @ M @ Ep for M in basis])
Bblk = np.array([Em.conj().T @ M @ Em for M in basis])
offres = max(nrm(Ep.conj().T @ M @ Em) for M in basis)
hres = max(max(nrm(A - A.conj().T) for A in Ablk), max(nrm(B - B.conj().T) for B in Bblk))
check("block decomposition: off-diagonal ~ 0 (P-even), blocks Hermitian (K-self-adjoint)",
      offres < 1e-8 and hres < 1e-8, f"off {offres:.1e}, herm {hres:.1e}")
M2full = np.real(np.einsum('iab,jba->ij', Ablk, Ablk) + np.einsum('iab,jba->ij', Bblk, Bblk))
ev2 = np.linalg.eigvalsh(M2full)
check("Gram of the 34 channel directions: full rank, positive definite",
      ev2.min() > 1e-6, f"min eig {ev2.min():.3e}, rank {int((ev2 > 1e-9*ev2.max()).sum())}/{d}")

def coords_of(Amat, Bmat):
    rhs = np.real(np.einsum('iab,ba->i', Ablk, Amat) + np.einsum('iab,ba->i', Bblk, Bmat))
    x = np.linalg.solve(M2full, rhs)
    res = nrm(np.einsum('i,iab->ab', x, Ablk) - Amat) + nrm(np.einsum('i,iab->ab', x, Bblk) - Bmat)
    return x, res
I96 = np.eye(96, dtype=complex)
xPip, rPip = coords_of(I96, 0 * I96)      # Pi_+ = (I+P)/2 : P=+1 sector projector
xPim, rPim = coords_of(0 * I96, I96)      # Pi_- = (I-P)/2 = (I+Q5)/2 = Pi_mirror (V8's map direction)
check("Pi_mirror = (I+Q5)/2 and Pi_+ = (I+P)/2 lie in the channel space",
      rPip < 1e-8 and rPim < 1e-8, f"fit residuals {rPip:.1e}, {rPim:.1e}")

# ================================================= [2] WEIGHT COLLAPSE
print("\n[2] WEIGHT COLLAPSE on W: which native weights can an invariant trace carry?")
CasP = sum(-(1j*J) @ (1j*J) for J in Jp)
CasM = sum(-(1j*J) @ (1j*J) for J in Jm)
sp5s = [g[i] @ g[j] for (i, j) in combinations(range(9, 14), 2)]
sp5t = [g[i] @ g[j] for (i, j) in combinations(range(4, 9), 2)]
Cas5s = sum(-0.25 * (X @ X) for X in sp5s)
Cas5t = sum(-0.25 * (X @ X) for X in sp5t)
for nm, Cw in [("su(2)+ Casimir", CasP), ("su(2)- Casimir", CasM),
               ("so(5)_s Casimir", Cas5s), ("so(5)_t Casimir", Cas5t)]:
    c0 = (np.trace(Cw) / tdim).real
    check(f"{nm} is a SCALAR on W (its weighted invariants collapse to plain traces)",
          nrm(Cw - c0 * np.eye(tdim)) < 1e-7, f"value {c0:.3f}, ||C - cI|| = {nrm(Cw - c0*np.eye(tdim)):.1e}")
chi_int = Rc(mono_big(e, list(range(4, 14))))
T5w = Rc(mono_big(e, [4, 5, 6, 7, 8]))
wrong5 = Rc(mono_big(e, [4, 9, 10, 11, 12]))
xr = np.random.randn(d); xr /= np.sqrt(xr @ M2full @ xr)
PhiA = np.einsum('i,iab->ab', xr, Ablk); PhiB = np.einsum('i,iab->ab', xr, Bblk)
Phi192 = kU @ np.block([[PhiA, np.zeros((96, 96))], [np.zeros((96, 96)), PhiB]]) @ kU.conj().T
podd = {"chi (Cl(14) volume)": C, "chi_int (16/16bar)": chi_int,
        "T5 (timelike volume)": T5w, "wrong 5-set volume e4,e9..e12": wrong5}
mx = 0.0
for nm, w in podd.items():
    vals = [abs(np.trace(w @ np.linalg.matrix_power(Phi192, n))) for n in range(1, 5)]
    mx = max(mx, max(vals))
    print(f"    P-odd weight {nm:<34s}: max_n |tr(w Phi^n)| = {max(vals):.2e}")
check("ALL P-odd native weights give identically-zero invariants on P-even channels", mx < 1e-7, f"max {mx:.2e}")
print("  => over the scanned native weight set the invariant weights collapse to span{I, Q5};")
print("     Q5 = -P = -K|_W (V8 identity): the parity-sensitive invariants are the KREIN SUPERTRACES")
print("     q_n = Str(Phi^n) = tr(sign(K) Phi^n) -- native at exactly the grade of K itself.")
print("     (Rep-theory remark, flagged, from V8's measured single-isotype structure W+ ~ 3x2x4x4:")
print("      the h-commutant on W is span{I, P, chi, P chi}; its K-self-adjoint P-even part is span{I, P}.)")

# ============================================== [3] THE INVARIANTS
print("\n[3] INVARIANT ENUMERATION (degree <= 4)")
D1 = ["t1", "q1"]; D2 = ["t2", "q2"]; D3 = ["t3", "q3"]; D4 = ["t4", "q4"]
quartics = ([(a,) for a in D4]
            + [(a, b) for a in D3 for b in D1]
            + [tuple(c) for c in combinations_with_replacement(D2, 2)]
            + [(a,) + tuple(c) for a in D2 for c in combinations_with_replacement(D1, 2)]
            + [tuple(c) for c in combinations_with_replacement(D1, 4)])
def flip_parity(mono):
    return (-1) ** sum(1 for b in mono if b.startswith("q"))
n_even = sum(1 for m in quartics if flip_parity(m) == 1)
print(f"  quartic invariant monomials in the basics: {len(quartics)} "
      f"({n_even} flip-even, {len(quartics)-n_even} flip-odd under the orientation flip)")
check("quartic monomial count = 20 (11 flip-even + 9 flip-odd)", len(quartics) == 20 and n_even == 11)
quadratics = [("t2",), ("q2",), ("t1", "t1"), ("t1", "q1"), ("q1", "q1")]

def basics_from_blocks(Am, Bm):
    A2, B2 = Am @ Am, Bm @ Bm
    sA = [np.trace(Am).real, np.trace(A2).real, np.trace(A2 @ Am).real, np.trace(A2 @ A2).real]
    sB = [np.trace(Bm).real, np.trace(B2).real, np.trace(B2 @ Bm).real, np.trace(B2 @ B2).real]
    out = {}
    for n in range(1, 5):
        out[f"t{n}"] = sA[n-1] + sB[n-1]
        out[f"q{n}"] = sA[n-1] - sB[n-1]
    return out
def basics_x(x):
    return basics_from_blocks(np.einsum('i,iab->ab', x, Ablk), np.einsum('i,iab->ab', x, Bblk))
def mono_val(mono, b):
    v = 1.0
    for f in mono: v *= b[f]
    return v

PhiF = C @ Phi192 @ np.linalg.inv(C)
xF, resF = coords_of(Ep.conj().T @ PhiF @ Ep, Em.conj().T @ PhiF @ Em)
bx, bF = basics_x(xr), basics_x(xF)
flipres = max(max(abs(bx[f"t{n}"] - bF[f"t{n}"]) for n in range(1, 5)),
              max(abs(bx[f"q{n}"] + bF[f"q{n}"]) for n in range(1, 5)))
check("orientation flip = chi conjugation: preserves the channel space, t_n invariant, q_n -> -q_n",
      resF < 1e-7 and flipres < 1e-7, f"channel res {resF:.1e}, basics res {flipres:.1e}")

hgens = [1j*J for J in Jp] + [1j*J for J in Jm] + sp5s + sp5t
Xh = sum(np.random.randn() * X for X in hgens)
Xh = 0.5 * (Xh - Xh.conj().T)
U = expm(0.05 * Xh)
PhiC = U @ Phi192 @ np.linalg.inv(U)
xC, resC = coords_of(Ep.conj().T @ PhiC @ Ep, Em.conj().T @ PhiC @ Em)
bC = basics_x(xC)
hres2 = max(abs(bx[k] - bC[k]) for k in bx)
check("h-invariance: all 8 basics invariant under a random h-conjugation (channel closed under h)",
      resC < 1e-6 and hres2 < 1e-6, f"channel res {resC:.1e}, basics res {hres2:.1e}")

NS = 400
Xs = np.random.randn(NS, d)
Xs /= np.sqrt(np.einsum('ni,ij,nj->n', Xs, M2full, Xs))[:, None]
Bs = [basics_x(x) for x in Xs]
Gq = np.array([[mono_val(m, b) for b in Bs] for m in quartics])
rms = np.sqrt((Gq ** 2).mean(axis=1))
sv = np.linalg.svd(Gq / rms[:, None], compute_uv=False)
rank4 = int((sv > 1e-9 * sv[0]).sum())
check("Gram independence: all 20 quartic invariants independent as functions on the channel",
      rank4 == 20, f"rank {rank4}/20, sv ratio {sv[-1]/sv[0]:.1e}")
G2 = np.array([[mono_val(m, b) for b in Bs] for m in quadratics])
sv2 = np.linalg.svd(G2 / np.sqrt((G2**2).mean(axis=1))[:, None], compute_uv=False)
check("quadratic invariants: 5 independent (t2, q2 = Str2, t1^2, t1 q1, q1^2)",
      int((sv2 > 1e-9 * sv2[0]).sum()) == 5, f"rank {int((sv2 > 1e-9*sv2[0]).sum())}/5")
RMS = {m: r for m, r in zip(quartics, rms)}

# ============================================== [4] POTENTIAL MACHINERY
print("\n[4] POTENTIAL MACHINERY (analytic gradients, bounded optimization)")
BIG = 1e7
def basics_grad(x):
    Am = np.einsum('i,iab->ab', x, Ablk); Bm = np.einsum('i,iab->ab', x, Bblk)
    A2, B2 = Am @ Am, Bm @ Bm
    dA = [np.eye(96, dtype=complex), Am, A2, A2 @ Am]
    dB = [np.eye(96, dtype=complex), Bm, B2, B2 @ Bm]
    gr = {}
    for n in range(1, 5):
        gA = n * np.real(np.einsum('iab,ba->i', Ablk, dA[n-1]))
        gB = n * np.real(np.einsum('iab,ba->i', Bblk, dB[n-1]))
        gr[f"t{n}"] = gA + gB
        gr[f"q{n}"] = gA - gB
    return basics_from_blocks(Am, Bm), gr
def V_and_grad(x, a2, lam):
    s = x @ M2full @ x
    if s > BIG:                       # barrier against runaway (unstable draws are screened anyway)
        return 1e30 * (s / BIG), 4e30 / BIG * (M2full @ x)
    b, gr = basics_grad(x)
    V = a2 * b["t2"]; gV = a2 * gr["t2"]
    for m, c in lam.items():
        if c == 0: continue
        V += c * mono_val(m, b)
        for i, f in enumerate(m):
            pref = c
            for j, f2 in enumerate(m):
                if j != i: pref *= b[f2]
            gV = gV + pref * gr[f]
    return V, gV
lam_test = {m: np.random.randn() for m in quartics}
x0 = 0.3 * np.random.randn(d)
V0, g0 = V_and_grad(x0, -1.0, lam_test)
gnum = np.zeros(d)
for i in range(d):
    dx = np.zeros(d); dx[i] = 1e-6
    gnum[i] = (V_and_grad(x0 + dx, -1.0, lam_test)[0] - V_and_grad(x0 - dx, -1.0, lam_test)[0]) / 2e-6
check("analytic gradient matches finite differences", nrm(g0 - gnum) / nrm(gnum) < 1e-5,
      f"rel {nrm(g0-gnum)/nrm(gnum):.1e}")

def basics_batch(X):
    Am = np.einsum('ni,iab->nab', X, Ablk); Bm = np.einsum('ni,iab->nab', X, Bblk)
    A2 = Am @ Am; B2 = Bm @ Bm
    out = {}
    sA = [np.einsum('naa->n', Am).real, np.einsum('naa->n', A2).real,
          np.einsum('nab,nba->n', A2, Am).real, np.einsum('nab,nba->n', A2, A2).real]
    sB = [np.einsum('naa->n', Bm).real, np.einsum('naa->n', B2).real,
          np.einsum('nab,nba->n', B2, Bm).real, np.einsum('nab,nba->n', B2, B2).real]
    for n in range(1, 5):
        out[f"t{n}"] = sA[n-1] + sB[n-1]
        out[f"q{n}"] = sA[n-1] - sB[n-1]
    return out
SCREEN = np.random.randn(800, d)
SCREEN /= np.sqrt(np.einsum('ni,ij,nj->n', SCREEN, M2full, SCREEN))[:, None]
SCREEN_B = basics_batch(SCREEN)
def quartic_batch(lam):
    v = np.zeros(SCREEN.shape[0])
    for m, c in lam.items():
        if c == 0: continue
        t = np.full(SCREEN.shape[0], c)
        for f in m: t = t * SCREEN_B[f]
        v += t
    return v
def stable(lam, polish=True):
    """min of the quartic form on the unit M2-sphere: sample screen + one gradient polish."""
    v = quartic_batch(lam)
    best = v.min()
    if polish:
        def f(x):
            s = x @ M2full @ x
            b, gr = basics_grad(x)
            Q = sum(c * mono_val(m, b) for m, c in lam.items())
            gQ = np.zeros(d)
            for m, c in lam.items():
                if c == 0: continue
                for i, ff in enumerate(m):
                    pref = c
                    for j, f2 in enumerate(m):
                        if j != i: pref *= b[f2]
                    gQ = gQ + pref * gr[ff]
            val = Q / s**2
            gv = gQ / s**2 - 4 * Q / s**3 * (M2full @ x)
            return val, gv
        x = SCREEN[int(np.argmin(v))].copy()
        r = spmin(f, x, jac=True, method="L-BFGS-B", options=dict(maxiter=120))
        best = min(best, r.fun)
    return best
BND = [(-80.0, 80.0)] * d
def minimize_V(a2, lam, nstart=8, xdets=None):
    starts = [np.random.randn(d) * 0.4 for _ in range(nstart)]
    if xdets is not None: starts += [xd.copy() for xd in xdets]
    bestx, bestV = None, np.inf
    for s in starts:
        r = spmin(lambda y: V_and_grad(y, a2, lam)[0], s,
                  jac=lambda y: V_and_grad(y, a2, lam)[1],
                  method="L-BFGS-B", bounds=BND, options=dict(maxiter=800, ftol=1e-14, gtol=1e-10))
        if np.isfinite(r.fun) and r.fun < bestV:
            bestV, bestx = r.fun, r.x
    return bestx, bestV
def classify(x):
    Am = np.einsum('i,iab->ab', x, Ablk); Bm = np.einsum('i,iab->ab', x, Bblk)
    mA = np.linalg.eigvalsh(Am); mB = np.linalg.eigvalsh(Bm)
    sc = np.sqrt(x @ M2full @ x)
    info = dict(mA=mA, mB=mB, scale=sc)
    if sc < 1e-5: return "SYM", info
    nx = x / sc
    cp = float(nx @ M2full @ (xPip / np.sqrt(xPip @ M2full @ xPip)))
    cm = float(nx @ M2full @ (xPim / np.sqrt(xPim @ M2full @ xPim)))
    info["cosPip"], info["cosPim"] = cp, cm
    mall = np.concatenate([np.abs(mA), np.abs(mB)])
    mmax = mall.max()
    selA = np.abs(mA).max() < 1e-3 * mmax and np.abs(mB).min() > 0.2 * mmax   # generations massless
    selB = np.abs(mB).max() < 1e-3 * mmax and np.abs(mA).min() > 0.2 * mmax   # mirrors massless
    if selA or selB:
        heavy = np.abs(mB) if selA else np.abs(mA)
        uniform = (heavy.max() - heavy.min()) < 1e-3 * mmax
        aligned = max(abs(cp), abs(cm)) > 0.999
        return ("ALIGN" if aligned else ("PSEL-uniform" if uniform else "PSEL-textured")), info
    if (mall.max() - mall.min()) < 1e-3 * mmax:
        return "BLIND-uniform", info
    return "MIXED", info
ALIGNED_CLASSES = ("ALIGN", "PSEL-uniform", "PSEL-textured")

xdets = [xPim.copy(), xPip.copy(), -xPim.copy()]
xI0 = np.zeros(d); xI0[names.index("I")] = 0.05; xdets.append(xI0)
xfam = np.zeros(d)
xfam[names.index("iJ-_3")] = 0.5; xfam[names.index("Q5*iJ-_3")] = 0.5
Afam = np.einsum('i,iab->ab', xfam, Ablk); Bfam = np.einsum('i,iab->ab', xfam, Bblk)
onesec = min(nrm(Afam), nrm(Bfam)) / max(nrm(Afam), nrm(Bfam))
if onesec > 1e-6:   # try the other relative sign
    xfam[names.index("Q5*iJ-_3")] = -0.5
    Afam = np.einsum('i,iab->ab', xfam, Ablk); Bfam = np.einsum('i,iab->ab', xfam, Bblk)
mfam = np.linalg.eigvalsh(Afam if nrm(Afam) > nrm(Bfam) else Bfam)
check("sign-texture corner element (iJ-_3 dressed) is one-sector-supported with spectrum +/-|m|",
      min(nrm(Afam), nrm(Bfam)) < 1e-8 and abs(np.abs(mfam).max() - np.abs(mfam).min()) < 1e-8,
      f"dead-sector norm {min(nrm(Afam), nrm(Bfam)):.1e}, |m| range [{np.abs(mfam).min():.3f}, {np.abs(mfam).max():.3f}]")
xdets.append(xfam.copy())

# ===================================== [5] THE REDUCED NATIVE FAMILY: analytic theorem + machine checks
print("\n[5] REDUCED NATIVE FAMILY  V = -t2 + l0*t2^2 + lq*q2^2 + l4*t4  (all four invariants native, l4 > 0)")
print("""  ANALYTIC REDUCTION (exact over the FULL 18432-dim P-even space E, since V depends only on the
  mass spectra and every spectrum pair is realizable in E): with p = sum(m_A^2), q = sum(m_B^2) and
  the t4 term minimized per sector at fixed (p, q) (uniform spectrum, Cauchy-Schwarz, needs l4 > 0):
     V(p,q) = -(p+q) + a(p^2+q^2) + 2b pq,   a = l0 + lq + l4/96,   b = l0 - lq
  (96 = measured sector multiplicity). Corner (one-sector) vs balanced:
     stable cone: a > 0 (corner bounded) and a + b > 0 (balanced bounded)
     corner wins  <=>  b > a  <=>  lq < -l4/192      V*_corner = -1/(4a)
     balanced wins <=>  b < a  <=>  lq > -l4/192     V*_bal   = -1/(2(a+b))
  The corner minimum manifold: A = 0, B^2 = m^2 I (or mirror image) -- ALL 96 states of one parity
  sector gapped at |m|, the other 96 EXACTLY massless. Pi_mirror is its unique positive point.""")
l0 = 1.0 / 192
def lam_red(lq192, l4r):
    return {("t2", "t2"): l0, ("q2", "q2"): lq192 / 192, ("t4",): l4r / 192}
def ab_of(lq192, l4r):
    a = l0 + lq192 / 192 + (l4r / 192) / 96
    b = l0 - lq192 / 192
    return a, b
tests5 = [(-0.50, 1.0, "ALIGNED side"), (+0.50, 1.0, "BLIND side"),
          (-0.25, 2.0, "ALIGNED side"), (+0.25, 2.0, "BLIND side"),
          (-4.0/192 - 0.01, 4.0, "boundary straddle, aligned side (lq*192 = -l4/192 - 0.01/192... shifted -0.01)"),
          (-4.0/192 + 0.01, 4.0, "boundary straddle, blind side (+0.01)")]
for lq192, l4r, tag in tests5:
    lam = lam_red(lq192, l4r)
    a, b = ab_of(lq192, l4r)
    sb = stable(lam)
    xs, Vs = minimize_V(-1.0, lam, nstart=8, xdets=xdets)
    cls, info = classify(xs)
    Vpred = -1.0 / (4 * a) if b > a else -1.0 / (2 * (a + b))
    print(f"    lq*192 = {lq192:+.4f}, l4 = {l4r:.1f}: sphere-min(quartic) = {sb:.2e}, "
          f"V* = {Vs:.6f} (analytic {Vpred:.6f}), class = {cls}, "
          f"cos(Pi+, Pi-) = ({info.get('cosPip', 0):+.4f}, {info.get('cosPim', 0):+.4f})  [{tag}]")
    ok = (sb > 0) and abs(Vs - Vpred) < 2e-3 * abs(Vpred) and \
         ((cls in ALIGNED_CLASSES) if b > a else (cls == "BLIND-uniform"))
    check(f"    reduced family at (lq*192, l4) = ({lq192:+.4f}, {l4r:.1f}): phase + depth match the theorem", ok, "")
lamU = lam_red(-1.5, 1.0)
sbU = stable(lamU)
check("    stability boundary is real: lq*192 = -1.5 (a < 0) is detected UNSTABLE by the sphere screen",
      sbU < -1e-6, f"sphere-min = {sbU:.2e}")

# sign-texture moduli + lifts (aligned-phase point lq*192 = -0.5, l4 = 1)
lam_al = lam_red(-0.5, 1.0)
a_al, _ = ab_of(-0.5, 1.0)
sopt = np.sqrt(1.0 / (2 * a_al) / 96)     # per-state |m| at the corner optimum
V_Pi = V_and_grad(sopt * xPim, -1.0, lam_al)[0]
V_tex = V_and_grad(sopt * xfam, -1.0, lam_al)[0]
print(f"    sign-texture moduli at the corner optimum scale |m| = {sopt:.4f}:")
print(f"      V(m*Pi_mirror) = {V_Pi:.8f}   V(m*[one-sector iJ-_3 texture]) = {V_tex:.8f}   analytic -1/(4a) = {-1/(4*a_al):.8f}")
check("    reduced family: sign-textured one-sector gapping EXACTLY degenerate with Pi_mirror (moduli)",
      abs(V_Pi - V_tex) < 1e-8 * abs(V_Pi) and abs(V_Pi - (-1/(4*a_al))) < 1e-8 * abs(V_Pi),
      f"dV = {abs(V_Pi - V_tex):.2e}")
lam_lift = dict(lam_al); lam_lift[("t3", "t1")] = -0.15 / (192 * 96)
sb_lift = stable(lam_lift)
V_Pi2 = minimize_V(-1.0, lam_lift, nstart=0, xdets=[sopt * xPim])[1]
V_tex2 = V_and_grad(sopt * xfam, -1.0, lam_lift)[0]   # t3*t1 vanishes identically on the texture branch
print(f"    lift by the flip-even native quartic t3*t1 (coeff < 0, still stable: sphere-min = {sb_lift:.2e}):")
print(f"      V(Pi branch, re-minimized) = {V_Pi2:.8f}   V(texture branch) = {V_tex2:.8f}")
check("    a generic flip-even quartic LIFTS the sign-texture moduli in favor of the exact projector pair",
      sb_lift > 0 and V_Pi2 < V_tex2 - 1e-6 * abs(V_Pi2), f"split {V_tex2 - V_Pi2:.3e}")
V_p = minimize_V(-1.0, lam_lift, nstart=0, xdets=[sopt * xPim])[1]
V_m = minimize_V(-1.0, lam_lift, nstart=0, xdets=[sopt * xPip])[1]
check("    flip-even potential: Pi_- and Pi_+ branches EXACTLY degenerate (orientation is SPONTANEOUS)",
      abs(V_p - V_m) < 1e-8 * abs(V_p), f"dV = {abs(V_p - V_m):.2e}")
lam_odd = dict(lam_lift); lam_odd[("q2", "t2")] = -0.3 / 192**2
sb_odd = stable(lam_odd)
V_p2 = minimize_V(-1.0, lam_odd, nstart=0, xdets=[sopt * xPim])[1]
V_m2 = minimize_V(-1.0, lam_odd, nstart=0, xdets=[sopt * xPip])[1]
print(f"    flip-odd native coupling q2*t2 (Krein-supertrace, stable: sphere-min = {sb_odd:.2e}):")
print(f"      V(Pi_mirror branch) = {V_p2:.8f}   V(Pi_+ branch) = {V_m2:.8f}")
check("    a flip-odd native coupling SELECTS one projector (orientation = one native coupling-sign bit)",
      sb_odd > 0 and abs(V_p2 - V_m2) > 1e-6 * abs(V_p2), f"split {abs(V_p2 - V_m2):.3e}")

# Hessian + Goldstone accounting at the lifted aligned vacuum
xstar, Vstar = minimize_V(-1.0, lam_lift, nstart=8, xdets=xdets)
cls_s, info_s = classify(xstar)
H = np.zeros((d, d))
for i in range(d):
    dx = np.zeros(d); dx[i] = 1e-5
    H[i] = (V_and_grad(xstar + dx, -1.0, lam_lift)[1] - V_and_grad(xstar - dx, -1.0, lam_lift)[1]) / 2e-5
H = 0.5 * (H + H.T)
evH = np.linalg.eigvalsh(H)
Phis = kU @ np.block([[np.einsum('i,iab->ab', xstar, Ablk), np.zeros((96, 96))],
                      [np.zeros((96, 96)), np.einsum('i,iab->ab', xstar, Bblk)]]) @ kU.conj().T
tangs = []
for X in hgens:
    T = comm(X, Phis)
    xt, rt = coords_of(Ep.conj().T @ T @ Ep, Em.conj().T @ T @ Em)
    if rt < 1e-6 and nrm(xt) > 1e-8: tangs.append(xt)
orb_rank = 0 if not tangs else int((np.linalg.svd(np.array(tangs), compute_uv=False) > 1e-6).sum())
nulls = int((np.abs(evH) < 1e-6 * np.abs(evH).max()).sum())
mAv, mBv = info_s["mA"], info_s["mB"]
light = mAv if np.abs(mAv).max() < np.abs(mBv).max() else mBv
heavy = mBv if light is mAv else mAv
print(f"    global vacuum of the lifted potential: class = {cls_s}, cos(Pi_-, Pi_+) = "
      f"({info_s.get('cosPim', 0):+.6f}, {info_s.get('cosPip', 0):+.6f})")
print(f"      masses: max|m_light-sector| = {np.abs(light).max():.2e}, gapped band "
      f"[{np.abs(heavy).min():.6f}, {np.abs(heavy).max():.6f}] x{len(heavy)}")
print(f"      Hessian: min eig = {evH.min():.3e}, null count = {nulls}; h-orbit (Goldstone) rank at the vacuum = {orb_rank}")
check("    lifted aligned vacuum = EXACT sector projector, h-invariant (0 Goldstones), no flat directions",
      cls_s == "ALIGN" and max(abs(info_s.get('cosPim', 0)), abs(info_s.get('cosPip', 0))) > 0.999
      and orb_rank == 0 and nulls == 0 and evH.min() > 1e-8, "")

# ====================================================== [6] PHASE MAP + FULL EVEN-FAMILY RANDOM SCAN
print("\n[6a] PHASE MAP over (l4, lq*192), l0 = 1/192.  Symbols: A aligned-class, S mirror-blind uniform, M mixed, U unstable")
l4s = [0.5, 1.0, 2.0, 4.0]
lqs = [-0.95, -0.6, -0.3, -0.1, -0.04, 0.0, 0.1, 0.3, 0.6, 0.95]
grid = {}
for l4r in l4s:
    row = ""
    for lqv in lqs:
        lam = lam_red(lqv, l4r)
        if stable(lam) < 1e-10:
            row += "  U"; grid[(l4r, lqv)] = "U"; continue
        xs, Vs = minimize_V(-1.0, lam, nstart=6, xdets=xdets)
        cls, info = classify(xs)
        sym = {"ALIGN": "A", "PSEL-uniform": "A", "PSEL-textured": "A",
               "BLIND-uniform": "S", "MIXED": "M", "SYM": "0"}[cls]
        row += f"  {sym}"; grid[(l4r, lqv)] = sym
    print(f"    l4 = {l4r:4.1f} |" + row + f"      (analytic boundary at lq*192 = {-l4r/192:+.4f})")
print("    lq*192:   " + " ".join(f"{v:+.2f}" for v in lqs))
bnd_ok = True
for l4r in l4s:
    for lqv in lqs:
        got = grid[(l4r, lqv)]
        if got == "U": continue
        margin = 0.02
        if lqv < -l4r/192 - margin and got != "A": bnd_ok = False
        if lqv > -l4r/192 + margin and got != "S": bnd_ok = False
check("phase map matches the analytic phases on every stable cell (boundary margin 0.02)", bnd_ok)

print("\n[6b] FULL FLIP-EVEN FAMILY: random stable draws over all 11 even quartic invariants")
even_monos = [m for m in quartics if flip_parity(m) == 1]
counts, align_q2_signs, kept_examples = {}, [], []
n_kept, n_att = 0, 0
while n_kept < 20 and n_att < 300:
    n_att += 1
    lam = {m: np.random.randn() / (RMS[m] * 6) for m in even_monos}
    lam[("t2", "t2")] = abs(lam[("t2", "t2")])          # bias the backbone couplings toward the
    lam[("t4",)] = abs(lam[("t4",)])                    # stable cone; stability still SCREENED
    if stable(lam) < 1e-10: continue
    n_kept += 1
    xs, Vs = minimize_V(-1.0, lam, nstart=8, xdets=xdets)
    cls, info = classify(xs)
    counts[cls] = counts.get(cls, 0) + 1
    if cls in ALIGNED_CLASSES:
        align_q2_signs.append(np.sign(lam[("q2", "q2")]))
        if not kept_examples: kept_examples.append(lam)
print(f"    attempts {n_att}, stable draws kept {n_kept}; vacuum classes: " +
      ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
n_align = sum(v for k, v in counts.items() if k in ALIGNED_CLASSES)
print(f"    aligned-class fraction {n_align}/{n_kept}; sign(q2^2 coupling) among aligned draws: "
      f"{align_q2_signs.count(-1.0)} negative / {len(align_q2_signs)} (reported, not asserted -- the clean")
print(f"    one-bit criterion is the reduced-family theorem; generic even draws mix several q-even invariants)")
check("both phases realized among random stable native draws (alignment is a PHASE: present, not forced)",
      n_align > 0 and n_align < n_kept, f"{n_align}/{n_kept}")
if kept_examples:
    lam0 = kept_examples[0]
    nopen = 0
    for _ in range(10):
        lam2 = {m: c * (1 + 0.05 * np.random.randn()) for m, c in lam0.items()}
        if stable(lam2) < 1e-12: continue
        xs, _ = minimize_V(-1.0, lam2, nstart=6, xdets=xdets)
        cls, _ = classify(xs)
        if cls in ALIGNED_CLASSES: nopen += 1
    print(f"    openness: 5% perturbations of an aligned draw in ALL 11 even couplings: {nopen}/10 stay aligned-class")
    check("alignment survives generic 5% perturbations of every coupling (open region in the full even family)",
          nopen >= 9, f"{nopen}/10")

# ====================================================== [7] CONTROLS
print("\n[7] CONTROLS (each can fail; discriminating power)")
# C1: scrambled weight -- a NON-native balanced involution R commuting with P
dgA = np.array([1.0] * 48 + [-1.0] * 48); np.random.shuffle(dgA)
dgB = np.array([1.0] * 48 + [-1.0] * 48); np.random.shuffle(dgB)
UA = np.linalg.qr(np.random.randn(96, 96) + 1j * np.random.randn(96, 96))[0]
UB = np.linalg.qr(np.random.randn(96, 96) + 1j * np.random.randn(96, 96))[0]
RA = UA @ np.diag(dgA) @ UA.conj().T; RB = UB @ np.diag(dgB) @ UB.conj().T
lqR, l4R = -0.5 / 192, 1.0 / 192
def VR_and_grad(x):
    Am = np.einsum('i,iab->ab', x, Ablk); Bm = np.einsum('i,iab->ab', x, Bblk)
    A2, B2 = Am @ Am, Bm @ Bm
    t2 = np.trace(A2).real + np.trace(B2).real
    t4 = np.trace(A2 @ A2).real + np.trace(B2 @ B2).real
    q2R = np.trace(RA @ A2).real + np.trace(RB @ B2).real
    gt2 = 2 * (np.real(np.einsum('iab,ba->i', Ablk, Am)) + np.real(np.einsum('iab,ba->i', Bblk, Bm)))
    gt4 = 4 * (np.real(np.einsum('iab,ba->i', Ablk, A2 @ Am)) + np.real(np.einsum('iab,ba->i', Bblk, B2 @ Bm)))
    gq2R = np.real(np.einsum('iab,ba->i', Ablk, RA @ Am + Am @ RA)) + \
           np.real(np.einsum('iab,ba->i', Bblk, RB @ Bm + Bm @ RB))
    V = -t2 + l0 * t2**2 + lqR * q2R**2 + l4R * t4
    gV = -gt2 + 2 * l0 * t2 * gt2 + 2 * lqR * q2R * gq2R + l4R * gt4
    return V, gV
bestx, bestV = None, np.inf
for s in [np.random.randn(d) * 0.4 for _ in range(8)] + xdets:
    r = spmin(lambda y: VR_and_grad(y)[0], s, jac=lambda y: VR_and_grad(y)[1],
              method="L-BFGS-B", bounds=BND, options=dict(maxiter=800, ftol=1e-14, gtol=1e-10))
    if np.isfinite(r.fun) and r.fun < bestV: bestV, bestx = r.fun, r.x
clsR, infoR = classify(bestx)
print(f"    C1 scrambled weight (same potential shape, R replacing sign(K)): vacuum class = {clsR}, "
      f"cos(Pi+, Pi-) = ({infoR.get('cosPip', 0):+.3f}, {infoR.get('cosPim', 0):+.3f})")
check("C1: with a non-native weight the parity-aligned vacuum DISAPPEARS (the phase tracks the native weight)",
      clsR not in ALIGNED_CLASSES, "")
# C2: random quartic polynomials of matched scale replacing the invariants
perms24 = [(0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),(0,3,1,2),(0,3,2,1),
           (1,0,2,3),(1,0,3,2),(1,2,0,3),(1,2,3,0),(1,3,0,2),(1,3,2,0),
           (2,0,1,3),(2,0,3,1),(2,1,0,3),(2,1,3,0),(2,3,0,1),(2,3,1,0),
           (3,0,1,2),(3,0,2,1),(3,1,0,2),(3,1,2,0),(3,2,0,1),(3,2,1,0)]
n_alignC, n_keptC, n_attC = 0, 0, 0
while n_keptC < 12 and n_attC < 150:
    n_attC += 1
    T4r = np.random.randn(d, d, d, d)
    T4r = sum(T4r.transpose(p) for p in perms24) / 24.0
    scale = np.abs(np.einsum('ijkl,ni,nj,nk,nl->n', T4r, SCREEN, SCREEN, SCREEN, SCREEN))
    T4r *= (0.02 / scale.mean())            # matched to the native quartic scale on the sphere
    T4r += 0.5 * l0 * np.einsum('ij,kl->ijkl', M2full, M2full) * (2/3)   # same t2^2-like backbone
    qv = np.einsum('ijkl,ni,nj,nk,nl->n', T4r, SCREEN, SCREEN, SCREEN, SCREEN)
    if qv.min() < 1e-10: continue
    n_keptC += 1
    def Vr(y): return -(y @ M2full @ y) + np.einsum('ijkl,i,j,k,l', T4r, y, y, y, y)
    def gVr(y): return -2 * M2full @ y + 4 * np.einsum('ijkl,j,k,l->i', T4r, y, y, y)
    bb = (None, np.inf)
    for s in [np.random.randn(d) * 0.4 for _ in range(6)] + xdets:
        r = spmin(Vr, s, jac=gVr, method="L-BFGS-B", bounds=BND, options=dict(maxiter=600))
        if np.isfinite(r.fun) and r.fun < bb[1]: bb = (r.x, r.fun)
    clsr, _ = classify(bb[0])
    if clsr in ALIGNED_CLASSES: n_alignC += 1
print(f"    C2 random symmetric quartic polynomials (matched scale, stability-screened): aligned-class minima "
      f"{n_alignC}/{n_keptC} (native even family gave {n_align}/{n_kept})")
check("C2: scrambled invariants do NOT reproduce the alignment phase", n_alignC == 0, f"{n_alignC}/{n_keptC}")
print("    C3: P-odd native weights give identically-zero invariants -- measured in [2] (max ~ 1e-13)")

# ====================================================== [8] VERDICT
print("\n" + "=" * 108)
print("[8] VERDICT (route A1)")
print("=" * 108)
print("""  ALIGNMENT IS AN OPEN-REGION PHASE OF THE NATIVE INVARIANT POTENTIALS -- NOT A THEOREM OF THEM.
  (+) Mechanism, stated exactly: a Krein-supertrace quartic potential with lq < -l4/192 inside the
      stable cone forces the global vacuum onto the mirror-hiding corner: all 96 states of one
      parity sector uniformly gapped, the other 96 EXACTLY massless -- V8's Pi_mirror payoff,
      produced as a potential MINIMUM (analytic over the full 18432-dim P-even space in the
      reduced family; numerically confirmed on the 34-dim native channel). Flip-even native
      quartics lift the sign-texture moduli to the exact projector pair; the orientation Z2 is
      spontaneous (flip-even) or one native coupling-sign (flip-odd) -- no import beyond K.
  (+) The invariant structure collapses: all four group Casimirs are scalars on W and every
      P-odd native weight gives vanishing invariants, so the ONLY parity-sensitive native
      invariants are the Krein supertraces Str(Phi^n) = tr(sign(K) Phi^n). The alignment
      question is thereby reduced to coupling SIGNS of supertrace invariants -- in the reduced
      family, to exactly ONE bit: sign(lq + l4/192).
  (-) Nothing computed here fixes that sign. On the other side of the boundary the vacuum is
      mirror-blind; both phases occur among random stable native draws. "GU forces alignment"
      is NOT established and is not claimed; what is established is that alignment no longer
      needs an imported DIRECTION -- it needs an imported (or someday derived) SIGN.
  Controls: a scrambled weight destroys the parity-aligned vacuum, scrambled quartic polynomials
  produce zero aligned minima, P-odd weights vanish identically. Scope: enumerated weights and
  channel, quartic truncation, frozen fiber, no dynamics, single signature (9,5).""")

if FAIL:
    print(f"\nFAILED CHECKS: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = anchors reproduced, all checks passed, controls have power.")
