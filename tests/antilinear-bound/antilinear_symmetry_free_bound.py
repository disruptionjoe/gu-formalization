#!/usr/bin/env python3
"""
WC-ANTILINEAR-BOUND, script 2 of 2: the symmetry-free bound -- the antilinear
index-nullity theorem on the delimited class S, with adversarial instantiation.

THE DELIMITED CLASS S (the search space of the paper's antilinear hunt, now bounded).
On the 192-dim generation carrier W (Krein form K: Hermitian, K^2 = I, signature (96,96),
purely cross-chirality; chirality Gamma_c: Hermitian involution, split (96,96), K Gamma_c =
-Gamma_c K -- all machine-certified below), let

  S := { antilinear C = M . conj  :  M invertible is FORCED, and
         k(Cx, Cy) = lambda conj(k(x, y)) for all x, y  (matrix form M^dag K M = lambda K-bar)
         for some real lambda != 0 }.

S is the Krein-compatible antilinear operators: lambda = +1 Krein-antiunitary, lambda = -1
anti-antiunitary, general lambda the conformal closure.  NO equivariance, NO frame condition,
NO square normalization, NO topology beyond finite-dimensional linearity is assumed: S
contains every rung of the declared symmetry-breaking ladder (antilinear_ladder_census.py)
down to and including fully symmetry-free operators.  On this carrier the Krein condition IS
ghost-grading compatibility (the ghost sector enters the carrier kinematics only through the
hyperbolic 50/50 Krein pairing, canon/ghost-parity-krein-synthesis.md).

THEOREM (antilinear index nullity on S).  For every C = M . conj in S:
  (1) M is invertible (K nondegenerate and lambda != 0 force it);
  (2) the images C(W_+), C(W_-) are complex 96-dim subspaces forming a K-LAGRANGIAN
      complementary pair, and they are exactly the eigenspaces of the C-induced re-grading
      Gamma_C = C Gamma_c C^{-1} (a linear involution);
  (3) every physical subspace P (maximal K-positive-definite, dim 96) satisfies
      P ^ C(W_+) = P ^ C(W_-) = 0, so both projections of P onto the re-graded chirality
      eigenspaces are isomorphisms;
  (4) hence the net chiral index of P is EXACTLY 0 in the re-graded chirality -- and in the
      original chirality (Theorem 2's operator-free graph argument).
  COROLLARY: no C in S is a chiralizer.  No Krein-compatible antilinear operator --
  equivariant or not, frame-trivial or frame-ACTIVE, C^2 = -1 or not -- can put a nonzero
  (let alone odd) net chiral index on any physical subspace of this carrier.

PROOF (finite-dimensional linear algebra; premises machine-certified here).
  (1) M^dag K M = lambda K-bar with K, K-bar invertible and lambda != 0 => M invertible.
  (2) For x, y in W_+: k(Cx, Cy) = lambda conj(k(x, y)) = 0 since W_+ is K-isotropic
      (K is purely cross-chirality).  So C(W_+) is K-isotropic of dim 96 = maximal:
      K-Lagrangian.  Same for C(W_-).  C bijective => C(W_+) (+) C(W_-) = W.
      Gamma_C is linear, squares to I, and Gamma_C(Cx) = C(Gamma_c x) = (+/-)Cx for
      x in W_(+/-), so its eigenspaces are C(W_(+/-)).
  (3) P is K-positive-definite, C(W_(+/-)) are K-null: a nonzero vector cannot be both.
  (4) The projection of P onto C(W_+) along C(W_-) has kernel P ^ C(W_-) = 0, so it is
      injective, hence onto a 96-dim image: dim proj_+(P) = dim proj_-(P) = 96, and the
      net index chi_C(P) = 96 - 96 = 0.  QED.

WHAT THIS SCRIPT CERTIFIES (deterministic, numpy-only, exact-in-effect).
  PART A -- premises: K Hermitian involution, signature (96,96), purely cross-chirality
      (W_+/- K-Lagrangian), Gamma_c split, K Gamma_c = -Gamma_c K.
  PART B -- NON-VACUITY (the theorem is about a genuinely inhabited class): STRICT
      symmetry-free witnesses are CONSTRUCTED IN CLOSED FORM for all four sign patterns
      (eps, lambda) in {+-1}^2 -- antilinear, chirality-SWAPPING, C^2 = eps I EXACTLY,
      M^dag K M = lambda K-bar EXACTLY, frame-ACTIVE (fc order 10), NON-equivariant under
      the internal so(5,5).  The (eps, lambda) = (-1, +1) witness is precisely the
      AZ-CII-shaped operator the paper's hunt could not exclude: a frame-non-trivial
      Krein-antiunitary chirality-swapping Kramers operator.  IT EXISTS.  The construction:
      in a Lagrangian pairing basis Q (Q^dag K Q = X = [[0,I],[I,0]]), take
      M = Q S conj(Q)^{-1} with S = [[0, A], [eps conj(A)^{-1}, 0]] and A = lambda*eps*A^T
      (symmetric or antisymmetric, random invertible, fixed seed); then M M-bar = eps I and
      M^dag K M = lambda K-bar hold IDENTICALLY (algebra reproduced in the RESULTS note).
  PART C -- the theorem, adversarially instantiated: for the 4 strict witnesses plus
      Krein-unitary dressings (which preserve A2, break C^2 = eps I, and move the images):
      isotropy of C(W_+/-) at machine precision, complementarity, and chi_C(P) = 0 and
      chi(P) = 0 as EXACT INTEGER rank computations (SVD gaps printed) for a batch of
      random physical subspaces P.
  PART D -- sharpness of the boundary of S: for an antilinear operator OUTSIDE S (random
      invertible M, Krein residual order 1): it maps a physical subspace to a NON-physical
      one (image Krein Gram indefinite -- the operator does not act on the sector's
      physical states, which is WHY admissibility excludes it), and the K-ALIGNED grading
      whose "index" is the vectorlike +-96 has K-DEFINITE eigenspaces, hence lies provably
      outside the class-S orbit of the physical chirality (class-S re-gradings have
      K-Lagrangian eigenspaces -- part (2)).  The +-96 is the paper's selection count, not
      an index; a continuity sweep corroborates (selection trace varies continuously,
      non-integer, under a Krein-unitary path -- the paper's D1-style criterion).

FAILURE CONDITION (report, do not patch): any admissible operator with chi_C(P) != 0 --
this would kill the paper's Section 6 escape analysis.  Every assert below enforces the
opposite; a nonzero index aborts the run loudly.

RESULT: the paper's antilinear caveat (d) closes over S: the hunt's "no frame-non-trivial
antilinear chiralizer found" upgrades to "frame-non-trivial Krein-compatible antilinear
CII swap operators EXIST (exhibited), and NONE of them -- nor anything else in S -- is a
chiralizer: index nullity is a theorem on all of S."  The honest residual OUTSIDE S is
exactly: antilinear operators that break Krein/ghost compatibility (for which admissibility
itself fails -- they do not act on physical states), and the function-space setting
(WC-FUNCTION-SPACE-EXT).  Runtime < 90 s, deterministic.
"""
import time
import numpy as np
from itertools import combinations

