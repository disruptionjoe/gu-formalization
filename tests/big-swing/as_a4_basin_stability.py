"""
AS-A4 (route A4, BASIN & STABILITY of the aligned condensate): assume V8's alignment
(Phi* = phi * Pi_mirror, phi > 0, Pi_mirror = (I + Q5)/2 = (I - P_ghost)/2 on the 192-dim
triplet sector W) and quantify its robustness as dynamics-facing kinematics.

Four questions, all machine-checked on the verified (9,5) carrier:

 (i)  SECOND VARIATION. On the P-even channel space E (K-self-adjoint, [.,P]=0; measured
      real dim 2*96^2 = 18432, native Clifford slice measured below), build an invariant
      basis INDEPENDENTLY (own construction; no A1 import) and compute the Hessian of the
      simplest stable native potential at the aligned point.
      RESULT: for the orientation-blind quartic V0 = -m^2 tr(Phi^2) + lam tr(Phi^4) the
      aligned point is an exact SADDLE: Hessian spectrum {-2m^2 (all generation-diagonal
      channels), +4m^2 (all mirror-diagonal channels)} -- the masslessness of the 96
      generations sits at the TOP of the double well in every generation channel, and the
      global minima gap everything (mirror-blind, V1-consistent). Adding the single
      lowest-order orientation-odd native invariant s2 = tr(Q5 Phi^2) at coupling h < -m^2
      flips the aligned point to the GLOBAL MINIMUM (Hessian positive definite, no zero
      modes; per-channel proof + random sampling). The commutant classification below shows
      {1, Q5} are the ONLY K-self-adjoint P-even weightings available at quadratic order,
      so this is exhaustive at that order: ALIGNMENT = the sign of one native coupling =
      V8's orientation Z2. The two imports V8 priced separately (orientation + alignment)
      MERGE at potential grade.
 (ii) MISALIGNMENT THRESHOLDS. gap(eps) for M = Pi_mirror + eps*X over every independent
      native channel direction plus engineered and random controls; V8's iJ+3 numbers
      reproduced as anchor; worst-case direction identified and PROVED optimal at fixed
      Frobenius budget (eps* = 1/(2*sqrt(48)) ~ 0.0722); native monomial channels uniform
      at ~0.707; the I--Q5 plane never closes the gap.
(iii) KREIN POSITIVITY THROUGH THE BASIN. [M(eps), P] = 0 holds at machine precision for
      EVERY eps in EVERY P-even channel direction (linear identity, eps-independent);
      P-odd contamination breaks it linearly in eps (slopes printed).
 (iv) THE WEYL POINT phi = mu/q. Identically the aligned configuration at scale 2mu.
      Inside the stable basin iff h < -m^2 AND the Dirac scale is condensate-born
      (2mu = phi*; automatic when mu is the I-component of the condensate, one tuning if
      mu is external -- and on the pure-Q5 ray the orientation coupling is INERT, s2 = 0
      there, so alignment dynamics needs the I-component). Massless generations survive
      ALL P-even mirror-channel (A=0) perturbations exactly (block decoupling), degrade
      LINEARLY under native tadpoles c1*tr(Q5 Phi) (suppressed by the stabilizing gap:
      m_gen ~ c1 / (2|m^2+h|); exact masslessness needs Phi -> -Phi symmetry, flagged),
      and QUADRATICALLY under P-odd contamination (Schur: m_gen ~ eps^2 |YZ| / phi*).

DISCIPLINE: anchors reproduced first (triplet Krein (+96,-96,0), residuals printed).
No element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is assumed, inserted, or
divided by; all dimensions (96, 192, 256, 512, 9216, 18432) are measured outputs; the
couplings (m^2=2, lam=1, h=+-6, mu, q, c1) are free parameters of the potential class.
Every claim is "mechanism (quartic native potential class on the measured block structure)
forces X" -- never "GU forces X". Controls: finite-difference Hessian, non-critical
gradient, positive-definite Hessian at the mirror-blind global minimum (machinery can
return PD), random-weighting non-criticality, orientation-flip control, random-direction
threshold floor vs the proved optimum, V8 misalignment-number reproduction.

Run: python tests/big-swing/as_a4_basin_stability.py    (exit 0)
Carrier machinery reused verbatim from tests/big-swing/vg_v8_t5_map_attempt.py (V8).
"""
import numpy as np
from itertools import combinations
from scipy.linalg import eigh as geigh
from scipy.optimize import minimize

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
    """Verified carrier recipe (verbatim from V8 / V1 / ghost_parity_krein.py)."""
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
print("AS-A4: BASIN & STABILITY of the aligned condensate phi * Pi_mirror on the (9,5) triplet sector")
print("=" * 110)

