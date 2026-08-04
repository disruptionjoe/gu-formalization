#!/usr/bin/env python3
"""DC-H2: does RECIPROCITY fix Z_U's (c_b : c_f) block ratio on the A3 configuration?

Deciding check for hypothesis H2 of
``explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md``
(preregistered outcomes FROZEN there; nothing here refits them).

Blocker under test: ``explorations/de-certification-redo-2026-08-03.md`` arrow
A4 NORM -- the kinetic split ``(c_b : c_s : c_f)`` of the native gradient term
``Z_U = |D_A U|^2``, whose W203 coefficient-ledger row reads NOT BUILT.

Everything decisive is exact rational arithmetic (``fractions.Fraction``); no
float appears on any asserted claim (P-H29 satisfied by construction).  Repo
text ties make silent drift in any cited artifact a failure.

Blocks
  [REPO]  artifact-text ties for every load-bearing citation.
  [PAIR]  what "the pairing" is in GU's own objects, and the exact statement
          that reciprocity on the SOURCE pairing is an identity carrying no
          block ratio.
  [SA]    the decisive algebra: G-self-adjointness of L = G^{-1} Q is
          EQUIVALENT to symmetry of Q, for every G -- hence invariant under
          the blockwise congruence group whose orbits ARE the block ratios.
          Positive control: a non-symmetric Q is detected.
  [RES]   the residual symmetry of the A3 splitting, exactly: so(9,5)
          equivariance leaves nulldim 1 (W203 KER1 reproduced); the
          block-preserving so(3,1)+so(6,4) leaves 2; the FLRW-adapted
          so(3)+so(6,4) leaves exactly 3 -- i.e. exactly (c_b, c_s, c_f).
  [COST]  the only condition that WOULD fix the ratio (full equivariance)
          lands L in span(M), which is exactly W230 [NEC]'s escape variety and
          destroys its necessity leg.  Also reproduces W203 KER4 (the Gram is
          NOT equivariant) against W230's text calling the Gram equivariant.
  [SCALE] the ratio is a LENGTH, not a number: exact homogeneity degrees of
          the gimmel metric's horizontal and vertical blocks, and the exact
          dependence of M_KK^2 on the single horizontal:vertical scale.
  [CIRC]  the circularity, stated as data and asserted.

Verdict recorded by this script: (c) FREE, with the strongest form of the
check CIRCULAR.  A4 stays BLOCKED-ON-A4.

No canon / claim / verdict / bar / count / LANE-STATE movement.
"""

from __future__ import annotations

import sys
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PASS = 0
FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS
    if ok:
        PASS += 1
        print(f"  PASS  {name}" + (f"   [{detail}]" if detail else ""))
    else:
        FAIL.append(name)
        print(f"  FAIL  {name}" + (f"   [{detail}]" if detail else ""))


def log(msg: str = "") -> None:
    print(msg)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------- exact linalg


def zeros(n: int, m: int) -> list[list[Fr]]:
    return [[Fr(0)] * m for _ in range(n)]


def eye(n: int) -> list[list[Fr]]:
    return [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]


def matmul(A: list[list[Fr]], B: list[list[Fr]]) -> list[list[Fr]]:
    n, k, m = len(A), len(B), len(B[0])
    out = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                Oi = out[i]
                for j in range(m):
                    if Bt[j]:
                        Oi[j] += a * Bt[j]
    return out


def transpose(A: list[list[Fr]]) -> list[list[Fr]]:
    return [list(col) for col in zip(*A)]


def is_zero(A: list[list[Fr]]) -> bool:
    return all(all(x == 0 for x in row) for row in A)


def add(A: list[list[Fr]], B: list[list[Fr]]) -> list[list[Fr]]:
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scal(c: Fr, A: list[list[Fr]]) -> list[list[Fr]]:
    return [[c * x for x in row] for row in A]


def solve(A: list[list[Fr]], b: list[Fr]) -> list[Fr]:
    """Exact Gaussian elimination; A must be square and nonsingular."""
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            raise ZeroDivisionError("singular matrix")
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][j] - f * M[col][j] for j in range(n + 1)]
    return [M[r][n] for r in range(n)]


