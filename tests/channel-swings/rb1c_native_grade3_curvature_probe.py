#!/usr/bin/env python3
r"""RB1c: actual-(9,5) grade-three source, trace-line reopener, and cyclic gate.

Layer 0
-------
This probe keeps three different objects separate.

1. ``S3`` is the full-adjoint grade-flipping formula emitted by RB1b,

       pi_sp(Phi1 ^ *F - 1/2 *[Phi1 ^ *(Phi2 ^ *F)]).

2. ``S_trace`` left-multiplies the unprojected formula by the unit DeWitt
   trace direction before the native ``sp(32,32;H)`` projection.  This is a
   new trace-line/stabilizer construction, not Weinstein's written map.

3. ``T_pol`` is the canonical symmetric polarization of the cubic functional
   built from ``S_trace``.  It is a different two-input Euler-covector
   geometry.  It is not promoted to a single linear curvature-to-source map
   unless it factors through the polarized curvature.

The trace reversal is load-bearing.  Raw Frobenius ``Sym2(T*X)`` has
signature (7,3), whereas the four-dimensional DeWitt trace reversal makes it
(6,4).  With the base (3,1), this is the difference between total signatures
(10,4) and (9,5), and hence between ``*^2=+1`` and ``*^2=-1`` on degree two.

Frozen gates
------------
* The native source must be nonzero on a non-Riemannian curvature witness,
  so a Riemannian zero cannot be blamed on a vacuous implementation.
* ``S3`` is rejected as a torsion-free Ricci/Einstein source only if the
  pointwise Clifford reduction kills every algebraic-Riemann irrep; scalar,
  traceless-Ricci, and Weyl fixtures are independent regressions.
* ``S_trace`` reopens only the trace-line stabilizer route.  It cannot re-enter
  RB1/RB2 unless the finite derivative of its cubic action agrees with the
  naive ``3 <delta,S_trace(theta^2)>`` current on every deterministic fixture.
* A four-ordering coefficient family is not selected by fitting.  Full sampled
  rank rejects a universal nonzero fit in that family.
* ``T_pol`` is admitted only as a separately named comparator.  If its
  two-input current does not factor through polarized curvature, the exact
  obstruction is reported rather than hidden.

This is a deterministic finite algebraic boundary probe.  It does not build a
global action, Ward identity, VEV, physical mass, anomaly/index, cosmological
prediction, or generation count.
"""

from __future__ import annotations

from itertools import combinations, permutations
from pathlib import Path
import sys
from typing import Callable

import numpy as np


HERE = Path(__file__).resolve().parent
TESTS = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TESTS))

import actual_sym2_c14_orbit_probe as sym2  # noqa: E402


TOL = 1.0e-8
FD_TOL = 2.0e-5
CYCLIC_GAP_FLOOR = 1.0e-3
CYCLIC_SEEDS = (
    2026073101,
    2026073102,
    2026073103,
    2026073104,
    2026073105,
    2026073106,
)
HELDOUT_SEED = 2026073199
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


def relative_scalar(left: float, right: float) -> float:
    return abs(left - right) / max(1.0, abs(left), abs(right))


# ---------------------------------------------------------------------------
# A. The actual DeWitt trace reversal and native Cl(9,5) real form
# ---------------------------------------------------------------------------


print("=" * 104)
print("RB1c ACTUAL-(9,5) GRADE-THREE / TRACE-LINE / CYCLIC SOURCE PROBE")
print("=" * 104)
print("\nDETERMINISTIC FIXTURE SEEDS:", CYCLIC_SEEDS)
print("ORDERING-FIT HELD-OUT SEED:", HELDOUT_SEED)
print("\nA. Trace reversal, hostile raw-Frobenius control, and native real form")


def symmetric_basis() -> list[np.ndarray]:
    result = []
    for left in range(4):
        for right in range(left, 4):
            value = np.zeros((4, 4), dtype=float)
            value[left, right] = 1.0
            value[right, left] = 1.0
            result.append(value)
    return result


def raw_frobenius(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.trace(sym2.ETA4 @ left @ sym2.ETA4 @ right))


def gram_signature(gram: np.ndarray) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(gram)
    return (
        int(np.sum(eigenvalues > TOL)),
        int(np.sum(eigenvalues < -TOL)),
        int(np.sum(np.abs(eigenvalues) <= TOL)),
    )


sym_basis = symmetric_basis()
raw_gram = np.array(
    [[raw_frobenius(left, right) for right in sym_basis] for left in sym_basis]
)
dewitt_gram = np.array(
    [[sym2.dewitt(left, right) for right in sym_basis] for left in sym_basis]
)
raw_signature = gram_signature(raw_gram)
dewitt_signature = gram_signature(dewitt_gram)
check(
    "raw Frobenius and trace-reversed DeWitt fibre signatures are (7,3) and (6,4)",
    raw_signature == (7, 3, 0) and dewitt_signature == (6, 4, 0),
    f"raw={raw_signature}, DeWitt={dewitt_signature}",
)

frame_gram = np.array(
    [
        [sym2.dewitt(left, right) for right in sym2.DEWITT_FRAME]
        for left in sym2.DEWITT_FRAME
    ]
)
check(
    "the repository DeWitt frame realizes diag(+^6,-^4)",
    max_abs(frame_gram - np.diag(sym2.ETA10)) < TOL,
)

original_gammas, original_metric = sym2.native_gammas()
split_order = (0, 1, 2, 9, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13)
gammas = [original_gammas[index] for index in split_order]
eta = original_metric[list(split_order)]
eta_expected = np.concatenate((np.array([1.0, 1.0, 1.0, -1.0]), sym2.ETA10))
IDENTITY = np.eye(gammas[0].shape[0], dtype=complex)
ZERO = np.zeros_like(IDENTITY)

