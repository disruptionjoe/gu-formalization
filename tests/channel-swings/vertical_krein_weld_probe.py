#!/usr/bin/env python3
r"""
VERTICAL--KREIN WELD.

Three questions are kept typed rather than collapsed:

1. SA-Y8 / Layer 0.  SHIAB-05's "Majorana scalar" is a map
      S+ tensor S+ -> Lambda^0_14.
   The Seiberg--Witten construction's "Majorana block" is built from the
   cross-chirality moment map
      mu: S+ tensor S- -> Lambda^2
   and then Clifford-acts as the even endomorphism c(mu).  Same word, different
   domain, codomain, and predicate.

2. SA-Y1 / physical channel.  A vertical component of a 14-dimensional
   one-form is not a Spin(9,5) scalar, but under
      Spin(9,5) -> Spin(3,1) x Spin(6,4)
   it lies in (1,10), hence is a four-dimensional Lorentz scalar multiplet.
   The physical fermion object is Psi^dagger K c(a_perp) Psi.  Test its
   Lorentz-scalar covariance, non-vanishing, and four-dimensional chirality.

3. B5 / P2.  Identify whether the four formerly-untyped X-sector special
   orbits are horizontal or vertical principal-symbol cells, and whether the
   canonical projected Rarita--Schwinger vertical symbol is nonzero on both
   product-rule families comprising X.

4. P1--P2 weld candidate.  Build the observer real structure and then compose
   the Krein pairing, rather than treating the reality map as inert.  The bare
   reality flips both base and internal chirality.  Its Krein-dual composite
       C_perp = K J_obs
   instead fixes base chirality, flips internal chirality, and has exactly the
   contragredient covariance of the B5 mirror slots.  Test whether the induced
   action gives one coherent parity to the vertical Clifford/RS symbol on both
   X families.  This can relate P2 to P1, but it does not identify C_perp with
   the metric-fibre loop holonomy or supply the formal differential/domain.

CONSTRUCTION FORK.  Program-native Cl(9,5), Krein pairing, symmetric metric
fibre, gamma-traceless RS projectors.  Complexified observer branching is used
only for the already-certified B5 support ledger.  No positive-Hilbert
substitution and no phase/domain selection.

Deterministic, foreground, numpy only, no writes, no network, no randomness.
EXIT 0 means all controls passed; the printed verdict carries the scope.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

import shiab_b5_native_packet_contract as packet_contract  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as b5_matrix  # noqa: E402
import shiab_b5_krein_mirror_orbit_reduction as b5_reduction  # noqa: E402


TOL = 1.0e-9
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0 + 0.0j]])
    for factor in factors:
        out = np.kron(out, factor)
    return out


def euclidean_jw_gammas(n_pairs: int) -> list[np.ndarray]:
    identity = np.eye(2, dtype=complex)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas: list[np.ndarray] = []
    for index in range(n_pairs):
        left = [sigma_3] * index
        right = [identity] * (n_pairs - 1 - index)
        gammas.append(kron_all(left + [sigma_1] + right))
        gammas.append(kron_all(left + [sigma_2] + right))
    return gammas


def signed_gammas(positive: int, negative: int) -> tuple[list[np.ndarray], np.ndarray]:
    euclidean = euclidean_jw_gammas((positive + negative) // 2)
    metric = np.array([1.0] * positive + [-1.0] * negative)
    gammas = [
        euclidean[index] if metric[index] > 0 else 1j * euclidean[index]
        for index in range(positive + negative)
    ]
    return gammas, metric


def product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    omega = product(gammas)
    scalar = complex(np.trace(omega @ omega) / omega.shape[0])
    if abs(scalar - 1.0) < TOL:
        return omega
    if abs(scalar + 1.0) < TOL:
        return 1j * omega
    raise AssertionError(f"chirality square is not scalar +/-1: {scalar}")


def commuting_real_structure(gammas: list[np.ndarray]) -> np.ndarray:
    """Unitary part U of the antilinear real structure U o conjugation.

    In the signed Jordan--Wigner representations used here, the product of the
    real gamma matrices commutes antilinearly with every Clifford generator.
    Both observer factors have real type, J^2=+1.
    """
    real_gammas = [
        gamma
        for gamma in gammas
        if np.max(np.abs(gamma.conj() - gamma)) < TOL
    ]
    unitary_part = product(real_gammas)
    norm_square = unitary_part @ unitary_part.conj().T
    scale = float(np.max(np.abs(np.diag(norm_square))))
    return unitary_part / np.sqrt(scale)


def antilinear_image(unitary_part: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Conjugation of a linear map by U o complex-conjugation."""
    return unitary_part @ matrix.conj() @ np.linalg.inv(unitary_part)