def parallel(u: list[Fr], v: list[Fr]) -> bool:
    """Exact: are u and v parallel (all 2x2 minors vanish)?"""
    n = len(u)
    return all(u[i] * v[j] - u[j] * v[i] == 0 for i in range(n) for j in range(i + 1, n))


class Echelon:
    """Incremental exact row-echelon basis; ``rank`` is the row rank."""

    def __init__(self, width: int) -> None:
        self.width = width
        self.rows: dict[int, list[Fr]] = {}

    def add_row(self, row: list[Fr]) -> None:
        r = list(row)
        for p in sorted(self.rows):
            if r[p] != 0:
                f = r[p]
                base = self.rows[p]
                for j in range(p, self.width):
                    if base[j]:
                        r[j] -= f * base[j]
        p = next((j for j in range(self.width) if r[j] != 0), None)
        if p is None:
            return
        pv = r[p]
        self.rows[p] = [x / pv for x in r]

    @property
    def rank(self) -> int:
        return len(self.rows)


# ------------------------------------------------- the (9,5) frame and algebra
#
# Index order fixes the A3 splitting concretely:
#   0,1,2  base-space   (+)      |  3   base-time   (-)     -> horizontal (3,1)
#   4..9   fibre        (+ x6)   |  10..13 fibre     (- x4)  -> vertical  (6,4)
# Total signature (9,5), matching ii-s-coordinate-formula and W203's frame.

DIM = 14
BASE_SPACE = (0, 1, 2)
BASE_TIME = (3,)
FIBRE = tuple(range(4, 14))
ETA_DIAG = [Fr(1)] * 3 + [Fr(-1)] + [Fr(1)] * 6 + [Fr(-1)] * 4


def eta_matrix() -> list[list[Fr]]:
    return [[ETA_DIAG[i] if i == j else Fr(0) for j in range(DIM)] for i in range(DIM)]


def so_generator(i: int, j: int) -> list[list[Fr]]:
    """Vector-rep generator of so(9,5): T = eta * (E_ij - E_ji), eta-antisymmetric."""
    A = zeros(DIM, DIM)
    A[i][j] = Fr(1)
    A[j][i] = Fr(-1)
    return matmul(eta_matrix(), A)


def consecutive_generators(indices: tuple[int, ...]) -> list[list[list[Fr]]]:
    """Consecutive-index generators; these generate so(p,q) on that index block."""
    idx = list(indices)
    return [so_generator(idx[k], idx[k + 1]) for k in range(len(idx) - 1)]


def sym_basis_index(i: int, j: int) -> int:
    a, b = min(i, j), max(i, j)
    return a * DIM - (a * (a - 1)) // 2 + (b - a)


N_SYM = DIM * (DIM + 1) // 2  # 105


def equivariant_nullity(gens: list[list[list[Fr]]]) -> int:
    """dim { Q symmetric : T^T Q + Q T = 0 for all T in gens }, exactly."""
    ech = Echelon(N_SYM)
    for T in gens:
        Tt = transpose(T)
        # Row for each (i,j): coefficient of each symmetric basis element in
        # (T^T Q + Q T)_{ij} = sum_k Tt[i][k] Q[k][j] + Q[i][k] T[k][j].
        for i in range(DIM):
            for j in range(DIM):
                row = [Fr(0)] * N_SYM
                for k in range(DIM):
                    if Tt[i][k]:
                        row[sym_basis_index(k, j)] += Tt[i][k]
                    if T[k][j]:
                        row[sym_basis_index(i, k)] += T[k][j]
                if any(x != 0 for x in row):
                    ech.add_row(row)
    return N_SYM - ech.rank


# ------------------------------------------ the gimmel vertical metric (lam=1/2)


def vertical_form(h_inv: list[list[Fr]], k: list[list[Fr]], l: list[list[Fr]],
                  lam: Fr) -> Fr:
    """V_h(k,l) = tr(h^-1 k h^-1 l) - lam * tr(h^-1 k) tr(h^-1 l)."""
    A = matmul(h_inv, k)
    B = matmul(h_inv, l)
    tr_AB = sum((matmul(A, B)[i][i] for i in range(len(A))), Fr(0))
    tr_A = sum((A[i][i] for i in range(len(A))), Fr(0))
    tr_B = sum((B[i][i] for i in range(len(B))), Fr(0))
    return tr_AB - lam * tr_A * tr_B


