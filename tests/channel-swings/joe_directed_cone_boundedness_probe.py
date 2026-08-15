#!/usr/bin/env python3
r"""Joe-directed channel, gate MC-1: does the CONE of Lorentzian metrics bound
the potential that SRC-3 found unbounded below?

TARGET CLAIM UNDER TEST (stated so the verdict is claim-indexed):

    "SRC-3's cause (2) -- the (6,4) signature of the internal DeWitt metric on
     the fibre of Y14 = Met(X4) -- is an ARTIFACT of linearising a CONE as a
     vector space.  The fibre of Met(X4) is not Sym^2(T*X); it is the open cone
     C of signature-(3,1) forms, a curved homogeneous space GL(4,R)/O(3,1) with
     a boundary at det g -> 0.  If SRC-3's runaway directions leave C, they are
     not physical field directions and the unboundedness evaporates."

The premise of that claim is TRUE and already banked in this repository
(explorations/canon-met-x4-contractibility-type-defect-2026-08-09.md, finding
D8: the Lorentzian metrics are NOT a convex cone; the fibre is GL(4,R)/O(3,1)
with homotopy type RP^3 x R^+).  This probe tests whether the true premise
reaches the conclusion.  It does not.

Four independent exact routes, each of which alone refutes the target claim:

  R1  EQUIVARIANCE / CONSTANT SIGNATURE.  GL(4,R) acts transitively on C
      (Sylvester) and the trace-reversed Frobenius metric is exactly invariant
      under that action.  So its signature is (6,4) at EVERY point of the cone.
      There is no basepoint at which the offending negative block is absent.
      Curvature of C cannot help: signature is a pointwise algebraic invariant
      and it never changes.

  R2  THE NEGATIVE DIRECTION IS THE CONE'S OWN DILATION.  The unique negative
      direction created by trace reversal is h = g, the Euler/dilation
      generator.  A cone is BY DEFINITION invariant under positive dilation.
      So the DeWitt-negative direction is the one direction the cone structure
      itself guarantees can never exit.  Cone geometry does not merely fail to
      bound the runaway; it certifies that the runaway is unobstructed.

  R3  COMPLETE RAYS.  For h = a*g0 + sum_i b_i E_{i3} spanning the whole
      4-dimensional DeWitt-negative subspace at g0, the ray g0 + t h stays in C
      for every t >= 0 IF AND ONLY IF a >= 0.  That is a closed half-space of
      the negative subspace consisting of complete rays running to infinity
      inside C.  Answer (a), not (b).  And the complementary half (a < 0) exits
      toward the VERTEX (det -> 0, the metric shrinking), where the field norm
      is BOUNDED -- so it was never a runaway direction to begin with.

  R4  TYPE AUDIT.  SRC-3's runaway parameter t multiplies v in T*_p Y14 (x) ad
      -- the CONNECTION fibre over a FIXED point p of Y14.  It does not move p.
      The cone is the space p lives in; t never travels in it.  And along the
      one cone motion that IS complete (dilation g -> lambda g), SRC-3's Q and
      K rescale by the SAME positive factor lambda^-2, so the sign of K is
      invariant along the entire dilation ray.

WHAT IS STANDARD OR ALREADY BANKED, AND IS THEREFORE NOT CLAIMED HERE.

  * The indefiniteness of the DeWitt supermetric, its one-parameter family, the
    critical parameter lambda_c = 1/n, and the conformal-factor problem of
    Euclidean quantum gravity: STANDARD LITERATURE.  DeWitt, Phys. Rev. 160
    (1967) 1113; Gibbons-Hawking-Perry, Nucl. Phys. B138 (1978) 141; Giulini
    on the geometry of superspace.
  * (7,3) -> (6,4) under trace reversal: this repository's canon,
    canon/shiab-existence-cl95.md Step 1.  Reproduced here as a cross-check.
  * The identification of the SINGLE flipped direction as the conformal/trace
    mode, the threshold lambda > 1/4, and the negative controls at lambda = 0:
    ALREADY COMPUTED in explorations/W168-reduction-krein-signature-2026-07-14.md
    (tests/W168_reduction_krein_signature.py), with the lambda-threshold also in
    explorations/n2-end-family-2026-07-20.md.  Reproduced here as a cross-check
    on an independently written implementation; NOT claimed as new.
  * Non-convexity of the Lorentzian locus and the Met_Riem / Met_Lor type
    defect: ALREADY BANKED at hostile-review grade in
    explorations/five-lens-analytic-council-2026-08-08.md and
    explorations/canon-met-x4-contractibility-type-defect-2026-08-09.md (D8).
    This probe supplies the first machine-checked certificate of it; the FINDING
    is theirs.
  * The moduli-provenance of the four fibre negatives: already banked as Half A
    of explorations/HYPOTHESIS-moduli-negative-not-time-negative-2026-08-09.md.
  * The gauge status of the conformal mode (PHYSICAL, not gauge):
    explorations/conformal-factor-mode-gauge-status-2026-07-11.md /
    tests/W78_conformal_mode_gauge_status.py.

WHAT IS NEW HERE, and it is only this: the CONE-BOUNDEDNESS adjudication.
R1-R4 against SRC-3, the explicit exit criterion on the whole DeWitt-negative
subspace (Layer 3), the unweighted-versus-weighted arc-length fork (Layer 5),
and the Layer 6 answer to the question the prior-art sweep found had never been
posed in this repository -- whether the metric cone truncates the W213/W159
conformal runaway.

Arithmetic: sympy Rational and integer only.  No floating point is load-bearing
anywhere in this file.  Inertia is computed TWO independent exact ways
(Descartes on the Berkowitz characteristic polynomial of a real-rooted
symmetric matrix; and exact symmetric congruence reduction over Q) and the two
must agree on every matrix tested.

Tags: [E] exact result, [C] control that must have discriminating power.
"""