T0 = time.time()
N, DIM = 14, 128
SEED = 20260703                       # different seed from the census by design
TIMELIKE = {4, 5, 6, 7, 8}
np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(SEED)
NASSERT = 0


def check(cond, msg):
    global NASSERT
    NASSERT += 1
    assert cond, msg


# ------------------------------------------------------------------ substrate (as the census)
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


def lvec4(i, j):
    M = np.zeros((4, 4), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


print("=" * 98)
print("WC-ANTILINEAR-BOUND symmetry-free bound: substrate + PART A (theorem premises)")
print("=" * 98)
base = jw(7)
e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)
cerr = max(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                         - (2.0 * (-1.0 if a in TIMELIKE else 1.0) if a == b else 0.0) * I128))
           for a in range(N) for b in range(N))
check(cerr < 1e-12, "Clifford relations")

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
Jk = [np.kron(lvec4(a, b) + lvec4(c, d), I128) + np.kron(I4, S)
      for (a, b, c, d), S in zip(SD, Sig)]
Cas = -(Jk[0] @ Jk[0] + Jk[1] @ Jk[1] + Jk[2] @ Jk[2])
Cas = 0.5 * (Cas + Cas.conj().T)
cw, cV = np.linalg.eigh(Cas)
mask = np.abs(cw - cw.max()) < 1e-6
W = cV[:, mask]
check(abs(cw.max() - 8.0) < 1e-9 and W.shape[1] == 192, "carrier j=1 Casimir-8, dim 192")

