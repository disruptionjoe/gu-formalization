"""
WAVE swing-3 (THE OUTSIDE) probe -- what IS the boundary, analytically?

Central EXACT claim under test (sharpens the swing's boundary characterization):

  The ~8% q<0 / K_S-null stratum IS the CHARACTERISTIC VARIETY of the (9,5) Dirac
  symbol, and "outside" is its timelike interior {q<0}. Concretely, for the
  Clifford symbol c(xi) = sum_mu xi_mu gamma^mu of Cl(9,5):

    (P1) c(xi)^2 = q(xi) * I exactly, with q(xi) = <xi,xi>_{9,5} = P - T.
    (P2) char variety {det c(xi) = 0} == {q(xi) = 0}: the operator's principal
         symbol degenerates EXACTLY on the lightcone q=0 -- that is the boundary.
    (P3) spacelike-dominant end (q>0): spectrum of c(xi) is REAL (+-sqrt q).
         timelike-dominant end (q<0): spectrum is IMAGINARY (+- i sqrt|q|).
         Crossing q=0 flips the symbol from real (hyperbolic/elliptic-reducible,
         limit-point, theta dissolves) to imaginary spectrum.
    (P4) the null-K_S little theorem, reconstructed from scratch: a Hermitian
         Krein form K with K c(xi) Hermitian (c(xi) is K-self-adjoint) forces
         every eigenvector with NON-REAL eigenvalue to be K-null. At q<0 the whole
         spectrum is imaginary => the K-definite cut does not exist => the operator
         is not constructible from committed structure there. Independently
         reproduces the banked Prong-0 C3 result (residual ~1e-15).

Deterministic, numpy only, no network, foreground. Two runs byte-identical.
This is a faithful finite toy of the symbol-level facts; the operator-grade /
sector-relative content it stands on lives in the cited Prong-0 receipt.
"""
import numpy as np

np.random.seed(20260721)
TOL = 1e-9

# ---- Pauli / building blocks ----
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

def kron(mats):
    out = np.array([[1]], dtype=complex)
    for m in mats:
        out = np.kron(out, m)
    return out

# ---- 14 anticommuting Hermitian generators (Jordan-Wigner tensor construction) ----
# gamma_{2k-1} = Z..Z X I..I ,  gamma_{2k} = Z..Z Y I..I  (k-1 leading Z's), size 2^7=128
NFAC = 7
def gen(k, P):  # k in 1..7, P in {X,Y}
    facs = [Z]*(k-1) + [P] + [I2]*(NFAC-k)
    return kron(facs)

herm = []
for k in range(1, NFAC+1):
    herm.append(gen(k, X))
    herm.append(gen(k, Y))
herm = herm[:14]  # 14 Hermitian generators, each ^2 = I, mutually anticommuting

# signature (9,5): first 9 spacelike (Hermitian, square +I),
# last 5 timelike -> multiply by i (anti-Hermitian, square -I)
gam = [herm[m] for m in range(9)] + [1j*herm[m] for m in range(9, 14)]
sig = np.array([+1]*9 + [-1]*5)
DIM = gam[0].shape[0]
I_D = np.eye(DIM, dtype=complex)

def csym(xi):
    return sum(xi[m]*gam[m] for m in range(14))

def q_of(xi):
    return float(sum(sig[m]*xi[m]**2 for m in range(14)))

checks = []
def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))

# ---- sanity: generators anticommute and have right squares ----
ac_ok = True
sq_ok = True
for a in range(14):
    sq = gam[a] @ gam[a]
    if not np.allclose(sq, sig[a]*I_D, atol=TOL):
        sq_ok = False
    for b in range(a+1, 14):
        if not np.allclose(gam[a]@gam[b] + gam[b]@gam[a], 0, atol=TOL):
            ac_ok = False
check("gamma-anticommute", ac_ok)
check("gamma-squares=eta", sq_ok)

# ---- test covectors ----
# spacelike-dominant (q>0), timelike-dominant (q<0), and null (q=0)
xi_space = np.zeros(14); xi_space[0] = 1.0                 # pure spacelike -> q=+1
xi_time  = np.zeros(14); xi_time[9]  = 1.0                 # pure timelike  -> q=-1
xi_null  = np.zeros(14); xi_null[0] = 1.0; xi_null[9] = 1.0  # q = 1-1 = 0 (lightlike)

# (P1) Clifford relation c^2 = q I
for tag, xi in [("space", xi_space), ("time", xi_time), ("null", xi_null)]:
    c = csym(xi)
    check(f"P1-clifford-{tag}", np.allclose(c@c, q_of(xi)*I_D, atol=TOL),
          f"q={q_of(xi):+.3f}")

# (P2) characteristic variety {det c = 0} == {q = 0}
def is_singular(xi):
    return abs(np.linalg.det(csym(xi))) < 1e-6  # det scale can be large; near 0 vs O(1)