from __future__ import annotations

from itertools import combinations

import sympy as sp

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


N = 4  # dim X4
DIMSYM = N * (N + 1) // 2  # 10


# ---------------------------------------------------------------------------
# Layer 0: exact inertia, two independent ways.
# ---------------------------------------------------------------------------
def inertia_descartes(M: sp.Matrix) -> tuple[int, int, int]:
    """(#positive, #negative, #zero) eigenvalues of a rational symmetric M.

    All eigenvalues of a real symmetric matrix are real, and for a real-rooted
    polynomial Descartes' rule of signs is an EQUALITY, not a bound.  So sign
    changes in the coefficient sequence of charpoly(x) count positive roots
    exactly, and of charpoly(-x) count negative roots exactly.
    """
    assert M == M.T, "inertia_descartes requires a symmetric matrix"
    x = sp.Symbol("x")
    poly = sp.Poly(M.charpoly(x).as_expr(), x, domain="QQ")
    coeffs = list(poly.all_coeffs())
    assert all(c.is_Rational for c in coeffs), "charpoly left the rationals"
    n = M.rows

    def sign_changes(cs: list) -> int:
        nz = [sp.sign(c) for c in cs if c != 0]
        return sum(1 for a, b in zip(nz, nz[1:]) if a != b)

    pos = sign_changes(coeffs)
    alt = [c * (-1) ** k for k, c in enumerate(coeffs)]  # charpoly(-x) up to sign
    neg = sign_changes(alt)
    zero = n - pos - neg
    return pos, neg, zero


def inertia_congruence(M: sp.Matrix) -> tuple[int, int, int]:
    """Same inertia by exact symmetric congruence reduction over Q (Lagrange).

    Independent of the characteristic polynomial entirely.  Sylvester's law of
    inertia guarantees the answer agrees.
    """
    assert M == M.T
    A = sp.Matrix(M)
    n = A.rows
    pos = neg = zero = 0
    idx = list(range(n))
    while idx:
        piv = None
        for i in idx:
            if A[i, i] != 0:
                piv = i
                break
        if piv is None:
            # all diagonal entries zero on the active block
            off = None
            for i, j in combinations(idx, 2):
                if A[i, j] != 0:
                    off = (i, j)
                    break
            if off is None:
                zero += len(idx)
                break
            i, j = off
            # e_i -> e_i + e_j turns a hyperbolic pair into a nonzero diagonal
            for k in idx:
                A[i, k] = A[i, k] + A[j, k]
            for k in idx:
                A[k, i] = A[k, i] + A[k, j]
            continue
        d = A[piv, piv]
        if d > 0:
            pos += 1
        else:
            neg += 1
        rest = [i for i in idx if i != piv]
        for i in rest:
            f = A[i, piv] / d
            if f == 0:
                continue
            for k in idx:
                A[i, k] = A[i, k] - f * A[piv, k]
            for k in idx:
                A[k, i] = A[k, i] - f * A[k, piv]
        idx = rest
    return pos, neg, zero


def inertia(M: sp.Matrix) -> tuple[int, int, int]:
    a = inertia_descartes(M)
    b = inertia_congruence(M)
    assert a == b, f"the two exact inertia methods disagree: {a} vs {b}"
    return a


# [C] The inertia machinery must have discriminating power on known matrices.
check("[C] inertia machinery: identity_4 is (4,0,0)",
      inertia(sp.eye(4)) == (4, 0, 0))
check("[C] inertia machinery: diag(1,1,1,-1) is (3,1,0)",
      inertia(sp.diag(1, 1, 1, -1)) == (3, 1, 0))
check("[C] inertia machinery: a degenerate matrix is detected as having a zero "
      "eigenvalue", inertia(sp.diag(1, 1, 1, 0)) == (3, 0, 1))
check("[C] inertia machinery: an off-diagonal hyperbolic pair (zero diagonal) "
      "is (1,1,0)", inertia(sp.Matrix([[0, 1], [1, 0]])) == (1, 1, 0))


# ---------------------------------------------------------------------------
# Layer 1: the cone C of signature-(3,1) forms on R^4.
# ---------------------------------------------------------------------------
G0 = sp.diag(1, 1, 1, -1)  # basepoint of the cone; index 3 is the timelike one


def in_cone(g: sp.Matrix) -> bool:
    """g lies in C iff it is symmetric with inertia exactly (3,1,0)."""
    return g == g.T and inertia(g) == (3, 1, 0)


check("[E] the basepoint g0 = diag(1,1,1,-1) lies in the cone C", in_cone(G0))

# C is a CONE: closed under multiplication by any positive rational.
check("[E] C is a cone: lambda*g in C for every positive rational lambda tested",
      all(in_cone(sp.Rational(p, q) * G0)
          for p, q in [(1, 7), (1, 2), (3, 2), (5, 1), (1000, 3)]))
# [C] and the negative dilation leaves C -- so the cone test is not vacuous.
check("[C] CONTROL: -g0 is NOT in C (signature (1,3)), so in_cone can return "
      "False", not in_cone(-G0))