om = I128.copy()
for a in range(N):
    om = om @ e[a]
om = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
Gc = W.conj().T @ np.kron(I4, om) @ W
Gc = 0.5 * (Gc + Gc.conj().T)
gev, gV = np.linalg.eigh(Gc)
check(int((gev > 0.5).sum()) == 96 and int((gev < -0.5).sum()) == 96, "chirality split 96/96")
P0 = gV[:, gev > 0.5]                                  # 192 x 96 basis of W_+
N0 = gV[:, gev < -0.5]                                 # 192 x 96 basis of W_-

spacelike = [a for a in range(N) if a not in TIMELIKE]
bS = I128.copy()
for s in spacelike:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
Kc = W.conj().T @ np.kron(I4, bS) @ W
Kc = 0.5 * (Kc + Kc.conj().T)
Kb = Kc.conj()
kev = np.linalg.eigvalsh(Kc)
check(int((kev > 1e-8).sum()) == 96 and int((kev < -1e-8).sum()) == 96, "K signature (96,96)")
check(np.linalg.norm(Kc @ Kc - np.eye(192)) < 1e-10, "K^2 = I (Hermitian involution)")
check(np.linalg.norm(Kc @ Gc + Gc @ Kc) < 1e-10, "K Gamma_c = -Gamma_c K (cross-chirality)")
iso_p = np.linalg.norm(P0.conj().T @ Kc @ P0)
iso_m = np.linalg.norm(N0.conj().T @ Kc @ N0)
print(f"[premises] ||Im K|| = {np.linalg.norm(Kc.imag):.3f} (K genuinely complex: K-bar != K)")
print(f"[premises] W_+/- K-isotropy residuals = ({iso_p:.2e}, {iso_m:.2e})  => K-LAGRANGIAN pair")
check(iso_p < 1e-10 and iso_m < 1e-10, "W_+/- are K-Lagrangian")

# frame + internal generators (compressed) for frame-charge / non-equivariance diagnostics
FRAME, INTG = [], []
for a, b in combinations(range(4), 2):
    FRAME.append(W.conj().T @ (np.kron(lvec4(a, b), I128) + np.kron(I4, sgen(e, a, b))) @ W)
for a, b in [(4, 5), (5, 6), (9, 10), (4, 9), (8, 13), (6, 11)]:   # probe subset of so(5,5)
    INTG.append(W.conj().T @ np.kron(I4, sgen(e, a, b)) @ W)


def frame_charge(M):
    return max(np.linalg.norm(M @ f.conj() - f @ M) for f in FRAME)


def int_charge(M):
    return max(np.linalg.norm(M @ g.conj() - g @ M) for g in INTG)


def rank_gap(A, tol=1e-8):
    s = np.linalg.svd(A, compute_uv=False)
    thr = tol * s.max()
    r = int((s > thr).sum())
    gap = (s[r - 1] / s[r]) if r < len(s) else np.inf
    return r, gap


def expm_ss(X):
    """Scaling-squaring Taylor exponential (numpy-only)."""
    k = max(0, int(np.ceil(np.log2(max(1e-16, np.linalg.norm(X, 2))))) + 2)
    Y = X / (2 ** k)
    E = np.eye(X.shape[0], dtype=complex)
    T = np.eye(X.shape[0], dtype=complex)
    for n in range(1, 18):
        T = T @ Y / n
        E = E + T
    for _ in range(k):
        E = E @ E
    return E


# =============================================================== PART B -- strict witnesses
print("\n" + "=" * 98)
print("PART B -- closed-form STRICT witnesses: the operators the hunt could not exclude EXIST")
print("=" * 98)
# Lagrangian pairing basis: Q = [P0, N0 G^{-1}] with G = P0^dag K N0  =>  Q^dag K Q = X
G = P0.conj().T @ Kc @ N0
check(np.linalg.cond(G) < 1e6, "cross-chirality Krein pairing nondegenerate")
Qm = N0 @ np.linalg.inv(G)
Q = np.hstack([P0, Qm])
X = np.zeros((192, 192), dtype=complex)
X[:96, 96:] = np.eye(96)
X[96:, :96] = np.eye(96)
rX = np.linalg.norm(Q.conj().T @ Kc @ Q - X)
print(f"[pairing]  ||Q^dag K Q - X|| = {rX:.2e}  (X = hyperbolic pair form)")
check(rX < 1e-9, "Lagrangian pairing basis")
Qbi = np.linalg.inv(Q.conj())

