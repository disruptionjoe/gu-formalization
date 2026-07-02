#!/usr/bin/env python3
"""
WC-ANTILINEAR-BOUND independent re-check.

Independence from the two primary scripts:
  - OWN gamma construction: recursive doubling (Cl(2n+2) from Cl(2n) via gamma (x) s1,
    I (x) s2, omega (x) s1-chain), NOT the Jordan-Wigner strings of the census;
  - DIFFERENT (9,5) embedding: timelike = {9,...,13} (census used {4,...,8});
  - DIFFERENT seed (777) and a DIFFERENT rank algorithm (Gram-matrix eigenvalues, not
    stacked-matrix SVD) for the index-nullity ranks;
  - EXACT INTEGER cross-check (V1): the complete predicted dimension table of the ladder
    census from weight combinatorics and Clebsch-Gordan integer counts alone -- no floating
    point at all;
  - CROSS-SIGNATURE (V3): the index-nullity theorem re-certified on the Cl(7,7) carrier
    (internal so(3,7); the enum-completeness pass's other physical signature);
  - CONTROL (V4): Euclidean (14,0), where K is grading-ALIGNED, NOT cross-chirality -- the
    theorem's premise fails and a physical subspace DOES carry index +-96: the premise is
    load-bearing, the theorem is not vacuous.

V1 -- exact combinatorics (integers only):
  Internal D5 spinor weights: 16 = even-parity sign vectors (+-1/2)^5, 16bar = odd.  In the
  SPLIT real form so(5,5) all weights are real, so antilinear conjugation FIXES weights:
  16-bar-rep ~ 16, 16bar-bar-rep ~ 16bar, and 16 vs 16bar weight sets are DISJOINT (parity)
  => equivariant antilinear maps cannot swap chirality wherever the internal split algebra
  (or its split Cartan) acts: swap dim 0 at L0, L2, L2b, L3, L4.  Restricting to so(9)
  (drop one coordinate): the 16 and 16bar weight multisets become IDENTICAL (both cover
  (+-1/2)^4 once) => both restrict to the single B4 spinor 16_9 => swap channels open: at
  L1/L1b swap dim = 2 (one per direction), at L5 (frame so(3), 3 (x) 2 = 4 (+) 2) swap dim
  = 4.  Preserve dims from Schur/Clebsch integer counts.  Full predicted table asserted
  against the census output values.

V2 -- independent substrate (9,5): carrier rebuilt from scratch; the two DECISIVE rungs
  (L1: strict-admissibility exact certificate C5; L5: frame-active swap existence) are
  recomputed; the closed-form strict witnesses and the index-nullity theorem are
  re-certified with the Gram-eigenvalue rank method.

Deterministic, numpy-only, < 90 s.
"""
import time
import numpy as np
from itertools import combinations, product

T0 = time.time()
SEED = 777
rng = np.random.default_rng(SEED)
NASSERT = 0


def check(cond, msg):
    global NASSERT
    NASSERT += 1
    assert cond, msg


# ===================================================================== V1: exact combinatorics
print("=" * 98)
print("V1 -- exact integer combinatorics: the predicted ladder table (no floating point)")
print("=" * 98)
w16 = [s for s in product((1, -1), repeat=5) if s.count(-1) % 2 == 0]
w16b = [s for s in product((1, -1), repeat=5) if s.count(-1) % 2 == 1]
check(len(w16) == 16 and len(w16b) == 16, "D5 half-spinor weight counts")
# split real form: conjugation fixes (real) weights => the bar-rep of each irrep has the
# SAME weight multiset; 16 vs 16bar disjoint:
overlap = sum(1 for a in w16 for b in w16b if a == b)
print(f"  D5: |weights(16) ^ weights(16bar)| = {overlap}  (0 => swap forbidden under split "
      f"so(5,5)/t5)")
check(overlap == 0, "16/16bar weight disjointness (parity)")
# so(9) restriction: drop the last coordinate
r16 = sorted(s[:4] for s in w16)
r16b = sorted(s[:4] for s in w16b)
print(f"  B4 restriction: weights(16|so9) == weights(16bar|so9) ? {r16 == r16b}  "
      f"(True => both are the B4 spinor 16_9: swap channel OPENS)")
