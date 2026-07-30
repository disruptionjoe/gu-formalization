#!/usr/bin/env python3
"""N2a: native C14, odd-kernel, and actual-Sym2 four-representative screen.

This is a deterministic finite algebraic probe against the N1 construction
hash.  It does not vary the action, identify a physical mass, classify all
Lorentzian Sym2 orbits, or transfer a result between the K-sesquilinear and
C-complex branches.

The actual symmetric-metric fibre is used.  A tangent tensor h enters Clifford
multiplication through the trace-reversed DeWitt musical

    alpha_h(k) = G_DW(h,k),

not through a Frobenius identification.  Grassmann survival is decided only
for planted total kernels; the packet's total P0 x rho(Phi) x Y_C kernel is not
supplied and therefore remains typed unresolved.
"""
from __future__ import annotations

from itertools import combinations, product
import os
import subprocess
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.normpath(os.path.join(HERE, ".."))
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as b5  # noqa: E402


TOL = 1.0e-8
FROZEN_HASH = "1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb"
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def native_gammas() -> tuple[list[np.ndarray], np.ndarray]:
    """The repo's exact signed-Jordan--Wigner 128x128 Cl(9,5) basis."""
    euclidean = cl95.jordan_wigner_gammas(7)
    metric = np.array([1.0] * 9 + [-1.0] * 5)
    gammas = [
        euclidean[index] if metric[index] > 0 else 1j * euclidean[index]
        for index in range(14)
    ]
    return gammas, metric


def clifford_defect(gammas: list[np.ndarray], metric: np.ndarray) -> float:
    identity = np.eye(gammas[0].shape[0], dtype=complex)
    return max(
        max_abs(
            gammas[left] @ gammas[right]
            + gammas[right] @ gammas[left]
            - (
                2.0 * metric[left] * identity
                if left == right
                else np.zeros_like(identity)
            )
        )
        for left in range(len(gammas))
        for right in range(len(gammas))
    )


def spin_generator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return 0.25 * (left @ right - right @ left)


def sym2_components(h: np.ndarray) -> np.ndarray:
    return np.array([h[i, j] for i in range(4) for j in range(i, 4)])


def sym2_from_components(components: np.ndarray) -> np.ndarray:
    out = np.zeros((4, 4), dtype=float)
    cursor = 0
    for i in range(4):
        for j in range(i, 4):
            out[i, j] = out[j, i] = float(components[cursor])
            cursor += 1
    return out


ETA4 = np.diag([1.0, 1.0, 1.0, -1.0])


def dewitt(h: np.ndarray, k: np.ndarray) -> float:
    """DeWitt form with the N1 trace reversal in four dimensions."""
    ah = ETA4 @ h
    ak = ETA4 @ k
    return float(np.trace(ah @ ak) - 0.5 * np.trace(ah) * np.trace(ak))


def make_dewitt_frame() -> tuple[list[np.ndarray], np.ndarray]:
    diagonal_a = [
        np.array([1.0, -1.0, 0.0, 0.0]) / np.sqrt(2.0),
        np.array([1.0, 1.0, -2.0, 0.0]) / np.sqrt(6.0),
        np.array([1.0, 1.0, 1.0, -3.0]) / np.sqrt(12.0),
    ]
    frame = [np.diag(np.diag(ETA4) * vector) for vector in diagonal_a]
    for i, j in ((0, 1), (0, 2), (1, 2)):
        h = np.zeros((4, 4))
        h[i, j] = h[j, i] = 1.0 / np.sqrt(2.0)
        frame.append(h)
    frame.append(ETA4 / 2.0)
    for i in range(3):
        h = np.zeros((4, 4))
        h[i, 3] = h[3, i] = 1.0 / np.sqrt(2.0)
        frame.append(h)
    return frame, np.array([1.0] * 6 + [-1.0] * 4)


DEWITT_FRAME, ETA10 = make_dewitt_frame()
FRAME_MATRIX = np.column_stack([sym2_components(h) for h in DEWITT_FRAME])


