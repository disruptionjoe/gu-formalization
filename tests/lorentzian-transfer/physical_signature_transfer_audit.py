#!/usr/bin/env python3
"""V15-1: side-by-side compact/complexified versus physical-signature audit.

The script deliberately constructs three different carrier objects:

* ``compact_selected``: the existing (4,0)+(5,5) self-dual 192-space;
* ``lorentz_complex_half``: one complex self-dual 192-space for
  (3,1)+(6,4); and
* ``lorentz_real_closure``: that space plus its physical-conjugate
  anti-self-dual partner, a 384-complex-dimensional real-form-stable closure.

It does not invent a Y14 source action, a positive-Hilbert completion, or a
physical-state projector.  All dimensions below are complex dimensions.

Run from the repository root with a Python environment containing NumPy:

    python tests/lorentzian-transfer/physical_signature_transfer_audit.py

Use ``--json`` for a machine-readable runtime result.  Exit status is nonzero
if a mathematical check, discriminating control, or receipt comparison fails.
"""

from __future__ import annotations

import argparse
import json
import sys
from itertools import combinations
from pathlib import Path

import numpy as np


N = 14
SPIN_DIM = 128
BASE_DIM = 4
SEED = 20260723
TOL = 1.0e-8
ROOT = Path(__file__).resolve().parents[2]
RECEIPT = Path(__file__).with_name("V15-1-receipt.json")

I2 = np.eye(2, dtype=complex)
I4 = np.eye(BASE_DIM, dtype=complex)
I128 = np.eye(SPIN_DIM, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)

rng = np.random.default_rng(SEED)
checks: list[dict[str, object]] = []