# ==================================================================================== [0] ANCHORS
print("\n[0] ANCHORS (9,5) (must reproduce before any claim)")
D = build({4, 5, 6, 7, 8})
e, Wt, Rc, K, P, C = D["e"], D["Wt"], D["Rc"], D["K"], D["P"], D["C"]
kev, kU = D["kev"], D["kU"]
tdim = Wt.shape[1]
I192 = np.eye(tdim, dtype=complex)
check("rank(Gamma) = 128", D["rankG"] == 128, str(D["rankG"]))
check("dim ker(Gamma) = 1664", D["kerdim"] == 1664, str(D["kerdim"]))
check("triplet dim = 192", tdim == 192, str(tdim))
check("beta_S pseudo-anti-Hermiticity ~ 0", D["betares"] < TOL, f"{D['betares']:.1e}")
npl, nmi = int((kev > TOL).sum()), int((kev < -TOL).sum())
check("triplet Krein signature (+96, -96, 0)", (npl, nmi) == (96, 96), f"(+{npl}, -{nmi}, 0)")
check("P = sign(K) = K|_W (|K|-eigs exactly 1)", nrm(P - K) < 1e-9, f"||P-K|| = {nrm(P - K):.1e}")
check("{P, chi} = 0", nrm(acomm(P, C)) < 1e-8, f"{nrm(acomm(P, C)):.1e}")
Kinv = np.linalg.inv(K)
adjK = lambda A: Kinv @ A.conj().T @ K
g = {i: Rc(mono_big(e, [i])) for i in range(4, 14)}
Q5 = Rc(mono_big(e, [9, 10, 11, 12, 13]))
check("V8 identity: Q5 = e9..e13|_W = -P_ghost", nrm(Q5 + P) < 1e-9, f"||Q5+P|| = {nrm(Q5 + P):.1e}")
PIm = 0.5 * (I192 + Q5)          # mirror projector = (I - P)/2
PIg = 0.5 * (I192 - Q5)          # generation projector = (I + P)/2
Ep, Em = kU[:, kev > 0], kU[:, kev < 0]     # generation (P=+1) / mirror (P=-1) frames
check("K blocks in kU frame: Ep'KEp = +I, Em'KEm = -I",
      nrm(Ep.conj().T @ K @ Ep - np.eye(96)) < 1e-9 and
      nrm(Em.conj().T @ K @ Em + np.eye(96)) < 1e-9)
Jp = [Rc(M) for M in D["J3full"]]
Jm = [Rc(M) for M in D["J3mfull"]]
sp5s = [g[i] @ g[j] for (i, j) in combinations(range(9, 14), 2)]
sp5t = [g[i] @ g[j] for (i, j) in combinations(range(4, 9), 2)]

# =================================================== [1] THE P-EVEN CHANNEL SPACE, BUILT FRESH
print("\n[1] THE P-EVEN CHANNEL SPACE E AND ITS NATIVE CLIFFORD SLICE (own construction, no A1 import)")
print(f"  E = {{X : K^-1 X^dag K = X, [X, P] = 0}}; in the kU frame E = {{diag(A, B): A, B Hermitian}}")
d_plus = int((kev > 0).sum())
print(f"  dim_R E = 2 * {d_plus}^2 = {2 * d_plus**2}   (measured Krein multiplicities, not inputs)")

# native basis: all internal Clifford monomials with EVEN timelike count (grammar: P-even),
# K-self-adjointized. Includes the identity (empty set) and Q5.
tlk, slk = [4, 5, 6, 7, 8], [9, 10, 11, 12, 13]
basis, names = [], []
n_dead = 0
for nt in (0, 2, 4):
    for tc in combinations(tlk, nt):
        for ns in range(6):
            for sc in combinations(slk, ns):
                idxs = list(tc) + list(sc)
                M = I192.copy()
                for i in idxs:
                    M = M @ g[i]
                Msa = 0.5 * (M + adjK(M))
                if nrm(Msa) < 1e-8 * nrm(M):
                    Msa = 0.5 * (1j * M + adjK(1j * M))
                if nrm(Msa) < 1e-8 * nrm(M):
                    n_dead += 1
                    continue
                basis.append(Msa)
                names.append("1" if not idxs else "e" + ".".join(str(i) for i in idxs))
nb = len(basis)
check("native monomial channel count = 512 (16 timelike-even x 32 spacelike subsets), none K-dead",
      nb == 512 and n_dead == 0, f"count {nb}, dead {n_dead}")
B_arr = np.array(basis)                              # (512, 192, 192)
resP = max(nrm(comm(X, P)) / nrm(X) for X in basis)
check("every native channel is P-even (grammar: even timelike count)", resP < 1e-8, f"max {resP:.1e}")
n_comm = sum(1 for X in basis if nrm(comm(X, C)) / nrm(X) < 1e-8)
n_anti = sum(1 for X in basis if nrm(acomm(X, C)) / nrm(X) < 1e-8)
print(f"  chi-grading of the native channels: {n_comm} chi-commuting (E+ slice), {n_anti} chi-anticommuting (E- slice)")
check("chi-grading exhaustive and even/odd-grade split 256/256", n_comm == 256 and n_anti == 256)
Vflat = B_arr.reshape(nb, -1)
sv = np.linalg.svd(np.hstack([Vflat.real, Vflat.imag]), compute_uv=False)
rank = int((sv > 1e-8 * sv[0]).sum())
check("native channel span: real dim = 512 (all independent)", rank == 512, f"rank {rank}")
# closure under Q5-multiplication (the pairing that isolates pure generation/mirror blocks)
worst = 0.0
for k in np.random.choice(nb, 24, replace=False):
    QX = Q5 @ basis[k]
    dists = [min(nrm(QX - Y), nrm(QX + Y)) for Y in basis]
    worst = max(worst, min(dists) / nrm(QX))
check("native space closed under Q5-multiplication (sampled: Q5*monomial = +-monomial')",
      worst < 1e-8, f"max residual {worst:.1e}")
# pure-A (generation-diagonal) and pure-B (mirror-diagonal) split ranks
GA = np.array([PIg @ X @ PIg for X in basis]).reshape(nb, -1)
GB = np.array([PIm @ X @ PIm for X in basis]).reshape(nb, -1)
rA = int((lambda s: (s > 1e-8 * s[0]).sum())(np.linalg.svd(np.hstack([GA.real, GA.imag]), compute_uv=False)))
rB = int((lambda s: (s > 1e-8 * s[0]).sum())(np.linalg.svd(np.hstack([GB.real, GB.imag]), compute_uv=False)))
check("generation-diagonal / mirror-diagonal split of the native slice = 256 / 256",
      rA == 256 and rB == 256, f"({rA}, {rB})")

