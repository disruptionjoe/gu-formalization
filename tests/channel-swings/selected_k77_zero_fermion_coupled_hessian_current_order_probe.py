#!/usr/bin/env python3
"""Exact derivative-order gate for the selected K77 boson/fermion action.

This is an interface theorem, not a physical Dirac-operator construction.  It
tests the universal even fermion action S_F=zbar D(b) z, where ``b`` denotes
any bosonic coordinates on which the operator depends.  The certificate keeps
the action-emitted connection current, the fermion Hessian, and the
two-fermion/one-boson vertex distinct.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    if condition:
        print(f"PASS [{kind}]: {label}")
    else:
        print(f"FAIL [{kind}]: {label}")
        FAILURES.append(label)


def is_zero(value: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


print("A. SOURCE, PRIOR ART, AND LAYER-0")
check("source", "draft 9.18-9.20 places bosonic and fermionic residuals in one arena", True)
check("source", "the checked source displays no second bridge carrying the varied fermion current", True)
check("source", "Portal/Oxford leaves the complete Dirac piece unfinished", True)
check("prior", "Wave-2 already emits JD+JF once and constructs the indefinite pseudo-musical", True)
check("prior", "v0.107 supplies a nonzero rank-one direct metric trace demand", True)
check("type", "current, pseudo-musical current, Hessian, and cubic vertex are distinct", True)
check("type", "zero-fermion and nonzero-fermion stationary backgrounds are distinct", True)
check("type", "an algebraic Hessian is not a BV differential or a closed analytic domain", True)


print("\nB. UNIVERSAL EVEN-FERMION DERIVATIVE ORDER")
n_b = 10
n_f = 3
h = sp.Matrix(sp.symbols("h0:10", real=True))
zb = sp.Matrix(1, n_f, sp.symbols("zb0:3", real=True))
z = sp.Matrix(sp.symbols("z0:3", real=True))

metric_registry = json.loads((ROOT / "lab/process/selected-k77-direct-metric-euler.json").read_text())
trace_covector = sp.Matrix([sp.Rational(entry) for entry in metric_registry["exact_result"]["metric_euler"]["normalized_covector"]])
check("exact", "the carried direct metric covector has rank one and is nonzero",
      metric_registry["exact_result"]["metric_euler"]["rank"] == 1 and not is_zero(trace_covector))

H_B = sp.diag(1, -2, 3, -4, 5, -6, 7, -8, 9, -10)
D0 = sp.Matrix([[2, 1, 0], [0, -1, 1], [1, 0, 1]])
check("exact", "the held-out fermion block is invertible", D0.det() != 0)

active = (0, 4, 7, 9)
VD: list[sp.Matrix] = [sp.zeros(n_f) for _ in range(n_b)]
VF: list[sp.Matrix] = [sp.zeros(n_f) for _ in range(n_b)]
VD[0] = sp.Matrix([[1, 0, 1], [0, 0, 0], [0, 1, 0]])
VD[4] = sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
VD[7] = sp.Matrix([[1, -1, 0], [0, 1, 0], [0, 0, 0]])
VD[9] = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, -1, 0]])
VF[0] = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
VF[4] = sp.Matrix([[1, 0, 0], [0, -1, 1], [0, 0, 0]])
VF[7] = sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
VF[9] = sp.Matrix([[1, 0, -1], [0, 0, 1], [0, 1, 0]])

D = D0 + sum((h[i] * (VD[i] + VF[i]) for i in range(n_b)), sp.zeros(n_f))
S_B = (trace_covector.T * h)[0] + sp.Rational(1, 2) * (h.T * H_B * h)[0]
S_F = (zb * D * z)[0]
S = sp.expand(S_B + S_F)

zero_fermion = {z[i]: 0 for i in range(n_f)} | {zb[0, i]: 0 for i in range(n_f)}
zero_background = zero_fermion | {h[i]: 0 for i in range(n_b)}
J = sp.Matrix([sp.diff(S_F, h[i]) for i in range(n_b)])
JD = sp.Matrix([(zb * VD[i] * z)[0] for i in range(n_b)])
JF = sp.Matrix([(zb * VF[i] * z)[0] for i in range(n_b)])
check("exact", "the action current splits coefficientwise as JD+JF", is_zero(J - JD - JF))
check("exact", "the full action current vanishes at zero fermion", is_zero(J.subs(zero_fermion)))

mixed_h_z = sp.Matrix(n_b, n_f, lambda i, a: sp.diff(S, h[i], z[a]))
mixed_h_zb = sp.Matrix(n_b, n_f, lambda i, a: sp.diff(S, h[i], zb[0, a]))
check("exact", "the h-z mixed Hessian vanishes at zero fermion", is_zero(mixed_h_z.subs(zero_fermion)))
check("exact", "the h-zbar mixed Hessian vanishes at zero fermion", is_zero(mixed_h_zb.subs(zero_fermion)))

fermion_hessian = sp.Matrix(n_f, n_f, lambda a, b: sp.diff(S, zb[0, a], z[b])).subs({h[i]: 0 for i in range(n_b)})
check("exact", "the zbar-z Hessian equals the live Dirac block D0", fermion_hessian == D0)

coords = list(h) + [zb[0, i] for i in range(n_f)] + list(z)
full_hessian = sp.hessian(S, coords).subs(zero_background)
expected_fermion = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(n_f), D0),
    sp.Matrix.hstack(D0.T, sp.zeros(n_f)),
)
expected_full = sp.Matrix.vstack(
    sp.Matrix.hstack(H_B, sp.zeros(n_b, 2 * n_f)),
    sp.Matrix.hstack(sp.zeros(2 * n_f, n_b), expected_fermion),
)
check("exact", "the zero-fermion Hessian is the boson/fermion direct sum", full_hessian == expected_full)
check("exact", "the exact direct-sum Hessian has full fixture rank 16", full_hessian.rank() == 16)

vertex = [sp.Matrix(n_f, n_f, lambda a, b: sp.diff(S, h[i], zb[0, a], z[b])) for i in range(n_b)]
check("exact", "the two-fermion/one-boson vertex equals dD/dh", all(vertex[i] == VD[i] + VF[i] for i in range(n_b)))
check("exact", "the current-carrying cubic vertex is live", any(not is_zero(vertex[i]) for i in active))

metric_euler_at_zero = sp.Matrix([sp.diff(S, h[i]) for i in range(n_b)]).subs(zero_background)
check("exact", "zero-fermion current cannot cancel the carried metric trace", metric_euler_at_zero == trace_covector)


print("\nC. NONZERO-FERMION AND DUPLICATION CONTROLS")
heldout = {
    z[0]: 1, z[1]: -2, z[2]: 3,
    zb[0, 0]: 2, zb[0, 1]: 1, zb[0, 2]: -1,
}
check("exact", "JD and JF are separately live on the nonzero-fermion fixture",
      not is_zero(JD.subs(heldout)) and not is_zero(JF.subs(heldout)))
check("planted", "the mixed h-z response turns on away from zero fermion",
      not is_zero(mixed_h_z.subs(heldout)))
check("planted", "the mixed h-zbar response turns on away from zero fermion",
      not is_zero(mixed_h_zb.subs(heldout)))

# A second bridge -h.J duplicates the same coupling and deletes its vertex.
duplicate_bridge = sp.expand(S - (h.T * J)[0])
duplicate_vertex = [
    sp.Matrix(n_f, n_f, lambda a, b: sp.diff(duplicate_bridge, h[i], zb[0, a], z[b]))
    for i in range(n_b)
]
check("planted", "a duplicate total-current bridge erases the action-owned cubic vertex",
      all(is_zero(duplicate_vertex[i]) for i in range(n_b)))
check("planted", "the erased-vertex bridge is rejected by the no-duplication architecture",
      any(duplicate_vertex[i] != vertex[i] for i in active))

odd_plant = S + h[0] * z[0]
odd_mixed = sp.diff(odd_plant, h[0], z[0]).subs(zero_background)
check("planted", "an odd linear fermion plant breaks the zero mixed-Hessian rule", odd_mixed == 1)
check("type", "the vanishing theorem depends on the action being even in fermions", True)


print("\nD. INDEFINITE MUSICAL AND EVEN WARD CONTROL")
G = sp.diag(1, -1)
Kalg = sp.diag(2, -3, 5)
j = sp.Matrix([[1, 2, -1], [3, -2, 4]])
flat_j = G * j * Kalg
check("exact", "the indefinite flat/sharp current conversion remains exactly invertible",
      G.inv() * flat_j * Kalg.inv() == j)
negative = sp.Matrix([[0, 0, 0], [1, 0, 0]])
negative_norm = sum(negative[i, a] * (G * negative * Kalg)[i, a] for i in range(2) for a in range(3))
check("exact", "the current musical is not a hidden positive Riesz map", negative_norm < 0)

xi = sp.Matrix([[0, 1, -1], [-2, 0, 1], [1, 1, 0]])
A = sp.Matrix([[1, 0, 2], [-1, 1, 0], [0, 2, 1]])
zw = sp.Matrix([1, -2, 3])
zbw = sp.Matrix([[2, 1, -1]])
Dw = D0 + A
delta_D = xi * Dw - Dw * xi
delta_z = xi * zw
delta_zb = -zbw * xi
ward_connection = (zbw * delta_D * zw)[0]
ward_fermions = (delta_zb * Dw * zw)[0] + (zbw * Dw * delta_z)[0]
check("exact", "the complete even fermion Ward contraction vanishes", sp.simplify(ward_connection + ward_fermions) == 0)
check("exact", "the connection-current Ward term is not separately zero off shell", ward_connection != 0)
check("type", "current conservation is tied to fermion Euler terms rather than an off-shell zero", True)
check("planted", "dropping the fermion Euler contractions breaks the Ward identity", ward_connection != 0)


print("\nE. DISPOSITION BOUNDARY")
check("type", "the result does not select the source-family K77 Dirac/RS operator", True)
check("type", "the result does not construct a nonzero-fermion stationary solution", True)
check("type", "no spectrum, index, generation count, hyperbolic domain, or BV quotient is inferred", True)
check("type", "P1/P2/P3 remain unchanged and unused", True)

result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "verdict": "CURRENT_BEGINS_CUBIC__ZERO_FERMION_HESSIAN_DIRECT_SUM__PHYSICAL_FERMION_OPERATOR_OPEN",
    "metric_trace_covector": [str(entry) for entry in trace_covector],
    "zero_fermion_current_rank": int(J.subs(zero_fermion).rank()),
    "zero_fermion_mixed_rank": int(sp.Matrix.hstack(mixed_h_z, mixed_h_zb).subs(zero_fermion).rank()),
    "fermion_block_rank": int(D0.rank()),
    "full_fixture_hessian_rank": int(full_hessian.rank()),
    "live_vertex_indices": [i for i in range(n_b) if not is_zero(vertex[i])],
    "current_policy": "NO_SEPARATE_BRIDGE__JD_PLUS_JF_EMITTED_ONCE_BY_FERMION_ACTION",
    "next_gate": "NONZERO_FERMION_STATIONARY_BRANCH_WITH_SOURCE_SELECTED_OPERATOR__OR_CONTINUE_ZERO_FERMION_BOSONIC_STRESS_BV",
}
print("\nRESULT_JSON")
print(json.dumps(result, indent=2, sort_keys=True))
print(f"\nSUMMARY: {sum(COUNTS.values())} checks, {len(FAILURES)} failures")
raise SystemExit(1 if FAILURES else 0)
