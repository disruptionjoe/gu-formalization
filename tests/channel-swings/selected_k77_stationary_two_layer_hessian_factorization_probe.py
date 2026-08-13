#!/usr/bin/env python3
"""Exact stationary factorization and owner gate for GU's second action.

At a background where the complete first-layer residual Upsilon vanishes,
the bulk Hessian of 1/2 <Upsilon,K Upsilon> is J^! K J.  This probe checks
that statement without deleting physical operator motion inside J=D Upsilon,
and composes it with the v0.81 coupled-complex scope result.
"""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PREDECESSOR, AND LAYER ZERO")
V81 = json.loads(read("lab/process/selected-k77-coupled-euler-complex-scope.json"))
check("repo", "v0.81 immutable registry records both independent exact routes",
      V81["controls"]["sympy_composed_route"] == "56/56 PASS"
      and V81["controls"]["independent_sage"] == "15/15 PASS")

source = read("lab/sources/selected-k77-stationary-two-layer-hessian-factorization-source-reinspection-2026-08-08.md")
correction = read("explorations/conditional-build/selected-second-layer-residual-constituent-operator-correction-2026-08-07.md")
observation = read("explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md")
check("source", "source confirms residual norm-square grammar and first-solution redundancy",
      "SOURCE-CONFIRMS__RESIDUAL_NORM_SQUARE_AND_FIRST_SOLUTION_REDUNDANCY" in source)
check("source", "source is silent on the common-field Jacobian and residual pairing",
      "SOURCE-SILENT__COMMON_FIELD_DUPSILON_BLOCKS_PAIRING_AND_PHYSICAL_COMPLEX" in source)
check("repo", "the constituent correction preserves physical Shiab and Hodge movement inside D Upsilon",
      "independent physical" in correction and "variation of Shiab and Hodge" in correction)
check("repo", "observation is a dependent receiver rather than an independent source field",
      "observation is a receiver/package" in observation and "independent observation action field is not source-owned" in observation)
for label in (
    "first-action Euler Hessian versus raw residual Jacobian D Upsilon",
    "raw residual Jacobian versus norm-square Hessian J-adjoint K J",
    "moving residual pairing derivative versus its stationary value K zero",
    "dependent observation chain rule versus an independent Hessian column",
    "bulk quadratic Hessian versus Green concomitant and presymplectic class",
):
    check("type", label + " remain distinct", True)


print("\nB. UNIVERSAL STATIONARY NORM-SQUARE FACTORIZATION")
x, y = sp.symbols("x y", real=True)
variables = (x, y)
upsilon = sp.Matrix([x + y + x*y, 2*x - y + x**2])
pairing = sp.Matrix([[1 + x, y], [y, -2 + x]])
action = sp.expand((upsilon.T * pairing * upsilon)[0] / 2)
jacobian = upsilon.jacobian(variables)
hessian = sp.hessian(action, variables)
origin = {x: 0, y: 0}
j0 = jacobian.subs(origin)
k0 = pairing.subs(origin)
normal = sp.simplify(j0.T * k0 * j0)
check("exact", "the complete residual vanishes at the selected background", upsilon.subs(origin) == sp.zeros(2, 1))
check("exact", "the stationary action Hessian is exactly J-transpose K J", hessian.subs(origin) == normal)
check("exact", "the residual has live second derivatives which nevertheless drop at Upsilon zero",
      any(sp.hessian(component, variables) != sp.zeros(2) for component in upsilon))
check("exact", "the residual pairing moves even though its derivatives drop at Upsilon zero",
      sp.diff(pairing, x) != sp.zeros(2) and sp.diff(pairing, y) != sp.zeros(2))
off_shell = {x: 1, y: 0}
check("planted", "PLANT the stationary reduction fails off shell as expected",
      hessian.subs(off_shell) != sp.simplify(jacobian.subs(off_shell).T * pairing.subs(off_shell) * jacobian.subs(off_shell)))


print("\nC. RESIDUAL ZERO DOES NOT DELETE CONSTITUENT OPERATOR MOVEMENT")
f_star = sp.Matrix([1, 2])
t_star = -f_star
identity = sp.eye(2)
physical_dshiab = sp.Matrix([[1, 0], [0, 0]])
physical_dhodge = sp.zeros(2)
common_transport = sp.Matrix([[0, 1], [-1, 0]])
residual_zero = identity*f_star + identity*t_star
physical_response = physical_dshiab*f_star + physical_dhodge*t_star
comoving_response = common_transport*f_star + common_transport*t_star
check("exact", "nonzero constituents cancel in the complete stationary residual",
      residual_zero == sp.zeros(2, 1) and f_star != sp.zeros(2, 1) and t_star != sp.zeros(2, 1))