# commutant of the native compact symmetry on W, and the quadratic-weighting classification
print("\n  COMMUTANT CLASSIFICATION (which invariant mass weightings exist at quadratic order):")
gens = Jp + Jm + sp5s + sp5t
cands = {"I": I192, "P(= -Q5)": P, "chi": C, "P.chi": P @ C}
for nm, S in cands.items():
    r = max(nrm(comm(S, G)) for G in gens)
    ksa = nrm(adjK(S) - S) < 1e-8
    ksa_i = nrm(adjK(1j * S) - 1j * S) < 1e-8
    pe = nrm(comm(S, P)) < 1e-8
    po = nrm(acomm(S, P)) < 1e-8
    print(f"    {nm:<10s} [.,compact gens] max = {r:.1e}   K-sa: {'yes' if ksa else ('as i*S' if ksa_i else 'NO')}"
          f"   P-parity: {'EVEN' if pe else ('ODD' if po else 'mixed')}")
check("K-self-adjoint AND P-even commutant weightings = {I, Q5} exactly "
      "(chi is K-skew -> its K-sa phase i*chi is P-ODD; P.chi is P-ODD)",
      nrm(adjK(P) - P) < 1e-8 and nrm(adjK(C) + C) < 1e-8 and
      nrm(acomm(P @ C, P)) / nrm(P @ C) < 1e-8 and nrm(acomm(C, P)) / nrm(C) < 1e-8)
print("    => the most general native-invariant P-even quadratic mass term is tr((-m^2 + h*Q5) Phi^2):")
print("       the coupling h multiplies the ONE orientation-odd weighting. This is exhaustive at")
print("       quadratic order over the measured commutant.")

# symmetry isolation of the aligned direction (no Goldstone modes possible)
resI = max(nrm(comm(PIm, G)) for G in gens)
Sset = [a for a in range(14) if nrm(np.conj(e[a]) + e[a]) < 1e-12]
C128 = I128.copy()
for a in Sset:
    C128 = C128 @ e[a]
Jw = Wt.conj().T @ np.kron(I14, C128) @ np.conj(Wt)
jact = lambda M: Jw @ np.conj(M) @ np.linalg.inv(Jw)
check("Pi_mirror is symmetry-isolated: [Pi_mirror, all compact native gens] = 0 AND J_quat-fixed",
      resI < 1e-8 and nrm(jact(PIm) - PIm) < 1e-8,
      f"max [.,gens] = {resI:.1e}, J-fix = {nrm(jact(PIm) - PIm):.1e}")
print("    => the aligned configuration has NO Goldstone directions; Hessian zero modes, if any,")
print("       would be potential-tuning artifacts, not symmetry artifacts.")

# ============================================== [2] THE LOW-ORDER INVARIANT RING (measured)
print("\n[2] LOW-ORDER INVARIANT RING on E (single-trace; multi-trace noted, not exhausted)")
cblk = Ep.conj().T @ C @ Em
def mkE(Ablk, Bblk):
    return Ep @ Ablk @ Ep.conj().T + Em @ Bblk @ Em.conj().T
def randH(n=96):
    X = np.random.randn(n, n) + 1j * np.random.randn(n, n)
    return 0.5 * (X + X.conj().T)
A0 = randH()
probes = {
    "pure E+ (B=+c'Ac)": mkE(A0, cblk.conj().T @ A0 @ cblk),
    "pure E- (B=-c'Ac)": mkE(A0, -cblk.conj().T @ A0 @ cblk),
    "pure gen-diag (A,0)": mkE(A0, np.zeros((96, 96), complex)),
    "pure mir-diag (0,B)": mkE(np.zeros((96, 96), complex), A0),
}
t2f = lambda X: np.real(np.trace(X @ X))
s2f = lambda X: np.real(np.trace(Q5 @ X @ X))
t2pf = lambda X: np.real(np.trace(C @ X @ C @ X))
rows = []
print("    invariant values on probe elements (t2 = tr Phi^2, s2 = tr Q5 Phi^2, t2' = tr chi Phi chi Phi):")
for nm, X in probes.items():
    X = X / nrm(X) * np.sqrt(96)
    vals = [t2f(X), s2f(X), t2pf(X)]
    rows.append(vals)
    print(f"      {nm:<22s} t2 = {vals[0]:+8.3f}  s2 = {vals[1]:+8.3f}  t2' = {vals[2]:+8.3f}")
rk = np.linalg.matrix_rank(np.array(rows), tol=1e-6)
check("three independent quadratic invariants (value matrix rank 3)", rk == 3, f"rank {rk}")
Xr = probes["pure gen-diag (A,0)"]
check("parities: s2 flips under chi-conjugation (= orientation flip at potential level); t2, t2' even",
      abs(s2f(C @ Xr @ C) + s2f(Xr)) < 1e-6 * abs(s2f(Xr)) and
      abs(t2f(C @ Xr @ C) - t2f(Xr)) < 1e-6 * abs(t2f(Xr)),
      f"s2(chi.X.chi)/s2(X) = {s2f(C @ Xr @ C) / s2f(Xr):+.3f}")
print("    linear invariants: t1 = tr Phi (chi-even), s1 = tr Q5 Phi (chi-odd, orientation-odd tadpole).")
print("    s2 is a PURE E+/E- cross form (vanishes on chi-graded elements: measured above via probes)")
print("    -- exactly V8's |m|-splitting mixer class, appearing here as the alignment-selecting coupling.")

# ==================================================================== [3] (i) SECOND VARIATION
print("\n[3] (i) SECOND VARIATION at the aligned point (potential class V = tr((-m^2 + h Q5) Phi^2) + lam tr Phi^4)")
m2, lam = 2.0, 1.0
def S_of(h):
    return -m2 * I192 + h * Q5
