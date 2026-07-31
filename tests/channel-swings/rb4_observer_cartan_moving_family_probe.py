#!/usr/bin/env python3
r"""RB4: moving observer/Cartan family and the separate moving-t question.

This finite deterministic probe keeps six objects distinct before computing:

1. ``u`` is a unit timelike vector on the four-dimensional Lorentz base.
2. ``t = h_tr`` is the canonical DeWitt-negative trace line in
   ``Sym^2(T*X)``.  Every induced base Lorentz transformation fixes this line.
3. ``P_W(u)`` is the observer-dependent negative four-plane

       W4(u) = R h_tr + (u^flat symmetric-product u^perp).

   It is a representative vertical maximal-compact/Cartan reduction.  That
   name alone does not identify a physical Pati--Salam reduction.
4. ``epsilon`` below is only the finite vertical Clifford soldering map
   ``v -> c(v)`` and its transported frame.  Passing its covariance test does
   not construct or source the full moving field epsilon_IG.
5. An internal Spin(4) rotation of the selected W4 plane can move ``t``.
   That is not an induced base Lorentz transformation: it takes the canonical
   trace vector away from the canonical trace line unless ``t`` is explicitly
   promoted to a transported spurion/order parameter.
6. A compatible complex structure ``J`` is an additional reduction.  The
   native even-even signature (6,4) admits orthogonal complex structures,
   whereas the raw odd-odd signature (7,3) does not.  No ``J`` is selected by
   the DeWitt metric, trace projector, or observer ``u``: the fixed-u SO(3)
   stabilizer produces a path/frame ambiguity.

The native metric is GU's trace-reversed DeWitt form.  The raw Frobenius form
is retained only as a hostile control: it has signature (7,3) and makes the
trace line positive, whereas the native fibre has signature (6,4) and makes
the trace line negative.

The probe establishes:

* exact joint covariance
  ``P_W(Lambda^-1 u) = Sym2(Lambda) P_W(u) Sym2(Lambda)^-1`` in the convention
  ``h -> Lambda^T h Lambda``;
* rank, complement, signature, orientation, Clifford, volume, and fixed-u
  stabilizer checks;
* failure of a planted frozen-projector/frozen-soldering construction;
* covariance of the conditional RB3b ``Phi`` family when the observer split,
  volumes, Clifford frame, and arguments are transported together;
* separately, covariance under internal Spin(4) rotations moving ``t`` only
  when ``t`` is explicitly transported, with a fixed-t hostile control;
* separately again, the optional compatible-complex-structure family
  ``(J,t,Jt)`` under joint O(6,4) transport, with fixed-J and fixed-u-
  stabilizer hostile controls.

NONCLAIMS: this is pointwise finite geometry.  It does not prove that the
observer reduction is derived, gauge, dynamical, or external; construct an
action selecting it; identify the compact group with the Standard Model;
construct the full epsilon_IG field; select a VEV; or make an index, mode,
generation, mass, stationarity, or cosmological claim.  In particular,
transporting a chosen J along a chosen Lambda is not a well-defined map
u -> J; an additional reduction is required.
"""

from __future__ import annotations

import contextlib
import io
from itertools import combinations
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
TESTS_ROOT = os.path.abspath(os.path.join(HERE, ".."))
if TESTS_ROOT not in sys.path:
    sys.path.insert(0, TESTS_ROOT)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

with contextlib.redirect_stdout(io.StringIO()):
    import full20_dewitt_loop_transport_probe as full20  # noqa: E402


TOL = 3.0e-8
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


def signature(matrix: np.ndarray) -> tuple[int, int, int]:
    hermitian = 0.5 * (matrix + matrix.conj().T)
    values = np.linalg.eigvalsh(hermitian)
    scale = max(1.0, float(np.max(np.abs(values))))
    threshold = TOL * scale
    return (
        int(np.sum(values > threshold)),
        int(np.sum(values < -threshold)),
        int(np.sum(np.abs(values) <= threshold)),
    )


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def matrix_exponential_series(matrix: np.ndarray, terms: int = 80) -> np.ndarray:
    """Deterministic small-matrix exponential without a SciPy dependency."""
    out = np.eye(matrix.shape[0], dtype=complex)
    term = out.copy()
    for order in range(1, terms + 1):
        term = term @ matrix / order
        out += term
    return out