# C is NOT convex.  Independently banked as finding D8 in
# explorations/canon-met-x4-contractibility-type-defect-2026-08-09.md; this is
# a cross-check of that banked result, not a new claim.
GA = sp.diag(1, 1, 1, -1)
GB = sp.diag(-1, 1, 1, 1)
check("[E] cross-check of banked D8: two elements of C whose SUM is degenerate "
      "-- C is not convex",
      in_cone(GA) and in_cone(GB) and not in_cone(GA + GB)
      and (GA + GB).det() == 0)
# [C] The Riemannian cone IS convex on the same machinery -- so the
# non-convexity above is a property of Lorentzian signature, not a code bug.
check("[C] CONTROL: the RIEMANNIAN cone is convex on the same machinery "
      "(sum of two positive-definite forms is positive definite)",
      inertia(sp.diag(1, 1, 1, 1) + sp.Matrix([[2, 1, 0, 0], [1, 2, 0, 0],
                                               [0, 0, 3, 1], [0, 0, 1, 3]]))
      == (4, 0, 0))

# GL(4,R) acts transitively on C (Sylvester), constructively verified.
TRANSITIVITY_WITNESSES = []
for A in [sp.Matrix([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 3], [0, 0, 0, 1]]),
          sp.Matrix([[2, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 3]]),
          sp.Matrix([[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]]),
          sp.Matrix([[3, 0, 0, 2], [0, 2, 1, 0], [0, 1, 2, 0], [1, 0, 0, 1]])]:
    g = (A.T * G0 * A)
    TRANSITIVITY_WITNESSES.append((A, g))
check("[E] every GL(4,Q) congruence image A^T g0 A of the basepoint is again "
      "in C (the orbit stays in the cone)",
      all(A.det() != 0 and in_cone(g) for A, g in TRANSITIVITY_WITNESSES))
check("[E] the orbit points are genuinely DIFFERENT points of the cone (not "
      "the basepoint in disguise)",
      all(g != G0 for _, g in TRANSITIVITY_WITNESSES))

# dim C = dim GL(4) - dim O(3,1) = 16 - 6 = 10 = dim Sym^2.  The tangent to the
# orbit at g0 is the image of gl(4) under M -> M^T g0 + g0 M.
ORBIT_IMAGE = []
for i in range(N):
    for j in range(N):
        M = sp.zeros(N, N)
        M[i, j] = 1
        S = M.T * G0 + G0 * M
        ORBIT_IMAGE.append([S[a, b] for a in range(N) for b in range(a, N)])
ORBIT_RANK = sp.Matrix(ORBIT_IMAGE).rank()
check("[E] the GL(4) orbit through g0 is 10-dimensional: rank of "
      "M -> M^T g0 + g0 M on gl(4) equals dim Sym^2 = 10", ORBIT_RANK == DIMSYM)
check("[E] the stabiliser so(3,1) therefore has dimension 16 - 10 = 6",
      16 - ORBIT_RANK == 6)
# Openness tested directly, not inferred: a small rational perturbation in EVERY
# basis direction stays in C, while a large one in a chosen direction does not.
_PERTURB = []
for _i in range(N):
    _E = sp.zeros(N, N)
    _E[_i, _i] = 1
    _PERTURB.append(_E)
for _i in range(N):
    for _j in range(_i + 1, N):
        _E = sp.zeros(N, N)
        _E[_i, _j] = 1
        _E[_j, _i] = 1
        _PERTURB.append(_E)
SMALL_OK = all(in_cone(G0 + sp.Rational(1, 100) * e) for e in _PERTURB)
BIG_EXITS = [e for e in _PERTURB if not in_cone(G0 + sp.Integer(3) * e)]
check("[E] C is OPEN: perturbing g0 by 1/100 in every one of the 10 Sym^2 basis "
      "directions stays inside C, so the tangent space at a cone point is the "
      "FULL 10-dimensional Sym^2 -- while a size-3 perturbation does leave, so "
      "the openness test has power", SMALL_OK and len(BIG_EXITS) > 0)


# ---------------------------------------------------------------------------
# Layer 2: the DeWitt / trace-reversed Frobenius metric on the fibre.
#
#   G_lambda(h,k) = tr(g^-1 h g^-1 k) - lambda * tr_g(h) * tr_g(k)
#
# lambda = 0   : the raw Frobenius metric      (canon: signature (7,3))
# lambda = 1/2 : trace reversal                (canon: signature (6,4))
# ---------------------------------------------------------------------------
def sym_basis() -> list[sp.Matrix]:
    out = []
    for i in range(N):
        E = sp.zeros(N, N)
        E[i, i] = 1
        out.append(E)
    for i in range(N):
        for j in range(i + 1, N):
            E = sp.zeros(N, N)
            E[i, j] = 1
            E[j, i] = 1
            out.append(E)
    return out


SYM = sym_basis()
assert len(SYM) == DIMSYM
# index bookkeeping: 0..3 are E_ii; then (0,1),(0,2),(0,3),(1,2),(1,3),(2,3)
OFF_INDEX = {}
c = N
for i in range(N):
    for j in range(i + 1, N):
        OFF_INDEX[(i, j)] = c
        c += 1


def dewitt_gram(g: sp.Matrix, lam) -> sp.Matrix:
    gi = g.inv()
    G = sp.zeros(DIMSYM, DIMSYM)
    tr = [sp.trace(gi * h) for h in SYM]
    for a in range(DIMSYM):
        for b in range(a, DIMSYM):
            val = sp.expand(sp.trace(gi * SYM[a] * gi * SYM[b]) - lam * tr[a] * tr[b])
            G[a, b] = val
            G[b, a] = val
    return G


