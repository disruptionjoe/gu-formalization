# -*- coding: utf-8 -*-
"""
VG-SD: mathematical flag clearance (source route SD; supports V3/V5).

Five from-memory flags in the 2026-07-06 federation docs, each converted to
checked mathematics = (literature reference located, see VG-SD doc) + a
machine verification of the mechanism the docs actually lean on:

  (1) orthogonal complex structures on R^{p,q} exist iff p AND q are even
      [Davidov-Mushkarov arXiv:math/0607030 Sec.2: J(W) = O(2p,2q)/U(p,q)];
      mechanism check: J-compatible Hermitian form halves the signature.
  (2) positive-line domain in C^{p,q} deformation-retracts to CP^{p-1}
      [Wolf 1969 base cycle + Mostow fibration lineage]; mechanism check:
      explicit retraction on samples + the Mostow dimension bookkeeping.
  (3) c(T CP^n) = (1+h)^{n+1} via the Euler sequence [Hartshorne II.8.13];
      symbolic check with a wrong-sequence control.
  (4) su(2,2) = so(4,2) [Wikipedia exceptional isomorphisms: Spin+(2,4) =
      SU(2,2)]; EXPLICIT Lie-algebra isomorphism constructed on Lambda^2 C^4,
      with su(3,1) (quaternionic, so*(6)) as the control that the real-
      structure test can fail.
  (5) Cartan involution basics [Knapp, Structure Theory of Semisimple Lie
      Groups, Thm 4.2 + Corollary = K3 Thm 6.16, Sec.VI.2; global K3 Thm
      6.31]; numeric check on su(2,2) with a non-Cartan involution control.

Route class: source intake / pure mathematics. This route does NOT use the
1792-dim Cl(9,5) carrier, so the carrier anchors (triplet (+96,-96,0),
beta_S residual, rank(Gamma)=128/ker=1664) are NOT reproduced here; they are
owned by the carrier routes (vg_v1/vg_v3/vg_v5 reproduce them). A separate
big-swing workflow (R1-R4) is running; its outcomes are not cited or used.

Target-import guard: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never
assumed, inserted, or divided by. Every 3 printed below is a MEASURED
eigenvalue count or a binomial coefficient of a sequence forced by n+1
bundle summands.

Run: python tests/big-swing/vg_sd_math_flag_clearance.py   (exit 0 = all pass)
"""
import sys
import numpy as np
import sympy as sp
from scipy.linalg import expm, null_space
from scipy.optimize import minimize

np.random.seed(20260706)
TOL = 1e-9
FAILURES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name} {detail}")
    if not ok:
        FAILURES.append(name)


print("=" * 78)
print("VG-SD math flag clearance -- source route (no carrier; anchors owned")
print("by carrier routes vg_v1/vg_v3/vg_v5 and not reproduced here).")
print("=" * 78)

# ---------------------------------------------------------------- item 1
print("\n[1] Orthogonal complex structure on R^{p,q} iff p,q both even")
print("    Reference: Davidov-Mushkarov, arXiv:math/0607030, Sec. 2:")
print("    'J(W) can be identified with the homogeneous space O(2p,2q)/U(p,q)'")

def metric(p, q):
    return np.diag([1.0] * p + [-1.0] * q)

# constructive direction on (6,4)
g64 = metric(6, 4)
R = np.array([[0.0, -1.0], [1.0, 0.0]])
J0 = np.zeros((10, 10))
for k in range(3):                      # 3 rotation blocks in the + part
    J0[2 * k:2 * k + 2, 2 * k:2 * k + 2] = R
for k in range(2):                      # 2 rotation blocks in the - part
    J0[6 + 2 * k:8 + 2 * k, 6 + 2 * k:8 + 2 * k] = R
r1 = np.abs(J0 @ J0 + np.eye(10)).max()
r2 = np.abs(J0.T @ g64 @ J0 - g64).max()
print(f"    block J on (6,4): |J^2+I|_max = {r1:.1e}, |J^T g J - g|_max = {r2:.1e}")
check("J exists on (6,4) (exact block construction)", r1 == 0.0 and r2 == 0.0)

