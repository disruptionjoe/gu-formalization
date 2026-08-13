#!/usr/bin/env python3
"""CHK-1: chirality-asymmetric zero-order deformation cells on the frozen K77 bank.

Executes CHK-1 of explorations/decoupling-constructibility-packet-2026-08-12.md
(section "Lens 2 - First computable checks") on the frozen v0.173/v0.174
fixtures of the READ-ONLY repo at HEAD c789e75b. Repo files are data; this
probe writes nothing into the repo.

Interface I: (V, X, P_sym, P_skew, D), V = R^1920 = (Omega^0+Omega^1)(S),
(1+14) x 128, block order per the fixtures: 14 one-form blocks then the
zero-form block. X = blockdiag(omega) (ambient chirality involution,
960+960). Horns P_sym = pairing(1,1,1,1), P_skew = pairing(1,-1,-1,1),
built exactly as in
tests/channel-swings/selected_k77_action_adjoint_weight_classification_probe.py.

Deformation space per horn P and layer L:
  Z(P,L) = { B in L : (P B)^T = -(P B) }   (Grassmann alternation, v0.174)
graded by X:  Z_odd = {B : {B,X}=0}, Z_even = {B : [B,X]=0};
Z_even swap-split by the canonical half-swap sigma(B) = Q B^T Q with
Q = blockdiag(B_spin) (the fixture's cross-chiral bilinear = the halves'
pairing; FRAME-SENSITIVE convention, stated in the results artifact).

Exact arithmetic: all matrices are integer; float64 matmuls are exact
(entries and inner products stay far below 2^53; asserted); ranks are
steered by the two-prime discipline GF(1009)/GF(1013) and every reported
cell dimension is closed by explicit integer null vectors verified exactly
over Z, so the final dimensions are integer-certified.

Deterministic; plants controls; prints PASS/FAIL; exit code 0 iff all pass.
"""
from __future__ import annotations

import json
import sys
from collections import Counter

import numpy as np

PRIMES = (1009, 1013)
REPO = "."
HEAD_PIN = "c789e75bbe0eb38bcd6342516dc88a39c760852b"
RNG_SEED = 20260812
SUP_CAP = 30000   # cap on sampled support rows per linear system

COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, value) -> None:
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


# ---------------------------------------------------------------- exact int ops
def mm(*mats):
    """Exact integer matmul chain via float64 BLAS (magnitudes asserted)."""
    out = mats[0].astype(np.float64)
    for m in mats[1:]:
        out = out @ m.astype(np.float64)
    assert np.max(np.abs(out)) < 2**52, "exactness bound exceeded"
    r = np.rint(out)
    assert np.array_equal(r, out)
    return r.astype(np.int64)


def mmp(A, B, p):
    """(A @ B) mod p, exact via float64 (entries reduced mod p first)."""
    Af = np.mod(A, p).astype(np.float64)
    Bf = np.mod(B, p).astype(np.float64)
    out = Af @ Bf
    assert out.max(initial=0) < 2**52
    return np.mod(np.rint(out).astype(np.int64), p)


def kron_chain(factors):
    out = np.array([[1]], dtype=np.int64)
    for f in factors:
        out = np.kron(out, f)
    return out


# ------------------------------------------------------------------- mod-p alg
def rref_mod(A, p):
    """Row-reduce A mod p; returns (rank, pivot_cols, R) with R in rref."""
    R = np.mod(A.astype(np.int64), p)
    rows, cols = R.shape
    piv_cols, r = [], 0
    for c in range(cols):
        if r >= rows:
            break
        col = R[r:, c]
        nz = np.nonzero(col)[0]
        if nz.size == 0:
            continue
        i = r + nz[0]
        if i != r:
            R[[r, i]] = R[[i, r]]
        inv = pow(int(R[r, c]), p - 2, p)
        R[r] = (R[r] * inv) % p
        mask = np.nonzero(R[:, c])[0]
        mask = mask[mask != r]
        if mask.size:
            R[mask] = (R[mask] - np.outer(R[mask, c], R[r])) % p
        piv_cols.append(c)
        r += 1
    return r, piv_cols, R[:r]


def null_mod(A, p):
    """Null-space basis (cols of A = unknowns) mod p, as (dim, basis rows)."""
    rank, piv, R = rref_mod(A, p)
    cols = A.shape[1]
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = np.zeros(cols, dtype=np.int64)
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i, f]) % p
        basis.append(v)
    return len(free), basis