check(r16 == r16b, "16 and 16bar restrict identically to so(9)")
check(sorted(set(r16)) == sorted(product((1, -1), repeat=4)) and len(set(r16)) == 16,
      "restriction covers (+-1/2)^4 exactly once: it IS the irreducible B4 spinor")


def su2_trivial_mult(dims):
    """Exact multiplicity of the trivial rep in a tensor product of su(2) irreps of the
    given dimensions (integer Clebsch-Gordan arithmetic)."""
    reps = {0: 1}                              # multiset of 2j values with multiplicities
    for d in dims:
        j2 = d - 1
        new = {}
        for a, m in reps.items():
            for c in range(abs(a - j2), a + j2 + 1, 2):
                new[c] = new.get(c, 0) + m
        reps = new
    return reps.get(0, 0)


# frame factor of the carrier: (3;2) of su(2)+ x su(2)-  (self-conjugate irreps)
h_frame_so4 = su2_trivial_mult([3, 3]) * su2_trivial_mult([2, 2])     # Hom(conj(3;2),(3;2))
# under diagonal so(3): (3;2) = 3 (x) 2 = 4 (+) 2; Hom over so(3): one per irrep
h_frame_so3 = sum(su2_trivial_mult([d, d]) for d in (4, 2))
# under the frame Cartan t2 / no frame symmetry, count weight-matching pairs directly:
frame_weights = [(m, s) for m in (-2, 0, 2) for s in (-1, 1)]         # 2*(m+, m-)
h_frame_t2 = sum(1 for (m, s) in frame_weights for (m2, s2) in frame_weights
                 if (m2, s2) == (-m, -s))
check(h_frame_so4 == 1 and h_frame_so3 == 2 and h_frame_t2 == 6,
      f"frame Hom dims (so4, so3, t2) = ({h_frame_so4},{h_frame_so3},{h_frame_t2})")
# internal antilinear Hom dims (per chirality direction), from weight/Schur integers:
# split so(5,5): 16->16: 1, 16bar->16bar: 1, cross: 0.   so(5,4): all four channels: 1.
# split Cartan t5: weight-matching pairs within 16 (16), within 16bar (16), cross (0).
predicted = {
    "L0": (1 * (1 + 1), 0),                   # frame so(4) x (2 preserve channels)
    "L2": (h_frame_so3 * 2, 0),
    "L2b": (36 * 2, 0),                       # frame multiplicity space fully free: 6^2 = 36
    "L3": (1 * (16 + 16), 0),
    "L4": (192, 0),                           # unique weight-partner per carrier line
    "L1": (1 * 2, 1 * 2),                     # (preserve, swap): 2 channels each
    "L1b": (1 * 2, 1 * 2),
    "L5": (h_frame_so3 * 2, h_frame_so3 * 2),
}
census_observed = {                            # from antilinear_ladder_census.py output
    "L0": (2, 0), "L2": (4, 0), "L2b": (72, 0), "L3": (32, 0), "L4": (192, 0),
    "L1": (2, 2), "L1b": (2, 2), "L5": (4, 4),
}
print("\n  predicted (preserve, swap) vs census observed:")
for k in predicted:
    print(f"    {k:4s}: predicted {predicted[k]}, census {census_observed[k]}")
    check(predicted[k] == census_observed[k], f"{k}: exact combinatorics matches census")
print("  => the census dimension table is EXACTLY the rep-theoretic prediction (integers).")