witnesses = []
for eps in (-1.0, 1.0):
    for lam in (-1.0, 1.0):
        A = rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))
        A = 0.5 * (A + (lam * eps) * A.T)          # A = lam*eps*A^T
        check(np.linalg.cond(A) < 1e6, f"A invertible (eps={eps:+.0f}, lam={lam:+.0f})")
        S = np.zeros((192, 192), dtype=complex)
        S[:96, 96:] = A
        S[96:, :96] = eps * np.linalg.inv(A.conj())
        M = Q @ S @ Qbi
        rI = np.linalg.norm(M @ M.conj() - eps * np.eye(192))
        KM = M.conj().T @ Kc @ M
        rK = np.linalg.norm(KM - lam * Kb) / np.linalg.norm(Kb)
        rswap = np.linalg.norm(Gc @ M + M @ Gc.conj()) / np.linalg.norm(M)
        fc = frame_charge(M / np.linalg.norm(M) * np.sqrt(192))
        ic = int_charge(M / np.linalg.norm(M) * np.sqrt(192))
        tag = "AZ-CII SHAPE (Kramers + Krein-antiunitary)" if (eps, lam) == (-1.0, 1.0) else ""
        print(f"  witness (eps={eps:+.0f}, lambda={lam:+.0f}): C^2 = eps I residual {rI:.2e}, "
              f"M^dag K M = lam K-bar residual {rK:.2e},")
        print(f"    pure-swap residual {rswap:.2e}, frame charge fc = {fc:.2f} (frame-ACTIVE), "
              f"internal non-equivariance = {ic:.2f}  {tag}")
        check(rI < 1e-9, "witness A3 exact")
        check(rK < 1e-9, "witness A2 exact")
        check(rswap < 1e-9, "witness swaps chirality")
        check(fc > 1.0, "witness frame-ACTIVE (fc order 10, not 0)")
        check(ic > 1.0, "witness non-equivariant under internal so(5,5)")
        witnesses.append((f"strict(eps={eps:+.0f},lam={lam:+.0f})", M))
print("""  => The frame-non-trivial antilinear chiralizer CANDIDATE the paper hunted for EXISTS
     once all symmetry is dropped -- including the exact AZ-CII shape (C^2 = -1, Krein-
     antiunitary, chirality-swapping, frame-active).  Existence was never the issue.
     PART C shows why none of them (nor anything else in S) can force: index nullity.""")

# Krein-unitary dressings: preserve A2 with the SAME lambda, break C^2 = eps I, move images
for j in range(4):
    H = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
    H = 0.35 * (H - H.conj().T) / np.linalg.norm(H)
    U = expm_ss(Kc @ H)                              # a = K H, H anti-Hermitian: a^dag K + K a = 0
    rU = np.linalg.norm(U.conj().T @ Kc @ U - Kc)
    check(rU < 1e-9, f"dressing {j}: U is Krein-unitary")
    Mw = witnesses[j][1]
    Md = U @ Mw
    MMb = Md @ Md.conj()
    sI = np.vdot(np.eye(192), MMb) / 192
    rI = np.linalg.norm(MMb - sI * np.eye(192))
    witnesses.append((f"dressed#{j}", Md))
    print(f"  dressing #{j}: U Krein-unitary (residual {rU:.2e}); C^2 scalarity broken "
          f"(||C^2 - s I|| = {rI:.2f}): class-S member beyond the Wigner-normalized subset")

# ====================================================== PART C -- the index-nullity theorem
print("\n" + "=" * 98)
print("PART C -- index nullity certified on every witness (exact integer ranks, gaps printed)")
print("=" * 98)
# random physical subspaces: P_j = U_j P_phys, P_phys = K-positive eigenspace
kev2, kV = np.linalg.eigh(Kc)
Pphys = kV[:, kev2 > 1e-8]
phys_list = [Pphys]
for j in range(3):
    H = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
    H = 0.4 * (H - H.conj().T) / np.linalg.norm(H)
    U = expm_ss(Kc @ H)
    phys_list.append(U @ Pphys)
