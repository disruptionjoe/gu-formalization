#!/usr/bin/env python3
"""
Finite-dimensional Pati-Salam proxy CHSH correlator fixture.

This script is intentionally dependency-free.  It builds the controlled proxy

    H_A = C^4_color tensor C^2_SU(2)_L
    H_B = C^4_anticolor tensor C^2_SU(2)_R

and evaluates the standard CHSH operator with Pauli observables embedded in
the SU(2)_L and SU(2)_R qubit factors.  The color/anticolor factors are
spectators in the controls.

What is executable here:
  - density-matrix and observable sanity checks;
  - a maximally entangled control state reaching 2*sqrt(2);
  - a product-state control staying inside the Bell bound;
  - an explicit pending gate for a future GU-derived rho_AB and GU-admissible
    observables.

What is not allowed:
  - using the control Bell state as if it were a GU derivation.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import sys
from typing import Dict, Iterable, List, Sequence, Tuple


Matrix = List[List[complex]]
Vector = List[complex]

COLOR_DIM = 4
QUBIT_DIM = 2
ALICE_DIM = COLOR_DIM * QUBIT_DIM
BOB_DIM = COLOR_DIM * QUBIT_DIM
TOTAL_DIM = ALICE_DIM * BOB_DIM
TOL = 1.0e-9
GU_CHSH_EPSILON = 1.0e-6


class PendingGUInput(RuntimeError):
    """Raised when the GU-derived state/observable data has not been supplied."""


@dataclass(frozen=True)
class DensityCandidate:
    name: str
    matrix: Matrix
    role: str
    provenance: str


@dataclass(frozen=True)
class Observable:
    name: str
    party: str
    matrix: Matrix
    provenance: str


@dataclass(frozen=True)
class CHSHObservables:
    alice_a: Observable
    alice_ap: Observable
    bob_b: Observable
    bob_bp: Observable


@dataclass(frozen=True)
class CHSHResult:
    label: str
    correlators: Dict[str, float]
    value: float


def zeros(rows: int, cols: int) -> Matrix:
    return [[0j for _ in range(cols)] for _ in range(rows)]


def identity(dim: int) -> Matrix:
    out = zeros(dim, dim)
    for i in range(dim):
        out[i][i] = 1.0 + 0j
    return out


def assert_shape(matrix: Matrix, rows: int, cols: int, label: str) -> None:
    assert len(matrix) == rows, f"{label}: expected {rows} rows, got {len(matrix)}"
    for row in matrix:
        assert len(row) == cols, f"{label}: expected {cols} cols, got {len(row)}"


def dagger(matrix: Matrix) -> Matrix:
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[i][j].conjugate() for i in range(rows)] for j in range(cols)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    left_rows = len(left)
    shared = len(left[0])
    assert_shape(right, shared, len(right[0]), "matmul right")
    right_cols = len(right[0])
    out = zeros(left_rows, right_cols)
    for i in range(left_rows):
        out_row = out[i]
        for k in range(shared):
            left_ik = left[i][k]
            if abs(left_ik) <= 0.0:
                continue
            right_row = right[k]
            for j in range(right_cols):
                out_row[j] += left_ik * right_row[j]
    return out


def mat_linear_combination(terms: Iterable[Tuple[complex, Matrix]]) -> Matrix:
    materialized = list(terms)
    assert materialized, "empty linear combination"
    rows = len(materialized[0][1])
    cols = len(materialized[0][1][0])
    out = zeros(rows, cols)
    for scalar, matrix in materialized:
        assert_shape(matrix, rows, cols, "linear-combination term")
        for i in range(rows):
            for j in range(cols):
                out[i][j] += scalar * matrix[i][j]
    return out


def kron(left: Matrix, right: Matrix) -> Matrix:
    left_rows = len(left)
    left_cols = len(left[0])
    right_rows = len(right)
    right_cols = len(right[0])
    out = zeros(left_rows * right_rows, left_cols * right_cols)
    for i in range(left_rows):
        for j in range(left_cols):
            left_ij = left[i][j]
            if abs(left_ij) <= 0.0:
                continue
            for r in range(right_rows):
                out_row = out[i * right_rows + r]
                right_row = right[r]
                for c in range(right_cols):
                    out_row[j * right_cols + c] = left_ij * right_row[c]
    return out


def kron_many(factors: Sequence[Matrix]) -> Matrix:
    assert factors, "kron_many needs at least one factor"
    out = factors[0]
    for factor in factors[1:]:
        out = kron(out, factor)
    return out


def trace(matrix: Matrix) -> complex:
    assert_shape(matrix, len(matrix), len(matrix), "trace matrix")
    return sum(matrix[i][i] for i in range(len(matrix)))


def max_abs_entry(matrix: Matrix) -> float:
    return max(abs(value) for row in matrix for value in row)


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    assert_shape(left, len(right), len(right[0]), "diff left")
    return max(abs(left[i][j] - right[i][j]) for i in range(len(left)) for j in range(len(left[0])))


def assert_matrix_close(left: Matrix, right: Matrix, label: str, tol: float = TOL) -> None:
    diff = max_abs_diff(left, right)
    assert diff <= tol, f"{label}: max matrix difference {diff:.3e} exceeds {tol:.3e}"


def assert_hermitian(matrix: Matrix, label: str, tol: float = TOL) -> None:
    assert_shape(matrix, len(matrix), len(matrix), label)
    assert_matrix_close(matrix, dagger(matrix), f"{label} Hermitian check", tol)


def assert_psd_hermitian(matrix: Matrix, label: str, tol: float = TOL) -> None:
    """LDL* positive-semidefinite check for Hermitian matrices.

    This is enough for the finite control fixture and avoids pulling in numpy.
    """
    assert_hermitian(matrix, label, tol)
    n = len(matrix)
    lower = zeros(n, n)
    diagonal = [0.0 for _ in range(n)]
    for i in range(n):
        lower[i][i] = 1.0 + 0j

    for k in range(n):
        pivot = matrix[k][k]
        for j in range(k):
            pivot -= lower[k][j] * diagonal[j] * lower[k][j].conjugate()
        assert abs(pivot.imag) <= 100.0 * tol, f"{label}: non-real LDL pivot at {k}: {pivot}"
        pivot_real = pivot.real
        assert pivot_real >= -100.0 * tol, f"{label}: negative LDL pivot at {k}: {pivot_real:.3e}"

        if pivot_real <= tol:
            diagonal[k] = 0.0
            for i in range(k + 1, n):
                residual = matrix[i][k]
                for j in range(k):
                    residual -= lower[i][j] * diagonal[j] * lower[k][j].conjugate()
                assert abs(residual) <= 1000.0 * tol, (
                    f"{label}: zero pivot at {k} has nonzero residual row entry "
                    f"{i}: {residual}"
                )
            continue

        diagonal[k] = pivot_real
        for i in range(k + 1, n):
            value = matrix[i][k]
            for j in range(k):
                value -= lower[i][j] * diagonal[j] * lower[k][j].conjugate()
            lower[i][k] = value / pivot_real


def assert_density_candidate(candidate: DensityCandidate) -> None:
    rho = candidate.matrix
    assert_shape(rho, TOTAL_DIM, TOTAL_DIM, candidate.name)
    assert_hermitian(rho, candidate.name)
    tr = trace(rho)
    assert abs(tr.imag) <= TOL, f"{candidate.name}: trace has imaginary part {tr.imag:.3e}"
    assert abs(tr.real - 1.0) <= TOL, f"{candidate.name}: trace {tr.real:.12f} != 1"
    assert_psd_hermitian(rho, candidate.name)


def vector_projector(vector: Vector) -> Matrix:
    norm_squared = sum(abs(value) ** 2 for value in vector)
    assert abs(norm_squared - 1.0) <= TOL, f"state vector norm^2 {norm_squared:.12f} != 1"
    dim = len(vector)
    out = zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            out[i][j] = vector[i] * vector[j].conjugate()
    return out


def basis_index(color_a: int, qubit_a: int, color_b: int, qubit_b: int) -> int:
    assert 0 <= color_a < COLOR_DIM
    assert 0 <= qubit_a < QUBIT_DIM
    assert 0 <= color_b < COLOR_DIM
    assert 0 <= qubit_b < QUBIT_DIM
    return (((color_a * QUBIT_DIM + qubit_a) * COLOR_DIM + color_b) * QUBIT_DIM + qubit_b)


def pauli_x() -> Matrix:
    return [
        [0j, 1.0 + 0j],
        [1.0 + 0j, 0j],
    ]


def pauli_z() -> Matrix:
    return [
        [1.0 + 0j, 0j],
        [0j, -1.0 + 0j],
    ]


def qubit_direction(z_weight: float, x_weight: float) -> Matrix:
    norm = math.sqrt(z_weight * z_weight + x_weight * x_weight)
    assert norm > 0.0, "qubit direction cannot be zero"
    return mat_linear_combination(
        [
            (z_weight / norm, pauli_z()),
            (x_weight / norm, pauli_x()),
        ]
    )


def embed_alice_su2(qubit_operator: Matrix) -> Matrix:
    return kron_many([identity(COLOR_DIM), qubit_operator, identity(COLOR_DIM), identity(QUBIT_DIM)])


def embed_bob_su2(qubit_operator: Matrix) -> Matrix:
    return kron_many([identity(COLOR_DIM), identity(QUBIT_DIM), identity(COLOR_DIM), qubit_operator])


def assert_observable(observable: Observable, require_gu_provenance: bool = False) -> None:
    assert observable.party in ("Alice", "Bob"), f"{observable.name}: unknown party {observable.party}"
    assert_shape(observable.matrix, TOTAL_DIM, TOTAL_DIM, observable.name)
    assert_hermitian(observable.matrix, observable.name)
    squared = matmul(observable.matrix, observable.matrix)
    assert_matrix_close(squared, identity(TOTAL_DIM), f"{observable.name} +/-1 spectrum check")
    if require_gu_provenance:
        assert observable.provenance.startswith("gu-admissible:"), (
            f"{observable.name}: GU gate requires gu-admissible provenance, "
            f"got {observable.provenance!r}"
        )


def assert_chsh_observable_set(observables: CHSHObservables, require_gu_provenance: bool = False) -> None:
    for observable in (
        observables.alice_a,
        observables.alice_ap,
        observables.bob_b,
        observables.bob_bp,
    ):
        assert_observable(observable, require_gu_provenance=require_gu_provenance)

    assert observables.alice_a.party == "Alice"
    assert observables.alice_ap.party == "Alice"
    assert observables.bob_b.party == "Bob"
    assert observables.bob_bp.party == "Bob"

    for alice in (observables.alice_a, observables.alice_ap):
        for bob in (observables.bob_b, observables.bob_bp):
            commutator = mat_linear_combination(
                [
                    (1.0, matmul(alice.matrix, bob.matrix)),
                    (-1.0, matmul(bob.matrix, alice.matrix)),
                ]
            )
            assert max_abs_entry(commutator) <= TOL, (
                f"{alice.name} and {bob.name} fail Alice/Bob local-commutation check"
            )


def control_observables() -> CHSHObservables:
    z = qubit_direction(1.0, 0.0)
    x = qubit_direction(0.0, 1.0)
    z_plus_x = qubit_direction(1.0, 1.0)
    z_minus_x = qubit_direction(1.0, -1.0)
    provenance = "control:pati-salam-proxy-su2-factor"
    return CHSHObservables(
        alice_a=Observable("A = Z on SU(2)_L", "Alice", embed_alice_su2(z), provenance),
        alice_ap=Observable("A' = X on SU(2)_L", "Alice", embed_alice_su2(x), provenance),
        bob_b=Observable("B = (Z+X)/sqrt(2) on SU(2)_R", "Bob", embed_bob_su2(z_plus_x), provenance),
        bob_bp=Observable("B' = (Z-X)/sqrt(2) on SU(2)_R", "Bob", embed_bob_su2(z_minus_x), provenance),
    )


def maximally_entangled_control_state() -> DensityCandidate:
    vector = [0j for _ in range(TOTAL_DIM)]
    amplitude = 1.0 / math.sqrt(ALICE_DIM)
    for color in range(COLOR_DIM):
        for qubit in range(QUBIT_DIM):
            vector[basis_index(color, qubit, color, qubit)] = amplitude + 0j
    return DensityCandidate(
        name="rho_control_phi_8",
        matrix=vector_projector(vector),
        role="control",
        provenance="control:maximally-entangled-on-C4xC2-proxy",
    )


def product_control_state() -> DensityCandidate:
    vector = [0j for _ in range(TOTAL_DIM)]
    vector[basis_index(0, 0, 0, 0)] = 1.0 + 0j
    return DensityCandidate(
        name="rho_control_product_00",
        matrix=vector_projector(vector),
        role="control",
        provenance="control:product-state-on-C4xC2-proxy",
    )


def expectation_value(rho: Matrix, operator: Matrix) -> float:
    assert_shape(rho, TOTAL_DIM, TOTAL_DIM, "rho")
    assert_shape(operator, TOTAL_DIM, TOTAL_DIM, "operator")
    total = 0j
    for i in range(TOTAL_DIM):
        for j in range(TOTAL_DIM):
            total += rho[i][j] * operator[j][i]
    assert abs(total.imag) <= 100.0 * TOL, f"expectation has imaginary part {total.imag:.3e}"
    return total.real


def chsh_correlators(rho: Matrix, observables: CHSHObservables) -> Dict[str, float]:
    return {
        "E(a,b)": expectation_value(rho, matmul(observables.alice_a.matrix, observables.bob_b.matrix)),
        "E(a,b')": expectation_value(rho, matmul(observables.alice_a.matrix, observables.bob_bp.matrix)),
        "E(a',b)": expectation_value(rho, matmul(observables.alice_ap.matrix, observables.bob_b.matrix)),
        "E(a',b')": expectation_value(rho, matmul(observables.alice_ap.matrix, observables.bob_bp.matrix)),
    }


def chsh_value(candidate: DensityCandidate, observables: CHSHObservables) -> CHSHResult:
    correlators = chsh_correlators(candidate.matrix, observables)
    value = correlators["E(a,b)"] + correlators["E(a,b')"] + correlators["E(a',b)"] - correlators["E(a',b')"]
    return CHSHResult(candidate.name, correlators, value)


def assert_close(value: float, expected: float, label: str, tol: float = TOL) -> None:
    assert abs(value - expected) <= tol, (
        f"{label}: expected {expected:.12f}, got {value:.12f}, "
        f"diff={abs(value - expected):.3e}"
    )


def run_control_fixture() -> Tuple[CHSHResult, CHSHResult]:
    observables = control_observables()
    assert_chsh_observable_set(observables)

    bell = maximally_entangled_control_state()
    product = product_control_state()
    assert_density_candidate(bell)
    assert_density_candidate(product)

    bell_result = chsh_value(bell, observables)
    product_result = chsh_value(product, observables)

    assert_close(bell_result.value, 2.0 * math.sqrt(2.0), "maximally entangled control CHSH")
    assert abs(product_result.value) <= 2.0 + TOL, (
        f"product control violates Bell bound: CHSH={product_result.value:.12f}"
    )
    assert_close(product_result.value, math.sqrt(2.0), "product control CHSH")
    return bell_result, product_result


def supply_gu_derived_rho_ab() -> DensityCandidate:
    """Future-work hook: return the GU-derived Alice/Bob density matrix.

    The returned candidate must be produced from GU zero modes, a GU two-point
    function, or another auditable GU construction.  Do not return
    maximally_entangled_control_state() here.
    """
    raise PendingGUInput(
        "No GU-derived rho_AB has been supplied. Expected provenance: "
        "gu-derived:<zero-mode-or-two-point-construction>."
    )


def supply_gu_admissible_observables() -> CHSHObservables:
    """Future-work hook: return GU-admissible CHSH observables.

    The observables must be justified by the GU measurement postulate.  If they
    are Pauli-like SU(2)_L/SU(2)_R operators, their provenance still needs to be
    GU-admissible rather than control-only.
    """
    raise PendingGUInput(
        "No GU-admissible observables have been supplied. Expected provenance: "
        "gu-admissible:<measurement-postulate-reference>."
    )


def reject_control_state_as_gu(candidate: DensityCandidate) -> None:
    assert candidate.role == "gu_derived", (
        f"GU gate requires role='gu_derived', got {candidate.role!r}"
    )
    assert candidate.provenance.startswith("gu-derived:"), (
        f"GU gate requires gu-derived provenance, got {candidate.provenance!r}"
    )
    assert "control:" not in candidate.provenance.lower(), (
        f"control provenance cannot be used as GU proof: {candidate.provenance!r}"
    )

    for forbidden in (maximally_entangled_control_state(), product_control_state()):
        diff = max_abs_diff(candidate.matrix, forbidden.matrix)
        assert diff > TOL, (
            f"{candidate.name} exactly matches forbidden control state "
            f"{forbidden.name}; a Bell/product control is not a GU derivation"
        )


def evaluate_gu_candidate(candidate: DensityCandidate, observables: CHSHObservables) -> CHSHResult:
    reject_control_state_as_gu(candidate)
    assert_density_candidate(candidate)
    assert_chsh_observable_set(observables, require_gu_provenance=True)
    result = chsh_value(candidate, observables)
    assert result.value > 2.0 + GU_CHSH_EPSILON, (
        f"GU-derived candidate did not clear CHSH gate: "
        f"{result.value:.12f} <= {2.0 + GU_CHSH_EPSILON:.12f}"
    )
    return result


def run_supplied_gu_gate(require_gu: bool) -> Tuple[str, str]:
    try:
        candidate = supply_gu_derived_rho_ab()
        observables = supply_gu_admissible_observables()
    except PendingGUInput as exc:
        if require_gu:
            raise AssertionError(f"GU gate required but pending: {exc}")
        return "PENDING_GU_INPUT", str(exc)

    result = evaluate_gu_candidate(candidate, observables)
    return "GU_CHSH_PASS", f"CHSH={result.value:.12f}"


def print_result(result: CHSHResult) -> None:
    print(f"{result.label}:")
    for key in ("E(a,b)", "E(a,b')", "E(a',b)", "E(a',b')"):
        print(f"  {key:8s} = {result.correlators[key]: .12f}")
    print(f"  CHSH     = {result.value: .12f}")


def main(argv: Sequence[str]) -> int:
    if "--help" in argv or "-h" in argv:
        print("usage: python tests/h3_pati_salam_chsh_correlator.py [--require-gu]")
        return 0

    require_gu = "--require-gu" in argv
    unknown = [arg for arg in argv if arg != "--require-gu"]
    assert not unknown, f"unknown argument(s): {unknown}"

    print("=" * 72)
    print("Pati-Salam proxy CHSH correlator fixture")
    print("=" * 72)
    print(f"H_A = C^{COLOR_DIM} tensor C^{QUBIT_DIM}_L, H_B = C^{COLOR_DIM} tensor C^{QUBIT_DIM}_R")
    print(f"Total finite Hilbert dimension: {TOTAL_DIM}")
    print()

    bell_result, product_result = run_control_fixture()
    print("Control states:")
    print_result(bell_result)
    print_result(product_result)
    print()
    print("Assertions:")
    print(f"  maximally entangled control reaches 2*sqrt(2) = {2.0 * math.sqrt(2.0):.12f}")
    print("  product control stays within |CHSH| <= 2")
    print("  density matrices are Hermitian, PSD, trace one")
    print("  observables are Hermitian +/-1 operators and Alice/Bob commute locally")
    print()

    gu_status, gu_message = run_supplied_gu_gate(require_gu=require_gu)
    print(f"GU-derived gate: {gu_status}")
    print(f"  {gu_message}")
    print()
    print("=" * 72)
    print("PASS: controls executable; GU-derived rho_AB remains explicit/pending")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except AssertionError as exc:
        print("=" * 72)
        print(f"FAIL: {exc}")
        print("=" * 72)
        sys.exit(1)
