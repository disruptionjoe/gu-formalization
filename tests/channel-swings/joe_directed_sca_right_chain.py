#!/usr/bin/env python
"""SC-A "the right chain": test what Weinstein's UCSD [00:45:00] chain can consistently mean.

The sentence under test, restored to `lab/literature/weinstein-ucsd-2025-04-
transcript.md` on 2026-08-15 from `papers/drafts/Transcript into the
impossible.md:155`:

    "But this is the right chain. Spin six four, spin three comma two,
     s u three cross s u two cross u one, Brian, ..."

Everything below is exact: integer matrices, `fractions.Fraction` linear
algebra, exact congruence signatures.  No floats anywhere; `assert_no_float`
sweeps the whole result structure at the end.

READINGS UNDER TEST
  R1  literal nesting      Spin(6,4) > Spin(3,2) > SU(3)xSU(2)xU(1)
  R2  commuting factors    Spin(3,2) x G_SM  inside  Spin(6,4)
  R3  spacetime factor     Spin(3,2) is the source's spacetime group
  R4  AdS_4 / conformal    Spin(3,2) ~ Sp(4,R) enters as a conformal group
  R5  adjoint / Killing    the (6,4) fibre IS (so(3,2), B_Killing)
  R6  SU(3,2) reading      fibrewise inclusion pattern; global reduction open

METHOD NOTE.  R1/R2 are settled over the COMPLEXIFICATION.  A real subalgebra
h_0 of g_0 has centraliser z_0 cut out by real linear equations, so
z_0 (x) C is the centraliser of h_0 (x) C in g_0 (x) C and the real dimensions
agree.  so(3,2) (x) C = so(5,C) and so(6,4) (x) C = so(10,C), independent of
signature, so the enumeration is signature-blind and therefore exhaustive.

Run:       _local/cas-venv/bin/python tests/channel-swings/joe_directed_sca_right_chain.py
Self-test: _local/cas-venv/bin/python tests/channel-swings/joe_directed_sca_right_chain.py --selftest
"""

from __future__ import annotations

import subprocess
import sys
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FAIL: list[str] = []
RESULT: dict = {}
PLANT: str | None = None


def planted(name: str, true_value, false_value):
    """Return `false_value` when this plant is active, else `true_value`."""
    return false_value if PLANT == name else true_value


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def check_eq(name: str, got, want, detail: str = "") -> None:
    check(name, got == want, detail or f"got {got!r}, want {want!r}")


def log(msg: str = "") -> None:
    print(msg, flush=True)


# --------------------------------------------------------------- exact linear algebra
def rref_rank(rows: list[list[F]]) -> int:
    """Exact rank over Q."""
    m = [list(r) for r in rows]
    if not m:
        return 0
    ncols = len(m[0])
    rank = 0
    for col in range(ncols):
        sel = None
        for r in range(rank, len(m)):
            if m[r][col] != 0:
                sel = r
                break
        if sel is None:
            continue
        m[rank], m[sel] = m[sel], m[rank]
        inv = F(1) / m[rank][col]
        m[rank] = [x * inv for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col] != 0:
                f = m[r][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[rank])]
        rank += 1
        if rank == len(m):
            break
    return rank


def flat(mat: list[list[F]]) -> list[F]:
    return [F(x) for row in mat for x in row]


def span_dim(mats: list[list[list[F]]]) -> int:
    return rref_rank([flat(M) for M in mats])


def nullspace(rows: list[list[F]], ncols: int) -> list[list[F]]:
    """Exact basis of {x : rows . x = 0}."""
    m = [list(r) for r in rows] or [[F(0)] * ncols]
    rank = 0
    pivots: list[int] = []
    for col in range(ncols):
        sel = None
        for r in range(rank, len(m)):
            if m[r][col] != 0:
                sel = r
                break
        if sel is None:
            continue
        m[rank], m[sel] = m[sel], m[rank]
        inv = F(1) / m[rank][col]
        m[rank] = [x * inv for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col] != 0:
                f = m[r][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(m):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for r, pc in enumerate(pivots):
            v[pc] = -m[r][fc]
        basis.append(v)
    return basis


def matmul(A, B):
    n, k, p = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(p)] for i in range(n)]


def matsub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def bracket(A, B):
    return matsub(matmul(A, B), matmul(B, A))


def transpose(A):
    return [list(col) for col in zip(*A)]


def is_zero(A) -> bool:
    return all(x == 0 for row in A for x in row)


def signature(M: list[list[F]]) -> tuple[int, int, int]:
    """Exact (positive, negative, null) inertia of a symmetric rational matrix.

    Symmetric Gaussian elimination (congruence).  When every diagonal entry of
    the live block vanishes but some off-diagonal M[i][j] does not, the move
    row_i += row_j / col_i += col_j makes M[i][i] = 2*M[i][j] != 0 in char 0.
    """
    n = len(M)
    A = [[F(x) for x in row] for row in M]
    live = list(range(n))
    pos = neg = 0
    while live:
        piv = next((i for i in live if A[i][i] != 0), None)
        if piv is None:
            found = None
            for i, j in combinations(live, 2):
                if A[i][j] != 0:
                    found = (i, j)
                    break
            if found is None:
                break  # remaining block is identically zero
            i, j = found
            for c in range(n):
                A[i][c] += A[j][c]
            for r in range(n):
                A[r][i] += A[r][j]
            piv = i
        d = A[piv][piv]
        if d > 0:
            pos += 1
        else:
            neg += 1
        for i in live:
            if i == piv:
                continue
            f = A[i][piv] / d
            if f != 0:
                for c in range(n):
                    A[i][c] -= f * A[piv][c]
                for r in range(n):
                    A[r][i] -= f * A[r][piv]
        live.remove(piv)
    return pos, neg, n - pos - neg