check(
    "the native Clifford basis is in actual base-(3,1) plus fibre-(6,4) order",
    np.array_equal(eta, eta_expected)
    and int(np.sum(eta > 0)) == 9
    and int(np.sum(eta < 0)) == 5,
    f"signature=({int(np.sum(eta > 0))},{int(np.sum(eta < 0))})",
)
check(
    "the reordered 128x128 matrices satisfy Cl(9,5)",
    sym2.clifford_defect(gammas, eta) < TOL,
)

h_trace = -sym2.ETA4 / 4.0
h_trace_coordinates = sym2.vector_coordinates(h_trace)
trace_frame_index = 6
trace_full_index = 4 + trace_frame_index
trace_gamma = gammas[trace_full_index]
check(
    "h_tr=-g/4 lies purely on the negative DeWitt trace line",
    np.count_nonzero(np.abs(h_trace_coordinates) > TOL) == 1
    and abs(h_trace_coordinates[trace_frame_index] + 0.5) < TOL
    and sym2.ETA10[trace_frame_index] == -1.0,
    f"coordinates={np.array2string(h_trace_coordinates, precision=3)}",
)
check(
    "the unit trace Clifford vector squares to -1",
    max_abs(trace_gamma @ trace_gamma + IDENTITY) < TOL,
)

raw_eta = eta.copy()
raw_eta[trace_full_index] = 1.0


def expected_hodge_square(dimension: int, degree: int, negative: int) -> int:
    return (-1) ** (degree * (dimension - degree) + negative)


check(
    "trace reversal changes the degree-2/12 Hodge square from hostile +1 to native -1",
    expected_hodge_square(14, 2, 4) == 1
    and expected_hodge_square(14, 12, 4) == 1
    and expected_hodge_square(14, 2, 5) == -1
    and expected_hodge_square(14, 12, 5) == -1,
)

krein = matrix_product(original_gammas[:9])
krein_inverse = np.linalg.inv(krein)
quaternionic_j = matrix_product(
    [original_gammas[index] for index in (1, 3, 5, 7, 10, 12)]
)
quaternionic_j_inverse = np.linalg.inv(quaternionic_j)


def krein_adjoint(matrix: np.ndarray) -> np.ndarray:
    return krein_inverse @ matrix.conj().T @ krein


def project_sp(matrix: np.ndarray) -> np.ndarray:
    """Native sp projection when its input is right-H linear."""
    return 0.5 * (matrix - krein_adjoint(matrix))


def h_defect(matrix: np.ndarray) -> float:
    return float(
        np.linalg.norm(
            matrix @ quaternionic_j - quaternionic_j @ matrix.conj()
        )
    )


def project_right_h(matrix: np.ndarray) -> np.ndarray:
    """Projection to matrices commuting with the native antilinear H action."""
    return 0.5 * (
        matrix
        + quaternionic_j @ matrix.conj() @ quaternionic_j_inverse
    )


check(
    "native gammas are Krein self-adjoint and right-H linear",
    max(max_abs(krein_adjoint(gamma) - gamma) for gamma in gammas) < TOL
    and max(h_defect(gamma) for gamma in gammas) < TOL,
)


# ---------------------------------------------------------------------------
# B. Sparse exterior algebra and the native source-shaped formula
# ---------------------------------------------------------------------------


Form = dict[tuple[int, ...], np.ndarray]
Source = Callable[[Form], Form]
FULL_KEY = tuple(range(14))