def vector_coordinates(h: np.ndarray) -> np.ndarray:
    return np.linalg.solve(FRAME_MATRIX, sym2_components(h))


def dewitt_musical(h: np.ndarray) -> np.ndarray:
    """Covector coefficients alpha_i=G_DW(h,f_i) in the dual frame."""
    return np.array([dewitt(h, frame) for frame in DEWITT_FRAME])


def trace_reversed_frobenius_matrix(h: np.ndarray) -> np.ndarray:
    """q with alpha_h(k)=tr(q^T k), displayed to expose trace reversal."""
    return ETA4 @ h @ ETA4 - 0.5 * np.trace(ETA4 @ h) * ETA4


def gamma_of_covector(alpha: np.ndarray, vertical_gammas: list[np.ndarray]) -> np.ndarray:
    return sum(
        (float(coefficient) * gamma for coefficient, gamma in zip(alpha, vertical_gammas)),
        np.zeros_like(vertical_gammas[0]),
    )


def lorentz_generators(metric: np.ndarray) -> list[np.ndarray]:
    generators = []
    for left, right in combinations(range(len(metric)), 2):
        generator = np.zeros((len(metric), len(metric)))
        generator[left, right] = 1.0
        generator[right, left] = -metric[left] * metric[right]
        generators.append(generator)
    return generators


def induced_sym2_generator(generator4: np.ndarray) -> np.ndarray:
    columns = []
    for frame in DEWITT_FRAME:
        delta = generator4.T @ frame + frame @ generator4
        columns.append(vector_coordinates(delta))
    return np.column_stack(columns)


def lifted_spin_generator(
    generator10: np.ndarray, vertical_gammas: list[np.ndarray]
) -> np.ndarray:
    """Spin lift for J_ab with (J_ab)_ab=1 in an orthonormal signed frame."""
    out = np.zeros_like(vertical_gammas[0])
    for left, right in combinations(range(10), 2):
        out += (
            generator10[left, right]
            * ETA10[left]
            * spin_generator(vertical_gammas[left], vertical_gammas[right])
        )
    return out


def stabilizer_dimension_sym2(h: np.ndarray) -> int:
    columns = [
        sym2_components(generator.T @ h + h @ generator)
        for generator in lorentz_generators(np.diag(ETA4))
    ]
    return 6 - int(np.linalg.matrix_rank(np.column_stack(columns), tol=TOL))


def stabilizer_dimension_vector(vector: np.ndarray) -> int:
    columns = [
        generator @ vector for generator in lorentz_generators(ETA10)
    ]
    return 45 - int(np.linalg.matrix_rank(np.column_stack(columns), tol=TOL))


def heldout_parts(source_name: str, target_name: str) -> tuple[int, int]:
    source = b5.TYPES[b5.SLOT_BY_NAME[source_name].h_type]
    target = b5.TYPES[b5.SLOT_BY_NAME[target_name].h_type]
    base = int(
        source.d5_weight == target.d5_weight
        and target.left_dim in b5.su2_vector_targets(source.left_dim)
        and target.right_dim in b5.su2_vector_targets(source.right_dim)
    )
    fibre = int(
        source.left_dim == target.left_dim
        and source.right_dim == target.right_dim
    ) * b5.vector_tensor_decomposition(source.d5_weight).get(
        target.d5_weight, 0
    )
    return base, fibre


def static_phase_matcher(
    phases: dict[str, int], cells: set[tuple[str, str]]
) -> bool:
    if set(phases) != set(b5.SLOT_BY_NAME):
        return False
    if any(phases[slot.name] != phases[slot.mirror] for slot in b5.SLOTS):
        return False
    for source, target in cells:
        mirror = (
            b5.SLOT_BY_NAME[source].mirror,
            b5.SLOT_BY_NAME[target].mirror,
        )
        if mirror not in cells:
            return False
        if phases[target] / phases[source] != phases[mirror[1]] / phases[mirror[0]]:
            return False
    return True