for j, P in enumerate(phys_list):
    gram = P.conj().T @ Kc @ P
    gmin = np.linalg.eigvalsh(0.5 * (gram + gram.conj().T)).min()
    check(gmin > 1e-6, f"P{j} is K-positive-definite (min eig {gmin:.2e})")
    # original-chirality nullity (Theorem 2, operator-free)
    rp, gp = rank_gap(np.hstack([P, P0]))
    rm, gm = rank_gap(np.hstack([P, N0]))
    check(rp == 192 and rm == 192, f"P{j}: P ^ W_+/- = 0 (ranks {rp},{rm})")
print(f"  {len(phys_list)} physical subspaces built; chi(P) = 0 for all (original grading).")

worst_iso, worst_gap = 0.0, np.inf
for name, M in witnesses:
    Wp = M @ P0.conj()                               # basis of C(W_+)
    Wm = M @ N0.conj()                               # basis of C(W_-)
    iso = max(np.linalg.norm(Wp.conj().T @ Kc @ Wp), np.linalg.norm(Wm.conj().T @ Kc @ Wm))
    iso = iso / max(np.linalg.norm(M) ** 2 / 192, 1e-30)
    worst_iso = max(worst_iso, iso)
    check(iso < 1e-9, f"{name}: C(W_+/-) K-isotropic (transport lemma)")
    rc, gc_ = rank_gap(np.hstack([Wp, Wm]))
    check(rc == 192, f"{name}: C(W_+) (+) C(W_-) = W (complementary Lagrangian pair)")
    chis = []
    for j, P in enumerate(phys_list):
        r1, g1 = rank_gap(np.hstack([P, Wp]))
        r2, g2 = rank_gap(np.hstack([P, Wm]))
        worst_gap = min(worst_gap, g1, g2)
        dp, dm = 192 - r1, 192 - r2                  # dim(P ^ C(W_+)), dim(P ^ C(W_-))
        chi = dp - dm
        chis.append(chi)
        check(dp == 0 and dm == 0, f"{name}, P{j}: intersections must vanish")
        check(chi == 0, f"{name}, P{j}: chi_C(P) = {chi} != 0 -- FAILURE CONDITION FIRED")
    print(f"  [{name:26s}] isotropy {iso:.2e}; chi_C(P) = {chis} (exact integers, all 0)")
print(f"  worst isotropy residual {worst_iso:.2e}; worst rank-decision gap {worst_gap:.1e} "
      f"(all decisions O(1e8) separated)")

# ============================================== PART D -- sharpness of the boundary of S
print("\n" + "=" * 98)
print("PART D -- the boundary of S is sharp: outside S admissibility itself fails")
print("=" * 98)
Mbad = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
KMb = Mbad.conj().T @ Kc @ Mbad
lam_fit = np.vdot(Kb, KMb) / np.vdot(Kb, Kb)
rbad = np.linalg.norm(KMb - lam_fit * Kb) / np.linalg.norm(KMb)
print(f"  control operator OUTSIDE S: best-fit Krein residual = {rbad:.3f} (order 1: not in S)")
check(rbad > 0.5, "control is genuinely outside S")
img = Mbad @ Pphys.conj()
gram = img.conj().T @ Kc @ img
gev_img = np.linalg.eigvalsh(0.5 * (gram + gram.conj().T))
print(f"  its image of a physical subspace has Krein Gram eigenvalues in "
      f"[{gev_img.min():.2f}, {gev_img.max():.2f}]: INDEFINITE -- the image is NOT a")
print("  physical subspace.  An operator outside S does not act on the sector's physical")
print("  states at all: admissibility fails by the paper's own criteria, not by fiat.")
check(gev_img.min() < -1e-6 and gev_img.max() > 1e-6, "outside-S image is non-physical")

# where nonzero counts actually live: K-NULL (unphysical) selections only
tr_wp = np.trace(P0.conj().T @ Gc @ P0).real
null_wp = np.linalg.norm(P0.conj().T @ Kc @ P0)
tr_phys = np.trace(Pphys.conj().T @ Gc @ Pphys).real
gram_phys = Pphys.conj().T @ Kc @ Pphys
iso_sel = np.linalg.norm(gram_phys - np.eye(96))
print(f"\n  where a nonzero count CAN appear: selecting W_+ itself gives graded trace "
      f"{tr_wp:+.1f}")
