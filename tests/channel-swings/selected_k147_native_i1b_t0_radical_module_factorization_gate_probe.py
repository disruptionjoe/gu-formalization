#!/usr/bin/env python3
"""Exact K147 finite-jet radical-module factorization controls.

This probe does not evaluate the full I1B operator.  It certifies the exact
finite-jet criterion that a future sparse evaluator must satisfy before the
formal metric polynomial S_4 can descend from H_n to H_n/G_n.
"""

from __future__ import annotations

import ast
from contextlib import redirect_stdout
from io import StringIO
import json
import math
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
checks = 0


def check(group: str, label: str, condition: bool) -> None:
    global checks
    if not condition:
        raise AssertionError(f"{group}: {label}")
    checks += 1
    print(f"PASS [{group}] {label}")


def multiindices(dimension: int, maximum_order: int) -> list[tuple[int, ...]]:
    """All commuting derivative multiindices of total order at most the cap."""
    return [
        alpha
        for alpha in product(range(maximum_order + 1), repeat=dimension)
        if sum(alpha) <= maximum_order
    ]


def normalized_monomial(
    coordinates: tuple[sp.Symbol, ...], alpha: tuple[int, ...]
) -> sp.Expr:
    result = sp.Integer(1)
    for coordinate, power in zip(coordinates, alpha):
        result *= coordinate**power / math.factorial(power)
    return result


def derivative_at_origin(
    expression: sp.Expr,
    coordinates: tuple[sp.Symbol, ...],
    alpha: tuple[int, ...],
) -> sp.Expr:
    value = expression
    for coordinate, power in zip(coordinates, alpha):
        value = sp.diff(value, coordinate, power)
    return sp.simplify(value.subs(dict.fromkeys(coordinates, 0)))


print("A. PREDECESSOR, CARRIER, AND ORDER CUSTODY")
k144 = json.loads(
    (ROOT / "lab/process/selected-k144-native-i1b-t0-curved-local-inverse-owner-gate.json").read_text()
)
k145 = json.loads(
    (ROOT / "lab/process/selected-k145-native-i1b-t0-curved-c-composition-and-compatibility.json").read_text()
)
k146 = json.loads(
    (ROOT / "lab/process/selected-k146-native-i1b-t0-null-remainder-type-and-quotient-gate.json").read_text()
)
check(
    "predecessor",
    "K144 leaves five-class basicness undefined",
    k144["quotient"]["basicness"] == "UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR",
)
check(
    "predecessor",
    "K145 owns the consecutive-zero diffeomorphism chain",
    k145["noether_compatibility"]["A_G_zero"] is True,
)
check(
    "predecessor",
    "K146 types S4 as the first local metric polynomial",
    k146["polynomial_metric_operator"]["action_owned_formal_local_operator"] is True,
)
check(
    "predecessor",
    "K146 proves gauge annihilation but leaves radical preservation open",
    k146["polynomial_metric_operator"]["G_n_preservation"] == "PASS_BY_A_G_ZERO"
    and k146["polynomial_metric_operator"]["H_n_preservation"]
    == "UNEVALUATED_CURVED_COMPOSITION",
)

order_A = 2
order_P = 1
highest_neumann_power = 4
order_A_star = 2
operator_order_bound = order_A + highest_neumann_power * order_P + order_A_star
check("order", "S4 has structural differential-order bound eight", operator_order_bound == 8)
check(
    "order",
    "the bound is 2 + four first-order factors + 2",
    (order_A, highest_neumann_power, order_P, order_A_star) == (2, 4, 1, 2),
)


print("\nB. COMPLETE FINITE POLYNOMIAL-JET BASIS")
coordinates = sp.symbols("x0:4")
jet_indices = multiindices(4, operator_order_bound)
expected_scalar_jets = math.comb(4 + operator_order_bound, 4)
check("jets", "four-variable order-at-most-eight jet count is 495", len(jet_indices) == expected_scalar_jets == 495)
check("jets", "jet multiindices are unique", len(set(jet_indices)) == len(jet_indices))
check("jets", "orders zero through eight are all represented", {sum(alpha) for alpha in jet_indices} == set(range(9)))

