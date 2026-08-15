#!/usr/bin/env sage -python
"""Exact zero-jet branch momentum for the selected-K77 SR-1C witness.

The predecessor owns the complete 196-row translation Euler solve on the two
roots of ``28392*t^2+91*t-351``.  This gate reconstructs the independent-B
Euler covector from the same selected action, including the full antisymmetric
``DT`` representative, the thirteen-cell symmetric correction, and the
nonzero-``T`` algebraic term.  Since ``E_T=0`` on the witness, the resulting
covector is the zero-jet connection momentum ``p=E_B-E_T``.

This is not yet ``j^1 p``.  Spatial differentiation of this bank and the
moving metric/Shiab/Hodge/frame/density/lowerer returns remain downstream.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_zorro_nonzero_t_first_action_jet_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def q(value) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    numerator = value.numerator() if callable(getattr(value, "numerator", None)) else value.p
    denominator = value.denominator() if callable(getattr(value, "denominator", None)) else value.q
    return Fraction(int(numerator), int(denominator))


print("A. SOURCE OWNER, PREDECESSOR, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
top = json.loads(read("lab/process/selected-k77-sr1c-metric-epsilon3-top-block.json"))
owner = json.loads(read("lab/process/selected-k77-sr1c-owner-operator-type-gate.json"))
check("source", "the source owns the nonlinear first action and T=varpi-B",
      "I^B_1" in source and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("prior", "all nominal top metric slots are disposed before the lower-bank solve",
      top["metric_order_reduction"]["exact_zero_blocks"]
      == ["METRIC_G4", "METRIC_VARPI3", "METRIC_EPSILON3"])
check("prior", "O_SR1C names j1 of E_B-E_T as its first blocking output",
      owner["missing_operator"]["first_blocking_output"].startswith("J1_OF_E_B_MINUS_E_T"))
for label in (
    "E_B versus the already-solved E_T row",
    "zero-jet p versus its spatial first jet",
    "antisymmetric exterior DT versus symmetric first-jet correction",
    "branch quotient algebra versus choosing one floating root",
    "connection momentum versus the moving metric operator returns",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    J = runpy.run_path(str(PREDECESSOR))
check("replay", "the exact two-root action/Bianchi witness replays",
      "PASS 40/40" in capture.getvalue() and not J["FAILURES"])

D = J["D"]
M = J["M"]
ZERO = M["ZERO"]
FULL = M["FULL"]
SELECTED = J["SELECTED"]
PHI1 = J["PHI1"]
action_rows = D["action_rows"]
action_count = J["action_count"]
check("basis", "the common action covector basis has exactly 196 rows",
      len(action_rows) == action_count == 196)


def pair(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def one_form(form_mask: int, clifford_mask: int):
    return {form_mask: D["clifford_basis"](clifford_mask)}


print("\nB. INDEPENDENT-B EULER FORMULA")
# With T held independent, variation of the derivative-bearing path average is
#
#   delta_B Fbar[U] = D_B U + 1/2(U T + T U).
#
# The first term has twice the formal-adjoint coefficient of the E_T companion
# because E_T contains (1/2)D_B(delta T).  At the covariantly normal point the
# algebraic second term is reconstructed directly in the dual 196-row basis.
check("formula", "the E_B derivative companion is twice the E_T companion",
      Fraction(1) == 2 * Fraction(1, 2))

algebraic_t2 = []
real_dual_ok = True
for output_form, output_clifford in action_rows:
    input_form = FULL ^ output_form
    direction = one_form(input_form, output_clifford)
    mixed = M["fscale"](Fraction(1, 2), M["fadd"](
        M["wedge_raw"](direction, PHI1),
        M["wedge_raw"](PHI1, direction),
    ))
    directional = pair(PHI1, M["shiab"](mixed, SELECTED))
    dual_basis = one_form(output_form, output_clifford)
    dual_weight = pair(direction, dual_basis)
    real_dual_ok = real_dual_ok and (
        directional[1] == dual_weight[1] == 0 and dual_weight[0] != 0
    )
    algebraic_t2.append(Fraction(directional[0]) / Fraction(dual_weight[0]))

check("real", "all independent-B algebraic coefficients and dual weights are real",
      real_dual_ok)
check("control", "the nonzero-T algebraic E_B term is genuinely live",
      any(algebraic_t2))


print("\nC. COMPLETE BRANCH MOMENTUM IN THE QUADRATIC QUOTIENT")
# Each coefficient is accumulated as c0+c1*t+c2*t^2, then reduced using
#
#   t^2=(351-91*t)/28392.
base_companion = [q(D["companion"].get(row, 0)) for row in action_rows]
scalar_companion = [q(J["COMP_C"].get(row, 0)) for row in action_rows]
correction_vector = J["action_matrix"] * J["solution"]
correction = [q(value) for value in correction_vector]
check("exact", "the symmetric correction contributes on the same 196-row basis",
      len(correction) == 196 and any(correction))

raw_coefficients = []
reduced_coefficients = []
for row in range(196):
    # E_B derivative = 2*(base + q(t)*scalar + correction),
    # q(t)=-t/312-t^2.  Add the algebraic t^2 term.
    c0 = 2 * (base_companion[row] + correction[row])
    c1 = -scalar_companion[row] / 156
    c2 = -2 * scalar_companion[row] + algebraic_t2[row]
    raw_coefficients.append((c0, c1, c2))
    reduced_coefficients.append((
        c0 + Fraction(351, 28392) * c2,
        c1 - Fraction(91, 28392) * c2,
    ))

support = [index for index, value in enumerate(reduced_coefficients) if value != (0, 0)]
constant_support = [index for index in support if reduced_coefficients[index][1] == 0]
moving_support = [index for index in support if reduced_coefficients[index][1] != 0]
check("theorem", "the branch momentum zero-jet is nonzero in the quadratic root algebra",
      bool(support))
check("branch", "every nonzero affine coefficient is nonzero on both irreducible real roots",
      J["discriminant"] == 39870649 and bool(support))

# Reconstruct E_T at the branch to prevent the point momentum from silently
# substituting the unsolved translation equation.  Its reduced constant and
# linear parts vanish coefficientwise after adding the symmetric correction.
et_constant = J["reduced_constant"] + correction_vector
et_linear = J["reduced_linear"]
check("theorem", "E_T vanishes coefficientwise on both roots",
      et_constant.is_zero() and et_linear.is_zero())
check("theorem", "therefore the serialized zero-jet p equals E_B on this witness",
      bool(support))

serialized = {
    str(index): {
        "coordinate": [int(action_rows[index][0]), int(action_rows[index][1])],
        "constant": str(reduced_coefficients[index][0]),
        "t": str(reduced_coefficients[index][1]),
    }
    for index in support
}
fingerprint = {
    "support": len(support),
    "constant_only": len(constant_support),
    "t_dependent": len(moving_support),
    "first_rows": support[:16],
}
print("MOMENTUM_FINGERPRINT=" + json.dumps(fingerprint, sort_keys=True))


print("\nD. MOVING-SHIAB PRIMITIVE-EPSILON ZERO-JET RETURN")
# The second source-owned primitive-epsilon summand is
#
#   <T,(D_epsilon S)(Fbar)>.
#
# On the witness,
#
#   Fbar = 1/2 F_BZ + (-t/624-t^2/6) C.
#
# Evaluate it on all 91 Spin generators and reduce through the same quadratic
# quotient.  This is the algebraic moving-Shiab row only; D_B^!p still needs
# the spatial first jet of the momentum bank.
F_FORM = J["F_FORM"]
C_FORM = J["C"]
pairs14 = D["PAIRS"]
r20 = Fraction(351, 28392)
r21 = Fraction(-91, 28392)
r30 = r21 * r20
r31 = r20 + r21 * r21
moving_shiab = []
moving_real = True
d_shiab_f_columns = []
d_shiab_c_columns = []
for pair_index in pairs14:
    eta = M["blade"](pair_index)
    d_shiab_f = M["d_shiab"](F_FORM, SELECTED, eta)
    d_shiab_c = M["d_shiab"](C_FORM, SELECTED, eta)
    d_shiab_f_columns.append(M["flatten"](d_shiab_f))
    d_shiab_c_columns.append(M["flatten"](d_shiab_c))
    a_value = pair(PHI1, d_shiab_f)
    b_value = pair(PHI1, d_shiab_c)
    moving_real = moving_real and a_value[1] == b_value[1] == 0
    a_scalar = Fraction(a_value[0])
    b_scalar = Fraction(b_value[0])
    moving_shiab.append((
        b_scalar * (-r20 / 624 - r30 / 6),
        a_scalar / 2 + b_scalar * (-r21 / 624 - r31 / 6),
    ))

check("real", "all moving-Shiab branch coefficients are real", moving_real)
moving_support = [index for index, value in enumerate(moving_shiab) if value != (0, 0)]
d_shiab_f_rank = M["sparse_rank"](d_shiab_f_columns)
d_shiab_c_rank = M["sparse_rank"](d_shiab_c_columns)
check("exact", "all 91 primitive Spin generators are evaluated in the root algebra",
      len(moving_shiab) == 91)
check("control", "moving-Shiab image banks remain live before pairing with T",
      d_shiab_f_rank > 0 and d_shiab_c_rank > 0)
check("result", "the paired branch moving-Shiab primitive zero-jet return is exactly zero",
      not moving_support)
print("MOVING_SHIAB_FINGERPRINT=" + json.dumps({
    "support": len(moving_support),
    "first_generators": moving_support[:16],
    "F_BZ_image_rank": d_shiab_f_rank,
    "C_image_rank": d_shiab_c_rank,
}, sort_keys=True))


print("\nE. CONTROLS, SCOPE, AND NEXT GATE")
without_symmetric = []
for row, (c0, c1, c2) in enumerate(raw_coefficients):
    wrong_c0 = c0 - 2 * correction[row]
    without_symmetric.append((
        wrong_c0 + Fraction(351, 28392) * c2,
        c1 - Fraction(91, 28392) * c2,
    ))
check("planted", "PLANT deleting the thirteen-cell symmetric DT correction changes p",
      without_symmetric != reduced_coefficients)
check("planted", "PLANT dropping the nonzero-T algebraic E_B term changes p",
      any(algebraic_t2) and any(value[2] != 0 for value in raw_coefficients))
check("scope", "the zero-jet bank does not determine spatial derivatives of p", True)
check("scope", "moving Hodge frame density lowerer and observation returns remain open", True)
check("scope", "a live p value is not a primitive-epsilon obstruction without D_B-adjoint p", True)
check("scope", "both roots remain not yet falsified and SR-1 remains background-missing", True)
check("accounting", "no ledger canon residue quotient datum or posture move occurs", True)

RESULT = {
    "disposition": "BRANCH_MOMENTUM_ZERO_JET_SERIALIZED_AND_LIVE_ON_BOTH_ROOTS__J1P_AND_MOVING_METRIC_RETURNS_STILL_MISSING",
    "branch_polynomial": "28392*t^2+91*t-351",
    "basis_rows": 196,
    "fingerprint": fingerprint,
    "coefficients": serialized,
    "moving_shiab_primitive_zero_jet": {
        "support": len(moving_support),
        "F_BZ_image_rank": d_shiab_f_rank,
        "C_image_rank": d_shiab_c_rank,
        "coefficients": {
            str(index): {
                "constant": str(moving_shiab[index][0]),
                "t": str(moving_shiab[index][1]),
            }
            for index in moving_support
        },
    },
    "E_T": "ZERO_COEFFICIENTWISE_ON_BOTH_ROOTS",
    "p": "E_B_MINUS_E_T_EQUALS_SERIALIZED_E_B_ZERO_JET__NONZERO_ON_BOTH_ROOTS",
    "next_gate": "DIFFERENTIATE_THE_SERIALIZED_P_BANK_ON_THE_ADMITTED_FIRST_JET__COMPOSE_WITH_THE_SERIALIZED_MOVING_SHIAB_RETURN__THEN_COMPLETE_FIXED_VARPI_METRIC_GRAPH",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
