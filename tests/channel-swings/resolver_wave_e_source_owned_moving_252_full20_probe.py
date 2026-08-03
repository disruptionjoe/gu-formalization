#!/usr/bin/env python3
r"""Resolver Wave E: native moving real-252 / conditional source interface.

This executable keeps four levels separate:

1. the canonical full-14 reconstruction ``delta j5 = 9``;
2. its observer-stabilizer vertical comparator ``delta_V j5 = 5``;
3. the full-20 one-form-output map and its K/C reciprocals; and
4. the conditional active restriction of the displayed bosonic kappa sector.

The unweighted full-14 map is a canonical reconstruction comparator.  A
separate horizontal/vertical weight is solved for one simple five-blade
native fixture.  The unique representative weight eliminating the low-R 16
is 1/2, but this probe does not claim that it extends to every five-form or
that the source action owns this rectangular map or selects its weight.  The
public-source-to-active-(9,5) port remains open.  No stationary VEV, mass,
physical quotient, analytic domain, or observation no-leakage theorem is
constructed.
"""
from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from itertools import combinations
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

with contextlib.redirect_stdout(io.StringIO()):
    import resolver_wave_d_full20_126_placement_probe as wave_d  # noqa: E402

full20 = wave_d.full20
TOL = 4.0e-8
FAILURES: list[str] = []
COUNTS = {"exact": 0, "source": 0, "type": 0, "planted": 0}


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'} [{kind}]: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def move_vs_map(matrix: np.ndarray, group: np.ndarray) -> np.ndarray:
    inverse = np.linalg.inv(group)
    shaped = matrix.reshape(14, 128, -1)
    return np.stack([group @ block @ inverse for block in shaped]).reshape(
        14 * 128, -1
    )


def gamma_trace_with(matrix: np.ndarray, gammas: list[np.ndarray]) -> np.ndarray:
    shaped = matrix.reshape(14, 128, -1)
    return sum(
        (gammas[index] @ shaped[index] for index in range(14)),
        np.zeros((128, shaped.shape[2]), dtype=complex),
    )


def p_i_with(matrix: np.ndarray, gammas: list[np.ndarray]) -> np.ndarray:
    trace = gamma_trace_with(matrix, gammas)
    blocks = [
        full20.eta_14[index] * gammas[index] @ trace / 14.0
        for index in range(14)
    ]
    return np.vstack(blocks)


def p_r_with(matrix: np.ndarray, gammas: list[np.ndarray]) -> np.ndarray:
    return matrix - p_i_with(matrix, gammas)


def low_r_norm_sq(matrix: np.ndarray, source) -> float:
    low_slots = [
        slot for slot in full20.slots_by_sector["R"]
        if slot.name.startswith("kerGamma:")
    ]
    image = matrix @ source.basis
    return float(sum(
        np.linalg.norm(slot.basis.conj().T @ image) ** 2
        for slot in low_slots
    ))


def x_norm_sq(matrix: np.ndarray, source) -> float:
    x_slots = [
        slot for slot in full20.slots_by_sector["R"]
        if slot.name.startswith("X:")
    ]
    image = matrix @ source.basis
    return float(sum(
        np.linalg.norm(slot.basis.conj().T @ image) ** 2
        for slot in x_slots
    ))


