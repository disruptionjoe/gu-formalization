#!/usr/bin/env python3
r"""N4a: typed curvature-irrep and frozen open-BV incidence probe.

Layer 0
-------
This probe consumes, without changing, N1's packet sealed by

    1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb.

It asks two different questions and keeps them different:

1. For a metric/Clifford-compatible Levi--Civita spin lift
   (nabla gamma = nabla P_R = 0), which Riemann irreducible components reach
   the physical vector-spinor curvature map C_RR:S -> T*Y tensor R?
2. How far can N1's ten-token open-BV grammar be type-filtered and quotiented
   using only maps actually supplied by N1/N4a?

The first question has an exact answer: scalar and Weyl curvature are killed
by P_R and only traceless Ricci remains.  The second does not have an exact
Hom-rank answer because observer-slot carriers, several token maps, invariant
contractions, and native-real-form multiplicities are not supplied.  The
number 233100 is a syntactic ceiling, not a rank.

Omega^IG is treated as a frozen token, not silently identified with F_A.
For a separate pointwise typing control only, this probe defines a
Spin-subalgebra witness rho(P_IG), with P_IG in Omega^2(Y,adP), independent
of F_A.  It does not prove covariance under the full Sp(32,32;H) action:
that additionally requires an equivariant vector/soldering action on gamma
and preservation of P_R.  It computes no IG Hom rank and uses no source
equation relating P_IG to D_A U.

This is N4a only.  It performs no EOM factorization and no CME test.
Deterministic, numpy only, no writes, no network.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import json
import os
import sys
from typing import Callable

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import unified_source_datum_packet_v0_probe as n1  # noqa: E402
import w177_ym_residual_and_mode_closure_probe as w177  # noqa: E402


SEALED_HASH = "1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb"
N = 14
TOL = 3.0e-9
OPEN_MONOMIAL_GHOST_DEGREE = 2
OPEN_MONOMIAL_ANTIFIELD_NUMBER = 2
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
    result: list[np.ndarray] = []
    for index in range(n_pairs):
        left = [sigma_3] * index
        right = [identity] * (n_pairs - index - 1)
        result.append(kron_all(left + [sigma_1] + right))
        result.append(kron_all(left + [sigma_2] + right))
    return result


def signed_gammas(positive: int, negative: int) -> tuple[list[np.ndarray], np.ndarray]:
    metric = np.array([1.0] * positive + [-1.0] * negative)
    euclidean = euclidean_gammas((positive + negative) // 2)
    gammas = [
        gamma if metric[index] > 0 else 1j * gamma
        for index, gamma in enumerate(euclidean)
    ]
    return gammas, metric


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    result = np.eye(gammas[0].shape[0], dtype=complex)
    for gamma in gammas:
        result = result @ gamma
    square = complex(np.trace(result @ result) / result.shape[0])
    if abs(square - 1.0) < TOL:
        return result
    if abs(square + 1.0) < TOL:
        return 1j * result
    raise AssertionError("chirality square is not scalar +/-1")


def factorized_native_gammas() -> tuple[list[np.ndarray], np.ndarray]:
    """Cl(3,1) hat-tensor Cl(6,4), in the actual base-then-fibre order."""
    gamma_4, eta_4 = signed_gammas(3, 1)
    gamma_10, eta_10 = signed_gammas(6, 4)
    omega_4 = normalized_chirality(gamma_4)
    base = [np.kron(gamma, np.eye(32, dtype=complex)) for gamma in gamma_4]
    fibre = [np.kron(omega_4, gamma) for gamma in gamma_10]
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
    """j(s)_a = gamma_a s / n for gamma^a represented by ``gammas``."""
    return np.stack(
        [
            eta[index] * gammas[index] @ spinor / len(gammas)
            for index in range(len(gammas))
        ]
    )


def p_i(
    gammas: list[np.ndarray], eta: np.ndarray, vector_spinor: np.ndarray
) -> np.ndarray:
    return j_map(gammas, eta, gamma_trace(gammas, vector_spinor))


def p_r(
    gammas: list[np.ndarray], eta: np.ndarray, vector_spinor: np.ndarray
) -> np.ndarray:
    return vector_spinor - p_i(gammas, eta, vector_spinor)


def gamma_and_j_matrices(
    gammas: list[np.ndarray], eta: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    gamma_matrix = np.hstack(gammas)
    j_matrix = np.vstack(
        [eta[index] * gammas[index] for index in range(len(gammas))]
    ) / len(gammas)
    return gamma_matrix, j_matrix


def ricci_and_scalar(
    riemann: np.ndarray, eta: np.ndarray
) -> tuple[np.ndarray, float]:
    metric = np.diag(eta)
    ricci = np.einsum("ac,abcd->bd", metric, riemann, optimize=True)
    scalar = float(np.einsum("bd,bd", metric, ricci, optimize=True))
    return ricci, scalar


def decompose_lc_riemann(
    riemann: np.ndarray, eta: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    """Return scalar, traceless-Ricci, Weyl, Ric0, and scalar curvature."""
    metric = np.diag(eta)
    ricci, scalar = ricci_and_scalar(riemann, eta)
    ricci_zero = ricci - scalar * metric / len(eta)
    scalar_part = scalar / (N * (N - 1)) * (
        np.einsum("ac,bd->abcd", metric, metric)
        - np.einsum("ad,bc->abcd", metric, metric)
    )
    ricci_part = (
        np.einsum("ac,bd->abcd", metric, ricci_zero)
        - np.einsum("ad,bc->abcd", metric, ricci_zero)
        - np.einsum("bc,ad->abcd", metric, ricci_zero)
        + np.einsum("bd,ac->abcd", metric, ricci_zero)
    ) / (N - 2)
    weyl = riemann - scalar_part - ricci_part
    return scalar_part, ricci_part, weyl, ricci_zero, scalar


def lc_spin_curvature(
    riemann: np.ndarray, gammas: list[np.ndarray]
) -> np.ndarray:
    """Omega^LC_ab = (1/4) R_cdab gamma^c gamma^d."""
    gamma_gamma = np.einsum(
        "cij,djk->cdik", np.stack(gammas), np.stack(gammas), optimize=True
    )
    return 0.25 * np.einsum(
        "cdab,cdij->abij", riemann, gamma_gamma, optimize=True
    )


def projected_rr_matrix_from_endomorphism_two_form(
    endomorphism_two_form: np.ndarray,
    gammas: list[np.ndarray],
    eta: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return P_R(gamma^a Omega_ab) and its unprojected B map."""
    spinor_dimension = gammas[0].shape[0]
    b_map = np.einsum(
        "aij,abjk->bik",
        np.stack(gammas),
        endomorphism_two_form,
        optimize=True,
    ).reshape(N * spinor_dimension, spinor_dimension)
    gamma_matrix, j_matrix = gamma_and_j_matrices(gammas, eta)
    return b_map - j_matrix @ (gamma_matrix @ b_map), b_map


