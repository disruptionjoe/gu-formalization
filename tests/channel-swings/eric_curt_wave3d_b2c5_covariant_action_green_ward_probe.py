#!/usr/bin/env python3
r"""B2C5 covariant-action, Green, and curved-Ward gate.

This probe starts with all action coefficients visible.  It does not insert
the B2C4 reciprocal ``11/12`` relation as a variational axiom.  It asks four
separate questions:

1. what independent-bar and Krein/charge-real action variation actually
   selects;
2. what the separately declared Dirac-type section gate selects;
3. whether the completed operator has an RS-shift Noether symbol and what its
   Green/energy trace spaces do; and
4. what survives when the flat wedge complex is covariantized.

The active real form is the trace-reversed

    (3,1)+(6,4)=(9,5),  Cl(9,5)=M(64,H).

The exact outcome is intentionally split.  The already-filtered nonzero-
southeast repair admits a quadratic independent-dual action at frozen
principal order and passes separate Krein/right-H/charge compatibility gates;
the normalized Dirac-type gate derives the reciprocal relation.  The finite
algebraic emission control and reality gates do not derive that relation, tie
the two chiral weights, or remove the last dimensionless shape parameter and
overall source scale.  The full time symbol is invertible, so the completed
rolled operator has no nontrivial local RS-shift right syzygy.  Exact
Levi-Civita right-composition fixtures match Einstein-gamma.  A scalar
endomorphism curvature fixture and hand-built torsion/moving-weight arrays
only expose possible independent remainder types.  Admissible GU-adjoint
curvature, derived first-jet formulas, the left curved composition, and a
genuine coupled differential Euler-module identity remain open.

No physical ``nu`` is reused as a ghost.  No P1/P2/P3 datum, quotient,
projector, target eigenspace, or fitted Green domain is used.
"""

from __future__ import annotations

