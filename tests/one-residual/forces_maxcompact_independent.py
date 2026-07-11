"""Independent re-derivation: the maximal compact of su(3,2) is EXACTLY su(3)+su(2)+u(1).

One Residual paper claim (papers/candidates/one-residual-complete-picture/
one-residual-complete-picture-2026-07-11.md, lines 16, 49-50):
  "the maximal compact of the ambient su(3,2) is su(3)+su(2)+u(1) with a single u(1) and no
   extra photon -- 12 generators, block-diagonal, precisely one u(1)."

This is an INDEPENDENT verifier for tests/legs/forces_maximal_compact_is_sm.py. Where that leg
counts anti-Hermitian generators by hand and subtracts one trace direction, this file instead
constructs the WHOLE real Lie algebra su(3,2) from its defining linear constraints, applies the
Cartan involution theta(X) = -X^dag as a linear operator on that space, and reads the maximal
compact k off as theta's (+1)-eigenspace -- then verifies dim, block structure, and the size of
the CENTER of k by pure linear algebra. No generator bookkeeping, no assumed answer.

Math independently established here:
  su(p,q) = {X in gl(n,C) : X^dag eta + eta X = 0, tr X = 0}, eta = diag(I_p, -I_q), n=p+q.
  Cartan involution theta(X) = -X^dag. k = fix(theta) (compact part), p_ = -1 eigenspace (noncompact).
  For su(3,2): expect dim su(3,2)=24, dim k=12, dim p_=12(=2pq), k block-diagonal,
  [k,k] semisimple of dim 11, center(k) of dim exactly 1  =>  k = su(3)+su(2)+u(1), one u(1).

Run: python tests/one-residual/forces_maxcompact_independent.py
"""
from __future__ import annotations

import numpy as np

FAIL: list[str] = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- represent a complex 5x5 matrix as a real vector of length 2*n*n (Re then Im) ----
P, Q = 3, 2
N = P + Q
ETA = np.diag([1.0] * P + [-1.0] * Q)
DIM_C = N * N


def mat_to_vec(M):
    return np.concatenate([M.real.flatten(), M.imag.flatten()])


def vec_to_mat(v):
    re = v[:DIM_C].reshape(N, N)
    im = v[DIM_C:].reshape(N, N)
    return re + 1j * im


def real_nullspace(A, tol=1e-9):
    """Orthonormal real basis of {x : A x = 0}."""
    _, s, vh = np.linalg.svd(A)
    rank = int((s > tol).sum())
    return vh[rank:].conj().T  # columns = null basis


def build_su32_basis():
    """Real basis of su(3,2) = {X: X^dag eta + eta X = 0, tr X = 0} via linear constraints."""
    # Assemble the two constraint operators as explicit real matrices by acting on each real coord.
    # Constraint A: X^dag eta + eta X = 0 (N*N complex eqns -> 2*N*N real rows). Constraint tr X = 0.
    ncoord = 2 * DIM_C
    consA = np.zeros((2 * DIM_C, ncoord))  # Re/Im of the N*N-entry matrix eqn A, flattened
    consTr = np.zeros((2, ncoord))         # Re/Im of tr X
    for j in range(ncoord):
        e = np.zeros(ncoord)
        e[j] = 1.0
        X = vec_to_mat(e)
        A = X.conj().T @ ETA + ETA @ X
        consA[:DIM_C, j] = A.real.flatten()
        consA[DIM_C:, j] = A.imag.flatten()
        t = np.trace(X)
        consTr[0, j] = t.real
        consTr[1, j] = t.imag
    C = np.vstack([consA, consTr])
    NB = real_nullspace(C)  # columns are real coords of basis elements
    basis = [vec_to_mat(NB[:, k]) for k in range(NB.shape[1])]
    return basis


def theta(X):
    return -X.conj().T


def commutator(A, B):
    return A @ B - B @ A


def span_dim(mats, tol=1e-8):
    """Real dimension of the span of a list of complex matrices (as real vectors)."""
    if not mats:
        return 0
    V = np.array([mat_to_vec(m) for m in mats])
    s = np.linalg.svd(V, compute_uv=False)
    return int((s > tol).sum())


def reduce_to_basis(mats, tol=1e-8):
    """Return an independent set of matrices spanning the same real space (via SVD range)."""
    V = np.array([mat_to_vec(m) for m in mats])   # rows = vectors
    u, s, vh = np.linalg.svd(V.T, full_matrices=False)  # columns of u = orthonormal range basis
    rank = int((s > tol).sum())
    return [vec_to_mat(u[:, i]) for i in range(rank)]


def project_onto(basis, X, tol=1e-8):
    """Return True if X lies in real span of basis."""
    V = np.array([mat_to_vec(m) for m in basis]).T  # columns basis
    x = mat_to_vec(X)
    coef, *_ = np.linalg.lstsq(V, x, rcond=None)
    return np.linalg.norm(V @ coef - x) < tol * (1 + np.linalg.norm(x))