def check(condition: bool, name: str, detail: str = "") -> None:
    """Record and enforce one audit assertion."""
    ok = bool(condition)
    checks.append({"name": name, "ok": ok, "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))
    if not ok:
        raise AssertionError(name)


def jordan_wigner(n: int) -> list[np.ndarray]:
    """Return 2n Hermitian Euclidean Clifford generators."""
    out: list[np.ndarray] = []
    for k in range(n):
        for middle in (S1, S2):
            matrix = np.array([[1.0 + 0.0j]])
            for factor in [S3] * k + [middle] + [I2] * (n - 1 - k):
                matrix = np.kron(matrix, factor)
            out.append(matrix)
    return out


EUCLIDEAN_GAMMAS = jordan_wigner(7)


def gammas(timelike: set[int]) -> list[np.ndarray]:
    """Realize Cl(p,q) by multiplying each timelike Euclidean gamma by i."""
    return [
        1j * EUCLIDEAN_GAMMAS[a] if a in timelike else EUCLIDEAN_GAMMAS[a]
        for a in range(N)
    ]


def spin_generator(e: list[np.ndarray], a: int, b: int) -> np.ndarray:
    return 0.25 * (e[a] @ e[b] - e[b] @ e[a])


def vector_generator(a: int, b: int, eta: np.ndarray) -> np.ndarray:
    """The (a,b) generator on vectors for diagonal metric eta."""
    matrix = np.zeros((BASE_DIM, BASE_DIM), dtype=complex)
    matrix[a, b] = eta[b]
    matrix[b, a] = -eta[a]
    return matrix


def base_tensor_generator(
    e: list[np.ndarray], eta: np.ndarray, a: int, b: int
) -> np.ndarray:
    return np.kron(vector_generator(a, b, eta), I128) + np.kron(
        I4, spin_generator(e, a, b)
    )


def normalize_involution(matrix: np.ndarray) -> np.ndarray:
    """Phase-normalize a Clifford volume element to square to +1."""
    square = complex(np.trace(matrix @ matrix) / matrix.shape[0])
    if square.real < 0:
        matrix = -1j * matrix
        square = complex(np.trace(matrix @ matrix) / matrix.shape[0])
    return matrix / np.sqrt(abs(square.real))


def volume(e: list[np.ndarray], directions: range) -> np.ndarray:
    out = I128.copy()
    for a in directions:
        out = out @ e[a]
    return normalize_involution(out)


def spinor_krein_metric(e: list[np.ndarray], timelike: set[int]) -> np.ndarray:
    """The program-native invariant spinor Krein metric used by the baseline."""
    out = I128.copy()
    for a in range(N):
        if a not in timelike:
            out = out @ e[a]
    if np.linalg.norm(out.conj().T + out) < 1.0e-9:
        out = 1j * out
    scale = np.sqrt(abs(complex((out @ out)[0, 0]).real))
    return out / scale


def casimir_selected_space(
    e: list[np.ndarray], eta: np.ndarray, self_dual_factor: complex
) -> tuple[np.ndarray, list[np.ndarray], np.ndarray]:
    """Select the Casimir-8 complex rank-192 self-dual sector.

    ``self_dual_factor=1`` is the compact self-dual algebra.  The Lorentzian
    factors ``+i`` and ``-i`` are the two complex Hodge-star eigenspaces.
    """
    generators = {
        (a, b): base_tensor_generator(e, eta, a, b)
        for a, b in combinations(range(BASE_DIM), 2)
    }
    chiral = [
        generators[(0, 1)] + self_dual_factor * generators[(2, 3)],
        generators[(0, 2)] - self_dual_factor * generators[(1, 3)],
        self_dual_factor * generators[(0, 3)] + generators[(1, 2)],
    ]
    casimir = -(chiral[0] @ chiral[0] + chiral[1] @ chiral[1] + chiral[2] @ chiral[2])
    eigenvalues, eigenvectors = np.linalg.eig(casimir)
    mask = np.abs(eigenvalues - 8.0) < 1.0e-6
    selected, _ = np.linalg.qr(eigenvectors[:, mask])
    residual = np.linalg.norm(casimir @ selected - 8.0 * selected)
    return selected, chiral, np.array([mask.sum(), residual])


def sector_generators(
    e: list[np.ndarray], eta_base: np.ndarray
) -> list[np.ndarray]:
    """so(base)+so(internal) generators on V_base tensor S."""
    out = [
        base_tensor_generator(e, eta_base, a, b)
        for a, b in combinations(range(BASE_DIM), 2)
    ]
    out.extend(
        np.kron(I4, spin_generator(e, a, b))
        for a, b in combinations(range(BASE_DIM, N), 2)
    )
    return out


def restrict(matrix: np.ndarray, basis: np.ndarray) -> np.ndarray:
    return basis.conj().T @ matrix @ basis


def leakage(matrix: np.ndarray, basis: np.ndarray) -> float:
    image = matrix @ basis
    return float(np.linalg.norm(image - basis @ (basis.conj().T @ image)))


def signature(matrix: np.ndarray, tol: float = TOL) -> tuple[int, int, int]:
    hermitian = 0.5 * (matrix + matrix.conj().T)
    eigenvalues = np.linalg.eigvalsh(hermitian)
    return (
        int(np.sum(eigenvalues > tol)),
        int(np.sum(eigenvalues < -tol)),
        int(np.sum(np.abs(eigenvalues) <= tol)),
    )


def rank(matrix: np.ndarray, tol: float = TOL) -> int:
    singular = np.linalg.svd(matrix, compute_uv=False)
    return int(np.sum(singular > tol))


def real_clifford_type(p: int, q: int) -> tuple[str, int]:
    """Exact mod-8 classification: return division type and matrix size."""
    n = p + q
    residue = (p - q) % 8
    algebra_type = {
        0: "R",
        1: "R+R",
        2: "R",
        3: "C",
        4: "H",
        5: "H+H",
        6: "H",
        7: "C",
    }[residue]
    exponent_numerator = {
        "R": n,
        "R+R": n - 1,
        "C": n - 1,
        "H": n - 2,
        "H+H": n - 3,
    }[algebra_type]
    check(
        exponent_numerator % 2 == 0,
        f"Cl({p},{q}) classification exponent integral",
    )
    return algebra_type, 2 ** (exponent_numerator // 2)


def even_clifford_type(p: int, q: int) -> tuple[str, int]:
    """Use Cl^0(p,q)=Cl(p,q-1) for q>0 in this convention."""
    if q:
        return real_clifford_type(p, q - 1)
    return real_clifford_type(q, p - 1)


def clean_spectra(
    eigen_a: np.ndarray, eigen_b: np.ndarray, tolerance: float
) -> bool:
    comparisons = (
        np.abs(eigen_a[:, None] - eigen_a[None, :]),
        np.abs(eigen_b[:, None] - eigen_b[None, :]),
        np.abs(eigen_a[:, None] - eigen_b[None, :]),
    )
    return all(not np.any((d > tolerance) & (d < 50.0 * tolerance)) for d in comparisons)


def hom_space(
    left: list[np.ndarray],
    right: list[np.ndarray],
    label: str,
    tolerance: float = 1.0e-6,
) -> list[np.ndarray]:
    """Compute all X satisfying X right_i = left_i X.

    This is the baseline census's generic-element/PSD-normal-matrix method.
    Every returned basis vector is checked against every Lie generator.
    """
    dimension = left[0].shape[0]
    for _ in range(16):
        coefficients = rng.uniform(0.5, 1.5, size=len(left)) * rng.choice(
            [-1.0, 1.0], size=len(left)
        )
        generic_left = sum(c * m for c, m in zip(coefficients, left))
        generic_right = sum(c * m for c, m in zip(coefficients, right))
        eigen_left, vectors_left = np.linalg.eig(generic_left)
        eigen_right, vectors_right = np.linalg.eig(generic_right)
        if not clean_spectra(eigen_left, eigen_right, tolerance):
            continue
        differences = np.abs(eigen_left[:, None] - eigen_right[None, :])
        rows, columns = np.nonzero(differences < tolerance)
        if len(rows) <= 4 * dimension:
            break
    else:
        raise RuntimeError(f"{label}: no clean generic element")

    if not len(rows):
        print(f"    {label}: dim 0 (generic spectra disjoint)")
        return []

    inverse_left = np.linalg.inv(vectors_left)
    inverse_right = np.linalg.inv(vectors_right)
    probe_pairs: list[tuple[np.ndarray, np.ndarray]] = []
    for _ in range(12):
        probe_coefficients = rng.standard_normal(len(left))
        probe_pairs.append(
            (
                sum(c * m for c, m in zip(probe_coefficients, left)),
                sum(c * m for c, m in zip(probe_coefficients, right)),
            )
        )

    variable_count = len(rows)
    normal = np.zeros((variable_count, variable_count), dtype=complex)
    for matrix_left, matrix_right in probe_pairs:
        transformed_left = inverse_left @ matrix_left @ vectors_left
        transformed_right = inverse_right @ matrix_right @ vectors_right
        rrh = transformed_right @ transformed_right.conj().T
        lhl = transformed_left.conj().T @ transformed_left
        left_slice = transformed_left[np.ix_(rows, rows)]
        right_slice = transformed_right[np.ix_(columns, columns)]
        normal += (
            (rows[:, None] == rows[None, :]) * rrh[np.ix_(columns, columns)].T
            - left_slice * right_slice.conj()
            - left_slice.conj().T * right_slice.T
            + (columns[:, None] == columns[None, :]) * lhl[np.ix_(rows, rows)]
        )
    normal = 0.5 * (normal + normal.conj().T)
    normal_eigenvalues, normal_vectors = np.linalg.eigh(normal)
    threshold = 1.0e-8 * max(1.0, float(normal_eigenvalues.max()))
    null_indices = np.nonzero(normal_eigenvalues < threshold)[0]

    basis: list[np.ndarray] = []
    for index in null_indices:
        transformed = np.zeros((dimension, dimension), dtype=complex)
        transformed[rows, columns] = normal_vectors[:, index]
        candidate = vectors_left @ transformed @ inverse_right
        basis.append(candidate / np.linalg.norm(candidate))

    worst = 0.0
    for candidate in basis:
        for matrix_left, matrix_right in zip(left, right):
            worst = max(
                worst,
                float(np.linalg.norm(candidate @ matrix_right - matrix_left @ candidate)),
            )
    next_eigenvalue = (
        float(normal_eigenvalues[len(null_indices)])
        if len(null_indices) < variable_count
        else float("inf")
    )
    check(
        worst < 2.0e-6,
        f"{label} basis residual",
        f"dim={len(basis)}, max={worst:.2e}, next={next_eigenvalue:.2e}",
    )
    return basis


def span_rank(matrices: list[np.ndarray], tol: float = 1.0e-7) -> int:
    if not matrices:
        return 0
    flattened = np.stack([m.reshape(-1) for m in matrices], axis=1)
    return rank(flattened, tol)


def census(
    compressed_generators: list[np.ndarray],
    chirality: np.ndarray,
    label: str,
) -> tuple[dict[str, int], dict[str, str]]:
    """Compute the five class-C Hom-space dimensions and anti chirality type."""
    commutant = hom_space(compressed_generators, compressed_generators, f"{label} comm")
    bilinear = hom_space(
        [-g.T for g in compressed_generators],
        compressed_generators,
        f"{label} bil",
    )
    sesquilinear = hom_space(
        [-g.conj().T for g in compressed_generators],
        compressed_generators,
        f"{label} ses",
    )
    antilinear = hom_space(
        compressed_generators,
        [g.conj() for g in compressed_generators],
        f"{label} anti",
    )

    # Linear maps use ordinary conjugation by Gamma.  The entrywise complex
    # conjugate appears only for antilinear maps M . conj below.
    swap_components = [0.5 * (m - chirality @ m @ chirality) for m in commutant]
    cross_linear = span_rank([m for m in swap_components if np.linalg.norm(m) > 1.0e-8])

    anti_types: list[str] = []
    for matrix in antilinear:
        preserve = np.linalg.norm(chirality @ matrix - matrix @ chirality.conj())
        swap = np.linalg.norm(chirality @ matrix + matrix @ chirality.conj())
        anti_types.append("preserve" if preserve < swap else "swap")
        check(
            min(preserve, swap) < 2.0e-6,
            f"{label} antilinear chirality purity",
            f"preserve={preserve:.2e}, swap={swap:.2e}",
        )

    dimensions = {
        "linear_commutant": len(commutant),
        "bilinear_forms": len(bilinear),
        "sesquilinear_forms": len(sesquilinear),
        "antilinear_intertwiners": len(antilinear),
        "cross_chirality_linear": cross_linear,
    }
    classification = {
        "total_chirality": (
            "none"
            if not anti_types
            else "all_preserve"
            if set(anti_types) == {"preserve"}
            else "all_swap"
            if set(anti_types) == {"swap"}
            else "mixed"
        )
    }
    print(f"    {label} census: {tuple(dimensions.values())}; anti={classification}")
    return dimensions, classification


def build_model(
    name: str,
    timelike: set[int],
    eta_base: np.ndarray,
    self_dual_factor: complex,
) -> dict[str, object]:
    e = gammas(timelike)
    basis, _, selection = casimir_selected_space(e, eta_base, self_dual_factor)
    check(
        basis.shape == (BASE_DIM * SPIN_DIM, 192),
        f"{name} Casimir-8 dimension",
        str(basis.shape[1]),
    )
    check(
        float(selection[1]) < 2.0e-9,
        f"{name} Casimir residual",
        f"{selection[1]:.2e}",
    )

    gamma_trace = np.hstack(e)
    embedded = np.zeros((N * SPIN_DIM, basis.shape[1]), dtype=complex)
    embedded[: BASE_DIM * SPIN_DIM, :] = basis
    gamma_residual = float(np.linalg.norm(gamma_trace @ embedded))
    check(
        gamma_residual < 2.0e-9,
        f"{name} gamma-traceless",
        f"{gamma_residual:.2e}",
    )

    generators = sector_generators(e, eta_base)
    generator_leakage = max(leakage(g, basis) for g in generators)
    check(
        generator_leakage < 2.0e-9,
        f"{name} real-form covariance",
        f"max leakage={generator_leakage:.2e}",
    )

    total_chirality = restrict(np.kron(I4, volume(e, range(N))), basis)
    internal_chirality = restrict(np.kron(I4, volume(e, range(BASE_DIM, N))), basis)
    total_split = signature(total_chirality)
    check(
        total_split == (96, 96, 0),
        f"{name} 14d chirality split",
        str(total_split),
    )
    alignment = min(
        np.linalg.norm(total_chirality - internal_chirality),
        np.linalg.norm(total_chirality + internal_chirality),
    )
    check(
        alignment < 2.0e-9,
        f"{name} selected-half total/internal chirality alignment",
        f"{alignment:.2e}",
    )

    beta = spinor_krein_metric(e, timelike)
    krein_full = np.kron(np.diag(eta_base), beta)
    krein_restricted = restrict(krein_full, basis)

    return {
        "name": name,
        "timelike": timelike,
        "eta_base": eta_base,
        "e": e,
        "basis": basis,
        "generators": generators,
        "compressed_generators": [restrict(g, basis) for g in generators],
        "total_chirality": total_chirality,
        "internal_chirality": internal_chirality,
        "krein_full": krein_full,
        "krein_restricted": krein_restricted,
    }


def physical_conjugation(e: list[np.ndarray]) -> np.ndarray:
    """Construct the Cl(9,5)-commuting quaternionic antilinear structure."""
    matrix = I128.copy()
    imaginary_directions = []
    for a, gamma in enumerate(e):
        if np.max(np.abs(gamma.real)) < 1.0e-12:
            imaginary_directions.append(a)
            matrix = matrix @ gamma
    scale = np.sqrt(abs(complex((matrix @ matrix.conj())[0, 0]).real))
    matrix = matrix / scale
    check(
        imaginary_directions == [1, 4, 6, 9, 11, 13],
        "physical real-structure imaginary-gamma control",
        str(imaginary_directions),
    )
    return np.kron(I4, matrix)


def compare_receipt(runtime: dict[str, object]) -> None:
    expected = json.loads(RECEIPT.read_text(encoding="utf-8"))
    expected_results = expected["expected_results"]
    check(
        runtime["exact_claims"] == expected_results["exact_claims"],
        "machine receipt exact-claim match",
    )
    check(
        runtime["census_dimensions"] == expected_results["census_dimensions"],
        "machine receipt census match",
    )
    check(
        runtime["antilinear_behavior"] == expected_results["antilinear_behavior"],
        "machine receipt antilinear match",
    )


def run_audit() -> dict[str, object]:
    print("=" * 96)
    print("V15-1 physical-signature transfer audit")
    print("=" * 96)

    compact = build_model(
        "compact_selected",
        timelike={4, 5, 6, 7, 8},
        eta_base=np.array([1.0, 1.0, 1.0, 1.0]),
        self_dual_factor=1.0,
    )
    lorentz_left = build_model(
        "lorentz_complex_half",
        timelike={3, 4, 5, 6, 7},
        eta_base=np.array([1.0, 1.0, 1.0, -1.0]),
        self_dual_factor=1j,
    )
    lorentz_right = build_model(
        "lorentz_conjugate_half",
        timelike={3, 4, 5, 6, 7},
        eta_base=np.array([1.0, 1.0, 1.0, -1.0]),
        self_dual_factor=-1j,
    )

    compact_signature = signature(compact["krein_restricted"])
    left_krein_rank = rank(lorentz_left["krein_restricted"])
    right_krein_rank = rank(lorentz_right["krein_restricted"])
    check(
        compact_signature == (96, 96, 0),
        "compact selected Krein signature",
        str(compact_signature),
    )
    check(
        left_krein_rank == 0 and right_krein_rank == 0,
        "single Lorentzian complex halves are Krein-null",
        f"ranks=({left_krein_rank},{right_krein_rank})",
    )

    overlap = np.linalg.norm(
        lorentz_left["basis"].conj().T @ lorentz_right["basis"]
    )
    closure_basis, _ = np.linalg.qr(
        np.hstack([lorentz_left["basis"], lorentz_right["basis"]])
    )
    check(
        closure_basis.shape[1] == 384 and overlap < 2.0e-9,
        "Lorentzian conjugate closure dimension",
        f"dim={closure_basis.shape[1]}, overlap={overlap:.2e}",
    )

    physical_krein = restrict(lorentz_left["krein_full"], closure_basis)
    closure_signature = signature(physical_krein)
    cross_pairing = (
        lorentz_left["basis"].conj().T
        @ lorentz_left["krein_full"]
        @ lorentz_right["basis"]
    )
    check(
        closure_signature == (192, 192, 0),
        "real-form-stable Lorentzian closure Krein signature",
        str(closure_signature),
    )
    check(
        rank(cross_pairing) == 192,
        "Lorentzian Krein form pairs the two null halves nondegenerately",
        f"rank={rank(cross_pairing)}",
    )

    physical_j = physical_conjugation(lorentz_left["e"])
    j_square = physical_j @ physical_j.conj()
    check(
        np.linalg.norm(j_square + np.eye(j_square.shape[0])) < 2.0e-9,
        "physical conjugation is quaternionic",
        f"||J^2+1||={np.linalg.norm(j_square + np.eye(j_square.shape[0])):.2e}",
    )
    image_left = physical_j @ lorentz_left["basis"].conj()
    leak_to_left = np.linalg.norm(
        image_left
        - lorentz_left["basis"] @ (lorentz_left["basis"].conj().T @ image_left)
    )
    leak_to_right = np.linalg.norm(
        image_left
        - lorentz_right["basis"] @ (lorentz_right["basis"].conj().T @ image_left)
    )
    check(
        leak_to_right < 2.0e-9 and leak_to_left > 1.0,
        "physical conjugation exchanges Lorentzian self-dual halves",
        f"to selected={leak_to_left:.2e}, to conjugate={leak_to_right:.2e}",
    )

    total_full = np.kron(I4, volume(lorentz_left["e"], range(N)))
    base_full = np.kron(I4, volume(lorentz_left["e"], range(BASE_DIM)))
    internal_full = np.kron(
        I4, volume(lorentz_left["e"], range(BASE_DIM, N))
    )
    total_preserve = np.linalg.norm(
        total_full @ physical_j - physical_j @ total_full.conj()
    )
    base_swap = np.linalg.norm(base_full @ physical_j + physical_j @ base_full.conj())
    internal_swap = np.linalg.norm(
        internal_full @ physical_j + physical_j @ internal_full.conj()
    )
    check(
        total_preserve < 2.0e-9,
        "physical conjugation preserves total 14d chirality",
        f"{total_preserve:.2e}",
    )
    check(
        base_swap < 2.0e-9 and internal_swap < 2.0e-9,
        "physical conjugation swaps base and internal chirality separately",
        f"base={base_swap:.2e}, internal={internal_swap:.2e}",
    )

    compact_even = even_clifford_type(5, 5)
    physical_even = even_clifford_type(6, 4)
    check(
        compact_even == ("R+R", 16),
        "Cl^0(5,5) has two self-conjugate real Weyl 16s",
        str(compact_even),
    )
    check(
        physical_even == ("C", 16),
        "Cl^0(6,4) has a complex-conjugate Weyl 16 pair",
        str(physical_even),
    )

    closure_generators = [
        restrict(g, closure_basis) for g in lorentz_left["generators"]
    ]
    closure_total_chirality = restrict(total_full, closure_basis)

    compact_census, compact_anti = census(
        compact["compressed_generators"],
        compact["total_chirality"],
        "compact_selected",
    )
    left_census, left_anti = census(
        lorentz_left["compressed_generators"],
        lorentz_left["total_chirality"],
        "lorentz_complex_half",
    )
    closure_census, closure_anti = census(
        closure_generators,
        closure_total_chirality,
        "lorentz_real_closure",
    )

    expected_census = {
        "compact_selected": {
            "linear_commutant": 2,
            "bilinear_forms": 2,
            "sesquilinear_forms": 2,
            "antilinear_intertwiners": 2,
            "cross_chirality_linear": 0,
        },
        "lorentz_complex_half": {
            "linear_commutant": 2,
            "bilinear_forms": 2,
            "sesquilinear_forms": 0,
            "antilinear_intertwiners": 0,
            "cross_chirality_linear": 0,
        },
        "lorentz_real_closure": {
            "linear_commutant": 4,
            "bilinear_forms": 4,
            "sesquilinear_forms": 4,
            "antilinear_intertwiners": 4,
            "cross_chirality_linear": 0,
        },
    }
    actual_census = {
        "compact_selected": compact_census,
        "lorentz_complex_half": left_census,
        "lorentz_real_closure": closure_census,
    }
    check(actual_census == expected_census, "three-object class-C census dimensions")

    # A wrong positive-Hilbert substitution is a discriminating fork control:
    # the identity form is positive, but it is not invariant under boosts.
    positive_identity = np.eye(BASE_DIM * SPIN_DIM, dtype=complex)
    lorentz_invariance_defect = max(
        np.linalg.norm(g.conj().T @ positive_identity + positive_identity @ g)
        for g in lorentz_left["generators"][:6]
    )
    check(
        lorentz_invariance_defect > 1.0,
        "positive-Hilbert default fails Lorentz boost invariance control",
        f"defect={lorentz_invariance_defect:.2e}",
    )

    exact_claims = {
        "compact_selected_dimension": 192,
        "lorentz_complex_half_dimension": 192,
        "lorentz_real_closure_dimension": 384,
        "compact_chiral_blocks": [96, 96],
        "lorentz_complex_half_chiral_blocks": [96, 96],
        "lorentz_real_closure_chiral_blocks": [192, 192],
        "compact_krein_signature": [96, 96],
        "lorentz_complex_half_krein_rank": 0,
        "lorentz_real_closure_krein_signature": [192, 192],
        "compact_internal_even_clifford": "M(16,R)+M(16,R)",
        "physical_internal_even_clifford": "M(16,C)",
    }
    antilinear_behavior = {
        "compact_selected_total_chirality": compact_anti["total_chirality"],
        "lorentz_complex_half_total_chirality": left_anti["total_chirality"],
        "lorentz_real_closure_total_chirality": closure_anti["total_chirality"],
        "physical_conjugation_total_chirality": "preserve",
        "physical_conjugation_base_chirality": "swap",
        "physical_conjugation_internal_chirality": "swap",
        "physical_conjugation_selected_half": "exchange_with_conjugate_half",
    }
    runtime = {
        "schema_version": 1,
        "audit": "V15-1-physical-signature-transfer",
        "seed": SEED,
        "exact_claims": exact_claims,
        "census_dimensions": actual_census,
        "antilinear_behavior": antilinear_behavior,
        "scope_residuals": [
            "no true-Y14 source action",
            "no physical-state projector",
            "no positive-Hilbert completion",
            "no Fredholm or net-handedness index",
            "selection of one Lorentzian complex self-dual half is not real-form-stable",
        ],
    }
    compare_receipt(runtime)
    runtime["checks"] = {
        "passed": sum(1 for item in checks if item["ok"]),
        "failed": sum(1 for item in checks if not item["ok"]),
        "total": len(checks),
    }
    return runtime


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        action="store_true",
        help="print the final runtime result as JSON after the audit",
    )
    arguments = parser.parse_args()
    try:
        runtime = run_audit()
    except Exception as exc:  # keep CI failure concise but explicit
        print(f"\nAUDIT FAILED: {exc}", file=sys.stderr)
        return 1
    print(
        f"\nAUDIT PASS: {runtime['checks']['passed']}/{runtime['checks']['total']} checks"
    )
    if arguments.json:
        print(json.dumps(runtime, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