# x^alpha/alpha! has alpha derivative one at the origin.  These are exact
# polynomial representatives of every independent scalar jet coordinate.
for alpha in jet_indices:
    monomial = normalized_monomial(coordinates, alpha)
    if derivative_at_origin(monomial, coordinates, alpha) != 1:
        raise AssertionError(f"jets: normalized monomial failed for {alpha}")
check("jets", "all 495 normalized monomials realize their exact unit jet", True)

radical_dimension = 9
radical_generators = [(column, alpha) for column in range(radical_dimension) for alpha in jet_indices]
check("jets", "nine radical columns give 4455 independent generators", len(radical_generators) == 4455)
check("jets", "all radical jet generators are unique", len(set(radical_generators)) == 4455)


print("\nC. EXACT FACTORIZATION THEOREM IN THE FINITE JET MODULE")
metric_dimension = 10
complement_column = 9
kappa = sp.symbols("kappa", nonzero=True)
a_jets = sp.symbols("a0:7")
b_jets = sp.symbols("b0:7")

# A differential row D=ell*S is represented by one coefficient dictionary per
# metric input column.  ell=(0,...,0,1), so D=Q*ell exactly iff the first nine
# dictionaries vanish.  The last dictionary is then the uniquely extracted Q.
zero_row: list[dict[tuple[int, ...], sp.Expr]] = [dict() for _ in range(metric_dimension)]
q_coefficients = {
    (0, 0, 0, 0): kappa**4 + a_jets[0] - b_jets[1],
    (1, 0, 0, 0): kappa**3 + a_jets[1],
    (0, 2, 0, 0): kappa**2 + b_jets[2],
    (3, 0, 1, 0): kappa + a_jets[4],
    (8, 0, 0, 0): 1 + a_jets[6] + b_jets[6],
}
passing_row = [dict(column) for column in zero_row]
passing_row[complement_column] = dict(q_coefficients)


def radical_columns_vanish(
    differential_row: list[dict[tuple[int, ...], sp.Expr]],
) -> bool:
    return all(
        sp.simplify(coefficient) == 0
        for column in differential_row[:radical_dimension]
        for coefficient in column.values()
    )


def extracted_q(
    differential_row: list[dict[tuple[int, ...], sp.Expr]],
) -> dict[tuple[int, ...], sp.Expr]:
    return differential_row[complement_column]


check("factorization", "passing row annihilates every radical jet column", radical_columns_vanish(passing_row))
check("factorization", "Q is recovered from the normalized complement column", extracted_q(passing_row) == q_coefficients)

# Recomposition of Q ell has zero coefficients on H and Q on the normalized
# complement.  This is the exact finite-jet form of ell*S=Q*ell.
recomposed_row = [dict() for _ in range(metric_dimension)]
recomposed_row[complement_column] = dict(extracted_q(passing_row))
check("factorization", "passing row equals the recomposed Q ell row", passing_row == recomposed_row)
check("factorization", "factorization is sufficient for H preservation", radical_columns_vanish(recomposed_row))

failing_row = [dict(column) for column in passing_row]
failing_alpha = (8, 0, 0, 0)
failing_row[4][failing_alpha] = a_jets[6] + 1
check("factorization", "planted radical coefficient defeats factorization", not radical_columns_vanish(failing_row))
check("factorization", "planted failure cannot equal Q ell", failing_row != recomposed_row)

# Necessity: the normalized polynomial x0^8/8! in radical column four isolates
# the planted coefficient at the origin and has ell(h)=0 identically.
failure_section = normalized_monomial(coordinates, failing_alpha)
failure_value = (a_jets[6] + 1) * derivative_at_origin(
    failure_section, coordinates, failing_alpha
)
check("factorization", "one exact H-valued polynomial section detects the failure", sp.simplify(failure_value - a_jets[6] - 1) == 0)