ETA4 = full20.ETA4_MATRIX
FRAME10 = full20.DEWITT_FRAME
ETA10 = np.diag([1.0] * 6 + [-1.0] * 4)
GAMMA10 = full20.gamma_10
IDENTITY10 = np.eye(10)
IDENTITY32 = np.eye(32, dtype=complex)


def frame_components(tensor: np.ndarray) -> np.ndarray:
    return np.linalg.solve(
        FRAME10,
        full20.symmetric_components(tensor),
    )


def frame_tensor(components: np.ndarray) -> np.ndarray:
    return full20.symmetric_matrix(FRAME10 @ components)


def induced_sym2(change: np.ndarray) -> np.ndarray:
    """The action h -> change^T h change in the signed DeWitt frame."""
    return np.column_stack(
        [
            frame_components(change.T @ frame_tensor(np.eye(10)[:, index]) @ change)
            for index in range(10)
        ]
    )


def induced_sym2_generator(generator: np.ndarray) -> np.ndarray:
    return np.column_stack(
        [
            frame_components(
                generator.T @ frame_tensor(np.eye(10)[:, index])
                + frame_tensor(np.eye(10)[:, index]) @ generator
            )
            for index in range(10)
        ]
    )


def raw_frobenius_gram() -> np.ndarray:
    inverse = np.linalg.inv(ETA4)
    actions = [inverse @ basis for basis in full20.SYMMETRIC_BASIS]
    coordinate_gram = np.array(
        [
            [float(np.trace(left @ right)) for right in actions]
            for left in actions
        ]
    )
    return FRAME10.T @ coordinate_gram @ FRAME10


def observer_w_frame(
    observer: np.ndarray,
    spatial_frame: list[np.ndarray],
) -> np.ndarray:
    """A DeWitt-orthonormal frame of W4(observer), including h_tr."""
    observer_flat = ETA4 @ observer
    tensors = [-0.5 * ETA4]
    for vector in spatial_frame:
        vector_flat = ETA4 @ vector
        tensors.append(
            (
                np.outer(observer_flat, vector_flat)
                + np.outer(vector_flat, observer_flat)
            )
            / np.sqrt(2.0)
        )
    return np.column_stack([frame_components(tensor) for tensor in tensors])


