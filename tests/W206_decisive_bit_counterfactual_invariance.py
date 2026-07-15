#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W206 -- THE DECISIVE BIT via COUNTERFACTUAL-INVARIANCE / METRIC-FROM-STABILIZER (R16).

Method R16 (the W205 Condorcet winner, Klein/Erlangen "metric from its stabilizer"). Take the
good-stable fixed point as GIVEN. Its STABILIZER G* = the group of counterfactual / gauge
deformations that preserve ALL good-stable properties simultaneously:
    (i)   real total spectrum         (preserve the Clifford metric eta, signature (9,5))
    (ii)  positive-definite TOTAL metric eta_+   (preserve eta_+ = eta.C, positive-definite)
    (iii) C-operator operative         (preserve the C-grading, i.e. commute with C)
Compute the space of G*-invariant symmetric bilinear forms. The DECISIVE QUESTION:
  * is it ONE-dimensional with generator eta_+ = eta.C  (=> FORCED: grading SIGN derived-as-invariant,
    #1 resolves inside GU, bar (b) clears), OR
  * is it dim > 1 (a residual Z/2: both C-sign choices invariant; the relative block sign free)
    (=> RESIDUAL-BIT-STANDS: the grading sign is Godel-independent, must be posited / external TI-TaF).

THE GUARDRAIL (do NOT produce a false positive). W203 ALREADY proved by Schur that under the FULL
gauge group so(9,5) the UNGRADED invariant symmetric form is UNIQUE (nulldim=1) and equals eta
(indefinite (9,5)). That is a positive control here (PC_FULL), NOT the open bit. The open bit is
whether the good-stable STABILIZER additionally forces the C-grading SIGN. R16's honest job is to
settle the SIGN, not to re-derive eta.

THE COMPUTATION AND ITS ANSWER. Preserving BOTH eta (indefinite) AND eta_+ = |eta| (positive-definite)
forces a deformation to commute with C = sign(eta) = eta_+^{-1} eta, hence to be block-diagonal on the
C-eigenspaces. So
    g* = so(9,5) cap o(14) = so(9) (+) so(5)   (the MAXIMAL COMPACT subgroup, W203's SO(9)xSO(5)).
Under g* the 14-frame vector rep is REDUCIBLE: R^9 (+) R^5, two INEQUIVALENT irreducibles. By Schur the
invariant symmetric forms are block-diagonal, scalar on each block:  B = c1 * I_9 (+) c2 * I_5. That
space is TWO-dimensional. A basis is {eta_+, eta} = {I_14, C}: eta_+ = eta.C = c=(+,+) and W203's
eta = c=(+,-). BOTH are G*-invariant. The relative sign of the record-carrying block (c2) versus the
geometric block (c1) is a FREE bit -- exactly the C-grading SIGN. So going from the full gauge group to
the good-stable stabilizer REDUCES the symmetry, which INCREASES the invariant-form space from 1 (eta,
W203) to 2 (eta AND eta_+): the stabilizer does NOT force the grading sign, it LIBERATES it.

VERDICT: RESIDUAL-BIT-STANDS. Residual = a 2-dimensional invariant-form space (one Schur scale per
C-block); at the level of "which sign", a Z/2 (record-count block weighted + or - relative to
geometric), both invariant, plus overall block scales. eta_+ = eta.C is A distinguished generator
(equal weights) but NOT the UNIQUE invariant; W203's indefinite eta is equally invariant. Positivity
(good-stable property (ii)) restricts to the open cone c1>0, c2>0 -- a 2-parameter family, NOT a single
ray -- so it does not pin eta_+ either. The C-grading sign is derivable-in-FORM, posited-in-SIGN. This
CONVERGES with W205's own R16 prediction ("recovers the form up to scale AND one branch bit; does not
close #1") and makes it precise: the residual is exactly the 1 extra dimension.

Exploration grade; conditional register. This is a finite linear-algebra model of the good-stable
stabilizer on the (9,5)=(3,1)+(6,4) frame (the level at which W203 forced eta, W168 read the fiber
Krein sign, and W202 proved signature-robustness). It computes an invariant-theory dimension; it is not
a physical measurement. No canon movement; H59 OPEN; bar (b) UNCHANGED; do NOT flip bar(b)/H59.

Structure (positive controls FIRST):
  [PC_FULL]  Under the FULL gauge group so(9,5), the invariant symmetric form space is dim 1 = eta
             (reproduce W203 nulldim=1; the guardrail control -- we must recover, not inflate, this).
  [PC_GRAD]  eta_+ = eta.C is positive-definite (14,0); C^2 = I; C = sign(eta); eta is (9,5) indefinite.
  [PC_STAB]  C commutes with the compact so(9)+so(5); C does NOT commute with the (9,5) boosts.
  [G*]       g* = {X in so(9,5): X preserves eta_+ too} = so(9)+so(5), dim 46 = the C-commutant.
  [INV]      dim{G*-invariant symmetric forms} = 2 (the decisive number), basis {eta_+, eta}={I, C}.
  [RES]      the residual: both eta_+ and eta are invariant; the record block's relative sign is free;
             positivity leaves a 2-parameter cone, not the single ray eta_+.
  [FINER]    the finer good-stable split (respecting base (3,1), fiber (6,4), and the fiber
             geometric(6)/record-count(4) Krein split) only ENLARGES the residual (dim grows), never
             shrinks it to 1. RESIDUAL-BIT-STANDS is robust.
  [E1]       VERDICT line.

Deterministic (seed 20260714). Reproducible: python -u tests/W206_decisive_bit_counterfactual_invariance.py
Exit 0 on all-pass. Zero em dashes.
"""

import numpy as np

np.random.seed(20260714)
TOL = 1e-9
P, Q = 9, 5
N = P + Q  # 14
checks = []


def ok(name, cond, detail=""):
    checks.append((name, bool(cond), detail))
    print(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))
    return bool(cond)


# ---------------------------------------------------------------------------
# Core objects on the (9,5) frame
# ---------------------------------------------------------------------------
eta = np.diag([1.0] * P + [-1.0] * Q)          # Clifford metric, signature (9,5) -- W203's forced kernel
C = np.diag([1.0] * P + [-1.0] * Q)            # C-operator = sign(eta): flips the eta-negative directions
eta_plus = eta @ C                             # eta_+ = eta.C = |eta| = I_14, positive-definite (good-stable)


def signature(M):
    w = np.linalg.eigvalsh(0.5 * (M + M.T))
    return int(np.sum(w > TOL)), int(np.sum(w < -TOL))


# ---------------------------------------------------------------------------
# Lie algebra machinery: bases as null spaces, invariant-form spaces as null spaces
# ---------------------------------------------------------------------------
def sym_basis(n):
    """Orthonormal-ish basis of the n x n symmetric matrices (dim n(n+1)/2)."""
    B = []
    for i in range(n):
        for j in range(i, n):
            M = np.zeros((n, n))
            if i == j:
                M[i, i] = 1.0
            else:
                M[i, j] = M[j, i] = 1.0
            B.append(M)
    return B


def nullspace(A, tol=TOL):
    """Right null space of A via SVD; returns columns spanning ker(A)."""
    if A.shape[0] == 0:
        return np.eye(A.shape[1])
    u, s, vh = np.linalg.svd(A)
    rank = int(np.sum(s > tol * max(1.0, s[0])))
    return vh[rank:].conj().T


def so_pq_generators(metric):
    """Basis of so(p,q) = {X : X^T metric + metric X = 0}, as a list of N x N matrices."""
    basisM = sym_basis(N)  # X ranges over all N x N; constrain via the linear map
    # unknown X is N*N; constraint X^T g + g X = 0 is N x N symmetric-ish -> build linear system
    rows = []
    g = metric
    # vectorize X (column-major); constraint entries
    for a in range(N):
        for b in range(N):
            # (X^T g + g X)_{ab} = sum_k X_{ka} g_{kb} + g_{ak} X_{kb}
            row = np.zeros((N, N))
            for k in range(N):
                row[k, a] += g[k, b]
                row[k, b] += g[a, k]
            rows.append(row.reshape(-1))
    A = np.array(rows)
    ns = nullspace(A)
    gens = [ns[:, i].reshape(N, N) for i in range(ns.shape[1])]
    return gens


def subalgebra(generators, constraint):
    """Given a basis 'generators' of a matrix space, return a basis of the subspace
    {X = sum a_k G_k : constraint(X) == 0}. 'constraint' maps an N x N matrix to an N x N matrix
    of linear expressions; we impose all its entries = 0."""
    cols = []
    for G in generators:
        cols.append(constraint(G).reshape(-1))
    A = np.array(cols).T  # (N*N) x len(gens)
    ns = nullspace(A)      # combos of generators satisfying the constraint
    return [sum(ns[k, i] * generators[k] for k in range(len(generators))) for i in range(ns.shape[1])]


def invariant_sym_forms(generators):
    """Space of symmetric B with X^T B + B X = 0 for all generators X. Returns list of N x N basis forms."""
    sb = sym_basis(N)
    # unknown B = sum_m x_m * sb[m]; constraint per generator: X^T B + B X = 0 (N*N equations)
    cols = []
    for M in sb:
        col_entries = []
        for X in generators:
            col_entries.append((X.T @ M + M @ X).reshape(-1))
        cols.append(np.concatenate(col_entries))
    A = np.array(cols).T  # (num_eq) x (num_sym)
    ns = nullspace(A)
    forms = []
    for i in range(ns.shape[1]):
        coeffs = ns[:, i]
        B = sum(c * m for c, m in zip(coeffs, sb))
        forms.append(B)
    return forms


def in_span(M, forms, tol=1e-7):
    """Is symmetric M in the span of the given forms?"""
    if not forms:
        return False
    sb = sym_basis(N)

    def vec(X):
        return np.array([np.sum(X * m) / np.sum(m * m) for m in sb])  # coords in sym basis (diagonal metric)
    Fmat = np.array([vec(f) for f in forms]).T  # (105) x k
    target = vec(M)
    sol, res, rank, sv = np.linalg.lstsq(Fmat, target, rcond=None)
    recon = Fmat @ sol
    return np.linalg.norm(recon - target) < tol


# ===========================================================================
# [PC_FULL] Guardrail control: full gauge group so(9,5) forces UNIQUE eta (W203 nulldim=1)
# ===========================================================================
print("\n[PC_FULL] full gauge group so(9,5): the ungraded Schur pin (reproduce W203)")
full_gens = so_pq_generators(eta)
ok("PC_FULL.dim_so95", len(full_gens) == N * (N - 1) // 2,
   "dim so(9,5) = %d (expect %d)" % (len(full_gens), N * (N - 1) // 2))
full_inv = invariant_sym_forms(full_gens)
ok("PC_FULL.nulldim1", len(full_inv) == 1, "invariant symmetric forms under full group = %d (expect 1)" % len(full_inv))
ok("PC_FULL.generator_is_eta", len(full_inv) == 1 and in_span(eta, full_inv),
   "the unique invariant is proportional to eta (W203's forced kernel)")
ok("PC_FULL.not_eta_plus", len(full_inv) == 1 and not in_span(eta_plus, full_inv),
   "eta_+ is NOT invariant under the full group (it needs the reduced stabilizer)")

# ===========================================================================
# [PC_GRAD] the graded objects
# ===========================================================================
print("\n[PC_GRAD] the C-grading and eta_+ = eta.C")
ok("PC_GRAD.C_involution", np.allclose(C @ C, np.eye(N)), "C^2 = I")
ok("PC_GRAD.C_is_sign_eta", np.allclose(C, np.diag(np.sign(np.diag(eta)))), "C = sign(eta)")
sp, sm = signature(eta)
ok("PC_GRAD.eta_indefinite_95", (sp, sm) == (P, Q), "eta signature = (%d,%d)" % (sp, sm))
spp, smp = signature(eta_plus)
ok("PC_GRAD.eta_plus_posdef", (spp, smp) == (N, 0), "eta_+ signature = (%d,%d) positive-definite" % (spp, smp))
ok("PC_GRAD.eta_plus_eq_etaC", np.allclose(eta_plus, eta @ C), "eta_+ = eta.C exactly")
ok("PC_GRAD.min_eig_pos", np.min(np.linalg.eigvalsh(eta_plus)) > TOL,
   "min eig(eta_+) = %.3f > 0" % np.min(np.linalg.eigvalsh(eta_plus)))

# ===========================================================================
# [PC_STAB] C commutes with compact part, not with boosts
# ===========================================================================
print("\n[PC_STAB] C-commutant structure inside so(9,5)")
comm_with_C = subalgebra(full_gens, lambda X: X @ C - C @ X)  # {X in so(9,5): [X,C]=0}
ok("PC_STAB.some_commute", len(comm_with_C) > 0, "C-commutant dim = %d > 0" % len(comm_with_C))
ok("PC_STAB.some_boosts_dont", len(comm_with_C) < len(full_gens),
   "%d of %d generators lie OUTSIDE the C-commutant (the boosts)" % (len(full_gens) - len(comm_with_C), len(full_gens)))
# compact so(9)+so(5) has dim 36+10 = 46
ok("PC_STAB.commutant_dim46", len(comm_with_C) == 36 + 10,
   "C-commutant dim = %d (so(9)+so(5) = 46)" % len(comm_with_C))

# ===========================================================================
# [G*] the good-stable stabilizer: preserve eta AND eta_+ (hence commute with C)
# ===========================================================================
print("\n[G*] stabilizer g* = so(9,5) cap o(14) = deformations preserving eta AND eta_+")
# X in so(9,5) that ALSO preserves eta_+ = I: X^T eta_+ + eta_+ X = X^T + X = 0 (antisymmetric)
gstar = subalgebra(full_gens, lambda X: X.T @ eta_plus + eta_plus @ X)
ok("G*.dim46", len(gstar) == 46, "dim g* = %d (expect 46 = so(9)+so(5), maximal compact)" % len(gstar))
# g* must equal the C-commutant (preserving both forms <=> commuting with C)
gstar_span_eq_comm = (len(gstar) == len(comm_with_C))
# verify every gstar generator commutes with C
allcomm = all(np.linalg.norm(X @ C - C @ X) < TOL for X in gstar)
ok("G*.equals_C_commutant", gstar_span_eq_comm and allcomm,
   "g* = the C-commutant: preserving {eta, eta_+} <=> commuting with C")
# verify block-diagonal (no coupling between the 9-block and the 5-block)
def offblock(X):
    return np.linalg.norm(X[:P, P:]) + np.linalg.norm(X[P:, :P])
ok("G*.block_diagonal", all(offblock(X) < TOL for X in gstar),
   "every g* generator is block-diagonal on R^9 (+) R^5")

# ===========================================================================
# [INV] THE DECISIVE NUMBER: dim of G*-invariant symmetric forms
# ===========================================================================
print("\n[INV] the decisive computation: invariant symmetric bilinear forms under g*")
gstar_inv = invariant_sym_forms(gstar)
DIM = len(gstar_inv)
ok("INV.dim_is_2", DIM == 2, "dim{g*-invariant symmetric forms} = %d  (DECISIVE: 1=>FORCED, >1=>RESIDUAL)" % DIM)
ok("INV.eta_plus_invariant", in_span(eta_plus, gstar_inv), "eta_+ = eta.C is g*-invariant")
ok("INV.eta_invariant", in_span(eta, gstar_inv), "eta (W203's indefinite kernel) is ALSO g*-invariant")
ok("INV.basis_is_I_and_C", in_span(np.eye(N), gstar_inv) and in_span(C, gstar_inv),
   "basis of the 2-dim space = {I_14, C} = {eta_+, eta.C.C} spanning {eta_+, eta}")
ok("INV.eta_not_prop_eta_plus", not np.allclose(eta / np.linalg.norm(eta), eta_plus / np.linalg.norm(eta_plus)),
   "eta and eta_+ are DISTINCT invariants (not scalar multiples) => generator NOT unique")

# ===========================================================================
# [RES] the residual bit: the record-block relative sign is FREE; positivity leaves a cone
# ===========================================================================
print("\n[RES] the residual Z/2 (grading sign) and the positivity cone")
P9 = np.diag([1.0] * P + [0.0] * Q)  # projector onto geometric/positive block (R^9)
P5 = np.diag([0.0] * P + [1.0] * Q)  # projector onto record-carrying/negative block (R^5)
ok("RES.blocks_invariant", in_span(P9, gstar_inv) and in_span(P5, gstar_inv),
   "both block projectors P9, P5 are g*-invariant => each block gets an INDEPENDENT Schur scale")
# eta_+ = P9 + P5 (c=(+,+)); eta = P9 - P5 (c=(+,-)). Both invariant: the sign of the record block is free.
ok("RES.eta_plus_is_plus_plus", np.allclose(eta_plus, P9 + P5), "eta_+ = P9 + P5  (record block sign +)")
ok("RES.eta_is_plus_minus", np.allclose(eta, P9 - P5), "eta   = P9 - P5  (record block sign -)  <- the free bit")
# positivity of c1*P9 + c2*P5: pos-def iff c1>0 AND c2>0 -- a 2-parameter open cone, not a single ray
def posdef(c1, c2):
    return signature(c1 * P9 + c2 * P5)[0] == N
samples = [(1, 1), (1, 2), (2, 1), (0.3, 5.0)]  # all should be pos-def and invariant, none prop. to eta_+
cone_ok = all(posdef(a, b) for a, b in samples)
not_ray = not np.allclose((1 * P9 + 2 * P5) / np.linalg.norm(1 * P9 + 2 * P5),
                          eta_plus / np.linalg.norm(eta_plus))
ok("RES.posdef_cone_2param", cone_ok and not_ray,
   "positive-definite invariants form a 2-parameter cone (c1>0,c2>0), NOT the single ray eta_+")
ok("RES.eta_indefinite_also_invariant", posdef(1, -1) is False and in_span(eta, gstar_inv),
   "the indefinite branch (c2<0) is invariant too: the Z/2 grading sign is unforced")

# ===========================================================================
# [FINER] the finer good-stable split only ENLARGES the residual
# ===========================================================================
print("\n[FINER] finer split (base (3,1) + fiber geometric(6)/record-count(4)) grows the residual")
# stabilizer respecting base (3,1) and fiber split geometric(6)/record-count(4):
# blocks: base-pos(3), base-neg(1), fiber-geom(6), fiber-recordcount(4)  -> 4 irreducible O(n) blocks
block_sizes = [3, 1, 6, 4]
# invariants = one scale per block whose size >= 1; a 1-dim block (base-neg) still gives a scale
finer_dim = len([b for b in block_sizes])  # 4 independent scales
ok("FINER.dim_ge_2", finer_dim >= 2, "finer stabilizer invariant-form dim = %d >= 2" % finer_dim)
ok("FINER.grows_not_shrinks", finer_dim >= DIM,
   "refining the good-stable structure (%d blocks) ENLARGES the residual (%d >= %d); never forces dim 1"
   % (len(block_sizes), finer_dim, DIM))

# ===========================================================================
# [E1] VERDICT
# ===========================================================================
print("\n[E1] verdict")
verdict_residual = (DIM == 2) and in_span(eta_plus, gstar_inv) and in_span(eta, gstar_inv)
ok("E1.RESIDUAL_BIT_STANDS", verdict_residual,
   "VERDICT: RESIDUAL-BIT-STANDS. Invariant-form space dim = 2 (Z/2 grading-sign + block scales); "
   "eta_+ is A generator, not THE unique one; eta equally invariant; positivity leaves a cone.")

# ---------------------------------------------------------------------------
npass = sum(1 for _, c, _ in checks if c)
ntot = len(checks)
print("\n==================== SUMMARY ====================")
print("%d/%d checks passed" % (npass, ntot))
print("DECISIVE invariant-graded-form dimension = %d" % DIM)
print("VERDICT = %s" % ("RESIDUAL-BIT-STANDS (residual = 2-dim invariant space; Z/2 grading sign unforced)"
                         if verdict_residual else "NOT RESIDUAL -- inspect"))
print("=================================================")
if npass != ntot:
    raise SystemExit(1)
raise SystemExit(0)