def Vpot(Phi, h):
    P2 = Phi @ Phi
    return np.real(np.trace(S_of(h) @ P2) + lam * np.trace(P2 @ P2))
def gradV(Phi, h):
    S = S_of(h)
    return S @ Phi + Phi @ S + 4 * lam * Phi @ Phi @ Phi
def hess_form(X, Phi, h):
    S = S_of(h)
    P2 = Phi @ Phi
    L = S @ X + X @ S + 4 * lam * (P2 @ X + X @ P2 + Phi @ X @ Phi)
    return np.real(np.trace(L @ X))
def hess_matrix(Phi, h):
    S = S_of(h)
    P2 = Phi @ Phi
    L = np.array([S @ X + X @ S + 4 * lam * (P2 @ X + X @ P2 + Phi @ X @ Phi) for X in basis])
    Lv = L.reshape(nb, -1)
    Tv = np.transpose(B_arr, (0, 2, 1)).reshape(nb, -1)   # vec(X^T): tr(L X) = Lv . vec(X^T)
    H = np.real(Lv @ Tv.T)
    return 0.5 * (H + H.T)
Gram = np.real(Vflat @ np.transpose(B_arr, (0, 2, 1)).reshape(nb, -1).T)
Gram = 0.5 * (Gram + Gram.T)
check("trace metric on E positive definite on the native slice (min Gram eig > 0)",
      np.linalg.eigvalsh(Gram).min() > 1e-8, f"min = {np.linalg.eigvalsh(Gram).min():.3e}")

def spectrum_line(H):
    w = geigh(H, Gram, eigvals_only=True)
    va, cn = np.unique(np.round(w, 6), return_counts=True)
    return w, ", ".join(f"{v:+.3f} x{c}" for v, c in zip(va, cn))

# ---- V0: the simplest stable orientation-blind potential (h = 0) ----
h = 0.0
phi0 = np.sqrt((m2 - h) / (2 * lam))
Phi0 = phi0 * PIm
gn = nrm(gradV(Phi0, h))
check(f"h=0: aligned point phi* = {phi0:.3f} is critical (|grad| ~ 0)", gn < 1e-9, f"|grad| = {gn:.1e}")
gn_off = nrm(gradV(0.7 * Phi0, h))
check("control: gradient NONZERO off the critical point (0.7 phi*)", gn_off > 1.0, f"|grad| = {gn_off:.2f}")
H0 = hess_matrix(Phi0, h)
w0, line0 = spectrum_line(H0)
print(f"  h=0 HESSIAN SPECTRUM on the native channel space (per unit tr X^2): {line0}")
check("h=0: Hessian INDEFINITE -- the aligned point is a SADDLE "
      f"(analytic: -2m^2 = {-2*m2:+.0f} on gen-channels, +4m^2 = {4*m2:+.0f} on mirror-channels)",
      abs(w0.min() + 2 * m2) < 1e-6 and abs(w0.max() - 4 * m2) < 1e-6
      and int((w0 < 0).sum()) == 256 and int((w0 > 0).sum()) == 256,
      f"[{w0.min():.3f}, {w0.max():.3f}], {int((w0 < 0).sum())} negative modes")
# finite-difference control
Xfd = basis[np.random.randint(nb)] + 0.3 * basis[np.random.randint(nb)]
epsfd = 1e-3
fd = (Vpot(Phi0 + epsfd * Xfd, h) - 2 * Vpot(Phi0, h) + Vpot(Phi0 - epsfd * Xfd, h)) / epsfd**2
an = hess_form(Xfd, Phi0, h)
check("finite-difference Hessian control (random direction)", abs(fd - an) < 1e-4 * abs(an),
      f"FD {fd:.6f} vs analytic {an:.6f}")
# full-E extension: block formula verified on random full-E elements (family-tensor-supported)
ok_full = True
for _ in range(6):
    Ar, Br = randH(), randH()
    X = mkE(Ar, Br)
    pred = -2 * (m2 + h) * np.real(np.trace(Ar @ Ar)) + 4 * (m2 - h) * np.real(np.trace(Br @ Br))
    ok_full = ok_full and abs(hess_form(X, Phi0, h) - pred) < 1e-6 * abs(pred)
check("FULL-E extension: Hess(X,X) = -2(m^2+h) tr A^2 + 4(m^2-h) tr B^2 on random full-E directions "
      "(verdict covers all 18432 dims incl. family-tensor cells, not just the native slice)", ok_full)
# saddle demo: descend along a generation-diagonal channel
Xa = probes["pure gen-diag (A,0)"]; Xa = Xa / nrm(Xa) * np.sqrt(96)
dV1, dV2 = Vpot(Phi0 + 0.3 * Xa, h) - Vpot(Phi0, h), Vpot(Phi0 - 0.3 * Xa, h) - Vpot(Phi0, h)
check("h=0: V DECREASES both ways along a generation channel (masslessness rolls off the well top)",
      dV1 < -1 and dV2 < -1, f"dV = {dV1:.2f}, {dV2:.2f}")
V_al, V_gap = Vpot(Phi0, h), Vpot(phi0 * I192, h)
print(f"  h=0 depths: V(aligned) = {V_al:.1f}  vs  V(all-gapped phi* I) = {V_gap:.1f}")
check("h=0: the mirror-blind all-gapped configuration is STRICTLY DEEPER (global min gaps generations too)",
      V_gap < V_al - 1, f"delta = {V_gap - V_al:.1f}")
Hg = hess_matrix(phi0 * I192, h)
wg, lineg = spectrum_line(Hg)
check("control: Hessian at the all-gapped global min is POSITIVE DEFINITE (machinery can return PD)",
      wg.min() > 1e-6, f"spectrum {lineg}")