def main() -> None:
    print("=" * 96)
    print("N2a ACTUAL-SYM2 / C14 / ODD-KERNEL FOUR-REPRESENTATIVE SCREEN")
    print("=" * 96)

    hash_probe = os.path.join(HERE, "unified_source_datum_packet_v0_probe.py")
    observed_hash = subprocess.run(
        [sys.executable, hash_probe, "--emit-hash"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    check(
        "frozen N1 executable construction hash matches",
        observed_hash == FROZEN_HASH,
        observed_hash,
    )

    native, native_metric = native_gammas()
    identity128 = np.eye(128, dtype=complex)
    check(
        "native signed-JW matrices are exact Cl(9,5) on C^128",
        clifford_defect(native, native_metric) < TOL,
    )

    # Reorder only the vector labels: (3,1) base followed by actual (6,4) fibre.
    split_order = [0, 1, 2, 9, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
    gamma14 = [native[index] for index in split_order]
    eta14 = native_metric[split_order]
    base_gammas = gamma14[:4]
    vertical_gammas = gamma14[4:]
    check(
        "split labels have (3,1)+(6,4) signature without changing the native basis",
        np.array_equal(eta14[:4], np.array([1.0, 1.0, 1.0, -1.0]))
        and np.array_equal(eta14[4:], ETA10),
    )

    transpose_signs = []
    for gamma in native:
        if max_abs(gamma.T - gamma) < TOL:
            transpose_signs.append(1)
        elif max_abs(gamma.T + gamma) < TOL:
            transpose_signs.append(-1)
        else:
            transpose_signs.append(0)
    symmetric_indices = [i for i, sign in enumerate(transpose_signs) if sign == 1]
    skew_indices = [i for i, sign in enumerate(transpose_signs) if sign == -1]
    check(
        "JW basis exposes seven transpose-symmetric and seven transpose-skew gammas",
        len(symmetric_indices) == len(skew_indices) == 7
        and 0 not in transpose_signs,
        f"sym={symmetric_indices}, skew={skew_indices}",
    )

    product_skew = matrix_product([native[i] for i in skew_indices])
    product_symmetric = matrix_product([native[i] for i in symmetric_indices])
    c_branches = {
        "C_-": (np.linalg.inv(product_skew), -1, 1),
        "C_+": (np.linalg.inv(product_symmetric), 1, -1),
    }
    for name, (charge, epsilon, tau) in c_branches.items():
        relation = max(
            max_abs(
                charge @ gamma @ np.linalg.inv(charge)
                - epsilon * gamma.T
            )
            for gamma in native
        )
        check(
            f"{name} solves C gamma C^-1=epsilon gamma^T and C^T=tau C",
            relation < TOL and max_abs(charge.T - tau * charge) < TOL,
            f"(epsilon,tau)=({epsilon:+d},{tau:+d})",
        )

    krein = matrix_product([native[i] for i in range(9)])
    spin14 = [
        spin_generator(native[left], native[right])
        for left, right in combinations(range(14), 2)
    ]
    check(
        "native K is Hermitian and Spin(9,5)-invariant",
        max_abs(krein.conj().T - krein) < TOL
        and max(
            max_abs(generator.conj().T @ krein + krein @ generator)
            for generator in spin14
        )
        < TOL,
    )

    gram = np.array(
        [[dewitt(left, right) for right in DEWITT_FRAME] for left in DEWITT_FRAME]
    )
    check(
        "actual Sym2 frame is DeWitt-orthonormal with signature (6,4)",
        max_abs(gram - np.diag(ETA10)) < TOL,
    )

    h_space = DEWITT_FRAME[0]
    h_trace = -ETA4 / 4.0  # G_DW(h_trace,k)=tau_g(k)=tr_g(k)/4.
    h_null = h_space + 2.0 * h_trace
    representatives = {
        "zero": np.zeros((4, 4)),
        "trace": h_trace,
        "spacelike_traceless": h_space,
        "null": h_null,
    }
    expected_rank = {
        "zero": 0,
        "trace": 128,
        "spacelike_traceless": 128,
        "null": 64,
    }
    expected_lorentz_stabilizer = {
        "zero": 6,
        "trace": 6,
        "spacelike_traceless": 1,
        "null": 1,
    }
    expected_frame_stabilizer = {
        "zero": 45,
        "trace": 36,
        "spacelike_traceless": 36,
        "null": 36,
    }

    trace_functional_test = np.array(
        [[0.3, 0.1, 0.0, 0.2], [0.1, -0.4, 0.3, 0.0],
         [0.0, 0.3, 0.8, -0.2], [0.2, 0.0, -0.2, 0.5]]
    )
    check(
        "chosen trace vector is the DeWitt dual of tau_g=tr_g/4",
        abs(
            dewitt(h_trace, trace_functional_test)
            - 0.25 * np.trace(ETA4 @ trace_functional_test)
        )
        < TOL,
    )

    orbit_rows: dict[str, dict[str, object]] = {}
    for name, h in representatives.items():
        alpha = dewitt_musical(h)
        vector = vector_coordinates(h)
        insertion = gamma_of_covector(alpha, vertical_gammas)
        norm = dewitt(h, h)
        trace = float(np.trace(ETA4 @ h))
        rank = int(np.linalg.matrix_rank(insertion, tol=TOL))
        square_defect = max_abs(insertion @ insertion - norm * identity128)
        lorentz_stabilizer = stabilizer_dimension_sym2(h)
        frame_stabilizer = stabilizer_dimension_vector(vector)
        orbit_rows[name] = {
            "trace": trace,
            "norm": norm,
            "rank": rank,
            "lorentz_stabilizer": lorentz_stabilizer,
            "frame_stabilizer": frame_stabilizer,
        }
        check(
            f"{name}: DeWitt-musical Clifford square and rank",
            square_defect < TOL and rank == expected_rank[name],
            f"tr={trace:+.3g}, G={norm:+.3g}, rank={rank}",
        )
        check(
            f"{name}: Lorentz-on-Sym2 and fibre-frame stabilizer dimensions",
            lorentz_stabilizer == expected_lorentz_stabilizer[name]
            and frame_stabilizer == expected_frame_stabilizer[name],
            f"Lorentz={lorentz_stabilizer}, frame={frame_stabilizer}",
        )
        if name == "null":
            check(
                "nonzero null insertion is rank-64 nilpotent, not zero",
                rank == 64
                and max_abs(insertion @ insertion) < TOL
                and np.linalg.norm(insertion) > 1.0,
            )
        for branch, (charge, _epsilon, _tau) in c_branches.items():
            kernel = charge @ insertion
            check(
                f"{name}/{branch}: bare complex-bilinear spinor kernel is skew",
                max_abs(kernel.T + kernel) < TOL,
            )
        k_kernel = krein @ insertion
        check(
            f"{name}/K: bare sesquilinear kernel is Hermitian",
            max_abs(k_kernel.conj().T - k_kernel) < TOL,
        )

    # DeWitt musical is trace-reversed, not a silent Frobenius identification.
    for name in ("trace", "null"):
        h = representatives[name]
        q = trace_reversed_frobenius_matrix(h)
        planted_k = trace_functional_test
        check(
            f"{name}: trace-reversed matrix represents the DeWitt covector",
            abs(float(np.trace(q.T @ planted_k)) - dewitt(h, planted_k)) < TOL,
        )
        check(
            f"{name}: naive Frobenius h is a hostile wrong-musical comparator",
            abs(float(np.trace(h.T @ planted_k)) - dewitt(h, planted_k)) > 1.0e-3,
        )

    # Covariance of a dynamical h-contracted term is not invariance of fixed h.
    lorentz4 = lorentz_generators(np.diag(ETA4))
    induced10 = [induced_sym2_generator(generator) for generator in lorentz4]
    check(
        "Lorentz action induced on actual Sym2 lies in so(6,4)",
        max(
            max_abs(generator.T @ np.diag(ETA10) + np.diag(ETA10) @ generator)
            for generator in induced10
        )
        < TOL,
    )
    for generator4, generator10 in zip(lorentz4, induced10):
        spin = lifted_spin_generator(generator10, vertical_gammas)
        check(
            "induced spin lift preserves K and both C branches",
            max_abs(spin.conj().T @ krein + krein @ spin) < TOL
            and all(
                max_abs(spin.T @ charge + charge @ spin) < TOL
                for charge, _epsilon, _tau in c_branches.values()
            ),
        )
        for h in representatives.values():
            alpha = dewitt_musical(h)
            delta_h = generator4.T @ h + h @ generator4
            delta_insertion = gamma_of_covector(
                dewitt_musical(delta_h), vertical_gammas
            )
            insertion = gamma_of_covector(alpha, vertical_gammas)
            check(
                "dynamical DeWitt-musical contraction is infinitesimally covariant",
                max_abs(spin @ insertion - insertion @ spin - delta_insertion)
                < TOL,
            )

    # A fixed non-invariant representative omits delta h and therefore breaks
    # the full Lorentz action.  The stabilizer calculation above is the exact
    # fixed-background statement.
    fixed_defects = {}
    for name, h in representatives.items():
        insertion = gamma_of_covector(dewitt_musical(h), vertical_gammas)
        fixed_defects[name] = sum(
            max_abs(
                lifted_spin_generator(generator, vertical_gammas) @ insertion
                - insertion @ lifted_spin_generator(generator, vertical_gammas)
            )
            > 1.0e-6
            for generator in induced10
        )
    check(
        "fixed zero/trace preserve all six Lorentz generators; space/null do not",
        fixed_defects["zero"] == fixed_defects["trace"] == 0
        and fixed_defects["spacelike_traceless"] > 0
        and fixed_defects["null"] > 0,
        str(fixed_defects),
    )

    # Similarity covariance: charge, K, and their contracted kernels transform
    # by the correct congruences in a non-unitary spinor basis.
    scales = np.linspace(0.7, 1.3, 128)
    phases = np.exp(1j * np.linspace(0.0, 0.6, 128))
    similarity = np.diag(scales * phases)
    similarity_inverse = np.diag(1.0 / (scales * phases))
    transformed_gammas = [
        similarity @ gamma @ similarity_inverse for gamma in native
    ]
    sample_alpha = dewitt_musical(h_null)
    sample_insertion = gamma_of_covector(sample_alpha, vertical_gammas)
    transformed_vertical = [
        transformed_gammas[index] for index in split_order[4:]
    ]
    transformed_insertion = gamma_of_covector(sample_alpha, transformed_vertical)
    transformed_krein = (
        similarity_inverse.conj().T @ krein @ similarity_inverse
    )
    check(
        "K-sesquilinear kernel obeys non-unitary similarity congruence",
        max_abs(
            transformed_krein @ transformed_insertion
            - similarity_inverse.conj().T
            @ (krein @ sample_insertion)
            @ similarity_inverse
        )
        < TOL,
    )
    for name, (charge, epsilon, tau) in c_branches.items():
        transformed_charge = (
            similarity_inverse.T @ charge @ similarity_inverse
        )
        check(
            f"{name} and C Gamma obey similarity-covariant congruence",
            max(
                max_abs(
                    transformed_charge
                    @ transformed_gamma
                    @ np.linalg.inv(transformed_charge)
                    - epsilon * transformed_gamma.T
                )
                for transformed_gamma in transformed_gammas
            )
            < TOL
            and max_abs(transformed_charge.T - tau * transformed_charge) < TOL
            and max_abs(
                transformed_charge @ transformed_insertion
                - similarity_inverse.T
                @ (charge @ sample_insertion)
                @ similarity_inverse
            )
            < TOL,
        )

    # Grassmann exchange belongs to the TOTAL kernel.  The bare spinor factor
    # is skew, but a gauge/provenance transpose sign can preserve or reverse it,
    # and a restriction P0 can still annihilate the pulled-back form.
    sample_c = c_branches["C_-"][0] @ gamma_of_covector(
        dewitt_musical(h_space), vertical_gammas
    )
    symmetric_gp = np.diag([2.0, -1.0])
    skew_gp = np.array([[0.0, 1.0], [-1.0, 0.0]])
    total_survives = np.kron(sample_c, symmetric_gp)
    total_cancels = np.kron(sample_c, skew_gp)
    check(
        "planted symmetric gauge/provenance factor leaves total odd kernel skew",
        max_abs(total_survives.T + total_survives) < TOL,
    )
    check(
        "planted skew gauge/provenance factor makes total odd kernel symmetric",
        max_abs(total_cancels.T - total_cancels) < TOL,
    )
    planted_p0 = np.zeros((256, 1), dtype=complex)
    planted_p0[0, 0] = 1.0
    check(
        "planted one-dimensional P0 can annihilate an otherwise surviving skew form",
        max_abs(planted_p0.T @ total_survives @ planted_p0) < TOL,
    )

    # Corrected full-20 support/provenance is a principal-symbol transport
    # ledger.  It is not silently reused as the zero-order c_rho(v) placement.
    all_cells = {
        (source.name, target.name)
        for source in b5.SLOTS
        for target in b5.SLOTS
        if b5.symbol_multiplicity(
            b5.TYPES[source.h_type], b5.TYPES[target.h_type]
        )
    }
    base_cells = {cell for cell in all_cells if heldout_parts(*cell) == (1, 0)}
    fibre_cells = {cell for cell in all_cells if heldout_parts(*cell) == (0, 1)}
    check(
        "corrected full-20 ledger is 20 slots, dimension 1920, 68+68 cells",
        len(b5.SLOTS) == 20
        and sum(slot.dimension for slot in b5.SLOTS) == 1920
        and len(all_cells) == 136
        and len(base_cells) == len(fibre_cells) == 68,
    )

    # The missing normal grading N is visible already on the imGamma/low-R
    # multiplicity plane: pairing-only coflip mixes them; N-corrected is I.
    root14 = np.sqrt(14.0)
    multiplicity_basis = np.array(
        [
            [2.0 / root14, np.sqrt(10.0) / root14],
            [np.sqrt(10.0) / root14, -2.0 / root14],
        ]
    )
    normal_grading = np.diag([1.0, -1.0])
    pairing_only = multiplicity_basis.T @ normal_grading @ multiplicity_basis
    expected_pairing_only = np.array(
        [[-3.0 / 7.0, 2.0 * np.sqrt(10.0) / 7.0],
         [2.0 * np.sqrt(10.0) / 7.0, 3.0 / 7.0]]
    )
    check(
        "hostile missing-N coflip mixes imGamma and low-kerGamma",
        max_abs(pairing_only - expected_pairing_only) < TOL
        and max_abs(pairing_only - np.eye(2)) > 0.5,
    )
    check(
        "normal-grading correction removes that multiplicity mixing",
        max_abs(
            multiplicity_basis.T
            @ normal_grading
            @ normal_grading
            @ multiplicity_basis
            - np.eye(2)
        )
        < TOL,
    )

    mirror_pairs = sorted(
        {tuple(sorted((slot.name, slot.mirror))) for slot in b5.SLOTS}
    )
    twist_phases = {slot.name: 1 for slot in b5.SLOTS}
    for slot_name in mirror_pairs[0]:
        twist_phases[slot_name] = -1
    phase_failures = {
        cell
        for cell in all_cells
        if twist_phases[cell[0]] != twist_phases[cell[1]]
    }
    check(
        "hostile relative mirror-pair phase passes static support/involution",
        static_phase_matcher(twist_phases, all_cells),
        str(mirror_pairs[0]),
    )
    check(
        "the same phase violates 28 actual nonzero coefficient equations",
        len(phase_failures) == 28,
        f"failures={len(phase_failures)}",
    )
    assignments = []
    for signs in product((-1, 1), repeat=len(mirror_pairs)):
        assignment = {
            slot_name: sign
            for sign, pair in zip(signs, mirror_pairs)
            for slot_name in pair
        }
        assignments.append(assignment)
    coefficient_admissible = [
        assignment
        for assignment in assignments
        if all(assignment[source] == assignment[target] for source, target in all_cells)
    ]
    check(
        "136 coefficient equations leave only one phase class up to global sign",
        len(assignments) == 2**10
        and len(coefficient_admissible) == 2
        and all(len(set(assignment.values())) == 1 for assignment in coefficient_admissible),
    )

    # Exterior-ten hostile comparator: central GL(4) weights force every
    # intertwiner Sym2 -> Lambda2+Lambda3 to have rank at most six.
    scalar = 2.0
    sym2_central = scalar**2 * np.eye(10)
    exterior_central = np.diag([scalar**2] * 6 + [scalar**3] * 4)
    coefficient_matrix = np.kron(
        np.eye(10), sym2_central
    ) - np.kron(exterior_central.T, np.eye(10))
    intertwiner_dimension = 100 - int(
        np.linalg.matrix_rank(coefficient_matrix, tol=TOL)
    )
    check(
        "exterior ten is not naturally GL(4)-isomorphic to actual Sym2",
        intertwiner_dimension == 60,
        f"Hom dimension under central test={intertwiner_dimension}, rank<=6",
    )

    # Horizontal comparator: transpose algebra still passes, scalarity does not.
    horizontal = base_gammas[0]
    for name, (charge, _epsilon, _tau) in c_branches.items():
        check(
            f"horizontal hostile comparator also has skew bare {name} gamma kernel",
            max_abs((charge @ horizontal).T + charge @ horizontal) < TOL,
        )
    base_spin = [
        spin_generator(base_gammas[left], base_gammas[right])
        for left, right in combinations(range(4), 2)
    ]
    horizontal_scalar_defect = max(
        max_abs(
            generator.conj().T @ (krein @ horizontal)
            + (krein @ horizontal) @ generator
        )
        for generator in base_spin
    )
    check(
        "horizontal component is not an individual observer-Lorentz scalar",
        horizontal_scalar_defect > 1.0e-6,
    )

    print("\nFour-representative ledger:")
    for name, row in orbit_rows.items():
        print(
            f"  {name:22s} tr={row['trace']:+.3g} G={row['norm']:+.3g} "
            f"rank(c)={row['rank']:3d} "
            f"stab_L={row['lorentz_stabilizer']} "
            f"stab_SO(6,4)={row['frame_stabilizer']}"
        )

    print("\nTyped findings:")
    print("  CONSTRUCTED: C_- (-1,+1) and C_+ (+1,-1) in the native 128 basis.")
    print("  CONSTRUCTED: both bare C Gamma(alpha_h) kernels are transpose-skew.")
    print("  UNRESOLVED: total odd survival without P0, rho(Phi), and Y_C.")
    print("  CONSTRUCTED: K Gamma(alpha_h) is a separate Hermitian branch.")
    print("  UNRESOLVED: any K<->C branch relation R_KC.")
    print("  CONSTRUCTED: fixed Lorentz stabilizers 6,6,1,1 for the four screen reps.")
    print("  UNRESOLVED: nonzero full-gauge stabilizers without Phi and rho.")
    print("  UNRESOLVED: zero-order c_rho(v) placement on the corrected E20 ledger.")
    print("  NOT CLAIMED: mass, stationarity, anomaly, index, count, or exhaustive orbit.")

    if FAILURES:
        print(f"\nCONTROLS FAILED: {FAILURES}")
        raise SystemExit(1)
    print("\nVERDICT: N2a-CONDITIONAL-ALGEBRA-CONSTRUCTED")
    print("VERDICT: TOTAL-ODD-KERNEL-AND-NONZERO-GAUGE-STABILIZER-TYPED-UNRESOLVED")
    print(f"FROZEN HASH: {FROZEN_HASH}")
    print("ALL CONTROLS PASSED")


if __name__ == "__main__":
    main()
