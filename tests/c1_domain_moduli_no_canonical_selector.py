#!/usr/bin/env python3
"""C1: the symmetry-fixed domain moduli on the filed (832,832) Green trace.

VERDICT on pass: NO-CANONICAL-SELECTOR__DOMAIN-MODULI-DIMENSION-346112

QUESTION.  U13 (`D1^dom`) and U14 (`D2^dom`) are recorded SOURCE-SILENT with
"no domain yet".  Register item M-M23 asks whether the Z/2 orientation datum is a
w1 obstruction or a choice in a connected Lagrangian Grassmannian.  This
certificate answers M-M23 by computing the dimension of the deck-fixed set of
admissible boundary conditions on the Green trace the repository has already
built.

INPUTS, both filed and neither computed here.
  * inertia(B_n) = (832, 832, 0) on the rank-1664 ker Gamma section trace --
    explorations/eric-curt-wave3d-section-green-domain-2026-07-31.md:44
  * for H = diag(I_n, -I_n) the maximal H-isotropic trace spaces are exactly the
    graphs L_U = {(x, Ux)} with U in U(n), and deck-fixing forces U* = U and
    U^2 = I -- tests/channel-swings/operator_domain_w1_bridge_audit.py

THE COMPUTATION.  A Hermitian unitary involution on C^n is exactly an orthogonal
splitting C^n = E+ (+) E- ; fixing dim E+ = k, the set of such U is the complex
Grassmannian Gr(k,n) = U(n)/(U(k) x U(n-k)), of real dimension 2k(n-k).  So the
deck-fixed admissible set is the disjoint union over k, and CANONICITY WOULD
REQUIRE IT TO BE A SINGLE POINT.  It is not: only k = 0 and k = n are isolated,
and those are the two definite sectors that ECW3D-A already showed are BOTH
admissible and right-H invariant.

WHAT THIS DOES AND DOES NOT SHOW.  It shows that with ALL CURRENTLY FILED
SYMMETRY -- Krein, right-H, deck -- the boundary condition is a positive-
dimensional choice and no canonical selector exists.  That is a row closure at
the stated grade, not a theorem about GU: a larger supplied symmetry group could
shrink the fixed set, and the deck action on trace data is itself one of the six
fields recorded as missing.  Stated as such in the artifact.

This is consistent with, and quantifies, the repository's own prior sentence:
"Existence is cheap; canonical selection is not."
"""

from __future__ import annotations

import numpy as np

TOL = 1e-9
N_TRACE = 832  # inertia (832, 832, 0), filed


def graph_subspace(u: np.ndarray) -> np.ndarray:
    """Columns spanning L_U = {(x, Ux)}."""
    n = u.shape[0]
    return np.vstack((np.eye(n, dtype=complex), u))


def is_maximal_isotropic(u: np.ndarray) -> bool:
    """L_U isotropic for H = diag(I_n, -I_n), and of half dimension."""
    n = u.shape[0]
    h = np.block([[np.eye(n), np.zeros((n, n))],
                  [np.zeros((n, n)), -np.eye(n)]]).astype(complex)
    basis = graph_subspace(u)
    form = basis.conj().T @ h @ basis
    isotropic = np.max(np.abs(form)) < TOL
    half_dim = np.linalg.matrix_rank(basis) == n
    return bool(isotropic and half_dim)


def deck_fixed(u: np.ndarray) -> bool:
    """Deck-fixing: U Hermitian and involutive."""
    return (np.max(np.abs(u - u.conj().T)) < TOL
            and np.max(np.abs(u @ u - np.eye(u.shape[0]))) < TOL)


def grassmannian_real_dim(k: int, n: int) -> int:
    """dim_R U(n)/(U(k) x U(n-k)) = 2k(n-k). Exact integer arithmetic."""
    return 2 * k * (n - k)


def main() -> None:
    print("=" * 78)
    print("C1 -- domain moduli on the filed (832,832) Green trace")
    print("=" * 78)

    # --- 1. the graph classification is real, checked at small n -------------
    rng = np.random.default_rng(20260808)
    for n in (2, 3, 5):
        q, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
        assert is_maximal_isotropic(q), f"graph of a unitary is not maximal isotropic at n={n}"
    print("\n[1] L_U = {(x,Ux)}, U unitary, is maximal isotropic for H = diag(I,-I)")
    print("    checked at n = 2, 3, 5")

    # --- 2. the deck-fixed family is continuous, not discrete ----------------
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    thetas = np.linspace(0.0, np.pi, 9)
    family = []
    for theta in thetas:
        u = np.cos(theta) * sz + np.sin(theta) * sx
        assert deck_fixed(u), "U(theta) is not deck-fixed"
        assert is_maximal_isotropic(u), "U(theta) graph is not maximal isotropic"
        family.append(u)
    distinct = sum(
        1 for i in range(len(family)) for j in range(i + 1, len(family))
        if np.max(np.abs(family[i] - family[j])) > TOL
    )
    assert distinct == len(family) * (len(family) - 1) // 2, "family is not distinct"
    print("\n[2] deck-fixed set is CONTINUOUS, not a discrete Z/2")
    print(f"    U(theta) = cos(theta) sigma_z + sin(theta) sigma_x : {len(family)}/{len(family)}"
          " deck-fixed and maximal isotropic, all distinct")
    print("    (this rank-2 family embeds block-diagonally in every n >= 2)")

    # --- 3. the moduli, exactly, at the filed n ------------------------------
    n = N_TRACE
    dims = [grassmannian_real_dim(k, n) for k in range(n + 1)]
    isolated = [k for k, d in enumerate(dims) if d == 0]
    top = max(dims)
    argtop = dims.index(top)

    print(f"\n[3] deck-fixed admissible set at n = {n}")
    print(f"    = disjoint union over k of Gr(k,{n}) = U({n})/(U(k) x U({n}-k))")
    print(f"    dim_R Gr(k,{n}) = 2k({n}-k)")
    print(f"    strata with dimension 0 : k = {isolated}   (the two definite sectors)")
    print(f"    maximal stratum         : k = {argtop}, dim_R = {top}")

    assert isolated == [0, n], "definite sectors are not the only isolated strata"
    assert top == 2 * (n // 2) * (n - n // 2) == 346112, f"unexpected top dimension {top}"

    print("\n[4] Verdict")
    print("    Canonicity would require the deck-fixed set to be a single point.")
    print(f"    It is not: the maximal stratum has real dimension {top}, and the")
    print("    only 0-dimensional strata are the two definite sectors, which")
    print("    ECW3D-A already showed are BOTH admissible and right-H invariant.")
    print("\nVERDICT: NO-CANONICAL-SELECTOR__DOMAIN-MODULI-DIMENSION-346112")
    print("\nSCOPE, and it is a real limit:")
    print("  * 'with all currently filed symmetry' -- Krein, right-H, deck.")
    print("    A larger supplied symmetry could shrink the fixed set.")
    print("  * the deck action on trace data is itself one of the six fields")
    print("    recorded as missing, so this is a closure AT THE STATED GRADE,")
    print("    not a theorem about GU.")
    print("  * this quantifies, and does not replace, the repository's own")
    print("    prior sentence: 'Existence is cheap; canonical selection is not.'")


if __name__ == "__main__":
    main()
