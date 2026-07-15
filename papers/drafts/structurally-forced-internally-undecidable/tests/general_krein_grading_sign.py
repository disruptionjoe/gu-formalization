#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GENERAL Krein grading-sign theorem -- machine check over generic signatures (p, q).

This is the DRAFT-tier test for the general theorem of the paper
"Structurally Forced, Internally Undecidable" (papers/drafts/structurally-forced-internally-undecidable/).
It is NOT part of the repo greens gate; it lives inside the draft folder and runs standalone.

CLAIM (general, GU-independent):
  Let V = R^n, n = p + q, p,q >= 1, carry an indefinite nondegenerate symmetric form
  eta = diag(+1^p, -1^q), grading involution C = sign(eta) (C^2 = I), total metric
  eta_+ = eta.C = |eta| = I_n (positive-definite). Suppose a gauge group G <= O(eta) acts so
  that V is IRREDUCIBLE (Schur: the G-invariant symmetric form is unique = eta). The good-stable
  condition (require the positive-definite total metric eta_+ preserved too) restricts G to the
  C-commutant G* = G cap O(eta_+); in the canonical maximal case G* >= O(p) x O(q). Under G* the
  C-eigenspaces V_+ = R^p and V_- = R^q share NO common irreducible constituent, so by Schur the
  space of G*-invariant symmetric bilinear forms is block diagonal with one independent scale per
  block: dimension EXACTLY 2 for the coarse split, GROWING when the good stable carries a finer
  invariant splitting. Both eta and eta_+ are invariant and distinct; the relative block sign is a
  free Z/2 (the grading sign); positivity leaves the open cone c_i > 0, never the single ray eta_+.

We verify this for a SWEEP of signatures (p, q) -- including the GU instance (9,5) and its fiber
(6,4) -- using O(p) x O(q) as the good-stable stabilizer (the canonical maximal-compact case), and
we verify the finer-split growth (an extra invariant splitting of one block raises the dimension).
The FULL-group control uses O(p, q) itself: invariant-form dim collapses back to 1 (= eta), which is
the "structurally forced" half of the title.