def lc_rr_matrix(
    riemann: np.ndarray, gammas: list[np.ndarray], eta: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    return projected_rr_matrix_from_endomorphism_two_form(
        lc_spin_curvature(riemann, gammas), gammas, eta
    )


def predicted_lc_rr_from_ricci_zero(
    ricci_zero: np.ndarray, gammas: list[np.ndarray], eta: np.ndarray
) -> np.ndarray:
    raw = 0.5 * np.einsum(
        "bd,dij->bij", ricci_zero, np.stack(gammas), optimize=True
    )
    spinor_dimension = gammas[0].shape[0]
    raw_matrix = raw.reshape(N * spinor_dimension, spinor_dimension)
    gamma_matrix, j_matrix = gamma_and_j_matrices(gammas, eta)
    return raw_matrix - j_matrix @ (gamma_matrix @ raw_matrix)


def legacy_mixed_convention_rr(
    riemann: np.ndarray, gammas: list[np.ndarray], eta: np.ndarray
) -> np.ndarray:
    """Reproduce the prior raised/lowered mixture for an append-only regression."""
    spinor_dimension = gammas[0].shape[0]
    gamma_lower = np.stack(
        [eta[index] * gammas[index] for index in range(len(gammas))]
    )
    gamma_gamma = np.einsum(
        "aij,bjk->abik", gamma_lower, gamma_lower, optimize=True
    )
    spin_curvature = 0.25 * np.einsum(
        "cdab,cdij->abij", riemann, gamma_gamma, optimize=True
    )
    b_map = np.einsum(
        "aij,abjk->bik", gamma_lower, spin_curvature, optimize=True
    ).reshape(N * spinor_dimension, spinor_dimension)
    gamma_matrix, j_matrix = gamma_and_j_matrices(gammas, eta)
    return b_map - j_matrix @ (gamma_matrix @ b_map)


def constant_curvature(eta: np.ndarray, sectional: float = 1.0) -> np.ndarray:
    metric = np.diag(eta)
    return sectional * (
        np.einsum("ac,bd->abcd", metric, metric)
        - np.einsum("ad,bc->abcd", metric, metric)
    )


def traceless_ricci_fixture(eta: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    metric = np.diag(eta)
    ricci_zero = np.zeros((N, N))
    ricci_zero[0, 0] = 1.0
    ricci_zero[1, 1] = -1.0
    riemann = (
        np.einsum("ac,bd->abcd", metric, ricci_zero)
        - np.einsum("ad,bc->abcd", metric, ricci_zero)
        - np.einsum("bc,ad->abcd", metric, ricci_zero)
        + np.einsum("bd,ac->abcd", metric, ricci_zero)
    ) / (N - 2)
    return riemann, ricci_zero


def pure_weyl_fixture() -> np.ndarray:
    """A diagonal algebraic curvature tensor with zero sectional row sums."""
    result = np.zeros((N, N, N, N))
    sectionals = {
        (0, 1): 1.0,
        (0, 2): -1.0,
        (0, 3): 0.0,
        (1, 2): 0.0,
        (1, 3): -1.0,
        (2, 3): 1.0,
    }
    for (left, right), value in sectionals.items():
        result[left, right, left, right] = value
        result[right, left, left, right] = -value
        result[left, right, right, left] = -value
        result[right, left, right, left] = value
    return result


def bianchi_defect(riemann: np.ndarray) -> float:
    cyclic = (
        riemann
        + riemann.transpose(0, 2, 3, 1)
        + riemann.transpose(0, 3, 1, 2)
    )
    return max_abs(cyclic)


@dataclass(frozen=True)
class Arrow:
    source: str
    target: str
    label: str
    matrix: np.ndarray


def typed_sum(arrows: tuple[Arrow, ...]) -> Arrow:
    if not arrows:
        raise ValueError("an empty arrow sum has no type")
    source = arrows[0].source
    target = arrows[0].target
    if any(arrow.source != source or arrow.target != target for arrow in arrows):
        raise ValueError("cannot concatenate arrows with different source/target")
    return Arrow(
        source,
        target,
        " + ".join(arrow.label for arrow in arrows),
        sum((arrow.matrix for arrow in arrows), np.zeros_like(arrows[0].matrix)),
    )


def pointwise_spin_pig_rr_matrix(
    gammas: list[np.ndarray], eta: np.ndarray
) -> np.ndarray:
    """A pointwise Spin-subalgebra P_IG witness, not a full-Sp IG map."""
    spinor_dimension = gammas[0].shape[0]
    represented_p_ig = np.zeros(
        (N, N, spinor_dimension, spinor_dimension), dtype=complex
    )
    generator = 0.25 * (
        gammas[4] @ gammas[5] - gammas[5] @ gammas[4]
    )
    represented_p_ig[0, 1] = generator
    represented_p_ig[1, 0] = -generator
    return projected_rr_matrix_from_endomorphism_two_form(
        represented_p_ig, gammas, eta
    )[0]


@dataclass(frozen=True)
class Token:
    name: str
    source: str | None
    target: str | None
    derivative_order: int
    physical_field_degree: int
    map_status: str


TOKENS = {
    "1": Token("1", "*", "*", 0, 0, "polymorphic identity"),
    "OmegaLC": Token(
        "OmegaLC", None, None, 2, 0,
        "LC correction arrow constructed; 20-slot insertion map absent",
    ),
    "F_A": Token(
        "F_A", None, None, 1, 2,
        "carrier supplied; observer-slot representation/contractions absent",
    ),
    "OmegaIG": Token(
        "OmegaIG", None, None, 1, 1,
        "frozen token; conditional rho(P_IG) witness is not a frozen slot map",
    ),
    "v": Token(
        "v", None, None, 0, 1,
        "c_rho(v) supplied; complete 20-slot incidence absent",
    ),
    "II": Token(
        "II", None, None, 1, 1,
        "geometric carrier supplied; 20-slot insertion map absent",
    ),
    "Tdelta": Token("Tdelta", "R", "R", 2, 0, "typed"),
    "deltaT": Token("deltaT", "S", "S", 2, 0, "typed"),
    "Q": Token("Q", "R", "R", 1, 0, "typed"),
    "jGamma": Token("jGamma", "VS", "VS", 0, 0, "typed projector"),
}


def canonical_word(word: tuple[str, ...]) -> tuple[str, ...]:
    """Apply only identity and (j Gamma)^2=(j Gamma) quotient rules."""
    without_identity = [token for token in word if token != "1"]
    result: list[str] = []
    for token in without_identity:
        if token == "jGamma" and result and result[-1] == "jGamma":
            continue
        result.append(token)
    return tuple(result) if result else ("1",)


def classify_word(word: tuple[str, ...]) -> tuple[str, str]:
    if len(word) < 1 or len(word) > 3:
        return "REJECTED", "composition length outside 1..3"
    if any(token not in TOKENS for token in word):
        return "REJECTED", "token outside frozen ten-family alphabet"
    entries = [TOKENS[token] for token in word]
    # Every frozen insertion is ghost/antifield neutral.  The surrounding
    # Z^+ Z^+ gamma gamma monomial already saturates both caps at 2.
    if (
        OPEN_MONOMIAL_GHOST_DEGREE > 2
        or OPEN_MONOMIAL_ANTIFIELD_NUMBER > 2
    ):
        return "REJECTED", "ghost or antifield cap exceeded"
    if sum(entry.derivative_order for entry in entries) > 2:
        return "REJECTED", "derivative order exceeds 2"
    if sum(entry.physical_field_degree for entry in entries) > 4:
        return "REJECTED", "physical-field degree exceeds 4"
    concrete = [entry for entry in entries if entry.name != "1"]
    if any(entry.source is None or entry.target is None for entry in concrete):
        return "RANK-DEFERRED", "at least one carrier map is not supplied"
    for left, right in zip(concrete, concrete[1:]):
        if left.target != right.source:
            return "REJECTED", f"{left.target} does not feed {right.source}"
    return "TYPED", "composes in the supplied partial incidence graph"


def partial_grammar_ledger() -> dict[str, object]:
    words = [
        word
        for length in (1, 2, 3)
        for word in itertools.product(TOKENS, repeat=length)
    ]
    counts = {"TYPED": 0, "REJECTED": 0, "RANK-DEFERRED": 0}
    quotient_representatives: set[tuple[str, ...]] = set()
    for word in words:
        status, _reason = classify_word(word)
        counts[status] += 1
        if status == "TYPED":
            quotient_representatives.add(canonical_word(word))
    return {
        "frozen_tokens": list(TOKENS),
        "ordered_words": len(words),
        "slot_pairs": 210,
        "syntactic_ceiling": 210 * len(words),
        "partial_word_status_counts": counts,
        "typed_partial_quotient_representatives": len(quotient_representatives),
        "hom_rank": "RANK-DEFERRED",
        "missing_for_hom_rank": [
            "20 observer-slot source and target carriers",
            "OmegaIG carrier/map as a frozen construction and its relation to F_A",
            "full token action on every slot",
            "native-real-form equivariant multiplicities",
            "first invariant pairing/contraction for every typed tuple",
        ],
        "degree_caps": {
            "derivative": 2,
            "physical_field": 4,
            "ghost": 2,
            "antifield": 2,
        },
        "open_monomial_degrees": {
            "ghost": OPEN_MONOMIAL_GHOST_DEGREE,
            "antifield": OPEN_MONOMIAL_ANTIFIELD_NUMBER,
            "insertion_increment": 0,
        },
    }


def jacobi(
    bracket: Callable[[np.ndarray, np.ndarray], np.ndarray],
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
) -> np.ndarray:
    return (
        bracket(x, bracket(y, z))
        + bracket(y, bracket(z, x))
        + bracket(z, bracket(x, y))
    )


print("=" * 96)
print("N4a FULL-20 CURVATURE IRREP / FROZEN OPEN-BV TYPED INCIDENCE")
print("=" * 96)

check(
    "frozen N1 construction hash is unchanged",
    n1.construction_hash() == SEALED_HASH == n1.SEALED_HASH,
)

gamma_grouped, eta_grouped = signed_gammas(9, 5)
gamma_native, eta_native = factorized_native_gammas()
spinor_dimension = gamma_grouped[0].shape[0]
check(
    "grouped and native Clifford realizations both satisfy Cl(9,5)",
    clifford_defect(gamma_grouped, eta_grouped) < TOL
    and clifford_defect(gamma_native, eta_native) < TOL,
)
check(
    "native realization has the actual 4+10 signature order",
    tuple(int(value) for value in eta_native)
    == (1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1),
)

rng = np.random.default_rng(20260730)
spinor = rng.normal(size=spinor_dimension) + 1j * rng.normal(
    size=spinor_dimension
)
vector_spinor = rng.normal(size=(N, spinor_dimension)) + 1j * rng.normal(
    size=(N, spinor_dimension)
)
i_part = p_i(gamma_grouped, eta_grouped, vector_spinor)
r_part = p_r(gamma_grouped, eta_grouped, vector_spinor)
check(
    "Gamma j=1 and j Gamma/P_R are exact complementary projectors",
    max_abs(gamma_trace(gamma_grouped, j_map(gamma_grouped, eta_grouped, spinor)) - spinor)
    < TOL
    and max_abs(p_i(gamma_grouped, eta_grouped, i_part) - i_part) < TOL
    and max_abs(p_r(gamma_grouped, eta_grouped, r_part) - r_part) < TOL
    and max_abs(i_part + r_part - vector_spinor) < TOL
    and np.linalg.norm(gamma_trace(gamma_grouped, r_part)) < 2.0e-11,
)

print("\nA. LC Riemann irreps under nabla gamma = nabla P_R = 0")
scalar_fixture = constant_curvature(eta_grouped)
ricci_fixture, planted_ricci_zero = traceless_ricci_fixture(eta_grouped)
weyl_fixture = pure_weyl_fixture()
fixture_maps: dict[str, np.ndarray] = {}
for label, fixture in (
    ("scalar", scalar_fixture),
    ("traceless-Ricci", ricci_fixture),
    ("Weyl", weyl_fixture),
):
    scalar_part, ricci_part, weyl_part, ricci_zero, scalar = decompose_lc_riemann(
        fixture, eta_grouped
    )
    c_rr, _raw = lc_rr_matrix(fixture, gamma_grouped, eta_grouped)
    predicted = predicted_lc_rr_from_ricci_zero(
        ricci_zero, gamma_grouped, eta_grouped
    )
    fixture_maps[label] = c_rr
    info(
        f"{label}: Scal={scalar:.6f}, ||Ric0||={np.linalg.norm(ricci_zero):.6f}, "
        f"||C_RR||={np.linalg.norm(c_rr):.8f}, identity defect="
        f"{np.linalg.norm(c_rr - predicted):.2e}"
    )
    check(
        f"{label} fixture is an algebraic LC curvature tensor",
        bianchi_defect(fixture) < TOL
        and np.linalg.norm(fixture - scalar_part - ricci_part - weyl_part) < TOL,
    )
    check(
        f"{label} fixture obeys C_RR=(1/2)P_R(Ric0_bd gamma^d)",
        np.linalg.norm(c_rr - predicted) < 2.0e-10,
    )

check(
    "LC scalar and Weyl components vanish after P_R",
    np.linalg.norm(fixture_maps["scalar"]) < 2.0e-10
    and np.linalg.norm(fixture_maps["Weyl"]) < 2.0e-10,
)
check(
    "LC traceless-Ricci component survives with the exact one-half coefficient",
    np.linalg.norm(fixture_maps["traceless-Ricci"]) > 1.0
    and max_abs(
        decompose_lc_riemann(ricci_fixture, eta_grouped)[3]
        - planted_ricci_zero
    )
    < TOL,
)

legacy_scalar = legacy_mixed_convention_rr(
    scalar_fixture, gamma_grouped, eta_grouped
)
check(
    "append-only regression detects the prior mixed-convention scalar leakage",
    np.linalg.norm(legacy_scalar) > 100.0
    and np.linalg.norm(fixture_maps["scalar"]) < 2.0e-10,
    f"legacy scalar leakage={np.linalg.norm(legacy_scalar):.8f}",
)

# The compatibility hypothesis is load-bearing.  A non-metric shear does not
# intertwine the gamma-trace projector; its conjugate remains a projector but
# no longer lands in the native ker(Gamma).
shear = np.eye(N)
shear[0, 1] = 0.375
shear_inverse = np.linalg.inv(shear)


def transport(value: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    return np.einsum("ab,bi->ai", matrix, value)


def nonparallel_projector(value: np.ndarray) -> np.ndarray:
    return transport(
        p_r(
            gamma_grouped,
            eta_grouped,
            transport(value, shear_inverse),
        ),
        shear,
    )


nonparallel_sample = nonparallel_projector(vector_spinor)
parallel_defect = np.linalg.norm(
    p_r(gamma_grouped, eta_grouped, transport(vector_spinor, shear))
    - transport(p_r(gamma_grouped, eta_grouped, vector_spinor), shear)
)
check(
    "nonparallel conjugated projector is idempotent but fails nabla P_R=0",
    np.linalg.norm(nonparallel_projector(nonparallel_sample) - nonparallel_sample)
    < 2.0e-11
    and parallel_defect > 1.0
    and np.linalg.norm(gamma_trace(gamma_grouped, nonparallel_sample)) > 1.0,
    f"intertwining defect={parallel_defect:.6f}",
)

print("\nB. W177 actual-Sym2 fixture and native 4+10 permutation")
w177_point = w177.fixed_w177_point()
metric, _partial, _connection, riemann_low = w177.riemann_data(
    w177_point, 1.0e-5, 1.0e-4
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
native_permutation = (0, 1, 2, 9, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13)
native_frame = grouped_frame[:, native_permutation]
native_riemann = np.einsum(
    "ia,jb,kc,ld,ijkl->abcd",
    native_frame,
    native_frame,
    native_frame,
    native_frame,
    riemann_low,
    optimize=True,
)
grouped_crr, _grouped_b = lc_rr_matrix(
    grouped_riemann, gamma_grouped, eta_grouped
)
native_crr, _native_b = lc_rr_matrix(native_riemann, gamma_native, eta_native)
_sp, _rp, _wp, w177_ricci_zero, w177_scalar = decompose_lc_riemann(
    grouped_riemann, eta_grouped
)
w177_predicted = predicted_lc_rr_from_ricci_zero(
    w177_ricci_zero, gamma_grouped, eta_grouped
)
gamma_matrix_grouped, _j_matrix_grouped = gamma_and_j_matrices(
    gamma_grouped, eta_grouped
)
legacy_w177 = legacy_mixed_convention_rr(
    grouped_riemann, gamma_grouped, eta_grouped
)
unaligned_crr = lc_rr_matrix(
    grouped_riemann, gamma_native, eta_native
)[0]
info(
    f"W177: scalar={w177_scalar:.9f}, corrected ||C_RR^LC||="
    f"{np.linalg.norm(grouped_crr):.8f}, rank="
    f"{np.linalg.matrix_rank(grouped_crr, tol=1.0e-7)}, "
    f"legacy ||C_RR||={np.linalg.norm(legacy_w177):.8f}"
)
check(
    "W177 central fixture reproduces its scalar-curvature anchor",
    abs(w177_scalar + 10.0) < 3.0e-5,
)
check(
    "native 4+10 frame permutation aligns signature and LC map invariants",
    max_abs(native_frame.T @ metric @ native_frame - np.diag(eta_native))
    < 5.0e-14
    and abs(np.linalg.norm(native_crr) - np.linalg.norm(grouped_crr)) < 2.0e-8
    and np.linalg.matrix_rank(native_crr, tol=1.0e-7)
    == np.linalg.matrix_rank(grouped_crr, tol=1.0e-7),
)
check(
    "W177 corrected LC map is Ric0-controlled, gamma-traceless, and full rank",
    np.linalg.norm(grouped_crr - w177_predicted) < 2.0e-5
    and np.linalg.norm(gamma_matrix_grouped @ grouped_crr) < 2.0e-11
    and np.linalg.matrix_rank(grouped_crr, tol=1.0e-7) == spinor_dimension
    and np.linalg.norm(grouped_crr) > 15.0,
)
check(
    "prior W177 qualitative nonzero/full-rank result survives while its norm is superseded",
    abs(np.linalg.norm(legacy_w177) - 21.04321084) < 3.0e-4
    and np.linalg.matrix_rank(legacy_w177, tol=1.0e-7) == spinor_dimension
    and abs(np.linalg.norm(grouped_crr) - np.linalg.norm(legacy_w177)) > 1.0,
)
check(
    "unaligned native gamma/grouped curvature plant is rejected",
    abs(np.linalg.norm(unaligned_crr) - np.linalg.norm(grouped_crr)) > 0.1,
)

print("\nC. LC arrow and pointwise Spin-compatible P_IG witness")
lc_arrow = Arrow("S", "T*Y tensor R", "C_RR^LC", grouped_crr)
ig_matrix = pointwise_spin_pig_rr_matrix(gamma_grouped, eta_grouped)
ig_arrow = Arrow(
    "S",
    "T*Y tensor R",
    "C_RR^PIG,pointwise-Spin[rho(P_IG); P_IG independent of F_A]",
    ig_matrix,
)
combined_arrow = typed_sum((lc_arrow, ig_arrow))
check(
    "LC and pointwise Spin-PIG matrices concatenate only after separate arrow typing",
    combined_arrow.source == "S"
    and combined_arrow.target == "T*Y tensor R"
    and np.linalg.norm(ig_arrow.matrix) > 1.0
    and np.linalg.norm(gamma_matrix_grouped @ ig_arrow.matrix) < 2.0e-11
    and np.linalg.norm(
        combined_arrow.matrix - lc_arrow.matrix - ig_arrow.matrix
    )
    < TOL,
)
try:
    typed_sum(
        (
            lc_arrow,
            Arrow("S", "T*Y tensor S", "planted ill-typed IG", ig_matrix),
        )
    )
except ValueError:
    incompatible_arrow_rejected = True
else:
    incompatible_arrow_rejected = False
check(
    "LC/IG concatenation rejects a planted target mismatch",
    incompatible_arrow_rejected,
)

print("\nD. Frozen open-BV grammar: maximal supplied incidence, no invented rank")
ledger = partial_grammar_ledger()
check(
    "frozen ten-family grammar has 1110 words and 233100 slot-word tuples",
    len(TOKENS) == 10
    and ledger["ordered_words"] == 1110
    and ledger["syntactic_ceiling"] == 233100,
)
check(
    "open monomial saturates but does not exceed ghost/antifield caps",
    OPEN_MONOMIAL_GHOST_DEGREE == 2
    and OPEN_MONOMIAL_ANTIFIELD_NUMBER == 2
    and ledger["open_monomial_degrees"]["insertion_increment"] == 0,
)
check(
    "ill-typed and overdepth words are rejected",
    classify_word(("Tdelta", "deltaT"))[0] == "REJECTED"
    and classify_word(("1", "1", "1", "1"))[0] == "REJECTED",
)
check(
    "derivative and physical-field caps reject planted excess words",
    classify_word(("Q", "Q", "Q"))[0] == "REJECTED"
    and classify_word(("F_A", "F_A", "v"))
    == ("REJECTED", "physical-field degree exceeds 4"),
)
check(
    "undefined OmegaIG slot incidence remains rank-deferred",
    classify_word(("OmegaIG",))[0] == "RANK-DEFERRED"
    and ledger["hom_rank"] == "RANK-DEFERRED",
)
check(
    "identity and jGamma projector quotient rules canonicalize exactly",
    canonical_word(("1", "Q")) == ("Q",)
    and canonical_word(("jGamma", "jGamma")) == ("jGamma",)
    and canonical_word(("1", "1", "1")) == ("1",),
)
info("OPEN-BV ledger: " + json.dumps(ledger, sort_keys=True))

# This is a hostile syntax/control sign plant, not a CME computation.
x = np.array([1.0, 2.0, -0.5])
y = np.array([-1.0, 0.25, 3.0])
z = np.array([2.0, -1.5, 0.75])
good_jacobi = jacobi(np.cross, x, y, z)
bad_jacobi = (
    np.cross(x, np.cross(y, z))
    - np.cross(y, np.cross(z, x))
    + np.cross(z, np.cross(x, y))
)
check(
    "planted Jacobi aggregation sign is detected without claiming CME",
    np.linalg.norm(good_jacobi) < TOL and np.linalg.norm(bad_jacobi) > 1.0,
)

print("\n" + "=" * 96)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("VERDICT: LC-RIEMANN-IRREP-MAP-IS-HALF-TRACELESS-RICCI-ONLY")
print("VERDICT: W177-TYPED-LC-C_RR-NONZERO-FULL-RANK")
print("VERDICT: POINTWISE-SPIN-COMPATIBLE-PIG-WITNESS-SEPARATED")
print("VERDICT: OPEN-BV-TYPED-INCIDENCE-BUILT")
print("RESIDUAL: FULL-SP-IG-COVARIANCE-AND-OPEN-BV-HOM-RANK-DEFERRED")
print("NONCLAIM: NO-SOURCE-EOM-FACTORIZATION; NO-CME-TEST")
print("=" * 96)