# use eigen-based rank test instead of det (det underflows at dim 128): min|eig|
def min_abs_eig(xi):
    return float(np.min(np.abs(np.linalg.eigvals(csym(xi)))))

check("P2-space-nonsingular", min_abs_eig(xi_space) > 0.5, f"min|eig|={min_abs_eig(xi_space):.3f}")
check("P2-time-nonsingular",  min_abs_eig(xi_time)  > 0.5, f"min|eig|={min_abs_eig(xi_time):.3f}")
check("P2-null-SINGULAR",     min_abs_eig(xi_null)  < 1e-8, f"min|eig|={min_abs_eig(xi_null):.2e}")

# genericity: 400 random covectors, the boundary {q=0} is exactly where c degenerates
rng = np.random.default_rng(20260721)
agree = 0
crossed = 0
N = 400
for _ in range(N):
    xi = rng.normal(size=14)
    q = q_of(xi)
    sing = min_abs_eig(xi) < 1e-6
    # generic random xi has q != 0, so c should be nonsingular; degeneracy <=> q==0
    if (abs(q) < 1e-6) == sing:
        agree += 1
    if q < 0:
        crossed += 1
check("P2-charvariety=={q=0}", agree == N, f"{agree}/{N} agree; q<0 frac={crossed/N:.2f}")

# (P3) real spectrum for q>0, imaginary spectrum for q<0
def spectrum_type(xi):
    ev = np.linalg.eigvals(csym(xi))
    max_im = float(np.max(np.abs(ev.imag)))
    max_re = float(np.max(np.abs(ev.real)))
    return max_re, max_im

re_s, im_s = spectrum_type(xi_space)
re_t, im_t = spectrum_type(xi_time)
check("P3-space-real-spectrum",     im_s < TOL and re_s > 0.5, f"re={re_s:.3f} im={im_s:.1e}")
check("P3-time-imaginary-spectrum", re_t < TOL and im_t > 0.5, f"re={re_t:.1e} im={im_t:.3f}")

# (P4) null-K_S little theorem, reconstructed:
# find a Hermitian Krein form K with K c(xi) Hermitian (c is K-self-adjoint).
# Candidates: products of timelike or spacelike gammas, x {1, i}, pick one that works.
def product(idxs):
    out = I_D.copy()
    for i in idxs:
        out = out @ gam[i]
    return out

time_idxs  = list(range(9, 14))
space_idxs = list(range(0, 9))
cands = []
for base, tag in [(product(time_idxs), "T"), (product(space_idxs), "S")]:
    for scale, stag in [(1.0, ""), (1j, "i")]:
        cands.append((scale*base, stag+tag))

def krein_ok(K):
    if not np.allclose(K, K.conj().T, atol=TOL):
        return False
    # K c(xi) Hermitian for all xi  <=>  K gamma^mu Hermitian for each mu
    for m in range(14):
        Kg = K @ gam[m]
        if not np.allclose(Kg, Kg.conj().T, atol=TOL):
            return False
    return True

K = None; Ktag = None
for Kc, tag in cands:
    if krein_ok(Kc):
        K, Ktag = Kc, tag
        break
check("P4-krein-form-exists", K is not None, f"K={Ktag}")

if K is not None:
    # c(xi) is a normal matrix in both regimes (Hermitian at q>0, anti-Herm at q<0),
    # so np.linalg.eig returns an orthonormal eigenbasis; the "spectral half" is a
    # genuine subspace and the right object is the Krein form RESTRICTED to it.
    def half_block(c, imag):
        w, V = np.linalg.eig(c)
        key = w.imag if imag else w.real           # split by sign of (imag or real) part
        idx = [j for j in range(len(w)) if key[j] > 1e-6]
        B = V[:, idx]
        B, _ = np.linalg.qr(B)                      # orthonormal basis of the half
        return B.conj().T @ (K @ B)                 # Krein form restricted to the half

    # at q<0 (imaginary spectrum): the little theorem => the half is EXACTLY K-null.
    Kb_neg = half_block(csym(xi_time), imag=True)
    check("P4-imag-half-is-K-NULL", np.linalg.norm(Kb_neg) < 1e-9,
          f"||K|half||={np.linalg.norm(Kb_neg):.2e}")
    # at q>0 (real spectrum): the SAME Krein form is NONDEGENERATE on the half
    # => a K-definite cut EXISTS => the operator IS constructible there.
    Kb_pos = half_block(csym(xi_space), imag=False)
    mineig = float(np.min(np.abs(np.linalg.eigvals(Kb_pos))))
    check("P4-real-half-K-nondegenerate-cut-exists", mineig > 1e-6,
          f"min|eig(K|half)|={mineig:.3f}")

# ---- report ----
npass = sum(1 for _, ok, _ in checks if ok)
print("WAVE swing-3 boundary=characteristic-variety probe")
print("-"*64)
for name, ok, detail in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:38s} {detail}")
print("-"*64)
print(f"HEADLINE: {npass}/{len(checks)} PASS")
import sys
sys.exit(0 if npass == len(checks) else 1)