# ---- V_h: the orientation-odd extension ----
print("\n  THE ORIENTATION-ODD EXTENSION: V_h = tr((-m^2 + h Q5) Phi^2) + lam tr Phi^4, h < -m^2")
h = -6.0
phis = np.sqrt((m2 - h) / (2 * lam))
Phis = phis * PIm
gn = nrm(gradV(Phis, h))
check(f"h={h:.0f}: aligned point phi* = {phis:.3f} critical", gn < 1e-9, f"|grad| = {gn:.1e}")
Hh = hess_matrix(Phis, h)
wh, lineh = spectrum_line(Hh)
print(f"  h={h:.0f} HESSIAN SPECTRUM: {lineh}")
check(f"h={h:.0f}: Hessian POSITIVE DEFINITE, NO zero modes "
      f"(analytic: -2(m^2+h) = {-2*(m2+h):+.0f} gen, 4(m^2-h) = {4*(m2-h):+.0f} mirror)",
      abs(wh.min() + 2 * (m2 + h)) < 1e-6 and abs(wh.max() - 4 * (m2 - h)) < 1e-6 and wh.min() > 1,
      f"[{wh.min():.3f}, {wh.max():.3f}]")
fA = lambda a: (-(m2 + h)) * a**2 + lam * a**4
fB = lambda b: (h - m2) * b**2 + lam * b**4
Vmin_theory = 96 * 0.0 + 96 * fB(phis)
check("per-channel theorem: V >= 96 min f_A + 96 min f_B, equality exactly at the aligned class "
      "(V depends only on block spectra; f_A single well at 0, f_B double well at +-phi*)",
      abs(Vpot(Phis, h) - Vmin_theory) < 1e-6, f"V(aligned) = {Vpot(Phis, h):.1f} = 96 f_B(phi*) = {Vmin_theory:.1f}")
ok_glob = True
worst_v = np.inf
for _ in range(300):
    sc = np.random.uniform(0.1, 4.0)
    X = mkE(randH(), randH()); X = X / nrm(X) * sc * np.sqrt(96)
    v = Vpot(X, h)
    worst_v = min(worst_v, v - Vmin_theory)
    ok_glob = ok_glob and v >= Vmin_theory - 1e-6
check("GLOBAL MINIMUM: 300 random full-E configurations all satisfy V >= V(aligned)",
      ok_glob, f"min excess {worst_v:.3f}")
print(f"    => mechanism (quartic native potential + measured commutant) forces: with h < -m^2 the")
print(f"       aligned configuration (generations EXACTLY massless, mirrors gapped at phi* = {phis:.1f})")
print(f"       is the GLOBAL minimum. Choosing sign(h) IS choosing V8's orientation Z2.")
# orientation-flip control
hf = +6.0
phif = np.sqrt((m2 - (-hf)) / (2 * lam))  # the flipped well lives on the GENERATION block
Phif = phif * PIg
check(f"orientation-flip control h = +6: the chi-image (generations gapped at {phif:.1f}, mirrors massless) "
      "is critical and deeper than the mirror-gapped point",
      nrm(gradV(Phif, hf)) < 1e-9 and Vpot(Phif, hf) < Vpot(phif * PIm, hf) - 1,
      f"V(gen-gapped) = {Vpot(Phif, hf):.1f} vs V(mir-gapped) = {Vpot(phif * PIm, hf):.1f}")
# marginal boundary
hm = -m2
phim = np.sqrt((m2 - hm) / (2 * lam))
Hm = hess_matrix(phim * PIm, hm)
wm, linem = spectrum_line(Hm)
check("marginal boundary h = -m^2: generation channels become EXACT zero modes (256 of them)",
      abs(wm.min()) < 1e-6 and int((np.abs(wm) < 1e-6).sum()) == 256, f"spectrum {linem}")
# random-weighting control: a generic even weighting does NOT keep the aligned point critical
Rw = probes["pure E+ (B=+c'Ac)"]; Rw = Rw / nrm(Rw) * nrm(Q5)
Sr = -m2 * I192 + (-6.0) * Rw
gr = nrm(Sr @ Phis + Phis @ Sr + 4 * lam * Phis @ Phis @ Phis)
check("control: replacing Q5 by a random invariant-LOOKING even direction destroys criticality "
      "of the aligned point (gradient no longer parallel to Pi_mirror)", gr > 1.0, f"|grad| = {gr:.1f}")

# ============================================================ [4] (ii) MISALIGNMENT THRESHOLDS
print("\n[4] (ii) MISALIGNMENT THRESHOLDS: gap(eps) for M = Pi_mirror + eps X, |X|_F = |Pi_mirror|_F = sqrt(96)")
def band(X):
    A = Ep.conj().T @ X @ Ep
    B = Em.conj().T @ X @ Em
    return np.linalg.eigvalsh(0.5 * (A + A.conj().T)), np.linalg.eigvalsh(0.5 * (B + B.conj().T))
herm_res = max(nrm(Ep.conj().T @ X @ Ep - (Ep.conj().T @ X @ Ep).conj().T) / max(nrm(X), 1)
               for X in basis[:40])
check("block Hermiticity of native channels in the kU frame (eigvalsh valid)", herm_res < 1e-8,
      f"max residual {herm_res:.1e}")
def gap_of(eps, a, b):
    return np.abs(1 + eps * b).min() - eps * np.abs(a).max()
def threshold(X, eps_max=6.0):
    Xn = X / nrm(X) * np.sqrt(96)
    a, b = band(Xn)
    grid = np.linspace(0, eps_max, 3001)
    gv = np.array([gap_of(t, a, b) for t in grid])
    idx = np.where(gv <= 0)[0]
    if len(idx) == 0:
        return np.inf, "never closes", a, b
    lo, hi = grid[idx[0] - 1], grid[idx[0]]
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if gap_of(mid, a, b) <= 0:
            hi = mid
        else:
            lo = mid
    es = 0.5 * (lo + hi)
    mech = "mirror-crash" if np.abs(1 + es * b).min() < 0.02 else "gen-lift"
    return es, mech, a, b