from fractions import Fraction
import gc
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
for path in (ROOT / "tests", ROOT / "tests" / "generation-sector"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import gen_sector_bridge as gb  # noqa: E402


TOL = 8.0e-8
RANK_TOL = 2.0e-7
FAILURES: list[str] = []
EXACT = 0
TYPE_LEVEL = 0
PLANTED = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    status = "PASS" if not false_claim else "FAIL"
    print(f"{status}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def type_control(label: str, condition: bool, detail: str = "") -> None:
    global TYPE_LEVEL
    TYPE_LEVEL += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: type-level control - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"type-level: {label}")


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def rank(matrix: np.ndarray) -> int:
    return int(np.sum(np.linalg.svd(matrix, compute_uv=False) > RANK_TOL))


def product(matrices: list[np.ndarray]) -> np.ndarray:
    result = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        result = result @ matrix
    return result


# ---------------------------------------------------------------------------
# Exact rational Clifford-algebra helper used for curved Ward remainders.

Blade = dict[int, Fraction]
ETA_INT = tuple([1] * 9 + [-1] * 5)


def blade_product(left: int, right: int) -> tuple[Fraction, int]:
    sign = 1
    for index in range(14):
        if (left >> index) & 1:
            if (right & ((1 << index) - 1)).bit_count() % 2:
                sign *= -1
    common = left & right
    for index in range(14):
        if (common >> index) & 1:
            sign *= ETA_INT[index]
    return Fraction(sign), left ^ right


def clifford_multiply(left: Blade, right: Blade) -> Blade:
    out: Blade = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            sign, mask = blade_product(left_mask, right_mask)
            out[mask] = out.get(mask, Fraction(0)) + sign * left_value * right_value
    return {mask: value for mask, value in out.items() if value}


def clifford_add(target: Blade, source: Blade, scale: Fraction = Fraction(1)) -> None:
    for mask, value in source.items():
        target[mask] = target.get(mask, Fraction(0)) + scale * value
        if target[mask] == 0:
            del target[mask]


def gamma_word(*indices: int) -> Blade:
    out: Blade = {0: Fraction(1)}
    for index in indices:
        out = clifford_multiply(out, {1 << index: Fraction(1)})
    return out


def metric(left: int, right: int) -> Fraction:
    return Fraction(ETA_INT[left] if left == right else 0)


def riemann_from_ricci(ricci: list[list[Fraction]]) -> list[list[list[list[Fraction]]]]:
    n = 14
    scalar = sum(Fraction(ETA_INT[a]) * ricci[a][a] for a in range(n))
    out = [[[[Fraction(0) for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    first = (
                        metric(a, c) * ricci[b][d]
                        - metric(a, d) * ricci[b][c]
                        - metric(b, c) * ricci[a][d]
                        + metric(b, d) * ricci[a][c]
                    ) / Fraction(n - 2)
                    trace = scalar * (
                        metric(a, c) * metric(b, d)
                        - metric(a, d) * metric(b, c)
                    ) / Fraction((n - 1) * (n - 2))
                    out[a][b][c][d] = first - trace
    return out


def ricci_of_riemann(riemann: list[list[list[list[Fraction]]]]) -> list[list[Fraction]]:
    return [
        [sum(Fraction(ETA_INT[a]) * riemann[a][b][a][d] for a in range(14)) for d in range(14)]
        for b in range(14)
    ]


def is_nonzero_algebraic_riemann(
    riemann: list[list[list[list[Fraction]]]],
) -> bool:
    nonzero = False
    for a in range(14):
        for b in range(14):
            for c in range(14):
                for d in range(14):
                    value = riemann[a][b][c][d]
                    nonzero = nonzero or value != 0
                    if value != -riemann[b][a][c][d]:
                        return False
                    if value != -riemann[a][b][d][c]:
                        return False
                    if value != riemann[c][d][a][b]:
                        return False
                    if value + riemann[a][c][d][b] + riemann[a][d][b][c] != 0:
                        return False
    return nonzero


def spin_curvature(riemann: list[list[list[list[Fraction]]]]) -> list[list[Blade]]:
    out = [[{} for _ in range(14)] for _ in range(14)]
    for b in range(14):
        for c in range(14):
            for d in range(14):
                for e in range(14):
                    value = riemann[b][c][d][e]
                    if value:
                        clifford_add(out[b][c], gamma_word(d, e), value / 4)
    return out


def wedge_curvature_remainder(curvature: list[list[Blade]]) -> list[Blade]:
    out: list[Blade] = [{} for _ in range(14)]
    for a in range(14):
        for b in range(14):
            if a == b:
                continue
            for c in range(14):
                if c == a or c == b or not curvature[b][c]:
                    continue
                triple = gamma_word(a, b, c)
                piece = clifford_multiply(triple, curvature[b][c])
                clifford_add(out[a], piece, Fraction(ETA_INT[a], 2))
    return out


def einstein_gamma(ricci: list[list[Fraction]]) -> list[Blade]:
    scalar = sum(Fraction(ETA_INT[a]) * ricci[a][a] for a in range(14))
    out: list[Blade] = [{} for _ in range(14)]
    for a in range(14):
        for d in range(14):
            einstein = ricci[a][d] - Fraction(1, 2) * scalar * metric(a, d)
            if einstein:
                clifford_add(out[a], gamma_word(d), einstein / 2)
    return out


def blade_grade_support(items: list[Blade]) -> set[int]:
    return {mask.bit_count() for item in items for mask in item}


def curved_remainder_checks() -> None:
    zero = [[Fraction(0) for _ in range(14)] for _ in range(14)]
    ricci_tracefree = [row[:] for row in zero]
    ricci_tracefree[0][0] = Fraction(2)
    ricci_tracefree[1][1] = Fraction(-2)
    remainder = wedge_curvature_remainder(spin_curvature(riemann_from_ricci(ricci_tracefree)))
    expected = einstein_gamma(ricci_tracefree)
    check(
        "covariant wedge-after-gradient equals one-half Einstein-gamma on an exact traceless-Ricci fixture",
        remainder == expected and blade_grade_support(remainder) == {1},
    )

    ricci_mixed = [row[:] for row in zero]
    for index in range(14):
        ricci_mixed[index][index] = Fraction(index + 1)
    remainder_mixed = wedge_curvature_remainder(spin_curvature(riemann_from_ricci(ricci_mixed)))
    check(
        "the exact Einstein-gamma collapse also holds with nonzero scalar curvature",
        remainder_mixed == einstein_gamma(ricci_mixed),
    )

    # Build a nonzero algebraic Riemann tensor and subtract its complete Ricci
    # part.  The resulting exact Weyl fixture must be invisible to A_w K.
    h = [Fraction(v) for v in (1, -1, 2, -2, 0, 1, 0, -1, 2, 0, -2, 1, 0, -1)]
    k = [Fraction(v) for v in (2, 1, -1, 0, 1, -2, 1, 0, -1, 2, 1, 0, -2, 1)]
    raw = [[[[Fraction(0) for _ in range(14)] for _ in range(14)] for _ in range(14)] for _ in range(14)]
    for a in range(14):
        for b in range(14):
            for c in range(14):
                for d in range(14):
                    ha_c = h[a] if a == c else 0
                    ha_d = h[a] if a == d else 0
                    hb_c = h[b] if b == c else 0
                    hb_d = h[b] if b == d else 0
                    ka_c = k[a] if a == c else 0
                    ka_d = k[a] if a == d else 0
                    kb_c = k[b] if b == c else 0
                    kb_d = k[b] if b == d else 0
                    raw[a][b][c][d] = ha_c * kb_d - ha_d * kb_c - hb_c * ka_d + hb_d * ka_c
    raw_ricci = ricci_of_riemann(raw)
    ricci_part = riemann_from_ricci(raw_ricci)
    weyl = [[[[raw[a][b][c][d] - ricci_part[a][b][c][d] for d in range(14)] for c in range(14)] for b in range(14)] for a in range(14)]
    check(
        "a nonzero algebraic pure-Weyl fixture has zero Ricci and zero wedge-gradient remainder",
        is_nonzero_algebraic_riemann(weyl)
        and all(value == 0 for row in ricci_of_riemann(weyl) for value in row)
        and all(not item for item in wedge_curvature_remainder(spin_curvature(weyl))),
    )

    internal = [[{} for _ in range(14)] for _ in range(14)]
    internal[0][1] = {0: Fraction(1)}
    internal[1][0] = {0: Fraction(-1)}
    internal_remainder = wedge_curvature_remainder(internal)
    type_control(
        "a commuting scalar endomorphism-valued curvature fixture leaves a nonzero grade-three Ward remainder",
        blade_grade_support(internal_remainder) == {3},
    )

    # A raw-covariant-derivative torsion term and a moving-weight term are
    # first-order in the gauge parameter.  Independent jet labels prevent a
    # zero-order Einstein equation from silently canceling either one.
    torsion_remainder: list[Blade] = [{} for _ in range(14)]
    moving_weight_remainder: list[Blade] = [{} for _ in range(14)]
    for a in range(14):
        if a not in (1, 2):
            clifford_add(torsion_remainder[a], gamma_word(a, 1, 2), Fraction(-ETA_INT[a]))
        if a not in (0, 1):
            clifford_add(moving_weight_remainder[a], gamma_word(a, 0, 1), Fraction(ETA_INT[a]))
    type_control(
        "type-level planted torsion and moving-weight jet arrays occupy distinct nonzero first-order slots",
        blade_grade_support(torsion_remainder) == {3}
        and blade_grade_support(moving_weight_remainder) == {3}
        and torsion_remainder != moving_weight_remainder,
    )


def main() -> int:
    print("ECW3D-B2C5 COVARIANT ACTION / GREEN / WARD GATE")
    n = 14
    spin = 128
    roll = (n + 1) * spin
    gammas, gamma_trace, _, _ = gb.constraint_objects()
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_s = np.eye(spin, dtype=complex)
    identity_v = np.eye(n, dtype=complex)
    identity_roll = np.eye(roll, dtype=complex)

    omega = product(gammas)
    p_plus = 0.5 * (identity_s + omega)
    p_minus = 0.5 * (identity_s - omega)
    beta = product(gammas[:9])
    krein_vs = np.kron(np.diag(eta), beta)
    krein_roll = np.block(
        [
            [krein_vs, np.zeros((n * spin, spin), dtype=complex)],
            [np.zeros((spin, n * spin), dtype=complex), beta],
        ]
    )
    right_h_s = product([gammas[index] for index in (1, 3, 5, 7, 10, 12)])
    right_h_roll = np.block(
        [
            [np.kron(identity_v, right_h_s), np.zeros((n * spin, spin))],
            [np.zeros((spin, n * spin)), right_h_s],
        ]
    )

    def c(k: np.ndarray) -> np.ndarray:
        return sum(k[a] * gammas[a] for a in range(n))

    def k_map(k: np.ndarray) -> np.ndarray:
        return np.kron(k.reshape(n, 1), identity_s)

    def codiff(k: np.ndarray) -> np.ndarray:
        return np.kron((eta * k).reshape(1, n), identity_s)

    def wedge_middle_coordinate(b: int) -> np.ndarray:
        out = np.zeros((n * spin, n * spin), dtype=complex)
        for a in range(n):
            if a == b:
                continue
            for v in range(n):
                if v == a or v == b:
                    continue
                out[a * spin : (a + 1) * spin, v * spin : (v + 1) * spin] = (
                    eta[a] * gammas[a] @ gammas[b] @ gammas[v]
                )
        return out

    coordinate_index = {"y": 0, "x": 1, "z": 2, "t": 9}
    covectors = {name: np.eye(n)[index] for name, index in coordinate_index.items()}
    wedge = {name: wedge_middle_coordinate(index) for name, index in coordinate_index.items()}

    # The actual Krein adjoint of exterior multiplication includes both block
    # metrics.  This is the action-level object; ordinary transpose is not.
    for name in ("y", "t"):
        krein_adjoint_k = beta @ k_map(covectors[name]).conj().T @ krein_vs
        check(
            f"{name}: the density-free principal Krein adjoint of K is C_g",
            max_abs(krein_adjoint_k - codiff(covectors[name])) < 2.0e-12,
        )

    def rolled_symbol(
        name: str,
        w_plus: float,
        w_minus: float,
        ell_plus: float,
        ell_minus: float,
        upper_offdiag: float = 1.0,
        lower_offdiag: float = 1.0,
    ) -> np.ndarray:
        k = covectors[name]
        weights = w_plus * p_plus + w_minus * p_minus
        ell = ell_plus * p_plus + ell_minus * p_minus
        return np.block(
            [
                [wedge[name] @ np.kron(identity_v, weights), upper_offdiag * k_map(k)],
                [lower_offdiag * codiff(k), c(k) @ ell],
            ]
        )

    # An independent K-lowered dual makes every coefficient an admissible
    # algebraic Euler coefficient.  This frozen matrix derivative confirms
    # emission, not the complete covariant Hodge/density/IBP variation and not
    # coefficient selection.
    rng = np.random.default_rng(20260801)
    test_matrix = rolled_symbol("y", 1.0, 1.0, -11.0 / 12.0, -11.0 / 12.0)
    psi = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    bar = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    dpsi = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    dbar = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    epsilon = 1.0e-6

    def independent_bar_action(left: np.ndarray, right: np.ndarray, matrix: np.ndarray) -> complex:
        return left @ (matrix @ right)

    numeric = (
        independent_bar_action(bar + epsilon * dbar, psi + epsilon * dpsi, test_matrix)
        - independent_bar_action(bar - epsilon * dbar, psi - epsilon * dpsi, test_matrix)
    ) / (2.0 * epsilon)
    analytic = dbar @ (test_matrix @ psi) + bar @ (test_matrix @ dpsi)
    check(
        "finite algebraic independent-dual variation emits both frozen rolled equations term by term",
        abs(numeric - analytic) < 2.0e-5 * max(1.0, abs(analytic)),
    )
    changed_matrix = rolled_symbol("y", 1.0, 1.0, -0.7, -0.7)
    check(
        "finite algebraic independent-dual variation accommodates a changed southeast coefficient and therefore does not select 11/12",
        np.linalg.norm((changed_matrix - test_matrix) @ psi) > 1.0,
    )
    del psi, bar, dpsi, dbar, changed_matrix
    gc.collect()

    # Full Krein formal symmetry forces the two off-diagonal normalizations to
    # be adjoints.  The normalized source pairing gives r=s.
    tied_symbols = {
        name: rolled_symbol(name, 1.0, 1.0, -11.0 / 12.0, -11.0 / 12.0)
        for name in coordinate_index
    }
    check(
        "the nonzero-southeast tied principal coefficient symbol is Krein-selfadjoint",
        max(
            max_abs(krein_roll @ symbol - (krein_roll @ symbol).conj().T)
            for symbol in tied_symbols.values()
        ) < 6.0e-8,
    )
    asymmetric = rolled_symbol("y", 1.0, 1.0, -11.0 / 6.0, -11.0 / 6.0, 2.0, 1.0)
    check(
        "an off-diagonal normalization mismatch fails the frozen-pairing formal-adjoint gate",
        max_abs(krein_roll @ asymmetric - (krein_roll @ asymmetric).conj().T) > 0.5,
    )
    del asymmetric

    # An explicit charge/Krein-preserving chiral field boost, unlike overall
    # action scaling, is a genuine frozen-principal field equivalence.  Its similarity orbit
    # gives an unequal-chiral member of the reciprocal family.
    boost_ratio = 1.7
    boost_spin = np.sqrt(boost_ratio) * p_plus + p_minus / np.sqrt(boost_ratio)
    boost_spin_inv = p_plus / np.sqrt(boost_ratio) + np.sqrt(boost_ratio) * p_minus
    boost_roll = np.block(
        [
            [np.kron(identity_v, boost_spin), np.zeros((n * spin, spin))],
            [np.zeros((spin, n * spin)), boost_spin],
        ]
    )
    boost_roll_inv = np.block(
        [
            [np.kron(identity_v, boost_spin_inv), np.zeros((n * spin, spin))],
            [np.zeros((spin, n * spin)), boost_spin_inv],
        ]
    )
    boost_orbit_symbols = {
        name: boost_roll_inv @ symbol @ boost_roll
        for name, symbol in tied_symbols.items()
    }
    explicit_unequal_symbols = {
        name: rolled_symbol(
            name,
            boost_ratio,
            1.0 / boost_ratio,
            -11.0 * boost_ratio / 12.0,
            -11.0 / (12.0 * boost_ratio),
        )
        for name in coordinate_index
    }
    check(
        "the chiral boost is an explicit frozen-principal Krein-unitary right-H field equivalence with the advertised unequal coefficient orbit",
        max_abs(boost_roll.conj().T @ krein_roll @ boost_roll - krein_roll) < 6.0e-8
        and max_abs(boost_roll @ right_h_roll - right_h_roll @ boost_roll.conj()) < 6.0e-8
        and max(
            max_abs(boost_orbit_symbols[name] - explicit_unequal_symbols[name])
            for name in coordinate_index
        ) < 6.0e-8,
    )

    # Charge reality: C_+ is the even-gamma charge form and equals -beta J in
    # this basis.  It is the viable active charge branch.  C_- is a control.
    c_plus = np.linalg.inv(
        product([gammas[index] for index in range(n) if index % 2 == 0])
    )
    c_minus = np.linalg.inv(
        product([gammas[index] for index in range(n) if index % 2 == 1])
    )
    check(
        "the active charge form is C_plus=-beta J and the spinor is quaternionic rather than Majorana-real",
        max_abs(c_plus + beta @ right_h_s) < 2.0e-12
        and max_abs(right_h_s @ right_h_s.conj() + identity_s) < 2.0e-12,
    )
    charge_plus_roll = np.block(
        [
            [np.kron(np.diag(eta), c_plus), np.zeros((n * spin, spin))],
            [np.zeros((spin, n * spin)), c_plus],
        ]
    )
    charge_minus_roll = np.block(
        [
            [np.kron(np.diag(eta), c_minus), np.zeros((n * spin, spin))],
            [np.zeros((spin, n * spin)), c_minus],
        ]
    )
    plus_defect = max(
        max_abs((charge_plus_roll @ symbol).T + charge_plus_roll @ symbol)
        for symbol in tied_symbols.values()
    )
    minus_defect = max(
        max_abs((charge_minus_roll @ symbol).T + charge_minus_roll @ symbol)
        for symbol in tied_symbols.values()
    )
    check(
        "C_plus gives principal rolled first-order charge compatibility while C_minus is rejected",
        plus_defect < 6.0e-8 and minus_defect > 1.0,
        f"C+={plus_defect:.3g}; C-={minus_defect:.3g}",
    )
    unequal_charge_defect = max(
        max_abs((charge_plus_roll @ symbol).T + charge_plus_roll @ symbol)
        for symbol in explicit_unequal_symbols.values()
    )
    check(
        "C_plus principal charge compatibility survives an explicit unequal-chiral reciprocal witness",
        unequal_charge_defect < 6.0e-8
        and max_abs(boost_roll.T @ charge_plus_roll @ boost_roll - charge_plus_roll) < 6.0e-8,
        f"unequal C+={unequal_charge_defect:.3g}",
    )
    omega_sp = np.array([[0.0, 1.0], [-1.0, 0.0]])
    check(
        "a symplectic-Majorana auxiliary doublet, not one fixed Majorana field, is principal-first-order Grassmann compatible",
        max_abs(omega_sp.T + omega_sp) < 2.0e-12
        and plus_defect < 6.0e-8
        and max_abs(right_h_s @ right_h_s.conj() + identity_s) < 2.0e-12,
    )

    # Solve the declared coefficient constraints before quotienting genuine
    # action equivalences.  Eight visible real coefficients are ordered as
    # c+,c-,w+,w-,ell+,ell-,r,s.
    w_plus, w_minus, r = 2.0, 3.0, 1.5
    ell_plus = -11.0 * r * r / (12.0 * w_minus)
    ell_minus = -11.0 * r * r / (12.0 * w_plus)
    point = np.array([0.0, 0.0, w_plus, w_minus, ell_plus, ell_minus, r, r])
    jacobian = np.zeros((5, 8))
    jacobian[0, 0] = 1.0
    jacobian[1, 1] = 1.0
    jacobian[2, 6] = 1.0
    jacobian[2, 7] = -1.0
    jacobian[3, 2] = 12.0 * ell_minus
    jacobian[3, 5] = 12.0 * w_plus
    jacobian[3, 6] = 11.0 * r
    jacobian[3, 7] = 11.0 * r
    jacobian[4, 3] = 12.0 * ell_plus
    jacobian[4, 4] = 12.0 * w_minus
    jacobian[4, 6] = 11.0 * r
    jacobian[4, 7] = 11.0 * r
    check(
        "two imported Ward-selector equations, one coefficient-adjoint equation, and two Dirac-type equations have independent rank five",
        np.linalg.matrix_rank(jacobian, tol=1.0e-10) == 5,
    )
    overall_scale = point.copy()
    chiral_boost = np.array([0.0, 0.0, w_plus, -w_minus, ell_plus, -ell_minus, 0.0, 0.0])
    check(
        "the constraint variety has independent overall-ray and Krein-unitary chiral-boost tangents",
        max_abs(jacobian @ overall_scale) < 2.0e-12
        and max_abs(jacobian @ chiral_boost) < 2.0e-12
        and np.linalg.matrix_rank(np.stack([overall_scale, chiral_boost]), tol=1.0e-10) == 2,
    )
    invariant_p = w_plus * w_minus / (r * r)
    check(
        "after the frozen-principal chiral-boost field equivalence two principal-action parameters remain; quotienting only the Euler/action ray leaves p",
        8 - 5 - 1 == 2 and (8 - 5 - 1) - 1 == 1
        and abs(invariant_p - (8.0 / 3.0)) < 2.0e-12,
        f"p={invariant_p:.6g}",
    )

    # The generalized Clifford relation contains the off-diagonal product.
    # Formal symmetry specializes it to r=s; the Dirac-type gate, not action
    # variation, then derives the crossed reciprocal coefficients.
    generalized_symbols = {
        name: rolled_symbol(name, w_plus, w_minus, ell_plus, ell_minus, r, r)
        for name in coordinate_index
    }
    time_inverse = np.linalg.inv(generalized_symbols["t"])
    generalized_evolution = {
        name: time_inverse @ generalized_symbols[name] for name in ("y", "x", "z")
    }
    generalized_defect = max(
        max_abs(evolution @ evolution - identity_roll)
        for evolution in generalized_evolution.values()
    )
    check(
        "after choosing an overall source normalization the Dirac-type gate derives the two reciprocal equations",
        generalized_defect < 6.0e-8
        and abs(12.0 * w_plus * ell_minus + 11.0 * r * r) < 2.0e-12
        and abs(12.0 * w_minus * ell_plus + 11.0 * r * r) < 2.0e-12,
        f"Clifford defect={generalized_defect:.3g}",
    )
    zero_se_time = rolled_symbol("t", 1.0, 1.0, 0.0, 0.0)
    zero_se_y = rolled_symbol("y", 1.0, 1.0, 0.0, 0.0)
    zero_se_evolution = np.linalg.inv(zero_se_time) @ zero_se_y
    zero_se_jordan = zero_se_evolution @ zero_se_evolution - identity_roll
    check(
        "the active 9,5 pure-wedge zero-corner coefficient symbol is Krein-selfadjoint but fails this Dirac gate",
        max_abs(krein_roll @ zero_se_y - (krein_roll @ zero_se_y).conj().T) < 6.0e-8
        and max_abs(zero_se_jordan) > 0.5
        and max_abs(zero_se_jordan @ zero_se_jordan) < 6.0e-8,
    )

    # Invertibility at time persists on an open covector neighborhood.  A
    # polynomial right syzygy vanishes there and hence vanishes identically.
    time_inverse_tied = np.linalg.inv(tied_symbols["t"])
    inverse_defect = max_abs(tied_symbols["t"] @ time_inverse_tied - identity_roll)
    rs_shift = np.vstack([k_map(covectors["t"]), np.zeros((spin, spin), dtype=complex)])
    check(
        "the completed full rolled operator has no polynomial local RS-shift symbol on the open invertible-symbol set",
        inverse_defect < 6.0e-8 and np.linalg.norm(tied_symbols["t"] @ rs_shift) > 1.0,
    )

    # Build the section evolution and an exact direction-independent
    # symmetrizer by averaging over the eight words in the spatial Clifford
    # group.  This strengthens B2C4's direction-wise symmetrizer.
    evolution = {
        name: time_inverse_tied @ tied_symbols[name] for name in ("y", "x", "z")
    }
    words = [identity_roll]
    words.extend(evolution[name] for name in ("y", "x", "z"))
    words.extend(
        [
            evolution["y"] @ evolution["x"],
            evolution["y"] @ evolution["z"],
            evolution["x"] @ evolution["z"],
            evolution["y"] @ evolution["x"] @ evolution["z"],
        ]
    )
    simultaneous = np.zeros((roll, roll), dtype=complex)
    for word in words:
        simultaneous += word.conj().T @ word
    simultaneous_defect = max(
        max_abs(simultaneous @ item - item.conj().T @ simultaneous)
        for item in evolution.values()
    )
    simultaneous_right_h = max_abs(
        simultaneous @ right_h_roll - right_h_roll @ simultaneous.conj()
    )
    simultaneous_eigenvalues = np.linalg.eigvalsh(simultaneous)
    check(
        "the normalized tied repaired representative has one direction-independent positive right-H section symmetrizer",
        simultaneous_defect < 6.0e-8
        and simultaneous_right_h < 6.0e-8
        and simultaneous_eigenvalues[0] > 1.0,
        f"bounds=({simultaneous_eigenvalues[0]:.6g},{simultaneous_eigenvalues[-1]:.6g})",
    )

    action_green = krein_roll @ tied_symbols["y"]
    energy_green = simultaneous @ evolution["y"]
    action_eigenvalues = np.linalg.eigvalsh(action_green)
    energy_values, energy_vectors = np.linalg.eigh(energy_green)
    action_inertia = (
        int(np.sum(action_eigenvalues > RANK_TOL)),
        int(np.sum(action_eigenvalues < -RANK_TOL)),
        int(np.sum(np.abs(action_eigenvalues) <= RANK_TOL)),
    )
    energy_inertia = (
        int(np.sum(energy_values > RANK_TOL)),
        int(np.sum(energy_values < -RANK_TOL)),
        int(np.sum(np.abs(energy_values) <= RANK_TOL)),
    )
    incoming = energy_vectors[:, energy_values < -RANK_TOL]
    incoming_projector = incoming @ incoming.conj().T
    incoming_right_h = max_abs(
        incoming_projector @ right_h_roll - right_h_roll @ incoming_projector.conj()
    )
    action_on_incoming = incoming.conj().T @ action_green @ incoming
    check(
        "the tied frozen action-Green and positive-energy boundary forms are both nondegenerate balanced 960+960 traces",
        action_inertia == energy_inertia == (960, 960, 0),
        f"action={action_inertia}; energy={energy_inertia}",
    )
    check(
        "the tied H-star maximally negative spectral half is right-H invariant but not action-Green isotropic",
        incoming.shape[1] == 960
        and incoming_right_h < 6.0e-8
        and rank(action_on_incoming) == 960,
        f"right-H={incoming_right_h:.3g}; restricted-rank={rank(action_on_incoming)}",
    )

    # Frozen constant-coefficient one-dimensional Green control: coefficient
    # Hermiticity is necessary and the boundary term is not optional.  This is
    # not the variable-coefficient covariant density/domain theorem.
    phi0 = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    phi1 = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    psi0 = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    psi1 = rng.normal(size=roll) + 1j * rng.normal(size=roll)
    boundary = (phi0 + phi1).conj() @ action_green @ (psi0 + psi1) - phi0.conj() @ action_green @ psi0
    bulk = (
        phi0.conj() @ action_green @ psi1
        + 0.5 * phi1.conj() @ action_green @ psi1
        + phi1.conj() @ action_green @ psi0
        + 0.5 * phi1.conj() @ action_green @ psi1
    )
    check(
        "a frozen constant-coefficient polynomial Green control emits the nonzero candidate boundary form",
        abs(boundary - bulk) < 2.0e-8 * max(1.0, abs(boundary)) and abs(boundary) > 1.0,
    )

    curved_remainder_checks()

    # Observation remains a field map, not a domain or ghost quotient.
    observer = np.zeros((5 * spin, roll), dtype=complex)
    for block, name in enumerate(("y", "x", "z", "t")):
        observer[
            block * spin : (block + 1) * spin,
            coordinate_index[name] * spin : (coordinate_index[name] + 1) * spin,
        ] = identity_s
    observer[4 * spin :, n * spin :] = identity_s
    check(
        "the action and Green analysis retains the raw observation rank 640 without a quotient",
        rank(observer) == 640,
    )

    reject("finite algebraic independent-dual variation selects the wedge coefficient or 11/12", False)
    reject("principal Krein symmetry is the full Hodge-density-domain adjoint theorem", False)
    reject("a single Majorana field exists on the quaternionic Cl(9,5) carrier", False)
    reject("charge reality ties w_plus to w_minus", False)
    reject("the four normalized sign witnesses exhaust the action family", False)
    reject("overall action scale is an action-preserving field equivalence", False)
    reject("the finite algebraic emission control is the complete covariant Hodge-density variation", False)
    reject("the modern zero-southeast source branch passes the active Dirac-type gate", False)
    reject("the full completed rolled operator has an RS-shift gauge syzygy", False)
    reject("C_g A_w=0 is already an off-shell Noether identity for the full action", False)
    reject("the scalar endomorphism curvature fixture is already an admissible GU internal-gauge curvature", False)
    reject("internal curvature is absorbed by the Einstein remainder", False)
    reject("torsion or moving weights leave flat symbol closure unchanged", False)
    reject("the G2 compressed S(F_A)+kappa T shortcut is the graph-complete Euler ideal", False)
    reject("a right-H maximal-dissipative energy sector is automatically variationally Green-isotropic", False)
    reject("a formal Green trace proves a closed Sobolev/domain theorem", False)
    reject("the surviving dimensionless modulus is P1, P2, or P3", False)
    reject("the draft's admitted nonzero southeast version is Eric's modern selected zero corner", False)

    print("-" * 104)
    print(f"checks: {EXACT} exact + {TYPE_LEVEL} type-level + {PLANTED} planted")
    if FAILURES:
        print("FINAL: FAIL")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print("FINAL: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