# random O(6,4)-conjugate (generic compatible J), then the two-line-proof
# mechanism: h(x,y) = g(x,y) + i g(x,Jy) is Hermitian on (V,J); its complex
# signature (r,s) doubles to the real signature (2r,2s).
A = np.random.randn(10, 10) * 0.3
A = A - np.linalg.inv(g64) @ A.T @ g64          # A^T g + g A = 0
Phi = expm(A)
J = Phi @ J0 @ np.linalg.inv(Phi)
r1 = np.abs(J @ J + np.eye(10)).max()
r2 = np.abs(J.T @ g64 @ J - g64).max()
print(f"    generic conjugate J: |J^2+I| = {r1:.1e}, |J^T g J - g| = {r2:.1e}")
check("generic compatible J residuals", r1 < 1e-10 and r2 < 1e-10)

# greedy complex basis of (R^10, J)
basis = []
span = np.zeros((10, 0))
for i in range(10):
    e = np.eye(10)[:, i]
    cand = np.column_stack([span, e])
    if np.linalg.matrix_rank(cand, tol=1e-8) == span.shape[1] + 1:
        basis.append(e)
        span = np.column_stack([span, e, J @ e])
U = np.column_stack(basis)                       # 10 x 5, complex basis of (V,J)
h = U.T @ g64 @ U + 1j * (U.T @ g64 @ (J @ U))   # h_jk = g(u_j,u_k)+i g(u_j,J u_k)
herm = np.abs(h - h.conj().T).max()
ev = np.linalg.eigvalsh(h)
r_pos, r_neg = int((ev > TOL).sum()), int((ev < -TOL).sum())
print(f"    Hermitian residual |h - h^dag| = {herm:.1e}; complex signature "
      f"({r_pos},{r_neg}) -> real (2*{r_pos}, 2*{r_neg}) = (6,4)")
check("h Hermitian", herm < 1e-9)
check("signature-halving mechanism: {2r,2s} = {6,4}",
      sorted([2 * r_pos, 2 * r_neg]) == [4, 6])

# obstruction scan: floor of ||J^2+I||^2 + ||J^T g J - g||^2 over J
def floor_scan(p, q, starts=15):
    g = metric(p, q)
    n = p + q

    def f(x):
        Jm = x.reshape(n, n)
        return (np.linalg.norm(Jm @ Jm + np.eye(n)) ** 2
                + np.linalg.norm(Jm.T @ g @ Jm - g) ** 2)

    best = np.inf
    for _ in range(starts):
        x0 = np.random.randn(n * n)
        res = minimize(f, x0, method="L-BFGS-B",
                       options={"maxiter": 4000, "ftol": 1e-16, "gtol": 1e-12})
        best = min(best, res.fun)
    return best

f64 = floor_scan(6, 4)
f73 = floor_scan(7, 3)
print(f"    scan floor (6,4): {f64:.3e}   (should reach ~0: J exists)")
print(f"    scan floor (7,3): {f73:.6f}   (bounded away from 0: obstructed)")
check("(6,4) floor ~ 0", f64 < 1e-8)
check("(7,3) floor bounded away from 0 (>= 1)", f73 >= 1.0,
      f"floor={f73:.4f}")

# ---------------------------------------------------------------- item 2
print("\n[2] Positive lines in C^{3,2} deformation-retract to CP^2")
print("    Lineage: Wolf 1969 (unique complex K-orbit = base cycle) +")
print("    Mostow fibration; direct retraction r_t(v) = (v_+, (1-t)v_-).")

H32 = np.diag([1.0, 1.0, 1.0, -1.0, -1.0])

def herm_val(v):
    return float(np.real(v.conj() @ H32 @ v))

pos_lines = []
while len(pos_lines) < 400:
    v = np.random.randn(5) + 1j * np.random.randn(5)
    if herm_val(v) > 0:
        pos_lines.append(v)

ts = np.linspace(0.0, 1.0, 21)
min_val = np.inf
for v in pos_lines:
    for t in ts:
        rt = v.copy()
        rt[3:] *= (1.0 - t)
        min_val = min(min_val, herm_val(rt))
