#!/usr/bin/env python3
r"""RB3b: trace-reversed native four-component vertex and full-20 witness.

This is a finite, deterministic construction probe.  It starts with the
actual

    Sym^2(T*X),       G_DW(h,k)
      = tr(g^-1 h g^-1 k) - 1/2 tr(g^-1 h) tr(g^-1 k),

whose orthonormal fibre has signature (6,4).  The normalized negative trace
gamma is called ``t``.  The trace line is canonical, but the displayed
maximal-compact split A=R^6, W=R^4 is not: induced base-Lorentz boosts mix
the six-plane with the three non-trace negative directions.  Conditional on
a moving observer/Cartan reduction selecting that split, it constructs

    Phi_t^lambda(w)
      = P_{ {-,t} }(vol_W c(w) + lambda vol_A c(w)),

for lambda=-1,+1, with lambda=2 planted as the non-isotropic control.  The
native defining representation is then the literal inclusion

    rho_S(Phi) = Phi,

and the zero-order operator is

    A_S = c(hat_tau) rho_S(Phi).

Layer 0 is explicit.  "Base scalar" means invariant under the proper base
Spin(3,1) action.  There are two such native Clifford copies: exterior base
degree zero and its base-volume (pseudoscalar) companion.  No parity or CP
condition supplied by the source selects between them.  The factorized
Cl(9,5) representation contributes an omega_4 factor to every odd internal
word; omitting that factor is a non-native phase error.

The probe also:

* distinguishes the actual DeWitt musical, norm, signature, and Hodge square
  from the raw Frobenius plant;
* verifies the analytic 4096-real raw End_C comparator, then the actual
  992-real native base-scalar and 512-real {Phi,c(t)}=0 parameter spaces;
* checks right-H linearity, Krein skewness of Phi, Krein self-adjointness of
  A_S, the two invariant C_+ / C_- transpose branches, and the cross-base-
  chirality Krein bilinear;
* applies the canonical diagonal lift on S plus (V tensor S), resolves it
  through the written P_I/P_R maps, and checks one finite witness in every
  one of the existing twenty thin summands;
* computes the complete deterministic thin-slot block support of every
  component, including its P0 support ceilings, and tests the corrected
  Gamma-natural coflip on the full associated lift.

NONCLAIMS: the four-component image is only a native conditional candidate.
The DeWitt metric alone does not select its maximal-compact/observer split;
that reduction must be dynamically constructed, identified with an existing
datum by an explicit map, or charged separately.
For fixed t, the image closes under only the Spin(3) stabilizer tested below,
not the three Spin(4) generators that move t.  The unnormalized defining-trace
Gram is not an action normalization or a cosmological coefficient.
This file does not construct or select G_SM, identify a Pati--Salam or
Standard-Model Higgs, choose a VEV, derive a mass, prove stationarity, compute
an index/generation count, or derive a cosmological prediction.
"""

from __future__ import annotations

import contextlib
from itertools import combinations
from math import comb
import io
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
TESTS_ROOT = os.path.abspath(os.path.join(HERE, ".."))
if TESTS_ROOT not in sys.path:
    sys.path.insert(0, TESTS_ROOT)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# This existing executable module owns the signed factorized Cl(9,5),
# Gamma/j/P_R, and twenty normalized slot embeddings.  Its top-level receipt
# is intentionally suppressed here; its failure ledger is checked below.
with contextlib.redirect_stdout(io.StringIO()):
    import full20_dewitt_loop_transport_probe as full20  # noqa: E402


TOL = 2.0e-8
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def signature(matrix: np.ndarray) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    scale = max(1.0, float(np.max(np.abs(values))))
    threshold = TOL * scale
    return (
        int(np.sum(values > threshold)),
        int(np.sum(values < -threshold)),
        int(np.sum(np.abs(values) <= threshold)),
    )


