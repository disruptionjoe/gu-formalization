#!/usr/bin/env python3
r"""RB6: target-blind source-concomitant spectral grammar.

This probe tests a deliberately frozen pointwise grammar on the actual
vertical fibre

    Sym^2(T*X),  dim = 10,

at the deterministic W177 gimmel-curvature point.  The fibre pairing is the
trace-reversed DeWitt form of signature (6,4).  Every adjoint below is the
indefinite DeWitt adjoint.

Layer 0 is strict:

* H is a source concomitant, not a physical fluctuation Hessian.
* Q is a commutator concomitant, not charge conjugation or a Dirac operator.
* A spectral rank or degeneracy is not a particle, index, or family count.
* The finite W177 background is nonstationary in the already-declared ambient
  Yang--Mills sector, so no physical mass spectrum is read here.

The admissible words and zero threshold are printed before any spectrum is
evaluated.  The W177 curvature words are geometry-owned on its explicitly
conditional ambient branch; they are not thereby the complete source-action
answer.  Distortion and section words whose values are absent are checked only
as action-owned formulas/types and are not spectrally evaluated.  No desired
subspace, selected eigenvector, particle label, or count datum enters a
candidate.  The raw Frobenius form and planted spectral/polar fixtures are
controls only and are excluded from the source grammar.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import w177_ym_residual_and_mode_closure_probe as w177  # noqa: E402


TOL = 2.0e-7
ZERO_THRESHOLD = 1.0e-7
# W177's finite-difference Ricci/curvature words split exact degeneracies at
# roughly 1e-6.  This coarser threshold is used only for stabilizer and
# commutator-rank claims, never to manufacture a spectral sign.
CONCOMITANT_RESOLUTION = 2.0e-5
FAILURES: list[str] = []
CHECK_COUNT = 0
IDENTITY10 = np.eye(10)


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value))) if value.size else 0.0


def fro(value: np.ndarray) -> float:
    return float(np.linalg.norm(value))


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    status = "PASS" if bool(condition) else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def inertia(symmetric: np.ndarray, tolerance: float = TOL) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(0.5 * (symmetric + symmetric.T))
    scale = max(1.0, float(np.max(np.abs(values))))
    cut = tolerance * scale
    return (
        int(np.sum(values > cut)),
        int(np.sum(values < -cut)),
        int(np.sum(np.abs(values) <= cut)),
    )


def metric_adjoint(matrix: np.ndarray, metric: np.ndarray) -> np.ndarray:
    return np.linalg.solve(metric, matrix.T @ metric)


def relative_defect(left: np.ndarray, right: np.ndarray) -> float:
    return fro(left - right) / max(1.0, fro(right))


def signed_frame(metric: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(0.5 * (metric + metric.T))
    order = np.concatenate(
        [np.flatnonzero(eigenvalues > 0.0), np.flatnonzero(eigenvalues < 0.0)]
    )
    values = eigenvalues[order]
    frame = eigenvectors[:, order] / np.sqrt(np.abs(values))
    signed_metric = np.diag(np.sign(values))
    return frame, signed_metric


def raw_frobenius_metric(base_metric: np.ndarray) -> np.ndarray:
    inverse = np.linalg.inv(base_metric)
    raised = [inverse @ element for element in w177.EBASIS]
    return np.array(
        [
            [float(np.trace(left @ right)) for right in raised]
            for left in raised
        ]
    )


def trace_involution(base_metric: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return the trace-line projector and the trace/traceless involution."""
    inverse = np.linalg.inv(base_metric)
    trace_covector = np.array(
        [float(np.trace(inverse @ element)) for element in w177.EBASIS]
    )
    base_components = w177.comps_of(base_metric)
    trace_line = 0.25 * np.outer(base_components, trace_covector)
    involution = IDENTITY10 - 2.0 * trace_line
    return trace_line, involution


def curvature_square(
    riemann_low: np.ndarray,
    inverse_metric: np.ndarray,
) -> np.ndarray:
    r"""B_IJ = R_IABC R_J^ABC with all three contractions ambient."""
    return np.einsum(
        "iabc,jdef,ad,be,cf->ij",
        riemann_low,
        riemann_low,
        inverse_metric,
        inverse_metric,
        inverse_metric,
        optimize=True,
    )


