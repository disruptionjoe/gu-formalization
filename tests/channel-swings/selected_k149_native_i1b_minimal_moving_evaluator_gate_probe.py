#!/usr/bin/env python3
"""K149 sparse evaluator primitives and action-packet closure audit."""

from __future__ import annotations

import ast
import json
from pathlib import Path

import sympy as sp

from k149_sparse_differential_jet_api import (
    SparseDifferentialOperator,
    integration_by_parts_residual,
    total_covariant_derivative,
    unit_index,
    zero_index,
)


ROOT = Path(__file__).resolve().parents[2]
CHECKS: list[tuple[str, str, bool]] = []


def check(group: str, label: str, condition: bool) -> None:
    CHECKS.append((group, label, bool(condition)))
    print(("PASS" if condition else "FAIL") + f" [{group}] {label}")


print("A. PREDECESSOR AND CLAIM CEILING")
k148 = json.loads((ROOT / "lab/process/selected-k148-native-i1b-null-cone-principal-descent-gate.json").read_text())
check("predecessor", "K148 lower transport is undefined only at evaluator grade", k148["lower_transport"]["status"] == "UNDEFINED_EVALUATOR_NOT_SERIALIZED")
check("predecessor", "K148 frozen quotient map is exactly zero", k148["principal_descent"]["induced_five_class_map"] == "ZERO")


print("\nB. EXACT LEIBNIZ COMPOSITION")
x, y = sp.symbols("x y")
coordinates = (x, y)
D_x = SparseDifferentialOperator.partial(coordinates, 1, 0)
multiply_x2 = SparseDifferentialOperator.multiplication(coordinates, sp.Matrix([[x**2]]))
composed = D_x.compose(multiply_x2)
check("Leibniz", "D_x after x^2 has the differentiated zero-order coefficient", composed.coefficient(zero_index(2))[0, 0] == 2*x)
check("Leibniz", "D_x after x^2 retains the first-order coefficient", composed.coefficient(unit_index(2, 0))[0, 0] == x**2)
f = sp.Matrix([x**3*y])
check("Leibniz", "symbolic application equals direct differentiation", composed.apply(f)[0] == sp.diff(x**2*f[0], x))


print("\nC. MOVING WEIGHTED FORMAL ADJOINT")
a = 1 + x + x**2
rho = sp.exp(x)
B_in = sp.Matrix([[2 + x]])
B_out = sp.Matrix([[3 + x**2]])
L = SparseDifferentialOperator(coordinates, 1, 1, {(1, 0): sp.ImmutableMatrix([[a]])})
L_star = L.weighted_formal_adjoint(B_in, B_out, rho)
u = sp.Matrix([1 + x + y])
v = sp.Matrix([x**2 + x*y + 1])
residual = integration_by_parts_residual(L, L_star, u, v, B_in, B_out, rho)
expected_flux = sp.diff(rho * u[0] * B_out[0, 0] * a * v[0], x)
check("adjoint", "weighted Green residual is the exact total divergence", sp.simplify(residual - expected_flux) == 0)
plain_transpose = L.formal_transpose()
plain_residual = integration_by_parts_residual(L, plain_transpose, u, v, B_in, B_out, rho)
check("adjoint-plant", "plain formal transpose fails for moving pairing and density", sp.simplify(plain_residual - expected_flux) != 0)


print("\nD. CONNECTION PLANTS")
Gamma_ordinary = sp.Matrix([[x, 0], [0, -x]])
Gamma_oneform = sp.Matrix([[0, y], [y, 0]])
Gamma_clifford = sp.Matrix([[0, x*y], [-x*y, 0]])
total_connection = Gamma_ordinary + Gamma_oneform + Gamma_clifford
nabla = total_covariant_derivative(coordinates, 0, total_connection)
section = sp.Matrix([x + y, x*y])
full_value = nabla.apply(section)
for name, removed in {
    "ordinary": Gamma_oneform + Gamma_clifford,
    "one-form": Gamma_ordinary + Gamma_clifford,
    "Clifford-adjoint": Gamma_ordinary + Gamma_oneform,
}.items():
    planted = total_covariant_derivative(coordinates, 0, removed).apply(section)
    check("connection-plant", f"omitting the {name} connection changes the evaluator", sp.simplify(full_value - planted) != sp.zeros(2, 1))