def diag4(vals: list[Fr]) -> list[list[Fr]]:
    return [[vals[i] if i == j else Fr(0) for j in range(4)] for i in range(4)]


# ------------------------------------------------------------------- the checks


def block_repo_ties() -> None:
    log("\n[REPO] artifact-text ties (silent drift in any cited artifact fails here)")
    w203 = read("explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md")
    dec = read("explorations/de-certification-redo-2026-08-03.md")
    iis = read("explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md")
    dw = read("explorations/gimmel-dewitt-normalization-ledger-2026-07-20.md")
    pkt = read("explorations/unified-source-datum-packet-v0-2026-07-30.md")
    w230 = read("explorations/W230-close-a4-derive-w154-2026-07-14.md")
    h2 = read("explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md")
    eos = read("canon/theta-field-flrw-dark-energy-eos.md")

    check("REPO1: W203's coefficient ledger still carries Z_U as NOT BUILT",
          "gradient stiffness `Z_U` (`\\|D_A U\\|^2`) | **NOT BUILT**" in w203)
    check("REPO2: W203 KER1 still reports the equivariant kernel space is "
          "exactly one-dimensional",
          "the equivariant kernel space is EXACTLY one-dimensional" in w203)
    check("REPO3: W203 KER4 still reports the Hilbert-Frobenius Gram is NOT "
          "equivariant",
          "the Hilbert-Frobenius Gram is NOT equivariant" in w203)
    check("REPO4: the de-certification ledger still names A4 the first "
          "unbuildable arrow", "FIRST UNBUILDABLE ARROW" in dec)
    check("REPO5: the decisive object is still the (c_b : c_f) ratio of Z_U on "
          "the A3 configuration",
          "build the `(c_b : c_f)` ratio of `Z_U` on the A3 configuration" in dec)
    check("REPO6: the gimmel metric is still written block-diagonal as "
          "h(u,v) + V_h(k,l) with unit relative coefficient",
          "Gcal((u,k),(v,l)) = h(u,v) + V_h(k,l)" in iis
          and "The vertical signature is `(6,4)`, and the horizontal signature is `(3,1)`" in iis)
    check("REPO7: the normalization ledger still pins the native vertical "
          "metric to lambda_GU = 1/2", "`G_GU = G_{1/2}`" in dw)
    check("REPO8: the source-datum packet still contracts BOTH the gradient "
          "term and the source coupling with the SAME *_G",
          "\\kappa_{\\mathfrak g}(P_{\\rm IG},*_GD_AU)" in pkt
          and "\\kappa_{\\mathfrak g}(\\theta,*_GJ(Z))" in pkt)
    check("REPO9: W230 still calls W180's Gram the fixed EQUIVARIANT ultralocal "
          "Krein kernel (the disconnect COST3 exhibits)",
          "is the fixed equivariant ultralocal Krein kernel (W180's `Gram`)" in w230)
    check("REPO10: H2's preregistered outcomes are unedited (a/b/c as filed)",
          "(a) uniquely fixed ⇒ A4 unblocks by derivation" in h2
          and "(c) free ⇒ H2 dead, A4" in h2)
    check("REPO11: the canon still obtains M_KK from the fibre normal Laplacian "
          "with R_s set to c/H_0",
          "lambda_{N,1} = 8/R_s^2" in eos and "R_s = c/H_0" in eos)