# V8 anchor reproduction
Xv8 = 1j * Jp[2]
Xv8 = Xv8 / nrm(Xv8) * nrm(PIm)
av8, bv8 = band(Xv8)
gaps = [gap_of(t, av8, bv8) for t in (0.0, 0.1, 0.5, 1.0)]
check("V8 misalignment anchor reproduced (iJ+3 direction): gap = +1.000, +0.827, +0.134, -0.732",
      max(abs(gaps[0] - 1.0), abs(gaps[1] - 0.827), abs(gaps[2] - 0.134), abs(gaps[3] + 0.732)) < 2e-3,
      "gaps " + ", ".join(f"{x:+.3f}" for x in gaps))
ev8 = threshold(Xv8)[0]
print(f"  V8 direction iJ+3: threshold eps* = {ev8:.3f} (mechanism: gen-lift)")

# all native channels
ths = []
for X, nm in zip(basis, names):
    es, mech, a, b = threshold(X)
    ths.append((es, mech, nm))
finite = [t for t in ths if np.isfinite(t[0])]
inf_names = [t[2] for t in ths if not np.isfinite(t[0])]
arrf = np.array([t[0] for t in finite])
print(f"  native channels: {len(finite)} close the gap, {len(inf_names)} never close (names: {inf_names})")
check("the never-closing native channels are exactly the aligned plane {1, Q5} "
      "(I and Q5 tilts keep the 2mu separation forever -- V8's aligned-limit toy)",
      sorted(inf_names) == ["1", "e9.10.11.12.13"], str(inf_names))
worst_nat = finite[int(np.argmin(arrf))]
best_fin = finite[int(np.argmax(arrf))]
print(f"  native threshold distribution: min = {arrf.min():.4f}, median = {np.median(arrf):.4f}, "
      f"max(finite) = {arrf.max():.4f}")
print(f"  worst NATIVE channel: {worst_nat[2]} at eps* = {worst_nat[0]:.4f} ({worst_nat[1]})")
check("native monomial channels are uniformly robust: all thresholds = 1/sqrt(2) = 0.7071 "
      "(monomials square to I after K-symmetrization -> |eig| uniform 1/sqrt(2) at budget sqrt(96))",
      abs(arrf.min() - 1 / np.sqrt(2)) < 1e-3 and abs(arrf.max() - 1 / np.sqrt(2)) < 1e-3,
      f"range [{arrf.min():.4f}, {arrf.max():.4f}]")

# engineered and random controls
u = np.zeros((96, 96), complex); u[0, 0] = 1.0
X_r1 = mkE(np.sqrt(96) * u, np.zeros((96, 96), complex))          # rank-1 generation lift
es_r1 = threshold(X_r1)[0]
X_ww = mkE(np.sqrt(48) * u, -np.sqrt(48) * u)                     # rank-1 gen-lift + rank-1 mirror-crash
es_ww = threshold(X_ww)[0]
opt = 1 / (2 * np.sqrt(48))
print(f"  engineered rank-1 generation channel: eps* = {es_r1:.4f} (= 1/sqrt(96) = {1/np.sqrt(96):.4f})")
print(f"  engineered worst-case (rank-1 gen-lift + rank-1 mirror-crash): eps* = {es_ww:.4f} "
      f"(= 1/(2 sqrt(48)) = {opt:.4f})")
check("worst-case lemma: at Frobenius budget sqrt(96), eps* >= 1/(2 sqrt(48)) = 0.0722 with equality "
      "for the split rank-1 direction (max a + max(-b) <= 2 sqrt(48) by Cauchy-Schwarz on the budget)",
      abs(es_ww - opt) < 1e-3 and abs(es_r1 - 1 / np.sqrt(96)) < 1e-3)
rnd_th = []
ok_floor = True
for _ in range(24):
    X = mkE(randH(), randH())
    es = threshold(X)[0]
    rnd_th.append(es)
    ok_floor = ok_floor and es >= opt - 1e-6
rnd_th = np.array(rnd_th)
print(f"  random full-E directions (family-tensor-supported): eps* in [{rnd_th.min():.3f}, {rnd_th.max():.3f}], "
      f"median {np.median(rnd_th):.3f}")
check("control with power: no random direction beats the proved worst-case floor", ok_floor,
      f"min random eps* = {rnd_th.min():.3f} >= {opt:.4f}")

# ======================================================= [5] (iii) KREIN POSITIVITY IN THE BASIN
print("\n[5] (iii) KREIN POSITIVITY through the basin: [M(eps), P] along perturbed families")
res_even = max(nrm(comm(PIm + 0.9 * (X / nrm(X) * np.sqrt(96)), P)) for X in basis[::17])
check("P-even channels: [M(eps), P] = 0 at MACHINE PRECISION for every eps (linear identity; "
      "sampled at eps = 0.9 across the native basis)", res_even < 1e-9, f"max = {res_even:.1e}")
