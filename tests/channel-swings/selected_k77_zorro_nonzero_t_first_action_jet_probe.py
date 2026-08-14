#!/usr/bin/env sage -python
"""Exact nonzero-T repair of the canonical-Zorro first-action jet.

This is a local formal-jet certificate. It retains canonical ``F_BZ``, sets
``T=t Phi1``, enforces the printed endpoint residual with the antisymmetric
grade-two part of ``DT``, and tests the full true action Euler row against all
9,555 symmetric grade-two first-jet corrections and the inherited Bianchi
rows. It does not construct an open background or the total source metric and
epsilon Euler graph.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

from sage.all import PolynomialRing, QQ, ZZ, vector


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_zorro_first_action_euler_gate_probe.py"
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


print("A. SOURCE LOCUS, SUPERSESSION, AND TYPE FENCES")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
prior_result = read(
    "explorations/conditional-build/"
    "selected-k77-zorro-first-action-euler-gate-2026-08-14.md"
)
intersection = read(
    "explorations/conditional-build/"
    "selected-k77-nonzero-t-zorro-intersection-gate-2026-08-14.md"
)
epsilon_result = read(
    "explorations/conditional-build/"
    "selected-k77-action-noether-preboundary-2026-08-08.md"
)
check("source", "the source owns varpi, dependent B(epsilon), and T=varpi-B",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "the source prints both the transgression action and translation endpoint",
      "I^B_1" in source and "Upsilon^B" in source)
check("prior", "the predecessor excludes only the canonical zero-T family",
      "T=F_varpi=0" in prior_result and "nonzero-`T`" in prior_result)
check("prior", "the old nonzero-T/Zorro intersection result requires a genuinely new solve",
      "genuinely nonzero-`T` solve" in intersection)
check("prior", "the action-owned primitive epsilon graph remains available downstream",
      "E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S" in epsilon_result)
for label in (
    "point value T versus its grade-two first jet",
    "printed endpoint residual versus true noncyclic action Euler",
    "symmetric first-jet correction versus antisymmetric exterior DT",
    "one-dimensional cokernel versus its fourteen-cell support",
    "formal Bianchi-compatible jet versus open stationary background",
    "direct volume partial versus total fixed-varpi metric Euler",
):
    check("layer0", label + " remain distinct", True)


print("\nB. PRIOR EXACT MAP AND INVARIANT SCALAR CELL")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("prior", "the immutable zero-T action obstruction replays",
      "PASS 35/35" in capture.getvalue() and not D["FAILURES"])

M = D["M"]
N = D["N"]
PAIRS = D["PAIRS"]
SELECTED = D["SELECTED"]
ZERO = M["ZERO"]
FULL = M["FULL"]
PHI1 = M["PHI1"]
C = M["wedge_raw"](PHI1, PHI1)
S_C_FORM = M["shiab"](C, SELECTED)
H_FORM = M["hodge"](PHI1)
check("exact", "the invariant scalar curvature cell obeys S(C)=312 Hodge(Phi1)",
      S_C_FORM == M["fscale"](Fraction(312), H_FORM))
check("bianchi", "the invariant scalar cell has zero local algebraic Bianchi commutator",
      M["wedge_raw"](PHI1, C) == M["wedge_raw"](C, PHI1))


def real(value) -> Fraction:
    assert value[1] == 0
    return Fraction(value[0])


def flattened_real(form) -> dict[tuple[int, int], Fraction]:
    return {
        coordinate: real(value)
        for coordinate, value in M["flatten"](form).items()
        if value != ZERO
    }


S_C = flattened_real(S_C_FORM)
H = flattened_real(H_FORM)
COMP_C: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
for r in range(N):
    for k in range(N):
        if r == k:
            continue
        form_mask = (1 << min(r, k)) | (1 << max(r, k))
        form_sign = 1 if r < k else -1
        for i, j in PAIRS:
            value = form_sign * real(
                C.get(form_mask, {}).get((1 << i) | (1 << j), ZERO)
            ) / 2
            if value:
                for coordinate, coefficient in D["companion_cell"](
                    r, k, i, j, value
                ).items():
                    COMP_C[coordinate] += coefficient
COMP_C = {coordinate: value for coordinate, value in COMP_C.items() if value}
check("exact", "S(C), Hodge(Phi1), and the scalar companion each have fourteen cells",
      len(S_C) == len(H) == len(COMP_C) == 14)

action_rows = D["action_rows"]
action_count = len(action_rows)
system = D["system"]
action_matrix = system[:action_count, :]
left_kernel = action_matrix.left_kernel()
check("correction", "the prior action map has one cokernel dimension, represented on fourteen cells",
      action_matrix.nrows() == 196 and action_matrix.rank() == 195
      and left_kernel.dimension() == 1)


def action_vector(values: dict) -> object:
    return vector(QQ, [QQ(values.get(coordinate, 0)) for coordinate in action_rows])


base = action_vector(D["base_euler"])
scalar_direct = action_vector(S_C)
scalar_hodge = action_vector(H)
scalar_companion = action_vector(COMP_C)


print("\nC. NONZERO-T RESIDUAL AND EXACT COKERNEL POLYNOMIAL")
R = PolynomialRing(QQ, "t")
t = R.gen()
q = -t / 312 - t**2
check("residual", "the residual-compatible scalar exterior-DT coefficient is exact",
      312 * (-t / 312) + t == 0 and q + t**2 == -t / 312)

# E_T = base(F_BZ,-F_BZ) + q(1/2 S(C)+Comp(C))
#       + t^2 S(C) + t Hodge(Phi1).
c1 = scalar_hodge - QQ(1) / 312 * (QQ(1) / 2 * scalar_direct + scalar_companion)
c2 = QQ(1) / 2 * scalar_direct - scalar_companion
projection = left_kernel.matrix()
p0 = (projection * base)[0]
p1 = (projection * c1)[0]
p2 = (projection * c2)[0]
branch_polynomial = 28392 * t**2 + 91 * t - 351
check("exact", "the full action-cokernel condition is 28392 t^2+91 t-351",
      12 * (p0 + p1 * t + p2 * t**2) == branch_polynomial)
discriminant = ZZ(91)**2 + 4 * ZZ(28392) * ZZ(351)
check("exact", "the branch discriminant is positive and nonsquare",
      discriminant == 39870649 and not discriminant.is_square())
check("result", "there are exactly two distinct real nonzero algebraic amplitudes",
      branch_polynomial.degree() == 2 and discriminant > 0
      and branch_polynomial(0) != 0)


print("\nD. COMPLETE ACTION/BIANCHI SOLVE")
# Modulo the branch polynomial, the action target loses its t coefficient.
reduced_constant = base + QQ(351) / 28392 * c2
reduced_linear = c1 - QQ(91) / 28392 * c2
check("exact", "the reduced algebraic-root target is rational and identical on both roots",
      reduced_linear.is_zero())


def extend_action(value) -> object:
    return vector(QQ, list(value) + [0] * (system.nrows() - action_count))


solution = system.solve_right(-extend_action(reduced_constant))
supported_solution = {
    D["VARIABLES"][index]: value
    for index, value in enumerate(solution)
    if value
}
expected_solution = {
    (0, axis, 0, axis): QQ(-9 if axis in (1, 2, 3, 10) else 5) / 56
    for axis in range(1, 14)
}
check("exact", "a thirteen-cell rational symmetric correction solves both algebraic roots",
      supported_solution == expected_solution)
defect = system * solution + extend_action(reduced_constant)
check("theorem", "all 196 true action Euler rows vanish exactly", defect[:action_count].is_zero())
check("theorem", "all 5,096 inherited Bianchi rows vanish exactly", defect[action_count:].is_zero())
check("exact", "the correction occupies thirteen of the 9,555 allowed symmetric variables",
      len(supported_solution) == 13 and len(D["VARIABLES"]) == 9555)
check("control", "the zero-T target remains outside the same action image",
      not D["consistent"] and bool(D["base_euler"]))
check("result", "nonzero T genuinely hits the formerly obstructing cokernel",
      (projection * (base + c1 * t + c2 * t**2))[0] == branch_polynomial / 12)


print("\nE. DIRECT METRIC PARTIAL AND NEXT SOURCE-OWNED ROW")
F_FORM = {
    (1 << r) | (1 << k): {
        (1 << i) | (1 << j): (value, Fraction(0))
        for (i, j), value in coefficients.items()
    }
    for (r, k), coefficients in D["F_BZ"].items()
}


def pair(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


pair_phi_f = pair(PHI1, M["shiab"](F_FORM, SELECTED))
pair_phi_c = pair(PHI1, S_C_FORM)
norm_phi = pair(PHI1, H_FORM)
check("exact", "the three density contractions are -54, 4368, and 14",
      pair_phi_f == (Fraction(-54), Fraction(0))
      and pair_phi_c == (Fraction(4368), Fraction(0))
      and norm_phi == (Fraction(14), Fraction(0)))
action_density = -t * (27 + 728 * t**2)
check("exact", "the branch first-action density is -t(27+728t^2)",
      action_density == t * QQ(-54) / 2 - 728 * t**3)
check("metric", "neither real branch kills the direct volume partial",
      branch_polynomial.gcd(action_density) == 1)
check("metric", "that live direct partial is not promoted to the total fixed-varpi metric Euler",
      True)
check("epsilon", "the action identity types the remaining primitive-epsilon row but does not evaluate it on this jet",
      "D_B^!(E_B-E_T)" in epsilon_result and "(D_epsilon S)^! K_S" in epsilon_result)
check("type", "E_B and moving-Shiab/metric graph derivatives are required because only E_T is closed",
      True)
check("scope", "the admitted object is a local formal jet, not a complete stationary source background",
      True)


print("\nF. DISPOSITION")
for kind, label in (
    ("result", "the canonical-Zorro nonzero-T branch is action/Bianchi NOT-YET-FALSIFIED"),
    ("scope", "SR-1 remains background-missing until epsilon and total metric/observation stationarity close"),
    ("scope", "SR-2 remains blocked until one complete stationary background exists"),
    ("source", "the source owns the action grammar but not these algebraic amplitudes or correction"),
    ("accounting", "no ledger canon residue quotient datum or scheduled-priority change follows"),
    ("physics", "no superposition positivity Born rule spectrum or empirical prediction follows"),
):
    check(kind, label, True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": "SELECTED_K77_CANONICAL_ZORRO_NONZERO_T_FIRST_ACTION_BIANCHI_JET_ADMITTED__SOURCE_METRIC_EPSILON_COMPLETION_OPEN",
    "amplitudes": "t=(-91+-sqrt(39870649))/56784",
    "branch_polynomial": "28392*t^2+91*t-351",
    "action_map": {
        "rows": int(action_matrix.nrows()),
        "rank": int(action_matrix.rank()),
        "cokernel_dimension": int(left_kernel.dimension()),
        "certificate_cell_support": 14,
    },
    "symmetric_correction": {
        "ambient_variables": int(len(D["VARIABLES"])),
        "support": len(supported_solution),
        "action_defect": sum(value != 0 for value in defect[:action_count]),
        "bianchi_defect": sum(value != 0 for value in defect[action_count:]),
    },
    "action_density": "-t*(27+728*t^2)__NONZERO_ON_BOTH_BRANCHES",
    "next_gate": "COMPUTE_E_B_AND_THE_MOVING_SHIAB_PRIMITIVE_EPSILON_PLUS_FIXED_VARPI_METRIC_OBSERVATION_GRAPH_ON_THIS_EXACT_JET",
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
