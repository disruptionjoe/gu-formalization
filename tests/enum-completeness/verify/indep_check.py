#!/usr/bin/env python3
"""Independent re-verification of the class-C generator census (WC-ENUM-COMPLETENESS).

INDEPENDENT RECOMPUTATION, per house convention (cf. tests/chase/MOVE-*/verify/):
  * my OWN gamma construction (recursive doubling, NOT the chaser's Jordan-Wigner ordering);
  * a DIFFERENT signature, Cl(7,7) (timelike = the LAST seven indices; internal so(3,7)),
    where the real Clifford algebra is M(128,R) (real type), not M(64,H);
  * a DIFFERENT null-space algorithm (successive SVD refinement of the matched-support
    parameterization, not a single PSD normal-matrix eigh);
  * the Euclidean (14,0) chirality-DETECTING control: there the invariant sesquilinear form
    is definite and chirality-DIAGONAL (the paper's grading-aligned |chi| = 96 control), so
    the method demonstrably does NOT always return "cross-chirality";
  * an EXACT weight-peeling Schur count on the compact form certifying the main script's
    dimensions 2/2/2/2 independently of any numerical Hom solve.

Checks:
 (1) Cl(7,7) carrier: dim 192, ||Gamma W|| = 0, Krein signature (+96,-96), cross-chirality.
 (2) Census under G = so(4)+so(3,7): dims of commutant / antilinear / bilinear / sesquilinear
     = 2/2/2/2; all forms purely cross-chirality; antilinear channel classified
     (preserve vs swap) and its per-block squares reported; NO chirality-swapping equivariant
     antilinear may exist (else: REPORT -- potential escape).
 (3) S-level antilinear commutant of Cl(7,7): C C-bar = +1 (REAL type, M(128,R)) -- the
     real/pseudoreal fork of items (1)/(2); contrast with Cl(9,5)'s quaternionic -1.  Both Z/2.
 (4) (14,0) control: all compressed generators anti-Hermitian => F = Id is an invariant
     DEFINITE sesquilinear form with nonzero chirality-diagonal blocks.
 (5) Weight peeling (14,0): joint Cartan spectrum of the carrier = the exact product multiset
     (triplet) x (doublet) x (16 + 16bar), all 192 joint weights distinct, chirality-aligned
     => Schur: End = 1^2+1^2 = 2, bilinear = 2, sesquilinear = 2, antilinear = 2.
"""
import time
import numpy as np
from itertools import combinations, product

T0 = time.time()
N, DIM = 14, 128
rng = np.random.default_rng(777)


# ------------------------------------------------------- my own gammas: recursive doubling
def gammas_recursive():
    """Cl(14,0) Hermitian generators by the standard doubling recursion (NOT Jordan-Wigner
    ordering): cl(2) = [sx, sy]; cl(n+2) = [sx (x) g for g in cl(n)] + [sy (x) I, sz (x) I]."""
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    G = [sx, sy]
    while len(G) < N:
        Iold = np.eye(G[0].shape[0], dtype=complex)
        G = [np.kron(sx, g) for g in G] + [np.kron(sy, Iold), np.kron(sz, Iold)]
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec4(i, j):
    M = np.zeros((4, 4), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def build(timelike):
    G = gammas_recursive()
    e = [(1j * G[a] if a in timelike else G[a]) for a in range(N)]
    I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)
    cerr = max(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                             - (2.0 * (-1.0 if a in timelike else 1.0) if a == b else 0.0) * I128))
               for a in range(N) for b in range(N))
    assert cerr < 1e-12, f"Clifford relations fail: {cerr:.2e}"
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    Jk = [np.kron(lvec4(a, b) + lvec4(c, d), I128) + np.kron(I4, S)
          for (a, b, c, d), S in zip(SD, Sig)]
    Cas = -(Jk[0] @ Jk[0] + Jk[1] @ Jk[1] + Jk[2] @ Jk[2])
    Cas = 0.5 * (Cas + Cas.conj().T)
    cw, cV = np.linalg.eigh(Cas)
    mask = np.abs(cw - cw.max()) < 1e-6
    W = cV[:, mask]
    assert abs(cw.max() - 8.0) < 1e-9 and W.shape[1] == 192
    Gamma = np.hstack([e[a] for a in range(N)])
    Wfull = np.zeros((N * DIM, 192), dtype=complex)
    Wfull[:4 * DIM, :] = W
    assert np.max(np.abs(Gamma @ Wfull)) < 1e-10
    gens = []
    for a, b in combinations(range(4), 2):
        gens.append(np.kron(lvec4(a, b), I128) + np.kron(I4, sgen(e, a, b)))
    for a, b in combinations(range(4, 14), 2):
        gens.append(np.kron(I4, sgen(e, a, b)))
    assert max(np.max(np.abs(g @ W - W @ (W.conj().T @ g @ W))) for g in gens) < 1e-9
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    Gc = W.conj().T @ np.kron(I4, om) @ W
    Gc = 0.5 * (Gc + Gc.conj().T)
    gev = np.linalg.eigvalsh(Gc)
    assert int((gev > 0.5).sum()) == 96 and int((gev < -0.5).sum()) == 96
    Gt = [W.conj().T @ g @ W for g in gens]
    return e, W, Gt, Gc, Jk


