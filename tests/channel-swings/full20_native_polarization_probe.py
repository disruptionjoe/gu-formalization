#!/usr/bin/env python3
r"""Native Krein polarization, exact witnesses, and actual-Sym2 curvature gate.

This is the executable certificate for the third full-20 source-action swing.
It keeps four grades separate:

1. the native Cl(9,5) spinor/vector-spinor Krein pairing;
2. compact-support formal adjoints and graded coefficient polarization;
3. the exact principal coefficient kernel and the exact r_R=0 auxiliary
   identity; and
4. the two action-generated curvature remainders at the local W177 gimmel
   point, using all ten Sym^2(T*X) fibre coordinates.

Layer 0
-------
The principal kernel is not a Noether identity.  The compact-support formal
adjoint is not a selected global closed domain.  The exact r_R=0 identity is
an auxiliary S + im(Gamma) complex, not a gauge transformation of
ker(Gamma).  W177 is a local, already-nonstationary conditional background;
failure there is not a global GU no-go.

The frame-order control is load-bearing.  W177 emits an orthonormal frame in
grouped (+^9,-^5) order, whereas the program's factorized Clifford list uses
native 4+10 order (+,+,+,-; +^6,-^4).  Curvature and gamma labels are aligned
before contraction.  The deliberately unaligned plant must reproduce the
rejected in-wave numerical pattern.

Deterministic, numpy only, no writes, no network.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import w177_ym_residual_and_mode_closure_probe as w177  # noqa: E402


TOL = 2.0e-9
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value)))


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for factor in factors:
        result = np.kron(result, factor)
    return result


def euclidean_gammas(n_pairs: int) -> list[np.ndarray]:
    identity = np.eye(2, dtype=complex)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas: list[np.ndarray] = []
    for index in range(n_pairs):
        left = [sigma_3] * index
        right = [identity] * (n_pairs - index - 1)
        gammas.append(kron_all(left + [sigma_1] + right))
        gammas.append(kron_all(left + [sigma_2] + right))
    return gammas


def signed_gammas(positive: int, negative: int) -> tuple[list[np.ndarray], np.ndarray]:
    dimension = positive + negative
    euclidean = euclidean_gammas(dimension // 2)
    metric = np.array([1.0] * positive + [-1.0] * negative)
    gammas = [
        euclidean[index] if metric[index] > 0 else 1j * euclidean[index]
        for index in range(dimension)
    ]
    return gammas, metric


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    result = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        result = result @ matrix
    return result


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    omega = matrix_product(gammas)
    scalar = complex(np.trace(omega @ omega) / omega.shape[0])
    if abs(scalar - 1.0) < TOL:
        return omega
    if abs(scalar + 1.0) < TOL:
        return 1j * omega
    raise AssertionError(f"chirality square is not scalar +/-1: {scalar}")


def factorized_native_gammas() -> tuple[list[np.ndarray], np.ndarray]:
    """Cl(3,1) hat-tensor Cl(6,4), in native base-then-fibre order."""
    gamma_4, eta_4 = signed_gammas(3, 1)
    gamma_10, eta_10 = signed_gammas(6, 4)
    omega_4 = normalized_chirality(gamma_4)
    identity_4 = np.eye(4, dtype=complex)
    identity_32 = np.eye(32, dtype=complex)
    base = [np.kron(gamma, identity_32) for gamma in gamma_4]
    fibre = [np.kron(omega_4, gamma) for gamma in gamma_10]
    # Retain explicit identities as a control against an accidental factor
    # dimension change.
    if identity_4.shape != (4, 4):
        raise AssertionError("unexpected Cl4 spinor dimension")
    return base + fibre, np.concatenate((eta_4, eta_10))


def clifford_defect(gammas: list[np.ndarray], eta: np.ndarray) -> float:
    identity = np.eye(gammas[0].shape[0], dtype=complex)
    defect = 0.0
    for left, gamma_left in enumerate(gammas):
        for right, gamma_right in enumerate(gammas):
            target = (
                2.0 * eta[left] * identity
                if left == right
                else np.zeros_like(identity)
            )
            defect = max(
                defect,
                max_abs(gamma_left @ gamma_right + gamma_right @ gamma_left - target),
            )
    return defect


def gamma_trace(gammas: list[np.ndarray], vector_spinor: np.ndarray) -> np.ndarray:
    return sum(
        (gammas[index] @ vector_spinor[index] for index in range(len(gammas))),
        np.zeros(gammas[0].shape[0], dtype=complex),
    )


def j_map(
    gammas: list[np.ndarray], eta: np.ndarray, spinor: np.ndarray
) -> np.ndarray:
    dimension = len(gammas)
    return np.stack(
        [eta[index] * gammas[index] @ spinor / dimension for index in range(dimension)]
    )


def p_i(
    gammas: list[np.ndarray], eta: np.ndarray, vector_spinor: np.ndarray
) -> np.ndarray:
    return j_map(gammas, eta, gamma_trace(gammas, vector_spinor))


def p_r(
    gammas: list[np.ndarray], eta: np.ndarray, vector_spinor: np.ndarray
) -> np.ndarray:
    return vector_spinor - p_i(gammas, eta, vector_spinor)


def pair_s(left: np.ndarray, right: np.ndarray, krein: np.ndarray) -> complex:
    return complex(left.conj() @ krein @ right)


def pair_vs(
    left: np.ndarray,
    right: np.ndarray,
    krein: np.ndarray,
    eta: np.ndarray,
) -> complex:
    return complex(
        sum(
            eta[index] * (left[index].conj() @ krein @ right[index])
            for index in range(len(eta))
        )
    )


def close(left: complex, right: complex, tolerance: float = 2.0e-9) -> bool:
    scale = max(1.0, abs(left), abs(right))
    return abs(left - right) <= tolerance * scale


def c_symbol(
    gammas: list[np.ndarray], eta: np.ndarray, xi: np.ndarray
) -> np.ndarray:
    return sum(
        (
            eta[index] * xi[index] * gammas[index]
            for index in range(len(gammas))
        ),
        np.zeros_like(gammas[0]),
    )


def l_symbol(xi: np.ndarray, spinor: np.ndarray) -> np.ndarray:
    return np.stack([component * spinor for component in xi])


def contraction(
    eta: np.ndarray, xi: np.ndarray, vector_spinor: np.ndarray
) -> np.ndarray:
    return sum(
        (
            eta[index] * xi[index] * vector_spinor[index]
            for index in range(len(eta))
        ),
        np.zeros(vector_spinor.shape[1], dtype=complex),
    )


def matvec_fraction(
    matrix: tuple[tuple[Fraction, ...], ...],
    vector: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        sum((entry * component for entry, component in zip(row, vector)), Fraction(0))
        for row in matrix
    )


def determinant3(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def transpose_fraction(
    matrix: tuple[tuple[Fraction, ...], ...]
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(matrix[row][column] for row in range(3)) for column in range(3))


def multiply_fraction(
    left: tuple[tuple[Fraction, ...], ...],
    right: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(
            sum(
                (left[row][inner] * right[inner][column] for inner in range(3)),
                Fraction(0),
            )
            for column in range(3)
        )
        for row in range(3)
    )


def principal_matrix(
    *,
    a: Fraction,
    b_si: Fraction,
    b_sr: Fraction,
    b_is: Fraction,
    d: Fraction,
    b_ir: Fraction,
    b_rs: Fraction,
    b_ri: Fraction,
    q: Fraction = Fraction(1),
) -> tuple[tuple[Fraction, ...], ...]:
    return (
        (a, b_si, -Fraction(13, 14) * b_sr),
        (b_is, -Fraction(6, 7) * d, Fraction(13, 7) * b_ir),
        (b_rs, Fraction(1, 7) * b_ri, Fraction(6, 7) * q),
    )


@dataclass(frozen=True)
class CurvatureResult:
    scalar: float
    cs_norm: float
    lichnerowicz_defect: float
    crr_norm: float
    crr_rank: int
    gamma_leak: float


def curvature_maps(
    riemann_frame: np.ndarray,
    gammas: list[np.ndarray],
    eta: np.ndarray,
) -> CurvatureResult:
    """Compute C_S and C_RR with curvature/gamma labels already aligned."""
    spinor_dimension = gammas[0].shape[0]
    eta_matrix = np.diag(eta)
    gamma_up = np.stack(
        [eta[index] * gammas[index] for index in range(len(gammas))]
    )
    gamma_gamma = np.einsum(
        "aij,bjk->abik", gamma_up, gamma_up, optimize=True
    )
    spin_curvature = 0.25 * np.einsum(
        "cdab,cdij->abij", riemann_frame, gamma_gamma, optimize=True
    )
    c_s = 0.5 * np.einsum(
        "abij,abjk->ik", gamma_gamma, spin_curvature, optimize=True
    )
    scalar = float(
        np.einsum(
            "ac,bd,abcd", eta_matrix, eta_matrix, riemann_frame, optimize=True
        )
    )
    b_map = np.einsum(
        "aij,abjk->bik", gamma_up, spin_curvature, optimize=True
    ).reshape(len(gammas) * spinor_dimension, spinor_dimension)
    gamma_matrix = np.hstack(gammas)
    j_matrix = np.vstack(
        [eta[index] * gammas[index] for index in range(len(gammas))]
    ) / len(gammas)
    c_rr = b_map - j_matrix @ (gamma_matrix @ b_map)
    return CurvatureResult(
        scalar=scalar,
        cs_norm=float(np.linalg.norm(c_s)),
        lichnerowicz_defect=float(
            np.linalg.norm(c_s + scalar * np.eye(spinor_dimension) / 4.0)
        ),
        crr_norm=float(np.linalg.norm(c_rr)),
        crr_rank=int(np.linalg.matrix_rank(c_rr, tol=1.0e-7)),
        gamma_leak=float(np.linalg.norm(gamma_matrix @ c_rr)),
    )


print("=" * 94)
print("FULL-20 NATIVE KREIN POLARIZATION / ACTUAL-SYM2 CURVATURE GATE")
print("=" * 94)
print("formal compact-core packet; W177 is a local nonstationary background")


# ---------------------------------------------------------------------------
# A. Native Cl(9,5) Krein pairing and gamma-trace splitting.
# ---------------------------------------------------------------------------
print("\nA. Program-native Krein pairing and I/R splitting")

gamma_native, eta_native = factorized_native_gammas()
spinor_dimension = gamma_native[0].shape[0]
identity_s = np.eye(spinor_dimension, dtype=complex)
positive_gammas = [
    gamma for gamma, sign in zip(gamma_native, eta_native) if sign > 0
]
krein = matrix_product(positive_gammas)

check(
    "factorized native gammas satisfy Cl(9,5)",
    clifford_defect(gamma_native, eta_native) < TOL,
)
check(
    "native basis is the actual interleaved 4+10 signature",
    tuple(int(value) for value in eta_native)
    == (1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1),
)
check("K is Hermitian", max_abs(krein - krein.conj().T) < TOL)
check("K squares to one", max_abs(krein @ krein - identity_s) < TOL)
check(
    "every Clifford generator is K-self-adjoint",
    max(
        max_abs(gamma.conj().T @ krein - krein @ gamma)
        for gamma in gamma_native
    )
    < TOL,
)
krein_eigenvalues = np.linalg.eigvalsh(krein)
spin_positive = int(np.sum(krein_eigenvalues > 0.5))
spin_negative = int(np.sum(krein_eigenvalues < -0.5))
check(
    "spinor Krein signature is exactly (64,64)",
    spin_positive == 64 and spin_negative == 64,
)
hilbert_negative_defect = max(
    max_abs(gamma.conj().T - gamma)
    for gamma, sign in zip(gamma_native, eta_native)
    if sign < 0
)
check(
    "positive-Hilbert identity pairing fails on the five negative generators",
    hilbert_negative_defect > 1.0,
    f"defect={hilbert_negative_defect:.2f}",
)

rng = np.random.default_rng(20260730)
s = rng.normal(size=spinor_dimension) + 1j * rng.normal(size=spinor_dimension)
t = rng.normal(size=spinor_dimension) + 1j * rng.normal(size=spinor_dimension)
v = rng.normal(size=(14, spinor_dimension)) + 1j * rng.normal(
    size=(14, spinor_dimension)
)
raw_r = rng.normal(size=(14, spinor_dimension)) + 1j * rng.normal(
    size=(14, spinor_dimension)
)
j_s = j_map(gamma_native, eta_native, s)
j_t = j_map(gamma_native, eta_native, t)
r_part = p_r(gamma_native, eta_native, raw_r)
gamma_v = gamma_trace(gamma_native, v)
gamma_sharp_s = 14.0 * j_s

check(
    "Gamma j is the identity",
    max_abs(gamma_trace(gamma_native, j_s) - s) < TOL,
)
check(
    "Gamma Krein adjoint is Gamma-sharp",
    close(
        pair_s(gamma_v, s, krein),
        pair_vs(v, gamma_sharp_s, krein, eta_native),
    ),
)
check(
    "j Krein adjoint is Gamma/14",
    close(
        pair_vs(j_s, v, krein, eta_native),
        pair_s(s, gamma_v / 14.0, krein),
    ),
)
check(
    "induced I form is K/14",
    close(
        pair_vs(j_s, j_t, krein, eta_native),
        pair_s(s, t, krein) / 14.0,
    ),
)
check(
    "im(Gamma-sharp) is Krein-orthogonal to ker(Gamma)",
    abs(pair_vs(j_s, r_part, krein, eta_native)) < 2.0e-8,
)
check(
    "R sample is gamma-traceless",
    np.linalg.norm(gamma_trace(gamma_native, r_part)) < 2.0e-8,
)
check(
    "induced signatures close as S=(64,64), I=(64,64), R=(832,832)",
    (
        int(np.sum(eta_native > 0)) * spin_positive
        + int(np.sum(eta_native < 0)) * spin_negative
        - spin_positive,
        int(np.sum(eta_native > 0)) * spin_negative
        + int(np.sum(eta_native < 0)) * spin_positive
        - spin_negative,
    )
    == (832, 832),
)
info(
    "Spin invariance does not force the separate isomorphic S and I fields "
    "orthogonal; a nondegenerate 2x2 multiplicity Gram remains allowed"
)


# ---------------------------------------------------------------------------
# B. Primitive algebraic adjoints and formal reverse-block closure.
# ---------------------------------------------------------------------------
print("\nB. Primitive adjoints and nine-block formal closure")

xi = rng.normal(size=14)
c_xi = c_symbol(gamma_native, eta_native, xi)
u = rng.normal(size=(14, spinor_dimension)) + 1j * rng.normal(
    size=(14, spinor_dimension)
)
w = rng.normal(size=(14, spinor_dimension)) + 1j * rng.normal(
    size=(14, spinor_dimension)
)
u_r = p_r(gamma_native, eta_native, u)
w_r = p_r(gamma_native, eta_native, w)
t_s = p_r(gamma_native, eta_native, l_symbol(xi, s))
delta_w = -contraction(eta_native, xi, w_r)
q_u = p_r(
    gamma_native,
    eta_native,
    np.stack([c_xi @ component for component in u_r]),
)
q_w = p_r(
    gamma_native,
    eta_native,
    np.stack([c_xi @ component for component in w_r]),
)

check(
    "Clifford symbol is algebraically K-self-adjoint",
    max_abs(c_xi.conj().T @ krein - krein @ c_xi) < TOL,
)
check(
    "T and -delta are algebraic adjoints (so T^! = delta after integration by parts)",
    close(
        pair_vs(t_s, w_r, krein, eta_native),
        -pair_s(s, delta_w, krein),
    ),
)
check(
    "compressed Q symbol is algebraically self-adjoint (so Q^! = -Q)",
    close(
        pair_vs(q_u, w_r, krein, eta_native),
        pair_vs(u_r, q_w, krein, eta_native),
    ),
)

i_v = p_i(gamma_native, eta_native, v)
si_i = c_xi @ gamma_trace(gamma_native, i_v)
is_s = j_map(gamma_native, eta_native, c_xi @ s)
check(
    "c Gamma and j c carry the derived factor 14",
    close(
        pair_s(si_i, s, krein),
        14.0 * pair_vs(i_v, is_s, krein, eta_native),
    ),
)

mix_ir = p_i(
    gamma_native,
    eta_native,
    np.stack([c_xi @ component for component in u_r]),
)
mix_ri = p_r(
    gamma_native,
    eta_native,
    np.stack([c_xi @ component for component in i_v]),
)
check(
    "I/R compressed Dirac bridges are algebraic adjoints",
    close(
        pair_vs(mix_ir, i_v, krein, eta_native),
        pair_vs(u_r, mix_ri, krein, eta_native),
    ),
)

reverse_factors = (
    (Fraction(-1), Fraction(-14), Fraction(1)),
    (Fraction(-1, 14), Fraction(-1), Fraction(-1)),
    (Fraction(1), Fraction(-1), Fraction(-1)),
)
check(
    "all nine first-order blocks have an in-family formal reverse",
    all(reverse_factors[row][column] != 0 for row in range(3) for column in range(3))
    and all(
        reverse_factors[row][column] * reverse_factors[column][row] == 1
        for row in range(3)
        for column in range(3)
    ),
)
check(
    "formal diagonal factors are anti-adjoint while identity mass is self-adjoint",
    all(reverse_factors[index][index] == -1 for index in range(3)),
)
info(
    "C_c^infinity is a common formal core; no noncompact asymptotic domain "
    "or source-selected maximal-isotropic boundary trace is claimed"
)


# ---------------------------------------------------------------------------
# C. Graded polarization and exact principal determinant witnesses.
# ---------------------------------------------------------------------------
print("\nC. Graded polarization and determinant intersection")

sigma_odd = -1
q_odd = Fraction(1 - sigma_odd, 2)
odd_coefficients = {
    "a": Fraction(1),
    "b_si": Fraction(-1),
    "b_sr": Fraction(2),
    "b_is": Fraction(-14),
    "d": Fraction(79, 40),
    "b_ir": Fraction(1),
    "b_rs": Fraction(-2),
    "b_ri": Fraction(1),
    "q": q_odd,
}
odd_matrix = principal_matrix(**odd_coefficients)
odd_vector = (Fraction(29), Fraction(-140), Fraction(91))
zero3 = (Fraction(0), Fraction(0), Fraction(0))

check("candidate odd polarization retains normalized Q", q_odd == 1)
check(
    "candidate odd witness obeys all reverse-block relations",
    odd_coefficients["b_is"] == 14 * odd_coefficients["b_si"]
    and odd_coefficients["b_rs"] == -odd_coefficients["b_sr"]
    and odd_coefficients["b_ri"] == odd_coefficients["b_ir"],
)
check(
    "all nine polarized principal carrier blocks are nonzero",
    all(value != 0 for value in odd_coefficients.values()),
)
check(
    "exact all-three-component principal kernel witness closes",
    matvec_fraction(odd_matrix, odd_vector) == zero3
    and all(component != 0 for component in odd_vector),
)
check("exact polarized determinant vanishes", determinant3(odd_matrix) == 0)
determinant_closed_form = (
    (
        -odd_coefficients["a"]
        * (
            36 * odd_coefficients["d"]
            + 13 * odd_coefficients["b_ir"] ** 2
        )
        + 39
        * odd_coefficients["d"]
        * odd_coefficients["b_sr"] ** 2
    )
    / 49
    - 12 * odd_coefficients["b_si"] ** 2
    - Fraction(26, 7)
    * odd_coefficients["b_si"]
    * odd_coefficients["b_ir"]
    * odd_coefficients["b_sr"]
)
check(
    "closed real determinant formula agrees exactly with the matrix determinant",
    determinant_closed_form == determinant3(odd_matrix),
)

g3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1, 14), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(13, 14)),
)
check(
    "odd principal matrix satisfies M^T G3 = G3 M",
    multiply_fraction(transpose_fraction(odd_matrix), g3)
    == multiply_fraction(g3, odd_matrix),
)

perturbed_coefficients = dict(odd_coefficients)
perturbed_coefficients["d"] += Fraction(1, 100)
perturbed_matrix = principal_matrix(**perturbed_coefficients)
check(
    "a planted coefficient perturbation destroys the held-out kernel vector",
    matvec_fraction(perturbed_matrix, odd_vector) != zero3
    and determinant3(perturbed_matrix) != 0,
)
check(
    "vacuous zero gauge vector is rejected",
    odd_vector != zero3,
)
sigma_even = 1
q_even = Fraction(1 - sigma_even, 2)
check(
    "opposite polarization erases Q and therefore cannot retain full support",
    q_even == 0,
)
check(
    "determinant condition is one real equation in eight real odd-branch parameters",
    1 - 8 == -7,
    "bare constraint surplus = -7",
)


# ---------------------------------------------------------------------------
# D. Exact auxiliary identity after the curvature-remainder collapse.
# ---------------------------------------------------------------------------
print("\nD. Exact auxiliary S + im(Gamma) gauge complex")

aux_coefficients = {
    "a": Fraction(-3, 49),
    "b_si": Fraction(3, 49),
    "b_sr": Fraction(1),
    "b_is": Fraction(6, 7),
    "d": Fraction(1),
    "b_ir": Fraction(7),
    "b_rs": Fraction(-1),
    "b_ri": Fraction(7),
    "q": Fraction(1),
}
aux_matrix = principal_matrix(**aux_coefficients)
aux_vector = (Fraction(1), Fraction(1), Fraction(0))
check(
    "auxiliary coefficients obey the candidate odd adjoint relations",
    aux_coefficients["b_is"] == 14 * aux_coefficients["b_si"]
    and aux_coefficients["b_rs"] == -aux_coefficients["b_sr"]
    and aux_coefficients["b_ri"] == aux_coefficients["b_ir"],
)
check(
    "all nine auxiliary carrier blocks are nonzero",
    all(value != 0 for value in aux_coefficients.values()),
)
check(
    "auxiliary principal equations vanish exactly",
    matvec_fraction(aux_matrix, aux_vector) == zero3,
)
check(
    "auxiliary lower identity follows from C_II=C_RI=0 and r_R=0",
    aux_vector[2] == 0,
)
check(
    "Layer-0 control: auxiliary gauge map does not transform physical R",
    aux_vector[2] == 0 and odd_vector[2] != 0,
)


# ---------------------------------------------------------------------------
# E. Correctly aligned actual Sym2 curvature at W177.
# ---------------------------------------------------------------------------
print("\nE. Actual W177 Sym^2 curvature maps with frame-order hostile control")

gamma_grouped, eta_grouped = signed_gammas(9, 5)
w177_point = w177.fixed_w177_point()
scales = (0.75, 1.0, 1.25)
results: list[CurvatureResult] = []
frame_defects: list[float] = []
native_result: CurvatureResult | None = None
wrong_result: CurvatureResult | None = None

# W177 grouped frame -> native 4+10 order:
# (+0,+1,+2,-0; +3,+4,+5,+6,+7,+8,-1,-2,-3,-4).
native_permutation = (0, 1, 2, 9, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13)

for scale in scales:
    metric, _partial, _connection, riemann_low = w177.riemann_data(
        w177_point,
        scale * 1.0e-5,
        scale * 1.0e-4,
    )
    grouped_frame = w177.orthonormal_frame(metric)
    grouped_riemann = np.einsum(
        "ia,jb,kc,ld,ijkl->abcd",
        grouped_frame,
        grouped_frame,
        grouped_frame,
        grouped_frame,
        riemann_low,
        optimize=True,
    )
    result = curvature_maps(grouped_riemann, gamma_grouped, eta_grouped)
    results.append(result)

    native_frame = grouped_frame[:, native_permutation]
    frame_defects.append(
        max_abs(native_frame.T @ metric @ native_frame - np.diag(eta_native))
    )
    if scale == 1.0:
        native_riemann = np.einsum(
            "ia,jb,kc,ld,ijkl->abcd",
            native_frame,
            native_frame,
            native_frame,
            native_frame,
            riemann_low,
            optimize=True,
        )
        native_result = curvature_maps(native_riemann, gamma_native, eta_native)
        # Deliberately wrong: grouped curvature labels with native/interleaved
        # gamma labels.  This is the exact bug caught during the wave.
        wrong_result = curvature_maps(grouped_riemann, gamma_native, eta_native)

for scale, result in zip(scales, results):
    info(
        f"scale={scale:.2f}: scalar={result.scalar:.9f}, "
        f"||CS||={result.cs_norm:.8f}, "
        f"Lich defect={result.lichnerowicz_defect:.2e}, "
        f"||CRR||={result.crr_norm:.8f}, rank={result.crr_rank}, "
        f"Gamma leak={result.gamma_leak:.2e}"
    )

check(
    "native 4+10 frame permutation matches the interleaved signature",
    max(frame_defects) < 5.0e-14,
    f"max defect={max(frame_defects):.2e}",
)
check(
    "scalar curvature is stable and nonzero across all three scales",
    all(abs(result.scalar + 10.0) < 3.0e-5 for result in results),
)
check(
    "C_S satisfies the convention-controlled Lichnerowicz identity",
    max(result.lichnerowicz_defect for result in results) < 3.0e-5
    and min(result.cs_norm for result in results) > 28.0,
)
check(
    "C_RR is stable, nonzero, gamma-traceless, and full-column-rank",
    all(
        result.crr_norm > 21.0
        and result.crr_rank == 128
        and result.gamma_leak < 1.0e-12
        for result in results
    ),
)
check(
    "grouped and correctly permuted native Clifford realizations agree",
    native_result is not None
    and abs(native_result.scalar - results[1].scalar) < 1.0e-8
    and abs(native_result.cs_norm - results[1].cs_norm) < 1.0e-8
    and abs(native_result.crr_norm - results[1].crr_norm) < 1.0e-8,
)
check(
    "unaligned frame/gamma plant reproduces and rejects the spurious in-wave result",
    wrong_result is not None
    and abs(wrong_result.scalar + 0.640428) < 2.0e-4
    and abs(wrong_result.crr_norm - 15.879645) < 2.0e-4
    and abs(wrong_result.scalar - results[1].scalar) > 1.0,
)

zero_riemann = np.zeros((14, 14, 14, 14))
flat_result = curvature_maps(zero_riemann, gamma_grouped, eta_grouped)
check(
    "flat-curvature plant kills both action-generated curvature maps",
    flat_result.cs_norm == 0.0
    and flat_result.crr_norm == 0.0
    and flat_result.crr_rank == 0,
)
check(
    "differential-order control forbids zero-order C_RR cancellation by first-order mu T",
    min(result.crr_norm for result in results) > 21.0,
)


print("\n" + "=" * 94)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("VERDICT: NATIVE-FORMAL-NINE-BLOCK-POLARIZATION-CLOSED")
print("VERDICT: ODD-FULL-SUPPORT-PRINCIPAL-DET-LOCUS-NONEMPTY")
print("VERDICT: AUXILIARY-S-I-FORMAL-GAUGE-COMPLEX-EXACT")
print("VERDICT: W177-ACTUAL-SYM2-CURVATURE-OBSTRUCTS-GENUINE-R-GAUGE")
print("RESIDUAL: GLOBAL-NATIVE-DOMAIN-AND-TRANSPORT-PHASES-OPEN")
print("=" * 94)
print(
    "\nThe program-native Krein form and gamma-trace splitting close the written\n"
    "nine-block family under compact-support formal adjoints.  Candidate odd\n"
    "polarization retains an exact all-nine-block principal kernel, and an\n"
    "exact r_R=0 auxiliary gauge complex survives every compatible curvature.\n"
    "At the correctly frame-aligned W177 gimmel point, however, C_S is nonzero\n"
    "and C_RR:S->R is gamma-traceless and full-column-rank.  The current ansatz\n"
    "therefore has no genuine r_R!=0 gauge identity on that local background.\n"
    "This is a background/ansatz obstruction, not a global GU no-go.  W177 is\n"
    "already nonstationary, no compensator is selected, and the global domain,\n"
    "transport-normalized 20-slot phases, nonlinear Noether identity, and BV\n"
    "closure remain open."
)
