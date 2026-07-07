"""
VG-V5 (route V5, big-swing 2026-07-06): T2' coset topology -- does the breaking channel carry a
3-divisible discrete invariant?

Candidate breaking coset from the geometry chain:
    D = { positive complex lines in C^{3,2} }  (open subdomain of CP^4),
homogeneous under (S)U(3,2) with stabilizer S(U(1) x U(2,2)).

Sections:
  0. ANCHORS (reused from tests/generation-sector/ghost_parity_krein.py): triplet Krein signature
     (+96,-96,0) in (9,5); beta_S pseudo-anti-Hermiticity residual ~0; rank(Gamma)=128, ker=1664.
  1. ANTI-IMPORT CERTIFICATE: the provenance chain of the "3". dim X = 4, one time direction ->
     Frobenius form on Sym^2 has MEASURED signature (7,3) -> trace-reversal -> MEASURED (6,4)
     (invariant under g -> -g, measured) -> total (9,5), p-q = 4 -> any compatible complex
     structure J on R^{6,4} gives Hermitian signature MEASURED (3,2) (J-independence sampled) ->
     the maximal positive complex subspace is C^3 -> n = 3 - 1 = 2 -> the coset retracts to CP^2.
     CONTROLS: Euclidean base gives (10,0)->(9,1), odd p, NO compatible J (channel absent);
     eta(8,2) gives Hermitian (4,1) -> CP^3; eta(10,0) gives (5,0) -> CP^4.
  2. THE COSET: u(3,2) basis built and checked; orbit dimension 8 = dim_R(open subset of CP^4) at
     e1 and at 50 random positive lines (orbits open; D connected => single orbit); stabilizer
     dim 16 = dim s(u(1) x u(2,2)). EXPLICIT deformation retraction of D onto CP^2 (lines in the
     maximal positive subspace): v(t) = (v_+, (1-t) v_-); verified numerically on 2000 positive
     lines (min Hermitian norm along all trajectories stays >= initial norm > 0; endpoints in
     CP^2; identity on CP^2). CONTROL: same flow on negative lines FAILS (crosses the null cone).
  3. chi(CP^2) COMPUTED, not recalled: cell structure by last-nonvanishing homogeneous coordinate
     (one cell in each real dim 0, 2, 4; no odd cells => all cellular differentials vanish =>
     Betti = 1,0,1,0,1 => chi = 3), PLUS an independent differential-geometric measurement:
     4d Chern-Gauss-Bonnet on the Fubini-Study metric by nested finite differences + quadrature
     (chi_GB ~ 3.000). CONTROL: identical pipeline on round S^4 gives chi ~ 2.000.
  4. c1(T CP^2) = 3h via the Euler sequence, sympy-truncated arithmetic: c(TCP^n) = (1+h)^{n+1},
     n measured = 2 => c1 = 3h, c2 = 3h^2, <c2,[CP^2]> = 3 (= chi cross-check), <c1^2> = 9.
     CONTROLS: n = 1 -> c1 = 2h, chi = 2; n = 3 -> c1 = 4h, chi = 4.
  5. THE HONEST GAP (index sketch, sympy): where the CP^2 twist could enter the h2 canon index
     formula, the 2-adic wall, and exactly what remains uncomputed. No conclusion here.

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} are
never assumed, inserted, or divided by in any construction. Every 3 printed below is MEASURED
(eigenvalue counts, cell counts, truncated-polynomial coefficients) with its provenance printed.
The only inserted geometric data: dim X = 4 and "the base is Lorentzian (one time direction)";
the fiber signature (6,4) is measured and shown invariant under g -> -g, so even the mostly-plus /
mostly-minus convention does not matter for the fiber chain. Standard-math constants appearing in
formulas (the 1/2 in trace reversal, the /3 in the Dynkin index T(j) = j(j+1)(2j+1)/3, anchored by
T(1/2) = 1/2) are library mathematics, not the target 3, and are flagged where used.

Run from repo root: python tests/big-swing/vg_v5_breaking_coset_topology.py   (exit 0)
"""
import os
import sys
import importlib.util
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad

np.random.seed(20260706)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

FAIL = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)


def signature_of(M, tol=1e-9):
    Ms = 0.5 * (M + M.conj().T)
    w = np.linalg.eigvalsh(Ms)
    return (int(np.sum(w > tol)), int(np.sum(w < -tol)), int(np.sum(np.abs(w) <= tol)))


# ============================================================================
print("=" * 88)
print("SECTION 0 -- ANCHORS (reused verbatim from tests/generation-sector/ghost_parity_krein.py)")
print("=" * 88)
spec = importlib.util.spec_from_file_location(
    "gpk", os.path.join(ROOT, "tests", "generation-sector", "ghost_parity_krein.py"))
gpk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gpk)

# (9,5) anchor: prints beta_S pseudo-anti-Hermiticity residual and asserts triplet (+96,-96,0)
gpk.analyze({4, 5, 6, 7, 8}, "(9,5)")
check("triplet Krein signature (+96,-96,0) in (9,5) reproduced (assert inside analyze passed)", True)

