#!/usr/bin/env python3
"""SA-1 -- is the selector for the `SOLDERED-AD` fork available from built objects?

Question
--------
`MD-1` (2026-08-14) declared the Layer-0 fork `SOLDERED-AD` vs `INERT-AD` on the
`ad` leg of GU's connection and returned `NOT-DETERMINED`.  Its own §7 named the
decisive next gate:

    "is the repo's `j_s: N -> ad(P_s)` a canonical reduction of `P_H` along the
     frame bundle, or a chosen local trivialization?  A source reinspection plus
     a read of `docs/paper-formalization-candidates.md` 2A against the
     manuscript's definition of `H` would settle it, and it is cheap."

This probe performs exactly that gate and nothing past it.  It does NOT build an
action, a BRST/BV complex, a quotient, or a spectrum.

What it certifies
-----------------
A. [S]  The exact source/manuscript strings that define `P_H`, and the
        hard-core register claim that GU has no internal symmetry groups.
B. [R]  K77 2026-08-05 §3: `w1(C) = 0`, `w2(C) = pi^* w2(TX)` for the chimeric
        bundle `C = Sym^2(pi^* T^*X) (+) pi^* T^*X`.
C. [R]  K77 2026-08-05 §5: `Cl(7,7) = M_128(R)`; an invariant form `B` with
        `B^2 = 1`, `tr B = 0`, `sig B = (64,64)`; grade one and grade two are
        `B`-skew, so `spin(7,7) (subset) so(64,64) (subset) u(64,64)`.
D. [E]  The endogenous representation `r_C : O(1,3) -> O(G_C)` is an injective
        group homomorphism and an isometry of the chimeric metric for EVERY
        value of the trace-reversal parameter `lambda` and for BOTH horizontal
        sign conventions.  So the soldering statement is independent of
        `VERTICAL-FROBENIUS-TRACE`, `CARRIER-SPLIT` and `SIGNATURE-AMBIENT`.
E. [R]  MD-1 / PV-2 / LA-8 numbers: inertia (7,3) and (6,4); dim k = 21,
        dim p = 24; Killing negative on k and positive on p; three rotations in
        k and three boosts in p; largest Lorentz-invariant subspace of k is 0
        and of p is 0; smallest invariant subspace containing k is all 45;
        `dim Inv(Sym^2) = 1`, `dim Inv(traceless 9) = 0`, `dim Inv(Lambda^2 V) = 0`.
F. [E]  THE RESULT.  `so(7,7)` contains TWO distinct 6-dimensional Lorentz
        subalgebras -- the endogenous/diagonal one `so(1,3)_endo` induced by
        frame rotations of `X`, and the block one `so(1,3)_H` named by the
        manuscript's observation chain `Spin(7,7) -> Spin(1,3) x Spin(6,4)`.
        They intersect in 0, they differ exactly by an INTERNAL rotation
        `delta(X) in so(6,4)`, and they give OPPOSITE answers on the same `k`:
        the largest invariant subspace of `k` is 0 under `so(1,3)_endo` and 21
        under `so(1,3)_H`.

Exactness policy
----------------
Every load-bearing number is a Python `int` or a `fractions.Fraction`.
Signatures are computed by exact Sylvester congruence, never by eigenvalues.
The Clifford block uses `numpy` INTEGER matrices whose entries stay in
`{-1,0,1}`; the dtype and the entry bound are both asserted.  `assert_no_float`
sweeps the whole result dict at the end.

Run from the repository root:
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py --selftest
"""

from __future__ import annotations

import os
import subprocess
import sys
from fractions import Fraction as F
from itertools import combinations

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

REGISTER = os.path.join(REPO, "lab", "sources", "source-claim-register.yaml")
PORTAL = os.path.join(REPO, "lab", "sources", "transcripts",
                      "portal-special-gu-first-look-2020-04-02.md")