def permutation_sign(indices: tuple[int, ...]) -> int:
    inversions = sum(
        indices[left] > indices[right]
        for left in range(len(indices))
        for right in range(left + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


def hodge_matrix(metric: np.ndarray, degree: int) -> np.ndarray:
    """Hodge star from degree k to n-k in an oriented signed ON frame."""
    dimension = len(metric)
    source = list(combinations(range(dimension), degree))
    target = list(combinations(range(dimension), dimension - degree))
    target_index = {multi_index: index for index, multi_index in enumerate(target)}
    out = np.zeros((len(target), len(source)))
    full_set = set(range(dimension))
    for column, multi_index in enumerate(source):
        complement = tuple(sorted(full_set.difference(multi_index)))
        wedge_sign = permutation_sign(multi_index + complement)
        metric_sign = float(np.prod(metric[list(multi_index)]))
        out[target_index[complement], column] = wedge_sign * metric_sign
    return out


def raw_frobenius_metric(metric: np.ndarray) -> np.ndarray:
    """The no-trace-reversal comparator on the actual Sym^2 coordinate basis."""
    inverse = np.linalg.inv(metric)
    actions = [inverse @ basis for basis in full20.SYMMETRIC_BASIS]
    return np.array(
        [
            [float(np.trace(left @ right)) for right in actions]
            for left in actions
        ]
    )


def dewitt_pair(h: np.ndarray, k: np.ndarray) -> float:
    inverse = np.linalg.inv(full20.ETA4_MATRIX)
    left = inverse @ h
    right = inverse @ k
    return float(
        np.trace(left @ right)
        - 0.5 * np.trace(left) * np.trace(right)
    )


def raw_frobenius_pair(h: np.ndarray, k: np.ndarray) -> float:
    inverse = np.linalg.inv(full20.ETA4_MATRIX)
    return float(np.trace((inverse @ h) @ (inverse @ k)))


def krein_adjoint(matrix: np.ndarray) -> np.ndarray:
    return full20.krein @ matrix.conj().T @ full20.krein


def right_h_defect(matrix: np.ndarray, j_h: np.ndarray) -> float:
    return max_abs(matrix @ j_h - j_h @ matrix.conj())


def spin_generator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return 0.25 * (left @ right - right @ left)


def induced_lorentz_on_dewitt(generator: np.ndarray) -> np.ndarray:
    """Infinitesimal Sym2 action in the chosen DeWitt orthonormal frame."""
    columns = []
    for index in range(10):
        tensor = full20.symmetric_matrix(full20.DEWITT_FRAME[:, index])
        delta = generator.T @ tensor + tensor @ generator
        components = full20.symmetric_components(delta)
        columns.append(np.linalg.solve(full20.DEWITT_FRAME, components))
    return np.column_stack(columns)


def induced_change_on_dewitt(change: np.ndarray) -> np.ndarray:
    """Finite Sym2 action in the chosen DeWitt orthonormal frame."""
    columns = []
    for index in range(10):
        tensor = full20.symmetric_matrix(full20.DEWITT_FRAME[:, index])
        moved = change.T @ tensor @ change
        components = full20.symmetric_components(moved)
        columns.append(np.linalg.solve(full20.DEWITT_FRAME, components))
    return np.column_stack(columns)


def anticommuting_projection(matrix: np.ndarray, t_gamma: np.ndarray) -> np.ndarray:
    """Projection to X t + t X = 0 using Ad_t's +/- eigenspaces."""
    return 0.5 * (
        matrix - t_gamma @ matrix @ np.linalg.inv(t_gamma)
    )


def normalized_hilbert_schmidt_gram(
    matrices: list[np.ndarray],
) -> np.ndarray:
    dimension = matrices[0].shape[0]
    return np.array(
        [
            [
                complex(np.trace(left.conj().T @ right) / dimension)
                for right in matrices
            ]
            for left in matrices
        ]
    )


def defining_real_trace_gram(matrices: list[np.ndarray]) -> np.ndarray:
    return np.array(
        [
            [
                float(np.trace(left @ right).real)
                for right in matrices
            ]
            for left in matrices
        ]
    )


def hilbert_schmidt_gram(matrices: list[np.ndarray]) -> np.ndarray:
    return np.array(
        [
            [
                float(np.trace(left.conj().T @ right).real)
                for right in matrices
            ]
            for left in matrices
        ]
    )


def span_projector(matrices: list[np.ndarray]) -> np.ndarray:
    columns = np.column_stack([matrix.reshape(-1) for matrix in matrices])
    q_basis, _r = np.linalg.qr(columns)
    return q_basis @ q_basis.conj().T


def commutator_span_leakages(
    matrices: list[np.ndarray], generators: list[np.ndarray]
) -> list[float]:
    """Largest raw Frobenius leakage per generator outside span(matrices)."""
    columns = np.column_stack([matrix.reshape(-1) for matrix in matrices])
    q_basis, _r = np.linalg.qr(columns, mode="reduced")
    leakages = []
    for generator in generators:
        generator_leakage = 0.0
        for matrix in matrices:
            commutator = generator @ matrix - matrix @ generator
            vector = commutator.reshape(-1)
            residual = vector - q_basis @ (q_basis.conj().T @ vector)
            generator_leakage = max(
                generator_leakage, float(np.linalg.norm(residual))
            )
        leakages.append(generator_leakage)
    return leakages


def apply_associated_lift(
    operator: np.ndarray, carrier: str, vectors: np.ndarray
) -> np.ndarray:
    """diag(A, 1_V tensor A) without materializing a 1920-square matrix."""
    if carrier == "S":
        return operator @ vectors
    reshaped = vectors.reshape(14, 128, -1)
    out = np.empty_like(reshaped)
    for vector_index in range(14):
        out[vector_index] = operator @ reshaped[vector_index]
    return out.reshape(14 * 128, -1)


def slot_witness(slot: full20.SlotBasis) -> np.ndarray:
    """A deterministic non-coordinate witness in each normalized thin slot."""
    count = min(3, slot.dimension)
    coefficients = np.arange(1, count + 1, dtype=float)
    coefficients /= np.linalg.norm(coefficients)
    return slot.basis[:, :count] @ coefficients[:, None]


def reconstruct_from_slots(
    carrier: str, vectors: np.ndarray
) -> tuple[np.ndarray, dict[str, float]]:
    targets = [slot for slot in full20.slots if slot.carrier == carrier]
    reconstructed = np.zeros_like(vectors)
    sector_norms = {"S": 0.0, "I": 0.0, "R": 0.0}
    for target in targets:
        coordinates = target.basis.conj().T @ vectors
        reconstructed += target.basis @ coordinates
        sector_norms[target.sector] += float(np.linalg.norm(coordinates) ** 2)
    return reconstructed, {
        sector: float(np.sqrt(value)) for sector, value in sector_norms.items()
    }


# =============================================================================
# A. Layer 0: actual DeWitt trace versus the raw Frobenius plant
# =============================================================================

print("=" * 96)
print("A. ACTUAL Sym^2 DEWITT TRACE, HODGE TYPE, AND RAW-FROBENIUS PLANT")
print("=" * 96)

eta4 = full20.ETA4_MATRIX
dewitt_gram = full20.dewitt_metric(eta4)
raw_gram = raw_frobenius_metric(eta4)
check(
    "actual Sym^2 DeWitt fibre has signature (6,4)",
    signature(dewitt_gram) == (6, 4, 0),
    str(signature(dewitt_gram)),
)
check(
    "raw Frobenius plant has the different signature (7,3)",
    signature(raw_gram) == (7, 3, 0),
    str(signature(raw_gram)),
)

h_trace = -0.25 * eta4
q_dewitt = (
    eta4 @ h_trace @ eta4
    - 0.5 * np.trace(eta4 @ h_trace) * eta4
)
q_raw = eta4 @ h_trace @ eta4
tau_matrix = 0.25 * eta4
test_tensor = np.array(
    [
        [2.0, 1.0, -3.0, 5.0],
        [1.0, -7.0, 11.0, 13.0],
        [-3.0, 11.0, 17.0, -19.0],
        [5.0, 13.0, -19.0, 23.0],
    ]
)
tau_test = 0.25 * float(np.trace(eta4 @ test_tensor))
check(
    "DeWitt musical trace reversal sends h_tr=-g/4 to +g^-1/4",
    max_abs(q_dewitt - tau_matrix) < TOL,
    f"defect {max_abs(q_dewitt - tau_matrix):.2e}",
)
check(
    "raw Frobenius musical is the hostile linear-sign inverse",
    max_abs(q_raw + tau_matrix) < TOL
    and abs(float(np.trace(q_dewitt.T @ test_tensor)) - tau_test) < TOL
    and abs(float(np.trace(q_raw.T @ test_tensor)) + tau_test) < TOL,
)
check(
    "trace direction is DeWitt-negative (-1/4) but raw-Frobenius-positive (+1/4)",
    abs(dewitt_pair(h_trace, h_trace) + 0.25) < TOL
    and abs(raw_frobenius_pair(h_trace, h_trace) - 0.25) < TOL,
)

actual_eta10 = np.array([1.0] * 6 + [-1.0] * 4)
raw_eta10_plant = np.array([1.0] * 7 + [-1.0] * 3)
actual_hodge_1 = hodge_matrix(actual_eta10, 1)
actual_hodge_9 = hodge_matrix(actual_eta10, 9)
raw_hodge_1 = hodge_matrix(raw_eta10_plant, 1)
raw_hodge_9 = hodge_matrix(raw_eta10_plant, 9)
check(
    "actual (6,4) Hodge star squares to -1 on one-forms",
    max_abs(actual_hodge_9 @ actual_hodge_1 + np.eye(10)) < TOL,
)
check(
    "raw (7,3) plant flips the Hodge type to star^2=+1 on one-forms",
    max_abs(raw_hodge_9 @ raw_hodge_1 - np.eye(10)) < TOL,
)

# The trace line is Lorentz-fixed, but a positive/negative plane split is
# extra Cartan/observer structure.  Spatial rotations preserve the displayed
# A6/W4 split; base boosts mix A6 with the three non-trace W directions.
lorentz_rotations = []
lorentz_boosts = []
for left, right in combinations(range(4), 2):
    generator = np.zeros((4, 4))
    if right == 3:
        generator[left, right] = 1.0
        generator[right, left] = 1.0
        lorentz_boosts.append(induced_lorentz_on_dewitt(generator))
    else:
        generator[left, right] = 1.0
        generator[right, left] = -1.0
        lorentz_rotations.append(induced_lorentz_on_dewitt(generator))

trace_basis_vector = np.eye(10)[:, 6]
split_projector = np.diag([0.0] * 6 + [1.0] * 4)
rotation_mix = max(
    np.linalg.norm(generator[:6, 6:])
    + np.linalg.norm(generator[6:, :6])
    for generator in lorentz_rotations
)
boost_mix = [
    (
        float(np.linalg.norm(generator[:6, 6:])),
        float(np.linalg.norm(generator[6:, :6])),
        float(np.linalg.norm(generator @ split_projector - split_projector @ generator)),
    )
    for generator in lorentz_boosts
]
check(
    "the DeWitt trace line is fixed by the full induced base-Lorentz algebra",
    max(
        np.linalg.norm(generator @ trace_basis_vector)
        for generator in lorentz_rotations + lorentz_boosts
    )
    < TOL,
)
check(
    "spatial rotations preserve the displayed A6/W4 Cartan split",
    rotation_mix < TOL,
    f"max leakage {rotation_mix:.2e}",
)
check(
    "all three base boosts mix A6 with the non-trace part of W4",
    all(
        left > 1.0 and right > 1.0 and commutator_norm > 1.0
        for left, right, commutator_norm in boost_mix
    ),
    str([(round(left, 6), round(right, 6), round(comm, 6))
         for left, right, comm in boost_mix]),
)

rapidity = 0.37
finite_boost = np.eye(4)
finite_boost[0, 0] = np.cosh(rapidity)
finite_boost[3, 3] = np.cosh(rapidity)
finite_boost[0, 3] = np.sinh(rapidity)
finite_boost[3, 0] = np.sinh(rapidity)
finite_induced = induced_change_on_dewitt(finite_boost)
moved_split_projector = (
    finite_induced
    @ split_projector
    @ np.linalg.inv(finite_induced)
)
finite_split_motion = float(
    np.linalg.norm(moved_split_projector - split_projector)
)
check(
    "a finite base boost moves the chosen W4 projector",
    finite_split_motion > 1.0,
    f"projector motion {finite_split_motion:.9f}",
)
info(
    "signature and the canonical trace line do not select A6 plus W4; "
    "the bidoublet formula is conditional on a moving observer/Cartan "
    "reduction, which must be derived or charged"
)


# =============================================================================
# B. Native parameter census and the projected four-component candidate
# =============================================================================

print("\n" + "=" * 96)
print("B. BASE-SCALAR NATIVE CENSUS AND Phi_t^lambda(W)")
print("=" * 96)

# Raw complex endomorphisms commuting with proper Spin(3,1) are
# span_C{1,omega4} tensor End_C(C^32): 2048 complex = 4096 real.  The native
# sp(32,32;H) real form admits only the listed Clifford degrees.  For exterior
# base degree 0 or 4, both copies leave internal degrees 2,3,6,7,10.
raw_base_scalar_real_dimension = 2 * 2 * 32 * 32
internal_native_degrees = (2, 3, 6, 7, 10)
one_native_copy_dimension = sum(comb(10, degree) for degree in internal_native_degrees)
native_base_scalar_real_dimension = 2 * one_native_copy_dimension


def anticommuting_monomial_count(degree: int) -> int:
    # If t is absent, anticommutation needs odd degree.  If t is present, it
    # needs even degree.  The other nine indices are freely selected.
    if degree % 2:
        return comb(9, degree)
    return comb(9, degree - 1)


one_anticommuting_copy_dimension = sum(
    anticommuting_monomial_count(degree)
    for degree in internal_native_degrees
)
native_anticommuting_real_dimension = 2 * one_anticommuting_copy_dimension
check(
    "unrestricted base-Lorentz-scalar End_C comparator has real dimension 4096",
    raw_base_scalar_real_dimension == 4096,
)
check(
    "native base-scalar plus base-pseudoscalar space has real dimension 992",
    one_native_copy_dimension == 496
    and native_base_scalar_real_dimension == 992,
    f"2 x {one_native_copy_dimension}",
)
check(
    "the native {Phi,c(t)}=0 space has real dimension 512",
    one_anticommuting_copy_dimension == 256
    and native_anticommuting_real_dimension == 512,
    f"2 x {one_anticommuting_copy_dimension}",
)

gamma10 = full20.gamma_10
t_internal = gamma10[6]
vol6 = matrix_product(gamma10[:6])
vol_w = matrix_product(gamma10[6:])
vol10 = vol6 @ vol_w
identity32 = np.eye(32, dtype=complex)
check(
    "internal split is the actual (6,4) Clifford split and t is negative",
    max_abs(t_internal @ t_internal + identity32) < TOL
    and max_abs(vol10 - matrix_product(gamma10)) < TOL,
)
check(
    "internal volume exchanges the unprojected volW*w and vol6*w legs",
    max(
        max_abs(vol10 @ (vol_w @ w_gamma) - vol6 @ w_gamma)
        for w_gamma in gamma10[6:]
    )
    < TOL
    and max_abs(vol10 @ vol10 + identity32) < TOL,
)


def internal_candidate(lambda_value: float) -> list[np.ndarray]:
    return [
        anticommuting_projection(
            vol_w @ w_gamma + lambda_value * vol6 @ w_gamma,
            t_internal,
        )
        for w_gamma in gamma10[6:]
    ]


candidates_internal = {
    lambda_value: internal_candidate(lambda_value)
    for lambda_value in (-1.0, 1.0, 2.0)
}
for lambda_value, components in candidates_internal.items():
    check(
        f"lambda={lambda_value:+g} has four independent nonzero components anticommuting with t",
        np.linalg.matrix_rank(
            np.column_stack([component.reshape(-1) for component in components]),
            tol=TOL,
        )
        == 4
        and max(
            max_abs(component @ t_internal + t_internal @ component)
            for component in components
        )
        < TOL,
    )

gram_minus = normalized_hilbert_schmidt_gram(candidates_internal[-1.0])
gram_plus = normalized_hilbert_schmidt_gram(candidates_internal[1.0])
gram_plant = normalized_hilbert_schmidt_gram(candidates_internal[2.0])
check(
    "lambda=+1 and lambda=-1 give isotropic Hilbert-Schmidt pullback Grams",
    max_abs(gram_minus - np.eye(4)) < TOL
    and max_abs(gram_plus - np.eye(4)) < TOL,
)
check(
    "lambda=2 Hilbert-Schmidt plant is anisotropic with Gram diag(1,4,4,4)",
    max_abs(gram_plant - np.diag([1.0, 4.0, 4.0, 4.0])) < TOL,
)
projector_minus = span_projector(candidates_internal[-1.0])
projector_plus = span_projector(candidates_internal[1.0])
projector_plant = span_projector(candidates_internal[2.0])
check(
    "lambda signs have the same image and differ by the planted domain reflection diag(1,-1,-1,-1)",
    max_abs(projector_minus - projector_plus) < TOL
    and np.linalg.det(np.diag([1.0, -1.0, -1.0, -1.0])) < 0.0,
)
check(
    "anisotropic lambda=2 plant keeps the image but fails the soldering normalization",
    max_abs(projector_plus - projector_plant) < TOL
    and max_abs(gram_plant - np.eye(4)) > 1.0,
)

spin3_stabilizer_generators = [
    spin_generator(gamma10[left], gamma10[right])
    for left, right in combinations(range(7, 10), 2)
]
spin4_t_mixing_generators = [
    spin_generator(gamma10[6], gamma10[index])
    for index in range(7, 10)
]
for lambda_value in (-1.0, 1.0):
    stabilizer_leakages = commutator_span_leakages(
        candidates_internal[lambda_value],
        spin3_stabilizer_generators,
    )
    t_mixing_leakages = commutator_span_leakages(
        candidates_internal[lambda_value],
        spin4_t_mixing_generators,
    )
    check(
        f"fixed-t lambda={lambda_value:+g} image closes under the Spin(3) stabilizer",
        max(stabilizer_leakages) < TOL,
        str([round(value, 9) for value in stabilizer_leakages]),
    )
    check(
        f"all three Spin(4) generators moving t leak from the fixed-t lambda={lambda_value:+g} image",
        all(
            abs(value - 4.0 * np.sqrt(2.0)) < TOL
            for value in t_mixing_leakages
        ),
        str([round(value, 9) for value in t_mixing_leakages]),
    )
info(
    "The fixed-t image is a Spin(3)-stabilizer module, not a fixed Spin(4) "
    "module.  Spin(4) covariance therefore requires the family with t moved "
    "by the observer/Cartan datum."
)


# =============================================================================
# C. Canonical rho, native real form, K/C branches, and Layer-0 chirality
# =============================================================================

print("\n" + "=" * 96)
print("C. rho_S INCLUSION, RIGHT-H/KREIN GATES, C_+ VERSUS C_-")
print("=" * 96)

identity128 = np.eye(128, dtype=complex)
omega4_full = np.kron(full20.omega_4, identity32)
omega14 = full20.normalized_chirality(full20.gamma_14)
raw_base_volume4 = matrix_product(full20.gamma_4)
base_volume_full = np.kron(raw_base_volume4, identity32)
c_hat_tau = full20.gamma_14[4 + 6]

# The real structure commuting antilinearly with every Cl(9,5) generator.
j_h = omega14 @ full20.commuting_real_structure(full20.gamma_14)
check(
    "J_H is quaternionic and commutes antilinearly with all fourteen gammas",
    max_abs(j_h @ j_h.conj() + identity128) < TOL
    and max(
        max_abs(
            j_h @ gamma.conj() @ np.linalg.inv(j_h) - gamma
        )
        for gamma in full20.gamma_14
    )
    < TOL,
)
check(
    "native unit c(hat_tau) is the DeWitt-negative trace gamma and squares to -I",
    max_abs(c_hat_tau @ c_hat_tau + identity128) < TOL,
)
raw_gamma10, raw_eta10_clifford = full20.signed_gammas(7, 3)
raw_trace_gamma_plant = np.kron(full20.omega_4, raw_gamma10[6])
check(
    "raw Frobenius trace plant is positive and squares to +I; it is not -c(hat_tau) in native Cl(6,4)",
    max_abs(raw_eta10_clifford - raw_eta10_plant) < TOL
    and max_abs(raw_trace_gamma_plant @ raw_trace_gamma_plant - identity128)
    < TOL
    and max_abs((-c_hat_tau) @ (-c_hat_tau) + identity128) < TOL,
)

base_spin_generators = [
    spin_generator(full20.gamma_14[left], full20.gamma_14[right])
    for left, right in combinations(range(4), 2)
]

# C_+/- are named by gamma^T C_+ = +C_+ gamma and
# gamma^T C_- = -C_- gamma.  Both are Spin-invariant bilinear matrices.
c_plus = matrix_product([full20.gamma_14[index] for index in range(0, 14, 2)])
c_minus = matrix_product([full20.gamma_14[index] for index in range(1, 14, 2)])
all_spin_generators = [
    spin_generator(full20.gamma_14[left], full20.gamma_14[right])
    for left, right in combinations(range(14), 2)
]
check(
    "C_+ and C_- are both Spin(9,5)-invariant bilinear matrices",
    max(
        max_abs(generator.T @ c_plus + c_plus @ generator)
        for generator in all_spin_generators
    )
    < TOL
    and max(
        max_abs(generator.T @ c_minus + c_minus @ generator)
        for generator in all_spin_generators
    )
    < TOL,
)
check(
    "C signs and transpose types are distinct",
    max(
        max_abs(gamma.T @ c_plus - c_plus @ gamma)
        for gamma in full20.gamma_14
    )
    < TOL
    and max(
        max_abs(gamma.T @ c_minus + c_minus @ gamma)
        for gamma in full20.gamma_14
    )
    < TOL
    and max_abs(c_plus.T + c_plus) < TOL
    and max_abs(c_minus.T - c_minus) < TOL,
)


def native_phi_branches(
    internal_components: list[np.ndarray],
) -> dict[str, list[np.ndarray]]:
    # An odd internal word in the factorized representation is omega4 tensor X.
    base_degree_zero = [
        np.kron(full20.omega_4, component)
        for component in internal_components
    ]
    base_degree_four = [
        base_volume_full @ component
        for component in base_degree_zero
    ]
    return {
        "base-degree-0 scalar": base_degree_zero,
        "base-degree-4 pseudoscalar": base_degree_four,
    }


all_branch_data: dict[
    tuple[float, str], tuple[list[np.ndarray], list[np.ndarray]]
] = {}
for lambda_value, internal_components in candidates_internal.items():
    for branch_name, phi_components in native_phi_branches(
        internal_components
    ).items():
        # For the defining associated spinor bundle this is not a fitted map:
        # rho_S is the literal matrix inclusion.
        rho_components = [component for component in phi_components]
        a_components = [
            c_hat_tau @ component for component in rho_components
        ]
        all_branch_data[(lambda_value, branch_name)] = (
            rho_components,
            a_components,
        )

        check(
            f"rho_S is exact defining-representation inclusion [{lambda_value:+g}, {branch_name}]",
            all(
                rho is phi
                for rho, phi in zip(rho_components, phi_components)
            ),
        )
        check(
            f"Phi is native right-H-linear and Krein-skew [{lambda_value:+g}, {branch_name}]",
            max(right_h_defect(phi, j_h) for phi in phi_components) < TOL
            and max(
                max_abs(krein_adjoint(phi) + phi)
                for phi in phi_components
            )
            < TOL,
        )
        check(
            f"Phi anticommutes with c(hat_tau), so A_S is Krein-self [{lambda_value:+g}, {branch_name}]",
            max(
                max_abs(phi @ c_hat_tau + c_hat_tau @ phi)
                for phi in phi_components
            )
            < TOL
            and max(
                max_abs(krein_adjoint(operator) - operator)
                for operator in a_components
            )
            < TOL,
        )
        check(
            f"Phi and A_S commute with first-four spin generators; induced-Sym2 boost covariance is separate [{lambda_value:+g}, {branch_name}]",
            max(
                max_abs(generator @ operator - operator @ generator)
                for generator in base_spin_generators
                for operator in phi_components + a_components
            )
            < TOL,
        )
        check(
            f"A_S preserves base chirality while K A_S is purely cross-chirality [{lambda_value:+g}, {branch_name}]",
            max(
                max_abs(operator @ omega4_full - omega4_full @ operator)
                for operator in a_components
            )
            < TOL
            and max(
                max_abs(
                    (full20.krein @ operator) @ omega4_full
                    + omega4_full @ (full20.krein @ operator)
                )
                for operator in a_components
            )
            < TOL,
        )
        check(
            f"C_+A is alternating but C_-A is symmetric [{lambda_value:+g}, {branch_name}]",
            max(
                max_abs((c_plus @ operator).T + c_plus @ operator)
                for operator in a_components
            )
            < TOL
            and max(
                max_abs((c_minus @ operator).T - c_minus @ operator)
                for operator in a_components
            )
            < TOL,
        )

for lambda_value in (-1.0, 1.0):
    scalar_phis = all_branch_data[
        (lambda_value, "base-degree-0 scalar")
    ][0]
    pseudoscalar_phis = all_branch_data[
        (lambda_value, "base-degree-4 pseudoscalar")
    ][0]
    scalar_invariant_gram = defining_real_trace_gram(scalar_phis)
    pseudoscalar_invariant_gram = defining_real_trace_gram(
        pseudoscalar_phis
    )
    scalar_hilbert_schmidt_gram = hilbert_schmidt_gram(scalar_phis)
    pseudoscalar_hilbert_schmidt_gram = hilbert_schmidt_gram(
        pseudoscalar_phis
    )
    check(
        f"defining ReTr(Phi_i Phi_j) has scalar +128 and pseudoscalar -128 signs [lambda={lambda_value:+g}]",
        max_abs(scalar_invariant_gram - 128.0 * np.eye(4)) < TOL
        and max_abs(
            pseudoscalar_invariant_gram + 128.0 * np.eye(4)
        )
        < TOL,
    )
    check(
        f"the invariant ReTr signs are distinct from the positive Hilbert-Schmidt isometry Gram [lambda={lambda_value:+g}]",
        max_abs(
            scalar_hilbert_schmidt_gram - 128.0 * np.eye(4)
        )
        < TOL
        and max_abs(
            pseudoscalar_hilbert_schmidt_gram - 128.0 * np.eye(4)
        )
        < TOL
        and max_abs(
            pseudoscalar_invariant_gram
            - pseudoscalar_hilbert_schmidt_gram
        )
        > 128.0,
    )
info(
    "The unnormalized defining ReTr fixture distinguishes the two branch "
    "signs.  It does not fix the invariant action coefficient, canonical "
    "field normalization, or any cosmological scale."
)

check(
    "the scalar and pseudoscalar copies are independent and neither is parity-selected",
    max_abs(base_volume_full - (-1j * omega4_full)) < TOL
    and max_abs(base_volume_full @ base_volume_full + identity128) < TOL,
)
info(
    "For an identical Grassmann field, the alternating C_+ A kernel survives; "
    "the symmetric C_- A kernel needs an additional antisymmetric label.  "
    "This is a bilinear statement, not a mass or VEV claim."
)


# =============================================================================
# D. Canonical S plus (V tensor S) lift and all twenty finite witnesses
# =============================================================================

print("\n" + "=" * 96)
print("D. CANONICAL FULL-20 LIFT, S/I/R RESOLUTION, AND TWENTY WITNESSES")
print("=" * 96)

check(
    "reused full-20 substrate passed its own executable controls",
    not full20.FAILURES
    and len(full20.slots) == 20
    and sum(slot.dimension for slot in full20.slots) == 1920,
)

field_coefficients = np.array([1.0, 2.0, -1.0, 3.0])
field_coefficients /= np.linalg.norm(field_coefficients)


def combined_operator(lambda_value: float, branch_name: str) -> np.ndarray:
    _phis, operators = all_branch_data[(lambda_value, branch_name)]
    return sum(
        (
            coefficient * operator
            for coefficient, operator in zip(field_coefficients, operators)
        ),
        np.zeros((128, 128), dtype=complex),
    )


representative_operators = {
    (lambda_value, branch_name): combined_operator(lambda_value, branch_name)
    for lambda_value in (-1.0, 1.0)
    for branch_name in (
        "base-degree-0 scalar",
        "base-degree-4 pseudoscalar",
    )
}

closure_defects: dict[tuple[float, str], float] = {}
nonzero_witnesses: dict[tuple[float, str], int] = {}
sector_profiles: dict[
    tuple[float, str], dict[str, tuple[float, float, float]]
] = {}
for key, operator in representative_operators.items():
    closure_defect = 0.0
    nonzero_count = 0
    profiles: dict[str, tuple[float, float, float]] = {}
    for source in full20.slots:
        witness = slot_witness(source)
        image = apply_associated_lift(operator, source.carrier, witness)
        reconstructed, sector_norms = reconstruct_from_slots(
            source.carrier, image
        )
        scale = max(1.0, float(np.linalg.norm(image)))
        closure_defect = max(
            closure_defect,
            float(np.linalg.norm(image - reconstructed)) / scale,
        )
        nonzero_count += int(float(np.linalg.norm(image)) > TOL)
        profiles[source.name] = (
            sector_norms["S"],
            sector_norms["I"],
            sector_norms["R"],
        )
    closure_defects[key] = closure_defect
    nonzero_witnesses[key] = nonzero_count
    sector_profiles[key] = profiles

check(
    "canonical diag(A_S,1_V tensor A_S) lift closes all 20 witnesses",
    max(closure_defects.values()) < TOL
    and min(nonzero_witnesses.values()) == 20,
    f"max residual {max(closure_defects.values()):.2e}",
)
check(
    "lift keeps S and V tensor S carrier types distinct",
    all(
        profile[0] > TOL
        and profile[1] < TOL
        and profile[2] < TOL
        for profiles in sector_profiles.values()
        for name, profile in profiles.items()
        if name.startswith("S:")
    )
    and all(
        profile[0] < TOL
        for profiles in sector_profiles.values()
        for name, profile in profiles.items()
        if not name.startswith("S:")
    ),
)

rng = np.random.default_rng(20260730)
random_vs = (
    rng.standard_normal((14 * 128, 3))
    + 1j * rng.standard_normal((14 * 128, 3))
)
sir_defects = []
r_trace_defects = []
for operator in representative_operators.values():
    image = apply_associated_lift(operator, "VS", random_vs)
    image_i = full20.p_i(image)
    image_r = full20.p_r(image)
    sir_defects.extend(
        [
            max_abs(image - image_i - image_r),
            max_abs(full20.p_i(image_i) - image_i),
            max_abs(full20.p_r(image_r) - image_r),
        ]
    )
    r_trace_defects.append(max_abs(full20.gamma_trace(image_r)))
check(
    "written P_I/P_R maps exactly resolve every tested lifted vector-spinor",
    max(sir_defects) < TOL and max(r_trace_defects) < TOL,
    (
        f"projector defect {max(sir_defects):.2e}, "
        f"R trace {max(r_trace_defects):.2e}"
    ),
)

# This is intentionally not asserted as slot preservation: a zero-order
# spinor operator need not commute with Gamma.  The finite statement is that
# the already-written S/I/R projectors and all twenty target embeddings close
# the image without adding a twenty-first carrier.
representative_profile = sector_profiles[
    (1.0, "base-degree-0 scalar")
]
mixed_i_to_r = any(
    profile[2] > TOL
    for name, profile in representative_profile.items()
    if name.startswith("imGamma:")
)
mixed_r_to_i = any(
    profile[1] > TOL
    for name, profile in representative_profile.items()
    if name.startswith(("kerGamma:", "X:"))
)
check(
    "finite witness detects the honest I/R mixing rather than assuming slot preservation",
    mixed_i_to_r and mixed_r_to_i,
)


# =============================================================================
# E. Exact thin-slot support, P0 ceilings, and corrected coflip parity
# =============================================================================

print("\n" + "=" * 96)
print("E. EXACT 44-CELL SUPPORT, P0 CEILINGS, AND GAMMA-NATURAL COFLIP")
print("=" * 96)


def thin_slot_support(
    operator: np.ndarray,
) -> tuple[set[tuple[str, str]], float, float]:
    """All coefficient blocks B_target^dag O B_source, not witness samples."""
    support: set[tuple[str, str]] = set()
    minimum_nonzero = float("inf")
    maximum_zero = 0.0
    for source in full20.slots:
        image = apply_associated_lift(operator, source.carrier, source.basis)
        for target in full20.slots:
            if target.carrier != source.carrier:
                continue
            block_norm = float(
                np.linalg.norm(target.basis.conj().T @ image)
            )
            if block_norm > 1.0e-8:
                support.add((source.name, target.name))
                minimum_nonzero = min(minimum_nonzero, block_norm)
            else:
                maximum_zero = max(maximum_zero, block_norm)
    return support, minimum_nonzero, maximum_zero


label_to_x = {
    "E+:L16+": "X:X2Tm",
    "E+:R16-": "X:X1Tp",
    "E-:L16-": "X:X2Tp",
    "E-:R16+": "X:X1Tm",
}
expected_support: set[tuple[str, str]] = set()
for label, x_name in label_to_x.items():
    s_name = f"S:{label}"
    i_name = f"imGamma:{label}"
    r_name = f"kerGamma:{label}"
    expected_support.update(
        {
            (s_name, s_name),             # SS
            (i_name, i_name),             # II
            (i_name, r_name),             # IR
            (i_name, x_name),             # IR
            (r_name, i_name),             # RI
            (x_name, i_name),             # RI
            (r_name, r_name),             # RR
            (r_name, x_name),             # RR
            (x_name, r_name),             # RR
            (x_name, x_name),             # RR
        }
    )
for diagonal_x in ("X:X32p", "X:X23m", "X:X32m", "X:X23p"):
    expected_support.add((diagonal_x, diagonal_x))

support_sector_counts = {
    ("S", "S"): 4,
    ("I", "I"): 4,
    ("I", "R"): 8,
    ("R", "I"): 8,
    ("R", "R"): 20,
}
check(
    "pre-registered exact support template is 4_SS+4_II+8_IR+8_RI+20_RR=44",
    len(expected_support) == 44
    and {
        sector_pair: sum(
            full20.sector_from_name(source) == sector_pair[0]
            and full20.sector_from_name(target) == sector_pair[1]
            for source, target in expected_support
        )
        for sector_pair in support_sector_counts
    }
    == support_sector_counts,
)

# Compute every block for all four lambda=+1 components in both native base
# copies.  The already-checked exact component relations then transfer this
# support to lambda=-1 and the nonzero lambda=2 normalization plant.
exact_supports: dict[tuple[str, int], set[tuple[str, str]]] = {}
minimum_nonzero_blocks: list[float] = []
maximum_zero_blocks: list[float] = []
for branch_name in (
    "base-degree-0 scalar",
    "base-degree-4 pseudoscalar",
):
    _phis, component_operators = all_branch_data[(1.0, branch_name)]
    for component_index, operator in enumerate(component_operators):
        support, minimum_nonzero, maximum_zero = thin_slot_support(operator)
        exact_supports[(branch_name, component_index)] = support
        minimum_nonzero_blocks.append(minimum_nonzero)
        maximum_zero_blocks.append(maximum_zero)

check(
    "all four scalar and all four pseudoscalar components have exactly the same 44 cells",
    all(support == expected_support for support in exact_supports.values()),
)
check(
    "zero/nonzero block classification has a planted-test-sized numerical gap",
    min(minimum_nonzero_blocks) > 0.8
    and max(maximum_zero_blocks) < 1.0e-12,
    (
        f"min nonzero {min(minimum_nonzero_blocks):.3e}, "
        f"max zero {max(maximum_zero_blocks):.3e}"
    ),
)

lambda_relations = {
    -1.0: np.array([1.0, -1.0, -1.0, -1.0]),
    2.0: np.array([1.0, 2.0, 2.0, 2.0]),
}
check(
    "lambda=-1 and lambda=2 transfer the same support by exact nonzero component rescalings",
    all(
        max(
            max_abs(
                candidate
                - scale * reference
            )
            for candidate, scale, reference in zip(
                candidates_internal[lambda_value],
                scales,
                candidates_internal[1.0],
            )
        )
        < TOL
        for lambda_value, scales in lambda_relations.items()
    ),
)


def p0_cell_ceiling(
    support: set[tuple[str, str]], sector: str | None
) -> int:
    if sector is None:
        return len(support)
    return sum(
        full20.sector_from_name(source) == sector
        and full20.sector_from_name(target) == sector
        for source, target in support
    )


p0_cell_ceilings = {
    "1": p0_cell_ceiling(expected_support, None),
    "P_S": p0_cell_ceiling(expected_support, "S"),
    "P_I": p0_cell_ceiling(expected_support, "I"),
    "P_R": p0_cell_ceiling(expected_support, "R"),
}
p0_carrier_ranks = {
    "1": 1920,
    "P_S": sum(slot.dimension for slot in full20.slots_by_sector["S"]),
    "P_I": sum(slot.dimension for slot in full20.slots_by_sector["I"]),
    "P_R": sum(slot.dimension for slot in full20.slots_by_sector["R"]),
}
check(
    "P0 sandwich support ceilings are 44,4,4,20 for 1,P_S,P_I,P_R",
    p0_cell_ceilings == {"1": 44, "P_S": 4, "P_I": 4, "P_R": 20},
    str(p0_cell_ceilings),
)
check(
    "P0 carrier-rank ceilings retain the complete 1920=128+128+1664 split",
    p0_carrier_ranks
    == {"1": 1920, "P_S": 128, "P_I": 128, "P_R": 1664},
    str(p0_carrier_ranks),
)


def apply_gamma_natural_coflip(
    carrier: str, vectors: np.ndarray
) -> np.ndarray:
    """Corrected antilinear coflip, including (N eta)_V on V tensor S."""
    if carrier == "S":
        return full20.cperp_spin @ vectors.conj()
    reshaped = vectors.conj().reshape(14, 128, -1)
    out = np.empty_like(reshaped)
    for vector_index in range(14):
        out[vector_index] = (
            full20.natural_vector_factor[vector_index]
            * full20.cperp_spin
            @ reshaped[vector_index]
        )
    return out.reshape(14 * 128, -1)


check(
    "owned corrected coflip maps all twenty slots to their declared mirrors",
    max(full20.natural_leakage.values()) < TOL
    and max(full20.pairing_leakage.values()) > 1.0,
    (
        f"corrected leakage {max(full20.natural_leakage.values()):.2e}, "
        f"pairing-only hostile leakage {max(full20.pairing_leakage.values()):.2e}"
    ),
)

coflip_spin_defects: dict[str, float] = {}
coflip_phi_defects: dict[str, float] = {}
coflip_full20_defects: dict[str, float] = {}
inverse_cperp = np.linalg.inv(full20.cperp_spin)
trace_coflip_defect = max_abs(
    full20.cperp_spin
    @ c_hat_tau.conj()
    @ inverse_cperp
    - c_hat_tau
)
check(
    "the normalized trace Clifford insertion is coflip-even",
    trace_coflip_defect < TOL,
    f"defect {trace_coflip_defect:.2e}",
)
for branch_name, coflip_sign in (
    ("base-degree-0 scalar", 1.0),
    ("base-degree-4 pseudoscalar", -1.0),
):
    spin_defect = 0.0
    phi_defect = 0.0
    full20_defect = 0.0
    for lambda_value in (-1.0, 1.0, 2.0):
        phis, component_operators = all_branch_data[
            (lambda_value, branch_name)
        ]
        for phi, operator in zip(phis, component_operators):
            phi_defect = max(
                phi_defect,
                max_abs(
                    full20.cperp_spin
                    @ phi.conj()
                    @ inverse_cperp
                    - coflip_sign * phi
                ),
            )
            spin_defect = max(
                spin_defect,
                max_abs(
                    full20.cperp_spin
                    @ operator.conj()
                    @ inverse_cperp
                    - coflip_sign * operator
                ),
            )
            for slot in full20.slots:
                witness = slot_witness(slot)
                left = apply_gamma_natural_coflip(
                    slot.carrier,
                    apply_associated_lift(
                        operator, slot.carrier, witness
                    ),
                )
                right = coflip_sign * apply_associated_lift(
                    operator,
                    slot.carrier,
                    apply_gamma_natural_coflip(
                        slot.carrier, witness
                    ),
                )
                scale = max(
                    1.0,
                    float(np.linalg.norm(left)),
                    float(np.linalg.norm(right)),
                )
                full20_defect = max(
                    full20_defect,
                    float(np.linalg.norm(left - right)) / scale,
                )
    coflip_spin_defects[branch_name] = spin_defect
    coflip_phi_defects[branch_name] = phi_defect
    coflip_full20_defects[branch_name] = full20_defect

check(
    "corrected Gamma-natural coflip makes base-degree-0 Phi and its vertex even",
    coflip_phi_defects["base-degree-0 scalar"] < TOL
    and
    coflip_spin_defects["base-degree-0 scalar"] < TOL
    and coflip_full20_defects["base-degree-0 scalar"] < TOL,
    (
        f"Phi {coflip_phi_defects['base-degree-0 scalar']:.2e}, "
        f"spin {coflip_spin_defects['base-degree-0 scalar']:.2e}, "
        f"full20 {coflip_full20_defects['base-degree-0 scalar']:.2e}"
    ),
)
check(
    "corrected Gamma-natural coflip makes base-degree-4 Phi and its vertex odd",
    coflip_phi_defects["base-degree-4 pseudoscalar"] < TOL
    and
    coflip_spin_defects["base-degree-4 pseudoscalar"] < TOL
    and coflip_full20_defects["base-degree-4 pseudoscalar"] < TOL,
    (
        f"Phi {coflip_phi_defects['base-degree-4 pseudoscalar']:.2e}, "
        f"spin {coflip_spin_defects['base-degree-4 pseudoscalar']:.2e}, "
        f"full20 {coflip_full20_defects['base-degree-4 pseudoscalar']:.2e}"
    ),
)
info(
    "The corrected coflip distinguishes the two branches (+ scalar, - "
    "pseudoscalar), but no source-owned parity/CP rule in this probe selects "
    "which sign is physical."
)


# =============================================================================
# F. Scoped verdict
# =============================================================================

print("\n" + "=" * 96)
print("F. SCOPED VERDICT")
print("=" * 96)

if FAILURES:
    print(f"FAIL: {len(FAILURES)} check(s):")
    for failure in FAILURES:
        print(f"  - {failure}")
    print("VERDICT: CONSTRUCTION-PROBE-FAILED; DO NOT INTERPRET")
    raise SystemExit(1)

print("PASS: all finite and analytic checks passed.")
print(
    "VERDICT: CONDITIONAL-NATIVE-TRACE-VERTEX-CONSTRUCTED.  "
    "lambda=+/-1 give an isotropic four-component map; lambda=2 is the "
    "non-isotropic plant.  The lambda signs share one image and differ by a "
    "planted domain reflection; whether that reflection is physical remains "
    "open.  A fixed t closes under its Spin(3) stabilizer but not the three "
    "Spin(4) generators that move t.  Conditional on a moving observer/Cartan "
    "reduction, both the first-four-spin scalar and base-volume companion "
    "survive the native right-H/K/C gates, so a parity/CP condition is still "
    "needed before choosing one."
)
print(
    "FULL-20: the canonical S plus (V tensor S) lift closes through the "
    "written S/I/R projectors and every one of the twenty finite witnesses; "
    "the exact ordered supported-block count in this fixed twenty-slot "
    "decomposition is 4_SS+4_II+8_IR+8_RI+20_RR=44, with P0 block ceilings "
    "44/4/4/20.  It honestly mixes I and R rather than preserving each "
    "provenance slot."
)
print(
    "COFLIP: the corrected Gamma-natural map makes both base-degree-0 Phi "
    "and its vertex even, and both base-degree-4 Phi and its vertex odd.  "
    "This distinction is constructed, but a rule selecting one sign is not."
)
print(
    "OPEN: no source-owned SM selector, VEV, Yukawa matrix, physical mass, "
    "observer/Cartan reduction or moving-t Spin(4) family, invariant-action "
    "normalization, stationary vacuum, generation count, or cosmological "
    "prediction was constructed or inferred."
)