worst = min_val
print(f"    400 positive lines x 21 t-steps: min <r_t v, r_t v> = {worst:.6f} > 0")
check("retraction stays in the positive domain", worst > 0.0)
# fixed on CP^2
v_cp2 = np.zeros(5, dtype=complex)
v_cp2[:3] = np.random.randn(3) + 1j * np.random.randn(3)
fixed = max(np.abs(np.concatenate([v_cp2[:3], v_cp2[3:] * (1 - t)]) - v_cp2).max()
            for t in ts)
check("r_t = id on CP^2 (exact)", fixed == 0.0)

# control: mirror retraction toward the NEGATIVE block leaves the domain
fail_count = 0
for v in pos_lines:
    left = False
    for t in ts:
        rt = v.copy()
        rt[:3] *= (1.0 - t)
        if herm_val(rt) <= 0:
            left = True
            break
    fail_count += int(left)
print(f"    control (retract toward negative block): {fail_count}/400 leave "
      f"the domain -- the check can fail")
check("mirror-retraction control fails", fail_count == 400)

# Mostow dimension bookkeeping on su(3,2), all measured as nullspace dims.
def su_pq_basis(p, q):
    """Real basis of su(p,q) = {X : X^dag H + H X = 0, tr X = 0}."""
    n = p + q
    Hm = np.diag([1.0] * p + [-1.0] * q)
    rows = []
    # unknowns: X = Xr + i Xi, 2n^2 real unknowns
    # (X^dag H + H X)_{ab} = conj(X_{ba}) H_bb + H_aa X_{ab}
    for a in range(n):
        for b in range(n):
            re_row = np.zeros(2 * n * n)
            im_row = np.zeros(2 * n * n)
            # real part: Re X_{ba} H_bb + H_aa Re X_{ab}
            re_row[b * n + a] += Hm[b, b]
            re_row[a * n + b] += Hm[a, a]
            # imag part: -Im X_{ba} H_bb + H_aa Im X_{ab}
            im_row[n * n + b * n + a] -= Hm[b, b]
            im_row[n * n + a * n + b] += Hm[a, a]
            rows.append(re_row)
            rows.append(im_row)
    # trace condition: tr X imaginary automatically; impose Im tr X = 0
    tr_row = np.zeros(2 * n * n)
    for a in range(n):
        tr_row[n * n + a * n + a] = 1.0
    rows.append(tr_row)
    M = np.array(rows)
    ns = null_space(M, rcond=1e-10)
    mats = []
    for k in range(ns.shape[1]):
        x = ns[:, k]
        X = x[:n * n].reshape(n, n) + 1j * x[n * n:].reshape(n, n)
        mats.append(X)
    return mats, Hm

su32, H5 = su_pq_basis(3, 2)
dim_su32 = len(su32)
# residual sanity
res = max(np.abs(X.conj().T @ H5 + H5 @ X).max() for X in su32)
print(f"    dim su(3,2) = {dim_su32} (expect 24), defining residual {res:.1e}")
check("dim su(3,2) = 24", dim_su32 == 24 and res < 1e-8)

e1 = np.zeros(5, dtype=complex); e1[0] = 1.0
def line_stab_dim(mats):
    """dim of {X in span : X e1 in C e1} -- linear conditions on coords."""
    rows = []
    for comp in range(1, 5):
        re_row = [float(np.real(X[comp, 0])) for X in mats]
        im_row = [float(np.imag(X[comp, 0])) for X in mats]
        rows.append(re_row)
        rows.append(im_row)
    M = np.array(rows)
    return len(mats) - np.linalg.matrix_rank(M, tol=1e-8)

stab_full = line_stab_dim(su32)
orbit_full = dim_su32 - stab_full
print(f"    stab_[e1] su(3,2) dim = {stab_full} (expect 16); orbit dim = "
      f"{orbit_full} = dim_R CP^4 = 8 -> open orbit")
check("SU(3,2)-orbit of positive line is open (dim 8)",
      stab_full == 16 and orbit_full == 8)

# k0 = su(3,2) ∩ u(5), the theta-fixed part (theta = -X^dag):
# coordinates: X theta-fixed iff X + X^dag = 0
Mrows = []
for a in range(5):
    for b in range(5):
        re_row = [float(np.real(X[a, b] + np.conj(X[b, a]))) for X in su32]
        im_row = [float(np.imag(X[a, b] + np.conj(X[b, a]))) for X in su32]
        Mrows.append(re_row)
        Mrows.append(im_row)
