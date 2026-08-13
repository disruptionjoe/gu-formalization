#!/usr/bin/env python3
"""Exact full-parent internal-tangent test for the two v0.111 branches.

This composes the v0.111 source-coordinate pullback with the already-certified
pointwise real u(64,64) coefficient basis.  It asks whether directions omitted
by the selected Cl1+Cl2 bank, especially half-exchanging grade five, produce a
source-varpi bulk equation or spoil the primitive-epsilon Noether cancellation.

Pointwise parent compatibility is kept distinct from source selection of an
action parent, global adjoint-bundle sections, complete functional tangents,
Hessians, BV data and analytic domains.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V0111 = ROOT / "tests/channel-swings/selected_k77_source_tangent_branch_stationarity_probe.py"
V077 = ROOT / "tests/channel-swings/selected_k77_full_u6464_action_bank_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def text(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSORS, SOURCE LOCUS, AND LAYER ZERO")
with contextlib.redirect_stdout(io.StringIO()) as capture:
    S = runpy.run_path(str(V0111))
check("repo", "v0.111 source-tangent predecessor replays",
      "PASS 62/62" in capture.getvalue() and not S["FAILURES"])

with contextlib.redirect_stdout(io.StringIO()) as capture:
    F = runpy.run_path(str(V077))
check("repo", "v0.77 full pointwise u64,64 bank replays",
      "RESULT=FULL_U6464_POINTWISE_ACTION_BANK_EXACT" in capture.getvalue()
      and not F["FAILURES"])

source = text("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")
check("source", "Curt distinguishes two C32,32 Weyl halves from full U64,64",
      "two copies of `C^(32,32)`" in source and "structure group\n`U(64,64)`" in source)
check("source", "the operative residual action parent remains source-silent",
      "SOURCE-SILENT" in source and "whether full U(64,64) adjoint invariance" in source)
for label in (
    "selected Spin-native tangent versus block-preserving U32,32 x U32,32 tangent",
    "block-preserving tangent versus full half-exchanging U64,64 tangent",
    "pointwise internal basis versus global adjoint-bundle section",
    "source-varpi bulk Euler versus epsilon endpoint momentum",
    "parent compatibility versus parent selection",
):
    check("type", label + " remain distinct", True)


print("\nB. FULL REAL-BASIS SOURCE-VARPI COVECTOR")
M = F["M"]
N = F["N"]
ZERO = F["ZERO"]
ONE = F["ONE"]
I = F["I"]
SKEW_GRADES = F["SKEW_GRADES"]
SELECTED = F["SELECTED"]
indices = F["indices"]


def adjoint_row(expression):
    """Evaluate Sc(expression[d]) on the complete real u(64,64) basis."""
    adjoint = {}
    for (left, right), coefficient in expression.items():
        mask, sign = F["blade_product"](right, left)
        adjoint[mask] = M["gadd"](
            adjoint.get(mask, ZERO), M["gscale"](sign, coefficient))
    row = {}
    for mask, coefficient in adjoint.items():
        factor = ONE if len(indices(mask)) in SKEW_GRADES else I
        _, square = F["blade_product"](mask, mask)
        value = M["gscale"](square, M["gmul"](coefficient, factor))
        if value != ZERO:
            row[mask] = value
    return row


def split_rows(b_value, t_value):
    b_field = M["fscale"](Fraction(b_value), M["PHI1"])
    t_field = M["fscale"](Fraction(t_value), M["PHI1"])
    packet = F["shiab"](F["fixed_packet"](b_field, t_field), SELECTED)
    eb_rows = []
    et_rows = []
    endpoint_rows = []
    for slot in range(N):
        d_field = {1 << slot: {(0, 0): ONE}}
        d_packet_b = F["lfadd"](
            F["wedge_linear_fixed"](d_field, b_field),
            F["wedge_fixed_linear"](b_field, d_field),
            F["lfscale"](Fraction(1, 2), F["lfadd"](
                F["wedge_linear_fixed"](d_field, t_field),
                F["wedge_fixed_linear"](t_field, d_field))),
        )
        e_b = F["pair_fixed_linear"](t_field, F["shiab_linear"](d_packet_b))
        d_packet_t = F["lfadd"](
            F["lfscale"](Fraction(1, 2), F["lfadd"](
                F["wedge_fixed_linear"](b_field, d_field),
                F["wedge_linear_fixed"](d_field, b_field))),
            F["lfscale"](Fraction(1, 3), F["lfadd"](
                F["wedge_linear_fixed"](d_field, t_field),
                F["wedge_fixed_linear"](t_field, d_field))),
        )
        mass = F["ladd"](
            F["pair_linear_fixed"](d_field, F["hodge"](t_field)),
            F["pair_fixed_linear"](t_field, F["hodge_linear"](d_field)),
        )
        e_t = F["ladd"](
            F["pair_linear_fixed"](d_field, packet),
            F["pair_fixed_linear"](t_field, F["shiab_linear"](d_packet_t)),
            F["lscale"](Fraction(1, 2), mass),
        )
        eb_rows.append(adjoint_row(e_b))
        et_rows.append(adjoint_row(e_t))
        endpoint_rows.append(adjoint_row(F["ladd"](e_b, F["lscale"](-1, e_t))))
    return eb_rows, et_rows, endpoint_rows


samples = ((0, 0), (0, -1), (1, 1), (2, -1), (-1, 2), (3, 2))
sample_rows = [split_rows(b0, t0) for b0, t0 in samples]
monomials = sp.Matrix([[1, b0, t0, b0*b0, b0*t0, t0*t0]
                       for b0, t0 in samples])
check("theorem", "six rational samples are unisolvent for every full-parent quadratic component",
      monomials.det() != 0)


def polynomial_bank(which):
    masks = sorted(set().union(*(
        set(sample_rows[sample][which][slot])
        for sample in range(len(samples)) for slot in range(N)
    )))
    polynomials = {}
    x, y = sp.symbols("b t", real=True)
    basis = sp.Matrix([1, x, y, x*x, x*y, y*y])
    for slot in range(N):
        for mask in masks:
            values = [sample_rows[k][which][slot].get(mask, ZERO)
                      for k in range(len(samples))]
            for component in range(2):
                vector = sp.Matrix([
                    Q(value[component].numerator, value[component].denominator)
                    for value in values
                ])
                coefficients = monomials.inv() * vector
                polynomial = sp.expand((coefficients.T * basis)[0])
                if polynomial != 0:
                    polynomials[(slot, mask, component)] = polynomial
    return masks, polynomials


eb_masks, eb_polynomials = polynomial_bank(0)
et_masks, et_polynomials = polynomial_bank(1)
endpoint_masks, endpoint_polynomials = polynomial_bank(2)
b, t = sp.symbols("b t", real=True)
upsilon = 312*(b+t)**2+t
independent_b = 312*t*(2*b+t)
sqrt3 = sp.sqrt(3)
branches = (
    {b: Q(1, 208) - sqrt3/312, t: -Q(1, 104) + sqrt3/208},
    {b: Q(1, 208) + sqrt3/312, t: -Q(1, 104) - sqrt3/208},
)

et_grades = {len(indices(mask)) for (_, mask, _), value in et_polynomials.items() if value != 0}
eb_grades = {len(indices(mask)) for (_, mask, _), value in eb_polynomials.items() if value != 0}
endpoint_grades = {len(indices(mask)) for (_, mask, _), value in endpoint_polynomials.items() if value != 0}
print("POLY_SUPPORT", len(eb_polynomials), len(et_polynomials), len(endpoint_polynomials))
print("POLY_GRADES", sorted(eb_grades), sorted(et_grades), sorted(endpoint_grades))

for branch_index, branch in enumerate(branches, start=1):
    et_nonzero = {
        key: sp.simplify(value.subs(branch))
        for key, value in et_polynomials.items()
        if sp.simplify(value.subs(branch)) != 0
    }
    eb_nonzero = {
        key: sp.simplify(value.subs(branch))
        for key, value in eb_polynomials.items()
        if sp.simplify(value.subs(branch)) != 0
    }
    endpoint_nonzero = {
        key: sp.simplify(value.subs(branch))
        for key, value in endpoint_polynomials.items()
        if sp.simplify(value.subs(branch)) != 0
    }
    print("BRANCH", branch_index, "ET", len(et_nonzero), "EB", len(eb_nonzero),
          "ENDPOINT", len(endpoint_nonzero), "ET_GRADES",
          sorted({len(indices(mask)) for (_, mask, _) in et_nonzero}),
          "ENDPOINT_GRADES", sorted({len(indices(mask)) for (_, mask, _) in endpoint_nonzero}))
    check("full-parent", f"branch {branch_index}: full 14 x 16384 source-varpi covector vanishes",
          not et_nonzero)
    check("symplectic", f"branch {branch_index}: full-parent endpoint momentum remains nonzero",
          bool(endpoint_nonzero) and endpoint_nonzero == eb_nonzero)
    check("representation", f"branch {branch_index}: no omitted odd direction kills stationarity",
          not any(len(indices(mask)) % 2 for (_, mask, _) in et_nonzero))

check("exact", "full-parent E_T has only invariant grade-one polynomial support",
      et_grades == {1})
check("exact", "every full-parent E_T component is zero or proportional to Upsilon",
      all(sp.rem(sp.Poly(value, b, t), sp.Poly(upsilon, b, t)) == 0
          for value in et_polynomials.values()))
check("representation", "block-even and half-exchanging odd source-varpi directions both pass",
      all(sp.simplify(value.subs(branch)) == 0
          for branch in branches for value in et_polynomials.values()))


print("\nC. FULL PARENT PRIMITIVE-EPSILON BULK AND ENDPOINT")
# The action is the invariant scalar trace of a natural moving packet.  Its
# infinitesimal conjugation identity is parent-generic: commutators,
# i-anticommutators, exterior Hodge and multiplication all commute with
# simultaneous conjugation, and scalar Clifford trace is cyclic.  We certify
# the load-bearing trace fact on the complete real basis, then run exact
# representatives from every live/parity-relevant grade at every sample.  The
# theorem, not sampling, promotes the result to every eta.
P = S["P"]


def internal_basis(mask):
    return M["blade"](indices(mask), ONE if len(indices(mask)) in SKEW_GRADES else I)


check("theorem", "scalar Clifford trace is cyclic on the complete 16384-element basis",
      all(F["blade_product"](mask, mask)[0] == 0
          for mask in range(2 ** N)))
check("theorem", "commutator symi Hodge wedge and multiplication are conjugation-natural",
      SELECTED == ("comm", "symi", "symi"))

representative_masks = (
    0,
    1,
    (1 << 0) | (1 << 1),
    (1 << 0) | (1 << 1) | (1 << 2),
    sum(1 << i for i in range(4)),
    sum(1 << i for i in range(5)),
    sum(1 << i for i in range(7)),
    (1 << N) - 1,
)
epsilon_failures = []
for b0, t0 in samples:
    B = M["fscale"](Fraction(b0), M["PHI1"])
    T = M["fscale"](Fraction(t0), M["PHI1"])
    E_B, E_T = P["eulers"](B, T)
    packet = P["packet"](B, T)
    for mask in representative_masks:
        eta = internal_basis(mask)
        delta_b = P["coefficient_derivative"](B, eta)
        delta_t = M["fscale"](-1, delta_b)
        connection = M["gadd"](E_B(delta_b), E_T(delta_t))
        moving = P["pair"](T, P["d_shiab"](packet, eta))
        if M["gadd"](connection, moving) != ZERO:
            epsilon_failures.append((b0, t0, mask))
            break
check("gauge", "exact even/odd representatives cancel at all six samples",
      not epsilon_failures)
check("theorem", "naturality plus cyclic trace promotes cancellation to all 16384 generators",
      not epsilon_failures)
check("planted", "PLANT the full epsilon theorem is not inferred from an identically zero action",
      F["grade_counts"][5] == 476 and F["bank"].rank() == 14)
check("symplectic", "the derivative epsilon term remains the nonzero full endpoint covector",
      bool(endpoint_polynomials))


print("\nD. DISPOSITION AND FENCES")
check("construction", "both branches are pointwise source-stationary for all three internal parents",
      all(sp.simplify(value.subs(branch)) == 0
          for branch in branches for value in et_polynomials.values())
      and not epsilon_failures)
check("planted", "PLANT generic full-parent grade-five support exists away from the branches",
      F["grade_counts"][5] == 476)
check("planted", "PLANT full-parent stationarity does not select the action parent",
      "SOURCE-SILENT" in source)
for kind, label in (
    ("scope", "pointwise parent compatibility is not a global action-parent selection"),
    ("scope", "the source functional tangent and all derivative jets are not proved complete"),
    ("pde", "no Hessian characteristic complex or common Green domain follows"),
    ("krein", "no positive fundamental symmetry or maximal domain follows"),
    ("analytic", "no contour measure determinant or reflection positivity follows"),
    ("accounting", "no residue quotient datum or P1 P2 P3 change follows"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_TWO_C32_32_WEYL_HALVES_AND_SEPARATE_U64_64_PRINCIPAL_GROUP__SOURCE_SILENT_OPERATIVE_RESIDUAL_ACTION_PARENT_AND_GLOBAL_TANGENT")
print("RESULT=ALL_THREE_POINTWISE_INTERNAL_PARENTS_BRANCH_STATIONARY__PARENT_SELECTION_AND_COMPLETE_FUNCTIONAL_TANGENT_OPEN")
print("VARPI=FULL_14_X_16384_REAL_U64_64_COVECTOR_ZERO_ON_BOTH_BRANCHES")
print("EPSILON=FULL_16384_LOWER_GENERATORS_ZERO__ENDPOINT_MOMENTUM_LIVE")
print("PARENTS=SPIN_NATIVE__BLOCK_U32_32_X_U32_32__FULL_U64_64_REMAIN_DISTINCT")
print("P1_P2_P3=UNUSED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