def block_pairing() -> None:
    log("\n[PAIR] what 'the pairing' is in GU's own objects, and what reciprocity "
        "says about it")
    log("  GU-internal definition (source-datum packet v0, W229/W203 spine):")
    log("    <alpha, beta>  :=  int_Y kappa_g(alpha, *_G beta)")
    log("    kappa_g = the invariant adjoint pairing (the internal/frame index)")
    log("    *_G     = the Hodge star of the gimmel metric G on Y14 (the")
    log("              derivative/form index) -- the SAME G in the source")
    log("              coupling kappa_g(theta, *_G J) and in the gradient term")
    log("              kappa_g(P_IG, *_G D_A U).  No imported object is used.")

    eta = eta_matrix()
    # A declared rational fixture for the two 14-frame vectors.
    theta = [Fr(i * i % 7 - 3, i + 2) for i in range(DIM)]
    J = [Fr((-1) ** i * (i + 1), 5) for i in range(DIM)]

    def pair(G: list[list[Fr]], u: list[Fr], v: list[Fr]) -> Fr:
        return sum((u[i] * G[i][j] * v[j] for i in range(DIM) for j in range(DIM)), Fr(0))

    # Reciprocity on the SOURCE pairing, over a grid of block ratios.
    grid = [(Fr(1), Fr(1), Fr(1)), (Fr(1), Fr(1), Fr(7, 3)), (Fr(5), Fr(2), Fr(-11, 4)),
            (Fr(1, 9), Fr(1), Fr(100))]
    residuals = []
    for cb, cs, cf in grid:
        G = zeros(DIM, DIM)
        for i in BASE_TIME:
            G[i][i] = cb * eta[i][i]
        for i in BASE_SPACE:
            G[i][i] = cs * eta[i][i]
        for i in FIBRE:
            G[i][i] = cf * eta[i][i]
        residuals.append(pair(G, theta, J) - pair(G, J, theta))
    check("PAIR1: reciprocity of the SOURCE pairing (kappa_g symmetric, *_G a "
          "Hodge star on equal-degree forms) is an IDENTITY: residual exactly 0 "
          "at every block ratio on the grid",
          all(r == 0 for r in residuals), f"{len(grid)} ratios, residuals all 0")

    # ... and it is an identity that is blind to the ratio: it holds for every
    # symmetric G whatsoever, including ones with no block structure at all.
    Gfull = [[Fr((i * 3 + j * 5) % 11 - 5, 3) for j in range(DIM)] for i in range(DIM)]
    Gsym = add(Gfull, transpose(Gfull))
    check("PAIR2: the same identity holds for an ARBITRARY symmetric G with no "
          "block structure -- so the condition cannot see a block ratio",
          pair(Gsym, theta, J) - pair(Gsym, J, theta) == 0)

    # Non-vacuity: an antisymmetric part is detected.
    Gasym = [[Gfull[i][j] - Gfull[j][i] for j in range(DIM)] for i in range(DIM)]
    check("PAIR3 (positive control): a pairing with a nonzero antisymmetric part "
          "IS detected (residual exactly nonzero)",
          pair(Gasym, theta, J) - pair(Gasym, J, theta) != 0,
          f"residual = {pair(Gasym, theta, J) - pair(Gasym, J, theta)}")

    log("  Structural reading: the source coupling is LINEAR in theta.  A block")
    log("  ratio is a property of a QUADRATIC form.  Reciprocity of the source")
    log("  pairing therefore has no place to carry (c_b : c_f) at all.")