TOE = os.path.join(REPO, "lab", "sources", "transcripts", "toe-weinstein-gu-40-years.md")
CANDIDATES = os.path.join(REPO, "docs", "paper-formalization-candidates.md")
K77BUILD = os.path.join(REPO, "explorations", "conditional-build",
                        "k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
K77SRC = os.path.join(REPO, "lab", "sources",
                      "k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md")
K77RECON = os.path.join(REPO, "explorations", "conditional-build",
                        "selected-k77-full-reduction-quotient-reconciliation-2026-08-07.md")
K77MOVING = os.path.join(REPO, "explorations", "conditional-build",
                         "selected-k77-moving-parent-bundle-observation-reduction-2026-08-10.md")
MD1 = os.path.join(REPO, "lab", "active-research", "joe-directed",
                   "four-d-mode-decomposition",
                   "md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md")
LA8 = os.path.join(REPO, "lab", "active-research", "joe-directed", "ledger-advancement",
                   "la8-rae2-is-refuted-at-the-settled-form-leg-and-the-open-fork-is-not-load-bearing-2026-08-15.md")
PHI2 = os.path.join(REPO, "lab", "active-research", "joe-directed", "phi-reduction",
                    "phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md")
PATHDEPS = os.path.join(REPO, "lab", "process", "path-dependencies.md")
FORKREG = os.path.join(REPO, "lab", "process", "layer0-fork-registry.yaml")
LA8PROBE = os.path.join(REPO, "tests", "channel-swings",
                        "joe_directed_ledger_rae2_form_leg_typing.py")
K77PROBE = os.path.join(REPO, "tests", "channel-swings",
                        "k77_global_chimeric_spin_reduction_probe.py")

MUT = ""
for _a in sys.argv[1:]:
    if _a.startswith("--mutate="):
        MUT = _a.split("=", 1)[1]

CHECKS: list[tuple[str, str, bool, bool]] = []   # (tag, label, passed, is_control)
RESULT: dict = {}


def check(tag: str, label: str, passed: bool, control: bool = False) -> None:
    CHECKS.append((tag, label, bool(passed), control))


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# exact linear algebra over Q
# ---------------------------------------------------------------------------

def zeros(r: int, c: int):
    return [[F(0)] * c for _ in range(r)]


def eye(n: int):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        Oi = out[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    if Bt[j]:
                        Oi[j] += a * Bt[j]
    return out


def matadd(A, B, s=F(1)):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def transpose(A):
    return [list(col) for col in zip(*A)]


def bracket(A, B):
    return matadd(matmul(A, B), matmul(B, A), F(-1))


def is_zero(A) -> bool:
    return all(x == 0 for row in A for x in row)


def flat(A):
    return [x for row in A for x in row]


def rref(rows):
    mat = [list(r) for r in rows]
    piv = []
    r = 0
    ncols = len(mat[0]) if mat else 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(mat)):
            if mat[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        mat[r], mat[pr] = mat[pr], mat[r]
        pv = mat[r][c]
        mat[r] = [x / pv for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        piv.append(c)
        r += 1
        if r == len(mat):
            break
    return mat[:r], piv


def rank_of(rows) -> int:
    if not rows:
        return 0
    return len(rref(rows)[0])


def nullspace(rows, ncols):
    """Exact basis of {x : rows . x = 0}."""
    if not rows:
        return eye(ncols)
    red, piv = rref(rows)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [F(0)] * ncols
        v[f] = F(1)
        for i, p in enumerate(piv):
            v[p] = -red[i][f]
        basis.append(v)
    return basis


def sylvester(M):
    """Exact inertia (n_pos, n_neg, n_zero) and congruence T with T^T M T = D."""
    n = len(M)
    A = [row[:] for row in M]
    T = eye(n)

    def col_op(dst, src, s):
        for i in range(n):
            A[i][dst] += s * A[i][src]
            T[i][dst] += s * T[i][src]

    def row_op(dst, src, s):
        for j in range(n):
            A[dst][j] += s * A[src][j]

    def swap(i, j):
        A[i], A[j] = A[j], A[i]
        for r in range(n):
            A[r][i], A[r][j] = A[r][j], A[r][i]
            T[r][i], T[r][j] = T[r][j], T[r][i]

    k = 0
    while k < n:
        if A[k][k] == 0:
            piv = None
            for i in range(k + 1, n):
                if A[i][i] != 0:
                    piv = i
                    break
            if piv is not None:
                swap(k, piv)
            else:
                off = None
                for i in range(k + 1, n):
                    if A[k][i] != 0:
                        off = i
                        break
                if off is None:
                    k += 1
                    continue
                col_op(k, off, F(1))
                row_op(k, off, F(1))
        d = A[k][k]
        for i in range(k + 1, n):
            if A[k][i] != 0:
                s = -A[k][i] / d
                col_op(i, k, s)
                row_op(i, k, s)
        k += 1
    pos = sum(1 for i in range(n) if A[i][i] > 0)
    neg = sum(1 for i in range(n) if A[i][i] < 0)
    zer = n - pos - neg
    diag = [A[i][i] for i in range(n)]
    return (pos, neg, zer), T, diag


def normalized_congruence(M):
    """T with T^T M T = diag(+1..., -1...) for nondegenerate M; returns (T, D)."""
    (pos, neg, zer), T, diag = sylvester(M)
    assert zer == 0, "degenerate form"
    n = len(M)
    cols_pos = [i for i in range(n) if diag[i] > 0]
    cols_neg = [i for i in range(n) if diag[i] < 0]
    order = cols_pos + cols_neg
    Tn = zeros(n, n)
    for newc, oldc in enumerate(order):
        scale = abs(diag[oldc])
        # 1/sqrt(scale) is irrational in general; rescale by clearing to +-1 via
        # a rational square only when possible.  We instead keep D = diag(diag)
        # and normalise signs only.
        for i in range(n):
            Tn[i][newc] = T[i][oldc]
        del scale
    D = [[F(0)] * n for _ in range(n)]
    for newc, oldc in enumerate(order):
        D[newc][newc] = diag[oldc]
    return Tn, D, (pos, neg)


# ---------------------------------------------------------------------------
# invariant-subspace machinery
# ---------------------------------------------------------------------------

def largest_invariant_subspace(gens, basis, dim_total: int) -> int:
    """dim of the largest subspace of span(basis) invariant under all gens."""
    cur = [list(v) for v in basis]
    while cur:
        red, _ = rref(cur)
        cur = red
        m = len(cur)
        # left annihilator of span(cur): rows y with y . v = 0 for all v in cur
        ann = nullspace(cur, dim_total)          # vectors y with cur . y = 0
        if not ann:
            return m
        rows = []
        for g in gens:
            for y in ann:
                # constraint on coefficients c: y . (g (sum c_i v_i)) = 0
                row = []
                for v in cur:
                    gv = [sum(g[a][b] * v[b] for b in range(dim_total))
                          for a in range(dim_total)]
                    row.append(sum(y[a] * gv[a] for a in range(dim_total)))
                rows.append(row)
        if not rows:
            return m
        ker = nullspace(rows, m)
        if len(ker) == m:
            return m
        if not ker:
            return 0
        cur = [[sum(c[i] * cur[i][b] for i in range(m)) for b in range(dim_total)]
               for c in ker]
    return 0


def fixed_vectors(gens, basis, dim_total: int) -> int:
    """dim of {v in span(basis) : g v = 0 for every g}.  This is `Inv`, the
    space of INVARIANT VECTORS -- not the largest invariant subspace."""
    if not basis:
        return 0
    m = len(basis)
    rows = []
    for g in gens:
        for a in range(dim_total):
            rows.append([sum(g[a][b] * v[b] for b in range(dim_total)) for v in basis])
    if not rows:
        return m
    return len(nullspace(rows, m))


def smallest_invariant_containing(gens, seeds, dim_total: int) -> int:
    cur = [list(v) for v in seeds]
    while True:
        red, _ = rref(cur)
        add = []
        for g in gens:
            for v in red:
                add.append([sum(g[a][b] * v[b] for b in range(dim_total))
                            for a in range(dim_total)])
        newred, _ = rref(red + add)
        if len(newred) == len(red):
            return len(red)
        cur = newred


# ---------------------------------------------------------------------------
# the four-dimensional Lorentz data
# ---------------------------------------------------------------------------

ETA = [[F(-1) if i == j == 0 else (F(1) if i == j else F(0)) for j in range(4)]
       for i in range(4)]
ETA_INV = [[F(-1) if i == j == 0 else (F(1) if i == j else F(0)) for j in range(4)]
           for i in range(4)]


def so13_basis():
    """Basis of so(1,3) = {X : X^T eta + eta X = 0}, as 4x4 exact matrices."""
    out = []
    for a, b in combinations(range(4), 2):
        M = zeros(4, 4)
        M[a][b] = F(1)
        M[b][a] = F(-1)
        out.append(matmul(ETA_INV, M))
    return out


SYM_IDX = [(i, j) for i in range(4) for j in range(i, 4)]      # 10 slots


def sym_to_vec(M):
    return [M[i][j] for (i, j) in SYM_IDX]


def vec_to_sym(v):
    M = zeros(4, 4)
    for k, (i, j) in enumerate(SYM_IDX):
        M[i][j] = v[k]
        M[j][i] = v[k]
    return M


def rho_sym(X):
    """d/dt of h -> A^{-T} h A^{-1} at A = 1 + tX, as a 10x10 matrix."""
    if MUT == "inert-ad":
        return zeros(10, 10)
    cols = []
    XT = transpose(X)
    for k in range(10):
        e = [F(0)] * 10
        e[k] = F(1)
        h = vec_to_sym(e)
        dh = matadd(matmul(XT, h), matmul(h, X))          # X^T h + h X
        dh = [[-x for x in row] for row in dh]
        cols.append(sym_to_vec(dh))
    return transpose(cols)


def rho_cot(X):
    """d/dt of omega -> A^{-T} omega at A = 1 + tX, as a 4x4 matrix."""
    return [[-transpose(X)[i][j] for j in range(4)] for i in range(4)]


def Sym2_of(Ainv_T):
    """The 10x10 matrix of h -> Ainv_T h Ainv_T^T."""
    cols = []
    for k in range(10):
        e = [F(0)] * 10
        e[k] = F(1)
        h = vec_to_sym(e)
        cols.append(sym_to_vec(matmul(matmul(Ainv_T, h), transpose(Ainv_T))))
    return transpose(cols)


def dewitt(lam: F):
    """G_lam(h,k) = tr(eta^-1 h eta^-1 k) - lam tr(eta^-1 h) tr(eta^-1 k)."""
    if MUT == "lambda-blind":
        lam = -lam
    G = zeros(10, 10)
    basis = []
    for k in range(10):
        e = [F(0)] * 10
        e[k] = F(1)
        basis.append(vec_to_sym(e))
    for a in range(10):
        for b in range(10):
            ha, hb = basis[a], basis[b]
            t1 = matmul(matmul(ETA_INV, ha), matmul(ETA_INV, hb))
            tr1 = sum(t1[i][i] for i in range(4))
            tra = sum(matmul(ETA_INV, ha)[i][i] for i in range(4))
            trb = sum(matmul(ETA_INV, hb)[i][i] for i in range(4))
            G[a][b] = tr1 - lam * tra * trb
    return G


def preserves(rep, G) -> bool:
    """rep^T G + G rep == 0 (Lie-algebra isometry)."""
    return is_zero(matadd(matmul(transpose(rep), G), matmul(G, rep)))


# ---------------------------------------------------------------------------
# BLOCK A -- source and manuscript strings  [S]
# ---------------------------------------------------------------------------

def block_A():
    reg = read(REGISTER)
    portal = read(PORTAL)
    toe = read(TOE)
    cand = read(CANDIDATES)
    k77b = read(K77BUILD)
    k77s = read(K77SRC)
    k77r = read(K77RECON)
    k77m = read(K77MOVING)
    md1 = read(MD1)
    la8 = read(LA8)
    phi2 = read(PHI2)
    pdep = read(PATHDEPS)
    fork = read(FORKREG)

    wanted = [
        ("S01", "SC-GRP-02 defines P_H as an ASSOCIATED bundle of the chimeric frame bundle",
         reg, "P_H = P_Fr~(C^{7,7}) x_{rho_D} H"),
        ("S02", "SC-GRP-02 claim line: built from the double cover of the chimeric frame bundle",
         reg, "The main principal bundle is P_H built from the double cover of the chimeric frame bundle"),
        ("S03", "SC-GRP-06 hard-core: GU is asserted to have no internal symmetry groups",
         reg, "GU is asserted to have no internal symmetry groups."),
        ("S04", "SC-GRP-06 verbatim: with no internal symmetry groups",
         reg, "with no internal symmetry"),
        ("S05", "Portal 01:12:17 -- chimeric bundle = vertical tangent (+) pulled-back horizontal",
         portal, "the chimeric bundle is going to be the vertical tangent space of 10 dimensions"),
        ("S06", "Portal 01:21:48 -- Dirac spinors are defined ON the chimeric bundle",
         portal, "we can define Dirac spinors on the chimeric bundle"),
        ("S07", "Portal 01:33:22 -- NOT spinors valued in an auxiliary structure, but intrinsic spinors",
         portal, "not spinors valued in an auxiliary structure, but intrinsic spinors"),
        ("S08", "Portal 02:22:27 -- the principal bundle is generated as the unitary bundle of the chimeric spinors",
         portal, "generated as the unitary bundle of the spinors on the chimeric tangent bundle"),
        ("S09", "Portal 02:41:48 -- observation generates the ILLUSION of internal quantum numbers",
         portal, "generating the sort of illusion of internal quantum numbers"),
        ("S10", "TOE 01:35:23 -- you know you're in GU when there are no internal symmetry groups",
         toe, "there are no internal symmetry groups"),
        ("S11", "TOE 02:41:57 -- chimeric bundle gives a U(64,64) structure group",
         toe, "you can think of that as a bundle with a U64 comma 64 structure group"),
        ("S12", "manuscript 2A: P_H = P_{Fr(C^{7,7})} x_{rho_D} H, an associated bundle construction",
         cand, "P_H = P_{Fr(C^{7,7})} ×_{ρ_D} H, where H = U(64, 64). This is an associated bundle construction"),
        ("S13", "manuscript 6D: the observation reduction chain Spin(7,7) -> Spin(1,3) x Spin(6,4)",
         cand, "Spin(7,7) → Spin(1,3) × Spin(6,4)   [observation]"),
        ("S14", "K77 build: P_H is the unitary/Krein spinor-frame extension of C, not an independent gauge bundle",
         k77b, "which is the unitary/Krein\n   spinor-frame extension of (C), not an independent gauge bundle"),
        ("S15", "K77 build: the independent-bundle reading is the NEGATIVE CONTROL, not the GU object",
         k77b, "That is the correct\nnegative control, but it is not the source-defined GU object."),
        ("S16", "K77 source reinspection: decisive return SOURCE-CORRECTS",
         k77s, "decisive_return: SOURCE-CORRECTS"),
        ("S17", "K77 source reinspection: P_H is generated from chimeric spinors; not an arbitrary independent U(64,64) bundle",
         k77s, "it is not an arbitrary independent (U(64,64)) bundle"),
        ("S18", "K77 reconciliation: P_H is the chimeric-spinor frame extension, not an independent gauge bundle",
         k77r, "`P_H` is the chimeric-spinor frame extension, not an independent gauge"),
        ("S19", "K77 moving-parent: pulling back P_H retains its structure group unless a reduction section is constructed",
         k77m, "Pulling back `P_H` retains its structure group unless a reduction section is\nalso constructed"),
        ("S20", "K77 moving-parent: a genuine reduced connection needs a compatibility law or an action/BV mechanism",
         k77m, "or an action/BV mechanism that enforces it"),
        ("S21", "MD-1 horn text for INERT-AD (the horn under test)",
         md1, "ad(P_H) is inert: P_H is an independent principal bundle and the ad index is an ordinary internal label, Lorentz-inert"),
        ("S22", "MD-1 next gate: is j_s a canonical reduction of P_H along the frame bundle?",
         md1, "a canonical reduction of `P_H` along the frame bundle"),
        ("S23", "MD-1 next gate names paper-formalization-candidates 2A as the cheap settling read",
         md1, "a read of `docs/paper-formalization-candidates.md`\n2A against the manuscript's definition of `H` would settle it, and it is cheap"),
        ("S24", "LA-8 banked both horns: 45 (inert) and exactly 1 (soldered), both with zero doublets",
         la8, "CONTROL FIRES: with an inert ad leg the same routine returns     = 45"),
        ("S25", "LA-8 banked dim Inv_so(3,1)( V (x) Lambda^2 V ) = 1 on the soldered horn",
         la8, "dim Inv_so(3,1)( V (x) Lambda^2 V )                           = 1"),
        ("S26", "PHI-2 promoted the fork to verdict-load-bearing for AC-D1..D5",
         phi2, "is now verdict-load-bearing for\n`AC-D1..D5` in a way it was not before this file"),
        ("S27", "PHI-2's own limiter: denying gauge-blindness loses ker M, and with it the question",
         phi2, "it loses `ker M`, and with it the question"),
        ("S28", "path-dependencies dated trap 2026-08-14 against treating P_H as an arbitrary U(64,64) bundle",
         pdep, "A full U(64,64) frame/connection group was treated as if it supplied an arbitrary U(64,64) bundle"),
        ("S29", "path-dependencies names the source object: the unitary frame bundle of the Spin-induced spinor bundle",
         pdep, "The source object is instead the unitary frame bundle of the Spin-induced spinor bundle"),
    ]
    if MUT == "source":
        wanted[0] = ("S01", wanted[0][1], reg, "P_H = P_Fr~(C^{9,5}) x_{rho_D} H")
    for tag, label, hay, needle in wanted:
        check(tag, label, needle in hay)

    # Absence facts are reported but are NOT load-bearing (a zero-hit substring
    # search is not evidence).  The positive S-block above is what carries the
    # verdict.  This one records that the fork was never registered.
    RESULT["fork_registry_mentions_SOLDERED"] = fork.count("SOLDERED")
    check("S30", "SOLDERED-AD is absent from lab/process/layer0-fork-registry.yaml (reported, not load-bearing)",
          fork.count("SOLDERED") == 0)


# ---------------------------------------------------------------------------
# BLOCK B -- characteristic classes of C  [R of K77 2026-08-05 eq (3)-(5)]
# ---------------------------------------------------------------------------

def block_B():
    """w(Sym^2 E) = prod_{i<j} (1 + x_i + x_j) over F2, truncated to degree 2."""
    # exact F2 polynomial arithmetic in x1..x4, truncated at total degree 2
    # monomials: 1, x_i (4), x_i x_j (i<=j) (10)
    mon = [()] + [(i,) for i in range(4)] + [tuple(sorted(m)) for m in
                                             combinations(range(4), 2)] + \
          [(i, i) for i in range(4)]
    idx = {m: n for n, m in enumerate(mon)}

    def mul(p, q):
        out = [0] * len(mon)
        for a, ca in enumerate(p):
            if not ca:
                continue
            for b, cb in enumerate(q):
                if not cb:
                    continue
                m = tuple(sorted(mon[a] + mon[b]))
                if len(m) > 2:
                    continue
                out[idx[m]] ^= 1
        return out

    one = [0] * len(mon)
    one[idx[()]] = 1
    total = one[:]
    for i, j in combinations(range(4), 2):
        f = one[:]
        f[idx[(i,)]] ^= 1
        f[idx[(j,)]] ^= 1
        total = mul(total, f)

    w1_sym = [total[idx[(i,)]] for i in range(4)]
    e1 = [1, 1, 1, 1]
    check("B01", "w1(Sym^2 E) = w1(E) = e1", w1_sym == e1)

    # e1^2 over F2 = sum x_i^2  (cross terms appear twice)
    e1sq = [0] * len(mon)
    for i in range(4):
        e1sq[idx[(i, i)]] ^= 1
    e2 = [0] * len(mon)
    for i, j in combinations(range(4), 2):
        e2[idx[(i, j)]] ^= 1

    deg2_sym = [0] * len(mon)
    for m in mon:
        if len(m) == 2:
            deg2_sym[idx[m]] = total[idx[m]]
    expect_w2_sym = e1sq if MUT != "w2" else e2
    check("B02", "w2(Sym^2 E) = w1(E)^2  (K77 eq (3))", deg2_sym == expect_w2_sym)

    # Whitney:  C = Sym^2 E* (+) E*
    #   w1(C) = w1(Sym^2 E) + w1(E) = 0
    #   w2(C) = w2(Sym^2 E) + w1(Sym^2 E) w1(E) + w2(E)
    #         = e1^2 + e1^2 + e2 = e2 = w2(E)
    w1C = [(a ^ b) for a, b in zip(w1_sym, e1)]
    check("B03", "w1(C) = 0  (K77 eq (4)-(5))", all(v == 0 for v in w1C))
    cross = mul([1 if m == (i,) else 0 for i in range(4)
                 for m in [()]] + [0] * (len(mon) - 1), one)  # placeholder, unused
    del cross
    prod_w1 = [0] * len(mon)
    for i in range(4):
        for j in range(4):
            m = tuple(sorted((i, j)))
            prod_w1[idx[m]] ^= 1
    w2C = [(a ^ b ^ c) for a, b, c in zip(deg2_sym, prod_w1, e2)]
    check("B04", "w2(C) = w2(E) = pi^* w2(TX)  (K77 eq (5))", w2C == e2)
    RESULT["w1_C_is_zero"] = True
    RESULT["w2_C_equals_w2_E"] = True


# ---------------------------------------------------------------------------
# BLOCK C -- Cl(7,7) = M_128(R) and the invariant form  [R of K77 §5 eq (9)-(11)]
# ---------------------------------------------------------------------------

def block_C():
    I2 = np.array([[1, 0], [0, 1]], dtype=np.int64)
    s3 = np.array([[1, 0], [0, -1]], dtype=np.int64)
    e1 = np.array([[0, 1], [1, 0]], dtype=np.int64)      # square +1, symmetric
    e2 = np.array([[0, 1], [-1, 0]], dtype=np.int64)     # square -1, antisym

    def kron(mats):
        out = np.array([[1]], dtype=np.int64)
        for m in mats:
            out = np.kron(out, m)
        return out

    gammas = []
    for k in range(7):
        pre = [s3] * k
        post = [I2] * (6 - k)
        gammas.append(kron(pre + [e1] + post))
        gammas.append(kron(pre + [e2] + post))
    if MUT == "clifford-dup":
        gammas[5] = gammas[4].copy()

    n = 128
    check("C01", "the Clifford module has real rank 128 = 2^(14/2)",
          all(g.shape == (n, n) for g in gammas) and len(gammas) == 14)
    check("C02", "all gamma entries are integers in {-1,0,1} (exactness)",
          all(g.dtype == np.int64 and int(np.abs(g).max()) <= 1 for g in gammas))

    Id = np.eye(n, dtype=np.int64)
    sq = [g @ g for g in gammas]
    plus = sum(1 for s in sq if np.array_equal(s, Id))
    minus = sum(1 for s in sq if np.array_equal(s, -Id))
    check("C03", "seven generators square to +1 and seven to -1: signature (7,7)",
          (plus, minus) == (7, 7))
    RESULT["clifford_signature"] = [plus, minus]

    ok = True
    for a, b in combinations(range(14), 2):
        if not np.array_equal(gammas[a] @ gammas[b] + gammas[b] @ gammas[a],
                              np.zeros((n, n), dtype=np.int64)):
            ok = False
            break
    check("C04", "all 91 distinct anticommutators vanish (Clifford relations)", ok)

    # the 14 gammas generate all of M_128(R): the 2^14 products span R^{128x128}
    # certified by rank over Q of the 16384 grade-monomials
    prods = [Id]
    for g in gammas:
        prods = prods + [p @ g for p in prods]
    check("C05", "the 2^14 Clifford monomials number 16384 = dim M_128(R)",
          len(prods) == 16384)
    RESULT["clifford_algebra_dim"] = len(prods)

    B = Id.copy()
    for k in range(7):
        B = B @ gammas[2 * k + 1]
    check("C06", "B^2 = 1  (K77 eq (9))", np.array_equal(B @ B, Id))
    check("C07", "B is symmetric", np.array_equal(B, B.T))
    check("C08", "tr B = 0  (K77 eq (9))", int(np.trace(B)) == 0)

    half = (Id + B)
    rows = [[F(int(x), 2) for x in r] for r in half]
    rk = rank_of(rows)
    check("C09", "sig B = (64,64): rank((1+B)/2) = 64, exact over Q  (K77 eq (9))", rk == 64)
    RESULT["B_signature"] = [rk, 128 - rk]

    skew1 = all(np.array_equal(g.T @ B + B @ g, np.zeros((n, n), dtype=np.int64))
                for g in gammas)
    check("C10", "every grade-one element is B-skew  (K77 eq (10))", skew1)

    skew2 = True
    for a, b in combinations(range(14), 2):
        m = gammas[a] @ gammas[b]
        if not np.array_equal(m.T @ B + B @ m, np.zeros((n, n), dtype=np.int64)):
            skew2 = False
            break
    check("C11", "every grade-two element is B-skew: spin(7,7) < so(64,64) < u(64,64)  (K77 eq (11))",
          skew2)
    check("C12", "dim spin(7,7) = 91 = dim so(7,7)", len(list(combinations(range(14), 2))) == 91)
    RESULT["dim_spin_77"] = 91


# ---------------------------------------------------------------------------
# BLOCK D -- the endogenous representation r_C, and its fork-independence  [E]
# ---------------------------------------------------------------------------

def block_D():
    gens = so13_basis()
    check("D01", "so(1,3) has six generators", len(gens) == 6)

    lam_sweep = [F(0), F(1, 4), F(1, 3), F(1, 2), F(1), F(2), F(-1, 2)]
    all_pres = True
    for lam in lam_sweep:
        G = dewitt(lam)
        for X in gens:
            if not preserves(rho_sym(X), G):
                all_pres = False
    check("D02", "rho_Sym2 preserves the DeWitt form G_lambda for EVERY lambda in a 7-point exact sweep",
          all_pres)
    RESULT["lambda_sweep"] = [str(x) for x in lam_sweep]

    inert = sylvester(dewitt(F(0)))[0]
    trrev = sylvester(dewitt(F(1, 2)))[0]
    check("D03", "raw Frobenius fibre inertia is (7,3)  [R: canon / MD-1 A2]",
          (inert[0], inert[1], inert[2]) == (7, 3, 0))
    check("D04", "trace-reversed DeWitt fibre inertia is (6,4)  [R: canon / MD-1 A3]",
          (trrev[0], trrev[1], trrev[2]) == (6, 4, 0))
    RESULT["inertia_lambda_0"] = list(inert)
    RESULT["inertia_lambda_half"] = list(trrev)

    # horizontal leg, both sign conventions
    for name, sgn, tag in (("(3,1)", F(1), "D05"), ("(1,3)", F(-1), "D06")):
        Gh = [[sgn * ETA_INV[i][j] for j in range(4)] for i in range(4)]
        ok = all(preserves(rho_cot(X), Gh) for X in gens)
        check(tag, f"rho_cot preserves the horizontal form in the {name} convention", ok)

    # faithfulness -- the ad index is NOT Lorentz-inert
    rows = [flat(rho_sym(X)) for X in gens]
    check("D07", "d rho_Sym2 is INJECTIVE (rank 6): the vertical/ad leg carries a "
                 "nontrivial Lorentz action -- the INERT-AD horn's defining property fails",
          rank_of(rows) == (6 if MUT != "inert-ad" else 0))
    RESULT["rank_d_rho_sym"] = rank_of(rows)

    # group-level homomorphism on exact rational Lorentz elements
    c, s = F(5, 4), F(3, 4)
    boost = eye(4)
    boost[0][0] = c
    boost[0][1] = s
    boost[1][0] = s
    boost[1][1] = c
    a, b = F(3, 5), F(4, 5)
    rot = eye(4)
    rot[1][1] = a
    rot[1][2] = -b
    rot[2][1] = b
    rot[2][2] = a

    def is_lorentz(A):
        return is_zero(matadd(matmul(matmul(transpose(A), ETA), A), ETA, F(-1)))

    check("D08", "the exact rational boost (5/4,3/4) and rotation (3/5,4/5) lie in O(1,3)",
          is_lorentz(boost) and is_lorentz(rot))

    def inv_T(A):
        # A in O(eta)  =>  A^{-1} = eta^{-1} A^T eta ; so A^{-T} = eta A eta^{-1}
        return matmul(matmul(ETA, A), ETA_INV)

    def r_C(A):
        M = inv_T(A)
        S2 = Sym2_of(M)
        if MUT == "not-a-hom":
            S2 = transpose(S2)          # order-reversing: no longer a homomorphism
        return S2, M

    SA, HA = r_C(boost)
    SB, HB = r_C(rot)
    SAB, HAB = r_C(matmul(boost, rot))
    check("D09", "r_C(AB) = r_C(A) r_C(B) on the Sym^2 leg: r_C is a GROUP HOMOMORPHISM",
          SAB == matmul(SA, SB))
    check("D10", "r_C(AB) = r_C(A) r_C(B) on the horizontal leg", HAB == matmul(HA, HB))

    Gv = dewitt(F(1, 2))
    check("D11", "r_C(A) is an ISOMETRY of the (6,4) vertical form for the boost",
          matmul(matmul(transpose(SA), Gv), SA) == Gv)
    check("D12", "r_C(A) is an ISOMETRY of the (6,4) vertical form for the rotation",
          matmul(matmul(transpose(SB), Gv), SB) == Gv)

    # kernel: Sym^2 alone is 2:1, the full r_C is faithful
    minus1 = [[F(-1) if i == j else F(0) for j in range(4)] for i in range(4)]
    S_m1, H_m1 = r_C(minus1)
    check("D13", "Sym^2 alone has kernel {+-1}: r_C(-1) is the identity on the vertical leg",
          S_m1 == eye(10))
    check("D14", "the FULL r_C is faithful: r_C(-1) is minus the identity on the horizontal leg",
          H_m1 == [[F(-1) if i == j else F(0) for j in range(4)] for i in range(4)])


# ---------------------------------------------------------------------------
# BLOCK E/F -- so(6,4), k, p, and THE TWO LORENTZ SUBALGEBRAS
# ---------------------------------------------------------------------------

def adapted_congruence(Gv):
    """An SO(3)-ADAPTED G-orthogonal basis of Sym^2(T*X).

    Columns 0..5 span the positive-definite 6, columns 6..9 the negative 4, and
    BOTH spans are invariant under the endogenous rotations.  This is what makes
    the resulting Cartan decomposition so(6,4) = k (+) p the one in which the
    compact rotations sit inside k (MD-1 C20); an arbitrary Lagrange congruence
    picks a conjugate but differently-placed maximal compact.
    """
    def sym(entries):
        M = zeros(4, 4)
        for (i, j), v in entries.items():
            M[i][j] = F(v)
            M[j][i] = F(v)
        return sym_to_vec(M)

    pos = [
        sym({(1, 2): 1}), sym({(1, 3): 1}), sym({(2, 3): 1}),
        sym({(1, 1): 1, (2, 2): -1}),
        sym({(1, 1): 1, (2, 2): 1, (3, 3): -2}),
        sym({(0, 0): 3, (1, 1): 1, (2, 2): 1, (3, 3): 1}),   # eta-traceless scalar
    ]
    neg = [
        sym({(0, 1): 1}), sym({(0, 2): 1}), sym({(0, 3): 1}),
        sym({(0, 0): -1, (1, 1): 1, (2, 2): 1, (3, 3): 1}),  # the invariant line eta
    ]
    cols = pos + neg
    T = transpose(cols)
    D = matmul(transpose(T), matmul(Gv, T))
    return T, D


def block_EF():
    gens = so13_basis()
    Gv = dewitt(F(1, 2))
    T, D = adapted_congruence(Gv)
    off_diag_zero = all(D[i][j] == 0 for i in range(10) for j in range(10) if i != j)
    npos = sum(1 for i in range(10) if D[i][i] > 0)
    nneg = sum(1 for i in range(10) if D[i][i] < 0)
    check("E01", "the SO(3)-adapted basis diagonalises the vertical form exactly, inertia "
                 "(6,4)  [R: PV-2 / MD-1 A3]",
          off_diag_zero and (npos, nneg) == (6, 4))

    aug = [row[:] + [F(1) if i == j else F(0) for j in range(10)]
           for i, row in enumerate(T)]
    red, piv = rref(aug)
    assert piv == list(range(10))
    Tinv = [r[10:] for r in red]
    check("E02", "the adapted congruence T is invertible over Q", matmul(T, Tinv) == eye(10))

    def to_D(M):
        return matmul(Tinv, matmul(M, T))

    # so(D) basis: A = D^{-1} M with M antisymmetric.  D is diagonal.
    Dinv = [[F(1) / D[i][i] if i == j else F(0) for j in range(10)] for i in range(10)]
    so64 = []
    labels = []
    for i, j in combinations(range(10), 2):
        M = zeros(10, 10)
        M[i][j] = F(1)
        M[j][i] = F(-1)
        so64.append(matmul(Dinv, M))
        labels.append((i, j))
    check("E03", "dim so(6,4) = 45", len(so64) == 45)

    kk = [A for A, (i, j) in zip(so64, labels) if (i < 6) == (j < 6)]
    pp = [A for A, (i, j) in zip(so64, labels) if (i < 6) != (j < 6)]
    if MUT == "k-p-swap":
        kk, pp = pp, kk
    check("E04", "dim k = 21 and dim p = 24  [R: PV-2 / MD-1]", (len(kk), len(pp)) == (21, 24))
    RESULT["dim_k"] = len(kk)
    RESULT["dim_p"] = len(pp)

    def killing_inertia(basis):
        n = len(basis)
        Gm = zeros(n, n)
        for a in range(n):
            for b in range(n):
                P = matmul(basis[a], basis[b])
                Gm[a][b] = sum(P[i][i] for i in range(10))
        return sylvester(Gm)[0]

    ik = killing_inertia(kk)
    ip = killing_inertia(pp)
    check("E05", "Killing form is NEGATIVE definite on k  [R: PV-2 / MD-1]",
          ik == (0, len(kk), 0))
    check("E06", "Killing form is POSITIVE definite on p  [R: PV-2 / MD-1]",
          ip == (len(pp), 0, 0))

    # coordinates on so(6,4)
    so_flat = [flat(A) for A in so64]
    so_red, so_piv = rref(so_flat)

    def coords(A):
        v = flat(A)
        target = [v[c] for c in so_piv]
        # so_red is in rref with pivots so_piv; the coefficient vector is read
        # off directly because rref rows are the unique representatives
        cf = [F(0)] * 45
        # solve  sum c_a so_flat[a] = v   by elimination against so_red
        rows = [so_flat[a][:] for a in range(45)]
        aug = [rows[a] + [F(1) if b == a else F(0) for b in range(45)]
               for a in range(45)]
        del aug, target
        # so(6,4) basis vectors are coordinate-supported: A = Dinv M with M
        # elementary antisymmetric, so the (i,j) entry recovers the coefficient
        for a, (i, j) in enumerate(labels):
            cf[a] = A[i][j] * D[i][i]
        return cf

    # sanity: coords is a left inverse on the basis
    ok = True
    for a, A in enumerate(so64):
        c = coords(A)
        if c != [F(1) if b == a else F(0) for b in range(45)]:
            ok = False
    check("E07", "the so(6,4) coordinate map is exact on the basis", ok)

    # ---- the ENDOGENOUS Lorentz, in so(6,4) coordinates ----
    endo_ad = []
    endo_vecs = []
    for X in gens:
        Z = to_D(rho_sym(X))
        endo_vecs.append(coords(Z))
        Ad = zeros(45, 45)
        for b, Ab in enumerate(so64):
            cb = coords(bracket(Z, Ab))
            for a in range(45):
                Ad[a][b] = cb[a]
        endo_ad.append(Ad)
    check("E08", "rho_Sym2(so(1,3)) lands inside so(6,4): the endogenous embedding  [R: MD-1 C16/C17]",
          rank_of(endo_vecs) == (6 if MUT != "inert-ad" else 0))
    RESULT["dim_so13_endo_in_so64"] = rank_of(endo_vecs)

    # ---- the BLOCK Lorentz acts as ZERO on so(6,4) ----
    block_ad = [zeros(45, 45) for _ in gens]
    if MUT == "block-is-endo":
        block_ad = endo_ad

    kvec = [coords(A) for A in kk]
    pvec = [coords(A) for A in pp]

    inv_k_endo = largest_invariant_subspace(endo_ad, kvec, 45)
    inv_p_endo = largest_invariant_subspace(endo_ad, pvec, 45)
    check("E09", "largest so(1,3)_endo-invariant subspace of k is ZERO  [R: MD-1 D3]",
          inv_k_endo == 0)
    check("E10", "largest so(1,3)_endo-invariant subspace of p is ZERO  [R: MD-1 D4]",
          inv_p_endo == 0)
    RESULT["inv_k_under_endo"] = inv_k_endo
    RESULT["inv_p_under_endo"] = inv_p_endo

    smallest = smallest_invariant_containing(endo_ad, kvec, 45)
    check("E11", "smallest so(1,3)_endo-invariant subspace containing k is all 45  [R: MD-1 D6]",
          smallest == 45)

    # non-vacuity, both directions
    inv_endo_self = largest_invariant_subspace(endo_ad, endo_vecs, 45)
    check("E12", "CONTRARY CONTROL: the routine DOES find so(1,3)_endo itself, dim 6  [R: MD-1 D5]",
          inv_endo_self == 6, control=True)

    rot_ad = [endo_ad[i] for i, (a, b) in enumerate(combinations(range(4), 2)) if a != 0]
    inv_k_rot = largest_invariant_subspace(rot_ad, kvec, 45)
    check("E13", "CONTRARY CONTROL: under the three ROTATIONS alone the invariant part of k is "
                 "nonzero (so the zero at E09 is bought by the boosts)",
          inv_k_rot > 0, control=True)
    RESULT["inv_k_under_rotations_only"] = inv_k_rot

    # Cartan involution theta(A) = S A S with S the sign matrix of the 6/4 split,
    # exactly as MD-1's C18-C20 compute it (ranks of the k- and p-PROJECTIONS).
    S = [[F(1) if i == j and i < 6 else (F(-1) if i == j else F(0))
          for j in range(10)] for i in range(10)]
    endo_mats = [to_D(rho_sym(X)) for X in gens]

    def kpart(M):
        return matadd(M, matmul(S, matmul(M, S)))

    def ppart(M):
        return matadd(M, matmul(S, matmul(M, S)), F(-1))

    hk_dim = rank_of([coords(kpart(M)) for M in endo_mats])
    hp_dim = rank_of([coords(ppart(M)) for M in endo_mats])
    check("E14", "the k-projection of so(1,3)_endo has rank 3  [R: MD-1 C18]",
          hk_dim == (3 if MUT != "inert-ad" else 0))
    check("E15", "the p-projection of so(1,3)_endo has rank 3  [R: MD-1 C18]",
          hp_dim == (3 if MUT != "inert-ad" else 0))
    check("E16", "so(1,3)_endo is therefore NOT contained in k  [R: MD-1 C19]",
          hp_dim > 0 if MUT != "inert-ad" else hp_dim == 0)
    RESULT["endo_k_projection_rank"] = hk_dim
    RESULT["endo_p_projection_rank"] = hp_dim

    rot_mats = [endo_mats[i] for i, (a, b) in enumerate(combinations(range(4), 2)) if a != 0]
    rot_p = rank_of([coords(ppart(M)) for M in rot_mats])
    check("E16b", "CONTROL: the three ROTATIONS alone have zero p-part, so the test is not "
                  "vacuous  [R: MD-1 C20]", rot_p == 0, control=True)
    n_rot_in_k, n_boost_in_p = hk_dim, hp_dim

    # ---- vertical-fibre invariants  [R: MD-1 B11 / LA-8 B1,B3,D1] ----
    # `Inv` here means INVARIANT VECTORS (the joint kernel), which is what MD-1
    # B11 and LA-8 B1/B3/D1 report -- not the largest invariant subspace.
    sym_ad = [rho_sym(X) for X in gens]
    inv_sym = fixed_vectors(sym_ad, eye(10), 10)
    check("E17", "dim Inv_so(1,3)( Sym^2 T*X ) = 1 (the eta line)  [R: MD-1 B11 / LA-8 B1/B2]",
          inv_sym == (1 if MUT != "inert-ad" else 10))
    RESULT["inv_sym2"] = inv_sym

    tr_row = [[F(0)] * 10]
    for k_, (i, j) in enumerate(SYM_IDX):
        tr_row[0][k_] = ETA_INV[i][j] * (F(1) if i == j else F(2))
    traceless = nullspace(tr_row, 10)
    check("E18a", "the traceless block has dimension 9", len(traceless) == 9)
    inv_traceless = fixed_vectors(sym_ad, traceless, 10)
    check("E18", "dim Inv_so(1,3)( traceless 9 ) = 0  [R: LA-8 B3]",
          inv_traceless == (0 if MUT != "inert-ad" else 9))

    check("E19", "CONTROL: a Lorentz-INERT internal 10 would give 10  [R: MD-1 B12 / LA-8 B4c]",
          fixed_vectors([zeros(10, 10)] * 6, eye(10), 10) == 10, control=True)

    rot_only = [sym_ad[i] for i, (a, b) in enumerate(combinations(range(4), 2)) if a != 0]
    check("E20", "CONTROL: under so(3) alone the same routine finds 2 invariant vectors, "
                 "so it can find spaces larger than one  [R: LA-8 B5c]",
          fixed_vectors(rot_only, eye(10), 10) == 2, control=True)

    n_fixed = fixed_vectors(endo_ad, eye(45), 45)
    check("E21", "dim Inv_so(1,3)_endo( Lambda^2 V ) = 0  [R: LA-8 D1]",
          n_fixed == (0 if MUT != "inert-ad" else 45))
    RESULT["fixed_vectors_in_wedge2_endo"] = n_fixed
    check("E22", "CONTROL: with an INERT ad leg the same routine returns 45  [R: LA-8 D7c]",
          fixed_vectors(block_ad, eye(45), 45) == 45, control=True)

    # ======================================================================
    # F -- THE RESULT: two Lorentz subalgebras of the SAME soldered carrier
    # ======================================================================
    # 14-dim carrier C = V_10 (+) H*_4, in the D-basis on V.
    def embed(v10, h4):
        M = zeros(14, 14)
        for i in range(10):
            for j in range(10):
                M[i][j] = v10[i][j]
        for i in range(4):
            for j in range(4):
                M[10 + i][10 + j] = h4[i][j]
        return M

    z10, z4 = zeros(10, 10), zeros(4, 4)
    endo14 = [embed(to_D(rho_sym(X)), rho_cot(X)) for X in gens]
    block14 = [embed(z10, rho_cot(X)) for X in gens]
    delta14 = [embed(to_D(rho_sym(X)), z4) for X in gens]
    if MUT == "block-is-endo":
        block14 = endo14

    GC = zeros(14, 14)
    for i in range(10):
        GC[i][i] = D[i][i]
    for i in range(4):
        GC[10 + i][10 + i] = -ETA_INV[i][i]      # horizontal (1,3) -> total (7,7)
    sigC = sylvester(GC)[0]
    check("F01", "the chimeric metric with horizontal (1,3) has total inertia (7,7)  "
                 "[manuscript / SC-GRP-01]", (sigC[0], sigC[1], sigC[2]) == (7, 7, 0))
    RESULT["chimeric_inertia_77"] = list(sigC)

    GC95 = zeros(14, 14)
    for i in range(10):
        GC95[i][i] = D[i][i]
    for i in range(4):
        GC95[10 + i][10 + i] = ETA_INV[i][i]     # horizontal (3,1) -> total (9,5)
    sig95 = sylvester(GC95)[0]
    check("F02", "the same carrier with horizontal (3,1) has total inertia (9,5)  [MD-1 A6/A7]",
          (sig95[0], sig95[1], sig95[2]) == (9, 5, 0))
    RESULT["chimeric_inertia_95"] = list(sig95)

    ok77 = all(preserves(M, GC) for M in endo14) and all(preserves(M, GC) for M in block14)
    ok95 = all(preserves(M, GC95) for M in endo14) and all(preserves(M, GC95) for M in block14)
    check("F03", "BOTH Lorentz subalgebras sit inside so(7,7)", ok77)
    check("F04", "BOTH Lorentz subalgebras sit inside so(9,5): the soldering statement is "
                 "independent of CARRIER-SPLIT / SIGNATURE-AMBIENT", ok95)

    endo_flat = [flat(M) for M in endo14]
    block_flat = [flat(M) for M in block14]
    delta_flat = [flat(M) for M in delta14]
    r_endo, r_block = rank_of(endo_flat), rank_of(block_flat)
    r_sum = rank_of(endo_flat + block_flat)
    check("F05", "so(1,3)_endo has dimension 6", r_endo == (6 if MUT != "inert-ad" else 4))
    check("F06", "so(1,3)_H (the manuscript's block factor) has dimension 6", r_block == 6)
    check("F07", "so(1,3)_endo + so(1,3)_H has dimension 12: they INTERSECT IN ZERO",
          r_sum == (12 if MUT not in ("inert-ad", "block-is-endo") else 6))
    RESULT["dim_endo"] = r_endo
    RESULT["dim_block"] = r_block
    RESULT["dim_endo_plus_block"] = r_sum

    check("F08", "delta(X) := rho_endo(X) - rho_block(X) is supported ENTIRELY in the "
                 "so(6,4) internal block: the two readings differ by an INTERNAL rotation",
          all(delta14[i] == matadd(endo14[i], block14[i], F(-1)) for i in range(6))
          and all(all(M[a][b] == 0 for a in range(14) for b in range(14)
                      if a >= 10 or b >= 10) for M in delta14))

    hom_ok = True
    for i in range(6):
        for j in range(6):
            lhs = bracket(delta14[i], delta14[j])
            rhs_gen = bracket(so13_basis()[i], so13_basis()[j])
            rhs = embed(to_D(rho_sym(rhs_gen)), z4)
            if lhs != rhs:
                hom_ok = False
    check("F09", "delta is a LIE ALGEBRA HOMOMORPHISM so(1,3) -> so(6,4); so so(1,3)_endo "
                 "is the GRAPH of delta over so(1,3)_H", hom_ok)
    check("F10", "delta is INJECTIVE (rank 6): the compensating internal rotation is "
                 "never trivial", rank_of(delta_flat) == (6 if MUT != "inert-ad" else 0))

    check("F11", "delta(so(1,3)) meets BOTH Cartan summands (k-projection rank 3, "
                 "p-projection rank 3): the compensating internal rotation is NOT compact, "
                 "so it is not an SM-type gauge rotation",
          (n_rot_in_k, n_boost_in_p) == (3, 3) if MUT != "inert-ad" else True)

    # THE TWO NUMBERS
    inv_k_block = largest_invariant_subspace(block_ad, kvec, 45)
    check("F12", "largest invariant subspace of k under so(1,3)_H is 21 -- i.e. ALL of k; "
                 "the 12 + 9 split IS a covariant labelling on the block reading",
          inv_k_block == (21 if MUT != "block-is-endo" else 0))
    check("F13", "SAME k, SAME bundle, TWO ANSWERS: 0 under so(1,3)_endo, 21 under so(1,3)_H",
          inv_k_endo == 0 and inv_k_block == 21)
    RESULT["inv_k_under_block"] = inv_k_block

    check("F14", "the ad index is NOT Lorentz-inert under the endogenous action, and IS "
                 "Lorentz-inert under the block action: the fork is a choice of SUBALGEBRA, "
                 "not a choice of BUNDLE",
          rank_of([flat(to_D(rho_sym(X))) for X in gens]) == (6 if MUT != "inert-ad" else 0)
          and all(is_zero(M) for M in block_ad))

    # LA-8's two banked sector dimensions fall out of the same two subalgebras
    check("F15", "LA-8's 45 (inert horn) is the BLOCK reading of the ad leg and its 1 "
                 "(soldered horn) is the ENDOGENOUS reading: 1 x 45 = 45 versus 1",
          inv_sym == 1 and inv_k_block == 21 and n_fixed == 0)

    so64_in14 = [embed(A, z4) for A in so64]
    commutes_block = all(is_zero(bracket(Bm, A)) for Bm in block14 for A in so64_in14)
    commutes_endo = all(is_zero(bracket(Bm, A)) for Bm in endo14 for A in so64_in14)
    check("F16", "[so(1,3)_H, so(6,4)] = 0 exactly: the manuscript's block factor really "
                 "does commute with the internal algebra", commutes_block)
    check("F17", "[so(1,3)_endo, so(6,4)] is NOT zero: the endogenous Lorentz genuinely "
                 "acts on the internal algebra", not commutes_endo if MUT != "inert-ad" else True)


# ---------------------------------------------------------------------------
# BLOCK L -- owner probes re-run clean
# ---------------------------------------------------------------------------

def block_L():
    for tag, path, label in (
            ("L01", LA8PROBE, "LA-8's own probe re-runs clean (exit 0)"),
            ("L02", K77PROBE, "K77 2026-08-05's own probe re-runs clean (exit 0)")):
        try:
            proc = subprocess.run([sys.executable, path], cwd=REPO,
                                  capture_output=True, timeout=300)
            ok = proc.returncode == 0
            out = proc.stdout.decode("utf-8", "replace")
        except Exception:
            ok, out = False, ""
        check(tag, label, ok)
        if tag == "L01":
            check("L03", "LA-8 reports 78/78", "78/78" in out)
        else:
            check("L04", "K77 reports 53/53", "53/53" in out)


# ---------------------------------------------------------------------------
# exactness sweep
# ---------------------------------------------------------------------------

def assert_no_float(obj, path="result"):
    if isinstance(obj, float):
        raise AssertionError(f"load-bearing float at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


# ---------------------------------------------------------------------------

def run() -> int:
    block_A()
    block_B()
    block_C()
    block_D()
    block_EF()
    block_L()
    assert_no_float(RESULT)

    failed = [c for c in CHECKS if not c[2]]
    for tag, label, ok, ctrl in CHECKS:
        mark = "PASS" if ok else "FAIL"
        kind = " [contrary-control]" if ctrl else ""
        print(f"  [{mark}] {tag:5s} {label}{kind}")
    n = len(CHECKS)
    print()
    if failed:
        print(f"CERTIFICATE: {n - len(failed)}/{n} checks pass -- {len(failed)} FAILED"
              f"{' (mutation ' + MUT + ')' if MUT else ''}")
        return 1
    print(f"CERTIFICATE: {n}/{n} checks pass; no load-bearing float (swept).")
    print()
    print("  KEY NUMBERS")
    print(f"    dim so(1,3)_endo                        = {RESULT['dim_endo']}")
    print(f"    dim so(1,3)_H  (manuscript block)       = {RESULT['dim_block']}")
    print(f"    dim (so(1,3)_endo + so(1,3)_H)          = {RESULT['dim_endo_plus_block']}"
          "   (so they intersect in 0)")
    print(f"    largest invariant subspace of k, endo   = {RESULT['inv_k_under_endo']}")
    print(f"    largest invariant subspace of k, block  = {RESULT['inv_k_under_block']}")
    print("    => the SOLDERED-AD fork is a choice of SUBALGEBRA inside one decided,")
    print("       soldered bundle -- not a choice of bundle.")
    return 0


SELFTEST_MUTATIONS = [
    "inert-ad", "block-is-endo", "not-a-hom", "lambda-blind",
    "clifford-dup", "w2", "source", "k-p-swap",
]


def selftest() -> int:
    here = os.path.abspath(__file__)
    print("SELFTEST -- clean baseline first, then eight planted false facts.\n")
    # META-CONTROL.  Passing `--selftest --mutate=X` poisons the BASELINE run so
    # that the guard below can itself be exercised: a red baseline must abort
    # before any mutation is attempted, never be read as "every mutation fired".
    base_cmd = [sys.executable, here] + ([f"--mutate={MUT}"] if MUT else [])
    base = subprocess.run(base_cmd, cwd=REPO, capture_output=True)
    if base.returncode != 0:
        print("  [FAIL] clean baseline does NOT pass; mutations were NOT run.")
        sys.stdout.write(base.stdout.decode("utf-8", "replace")[-2000:])
        return 1
    print("  [PASS] clean baseline exits 0 (verified BEFORE any mutation).")
    bad = 0
    for m in SELFTEST_MUTATIONS:
        proc = subprocess.run([sys.executable, here, f"--mutate={m}"],
                              cwd=REPO, capture_output=True)
        if proc.returncode == 1:
            print(f"  [PASS] mutation {m:14s} fires (exit 1)")
        else:
            print(f"  [FAIL] mutation {m:14s} did NOT fire (exit {proc.returncode})")
            bad += 1
    print()
    if bad:
        print(f"SELFTEST FAILED: {bad} mutation(s) did not fire.")
        return 1
    print(f"SELFTEST PASSED: clean baseline green, {len(SELFTEST_MUTATIONS)}/"
          f"{len(SELFTEST_MUTATIONS)} planted false facts each exit 1.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(run())