G_FROB = dewitt_gram(G0, 0)
G_TR = dewitt_gram(G0, sp.Rational(1, 2))

check("[E] canon cross-check (shiab-existence-cl95 Step 1): the raw Frobenius "
      "metric on the fibre has signature (7,3)", inertia(G_FROB) == (7, 3, 0))
check("[E] canon cross-check (shiab-existence-cl95 Step 1): TRACE REVERSAL "
      "(lambda = 1/2) shifts the fibre signature to (6,4)",
      inertia(G_TR) == (6, 4, 0))
# [C] Not any lambda does this -- the trace-reversal value is doing real work.
check("[C] CONTROL: lambda = 0 does NOT give (6,4); the (6,4) reading depends "
      "on trace reversal", inertia(G_FROB) != (6, 4, 0))
check("[C] CONTROL: lambda = 1/8 (below the critical value) still gives (7,3), "
      "so the flip is not produced by any nonzero lambda",
      inertia(dewitt_gram(G0, sp.Rational(1, 8))) == (7, 3, 0))

# The one-parameter DeWitt family and its critical parameter.  STANDARD
# (DeWitt 1967): in n dimensions the trace direction flips at lambda_c = 1/n.
LAM = sp.Symbol("lam")
TRACE_DIR_NORM = sp.expand(sp.trace(G0.inv() * G0 * G0.inv() * G0)
                           - LAM * sp.trace(G0.inv() * G0) ** 2)
LAM_CRIT = sp.solve(sp.Eq(TRACE_DIR_NORM, 0), LAM)
check("[E] W168 + standard DeWitt family, REPRODUCED (not new): G_lambda(g,g) = n - lambda n^2 "
      "= 4 - 16 lambda, vanishing exactly at lambda_c = 1/n = 1/4",
      TRACE_DIR_NORM == 4 - 16 * LAM and LAM_CRIT == [sp.Rational(1, 4)])
check("[E] W168 REPRODUCED (not new): trace reversal lambda = 1/2 lies strictly ABOVE lambda_c = 1/4, "
      "which is why it flips exactly one direction negative: (7,3) -> (6,4)",
      sp.Rational(1, 2) > sp.Rational(1, 4)
      and inertia(dewitt_gram(G0, sp.Rational(1, 2))) == (6, 4, 0)
      and inertia(dewitt_gram(G0, sp.Rational(1, 4)))[2] == 1)


# ---------------------------------------------------------------------------
# ROUTE R1: the signature is CONSTANT on the whole cone.
# ---------------------------------------------------------------------------
def sym_action(A: sp.Matrix) -> sp.Matrix:
    """10x10 matrix of the tangent action h -> A^T h A on Sym^2 in basis SYM."""
    S = sp.zeros(DIMSYM, DIMSYM)
    for b in range(DIMSYM):
        img = A.T * SYM[b] * A
        col = []
        for i in range(N):
            col.append(img[i, i])
        for i in range(N):
            for j in range(i + 1, N):
                col.append(img[i, j])
        for a in range(DIMSYM):
            S[a, b] = col[a]
    return S


EQUIVARIANT = True
NAIVE_BREAKS = False
for A, g in TRANSITIVITY_WITNESSES:
    S = sym_action(A)
    Gg = dewitt_gram(g, sp.Rational(1, 2))
    if sp.simplify(S.T * Gg * S - G_TR) != sp.zeros(DIMSYM, DIMSYM):
        EQUIVARIANT = False
    # naive comparison WITHOUT transporting the tangent vector must differ
    if sp.simplify(Gg - G_TR) != sp.zeros(DIMSYM, DIMSYM):
        NAIVE_BREAKS = True

check("[E] R1: the trace-reversed DeWitt metric is EXACTLY GL(4)-equivariant: "
      "S(A)^T G_{A^T g A} S(A) = G_g on every witness", EQUIVARIANT)
check("[C] CONTROL: forgetting to transport the tangent vector DOES break the "
      "identity (G_{A^T g A} != G_g as matrices), so R1 is not vacuous",
      NAIVE_BREAKS)

SIGS = [inertia(dewitt_gram(g, sp.Rational(1, 2)))
        for _, g in TRANSITIVITY_WITNESSES]
check("[E] R1 CONSEQUENCE: the trace-reversed DeWitt metric has signature "
      "(6,4) at EVERY tested point of the cone, not only at the basepoint",
      all(s == (6, 4, 0) for s in SIGS))
check("[E] R1 CONSEQUENCE: there is NO point of the cone at which the DeWitt "
      "metric is definite -- the negative block has exactly 4 dimensions "
      "everywhere", all(s[1] == 4 for s in SIGS))
check("[E] R1 VERDICT: 'move to a better basepoint in the cone' is unavailable. "
      "Transitivity + equivariance forbid it.",
      EQUIVARIANT and all(s == (6, 4, 0) for s in SIGS) and ORBIT_RANK == DIMSYM)


# ---------------------------------------------------------------------------
# ROUTE R2: the negative direction created by trace reversal IS the cone's own
# dilation generator (the Euler vector field h = g).
# ---------------------------------------------------------------------------
G0_VEC = sp.Matrix([G0[i, i] for i in range(N)]
                   + [G0[i, j] for i in range(N) for j in range(i + 1, N)])