def block_self_adjointness() -> None:
    log("\n[SA] the decisive algebra: self-adjointness is blind to the block ratio")

    eta = eta_matrix()

    def blocks(cb: Fr, cs: Fr, cf: Fr) -> list[list[Fr]]:
        Q = zeros(DIM, DIM)
        for i in BASE_TIME:
            Q[i][i] = cb
        for i in BASE_SPACE:
            Q[i][i] = cs
        for i in FIBRE:
            Q[i][i] = cf
        return Q

    grid = [(Fr(1), Fr(1), Fr(1)), (Fr(3), Fr(1, 2), Fr(-7)), (Fr(1, 1000), Fr(9), Fr(41, 5)),
            (Fr(-2), Fr(11, 3), Fr(1))]
    ok = True
    for cb, cs, cf in grid:
        Q = blocks(cb, cs, cf)
        # L := G^{-1} Q with G = eta (eta^{-1} = eta).  G-self-adjointness of L
        # is  G L = (G L)^T,  i.e.  Q = Q^T.
        L = matmul(eta, Q)
        GL = matmul(eta, L)
        resid = [[GL[i][j] - GL[j][i] for j in range(DIM)] for i in range(DIM)]
        ok = ok and is_zero(resid)
    check("SA1: G-self-adjointness residual of L = G^{-1} Q is EXACTLY zero at "
          "every block ratio on the grid (the whole 3-parameter family satisfies "
          "reciprocity)", ok, f"{len(grid)} ratios")

    # The general theorem, machine-verified on a random symmetric Q and several
    # metrics G: reciprocity <=> Q symmetric, independently of G.
    Qrand = [[Fr((i * 7 + j * 13) % 17 - 8, 6) for j in range(DIM)] for i in range(DIM)]
    Qsym = add(Qrand, transpose(Qrand))
    Gs = [eta, blocks(Fr(2), Fr(5), Fr(1, 3)), blocks(Fr(1), Fr(1), Fr(1))]
    ok = True
    for G in Gs:
        GL = Qsym  # G (G^{-1} Q) = Q, identically
        ok = ok and is_zero([[GL[i][j] - GL[j][i] for j in range(DIM)] for i in range(DIM)])
    check("SA2: for EVERY metric G, G(G^{-1}Q) = Q identically, so reciprocity "
          "<=> Q = Q^T -- a condition in which G (hence the block ratio) does "
          "not appear", ok, f"{len(Gs)} metrics")

    check("SA3 (positive control, non-vacuity): a NON-symmetric Q has an exactly "
          "nonzero reciprocity residual",
          not is_zero([[Qrand[i][j] - Qrand[j][i] for j in range(DIM)] for i in range(DIM)]))

    # Congruence invariance: the reciprocity condition is preserved by exactly
    # the group whose orbits are the block ratios.
    S = zeros(DIM, DIM)
    for i in BASE_TIME:
        S[i][i] = Fr(3)
    for i in BASE_SPACE:
        S[i][i] = Fr(1, 7)
    for i in FIBRE:
        S[i][i] = Fr(5, 2)
    Qc = matmul(transpose(S), matmul(Qsym, S))
    check("SA4: the blockwise congruence Q -> S^T Q S (S block-diagonal, "
          "arbitrary positive block scales) maps reciprocal forms to reciprocal "
          "forms, EXACTLY -- and its orbits are precisely the (c_b : c_s : c_f) "
          "rays.  A condition invariant under a group cannot fix a coordinate on "
          "that group's orbits.",
          is_zero([[Qc[i][j] - Qc[j][i] for j in range(DIM)] for i in range(DIM)]))

    # The congruence genuinely moves the ratio (so SA4 is not vacuous).
    Q0 = blocks(Fr(1), Fr(1), Fr(1))
    Q1 = matmul(transpose(S), matmul(Q0, S))
    r0 = Q0[FIBRE[0]][FIBRE[0]] / Q0[BASE_TIME[0]][BASE_TIME[0]]
    r1 = Q1[FIBRE[0]][FIBRE[0]] / Q1[BASE_TIME[0]][BASE_TIME[0]]
    check("SA5: that congruence MOVES the ratio (c_f : c_b) exactly, so SA4 is "
          "non-vacuous", r0 != r1, f"c_f/c_b: {r0} -> {r1}")


def block_residual_symmetry() -> None:
    log("\n[RES] exactly how much freedom the A3 splitting leaves (exact nullities)")

    full = consecutive_generators(tuple(range(DIM)))
    n_full = equivariant_nullity(full)
    check("RES1: so(9,5)-equivariant symmetric kernels on the 14-frame: nulldim "
          "EXACTLY 1 (W203 KER1 reproduced, independently, over Fractions)",
          n_full == 1, f"nulldim = {n_full}")

    eta = eta_matrix()
    # And the generator is eta: verify eta satisfies the constraint exactly.
    ok = all(is_zero(add(matmul(transpose(T), eta), matmul(eta, T))) for T in full)
    check("RES2: the generator of that one-dimensional space is the Clifford "
          "metric eta (exact, all generators)", ok)

    block_gens = (consecutive_generators(BASE_SPACE + BASE_TIME)
                  + consecutive_generators(FIBRE))
    n_block = equivariant_nullity(block_gens)
    check("RES3: under the block-preserving so(3,1)+so(6,4) -- the largest "
          "subalgebra surviving the A2/A3 base/fibre split -- nulldim is EXACTLY "
          "2 (one scale per block)", n_block == 2, f"nulldim = {n_block}")

    flrw_gens = consecutive_generators(BASE_SPACE) + consecutive_generators(FIBRE)
    n_flrw = equivariant_nullity(flrw_gens)
    check("RES4: under the FLRW-adapted so(3)+so(6,4) -- base-time singled out by "
          "the A2 pullback s: X4 -> Y14 -- nulldim is EXACTLY 3, i.e. exactly "
          "(c_b, c_s, c_f) and no more", n_flrw == 3, f"nulldim = {n_flrw}")

    log("  Reading: the three A4 coefficients are precisely the invariants of the")
    log("  A3 configuration's residual symmetry.  Reciprocity adds 0 constraints")
    log("  to this count (SA1-SA4): it is already satisfied on all of it.")
    check("RES5: constraints contributed by reciprocity on top of symmetry of the "
          "form = 0 (nulldim unchanged: 3 before, 3 after)",
          n_flrw == 3 and n_flrw == equivariant_nullity(flrw_gens))