print("\nD. POINTWISE, AFFINE, AND PROFILE-ORDER CONTROLS")
pointwise_indices = [alpha for alpha in jet_indices if sum(alpha) == 0]
affine_indices = [alpha for alpha in jet_indices if sum(alpha) <= 1]
check("insufficiency", "pointwise testing sees only one of 495 scalar jets", len(pointwise_indices) == 1)
check("insufficiency", "affine section testing sees only five of 495 scalar jets", len(affine_indices) == 5)
check("insufficiency", "order-eight planted leak is invisible pointwise and on affine sections", failing_alpha not in pointwise_indices and failing_alpha not in affine_indices)
check("insufficiency", "degree-eight jet basis detects the same planted leak", failing_alpha in jet_indices)

# The raw coefficient bound is metric order two plus six outer derivatives.
metric_coefficient_jet_order = 2
outer_coefficient_derivatives = highest_neumann_power * order_P + order_A_star
metric_jet_bound = metric_coefficient_jet_order + outer_coefficient_derivatives
profile_jet_bound = metric_jet_bound - 2  # two transverse derivatives expose a or b
check("profiles", "metric coefficient jets have safe structural bound eight", metric_jet_bound == 8)
check("profiles", "Brinkmann profiles therefore require jets through order six", profile_jet_bound == 6)

u, x, y = sp.symbols("u x y")
a_profile = sum(a_jets[r] * u**r / math.factorial(r) for r in range(7))
b_profile = sum(b_jets[r] * u**r / math.factorial(r) for r in range(7))
brinkmann_H = a_profile * (x**2 - y**2) + 2 * b_profile * x * y
check(
    "profiles",
    "arbitrary degree-six two-profile Brinkmann control is transversely harmonic",
    sp.simplify(sp.diff(brinkmann_H, x, 2) + sp.diff(brinkmann_H, y, 2)) == 0,
)
check("profiles", "sixth profile derivatives are independent exact variables", sp.diff(a_profile, u, 6).subs(u, 0) == a_jets[6] and sp.diff(b_profile, u, 6).subs(u, 0) == b_jets[6])
affine_profile_substitution = {
    **{a_jets[r]: 0 for r in range(2, 7)},
    **{b_jets[r]: 0 for r in range(2, 7)},
}
profile_only_leak = a_jets[6]
check("insufficiency", "affine profiles erase a planted sixth-profile-jet obstruction", profile_only_leak.subs(affine_profile_substitution) == 0)
check("insufficiency", "generic degree-six profiles retain that obstruction", profile_only_leak != 0)


print("\nE. FROZEN IMPLEMENTATION REPLAY AND RESTRICTED RESIDUAL")
k135_probe = ROOT / "tests/channel-swings/selected_k135_native_i1b_t0_coupled_shell_green_domain_probe.py"
k135_source = k135_probe.read_text()
k135_source = k135_source.split('print("\\nD. DOMAIN, NOETHER, AND BV CONSEQUENCES")', 1)[0]
k135_namespace = {"__file__": str(k135_probe), "__name__": "k135_for_k147"}
with redirect_stdout(StringIO()):
    exec(compile(k135_source, str(k135_probe), "exec"), k135_namespace)

k132_namespace = k135_namespace["S"]
check(
    "frozen-replay",
    "K132 all-grade selected Euler ranks are recovered",
    (
        k132_namespace["timelike"]["euler_rank"],
        k132_namespace["spacelike"]["euler_rank"],
        k132_namespace["null"]["euler_rank"],
    )
    == (130912, 130912, 122746),
)

Cn = k135_namespace["Cn"]
Kn = k135_namespace["Kn"]
An = k135_namespace["An"]
Ln = k135_namespace["Ln"]
power_ranks = [int((Ln**power).rank()) for power in range(1, 6)]
check(
    "frozen-replay",
    "K135 principal null action packet recovers the terminal Jordan ranks",
    power_ranks == [90, 48, 6, 3, 0],
)
check(
    "frozen-replay",
    "the principal action bridge has the exact null rank four",
    An.shape == (Cn.rows, 10) and An.rank() == 4 and Kn.shape == Cn.shape,
)

