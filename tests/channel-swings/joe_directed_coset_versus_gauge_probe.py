#!/usr/bin/env python3
"""Joe-directed coset-vs-gauge route, gate CG-1: is the 24-dimensional `p`
sector of so(6,4) a GAUGE sector or a COSET sector, and what does each reading
do to the kinetic/quartic terms?

BACKGROUND.  PV-2 established exactly that so(6,4) = k(21) (+) p(24) is the
Cartan decomposition, with the Killing form NEGATIVE on every direction of k
and POSITIVE on every direction of p.  SRC-3 then used that indefiniteness,
plus CC-1's result that the Ad(G)-invariant bilinear form space of so(6,4) is
exactly ONE-dimensional, to show the source's Mexican-hat potential is
unbounded below, and named a SECOND independent cause: the internal DeWitt
metric of signature (6,4), which SRC-3 graded "geometric, not a choice".

THE QUESTION THIS GATE DECIDES.  Both of those readings presuppose that the
relevant invariance group is the FULL non-compact G.  The source, however,
declares a REDUCTION -- UCSD 2025-04 [00:46:40]: "reduce maximal compact
subgroups along the fibers" -- after which the relevant invariance group is
K = SO(6) x SO(4).  This probe asks, exactly, what changes.

WHAT IS PRIOR ART AND IS NOT RE-CLAIMED HERE.
  * so(6,4) = k(21) (+) p(24) and the Killing signature on each summand: PV-2.
  * dim of the Ad(G)-invariant bilinear form space = 1: CC-1.
  * B_theta(X,Y) = -B(X, theta Y) is positive definite, theta-even part is the
    maximal compact, "Weinstein's punchline is the Gupta-Bleuler move":
    VG-V2 (explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md),
    computed there on so(9,5) and on a theta-stable so(6,4) SUB-BLOCK.  This
    probe runs it on the NATIVE vertical so(6,4) that PV-2/SRC-3 use, as an
    instance, not as a new result.
  * That the maximal-compact reduction is EXTERNAL rather than GU-forced:
    explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md.
    Nothing here contradicts that audit; see the artifact.

WHAT IS NEW HERE AND CARRIES THE GATE.
  (i)  the reduction supplies a K-invariant positive-definite companion on the
       INTERNAL 10 as well as on the adjoint 45, which closes SRC-3's second
       ("geometric") cause -- VG-V2 did the adjoint only;
  (ii) a THIRD runaway cause SRC-3 did not name: Killing-NULL but NON-abelian
       brackets, on which the quartic vanishes while the quadratic need not;
  (iii) SRC-3's abelian flat-direction paragraph is re-typed: abelian pairs
       give a^a = 0, hence Q = 0 as well as K = 0, so they are flat, not
       runaways;
  (iv) the structural typing: p is NOT a subalgebra, so "gauge exactly p" is
       not an available reading at all.

All arithmetic is exact integer arithmetic on integer matrices, plus exact
mod-p linear algebra used only in a two-sided sandwich (an explicit rational
lower bound together with a mod-p upper bound), never as a stand-alone answer.
The Killing form is computed as tr(XY), which is the true Killing form divided
by the fixed POSITIVE constant (N-2) = 8; only signs and vanishing are used,
so the normalisation is immaterial and is the same convention PV-2 and SRC-3
use.
"""
from __future__ import annotations

from itertools import combinations

import numpy as np

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


# ---------------------------------------------------------------------------
# Section 0 -- so(6,4), the Cartan split, and live PV-2 / SRC-3 controls.
# ---------------------------------------------------------------------------
P, Q_, N = 6, 4, 10
ETA = np.diag([1] * P + [-1] * Q_).astype(np.int64)
ETA_PLUS = np.eye(N, dtype=np.int64)          # the reduction's companion metric

BASIS: list[np.ndarray] = []
KIND: list[str] = []
LABEL: list[tuple[int, int]] = []
for i in range(N):
    for j in range(i + 1, N):
        A = np.zeros((N, N), dtype=np.int64)
        A[i, j], A[j, i] = 1, -1
        BASIS.append(ETA @ A)
        KIND.append("k" if (j < P or i >= P) else "p")
        LABEL.append((i, j))