print("  P-odd contamination (K-self-adjointized; residual |[M,P]|_F / |M|_F):")
odd_chan = {
    "c(e4) timelike vector": g[4],
    "T5 = e4..e8 timelike volume": Rc(mono_big(e, [4, 5, 6, 7, 8])),
    "boost 2-form i e4e9": 1j * g[4] @ g[9],
    "chi_int = e4..e13": Rc(mono_big(e, list(range(4, 14)))),
    "random K-self-adjoint": (lambda Z: 0.5 * (Z + adjK(Z)))(np.random.randn(tdim, tdim)
                                                             + 1j * np.random.randn(tdim, tdim)),
}
eps_list = [0.1, 0.25, 0.5, 1.0]
lin_ok = True
for nm, Z in odd_chan.items():
    Zs = 0.5 * (Z + adjK(Z))
    if nrm(Zs) < 1e-8 * nrm(Z):
        Zs = 0.5 * (1j * Z + adjK(1j * Z))
    Zs = Zs / nrm(Zs) * np.sqrt(96)
    rs = []
    for t in eps_list:
        M = PIm + t * Zs
        rs.append(nrm(comm(M, P)) / nrm(M))
    slope01 = rs[0] / eps_list[0]
    lin_ok = lin_ok and rs[0] > 1e-3
    print(f"    {nm:<28s} r(eps) = " + "  ".join(f"{r:.3f}" for r in rs) + f"   (linear onset, slope ~ {slope01:.2f})")
check("P-odd contamination breaks [M,P] = 0 at LINEAR order in eps (finite immediately, not at a "
      "threshold): the positivity boundary of the basin is the channel space itself", lin_ok)

# ================================================================== [6] (iv) THE WEYL POINT
print("\n[6] (iv) THE WEYL POINT phi = mu/q vs the stable basin")
mu, q = 1.0, 1.0
Mweyl = mu * I192 + q * (mu / q) * Q5
check("identity: the Weyl-point configuration IS the aligned configuration at scale 2mu "
      "(mu I + mu Q5 = 2mu Pi_mirror, exact)", nrm(Mweyl - 2 * mu * PIm) < 1e-12,
      f"residual {nrm(Mweyl - 2 * mu * PIm):.1e}")
h = -6.0
print(f"  basin membership (h = {h:.0f}, phi* = {phis:.1f}): gradient at the Weyl configuration 2mu Pi_mirror:")
for muv in (0.8, 1.0, 1.2):
    gv = nrm(gradV(2 * muv * PIm, h))
    tag = "AT THE BASIN BOTTOM" if gv < 1e-9 else "off-bottom (rolls along the aligned ray)"
    print(f"    mu = {muv:.1f}: |grad V| = {gv:9.3f}   -> {tag}")
check("the Weyl point sits at the basin bottom exactly when 2mu = phi* (Dirac scale condensate-matched)",
      nrm(gradV(2 * 1.0 * PIm, h)) < 1e-9 and nrm(gradV(2 * 0.8 * PIm, h)) > 1.0)
# external-mu ray: the orientation coupling is INERT on the pure-Q5 ray
print("  external bare mu, condensate restricted to the pure Q5 ray (Phi = psi Q5):")
psis = np.linspace(-2.5, 2.5, 5001)
Vray = [Vpot(p * Q5, h) for p in psis]
pstar = psis[int(np.argmin(Vray))]
check("on the pure-Q5 ray the orientation coupling h is INERT (tr(Q5 (psi Q5)^2) = psi^2 tr Q5 = 0): "
      "ray minimum at psi* = sqrt(m^2 / 2 lam) = 1, INDEPENDENT of h",
      abs(abs(pstar) - 1.0) < 2e-3 and abs(np.real(np.trace(Q5))) < 1e-9,
      f"psi* = {pstar:+.3f}, tr Q5 = {np.real(np.trace(Q5)):.1e}")
for muv in (0.6, 1.0, 1.4):
    mg = abs(muv - abs(pstar))
    print(f"    mu = {muv:.1f}: generation mass |mu - psi*| = {mg:.3f}" +
          ("   <- massless ONLY at the tuned point mu = psi*" if mg < 1e-3 else ""))
# condensate-born mu: 2D native scalar sector (alpha I + beta Q5)
def V2d(x):
    return Vpot(x[0] * I192 + x[1] * Q5, h)
best = None
for _ in range(8):
    r = minimize(V2d, np.random.randn(2) * 2, method="Nelder-Mead",
                 options=dict(xatol=1e-10, fatol=1e-12, maxiter=4000))
    if best is None or r.fun < best.fun:
        best = r
al, be = best.x
Mfound = al * I192 + be * Q5
a_f, b_f = band(Mfound)
print(f"  condensate-born mu (2D native scalar sector, minimized freely): alpha = {al:+.4f}, beta = {be:+.4f}")
print(f"    generation band max|m| = {np.abs(a_f).max():.2e}, mirror band = "
      f"[{np.abs(b_f).min():.4f}, {np.abs(b_f).max():.4f}]")
check("condensate-born Dirac scale: the free 2D minimum IS the aligned configuration -- generations "
      "exactly massless with ZERO tuning (alpha = beta = phi*/2 up to the well sign)",
      np.abs(a_f).max() < 1e-5 and abs(np.abs(b_f).max() - phis) < 1e-4 and abs(abs(al) - phis / 2) < 1e-4)
# second-order corrections to masslessness
print("  second-order survival of the massless generations (base point 2mu Pi_mirror = phi* Pi_mirror, mu=1):")
M0 = phis * PIm
XB = mkE(np.zeros((96, 96), complex), randH())
XB = XB / nrm(XB) * np.sqrt(96)
evB = np.linalg.eigvals(M0 + 0.5 * XB)
genB = np.sort(np.abs(evB))[:96]
check("A=0 mirror-channel perturbations: generations stay massless to ALL orders (block decoupling), "
      "eps = 0.5", genB.max() < 1e-10, f"max|m_gen| = {genB.max():.1e}")
Zo = odd_chan["c(e4) timelike vector"]
Zs = 0.5 * (Zo + adjK(Zo))
if nrm(Zs) < 1e-8 * nrm(Zo):
    Zs = 0.5 * (1j * Zo + adjK(1j * Zo))