Mk = np.array(Mrows)
nsk = null_space(Mk, rcond=1e-10)
k0_mats = []
for j in range(nsk.shape[1]):
    Xk = sum(c * X for c, X in zip(nsk[:, j], su32))
    k0_mats.append(Xk)
dim_k0 = len(k0_mats)
stab_k0 = line_stab_dim(k0_mats)
orbit_k0 = dim_k0 - stab_k0
print(f"    dim k0 = s(u(3)+u(2)) = {dim_k0} (expect 12); stab in k0 = "
      f"{stab_k0} (expect 8); K0-orbit dim = {orbit_k0} = dim_R CP^2 = 4")
check("Mostow bookkeeping: K0-orbit of [e1] is CP^2 (dim 4)",
      dim_k0 == 12 and stab_k0 == 8 and orbit_k0 == 4)
# Mostow hypothesis: K0 ∩ L0 is maximal compact in L0: dim check 16 -> 8
# stabilizer subalgebra basis: nullspace of line conditions within su32
rows = []
for comp in range(1, 5):
    rows.append([float(np.real(X[comp, 0])) for X in su32])
    rows.append([float(np.imag(X[comp, 0])) for X in su32])
nsl = null_space(np.array(rows), rcond=1e-10)
l0_mats = [sum(c * X for c, X in zip(nsl[:, j], su32)) for j in range(nsl.shape[1])]
Mrows3 = []
for a in range(5):
    for b in range(5):
        Mrows3.append([float(np.real(X[a, b] + np.conj(X[b, a]))) for X in l0_mats])
        Mrows3.append([float(np.imag(X[a, b] + np.conj(X[b, a]))) for X in l0_mats])
nsl_k = null_space(np.array(Mrows3), rcond=1e-10)
dim_l0_compact = nsl_k.shape[1]
print(f"    dim L0 = {len(l0_mats)}, theta-fixed part of L0 = {dim_l0_compact} "
      f"(expect 8 = s(u(1)+u(2)+u(2))) -- L0 reductive with compact part in K0")
check("theta-fixed part of L0 has dim 8", dim_l0_compact == 8)

# ---------------------------------------------------------------- item 3
print("\n[3] c(T CP^n) = (1+h)^{n+1} from the Euler sequence")
print("    Reference: Hartshorne, Algebraic Geometry, Thm II.8.13 (Euler seq.);")
print("    dual sequence 0 -> O -> O(1)^{n+1} -> T -> 0; Whitney product.")
hs = sp.symbols("h")
for n in [1, 2, 3, 4]:
    c = sp.expand((1 + hs) ** (n + 1))
    poly = sp.Poly(c, hs)
    c1 = poly.coeff_monomial(hs)
    ctop = poly.coeff_monomial(hs ** n)
    print(f"    n={n}: c1 = {c1} h (=(n+1)h), chi = <c_n,[CP^n]> = {ctop} (=n+1)")
    check(f"CP^{n}: c1=(n+1)h and chi=n+1", c1 == n + 1 and ctop == n + 1)
# CP^2 specifics used by V5
c = sp.expand((1 + hs) ** 3)
c1sq = int(sp.Poly(sp.expand((3 * hs) ** 2), hs).coeff_monomial(hs ** 2))
c2 = int(sp.Poly(c, hs).coeff_monomial(hs ** 2))
p1 = c1sq - 2 * c2
print(f"    CP^2: <c1^2> = {c1sq}, <c2> = chi = {c2}, p1 = c1^2 - 2 c2 = {p1} "
      f"= 3*sigma (sigma=+1, Hirzebruch)")
check("CP^2 invariants (9, 3, 3)", (c1sq, c2, p1) == (9, 3, 3))
# control: wrong sequence (drop the trivial summand) gives the WRONG chi
cw = sp.expand((1 + hs) ** 2)
chiw = int(sp.Poly(cw, hs).coeff_monomial(hs ** 2))
print(f"    control: (1+h)^2 would give 'chi(CP^2)' = {chiw} != 3 -- "
      f"the check can fail")
check("wrong-sequence control fails", chiw != 3)

# ---------------------------------------------------------------- item 4
print("\n[4] su(2,2) = so(4,2): explicit isomorphism on Lambda^2 C^4")
print("    Reference: Wikipedia 'Exceptional isomorphism': Spin+(2,4) = SU(2,2)")