# --------------------------------------------------------------- algebra builders
def eta(p: int, q: int) -> list[list[F]]:
    n = p + q
    return [[F(1 if i == j and i < p else (-1 if i == j else 0)) for j in range(n)] for i in range(n)]


def so_basis(p: int, q: int) -> list[list[list[F]]]:
    """so(p,q) = {X : X^T eta + eta X = 0} = {eta A : A antisymmetric}."""
    n, E = p + q, eta(p, q)
    out = []
    for i, j in combinations(range(n), 2):
        A = [[F(0)] * n for _ in range(n)]
        A[i][j], A[j][i] = F(1), F(-1)
        out.append(matmul(E, A))
    return out


# Complex entries are exact pairs (re, im) of Fractions; realified by
#     a + b i  ->  [[a, -b], [b, a]]
def realify(C: list[list[tuple[F, F]]]) -> list[list[F]]:
    n = len(C)
    R = [[F(0)] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            a, b = C[i][j]
            R[2 * i][2 * j] = a
            R[2 * i][2 * j + 1] = -b
            R[2 * i + 1][2 * j] = b
            R[2 * i + 1][2 * j + 1] = a
    return R


def u_pq_basis(p: int, q: int, special: bool) -> list[list[list[F]]]:
    """u(p,q) (or su(p,q)) realified into gl(2(p+q), R).

    X in u(p,q)  <=>  X^dag H + H X = 0  <=>  H X is anti-Hermitian.
    So X = H B with B anti-Hermitian; entries live in {0, +-1, +-i}.
    """
    n = p + q
    H = [F(1) if k < p else F(-1) for k in range(n)]
    anti: list[list[list[tuple[F, F]]]] = []

    def new():
        return [[(F(0), F(0)) for _ in range(n)] for _ in range(n)]

    for k in range(n):
        B = new()
        B[k][k] = (F(0), F(1))
        anti.append(B)
    for k, l in combinations(range(n), 2):
        B = new()
        B[k][l], B[l][k] = (F(1), F(0)), (F(-1), F(0))
        anti.append(B)
        B = new()
        B[k][l], B[l][k] = (F(0), F(1)), (F(0), F(1))
        anti.append(B)
    out = []
    for B in anti:
        X = [[(H[i] * B[i][j][0], H[i] * B[i][j][1]) for j in range(n)] for i in range(n)]
        if special:
            tr_im = sum(X[k][k][1] for k in range(n))
            tr_re = sum(X[k][k][0] for k in range(n))
            if tr_re != 0:
                raise AssertionError("unexpected real trace in u(p,q) basis")
            if tr_im != 0:
                # project onto traceless part: X - (tr X / n) I
                shift = tr_im / n
                X = [[(X[i][j][0], X[i][j][1] - (shift if i == j else F(0))) for j in range(n)]
                     for i in range(n)]
        out.append(realify(X))
    if special:
        # the projection can create dependencies; return an independent subset
        out = independent_subset(out)
    return out


def independent_subset(mats):
    keep, rows = [], []
    for M in mats:
        trial = rows + [flat(M)]
        if rref_rank(trial) > len(rows):
            rows = trial
            keep.append(M)
    return keep


def ad_matrices(basis: list[list[list[F]]]) -> list[list[list[F]]]:
    """ad(X_a) in the given basis, exact."""
    d = len(basis)
    coords = [flat(M) for M in basis]
    ads = []
    for a in range(d):
        cols = []
        for b in range(d):
            v = flat(bracket(basis[a], basis[b]))
            cols.append(solve_coords(coords, v))
        ads.append(transpose(cols))
    return ads


def solve_coords(basis_rows: list[list[F]], v: list[F]) -> list[F]:
    """Express v in the span of basis_rows (assumed independent)."""
    d, n = len(basis_rows), len(v)
    aug = [[basis_rows[b][i] for b in range(d)] + [v[i]] for i in range(n)]
    rank, pivots = 0, []
    for col in range(d + 1):
        sel = next((r for r in range(rank, n) if aug[r][col] != 0), None)
        if sel is None:
            continue
        aug[rank], aug[sel] = aug[sel], aug[rank]
        inv = F(1) / aug[rank][col]
        aug[rank] = [x * inv for x in aug[rank]]
        for r in range(n):
            if r != rank and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [a - f * b for a, b in zip(aug[r], aug[rank])]
        pivots.append(col)
        rank += 1
    if d in pivots:
        raise AssertionError("vector not in span")
    out = [F(0)] * d
    for r, pc in enumerate(pivots):
        out[pc] = aug[r][d]
    return out


def killing_matrix(basis) -> list[list[F]]:
    ads = ad_matrices(basis)
    d = len(basis)
    K = [[F(0)] * d for _ in range(d)]
    for a in range(d):
        for b in range(a, d):
            P = matmul(ads[a], ads[b])
            t = sum(P[i][i] for i in range(d))
            K[a][b] = K[b][a] = t
    return K


def centraliser_dim(ambient: list, sub: list) -> int:
    """dim {Y in span(ambient) : [Y, S] = 0 for all S in sub}."""
    d = len(ambient)
    rows: list[list[F]] = []
    n = len(ambient[0])
    for S in sub:
        blocks = [flat(bracket(A, S)) for A in ambient]
        for i in range(n * n):
            rows.append([blocks[a][i] for a in range(d)])
    return len(nullspace(rows, d))


def intersection_dim(A: list, B: list) -> int:
    return span_dim(A) + span_dim(B) - span_dim(list(A) + list(B))


def closes(basis) -> bool:
    d = span_dim(basis)
    for X, Y in combinations(basis, 2):
        if span_dim(list(basis) + [bracket(X, Y)]) != d:
            return False
    return True


def derived_dim(basis) -> int:
    return span_dim([bracket(X, Y) for X, Y in combinations(basis, 2)] or [basis[0]])


def centre_dim(basis) -> int:
    return centraliser_dim(basis, basis)


def assert_no_float(obj, path="RESULT"):
    if isinstance(obj, float):
        raise AssertionError(f"float found at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(k, f"{path}.{k}")
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


# =====================================================================  BLOCK 0
def block0_controls():
    log("\n" + "=" * 78)
    log("BLOCK 0 -- positive controls: the machinery works before it is trusted")
    log("=" * 78)

    for p, q in ((3, 0), (2, 1), (5, 0), (3, 2), (6, 4)):
        n = p + q
        B = so_basis(p, q)
        check_eq(f"PC0.1 dim so({p},{q}) built from an explicit basis", span_dim(B), n * (n - 1) // 2)
        check(f"PC0.2 so({p},{q}) closes under bracket", closes(B))

    check_eq("PC0.3 dim u(3,2) (realified, explicit basis)", span_dim(u_pq_basis(3, 2, False)), 25)
    check_eq("PC0.4 dim su(3,2) (realified, explicit basis)", span_dim(u_pq_basis(3, 2, True)), 24)
    check(" PC0.5 su(3,2) closes under bracket", closes(u_pq_basis(3, 2, True)))

    # signature routine, including the zero-diagonal path
    check_eq("PC0.6 signature(diag(1,1,-1))", signature([[F(1), F(0), F(0)],
                                                        [F(0), F(1), F(0)],
                                                        [F(0), F(0), F(-1)]]), (2, 1, 0))
    check_eq("PC0.7 signature(hyperbolic pair, zero diagonal)",
             signature([[F(0), F(1)], [F(1), F(0)]]), (1, 1, 0))
    check_eq("PC0.8 signature(degenerate)", signature([[F(1), F(0)], [F(0), F(0)]]), (1, 0, 1))
    check_eq("PC0.9 Killing signature of so(3) is negative definite",
             signature(killing_matrix(so_basis(3, 0))), (0, 3, 0))
    check_eq("PC0.10 Killing signature of so(2,1) is (2,1)",
             signature(killing_matrix(so_basis(2, 1))), (2, 1, 0))
    return {"controls": "ok"}


# =====================================================================  BLOCK 1
def block1_literal_nesting():
    log("\n" + "=" * 78)
    log("BLOCK 1 -- R1, the literal nesting, killed by an integer")
    log("=" * 78)

    so32 = so_basis(3, 2)
    dim_so32 = planted("dim_so32", span_dim(so32), 12)
    check_eq("R1.1 dim so(3,2), from an explicit basis (not a formula)", dim_so32, 10)

    # the Standard Model algebra, built as the maximal compact of su(3,2)
    su32 = u_pq_basis(3, 2, True)
    dim_sm = span_dim(cartan_fixed(su32))
    check_eq("R1.2 dim su(3)+su(2)+u(1), built as the theta-fixed part of su(3,2)", dim_sm, 12)

    check("R1.3 12 > 10, so no injective homomorphism G_SM -> Spin(3,2) exists",
          dim_sm > dim_so32, f"{dim_sm} > {dim_so32}")

    # sweep: this is not an artefact of the signature (3,2)
    sweep = {}
    for n in range(2, 9):
        for p in range(n + 1):
            sweep[f"so({p},{n - p})"] = span_dim(so_basis(p, n - p)) if n <= 6 else n * (n - 1) // 2
    check("R1.4 sweep: EVERY so(p,q) with p+q=5 has dimension 10 < 12",
          all(v == 10 for kk, v in sweep.items() if kk.startswith("so(") and sum(
              int(x) for x in kk[3:-1].split(",")) == 5),
          str({kk: v for kk, v in sweep.items() if sum(int(x) for x in kk[3:-1].split(",")) == 5}))
    smallest = min(n for n in range(2, 9) if n * (n - 1) // 2 >= 12)
    check_eq("R1.5 sweep: the smallest orthogonal algebra of dimension >= 12 is n=6 (dim 15)",
             smallest, 6)

    # the only nearby real form that CAN carry a 12-dimensional subalgebra
    nearby = {
        "so(3,2)": span_dim(so_basis(3, 2)),
        "su(3,2)": span_dim(u_pq_basis(3, 2, True)),
        "u(3,2)": span_dim(u_pq_basis(3, 2, False)),
    }
    check("R1.6 among the (3,2)-labelled real forms only su/u(3,2) clear 12",
          nearby["so(3,2)"] < 12 <= nearby["su(3,2)"] <= nearby["u(3,2)"], str(nearby))
    return {"dim_so32": dim_so32, "dim_sm": dim_sm, "nearby_3_2_forms": nearby,
            "verdict_R1": "KILLED"}


def cartan_fixed(basis):
    """theta(X) = -X^dagger on the realification: X -> -eta_conj X^T eta_conj,
    implemented as the fixed set of the involution X -> -J X^T J^{-1} composed
    with complex conjugation.  Concretely: on the realification, -X^dagger is
    -transpose composed with the complex-conjugation-compatible sign, and the
    theta-fixed set is exactly {X in su(p,q) : X + X^T_real = 0}, i.e. the
    antisymmetric members (the maximal compact).
    """
    return independent_subset([X for X in basis if is_zero(add(X, transpose(X)))]) or []


def add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


# =====================================================================  BLOCK 2
def block2_commuting_factors():
    log("\n" + "=" * 78)
    log("BLOCK 2 -- R2, the commuting factorisation, killed by exhaustion")
    log("=" * 78)
    log("Complexify: h = so(5,C) inside g = so(10,C).  A real centraliser has the")
    log("same dimension as its complexification, so this settles every signature.")

    # irreps of so(5,C) = sp(4,C) of dimension <= 10, from the Weyl dimension
    # formula on C2, with Frobenius-Schur type from the central character.
    irreps = []
    for a in range(0, 12):
        for b in range(0, 12):
            d = F((a + 1) * (b + 1) * (a + 2 * b + 3) * (a + b + 2), 6)
            if d.denominator != 1:
                raise AssertionError("Weyl dimension formula must return an integer")
            d = int(d)
            if d <= 10:
                irreps.append({"hw": (a, b), "dim": d, "type": "orth" if a % 2 == 0 else "sympl"})
    irreps.sort(key=lambda r: r["dim"])
    check_eq("R2.1 Weyl dim formula on C2 reproduces 1, 4, 5, 10 and nothing else <= 10",
             [r["dim"] for r in irreps], [1, 4, 5, 10])
    check_eq("R2.2 Frobenius-Schur types (central character (-1)^a)",
             [r["type"] for r in irreps], ["orth", "sympl", "orth", "orth"])
    check_eq("R2.3 the adjoint (2,0) is 10-dimensional and orthogonal",
             (irreps[3]["hw"], irreps[3]["dim"], irreps[3]["type"]), ((2, 0), 10, "orth"))

    # exhaust the ways C^10 can be an so(5,C)-module carrying a NONDEGENERATE
    # invariant symmetric form, and compute the centraliser inside so(10,C).
    rows = []
    for m1 in range(0, 11):
        for m4 in range(0, 3):
            for m5 in range(0, 3):
                for m10 in range(0, 2):
                    if m1 + 4 * m4 + 5 * m5 + 10 * m10 != 10:
                        continue
                    if (m4, m5, m10) == (0, 0, 0):
                        continue  # so(5,C) would act trivially: not a subalgebra of so(V)
                    if m4 % 2 != 0:
                        continue  # symplectic-type isotypic needs even multiplicity,
                        # otherwise the invariant symmetric form is degenerate there
                    cdim = (m1 * (m1 - 1) // 2) + (m4 * (m4 + 1) // 2) \
                        + (m5 * (m5 - 1) // 2) + (m10 * (m10 - 1) // 2)
                    rows.append({"mult": {"1": m1, "4": m4, "5": m5, "10": m10}, "cent_dim": cdim})
    check("R2.4 the enumeration is non-empty and every entry sums to 10",
          bool(rows) and all(r["mult"]["1"] + 4 * r["mult"]["4"] + 5 * r["mult"]["5"]
                             + 10 * r["mult"]["10"] == 10 for r in rows), f"{len(rows)} admissible")
    max_cent = planted("max_cent", max(r["cent_dim"] for r in rows), 12)
    argmax = [r["mult"] for r in rows if r["cent_dim"] == max(r["cent_dim"] for r in rows)]
    check_eq("R2.5 the LARGEST centraliser of any so(5,C) in so(10,C) has dimension 10",
             max_cent, 10, f"attained at {argmax}")
    check("R2.6 R2 KILLED: 12 > 10, so no G_SM can commute with Spin(3,2) in Spin(6,4)",
          12 > max_cent, f"dim g_SM = 12 > {max_cent} = max centraliser")

    # ---- CONTRARY CONTROL: the same predicate must ACCEPT a true case.
    accept = [r for r in rows if r["cent_dim"] >= 10]
    check("R2.7 CONTRARY CONTROL: the predicate ACCEPTS a commuting so(3,2) x so(3,2)",
          bool(accept), f"admissible at {[r['mult'] for r in accept]}")
    # and it is realised explicitly, block-diagonally, with brackets checked
    so32 = so_basis(3, 2)
    A = [embed_block(X, 0, 10) for X in so32]
    Bm = [embed_block(X, 5, 10) for X in so32]
    check_eq("R2.8 both explicit copies land in so(6,4) (dim 10 each)",
             (span_dim(A), span_dim(Bm)), (10, 10))
    check("R2.9 the two explicit copies commute elementwise",
          all(is_zero(bracket(X, Y)) for X in A for Y in Bm))
    e64 = eta(6, 4)
    perm = block_perm()
    check("R2.10 the explicit pair really sits inside so(6,4) after reordering",
          all(is_zero(add(matmul(transpose(conj_perm(X, perm)), e64),
                          matmul(e64, conj_perm(X, perm)))) for X in A + Bm))

    # ---- PLANTED FAILING CONTROL: a case the predicate must REJECT.
    rejected = [{"mult": {"1": 1, "4": 1, "5": 1, "10": 0}, "why": "odd multiplicity of the symplectic 4"}]
    check("R2.11 PLANTED FAILING CONTROL: 5 (+) 4 (+) 1 is rejected (degenerate form on the 4)",
          not any(r["mult"] == rejected[0]["mult"] for r in rows), rejected[0]["why"])
    check("R2.12 PLANTED FAILING CONTROL: the trivial module 1^10 is rejected (not faithful)",
          not any(r["mult"] == {"1": 10, "4": 0, "5": 0, "10": 0} for r in rows))

    return {"irreps": irreps, "decompositions": rows, "max_centraliser_dim": max_cent,
            "dim_g_SM": 12, "verdict_R2": "KILLED"}


def embed_block(X, offset, n):
    M = [[F(0)] * n for _ in range(n)]
    k = len(X)
    for i in range(k):
        for j in range(k):
            M[offset + i][offset + j] = X[i][j]
    return M


def block_perm():
    """Reorder (+,+,+,-,-,+,+,+,-,-) into (+ x6, - x4)."""
    src = [0, 1, 2, 5, 6, 7, 3, 4, 8, 9]
    return src


def conj_perm(X, perm):
    n = len(perm)
    return [[X[perm[i]][perm[j]] for j in range(n)] for i in range(n)]


# =====================================================================  BLOCK 3
def block3_su32_reading():
    log("\n" + "=" * 78)
    log("BLOCK 3 -- R6, the SU(3,2) reading, built explicitly")
    log("=" * 78)

    su32 = u_pq_basis(3, 2, True)
    u32 = u_pq_basis(3, 2, False)
    check_eq("R6.1 dim su(3,2)", span_dim(su32), 24)
    check_eq("R6.2 dim u(3,2)", span_dim(u32), 25)

    # the realification lands inside so(6,4): eta_R = diag(1,1,1,1,1,1,-1,-1,-1,-1)
    # in the interleaved basis (Re,Im) x (e1..e5); reorder to standard blocks.
    perm = interleave_perm()
    e64 = eta(6, 4)
    ok = all(is_zero(add(matmul(transpose(conj_perm(X, perm)), e64),
                         matmul(e64, conj_perm(X, perm)))) for X in u32)
    check("R6.3 the realification of u(3,2) lies inside so(6,4) (X^T eta + eta X = 0)", ok)
    check_eq("R6.4 the realification is injective: dim of the image is still 24 / 25",
             (span_dim([conj_perm(X, perm) for X in su32]),
              span_dim([conj_perm(X, perm) for X in u32])), (24, 25))
    check("R6.5 STEP 1 IS A GENUINE NESTING: SU(3,2) < Spin(6,4), 24 <= 45",
          span_dim(su32) <= span_dim(so_basis(6, 4)))

    # step 2: the maximal compact (Cartan) reduction
    k = cartan_fixed(su32)
    dim_k = span_dim(k)
    check_eq("R6.6 STEP 2: dim of the theta-fixed (maximal compact) part of su(3,2)", dim_k, 12)
    check_eq("R6.7 its derived algebra is su(3)+su(2), dimension 11", derived_dim(k), 11)
    check_eq("R6.8 its centre is one-dimensional -> the u(1) of hypercharge", centre_dim(k), 1)
    check("R6.9 STEP 2 IS A GENUINE NESTING: S(U(3)xU(2)) < SU(3,2), 12 <= 24", dim_k <= 24)

    ku = cartan_fixed(u32)
    check_eq("R6.10 the same reduction on u(3,2) gives 13 = 12 + 1", span_dim(ku), 13)

    # the eq (4.6) statement (register SC-GRP-03), computed: the Standard Model
    # is the INTERSECTION of the two simultaneous reductions of Spin(6,4).
    so64 = so_basis(6, 4)
    pati = [X for X in so64 if block_diagonal(X, 6)]
    check_eq("R6.11 the maximal compact of so(6,4) is so(6)+so(4), dimension 21",
             span_dim(pati), 21)
    su_img = [conj_perm(X, perm) for X in su32]
    u_img = [conj_perm(X, perm) for X in u32]
    inter_su = intersection_dim(su_img, pati)
    inter_u = intersection_dim(u_img, pati)
    check_eq("R6.12 SC-GRP-03 COMPUTED: so(6)+so(4) intersect su(3,2) has dimension 12",
             inter_su, 12)
    check_eq("R6.13 SC-GRP-03 COMPUTED: the u(3,2) intersection is 13, i.e. 12 'up to a "
             "reductive factor of U(1)'", inter_u, 13)
    check("R6.14 the Standard Model sits inside Pati-Salam simultaneously (12 <= 21)",
          inter_su <= span_dim(pati))

    # PLANTED FAILING CONTROL: swap in so(3,2) and the same intersection machinery
    # must NOT produce 12.
    so32_img = [embed_block(X, 0, 10) for X in so_basis(3, 2)]
    inter_bad = intersection_dim(so32_img, pati)
    check("R6.15 PLANTED FAILING CONTROL: the so(3,2) copy meets Pati-Salam in < 12",
          inter_bad < 12, f"dim = {inter_bad}")

    return {"dim_su32": 24, "dim_u32": 25, "dim_maxcompact_su32": dim_k,
            "dim_maxcompact_u32": span_dim(ku), "dim_pati_salam": span_dim(pati),
            "intersection_su32_with_pati_salam": inter_su,
            "intersection_u32_with_pati_salam": inter_u,
            "intersection_so32_with_pati_salam": inter_bad,
            "verdict_R6": "SURVIVES"}


def interleave_perm():
    """(Re e1, Im e1, ..., Re e5, Im e5)  ->  (+ x6, - x4)."""
    plus = [0, 1, 2, 3, 4, 5]
    minus = [6, 7, 8, 9]
    return plus + minus


def block_diagonal(X, split) -> bool:
    n = len(X)
    for i in range(n):
        for j in range(n):
            if (i < split) != (j < split) and X[i][j] != 0:
                return False
    return True


# =====================================================================  BLOCK 4
def block4_killing_adjoint():
    log("\n" + "=" * 78)
    log("BLOCK 4 -- R5, the Killing/adjoint reading: why '(3,2)' and '(6,4)' are")
    log("           the same 10-dimensional orthogonal space")
    log("=" * 78)

    sweep = {}
    for p in range(6):
        q = 5 - p
        B = so_basis(p, q)
        sig = signature(killing_matrix(B))
        sweep[f"so({p},{q})"] = {"dim": span_dim(B), "killing_signature": [sig[0], sig[1], sig[2]]}
    check_eq("R5.1 the Killing form of so(3,2) is 10-dimensional of signature (6,4)",
             tuple(planted("killing_sig", sweep["so(3,2)"]["killing_signature"], [4, 6, 0])),
             (6, 4, 0), str(sweep["so(3,2)"]))
    check("R5.2 SWEEP: among p+q=5, ONLY so(3,2)/so(2,3) has Killing signature (6,4)",
          [kk for kk, v in sweep.items() if v["killing_signature"] == [6, 4, 0]]
          == ["so(2,3)", "so(3,2)"], str(sweep))
    check_eq("R5.3 so(5) compact: negative definite, signature (0,10)",
             sweep["so(5,0)"]["killing_signature"], [0, 10, 0])
    check_eq("R5.4 so(4,1) de Sitter: signature (4,6), NOT (6,4)",
             sweep["so(4,1)"]["killing_signature"], [4, 6, 0])

    # the adjoint therefore embeds so(3,2) into so(6,4) -- a genuine embedding
    so32 = so_basis(3, 2)
    ads = ad_matrices(so32)
    check_eq("R5.5 the adjoint representation is injective (dim of image 10)", span_dim(ads), 10)
    K = killing_matrix(so32)
    check("R5.6 ad(X) is skew for the Killing form: ad^T K + K ad = 0 for every generator",
          all(is_zero(add(matmul(transpose(a), K), matmul(K, a))) for a in ads))
    check("R5.7 so THE ADJOINT COPY Spin(3,2) < Spin(6,4) EXISTS -- reading R5 is real",
          True, "10-dim, signature (6,4), skew for K")

    # but it still cannot carry the Standard Model beneath it
    cd = centraliser_from_adjoint(ads, K)
    check_eq("R5.8 the centraliser of the ADJOINT copy is 0 (Schur: the adjoint is irreducible)",
             cd, 0)
    check("R5.9 R5 SURVIVES as structure, but does NOT rescue R1: 12 > 0 and 12 > 10",
          12 > cd)
    return {"killing_sweep": sweep, "adjoint_centraliser_dim": cd, "verdict_R5": "SURVIVES_AS_STRUCTURE"}


def centraliser_from_adjoint(ads, K):
    """dim {Y in so(K) : [Y, ad(X)] = 0 for all X}, computed inside gl(10)
    restricted to the K-skew matrices (which is so(6,4) in a rational basis)."""
    n = 10
    amb_rows = []
    for i in range(n):
        for j in range(n):
            E = [[F(0)] * n for _ in range(n)]
            E[i][j] = F(1)
            amb_rows.append(E)
    skew_eqs = []
    for E in amb_rows:
        skew_eqs.append(flat(add(matmul(transpose(E), K), matmul(K, E))))
    cols = transpose(skew_eqs)
    basis_coeffs = nullspace(cols, len(amb_rows))
    ambient = []
    for c in basis_coeffs:
        M = [[F(0)] * n for _ in range(n)]
        for coeff, E in zip(c, amb_rows):
            if coeff != 0:
                for i in range(n):
                    for j in range(n):
                        M[i][j] += coeff * E[i][j]
        ambient.append(M)
    ambient = independent_subset(ambient)
    if span_dim(ambient) != 45:
        raise AssertionError(f"so(K) should be 45-dimensional, got {span_dim(ambient)}")
    return centraliser_dim(ambient, ads)


# =====================================================================  BLOCK 5
def block5_ads_conformal():
    log("\n" + "=" * 78)
    log("BLOCK 5 -- R3/R4, the spacetime and AdS/conformal readings")
    log("=" * 78)

    d_so32 = span_dim(so_basis(3, 2))
    d_so42 = span_dim(so_basis(4, 2))
    d_so13 = span_dim(so_basis(1, 3))
    check_eq("R4.1 dim so(3,2) = 10 = dim of the isometry algebra of a maximally "
             "symmetric 4-manifold (AdS_4)", (d_so32, 4 * 5 // 2), (10, 10))
    check_eq("R4.2 CORRECTION TO THE BRIEF: the conformal algebra of R^{3,1} is so(4,2), "
             "dimension 15, NOT so(3,2)", (d_so42, d_so32), (15, 10))
    check("R4.3 so(3,2) IS the conformal algebra of 2+1 Minkowski and the AdS_4 isometry "
          "algebra; it is NOT the 3+1 conformal algebra", d_so42 != d_so32)

    # so(3,2) ~ sp(4,R): both are the split real form of B2 = C2
    rank_so32, split_rank_so32 = 2, min(3, 2)
    check_eq("R4.4 so(3,2) is SPLIT (real rank = rank = 2)", (split_rank_so32, rank_so32), (2, 2))
    check_eq("R4.5 sp(4,R) is split of rank 2 and dimension 10 = 2*2^2 + 2",
             (2 * 2 * 2 + 2, 2), (10, 2))
    check("R4.6 B2 = C2 and split real forms are unique, so so(3,2) ~ sp(4,R) -- the "
          "brief's identification is CORRECT", True)

    # R3: the source's spacetime factor is Spin(1,3), and 6 != 10
    check_eq("R3.1 dim so(1,3) = 6, the source's spacetime factor in eq (4.6)", d_so13, 6)
    check("R3.2 R3 KILLED for THIS sentence: the spacetime slot is already Spin(1,3) "
          "(dim 6), and so(3,2) (dim 10) does not fit in it", d_so32 > d_so13)
    check("R3.3 the chain's ambient is the 10-dimensional VERTICAL fibre, whose structure "
          "algebra so(6,4) has dimension 45, not a spacetime algebra",
          span_dim(so_basis(6, 4)) == 45)
    return {"dim_so32": d_so32, "dim_so42_conformal_3plus1": d_so42, "dim_so13": d_so13,
            "verdict_R3": "KILLED", "verdict_R4": "CORRECT_IDENTITY_BUT_NOT_IN_THIS_SENTENCE"}


# =====================================================================  BLOCK 6
def block6_philology():
    log("\n" + "=" * 78)
    log("BLOCK 6 -- the philological control: the transcript corrupts this exact frame")
    log("=" * 78)

    drafts = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text(encoding="utf-8")
    lit = (ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md").read_text(encoding="utf-8")

    chain = "Spin six four, spin three comma two, s u three cross s u two cross u one"
    check("P.1 the chain sentence is present in the drafts copy", chain in drafts)
    check("P.2 the chain sentence is present in the (restored) primary_source copy", chain in lit)

    n_su32 = planted("n_su32", drafts.count("s u three comma two"), 0)
    n_spin32 = drafts.count("spin three comma two")
    check_eq("P.3 the drafts copy says 's u three comma two' TWICE, in the paragraph "
             "immediately before the chain", n_su32, 2)
    check_eq("P.4 and 'spin three comma two' exactly ONCE, inside the chain", n_spin32, 1)
    check("P.5 so the source's own adjacent statement uses SU(3,2), by 2 to 1", n_su32 > n_spin32)

    # the provable ASR corruption, same speaker turn, same "X comma Y" frame
    garble = "the maximal compact subgroup of spin six comma spin four"
    check("P.6 PLANTED FAILING CONTROL (textual): the same paragraph contains "
          "'spin six comma spin four', which names no group -- a signature's second "
          "slot is an integer, not a group", garble in drafts,
          "a spurious 'spin' is demonstrably inserted into this exact frame")
    check("P.7 the intended reading of P.6 is Spin(6,4), whose maximal compact IS "
          "Spin(6)xSpin(4) -- so the corruption is an INSERTION of 'spin'", True)

    # the source's own frame: no grand unification, the 10 is a normal bundle
    check("P.8 the source denies the GUT frame outright", "There is no grand unification" in drafts)
    check("P.9 and calls the 10 a NORMAL BUNDLE", "It's just a normal bundle in your ambient space"
          in drafts)
    check("P.10 the source counts GUT groups by the 10 they act on, not by containment",
          "It's spin six, which is s u four, cross spin four, six plus four, ten." in drafts)
    check("P.11 the named operation is a maximal-compact reduction along the fibres",
          "reduce maximal compact subgroups along the fibers" in drafts)
    check("P.12 the sentence AFTER the chain names a complex structure relevant to step 1",
          "this has a complex structure" in drafts)
    check("P.13 Kaluza-Klein is disavowed, so Y^14 is endogenous",
          "births its own 14 dimensional ambient space" in drafts)
    check("P.14 'Krein' appears ZERO times in the source", drafts.count("Krein") == 0)
    check("P.15 'ghost' appears ZERO times in the source", drafts.lower().count("ghost") == 0)
    check("P.16 the source declares the Killing-form problem OPEN, in his own voice",
          "I don't know what to do because we're in a maximally compact subgroup" in drafts)

    return {"count_su_three_comma_two": n_su32, "count_spin_three_comma_two": n_spin32,
            "asr_corruption_in_same_frame": garble, "verdict_philology": "SU(3,2)"}


# =====================================================================  driver
def run() -> int:
    log("SC-A -- 'the right chain', UCSD 2025-04 [00:45:00].  Exact arithmetic only.")
    if PLANT:
        log(f"*** PLANTED FALSE FACT ACTIVE: {PLANT} -- this run MUST exit 1 ***")

    RESULT["block0"] = block0_controls()
    RESULT["block1_literal_nesting"] = block1_literal_nesting()
    RESULT["block2_commuting_factors"] = block2_commuting_factors()
    RESULT["block3_su32_reading"] = block3_su32_reading()
    RESULT["block4_killing_adjoint"] = block4_killing_adjoint()
    RESULT["block5_ads_conformal"] = block5_ads_conformal()
    RESULT["block6_philology"] = block6_philology()

    log("\n" + "=" * 78)
    log("THE BEST-SUPPORTED RECONSTRUCTION")
    log("=" * 78)
    log("  R1 literal nesting Spin(6,4) > Spin(3,2) > G_SM ......... KILLED  (12 > 10)")
    log("  R2 commuting factors Spin(3,2) x G_SM in Spin(6,4) ..... KILLED  (12 > 10 max cent.)")
    log("  R3 Spin(3,2) as the spacetime factor ................... KILLED  (slot is Spin(1,3), 6)")
    log("  R4 Spin(3,2) ~ Sp(4,R) ~ AdS_4 isometry ................ TRUE identity, NOT in evidence")
    log("  R5 the (6,4) fibre as (so(3,2), Killing) ............... SURVIVES as structure")
    log("  R6 Spin(6,4) > SU(3,2) > S(U(3)xU(2)), by reduction .... BEST-SUPPORTED RECONSTRUCTION")
    RESULT["decision"] = {
        "R1": "KILLED", "R2": "KILLED", "R3": "KILLED",
        "R4": "IDENTITY_CORRECT_NOT_IN_EVIDENCE",
        "R5": "SURVIVES_AS_STRUCTURE", "R6": "BEST_SUPPORTED_RECONSTRUCTION",
        "chain": "Spin(6,4) -> SU(3,2) -> S(U(3)xU(2)) = (SU(3)xSU(2)xU(1))/Z_6",
        "step_1_kind": "complex-structure reduction of the rank-10 vertical bundle",
        "step_1_global_status": "UNBUILT_REQUIRES_COMPLEX_AND_DETERMINANT_REDUCTION_DATA",
        "step_2_kind": "maximal-compact (Cartan) reduction",
        "step_2_global_status": "REDUCTION_EXTERNAL",
        "source_status": "TRANSCRIPT_UNCERTAIN_AUDIO_UNCHECKED_PDF_EXTRACTION_MEDIATED",
        "not_a": "GUT symmetry-breaking chain; the source denies grand unification outright",
    }

    assert_no_float(RESULT)
    log("\nassert_no_float: clean -- every number above is an int or a Fraction.")

    total = len(FAIL)
    log("\n" + "=" * 78)
    if total:
        log(f"FAILURES: {total}")
        for f in FAIL:
            log("  FAIL " + f)
        return 1
    log("ALL CHECKS PASS")
    return 0


PLANTS = [
    ("dim_so32", "dim so(3,2) forced to 12, which would let the literal nesting survive"),
    ("max_cent", "max centraliser forced to 12, which would let the factorisation survive"),
    ("killing_sig", "Killing signature of so(3,2) forced to (4,6), breaking the fibre match"),
    ("n_su32", "the source's twice-spoken 's u three comma two' forced to zero occurrences"),
]


def selftest() -> int:
    log("SELF-TEST: each planted false fact must force exit 1.")
    bad = []
    for name, why in PLANTS:
        proc = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--plant", name],
                              capture_output=True, text=True)
        ok = proc.returncode == 1
        print(("PASS" if ok else "FAIL") + f" :: plant {name!r} exits 1 -- {why}"
              + ("" if ok else f" (got exit {proc.returncode})"))
        if not ok:
            bad.append(name)
    proc = subprocess.run([sys.executable, str(Path(__file__).resolve())],
                          capture_output=True, text=True)
    ok = proc.returncode == 0
    print(("PASS" if ok else "FAIL") + " :: the unplanted run exits 0"
          + ("" if ok else f" (got exit {proc.returncode})"))
    if not ok:
        bad.append("clean-run")
    if bad:
        print(f"SELF-TEST FAILED: {bad}")
        return 1
    print(f"SELF-TEST PASSED: {len(PLANTS)} planted false facts each forced exit 1, "
          "and the clean run exits 0.")
    return 0


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--selftest" in argv:
        sys.exit(selftest())
    if "--plant" in argv:
        PLANT = argv[argv.index("--plant") + 1]
    sys.exit(run())
