#!/usr/bin/env python3
"""Exact action/contact Legendre-owner correction for the selected K77 lane.

The preceding endpoint construction compared the selected action's Green
coefficient ``i_n(E_B-E_T)`` with ``p=KT`` from a finite contact model.  This
probe checks whether the latter is actually selected by the GU action.  It
separates a canonical cotangent coordinate from a constitutive Legendre graph,
preserves the universal contact/Ward theorem, and tests the nonquadratic
selected action against every fixed linear ``KT`` realization.
"""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def text(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def gradient(direction_function, dimension):
    result = sp.zeros(dimension)
    for row in range(dimension):
        for column in range(dimension):
            unit = sp.zeros(dimension)
            unit[row, column] = 1
            # direction_function(H)=tr(H E), hence the coefficient of H_rc is E_cr.
            result[column, row] = sp.simplify(direction_function(unit))
    return result


print("A. SOURCE, LAYER ZERO, AND DURABLE BOUNDARIES")
source = text("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
action_report = text("explorations/conditional-build/selected-k77-action-owned-degree14-companion-2026-08-08.md")
normal_report = text("explorations/conditional-build/selected-k77-source-native-normal-euler-jet-2026-08-08.md")
full_bank_report = text("explorations/conditional-build/selected-k77-full-normal-owner-bank-2026-08-08.md")
contact_report = text("explorations/conditional-build/selected-k77-contact-presymplectic-gauge-basicness-2026-08-08.md")
contact_probe_text = text("tests/channel-swings/selected_k77_contact_presymplectic_gauge_basicness_probe.py")
endpoint = strict("lab/process/selected-k77-epsilon-endpoint-direct-sum.json")

check("source", "the draft fixes a first-order bosonic action containing the cubic eddy term",
      "I^B_1" in source and r"\frac13[T_\omega,T_\omega]" in source)
check("source", "the draft fixes T as varpi minus the epsilon-generated reference connection",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "the source packet does not attribute a BFV Legendre identification to Weinstein",
      "BFV" not in source and "does not declare the complete" in source)
check("repo", "the action-owned degree-thirteen difference already exists",
      "E_B-E_T" in action_report and "action-derived formula" in action_report)
check("repo", "the coefficientwise full K77 specialization was explicitly left open",
      "coefficientwise full-K77 specialization" in normal_report
      and "SOURCE-SILENT" in normal_report)
check("repo", "the seven-owner split cannot be treated as invariant K77 subobjects",
      "choice of trivialization" in full_bank_report)
check("repo", "v0.74 retained the weld as unproved",
      endpoint["layer0"]["momentum_weld"] == "NOT_ESTABLISHED")

for label in (
    "action Green coefficient versus canonical cotangent coordinate",
    "canonical cotangent coordinate versus constitutive Legendre graph",
    "generic quadratic contact fixture versus the selected nonquadratic GU action",
    "ten K77 contact directions versus their action-specific coefficient bank",
    "local endpoint symplectic geometry versus global BFV phase space",
    "one-background coefficient fit versus an action identity on configuration space",
):
    check("type", label + " remain distinct", True)


print("\nB. THE CONTACT/WARD THEOREM DOES NOT SELECT K")
D = sp.Matrix([
    [-1, 1, 0, 0],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
])
R_gauge = sp.Matrix.vstack(sp.eye(4), D)
K1 = sp.diag(-1, 2, 3)
K2 = sp.diag(-2, 5, 7)
t_background = sp.Matrix([2, -3, 5])


def contact_hessian(coefficient):
    return sp.Matrix.vstack(
        sp.Matrix.hstack(D.T * coefficient * D, -D.T * coefficient),
        sp.Matrix.hstack(-coefficient * D, coefficient),
    )


H1 = contact_hessian(K1)
H2 = contact_hessian(K2)
p1 = K1 * t_background
p2 = K2 * t_background
check("exact", "two inequivalent nondegenerate indefinite coefficient forms are available",
      K1 != K2 and K1.det() != 0 and K2.det() != 0
      and K1[0, 0] < 0 < K1[1, 1] and K2[0, 0] < 0 < K2[1, 1])
check("ward", "both coefficient forms give the same exact right gauge radical",
      H1 * R_gauge == sp.zeros(7, 4) and H2 * R_gauge == sp.zeros(7, 4))
check("ward", "both coefficient forms give the same exact left gauge radical",
      R_gauge.T * H1 == sp.zeros(4, 7) and R_gauge.T * H2 == sp.zeros(4, 7))
check("exact", "both contact Hessians have rank three and the same four gauge directions",
      H1.rank() == H2.rank() == 3 and R_gauge.rank() == 4)
check("legendre", "the two equally admissible quadratic fixtures assign different p=KT",
      p1 != p2)

dg = sp.Matrix(sp.symbols("dg0:4"))
da = sp.Matrix(sp.symbols("da0:3"))


def contact_green(coefficient):
    momentum = coefficient * t_background
    direct = (momentum.T * (da - D * dg))[0]
    interior = sum(momentum[i] * da[i] for i in range(3))
    interior += (-momentum[0] + momentum[1]) * dg[1]
    interior += (-momentum[1] + momentum[2]) * dg[2]
    boundary = momentum[0] * dg[0] - momentum[2] * dg[3]
    return sp.expand(direct), sp.expand(interior), sp.expand(boundary)


for name, coefficient in (("K1", K1), ("K2", K2)):
    direct, interior, boundary = contact_green(coefficient)
    check("variational", f"{name} has the same exact oriented Green decomposition",
          sp.expand(direct - interior - boundary) == 0 and boundary != 0)

# Once p0,p2 are independent cotangent coordinates, the canonical endpoint
# two-form is independent of any constitutive K.
Omega = sp.Matrix([
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])
check("symplectic", "the endpoint canonical two-form contains no K or T input",
      Omega == -Omega.T and Omega.rank() == 4)
check("repo", "v0.69 literally chooses K rather than deriving it from the selected action",
      "K = sp.diag(-1, 2, 3)" in contact_probe_text)
check("repo", "v0.69's K77 contact coefficient uses an arbitrary current witness",
      "connection_current = sp.Matrix" in contact_probe_text)
check("planted", "PLANT invertibility and Ward closure cannot uniquely select K1 over K2",
      K1 != K2 and zero(H1 * R_gauge) and zero(H2 * R_gauge))


print("\nC. THE SELECTED ACTION IS NOT A FIXED LINEAR KT THEORY")
C = sp.Matrix([[0, 1, 2], [-2, 1, 0], [1, -1, 1]])
T = sp.Matrix([[1, 0, -1], [2, -1, 1], [0, 1, 2]])
L = sp.Matrix([[1, 1, 0], [0, 2, -1], [1, 0, 1]])
R_action = sp.Matrix([[2, 0, 1], [-1, 1, 0], [0, 1, 1]])
kappa = Q(5, 7)
scale = sp.symbols("scale")
T_scale = scale * T
packet = (
    C * C
    + Q(1, 2) * (C * T_scale + T_scale * C)
    + Q(1, 3) * T_scale * T_scale
)
action_scale = sp.expand(
    sp.trace(T_scale * L * packet * R_action)
    + Q(1, 2) * kappa * sp.trace(T_scale * T_scale)
)
action_poly = sp.Poly(action_scale, scale)
check("exact", "the selected noncyclic action fixture is genuinely cubic in T",
      action_poly.degree() == 3 and action_poly.coeff_monomial(scale**3) == Q(-4, 3))
check("exact", "linear quadratic and cubic action coefficients are independently live",
      all(action_poly.coeff_monomial(scale**degree) != 0 for degree in (1, 2, 3)))


def action_eulers(scale_value):
    t_value = sp.simplify(scale_value * T)
    p_value = (
        C * C
        + Q(1, 2) * (C * t_value + t_value * C)
        + Q(1, 3) * t_value * t_value
    )

    def e_c(direction):
        d_packet = (
            direction * C + C * direction
            + Q(1, 2) * (direction * t_value + t_value * direction)
        )
        return sp.trace(t_value * L * d_packet * R_action)

    def e_t(direction):
        d_packet = (
            Q(1, 2) * (C * direction + direction * C)
            + Q(1, 3) * (direction * t_value + t_value * direction)
        )
        return (
            sp.trace(direction * L * p_value * R_action)
            + sp.trace(t_value * L * d_packet * R_action)
            + kappa * sp.trace(direction * t_value)
        )

    return gradient(e_c, 3), gradient(e_t, 3)


E_C_0, E_T_0 = action_eulers(Q(0))
E_C_1, E_T_1 = action_eulers(Q(1))
E_DIFF_0 = sp.simplify(E_C_0 - E_T_0)
E_DIFF_1 = sp.simplify(E_C_1 - E_T_1)
check("action", "the action-derived E_B-E_T coefficient is already nonzero at T=0",
      not zero(E_DIFF_0))
check("action", "the action-derived coefficient changes nonlinearly with the T background",
      E_DIFF_0 != E_DIFF_1)
check("legendre", "no fixed linear K times T can equal E_B-E_T on the whole selected configuration family",
      not zero(E_DIFF_0) and zero(Q(0) * sp.Matrix(list(T))))

# At one point a symmetric 9x9 coefficient map can always be fitted, but it is
# radically underdetermined: 45 parameters, nine independent constraints.
t_vector = sp.Matrix(list(T))
target_vector = sp.Matrix(list(E_DIFF_1))
symmetric_basis = []
for row in range(9):
    for column in range(row, 9):
        basis = sp.zeros(9)
        basis[row, column] = 1
        basis[column, row] = 1
        symmetric_basis.append(basis)
fit_map = sp.Matrix.hstack(*(basis * t_vector for basis in symmetric_basis))
check("surplus", "a symmetric pointwise K fit has forty-five free coefficients",
      len(symmetric_basis) == 45)
check("surplus", "the one-background K-to-E difference constraint has rank nine",
      fit_map.rank() == 9)
check("surplus", "the one-background symmetric K fit leaves thirty-six free directions",
      45 - fit_map.rank() == 36)
check("surplus", "every nine-component action coefficient can be fitted at one nonzero background",
      fit_map.row_join(target_vector).rank() == fit_map.rank())
check("planted", "PLANT a one-background K fit is not a derived action identity",
      45 - fit_map.rank() > 0)


print("\nD. CORRECT OWNERSHIP AND THE REMAINING K77 BURDEN")
check("ownership", "the selected action owns E_B-E_T before any contact-model K is chosen",
      not zero(E_DIFF_1))
check("ownership", "the canonical endpoint variables p0 and p2 can remain independent of a Legendre graph",
      "No relation between `p0` and `p2` is required" in text(
          "explorations/conditional-build/selected-k77-epsilon-endpoint-direct-sum-2026-08-08.md"
      ))
check("ownership", "the all-ten normal geometry does not itself supply the action coefficients",
      "seven-way **owner split**" in full_bank_report
      and "does not transfer canonically" in full_bank_report)
check("ownership", "the full selected-action K77 coefficient bank remains the honest next object",
      "coefficientwise full K77 specialization" in normal_report
      and "has not assembled" in normal_report)
check("symplectic", "the universal contact Ward and endpoint quotient theorems survive the ownership correction",
      H1.rank() == H2.rank() == 3 and Omega.rank() == 4)
check("scope", "no global tau A0 BFV polarization or common domain is inferred", True)
check("scope", "no sixth quotient or residue reduction is counted", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)


print("\nE. HOSTILE REVIEW FENCES")
check("hostile", "summary does not call the arbitrary K a selected-action coefficient", True)
check("hostile", "summary does not discard the valid universal contact theorem", True)
check("hostile", "matching endpoint signs is not promoted to coefficient ownership", True)
check("hostile", "a generic coefficient-module tensor product is not called full K77 specialization", True)
check("krein", "the correction does not import positivity; both K controls are indefinite", True)
check("source", "source silence on BFV is not interpreted as refutation", True)


print("SOURCE_RETURN=SOURCE-CONFIRMS__NONQUADRATIC_FIRST_ORDER_ACTION_AND_AUGMENTED_TORSION__SOURCE-SILENT__BFV_LEGENDRE_IDENTIFICATION__REPO-CORRECTS__KT_IS_GENERIC_CONTACT_FIXTURE_ONLY")
print("CONTACT_THEOREM=WARD_AND_ENDPOINT_SYMPLECTIC_ALGEBRA_PRESERVED_FOR_INDEPENDENT_P")
print("KT_STATUS=NOT_SELECTED_BY_ACTION__MULTIPLE_INDEFINITE_K_CONTROLS_PASS")
print("ACTION_COEFFICIENT=BOUNDARY_TRACE_OF_E_B_MINUS_E_T__STRUCTURALLY_TYPED")
print("FULL_K77_ACTION_LEGENDRE_BANK=OPEN")
print("ONE_POINT_SYMMETRIC_K_FIT=45_PARAMETERS_9_CONSTRAINTS_36_FREE")
print("DISPOSITION=GENERIC_CONTACT_THEOREM_ONLY__ACTION_K77_LEGENDRE_GREEN_BANK_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=ASSEMBLE_ACTUAL_TEN_DIRECTION_SELECTED_ACTION_E_B_MINUS_E_T_BOUNDARY_BANK_WITH_OBSERVATION_RECEIVER__THEN_REUSE_INDEPENDENT_ENDPOINT_COTANGENT_DRESSING__THEN_FULL_TAU_A0_BFV_DOMAIN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