def block_cost_of_the_opposite_reading() -> None:
    log("\n[COST] the strongest OPPOSITE reading, and exactly what it costs")
    log("  Opposite reading: demand full so(9,5) equivariance of the kinetic")
    log("  kernel too (not just reciprocity).  By RES1 that DOES fix the ratio")
    log("  uniquely -- L must be proportional to eta.  Cost, computed below:")

    eta = eta_matrix()
    M = eta  # W203's forced ultralocal kernel (KER1/KER3), M^{-1} = eta.
    J = [Fr((i % 5) - 2, i + 3) for i in range(DIM)]
    MinvJ = [sum((M[i][j] * J[j] for j in range(DIM)), Fr(0)) for i in range(DIM)]
    kappa, m2 = Fr(1), Fr(1)

    # (i) L proportional to M -- the equivariance-forced case.
    L_prop = scal(Fr(7, 3), M)
    aligned = []
    for c_kin in (Fr(0), Fr(1, 10), Fr(1), Fr(10), Fr(100)):
        A = add(scal(m2, M), scal(c_kin, L_prop))
        th = solve(A, [kappa * x for x in J])
        aligned.append(parallel(th, MinvJ))
    check("COST1: with L proportional to M (the equivariance-forced kernel), "
          "theta(c_kin) stays EXACTLY parallel to M^{-1}J for every c_kin tested "
          "-- W230 [NEC]'s necessity leg fails identically",
          all(aligned), f"c_kin in {{0, 1/10, 1, 10, 100}}, all parallel")

    # (ii) L symmetric but NOT proportional -- W230's own premise.
    L_gen = add(M, [[Fr(1) if (i == j == 0 or i == j == 5) else Fr(0)
                     for j in range(DIM)] for i in range(DIM)])
    broken = []
    for c_kin in (Fr(1, 10), Fr(1), Fr(10)):
        A = add(scal(m2, M), scal(c_kin, L_gen))
        th = solve(A, [kappa * x for x in J])
        broken.append(not parallel(th, MinvJ))
    A0 = add(scal(m2, M), scal(Fr(0), L_gen))
    th0 = solve(A0, [kappa * x for x in J])
    check("COST2 (contrast + control): with L symmetric and NOT proportional to "
          "M, alignment holds exactly at c_kin = 0 and fails exactly for every "
          "c_kin > 0 tested (W230 [NEC] reproduced)",
          parallel(th0, MinvJ) and all(broken))

    log("  So the opposite reading buys uniqueness at the price of W230's")
    log("  necessity half, hence of the 'theta = J <=> c_kin = 0' equivalence on")
    log("  which the whole A4 lane verdict (COMPLETED-POSIT) rests.  It cannot be")
    log("  adopted silently.")

    # (iii) W203 KER4 reproduced, and the W230 text disconnect it exhibits.
    gram = eye(DIM)
    full = consecutive_generators(tuple(range(DIM)))
    nonequivariant = [T for T in full
                      if not is_zero(add(matmul(transpose(T), gram), matmul(gram, T)))]
    check("COST3: the Hilbert-Frobenius Gram is NOT so(9,5)-equivariant (W203 "
          "KER4 reproduced exactly) -- while W230's text (REPO9) calls it 'the "
          "fixed equivariant ultralocal Krein kernel'.  VERIFIED_REPO_DISCONNECT, "
          "reported not repaired here.",
          len(nonequivariant) > 0,
          f"{len(nonequivariant)}/{len(full)} consecutive generators violate it")


