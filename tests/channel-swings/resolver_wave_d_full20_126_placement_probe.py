#!/usr/bin/env python3
r"""Native finite-matrix gate for Resolver Wave D.

The written source insertion is

    c_rho(v) = sum_i c(nu^i) rho(Phi_i),

with ``Phi_i`` a genuine native connection coefficient.  This probe uses the
actual trace-reversed ``(3,1)+(6,4)`` Cl(9,5) carrier and asks whether a
grade-six coefficient can emit a real grade-five effective kernel.  It keeps
three maps separate:

1. the source's contracted End(S) insertion ``c_rho``;
2. a componentwise diagonal lift to vector-spinors; and
3. a distinct one-form-as-output map ``S -> V tensor S``.

For the planted five-form representative, the third map has one desired 144
component per source together with paired imGamma/kerGamma 16 components; it
is neither a pure S-to-144 map nor silently identified with the first. Full
moving-soldering descent, source ownership, P0/Y placement, VEV selection, and
mass remain open.
"""
from __future__ import annotations

import contextlib
import io
from itertools import combinations
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

with contextlib.redirect_stdout(io.StringIO()):
    import full20_dewitt_loop_transport_probe as full20  # noqa: E402


TOL = 3.0e-8
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(128, dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def word(indices: tuple[int, ...]) -> np.ndarray:
    return matrix_product([full20.gamma_14[index] for index in indices])


def krein_adjoint(matrix: np.ndarray) -> np.ndarray:
    return full20.krein @ matrix.conj().T @ full20.krein


identity128 = np.eye(128, dtype=complex)
j_h = (
    full20.normalized_chirality(full20.gamma_14)
    @ full20.commuting_real_structure(full20.gamma_14)
)


def right_h_defect(matrix: np.ndarray) -> float:
    return max_abs(matrix @ j_h - j_h @ matrix.conj())


def wedge_sign(index: int, form: tuple[int, ...]) -> int:
    if index in form:
        return 0
    return -1 if sum(value < index for value in form) % 2 else 1


print("=" * 96)
print("RESOLVER WAVE D — NATIVE 126 CONNECTION PLACEMENT")
print("=" * 96)

check("inherited full-20 fixture is healthy", not full20.FAILURES)
check(
    "native split is actual trace-reversed (3,1)+(6,4)",
    tuple(full20.eta_14[:4]) == (1.0, 1.0, 1.0, -1.0)
    and tuple(full20.eta_14[4:]) == (1.0,) * 6 + (-1.0,) * 4,
)
check(
    "J_H is quaternionic and commutes antilinearly with every gamma",
    max_abs(j_h @ j_h.conj() + identity128) < TOL
    and max(
        max_abs(j_h @ gamma.conj() @ np.linalg.inv(j_h) - gamma)
        for gamma in full20.gamma_14
    ) < TOL,
)


# -------------------------------------------------------------------------
# A. Native adjoint and scalar-phase classification
# -------------------------------------------------------------------------


print("\nA. NATIVE ADJOINT / RIGHT-H CLASSIFICATION")
vertical = tuple(range(4, 14))
grade4 = [word(indices) for indices in combinations(vertical, 4)]
grade5 = [word(indices) for indices in combinations(vertical, 5)]
grade6 = [word(indices) for indices in combinations(vertical, 6)]
grade7 = [word(indices) for indices in combinations(vertical, 7)]

check(
    "all 210 internal grade-six blades are K-anti and right-H linear",
    len(grade6) == 210
    and max(max_abs(krein_adjoint(value) + value) for value in grade6) < TOL
    and max(right_h_defect(value) for value in grade6) < TOL,
)
check(
    "all real internal grade-five blades are K-self and right-H linear",
    len(grade5) == 252
    and max(max_abs(krein_adjoint(value) - value) for value in grade5) < TOL
    and max(right_h_defect(value) for value in grade5) < TOL,
)
check(
    "all real internal grade-seven blades are K-anti and right-H linear",
    len(grade7) == 120
    and max(max_abs(krein_adjoint(value) + value) for value in grade7) < TOL
    and max(right_h_defect(value) for value in grade7) < TOL,
)
check(
    "raw grade four is K-self and cannot be the native connection coefficient",
    len(grade4) == 210
    and max(max_abs(krein_adjoint(value) - value) for value in grade4) < TOL,
)

phase5 = 1j * grade5[0]
phase4 = 1j * grade4[0]
check(
    "i times raw grade five repairs K parity but breaks right-H",
    max_abs(krein_adjoint(phase5) + phase5) < TOL
    and right_h_defect(phase5) > 1.0,
    f"H defect={right_h_defect(phase5):.6g}",
)
check(
    "i times raw grade four has the same fatal phase fork",
    max_abs(krein_adjoint(phase4) + phase4) < TOL
    and right_h_defect(phase4) > 1.0,
    f"H defect={right_h_defect(phase4):.6g}",
)


# -------------------------------------------------------------------------
# B. K and C physical spinor factors, with total-kernel controls
# -------------------------------------------------------------------------


print("\nB. K/C BILINEAR CLASSES")
c_plus = matrix_product([full20.gamma_14[index] for index in range(0, 14, 2)])
c_minus = matrix_product([full20.gamma_14[index] for index in range(1, 14, 2)])
check(
    "C+ and C- have the two invariant transpose conventions",
    max(max_abs(gamma.T @ c_plus - c_plus @ gamma)
        for gamma in full20.gamma_14) < TOL
    and max(max_abs(gamma.T @ c_minus + c_minus @ gamma)
            for gamma in full20.gamma_14) < TOL
    and max_abs(c_plus.T + c_plus) < TOL
    and max_abs(c_minus.T - c_minus) < TOL,
)
check(
    "both C branches make every real grade-five spinor kernel alternating",
    max(
        max_abs((charge @ value).T + charge @ value)
        for charge in (c_plus, c_minus)
        for value in grade5
    ) < TOL,
)
check(
    "both C branches make every real grade-seven spinor kernel symmetric",
    max(
        max_abs((charge @ value).T - charge @ value)
        for charge in (c_plus, c_minus)
        for value in grade7
    ) < TOL,
)
check(
    "K times grade five is Hermitian while K times grade seven is anti-Hermitian",
    max(max_abs((full20.krein @ value).conj().T - full20.krein @ value)
        for value in grade5) < TOL
    and max(max_abs((full20.krein @ value).conj().T + full20.krein @ value)
            for value in grade7) < TOL,
)

# The bare spinor class is useful but never the total P0/rho/Y class.
symmetric_y = np.diag([2.0, -1.0, 3.0])
skew_y = np.array(
    [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
)
b5 = c_plus @ grade5[0]
b7 = c_plus @ grade7[0]
check(
    "symmetric provenance preserves grade-five C survival and kills grade seven",
    max_abs(np.kron(b5, symmetric_y).T + np.kron(b5, symmetric_y)) < TOL
    and max_abs(np.kron(b7, symmetric_y).T - np.kron(b7, symmetric_y)) < TOL,
)
check(
    "rank-two skew three-generation provenance reverses both C verdicts",
    max_abs(np.kron(b5, skew_y).T - np.kron(b5, skew_y)) < TOL
    and max_abs(np.kron(b7, skew_y).T + np.kron(b7, skew_y)) < TOL,
)
antihermitian_y = 1.0j * np.diag([1.0, 2.0, 3.0])
k7_total = np.kron(full20.krein @ grade7[0], antihermitian_y)
check(
    "full-rank anti-Hermitian M3 provenance makes total K-grade-seven Hermitian",
    max_abs(k7_total.conj().T - k7_total) < TOL
    and np.linalg.matrix_rank(antihermitian_y) == 3,
)


# -------------------------------------------------------------------------
# C. The written c_rho contraction and the trace-reversed musical
# -------------------------------------------------------------------------


print("\nC. SOURCE-WRITTEN c_rho CONTRACTION")
beta_local = (0, 1, 2, 3, 4)
beta_full = tuple(4 + index for index in beta_local)
phi5 = word(beta_full)


def pure_five_components(use_full14: bool, metric_override=None):
    indices = tuple(range(14)) if use_full14 else vertical
    metric = full20.eta_14 if metric_override is None else metric_override
    components = []
    for index in indices:
        if index in beta_full:
            components.append(np.zeros((128, 128), dtype=complex))
            continue
        form = tuple(sorted((index,) + beta_full))
        coefficient = metric[index] * wedge_sign(index, beta_full)
        components.append(coefficient * word(form))
    return components


vertical_components = pure_five_components(False)
vertical_c_rho = sum(
    (full20.gamma_14[index] @ component
     for index, component in zip(vertical, vertical_components)),
    np.zeros((128, 128), dtype=complex),
)
check(
    "vertical trace-reversed grade-six connection contracts to exactly 5 phi5",
    max_abs(vertical_c_rho - 5.0 * phi5) < TOL,
)

full_components = pure_five_components(True)
full_c_rho = sum(
    (gamma @ component for gamma, component in zip(full20.gamma_14, full_components)),
    np.zeros((128, 128), dtype=complex),
)
horizontal_c_rho = sum(
    (full20.gamma_14[index] @ full_components[index] for index in range(4)),
    np.zeros((128, 128), dtype=complex),
)
check(
    "full Spin(9,5) contraction locks horizontal 4 plus vertical 5 to 9 phi5",
    max_abs(horizontal_c_rho - 4.0 * phi5) < TOL
    and max_abs(full_c_rho - 9.0 * phi5) < TOL,
)

wrong_metric = np.ones(14)
wrong_components = pure_five_components(False, wrong_metric)
wrong_c_rho = sum(
    (full20.gamma_14[index] @ component
     for index, component in zip(vertical, wrong_components)),
    np.zeros((128, 128), dtype=complex),
)
check(
    "hostile raw-Frobenius musical does not reproduce the coefficient five",
    max_abs(wrong_c_rho - 5.0 * phi5) > 1.0,
    f"wrong/phi coefficient={np.trace(np.linalg.solve(phi5, wrong_c_rho)).real/128:.3g}",
)

# A generic grade-six coefficient can also emit grade seven.  Bare K/C
# projections remove that part, but the total ordered Y kernel can reverse the
# verdict as shown above.
generic_index = 4 + 9
generic_form = tuple(4 + index for index in (0, 1, 2, 3, 4, 5))
generic_grade7 = full20.gamma_14[generic_index] @ word(generic_form)
check(
    "disjoint one-form and grade-six legs give a live grade-seven companion",
    max_abs(generic_grade7) > 0.5
    and max_abs(krein_adjoint(generic_grade7) + generic_grade7) < TOL,
)


# -------------------------------------------------------------------------
# D. Full-20 placement fork: written contraction versus one-form output
# -------------------------------------------------------------------------


print("\nD. FULL-20 PLACEMENT FORK")


def componentwise(operator: np.ndarray, vector_spinors: np.ndarray) -> np.ndarray:
    shaped = vector_spinors.reshape(14, 128, -1)
    return np.stack([operator @ shaped[index] for index in range(14)]).reshape(
        14 * 128, -1
    )


sample_i = full20.slots_by_sector["I"][0].basis
sample_r = full20.slot_by_name["X:X2Tp"].basis
i_to_r_leak = np.linalg.norm(full20.p_r(componentwise(phi5, sample_i)))
r_to_i_leak = np.linalg.norm(full20.p_i(componentwise(phi5, sample_r)))
check(
    "naive componentwise End(S) lift does not preserve the written I/R split",
    i_to_r_leak > 1.0e-4 and r_to_i_leak > 1.0e-4,
    f"I->R={i_to_r_leak:.6g}, R->I={r_to_i_leak:.6g}",
)

# Distinct comparator: retain the connection covector as the output vector
# index.  This is not c_rho, but it tests whether the same native component has
# useful full-20 incidence if a superconnection/soldering rule later derives it.
vertical_one_form_map = np.vstack(
    [np.zeros((4 * 128, 128), dtype=complex)] + vertical_components
)
gamma_trace = full20.gamma_trace(vertical_one_form_map)
one_form_i = full20.p_i(vertical_one_form_map)
one_form_r = full20.p_r(vertical_one_form_map)
check(
    "one-form-as-output comparator has gamma trace exactly 5 phi5",
    max_abs(gamma_trace - 5.0 * phi5) < TOL,
)
check(
    "the comparator has nonzero imGamma and gamma-traceless pieces",
    np.linalg.matrix_rank(one_form_i, tol=TOL) == 128
    and np.linalg.matrix_rank(one_form_r, tol=TOL) == 128
    and max_abs(full20.gamma_trace(one_form_r)) < TOL,
)

expected_support = {
    "S:E+:L16+": {"imGamma:E-:L16-", "kerGamma:E-:L16-", "X:X2Tp"},
    "S:E+:R16-": {"imGamma:E-:R16+", "kerGamma:E-:R16+", "X:X1Tm"},
    "S:E-:L16-": {"imGamma:E+:L16+", "kerGamma:E+:L16+", "X:X2Tm"},
    "S:E-:R16+": {"imGamma:E+:R16-", "kerGamma:E+:R16-", "X:X1Tp"},
}
observed_support = {}
for source in full20.slots_by_sector["S"]:
    amplitudes = {
        target.name: float(np.linalg.norm(
            target.basis.conj().T @ (vertical_one_form_map @ source.basis)
        ))
        for target in full20.slots_by_sector["I"] + full20.slots_by_sector["R"]
    }
    observed_support[source.name] = {
        name for name, amplitude in amplitudes.items() if amplitude > 1.0e-7
    }
check(
    "chosen one-form comparator has one 144 plus paired I/R 16s per source",
    observed_support == expected_support,
    repr(observed_support),
)

WRITTEN_C_RHO_EQUALS_ONE_FORM_OUTPUT = False
MOVING_EPSILON_DESCENT_BUILT = False
SOURCE_SELECTS_NONZERO_COMPONENT = False
check(
    "Layer-0 fence: the 144-bearing comparator is not the written c_rho map",
    not WRITTEN_C_RHO_EQUALS_ONE_FORM_OUTPUT,
)
check("moving epsilon/full-Sp descent remains open", not MOVING_EPSILON_DESCENT_BUILT)
check("source ownership and nonzero selection remain open",
      not SOURCE_SELECTS_NONZERO_COMPONENT)

print("\nVerdict: native grade-six connection coefficients emit a canonical real")
print("grade-five/252 spinor kernel under the written contraction.  The bare")
print("K/C factors are favorable, but total Y/P0 placement can reverse them.")
print("A distinct one-form-output map has the desired 144 components plus")
print("paired imGamma and low-R kerGamma 16 companions; no source rule")
print("yet identifies that comparator with c_rho.  Full-20 physical placement is")
print("therefore partial, not a mass or mediator construction.")

if FAILURES:
    print("\nFAILURES:", ", ".join(FAILURES))
    raise SystemExit(1)
print("\nAll Wave-D native finite-matrix checks passed.")