def metric_projector(frame: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    restricted_gram = frame.T @ ETA10 @ frame
    projector = (
        frame
        @ np.linalg.inv(restricted_gram)
        @ frame.T
        @ ETA10
    )
    return projector, restricted_gram


def epsilon(vector: np.ndarray) -> np.ndarray:
    """The finite vertical Clifford soldering map in the fixed trivialization."""
    return sum(
        (float(vector[index]) * GAMMA10[index] for index in range(10)),
        np.zeros_like(GAMMA10[0]),
    )


def clifford_spin_generator(orthogonal_generator: np.ndarray) -> np.ndarray:
    """Lift an so(6,4) generator by solving its exact Clifford adjoint action."""
    spin_basis = []
    vector_actions = []
    signature_vector = np.diag(ETA10)
    for left, right in combinations(range(10), 2):
        spin = 0.25 * (
            GAMMA10[left] @ GAMMA10[right]
            - GAMMA10[right] @ GAMMA10[left]
        )
        action = np.zeros((10, 10), dtype=complex)
        for source in range(10):
            commutator = (
                spin @ GAMMA10[source] - GAMMA10[source] @ spin
            )
            for target in range(10):
                action[target, source] = (
                    np.trace(GAMMA10[target] @ commutator)
                    / (32.0 * signature_vector[target])
                )
        spin_basis.append(spin)
        vector_actions.append(action)

    action_matrix = np.column_stack(
        [action.reshape(-1) for action in vector_actions]
    )
    coefficients, _residuals, rank, _singular_values = np.linalg.lstsq(
        action_matrix,
        orthogonal_generator.reshape(-1),
        rcond=None,
    )
    check(
        "the induced so(6,4) generator has a unique Clifford spin lift",
        rank == len(spin_basis)
        and max_abs(
            (action_matrix @ coefficients).reshape(10, 10)
            - orthogonal_generator
        )
        < TOL,
    )
    return sum(
        (
            coefficient * spin
            for coefficient, spin in zip(coefficients, spin_basis)
        ),
        np.zeros_like(spin_basis[0]),
    )


def anticommuting_projection(
    matrix: np.ndarray,
    trace_gamma: np.ndarray,
) -> np.ndarray:
    return 0.5 * (
        matrix
        - trace_gamma @ matrix @ np.linalg.inv(trace_gamma)
    )


def phi(
    trace_gamma: np.ndarray,
    w_gamma: np.ndarray,
    volume_a: np.ndarray,
    volume_w: np.ndarray,
) -> np.ndarray:
    """The lambda=+1 conditional RB3b family."""
    return anticommuting_projection(
        volume_w @ w_gamma + volume_a @ w_gamma,
        trace_gamma,
    )


def standard_complex_structure(signature_blocks: tuple[int, int]) -> np.ndarray:
    """One orthogonal J when both signature counts are even."""
    positive, negative = signature_blocks
    if positive % 2 or negative % 2:
        raise ValueError("orthogonal complex structures require even p and q")
    out = np.zeros((positive + negative, positive + negative))
    for block_start, block_stop in (
        (0, positive),
        (positive, positive + negative),
    ):
        for left in range(block_start, block_stop, 2):
            right = left + 1
            out[left, right] = -1.0
            out[right, left] = 1.0
    return out


print("=" * 96)
print("A. LAYER 0: TRACE REVERSAL, OBSERVER W4, AND THE CARTAN PROJECTOR")
print("=" * 96)

dewitt_gram = FRAME10.T @ full20.dewitt_metric(ETA4) @ FRAME10
raw_gram = raw_frobenius_gram()
trace_coordinate = -np.eye(10)[:, 6]
check(
    "native trace-reversed DeWitt frame has signature (6,4)",
    signature(dewitt_gram) == (6, 4, 0)
    and max_abs(dewitt_gram - ETA10) < TOL,
    str(signature(dewitt_gram)),
)
check(
    "raw Frobenius hostile control has signature (7,3), not the native fibre",
    signature(raw_gram) == (7, 3, 0),
    str(signature(raw_gram)),
)
check(
    "h_tr is negative for DeWitt and positive for raw Frobenius",
    abs(float(trace_coordinate @ dewitt_gram @ trace_coordinate) + 1.0) < TOL
    and abs(float(trace_coordinate @ raw_gram @ trace_coordinate) - 1.0) < TOL,
)

observer0 = np.array([0.0, 0.0, 0.0, 1.0])
spatial0 = [np.eye(4)[:, index] for index in range(3)]
w_frame0 = observer_w_frame(observer0, spatial0)
projector_w0, gram_w0 = metric_projector(w_frame0)
projector_a0 = IDENTITY10 - projector_w0
a_frame0 = np.eye(10)[:, :6]
check(
    "u is unit timelike and its supplied spatial frame is u-perpendicular",
    abs(float(observer0 @ ETA4 @ observer0) + 1.0) < TOL
    and max(abs(float(observer0 @ ETA4 @ vector)) for vector in spatial0) < TOL,
)
check(
    "W4(u)=R h_tr plus u-flat symmetric-product u-perp is negative rank four",
    np.linalg.matrix_rank(w_frame0, tol=TOL) == 4
    and signature(gram_w0) == (0, 4, 0),
    f"signature {signature(gram_w0)}",
)
check(
    "P_W and its complement are DeWitt-self-adjoint orthogonal projectors of ranks 4 and 6",
    np.linalg.matrix_rank(projector_w0, tol=TOL) == 4
    and np.linalg.matrix_rank(projector_a0, tol=TOL) == 6
    and max_abs(projector_w0 @ projector_w0 - projector_w0) < TOL
    and max_abs(projector_a0 @ projector_a0 - projector_a0) < TOL
    and max_abs(projector_a0 @ projector_w0) < TOL
    and max_abs(projector_w0.T @ ETA10 - ETA10 @ projector_w0) < TOL,
)
check(
    "the W4 complement is positive rank six",
    signature(a_frame0.T @ ETA10 @ a_frame0) == (6, 0, 0),
)
info(
    "P_W is the finite representative of a vertical Cartan reduction. "
    "This does not by itself identify a physical compact or Pati--Salam "
    "reduction."
)


print("\n" + "=" * 96)
print("B. JOINT BASE-LORENTZ TRANSPORT AND HOSTILE FROZEN-PROJECTOR CONTROL")
print("=" * 96)

rapidity = 0.37
base_boost_generator = np.zeros((4, 4))
base_boost_generator[0, 3] = 1.0
base_boost_generator[3, 0] = 1.0
base_boost = np.eye(4)
base_boost[0, 0] = np.cosh(rapidity)
base_boost[3, 3] = np.cosh(rapidity)
base_boost[0, 3] = np.sinh(rapidity)
base_boost[3, 0] = np.sinh(rapidity)
sym2_boost = induced_sym2(base_boost)
sym2_boost_generator = induced_sym2_generator(base_boost_generator)
check(
    "the base boost is proper orthochronous and its Sym2 action is a proper DeWitt isometry",
    max_abs(base_boost.T @ ETA4 @ base_boost - ETA4) < TOL
    and np.linalg.det(base_boost) > 0.0
    and base_boost[3, 3] > 0.0
    and max_abs(sym2_boost.T @ ETA10 @ sym2_boost - ETA10) < TOL
    and abs(float(np.linalg.det(sym2_boost)) - 1.0) < TOL,
)
check(
    "finite Sym2 transport is the exponential of the induced generator",
    max_abs(
        matrix_exponential_series(rapidity * sym2_boost_generator)
        - sym2_boost
    )
    < TOL,
)

# With h -> Lambda^T h Lambda, vector representatives move by Lambda^-1.
inverse_boost = np.linalg.inv(base_boost)
observer1 = inverse_boost @ observer0
spatial1 = [inverse_boost @ vector for vector in spatial0]
w_frame1 = observer_w_frame(observer1, spatial1)
projector_w1, gram_w1 = metric_projector(w_frame1)
projector_a1 = IDENTITY10 - projector_w1
check(
    "the transported observer remains unit timelike with an orthonormal perpendicular frame",
    abs(float(observer1 @ ETA4 @ observer1) + 1.0) < TOL
    and max(abs(float(observer1 @ ETA4 @ vector)) for vector in spatial1) < TOL
    and max_abs(
        np.array(
            [
                [left @ ETA4 @ right for right in spatial1]
                for left in spatial1
            ]
        )
        - np.eye(3)
    )
    < TOL,
)
check(
    "the explicit W4(Lambda^-1 u) frame equals Sym2(Lambda) W4(u)",
    max_abs(w_frame1 - sym2_boost @ w_frame0) < TOL,
)
projector_covariance_defect = max_abs(
    projector_w1
    - sym2_boost @ projector_w0 @ np.linalg.inv(sym2_boost)
)
check(
    "P_W(Lambda^-1 u)=Sym2(Lambda) P_W(u) Sym2(Lambda)^-1",
    projector_covariance_defect < TOL,
    f"defect {projector_covariance_defect:.2e}",
)
check(
    "transport preserves W4/complement ranks and signatures",
    np.linalg.matrix_rank(projector_w1, tol=TOL) == 4
    and np.linalg.matrix_rank(projector_a1, tol=TOL) == 6
    and signature(gram_w1) == (0, 4, 0)
    and signature(
        (sym2_boost @ a_frame0).T
        @ ETA10
        @ (sym2_boost @ a_frame0)
    )
    == (6, 0, 0),
)

frozen_projector_residual = float(
    np.linalg.norm(
        projector_w0
        - sym2_boost @ projector_w0 @ np.linalg.inv(sym2_boost)
    )
)
check(
    "planted frozen W4 projector fails under a genuine base boost",
    frozen_projector_residual > 1.0,
    f"residual {frozen_projector_residual:.9f}",
)

rotation_angle = 0.41
base_rotation = np.eye(4)
base_rotation[0, 0] = np.cos(rotation_angle)
base_rotation[0, 1] = -np.sin(rotation_angle)
base_rotation[1, 0] = np.sin(rotation_angle)
base_rotation[1, 1] = np.cos(rotation_angle)
sym2_rotation = induced_sym2(base_rotation)
check(
    "the fixed-u spatial Spin(3) stabilizer preserves P_W exactly",
    max_abs(np.linalg.inv(base_rotation) @ observer0 - observer0) < TOL
    and max_abs(
        sym2_rotation @ projector_w0 @ np.linalg.inv(sym2_rotation)
        - projector_w0
    )
    < TOL,
)


print("\n" + "=" * 96)
print("C. ORIENTATION, CLIFFORD SOLDERING, VOLUMES, AND MOVING Phi")
print("=" * 96)

spin_boost_generator = clifford_spin_generator(sym2_boost_generator)
spin_boost = matrix_exponential_series(rapidity * spin_boost_generator)
spin_boost_inverse = np.linalg.inv(spin_boost)
moved_gammas = [
    epsilon(sym2_boost[:, index])
    for index in range(10)
]
check(
    "the spin lift transports every vertical Clifford generator with Sym2(Lambda)",
    max(
        max_abs(
            spin_boost @ GAMMA10[index] @ spin_boost_inverse
            - moved_gammas[index]
        )
        for index in range(10)
    )
    < TOL,
)
check(
    "the transported Clifford frame still realizes Cl(6,4)",
    max(
        max_abs(
            moved_gammas[left] @ moved_gammas[right]
            + moved_gammas[right] @ moved_gammas[left]
            - 2.0 * ETA10[left, right] * IDENTITY32
        )
        for left in range(10)
        for right in range(10)
    )
    < TOL,
)

generic_vector = np.array(
    [1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0, 9.0, -10.0]
)
check(
    "the finite vertical soldering obeys U epsilon(v) U^-1=epsilon(Sym2(Lambda)v)",
    max_abs(
        spin_boost @ epsilon(generic_vector) @ spin_boost_inverse
        - epsilon(sym2_boost @ generic_vector)
    )
    < TOL,
)
frozen_soldering_residual = max(
    np.linalg.norm(moved_gammas[index] - GAMMA10[index])
    for index in range(10)
)
check(
    "planted frozen Clifford/soldering frame fails for the moved observer split",
    frozen_soldering_residual > 0.1,
    f"max residual {frozen_soldering_residual:.9f}",
)

volume_a0 = matrix_product(GAMMA10[:6])
volume_w0 = matrix_product(GAMMA10[6:])
volume_10 = volume_a0 @ volume_w0
volume_a1 = matrix_product(moved_gammas[:6])
volume_w1 = matrix_product(moved_gammas[6:])
check(
    "proper transport preserves orientation and jointly transports A6/W4 volumes",
    np.linalg.det(sym2_boost) > 0.0
    and max_abs(
        volume_a1
        - spin_boost @ volume_a0 @ spin_boost_inverse
    )
    < TOL
    and max_abs(
        volume_w1
        - spin_boost @ volume_w0 @ spin_boost_inverse
    )
    < TOL
    and max_abs(volume_a1 @ volume_w1 - volume_10) < TOL,
)
check(
    "volume squares retain the native positive-six/negative-four types",
    max_abs(volume_a1 @ volume_a1 + IDENTITY32) < TOL
    and max_abs(volume_w1 @ volume_w1 - IDENTITY32) < TOL,
)

trace_gamma0 = GAMMA10[6]
trace_gamma1 = moved_gammas[6]
check(
    "base Lorentz transport moves P_W but fixes the canonical DeWitt trace line",
    frozen_projector_residual > 1.0
    and max_abs(trace_gamma1 - trace_gamma0) < TOL
    and max_abs(sym2_boost @ np.eye(10)[:, 6] - np.eye(10)[:, 6]) < TOL,
)
base_phi_defect = max(
    max_abs(
        spin_boost
        @ phi(trace_gamma0, GAMMA10[index], volume_a0, volume_w0)
        @ spin_boost_inverse
        - phi(
            trace_gamma1,
            moved_gammas[index],
            volume_a1,
            volume_w1,
        )
    )
    for index in range(6, 10)
)
check(
    "the conditional Phi family is covariant when split, volumes, Clifford frame, and w move together",
    base_phi_defect < TOL,
    f"defect {base_phi_defect:.2e}",
)
frozen_phi_residual = max(
    np.linalg.norm(
        spin_boost
        @ phi(trace_gamma0, GAMMA10[index], volume_a0, volume_w0)
        @ spin_boost_inverse
        - phi(
            trace_gamma0,
            moved_gammas[index],
            volume_a0,
            volume_w0,
        )
    )
    for index in range(6, 10)
)
check(
    "freezing the Cartan volumes while moving w breaks the planted Phi family",
    frozen_phi_residual > 1.0,
    f"max residual {frozen_phi_residual:.9f}",
)
info(
    "These checks construct the jointly moving finite family.  They do not "
    "supply the spacetime field epsilon_IG or decide who owns its variation."
)


print("\n" + "=" * 96)
print("D. SEPARATE INTERNAL Spin(4) TEST: MOVING t IS A SPURION/ORDER-PARAMETER BRANCH")
print("=" * 96)

# This compact rotation acts inside the already selected negative W4 plane.
# Unlike the induced base boost above, it moves the canonical trace vector.
internal_angle = 0.41
internal_moving_t_generator = 0.25 * (
    GAMMA10[6] @ GAMMA10[7] - GAMMA10[7] @ GAMMA10[6]
)
internal_moving_t = (
    np.cos(internal_angle / 2.0) * IDENTITY32
    + 2.0
    * np.sin(internal_angle / 2.0)
    * internal_moving_t_generator
)
internal_moving_t_inverse = np.linalg.inv(internal_moving_t)
internal_t1 = (
    internal_moving_t @ trace_gamma0 @ internal_moving_t_inverse
)
internal_w1 = [
    internal_moving_t @ GAMMA10[index] @ internal_moving_t_inverse
    for index in range(6, 10)
]
check(
    "the selected internal Spin(4) rotation preserves W4 and its volume but moves t",
    max_abs(
        internal_moving_t @ volume_w0 @ internal_moving_t_inverse
        - volume_w0
    )
    < TOL
    and max_abs(
        internal_moving_t @ volume_a0 @ internal_moving_t_inverse
        - volume_a0
    )
    < TOL
    and max_abs(internal_t1 - trace_gamma0) > 0.1,
)
internal_joint_defect = max(
    max_abs(
        internal_moving_t
        @ phi(trace_gamma0, GAMMA10[index], volume_a0, volume_w0)
        @ internal_moving_t_inverse
        - phi(internal_t1, internal_w1[index - 6], volume_a0, volume_w0)
    )
    for index in range(6, 10)
)
check(
    "internal Spin(4) covariance is restored when t and w are transported together",
    internal_joint_defect < TOL,
    f"defect {internal_joint_defect:.2e}",
)
internal_frozen_t_residual = max(
    np.linalg.norm(
        internal_moving_t
        @ phi(trace_gamma0, GAMMA10[index], volume_a0, volume_w0)
        @ internal_moving_t_inverse
        - phi(
            trace_gamma0,
            internal_w1[index - 6],
            volume_a0,
            volume_w0,
        )
    )
    for index in range(6, 10)
)
check(
    "planted fixed-t family fails for every non-stabilizer internal Spin(4) motion",
    internal_frozen_t_residual > 1.0,
    f"max residual {internal_frozen_t_residual:.9f}",
)

# A compact rotation among t-perpendicular W legs belongs to the fixed-t
# Spin(3) stabilizer and therefore does not require a t spurion.
internal_stabilizer_generator = 0.25 * (
    GAMMA10[7] @ GAMMA10[8] - GAMMA10[8] @ GAMMA10[7]
)
internal_stabilizer = (
    np.cos(internal_angle / 2.0) * IDENTITY32
    + 2.0
    * np.sin(internal_angle / 2.0)
    * internal_stabilizer_generator
)
internal_stabilizer_inverse = np.linalg.inv(internal_stabilizer)
check(
    "the fixed-t Spin(3) stabilizer remains covariant without moving t",
    max_abs(
        internal_stabilizer
        @ trace_gamma0
        @ internal_stabilizer_inverse
        - trace_gamma0
    )
    < TOL
    and max(
        max_abs(
            internal_stabilizer
            @ phi(trace_gamma0, GAMMA10[index], volume_a0, volume_w0)
            @ internal_stabilizer_inverse
            - phi(
                trace_gamma0,
                internal_stabilizer
                @ GAMMA10[index]
                @ internal_stabilizer_inverse,
                volume_a0,
                volume_w0,
            )
        )
        for index in range(6, 10)
    )
    < TOL,
)
info(
    "The two groups did different jobs.  Base Lorentz transport fixed the "
    "canonical trace line while moving W4(u).  The internal Spin(4) motion "
    "kept W4 fixed but moved t.  Its passing family is therefore conditional "
    "on explicitly treating t as a spurion/order parameter, not a derivation "
    "from the canonical DeWitt trace."
)


print("\n" + "=" * 96)
print("E. DISTINCT OPTIONAL J BRANCH: THE DISTINGUISHED LINE WITH A COMPLEX STRUCTURE")
print("=" * 96)

# A real pseudo-Euclidean vector space admits an orthogonal complex structure
# only when both inertia indices are even.  In a J-adapted real basis, every
# positive and every negative Hermitian line contributes two real directions.
native_signature = signature(dewitt_gram)[:2]
raw_signature = signature(raw_gram)[:2]
check(
    "the even-even native signature (6,4) admits an orthogonal complex structure",
    native_signature == (6, 4)
    and all(index % 2 == 0 for index in native_signature),
)
check(
    "the raw (7,3) Frobenius signature fails the orthogonal-complex parity obstruction",
    raw_signature == (7, 3)
    and any(index % 2 == 1 for index in raw_signature),
)

complex0 = standard_complex_structure(native_signature)
trace_vector0 = np.eye(10)[:, 6]
complex_trace0 = complex0 @ trace_vector0
trace_projector = np.outer(trace_vector0, trace_vector0)
check(
    "the explicit native J obeys J^2=-1 and J^T G_DW J=G_DW",
    max_abs(complex0 @ complex0 + IDENTITY10) < TOL
    and max_abs(complex0.T @ ETA10 @ complex0 - ETA10) < TOL,
)
check(
    "Jt is a second negative unit direction DeWitt-orthogonal to t",
    abs(float(complex_trace0 @ ETA10 @ complex_trace0) + 1.0) < TOL
    and abs(float(trace_vector0 @ ETA10 @ complex_trace0)) < TOL,
)
check(
    "J is not canonical from the distinguished trace projector because it moves the trace line",
    max_abs(complex0 @ trace_projector - trace_projector @ complex0) > 0.5,
)

# The observer is a coset variable: a Lorentz transformation taking u0 to u
# is defined only modulo the fixed-u spatial SO(3).  Therefore a transported
# J descends to a map u -> J only if its seed is fixed by that stabilizer.
complex_stabilizer = (
    sym2_rotation @ complex0 @ np.linalg.inv(sym2_rotation)
)
stabilizer_j_residual = float(np.linalg.norm(complex_stabilizer - complex0))
stabilizer_jt_residual = float(
    np.linalg.norm(
        complex_stabilizer @ trace_vector0
        - complex0 @ trace_vector0
    )
)
check(
    "fixed-u SO(3) keeps u, P_W, and t fixed but generally changes compatible J",
    max_abs(np.linalg.inv(base_rotation) @ observer0 - observer0) < TOL
    and max_abs(
        sym2_rotation
        @ projector_w0
        @ np.linalg.inv(sym2_rotation)
        - projector_w0
    )
    < TOL
    and max_abs(sym2_rotation @ trace_vector0 - trace_vector0) < TOL
    and stabilizer_j_residual > 1.0
    and stabilizer_jt_residual > 0.1,
    (
        f"J residual {stabilizer_j_residual:.9f}, "
        f"Jt residual {stabilizer_jt_residual:.9f}"
    ),
)

# This is not just an unlucky displayed J.  The fixed-u SO(3) Casimir on
# Sym^2 has real eigenspaces of dimensions 2, 3, and 5.  Any stabilizer-
# commuting J would preserve each Casimir eigenspace, but no real operator
# squaring to -1 exists on the odd three-dimensional eigenspace.
stabilizer_generators = []
for left, right in combinations(range(3), 2):
    base_generator = np.zeros((4, 4))
    base_generator[left, right] = 1.0
    base_generator[right, left] = -1.0
    stabilizer_generators.append(induced_sym2_generator(base_generator))
stabilizer_casimir = -sum(
    (generator @ generator for generator in stabilizer_generators),
    np.zeros((10, 10)),
)
casimir_values = np.linalg.eigvalsh(
    0.5 * (stabilizer_casimir + stabilizer_casimir.T)
)
casimir_multiplicities = tuple(
    int(np.sum(np.abs(casimir_values - value) < TOL))
    for value in (0.0, 2.0, 6.0)
)
check(
    "the fixed-u SO(3) Casimir has 1+1, 3, and 5 blocks, obstructing every observer-equivariant real J",
    casimir_multiplicities == (2, 3, 5),
    f"multiplicities {casimir_multiplicities}",
)
info(
    "Consequently, choosing Lambda only from u is insufficient: two choices "
    "differing by the fixed-u stabilizer give different J.  There is no "
    "observer-only equivariant u -> J map on this real orthogonal reading."
)

# The compatible-J ambiguity remains large even after requiring J to preserve
# the selected A6/W4 split.  Linearize J^2=-1, J^T G J=G, and [J,P_W]=0 at the
# displayed J.  The nullity is the local dimension of the family, not a count
# of physical modes or vacua.
j_tangent_columns = []
for row in range(10):
    for column in range(10):
        variation = np.zeros((10, 10))
        variation[row, column] = 1.0
        constraints = np.concatenate(
            [
                (variation @ complex0 + complex0 @ variation).reshape(-1),
                (
                    variation.T @ ETA10 @ complex0
                    + complex0.T @ ETA10 @ variation
                ).reshape(-1),
                (
                    variation @ projector_w0
                    - projector_w0 @ variation
                ).reshape(-1),
            ]
        )
        j_tangent_columns.append(constraints)
j_tangent_constraint = np.column_stack(j_tangent_columns)
j_tangent_dimension = 100 - np.linalg.matrix_rank(
    j_tangent_constraint,
    tol=TOL,
)
check(
    "P_W-commuting orthogonal compatible J has local family dimension 8",
    max_abs(complex0 @ projector_w0 - projector_w0 @ complex0) < TOL
    and j_tangent_dimension == 8,
    f"linearized nullity {j_tangent_dimension}",
)
info(
    "The eight dimensions agree with O(6)/U(3) times O(4)/U(2): dimensions "
    "6 plus 2.  This is a reduction-family dimension, not a physical count."
)

# This is a family statement, not a preferred J: conjugate J and move t under
# the same O(6,4) element.  The induced base boost happens to fix t, which is a
# useful control because it isolates the necessity of transporting J.
complex1 = sym2_boost @ complex0 @ np.linalg.inv(sym2_boost)
trace_vector1 = sym2_boost @ trace_vector0
complex_trace1 = complex1 @ trace_vector1
check(
    "joint O(6,4) transport preserves the compatible-complex-structure equations",
    max_abs(complex1 @ complex1 + IDENTITY10) < TOL
    and max_abs(complex1.T @ ETA10 @ complex1 - ETA10) < TOL
    and max_abs(
        complex_trace1 - sym2_boost @ complex_trace0
    )
    < TOL,
)
complex_line_frame0 = np.column_stack([trace_vector0, complex_trace0])
complex_line_frame1 = np.column_stack([trace_vector1, complex_trace1])
complex_line_projector0, complex_line_gram0 = metric_projector(
    complex_line_frame0
)
complex_line_projector1, complex_line_gram1 = metric_projector(
    complex_line_frame1
)
check(
    "the real two-plane underlying the complex trace line is negative and transports covariantly",
    signature(complex_line_gram0) == (0, 2, 0)
    and signature(complex_line_gram1) == (0, 2, 0)
    and max_abs(
        complex_line_projector1
        - sym2_boost
        @ complex_line_projector0
        @ np.linalg.inv(sym2_boost)
    )
    < TOL,
)
fixed_complex_residual = float(
    np.linalg.norm(
        complex0 @ trace_vector0
        - sym2_boost @ complex_trace0
    )
)
check(
    "planted fixed J and fixed t fail full O(6,4) covariance",
    max_abs(complex1 - complex0) > 0.1
    and fixed_complex_residual > 0.1,
    f"Jt residual {fixed_complex_residual:.9f}",
)
info(
    "On the orthogonal real-J reading, the transcript-compatible formula "
    "t -> Jt is algebraically available only after trace reversal, but J is "
    "an extra compatible reduction.  "
    "The metric, observer u, trace projector, and internal moving-t spurion "
    "do not canonically supply it; a choice of transport frame changes it."
)


print("\n" + "=" * 96)
if FAILURES:
    print(f"FAIL: {len(FAILURES)} RB4 checks failed")
    for failure in FAILURES:
        print(f"  - {failure}")
    raise SystemExit(1)

print("PASS: RB4 moving observer/Cartan finite family")
print(
    "The trace-reversed observer family is exactly base-Lorentz covariant "
    "when P_W, its complement, oriented volumes, and the Clifford soldering "
    "frame move together.  Frozen-projector and frozen-soldering controls "
    "fail.  Separately, internal Spin(4) covariance beyond the fixed-t "
    "Spin(3) stabilizer requires t itself to move as an explicit spurion or "
    "order parameter.  A compatible J exists only on the trace-reversed "
    "even-even signature and also has to move as an additional reduction; "
    "u alone cannot select it because the fixed-u stabilizer changes J.  "
    "No source ownership or physical compact-group identification is inferred."
)