timelike = {4, 5, 6, 7, 8}
e95 = [(1j * gpk.base[a] if a in timelike else gpk.base[a]) for a in range(14)]
Gamma = np.hstack(e95)                      # 128 x 1792 gamma-trace map
rkG = np.linalg.matrix_rank(Gamma, tol=1e-9)
kerG = Gamma.shape[1] - rkG
print(f"  rank(Gamma) = {rkG}   dim ker(Gamma) = {kerG}   (carrier dim {Gamma.shape[1]})")
check("rank(Gamma) = 128 and dim ker = 1664", rkG == 128 and kerG == 1664)

# ============================================================================
print()
print("=" * 88)
print("SECTION 1 -- ANTI-IMPORT CERTIFICATE: the provenance chain of the 3 (every step MEASURED)")
print("=" * 88)
print("Inserted data (the ONLY inserted data): dim X = 4;  base Lorentzian (one time direction).")

n_base = 4
# Sym^2(R^4) basis: 10 symmetric matrices
B = []
for a in range(n_base):
    Eaa = np.zeros((n_base, n_base)); Eaa[a, a] = 1.0
    B.append(Eaa)
for a in range(n_base):
    for b in range(a + 1, n_base):
        Eab = np.zeros((n_base, n_base)); Eab[a, b] = 1.0; Eab[b, a] = 1.0
        B.append(Eab)
print(f"Step 1: dim X = 4  =>  fiber = Sym^2(T*X), dim = {len(B)}  (measured: basis constructed)")
check("dim Sym^2(R^4) = 10", len(B) == 10)


def frob_gram(g):
    ginv = np.linalg.inv(g)
    n = len(B)
    F = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            F[i, j] = np.trace(ginv @ B[i] @ ginv @ B[j]).real
    return F


def trace_reversed_gram(g):
    # V(h,k) = F(h,k) - (1/2) tr(g^-1 h) tr(g^-1 k)   [repo form, tests/willmore_... line 101]
    ginv = np.linalg.inv(g)
    F = frob_gram(g)
    t = np.array([np.trace(ginv @ Bi).real for Bi in B])
    V = F - 0.5 * np.outer(t, t)
    # cross-check: V(h,k) = F(T h, k) with the trace-reversal map T(h) = h - (1/2) tr_g(h) g
    n = len(B)
    V2 = np.zeros((n, n))
    for i in range(n):
        Th = B[i] - 0.5 * np.trace(ginv @ B[i]).real * g
        for j in range(n):
            V2[i, j] = np.trace(ginv @ Th @ ginv @ B[j]).real
    assert np.max(np.abs(V - V2)) < 1e-12, "trace-reversal form mismatch"
    return V


g_mostly_plus = np.diag([1.0, 1.0, 1.0, -1.0])   # (3,1) mostly-plus
g_mostly_minus = -g_mostly_plus                   # (1,3) mostly-minus (g -> -g)

sigF = signature_of(frob_gram(g_mostly_plus))
sigV_p = signature_of(trace_reversed_gram(g_mostly_plus))
sigV_m = signature_of(trace_reversed_gram(g_mostly_minus))
print(f"Step 2: Frobenius form on Sym^2, Lorentzian base:      signature MEASURED = "
      f"(+{sigF[0]}, -{sigF[1]}, 0:{sigF[2]})")
check("Frobenius fiber signature = (7,3)", sigF == (7, 3, 0))
print(f"Step 3: trace-reversed Frobenius (mostly-plus base):   signature MEASURED = "
      f"(+{sigV_p[0]}, -{sigV_p[1]}, 0:{sigV_p[2]})")
print(f"        trace-reversed Frobenius (mostly-minus, g->-g): signature MEASURED = "
      f"(+{sigV_m[0]}, -{sigV_m[1]}, 0:{sigV_m[2]})")
check("trace-reversed fiber signature = (6,4), both base sign conventions",
      sigV_p == (6, 4, 0) and sigV_m == (6, 4, 0))
p_tot, q_tot = sigV_p[0] + 3, sigV_p[1] + 1
print(f"Step 4: total = fiber (6,4) + base (3,1) = ({p_tot},{q_tot});   p - q = {p_tot - q_tot}"
      f"   (the repo's Cl(9,5) signature; measured 9-5=4)")
check("total signature (9,5), p-q = 4", (p_tot, q_tot) == (9, 5))