def vertical_curvature_square(
    riemann_low: np.ndarray,
    inverse_vertical_metric: np.ndarray,
) -> np.ndarray:
    """The equally canonical contraction with every contracted leg vertical."""
    vertical = riemann_low[4:, 4:, 4:, 4:]
    return np.einsum(
        "iabc,jdef,ad,be,cf->ij",
        vertical,
        vertical,
        inverse_vertical_metric,
        inverse_vertical_metric,
        inverse_vertical_metric,
        optimize=True,
    )


@dataclass(frozen=True)
class FrozenWord:
    name: str
    expression: str


@dataclass
class SpectralReport:
    name: str
    adjoint_defect: float
    matrix_rank: int
    real_branch: bool
    diagonalizable: bool
    gap: float
    negative_dimension: int
    negative_inertia: tuple[int, int, int] | None
    eigenvalues: np.ndarray
    stabilizer_dimension: int


@dataclass
class PolarReport:
    name: str
    skew_defect: float
    matrix_norm: float
    matrix_rank: int
    smallest_singular_value: float
    branch: str
    minus_square_eigenvalues: np.ndarray


# These tables are the pre-spectrum freeze.  They contain only source-owned
# tensors and canonical operations listed in the RB6 run plan.
H_WORDS = (
    FrozenWord("identity", "id"),
    FrozenWord("trace_involution", "trace_involution"),
    FrozenWord("ricci_sharp", "gv_inverse @ ricci_vv"),
    FrozenWord(
        "einstein_sharp",
        "gv_inverse @ ricci_vv - (scalar_curvature / 2) * id",
    ),
    FrozenWord(
        "restricted_ambient_tracefree_ricci_sharp",
        "gv_inverse @ ricci_vv - (scalar_curvature / 14) * id",
    ),
    FrozenWord(
        "vertical_tracefree_ricci_sharp",
        "ricci_sharp - (trace(ricci_sharp) / 10) * id",
    ),
    FrozenWord(
        "curvature_square_sharp",
        "gv_inverse @ curvature_square_vv",
    ),
    FrozenWord(
        "vertical_curvature_square_sharp",
        "gv_inverse @ vertical_curvature_square_vv",
    ),
)

Q_WORDS = (
    FrozenWord(
        "ricci_trace_commutator",
        "commutator(ricci_sharp, trace_involution)",
    ),
    FrozenWord(
        "ricci_curvature_square_commutator",
        "commutator(ricci_sharp, curvature_square_sharp)",
    ),
    FrozenWord(
        "trace_curvature_square_commutator",
        "commutator(trace_involution, curvature_square_sharp)",
    ),
    FrozenWord(
        "ricci_vertical_curvature_square_commutator",
        "commutator(ricci_sharp, vertical_curvature_square_sharp)",
    ),
    FrozenWord(
        "trace_vertical_curvature_square_commutator",
        "commutator(trace_involution, vertical_curvature_square_sharp)",
    ),
)

ACTION_TYPE_WORDS = (
    FrozenWord(
        "theta_gram_sharp_type",
        "gv_inverse @ (theta @ kappa @ theta.T)",
    ),
    FrozenWord(
        "distortion_gram_sharp_type",
        "gv_inverse @ (distortion_v @ kappa @ distortion_v.T)",
    ),
    FrozenWord(
        "curvature_gram_sharp_type",
        "gv_inverse @ contract(gv_inverse, curvature_v, kappa)",
    ),
    FrozenWord(
        "conditional_second_form_square_type",
        "second_form @ metric_adjoint(second_form, gv)",
    ),
)

FORBIDDEN_IDENTIFIERS = {
    "u",
    "P_W",
    "J",
    "Omega_C",
    "epsilon_flag",
    "gamma",
    "hypercharge",
    "P3",
}
FORBIDDEN_PHRASES = (
    "chosen 6+4 block",
    "rank four",
    "selected eigenvectors",
    "standard model",
)


def word_is_target_blind(word: FrozenWord) -> bool:
    identifiers = set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", word.expression))
    lowered = word.expression.lower()
    return (
        identifiers.isdisjoint(FORBIDDEN_IDENTIFIERS)
        and all(phrase not in lowered for phrase in FORBIDDEN_PHRASES)
    )


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def algebra_generators(signed_metric: np.ndarray) -> list[np.ndarray]:
    signs = np.diag(signed_metric)
    generators: list[np.ndarray] = []
    for left in range(len(signs)):
        for right in range(left + 1, len(signs)):
            generator = np.zeros_like(signed_metric)
            generator[left, right] = 1.0
            generator[right, left] = -signs[left] / signs[right]
            generators.append(generator)
    return generators