def spin_generator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return 0.25 * (left @ right - right @ left)


def clifford_error(gammas: list[np.ndarray], metric: np.ndarray) -> float:
    identity = np.eye(gammas[0].shape[0], dtype=complex)
    error = 0.0
    for left in range(len(gammas)):
        for right in range(len(gammas)):
            expected = (
                2.0 * metric[left] * identity if left == right else np.zeros_like(identity)
            )
            observed = gammas[left] @ gammas[right] + gammas[right] @ gammas[left]
            error = max(error, float(np.max(np.abs(observed - expected))))
    return error


def gamma_trace_projector(
    gammas: list[np.ndarray], metric: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Algebraic gamma-traceless projector on V tensor S.

    G = [gamma_i] and J = (1/n)[eta_i gamma_i]^T obey GJ=1, so P=1-JG
    is the signature-correct projector.  It is not an ordinary Hilbert
    orthogonal projector; that distinction is intentional.
    """
    vector_dimension = len(gammas)
    spinor_dimension = gammas[0].shape[0]
    gamma_trace = np.hstack(gammas)
    injection = np.vstack(
        [metric[index] * gammas[index] for index in range(vector_dimension)]
    ) / vector_dimension
    identity = np.eye(vector_dimension * spinor_dimension, dtype=complex)
    projector = identity - injection @ gamma_trace
    return gamma_trace, projector


@dataclass(frozen=True)
class BilinearObject:
    name: str
    input_chirality: str
    codomain: str
    role: str


SHIAB_MAJORANA = BilinearObject(
    "SHIAB-05 same-Weyl scalar",
    "S+ tensor S+",
    "Lambda^0_14",
    "same-chirality scalar mass spurion",
)
SW_MAJORANA = BilinearObject(
    "SW moment-map block",
    "S+ tensor S-",
    "Lambda^2 then c(mu) in End(S)",
    "cross-chirality source bilinear producing an even endomorphism",
)


print("=" * 88)
print("L0. SA-Y8 semantic object identity")
print("=" * 88)
same_majorana_object = (
    SHIAB_MAJORANA.input_chirality == SW_MAJORANA.input_chirality
    and SHIAB_MAJORANA.codomain == SW_MAJORANA.codomain
    and SHIAB_MAJORANA.role == SW_MAJORANA.role
)
check(
    "the two 'Majorana block' uses are HOMONYMS, not the same map",
    not same_majorana_object,
)
planted_copy = BilinearObject(
    SHIAB_MAJORANA.name,
    SHIAB_MAJORANA.input_chirality,
    SHIAB_MAJORANA.codomain,
    SHIAB_MAJORANA.role,
)
check(
    "planted same-object control is recognized",
    (
        planted_copy.input_chirality == SHIAB_MAJORANA.input_chirality
        and planted_copy.codomain == SHIAB_MAJORANA.codomain
        and planted_copy.role == SHIAB_MAJORANA.role
    ),
)


print("\n" + "=" * 88)
print("P1. Factorized program-native Cl(9,5) = Cl(3,1) hat-tensor Cl(6,4)")
print("=" * 88)
gamma_4, eta_4 = signed_gammas(3, 1)
gamma_10, eta_10 = signed_gammas(6, 4)
omega_4_small = normalized_chirality(gamma_4)
omega_10 = normalized_chirality(gamma_10)
identity_4 = np.eye(4, dtype=complex)
identity_32 = np.eye(32, dtype=complex)

base_gammas = [np.kron(gamma, identity_32) for gamma in gamma_4]
vertical_gammas = [np.kron(omega_4_small, gamma) for gamma in gamma_10]
gamma_14 = base_gammas + vertical_gammas
eta_14 = np.concatenate((eta_4, eta_10))
omega_4 = np.kron(omega_4_small, identity_32)

clifford_defect = clifford_error(gamma_14, eta_14)
check("factorized gammas satisfy Cl(9,5)", clifford_defect < TOL, f"{clifford_defect:.2e}")
check(
    "signature is exactly (9,5)",
    int(np.sum(eta_14 > 0)) == 9 and int(np.sum(eta_14 < 0)) == 5,
)

positive_gammas = [
    gamma_14[index] for index, sign in enumerate(eta_14) if sign > 0
]
krein = product(positive_gammas)
identity_128 = np.eye(128, dtype=complex)
check("K is Hermitian", np.max(np.abs(krein.conj().T - krein)) < TOL)
check("K is invertible", abs(np.linalg.det(krein)) > 1.0e-6)

spin_generators_14 = [
    spin_generator(gamma_14[left], gamma_14[right])
    for left, right in combinations(range(14), 2)
]
krein_invariance = max(
    float(np.max(np.abs(generator.conj().T @ krein + krein @ generator)))
    for generator in spin_generators_14
)
check(
    "K is Spin(9,5)-invariant (all 91 infinitesimal generators)",
    krein_invariance < TOL,
    f"{krein_invariance:.2e}",
)


print("\n" + "=" * 88)
print("P2. The vertical Lambda^1 component is a 4D Lorentz scalar multiplet")
print("=" * 88)
lorentz_generators = [
    spin_generator(base_gammas[left], base_gammas[right])
    for left, right in combinations(range(4), 2)
]


def scalar_covariance_defect(bilinear_matrix: np.ndarray) -> float:
    return max(
        float(
            np.max(
                np.abs(
                    generator.conj().T @ bilinear_matrix
                    + bilinear_matrix @ generator
                )
            )
        )
        for generator in lorentz_generators
    )


vertical_bilinears = [krein @ gamma for gamma in vertical_gammas]
horizontal_bilinears = [krein @ gamma for gamma in base_gammas]
vertical_scalar_defect = max(scalar_covariance_defect(matrix) for matrix in vertical_bilinears)
horizontal_scalar_defects = [scalar_covariance_defect(matrix) for matrix in horizontal_bilinears]
check(
    "all ten K c(a_perp) bilinears are 4D Lorentz scalars",
    vertical_scalar_defect < TOL,
    f"max defect {vertical_scalar_defect:.2e}",
)
check(
    "planted horizontal one-form components are not individual Lorentz scalars",
    min(horizontal_scalar_defects) > 1.0e-6,
    f"min defect {min(horizontal_scalar_defects):.2e}",
)

vertical_chirality_defect = max(
    float(np.max(np.abs(matrix @ omega_4 + omega_4 @ matrix)))
    for matrix in vertical_bilinears
)
identity_pairing_preserves = all(
    np.max(np.abs(gamma @ omega_4 - omega_4 @ gamma)) < TOL
    for gamma in vertical_gammas
)
check(
    "K c(a_perp) is cross-chirality in 4D",
    vertical_chirality_defect < TOL,
    f"{vertical_chirality_defect:.2e}",
)
check(
    "identity-pairing control leaves c(a_perp) chirality-preserving",
    identity_pairing_preserves,
)
check(
    "the vertical bilinear is nonzero and Hermitian",
    all(
        np.linalg.norm(matrix) > 1.0
        and np.max(np.abs(matrix.conj().T - matrix)) < TOL
        for matrix in vertical_bilinears
    ),
)

# A connection component also carries an endomorphism/gauge factor.  The
# observer-compatible internal Spin(6,4) generators commute with Spin(3,1), so
# including them preserves the scalar conclusion.  A mixed base--vertical
# generator is the planted counterexample: "vertical one-form" alone is not
# enough if its endomorphism breaks the observer split.
internal_generators = [
    spin_generator(vertical_gammas[index], vertical_gammas[(index + 1) % 10])
    for index in range(10)
]
connection_bilinears = [
    krein @ vertical_gammas[index] @ internal_generators[index]
    for index in range(10)
]
internal_connection_defect = max(
    scalar_covariance_defect(matrix) for matrix in connection_bilinears
)
mixed_generator = spin_generator(base_gammas[0], vertical_gammas[0])
mixed_connection_defect = scalar_covariance_defect(
    krein @ vertical_gammas[0] @ mixed_generator
)
check(
    "observer-compatible internal connection factors preserve 4D scalarity",
    internal_connection_defect < TOL,
    f"{internal_connection_defect:.2e}",
)
check(
    "planted mixed base--vertical connection factor breaks 4D scalarity",
    mixed_connection_defect > 1.0e-6,
    f"{mixed_connection_defect:.2e}",
)


print("\n" + "=" * 88)
print("P3. Gamma-traceless product blocks: the canonical vertical RS symbol reaches X")
print("=" * 88)
trace_4, projector_4 = gamma_trace_projector(gamma_4, eta_4)
trace_10, projector_10 = gamma_trace_projector(gamma_10, eta_10)
check(
    "RS4 projector is idempotent with rank 12",
    np.max(np.abs(projector_4 @ projector_4 - projector_4)) < TOL
    and np.linalg.matrix_rank(projector_4, tol=TOL) == 12,
)
check(
    "RS10 projector is idempotent with rank 288",
    np.max(np.abs(projector_10 @ projector_10 - projector_10)) < TOL
    and np.linalg.matrix_rank(projector_10, tol=TOL) == 288,
)
check(
    "product-rule X dimension is 384 + 1152 = 1536",
    12 * 32 + 4 * 288 == 1536,
)

# X family A: RS(3,1) tensor S(6,4).  The vertical Clifford symbol is
# (1_V4 tensor omega_4) tensor gamma_10(v), and stays inside RS4.
rs4_chirality = np.kron(np.eye(4), omega_4_small)
rs4_vertical_factor = projector_4 @ rs4_chirality @ projector_4
check(
    "vertical symbol is nonzero on RS4 tensor S10 (X32/X23 family)",
    np.linalg.matrix_rank(rs4_vertical_factor, tol=TOL) == 12,
)
check(
    "RS4 gamma trace remains zero after the vertical symbol",
    np.max(np.abs(trace_4 @ rs4_vertical_factor)) < TOL,
)

# X family B: S(3,1) tensor RS(6,4).  Project the internal Clifford symbol
# back to gamma-traceless vector-spinors and check every vertical direction.
identity_vector_10 = np.eye(10, dtype=complex)
rs10_symbols = [
    projector_10
    @ np.kron(identity_vector_10, gamma)
    @ projector_10
    for gamma in gamma_10
]
rs10_nonzero_ranks = [
    int(np.linalg.matrix_rank(symbol, tol=TOL)) for symbol in rs10_symbols
]
check(
    "vertical symbol is nonzero on S4 tensor RS10 (X2T/X1T family), all directions",
    min(rs10_nonzero_ranks) > 0,
    f"ranks {sorted(set(rs10_nonzero_ranks))}",
)
check(
    "RS10 gamma trace remains zero after every projected symbol",
    max(float(np.max(np.abs(trace_10 @ symbol))) for symbol in rs10_symbols) < TOL,
)
rs10_chirality = np.kron(identity_vector_10, omega_10)
rs10_cross_defect = max(
    float(np.max(np.abs(symbol @ rs10_chirality + rs10_chirality @ symbol)))
    for symbol in rs10_symbols
)
check(
    "the projected RS10 vertical symbol flips internal chirality",
    rs10_cross_defect < TOL,
    f"{rs10_cross_defect:.2e}",
)


print("\n" + "=" * 88)
print("P4. B5 special-orbit typing")
print("=" * 88)


def symbol_parts(
    source: b5_matrix.HType, target: b5_matrix.HType
) -> tuple[int, int]:
    base_part = int(
        source.d5_weight == target.d5_weight
        and target.left_dim in b5_matrix.su2_vector_targets(source.left_dim)
        and target.right_dim in b5_matrix.su2_vector_targets(source.right_dim)
    )
    fiber_part = int(
        source.left_dim == target.left_dim
        and source.right_dim == target.right_dim
    ) * b5_matrix.vector_tensor_decomposition(source.d5_weight).get(
        target.d5_weight, 0
    )
    return base_part, fiber_part


cells = b5_reduction.nonzero_cells()
joint_orbits = b5_reduction.joint_orbits(cells)
special_orbits = sorted(
    tuple(sorted(orbit)) for orbit in joint_orbits if len(orbit) == 2
)
x_orbits = [
    orbit for orbit in special_orbits if orbit[0][0].startswith("X:")
]


def cell_parts(cell: tuple[str, str]) -> tuple[int, int]:
    source, target = cell
    return symbol_parts(
        b5_matrix.TYPES[b5_matrix.SLOT_BY_NAME[source].h_type],
        b5_matrix.TYPES[b5_matrix.SLOT_BY_NAME[target].h_type],
    )


check("B5 has ten special orbits and four X-sector special orbits",
      len(special_orbits) == 10 and len(x_orbits) == 4)
check(
    "all ten special orbits are vertical-only symbol cells",
    all(cell_parts(orbit[0]) == (0, 1) for orbit in special_orbits),
)
check(
    "all four formerly-untyped X-sector orbits are vertical-only",
    all(cell_parts(orbit[0]) == (0, 1) for orbit in x_orbits),
)
non_special_cells = [
    cell
    for orbit in joint_orbits
    if len(orbit) == 4
    for cell in orbit
]
check(
    "planted support control: the complete B5 class also contains horizontal cells",
    any(cell_parts(cell)[0] == 1 for cell in non_special_cells),
)

x_type_names = {
    b5_matrix.SLOT_BY_NAME[orbit[0][0]].h_type for orbit in x_orbits
}
rs4_family_present = any(name.startswith(("X32", "X23")) for name in x_type_names)
rs10_family_present = any(name.startswith(("X2T", "X1T")) for name in x_type_names)
check(
    "the four X orbits cover both product-rule X families",
    rs4_family_present and rs10_family_present,
    f"{sorted(x_type_names)}",
)


print("\n" + "=" * 88)
print("P5. Krein-dual coflip candidate: one relative parity on all vertical symbols")
print("=" * 88)

# Each observer factor has a real structure J=U o conjugation that commutes
# with its Clifford generators.  Because normalized chirality contains i in
# both signatures, the bare observer reality flips BOTH base and internal
# chirality.  This is not the normal-only B5 support mirror.
j4_unitary = commuting_real_structure(gamma_4)
j10_unitary = commuting_real_structure(gamma_10)
observer_reality = np.kron(j4_unitary, j10_unitary)
internal_chirality = np.kron(identity_4, omega_10)
total_chirality = omega_4 @ internal_chirality

j4_clifford_defect = max(
    float(np.max(np.abs(antilinear_image(j4_unitary, gamma) - gamma)))
    for gamma in gamma_4
)
j10_clifford_defect = max(
    float(np.max(np.abs(antilinear_image(j10_unitary, gamma) - gamma)))
    for gamma in gamma_10
)
check(
    "factor real structures commute antilinearly with every Clifford generator",
    max(j4_clifford_defect, j10_clifford_defect) < TOL,
)
check(
    "both factor real structures square to +1",
    np.max(np.abs(j4_unitary @ j4_unitary.conj() - identity_4)) < TOL
    and np.max(np.abs(j10_unitary @ j10_unitary.conj() - identity_32)) < TOL,
)
check(
    "the bare observer reality flips base and internal chirality together",
    np.max(np.abs(antilinear_image(observer_reality, omega_4) + omega_4)) < TOL
    and np.max(
        np.abs(antilinear_image(observer_reality, internal_chirality) + internal_chirality)
    )
    < TOL
    and np.max(
        np.abs(antilinear_image(observer_reality, total_chirality) - total_chirality)
    )
    < TOL,
)

# Compose the pairing.  C_perp=K J_obs is an antilinear Riesz/duality map:
# it transforms infinitesimal observer generators contragrediently, not by
# ordinary commutation.  This is the correct covariance predicate for the B5
# mirror slots, which are dual H_C representations.
krein_dual_coflip = krein @ observer_reality
internal_spin_generators = [
    spin_generator(vertical_gammas[left], vertical_gammas[right])
    for left, right in combinations(range(10), 2)
]
observer_spin_generators = lorentz_generators + internal_spin_generators
contragredient_defect = max(
    float(
        np.max(
            np.abs(
                antilinear_image(krein_dual_coflip, generator)
                + generator.conj().T
            )
        )
    )
    for generator in observer_spin_generators
)
check(
    "C_perp = K J_obs is an antilinear involution",
    np.max(
        np.abs(
            krein_dual_coflip @ krein_dual_coflip.conj() - identity_128
        )
    )
    < TOL,
)
check(
    "C_perp has the B5 support action: base chirality fixed, internal flipped",
    np.max(np.abs(antilinear_image(krein_dual_coflip, omega_4) - omega_4))
    < TOL
    and np.max(
        np.abs(
            antilinear_image(krein_dual_coflip, internal_chirality)
            + internal_chirality
        )
    )
    < TOL
    and np.max(
        np.abs(
            antilinear_image(krein_dual_coflip, total_chirality)
            + total_chirality
        )
    )
    < TOL,
)
check(
    "C_perp is observer-contragredient-covariant",
    contragredient_defect < TOL,
    f"{contragredient_defect:.2e}",
)

# Planted near-miss: applying only the internal real structure has the desired
# chirality labels, but complex conjugation acts on the whole tensor product,
# so it is not Lorentz-covariant.  The Krein composition is load-bearing.
internal_only_reality = np.kron(identity_4, j10_unitary)
internal_only_covariance_defect = max(
    float(
        np.max(
            np.abs(
                antilinear_image(internal_only_reality, generator) - generator
            )
        )
    )
    for generator in lorentz_generators
)
check(
    "planted internal-only reality has the right labels but fails Lorentz covariance",
    np.max(
        np.abs(
            antilinear_image(internal_only_reality, omega_4) - omega_4
        )
    )
    < TOL
    and np.max(
        np.abs(
            antilinear_image(internal_only_reality, internal_chirality)
            + internal_chirality
        )
    )
    < TOL
    and internal_only_covariance_defect > 1.0e-6,
    f"covariance defect {internal_only_covariance_defect:.2e}",
)

# Factor C_perp so its induced action can be checked directly on the two
# product-rule RS families.  The vector factor uses the native signature
# metric.  Both gamma-traceless projectors are preserved.
krein_4 = product(
    [gamma for gamma, sign in zip(gamma_4, eta_4) if sign > 0]
)
krein_10 = product(
    [gamma for gamma, sign in zip(gamma_10, eta_10) if sign > 0]
)
dual_4 = krein_4 @ j4_unitary
dual_10 = krein_10 @ j10_unitary
factorized_dual = np.kron(dual_4, dual_10)
check(
    "C_perp factorizes into the two observer duality maps",
    np.max(np.abs(factorized_dual - krein_dual_coflip)) < TOL,
)

dual_rs4 = np.kron(np.diag(eta_4), dual_4)
dual_rs10 = np.kron(np.diag(eta_10), dual_10)
check(
    "the induced duality preserves both gamma-traceless RS projectors",
    np.max(np.abs(antilinear_image(dual_rs4, projector_4) - projector_4))
    < TOL
    and np.max(
        np.abs(antilinear_image(dual_rs10, projector_10) - projector_10)
    )
    < TOL,
)

base_gamma_dual_signs = []
for index, gamma in enumerate(gamma_4):
    transformed = eta_4[index] * antilinear_image(dual_4, gamma)
    base_gamma_dual_signs.append(
        1 if np.max(np.abs(transformed - gamma)) < TOL else -1
    )
vertical_gamma_dual_signs = []
for index, gamma in enumerate(gamma_10):
    transformed = eta_10[index] * antilinear_image(dual_10, gamma)
    vertical_gamma_dual_signs.append(
        1 if np.max(np.abs(transformed - gamma)) < TOL else -1
    )
check(
    "horizontal Clifford symbol is coflip-even (contrast control)",
    base_gamma_dual_signs == [1] * 4,
)
check(
    "all ten vertical Clifford directions have one coflip-odd parity",
    vertical_gamma_dual_signs == [-1] * 10,
)

rs4_factor_dual_defect = np.max(
    np.abs(
        antilinear_image(dual_rs4, rs4_vertical_factor)
        - rs4_vertical_factor
    )
)
rs10_projected_parities = []
for index, symbol in enumerate(rs10_symbols):
    # Projector preservation means the induced sign of P(I tensor gamma_i)P
    # is the same as the internal gamma sign.  Include the vertical-vector
    # duality eta_i, exactly as for the spinor symbol.
    gamma_sign = (
        1
        if np.max(
            np.abs(
                antilinear_image(dual_10, gamma_10[index]) - gamma_10[index]
            )
        )
        < TOL
        else -1
    )
    rs10_projected_parities.append(int(eta_10[index]) * gamma_sign)
check(
    "the RS4 tensor S10 X family inherits the same coflip-odd parity",
    rs4_factor_dual_defect < TOL
    and vertical_gamma_dual_signs == [-1] * 10,
)
check(
    "the S4 tensor RS10 X family inherits the same coflip-odd parity",
    rs10_projected_parities == [-1] * 10,
)
check(
    "all ten B5 special edges therefore share one relative algebraic parity",
    all(cell_parts(orbit[0]) == (0, 1) for orbit in special_orbits)
    and vertical_gamma_dual_signs == [-1] * 10
    and rs10_projected_parities == [-1] * 10,
)


print("\n" + "=" * 88)
print("P6. Fail-closed native packet boundary")
print("=" * 88)
partial_packet = dict(packet_contract.UNFROZEN)
# Record the conditional algebraic coflip candidate without pretending it is
# already identified with the metric-fibre loop holonomy or that the remaining
# operator packet has been built.
partial_packet["coflip_linearity_and_phases"] = {
    "kind": "antilinear",
    "candidate": "K_times_J_observer",
    "special_edge_relative_parity": "uniform",
    "status": "conditional_not_frozen",
}
try:
    packet_contract.admit(partial_packet)
except AssertionError:
    partial_rejected = True
else:
    partial_rejected = False
check(
    "the conditional one-bit weld does not masquerade as the five-field native packet",
    partial_rejected,
)


print("\n" + "=" * 88)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID")
    sys.exit(1)

print(
    "VERDICT: L0-HOMONYM + 4D-SCALAR-BRIDGE + "
    "P2-VERTICAL-SYMBOL-TYPED + CONDITIONAL-P1-P2-ONE-BIT-WELD"
)
print("=" * 88)
print(
    "\nSA-Y8.  The SW moment-map 'Majorana block' and SHIAB-05's same-Weyl\n"
    "Lambda^0 scalar are different mathematical objects.  T3 does not supply\n"
    "the conditional SA-Y8 spurion merely by carrying the same nickname.\n"
    "\nSA-Y1.  Lambda^1_14 and Lambda^0_14 remain different Spin(9,5) channels,\n"
    "but the physical reduction resolves the mass question: the vertical\n"
    "(1,10) component is a 4D Lorentz-scalar multiplet, and Psi^dag K c(a_perp)\n"
    "Psi is nonzero, Hermitian, and cross-chirality.  The conclusion survives\n"
    "an observer-compatible internal connection factor and correctly fails for\n"
    "a planted mixed base--vertical factor.  Thus k=0 is unique only\n"
    "for a bare full-Spin(9,5) scalar carrier; it is not the unique route to a\n"
    "4D mass-type Yukawa after the declared 4+10 split.\n"
    "\nP2.  The four X-sector special orbits are not an unclassified abstract\n"
    "sector: all four are vertical-only principal-symbol edges, split across\n"
    "RS4 tensor S10 and S4 tensor RS10, and the canonical projected vertical RS\n"
    "symbol is nonzero on both families.  P2 is therefore typed as the\n"
    "phase/orientation of the program-native vertical RS symbol on X.\n"
    "\nP1--P2.  The bare observer reality has the wrong mirror action; after the\n"
    "Krein pairing is composed, C_perp=K J_obs is an antilinear involution with\n"
    "exactly the B5 dual-slot action.  It gives one uniform relative parity to\n"
    "the vertical symbol on S and both X families, while a horizontal control\n"
    "has the opposite parity.  Conditional on identifying this algebraic\n"
    "duality with the physical fibre-loop coflip and the actual differential,\n"
    "P2 is not a second datum: the same global orientation bit relates all ten\n"
    "special edges.\n"
    "\nBOUNDARY.  The fibre-loop-to-C_perp identification, normalized 20-slot\n"
    "pairing table, formal-adjoint sign of the written differential, Green\n"
    "boundary form, and common domain remain unbuilt.  Therefore no absolute\n"
    "B5 delta_e assignment, signed phase sum, or native packet is selected."
)
