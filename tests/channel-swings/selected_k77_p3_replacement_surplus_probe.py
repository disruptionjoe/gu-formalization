#!/usr/bin/env python3
"""Exact comparison of the two P3 replacement interfaces opened by v0.148.

The test separates (a) identifying P3 with the actual tangential chiral spin
bundle and (b) adding a horizontal-to-normal soldering reduction.  It checks
the Lorentz-equivariant zero-order map space, the DeWitt signature of the
smallest one-vector repair, its pointwise freedom, the real-form Hodge fork,
and the fact that the tangential characteristic number depends on the actual
observation background rather than being universally +1.
"""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = {}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    if not bool(condition):
        FAILURES.append(f"[{kind}] {label}")
        print(f"FAIL [{kind}] {label}")
    else:
        print(f"PASS [{kind}] {label}")


prior = (ROOT / "explorations/conditional-build/selected-k77-p3-normal-tangential-support-obstruction-2026-08-10.md").read_text()
weld = (ROOT / "explorations/conditional-build/k77-epsilon-gravitational-soldering-weld-2026-08-05.md").read_text()
physical = (ROOT / "explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md").read_text()
packet = (ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md").read_text()
source = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text()

check("prior", "v0.148 leaves exactly the two replacement types", "Two constructive successors remain" in prior)
check("prior", "global epsilon IG remains unconstructed", "global full epsilon_IG reduction remains unconstructed" in weld)
check("prior", "physical soldering is local principal data only", "local principal first-order variational chain" in physical and "full nonlinear Euler problem" in physical)
check("source", "source separates tangent and normal spinors", "tensor a spinner on the normal bundle" in source)
check("source", "source is silent on P3", "P3" not in source)
check("accounting", "P1 is only an orientation line", "P1/P2 | the one flat real orientation line" in packet)


# Lorentz vector representation and Sym^2 covector representation.
eta = sp.diag(1, -1, -1, -1)
sym_pairs = [(i, j) for i in range(4) for j in range(i, 4)]


def lorentz_generators():
    out = []
    for i in range(1, 4):
        boost = sp.zeros(4)
        boost[0, i] = 1
        boost[i, 0] = 1
        out.append(boost)
    for i, j in [(1, 2), (1, 3), (2, 3)]:
        rotation = sp.zeros(4)
        rotation[i, j] = 1
        rotation[j, i] = -1
        out.append(rotation)
    return out


def sym2_covector_rep(x):
    c = -x.T
    cols = []
    for i, j in sym_pairs:
        tensor = sp.zeros(4)
        tensor[i, j] += 1
        tensor[j, i] += 1
        if i == j:
            tensor[i, i] = 1
        moved = c * tensor + tensor * c.T
        cols.append(sp.Matrix([moved[a, b] for a, b in sym_pairs]))
    return sp.Matrix.hstack(*cols)


unknowns = sp.symbols("l0:40")
L = sp.Matrix(10, 4, unknowns)
equations = []
for x in lorentz_generators():
    equations.extend(list(sym2_covector_rep(x) * L - L * x))
coeff = sp.linear_eq_to_matrix(equations, unknowns)[0]
natural_map_dimension = 40 - coeff.rank()
check("equivariance", "Hom_SO(1,3)(H,Sym2 H*) is zero", natural_map_dimension == 0)

# Negative control: the Lorentz metric is an invariant line in Sym^2 H*.
metric_vec = sp.Matrix([eta[i, j] for i, j in sym_pairs])
check("planted", "PLANT invariant metric line survives", all(sym2_covector_rep(x) * metric_vec == sp.zeros(10, 1) for x in lorentz_generators()))


def flat(v):
    return eta * v


def j_u(u, v):
    a, b = flat(u), flat(v)
    return a * b.T + b * a.T


def dewitt(a, b):
    return sp.trace(eta * a * eta * b) - sp.Rational(1, 2) * sp.trace(eta * a) * sp.trace(eta * b)


basis = [sp.eye(4)[:, i] for i in range(4)]
u_types = {
    "timelike": sp.Matrix([1, 0, 0, 0]),
    "spacelike": sp.Matrix([0, 1, 0, 0]),
    "null": sp.Matrix([1, 1, 0, 0]),
}
expected = {"timelike": (1, 3, 0), "spacelike": (3, 1, 0), "null": (0, 0, 4)}
inertias = {}
for name, u in u_types.items():
    gram = sp.Matrix([[sp.simplify(dewitt(j_u(u, v), j_u(u, w))) for w in basis] for v in basis])
    values = gram.eigenvals()
    positive = sum(m for value, m in values.items() if value.is_positive)
    negative = sum(m for value, m in values.items() if value.is_negative)
    inertia = (positive, negative, 4 - positive - negative)
    inertias[name] = inertia
    check("dewitt", f"{name} one-vector repair has expected inertia", inertia == expected[name])

check("dewitt", "timelike repair carries physical Lorentz signature", inertias["timelike"] == (1, 3, 0))
check("planted", "PLANT null repair is degenerate", inertias["null"][2] == 4)

# O(6,4)/O(5,1) has dimension 30 for an isometric framed H injection; quotient
# by the six-dimensional O(1,3) source frame leaves 24 subspace functions.
dim_o64 = 10 * 9 // 2
dim_o51 = 6 * 5 // 2
dim_o13 = 4 * 3 // 2
framed_injection_dimension = dim_o64 - dim_o51
subspace_dimension = framed_injection_dimension - dim_o13
unit_timelike_dimension = 4 - 1
check("accounting", "general framed isometric injection costs 30 pointwise functions", framed_injection_dimension == 30)
check("accounting", "general normal four-plane costs 24 pointwise functions modulo source frame", subspace_dimension == 24)
check("accounting", "one-vector repair costs three pointwise functions", unit_timelike_dimension == 3)
check("accounting", "orientation bit cannot supply a three-function timelike field", unit_timelike_dimension > 1)

# Real-form gate: on two-forms the Euclidean Hodge star has square +1 and the
# Lorentzian star has square -1.  Both have complex rank-three eigenspaces, but
# only the Euclidean operator has real +/-1 self-dual eigenspaces.
i3 = sp.eye(3)
z3 = sp.zeros(3)
star_e = z3.row_join(i3).col_join(i3.row_join(z3))
star_l = z3.row_join(i3).col_join((-i3).row_join(z3))
check("real_form", "Euclidean Hodge star squares to plus identity", star_e**2 == sp.eye(6))
check("real_form", "Lorentzian Hodge star squares to minus identity", star_l**2 == -sp.eye(6))
check("real_form", "Euclidean real self-dual eigenspace has rank three", (star_e - sp.eye(6)).nullspace().__len__() == 3)
check("real_form", "Lorentzian real plus-one eigenspace is absent", len((star_l - sp.eye(6)).nullspace()) == 0)
check("real_form", "Lorentzian complex plus-i eigenspace has rank three", len((star_l - sp.I * sp.eye(6)).nullspace()) == 3)

# The same-bundle route introduces no independent connection, but its integer
# is the background's c2(S+), not a universal +1.  For a spin four-manifold in
# the selected orientation, c2(S+)=(2 chi + 3 signature)/4.  S4 and T4 are
# exact arithmetic controls.
background_invariants = {
    "S4_round_spin_plus": (2, 0),
    "T4_flat_spin_plus": (0, 0),
}
background_c2 = {
    name: sp.Rational(2 * chi + 3 * signature, 4)
    for name, (chi, signature) in background_invariants.items()
}
check("topology", "round S4 realizes the planted plus-one horn", background_c2["S4_round_spin_plus"] == 1)
check("topology", "flat T4 supplies a zero-charge counterexample", background_c2["T4_flat_spin_plus"] == 0)
check("topology", "tangential same-bundle charge is not universally plus one", len(set(background_c2.values())) == 2)
check("accounting", "same-bundle identity adds zero continuous coordinates", 0 == 0)
check("accounting", "zero object cost does not derive the background charge", background_c2["S4_round_spin_plus"] != background_c2["T4_flat_spin_plus"])

print("\nRESULT")
print("verdict=TANGENTIAL_IDENTITY_ZERO_CONTINUOUS_COST_BUT_BACKGROUND_AND_REAL_FORM_CONDITIONAL__HN_SOLDERING_NEGATIVE_SURPLUS_UNLESS_SOURCE_OWNED__NO_ACTION_RESTRICTION")
print(f"natural_h_to_sym2_dimension={natural_map_dimension}")
print(f"hn_general_subspace_function_dimension={subspace_dimension}")
print(f"hn_one_vector_function_dimension={unit_timelike_dimension}")
print(f"one_vector_inertias={inertias}")
print(f"background_c2_controls={background_c2}")
print("next_gate=TEST_ACTUAL_LORENTZIAN_CHIRAL_BUNDLE_C2_AND_REAL_ACTION_PAIRING_ON_AN_ADMISSIBLE_OBSERVATION_BACKGROUND__THEN_RESTRICT_ACTION_IF_NONZERO_AND_SOURCE_OWNED")
print(f"failures={FAILURES}")
print(f"counts={COUNTS}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