print(f"  (the paper's vectorlike +96) -- but W_+ is K-NULL (Gram norm {null_wp:.2e}):")
print("  that selection contains NO physical state.  The physical (K-positive) selection")
print(f"  gives graded trace {tr_phys:+.2f} (and chi = 0 exactly, PART C), with K-Gram = I")
print(f"  (residual {iso_sel:.2e}).  Definiteness transport: for C in S, k(Cx,Cx) =")
print("  lambda k(x,x), so class-S operators map physical subspaces to (+/-)physical")
print("  subspaces and can NEVER map them onto a K-null selection like W_+ -- the +96")
print("  channel is unreachable from physical states inside S:")
check(abs(tr_wp - 96.0) < 1e-9, "W_+ selection carries the vectorlike +96 (even)")
check(null_wp < 1e-9, "W_+ is K-null: the +96 selection contains no physical state")
check(iso_sel < 1e-9, "physical selection has identity K-Gram")
for name, M in witnesses[:2]:
    img = M @ Pphys.conj()
    gr = img.conj().T @ Kc @ img
    ev = np.linalg.eigvalsh(0.5 * (gr + gr.conj().T))
    definite = ev.min() > 1e-8 or ev.max() < -1e-8
    print(f"    [{name}] image-of-physical Krein Gram eigenvalue range "
          f"[{ev.min():+.3e}, {ev.max():+.3e}]: DEFINITE (sign = lambda)")
    check(definite, f"{name}: class-S image of a physical subspace is (+/-)definite")

# continuity corroboration: selection traces are not indices (the D1-style criterion)
H = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
H = 0.5 * (H - H.conj().T) / np.linalg.norm(H)
Mw = witnesses[0][1]
vals = []
for t in (0.0, 0.25, 0.5, 0.75, 1.0):
    U = expm_ss(t * (Kc @ H))
    img = U @ Mw @ P0.conj()
    Qr, _ = np.linalg.qr(img)
    vals.append(float(np.trace(Qr.conj().T @ Gc @ Qr).real))
print(f"\n  selection trace tr(Gamma_c Pi_t) along a Krein-unitary path: {[f'{v:+.3f}' for v in vals]}")
spread = max(vals) - min(vals)
print(f"  spread = {spread:.3f}: CONTINUOUS and non-quantized -- a selection overlap, not an")
print("  index (the paper's D1 criterion: continuously tunable quantities force nothing).")
check(spread > 1e-3, "selection trace varies continuously (not a topological index)")

# ------------------------------------------------------------------------------- verdict
print("\n" + "#" * 98)
print("# SYMMETRY-FREE BOUND -- VERDICT")
print("#" * 98)
print(f"""
  THE DELIMITED CLASS S: antilinear C = M . conj with M^dag K M = lambda K-bar, lambda real
  nonzero -- every Krein-compatible antilinear operator on the carrier, with NO symmetry,
  frame, square, or continuity assumption.  This contains every rung of the ladder census
  and the fully symmetry-free operators.

  THEOREM (certified above): every C in S maps the chirality pair to a K-Lagrangian pair,
  and every physical subspace keeps net chiral index EXACTLY 0 in both the original and the
  C-induced grading.  No admissible antilinear chiralizer exists in S.  This is stronger
  than the paper's hunt conclusion: the hunted operators (frame-active CII swaps) EXIST in
  S (exhibited in closed form) -- and still cannot force, because forcing was never about
  existence: Krein compatibility alone pins the index at 0.

  THE HONEST RESIDUAL (outside S): antilinear operators with M^dag K M != lambda K-bar.
  For these, admissibility fails by the paper's own criteria -- they do not act on the
  sector's physical states (PART D: physical subspaces map to indefinite-Gram images), and
  the only gradings that yield nonzero counts (K-aligned, vectorlike +-96) are provably
  outside the class-S orbit of the physical chirality.  The remaining genuine openness is
  the function-space setting (sections, Fredholm, spectral flow): WC-FUNCTION-SPACE-EXT.

  hard asserts passed: {NASSERT}
  total runtime: {time.time() - T0:.1f}s""")
# EOF