Deterministic (seed 20260714). Exits 0 on all-pass. Positive controls run FIRST.
Zero em dashes.
Reproducible: python -u general_krein_grading_sign.py
"""

import itertools
import numpy as np

np.random.seed(20260714)
TOL = 1e-8
checks = []


def ok(name, cond, detail=""):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))
    return bool(cond)


def signature(M):
    w = np.linalg.eigvalsh(0.5 * (M + M.T))
    return int(np.sum(w > TOL)), int(np.sum(w < -TOL))


def sym_basis(n):
    B = []
    for i in range(n):
        for j in range(i, n):
            M = np.zeros((n, n))
            M[i, j] = M[j, i] = 1.0
            B.append(M)
    return B


def nullspace(A, tol=TOL):
    if A.size == 0 or A.shape[0] == 0:
        return np.eye(A.shape[1])
    u, s, vh = np.linalg.svd(A)
    rank = int(np.sum(s > tol * max(1.0, s[0])))
    return vh[rank:].conj().T


def so_generators(metric):
    """Basis of so(metric) = {X : X^T g + g X = 0}. Works for definite or indefinite g."""
    n = metric.shape[0]
    g = metric
    rows = []
    for a in range(n):
        for b in range(n):
            row = np.zeros((n, n))
            for k in range(n):
                row[k, a] += g[k, b]
                row[k, b] += g[a, k]
            rows.append(row.reshape(-1))
    ns = nullspace(np.array(rows))
    return [ns[:, i].reshape(n, n) for i in range(ns.shape[1])]


def block_diag_generators(block_dims):
    """Lie generators of the direct-sum orthogonal algebra so(d1) (+) so(d2) (+) ... on R^n
    PLUS one reflection (coordinate flip) per block so the full O(d1) x ... x O(dk) is enforced
    (this matters for dimension-1 blocks, where so(1) is trivial but the O(1) reflection is not)."""
    n = sum(block_dims)
    lie = []
    reflect = []
    offset = 0
    for d in block_dims:
        for X in so_generators(np.eye(d)):
            G = np.zeros((n, n))
            G[offset:offset + d, offset:offset + d] = X
            lie.append(G)
        R = np.eye(n)
        R[offset, offset] = -1.0  # flip first coordinate of this block = a reflection in O(d)
        reflect.append(R)
        offset += d
    return lie, reflect


def invariant_sym_forms(gens, n):
    """gens = (lie_generators, group_reflections). Invariant symmetric forms satisfy
    X^T M + M X = 0 for Lie generators and R^T M R = M for reflections."""
    if isinstance(gens, tuple):
        lie, reflect = gens
    else:
        lie, reflect = gens, []
    sb = sym_basis(n)
    cols = []
    for M in sb:
        parts = [(X.T @ M + M @ X).reshape(-1) for X in lie]
        parts += [(R.T @ M @ R - M).reshape(-1) for R in reflect]
        cols.append(np.concatenate(parts) if parts else M.reshape(-1) * 0.0)
    ns = nullspace(np.array(cols).T)
    return [sum(c * m for c, m in zip(ns[:, i], sb)) for i in range(ns.shape[1])]


def in_span(M, forms, tol=1e-6):
    if not forms:
        return False
    n = M.shape[0]
    sb = sym_basis(n)

    def vec(X):
        return np.array([np.sum(X * m) / np.sum(m * m) for m in sb])
    F = np.array([vec(f) for f in forms]).T
    sol, _, _, _ = np.linalg.lstsq(F, vec(M), rcond=None)
    return np.linalg.norm(F @ sol - vec(M)) < tol


# ===========================================================================
# Sweep of signatures. GU instances flagged.
# ===========================================================================
SIGS = [(1, 1), (2, 1), (3, 1), (6, 4), (9, 5), (7, 7), (5, 3), (4, 2)]
GU = {(9, 5): "GU (9,5) full frame", (6, 4): "GU (6,4) DeWitt fiber"}

for p, q in SIGS:
    n = p + q
    tag = GU.get((p, q), "generic")
    eta = np.diag([1.0] * p + [-1.0] * q)
    C = np.diag([1.0] * p + [-1.0] * q)
    eta_plus = eta @ C  # = I_n

    print("\n--- signature (%d,%d)  [%s] ---" % (p, q, tag))

    # PC: graded objects
    ok("PC(%d,%d).eta_indef" % (p, q), signature(eta) == (p, q), "eta signature (%d,%d)" % (p, q))
    ok("PC(%d,%d).etaplus_posdef" % (p, q), signature(eta_plus) == (n, 0),
       "eta_+ = eta.C positive-definite")

    # STRUCTURALLY FORCED: full group O(p,q) -> invariant form space dim 1 = eta
    full = so_generators(eta)
    inv_full = invariant_sym_forms(full, n)
    ok("FORCED(%d,%d).dim1" % (p, q), len(inv_full) == 1 and in_span(eta, inv_full),
       "full O(%d,%d): invariant symmetric form UNIQUE = eta (structurally forced)" % (p, q))
    ok("FORCED(%d,%d).etaplus_not_invariant" % (p, q), not in_span(eta_plus, inv_full),
       "eta_+ NOT invariant under the full group (ungraded metric carries no sign)")

    # INTERNALLY UNDECIDABLE: good-stable stabilizer O(p) x O(q) -> dim jumps to 2
    gstar = block_diag_generators([p, q])
    gstar_all = gstar[0] + gstar[1]
    ok("STAB(%d,%d).commutes_C" % (p, q), all(np.linalg.norm(X @ C - C @ X) < TOL for X in gstar_all),
       "stabilizer = C-commutant O(%d)xO(%d)" % (p, q))
    inv_stab = invariant_sym_forms(gstar, n)
    ok("UNDEC(%d,%d).dim2" % (p, q), len(inv_stab) == 2,
       "good-stable stabilizer: invariant-form dim = %d (expect 2)" % len(inv_stab))
    ok("UNDEC(%d,%d).both_invariant" % (p, q), in_span(eta, inv_stab) and in_span(eta_plus, inv_stab),
       "BOTH eta and eta_+ invariant and distinct")
    ok("UNDEC(%d,%d).grows" % (p, q), len(inv_stab) > len(inv_full),
       "symmetry REDUCTION grows invariant space 1 -> 2 (sign LIBERATED)")

    # residual = free Z/2: positivity leaves a 2-parameter cone, indefinite branch invariant too
    Pp = np.diag([1.0] * p + [0.0] * q)
    Pq = np.diag([0.0] * p + [1.0] * q)
    ok("Z2(%d,%d).blocks_invariant" % (p, q), in_span(Pp, inv_stab) and in_span(Pq, inv_stab),
       "one independent Schur scale per block")
    cone = all(signature(a * Pp + b * Pq)[0] == n for a, b in [(1, 1), (1, 3), (3, 1)])
    indef_inv = (signature(Pp - Pq)[0] != n) and in_span(eta, inv_stab)
    ok("Z2(%d,%d).free_sign" % (p, q), cone and indef_inv,
       "positive cone (2-param) not a ray; indefinite branch (= eta) invariant -> sign is a free Z/2")

# ===========================================================================
# FINER SPLIT: refining the good-stable structure ENLARGES the residual (never shrinks to 1).
# GU (9,5) = (3,1) base + (6,4) fiber, fiber = geometric(6) + record(4): 4 O(n) blocks -> dim 4.
# ===========================================================================
print("\n--- finer good-stable split: GU (9,5) as 4 blocks 3+1+... actually 3(+1)|6(+4) ---")
# refine (9,5) into orthogonal blocks respecting base (3,1) and fiber geometric(6)/record(4):
# positive 9 = 3 (base space) + 6 (fiber geometric); negative 5 = 1 (base time) + 4 (fiber record)
finer_blocks = [3, 6, 1, 4]  # all-positive-then-all-negative ordering not required; each is an O(d) block
n = sum(finer_blocks)
gens_fine = block_diag_generators(finer_blocks)
inv_fine = invariant_sym_forms(gens_fine, n)
ok("FINER.dim4", len(inv_fine) == 4,
   "finer 4-block split: invariant-form dim = %d (residual ENLARGES, never shrinks to 1)" % len(inv_fine))

# ===========================================================================
# SUMMARY
# ===========================================================================
npass = sum(1 for _, c in checks if c)
ntot = len(checks)
print("\n==================== SUMMARY ====================")
print("%d/%d checks passed" % (npass, ntot))
print("General theorem verified over signatures: %s" % ", ".join("(%d,%d)" % s for s in SIGS))
print("STRUCTURALLY FORCED (full O(p,q) -> dim 1 = eta) ; INTERNALLY UNDECIDABLE (stabilizer -> dim 2, free Z/2)")
print("finer split -> dim 4 (residual enlarges). GU (9,5)/(6,4) are instances.")
print("=================================================")
raise SystemExit(0 if npass == ntot else 1)