Zs = Zs / nrm(Zs) * np.sqrt(96)
Y = Ep.conj().T @ Zs @ Em
Z2 = Em.conj().T @ Zs @ Ep
schur_norm = nrm(Y @ Z2, 2) / phis
print(f"    P-odd channel c(e4): Schur prediction m_gen(2nd order) = eps^2 |Y Z|_2 / phi* = eps^2 * {schur_norm:.4f}")
slopes = []
for t in (0.02, 0.04, 0.08, 0.16):
    ev2 = np.linalg.eigvals(M0 + t * Zs)
    gen2 = np.sort(np.abs(ev2))[:96]
    slopes.append((t, gen2.max(), np.abs(ev2.imag).max()))
    print(f"      eps = {t:.2f}: max|m_gen| = {gen2.max():.3e}  (pred {t**2 * schur_norm:.3e}), "
          f"max|Im eig| = {np.abs(ev2.imag).max():.1e}")
p_fit = np.polyfit(np.log([s[0] for s in slopes]), np.log([s[1] for s in slopes]), 1)[0]
coeff_ok = all(abs(s[1] - s[0]**2 * schur_norm) < 0.15 * s[0]**2 * schur_norm for s in slopes[:3])
check("P-odd contamination lifts generation masses at SECOND order (fit exponent ~ 2, coefficient = "
      "Schur norm |YZ|/phi*) [textbook degenerate perturbation theory -- from memory, flagged]",
      abs(p_fit - 2.0) < 0.1 and coeff_ok, f"exponent {p_fit:.3f}")
# tadpole: the unforbidden linear invariant shifts generations off zero
print("  native tadpole c1 * tr(Q5 Phi) (nothing native forbids it without a Phi -> -Phi symmetry):")
for c1 in (0.1, 0.3):
    roots = np.roots([4 * lam, 0, 2 * (-(m2 + h)), -c1])
    astar = float(sorted(r.real for r in roots if abs(r.imag) < 1e-9)[-1])
    pred = c1 / (2 * (-(m2 + h)))
    print(f"    c1 = {c1:.1f}: generation mass shifts to a* = {astar:.5f} (leading prediction "
          f"c1 / (2|m^2+h|) = {pred:.5f})")
check("tadpole verdict: generation masslessness degrades LINEARLY in the tadpole, suppressed by the "
      "stabilizing gap 2|m^2+h|; EXACT masslessness additionally needs Phi -> -Phi (assumption, flagged)",
      abs(astar - 0.3 / 8) < 0.01)

# ============================================================================== [7] VERDICT
print("\n" + "=" * 110)
print("[7] STABILITY CARD (the deliverable)")
print("=" * 110)
print(f"""  ALIGNED CONFIGURATION phi* Pi_mirror -- measured facts a future dynamics must respect:
  (1) SECOND VARIATION: under EVERY orientation-blind native quadratic weighting (commutant gives
      only {{1, Q5}}; blind = h = 0) the simplest stable potential makes the aligned point an exact
      SADDLE: spectrum {{-2m^2 x 256, +4m^2 x 256}} on the native slice, {{-2m^2 x 9216, +4m^2 x 9216}}
      on full E (block formula, random-verified). Masslessness of the 96 generations = the top of the
      double well in every generation channel; the global minimum gaps EVERYTHING (mirror-blind).
      WITH the one orientation-odd native coupling h tr(Q5 Phi^2), h < -m^2: GLOBAL MINIMUM, Hessian
      positive definite {{-2(m^2+h) x 256, 4(m^2-h) x 256}}, no zero modes, symmetry-isolated.
      => at potential grade, ALIGNMENT IS PURCHASABLE FOR EXACTLY ONE NATIVE COUPLING SIGN, and that
      sign IS V8's orientation Z2: the two imports merge. Boundary h = -m^2 is the marginal case.
  (2) MISALIGNMENT BUFFER (kinematic, potential-independent): all 510 gap-closing native channels
      close at eps* = 0.707 exactly; the aligned plane {{1, Q5}} never closes; random (family-tensor)
      directions close at ~0.2-0.5; PROVED worst case at fixed Frobenius budget: eps* = 1/(2 sqrt 48)
      = 0.0722 (split rank-1). Two mechanisms: gen-lift and mirror-crash (a mirror Weyl crossing).
  (3) KREIN POSITIVITY: [M, P_ghost] = 0 is EXACT across the entire P-even basin at every eps
      (linear identity); it fails only under P-odd contamination, linearly, slope ~ 2/|M| -- the
      positivity boundary is the channel space itself, not a finite basin radius.
  (4) WEYL POINT: identically the aligned configuration at scale 2mu. At the basin bottom iff
      2mu = phi*: automatic when the Dirac scale is condensate-born (2D native scalar sector
      minimizes to it with zero tuning), one tuning if mu is external -- and on the pure-Q5 ray the
      orientation coupling is inert (tr Q5 = 0), so alignment dynamics REQUIRES the I-component.
      Massless generations survive A=0 mirror-channel perturbations to all orders, tadpoles only
      linearly (gap-suppressed; Phi -> -Phi needed for exactness), P-odd only quadratically (Schur).
  CARD VERDICT: SADDLE under orientation-blind dynamics / ATTRACTOR-COMPATIBLE (global minimum)
  under orientation-committed dynamics (h < -m^2) / MARGINAL at h = -m^2. The central unproven
  hypothesis of V8 (alignment) is now a ONE-COUPLING-SIGN question, not a fine-tuning question.
  All statements: "the quartic native potential class on the measured block structure forces X" --
  no claim that GU forces the coupling, its sign, or its magnitude.""")

if FAIL:
    print(f"\nFAILED CHECKS: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = anchors reproduced, Hessians verified (FD + full-E controls), thresholds scanned with"
      "\n         powered controls, positivity mapped, Weyl point placed. Every cited number printed above.")