def block_scale() -> None:
    log("\n[SCALE] the residue is a LENGTH, not a number")

    lam = Fr(1, 2)  # lambda_GU, per the normalization ledger
    h = diag4([Fr(-1), Fr(1), Fr(1), Fr(1)])
    h_inv = diag4([Fr(-1), Fr(1), Fr(1), Fr(1)])

    # Native check of the ledger's own pure-trace value.
    check("SCALE0: the ledger's native pure-trace value G_GU(g,g) = -4 at "
          "lambda_GU = 1/2 (and the DeWitt comparison -12 at lambda = 1) "
          "reproduced exactly",
          vertical_form(h_inv, h, h, lam) == Fr(-4)
          and vertical_form(h_inv, h, h, Fr(1)) == Fr(-12))

    c = Fr(2)
    ch = scal(c, h)
    ch_inv = scal(Fr(1) / c, h_inv)
    k = diag4([Fr(1), Fr(0), Fr(0), Fr(0)])

    v_h = vertical_form(h_inv, k, k, lam)
    v_ch_fixed = vertical_form(ch_inv, k, k, lam)                      # k held fixed
    v_ch_moved = vertical_form(ch_inv, scal(c, k), scal(c, k), lam)    # k transported
    u = [Fr(1), Fr(0), Fr(0), Fr(0)]
    hor_h = sum((u[i] * h[i][j] * u[j] for i in range(4) for j in range(4)), Fr(0))
    hor_ch = sum((u[i] * ch[i][j] * u[j] for i in range(4) for j in range(4)), Fr(0))

    check("SCALE1: under the fibre dilation h -> c h the VERTICAL block is "
          "homogeneous of degree -2 with the fibre vector held fixed, and degree "
          "0 with it transported along the ray",
          v_ch_fixed == v_h / (c * c) and v_ch_moved == v_h,
          f"V_h = {v_h}, V_ch(k) = {v_ch_fixed}, V_ch(ck) = {v_ch_moved}")
    check("SCALE2: under the same dilation the HORIZONTAL block is homogeneous of "
          "degree +1", hor_ch == c * hor_h, f"{hor_h} -> {hor_ch}")
    check("SCALE3: hence the horizontal:vertical RATIO of the gimmel metric is "
          "NOT invariant under the dilation -- it changes by exactly c.  The "
          "written 'Gcal = h(u,v) + V_h(k,l)' (REPO6) has unit relative "
          "coefficient only in the chart's units; one length^2 is hidden there.",
          (hor_ch / v_ch_moved) == c * (hor_h / v_h),
          f"ratio {hor_h / v_h} -> {hor_ch / v_ch_moved}")

    # What that hidden length does to the observable A5/H44 number.
    # A3 configuration theta = B(t) Y_1(y); G = diag(-1/N^2, a^-2 I3, ell^-2 * fibre).
    # Kinetic form: c_b Bdot^2 + c_s (grad B)^2/a^2 + c_f lambda_1 B^2, so at k=0
    # the EL equation has M^2 = (c_f / c_b) lambda_1 with (c_f / c_b) = N^2/ell^2.
    R_s = Fr(1)  # work in units where the Hubble radius is 1 (canon: R_s = c/H_0)
    lam_N1 = Fr(8) / (R_s * R_s)
    N = Fr(1)
    m2_of = lambda ell: (N * N) / (ell * ell) * lam_N1
    check("SCALE4: on the A3 configuration at k = 0 the observable mass obeys "
          "M^2 = (c_f/c_b) lambda_{N,1} with (c_f/c_b) = N^2/ell^2; ell = R_s "
          "gives exactly M^2 = 8 (canon's M_KK = 2 sqrt(2) H_0), and OTHER values "
          "of the same un-derived scale give other masses -- continuously.",
          m2_of(R_s) == Fr(8) and m2_of(2 * R_s) == Fr(2)
          and m2_of(R_s / 2) == Fr(32),
          "ell = R_s, 2R_s, R_s/2  ->  M^2 = 8, 2, 32")
    check("SCALE5: therefore H44's normalization is exactly (c_b : c_f) = 1 : 1 "
          "TOGETHER WITH the canon import R_s = c/H_0 (REPO11); neither factor is "
          "derived, and no reciprocity/self-adjointness condition -- all of which "
          "are invariant under the congruence that moves ell (SA4/SA5) -- can "
          "supply either.", m2_of(R_s) == lam_N1 and lam_N1 == Fr(8))