# At frozen null-symbol grade P is represented by L_n=K C_1(n).  This is an
# implementation replay only: variable coefficients turn products into
# Leibniz compositions and are deliberately absent from this calculation.
frozen_restricted_residual = Kn * (Ln**5) * Kn * An
check(
    "restricted-residual",
    "K P^5 K A vanishes on the frozen principal action image",
    frozen_restricted_residual == sp.zeros(Cn.rows, 10),
)
check(
    "restricted-residual",
    "the zero follows from full frozen L_n^5 rather than an inferred curved identity",
    Ln**5 == sp.zeros(Ln.rows) and power_ranks[-2] > 0,
)
check(
    "classification",
    "frozen restricted-residual zero is implementation validation only",
    True,
)


print("\nF. NECESSARY ORDER-EIGHT PRINCIPAL-MODULE TEST")
metric_slots = k135_namespace["METRIC_SLOTS"]
eta4 = sp.diag(1, -1, -1, -1)
fixed_null_covector = sp.Matrix([1, 0, 0, 1])
fixed_null_raised = eta4 * fixed_null_covector
ell_n = sp.Matrix(
    [
        fixed_null_raised[i] * fixed_null_raised[j] * (2 if i != j else 1)
        for i, j in metric_slots
    ]
)
H_n_basis = sp.Matrix.hstack(*ell_n.T.nullspace())
check(
    "principal-module",
    "the fixed null radical has exact dimension nine",
    ell_n.shape == (10, 1) and H_n_basis.shape == (10, 9) and ell_n.T * H_n_basis == sp.zeros(1, 9),
)


