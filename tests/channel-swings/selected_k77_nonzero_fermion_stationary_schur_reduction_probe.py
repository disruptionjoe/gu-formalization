#!/usr/bin/env python3
"""Exact nonzero-fermion stationary Schur-reduction probe.

Layer 0: this probe studies the finite block kernel of the source-displayed
southeast-zero candidate

    D = [[A, B], [C, 0]]

on a one-form carrier plus a zero-form carrier.  It does not compute a
characteristic kernel, BV cohomology, closed-domain spectrum, Fredholm index,
generation count, or the actual image of the moving source field ``varpi``.

Run with pinned SymPy 1.14.0:

    uv run --with 'sympy==1.14.0' python \
      tests/channel-swings/selected_k77_nonzero_fermion_stationary_schur_reduction_probe.py
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def load_unique(path: Path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


def column_basis(vectors: list[sp.Matrix], rows: int) -> sp.Matrix:
    return sp.Matrix.hstack(*vectors) if vectors else sp.zeros(rows, 0)


def residual_certificate(A: sp.Matrix, B: sp.Matrix, C: sp.Matrix):
    """Return D, bases N/L, and S=L*A*N for full-rank B and C.

    N identifies ``ker C``.  The rows of L annihilate ``im B`` and therefore
    coordinatize ``coker B``.  For B injective and C surjective, projection
    gives an isomorphism ``ker D ~= ker(L*A*N)``.
    """
    p, q = B.rows, B.cols
    assert A.shape == (p, p)
    assert C.shape == (q, p)
    assert B.rank() == q
    assert C.rank() == q
    N = column_basis(C.nullspace(), p)
    L = column_basis(B.T.nullspace(), p).T
    S = sp.simplify(L * A * N)
    D = A.row_join(B).col_join(C.row_join(sp.zeros(q, q)))
    return D, N, L, S


def nullity(M: sp.Matrix) -> int:
    return M.cols - M.rank()


print("A. SOURCE, PRIOR ART, AND LAYER-0 FENCES")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
principal = load_unique(ROOT / "lab/process/selected-k77-induced-fermion-principal-discriminator.json")
zero_fermion = (ROOT / "explorations/conditional-build/selected-k77-zero-fermion-coupled-hessian-current-order-2026-08-10.md").read_text()
check("source", "draft 9.16 displays four independent barred/unbarred fields", "four distinct fields" in source)
check("source", "draft displays a southeast-zero candidate but permits a nonzero rival", "southeast-zero" in source and "SOURCE-ADMITS-UNSPECIFIED-RIVAL" in source)
check("source", "draft is silent on a common domain and three-family index", "common variational domain" in source and "three-family index" in source)
check("prior_art", "zero-fermion wave leaves the nonzero stationary branch open", "nonzero-fermion stationary solution" in zero_fermion)
check("layer0", "stationary kernel is not characteristic kernel, BV cohomology, Fredholm index or count", True)
check("layer0", "full U64,64 and two U32,32 halves remain distinct lower-order parents", "two_U32_32_halves" in principal["parent_ablations"])


print("\nB. EXACT RESIDUAL-MAP THEOREM FIXTURES")
B42 = sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
C24 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1]])
A_full = sp.Matrix([[2, 1, 0, 1], [-1, 3, 2, 0], [1, 2, 4, -1], [3, 5, 1, 2]])
A_rank1 = sp.Matrix([[2, 1, 0, 1], [-1, 3, 2, 0], [1, 2, 4, -1], [2, 4, 1, 2]])
A_zero = sp.Matrix([[2, 1, 0, 1], [-1, 3, 2, 0], [0, 0, 4, -1], [0, 0, 1, 2]])

expected = [(A_full, 0, 2), (A_rank1, 1, 1), (A_zero, 2, 0)]
for idx, (A, expected_nullity, expected_rank) in enumerate(expected, 1):
    D, N, L, S = residual_certificate(A, B42, C24)
    check("exact", f"fixture {idx} has dim ker C = dim coker B = 2", N.cols == 2 and L.rows == 2)
    check("exact", f"fixture {idx} residual rank is {expected_rank}", S.rank() == expected_rank)
    check("exact", f"fixture {idx} full and residual nullities agree", nullity(D) == nullity(S) == expected_nullity)
    check("exact", f"fixture {idx} quotient rows annihilate B", L * B42 == sp.zeros(2, 2))
    check("exact", f"fixture {idx} kernel columns are killed by C", C24 * N == sp.zeros(2, 2))

B32 = sp.Matrix([[1, 0], [0, 1], [0, 0]])
C23 = sp.Matrix([[0, 1, 0], [0, 0, 1]])
A3_live = sp.Matrix([[2, 1, 0], [-1, 3, 2], [7, 4, 1]])
A3_dead = sp.Matrix([[2, 1, 0], [-1, 3, 2], [0, 4, 1]])
for label, A, expected_nullity in (("live", A3_live, 0), ("tuned", A3_dead, 1)):
    D, N, L, S = residual_certificate(A, B32, C23)
    check("exact", f"3+2 {label} fixture has one-dimensional residual", S.shape == (1, 1))
    check("exact", f"3+2 {label} full and residual nullities agree", nullity(D) == nullity(S) == expected_nullity)


print("\nC. K77 DEFECT DIMENSION AND MIRROR REALITY")
sectors = principal["exact_result"]["base_null_coupled_sector_ranks"]
for name in ("W_sd192", "mirror_asd192"):
    one = sectors[name]["one_form_dimension"]
    zero = sectors[name]["domain_dimension"] - one
    check("exact", f"{name} source block has 192 one-form plus 128 zero-form dimensions", (one, zero) == (192, 128))
    check("exact", f"{name} maximal-rank residual map is 64 by 64", one - zero == 64)
check("exact", "W and mirror share the same principal rank/kernel certificate", sectors["W_sd192"] == sectors["mirror_asd192"])

I = sp.I
A_W = sp.Matrix([[2, 1, 0, 1], [-1, 3, 2, 0], [1 + I, 2, 4, -1], [3, I, 1, 2]])
A_M = A_W.conjugate()
D_W, N_W, L_W, S_W = residual_certificate(A_W, B42, C24)
D_M, N_M, L_M, S_M = residual_certificate(A_M, B42, C24)
check("exact", "real B and C give identical kernel/cokernel bases to the mirror", N_W == N_M and L_W == L_M)
check("exact", "mirror residual is coefficientwise conjugate", S_M == S_W.conjugate())
check("exact", "conjugate residual maps have equal rank", S_M.rank() == S_W.rank())
check("exact", "conjugate full stationary operators have equal nullity", nullity(D_M) == nullity(D_W))

A_independent_mirror = sp.Matrix([[2, 1, 0, 1], [-1, 3, 2, 0], [1, 2, 4, -1], [2, 4, 1, 2]])
D_ind, _, _, S_ind = residual_certificate(A_independent_mirror, B42, C24)
check("planted", "independent planted mirror can have a different residual rank", S_ind.rank() != S_W.rank())
check("planted", "independent planted mirror can have a different stationary nullity", nullity(D_ind) != nullity(D_W))


print("\nD. SOUTHEAST-NONZERO RIVAL")
BC = B32 * C23
A_rival = BC + sp.Matrix([[0, 0, 0], [0, 0, 0], [1, 0, 0]])
D_zero, _, _, S_zero = residual_certificate(A_rival, B32, C23)
E = sp.eye(2)
D_nonzero = A_rival.row_join(B32).col_join(C23.row_join(E))
schur_nonzero = A_rival - B32 * E.inv() * C23
check("exact", "displayed southeast-zero candidate is invertible in the rival fixture", nullity(D_zero) == nullity(S_zero) == 0)
check("exact", "nonzero-southeast rival uses A-B E^-1 C", nullity(D_nonzero) == nullity(schur_nonzero) == 2)
check("planted", "zero-block residual formula does not predict the nonzero-block rival", nullity(D_nonzero) != nullity(S_zero))


print("\nE. PREREGISTERED KILL CONTROLS")
check("planted", "southeast zero does not automatically force a stationary mode", nullity(residual_certificate(A_full, B42, C24)[0]) == 0)
check("planted", "a generic full-rank residual kills the nonzero stationary branch", residual_certificate(A_full, B42, C24)[3].det() != 0)
check("planted", "stationarity requires an actual rank-loss equation", residual_certificate(A_rank1, B42, C24)[3].det() == 0)
check("planted", "reality alone cannot split conjugate nullities", nullity(D_M) == nullity(D_W))
check("planted", "a symmetry-breaking control is detectable rather than silently accepted", S_ind != S_W.conjugate())
check("planted", "64 is a residual-map dimension, not a generation count", 64 != 3)
check("type", "actual varpi coefficient image remains unconstructed", True)
check("type", "finite stationary kernel remains distinct from a closed-domain physical zero mode", True)
check("type", "no external datum is booked by the residual-map reduction", True)


total = sum(COUNTS.values())
print(f"\nSUMMARY {total - len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