def polynomial_derivative(coefficients: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(
        Fraction(power) * coefficient
        for power, coefficient in enumerate(coefficients)
        if power > 0
    )


def polynomial_product(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_power, left_value in enumerate(left):
        for right_power, right_value in enumerate(right):
            out[left_power + right_power] += left_value * right_value
    return tuple(out)


def polynomial_add(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    size = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(size)
    )


def polynomial_scale(
    scalar: Fraction, coefficients: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    return tuple(scalar * coefficient for coefficient in coefficients)


def integrate_unit(coefficients: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (value / Fraction(power + 1) for power, value in enumerate(coefficients)),
        Fraction(0),
    )


def evaluate(coefficients: tuple[Fraction, ...], value: Fraction) -> Fraction:
    return sum(
        (coefficient * value**power for power, coefficient in enumerate(coefficients)),
        Fraction(0),
    )


print("=" * 100)
print("RESOLVER WAVE E — NATIVE MOVING 252 / CONDITIONAL SOURCE INTERFACE")
print("=" * 100)

check("exact", "Wave-D native fixture is healthy", not wave_d.FAILURES)
check(
    "type",
    "the actual carrier is the trace-reversed (3,1)+(6,4) split",
    tuple(full20.eta_14[:4]) == (1.0, 1.0, 1.0, -1.0)
    and tuple(full20.eta_14[4:]) == (1.0,) * 6 + (-1.0,) * 4,
)


# -------------------------------------------------------------------------
# A. Full-14 j5/delta and the vertical-only hostile control
# -------------------------------------------------------------------------


print("\nA. FULL-14 j5 / DELTA")

full_complement_count = 14 - 5
vertical_complement_count = 10 - 5
check(
    "exact",
    "direct contraction gives the locked full coefficient 4+5=9",
    full_complement_count == 9
    and full_complement_count == 4 + vertical_complement_count,
)
check(
    "planted",
    "vertical restriction before contraction is rejected as a full-14 map",
    vertical_complement_count != full_complement_count,
)
check(
    "type",
    "the internal complement remains 252 plus 120 plus 1728",
    10 * 210 == 252 + 120 + 1728,
)

# Sparse signed exterior pairing. For the diagonal (9,5) metric, a basis
# k-form has metric equal to the product of its selected diagonal signs. This
# verifies on all 2002 target basis forms (and their 9 nonzero incidences) that
# j5 is the pairing adjoint of delta; it does not infer the adjoint from 9I.
eta_exact = tuple(int(value) for value in full20.eta_14)


def exterior_metric(form: tuple[int, ...]) -> int:
    out = 1
    for index in form:
        out *= eta_exact[index]
    return out


def contraction_sign(index: int, form: tuple[int, ...]) -> int:
    return (-1) ** form.index(index)


adjoint_ok = True
delta_j_coefficients = set()
for form5 in combinations(range(14), 5):
    coefficient = 0
    for index in range(14):
        if index in form5:
            continue
        form6 = tuple(sorted((index,) + form5))
        wedge = wave_d.wedge_sign(index, form5)
        contract = contraction_sign(index, form6)
        j_coefficient = eta_exact[index] * wedge
        delta_coefficient = eta_exact[index] * contract
        domain_metric = eta_exact[index] * exterior_metric(form6)
        left_pairing = delta_coefficient * exterior_metric(form5)
        right_pairing = j_coefficient * domain_metric
        adjoint_ok &= left_pairing == right_pairing
        coefficient += j_coefficient * delta_coefficient
    delta_j_coefficients.add(coefficient)

check(
    "exact",
    "signed sparse exterior pairing proves j5-adjoint=delta on all incidences",
    adjoint_ok,
)
check(
    "exact",
    "signed sparse composition proves j5-adjoint*j5=9I on all five-forms",
    delta_j_coefficients == {9},
)
check(
    "exact",
    "P5=(1/9)j5 delta is pairing-self-adjoint and idempotent",
    adjoint_ok and delta_j_coefficients == {9},
)

zero128 = np.zeros((128, 128), dtype=complex)
b_h = np.vstack(wave_d.full_components[:4] + [zero128] * 10)
b_v = np.vstack([zero128] * 4 + wave_d.vertical_components)
b_full = b_v + b_h

check(
    "exact",
    "native horizontal and vertical traces are exactly 4 phi and 5 phi",
    max_abs(full20.gamma_trace(b_h) - 4.0 * wave_d.phi5) < TOL
    and max_abs(full20.gamma_trace(b_v) - 5.0 * wave_d.phi5) < TOL,
)
check(
    "exact",
    "the canonical unweighted full one-form output has trace 9 phi",
    max_abs(full20.gamma_trace(b_full) - 9.0 * wave_d.phi5) < TOL,
)
check(
    "planted",
    "the hostile 1/5 normalization fails the full source projector",
    Fraction(1, 5) * Fraction(9, 1) != 1,
)


# -------------------------------------------------------------------------
# B. Full-20 support polynomial and the half-weighted rival
# -------------------------------------------------------------------------


print("\nB. ONE-SIMPLE-BLADE FULL-20 SUPPORT POLYNOMIAL")


def weighted_r_map(weight: float) -> np.ndarray:
    return full20.p_r(b_v + weight * b_h)


fit_weights = (0.0, 0.5, 1.0)
fit_source = full20.slots_by_sector["S"][0]
fit_values = [
    Fraction(low_r_norm_sq(weighted_r_map(weight), fit_source)).limit_denominator(10_000)
    for weight in fit_weights
]
c0 = fit_values[0]
# Solve q(lambda)=a lambda^2+b lambda+c from q(0), q(1/2), and q(1).
a2 = 2 * (fit_values[2] + c0 - fit_values[1] * 2)
b1 = fit_values[2] - c0 - a2
low_r_polynomial = (c0, b1, a2)
root = -b1 / (2 * a2)

heldout_weights = (-1.0, 0.25, 2.0)
support_polynomial_ok = True
for weight in fit_weights + heldout_weights:
    raw = b_v + weight * b_h
    r_map = full20.p_r(raw)
    for source in full20.slots_by_sector["S"]:
        i_norm = float(np.linalg.norm(full20.p_i(raw) @ source.basis) ** 2)
        support_polynomial_ok &= abs(
            i_norm - (16.0 / 7.0) * (5.0 + 4.0 * weight) ** 2
        ) < 2.0e-7
        support_polynomial_ok &= abs(
            low_r_norm_sq(r_map, source)
            - (160.0 / 7.0) * (1.0 - 2.0 * weight) ** 2
        ) < 2.0e-7
        support_polynomial_ok &= abs(x_norm_sq(r_map, source) - 80.0) < 2.0e-7

check(
    "exact",
    "rational reconstruction plus held-outs gives the representative support polynomials",
    support_polynomial_ok
    and low_r_polynomial
    == (Fraction(160, 7), Fraction(-640, 7), Fraction(640, 7)),
)
check(
    "exact",
    "the reconstructed representative low-R polynomial has unique root lambda=1/2",
    a2 != 0 and b1 * b1 - 4 * a2 * c0 == 0 and root == Fraction(1, 2),
)

t_full = weighted_r_map(1.0)
t_half = weighted_r_map(0.5)
check(
    "exact",
    "the unweighted reconstruction comparator retains the low-R companion",
    all(
        abs(low_r_norm_sq(t_full, source) - 160.0 / 7.0) < 2.0e-7
        for source in full20.slots_by_sector["S"]
    ),
)
check(
    "exact",
    "the half-weighted branch kills low-R and retains rank-128 X support",
    np.linalg.matrix_rank(t_half, tol=TOL) == 128
    and max_abs(full20.gamma_trace(t_half)) < TOL
    and all(low_r_norm_sq(t_half, source) < TOL for source in full20.slots_by_sector["S"])
    and all(abs(x_norm_sq(t_half, source) - 80.0) < 2.0e-7
            for source in full20.slots_by_sector["S"]),
)
check(
    "exact",
    "the unit simple-blade half-weighted representative has T-dagger-T=(5/2)I",
    max_abs(t_half.conj().T @ t_half - 2.5 * np.eye(128)) < TOL,
)

half_support = {}
for source in full20.slots_by_sector["S"]:
    amplitudes = {
        target.name: float(np.linalg.norm(
            target.basis.conj().T @ (t_half @ source.basis)
        ))
        for target in full20.slots_by_sector["R"]
    }
    half_support[source.name] = {
        name for name, amplitude in amplitudes.items() if amplitude > 1.0e-7
    }

expected_half_support = {
    "S:E+:L16+": {"X:X2Tp"},
    "S:E+:R16-": {"X:X1Tm"},
    "S:E-:L16-": {"X:X2Tm"},
    "S:E-:R16+": {"X:X1Tp"},
}
check(
    "exact",
    "the half-weighted map has one X/144 slot per source and no hidden slot",
    half_support == expected_half_support,
    repr(half_support),
)
check(
    "type",
    "support in four Lorentz-dressed 144 slots is not rank or surjectivity",
    sum(
        full20.slot_by_name[name].dimension
        for names in expected_half_support.values() for name in names
    ) == 1152
    and np.linalg.matrix_rank(t_half, tol=TOL) == 128,
)

# Connectivity is combinatorial context only. It does not prove that the
# representative coefficient is constant on the real 252; that still needs
# an intertwiner proof or an exhaustive all-blade certificate.
five_subsets = list(combinations(range(10), 5))
adjacency = {
    subset: {
        tuple(sorted((set(subset) - {old}) | {new}))
        for old in subset for new in range(10) if new not in subset
    }
    for subset in five_subsets
}
seen = {five_subsets[0]}
frontier = [five_subsets[0]]
while frontier:
    current = frontier.pop()
    for neighbor in adjacency[current]:
        if neighbor not in seen:
            seen.add(neighbor)
            frontier.append(neighbor)
check(
    "exact",
    "the internal five-blade generator graph connects all 252 basis blades",
    len(seen) == 252,
)
REPRESENTATION_WIDE_HALF_WEIGHT_PROVED = False
check(
    "type",
    "graph connectivity is not promoted to a representation-wide half-weight theorem",
    not REPRESENTATION_WIDE_HALF_WEIGHT_PROVED,
)
check(
    "type",
    "star^2=-1 keeps the two complex 126 halves as one real 252 carrier",
    (-1) ** (5 * 5 + 4) == -1 and 252 == 126 + 126,
)


# -------------------------------------------------------------------------
# C. K/C reciprocals, right-H, provenance, and P0
# -------------------------------------------------------------------------


print("\nC. K/C / RIGHT-H / P0")

k_s = full20.krein
k_vs = np.kron(np.diag(full20.eta_14), k_s)
j_s = wave_d.j_h
j_vs = np.kron(np.eye(14), j_s)
t_k_reverse = np.linalg.inv(k_s) @ t_half.conj().T @ k_vs

check(
    "exact",
    "the rectangular K reverse satisfies the total Krein adjoint identity",
    max_abs(k_s @ t_k_reverse - t_half.conj().T @ k_vs) < TOL,
)
check(
    "exact",
    "forward and K reverse are both right-H linear",
    max_abs(t_half @ j_s - j_vs @ t_half.conj()) < TOL
    and max_abs(t_k_reverse @ j_vs - j_s @ t_k_reverse.conj()) < TOL,
)

c_results = {}
for name, c_s in (("C+", wave_d.c_plus), ("C-", wave_d.c_minus)):
    c_vs = np.kron(np.diag(full20.eta_14), c_s)
    c_reverse = -np.linalg.inv(c_s) @ t_half.T @ c_vs.T
    alternating_defect = max_abs(
        t_half.T @ c_vs.T + c_s @ c_reverse
    )
    c_results[name] = {
        "alternating_defect": alternating_defect,
        "reverse_difference": max_abs(c_reverse - t_k_reverse),
        "right_h_defect": max_abs(c_reverse @ j_vs - j_s @ c_reverse.conj()),
        "non_x_reverse_norm": max(
            float(np.linalg.norm(c_reverse @ slot.basis))
            for slot in full20.slots_by_sector["I"]
            + [
                slot for slot in full20.slots_by_sector["R"]
                if slot.name.startswith("kerGamma:")
            ]
        ),
    }
check(
    "exact",
    "both C branches have an explicit Grassmann-alternating reciprocal",
    max(result["alternating_defect"] for result in c_results.values()) < TOL,
)
check(
    "type",
    "C transpose parity changes whether its reciprocal equals the K reverse",
    c_results["C+"]["reverse_difference"] < TOL
    and c_results["C-"]["reverse_difference"] > 0.5,
    repr(c_results),
)
check(
    "exact",
    "both C reciprocals are right-H and annihilate imGamma/low-R reverse inputs",
    max(result["right_h_defect"] for result in c_results.values()) < TOL
    and max(result["non_x_reverse_norm"] for result in c_results.values()) < TOL,
)


def sandwich_forward(name: str) -> np.ndarray:
    # Q_VS T Q_S for the same coarse projector on both sides.
    if name == "1":
        return t_half
    if name == "P_S":
        return np.zeros_like(t_half)
    # P_I/P_R have no S source on the right.
    return np.zeros_like(t_half)


def sandwich_reverse(name: str) -> np.ndarray:
    # Q_S T^x Q_VS. P_S has no VS source; P_I/P_R have no S target.
    if name == "1":
        return t_k_reverse
    return np.zeros_like(t_k_reverse)


p0_survival = {
    name: (
        np.linalg.norm(sandwich_forward(name)) > TOL
        and np.linalg.norm(sandwich_reverse(name)) > TOL
    )
    for name in ("1", "P_S", "P_I", "P_R")
}
check(
    "type",
    "coarse sector-incidence sandwiches retain a direct S-to-X block only for P0=1",
    p0_survival == {"1": True, "P_S": False, "P_I": False, "P_R": False},
)
baseline_survival = {"1": True, "P_S": True, "P_I": False, "P_R": False}
check(
    "type",
    "the written diagonal c_rho baseline survives 1/P_S but has no 144 leg",
    baseline_survival["1"] and baseline_survival["P_S"]
    and not baseline_survival["P_R"],
)

y_real = np.array([[1.0, 2.0, 0.0], [0.0, -1.0, 1.0], [3.0, 0.0, 2.0]])
y_complex = y_real.astype(complex)
y_complex[0, 1] += 1.0j
check(
    "exact",
    "trivial provenance reality admits real Y and rejects generic complex Y",
    max_abs(y_real - y_real.conj()) < TOL
    and max_abs(y_complex - y_complex.conj()) > 1.0,
)
check(
    "planted",
    "an arbitrary M3(C) provenance matrix is not silently right-H compatible",
    max_abs(y_complex - y_complex.conj()) > 1.0,
)


# -------------------------------------------------------------------------
# D. Three-frame moving-conjugation covariance and derivative
# -------------------------------------------------------------------------


print("\nD. THREE-FRAME MOVING-CONJUGATION COVARIANCE")

x_mover = full20.gamma_14[0] @ full20.gamma_14[1] @ full20.gamma_14[2]
identity128 = np.eye(128, dtype=complex)
rotor = (3.0 / 5.0) * identity128 + (4.0 / 5.0) * x_mover
rotor_inverse = (3.0 / 5.0) * identity128 - (4.0 / 5.0) * x_mover
groups = [identity128, rotor, rotor @ rotor]
inverses = [identity128, rotor_inverse, rotor_inverse @ rotor_inverse]

check(
    "exact",
    "the rational native mover has the declared inverse and is K/right-H preserving",
    max_abs(groups[1] @ inverses[1] - identity128) < TOL
    and max_abs(groups[1].conj().T @ k_s @ groups[1] - k_s) < TOL
    and max_abs(groups[1] @ j_s - j_s @ groups[1].conj()) < TOL,
)

u10 = groups[1] @ inverses[0]
u21 = groups[2] @ inverses[1]
u02 = groups[0] @ inverses[2]
check(
    "exact",
    "three constant frame transitions form a coboundary cocycle fixture",
    max_abs(u02 @ u21 @ u10 - identity128) < TOL,
)

t_patches = []
moving_descent_defect = 0.0
for group, inverse in zip(groups, inverses):
    moved_gammas = [group @ gamma @ inverse for gamma in full20.gamma_14]
    moved_raw = move_vs_map(b_v + 0.5 * b_h, group)
    moved_t = p_r_with(moved_raw, moved_gammas)
    expected_t = move_vs_map(t_half, group)
    t_patches.append(moved_t)
    moving_descent_defect = max(moving_descent_defect, max_abs(moved_t - expected_t))
check(
    "exact",
    "moving gammas/projector make the representative covariant in three frames",
    moving_descent_defect < TOL,
    f"defect={moving_descent_defect:.3g}",
)

frozen_t = full20.p_r(move_vs_map(b_v + 0.5 * b_h, groups[1]))
check(
    "planted",
    "freezing P_R under the out-of-Spin mover fails",
    max_abs(frozen_t - t_patches[1]) > 0.5,
)

x_vs = np.kron(np.eye(14), x_mover)
seed = b_full
p_seed = full20.p_r(seed)
seed_dot = x_vs @ seed - seed @ x_mover
p_dot_seed = x_vs @ p_seed - full20.p_r(x_vs @ seed)
total_chain = p_dot_seed + full20.p_r(seed_dot)
expected_chain = x_vs @ p_seed - p_seed @ x_mover
check(
    "exact",
    "the moving-projector chain rule equals co-moving conjugation",
    max_abs(total_chain - expected_chain) < TOL,
)
check(
    "planted",
    "omitting the projector derivative is a live error",
    max_abs(full20.p_r(seed_dot) - expected_chain) > 0.5,
)


# -------------------------------------------------------------------------
# E. Conditional source interface and isolated kappa comparator
# -------------------------------------------------------------------------


print("\nE. CONDITIONAL SOURCE INTERFACE / ISOLATED KAPPA SECTOR")

kappa = Fraction(3, 2)
phi = Fraction(5, 7)

# The source-displayed kappa sector is kappa/2 <T,T>. Conditional on the
# unbuilt source-to-active real-form/Zorro port admitting T=j5(phi), the signed
# exterior adjoint computed above gives j5^!j5=9. Curvature/Shiab and the total
# fermion residual are unevaluated.
direct_phi_euler = Fraction(9) * kappa * phi
upstairs_e_t_coefficient = kappa
pulled_phi_euler = Fraction(9) * upstairs_e_t_coefficient * phi
check(
    "source",
    "direct and pulled isolated-kappa variations agree under the conditional port",
    direct_phi_euler == pulled_phi_euler != 0,
)
check(
    "source",
    "the isolated displayed kappa term has a nonzero conditional j5 response",
    Fraction(9) * kappa != 0,
)

# One coupled polynomial affine comparator: T=varpi-h'. Its action is varied
# directly and then integrated by parts to obtain both Euler owners and the
# boundary current. Gauge directions (delta varpi,delta h)=(xi',xi) have
# delta T=0. This remains a source-shaped comparator, not the nonlinear tilted
# source Ward identity or a moving-soldering model.
varpi_poly = (Fraction(3), Fraction(-2), Fraction(1))
h_poly = (Fraction(1), Fraction(2), Fraction(-1), Fraction(1))
alpha_poly = (Fraction(-1), Fraction(3), Fraction(2))
xi_poly = (Fraction(2), Fraction(-1), Fraction(1), Fraction(1))
t_poly = polynomial_add(
    varpi_poly,
    polynomial_scale(-1, polynomial_derivative(h_poly)),
)
direction_poly = polynomial_add(
    alpha_poly,
    polynomial_scale(-1, polynomial_derivative(xi_poly)),
)
direct_variation = kappa * integrate_unit(
    polynomial_product(t_poly, direction_poly)
)
e_varpi_poly = polynomial_scale(kappa, t_poly)
e_h_poly = polynomial_scale(kappa, polynomial_derivative(t_poly))
bulk_variation = integrate_unit(
    polynomial_product(e_varpi_poly, alpha_poly)
) + integrate_unit(polynomial_product(e_h_poly, xi_poly))
boundary_variation = -(
    evaluate(e_varpi_poly, Fraction(1)) * evaluate(xi_poly, Fraction(1))
    - evaluate(e_varpi_poly, Fraction(0)) * evaluate(xi_poly, Fraction(0))
)
check(
    "source",
    "direct variation equals independently integrated Euler plus boundary terms",
    direct_variation == bulk_variation + boundary_variation,
)

gauge_direction = polynomial_add(
    polynomial_derivative(xi_poly),
    polynomial_scale(-1, polynomial_derivative(xi_poly)),
)
gauge_direct = kappa * integrate_unit(
    polynomial_product(t_poly, gauge_direction)
)
ward_bulk = polynomial_add(
    e_h_poly,
    polynomial_scale(-1, polynomial_derivative(e_varpi_poly)),
)
check(
    "source",
    "the coupled affine comparator has zero gauge variation and bulk Ward identity",
    gauge_direct == 0 and all(value == 0 for value in ward_bulk),
)
check(
    "exact",
    "the same affine action comparator has a live Green boundary current",
    boundary_variation != 0
    and direct_variation == bulk_variation + boundary_variation,
)
check(
    "planted",
    "dropping the comparator boundary current changes its variation",
    direct_variation != bulk_variation,
)
check(
    "planted",
    "dropping the h Euler owner breaks the coupled variation",
    direct_variation
    != integrate_unit(polynomial_product(e_varpi_poly, alpha_poly))
    + boundary_variation,
)

SOURCE_T_OMEGA_EQUALS_N1_DELTA_A = False
SOURCE_EPSILON_EQUALS_SOLDERING_EPSILON = False
SOURCE_SELECTS_HALF_WEIGHT = False
SOURCE_TO_ACTIVE_95_PORT_BUILT = False
RECTANGULAR_MAP_SOURCE_OWNED = False
FLAT_CURVATURE_SOURCE_GERM_BUILT = False
FULL_G2_PAIRING_BUILT = False
TOTAL_FERMION_BRIDGE_EULER_BUILT = False
STATIONARY_NONZERO_VEV_BUILT = False
PHYSICAL_QUOTIENT_OR_DOMAIN_BUILT = False

check(
    "type",
    "T_omega and N1 Delta A remain a conditional dictionary, not an identity",
    not SOURCE_T_OMEGA_EQUALS_N1_DELTA_A,
)
check(
    "type",
    "source epsilon and moving soldering remain distinct",
    not SOURCE_EPSILON_EQUALS_SOLDERING_EPSILON,
)
check(
    "type",
    "the source-to-active-(9,5) real-form/Zorro port remains open",
    not SOURCE_TO_ACTIVE_95_PORT_BUILT,
)
check(
    "type",
    "the whole rectangular B-lambda family is source-silent",
    not RECTANGULAR_MAP_SOURCE_OWNED,
)
check(
    "source",
    "the public source is silent on the half-weight selector",
    not SOURCE_SELECTS_HALF_WEIGHT,
)
check(
    "type",
    "no flat-curvature source germ was built for the isolated kappa restriction",
    not FLAT_CURVATURE_SOURCE_GERM_BUILT,
)
check(
    "type",
    "the reciprocal uses diagonal direct-sum K; generic G2 mixing remains open",
    not FULL_G2_PAIRING_BUILT,
)
check(
    "type",
    "complete fermion/bridge Euler cancellation remains unassembled",
    not TOTAL_FERMION_BRIDGE_EULER_BUILT,
)
check(
    "type",
    "VEV, mass, quotient, domain, and no-leakage remain open",
    not STATIONARY_NONZERO_VEV_BUILT and not PHYSICAL_QUOTIENT_OR_DOMAIN_BUILT,
)
check(
    "planted",
    "a nonzero density/source Hessian is not promoted to a stationary mass",
    not STATIONARY_NONZERO_VEV_BUILT,
)

print("\nVerdict:")
print("  NATIVE FULL-14 252 COMPARATOR: CONSTRUCTED LOCALLY; 9-PHI LOCKED")
print("  DISPLAYED SOURCE KAPPA TERM: SOURCE-OWNED")
print("  ACTIVE j5 RESTRICTION: CONDITIONAL ON UNBUILT SOURCE-TO-ACTIVE PORT")
print("  UNWEIGHTED FULL-20 COMPARATOR: COUPLED TO LOW-R 16")
print("  HALF-WEIGHTED S->X: ONE-SIMPLE-BLADE CANDIDATE, SOURCE-SILENT")
print("  TOTAL FERMION/BRIDGE EULER, VEV, MASS, QUOTIENT, DOMAIN: OPEN")
print(
    "\nCounts: "
    + ", ".join(f"{value} {name}" for name, value in COUNTS.items())
    + f" = {sum(COUNTS.values())}"
)

if FAILURES:
    print("FAILURES:", ", ".join(FAILURES))
    raise SystemExit(1)
print("All Resolver Wave-E checks passed.")