NG = len(BASIS)
K_IDX = [a for a in range(NG) if KIND[a] == "k"]
P_IDX = [a for a in range(NG) if KIND[a] == "p"]

check("eta squares to the identity on the internal 10",
      np.array_equal(ETA @ ETA, np.eye(N, dtype=np.int64)))
check("every basis element satisfies X^T eta + eta X = 0 (so lies in so(6,4))",
      all(not (X.T @ ETA + ETA @ X).any() for X in BASIS))
check("so(6,4) has dimension 45, with |k| = 21 and |p| = 24",
      NG == 45 and len(K_IDX) == 21 and len(P_IDX) == 24)


def br(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return X @ Y - Y @ X


def kill(X: np.ndarray, Y: np.ndarray) -> int:
    """Killing form up to the fixed positive constant (N-2); PV-2/SRC-3 convention."""
    return int(np.trace(X @ Y))


def theta_form(X: np.ndarray, Y: np.ndarray) -> int:
    """B_theta(X,Y) = -B(X, theta Y) with theta(Y) = -Y^T, i.e. tr(X Y^T)."""
    return int(np.trace(X @ Y.T))


check("CONTROL (PV-2): the Killing form is NEGATIVE on every k basis direction",
      all(kill(BASIS[a], BASIS[a]) < 0 for a in K_IDX))
check("CONTROL (PV-2): the Killing form is POSITIVE on every p basis direction",
      all(kill(BASIS[a], BASIS[a]) > 0 for a in P_IDX))


def coords(W: np.ndarray) -> np.ndarray:
    """Coordinates of W in the basis.  Uses Gram(B_theta) = 2*I, checked below."""
    out = np.zeros(NG, dtype=np.int64)
    for a in range(NG):
        t = theta_form(W, BASIS[a])
        assert t % 2 == 0, "coordinate extraction must be exact"
        out[a] = t // 2
    return out


def in_span(W: np.ndarray, idx: list[int]) -> bool:
    c = coords(W)
    mask = np.ones(NG, dtype=bool)
    mask[idx] = False
    return not c[mask].any()


check("CONTROL (PV-2): k is a subalgebra -- every bracket of two k generators "
      "lies in k", all(in_span(br(BASIS[a], BASIS[b]), K_IDX)
                       for a, b in combinations(K_IDX, 2)))
check("CONTROL (PV-2): [p,p] lands back in k (symmetric-space structure)",
      all(in_span(br(BASIS[a], BASIS[b]), K_IDX)
          for a, b in combinations(P_IDX, 2)))


def quartic(X: np.ndarray, Y: np.ndarray, g_mu: int, g_nu: int, pair) -> int:
    """K(v) for the two-leg ray a_mu = X, a_nu = Y: (a^a)_{mu nu} = [X,Y]."""
    C = br(X, Y)
    return 2 * g_mu * g_nu * pair(C, C)


IDX01 = LABEL.index((0, 1))
IDX12 = LABEL.index((1, 2))
X_SRC3, Y_SRC3 = BASIS[IDX01], BASIS[IDX12]

# Metric factors are READ from the metrics, never hardcoded, so the checks
# below have a real failure path if either metric were mis-built.
G00, G11, G66 = int(ETA[0, 0]), int(ETA[1, 1]), int(ETA[6, 6])
GP00, GP11, GP66 = (int(ETA_PLUS[0, 0]), int(ETA_PLUS[1, 1]),
                    int(ETA_PLUS[6, 6]))
K_SRC3_SPACELIKE = quartic(X_SRC3, Y_SRC3, G00, G11, kill)
K_SRC3_MIXED = quartic(X_SRC3, Y_SRC3, G00, G66, kill)
check("CONTROL (SRC-3): the published k-valued ray reproduces K = -4 exactly "
      "under (Killing, eta)", K_SRC3_SPACELIKE == -4)
check("CONTROL (SRC-3): the same bracket with one timelike internal leg "
      "reproduces K = +4 exactly", K_SRC3_MIXED == 4)


# ---------------------------------------------------------------------------
# Section 1 -- the symmetric-pair certificate: is p a coset direction?
# ---------------------------------------------------------------------------
check("so(6,4) is transpose-closed: X in g implies X^T in g (the algebraic "
      "hypothesis behind the global Cartan decomposition G = K exp(p))",
      all(not (X.T.T @ ETA + ETA @ X.T).any() for X in BASIS))
check("theta(X) = -X^T maps g into g and is involutive",
      all(not ((-X.T).T @ ETA + ETA @ (-X.T)).any() for X in BASIS)
      and all(np.array_equal(-(-X.T).T, X) for X in BASIS))
check("theta is a Lie ALGEBRA AUTOMORPHISM: theta[X,Y] = [theta X, theta Y] on "
      "all 990 basis pairs",
      all(np.array_equal(-br(BASIS[a], BASIS[b]).T,
                         br(-BASIS[a].T, -BASIS[b].T))
          for a, b in combinations(range(NG), 2)))
check("k is exactly the +1 eigenspace of theta (21 antisymmetric generators)",
      all(np.array_equal(-BASIS[a].T, BASIS[a]) for a in K_IDX))
check("p is exactly the -1 eigenspace of theta (24 symmetric generators)",
      all(np.array_equal(-BASIS[a].T, -BASIS[a]) for a in P_IDX))
check("[k,p] lands in p, completing the symmetric-pair axioms",
      all(in_span(br(BASIS[a], BASIS[b]), P_IDX) for a in K_IDX for b in P_IDX))

# p is NOT a subalgebra.  Exhibit it, do not assert it.
pp_nonzero = [(a, b) for a, b in combinations(P_IDX, 2)
              if br(BASIS[a], BASIS[b]).any()]
check("there EXIST p-pairs with nonzero bracket, so [p,p] is not trivially "
      "contained in p by vacuity", len(pp_nonzero) > 0)
a0, b0 = pp_nonzero[0]
C0 = br(BASIS[a0], BASIS[b0])
check("GATE: p is NOT a subalgebra -- an explicit pair in p brackets to a "
      "NONZERO element whose p-component vanishes and whose k-component does "
      "not", C0.any() and in_span(C0, K_IDX) and not in_span(C0, P_IDX))
check("no p-pair brackets to a nonzero element of p (checked over all pairs)",
      all(not br(BASIS[a], BASIS[b]).any()
          or not in_span(br(BASIS[a], BASIS[b]), P_IDX)
          for a, b in combinations(P_IDX, 2)))

check("k and p are Killing-ORTHOGONAL (all 21 x 24 pairs), as a Cartan "
      "decomposition requires",
      all(kill(BASIS[a], BASIS[b]) == 0 for a in K_IDX for b in P_IDX))

W_NULL = BASIS[K_IDX[0]] + BASIS[P_IDX[0]]
check("Killing-NULL nonzero elements exist in so(6,4): k + p directions of "
      "equal Killing magnitude pair to exactly zero",
      W_NULL.any() and kill(W_NULL, W_NULL) == 0)
check("the same nonzero element is strictly POSITIVE under B_theta, so B_theta "
      "has no null directions where the Killing form does",
      theta_form(W_NULL, W_NULL) > 0)


# ---------------------------------------------------------------------------
# Section 2 -- the two pairings on the adjoint 45.
# ---------------------------------------------------------------------------
GRAM_THETA = np.array([[theta_form(BASIS[a], BASIS[b]) for b in range(NG)]
                       for a in range(NG)], dtype=np.int64)
GRAM_KILL = np.array([[kill(BASIS[a], BASIS[b]) for b in range(NG)]
                      for a in range(NG)], dtype=np.int64)

check("GATE: the B_theta Gram matrix on this basis is EXACTLY 2 * I_45, which "
      "certifies B_theta symmetric and POSITIVE DEFINITE (cf. VG-V2 on "
      "so(9,5))", np.array_equal(GRAM_THETA, 2 * np.eye(NG, dtype=np.int64)))
check("the Killing Gram matrix is diagonal with exactly 24 positive and 21 "
      "negative entries -- INDEFINITE",
      np.array_equal(GRAM_KILL, np.diag(np.diag(GRAM_KILL)))
      and int((np.diag(GRAM_KILL) > 0).sum()) == 24
      and int((np.diag(GRAM_KILL) < 0).sum()) == 21)
check("B_theta and the Killing form are linearly independent as bilinear forms: "
      "no scalar multiple of an indefinite form is positive definite",
      np.any(np.diag(GRAM_KILL) > 0) and np.any(np.diag(GRAM_KILL) < 0)
      and np.all(np.diag(GRAM_THETA) > 0))


def ad_matrix(Z: np.ndarray) -> np.ndarray:
    return np.array([coords(br(Z, BASIS[b])) for b in range(NG)],
                    dtype=np.int64).T


AD = [ad_matrix(Z) for Z in BASIS]


def invariance_residual(S: np.ndarray, a: int) -> np.ndarray:
    return AD[a].T @ S + S @ AD[a]


PRIME = 1000003


def rank_mod_p(M: np.ndarray) -> int:
    """Exact rank over F_PRIME.  rank_Q(M) >= rank_{F_p}(M) for integer M, so
    this gives a rigorous LOWER bound on the rational rank and, dually, an
    upper bound on the rational nullity.  Never used as a stand-alone answer:
    every use below is sandwiched against explicit rational witnesses."""
    M = np.array(M, dtype=np.int64) % PRIME
    rank, row = 0, 0
    for c in range(M.shape[1]):
        piv = None
        for r in range(row, M.shape[0]):
            if M[r, c] % PRIME:
                piv = r
                break
        if piv is None:
            continue
        M[[row, piv]] = M[[piv, row]]
        M[row] = (M[row] * pow(int(M[row, c]), PRIME - 2, PRIME)) % PRIME
        nz = np.nonzero(M[row + 1:, c])[0]
        if nz.size:
            M[row + 1 + nz] = (M[row + 1 + nz]
                               - np.outer(M[row + 1 + nz, c], M[row])) % PRIME
        rank += 1
        row += 1
    return rank


check("GATE: B_theta is Ad(K)-INVARIANT -- the residual vanishes for all 21 "
      "generators of k",
      all(not invariance_residual(GRAM_THETA, a).any() for a in K_IDX))
check("GATE (the price, and it is the AUDIT's point): B_theta is NOT "
      "Ad(G)-invariant -- an explicit generator of p gives a nonzero residual",
      any(invariance_residual(GRAM_THETA, a).any() for a in P_IDX))
check("CONTROL (CC-1): the Killing form IS Ad(G)-invariant, for all 45 "
      "generators",
      all(not invariance_residual(GRAM_KILL, a).any() for a in range(NG)))
check("CONTROL: the Killing form is a fortiori Ad(K)-invariant, so both forms "
      "live in the Ad(K)-invariant space",
      all(not invariance_residual(GRAM_KILL, a).any() for a in K_IDX))

# Four independent Ad(K)-invariant forms: so(6), su(2)_L, su(2)_R, p.
SO6 = [a for a in K_IDX if LABEL[a][1] < P]
SO4 = [a for a in K_IDX if LABEL[a][0] >= P]
check("k splits as so(6) (dim 15) + so(4) (dim 6)",
      len(SO6) == 15 and len(SO4) == 6 and len(SO6) + len(SO4) == 21)

EPS: dict[tuple[int, int], tuple[tuple[int, int], int]] = {}
for perm, sgn in (((0, 1, 2, 3), 1), ((0, 2, 1, 3), -1), ((0, 3, 1, 2), 1)):
    i, j, kk, ll = perm
    EPS[(P + i, P + j)] = ((P + kk, P + ll), sgn)
    EPS[(P + kk, P + ll)] = ((P + i, P + j), sgn)

STAR = np.zeros((NG, NG), dtype=np.int64)
for a in SO4:
    (tgt, sgn) = EPS[LABEL[a]]
    STAR[LABEL.index(tgt), a] = sgn
STAR2 = STAR @ STAR
check("the Hodge star on the so(4) block squares to the identity there, on the "
      "full 6 x 6 block and not merely on its diagonal",
      all(int(STAR2[a, b]) == (1 if a == b else 0)
          for a in SO4 for b in SO4)
      and not STAR2[np.ix_(SO4, [c for c in range(NG) if c not in SO4])].any())

PROJ_L = np.zeros((NG, NG), dtype=np.int64)
PROJ_R = np.zeros((NG, NG), dtype=np.int64)
for a in SO4:
    PROJ_L[a, a] += 1
    PROJ_R[a, a] += 1
PROJ_L = PROJ_L + STAR
PROJ_R = PROJ_R - STAR      # 2 * projectors; integer multiples are fine


def diag_proj(idx: list[int]) -> np.ndarray:
    M = np.zeros((NG, NG), dtype=np.int64)
    for a in idx:
        M[a, a] = 1
    return M


FORMS = {
    "so(6) block": diag_proj(SO6),
    "su(2)_L block": PROJ_L,
    "su(2)_R block": PROJ_R,
    "p block": diag_proj(P_IDX),
}
check("GATE: at least FOUR linearly independent Ad(K)-invariant symmetric "
      "forms exist on so(6,4), against exactly ONE Ad(G)-invariant form (CC-1)",
      all(not invariance_residual(S, a).any()
          for S in FORMS.values() for a in K_IDX)
      and rank_mod_p(np.array([S[np.triu_indices(NG)]
                               for S in FORMS.values()], dtype=np.int64)) == 4)
check("each of the four is genuinely a form on a PROPER subspace, so none is a "
      "multiple of the Killing form",
      all(int(np.count_nonzero(np.diag(S))) < NG for S in FORMS.values()))


# ---------------------------------------------------------------------------
# Section 3 -- the internal 10.  SRC-3 graded this cause "geometric, not a
# choice".  The same declared reduction supplies a K-invariant positive
# companion here too.
# ---------------------------------------------------------------------------
check("every k generator is ANTISYMMETRIC as a 10x10 matrix, hence annihilates "
      "the Euclidean companion metric",
      all(np.array_equal(BASIS[a].T, -BASIS[a]) for a in K_IDX))
check("GATE: eta_plus = I_10 is K-INVARIANT (Z^T eta_+ + eta_+ Z = 0 for all "
      "21 generators of k)",
      all(not (BASIS[a].T @ ETA_PLUS + ETA_PLUS @ BASIS[a]).any()
          for a in K_IDX))
check("GATE (the price again): eta_plus is NOT G-invariant -- an explicit "
      "generator of p gives a nonzero residual",
      any((BASIS[a].T @ ETA_PLUS + ETA_PLUS @ BASIS[a]).any() for a in P_IDX))
check("eta_plus is positive definite while eta has signature (6,4)",
      int((np.diag(ETA_PLUS) > 0).sum()) == 10
      and int((np.diag(ETA) > 0).sum()) == 6
      and int((np.diag(ETA) < 0).sum()) == 4)

def nullity_mod_p(gens: list[int]) -> int:
    """Upper bound on the rational dimension of the invariant symmetric form
    space on the internal 10, via rank_Q >= rank_{F_p}."""
    pairs = [(i, j) for i in range(N) for j in range(i, N)]
    col = {pq: c for c, pq in enumerate(pairs)}
    rows = []
    for a in gens:
        Z = BASIS[a]
        for (i, j) in pairs:
            r = np.zeros(len(pairs), dtype=np.int64)
            for m in range(N):
                r[col[(min(m, j), max(m, j))]] += int(Z[m, i])
                r[col[(min(i, m), max(i, m))]] += int(Z[m, j])
            rows.append(r)
    M = np.array(rows, dtype=np.int64)
    return M.shape[1] - rank_mod_p(M)


NUL_K = nullity_mod_p(K_IDX)
NUL_G = nullity_mod_p(list(range(NG)))
check("SANDWICH (internal 10, K-invariance): two explicit rational solutions "
      "exist (eta and eta_plus) and the mod-p nullity is 2, so the dimension "
      "is EXACTLY 2",
      NUL_K == 2
      and all(not (BASIS[a].T @ ETA + ETA @ BASIS[a]).any() for a in K_IDX)
      and all(not (BASIS[a].T @ ETA_PLUS + ETA_PLUS @ BASIS[a]).any()
              for a in K_IDX))
check("SANDWICH (internal 10, G-invariance): one explicit rational solution "
      "exists (eta) and the mod-p nullity is 1, so the dimension is EXACTLY 1 "
      "-- the reduction strictly ENLARGES the available forms, 1 -> 2",
      NUL_G == 1 and NUL_K > NUL_G)


# ---------------------------------------------------------------------------
# Section 4 -- SRC-3 re-run under the post-reduction pairing, and the limits.
# ---------------------------------------------------------------------------
K_REPAIR_SPACELIKE = quartic(X_SRC3, Y_SRC3, GP00, GP11, theta_form)
K_REPAIR_MIXED = quartic(X_SRC3, Y_SRC3, GP00, GP66, theta_form)
check("GATE: SRC-3's published negative ray is STRICTLY POSITIVE under "
      "(B_theta, eta_plus) -- the ad-side cause is removed",
      K_SRC3_SPACELIKE < 0 < K_REPAIR_SPACELIKE)
check("GATE: SRC-3's second, 'geometric' cause is removed by the SAME "
      "reduction -- under eta the timelike internal leg FLIPS the sign of the "
      "identical bracket, under eta_plus it does not, and both configurations "
      "are positive",
      K_SRC3_MIXED * K_SRC3_SPACELIKE < 0
      and K_REPAIR_MIXED > 0
      and K_REPAIR_MIXED == K_REPAIR_SPACELIKE)

sweep_theta, sweep_kill = [], []
for a in range(NG):
    for b in range(NG):
        if a == b:
            continue
        for gm, gn in ((1, 1), (1, -1)):
            sweep_kill.append(quartic(BASIS[a], BASIS[b], gm, gn, kill))
        sweep_theta.append(quartic(BASIS[a], BASIS[b], 1, 1, theta_form))
check("SWEEP: under (Killing, eta) the quartic takes BOTH signs over the basis "
      "sweep", min(sweep_kill) < 0 < max(sweep_kill))
check("GATE SWEEP: under (B_theta, eta_plus) the quartic is NEVER negative "
      "over the same sweep", min(sweep_theta) >= 0)
check("GATE SWEEP: under (B_theta, eta_plus) the quartic vanishes EXACTLY on "
      "the vanishing brackets, and on no others",
      all((quartic(BASIS[a], BASIS[b], 1, 1, theta_form) == 0)
          == (not br(BASIS[a], BASIS[b]).any())
          for a in range(NG) for b in range(NG) if a != b))

# The third cause SRC-3 did not name: Killing-NULL but NON-abelian brackets.
null_witness = None
for a in range(NG):
    for b, c in combinations(range(NG), 2):
        Y2 = BASIS[b] + BASIS[c]
        C = br(BASIS[a], Y2)
        if C.any() and kill(C, C) == 0:
            null_witness = (BASIS[a], Y2, C)
            break
    if null_witness:
        break
check("GATE (new): a NON-abelian Killing-NULL bracket exists -- an explicit "
      "ray with [X,Y] != 0 on which the Killing quartic vanishes, so SRC-3's "
      "K = 0 locus is strictly larger than its abelian pairs",
      null_witness is not None
      and null_witness[2].any()
      and kill(null_witness[2], null_witness[2]) == 0)
check("GATE (new): on that same ray B_theta gives a STRICTLY POSITIVE quartic, "
      "so the third cause is closed by the same reduction",
      null_witness is not None
      and theta_form(null_witness[2], null_witness[2]) > 0)

abelian_pairs = [(a, b) for a, b in combinations(range(NG), 2)
                 if not br(BASIS[a], BASIS[b]).any()]
check("RE-TYPING of SRC-3's flat directions: on abelian pairs the whole "
      "curvature perturbation a^a vanishes, so the QUADRATIC Q = 2<F0, a^a> "
      "vanishes together with the quartic, under ANY pairing -- these are flat "
      "directions, not runaways",
      len(abelian_pairs) > 0
      and all(not br(BASIS[a], BASIS[b]).any() for a, b in abelian_pairs))


# ---------------------------------------------------------------------------
# Section 5 -- boundedness.  The whole obstruction is Cauchy-Schwarz.
# ---------------------------------------------------------------------------
F0_A, F0_B = BASIS[IDX01], BASIS[LABEL.index((2, 3))]


def cs_ok(pair, gm: int, gn: int, F0: np.ndarray,
          X: np.ndarray, Y: np.ndarray) -> bool:
    """Cauchy-Schwarz: <F0, w>^2 <= <F0,F0><w,w> with w = [X,Y]."""
    w = br(X, Y)
    return pair(F0, w) ** 2 <= pair(F0, F0) * pair(w, w)


cs_theta = [cs_ok(theta_form, 1, 1, F0, BASIS[a], BASIS[b])
            for F0 in (F0_A, F0_B) for a in range(NG) for b in range(NG)
            if a != b]
cs_kill = [cs_ok(kill, 1, 1, F0, BASIS[a], BASIS[b])
           for F0 in (F0_A, F0_B) for a in range(NG) for b in range(NG)
           if a != b]
check("GATE: Cauchy-Schwarz HOLDS everywhere in the sweep under B_theta, which "
      "is what makes V(a) = ||a^a + F0||^2 - ||F0||^2 a completion of square "
      "bounded below by -||F0||^2", all(cs_theta))
check("GATE: Cauchy-Schwarz FAILS somewhere in the same sweep under the "
      "Killing form -- the entire SRC-3 obstruction is the absence of "
      "Cauchy-Schwarz for an INDEFINITE form", not all(cs_kill))

comp_sq_ok = True
for F0 in (F0_A, F0_B):
    for a in range(0, NG, 7):
        for b in range(1, NG, 11):
            if a == b:
                continue
            w = br(BASIS[a], BASIS[b])
            lhs = 2 * theta_form(F0, w) + theta_form(w, w)
            rhs = theta_form(w + F0, w + F0) - theta_form(F0, F0)
            if lhs != rhs or lhs < -theta_form(F0, F0):
                comp_sq_ok = False
check("GATE: the completion of square holds exactly, and no sampled "
      "configuration falls below -||F0||^2 under (B_theta, eta_plus)",
      comp_sq_ok)

runaway = any(quartic(BASIS[a], BASIS[b], gm, gn, kill) < 0
              for a in range(NG) for b in range(NG) if a != b
              for gm, gn in ((1, 1), (1, -1)))
check("CONTROL: under (Killing, eta) rays with a NEGATIVE quartic exist, so "
      "V(t v) -> -infinity there and SRC-3's conclusion stands on ITS stated "
      "condition", runaway)


passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
print(f"SRC-3 ray under (Killing, eta): spacelike {K_SRC3_SPACELIKE}, "
      f"mixed {K_SRC3_MIXED}")
print(f"same ray under (B_theta, eta_plus): spacelike {K_REPAIR_SPACELIKE}, "
      f"mixed {K_REPAIR_MIXED}")
print(f"internal-10 invariant symmetric form space: dim {NUL_G} under G, "
      f"dim {NUL_K} under K")
print(f"adjoint-45 invariant symmetric forms: 1 under G (CC-1), >= 4 under K")
print(f"quartic sweep min: Killing {min(sweep_kill)}, B_theta {min(sweep_theta)}")
raise SystemExit(0 if passed == len(CHECKS) else 1)