NORM_DILATION = (G0_VEC.T * G_TR * G0_VEC)[0, 0]
check("[E] R2 (W168 REPRODUCED): the dilation (Euler) direction h = g0 is DeWitt-TIMELIKE: "
      "G_{1/2}(g0,g0) = -4 < 0", NORM_DILATION == -4)
check("[C] CONTROL: under the raw Frobenius metric the SAME direction is "
      "POSITIVE (+4), so the negativity is produced by trace reversal and the "
      "computation can return either sign",
      (G0_VEC.T * G_FROB * G0_VEC)[0, 0] == 4)
check("[E] R2: the dilation ray (1+t) g0 stays in C for every positive rational "
      "t tested, by the defining property of a cone",
      all(in_cone((1 + sp.Rational(p, q)) * G0)
          for p, q in [(1, 4), (1, 1), (7, 2), (100, 1), (10 ** 6, 1)]))
T = sp.Symbol("t", positive=True)
DIL_NORM = sp.simplify(
    (G0_VEC.T * dewitt_gram((1 + T) * G0, sp.Rational(1, 2)) * G0_VEC)[0, 0])
check("[E] R2: the tangent to the dilation ray stays DeWitt-NEGATIVE at every "
      "point of the ray: G_{1/2}|_{(1+t)g0}(g0,g0) = -4/(1+t)^2 < 0 for all "
      "t > -1", sp.simplify(DIL_NORM - (-4 / (1 + T) ** 2)) == 0)
check("[E] R2 VERDICT: the DeWitt-negative direction is exactly the generator "
      "of the invariance that MAKES C a cone. Cone geometry certifies this "
      "runaway is unobstructed; it cannot bound it.",
      NORM_DILATION < 0 and sp.simplify(DIL_NORM - (-4 / (1 + T) ** 2)) == 0)


# ---------------------------------------------------------------------------
# ROUTE R3: the whole 4-dimensional DeWitt-negative subspace, and which of its
# rays exit the cone.
# ---------------------------------------------------------------------------
# Explicit G_TR-orthogonal split of the tangent space at g0.
NEG_BASIS = [G0,
             SYM[OFF_INDEX[(0, 3)]],
             SYM[OFF_INDEX[(1, 3)]],
             SYM[OFF_INDEX[(2, 3)]]]
# The positive block: the Euclidean-orthogonal complement of the coefficient
# vector v = (1,1,1,-1) inside the diagonal block (where G reduces to
# I - (1/2) v v^T, so v^perp is both G-orthogonal to the conformal direction
# and G-positive), plus the three purely spatial off-diagonal directions.
POS_BASIS = [SYM[0] - SYM[1],
             SYM[0] + SYM[1] - 2 * SYM[2],
             SYM[0] + SYM[1] + SYM[2] + 3 * SYM[3],
             SYM[OFF_INDEX[(0, 1)]], SYM[OFF_INDEX[(0, 2)]],
             SYM[OFF_INDEX[(1, 2)]]]


def to_vec(h: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([h[i, i] for i in range(N)]
                     + [h[i, j] for i in range(N) for j in range(i + 1, N)])


NEG_V = [to_vec(h) for h in NEG_BASIS]
POS_V = [to_vec(h) for h in POS_BASIS]
NEG_GRAM = sp.Matrix(4, 4, lambda a, b: (NEG_V[a].T * G_TR * NEG_V[b])[0, 0])
POS_GRAM = sp.Matrix(6, 6, lambda a, b: (POS_V[a].T * G_TR * POS_V[b])[0, 0])
CROSS = sp.Matrix(4, 6, lambda a, b: (NEG_V[a].T * G_TR * POS_V[b])[0, 0])

check("[E] R3: the named 4-dimensional block {g0, E_03, E_13, E_23} is "
      "NEGATIVE DEFINITE for the trace-reversed metric",
      inertia(NEG_GRAM) == (0, 4, 0))
check("[E] R3: the complementary named 6-dimensional block is POSITIVE "
      "DEFINITE", inertia(POS_GRAM) == (6, 0, 0))
check("[E] R3: the two blocks are exactly G-orthogonal, so this is the (6,4) "
      "splitting itself, named explicitly", CROSS == sp.zeros(4, 6))
# Discriminating version: swapping the conformal direction out of the negative
# block for ANY positive-block direction must destroy negative-definiteness.
SWAP_ALL_BREAK = True
for rep in POS_BASIS:
    alt = [to_vec(rep)] + NEG_V[1:]
    gram = sp.Matrix(4, 4, lambda a, b: (alt[a].T * G_TR * alt[b])[0, 0])
    if inertia(gram) == (0, 4, 0):
        SWAP_ALL_BREAK = False
check("[E] R3: the four DeWitt-negative directions are exactly the CONFORMAL "
      "(dilation) direction g0 plus the three mixed space-time directions "
      "E_i3 -- substituting ANY of the six positive-block directions for the "
      "conformal one destroys negative-definiteness in all six cases",
      inertia(NEG_GRAM) == (0, 4, 0) and SWAP_ALL_BREAK)

# Sylvester-frame rationality: a rational congruence diagonalising G_TR with
# exactly 6 positive and 4 negative rational entries.  This is the exact link
# to SRC-3's eta = diag(+1^6, -1^4) internal metric.
DIAG_ENTRIES = [NEG_GRAM[a, a] for a in range(4)] + [POS_GRAM[b, b]
                                                     for b in range(6)]
check("[E] R3: an explicit RATIONAL G-orthogonal frame exists with exactly 6 "
      "positive and 4 negative diagonal entries; by Sylvester's law the real "
      "orthonormal frame is then eta = diag(+1^6, -1^4), which is precisely "
      "SRC-3's internal metric",
      NEG_GRAM.is_diagonal() and POS_GRAM.is_diagonal()
      and sum(1 for d in DIAG_ENTRIES if d > 0) == 6
      and sum(1 for d in DIAG_ENTRIES if d < 0) == 4)

# The exact cone-exit criterion on the whole negative subspace.
a_s, b0, b1, b2, t_s = sp.symbols("a b0 b1 b2 t", real=True)
H_GEN = (a_s * G0
         + b0 * SYM[OFF_INDEX[(0, 3)]]
         + b1 * SYM[OFF_INDEX[(1, 3)]]
         + b2 * SYM[OFF_INDEX[(2, 3)]])
RAY = G0 + t_s * H_GEN
DET_RAY = sp.factor(sp.expand(RAY.det()))
U = 1 + t_s * a_s
DET_TARGET = sp.factor(-U ** 2 * (U ** 2 + t_s ** 2 * (b0 ** 2 + b1 ** 2 + b2 ** 2)))
check("[E] R3: exact determinant along a general ray in the DeWitt-negative "
      "subspace: det(g0 + t h) = -(1+ta)^2 [ (1+ta)^2 + t^2 (b0^2+b1^2+b2^2) ]",
      sp.simplify(DET_RAY - DET_TARGET) == 0)
check("[E] R3: therefore the ray leaves the cone EXACTLY where 1 + t a = 0, "
      "i.e. never for a >= 0 and t >= 0, and at the single finite parameter "
      "t = 1/|a| when a < 0",
      sp.simplify(sp.solve(sp.Eq(U, 0), t_s)[0] + 1 / a_s) == 0)

# Verified on explicit rational instances rather than only symbolically.
COMPLETE_OK = True
for (aa, bb0, bb1, bb2) in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0),
                            (0, 0, 0, 1), (1, 1, 1, 1), (3, -2, 5, 0),
                            (0, 2, -3, 7), (sp.Rational(1, 5), 4, 0, -1)]:
    h = (aa * G0 + bb0 * SYM[OFF_INDEX[(0, 3)]] + bb1 * SYM[OFF_INDEX[(1, 3)]]
         + bb2 * SYM[OFF_INDEX[(2, 3)]])
    hv = to_vec(h)
    if (hv.T * G_TR * hv)[0, 0] >= 0:
        COMPLETE_OK = False  # must be a genuinely DeWitt-negative direction
    for tt in [sp.Rational(1, 10), 1, 10, 10 ** 3, 10 ** 6, 10 ** 12]:
        if not in_cone(G0 + tt * h):
            COMPLETE_OK = False