# ------------------------------------ independent Hom solver: successive SVD refinement
def solve_hom(As, Bs, label, tol=1e-6):
    n = As[0].shape[0]
    for _ in range(10):
        c = rng.uniform(0.4, 1.6, size=len(As)) * rng.choice([-1.0, 1.0], size=len(As))
        A = sum(x * m for x, m in zip(c, As))
        B = sum(x * m for x, m in zip(c, Bs))
        lamA, VA = np.linalg.eig(A)
        lamB, VB = np.linalg.eig(B)
        dAA = np.abs(lamA[:, None] - lamA[None, :])
        dBB = np.abs(lamB[:, None] - lamB[None, :])
        dAB = np.abs(lamA[:, None] - lamB[None, :])
        if not any(((d > tol) & (d < 50 * tol)).any() for d in (dAA, dBB, dAB)):
            break
    VAi, VBi = np.linalg.inv(VA), np.linalg.inv(VB)
    ks, ls = np.nonzero(dAB < tol)
    nv = len(ks)
    if nv == 0:
        print(f"  [{label:40s}] match set empty => dim 0")
        return []
    basis = np.eye(nv, dtype=complex)                      # coefficients over support vars
    for _ in range(6):                                     # successive refinement, fresh probes
        cc = rng.standard_normal(len(As))
        Ai = sum(x * m for x, m in zip(cc, As))
        Bi = sum(x * m for x, m in zip(cc, Bs))
        At, Bt = VAi @ Ai @ VA, VBi @ Bi @ VB
        k = basis.shape[1]
        if k == 0:
            break
        Rmat = np.zeros((n * n, k), dtype=complex)
        for col in range(k):
            Xt = np.zeros((n, n), dtype=complex)
            Xt[ks, ls] = basis[:, col]
            Rmat[:, col] = (Xt @ Bt - At @ Xt).ravel()
        if k == 1:
            if np.linalg.norm(Rmat) > 1e-6:
                basis = basis[:, :0]
            continue
        u, s, vh = np.linalg.svd(Rmat, full_matrices=False)
        keep = s < 1e-8 * max(1.0, s.max())
        basis = basis @ vh[keep].conj().T
    Xs = []
    for col in range(basis.shape[1]):
        Xt = np.zeros((n, n), dtype=complex)
        Xt[ks, ls] = basis[:, col]
        X = VA @ Xt @ VBi
        Xs.append(X / np.linalg.norm(X))
    worst = 0.0
    if Xs:
        Xst = np.stack(Xs)
        for Ai, Bi in zip(As, Bs):                          # verify against ALL generators
            worst = max(worst, float(np.linalg.norm(Xst @ Bi - Ai @ Xst, axis=(1, 2)).max()))
        assert worst < 1e-6, f"{label}: residual {worst:.2e}"
    print(f"  [{label:40s}] dim = {len(Xs)}  (max residual over ALL gens {worst:.2e})")
    return Xs


print("=" * 98)
print("(1)+(2)  Cl(7,7) carrier and census   [timelike = {7..13}; internal so(3,7); M(128,R)]")
print("=" * 98)
TL77 = set(range(7, 14))
e7, W7, G7, Gc7, Jk7 = build(TL77)
I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)

# Krein form: product of spacelike gammas on S (fall back to timelike product if needed)
for cand in ("spacelike", "timelike"):
    idxs = [a for a in range(N) if (a not in TL77) == (cand == "spacelike")]
    bS = I128.copy()
    for a in idxs:
        bS = bS @ e7[a]
    if np.linalg.norm(bS.conj().T - bS) > 1e-9:
        bS = 1j * bS if np.linalg.norm((1j * bS).conj().T - (1j * bS)) < 1e-9 else bS
    K = np.kron(I4, bS)
    gens512 = []
    for a, b in combinations(range(4), 2):
        gens512.append(np.kron(lvec4(a, b), I128) + np.kron(I4, sgen(e7, a, b)))
    for a, b in combinations(range(4, 14), 2):
        gens512.append(np.kron(I4, sgen(e7, a, b)))
    kinv = max(np.max(np.abs(g.conj().T @ K + K @ g)) for g in gens512)
    if kinv < 1e-9:
        break