def stabilizer_dimension(
    matrix: np.ndarray,
    frame: np.ndarray,
    signed_metric: np.ndarray,
) -> int:
    """Dimension of the infinitesimal O(6,4) centralizer of one word."""
    in_frame = np.linalg.solve(frame, matrix @ frame)
    columns = np.column_stack(
        [
            commutator(generator, in_frame).reshape(-1)
            for generator in algebra_generators(signed_metric)
        ]
    )
    singular_values = np.linalg.svd(columns, compute_uv=False)
    scale = max(1.0, float(np.max(singular_values)))
    rank = int(np.sum(singular_values > CONCOMITANT_RESOLUTION * scale))
    return columns.shape[1] - rank


def spectral_report(
    name: str,
    matrix: np.ndarray,
    metric: np.ndarray,
    frame: np.ndarray,
    signed_metric: np.ndarray,
) -> SpectralReport:
    adjoint_defect = relative_defect(metric_adjoint(matrix, metric), matrix)
    values, vectors = np.linalg.eig(matrix)
    real_branch = max_abs(values.imag) < 3.0e-6
    vector_rank = np.linalg.matrix_rank(vectors, tol=2.0e-7)
    diagonalizable = vector_rank == matrix.shape[0]
    if real_branch:
        real_values = values.real
        gap = float(np.min(np.abs(real_values)))
        negative = real_values < -ZERO_THRESHOLD
        negative_dimension = int(np.sum(negative))
        if negative_dimension:
            # Near-degenerate real operators can be returned as tiny complex
            # conjugate pairs.  Taking real parts alone drops half of such a
            # real invariant plane.  Recover its real span before measuring
            # the restricted indefinite inertia.
            selected = vectors[:, negative]
            real_span = np.column_stack([selected.real, selected.imag])
            left, singular_values, _right = np.linalg.svd(
                real_span, full_matrices=False
            )
            span_rank = int(
                np.sum(
                    singular_values
                    > 2.0e-7 * max(1.0, float(np.max(singular_values)))
                )
            )
            basis = left[:, :span_rank]
            negative_inertia = inertia(basis.T @ metric @ basis, 2.0e-6)
        else:
            negative_inertia = (0, 0, 0)
    else:
        real_values = values
        gap = float("nan")
        negative_dimension = -1
        negative_inertia = None
    return SpectralReport(
        name=name,
        adjoint_defect=adjoint_defect,
        matrix_rank=int(np.linalg.matrix_rank(matrix, tol=ZERO_THRESHOLD)),
        real_branch=real_branch,
        diagonalizable=diagonalizable,
        gap=gap,
        negative_dimension=negative_dimension,
        negative_inertia=negative_inertia,
        eigenvalues=np.asarray(real_values),
        stabilizer_dimension=stabilizer_dimension(
            matrix, frame, signed_metric
        ),
    )


def polar_report(name: str, matrix: np.ndarray, metric: np.ndarray) -> PolarReport:
    skew_defect = relative_defect(metric_adjoint(matrix, metric), -matrix)
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    smallest = float(np.min(singular_values))
    scale = max(1.0, float(np.max(singular_values)))
    matrix_rank = int(
        np.sum(singular_values > CONCOMITANT_RESOLUTION * scale)
    )
    minus_square = -matrix @ matrix
    values, vectors = np.linalg.eig(minus_square)
    if matrix_rank < matrix.shape[0]:
        branch = "SINGULAR"
    elif max_abs(values.imag) >= 3.0e-6:
        branch = "NONREAL-MINUS-SQUARE"
    elif np.linalg.matrix_rank(vectors, tol=2.0e-7) < matrix.shape[0]:
        branch = "NONDIAGONALIZABLE"
    elif float(np.min(values.real)) <= ZERO_THRESHOLD:
        branch = "NO-POSITIVE-REAL-BRANCH"
    else:
        branch = "POLAR-ADMISSIBLE"
    return PolarReport(
        name=name,
        skew_defect=skew_defect,
        matrix_norm=fro(matrix),
        matrix_rank=matrix_rank,
        smallest_singular_value=smallest,
        branch=branch,
        minus_square_eigenvalues=values,
    )