check("[E] R3 MAIN RESULT: every tested DeWitt-negative direction with a >= 0 "
      "gives a ray g0 + t h that is still in the cone at t = 10^12 -- these "
      "are COMPLETE rays running to infinity INSIDE C. Answer (a), not (b).",
      COMPLETE_OK)

# [C] The cone-exit test MUST be able to fire, or R3 is vacuous.
EXIT_H = -G0
EXIT_TS = [tt for tt in [sp.Rational(1, 2), sp.Rational(9, 10), 1,
                         sp.Rational(11, 10), 2]
           if not in_cone(G0 + tt * EXIT_H)]
check("[C] CONTROL: the cone-exit test fires. h = -g0 is DeWitt-negative and "
      "the ray g0 - t g0 LEAVES C at the finite parameter t = 1",
      (to_vec(EXIT_H).T * G_TR * to_vec(EXIT_H))[0, 0] < 0
      and EXIT_TS == [1, sp.Rational(11, 10), 2])
# [C] A second, differently shaped exiting direction outside the negative block.
check("[C] CONTROL: a DeWitt-POSITIVE direction can also exit -- h = E_33 "
      "leaves C at t = 1, so exiting is not correlated with the DeWitt sign",
      (to_vec(SYM[3]).T * G_TR * to_vec(SYM[3]))[0, 0] > 0
      and not in_cone(G0 + 1 * SYM[3]) and in_cone(G0 + sp.Rational(1, 2) * SYM[3]))

# The exiting half is not a runaway: it heads to the VERTEX, at bounded norm.
EXIT_NORM_SQ = sp.expand(sum((G0 - t_s * G0)[i, j] ** 2
                             for i in range(N) for j in range(N)))
check("[E] R3: the exiting half (a < 0) runs toward the cone's VERTEX "
      "(det -> 0, the metric shrinking), where the Frobenius norm of the field "
      "is BOUNDED on the closed parameter interval -- so it was never a "
      "runaway direction. At the exit parameter t = 1 the norm is exactly 0.",
      EXIT_NORM_SQ.subs(t_s, 1) == 0 and EXIT_NORM_SQ.subs(t_s, 0) == 4)

check("[E] R3 VERDICT: the DeWitt-negative subspace contains a closed "
      "HALF-SPACE (a >= 0) of complete rays to infinity inside C, and the "
      "complementary half does not diverge at all. The cone bounds nothing.",
      COMPLETE_OK and EXIT_NORM_SQ.subs(t_s, 1) == 0)