Kc = W7.conj().T @ K @ W7
Kc = 0.5 * (Kc + Kc.conj().T)
kev = np.linalg.eigvalsh(Kc)
ksig = (int((kev > 1e-8).sum()), int((kev < -1e-8).sum()))
Pp7, Pm7 = (np.eye(192) + Gc7) / 2, (np.eye(192) - Gc7) / 2
kblk = max(np.linalg.norm(Pp7 @ Kc @ Pp7), np.linalg.norm(Pm7 @ Kc @ Pm7))
print(f"  Krein ({cand} product): invariance {kinv:.2e}; signature (+{ksig[0]},-{ksig[1]}); "
      f"same-chirality blocks {kblk:.2e}")
assert ksig == (96, 96) and kblk < 1e-8

comm = solve_hom(G7, G7, "Cl(7,7): linear commutant")
anti = solve_hom(G7, [g.conj() for g in G7], "Cl(7,7): antilinear intertwiners")
bil = solve_hom([-g.T for g in G7], G7, "Cl(7,7): invariant bilinear forms")
ses = solve_hom([-g.conj().T for g in G7], G7, "Cl(7,7): invariant sesquilinear forms")
assert len(comm) == 2 and len(anti) == 2 and len(bil) == 2 and len(ses) == 2

worst_bil = max(max(np.linalg.norm(Pp7.T @ B @ Pp7), np.linalg.norm(Pm7.T @ B @ Pm7)) for B in bil)
worst_ses = max(max(np.linalg.norm(Pp7 @ F @ Pp7), np.linalg.norm(Pm7 @ F @ Pm7)) for F in ses)
worst_off = max(max(np.linalg.norm(Pp7 @ X @ Pm7), np.linalg.norm(Pm7 @ X @ Pp7)) for X in comm)
print(f"  bilinear same-chirality blocks max {worst_bil:.2e}; sesquilinear {worst_ses:.2e}; "
      f"commutant off-diagonal {worst_off:.2e}")
assert worst_bil < 1e-8 and worst_ses < 1e-8 and worst_off < 1e-8

n_swap = 0
for i, M in enumerate(anti):
    sw = np.linalg.norm(Gc7 @ M + M @ Gc7.conj())
    pv = np.linalg.norm(Gc7 @ M - M @ Gc7.conj())
    assert min(sw, pv) < 1e-8
    n_swap += int(sw < 1e-8)
    Mn = M / np.linalg.norm(M) * np.sqrt(192)
    C2 = Mn @ Mn.conj()
    cp = (np.trace(Pp7 @ C2) / 96).real
    cm = (np.trace(Pm7 @ C2) / 96).real
    print(f"  antilinear #{i}: {'SWAP' if sw < 1e-8 else 'PRESERVE'};  "
          f"C^2 = ({cp:+.3f}) P+ + ({cm:+.3f}) P-")
print(f"  chirality-swapping equivariant antilinears: {n_swap} (0 => no re-grading escape in (7,7))")
assert n_swap == 0

print("\n" + "=" * 98)
print("(3)  Cl(7,7) S-level antilinear commutant: real type (M(128,R)) -- the item (1)/(2) fork")
print("=" * 98)
words7 = [e7[a] for a in range(N)] + [e7[a] @ e7[b] for a, b in combinations(range(N), 2)][:40]
CS7 = solve_hom(words7, [w.conj() for w in words7], "Cl(7,7) antilinear commutant on S")
assert len(CS7) == 1
C7 = CS7[0] * np.sqrt(DIM)
s7 = (np.trace(C7 @ C7.conj()) / DIM).real
print(f"  C C-bar = {s7:+.4f} I  =>  REAL structure (+1): Cl(7,7) = M(128,R); the mod-2 real/")
print("  pseudoreal wall (item 2).  Contrast Cl(9,5) = M(64,H): -1 (Kramers, item 1).  Both Z/2.")
assert s7 > 0