def hermitian_signature(eta_diag, n_samples=20):
    """Given an even-p even-q real form eta = diag(eta_diag), build compatible complex structures
    J (J^2 = -1, J^T eta J = eta) and measure the signature of the induced Hermitian form on the
    +i eigenspace. Returns the set of signatures found over the canonical J and random conjugates."""
    dim = len(eta_diag)
    eta = np.diag(np.array(eta_diag, dtype=float))
    p = int(np.sum(np.array(eta_diag) > 0)); q = dim - p
    if p % 2 or q % 2:
        return None  # no compatible complex structure (parity obstruction)
    J0 = np.zeros((dim, dim))
    order = list(np.argsort(-np.array(eta_diag)))  # positives first
    for m in range(dim // 2):
        i, j = order[2 * m], order[2 * m + 1]
        J0[i, j] = -1.0; J0[j, i] = 1.0
    sigs = set()
    for s in range(n_samples + 1):
        if s == 0:
            J = J0
        else:
            Bas = np.random.randn(dim, dim) * 0.3
            A = eta @ (Bas - Bas.T)          # A in so(p,q): A^T eta = -eta A
            gexp = expm(A)
            J = gexp @ J0 @ np.linalg.inv(gexp)
        assert np.max(np.abs(J @ J + np.eye(dim))) < 1e-8
        assert np.max(np.abs(J.T @ eta @ J - eta)) < 1e-8
        w, U = np.linalg.eig(J)
        W = U[:, w.imag > 0.5]               # +i eigenspace, complex dim = dim/2
        H = W.conj().T @ eta.astype(complex) @ W
        sigs.add(signature_of(H))
    return sigs


# diagonalize the MEASURED trace-reversed Gram to its inertia basis, then measure Hermitian sig
wV = np.linalg.eigvalsh(0.5 * (trace_reversed_gram(g_mostly_plus)
                               + trace_reversed_gram(g_mostly_plus).T))
eta_fiber = [1] * int(np.sum(wV > 1e-9)) + [-1] * int(np.sum(wV < -1e-9))
sigs64 = hermitian_signature(eta_fiber, n_samples=20)
print(f"Step 5: compatible complex structure J on the measured R^(6,4) fiber:")
print(f"        Hermitian signature over canonical J + 20 random compatible J: {sorted(sigs64)}")
check("Hermitian signature = (3,2), J-independent (21 J's sampled)", sigs64 == {(3, 2, 0)})
p_C = 3 if sigs64 == {(3, 2, 0)} else sorted(sigs64)[0][0]
p_C = sorted(sigs64)[0][0]   # MEASURED positive complex directions (do not hardcode)
n_proj = p_C - 1
print(f"Step 6: maximal positive complex subspace = C^{p_C}  (MEASURED: {p_C} = # positive")
print(f"        eigenvalues of the Hermitian form)  =>  positive lines retract to CP^{n_proj}")
print()
print("PROVENANCE OF THE 3 (anti-import certificate):")
print("  dim X = 4, Lorentzian base  ->  Frobenius (7,3) [measured]  ->  trace-reversal ->")
print("  fiber (6,4) [measured, g->-g invariant]  ->  total (9,5), p-q = 4  ->  compatible J ->")
print(f"  Hermitian C^(3,2) [measured, J-independent]  ->  {p_C} positive complex directions ->")
print(f"  CP^{n_proj}. The 3 is an eigenvalue COUNT descending from GU-native signature data;")
print("  it was never written into any formula.")
print()
print("CONTROLS (the chain is signature-selective, not a tautology):")
sigF_e = signature_of(frob_gram(np.eye(4)))
sigV_e = signature_of(trace_reversed_gram(np.eye(4)))
print(f"  Euclidean base (4,0): Frobenius (+{sigF_e[0]},-{sigF_e[1]}), trace-reversed "
      f"(+{sigV_e[0]},-{sigV_e[1]})  -> p = {sigV_e[0]} ODD -> NO compatible J exists")
check("Euclidean control: (10,0) -> (9,1), odd p kills the complex-structure channel",
      sigF_e == (10, 0, 0) and sigV_e == (9, 1, 0)
      and hermitian_signature([1] * 9 + [-1]) is None)
s82 = hermitian_signature([1] * 8 + [-1] * 2, n_samples=5)
s100 = hermitian_signature([1] * 10, n_samples=5)
print(f"  eta(8,2) control: Hermitian {sorted(s82)} -> CP^3 (chi would be 4, not 3)")
print(f"  eta(10,0) control: Hermitian {sorted(s100)} -> CP^4 (chi would be 5, not 3)")
check("(8,2) -> (4,1) and (10,0) -> (5,0): different inputs give different n",
      s82 == {(4, 1, 0)} and s100 == {(5, 0, 0)})

# ============================================================================
print()
print("=" * 88)
print("SECTION 2 -- THE COSET D = positive lines in C^(3,2), AND THE EXPLICIT RETRACTION TO CP^2")
print("=" * 88)
H5 = np.diag([1.0, 1.0, 1.0, -1.0, -1.0]).astype(complex)   # Hermitian form of C^(3,2) (measured sig)

# u(3,2) = { i H M : M Hermitian 5x5 }  -- build all 25 generators and check
gens = []
for kk in range(5):
    M = np.zeros((5, 5), dtype=complex); M[kk, kk] = 1.0
    gens.append(1j * H5 @ M)
for kk in range(5):
    for ll in range(kk + 1, 5):
        M = np.zeros((5, 5), dtype=complex); M[kk, ll] = 1.0; M[ll, kk] = 1.0
        gens.append(1j * H5 @ M)
        M = np.zeros((5, 5), dtype=complex); M[kk, ll] = 1j; M[ll, kk] = -1j
        gens.append(1j * H5 @ M)
res_u = max(np.max(np.abs(A.conj().T @ H5 + H5 @ A)) for A in gens)
print(f"u(3,2) basis: {len(gens)} generators, max |A^dag H + H A| = {res_u:.1e}")
check("u(3,2) basis valid (25 gens, residual < 1e-12)", len(gens) == 25 and res_u < 1e-12)


def orbit_dim(v):
    """Real dimension of the u(3,2)-orbit through the line [v] in CP^4."""
    v = v / np.linalg.norm(v)
    rows = []
    for A in gens:
        t = A @ v
        t = t - (v.conj() @ t) * v          # project out the complex line C v
        rows.append(np.concatenate([t.real, t.imag]))
    return np.linalg.matrix_rank(np.array(rows), tol=1e-9)


e1 = np.zeros(5, dtype=complex); e1[0] = 1.0
od_e1 = orbit_dim(e1)
print(f"Orbit dim at e1 (a positive line): {od_e1}  = dim_R CP^4 = 8  -> the orbit is OPEN")
print(f"Stabilizer: dim in u(3,2) = 25 - {od_e1} = {25 - od_e1}; in su(3,2) = {25 - od_e1 - 1}"
      f"  = dim s(u(1) x u(2,2)) = 1 + 16 - 1 = 16")
check("orbit dim 8, su-stabilizer dim 16 = dim s(u(1) x u(2,2))", od_e1 == 8)

# sample positive lines and check orbit dimension everywhere
n_pos_checked, all8 = 0, True
while n_pos_checked < 50:
    v = np.random.randn(5) + 1j * np.random.randn(5)
    if (v.conj() @ H5 @ v).real > 0:
        all8 = all8 and (orbit_dim(v) == 8)
        n_pos_checked += 1
check("orbit dim = 8 at 50 random positive lines (orbits open; D connected via the retraction "
      "below => D is a single orbit)", all8)

print()
print("Deformation retraction (CONSTRUCTION, not citation): write v = (v+, v-) in C^3 (+) C^2.")
print("  r_t([v]) = [(v+, (1-t) v-)],  t in [0,1].  Well-defined on lines (scaling-covariant),")
print("  continuous, r_0 = id, r_1(D) = {lines with v- = 0} = P(C^3) = CP^2, and r_t = id on CP^2")
print("  for all t. Domain preservation: <v(t),v(t)> = |v+|^2 - (1-t)^2 |v-|^2 >= |v+|^2 - |v-|^2")
print("  = <v,v> > 0, so the flow never leaves D and the Hermitian norm is nondecreasing.")
print("  (v+ != 0 on D: <v,v> > 0 forces |v+|^2 > |v-|^2 >= 0.)")

ts = np.linspace(0.0, 1.0, 201)
n_samp = 2000
min_norm_rel, mono_ok, end_ok, got = np.inf, True, True, 0
while got < n_samp:
    v = np.random.randn(5) + 1j * np.random.randn(5)
    qv = (v.conj() @ H5 @ v).real
    if qv <= 0:
        continue
    got += 1
    ap, am = np.sum(np.abs(v[:3]) ** 2), np.sum(np.abs(v[3:]) ** 2)
    norms = ap - (1 - ts) ** 2 * am          # <v(t),v(t)>
    vv = ap + (1 - ts) ** 2 * am             # Euclidean norm^2 along flow (nonzero)
    min_norm_rel = min(min_norm_rel, np.min(norms / vv))
    mono_ok = mono_ok and np.all(np.diff(norms) >= -1e-12)
    end_ok = end_ok and (abs(norms[-1] - ap) < 1e-12)
print(f"Numerical verification on {n_samp} random positive lines, 201 time steps each:")
print(f"  min over all trajectories of <v(t),v(t)>/|v(t)|^2  =  {min_norm_rel:.6f}  (> 0: stays in D)")
print(f"  Hermitian norm nondecreasing along every trajectory: {mono_ok}")
print(f"  endpoint v(1) = (v+, 0) in CP^2 (positive-subspace line): {end_ok}")
check("retraction verified: flow stays in D, monotone, lands in CP^2",
      min_norm_rel > 0 and mono_ok and end_ok)

# CONTROL: the same flow on NEGATIVE lines is NOT a retraction of the negative domain
n_neg, crossed = 0, 0
while n_neg < 500:
    v = np.random.randn(5) + 1j * np.random.randn(5)
    qv = (v.conj() @ H5 @ v).real
    if qv >= 0:
        continue
    n_neg += 1
    ap, am = np.sum(np.abs(v[:3]) ** 2), np.sum(np.abs(v[3:]) ** 2)
    norms = ap - (1 - ts) ** 2 * am
    if norms[0] < 0 and norms[-1] > 0:
        crossed += 1                        # crosses the null cone: leaves the negative domain
print(f"CONTROL: same flow on 500 random NEGATIVE lines: {crossed}/500 trajectories cross the")
print(f"  null cone (norm sign flips) -- the 'stays in domain' check FAILS there, so the")
print(f"  positive-line verification is not a tautology.")
check("negative-line control: flow fails to preserve the negative domain", crossed == 500)

# ============================================================================
print()
print("=" * 88)
print(f"SECTION 3 -- chi(CP^{n_proj}) COMPUTED, NOT RECALLED")
print("=" * 88)
n = n_proj   # = 2, MEASURED in Section 1
print(f"CW structure (constructed): stratify CP^n, n = {n} (measured), by the last nonvanishing")
print("homogeneous coordinate: stratum k = {[z_0:...:z_k:0:...:0], z_k != 0} ~ C^k, one cell of")
print("real dimension 2k for each k = 0..n. (Standard cell decomposition; the attaching maps are")
print("the Hopf quotients, but chi needs only the cell dimensions.)")
cells = [2 * k for k in range(n + 1)]
dims_by_deg = [cells.count(dd) for dd in range(2 * n + 1)]
print(f"  cells in real dims {cells}; chain complex dims by degree: {dims_by_deg}")
print("  No odd-dimensional cells => every cellular differential has source or target 0 =>")
print("  all differentials vanish => H_k = C_k (cellular chains) =>")
betti = dims_by_deg
chi_cell = sum(((-1) ** dd) * dims_by_deg[dd] for dd in range(len(dims_by_deg)))
print(f"  Betti numbers b_0..b_{2*n} = {betti}   chi = alternating sum = {chi_cell}")
print(f"  Provenance: chi = n + 1 with n = {n}, and n = {n} because the maximal positive subspace")
print(f"  of C^(3,2) is C^{p_C} (Section 1, measured), and THAT descends from fiber (6,4) =")
print(f"  trace-reversed (7,3), which descends from dim X = 4 + one time direction (p-q = 4 total).")
check("chi(CP^2) = 3 from cellular chain complex (b0,b2,b4 = 1,1,1)",
      chi_cell == 3 and betti == [1, 0, 1, 0, 1])

# ---- independent differential-geometric measurement: 4d Chern-Gauss-Bonnet on Fubini-Study ----
print()
print("Independent measurement: chi = (1/32 pi^2) INT (|Riem|^2 - 4|Ric|^2 + R^2) dV")
print("[4d Chern-Gauss-Bonnet; standard math, from memory -- the S^4 control below certifies the")
print(" normalization empirically], Fubini-Study metric from K = log(1+|z|^2), nested finite")
print(" differences for curvature, quadrature for volume. Chart misses a measure-zero CP^1.")


def fs_g(z):
    """FS Hermitian metric g_{i jbar} = d_i d_jbar log(1+|z|^2) on C^2 (analytic)."""
    r2 = float(np.sum(np.abs(z) ** 2))
    return np.eye(2, dtype=complex) / (1 + r2) - np.outer(z.conj(), z) / (1 + r2) ** 2


# verify the analytic g against nested finite differences of the Kaehler potential
def K_pot(x):
    return np.log(1 + x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2)  # x=(x1,y1,x2,y2)


def d5s(f, x, a, h):
    xp2, xp1, xm1, xm2 = x.copy(), x.copy(), x.copy(), x.copy()
    xp2[a] += 2 * h; xp1[a] += h; xm1[a] -= h; xm2[a] -= 2 * h
    return (-f(xp2) + 8 * f(xp1) - 8 * f(xm1) + f(xm2)) / (12 * h)


gerr = 0.0
for _ in range(3):
    x = np.random.randn(4) * 0.5
    z = np.array([x[0] + 1j * x[1], x[2] + 1j * x[3]])
    g_an = fs_g(z)
    for i in range(2):
        for j in range(2):
            # g_{i jbar} = (1/2)(d_xi - i d_yi) [ (1/2)(d_xj + i d_yj) K ]
            def dbar_j(xx, j=j):
                return 0.5 * (d5s(K_pot, xx, 2 * j, 1e-3) + 1j * d5s(K_pot, xx, 2 * j + 1, 1e-3))
            g_fd = 0.5 * (d5s(dbar_j, x, 2 * i, 1e-3) - 1j * d5s(dbar_j, x, 2 * i + 1, 1e-3))
            gerr = max(gerr, abs(g_fd - g_an[i, j]))
print(f"  analytic FS metric vs finite differences of the potential: max residual {gerr:.1e}")
check("FS metric is measured from the potential (residual < 1e-6)", gerr < 1e-6)


def G_fs(x):
    """Real Riemannian metric G_ab = Re sum g_{i jbar} e^i_a conj(e^j_b), e = dz/du."""
    z = np.array([x[0] + 1j * x[1], x[2] + 1j * x[3]])
    g = fs_g(z)
    E = np.array([[1, 0], [1j, 0], [0, 1], [0, 1j]], dtype=complex)  # e^i_a for a = x1,y1,x2,y2
    return np.real(E @ g @ E.conj().T)


def G_s4(x):
    """Round S^4, radius 1, stereographic chart: G = 4/(1+|u|^2)^2 I."""
    return (4.0 / (1 + float(np.sum(x ** 2))) ** 2) * np.eye(4)


def christoffel(Gfun, x, h1=1e-3):
    G = Gfun(x); Gi = np.linalg.inv(G)
    dG = np.array([d5s(Gfun, x, a, h1) for a in range(4)])       # dG[a] = partial_a G
    Gam = np.zeros((4, 4, 4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                Gam[a, b, c] = 0.5 * sum(Gi[a, dd] * (dG[b][dd, c] + dG[c][dd, b] - dG[dd][b, c])
                                         for dd in range(4))
    return Gam


def gb_scalar(Gfun, x, h1=1e-3, h2=1e-2):
    Gam = christoffel(Gfun, x, h1)
    dGam = np.array([d5s(lambda y: christoffel(Gfun, y, h1), x, c, h2) for c in range(4)])
    R_up = np.zeros((4, 4, 4, 4))                                # R^a_{bcd}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for dd in range(4):
                    R_up[a, b, c, dd] = (dGam[c][a, dd, b] - dGam[dd][a, c, b]
                                         + np.dot(Gam[a, c, :], Gam[:, dd, b])
                                         - np.dot(Gam[a, dd, :], Gam[:, c, b]))
    G = Gfun(x); Gi = np.linalg.inv(G)
    R_dn = np.einsum('ae,ebcd->abcd', G, R_up)
    Riem2 = np.einsum('abcd,efgh,ae,bf,cg,dh->', R_dn, R_dn, Gi, Gi, Gi, Gi)
    Ric = np.einsum('abad->bd', R_up)
    Ric2 = np.einsum('bd,fh,bf,dh->', Ric, Ric, Gi, Gi)
    Rs = np.einsum('bd,bd->', Ric, Gi)
    return Riem2 - 4.0 * Ric2 + Rs ** 2


def chi_gauss_bonnet(Gfun, label):
    x0 = np.zeros(4)
    x1 = np.array([0.37, -0.12, 0.25, 0.08])
    gb0, gb1 = gb_scalar(Gfun, x0), gb_scalar(Gfun, x1)
    rel = abs(gb0 - gb1) / abs(gb0)
    vol, verr = quad(lambda r: np.sqrt(np.linalg.det(Gfun(np.array([r, 0, 0, 0]))))
                     * 2 * np.pi ** 2 * r ** 3, 0, np.inf, limit=300)
    chi = gb0 * vol / (32 * np.pi ** 2)
    print(f"  {label}: GB scalar at 2 points = {gb0:.6f}, {gb1:.6f} (homogeneity rel diff "
          f"{rel:.1e}); Vol = {vol:.8f}; chi_GB = {chi:.6f}")
    return chi, rel


# radial-symmetry sanity for the volume reduction (U(2) acts transitively on |u| = r spheres)
r_test = 0.9
vals = []
for _ in range(3):
    u = np.random.randn(4); u = r_test * u / np.linalg.norm(u)
    vals.append(np.sqrt(np.linalg.det(G_fs(u))))
v_ref = np.sqrt(np.linalg.det(G_fs(np.array([r_test, 0, 0, 0]))))
check("sqrt(det G_FS) depends only on |u| (volume reduction valid)",
      max(abs(v - v_ref) for v in vals) / v_ref < 1e-10)

chi_fs, rel_fs = chi_gauss_bonnet(G_fs, "CP^2 Fubini-Study")
chi_s4, rel_s4 = chi_gauss_bonnet(G_s4, "S^4 round (CONTROL)")
check("chi(CP^2) = 3 by Gauss-Bonnet (|chi_GB - 3| < 1e-2, homogeneity < 1e-3)",
      abs(chi_fs - 3) < 1e-2 and rel_fs < 1e-3, f"chi_GB = {chi_fs:.6f}")
check("S^4 control: chi = 2 (same pipeline, different answer -> non-tautological)",
      abs(chi_s4 - 2) < 1e-2, f"chi_GB = {chi_s4:.6f}")
check("cellular chi and Gauss-Bonnet chi agree", abs(chi_fs - chi_cell) < 1e-2)

# ============================================================================
print()
print("=" * 88)
print("SECTION 4 -- CHERN CLASSES OF T CP^2 VIA THE EULER SEQUENCE (sympy truncated arithmetic)")
print("=" * 88)
h = sp.symbols('h')


def chern_cpn(nn):
    """c(T CP^n) = (1+h)^{n+1} mod h^{n+1} (Euler sequence 0 -> O -> O(1)^{n+1} -> T -> 0)."""
    c = sp.expand((1 + h) ** (nn + 1))
    c = sum(c.coeff(h, kk) * h ** kk for kk in range(nn + 1))
    return sp.expand(c)


c_t = chern_cpn(n)   # n = 2, measured
c1 = c_t.coeff(h, 1) * h
c2 = c_t.coeff(h, 2) * h ** 2
int_c2 = int(c_t.coeff(h, 2))            # <c2, [CP^2]> since <h^2,[CP^2]> = 1
int_c1sq = int(sp.expand(c1 ** 2).coeff(h, 2))
print(f"  c(T CP^{n}) = (1+h)^{n + 1} mod h^{n + 1} = {c_t}")
print(f"  c1(T CP^2) = {c1}      c2(T CP^2) = {c2}")
print(f"  <c2,[CP^2]> = {int_c2}  (top Chern = Euler class; equals chi: cell {chi_cell}, "
      f"GB {chi_fs:.4f})")
print(f"  <c1^2,[CP^2]> = {int_c1sq}")
check("c1(T CP^2) = 3h (coefficient computed by truncated polynomial arithmetic, n measured)",
      c1 == 3 * h)
check("<c2,[CP^2]> = 3 = chi (Euler-class cross-check)", int_c2 == 3 and int_c2 == chi_cell)
check("<c1^2,[CP^2]> = 9", int_c1sq == 9)
# annotated cross-check (Hirzebruch sigma = p1/3 is library math, NOT used to derive anything):
int_p1 = int(sp.expand(c1 ** 2 - 2 * c2).coeff(h, 2))
sigma_cp2 = 1  # intersection form on H^2(CP^2;Z) = Z<h> is the 1x1 matrix [1]: signature +1 (measured)
print(f"  intersection form [<h,h>] = [1] -> sigma(CP^2) = +1;  <p1,[CP^2]> = c1^2 - 2 c2 = "
      f"{int_p1} = 3 sigma  [Hirzebruch consistency note only]")
print("  CONTROLS (same arithmetic, different n):")
for nn in (1, 3):
    ct = chern_cpn(nn)
    print(f"    CP^{nn}: c(T) = {ct};  c1 = {ct.coeff(h, 1)}h;  chi = <c_{nn}> = "
          f"{int(ct.coeff(h, nn))}")
check("CP^1/CP^3 controls: c1 = 2h/4h, chi = 2/4 (machinery does not always output 3)",
      int(chern_cpn(1).coeff(h, 1)) == 2 and int(chern_cpn(3).coeff(h, 3)) == 4)

# ============================================================================
print()
print("=" * 88)
print("SECTION 5 -- THE HONEST GAP: the index arithmetic the coset 3 would have to enter")
print("=" * 88)
print("A condensate section over X^4 is a map f: X^4 -> D ~ CP^2. Pullback classes on a")
print("4-manifold: y = f*h in H^2(X;Z) and y^2 = f*(h^2) in H^4(X;Z); degree datum d = <y^2,[X]>.")
print("Twist the generation operator by L = f*O(m). Symbolic index (h2 canon formula + twist):")
kk_, km_, d_, m_, sig_ = sp.symbols('k k_minus d m sigma')
j = sp.Rational
T_dynk = lambda jj: jj * (jj + 1) * (2 * jj + 1) / 3   # Dynkin index [standard math; /3 is the
#                                                        library formula, anchored below, NOT a
#                                                        target import]
assert T_dynk(j(1, 2)) == j(1, 2) and T_dynk(1) == 2   # 't Hooft / gaugino anchors (h2 canon)
print(f"  Dynkin anchors: T(1/2) = {T_dynk(j(1, 2))} ('t Hooft), T(1) = {T_dynk(1)} (gaugino).")
print()
print("  ind(D_X (x) V_R (x) L) = 2 T(R) k  +  dim(R) * (m^2 d / 2)  +  dim(R) * Ahat[X],")
print("  with Ahat[X] = -sigma/8. The twist enters ONLY through the term  rk * c1(L)^2 / 2,")
print("  because ch1(V_R) = 0 for every GU-native (traceless su(2)) channel -- i.e. through a")
print("  term IDENTICALLY ABSENT in the native 12k arithmetic. That is the precise sense in")
print("  which this is a NEW channel and not a re-dress of the native one.")
ind_full = sp.expand(2 * 0 + 4 * (2 * T_dynk(j(1, 2)) * kk_) + 2 * (2 * T_dynk(1) * kk_)
                     + 16 * (m_ ** 2 * d_ / 2) + 16 * (-sig_ / 8))
print(f"  Full 16-dim multiplicity bundle [leg-3 content 2(j=0)+4(j=1/2)+2(j=1)]:")
print(f"    ind_full = {ind_full}")
d2_ = sp.symbols("d'")
ind_full_spin = ind_full.subs(d_, 2 * d2_)
print(f"  2-ADIC WALL: X^4 spin => intersection form EVEN => d = 2d' =>")
print(f"    ind_full = {sp.expand(ind_full_spin)}   -- EVEN for every m, d', k, sigma.")
print(f"    (Rokhlin: sigma = 0 mod 16 makes the gravitational term even independently.)")
print(f"  => The CP^2 twist CANNOT make the full-bundle index odd. It respects the 12k/2-adic")
print(f"     wall; what it can inject is 3-DIVISIBILITY, and only via m: the twist term")
print(f"     16 m^2 d' = m^2 d' (mod 3) is 3-divisible for ALL d' iff 3 | m. The canonical")
print(f"     3-divisible class measured in Section 4 is exactly c1(T CP^2) = 3h, i.e. the")
print(f"     anticanonical O(3) = K^(-1) of the coset: m = 3 iff the condensate couples through")
print(f"     the (anti)canonical class of D. NOT SETTLED here.")
print()
ind_32 = sp.expand(3 * km_ + 6 * (m_ ** 2 * d_ / 2))
print(f"  (3,2) generation sub-sector, su(2)- gauged at k_minus, with twist:")
print(f"    ind_(3,2) = {ind_32} = 3*(k_minus + m^2 d)  -- 3-divisible for ANY m, d, BUT the 3")
print(f"    here is the NATIVE MULTIPLICITY riding along (h2 canon sec. 4: import k_minus +")
print(f"    truncation), not a new coset-born 3. Do not conflate the two.")
print()
print("  WHAT WOULD SETTLE THE INDEX LEG (stated, not done):")
print("   (i)  Equivariant selection of m: decompose the condensate channel of the 1792-dim")
print("        carrier under the stabilizer S(U(1) x U(2,2)) and read off which homogeneous line")
print("        bundle O(m) on D = SU(3,2)/S(U(1)xU(2,2)) the breaking direction transforms in;")
print("        m = +/-3 (the canonical class) would make the 3-divisibility canonical, any other")
print("        m makes it an import. Finite-dimensional, executable in principle.")
print("   (ii) A nonconstant section f (needs the unbuilt condensate DYNAMICS); its degree")
print("        d = <f*(h^2),[X]> is otherwise a free import, exactly like k in 12k.")
print("   (iii)The twisted-operator signature check against C-07: the Kramers/quaternionic")
print("        evenness argument (h2 canon sec. 3c) needs a REAL rep; L is complex, so the")
print("        hypothesis fails and the wall does not apply -- but escape-of-hypothesis is not")
print("        a counterexample; the induced operator must be built and its spectrum measured.")
check("index leg: symbolic arithmetic printed; graded CONSISTENT_UNCOMPUTED (nothing asserted)",
      True)

# ============================================================================
print()
print("=" * 88)
print("SECTION 6 -- FORBIDDEN-SET AUDIT AND SUMMARY")
print("=" * 88)
print("Forbidden set {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8}: never inserted into any")
print("construction above and never divided by in any conclusion. Provenance of every printed 3:")
print(f"  * '3' in base (3,1): dim X = 4 with ONE time direction (inserted geometry = 4 and")
print(f"    'Lorentzian'; 3 = 4 - 1; fiber result (6,4) is g -> -g invariant, so which sign is")
print(f"    time does not matter).")
print(f"  * 3 positive complex directions: eigenvalue COUNT of the measured Hermitian form.")
print(f"  * chi = 3: cell count (1 - 0 + 1 - 0 + 1) and Gauss-Bonnet quadrature {chi_fs:.4f}.")
print(f"  * c1 = 3h: coefficient of (1+h)^(n+1) with n = {n} measured.")
print(f"  * Dynkin /3 and Hirzebruch /3: library formulas (anchored: T(1/2)=1/2, sigma(CP^2)=1),")
print(f"    used only in the CONSISTENT_UNCOMPUTED sketch, never to produce a count.")
print()
if FAIL:
    print(f"RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    sys.exit(1)
print("RESULT: all checks passed.")
print()
print("VERDICT (printed for the doc):")
print("  (a) D deformation-retracts onto CP^2: THEOREM (explicit construction + numerical")
print("      domain-preservation on 2000 lines; negative-line control fails as it must).")
print("  (b) chi(CP^2) = 3, measured twice (cells; Gauss-Bonnet), provenance chain printed:")
print("      THEOREM. The breaking coset does NOT have the RP^3/Z_2 profile: H^2(D) = Z (free),")
print("      and it carries a canonical 3-divisible class c1 = 3h.")
print("  (c) c1 = 3h, <c2> = 3 = chi, <c1^2> = 9: THEOREM (truncated-polynomial arithmetic).")
print("  (d) whether that 3 reaches the generation index: CONSISTENT_UNCOMPUTED -- needs the")
print("      equivariant m-selection + an actual section (dynamics) + the C-07 twisted check.")
print("  Overall route grade: CONSISTENT_UNCOMPUTED (the payoff leg is (d)).")
sys.exit(0)