# ---------------------------------------------------------------------------
# ROUTE R4: type audit of SRC-3's runaway, and the dilation homogeneity.
#
# SRC-3 re-derived here from scratch in exact integer arithmetic, so this probe
# does not merely cite it.
# ---------------------------------------------------------------------------
P_, Q_, NN = 6, 4, 10
ETA = sp.diag(*([1] * P_ + [-1] * Q_))
SO_BASIS, SO_KIND, SO_LABEL = [], [], []
for i in range(NN):
    for j in range(i + 1, NN):
        A = sp.zeros(NN, NN)
        A[i, j], A[j, i] = 1, -1
        SO_BASIS.append(ETA * A)
        SO_KIND.append("k" if (j < P_ or i >= P_) else "p")
        SO_LABEL.append((i, j))
check("[E] SRC-3 control re-derived: so(6,4) has 45 generators, 21 in k and 24 "
      "in p", len(SO_BASIS) == 45 and SO_KIND.count("k") == 21
      and SO_KIND.count("p") == 24)


def killing(X, Y):
    return sp.trace(X * Y)


IDX = {lab: n for n, lab in enumerate(SO_LABEL)}
XG = SO_BASIS[IDX[(0, 1)]]
YG = SO_BASIS[IDX[(1, 2)]]
BR = XG * YG - YG * XG
K_SPACELIKE = 2 * ETA[0, 0] * ETA[1, 1] * killing(BR, BR)
K_TIMELIKE = 2 * ETA[0, 0] * ETA[6, 6] * killing(BR, BR)
check("[E] SRC-3 reproduced independently: the explicit k-valued ray with both "
      "internal legs SPACELIKE gives K = -4 < 0", K_SPACELIKE == -4)
check("[E] SRC-3 reproduced independently: the SAME bracket with one internal "
      "leg TIMELIKE gives K = +4 -- the (6,4) internal metric is SRC-3's "
      "independent cause (2)", K_TIMELIKE == 4)
check("[C] CONTROL: the two SRC-3 values differ in sign, so the internal metric "
      "genuinely re-signs the quartic and cause (2) is not a restatement of "
      "cause (1)", K_SPACELIKE * K_TIMELIKE < 0)

# The type fact: SRC-3's ray is a ray in the CONNECTION fibre over a FIXED
# point of Y14.  Under the ONE cone motion that is complete -- dilation -- both
# terms of V rescale by the same POSITIVE factor, so no sign can change.
LAM_POS = sp.Symbol("mu", positive=True)
G_DIL = LAM_POS * G0
SCALE_Q = sp.simplify((G_DIL.inv()[0, 0] * G_DIL.inv()[1, 1])
                      / (G0.inv()[0, 0] * G0.inv()[1, 1]))
check("[E] R4: under the cone dilation g -> mu g (mu > 0), the two-inverse-"
      "metric contraction that builds BOTH Q and K rescales by exactly "
      "mu^-2 > 0", sp.simplify(SCALE_Q - LAM_POS ** -2) == 0)
check("[E] R4 CONSEQUENCE: V(t v; mu g) = mu^-2 V(t v; g). The sign of K -- and "
      "hence SRC-3's unboundedness -- is INVARIANT along the entire dilation "
      "ray, which is the one cone direction that provably never exits.",
      sp.simplify(SCALE_Q - LAM_POS ** -2) == 0)
check("[C] CONTROL: mu^-2 is strictly positive for every mu > 0, so this "
      "rescaling can never flip a sign -- and a NEGATIVE rescaling would have "
      "been visible to the same test",
      sp.simplify((SCALE_Q).subs(LAM_POS, 7)) > 0
      and sp.simplify((SCALE_Q).subs(LAM_POS, sp.Rational(1, 7))) > 0)

# Full GL(4) transport: K's sign is the same at every point of the cone.
SIGN_STABLE = True
for A, g in TRANSITIVITY_WITNESSES:
    Gg = dewitt_gram(g, sp.Rational(1, 2))
    inv = Gg.inv()
    # a mixed-sign pair must remain available: (6,4) at every point
    ins = inertia(Gg)
    if ins != (6, 4, 0):
        SIGN_STABLE = False
check("[E] R4: transported to every tested point of the cone, the internal "
      "metric still has 6 positive and 4 negative directions, so SRC-3's "
      "sign-flipping pair of internal legs exists at EVERY point of C",
      SIGN_STABLE)
check("[E] R4 VERDICT: SRC-3's parameter t scales the connection over a FIXED "
      "point of Y14; it never travels in the cone. And every cone motion that "
      "could be attempted leaves the sign of K unchanged.",
      SIGN_STABLE and sp.simplify(SCALE_Q - LAM_POS ** -2) == 0)


# ---------------------------------------------------------------------------
# Layer 5: the density-weight fork -- where the standard DeWitt statement and
# this repository's canon metric differ.  STANDARD result attributed, not
# claimed: DeWitt (1967) / Giulini -- with the density weight of Wheeler-DeWitt
# superspace the degenerate boundary sits at FINITE distance.
# ---------------------------------------------------------------------------
s_s = sp.Symbol("s", real=True)
w_s = sp.Symbol("w", positive=True)
# g(s) = e^{2s} g0 ; tangent 2g ; G_{1/2}(2g,2g) = -16 ; |det g| = e^{8s}
SPEED = sp.sqrt(16) * sp.exp(4 * w_s * s_s)  # sqrt(|G|) with weight |det g|^w
LEN_INWARD = sp.integrate(SPEED, (s_s, -sp.oo, 0))
LEN_UNWEIGHTED = sp.integrate(sp.Integer(4), (s_s, -sp.oo, 0))
LEN_OUTWARD_W = sp.integrate(SPEED, (s_s, 0, sp.oo))
check("[E] standard result reproduced (DeWitt 1967; Giulini): with a positive "
      "density weight |det g|^w the conformal ray reaches the degenerate "
      "boundary at FINITE DeWitt length 1/w",
      sp.simplify(LEN_INWARD - 1 / w_s) == 0)