print("\n" + "=" * 98)
print("(4)+(5)  Euclidean (14,0) control + exact weight-peeling Schur count")
print("=" * 98)
e0, W0, G0, Gc0, Jk0 = build(set())
ah = max(np.max(np.abs(g + g.conj().T)) for g in G0)
Pp0, Pm0 = (np.eye(192) + Gc0) / 2, (np.eye(192) - Gc0) / 2
print(f"  all 51 compressed generators anti-Hermitian: max ||g + g^dag|| = {ah:.2e}")
assert ah < 1e-9
print("  => F = Id is an invariant sesquilinear form: DEFINITE, signature (+192, 0), with")
print(f"     chirality-diagonal blocks ||P+ F P+|| = {np.linalg.norm(Pp0 @ np.eye(192) @ Pp0):.1f}"
      f" != 0: the (14,0) grading-aligned CONTROL (the paper's |chi| = 96 detector) --")
print("     the cross-chirality verdicts in (9,5)/(7,7) are signature-sensitive, not a method artifact.")

# weight peeling: 7 commuting Cartans (su(2)+, su(2)-, five internal rotations)
ASD = np.kron(lvec4(0, 1) - lvec4(2, 3), np.eye(DIM, dtype=complex)) \
    + np.kron(np.eye(4, dtype=complex), sgen(e0, 0, 1) - sgen(e0, 2, 3))
carts512 = [Jk0[0], ASD] + [np.kron(np.eye(4, dtype=complex), sgen(e0, a, a + 1))
                            for a in (4, 6, 8, 10, 12)]
carts = [W0.conj().T @ h @ W0 for h in carts512]
cerr = max(np.max(np.abs(h1 @ h2 - h2 @ h1)) for h1 in carts for h2 in carts)
assert cerr < 1e-9
A = sum(r * h for r, h in zip(rng.uniform(0.5, 1.5, 7), carts))
lam, V = np.linalg.eig(A)
w = np.zeros((192, 7))
for i in range(192):
    v = V[:, i]
    v = v / np.linalg.norm(v)
    for j, h in enumerate(carts):
        w[i, j] = (v.conj() @ (h @ v)).imag       # anti-Hermitian: eigenvalue = i * weight
w2 = 2.0 * w                                      # doubled weights should be integers (x scale)
scale1 = np.max(np.abs(w2[:, 0])) / 4.0           # su(2)+ doubled triplet weights {-4,0,4}?
w2[:, 0] = w2[:, 0] / np.max(np.abs(w2[:, 0])) * 2.0   # normalize su(2)+ to {-2, 0, +2}
w2[:, 1] = w2[:, 1] / np.max(np.abs(w2[:, 1])) * 1.0   # su(2)- doublet to {-1, +1}
for j in range(2, 7):
    w2[:, j] = w2[:, j] / np.max(np.abs(w2[:, j])) * 1.0   # spinor components to {-1, +1}
rounded = np.round(w2)
qerr = np.max(np.abs(w2 - rounded))
print(f"  joint Cartan weights quantization error after normalization = {qerr:.2e}")
assert qerr < 1e-6
tuples = [tuple(int(x) for x in row) for row in rounded]
assert len(set(tuples)) == 192, "joint weights must be simple (all distinct)"
exp16 = [s for s in product([1, -1], repeat=5) if s.count(-1) % 2 == 0]
exp16b = [s for s in product([1, -1], repeat=5) if s.count(-1) % 2 == 1]
chirs = [int(np.sign((V[:, i].conj() @ (Gc0 @ V[:, i])).real)) for i in range(192)]
setP = sorted(t for t, ch in zip(tuples, chirs) if ch > 0)
setM = sorted(t for t, ch in zip(tuples, chirs) if ch < 0)
expP = sorted((a, b) + s for a in (-2, 0, 2) for b in (-1, 1) for s in exp16)
expM = sorted((a, b) + s for a in (-2, 0, 2) for b in (-1, 1) for s in exp16b)
okP, okM = (setP == expP or setP == expM), (setM == expM or setM == expP)
print(f"  W_+ weight multiset == (triplet)x(doublet)x(16 or 16bar): {okP};  W_- likewise: {okM}")
assert okP and okM and setP != setM
print("""  => EXACT Schur count from the certified decomposition W = (3,2,16) (+) (3,2,16bar),
     both multiplicity 1, inequivalent, conjugate/dual to each other:
       End_G(W) = 1^2 + 1^2 = 2;  bilinear = 2;  sesquilinear = 2;  antilinear = 2
     -- independently reproducing the main census dimensions (2/2/2/2).""")

print("\n" + "#" * 98)
print("# INDEPENDENT CHECK: PASS.  Cl(7,7) census reproduces 2/2/2/2, all forms cross-chirality,")
print("# no antilinear re-grading; S-level fork lands REAL (+1) as M(128,R) requires (item 2);")
print("# (14,0) control detects chirality-diagonal forms; weight-peeling Schur count matches.")
print("#" * 98)
print(f"  total runtime: {time.time() - T0:.1f}s")