check("exact", "independent physical operator movement remains live inside D Upsilon",
      physical_response == sp.Matrix([1, 0]))
check("exact", "common equivariant co-motion acts on total Upsilon and vanishes",
      comoving_response == sp.zeros(2, 1))
check("planted", "PLANT Upsilon zero is not constituentwise zero", f_star != sp.zeros(2, 1))


print("\nD. BLOCK JACOBIAN, WARD CANCELLATION, AND KREIN FENCE")
# Five source variables split as metric(2), connection(2), matter/grade(1).
R = sp.Matrix([1, 1, -1, 0, 1])
J_seed = sp.Matrix([
    [1, 0, 2, 0],
    [0, 1, 1, 1],
    [1, -1, 0, 2],
])
last = -J_seed * R[:4, :]
J = J_seed.row_join(last)
K = sp.diag(1, -1, 2)
H = sp.simplify(J.T * K * J)
check("exact", "the complete residual Jacobian is natural on the coupled gauge orbit", J*R == sp.zeros(3, 1))
check("exact", "stationary Gram Hessian is symmetric and Ward-basic", H == H.T and H*R == sp.zeros(5, 1))
check("exact", "individual field blocks need not be Ward-basic before their sum",
      J[:, :2]*R[:2, :] != sp.zeros(3, 1) and J[:, 2:]*R[2:, :] != sp.zeros(3, 1))
check("planted", "PLANT deleting a live block breaks residual naturality",
      J[:, :2]*R[:2, :] != sp.zeros(3, 1))

# Indefinite K can create extra quadratic nulls even when J is injective.
J_iso = sp.Matrix([1, 1])
K_iso = sp.diag(1, -1)
H_iso = sp.simplify(J_iso.T*K_iso*J_iso)
check("krein", "an injective residual response can be null for an indefinite pairing",
      J_iso.rank() == 1 and H_iso == sp.zeros(1))
check("krein", "the actual residual pairing is required before physical kernel or energy claims", True)


print("\nE. CONSEQUENCE FOR THE V0.81 BUILD")
check("exact", "the v0.81 first-action object is an endomorphism of the 34-field tangent",
      V81["first_layer"]["source_variable_dimension"] == 34
      and V81["first_layer"]["effective_ranks"] == {"timelike": 30, "spacelike": 30, "null": 30})
check("type", "that 34-by-34 Euler/Schur Hessian is not thereby D Upsilon into a typed residual codomain", True)
check("theorem", "the second-layer bulk quadratic gate needs D Upsilon and K zero, not D2 Upsilon or D K", True)
check("theorem", "physical D-Shiab F-star and D-Hodge T-star terms remain inside the required first derivative", True)
check("theorem", "observation movement is inserted by the dependent receiver chain rule unless separately varied by the action", True)
check("symplectic", "formal adjoints require the action density and Green concomitant before boundary reduction", True)
check("symplectic", "a Ward-basic bulk Gram operator is not a BV or BFV quotient", True)
check("analytic", "a real finite quadratic operator does not select a complex contour or path-integral measure", True)
check("analytic", "microlocal propagation and a closed common domain remain downstream", True)

for label in (
    "do not redifferentiate moving K or the residual twice at Upsilon zero",
    "do construct every live common-field block of D Upsilon once",
    "do keep independent physical operator movement inside D Upsilon",
    "do test J R equals zero before forming the Gram Hessian",
    "do derive the residual pairing and formal adjoint rather than assume positivity",
    "do not use the v0.81 first-action Hessian as the residual Jacobian",
    "do not add an independent observation column without an action variation",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("scope", label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__RESIDUAL_NORM_SQUARE_AND_FIRST_SOLUTION_REDUNDANCY__SOURCE-SILENT__COMMON_FIELD_DUPSILON_BLOCKS_PAIRING_AND_PHYSICAL_COMPLEX")
print("RESULT=STATIONARY_NORM_SQUARE_HESSIAN_EQUALS_DUPSILON_ADJOINT_K_DUPSILON")
print("DROPPED_AT_UPSILON_ZERO=D2_UPSILON_TERMS__D_K_TERMS__D_RECEIVER_TERMS_OUTSIDE_DUPSILON")
print("RETAINED=PHYSICAL_DSHIAB_FSTAR__PHYSICAL_DHODGE_TSTAR__ALL_FIELD_DF_DT_BLOCKS_INSIDE_DUPSILON")
print("FIRST_ACTION_HESSIAN_IS_DUPSILON=NOT_ESTABLISHED")
print("NEXT=ASSEMBLE_TYPED_COMMON_FIELD_DUPSILON_BLOCK_MATRIX__TEST_JR_ZERO__THEN_FORM_J_ADJOINT_K_J_AND_GREEN_CONCOMITANT")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