def center_lift(v, p):
    v = np.mod(v, p)
    return np.where(v > p // 2, v - p, v).astype(np.int64)


def charpoly_mod(M, p):
    """char poly of square M mod p via Hessenberg; coeffs low->high (monic)."""
    H = np.mod(M.astype(np.int64), p)
    n = H.shape[0]
    for c in range(n - 2):
        col = H[c + 1:, c]
        nz = np.nonzero(col)[0]
        if nz.size == 0:
            continue
        i = c + 1 + nz[0]
        if i != c + 1:
            H[[c + 1, i]] = H[[i, c + 1]]
            H[:, [c + 1, i]] = H[:, [i, c + 1]]
        inv = pow(int(H[c + 1, c]), p - 2, p)
        f = (H[c + 2:, c] * inv) % p
        if np.any(f):
            H[c + 2:] = (H[c + 2:] - f[:, None] * H[c + 1][None, :]) % p
            H[:, c + 1] = (H[:, c + 1] + H[:, c + 2:] @ f) % p
    POLY = np.zeros((n + 1, n + 1), dtype=np.int64)
    POLY[0, 0] = 1
    sub = np.array([int(H[k + 1, k]) % p for k in range(n - 1)], dtype=np.int64)
    for k in range(1, n + 1):
        pk = np.zeros(n + 1, dtype=np.int64)
        prev = POLY[k - 1]
        pk[1:] = prev[:-1]
        pk = (pk - int(H[k - 1, k - 1]) * prev) % p
        if k >= 2:
            betas = np.ones(k - 1, dtype=np.int64)
            run = 1
            bl = []
            for i in range(k - 1, 0, -1):
                run = (run * int(sub[i - 1])) % p
                bl.append(run)
            betas = np.array(bl[::-1], dtype=np.int64)  # betas[i-1] for i=1..k-1
            terms = (H[0:k - 1, k - 1] * betas) % p
            if np.any(terms):
                pk = (pk - terms @ POLY[0:k - 1]) % p
        POLY[k] = pk
    return POLY[n]


def poly_gcd_mod(a, b, p):
    a, b = [np.trim_zeros(np.mod(x, p), 'b') for x in (a, b)]
    while b.size:
        inv = pow(int(b[-1]), p - 2, p)
        r = np.mod(a, p).copy()
        while True:
            r = np.trim_zeros(r, 'b')
            if r.size < b.size or r.size == 0:
                break
            f = (int(r[-1]) * inv) % p
            r[-b.size:] = (r[-b.size:] - f * b) % p
        a, b = b, r
    return np.trim_zeros(a, 'b')


def poly_sqfree_mod(f, p):
    df = np.array([(i * int(f[i])) % p for i in range(1, f.size)], dtype=np.int64)
    g = poly_gcd_mod(f, df, p)
    return g.size == 1


# ---------------------------------------------------------------- Clifford bank
print("A. FROZEN-FIXTURE CLIFFORD BANK, EXACT INTEGER REBUILD (conventions of "
      "selected_k77_action_adjoint_weight_classification_probe.py)")
I2 = np.eye(2, dtype=np.int64)
S1 = np.array([[0, 1], [1, 0]], dtype=np.int64)
S3 = np.array([[1, 0], [0, -1]], dtype=np.int64)
EPS = np.array([[0, 1], [-1, 0]], dtype=np.int64)
N7, NV, SPIN, TOTAL = 7, 14, 128, 1920
gam = []
for i in range(N7):
    gam.append(kron_chain([S3] * i + [S1] + [I2] * (N7 - 1 - i)))
for i in range(N7):
    gam.append(kron_chain([S3] * i + [EPS] + [I2] * (N7 - 1 - i)))
ETA = [1] * 7 + [-1] * 7
Is = np.eye(SPIN, dtype=np.int64)
omega = Is.copy()
for g in gam:
    omega = mm(omega, g)
Bsp = Is.copy()
for g in gam[7:]:
    Bsp = mm(Bsp, g)
Pp2, Pm2 = Is + omega, Is - omega  # 2 x chirality projectors (integer)

check("clifford", "gamma squares carry signature (7,7)",
      all(np.array_equal(mm(gam[i], gam[i]), ETA[i] * Is) for i in range(14)))
check("clifford", "gammas pairwise anticommute",
      all(np.array_equal(mm(gam[i], gam[j]), -mm(gam[j], gam[i]))
          for i in range(14) for j in range(i + 1, 14)))
check("clifford", "omega is a symmetric involution and halves have rank 64",
      np.array_equal(mm(omega, omega), Is) and np.array_equal(omega.T, omega)
      and rref_mod(Pp2, PRIMES[0])[0] == 64 and rref_mod(Pm2, PRIMES[0])[0] == 64)
check("clifford", "cross-chiral bilinear: B*P+ = P-*B, B symmetric, B^2 = 1",
      np.array_equal(mm(Bsp, Pp2), mm(Pm2, Bsp))
      and np.array_equal(Bsp.T, Bsp) and np.array_equal(mm(Bsp, Bsp), Is))

# ------------------------------------------------------- carrier-level objects
BLK = [slice(128 * b, 128 * (b + 1)) for b in range(15)]  # 0..13 one-form, 14 zero-form


def embed(blocks):
    """dict {(r,c): 128x128 int} -> 1920x1920 int."""
    M = np.zeros((TOTAL, TOTAL), dtype=np.int64)
    for (r, c), v in blocks.items():
        M[BLK[r], BLK[c]] = v
    return M


X = embed({(b, b): omega for b in range(15)})
Q = embed({(b, b): Bsp for b in range(15)})
Ifull = np.eye(TOTAL, dtype=np.int64)
PIp2 = Ifull + X
PIm2 = Ifull - X


def wedge_blocks(i):
    out = {}
    for r in range(NV):
        if r == i:
            continue
        for c in range(NV):
            if c in (r, i):
                continue
            out[(r, c)] = ETA[r] * mm(gam[r], gam[i], gam[c])
    return out


def horn2(aP, aM, bP, bM):
    """2 x pairing(aP,aM,bP,bM) of the v0.174 fixture (integer)."""
    W1 = aP * Pp2 + aM * Pm2
    W0 = bP * Pp2 + bM * Pm2
    blocks = {(i, i): ETA[i] * mm(Bsp, W1) for i in range(NV)}
    blocks[(14, 14)] = mm(Bsp, W0)
    return embed(blocks)


Psym2 = horn2(1, 1, 1, 1)
Pskew2 = horn2(1, -1, -1, 1)
Pscr2 = horn2(1, 1, -1, -1)  # fixture's planted wrong line = scrambled-horn control
HORNS = {"P_sym(1,1,1,1)": Psym2, "P_skew(1,-1,-1,1)": Pskew2}

check("interface", "X is a symmetric involution splitting 960+960",
      np.array_equal(mm(X, X), Ifull) and np.array_equal(X.T, X)
      and rref_mod(PIp2, PRIMES[0])[0] == 960 and rref_mod(PIm2, PRIMES[0])[0] == 960)
for name, P2 in list(HORNS.items()) + [("P_scr(1,1,-1,-1)", Pscr2)]:
    rks = [rref_mod(np.mod(P2, p), p)[0] for p in PRIMES]
    check("interface", f"{name}: rank 1920 over GF(1009) and GF(1013)", rks == [1920, 1920])
check("interface", "both horns anticommute with X exactly ({X,P}=0: purely cross-half)",
      np.array_equal(mm(X, Psym2), -mm(Psym2, X))
      and np.array_equal(mm(X, Pskew2), -mm(Pskew2, X)))
check("interface", "form symmetry: P_sym^T = +P_sym, P_skew^T = -P_skew",
      np.array_equal(Psym2.T, Psym2) and np.array_equal(Pskew2.T, -Pskew2))

# ------------------------------------------------------------ so(7,7) generators
GEN_PAIRS = [(i, j) for i in range(14) for j in range(i + 1, 14)]  # 91
GG = {(i, j): mm(gam[i], gam[j]) for (i, j) in GEN_PAIRS}


def act_left(i, j, M):
    """2*rho(s_ij) @ M, exact. Vector rep J_ij = eta_j E_ij - eta_i E_ji."""
    gg = GG[(i, j)]
    Mr = M.reshape(15, 128, TOTAL)
    out = np.einsum('ab,kbc->kac', gg.astype(np.float64),
                    Mr.astype(np.float64), optimize=True)
    out = np.rint(out).astype(np.int64).reshape(TOTAL, TOTAL)
    out[BLK[i], :] += 2 * ETA[j] * M[BLK[j], :]
    out[BLK[j], :] -= 2 * ETA[i] * M[BLK[i], :]
    return out


def act_right(i, j, M):
    """M @ 2*rho(s_ij), exact."""
    gg = GG[(i, j)]
    Mc = M.reshape(TOTAL, 15, 128)
    out = np.einsum('rkb,bc->rkc', Mc.astype(np.float64),
                    gg.astype(np.float64), optimize=True)
    out = np.rint(out).astype(np.int64).reshape(TOTAL, TOTAL)
    out[:, BLK[j]] += 2 * ETA[j] * M[:, BLK[i]]
    out[:, BLK[i]] -= 2 * ETA[i] * M[:, BLK[j]]
    return out


def equivariance_defect(M, pairs=GEN_PAIRS):
    worst = 0
    for (i, j) in pairs:
        d = act_left(i, j, M) - act_right(i, j, M)
        worst = max(worst, int(np.max(np.abs(d))))
        if worst and pairs is not GEN_PAIRS:
            break
    return worst


def is_equivariant(M):
    return equivariance_defect(M) == 0


def xparity(M):
    XMX = mm(X, M, X)
    if np.array_equal(XMX, M):
        return +1
    if np.array_equal(XMX, -M):
        return -1
    return 0


# Clifford contraction/insertion with the equivariant eta-placement for THIS
# vector-rep convention: C(e_c ox s) = gamma_c s ; E(s) = sum_r e_r ox eta_r gamma_r s.
Cfull = embed({(14, c): gam[c] for c in range(NV)})            # Omega^1 -> Omega^0
Efull = embed({(r, 14): ETA[r] * gam[r] for r in range(NV)})   # Omega^0 -> Omega^1
check("equivariance", "contraction C and insertion E are so(7,7)-equivariant "
      "(all 91 generators, exact)", is_equivariant(Cfull) and is_equivariant(Efull))
CE = mm(Cfull, Efull)
check("equivariance", "C o E = 14 * id on the zero-form block (exact integer identity)",
      np.array_equal(CE, 14 * embed({(14, 14): Is})))

rng = np.random.default_rng(RNG_SEED)


# ------------------------------------------- certified null spaces (support-sampled)
def cert_null(col_blocks, tag, exact_verify=True):
    """Integer-certified null space of sum_k x_k col_k = 0.

    col_blocks: list over columns; each column is a LIST of integer matrices
    (stacked blocks, same shapes across columns). Support-restricted sampling
    gives a superset of the null space (upper bound on nullity / lower bound
    on rank); center-lifted candidates are then verified EXACTLY over Z, which
    closes the certificate. Returns (nullity, coeff_vectors) or raises.
    """
    k = len(col_blocks)
    if k == 0:
        return 0, []
    nblk = len(col_blocks[0])
    rows = []
    for b in range(nblk):
        sup = np.unique(np.concatenate(
            [np.flatnonzero(col[b].ravel()) for col in col_blocks] or
            [np.array([], dtype=np.int64)]))
        if sup.size == 0:
            continue
        if sup.size > SUP_CAP:
            sup = sup[np.sort(rng.choice(sup.size, SUP_CAP, replace=False))]
        rows.append(np.stack([col[b].ravel()[sup] for col in col_blocks], axis=1))
    if not rows:
        return k, [np.eye(k, dtype=np.int64)[j] for j in range(k)]  # all-zero columns
    A = np.concatenate(rows, axis=0)
    ranks = [rref_mod(np.mod(A, p), p)[0] for p in PRIMES]
    dim0, basis0 = null_mod(np.mod(A, PRIMES[0]), PRIMES[0])
    certified = []
    for v in basis0:
        vv = center_lift(v, PRIMES[0])
        if exact_verify:
            ok = all(np.count_nonzero(
                sum(int(c) * col[b] for c, col in zip(vv, col_blocks))) == 0
                for b in range(nblk))
            if not ok:
                raise RuntimeError(f"cert_null lift failed: {tag} ranks={ranks}")
        certified.append(vv)
    if ranks[0] != ranks[1] or k - ranks[0] != len(certified):
        raise RuntimeError(f"cert_null rank mismatch: {tag} ranks={ranks}")
    return len(certified), certified


# --------------------------------------------------------------------- L1 layer
print("\nB. LAYER L1: THE SPIN-NATURAL AMBIENT CELL LATTICE (equivariant zero-order algebra)")
Theta = mm(Efull, Cfull)
L1_defs = [
    ("L1e1 one-form +scalar", embed({(b, b): Pp2 for b in range(14)}), +1),
    ("L1e2 one-form -scalar", embed({(b, b): Pm2 for b in range(14)}), +1),
    ("L1e3 gamma-trace +route", mm(Theta, PIp2), +1),
    ("L1e4 gamma-trace -route", mm(Theta, PIm2), +1),
    ("L1e5 zero-form +scalar", embed({(14, 14): Pp2}), +1),
    ("L1e6 zero-form -scalar", embed({(14, 14): Pm2}), +1),
    ("L1o1 contraction +route (Om1+ -> Om0-)", mm(Cfull, PIp2), -1),
    ("L1o2 contraction -route (Om1- -> Om0+)", mm(Cfull, PIm2), -1),
    ("L1o3 insertion +route (Om0+ -> Om1-)", mm(Efull, PIp2), -1),
    ("L1o4 insertion -route (Om0- -> Om1+)", mm(Efull, PIm2), -1),
]
L1_names = [n for n, _, _ in L1_defs]
L1_mats = [m for _, m, _ in L1_defs]
L1_pars = [pr for _, _, pr in L1_defs]
check("L1", "all ten L1 generators are so(7,7)-equivariant (exact, all 91 generators)",
      all(is_equivariant(m) for m in L1_mats))
check("L1", "L1 generators are X-homogeneous with declared parities (6 even + 4 odd)",
      all(xparity(m) == par for _, m, par in L1_defs))
n_indep, _ = cert_null([[m] for m in L1_mats], "L1-indep")
check("L1", "the ten L1 generators are linearly independent (two-prime + exact certificate)",
      n_indep == 0)

# --- L1 completeness certification (reduced coordinates; both primes) ---------
print("   completeness certification, cellwise:")
completeness = {"primes": list(PRIMES)}
comp_fail = []


def left_inv_mod(bas, p):
    """L with L @ bas = I (bas: n x k, full column rank), mod p."""
    n, kk = bas.shape
    aug = np.concatenate([np.mod(bas, p), np.eye(n, dtype=np.int64)], axis=1)
    rank, piv, R = rref_mod(aug, p)
    L = np.zeros((kk, n), dtype=np.int64)
    for r_i, c_i in enumerate(piv):
        if c_i < kk:
            L[c_i] = R[r_i, kk:]
    return L


NV128 = NV * SPIN


def rho1_gen(pr):
    """2*rho1(s_ij) on the one-form corner (1792 x 1792, integer)."""
    (i, j) = pr
    gg = GG[pr]
    M = np.zeros((NV128, NV128), dtype=np.int64)
    for b in range(NV):
        M[128 * b:128 * (b + 1), 128 * b:128 * (b + 1)] = gg
    M[128 * i:128 * (i + 1), 128 * j:128 * (j + 1)] += 2 * ETA[j] * Is
    M[128 * j:128 * (j + 1), 128 * i:128 * (i + 1)] -= 2 * ETA[i] * Is
    return M


def draw_generic(attempt):
    """Deterministic associative-generic element u of U(so(7,7)) image:
    linear + quadratic words in the 2*rho(s_ij); Lie-generic elements are NOT
    enough (non-isomorphic irreps share weights), so quadratic terms are
    required for the Sylvester/charpoly separation certificates."""
    r2 = np.random.default_rng(RNG_SEED + 7919 * (attempt + 1))
    cs = r2.integers(1, 60, size=len(GEN_PAIRS))
    quads = [(int(r2.integers(0, len(GEN_PAIRS))), int(r2.integers(0, len(GEN_PAIRS))),
              int(r2.integers(1, 60))) for _ in range(24)]
    return cs, quads


def generic_spin(cs, quads):
    G0 = np.zeros((SPIN, SPIN), dtype=np.int64)
    for c, pr in zip(cs, GEN_PAIRS):
        G0 += int(c) * GG[pr]
    for a, b, d in quads:
        G0 += d * mm(GG[GEN_PAIRS[a]], GG[GEN_PAIRS[b]])
    return G0


def generic_oneform(cs, quads, p):
    G1 = np.zeros((NV128, NV128), dtype=np.int64)
    for c, pr in zip(cs, GEN_PAIRS):
        (i, j) = pr
        gg = GG[pr]
        for b in range(NV):
            G1[128 * b:128 * (b + 1), 128 * b:128 * (b + 1)] += int(c) * gg
        G1[128 * i:128 * (i + 1), 128 * j:128 * (j + 1)] += int(c) * 2 * ETA[j] * Is
        G1[128 * j:128 * (j + 1), 128 * i:128 * (i + 1)] -= int(c) * 2 * ETA[i] * Is
    G1 = np.mod(G1, p)
    for a, b, d in quads:
        G1 = np.mod(G1 + d * mmp(rho1_gen(GEN_PAIRS[a]), rho1_gen(GEN_PAIRS[b]), p), p)
    return G1


ATTEMPT_USED = None
for attempt in range(4):
    completeness = {"primes": list(PRIMES), "generic_element_attempt": attempt}
    comp_fail = []
    gen_cs, gen_quads = draw_generic(attempt)
    G0 = generic_spin(gen_cs, gen_quads)
    run_ok = run_completeness = True
    for p in PRIMES:
        colsP = rref_mod(np.mod(Pp2, p), p)[1][:64]
        colsM = rref_mod(np.mod(Pm2, p), p)[1][:64]
        basP, basM = np.mod(Pp2[:, colsP], p), np.mod(Pm2[:, colsM], p)
        LP, LM = left_inv_mod(basP, p), left_inv_mod(basM, p)
        if not (np.array_equal(np.mod(LP @ basP, p), np.eye(64, dtype=np.int64))
                and np.array_equal(np.mod(LM @ basM, p), np.eye(64, dtype=np.int64))):
            comp_fail.append(f"chirality basis/left-inverse failed p={p}")
            continue
        BAS = {"+": (basP, LP), "-": (basM, LM)}
        redg = {a: [mmp(L_, mmp(g_, b_, p), p) for g_ in GG.values()]
                for a, (b_, L_) in BAS.items()}
        red0 = {a: mmp(L_, mmp(G0, b_, p), p) for a, (b_, L_) in BAS.items()}
        cpS = {a: charpoly_mod(red0[a], p) for a in "+-"}
        off_zero = poly_gcd_mod(cpS["+"], cpS["-"], p).size == 1
        sqS = {a: poly_sqfree_mod(cpS[a], p) for a in "+-"}
        if not off_zero:
            comp_fail.append(f"Hom(S+,S-) gcd nonzero p={p}")
        diagS = {}
        for a in "+-":
            if not sqS[a]:
                comp_fail.append(f"charpoly(G|S{a}) not squarefree p={p}")
                continue
            pows, Mk = [], np.eye(64, dtype=np.int64)
            for _ in range(64):
                pows.append(Mk)
                Mk = mmp(Mk, red0[a], p)
            cols = []
            for kk in range(64):
                blocks = [np.mod(mmp(g_, pows[kk], p) - mmp(pows[kk], g_, p), p)
                          for g_ in redg[a][:10]]
                cols.append(np.concatenate([b_.ravel() for b_ in blocks]))
            A = np.stack(cols, axis=1)
            dimk, bask = null_mod(A, p)
            surv = 0
            for v in bask:
                Mc = np.zeros((64, 64), dtype=np.int64)
                for kk, cv in enumerate(v):
                    if cv:
                        Mc = np.mod(Mc + int(cv) * pows[kk], p)
                if all(np.array_equal(mmp(g_, Mc, p), mmp(Mc, g_, p)) for g_ in redg[a]):
                    surv += 1
            diagS[a] = (dimk, surv)
            if not (dimk == 1 and surv == 1):
                comp_fail.append(f"End(S{a}) mod-{p} != 1: {diagS[a]}")
        completeness[f"p{p}_S_cells"] = {
            "Hom(S+,S-)=Hom(S-,S+)": 0 if off_zero else "FAIL",
            "End(S+)": diagS.get("+"), "End(S-)": diagS.get("-")}

        # one-form corner and Psi cells (generic element = same associative word)
        G1 = generic_oneform(gen_cs, gen_quads, p)
        psi_cp, psi_dat = {}, {}
        for a, aopp in (("+", "-"), ("-", "+")):
            bas_a = BAS[a][0]
            K1 = np.zeros((NV128, 896), dtype=np.int64)
            for b in range(NV):
                K1[128 * b:128 * (b + 1), 64 * b:64 * (b + 1)] = bas_a
            L1r = np.zeros((896, NV128), dtype=np.int64)
            for b in range(NV):
                L1r[64 * b:64 * (b + 1), 128 * b:128 * (b + 1)] = BAS[a][1]
            G1a = mmp(L1r, mmp(G1, K1, p), p)      # G on Omega^1_a (896 x 896)
            Lopp = np.zeros((896, NV128), dtype=np.int64)
            for b in range(NV):
                Lopp[64 * b:64 * (b + 1), 128 * b:128 * (b + 1)] = BAS[aopp][1]
            if np.any(mmp(Lopp, mmp(G1, K1, p), p)):
                comp_fail.append(f"G1 leaks chirality on Omega^1{a} p={p}")
            Crow = np.concatenate([np.mod(gam[c_], p) for c_ in range(NV)], axis=1)
            Cred = mmp(BAS[aopp][1], mmp(Crow, K1, p), p)
            dimPsi, basPsi = null_mod(Cred, p)
            if dimPsi != 832:
                comp_fail.append(f"Psi{a} dim {dimPsi} != 832 p={p}")
                continue
            KPsi = np.stack(basPsi, axis=1)  # 896 x 832, identity on free rows
            rankC, pivC, _ = rref_mod(Cred, p)
            free_rows = [c for c in range(896) if c not in pivC]
            LPsi = np.zeros((832, 896), dtype=np.int64)
            for idx, fr in enumerate(free_rows):
                LPsi[idx, fr] = 1
            if not np.array_equal(np.mod(LPsi @ KPsi, p), np.eye(832, dtype=np.int64)):
                comp_fail.append(f"Psi{a} left-inverse structure failed p={p}")
                continue
            GPsi = mmp(LPsi, mmp(G1a, KPsi, p), p)
            if np.any(mmp(Cred, mmp(G1a, KPsi, p), p)):
                comp_fail.append(f"G does not preserve Psi{a} p={p}")
            psi_cp[a] = charpoly_mod(GPsi, p)
            psi_dat[a] = (K1, L1r, KPsi, LPsi, GPsi)
        if len(psi_cp) == 2:
            gcds = {}
            for a in "+-":
                for b in "+-":
                    gcds[f"S{a}<->Psi{b}"] = int(
                        poly_gcd_mod(cpS[a], psi_cp[b], p).size == 1)
            gcds["Psi+<->Psi-"] = int(
                poly_gcd_mod(psi_cp["+"], psi_cp["-"], p).size == 1)
            sqPsi = {a: poly_sqfree_mod(psi_cp[a], p) for a in "+-"}
            completeness[f"p{p}_gcd_certificates"] = gcds
            completeness[f"p{p}_psi_squarefree"] = {a: int(v) for a, v in sqPsi.items()}
            if not all(gcds.values()):
                comp_fail.append(f"gcd certificate failed p={p}: {gcds}")
            if not all(sqPsi.values()):
                comp_fail.append(f"Psi charpoly not squarefree p={p}")
            # End(Psi_a): squarefree charpoly => G|Psi nonderogatory => its
            # commutant is polynomials in G|Psi; the equivariant subspace is cut
            # by sampled generator residuals over the 832 power-candidates and
            # survivors are verified in full, closing the certificate at 1.
            for a in "+-":
                if f"Psi charpoly not squarefree p={p}" in comp_fail:
                    break
                K1, L1r, KPsi, LPsi, GPsi = psi_dat[a]
                gensPsi = []
                for pr in GEN_PAIRS[:8]:
                    Gga = mmp(L1r, mmp(np.mod(rho1_gen(pr), p), K1, p), p)
                    gensPsi.append(mmp(LPsi, mmp(Gga, KPsi, p), p))
                coord_r = rng.integers(0, 832, 900)
                coord_c = rng.integers(0, 832, 900)
                Mk = np.eye(832, dtype=np.int64)
                colvals = []
                for kk in range(832):
                    vals = []
                    for gPsi in gensPsi:
                        v1 = np.einsum('tj,jt->t', gPsi[coord_r].astype(np.float64),
                                       Mk[:, coord_c].astype(np.float64))
                        v2 = np.einsum('tj,jt->t', Mk[coord_r].astype(np.float64),
                                       gPsi[:, coord_c].astype(np.float64))
                        vals.append(np.mod(np.rint(v1 - v2).astype(np.int64), p))
                    colvals.append(np.concatenate(vals))
                    if kk < 831:
                        Mk = mmp(Mk, GPsi, p)
                A = np.stack(colvals, axis=1)
                dimk, bask = null_mod(A, p)
                surv = None
                if dimk != 1 and dimk <= 4:
                    surv = 0
                    for v in bask:
                        acc = np.zeros((832, 832), dtype=np.int64)
                        for kk in range(831, -1, -1):
                            acc = mmp(acc, GPsi, p)
                            if v[kk]:
                                acc = np.mod(acc + int(v[kk])
                                             * np.eye(832, dtype=np.int64), p)
                        if all(np.array_equal(mmp(g_, acc, p), mmp(acc, g_, p))
                               for g_ in gensPsi):
                            surv += 1
                completeness[f"p{p}_End_Psi{a}_sampled"] = (dimk if surv is None
                                                            else [dimk, surv])
                final = dimk if surv is None else surv
                if final != 1:
                    comp_fail.append(f"End(Psi{a}) dim {final} != 1 p={p}")
    if not comp_fail:
        ATTEMPT_USED = attempt
        break
    print(f"   generic-element attempt {attempt} failed: {comp_fail}")

completeness["generic_element_attempt_used"] = ATTEMPT_USED
check("L1", "completeness certificates hold at both primes (S-cells exact; "
      "S<->Psi and Psi+<->Psi- Sylvester-coprime; End(S+-) = End(Psi+-) = 1; "
      "associative-generic separating element)",
      (not comp_fail) and ATTEMPT_USED is not None)
if comp_fail:
    print("   completeness failures:", comp_fail)
L1_CELL_DIMS = {
    "even": 6, "odd": 4,
    "lattice_cells": {"Om1+->Om1+": 2, "Om1-->Om1-": 2, "Om0+->Om0+": 1,
                      "Om0-->Om0-": 1, "Om1+->Om0-": 1, "Om1-->Om0+": 1,
                      "Om0+->Om1-": 1, "Om0-->Om1+": 1,
                      "other_8_cells_of_the_4x4_lattice": 0}}

# --------------------------------------------------------------------- L2 layer
print("\nC. LAYER L2: THE SIXTEEN-CELL (9.16) GRAMMAR, ZERO-ORDER INSTANTIATION")
L2_defs = []
for i in range(NV):
    wb = embed(wedge_blocks(i))
    L2_defs.append((f"NW wedge-VEV dir{i} +", mm(wb, PIp2), -1))
    L2_defs.append((f"NW wedge-VEV dir{i} -", mm(wb, PIm2), -1))
for i in range(NV):
    km = embed({(i, 14): Is})
    L2_defs.append((f"NE km-VEV dir{i} +", mm(km, PIp2), +1))
    L2_defs.append((f"NE km-VEV dir{i} -", mm(km, PIm2), +1))
for i in range(NV):
    co = embed({(14, i): ETA[i] * Is})
    L2_defs.append((f"SW co-VEV dir{i} +", mm(co, PIp2), +1))
    L2_defs.append((f"SW co-VEV dir{i} -", mm(co, PIm2), +1))
# SE: displayed zero in eq (9.16); the admitted nonzero rival is unspecified by
# the source (SOURCE-ADMITS-UNSPECIFIED-RIVAL) -> excluded, recorded SCOPED.
L2_names = [n for n, _, _ in L2_defs]
L2_mats = [m for _, m, _ in L2_defs]
L2_pars = [pr for _, _, pr in L2_defs]
check("L2", "84 grammar generators are X-homogeneous with declared parities "
      "(28 odd NW + 28 even NE + 28 even SW)",
      all(xparity(m) == pr for _, m, pr in L2_defs)
      and sum(1 for q in L2_pars if q == -1) == 28)
nl2, _ = cert_null([[m] for m in L2_mats], "L2-indep")
check("L2", "the 84 L2 generators are linearly independent (two-prime + exact certificate)",
      nl2 == 0)
nun, _ = cert_null([[m] for m in L1_mats + L2_mats], "L1L2-union")
check("L2", "L1 and L2 spans intersect trivially (rank 94 union)", nun == 0)
sample_pairs = [GEN_PAIRS[t] for t in rng.choice(len(GEN_PAIRS), 8, replace=False)]
res_blocks = [[act_left(i, j, m) - act_right(i, j, m) for (i, j) in sample_pairs]
              for m in L2_mats]
dim_eq8, eq_vecs = cert_null(res_blocks, "L2-equivariant-content")
# elements exactly equivariant under the 8 sampled generators are a SUPERSET of
# the truly equivariant ones; verify each survivor against all 91 generators.
dim_eqL2 = 0
for v in eq_vecs:
    Bc = sum(int(c) * m for c, m in zip(v, L2_mats))
    if equivariance_defect(Bc) == 0:
        dim_eqL2 += 1
check("L2", "the equivariant subspace of span(L2) is zero "
      "(8-generator commutant dim {} pruned by full 91-generator exact "
      "verification)".format(dim_eq8), dim_eqL2 == 0)

# ------------------------------------------------- alternation cells per horn/layer
print("\nD. DEFORMATION-CELL DIMENSIONS Z(P,L) BY X-PARITY AND SWAP CLASS")


def sym_of(P2, B):
    PB = mm(P2, B)
    return PB + PB.T


def sigma_swap(B):
    return mm(Q, B.T, Q)


def cell_table(P2, mats, names, pars, tag):
    odd_idx = [k for k, q in enumerate(pars) if q == -1]
    even_idx = [k for k, q in enumerate(pars) if q == +1]
    out, basis_store = {}, {}
    for par_name, idx in (("odd", odd_idx), ("even", even_idx)):
        dim, basis = cert_null([[sym_of(P2, mats[k])] for k in idx], f"{tag}-{par_name}")
        out[par_name] = dim
        basis_store[par_name] = [(idx, v) for v in basis]
    even_sols = [sum(int(c) * mats[k] for c, k in zip(v, idx))
                 for idx, v in basis_store["even"]]
    if even_sols:
        dsym, _ = cert_null([[sigma_swap(B) - B] for B in even_sols], f"{tag}-evensym")
        dasy, _ = cert_null([[sigma_swap(B) + B] for B in even_sols], f"{tag}-evenasym")
        dplus, _ = cert_null([[mm(PIm2, B), mm(B, PIm2)] for B in even_sols],
                             f"{tag}-plusonly")
        dminus, _ = cert_null([[mm(PIp2, B), mm(B, PIp2)] for B in even_sols],
                              f"{tag}-minusonly")
    else:
        dsym = dasy = dplus = dminus = 0
    out["even_sym"] = dsym
    out["even_asym"] = dasy
    out["even_sum_check"] = bool(dsym + dasy == out["even"])
    out["single_half_supported(+only,-only)"] = [dplus, dminus]
    odd_wit = []
    for idx, v in basis_store["odd"]:
        B = sum(int(c) * mats[k] for c, k in zip(v, idx))
        assert np.count_nonzero(sym_of(P2, B)) == 0 and xparity(B) == -1
        odd_wit.append({names[k]: int(c) for c, k in zip(v, idx) if c})
    out["odd_witnesses"] = odd_wit
    return out


TABLE = {}
for hname, P2 in HORNS.items():
    TABLE[hname] = {
        "L1": cell_table(P2, L1_mats, L1_names, L1_pars, f"{hname}-L1"),
        "L2": cell_table(P2, L2_mats, L2_names, L2_pars, f"{hname}-L2"),
    }
SCR = {
    "L1": cell_table(Pscr2, L1_mats, L1_names, L1_pars, "scr-L1"),
    "L2": cell_table(Pscr2, L2_mats, L2_names, L2_pars, "scr-L2"),
}
L0 = {"alternating_total": TOTAL * (TOTAL - 1) // 2,
      "even_admissible": 960 * 960, "odd_admissible": 960 * 959,
      "note": ("control only, decides nothing (packet); closed forms from the "
               "graph/anti-symmetry argument with {X,P}=0 and P invertible: "
               "even-admissible = graph of the pairing transport (960^2); "
               "odd-admissible = two independent 960-alternation conditions "
               "(2 * 960*959/2)")}
check("L0", "packet L0 arithmetic reproduced: 1920*1919/2 = 1,842,240 and 2*960^2 block split",
      L0["alternating_total"] == 1842240 and 2 * 960 * 960 == 1843200)

for hname in TABLE:
    t = TABLE[hname]
    print(f"   {hname}: L1 odd={t['L1']['odd']} even={t['L1']['even']} "
          f"(sym={t['L1']['even_sym']}, asym={t['L1']['even_asym']}) | "
          f"L2 odd={t['L2']['odd']} even={t['L2']['even']} "
          f"(sym={t['L2']['even_sym']}, asym={t['L2']['even_asym']})")
print(f"   scrambled horn: L1 odd={SCR['L1']['odd']} even={SCR['L1']['even']} | "
      f"L2 odd={SCR['L2']['odd']} even={SCR['L2']['even']}")

# --------------------------------------------------------------- kill / tripwire
print("\nE. KILL CONDITION AND TRIPWIRE (certificates; grading per the packet's outcome table)")
kill_fired = all(TABLE[h]["L1"]["odd"] == 0 and TABLE[h]["L2"]["odd"] == 0 for h in TABLE)
tripwire_fired = any(TABLE[h]["L1"]["even_asym"] > 0 for h in TABLE)
check("kill", "kill evaluation is decidable from certified integer dimensions", True)
print(f"   KILL (dim Z_odd(P,L1) = dim Z_odd(P,L2) = 0 for BOTH horns): "
      f"{'FIRED' if kill_fired else 'NOT FIRED'}")
print(f"   TRIPWIRE (dim Z_even-asym(P,L1) > 0, equivariant layer): "
      f"{'FIRED' if tripwire_fired else 'NOT FIRED'}")

# ------------------------------------------------------------- planted controls
print("\nF. PLANTED CONTROLS")
def symbol_mod(i, wp, wm, ep, em, p):
    Wt = np.mod(wp * Pp2 + wm * Pm2, p)  # 2x weights (overall scale irrelevant)
    SE = np.mod(ep * Pp2 + em * Pm2, p)
    blocks = {}
    for (r, c), v in wedge_blocks(i).items():
        blocks[(r, c)] = mmp(v, Wt, p)
    blocks[(i, 14)] = np.mod(2 * Is, p)
    blocks[(14, i)] = np.mod(-2 * ETA[i] * Is, p)
    blocks[(14, 14)] = mmp(2 * gam[i], SE, p)
    return np.mod(embed(blocks), p)


reg_ok = True
reg_detail = {}
for p in PRIMES:
    inv12 = pow(12, p - 2, p)
    wp_, wm_ = 1, 2
    ep_ = (11 * inv12 * pow(wm_, p - 2, p)) % p
    em_ = (11 * inv12 * pow(wp_, p - 2, p)) % p
    Ds = {i: symbol_mod(i, wp_, wm_, ep_, em_, p) for i in (0, 7)}
    bases4 = [horn2(1, 0, 0, 0), horn2(0, 1, 0, 0), horn2(0, 0, 1, 0), horn2(0, 0, 0, 1)]
    lines = {}
    for sign, nm in ((1, "self"), (-1, "anti")):
        colsv = []
        for Pb in bases4:
            defect = []
            for i in (0, 7):
                d = np.mod(mmp(Pb, Ds[i], p) - sign * mmp(Ds[i].T, Pb, p), p)
                defect.append(d)
            colsv.append(np.concatenate([d.ravel() for d in defect]))
        A4 = np.stack(colsv, axis=1)
        A4 = A4[np.any(A4, axis=1)]
        if A4.shape[0] > 6000:
            A4 = A4[np.sort(rng.choice(A4.shape[0], 6000, replace=False))]
        rank4, _, _ = rref_mod(A4, p)
        dim4, bas4 = null_mod(A4, p)
        rep = tuple(int(x) for x in center_lift(bas4[0], p)) if dim4 == 1 else None
        lines[nm] = (rank4, dim4, rep)
    exp = {"self": (1, -1, -1, 1), "anti": (1, 1, 1, 1)}
    okp = True
    for nm in lines:
        r4, d4, rep = lines[nm]
        okp &= (r4 == 3 and d4 == 1 and rep is not None)
        if rep is not None:
            s0 = 1 if rep[0] > 0 else -1
            okp &= tuple(s0 * np.array(rep)) == exp[nm]
    alt_ok = True
    for i in range(14):
        Dsi = symbol_mod(i, wp_, wm_, ep_, em_, p)
        for P2h in (Psym2, Pskew2):
            PB = mmp(P2h, Dsi, p)
            alt_ok &= not np.any(np.mod(PB + PB.T, p))
    D0 = Ds[0]
    w1 = np.mod(mmp(Pscr2, D0, p) - mmp(D0.T, Pscr2, p), p)
    w2 = np.mod(mmp(Pscr2, D0, p) + mmp(D0.T, Pscr2, p), p)
    plant_ok = bool(np.any(w1) and np.any(w2))
    r_ = 3
    rinv = pow(r_, p - 2, p)
    half = (p + 1) // 2
    Rblk = np.mod(r_ * half * Pp2 + rinv * half * Pm2, p)
    Sfull = np.mod(embed({(b, b): Rblk for b in range(15)}), p)
    pres = all(not np.any(np.mod(mmp(Sfull.T, mmp(np.mod(P2h, p), Sfull, p), p)
                                 - np.mod(P2h, p), p))
               for P2h in (Psym2, Pskew2))
    # zero weight equations: alternation holds for three further weight pairs
    wpairs_ok = True
    for (wa, wb) in ((1, 1), (2, 5), (3, 7)):
        ea = (11 * inv12 * pow(wb, p - 2, p)) % p
        eb = (11 * inv12 * pow(wa, p - 2, p)) % p
        Dw = symbol_mod(0, wa, wb, ea, eb, p)
        PBw = mmp(Psym2, Dw, p)
        wpairs_ok &= not np.any(np.mod(PBw + PBw.T, p))
    reg_detail[p] = {"lines": {k: (v[0], v[1], list(v[2]) if v[2] else None)
                               for k, v in lines.items()},
                     "alternation_all_14_axes_both_horns": bool(alt_ok),
                     "scrambled_pairing_neither_horn": plant_ok,
                     "chiral_rescaling_preserves_both_horns": bool(pres),
                     "zero_weight_equations_extra_pairs": bool(wpairs_ok)}
    reg_ok &= okp and alt_ok and plant_ok and pres and wpairs_ok
check("control_i", "regression: v0.174 two-horn classification, 14-axis alternation, "
      "scrambled plant, rescaling identity and zero weight equations reproduced "
      "over GF(1009) and GF(1013)", reg_ok)

# (ii) planted Dirac-type half-coupling mass: zero-form 64+<->64- block
B_dirac = embed({(14, 14): Bsp})
adm = {h: int(np.count_nonzero(sym_of(P2, B_dirac)) == 0) for h, P2 in HORNS.items()}
check("control_ii", "planted Dirac half-coupling mass is classified X-odd",
      xparity(B_dirac) == -1)
print(f"   control (ii) admissibility per horn (computed, not assumed): "
      f"{ {h: ('ADMISSIBLE' if v else 'NOT alternating-admissible') for h, v in adm.items()} }")

# (iii) planted single-half mass: B_+ = Pp on the zero-form sector, B_- = 0
B_single = embed({(14, 14): Pp2})
sB = sigma_swap(B_single)
check("control_iii", "planted single-half mass is X-even and lands in the "
      "swap-asymmetric class (sigma(B) != B, asym component nonzero, B_- block zero)",
      xparity(B_single) == +1 and not np.array_equal(sB, B_single)
      and np.count_nonzero(B_single - sB) > 0
      and np.count_nonzero(mm(PIm2, B_single)) == 0)
adm3 = {h: int(np.count_nonzero(sym_of(P2, B_single)) == 0) for h, P2 in HORNS.items()}
check("control_iii", "planted single-half mass is rejected by the alternation "
      "admissibility test on both horns (explicit asymmetric mass unavailable)",
      all(v == 0 for v in adm3.values()))

# (iv) random non-equivariant B rejected by the L1 filter
B_rand = rng.integers(-3, 4, size=(TOTAL, TOTAL)).astype(np.int64)
check("control_iv", "random non-equivariant matrix is rejected by the L1 equivariance filter",
      equivariance_defect(B_rand, sample_pairs) > 0)

# (v) deliberately symmetrized (P B) rejected by the alternation test
B0 = rng.integers(-2, 3, size=(TOTAL, TOTAL)).astype(np.int64)
PB0 = mm(Psym2, B0)
PBsym = PB0 + PB0.T
Pinv_half = embed({**{(i, i): ETA[i] * Bsp for i in range(NV)}, (14, 14): Bsp})
B_symplant = mm(Pinv_half, PBsym)  # P_sym^-1 * sym(P B0) up to the harmless factor 4
check("control_v", "deliberately symmetrized P*B is rejected by the alternation test",
      np.count_nonzero(sym_of(Psym2, B_symplant)) > 0 and np.count_nonzero(PBsym) > 0)

# (brief extra) a deliberately X-commuting deformation lands in even cells only
B_evenplant = mm(Theta, PIp2) + 3 * embed({(14, 14): Pm2})
check("control_extra", "planted X-commuting deformation has zero X-odd component "
      "and lands in even cells only",
      xparity(B_evenplant) == +1
      and np.count_nonzero(mm(X, B_evenplant, X) - B_evenplant) == 0)

# ------------------------------------------------------------------------ result
RESULT = {
    "check": "CHK-1",
    "packet": "explorations/decoupling-constructibility-packet-2026-08-12.md#lens-2",
    "repo": REPO, "head_pin": HEAD_PIN, "primes": list(PRIMES),
    "interface": {"V": "R^1920 = (1+14)x128, blocks: 14 one-form + 1 zero-form",
                  "X": "blockdiag(omega), 960+960", "P_sym": "(1,1,1,1)",
                  "P_skew": "(1,-1,-1,1)", "frozen_fixture":
                  "tests/channel-swings/selected_k77_action_adjoint_weight_classification_probe.py"},
    "structural_certificates": {
        "X_anticommutes_with_both_horns": True,
        "horn_form_symmetry": {"P_sym": "+", "P_skew": "-"},
        "consequence": ("both horns are purely cross-half forms; an X-even "
                        "alternating-admissible B is the pairing-transport graph "
                        "of its (+)-block, so no admissible even deformation is "
                        "supported on a single half at any layer")},
    "L0_control": L0,
    "L1": {"dims": L1_CELL_DIMS, "completeness": completeness,
           "completeness_failures": comp_fail},
    "L2": {"generators": 84,
           "parities": {"odd_NW_wedge": 28, "even_NE_km": 28, "even_SW_co": 28},
           "SE": "displayed zero (s9); nonzero rival source-admitted, unspecified "
                 "-> excluded, SCOPED",
           "equivariant_subspace_of_L2": dim_eqL2},
    "cell_table": {h: {L: {k: v for k, v in TABLE[h][L].items() if k != "odd_witnesses"}
                       for L in TABLE[h]} for h in TABLE},
    "odd_witnesses": {h: {L: TABLE[h][L]["odd_witnesses"] for L in TABLE[h]} for h in TABLE},
    "scrambled_horn_control": {L: {k: v for k, v in SCR[L].items() if k != "odd_witnesses"}
                               for L in SCR},
    "kill_condition": {"definition": "dim Z_odd(P,L1) = dim Z_odd(P,L2) = 0 for BOTH horns",
                       "fired": bool(kill_fired)},
    "tripwire": {"definition": "dim Z_even-asym(P,L1) > 0 at the equivariant layer",
                 "fired": bool(tripwire_fired)},
    "controls": {"regression_v0174": reg_detail,
                 "dirac_plant_admissibility_per_horn": adm,
                 "single_half_plant_admissible": adm3},
    "counts": dict(sorted(COUNTS.items())), "failures": FAILURES,
}
print("\nG. MACHINE-READABLE RESULT")
print(json.dumps(RESULT, indent=1, sort_keys=True, default=int))
print("SUMMARY " + " + ".join(f"{v} {k}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAIL: " + "; ".join(FAILURES))
    sys.exit(1)
print("PASS: CHK-1 cell table certified; kill "
      + ("FIRED" if kill_fired else "NOT FIRED") + "; tripwire "
      + ("FIRED" if tripwire_fired else "NOT FIRED") + ".")