check("[E] repo-specific consequence: canon's Y14 fibre metric is the "
      "UNWEIGHTED pointwise Frobenius metric (w = 0), for which the same "
      "boundary is at INFINITE distance -- the standard finite-distance "
      "statement does NOT transfer to canon's metric unchanged",
      LEN_UNWEIGHTED is sp.oo or LEN_UNWEIGHTED == sp.oo)
check("[E] and the OUTWARD conformal ray -- the runaway direction, det g -> "
      "infinity -- has INFINITE length for EVERY weight w > 0 as well, so no "
      "choice of density weight truncates the runaway",
      LEN_OUTWARD_W is sp.oo or LEN_OUTWARD_W == sp.oo)
check("[C] CONTROL: the two conformal directions give DIFFERENT answers "
      "(finite inward vs infinite outward), so the arc-length machinery "
      "discriminates and did not return one answer by construction",
      sp.simplify(LEN_INWARD - 1 / w_s) == 0
      and (LEN_OUTWARD_W is sp.oo or LEN_OUTWARD_W == sp.oo))


# ---------------------------------------------------------------------------
# Layer 6: cross-application to the repository's OTHER unbounded-below result.
#
# W213 / W126 / W159 found V_eff(u) = -64u^2 - 8u + 2, unbounded below, with the
# runaway carried by the scale amplitude p (4-volume N ~ e^{4p}) -- i.e. by
# EXACTLY the conformal/trace mode that W168 showed is the DeWitt-negative
# direction.  Unlike SRC-3's runaway, THAT runaway is genuinely a motion in the
# cone, so the cone question is on-type for it.  The prior-art sweep found the
# question "does p -> -infinity exit the Lorentzian cone / reach det g = 0?"
# was never posed.  It is posed and answered here.
# ---------------------------------------------------------------------------
CONF_SCALES = list(range(1, 21)) + [40, 80, 200]
CONF_OUT = all(in_cone(sp.Integer(2) ** k * G0) for k in CONF_SCALES)
CONF_IN = all(in_cone(sp.Rational(1, 2 ** k) * G0) for k in CONF_SCALES)
p_s = sp.Symbol("p", real=True)
DET_CONF = sp.simplify((sp.exp(2 * p_s) * G0).det())
check("[E] W213/W159 cross-application, outward: the conformal ray e^{2p} g0 "
      "with p -> +infinity (4-volume growing) is still in C out to a 2^200 rescaling; "
      "det = e^{8p} det g0 is never zero at finite p",
      CONF_OUT and sp.simplify(DET_CONF - (-sp.exp(8 * p_s))) == 0)
check("[E] W213/W159 cross-application, inward: the conformal ray with "
      "p -> -infinity (the metric shrinking toward the degenerate boundary) is "
      "STILL in C down to a 2^-200 rescaling. The boundary det g = 0 is reached only at "
      "p = -infinity, never at any finite parameter.", CONF_IN)
check("[E] W213/W159 ANSWER (question never previously posed in this repo): the "
      "Lorentzian metric cone does NOT truncate the conformal runaway in "
      "either direction. The only bounding mechanism on record stays the W159 "
      "DBI velocity wall, which bounds velocity and not excursion.",
      CONF_OUT and CONF_IN)
check("[C] CONTROL: the same in_cone test DOES reject a nearby non-conformal "
      "rescaling that changes the signature, so Layer 6 is not vacuous",
      not in_cone(sp.diag(2 ** 200, 2 ** 200, 2 ** 200, 2 ** 200)))


# ---------------------------------------------------------------------------
# Verdict, claim-indexed.
# ---------------------------------------------------------------------------
CONE_DOES_NOT_BOUND = (
    EQUIVARIANT
    and all(s == (6, 4, 0) for s in SIGS)
    and NORM_DILATION < 0
    and COMPLETE_OK
    and SIGN_STABLE
)
check("[E] CLAIM-INDEXED VERDICT. Target claim: \"SRC-3's cause (2) is an "
      "artifact of linearising the cone of Lorentzian metrics as a vector "
      "space.\" REFUTED, four independent exact ways (R1 constant signature; "
      "R2 the negative direction IS the cone's dilation; R3 complete rays; "
      "R4 type audit + dilation homogeneity). The cone does NOT bound the "
      "runaway; SRC-3's cause (2) STANDS.", CONE_DOES_NOT_BOUND)

passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
n_exact = sum(1 for n, _ in CHECKS if n.startswith("[E]"))
n_ctrl = sum(1 for n, _ in CHECKS if n.startswith("[C]"))
print(f"\n{passed}/{len(CHECKS)} exact checks passed "
      f"({n_exact} [E] exact results, {n_ctrl} [C] controls with power)")
print(f"fibre signature, raw Frobenius : {inertia(G_FROB)}")
print(f"fibre signature, trace-reversed: {inertia(G_TR)}")
print(f"DeWitt norm of the dilation direction G(g0,g0) = {NORM_DILATION}")
print(f"det(g0 + t h) on the negative subspace = {DET_TARGET}")
print(f"SRC-3 reproduced: K(spacelike legs) = {K_SPACELIKE}, "
      f"K(one timelike leg) = {K_TIMELIKE}")
print("VERDICT: the cone does NOT bound the runaway. SRC-3 cause (2) STANDS.")
raise SystemExit(0 if passed == len(CHECKS) else 1)