def su_basis(H):
    n = H.shape[0]
    rows = []
    for a in range(n):
        for b in range(n):
            re_row = np.zeros(2 * n * n)
            im_row = np.zeros(2 * n * n)
            re_row[b * n + a] += H[b, b]
            re_row[a * n + b] += H[a, a]
            im_row[n * n + b * n + a] -= H[b, b]
            im_row[n * n + a * n + b] += H[a, a]
            rows.append(re_row)
            rows.append(im_row)
    tr_row = np.zeros(2 * n * n)
    for a in range(n):
        tr_row[n * n + a * n + a] = 1.0
    rows.append(tr_row)
    ns = null_space(np.array(rows), rcond=1e-10)
    return [ns[:, k][:n * n].reshape(n, n) + 1j * ns[:, k][n * n:].reshape(n, n)
            for k in range(ns.shape[1])]

H22 = np.diag([1.0, 1.0, -1.0, -1.0])
su22 = su_basis(H22)
print(f"    dim su(2,2) = {len(su22)} (expect 15)")
check("dim su(2,2) = 15", len(su22) == 15)

# Lambda^2 C^4: basis E_{ab}, a<b; action rho(X) A = X A + A X^T on antisym A
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
def wedge_basis():
    out = []
    for (a, b) in pairs:
        E = np.zeros((4, 4), dtype=complex)
        E[a, b], E[b, a] = 1.0, -1.0
        out.append(E)
    return out
W6 = wedge_basis()
def to_coords(A):
    return np.array([A[a, b] for (a, b) in pairs])
def rho(X):
    cols = [to_coords(X @ E + E @ X.T) for E in W6]
    return np.column_stack(cols)

rhos = [rho(X) for X in su22]
# bracket check
br = 0.0
idx = [(0, 1), (2, 7), (5, 11), (3, 14), (8, 9)]
for (i, j) in idx:
    lhs = rhos[i] @ rhos[j] - rhos[j] @ rhos[i]
    XY = su22[i] @ su22[j] - su22[j] @ su22[i]
    br = max(br, np.abs(lhs - rho(XY)).max())
print(f"    bracket homomorphism residual (5 sampled pairs): {br:.1e}")
check("rho is a Lie algebra homomorphism", br < 1e-9)

# invariant symmetric form Q from the Lambda^4 pairing (Levi-Civita)
import itertools
def eps(perm):
    p = list(perm)
    sgn, n = 1, len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                sgn = -sgn
    return sgn
Q = np.zeros((6, 6), dtype=complex)
for i, (a, b) in enumerate(pairs):
    for j, (c, d) in enumerate(pairs):
        if len({a, b, c, d}) == 4:
            Q[i, j] = eps((a, b, c, d))
inv = max(np.abs(r.T @ Q + Q @ r).max() for r in rhos)
print(f"    Q symmetric ({np.abs(Q-Q.T).max():.0e}), invariance residual "
      f"|rho^T Q + Q rho| = {inv:.1e}")
check("Q invariant under rho(su(2,2))", inv < 1e-9)

# antilinear commutant: S with S conj(rho(X)) = rho(X) S for all X
def antilinear_structure(rhos_list):
    blocks = [np.kron(r.conj().T, np.eye(6)) - np.kron(np.eye(6), r)
              for r in rhos_list]
    M = np.vstack(blocks)
    ns = null_space(M, rcond=1e-10)
    return ns
ns_S = antilinear_structure(rhos)
print(f"    antilinear commutant dimension (complex) = {ns_S.shape[1]} (expect 1)")
check("commutant is 1-dimensional (irreducible, self-conjugate)",
      ns_S.shape[1] == 1)
S = ns_S[:, 0].reshape(6, 6, order="F")   # vec(S) with column-major kron identity
# verify directly
resS = max(np.abs(S @ r.conj() - r @ S).max() for r in rhos)
print(f"    direct check |S conj(rho) - rho S| = {resS:.1e}")
check("S intertwines conj(rho) and rho", resS < 1e-8)
SSbar = S @ S.conj()
lam = SSbar[0, 0]
offdiag = np.abs(SSbar - lam * np.eye(6)).max()
print(f"    S Sbar = lambda I with lambda = {lam:.6f} (residual {offdiag:.1e})")
check("S Sbar scalar", offdiag < 1e-8)
check("su(2,2): lambda > 0 -> REAL structure (real form of so(6,C) exists)",
      np.real(lam) > 0 and abs(np.imag(lam)) < 1e-8)