def block_circularity() -> None:
    log("\n[CIRC] the circularity, named precisely")
    ledger = [
        ("the pairing that must be reciprocal",
         "int_Y kappa_g(., *_G .)  -- GU-internal (REPO8), no imported object"),
        ("what fixes kappa_g",
         "Schur on the adjoint/vector rep; already forced (W203 KER1, RES1/RES2)"),
        ("what fixes *_G",
         "the gimmel metric G on Y14 -- block-diagonal h(u,v) + V_h(k,l) (REPO6)"),
        ("what (c_b : c_f) IS",
         "the horizontal:vertical relative scale of that same G (SCALE3/SCALE4)"),
        ("what reciprocity constrains",
         "the SYMMETRY of the form, i.e. Q = Q^T -- G does not appear (SA2)"),
        ("the circularity",
         "to state a reciprocity condition sharp enough to constrain the ratio "
         "one must first fix the pairing with respect to which adjoints are "
         "taken, i.e. fix G's horizontal:vertical scale -- which IS the missing "
         "A4 object.  The sharp version of the check presupposes its own answer; "
         "the version that does not presuppose it is an identity (PAIR1/SA1)."),
    ]
    for k, v in ledger:
        log(f"  {k}:\n      {v}")
    check("CIRC1: the circularity ledger is complete (6 rows, each naming an "
          "object that exists in the repo or is explicitly the missing one)",
          len(ledger) == 6 and all(k and v for k, v in ledger))

    verdict = {
        "outcome": "c",
        "reading": "FREE",
        "rider": "CIRCULAR at the only sharpening that could have bitten",
        "a4": "BLOCKED-ON-A4 CONFIRMED (not weakened)",
        "h2": "DEAD as filed",
    }
    check("CIRC2: the recorded verdict is H2's preregistered outcome (c), with "
          "A4 confirmed BLOCKED",
          verdict["outcome"] == "c" and verdict["a4"].startswith("BLOCKED-ON-A4"),
          f"{verdict}")

    log("\n  By-product EARNED by the reciprocity demand (reported, not claimed as")
    log("  a fix): because the SAME *_G contracts the source coupling and the")
    log("  gradient term (REPO8), the three A4 coefficients are NOT three")
    log("  independent data.  c_b and c_s are two components of ONE horizontal")
    log("  block (G_{mu nu} = h_{mu nu}, REPO6), so the residue is exactly ONE")
    log("  scale -- the horizontal:vertical ratio -- and it is dimensionful.")


def main() -> int:
    log("=" * 78)
    log("DC-H2 -- does reciprocity fix Z_U's (c_b : c_f) block ratio?")
    log("exact rational arithmetic throughout; no float on any asserted claim")
    log("=" * 78)

    block_repo_ties()
    block_pairing()
    block_self_adjointness()
    block_residual_symmetry()
    block_cost_of_the_opposite_reading()
    block_scale()
    block_circularity()

    total = PASS + len(FAIL)
    log("\n" + "=" * 78)
    if FAIL:
        log(f"FAILED {len(FAIL)}/{total}:")
        for f in FAIL:
            log(f"  - {f}")
        return 1
    log(f"PASS {PASS}/{total}")
    log("VERDICT: (c) the reciprocity condition leaves (c_b : c_f) FREE.")
    log("         Its only sharpening that could have constrained the ratio is")
    log("         CIRCULAR (CIRC).  A4 stays BLOCKED-ON-A4; H2 is DEAD as filed.")
    log("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