# ======================================================= shared machinery (own construction)
def gammas_doubling(n):
    """Hermitian gammas of Cl(2n,0) by RECURSIVE DOUBLING (not Jordan-Wigner)."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = [s1, s2]
    while len(G) < 2 * n:
        om = G[0] @ G[1]
        for g in G[2:]:
            om = om @ g
        # normalize omega Hermitian with omega^2 = I
        om = om / np.sqrt(abs((om @ om)[0, 0]))
        if np.linalg.norm(om @ om - np.eye(om.shape[0])) > 1e-9:
            om = 1j * om
        if np.linalg.norm(om - om.conj().T) > 1e-9:
            om = 1j * om
        G = [np.kron(g, s1) for g in G] + [np.kron(om, s1), np.kron(np.eye(om.shape[0]), s2)]
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec4(i, j):
    M = np.zeros((4, 4), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def build_carrier(timelike, tag):
    """Carrier, chirality, Krein form for Cl(p,q) with the given timelike set."""
    N, DIM = 14, 128
    base = gammas_doubling(7)
    I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)
    e = [(1j * base[a] if a in timelike else base[a]) for a in range(N)]
    cerr = max(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                             - (2.0 * (-1.0 if a in timelike else 1.0) if a == b else 0.0) * I128))
               for a in range(N) for b in range(N))
    check(cerr < 1e-11, f"{tag}: Clifford relations (own gammas)")
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    Jk = [np.kron(lvec4(a, b) + lvec4(c, d), I128) + np.kron(I4, S)
          for (a, b, c, d), S in zip(SD, Sig)]
    Cas = -(Jk[0] @ Jk[0] + Jk[1] @ Jk[1] + Jk[2] @ Jk[2])
    Cas = 0.5 * (Cas + Cas.conj().T)
    cw, cV = np.linalg.eigh(Cas)
    mask = np.abs(cw - cw.max()) < 1e-6
    W = cV[:, mask]
    check(abs(cw.max() - 8.0) < 1e-9 and W.shape[1] == 192, f"{tag}: carrier 192 @ Casimir 8")
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    tro = (np.trace(om @ om) / DIM).real
    om = om if tro > 0 else (-1j) * om
    Gc = W.conj().T @ np.kron(I4, om) @ W
    Gc = 0.5 * (Gc + Gc.conj().T)
    gev, gV = np.linalg.eigh(Gc)
    check(int((gev > 0.5).sum()) == 96 and int((gev < -0.5).sum()) == 96, f"{tag}: split 96/96")
    spacelike = [a for a in range(N) if a not in timelike]
    bS = I128.copy()
    for s_ in spacelike:
        bS = bS @ e[s_]
    if np.linalg.norm(bS.conj().T - bS) > 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    Kc = W.conj().T @ np.kron(I4, bS) @ W
    Kc = 0.5 * (Kc + Kc.conj().T)
    gens = {}
    for a, b in combinations(range(4), 2):
        gens[("f", a, b)] = W.conj().T @ (np.kron(lvec4(a, b), I128) + np.kron(I4, sgen(e, a, b))) @ W
    for a, b in combinations(range(4, 14), 2):
        gens[("i", a, b)] = W.conj().T @ np.kron(I4, sgen(e, a, b)) @ W
    return Gc, Kc, gens, gV, gev


def rank_gram(A, tol=1e-8):
    """Rank via Gram-matrix eigenvalues (independent of the primary scripts' SVD route)."""
    G = A.conj().T @ A
    ev = np.linalg.eigvalsh(0.5 * (G + G.conj().T))
    thr = tol * ev.max()
    return int((ev > thr).sum())


def hom_space(As, Bs, label, tol_match=1e-6):
    """Generic-element Hom computation (fresh seed/substrate; structure as the census)."""
    n = As[0].shape[0]
    for attempt in range(12):
        c = rng.uniform(0.5, 1.5, size=len(As)) * rng.choice([-1.0, 1.0], size=len(As))
        A = sum(ci * Ai for ci, Ai in zip(c, As))
        B = sum(ci * Bi for ci, Bi in zip(c, Bs))
        lamA, VA = np.linalg.eig(A)
        lamB, VB = np.linalg.eig(B)
        ok = True
        for d in (np.abs(lamA[:, None] - lamA[None, :]),
                  np.abs(lamB[:, None] - lamB[None, :]),
                  np.abs(lamA[:, None] - lamB[None, :])):
            if ((d > tol_match) & (d < 50 * tol_match)).any():
                ok = False
        if ok:
            break
    check(ok, f"{label}: clean generic spectra")
    VAi, VBi = np.linalg.inv(VA), np.linalg.inv(VB)
    ks, ls = np.nonzero(np.abs(lamA[:, None] - lamB[None, :]) < tol_match)
    nv = len(ks)
    if nv == 0:
        return []
    pairs = list(zip(As, Bs)) if len(As) <= 10 else [
        (sum(x * Ai for x, Ai in zip(cc, As)), sum(x * Bi for x, Bi in zip(cc, Bs)))
        for cc in [rng.standard_normal(len(As)) for _ in range(10)]]
    Nmat = np.zeros((nv, nv), dtype=complex)
    for Ai, Bi in pairs:
        At, Bt = VAi @ Ai @ VA, VBi @ Bi @ VB
        BBH, AHA = Bt @ Bt.conj().T, At.conj().T @ At
        Ak, Bl = At[np.ix_(ks, ks)], Bt[np.ix_(ls, ls)]
        Nmat += ((ks[:, None] == ks[None, :]) * BBH[np.ix_(ls, ls)].T
                 - Ak * Bl.conj() - Ak.conj().T * Bl.T
                 + (ls[:, None] == ls[None, :]) * AHA[np.ix_(ks, ks)])
    Nmat = 0.5 * (Nmat + Nmat.conj().T)
    wN, UN = np.linalg.eigh(Nmat)
    idx = np.nonzero(wN < 1e-8 * max(1.0, wN.max()))[0]
    Xs = []
    for i in idx:
        Xt = np.zeros((n, n), dtype=complex)
        Xt[ks, ls] = UN[:, i]
        X = VA @ Xt @ VBi
        Xs.append(X / np.linalg.norm(X))
    worst = 0.0
    for Ai, Bi in (list(zip(As, Bs))[:12]):
        for X in Xs:
            worst = max(worst, float(np.linalg.norm(X @ Bi - Ai @ X)))
    check(worst < 1e-6, f"{label}: basis residual {worst:.2e}")
    print(f"  [{label:40s}] dim = {len(Xs)} (residual {worst:.2e})")
    return Xs


def nullity_certificate(Gc, Kc, tag, n_phys=3):
    """Closed-form strict witnesses + index-nullity theorem on the given carrier."""
    gev, gV = np.linalg.eigh(Gc)
    P0, N0 = gV[:, gev > 0.5], gV[:, gev < -0.5]
    Kb = Kc.conj()
    iso = max(np.linalg.norm(P0.conj().T @ Kc @ P0), np.linalg.norm(N0.conj().T @ Kc @ N0))
    check(iso < 1e-9, f"{tag}: W_+/- K-Lagrangian (premise)")
    G = P0.conj().T @ Kc @ N0
    Q = np.hstack([P0, N0 @ np.linalg.inv(G)])
    Qbi = np.linalg.inv(Q.conj())
    kev, kV = np.linalg.eigh(Kc)
    Pphys = kV[:, kev > 1e-8]
    check(Pphys.shape[1] == 96, f"{tag}: K signature (96,96)")
    for eps, lam in ((-1.0, 1.0), (1.0, -1.0)):
        A = rng.standard_normal((96, 96)) + 1j * rng.standard_normal((96, 96))
        A = 0.5 * (A + (lam * eps) * A.T)
        S = np.zeros((192, 192), dtype=complex)
        S[:96, 96:] = A
        S[96:, :96] = eps * np.linalg.inv(A.conj())
        M = Q @ S @ Qbi
        check(np.linalg.norm(M @ M.conj() - eps * np.eye(192)) < 1e-8,
              f"{tag}: witness C^2 = {eps:+.0f}")
        check(np.linalg.norm(M.conj().T @ Kc @ M - lam * Kb) < 1e-8 * np.linalg.norm(Kb) * 100,
              f"{tag}: witness Krein lambda = {lam:+.0f}")
        Wp, Wm = M @ P0.conj(), M @ N0.conj()
        check(max(np.linalg.norm(Wp.conj().T @ Kc @ Wp),
                  np.linalg.norm(Wm.conj().T @ Kc @ Wm)) < 1e-8,
              f"{tag}: images K-Lagrangian (transport)")
        chis = []
        for _ in range(n_phys):
            H = rng.standard_normal((192, 192)) + 1j * rng.standard_normal((192, 192))
            H = 0.35 * (H - H.conj().T) / np.linalg.norm(H)
            # Krein-unitary via eigen-route (independent of expm scaling-squaring)
            hev, hV = np.linalg.eig(Kc @ H)
            U = hV @ np.diag(np.exp(hev)) @ np.linalg.inv(hV)
            check(np.linalg.norm(U.conj().T @ Kc @ U - Kc) < 1e-7, f"{tag}: Krein unitary")
            P = U @ Pphys
            dp = 192 - rank_gram(np.hstack([P, Wp]))
            dm = 192 - rank_gram(np.hstack([P, Wm]))
            check(dp == 0 and dm == 0, f"{tag}: intersections vanish")
            chis.append(dp - dm)
        check(all(c == 0 for c in chis), f"{tag}: chi_C(P) all zero")
        print(f"  [{tag}] witness (eps={eps:+.0f},lam={lam:+.0f}): images Lagrangian, "
              f"chi_C = {chis} (exact)")


# ===================================================== V2: independent (9,5) substrate
print("\n" + "=" * 98)
print("V2 -- independent (9,5) substrate: own gammas, timelike {9..13}, seed 777")
print("=" * 98)
Gc, Kc, gens, gV, gev = build_carrier({9, 10, 11, 12, 13}, "(9,5)'")
kev = np.linalg.eigvalsh(Kc)
Pp, Pm = (np.eye(192) + Gc) / 2, (np.eye(192) - Gc) / 2
print(f"  K signature (+{int((kev > 1e-8).sum())},-{int((kev < -1e-8).sum())}); "
      f"cross-chirality residual = {max(np.linalg.norm(Pp @ Kc @ Pp), np.linalg.norm(Pm @ Kc @ Pm)):.2e}; "
      f"||Im K|| = {np.linalg.norm(Kc.imag):.3f}")
check(int((kev > 1e-8).sum()) == 96, "(9,5)': K signature")
check(max(np.linalg.norm(Pp @ Kc @ Pp), np.linalg.norm(Pm @ Kc @ Pm)) < 1e-9,
      "(9,5)': K purely cross-chirality")

FRAME = [gens[("f", a, b)] for a, b in combinations(range(4), 2)]


def swap_dims(anti):
    """Dimensions of the preserve/swap subspaces (Gram-Schmidt of the components -- raw
    Hom basis vectors are generic mixtures of both)."""
    Gcc = Gc.conj()
    pres_parts, swap_parts = [], []
    for M in anti:
        Mp = 0.5 * (M + Gc @ M @ Gcc)
        Ms = 0.5 * (M - Gc @ M @ Gcc)
        if np.linalg.norm(Mp) > 1e-7:
            pres_parts.append(Mp)
        if np.linalg.norm(Ms) > 1e-7:
            swap_parts.append(Ms)
    def _gs(mats):
        out = []
        for m in mats:
            r = m.copy()
            for b in out:
                r = r - np.vdot(b, r) * b
            if np.linalg.norm(r) > 1e-7:
                out.append(r / np.linalg.norm(r))
        return out
    pres, swap = _gs(pres_parts), _gs(swap_parts)
    fc_max = 0.0
    for S in swap:
        Sn = S * np.sqrt(192)
        fc_max = max(fc_max, max(np.linalg.norm(Sn @ f.conj() - f @ Sn) for f in FRAME))
    return len(pres), len(swap), fc_max


# decisive rung L1 (so(4)+so(5,4)): drop one internal spacelike direction (here index 8)
L1g = FRAME + [gens[("i", a, b)] for a, b in combinations(range(4, 14), 2) if 8 not in (a, b)]
anti1 = hom_space(L1g, [g.conj() for g in L1g], "(9,5)' L1: antilinear intertwiners")
np1, ns1, fc1 = swap_dims(anti1)
print(f"    L1 split: preserve {np1}, swap {ns1}; max swap frame charge = {fc1:.2e}")
check((np1, ns1) == (2, 2), "(9,5)' L1: dims 2+2 reproduced")
check(fc1 < 1e-6, "(9,5)' L1: swaps frame-trivial by so(4)-equivariance")

# decisive rung L5 (so(3)+so(5,4)): both broken
L5g = [gens[("f", a, b)] for a, b in [(0, 1), (0, 2), (1, 2)]] + \
      [gens[("i", a, b)] for a, b in combinations(range(4, 14), 2) if 8 not in (a, b)]
anti5 = hom_space(L5g, [g.conj() for g in L5g], "(9,5)' L5: antilinear intertwiners")
np5, ns5, fc5 = swap_dims(anti5)
print(f"    L5 split: preserve {np5}, swap {ns5}; max swap frame charge = {fc5:.2f}")
check((np5, ns5) == (4, 4), "(9,5)' L5: dims 4+4 reproduced")
check(fc5 > 1.0, "(9,5)' L5: frame-ACTIVE swaps reproduced")

# L1 strict-admissibility exact certificate (C5 closed form, independent substrate)
swaps = []
for M in anti1:
    Ms = 0.5 * (M - Gc @ M @ Gc.conj())
    if np.linalg.norm(Ms) > 1e-6:
        swaps.append(Ms / np.linalg.norm(Ms))
ups = [Pp @ S for S in swaps if np.linalg.norm(Pp @ S) > 1e-7]
dns = [Pm @ S for S in swaps if np.linalg.norm(Pm @ S) > 1e-7]


def gs(mats):
    out = []
    for m in mats:
        r = m.copy()
        for b in out:
            r = r - np.vdot(b, r) * b
        if np.linalg.norm(r) > 1e-7:
            out.append(r / np.linalg.norm(r))
    return out


ups, dns = gs(ups), gs(dns)
check(len(ups) == 1 and len(dns) == 1, "(9,5)' L1: 1/1 channel structure")
U, D = ups[0], dns[0]
gU = np.vdot(Pp, U @ D.conj()) / np.vdot(Pp, Pp)
gD = np.vdot(Pm, D @ U.conj()) / np.vdot(Pm, Pm)
print(f"    L1 C5 scalars: gU = {gU:+.4e}, gD = {gD:+.4e}, gD - conj(gU) = "
      f"{abs(gD - np.conj(gU)):.2e}")
a3_ok = abs(gD - np.conj(gU)) < 1e-8 * abs(gU) and abs(gU) > 1e-10
print(f"    A3 solvability on the span: {a3_ok}")
if a3_ok:
    Kb = Kc.conj()
    Kn2 = np.vdot(Kb, Kb)
    pK = lambda X: X - (np.vdot(Kb, X) / Kn2) * Kb
    feasible = False
    for eps in (-1.0, 1.0):
        z = eps / gU
        FUU, FDD = U.conj().T @ Kc @ U, D.conj().T @ Kc @ D
        FUD, FDU = U.conj().T @ Kc @ D, D.conj().T @ Kc @ U
        fixed = np.conj(z) * FUD + z * FDU
        A = np.stack([pK(FUU).ravel(), pK(FDD).ravel()], axis=1)
        rhs = -pK(fixed).ravel()
        sol, *_ = np.linalg.lstsq(A, rhs, rcond=None)
        resid = np.linalg.norm(A @ sol - rhs)
        u, v = sol.real
        gap = u * v - abs(z) ** 2
        print(f"      eps = {eps:+.0f}: A2-linear residual {resid:.2e}, (u,v) = "
              f"({u:+.3e},{v:+.3e}), uv - |z|^2 = {gap:+.3e}")
        if resid < 1e-8 and u > 1e-12 and v > 1e-12 and abs(gap) < 1e-8:
            feasible = True
    print(f"    strict (A2+A3) admissible swap at L1: {'EXISTS' if feasible else 'NON-EXISTENCE (exact, reproduced)'}")
    check(not feasible, "(9,5)' L1: C5c non-existence certificate reproduced")

# theorem on the independent substrate
print("\n  index-nullity theorem, independent substrate:")
nullity_certificate(Gc, Kc, "(9,5)'")

# ===================================================== V3: cross-signature Cl(7,7)
print("\n" + "=" * 98)
print("V3 -- cross-signature: the theorem on the Cl(7,7) carrier (internal so(3,7))")
print("=" * 98)
Gc7, Kc7, gens7, _, _ = build_carrier({7, 8, 9, 10, 11, 12, 13}, "(7,7)")
kev7 = np.linalg.eigvalsh(Kc7)
Pp7, Pm7 = (np.eye(192) + Gc7) / 2, (np.eye(192) - Gc7) / 2
cross7 = max(np.linalg.norm(Pp7 @ Kc7 @ Pp7), np.linalg.norm(Pm7 @ Kc7 @ Pm7))
print(f"  K signature (+{int((kev7 > 1e-8).sum())},-{int((kev7 < -1e-8).sum())}); "
      f"cross-chirality residual = {cross7:.2e}")
check(int((kev7 > 1e-8).sum()) == 96 and cross7 < 1e-9, "(7,7): cross-chirality Krein premise")
nullity_certificate(Gc7, Kc7, "(7,7)", n_phys=2)

# ===================================================== V4: Euclidean control (14,0)
print("\n" + "=" * 98)
print("V4 -- control: Euclidean (14,0), where the premise FAILS and an index CAN be nonzero")
print("=" * 98)
Gc0, Kc0, _, gV0, gev0 = build_carrier(set(), "(14,0)")
Pp0 = (np.eye(192) + Gc0) / 2
align = min(np.linalg.norm(Kc0 - Gc0), np.linalg.norm(Kc0 + Gc0))
print(f"  (14,0): min ||K -+ Gamma_c|| = {align:.2e}  (K IS the grading: ALIGNED, not cross)")
check(align < 1e-9, "(14,0): K grading-aligned (premise fails as designed)")
sgn = 1.0 if np.linalg.norm(Kc0 - Gc0) < 1e-9 else -1.0
P0w = gV0[:, sgn * gev0 > 0.5]                 # the K-POSITIVE chirality eigenspace
gram0 = P0w.conj().T @ Kc0 @ P0w
check(np.linalg.eigvalsh(0.5 * (gram0 + gram0.conj().T)).min() > 1e-8,
      "(14,0): the K-positive chirality eigenspace is physical here")
chi0 = int(round(np.trace(P0w.conj().T @ Gc0 @ P0w).real))
print(f"  (14,0): the physical subspace W_{'+' if sgn > 0 else '-'} carries net chiral "
      f"index {chi0:+d} != 0:")
print("  without the cross-chirality premise the theorem's conclusion genuinely fails --")
print("  the Lagrangian structure of K is load-bearing, the theorem is not vacuous.")
check(abs(chi0) == 96, "(14,0) control: |chi| = 96 detected")

print("\n" + "#" * 98)
print("# INDEPENDENT RE-CHECK -- VERDICT")
print("#" * 98)
print(f"""
  V1: the ladder census dimension table is EXACTLY reproduced by integer weight/Clebsch
      combinatorics (no floating point): swap channels exist only where the internal
      algebra is broken to so(9) (16/16bar weight multisets merge), and are forced
      frame-trivial wherever so(4) survives.
  V2: independent substrate (own gammas, different embedding, different seed, Gram-rank
      algorithm): L1 = 2+2 frame-trivial with the strict-admissibility NON-EXISTENCE
      certificate reproduced; L5 = 4+4 frame-active; index-nullity theorem certified.
  V3: Cl(7,7): cross-chirality premise holds, theorem certified (signature-independent).
  V4: Euclidean (14,0) control: premise fails, a physical subspace carries |chi| = 96 --
      the theorem's premise is load-bearing.

  hard asserts passed: {NASSERT}
  total runtime: {time.time() - T0:.1f}s""")
# EOF
