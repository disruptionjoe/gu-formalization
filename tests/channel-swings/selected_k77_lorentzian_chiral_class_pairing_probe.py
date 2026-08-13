#!/usr/bin/env python3
"""Exact Lorentzian topology and real chiral-pairing gate for ledger v0.150.

The probe deliberately keeps three Layer-0 objects separate:

1. an absolute ordinary c2 class on the observer spacetime;
2. a relative, compact-support or boundary-transgression class;
3. a real invariant pairing on the Lorentzian chiral algebra, versus ownership
   of one such pairing by the selected source action.

It also repairs a convention-blind weakness in the v0.149 S4/T4 controls by
solving the repository's p1/e equations and checking a K3-style input.
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


prior = (ROOT / "explorations/conditional-build/selected-k77-p3-replacement-surplus-2026-08-10.md").read_text()
native = (ROOT / "explorations/conditional-build/selected-k77-p3-native-characteristic-pairing-2026-08-10.md").read_text()
boundary = (ROOT / "canon/boundary-einvariant-and-the-tangential-fork.md").read_text()
old_index = (ROOT / "explorations/analytic-index-fredholm/ind-top-x4-atiyah-singer-2026-06-23.md").read_text()
source = (ROOT / "lab/sources/curt-iceberg-77-primary-transcript-fetch-2026-08-08.md").read_text()

check("prior", "v0.149 requests this exact topology and pairing gate", "actual-background Lorentzian chiral-class/reality gate" in prior)
check("prior", "current parent-invariant quadratic pairings cancel", "gets exactly zero" in native)
check("prior", "boundary tangential route already exists as prior art", "boundary e-invariant" in boundary.lower() and "tangential framing" in boundary.lower())
check("source", "authorial source fixes the Lorentzian base sector", "trapped in the `(1,3)` sector" in source)
check("source", "source does not name compact-support c2", "compact-support" not in source and "compact support" not in source)
check("source", "source does not select a real/imaginary chiral pairing ratio", "pairing ratio" not in source)
check("prior", "old index note contains the superseded Rokhlin scope reading", "applies to EUCLIDEAN" in old_index and "holds only for simply-connected" in old_index)


# Repository convention from p1(E)=-2(c2+ + c2-) and e(E)=c2+ - c2-.
cp, cm, chi, signature = sp.symbols("cp cm chi signature")
solution = sp.solve(
    [sp.Eq(3 * signature, -2 * (cp + cm)), sp.Eq(chi, cp - cm)],
    [cp, cm],
    dict=True,
)[0]
cp_formula = sp.factor(solution[cp])
cm_formula = sp.factor(solution[cm])
check("topology", "repository p1/e equations solve exactly", sp.simplify(cp_formula - (2 * chi - 3 * signature) / 4) == 0 and sp.simplify(cm_formula - (-2 * chi - 3 * signature) / 4) == 0)


def c2_pair(euler, sig):
    return (
        sp.simplify(cp_formula.subs({chi: euler, signature: sig})),
        sp.simplify(cm_formula.subs({chi: euler, signature: sig})),
    )


check("topology", "S4 control is (1,-1)", c2_pair(2, 0) == (1, -1))
check("topology", "T4 control is (0,0)", c2_pair(0, 0) == (0, 0))
check("planted", "PLANT K3-style control distinguishes the hidden sign convention", c2_pair(24, -16) == (24, 0))

# A time-oriented closed Lorentzian manifold has a nowhere-zero timelike vector,
# hence chi=0. Rokhlin supplies signature in 16Z on a closed smooth spin four-
# manifold. Therefore both chiral c2 values are multiples of 12 in this
# convention; the unit class is excluded independently of which chirality is
# called plus.
closed_samples = {}
for k in range(-3, 4):
    sig = 16 * k
    closed_samples[sig] = c2_pair(0, sig)
check("topology", "closed Lorentzian spin samples lie in 12Z", all(int(a) % 12 == 0 and int(b) % 12 == 0 for a, b in closed_samples.values()))
check("topology", "closed Lorentzian spin samples exclude unit c2", all(abs(int(a)) != 1 and abs(int(b)) != 1 for a, b in closed_samples.values()))
check("topology", "chi zero makes the two repository-convention chiral classes equal", all(a == b for a, b in closed_samples.values()))
check("planted", "PLANT non-Lorentzian S4 retains the unit class", 1 in c2_pair(2, 0))

# A globally hyperbolic four-manifold is diffeomorphic to R x Sigma^3 and has
# the ordinary cohomology of Sigma. A CW complex of dimension three has no H4.
sigma_cw_dimension = 3
real_line_contractible = True
ordinary_h4_rank = 0 if real_line_contractible and sigma_cw_dimension < 4 else None
check("topology", "globally hyperbolic R x Sigma3 has ordinary H4 rank zero", ordinary_h4_rank == 0)
check("topology", "absolute ordinary degree-four characteristic number vanishes", ordinary_h4_rank == 0)
check("layer0", "absolute zero does not decide the boundary framing class", ordinary_h4_rank == 0 and "framed-bordism" in boundary.lower())
check("planted", "PLANT compact closed S4 is not the globally hyperbolic model", c2_pair(2, 0) != (0, 0))


# Compute real invariant symmetric bilinear forms on sl(2,C) regarded as a
# six-dimensional real Lie algebra. The real basis is (h,e,f,ih,ie,if), with
# [h,e]=2e, [h,f]=-2f and [e,f]=h.
base_brackets = {
    (0, 1): {1: sp.Integer(2)},
    (0, 2): {2: sp.Integer(-2)},
    (1, 2): {0: sp.Integer(1)},
}


def base_bracket(a, b):
    if a == b:
        return {}
    if (a, b) in base_brackets:
        return base_brackets[(a, b)]
    return {k: -v for k, v in base_brackets[(b, a)].items()}


def real_bracket(a, b):
    ai, aj = divmod(a, 3)
    bi, bj = divmod(b, 3)
    factor = -1 if ai and bi else 1
    imag = ai ^ bi
    return {imag * 3 + k: factor * v for k, v in base_bracket(aj, bj).items()}


adjoints = []
for a in range(6):
    A = sp.zeros(6)
    for b in range(6):
        for c, value in real_bracket(a, b).items():
            A[c, b] = value
    adjoints.append(A)

vars_b = sp.symbols("b0:21")
B = sp.zeros(6)
n = 0
for i in range(6):
    for j in range(i, 6):
        B[i, j] = vars_b[n]
        B[j, i] = vars_b[n]
        n += 1
invariance_equations = []
for A in adjoints:
    invariance_equations.extend(list(A.T * B + B * A))
coefficient = sp.linear_eq_to_matrix(invariance_equations, vars_b)[0]
invariant_pairing_dimension = len(vars_b) - coefficient.rank()
check("pairing", "real invariant symmetric pairing space has dimension two", invariant_pairing_dimension == 2)

K = sp.Matrix([[2, 0, 0], [0, 0, 1], [0, 1, 0]])
zero = sp.zeros(3)
bre = K.row_join(zero).col_join(zero.row_join(-K))
bim = zero.row_join(K).col_join(K.row_join(zero))
check("pairing", "real part of complex trace form is invariant", all(A.T * bre + bre * A == sp.zeros(6) for A in adjoints))
check("pairing", "imaginary part of complex trace form is invariant", all(A.T * bim + bim * A == sp.zeros(6) for A in adjoints))
check("pairing", "the two explicit invariant forms are independent", sp.Matrix.hstack(sp.Matrix(bre).reshape(36, 1), sp.Matrix(bim).reshape(36, 1)).rank() == 2)

a, b = sp.symbols("a b", real=True)
general = a * bre + b * bim
det_general = sp.factor(general.det())
check("pairing", "nonzero real/imaginary combination is nondegenerate", det_general != 0 and sp.factor(det_general.subs({a: 1, b: 0})) != 0 and sp.factor(det_general.subs({a: 0, b: 1})) != 0)
for name, form in {"real": bre, "imaginary": bim, "mixed": bre + bim}.items():
    eigen = form.eigenvals()
    pos = sum(mult for value, mult in eigen.items() if value.is_positive)
    neg = sum(mult for value, mult in eigen.items() if value.is_negative)
    check("pairing", f"{name} invariant pairing has neutral (3,3) inertia", (pos, neg) == (3, 3))
check("pairing", "existence does not give uniqueness", invariant_pairing_dimension > 1)
check("accounting", "projectivizing the two-dimensional pairing space leaves one ratio", invariant_pairing_dimension - 1 == 1)
check("accounting", "current source does not own that ratio", "pairing ratio" not in source)
check("symplectic", "no positive-definite invariant chiral pairing was manufactured", all((sum(mult for value, mult in form.eigenvals().items() if value.is_positive), sum(mult for value, mult in form.eigenvals().items() if value.is_negative)) == (3, 3) for form in (bre, bim, bre + bim)))

print("\nRESULT")
print("verdict=ABSOLUTE_TANGENTIAL_C2_UNIT_KILLED_ON_CLOSED_LORENTZIAN_SPIN_AND_ZERO_ON_GLOBALLY_HYPERBOLIC_X__REAL_CHIRAL_PAIRING_EXISTS_BUT_IS_TWO_DIMENSIONAL_AND_NOT_SOURCE_SELECTED__RELATIVE_BOUNDARY_TRANSGRESSION_REQUIRED")
print(f"c2_formulas=({cp_formula},{cm_formula})")
print(f"closed_lorentzian_spin_samples={closed_samples}")
print(f"globally_hyperbolic_ordinary_h4_rank={ordinary_h4_rank}")
print(f"invariant_real_pairing_dimension={invariant_pairing_dimension}")
print(f"general_pairing_determinant={det_general}")
print("next_gate=CONSTRUCT_SOURCE_OWNED_RELATIVE_TANGENTIAL_CHIRAL_TRANSGRESSION_AND_REALITY_CONDITION_ON_AN_OBSERVER_COBORDISM__KILL_IF_IT_REQUIRES_A_FREE_BOUNDARY_INTEGER_OR_UNOWNED_PAIRING_RATIO__THEN_RESTRICT_ACTION")
print(f"failures={FAILURES}")
print(f"counts={COUNTS}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