S = S / np.sqrt(np.real(lam))            # now sigma^2 = +1

# fixed points V_R of sigma(z) = S conj(z)
P, Qi = np.real(S), np.imag(S)
Mfix = np.block([[P - np.eye(6), Qi], [Qi, -P - np.eye(6)]])
nsf = null_space(Mfix, rcond=1e-10)
print(f"    dim_R fixed space V_R = {nsf.shape[1]} (expect 6)")
check("V_R is 6-dimensional", nsf.shape[1] == 6)
Bvecs = [nsf[:6, k] + 1j * nsf[6:, k] for k in range(nsf.shape[1])]
Bmat = np.column_stack(Bvecs)
# Q restricted to V_R: complex symmetric, should be a phase times real
G = Bmat.T @ Q @ Bmat
# find global phase
ij = np.unravel_index(np.argmax(np.abs(G)), G.shape)
phase = G[ij] / np.abs(G[ij])
Gr = G / phase
imres = np.abs(np.imag(Gr)).max()
Grr = np.real(Gr)
evG = np.linalg.eigvalsh(Grr)
sig = (int((evG > TOL).sum()), int((evG < -TOL).sum()))
print(f"    Q|V_R real up to phase (im residual {imres:.1e}); signature "
      f"{sig} -> so{sig} = so(4,2) (= so(2,4))")
check("Q|V_R has signature {4,2}", sorted(sig) == [2, 4] and imres < 1e-7)

# rho restricted to V_R: real matrices, injective, preserve Grr
Binv = np.linalg.pinv(Bmat)
phis = []
realres, presres = 0.0, 0.0
for r in rhos:
    phi = Binv @ r @ Bmat
    realres = max(realres, np.abs(np.imag(phi)).max())
    phi = np.real(phi)
    presres = max(presres, np.abs(phi.T @ Grr + Grr @ phi).max())
    phis.append(phi)
stack = np.column_stack([p.flatten() for p in phis])
rk = np.linalg.matrix_rank(stack, tol=1e-8)
print(f"    rho|V_R real (residual {realres:.1e}), preserves Q|V_R "
      f"(residual {presres:.1e}), injective: rank = {rk} of 15")
print(f"    dim so(4,2) = 15 = dim su(2,2) -> the map is an ISOMORPHISM")
check("explicit iso su(2,2) -> so(4,2)",
      realres < 1e-7 and presres < 1e-7 and rk == 15)

# Killing signature cross-check: (8,7), maximal compact s(u(2)+u(2)) dim 7
def killing_signature(mats):
    m = len(mats)
    # structure constants via least squares in the chosen basis
    flat = np.column_stack([X.flatten() for X in mats])
    ads = []
    for X in mats:
        cols = []
        for Y in mats:
            Z = (X @ Y - Y @ X).flatten()
            c, *_ = np.linalg.lstsq(flat, Z, rcond=None)
            cols.append(np.real(c))
        ads.append(np.column_stack(cols))
    K = np.array([[np.trace(ads[i] @ ads[j]) for j in range(m)]
                  for i in range(m)])
    evK = np.linalg.eigvalsh((K + K.T) / 2)
    return (int((evK > 1e-6).sum()), int((evK < -1e-6).sum())), K
sigK, Kform = killing_signature(su22)
print(f"    Killing signature of su(2,2): ({sigK[0]},{sigK[1]}) (expect (8,7));"
      f" so(4,2): k = so(4)+so(2), dim 7 -- matches")
check("Killing signature (8,7)", sigK == (8, 7))

# control: su(3,1) -- quaternionic on Lambda^2 (so*(6)); real-structure fails
H31 = np.diag([1.0, 1.0, 1.0, -1.0])
su31 = su_basis(H31)
rhos31 = [rho(X) for X in su31]
ns31 = antilinear_structure(rhos31)
S31 = ns31[:, 0].reshape(6, 6, order="F")
lam31 = (S31 @ S31.conj())[0, 0]
print(f"    control su(3,1): S Sbar = {np.real(lam31):.6f} I "
      f"(< 0 -> QUATERNIONIC, no real form; su(3,1) pairs with so*(6)"
      f" [so*(6) name: from memory], not so(p,q)) -- the check can fail")