def permutation_sign(indices: tuple[int, ...]) -> int:
    inversions = sum(
        indices[left] > indices[right]
        for left in range(len(indices))
        for right in range(left + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


def add_forms(*forms: Form) -> Form:
    keys = set().union(*(form.keys() for form in forms))
    return {
        key: sum(
            (form.get(key, ZERO) for form in forms),
            ZERO.copy(),
        )
        for key in keys
    }


def scale_form(form: Form, scalar: float) -> Form:
    return {key: scalar * value for key, value in form.items()}


def wedge(left: Form, right: Form) -> Form:
    out: Form = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            joined = left_key + right_key
            if len(set(joined)) != len(joined):
                continue
            key = tuple(sorted(joined))
            value = permutation_sign(joined) * (left_value @ right_value)
            out[key] = out.get(key, ZERO.copy()) + value
    return out


def hodge(form: Form, metric: np.ndarray = eta) -> Form:
    out: Form = {}
    for key, value in form.items():
        complement = tuple(index for index in FULL_KEY if index not in key)
        coefficient = (
            permutation_sign(key + complement)
            * float(np.prod(metric[list(key)]))
        )
        out[complement] = coefficient * value
    return out


def form_degree(form: Form) -> int:
    degrees = {len(key) for key in form}
    if len(degrees) != 1:
        raise ValueError(f"inhomogeneous or empty form: {degrees}")
    return next(iter(degrees))


def form_norm(form: Form) -> float:
    return float(
        np.sqrt(sum(np.linalg.norm(value) ** 2 for value in form.values()))
    )


def form_relative(left: Form, right: Form) -> float:
    keys = set(left) | set(right)
    numerator = np.sqrt(
        sum(
            np.linalg.norm(left.get(key, ZERO) - right.get(key, ZERO)) ** 2
            for key in keys
        )
    )
    return float(numerator / max(1.0, form_norm(right)))


def form_krein_defect(form: Form) -> float:
    return max(
        (np.linalg.norm(krein_adjoint(value) + value) for value in form.values()),
        default=0.0,
    )


def form_h_defect(form: Form) -> float:
    return max((h_defect(value) for value in form.values()), default=0.0)


def project_form(form: Form) -> Form:
    return {key: project_sp(value) for key, value in form.items()}


def left_multiply(matrix: np.ndarray, form: Form) -> Form:
    return {key: matrix @ value for key, value in form.items()}


def right_multiply(form: Form, matrix: np.ndarray) -> Form:
    return {key: value @ matrix for key, value in form.items()}


def adjoint_form(group: np.ndarray, form: Form) -> Form:
    inverse = np.linalg.inv(group)
    return {key: group @ value @ inverse for key, value in form.items()}


def top_pair(one_form: Form, density_source: Form) -> float:
    top = wedge(one_form, density_source)
    return float(0.5 * np.trace(top.get(FULL_KEY, ZERO)).real)


phi_one: Form = {(index,): gammas[index] for index in range(14)}
phi_two: Form = {
    pair: gammas[pair[0]] @ gammas[pair[1]]
    for pair in combinations(range(14), 2)
}


def raw_source_pieces(
    curvature: Form,
    one: Form = phi_one,
    two: Form = phi_two,
) -> tuple[Form, Form]:
    first = wedge(one, hodge(curvature))
    second = hodge(
        wedge(
            one,
            hodge(wedge(two, hodge(curvature))),
        )
    )
    return first, second


def raw_source(
    curvature: Form,
    one: Form = phi_one,
    two: Form = phi_two,
) -> Form:
    first, second = raw_source_pieces(curvature, one, two)
    return add_forms(first, scale_form(second, -0.5))


def grade_three_source(
    curvature: Form,
    one: Form = phi_one,
    two: Form = phi_two,
) -> Form:
    return project_form(raw_source(curvature, one, two))


def trace_line_source(
    curvature: Form,
    one: Form = phi_one,
    two: Form = phi_two,
    trace: np.ndarray = trace_gamma,
) -> Form:
    return project_form(left_multiply(trace, raw_source(curvature, one, two)))


hodge_plant: Form = {(0, 1): IDENTITY.copy()}
check(
    "the sparse Hodge implementation realizes the native and hostile star-square signs",
    form_relative(hodge(hodge(hodge_plant)), scale_form(hodge_plant, -1.0)) < TOL
    and form_relative(
        hodge(hodge(hodge_plant, raw_eta), raw_eta),
        hodge_plant,
    )
    < TOL,
)

print("\nB. Non-Riemannian witness and pointwise Levi-Civita/Riemann closure")
generic_curvature: Form = {(0, 1): gammas[2] @ gammas[3]}
generic_s3 = grade_three_source(generic_curvature)
generic_trace = trace_line_source(generic_curvature)
check(
    "the native grade-three source is nonzero on a non-Riemannian witness",
    form_norm(generic_s3) > 1.0e-3,
    f"norm={form_norm(generic_s3):.6g}",
)
check(
    "non-Riemannian source outputs are degree 13, native Krein-skew, and right-H linear",
    form_degree(generic_s3) == 13
    and form_degree(generic_trace) == 13
    and form_krein_defect(generic_s3) < TOL
    and form_krein_defect(generic_trace) < TOL
    and form_h_defect(generic_s3) < TOL
    and form_h_defect(generic_trace) < TOL,
)
check(
    "a final extra Hodge is detected as the wrong degree-one object",
    form_degree(hodge(generic_s3)) == 1,
)


NATIVE_DIMENSION = 14
native_metric_matrix = np.diag(eta)


def constant_riemann_tensor(sectional: float = 1.0) -> np.ndarray:
    return sectional * (
        np.einsum(
            "ac,bd->abcd",
            native_metric_matrix,
            native_metric_matrix,
        )
        - np.einsum(
            "ad,bc->abcd",
            native_metric_matrix,
            native_metric_matrix,
        )
    )


def traceless_ricci_riemann_tensor() -> tuple[np.ndarray, np.ndarray]:
    ricci_zero = np.zeros((NATIVE_DIMENSION, NATIVE_DIMENSION))
    ricci_zero[0, 0] = 1.0
    ricci_zero[1, 1] = -1.0
    riemann = (
        np.einsum(
            "ac,bd->abcd",
            native_metric_matrix,
            ricci_zero,
        )
        - np.einsum(
            "ad,bc->abcd",
            native_metric_matrix,
            ricci_zero,
        )
        - np.einsum(
            "bc,ad->abcd",
            native_metric_matrix,
            ricci_zero,
        )
        + np.einsum(
            "bd,ac->abcd",
            native_metric_matrix,
            ricci_zero,
        )
    ) / (NATIVE_DIMENSION - 2)
    return riemann, ricci_zero


def pure_weyl_riemann_tensor() -> np.ndarray:
    """Diagonal Weyl plant on four positive native directions."""
    result = np.zeros(
        (
            NATIVE_DIMENSION,
            NATIVE_DIMENSION,
            NATIVE_DIMENSION,
            NATIVE_DIMENSION,
        )
    )
    sectionals = {
        (0, 1): 1.0,
        (0, 2): -1.0,
        (0, 4): 0.0,
        (1, 2): 0.0,
        (1, 4): -1.0,
        (2, 4): 1.0,
    }
    for (left, right), value in sectionals.items():
        result[left, right, left, right] = value
        result[right, left, left, right] = -value
        result[left, right, right, left] = -value
        result[right, left, right, left] = value
    return result


def riemann_defects(riemann: np.ndarray) -> tuple[float, float]:
    symmetry = max(
        max_abs(riemann + riemann.swapaxes(0, 1)),
        max_abs(riemann + riemann.swapaxes(2, 3)),
        max_abs(riemann - riemann.transpose(2, 3, 0, 1)),
    )
    bianchi = max_abs(
        riemann
        + riemann.transpose(0, 2, 3, 1)
        + riemann.transpose(0, 3, 1, 2)
    )
    return symmetry, bianchi


def ricci_and_scalar(riemann: np.ndarray) -> tuple[np.ndarray, float]:
    ricci = np.einsum(
        "ac,abcd->bd",
        native_metric_matrix,
        riemann,
        optimize=True,
    )
    scalar = float(
        np.einsum(
            "bd,bd",
            native_metric_matrix,
            ricci,
            optimize=True,
        )
    )
    return ricci, scalar


def spin_curvature_form(riemann: np.ndarray) -> Form:
    """F_ab=(1/4)R_cdab gamma^c gamma^d, using antisymmetry in c,d."""
    result: Form = {}
    for external_left, external_right in combinations(
        range(NATIVE_DIMENSION),
        2,
    ):
        value = ZERO.copy()
        for clifford_left, clifford_right in combinations(
            range(NATIVE_DIMENSION),
            2,
        ):
            coefficient = 0.5 * riemann[
                clifford_left,
                clifford_right,
                external_left,
                external_right,
            ]
            if coefficient:
                value += coefficient * phi_two[
                    (clifford_left, clifford_right)
                ]
        result[(external_left, external_right)] = value
    return result


def antisymmetric_component(form: Form, left: int, right: int) -> np.ndarray:
    if left == right:
        return ZERO
    if left < right:
        return form[(left, right)]
    return -form[(right, left)]


def gamma_one_contraction(curvature: Form) -> Form:
    """C_b=gamma^a F_ab; its grade-three part is the Bianchi channel."""
    return {
        (right,): sum(
            (
                gammas[left]
                @ antisymmetric_component(curvature, left, right)
                for left in range(NATIVE_DIMENSION)
            ),
            ZERO.copy(),
        )
        for right in range(NATIVE_DIMENSION)
    }


def predicted_ricci_contraction(ricci: np.ndarray) -> Form:
    return {
        (right,): 0.5
        * sum(
            (
                ricci[right, clifford] * gammas[clifford]
                for clifford in range(NATIVE_DIMENSION)
            ),
            ZERO.copy(),
        )
        for right in range(NATIVE_DIMENSION)
    }


def gamma_two_contraction(curvature: Form) -> np.ndarray:
    """Direct gamma^{ab}F_ab in the N4a raised-gamma convention."""
    return sum(
        (
            phi_two[(left, right)] @ curvature[(left, right)]
            for left, right in combinations(
                range(NATIVE_DIMENSION),
                2,
            )
        ),
        ZERO.copy(),
    )


def source_hodge_two_contraction(curvature: Form) -> np.ndarray:
    """The source formula's Hodge-normalized two-gamma contraction."""
    contracted = hodge(wedge(phi_two, hodge(curvature)))
    if set(contracted) != {()}:
        raise AssertionError("two-gamma contraction did not produce a 0-form")
    return contracted[()]


traceless_riemann, planted_ricci_zero = (
    traceless_ricci_riemann_tensor()
)
riemann_tensors = {
    "scalar": constant_riemann_tensor(),
    "traceless-Ricci": traceless_riemann,
    "Weyl": pure_weyl_riemann_tensor(),
}
riemann_curvatures: dict[str, Form] = {}
riemann_raw_sources: dict[str, Form] = {}
riemann_s3_sources: dict[str, Form] = {}
riemann_first_piece_norms: dict[str, float] = {}
riemann_second_piece_norms: dict[str, float] = {}
riemann_scalars: dict[str, float] = {}
riemann_ricci: dict[str, np.ndarray] = {}

for label, riemann in riemann_tensors.items():
    symmetry_defect, bianchi_defect = riemann_defects(riemann)
    ricci, scalar = ricci_and_scalar(riemann)
    curvature = spin_curvature_form(riemann)
    one_contraction = gamma_one_contraction(curvature)
    predicted_one = predicted_ricci_contraction(ricci)
    two_contraction = gamma_two_contraction(curvature)
    source_two_contraction = source_hodge_two_contraction(curvature)
    scalar_matrix_coefficient = complex(
        np.trace(two_contraction) / two_contraction.shape[0]
    )
    two_scalar_defect = float(
        np.linalg.norm(
            two_contraction
            - scalar_matrix_coefficient * IDENTITY
        )
    )
    source_scalar_coefficient = complex(
        np.trace(source_two_contraction)
        / source_two_contraction.shape[0]
    )
    source_two_scalar_defect = float(
        np.linalg.norm(
            source_two_contraction
            - source_scalar_coefficient * IDENTITY
        )
    )
    first_piece, second_piece = raw_source_pieces(curvature)
    raw_value = add_forms(first_piece, scale_form(second_piece, -0.5))
    s3_value = project_form(raw_value)

    riemann_curvatures[label] = curvature
    riemann_raw_sources[label] = raw_value
    riemann_s3_sources[label] = s3_value
    riemann_first_piece_norms[label] = form_norm(first_piece)
    riemann_second_piece_norms[label] = form_norm(second_piece)
    riemann_scalars[label] = scalar
    riemann_ricci[label] = ricci

    check(
        f"{label} plant has all algebraic Riemann symmetries and first Bianchi",
        symmetry_defect < TOL and bianchi_defect < TOL,
        f"symmetry={symmetry_defect:.3e}, Bianchi={bianchi_defect:.3e}",
    )
    check(
        f"{label}: gamma^a F_ab reduces exactly to one-half Ricci times gamma",
        form_relative(one_contraction, predicted_one) < TOL,
        f"residual={form_relative(one_contraction, predicted_one):.3e}",
    )
    check(
        f"{label}: gamma-ab F_ab has no grade-four or grade-two remainder",
        two_scalar_defect < TOL
        and abs(scalar_matrix_coefficient.real + scalar / 4.0) < TOL
        and abs(scalar_matrix_coefficient.imag) < TOL,
        (
            f"scalar={scalar_matrix_coefficient.real:.6g}, "
            f"nonscalar={two_scalar_defect:.3e}"
        ),
    )
    check(
        f"{label}: the source Hodge contraction is likewise purely scalar",
        source_two_scalar_defect < TOL,
        (
            f"scalar={source_scalar_coefficient.real:.6g}, "
            f"nonscalar={source_two_scalar_defect:.3e}"
        ),
    )
    check(
        f"{label}: the surviving grade-one pieces are killed by pi_sp",
        form_norm(project_form(first_piece)) < TOL
        and form_norm(project_form(second_piece)) < TOL
        and form_norm(s3_value) < TOL,
        (
            f"pi(first)={form_norm(project_form(first_piece)):.3e}, "
            f"pi(second)={form_norm(project_form(second_piece)):.3e}, "
            f"S3={form_norm(s3_value):.3e}"
        ),
    )

check(
    "the three plants independently isolate scalar, traceless-Ricci, and Weyl curvature",
    np.linalg.norm(
        riemann_ricci["scalar"]
        - riemann_scalars["scalar"]
        * native_metric_matrix
        / NATIVE_DIMENSION
    )
    < TOL
    and abs(riemann_scalars["scalar"]) > 1.0
    and abs(riemann_scalars["traceless-Ricci"]) < TOL
    and max_abs(
        riemann_ricci["traceless-Ricci"]
        - planted_ricci_zero
    )
    < TOL
    and np.linalg.norm(riemann_ricci["Weyl"]) < TOL
    and np.linalg.norm(riemann_tensors["Weyl"]) > 1.0e-3,
)
algebraic_riemann_dimension = (
    NATIVE_DIMENSION**2 * (NATIVE_DIMENSION**2 - 1) // 12
)
scalar_irrep_dimension = 1
traceless_ricci_irrep_dimension = (
    NATIVE_DIMENSION * (NATIVE_DIMENSION + 1) // 2 - 1
)
weyl_irrep_dimension = (
    (NATIVE_DIMENSION + 2)
    * (NATIVE_DIMENSION + 1)
    * NATIVE_DIMENSION
    * (NATIVE_DIMENSION - 3)
    // 12
)
check(
    "scalar plus traceless-Ricci plus Weyl exhaust the algebraic-Riemann representation",
    algebraic_riemann_dimension
    == scalar_irrep_dimension
    + traceless_ricci_irrep_dimension
    + weyl_irrep_dimension
    == 3185,
    (
        f"{scalar_irrep_dimension}+{traceless_ricci_irrep_dimension}"
        f"+{weyl_irrep_dimension}={algebraic_riemann_dimension}"
    ),
)
check(
    "scalar and traceless-Ricci plants power the raw-zero-versus-projected-zero distinction",
    form_norm(riemann_raw_sources["scalar"]) > 1.0e-3
    and form_norm(riemann_raw_sources["traceless-Ricci"]) > 1.0e-3
    and riemann_first_piece_norms["traceless-Ricci"] > 1.0e-3
    and riemann_second_piece_norms["scalar"] > 1.0e-3,
    (
        f"raw scalar={form_norm(riemann_raw_sources['scalar']):.6g}, "
        "raw Ric0="
        f"{form_norm(riemann_raw_sources['traceless-Ricci']):.6g}"
    ),
)

constant_curvature = riemann_curvatures["scalar"]
constant_raw = riemann_raw_sources["scalar"]
constant_s3 = riemann_s3_sources["scalar"]
constant_trace = trace_line_source(constant_curvature)
check(
    "the DeWitt trace-line adapter reopens a nonzero smaller-stabilizer source",
    form_norm(constant_trace) > 1.0e-3
    and form_krein_defect(constant_trace) < TOL
    and form_h_defect(constant_trace) < TOL,
    f"norm={form_norm(constant_trace):.6g}",
)


# ---------------------------------------------------------------------------
# C. Native cyclic/transgression test and ordering plants
# ---------------------------------------------------------------------------


print("\nC. RB2 cyclic identity on deterministic seeded native fixtures")


def clifford_monomial(indices: tuple[int, ...]) -> np.ndarray:
    return matrix_product([gammas[index] for index in indices])


grade_two_basis = [
    clifford_monomial(pair)
    for pair in (
        (0, 1),
        (0, 4),
        (1, 5),
        (2, 7),
        (3, 8),
        (4, 9),
        (5, 10),
        (6, 11),
        (7, 12),
        (8, 13),
    )
]
grade_three_basis = [
    clifford_monomial(triple)
    for triple in (
        (0, 1, 2),
        (0, 4, 10),
        (1, 5, 11),
        (2, 6, 12),
        (3, 7, 13),
        (4, 8, 9),
        (5, 9, 12),
        (6, 10, 13),
        (1, 8, 11),
        (2, 9, 13),
    )
]
native_theta_basis = grade_two_basis + grade_three_basis
check(
    "all planted grade-two/three coefficients are native sp(32,32;H)",
    max(np.linalg.norm(krein_adjoint(value) + value) for value in native_theta_basis)
    < TOL
    and max(h_defect(value) for value in native_theta_basis) < TOL,
)


def random_native_one_form(
    rng: np.random.Generator,
    scale: float,
) -> Form:
    external = rng.choice(14, size=8, replace=False)
    result: Form = {}
    for index in external:
        raw = (
            rng.standard_normal(IDENTITY.shape)
            + 1j * rng.standard_normal(IDENTITY.shape)
        )
        result[(int(index),)] = scale * project_sp(project_right_h(raw))
    return result


def make_fixture(seed: int) -> tuple[Form, Form]:
    rng = np.random.default_rng(seed)
    return (
        random_native_one_form(rng, 0.11),
        random_native_one_form(rng, 0.07),
    )


fixtures = [make_fixture(seed) for seed in CYCLIC_SEEDS]
heldout_fixture = make_fixture(HELDOUT_SEED)
check(
    "every deterministic theta and variation is Krein-skew and right-H linear",
    max(
        max(form_krein_defect(theta), form_krein_defect(delta))
        for theta, delta in fixtures + [heldout_fixture]
    )
    < TOL
    and max(
        max(form_h_defect(theta), form_h_defect(delta))
        for theta, delta in fixtures + [heldout_fixture]
    )
    < TOL,
)


def quadratic(theta: Form) -> Form:
    return wedge(theta, theta)


def quadratic_derivative(theta: Form, delta: Form) -> Form:
    return add_forms(wedge(delta, theta), wedge(theta, delta))


def cubic_action(theta: Form, source: Source) -> float:
    return top_pair(theta, source(quadratic(theta)))


def exact_cubic_derivative(theta: Form, delta: Form, source: Source) -> float:
    return (
        top_pair(delta, source(quadratic(theta)))
        + top_pair(theta, source(quadratic_derivative(theta, delta)))
    )


def finite_cubic_derivative(
    theta: Form,
    delta: Form,
    source: Source,
    step: float = 1.0e-6,
) -> float:
    plus = add_forms(theta, scale_form(delta, step))
    minus = add_forms(theta, scale_form(delta, -step))
    return (cubic_action(plus, source) - cubic_action(minus, source)) / (
        2.0 * step
    )


def naive_cyclic_current(theta: Form, delta: Form, source: Source) -> float:
    return 3.0 * top_pair(delta, source(quadratic(theta)))


def cyclic_gap(theta: Form, delta: Form, source: Source) -> tuple[float, float, float]:
    exact = exact_cubic_derivative(theta, delta, source)
    naive = naive_cyclic_current(theta, delta, source)
    gap = abs(exact - naive) / max(1.0e-12, abs(exact), abs(naive))
    return exact, naive, gap


grade_three_gaps = [
    cyclic_gap(theta, delta, grade_three_source)
    for theta, delta in fixtures
]
trace_gaps = [
    cyclic_gap(theta, delta, trace_line_source)
    for theta, delta in fixtures
]
finite_trace_derivatives = [
    finite_cubic_derivative(theta, delta, trace_line_source)
    for theta, delta in fixtures
]
check(
    "the exact cubic derivative agrees with central finite differences on every trace-line fixture",
    all(
        relative_scalar(finite, exact) < FD_TOL
        for finite, (exact, _naive, _gap) in zip(
            finite_trace_derivatives,
            trace_gaps,
        )
    ),
    "max residual="
    + f"{max(relative_scalar(f, e[0]) for f, e in zip(finite_trace_derivatives, trace_gaps)):.3e}",
)
check(
    "the native grade-three formula fails the naive RB2 cyclic current on every nondegenerate fixture",
    all(
        gap > CYCLIC_GAP_FLOOR
        and max(abs(exact), abs(naive)) > 1.0e-3
        for exact, naive, gap in grade_three_gaps
    ),
    "gaps=" + np.array2string(np.array([row[2] for row in grade_three_gaps]), precision=3),
)
check(
    "the trace-line adapter also fails the naive RB2 cyclic current on every nondegenerate fixture",
    all(
        gap > CYCLIC_GAP_FLOOR
        and max(abs(exact), abs(naive)) > 1.0e-3
        for exact, naive, gap in trace_gaps
    ),
    "gaps=" + np.array2string(np.array([row[2] for row in trace_gaps]), precision=3),
)


def ordered_trace_source(curvature: Form, column: int) -> Form:
    first, second = raw_source_pieces(curvature)
    ordered = (
        left_multiply(trace_gamma, first),
        right_multiply(first, trace_gamma),
        left_multiply(trace_gamma, second),
        right_multiply(second, trace_gamma),
    )[column]
    return project_form(ordered)


ordering_residual = np.array(
    [
        [
            exact_cubic_derivative(
                theta,
                delta,
                lambda curvature, column=column: ordered_trace_source(
                    curvature,
                    column,
                ),
            )
            - naive_cyclic_current(
                theta,
                delta,
                lambda curvature, column=column: ordered_trace_source(
                    curvature,
                    column,
                ),
            )
            for column in range(4)
        ]
        for theta, delta in fixtures
    ]
)
ordering_singular = np.linalg.svd(ordering_residual, compute_uv=False)
ordering_rank = int(
    np.linalg.matrix_rank(
        ordering_residual,
        tol=max(ordering_singular) * 1.0e-10,
    )
)
check(
    "the left/right first/second four-ordering family has no sampled nonzero universal cyclic fit",
    ordering_rank == 4
    and ordering_singular[-1] / ordering_singular[0] > 1.0e-5,
    (
        f"rank={ordering_rank}, singular="
        f"{np.array2string(ordering_singular, precision=3)}"
    ),
)

_u_order, _s_order, vh_order = np.linalg.svd(
    ordering_residual,
    full_matrices=False,
)
least_bad_coefficients = vh_order[-1]
heldout_ordering_residual = np.array(
    [
        exact_cubic_derivative(
            heldout_fixture[0],
            heldout_fixture[1],
            lambda curvature, column=column: ordered_trace_source(
                curvature,
                column,
            ),
        )
        - naive_cyclic_current(
            heldout_fixture[0],
            heldout_fixture[1],
            lambda curvature, column=column: ordered_trace_source(
                curvature,
                column,
            ),
        )
        for column in range(4)
    ]
)
heldout_least_bad = float(heldout_ordering_residual @ least_bad_coefficients)
check(
    "the ordering-fit held-out fixture rejects even the training least-singular ordering",
    abs(heldout_least_bad) > 1.0e-3,
    f"residual={heldout_least_bad:.6g}",
)


print("\nC2. Restricted grade-two/three first-pass audit")


def random_restricted_one_form(
    rng: np.random.Generator,
    scale: float,
) -> Form:
    external = rng.choice(14, size=8, replace=False)
    result: Form = {}
    for position, index in enumerate(external):
        matrix = ZERO.copy()
        for offset in range(3):
            basis_index = int(rng.integers(0, len(native_theta_basis)))
            matrix += (
                float(rng.normal())
                * native_theta_basis[
                    (basis_index + position + offset)
                    % len(native_theta_basis)
                ]
            )
        result[(int(index),)] = scale * matrix
    return result


def make_restricted_fixture(seed: int) -> tuple[Form, Form]:
    rng = np.random.default_rng(seed)
    return (
        random_restricted_one_form(rng, 0.11),
        random_restricted_one_form(rng, 0.07),
    )


restricted_fixtures = [
    make_restricted_fixture(seed)
    for seed in CYCLIC_SEEDS
]
restricted_heldout = make_restricted_fixture(HELDOUT_SEED)
restricted_grade_three_gaps = [
    cyclic_gap(theta, delta, grade_three_source)
    for theta, delta in restricted_fixtures
]
restricted_ordering_residual = np.array(
    [
        [
            exact_cubic_derivative(
                theta,
                delta,
                lambda curvature, column=column: ordered_trace_source(
                    curvature,
                    column,
                ),
            )
            - naive_cyclic_current(
                theta,
                delta,
                lambda curvature, column=column: ordered_trace_source(
                    curvature,
                    column,
                ),
            )
            for column in range(4)
        ]
        for theta, delta in restricted_fixtures
    ]
)
(
    _restricted_u,
    restricted_singular,
    restricted_vh,
) = np.linalg.svd(restricted_ordering_residual, full_matrices=False)
restricted_rank = int(
    np.linalg.matrix_rank(
        restricted_ordering_residual,
        tol=restricted_singular[0] * 1.0e-10,
    )
)
restricted_null = restricted_vh[-1]
restricted_null /= max(abs(restricted_null))
if restricted_null[np.argmax(abs(restricted_null))] < 0:
    restricted_null *= -1.0
restricted_training_null = float(
    np.linalg.norm(restricted_ordering_residual @ restricted_null)
)
restricted_heldout_row = np.array(
    [
        exact_cubic_derivative(
            restricted_heldout[0],
            restricted_heldout[1],
            lambda curvature, column=column: ordered_trace_source(
                curvature,
                column,
            ),
        )
        - naive_cyclic_current(
            restricted_heldout[0],
            restricted_heldout[1],
            lambda curvature, column=column: ordered_trace_source(
                curvature,
                column,
            ),
        )
        for column in range(4)
    ]
)
restricted_heldout_null = float(restricted_heldout_row @ restricted_null)
check(
    "the first restricted grade-two/three suite does not support the earlier cyclic-failure claim",
    max(row[2] for row in restricted_grade_three_gaps) < CYCLIC_GAP_FLOOR,
    (
        "gaps="
        + np.array2string(
            np.array([row[2] for row in restricted_grade_three_gaps]),
            precision=3,
        )
    ),
)
check(
    "its rank-three ordering null is a finite-training accident rejected by the held-out restricted fixture",
    restricted_rank == 3
    and restricted_training_null < TOL
    and abs(restricted_heldout_null) > 1.0e-3,
    (
        f"rank={restricted_rank}, null="
        f"{np.array2string(restricted_null, precision=6)}, "
        f"training={restricted_training_null:.3e}, "
        f"heldout={restricted_heldout_null:.6g}"
    ),
)


# ---------------------------------------------------------------------------
# D. Canonical polarization: constructive adjacent geometry, then factor gate
# ---------------------------------------------------------------------------


print("\nD. Canonical polarized Euler-covector comparator")


def raw_trilinear(
    first: Form,
    second: Form,
    third: Form,
    source: Source = trace_line_source,
) -> float:
    return top_pair(first, source(wedge(second, third)))


def polarized_trilinear(
    first: Form,
    second: Form,
    third: Form,
    source: Source = trace_line_source,
) -> float:
    entries = (first, second, third)
    return float(
        sum(
            raw_trilinear(
                entries[order[0]],
                entries[order[1]],
                entries[order[2]],
                source,
            )
            for order in permutations(range(3))
        )
        / 6.0
    )


polarized_values = [
    polarized_trilinear(delta, theta, theta)
    for theta, delta in fixtures
]
polarized_derivative_residuals = [
    relative_scalar(
        finite,
        3.0 * polarized,
    )
    for finite, polarized in zip(finite_trace_derivatives, polarized_values)
]
check(
    "the canonical full polarization is nonzero and satisfies the cubic derivative identity by construction",
    max(abs(value) for value in polarized_values) > 1.0e-3
    and max(polarized_derivative_residuals) < FD_TOL,
    (
        f"max-value={max(abs(value) for value in polarized_values):.6g}, "
        f"max-residual={max(polarized_derivative_residuals):.3e}"
    ),
)
check(
    "the polarized trilinear comparator is permutation-symmetric on a planted triple",
    max(
        abs(
            polarized_trilinear(
                (fixtures[0][1], fixtures[0][0], fixtures[1][0])[order[0]],
                (fixtures[0][1], fixtures[0][0], fixtures[1][0])[order[1]],
                (fixtures[0][1], fixtures[0][0], fixtures[1][0])[order[2]],
            )
            - polarized_trilinear(
                fixtures[0][1],
                fixtures[0][0],
                fixtures[1][0],
            )
        )
        for order in permutations(range(3))
    )
    < TOL,
)

rotor_generator = gammas[0] @ gammas[1]
rotor_parameter = 0.173
rotor = (
    np.cos(rotor_parameter) * IDENTITY
    + np.sin(rotor_parameter) * rotor_generator
)
rotor_inverse = np.linalg.inv(rotor)
check(
    "the homogeneous covariance plant is an honest native K-unitary right-H rotor",
    max_abs(rotor.conj().T @ krein @ rotor - krein) < TOL
    and h_defect(rotor) < TOL
    and max_abs(rotor @ rotor_inverse - IDENTITY) < TOL,
)

rotated_phi_one = adjoint_form(rotor, phi_one)
rotated_phi_two = adjoint_form(rotor, phi_two)
rotated_trace_gamma = rotor @ trace_gamma @ rotor_inverse


def rotated_trace_source(curvature: Form) -> Form:
    return trace_line_source(
        curvature,
        rotated_phi_one,
        rotated_phi_two,
        rotated_trace_gamma,
    )


covariance_theta, covariance_delta = fixtures[0]
covariance_theta_g = adjoint_form(rotor, covariance_theta)
covariance_delta_g = adjoint_form(rotor, covariance_delta)
covariance_curvature = quadratic(covariance_theta)
covariance_source_g = rotated_trace_source(
    adjoint_form(rotor, covariance_curvature)
)
covariance_source_expected = adjoint_form(
    rotor,
    trace_line_source(covariance_curvature),
)
polarized_before = polarized_trilinear(
    covariance_delta,
    covariance_theta,
    covariance_theta,
)
polarized_after = polarized_trilinear(
    covariance_delta_g,
    covariance_theta_g,
    covariance_theta_g,
    rotated_trace_source,
)
check(
    "one finite moving-data native homogeneous-covariance proxy passes",
    form_relative(covariance_source_g, covariance_source_expected) < TOL
    and relative_scalar(polarized_after, polarized_before) < TOL,
    (
        f"source={form_relative(covariance_source_g, covariance_source_expected):.3e}, "
        f"scalar={relative_scalar(polarized_after, polarized_before):.3e}"
    ),
)


def monomial_one_form(external: int, matrix: np.ndarray) -> Form:
    return {(external,): matrix}


# The two internal coefficients are distinct commuting bivectors, so their
# polarized curvature is exactly zero.  The x-suite is twelve generic
# full-adjoint one-forms from the six deterministic seeded fixtures.  A
# nonzero polarized covector on any x proves that it cannot depend on
# polarized curvature alone.
factor_matrix_y = clifford_monomial((0, 1))
factor_matrix_z = clifford_monomial((2, 3))
factor_y = monomial_one_form(0, factor_matrix_y)
factor_z = monomial_one_form(1, factor_matrix_z)
factor_x_suite = [
    candidate
    for theta_value, delta_value in fixtures
    for candidate in (theta_value, delta_value)
]
polarized_curvature_zero = scale_form(
    add_forms(wedge(factor_y, factor_z), wedge(factor_z, factor_y)),
    0.5,
)
factor_obstruction_values = np.array(
    [
        polarized_trilinear(candidate, factor_y, factor_z)
        for candidate in factor_x_suite
    ]
)
check(
    "the planted pair has exactly zero polarized curvature",
    form_norm(polarized_curvature_zero) < TOL,
    f"norm={form_norm(polarized_curvature_zero):.3e}",
)
check(
    "the canonical polarized covector does not factor through one linear curvature-to-source map",
    max(abs(factor_obstruction_values)) > 1.0e-3,
    (
        "zero-curvature current values="
        + np.array2string(factor_obstruction_values, precision=3)
    ),
)


# ---------------------------------------------------------------------------
# E. Typed disposition
# ---------------------------------------------------------------------------


print("\nE. Typed disposition")
check(
    "S3 is killed on every algebraic-Riemann irrep, not as a generic full-adjoint map",
    all(form_norm(value) < TOL for value in riemann_s3_sources.values())
    and form_norm(generic_s3) > 1.0e-3,
)
check(
    "the trace-line adapter remains pre-RB1 because it fails cyclicity despite reopening the carrier",
    form_norm(constant_trace) > 1.0e-3
    and all(row[2] > CYCLIC_GAP_FLOOR for row in trace_gaps),
)
check(
    "the polarized comparator is a viable different Euler-covector geometry but not a linear S(Lambda2) reentry",
    max(polarized_derivative_residuals) < FD_TOL
    and max(abs(factor_obstruction_values)) > 1.0e-3,
)

if FAILURES:
    print(f"\nCONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("\nVERDICT: NATIVE-GRADE3-NO-REENTRY-AS-WRITTEN")
print("S3: NONZERO-ON-NON-RIEMANNIAN-WITNESS; ZERO-ON-ALL-ALGEBRAIC-RIEMANN-IRREPS")
print("TRACE-LINE: CARRIER-REOPENED-AT-DEWITT-STABILIZER; RB2-CYCLIC-GATE-FAILED")
print("POLARIZATION: NONZERO-EULER-COVECTOR; ONE-FINITE-COVARIANCE-PROXY-PASS")
print("FACTORIZATION: NO-SINGLE-LINEAR-S(LAMBDA2)-REPRESENTATIVE-IN-PLANTED-FIXTURE")
print("REENTRY: NONE; RB1/RB2 SOURCE RECORDS UNCHANGED")
print("NONCLAIM: NO ACTION/VEV/MASS/INDEX/COUNT/COSMOLOGICAL PREDICTION")
print("ALL CONTROLS PASSED")