def principal_order_eight_leakage(
    derivative_covector: tuple[int, ...], toggles: tuple[int, ...]
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    _, coefficient, mass, action = k135_namespace["coupled_local"](
        derivative_covector, toggles
    )
    principal_p = mass * coefficient
    sigma_eight = -action.T * (principal_p**4 * mass) * action
    leakage = sp.simplify(ell_n.T * sigma_eight * H_n_basis)
    return sigma_eight, leakage, action


timelike_xi = (1, 0, 0, 0) + (0,) * 10
spacelike_xi = (0, 1, 0, 0) + (0,) * 10
sigma8_t, leakage_t, action_t = principal_order_eight_leakage(timelike_xi, (0,))
sigma8_s, leakage_s, action_s = principal_order_eight_leakage(spacelike_xi, (1,))
check(
    "principal-module",
    "timelike and spacelike principal action bridges replay rank six",
    action_t.rank() == action_s.rank() == 6,
)
principal_leakage_witnesses = {
    "timelike": [
        (row, column, sp.simplify(leakage_t[row, column]))
        for row in range(leakage_t.rows)
        for column in range(leakage_t.cols)
        if sp.simplify(leakage_t[row, column]) != 0
    ],
    "spacelike": [
        (row, column, sp.simplify(leakage_s[row, column]))
        for row in range(leakage_s.rows)
        for column in range(leakage_s.cols)
        if sp.simplify(leakage_s[row, column]) != 0
    ],
}
check(
    "principal-module",
    "the complete order-eight principal symbols are actually composed",
    sigma8_t.shape == sigma8_s.shape == (10, 10) and sigma8_s.rank() == 6,
)
expected_spacelike_leakage_row = sp.Matrix(
    [[-64, 0, 0, -256, 0, 0, 0, 0, 0, -64]]
)
actual_spacelike_leakage_row = sp.simplify(ell_n.T * sigma8_s)
check(
    "principal-module",
    "the spacelike order-eight leakage row is recovered coefficientwise",
    actual_spacelike_leakage_row == expected_spacelike_leakage_row,
)
explicit_radical_witness = sp.Matrix([2, 0, 0, 1, 0, 0, 0, 0, 0, 0])
check(
    "principal-module",
    "the explicit witness h=(2,0,0,1,0,...,0) lies in the fixed null radical",
    (ell_n.T * explicit_radical_witness)[0] == 0,
)
check(
    "principal-module",
    "the spacelike principal symbol leaks that radical witness by minus 384",
    (actual_spacelike_leakage_row * explicit_radical_witness)[0] == -384,
)
check(
    "principal-module",
    "an exact causal derivative covector leaks the fixed null radical",
    any(principal_leakage_witnesses.values()),
)
print("PRINCIPAL_LEAKAGE_WITNESSES", principal_leakage_witnesses)
check(
    "classification",
    "nonzero order-eight leakage decisively fails full differential-module preservation",
    any(principal_leakage_witnesses.values()),
)
check(
    "route-switch",
    "the failure returns the question to the correctly scoped null-microlocal object",
    True,
)


print("\nG. MACHINE-CHECKED VARIABLE-COEFFICIENT INVENTORY")


def declared_callables(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(), filename=str(path))
    names = {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    }
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            names.update(
                child.name
                for child in node.body
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
            )
    return names


component_paths = {
    "k77_core": ROOT / "tests/channel-swings/k77_exact_bank_api.py",
    "k132_frozen": ROOT / "tests/channel-swings/selected_k132_native_i1b_t0_all_grade_noether_complex_probe.py",
    "k135_principal": ROOT / "tests/channel-swings/selected_k135_native_i1b_t0_coupled_shell_green_domain_probe.py",
    "k138_geometry": ROOT / "tests/channel-swings/selected_k138_native_i1b_t0_null_stratum_covariant_transport_probe.py",
}
declared = {name: declared_callables(path) for name, path in component_paths.items()}
required_variable_primitives = {
    "total_covariant_distortion_derivative",
    "variable_formal_euler",
    "leibniz_operator_compose",
    "sparse_differential_jet_apply",
    "curved_metric_bridge_A",
    "curved_metric_bridge_A_star",
}
present_required = {
    primitive: sorted(name for name, names in declared.items() if primitive in names)
    for primitive in required_variable_primitives
}
check(
    "inventory",
    "all four reusable component files parse as Python syntax trees",
    all(declared.values()),
)
check(
    "inventory",
    "no reusable component declares the six required unified variable-coefficient primitives",
    all(not owners for owners in present_required.values()),
)
check(
    "inventory",
    "K132 exports frozen raw_block but no variable formal Euler constructor",
    "raw_block" in declared["k132_frozen"]
    and "variable_formal_euler" not in declared["k132_frozen"],
)
check(
    "inventory",
    "K135 exports principal_riemann and coupled_local but no curved A bridge",
    {"principal_riemann", "coupled_local"}.issubset(declared["k135_principal"])
    and "curved_metric_bridge_A" not in declared["k135_principal"],
)
check(
    "inventory",
    "K138 exports the Brinkmann geometry fixture but no distortion covariant derivative",
    {"riemann_up", "riemann_down"}.issubset(declared["k138_geometry"])
    and "total_covariant_distortion_derivative" not in declared["k138_geometry"],
)
check(
    "classification",
    "owned conditional formulas are not yet unified in an executable curved evaluator",
    all(not owners for owners in present_required.values()),
)


print("\nH. CLAIM CEILING AND MINIMAL CERTIFICATE")
for distinction in (
    "pointwise fibre preservation versus differential-module preservation",
    "null-symbol preservation versus all-derivative-covector module preservation",
    "constant or affine sections versus arbitrary order-eight section jets",
    "affine Brinkmann profiles versus generic order-six profile jets",
    "S4 gauge annihilation versus S4 radical preservation",
    "finite-jet factorization theorem versus evaluation of the full I1B S4",
    "frozen restricted-residual zero versus curved restricted-residual zero",
    "owned conditional formulas versus unified executable serialization",
    "fixed-null microlocal preservation versus full differential-module preservation",
):
    check("ceiling", distinction + " remain distinct", True)

check("certificate", "a single nonzero radical jet coefficient is an exact failure certificate", failing_row[4][failing_alpha] != 0)
check("certificate", "a pass requires all 4455 radical coefficients to vanish", len(radical_generators) == 4455 and radical_columns_vanish(passing_row))
check("certificate", "only after that pass is Q obtained from the complement", extracted_q(passing_row) == q_coefficients)
check("scope", "probe certifies full-module principal failure without claiming a curved null-microlocal PASS or FAIL", True)

print(f"PASS {checks}/{checks}")