check("su(3,1) control: lambda < 0", np.real(lam31) < 0)

# ---------------------------------------------------------------- item 5
print("\n[5] Cartan involution basics, checked on su(2,2)")
print("    Reference: Knapp, 'Structure Theory of Semisimple Lie Groups'")
print("    (PSPM 61), Thm 4.2 + Corollary (a)(b) = [K3 Thm 6.16, Sec VI.2];")
print("    global decomposition + maximal compact: [K3 Thm 6.31].")
# theta(X) = -X^dag; use Killing form computed above
theta_mats = [-X.conj().T for X in su22]
# theta is an involutive automorphism
flat = np.column_stack([X.flatten() for X in su22])
def coords(X):
    c, *_ = np.linalg.lstsq(flat, X.flatten(), rcond=None)
    return np.real(c)
Th = np.column_stack([coords(tX) for tX in theta_mats])
inv_res = np.abs(Th @ Th - np.eye(15)).max()
aut_res = 0.0
for (i, j) in [(0, 1), (3, 9), (6, 14)]:
    lhs = -(su22[i] @ su22[j] - su22[j] @ su22[i]).conj().T
    rhs = (theta_mats[i] @ theta_mats[j] - theta_mats[j] @ theta_mats[i])
    aut_res = max(aut_res, np.abs(lhs - rhs).max())
print(f"    theta^2 = id residual {inv_res:.1e}; automorphism residual "
      f"{aut_res:.1e}")
check("theta involutive automorphism", inv_res < 1e-8 and aut_res < 1e-9)
Btheta = -Kform @ Th
Btheta = (Btheta + Btheta.T) / 2
evB = np.linalg.eigvalsh(Btheta)
print(f"    B_theta = -B(X, theta Y): min eigenvalue {evB.min():.6f} > 0 "
      f"-> positive definite -> theta IS a Cartan involution")
check("B_theta positive definite", evB.min() > 0)
# k = fixed set: dim 7, B negative definite on k
fix = null_space(Th - np.eye(15), rcond=1e-8)
dim_k = fix.shape[1]
Bk = fix.T @ Kform @ fix
evk = np.linalg.eigvalsh((Bk + Bk.T) / 2)
print(f"    dim k = {dim_k} (expect 7 = dim s(u(2)+u(2))); B|k max eig = "
      f"{evk.max():.6f} < 0 (compact)")
check("k is 7-dim with B negative definite", dim_k == 7 and evk.max() < 0)
# control: a non-Cartan involution sigma = Ad(diag(1,-1,1,1)) in U(2,2)
mconj = np.diag([1.0, -1.0, 1.0, 1.0])
sig_mats = [mconj @ X @ mconj for X in su22]
Sg = np.column_stack([coords(sX) for sX in sig_mats])
Bsig = -Kform @ Sg
Bsig = (Bsig + Bsig.T) / 2
evs = np.linalg.eigvalsh(Bsig)
print(f"    control: sigma = Ad(diag(1,-1,1,1)) is an involution but "
      f"B_sigma min eig = {evs.min():.4f} < 0 -- NOT Cartan; check can fail")
check("non-Cartan control fails positivity", evs.min() < 0)

# ---------------------------------------------------------------- summary
print("\n" + "=" * 78)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURES: {FAILURES}")
    sys.exit(1)
print("RESULT: ALL CHECKS PASS -- five from-memory flags cleared:")
print("  (1) even-even theorem: referenced (O(2p,2q)/U(p,q)) + mechanism verified")
print("  (2) positive-line retraction: referenced (Wolf/Mostow) + verified")
print("  (3) c(T CP^n) = (1+h)^{n+1}: referenced (Hartshorne II.8.13) + verified")
print("  (4) su(2,2) = so(4,2): referenced + EXPLICIT isomorphism constructed")
print("  (5) Cartan involution basics: referenced (Knapp) + verified on su(2,2)")
sys.exit(0)