def main():
    print("[independent] maximal compact of su(3,2) via Cartan involution theta(X) = -X^dag\n")

    basis = build_su32_basis()
    d = span_dim(basis)
    print(f"  built su(3,2) from constraints: real dimension = {d}")
    check("su(3,2) has dimension 24 = 5^2 - 1", d == 24, f"dim = {d}")

    # theta must be an involutive automorphism preserving su(3,2)
    theta_ok = all(project_onto(basis, theta(b)) for b in basis)
    invol = all(np.allclose(theta(theta(b)), b) for b in basis)
    check("theta(X) = -X^dag preserves su(3,2) and is involutive (theta^2 = id)", theta_ok and invol)

    # Split su(3,2) by the involution theta via projectors (theta^2=id, so P_+/-=(1 +/- theta)/2).
    # k = fix(theta): theta(X)=X <=> -X^dag=X <=> X anti-Hermitian.  p = (-1)-space: X Hermitian.
    # Projecting EVERY basis element and taking the real span is exact (no eigen-solve of a
    # non-orthonormal coordinate matrix); the two spans are the genuine eigenspaces of theta.
    k = reduce_to_basis([0.5 * (b + theta(b)) for b in basis])   # anti-Herm parts -> maximal compact
    p_ = reduce_to_basis([0.5 * (b - theta(b)) for b in basis])  # Herm parts      -> noncompact part
    dim_k = span_dim(k)
    dim_p = span_dim(p_)
    print(f"  theta eigenspaces: dim k (+1) = {dim_k}, dim p (-1) = {dim_p}")
    check("maximal compact k = fix(theta) has dimension 12", dim_k == 12, f"dim k = {dim_k}")
    check("noncompact part p has dimension 12 = 2*p*q (2*3*2)", dim_p == 12, f"dim p = {dim_p}")

    # k must be a subalgebra: [k,k] subset of k
    closed = all(project_onto(k, commutator(a, b)) for a in k for b in k)
    check("k is a Lie subalgebra ([k,k] subset k)", closed)

    # Block-diagonal: every element of k has zero (3x2) and (2x3) off-blocks.
    offmax = 0.0
    for m in k:
        offmax = max(offmax, np.abs(m[:P, P:]).max(), np.abs(m[P:, :P]).max())
    check("k is BLOCK-DIAGONAL (u(3)+u(2); no color-electroweak mixing)", offmax < 1e-9,
          f"off-block max = {offmax:.1e}")

    # Derived algebra [k,k] = semisimple part; its dimension should be 11 = 8 (su3) + 3 (su2).
    brackets = [commutator(a, b) for a in k for b in k]
    dim_derived = span_dim(brackets)
    check("[k,k] is semisimple of dimension 11 = su(3)(8) + su(2)(3)", dim_derived == 11,
          f"dim [k,k] = {dim_derived}")

    # CENTER of k: elements commuting with every element of k. Solve linear system in k-coords.
    # z = sum c_i k_i with [z, k_j] = 0 for all j.  Build real linear map c -> ([z,k_j])_j and null it.
    Kb = np.array([mat_to_vec(m) for m in k]).T      # 2*DIM_C x 12
    rows = []
    for kj in k:
        # each c -> [sum c_i k_i, k_j] is linear in c; assemble as 2*DIM_C x 12 block
        blk = np.array([mat_to_vec(commutator(ki, kj)) for ki in k]).T  # 2*DIM_C x 12
        rows.append(blk)
    Csys = np.vstack(rows)  # (num_j * 2*DIM_C) x 12
    center_null = real_nullspace(Csys)
    dim_center = center_null.shape[1]
    print(f"  center(k) dimension = {dim_center}")
    check("center(k) is EXACTLY 1-dimensional (precisely ONE u(1), no extra photon)", dim_center == 1,
          f"dim center = {dim_center}")

    # Cross-check: dim k = dim[k,k] + dim center  => 12 = 11 + 1 (reductive: semisimple + center)
    check("k = [k,k] (+) center: 12 = 11 + 1  =>  su(3)+su(2)+u(1)", dim_k == dim_derived + dim_center,
          f"{dim_k} = {dim_derived} + {dim_center}")

    print("\n[verdict]")
    if not FAIL:
        print("  * INDEPENDENTLY re-derived: the maximal compact of su(3,2) is EXACTLY su(3)+su(2)+u(1).")
        print("    Built the full 24-dim algebra from its defining constraints, took the Cartan-involution")
        print("    (+1)-eigenspace -> 12 dims, block-diagonal, derived algebra 11 (su3+su2) + center 1 (one u(1)).")
        print("  * Confirms tests/legs/forces_maximal_compact_is_sm.py by a disjoint method (no generator")
        print("    counting): the SM gauge algebra with precisely ONE U(1) and no extra photon is what the")
        print("    maximal-compact / Cartan selection forces. EXISTENCE grade.")
    else:
        print(f"\nFAILED: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = max compact of su(3,2) = su(3)+su(2)+u(1), dim 12, exactly one U(1) (independent).")


if __name__ == "__main__":
    main()