def sorted_spectrum(matrix: np.ndarray) -> np.ndarray:
    values = np.linalg.eigvals(matrix)
    return np.array(sorted(values, key=lambda item: (item.real, item.imag)))


def identity_trace_fit(
    matrix: np.ndarray,
    trace_word: np.ndarray,
) -> tuple[np.ndarray, float]:
    design = np.column_stack([IDENTITY10.reshape(-1), trace_word.reshape(-1)])
    coefficients, _residuals, _rank, _singular = np.linalg.lstsq(
        design, matrix.reshape(-1), rcond=None
    )
    fitted = coefficients[0] * IDENTITY10 + coefficients[1] * trace_word
    return coefficients, relative_defect(matrix, fitted)


def main() -> int:
    print("=" * 96)
    print("A. PRE-SPECTRUM FREEZE AND LAYER-0 TYPE GATE")
    print("=" * 96)
    print(f"Frozen zero threshold: {ZERO_THRESHOLD:.1e}")
    for word in H_WORDS + Q_WORDS + ACTION_TYPE_WORDS:
        print(f"FROZEN: {word.name} := {word.expression}")
    check(
        "every frozen candidate expression clears the forbidden-symbol gate",
        all(
            word_is_target_blind(word)
            for word in H_WORDS + Q_WORDS + ACTION_TYPE_WORDS
        ),
    )
    check(
        "every frozen adapter terminates in End(Sym2 T*X)",
        all("sharp" in word.name or word.name in {"identity", "trace_involution"}
            for word in H_WORDS)
        and all("commutator" in word.name for word in Q_WORDS),
        "all outputs are real 10x10 endomorphisms",
    )
    info(
        "The candidate tables are now frozen.  Ranks, signs, and spectra have "
        "not yet been read."
    )

    print("\n" + "=" * 96)
    print("B. GEOMETRY-OWNED W177 BRANCH AND TRACE REVERSAL")
    print("=" * 96)
    hvec = w177.fixed_w177_point()
    base_metric = w177.vmat(hvec)
    metric, _partial_metric, _connection, riemann_low = w177.riemann_data(
        hvec, 1.0e-5, 1.0e-4
    )
    inverse_metric = np.linalg.inv(metric)
    vertical_metric = metric[4:, 4:]
    inverse_vertical_metric = np.linalg.inv(vertical_metric)
    raw_metric = raw_frobenius_metric(base_metric)
    frame, signed_metric = signed_frame(vertical_metric)
    trace_line, trace_word = trace_involution(base_metric)

    check(
        "actual trace-reversed vertical metric has signature (6,4)",
        inertia(vertical_metric) == (6, 4, 0),
        str(inertia(vertical_metric)),
    )
    check(
        "raw Frobenius hostile comparator has signature (7,3)",
        inertia(raw_metric) == (7, 3, 0),
        str(inertia(raw_metric)),
    )
    check(
        "signed frame realizes the native indefinite metric",
        max_abs(frame.T @ vertical_metric @ frame - signed_metric) < 2.0e-9,
    )
    check(
        "trace-line map is a projector and the trace involution squares to identity",
        max_abs(trace_line @ trace_line - trace_line) < 2.0e-9
        and max_abs(trace_word @ trace_word - IDENTITY10) < 2.0e-9,
    )
    check(
        "trace involution is DeWitt-self-adjoint",
        relative_defect(
            metric_adjoint(trace_word, vertical_metric), trace_word
        )
        < 2.0e-9,
    )

    ricci = w177.ricci_from_riemann(metric, riemann_low)
    ricci_symmetry_defect = relative_defect(ricci, ricci.T)
    ricci_covariant = 0.5 * (ricci + ricci.T)
    scalar_curvature = float(np.trace(inverse_metric @ ricci_covariant))
    ricci_vertical = ricci_covariant[4:, 4:]
    square_full = curvature_square(riemann_low, inverse_metric)
    square_full = 0.5 * (square_full + square_full.T)
    square_vertical = vertical_curvature_square(
        riemann_low, inverse_vertical_metric
    )
    square_vertical = 0.5 * (square_vertical + square_vertical.T)

    h_values: dict[str, np.ndarray] = {
        "identity": IDENTITY10,
        "trace_involution": trace_word,
        "ricci_sharp": inverse_vertical_metric @ ricci_vertical,
        "einstein_sharp": (
            inverse_vertical_metric @ ricci_vertical
            - 0.5 * scalar_curvature * IDENTITY10
        ),
        "restricted_ambient_tracefree_ricci_sharp": (
            inverse_vertical_metric @ ricci_vertical
            - (scalar_curvature / 14.0) * IDENTITY10
        ),
        "vertical_tracefree_ricci_sharp": (
            inverse_vertical_metric @ ricci_vertical
            - (
                np.trace(inverse_vertical_metric @ ricci_vertical) / 10.0
            )
            * IDENTITY10
        ),
        "curvature_square_sharp": (
            inverse_vertical_metric @ square_full[4:, 4:]
        ),
        "vertical_curvature_square_sharp": (
            inverse_vertical_metric @ square_vertical
        ),
    }
    check(
        "numerical Ricci symmetry projection is below the finite-difference floor",
        ricci_symmetry_defect < 2.0e-5,
        f"relative raw defect {ricci_symmetry_defect:.3e}",
    )
    check(
        "all frozen H adapters produced finite real 10x10 endomorphisms",
        set(h_values) == {word.name for word in H_WORDS}
        and all(
            value.shape == (10, 10)
            and np.isrealobj(value)
            and np.all(np.isfinite(value))
            for value in h_values.values()
        ),
    )

    q_values: dict[str, np.ndarray] = {
        "ricci_trace_commutator": commutator(
            h_values["ricci_sharp"], trace_word
        ),
        "ricci_curvature_square_commutator": commutator(
            h_values["ricci_sharp"], h_values["curvature_square_sharp"]
        ),
        "trace_curvature_square_commutator": commutator(
            trace_word, h_values["curvature_square_sharp"]
        ),
        "ricci_vertical_curvature_square_commutator": commutator(
            h_values["ricci_sharp"],
            h_values["vertical_curvature_square_sharp"],
        ),
        "trace_vertical_curvature_square_commutator": commutator(
            trace_word, h_values["vertical_curvature_square_sharp"]
        ),
    }
    check(
        "all frozen Q adapters produced finite real 10x10 endomorphisms",
        set(q_values) == {word.name for word in Q_WORDS}
        and all(
            value.shape == (10, 10)
            and np.isrealobj(value)
            and np.all(np.isfinite(value))
            for value in q_values.values()
        ),
    )
    info(
        "Only the vertical bundle is canonical here.  The horizontal "
        "projection and curvature words that use it remain conditional on "
        "the W177 ambient branch.  Under its declared A0=spinlift(nabla_gimmel) "
        "ambient-Yang--Mills identification, the all-leg and vertical-only "
        "curvature squares are also the corresponding evaluable action-owned "
        "curvature Gram words, up to invariant-pairing normalization."
    )

    print("\n" + "=" * 96)
    print("B2. ACTION-OWNED FORMULA/TYPE CONTROLS (VALUES ABSENT)")
    print("=" * 96)
    type_rng = np.random.default_rng(2026073101)
    internal_metric = np.diag([1.0, 1.0, 1.0, -1.0, -1.0])
    theta_fixture = type_rng.normal(size=(10, 5))
    distortion_fixture = type_rng.normal(size=(10, 5))
    curvature_fixture = type_rng.normal(size=(10, 10, 5))
    curvature_fixture = 0.5 * (
        curvature_fixture - curvature_fixture.transpose(1, 0, 2)
    )
    second_form_fixture = type_rng.normal(size=(10, 10))
    theta_bilinear = theta_fixture @ internal_metric @ theta_fixture.T
    distortion_bilinear = (
        distortion_fixture @ internal_metric @ distortion_fixture.T
    )
    curvature_bilinear = np.einsum(
        "kl,ika,jlb,ab->ij",
        inverse_vertical_metric,
        curvature_fixture,
        curvature_fixture,
        internal_metric,
        optimize=True,
    )
    action_type_values = {
        "theta_gram_sharp_type": inverse_vertical_metric @ theta_bilinear,
        "distortion_gram_sharp_type": (
            inverse_vertical_metric @ distortion_bilinear
        ),
        "curvature_gram_sharp_type": (
            inverse_vertical_metric @ curvature_bilinear
        ),
        "conditional_second_form_square_type": (
            second_form_fixture
            @ metric_adjoint(second_form_fixture, vertical_metric)
        ),
    }
    check(
        "coframe, distortion, and curvature Gram formulas type to DeWitt-self-adjoint endomorphisms",
        all(
            value.shape == (10, 10)
            and relative_defect(
                metric_adjoint(value, vertical_metric), value
            )
            < 2.0e-9
            for name, value in action_type_values.items()
            if name != "conditional_second_form_square_type"
        ),
    )
    check(
        "conditional second-form adjoint square types to a DeWitt-self-adjoint endomorphism",
        action_type_values["conditional_second_form_square_type"].shape
        == (10, 10)
        and relative_defect(
            metric_adjoint(
                action_type_values["conditional_second_form_square_type"],
                vertical_metric,
            ),
            action_type_values["conditional_second_form_square_type"],
        )
        < 2.0e-9,
    )
    planted_commutators = [
        commutator(left, right)
        for index, left in enumerate(action_type_values.values())
        for right in list(action_type_values.values())[index + 1 :]
    ]
    check(
        "commutators of the formula-grade self-adjoint controls are DeWitt-skew",
        max(
            relative_defect(
                metric_adjoint(value, vertical_metric), -value
            )
            for value in planted_commutators
        )
        < 2.0e-9,
        "finite witnesses of [A,B]^dag = -[A,B]",
    )
    info(
        "These are planted type witnesses only.  The coframe/distortion/"
        "curvature values, stationary solution, reduction, and the "
        "normal-to-vertical graph identification needed to evaluate them are "
        "absent.  No spectrum is read from these fixtures."
    )

    print("\n" + "=" * 96)
    print("C. POST-FREEZE H SPECTRA, SIGNATURES, AND AMBIGUITY")
    print("=" * 96)
    h_reports = [
        spectral_report(
            word.name,
            h_values[word.name],
            vertical_metric,
            frame,
            signed_metric,
        )
        for word in H_WORDS
    ]
    for report in h_reports:
        displayed = np.round(report.eigenvalues, 8)
        info(
            f"H {report.name}: adjoint_defect={report.adjoint_defect:.3e}, "
            f"matrix_rank={report.matrix_rank}, real={report.real_branch}, "
            f"diagonalizable={report.diagonalizable}, gap={report.gap:.8g}, "
            f"negative_dimension={report.negative_dimension}, "
            f"negative_inertia={report.negative_inertia}, "
            f"so(6,4)_centralizer_dim={report.stabilizer_dimension}, "
            f"eigenvalues={displayed}"
        )
    check(
        "every geometry-owned H word is DeWitt-self-adjoint",
        max(report.adjoint_defect for report in h_reports) < TOL,
        f"max defect {max(report.adjoint_defect for report in h_reports):.3e}",
    )
    check(
        "every geometry-owned H word lies on a real diagonalizable finite branch",
        all(report.real_branch and report.diagonalizable for report in h_reports),
    )

    nontrivial_reports = [
        report
        for report in h_reports
        if report.name not in {"identity", "trace_involution"}
    ]
    negative_profiles = {
        (report.negative_dimension, report.negative_inertia)
        for report in nontrivial_reports
    }
    check(
        "canonical scalar shifts or contractions yield incompatible negative sectors",
        len(negative_profiles) > 1,
        f"profiles={sorted(negative_profiles, key=str)}",
    )
    expected_fits = {
        "ricci_sharp": np.array([-0.5, -0.75]),
        "curvature_square_sharp": np.array([0.875, 1.125]),
        "vertical_curvature_square_sharp": np.array([0.75, 0.75]),
    }
    fit_details = {}
    for name, expected in expected_fits.items():
        coefficients, defect = identity_trace_fit(h_values[name], trace_word)
        fit_details[name] = (coefficients, defect)
        info(
            f"{name} fit to a*identity+b*trace_involution: "
            f"(a,b)={np.round(coefficients, 9)}, residual={defect:.3e}"
        )
    check(
        "Ricci and both curvature-square contractions reduce to the predicted identity/trace span at the FD floor",
        all(
            max_abs(fit_details[name][0] - expected) < 2.0e-6
            and fit_details[name][1] < 2.0e-6
            for name, expected in expected_fits.items()
        ),
    )
    check(
        "no frozen H word yields a gapped four-dimensional negative-definite sector",
        not any(
            report.gap > ZERO_THRESHOLD
            and report.negative_dimension == 4
            and report.negative_inertia == (0, 4, 0)
            for report in h_reports
        ),
        "post-read kill; spectral dimension is not a count",
    )
    source_gapped = [
        report.name
        for report in nontrivial_reports
        if report.real_branch and report.gap > ZERO_THRESHOLD
    ]
    info(f"Nontrivial geometry words with a finite zero gap: {source_gapped}")

    # A coordinate-basis change checks that the endomorphism adapters transform
    # by similarity and that the displayed spectra are not coordinate artefacts.
    rng = np.random.default_rng(20260731)
    basis_change = np.eye(10) + 0.04 * rng.normal(size=(10, 10))
    changed_metric = basis_change.T @ vertical_metric @ basis_change
    inverse_change = np.linalg.inv(basis_change)
    covariance_defects = []
    spectral_defects = []
    for value in h_values.values():
        changed_value = inverse_change @ value @ basis_change
        covariance_defects.append(
            relative_defect(
                metric_adjoint(changed_value, changed_metric), changed_value
            )
        )
        spectral_defects.append(
            max_abs(sorted_spectrum(changed_value) - sorted_spectrum(value))
        )
    check(
        "all H words retain their indefinite adjoint and spectrum under fibre-basis covariance",
        max(covariance_defects) < TOL and max(spectral_defects) < 2.0e-8,
        f"adjoint={max(covariance_defects):.3e}, spectrum={max(spectral_defects):.3e}",
    )

    print("\n" + "=" * 96)
    print("D. POST-FREEZE COMMUTATOR WORDS AND POLAR GATE")
    print("=" * 96)
    q_reports = [
        polar_report(word.name, q_values[word.name], vertical_metric)
        for word in Q_WORDS
    ]
    for report in q_reports:
        info(
            f"Q {report.name}: skew_defect={report.skew_defect:.3e}, "
            f"norm={report.matrix_norm:.3e}, "
            f"matrix_rank={report.matrix_rank}, "
            f"smallest_singular={report.smallest_singular_value:.3e}, "
            f"branch={report.branch}, "
            f"spectrum(-Q^2)={np.round(report.minus_square_eigenvalues, 8)}"
        )
    check(
        "every commutator word is DeWitt-skew",
        max(report.skew_defect for report in q_reports) < TOL,
        f"max defect {max(report.skew_defect for report in q_reports):.3e}",
    )
    check(
        "all geometry-owned commutators are unresolved from zero at the W177 FD floor",
        all(
            report.matrix_rank == 0
            and report.matrix_norm < CONCOMITANT_RESOLUTION
            for report in q_reports
        ),
        "the fitted identity/trace representatives commute exactly",
    )
    polar_eligible = [
        report.name
        for report in q_reports
        if report.branch == "POLAR-ADMISSIBLE"
    ]
    info(
        "Geometry-owned commutators clearing the positive-real polar gate: "
        f"{polar_eligible}"
    )

    q_covariance_defects = []
    for value in q_values.values():
        changed_value = inverse_change @ value @ basis_change
        q_covariance_defects.append(
            relative_defect(
                metric_adjoint(changed_value, changed_metric), -changed_value
            )
        )
    check(
        "all Q words retain their indefinite skew adjoint under fibre-basis covariance",
        max(q_covariance_defects) < TOL,
        f"max defect {max(q_covariance_defects):.3e}",
    )

    print("\n" + "=" * 96)
    print("E. HOSTILE AND PLANTED CLASSIFIER CONTROLS")
    print("=" * 96)
    raw_ricci_sharp = np.linalg.solve(raw_metric, ricci_vertical)
    musical_difference = relative_defect(
        raw_ricci_sharp,
        h_values["ricci_sharp"],
    )
    check(
        "raw Frobenius and native DeWitt musicals produce different Ricci-sharp words",
        musical_difference > 1.0e-2,
        f"relative musical difference {musical_difference:.3e}",
    )
    check(
        "raw (7,3) inertia fails the even-even orthogonal polar precondition",
        inertia(raw_metric)[:2] == (7, 3),
    )

    # A source-independent gapped diagonal word checks the spectral classifier.
    planted_diagonal = np.diag(
        [-2.4, -1.1, 0.35, 0.9, 1.8, 2.7, -0.65, 0.55, 1.4, 2.2]
    )
    planted_h = frame @ planted_diagonal @ np.linalg.inv(frame)
    planted_h_report = spectral_report(
        "planted_gapped_control",
        planted_h,
        vertical_metric,
        frame,
        signed_metric,
    )
    check(
        "planted spectral control is self-adjoint, real, diagonalizable, and gapped",
        planted_h_report.adjoint_defect < TOL
        and planted_h_report.real_branch
        and planted_h_report.diagonalizable
        and planted_h_report.gap > 0.3,
        f"gap {planted_h_report.gap:.3f}",
    )

    # A block-rotation on every same-sign pair is an invertible DeWitt-skew
    # positive control for the polar classifier.  It is not a source candidate.
    planted_rotation = np.zeros((10, 10))
    for left in (0, 2, 4, 6, 8):
        right = left + 1
        planted_rotation[left, right] = -1.0
        planted_rotation[right, left] = 1.0
    planted_q = frame @ planted_rotation @ np.linalg.inv(frame)
    planted_q_report = polar_report(
        "planted_polar_control", planted_q, vertical_metric
    )
    singular_rotation = planted_rotation.copy()
    singular_rotation[8:10, 8:10] = 0.0
    singular_q = frame @ singular_rotation @ np.linalg.inv(frame)
    singular_q_report = polar_report(
        "planted_singular_control", singular_q, vertical_metric
    )
    check(
        "planted invertible skew control clears the polar classifier",
        planted_q_report.skew_defect < TOL
        and planted_q_report.branch == "POLAR-ADMISSIBLE",
        planted_q_report.branch,
    )
    check(
        "planted singular skew control is rejected",
        singular_q_report.skew_defect < TOL
        and singular_q_report.branch == "SINGULAR",
        singular_q_report.branch,
    )
    info(
        "The planted invertible control proves only that the algebraic polar "
        "branch is nonempty.  It is excluded from the source grammar and "
        "supports no genericity or ownership claim."
    )

    print("\n" + "=" * 96)
    print("F. W177 STATIONARITY PRECONDITION (IMPORTED CONTROL)")
    print("=" * 96)
    stationarity = w177.evaluate_scale(hvec, 1.0)
    check(
        "W177 geometry background reproduces the prior nonzero ambient YM residual",
        abs(stationarity.residual_norm - 3.19904) < 0.02,
        f"||D_A*F_A||={stationarity.residual_norm:.8f}",
    )
    check(
        "the residual remains separated from its contracted-Bianchi comparison floor",
        stationarity.residual_norm
        > 100.0 * max(stationarity.bianchi_defect, 1.0e-12),
        f"floor={stationarity.bianchi_defect:.3e}",
    )
    info(
        "Therefore none of the H spectra above is read as a physical Hessian "
        "or mass spectrum on this background."
    )

    print("\n" + "=" * 96)
    print("G. VERDICT")
    print("=" * 96)
    if polar_eligible:
        verdict = (
            "GEOMETRY-OWNED-CANDIDATE-POLAR-BRANCH-FOUND-BUT-NONUNIQUE-AND-"
            "NONSTATIONARY; ACTION-OWNED-FORMULAS-TYPED-BUT-UNEVALUATED"
        )
    else:
        verdict = (
            "GEOMETRY-OWNED-BUT-NONSELECTING; "
            "SPECTRAL-OWNERSHIP-BLOCKED-BY-AMBIGUITY-AND-POLAR-FAILURE; "
            "ACTION-OWNED-FORMULAS-TYPED-BUT-UNEVALUATED"
        )
    print(f"VERDICT: {verdict}")
    print(
        "The target-blind conditional geometry does construct typed "
        "DeWitt-self-adjoint H words and DeWitt-skew commutators; its two "
        "curvature-square words are also conditionally action-owned ambient-YM "
        "Gram operators.  The other action-owned distortion/section formulas "
        "are type-complete but lack values.  Canonical shifts/contractions do not select one common "
        "negative sector.  Polar eligibility is reported exactly above.  "
        "The W177 nonstationarity gate remains shut."
    )
    print(
        "NONCLAIMS: no Standard Model group, compactification, VEV, mass, "
        "cosmological value, anomaly, index, generation, or count is inferred."
    )

    if FAILURES:
        print(f"FAILED checks: {FAILURES}")
        return 1
    print(f"PASS: all {CHECK_COUNT} RB6 checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
