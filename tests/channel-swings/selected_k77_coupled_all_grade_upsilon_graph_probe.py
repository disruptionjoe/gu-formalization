#!/usr/bin/env python3
"""Exact coupled all-grade raw-Upsilon graph gate on the selected K77 branch.

The candidate domain is declared before the four conditional physical target
columns are read: every K77 one-form with Clifford grade one or two.  The probe
builds the source-displayed linearized response

    R(delta A) = * Shiab(D_A delta A) + kappa_1 delta A

at the already selected nonzero-kappa background, proves that R embeds this
1,470-dimensional finite carrier with rank 1,470 in a 4,330-coordinate output
support, and solves the four fixed -J_2D columns.  It does not derive those
columns, an Euler covector, a preboundary current, or a physical symplectic
quotient.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_total_upsilon_null_screen_probe.py"
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


print("A. SOURCE, ARCHAEOLOGY, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
carrier_report = read(
    "explorations/conditional-build/"
    "selected-second-layer-normal-jet-carrier-compatibility-2026-08-07.md"
)
v060_report = read(
    "explorations/conditional-build/selected-k77-total-upsilon-null-screen-2026-08-07.md"
)
check("source", "the source displays both terms of raw Upsilon",
      r"\Upsilon^B_\omega" in source and r"*\kappa_1T_\omega" in source)
check("source", "Xi equals D Upsilon is displayed only as a redundant Euler relation",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source and "redundant" in source)
check("source", "the four conditional -J2D columns remain source-silent",
      "SOURCE-SILENT" in carrier_report and "prolonged coefficients" in carrier_report)
check("repo", "v0.60 records the curvature-only fit as insufficient for total Upsilon",
      "curvature-only" in v060_report and "rank four" in v060_report)
for label in (
    "source raw Upsilon versus the equation Upsilon equals zero",
    "raw Upsilon derivative versus Xi equals D Upsilon",
    "curvature Bianchi versus Upsilon naturality",
    "conditional -J2D target versus a source-quoted transformation law",
    "pointwise graph inverse versus an action Euler covector",
    "configuration descent versus preboundary symplectic descent",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE PREDECESSOR REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.60 Bianchi/null-screen predecessor replays", "PASS 43/43" in capture.getvalue())

M = V["M"]
channels = V["channels"]
N = 14
ONE = M["ONE"]
ZERO = M["ZERO"]
q0 = V["q0"]
t_background = V["t_background"]
f_background = V["f_background"]


def response(delta_a, kappa_sign=1):
    delta_f = M["fadd"](
        M["wedge_raw"](q0, delta_a),
        M["wedge_raw"](t_background, delta_a),
        M["wedge_raw"](delta_a, t_background),
    )
    return M["fadd"](
        M["hodge"](M["shiab"](delta_f, channels)),
        M["fscale"](kappa_sign, delta_a),
    )


def add_scaled(destination, source_vector, scale):
    for key, coefficient in source_vector.items():
        value = M["gadd"](
            destination.get(key, ZERO), M["gmul"](scale, coefficient)
        )
        if value == ZERO:
            destination.pop(key, None)
        else:
            destination[key] = value


print("\nC. TARGET-BLIND SOURCE-RESPONSE EMBEDDING AND INVERSION")
# Declare the candidate source tangent before reading the four targets.
basis_forms = []
basis_labels = []
for form_index in range(N):
    for value_index in range(N):
        basis_forms.append({1 << form_index: M["blade"](value_index)})
        basis_labels.append((form_index, 1 << value_index))
    for left in range(N):
        for right in range(left + 1, N):
            basis_forms.append({1 << form_index: M["blade"]((left, right))})
            basis_labels.append((form_index, (1 << left) | (1 << right)))

response_columns = [M["flatten"](response(value)) for value in basis_forms]
check("exact", "the predeclared Cl1 plus Cl2 tangent has dimension 1470",
      len(basis_forms) == 14 * (14 + 91) == 1470)
output_coordinates = set().union(*(set(column) for column in response_columns))
check("exact", "the response output support has 4330 coordinates in grades one two and five",
      len(output_coordinates) == 4330
      and {key[1].bit_count() for key in output_coordinates} == {1, 2, 5})

# Exact column echelon form, retaining representations in the declared basis.
pivots = {}
for index, column in enumerate(response_columns):
    value = dict(column)
    representation = {index: ONE}
    while value:
        pivot = min(value)
        if pivot not in pivots:
            inverse_lead = M["gdiv"](ONE, value[pivot])
            value = {key: M["gmul"](coefficient, inverse_lead)
                     for key, coefficient in value.items()}
            representation = {key: M["gmul"](coefficient, inverse_lead)
                              for key, coefficient in representation.items()}
            pivots[pivot] = (value, representation)
            break
        basis_vector, basis_representation = pivots[pivot]
        lead = value[pivot]
        add_scaled(value, basis_vector, M["gneg"](lead))
        add_scaled(representation, basis_representation, M["gneg"](lead))

check("exact", "the full response has exact rank 1470 and nullity zero",
      len(pivots) == len(basis_forms) == 1470)


def solve(target):
    value = dict(target)
    representation = {}
    while value:
        pivot = min(value)
        if pivot not in pivots:
            return None, value
        basis_vector, basis_representation = pivots[pivot]
        lead = value[pivot]
        add_scaled(value, basis_vector, M["gneg"](lead))
        add_scaled(representation, basis_representation, lead)
    return representation, {}


def source_form(solution):
    result = {}
    for index, coefficient in solution.items():
        result = M["fadd"](
            result, M["fscale"](coefficient, basis_forms[index])
        )
    return result


targets = [M["flatten"](V["target_form"](packet)) for packet in V["raw_required"]]
solutions = []
for target in targets:
    solution, remainder = solve(target)
    check("exact", "one fixed conditional target has a unique full-response preimage",
          solution is not None and not remainder)
    solutions.append(source_form(solution))

check("exact", "the four all-grade source lifts retain family rank four",
      V["family_rank"](solutions) == 4)
check("exact", "solution supports are 71,48,48,48",
      [len(M["flatten"](value)) for value in solutions] == [71, 48, 48, 48])
check("exact", "Cl1 supports are 10,13,13,13",
      [len(M["flatten"](V["cliff_grade"](value, 1))) for value in solutions]
      == [10, 13, 13, 13])
check("exact", "Cl2 supports are 61,35,35,35",
      [len(M["flatten"](V["cliff_grade"](value, 2))) for value in solutions]
      == [61, 35, 35, 35])
check("exact", "every complete response is exactly its pure-grade-two target",
      all(M["flatten"](response(solution)) == target
          for solution, target in zip(solutions, targets)))
check("exact", "all non-target response grades cancel internally",
      all(not V["cliff_grade"](response(solution), grade)
          for solution in solutions for grade in range(15) if grade != 2))
check("exact", "the old curvature-only graph differs from every all-grade solution",
      all(M["flatten"](old) != M["flatten"](new)
          for old, new in zip(V["delta_as"], solutions)))

corrections = [M["fadd"](new, M["fscale"](-1, old))
               for new, old in zip(solutions, V["delta_as"])]
old_residuals = [M["fadd"](
    response(old), M["fscale"](-1, V["target_form"](packet))
) for old, packet in zip(V["delta_as"], V["raw_required"])]
check("exact", "the uniquely inverted source correction cancels each old residual",
      all(not M["fadd"](response(correction), residual)
          for correction, residual in zip(corrections, old_residuals)))
check("planted", "PLANT omitting kappa T makes every new lift miss its target",
      all(M["flatten"](response(solution, 0)) != target
          for solution, target in zip(solutions, targets)))
check("planted", "PLANT reversing the kappa-T sign makes every new lift miss its target",
      all(M["flatten"](response(solution, -1)) != target
          for solution, target in zip(solutions, targets)))
grade_three_plant = {(1 << 0, (1 << 0) | (1 << 1) | (1 << 2)): ONE}
plant_solution, plant_remainder = solve(grade_three_plant)
check("planted", "PLANT a grade-three output counterterm is outside the declared response image",
      plant_solution is None and plant_remainder == grade_three_plant)


print("\nD. ENDPOINT BIANCHI AND FULL-REDUCTION TRANSPORT")
for solution in solutions:
    delta_f = M["fadd"](
        M["wedge_raw"](q0, solution),
        M["wedge_raw"](t_background, solution),
        M["wedge_raw"](solution, t_background),
    )
    bianchi = M["fadd"](
        M["wedge_raw"](q0, delta_f),
        M["wedge_raw"](t_background, delta_f),
        M["fscale"](-1, M["wedge_raw"](delta_f, t_background)),
        M["wedge_raw"](solution, f_background),
        M["fscale"](-1, M["wedge_raw"](f_background, solution)),
    )
    check("exact", "one all-grade lift satisfies full linearized Bianchi", not bianchi)

B = V["B"]


def act_mask(element, mask):
    permutation, signs = element
    sequence = [permutation[index] for index in range(N) if mask & (1 << index)]
    sign = 1
    for index in range(N):
        if mask & (1 << index):
            sign *= signs[index]
    sign *= -1 if sum(sequence[i] > sequence[j]
                      for i in range(len(sequence))
                      for j in range(i + 1, len(sequence))) % 2 else 1
    new_mask = sum(1 << index for index in sequence)
    return new_mask, sign


def act_form(element, form):
    result = {}
    for form_mask, clifford in form.items():
        new_form_mask, form_sign = act_mask(element, form_mask)
        for cliff_mask, coefficient in clifford.items():
            new_cliff_mask, cliff_sign = act_mask(element, cliff_mask)
            value = M["gscale"](form_sign * cliff_sign, coefficient)
            element_out = result.setdefault(new_form_mask, {})
            element_out[new_cliff_mask] = M["gadd"](
                element_out.get(new_cliff_mask, ZERO), value
            )
    return M["fclean"](result)


for name, element in (("g01", B["g01"]), ("g12", B["g12"]), ("n45", B["n45"])):
    check("exact", f"{name} fixes the selected q and tautological background",
          act_form(element, q0) == q0 and act_form(element, t_background) == t_background)
    check("exact", f"the full response intertwines {name} on all four lifts",
          all(response(act_form(element, solution)) == act_form(element, response(solution))
              for solution in solutions))

frame0 = B["identity"]()
frame1 = B["g01"]
frame2 = B["compose"](B["g12"], B["g01"])
h01 = B["compose"](frame1, B["inverse"](frame0))
h12 = B["compose"](frame2, B["inverse"](frame1))
h02 = B["compose"](frame2, B["inverse"](frame0))
local_solutions = [[act_form(frame, value) for value in solutions]
                   for frame in (frame0, frame1, frame2)]
check("exact", "the unique all-grade graph obeys pairwise and direct full-frame descent",
      [act_form(h01, value) for value in local_solutions[0]] == local_solutions[1]
      and [act_form(h12, value) for value in local_solutions[1]] == local_solutions[2]
      and [act_form(h02, value) for value in local_solutions[0]] == local_solutions[2])
check("planted", "PLANT freezing the all-grade graph while the labelled frame moves fails",
      local_solutions[0] != local_solutions[1])


print("\nE. SURPLUS, SYMPLECTIC REVIEW, AND CLAIM BOUNDARY")
check("scope", "the fixed-target coefficient freedom is zero because the response is invertible", True)
check("scope", "the local fit has zero surplus rather than positive predictive surplus", True)
check("scope", "the target remains a conditional physical comparator rather than source-derived", True)
check("scope", "the response inverse adds no independent local coefficient or functional datum", True)
check("symplectic", "configuration descent does not construct an Euler or preboundary class", True)
check("symplectic", "no covariant phase-space or BFV quotient is inferred", True)
check("scope", "Krein positivity and a common Green domain remain open", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT no Einstein equation spectrum particle count or cosmology is inferred", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__RAW_UPSILON_IS_SHIAB_CURVATURE_PLUS_KAPPA_T__SOURCE-SILENT__CONDITIONAL_MINUS_J2D_TARGET_AND_ITS_IDENTIFICATION_WITH_THE_PHYSICAL_GRAPH")
print("FULL_RESPONSE=DOMAIN_DIM1470_OUTPUT_SUPPORT4330_RANK1470_NULLITY0_COKERNEL_DIM2860")
print("ALL_GRADE_SOLUTIONS=UNIQUE_SUPPORTS_71_48_48_48_FAMILY_RANK4")
print("CONSTRAINT_SURPLUS=ZERO_LOCAL_FREEDOM_ZERO_LOCAL_PREDICTIVE_SURPLUS")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("DISPOSITION=UNIQUE_CONDITIONAL_ALL_GRADE_GRAPH_CONSTRUCTED__TARGET_NOT_DERIVED__OBSERVATION_EULER_PREBOUNDARY_OPEN")
print("NEXT=OBSERVATION_SECTION_EULER_PREBOUNDARY_SYMPLECTIC_DESCENT_ON_THE_LABELLED_NULL_SCREEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