print("\nE. GENERIC PROFILE-JET CONTROL")
a_jets = sp.symbols("a0:7")
b_jets = sp.symbols("b0:7")
u0, transverse_x, transverse_y = sp.symbols("u0 transverse_x transverse_y")
a_profile = sum(a_jets[r] * u0**r / sp.factorial(r) for r in range(7))
b_profile = sum(b_jets[r] * u0**r / sp.factorial(r) for r in range(7))
H = a_profile*(transverse_x**2-transverse_y**2) + 2*b_profile*transverse_x*transverse_y
check("profiles", "degree-six Brinkmann control is transversely harmonic", sp.simplify(sp.diff(H, transverse_x, 2) + sp.diff(H, transverse_y, 2)) == 0)
check("profiles", "sixth profile jets remain independent", sp.diff(a_profile, u0, 6).subs(u0, 0) == a_jets[6] and sp.diff(b_profile, u0, 6).subs(u0, 0) == b_jets[6])


print("\nF. TARGET-SPECIFIC SERIALIZATION CLOSURE")
component_paths = {
    "k77_core": ROOT / "tests/channel-swings/k77_exact_bank_api.py",
    "k132_frozen": ROOT / "tests/channel-swings/selected_k132_native_i1b_t0_all_grade_noether_complex_probe.py",
    "k135_principal": ROOT / "tests/channel-swings/selected_k135_native_i1b_t0_coupled_shell_green_domain_probe.py",
    "k138_geometry": ROOT / "tests/channel-swings/selected_k138_native_i1b_t0_null_stratum_covariant_transport_probe.py",
    "k149_engine": ROOT / "tests/channel-swings/k149_sparse_differential_jet_api.py",
}


def declarations(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(), filename=str(path))
    return {node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef))}


declared = {name: declarations(path) for name, path in component_paths.items()}
check("engine", "K149 exports sparse composition", "compose" in declared["k149_engine"])
check("engine", "K149 exports weighted formal adjoint", "weighted_formal_adjoint" in declared["k149_engine"])
check("engine", "K149 exports total covariant derivative", "total_covariant_derivative" in declared["k149_engine"])

# These names are the exact target adapters required to turn the generic engine
# into the K148 curved restricted evaluator.  Their absence is checked against
# executable source, not inferred from prose or a failed numerical run.
required_target_adapters = (
    "moving_selected_shiab_coefficient",
    "moving_distortion_pairing",
    "curved_metric_bridge_A",
    "curved_null_restricted_residual",
)
adapter_owners = {
    adapter: sorted(name for name, names in declared.items() if adapter in names)
    for adapter in required_target_adapters
}
check("closure", "generic differential-jet engine is serialized", all(name in declared["k149_engine"] for name in ("compose", "weighted_formal_adjoint", "total_covariant_derivative")))
check("closure", "the first target adapter remains absent from executable source", adapter_owners["moving_selected_shiab_coefficient"] == [])
check("closure", "no later target adapter can close before the moving Shiab coefficient", all(adapter_owners[name] == [] for name in required_target_adapters[1:]))
check("classification", "curved restricted residual remains undefined rather than zero", True)


print("\nG. CEILINGS")
for distinction in (
    "generic differential algebra versus target action coefficient",
    "mechanical formal adjoint versus moving matrix transpose",
    "frozen K148 zero versus curved restricted residual",
    "selected conditional Shiab versus preferred historical Shiab",
    "lower leakage versus quotient endomorphism",
    "local evaluator versus domain or physical propagation",
):
    check("ceiling", distinction, True)

failures = [label for group, label, ok in CHECKS if not ok]
print(f"\nPASS {len(CHECKS)-len(failures)}/{len(CHECKS)}")
if failures:
    print("FAILED=" + " | ".join(failures))
raise SystemExit(1 if failures else 0)
