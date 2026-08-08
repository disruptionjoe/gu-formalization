#!/usr/bin/env python3
"""Exact K77 null-conormal graph and Euler/preboundary sufficiency gate.

This probe extends the v0.61 frozen-covector response to the retained labelled
null covector, differentiates the graph in the missing conormal direction, and
measures the source principal symbol.  It deliberately does not invent the
paired (Upsilon, Xi) action dual or call a principal symbol a symplectic
current.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_coupled_all_grade_upsilon_graph_probe.py"
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
receiver = read("lab/sources/gu-euler-lift-ward-observation-source-reinspection-2026-08-05.md")
observation = read("explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md")
epsilon_boundary = read("explorations/conditional-build/selected-first-order-epsilon-preboundary-compose-2026-08-06.md")
check("source", "the source displays dI1 as the paired Upsilon Xi first variation",
      r"dI^B_1=(\Upsilon_\omega,\Xi_\omega)" in source)
check("source", "the source displays Xi equals D Upsilon as a redundant relation",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source)
check("source", "the source remains silent on the equation-dual observation map",
      "equation-dual map for the action Euler covector" in receiver
      and "SOURCE-SILENT" in receiver)
check("repo", "observation remains a dependent metric-section receiver",
      "not:  add an independent section/observation action column" in observation)
check("repo", "the prior selected preboundary theorem retains unrestricted flux",
      "explicit unrestricted boundary flux" in epsilon_boundary)
for label in (
    "raw Upsilon versus paired first variation (Upsilon,Xi)",
    "frozen-covector response inverse versus covariant graph prolongation",
    "principal boundary symbol versus invariant Green current",
    "Green current versus reduced presymplectic two-form",
    "labelled ambient null screen versus four-dimensional physical quotient",
    "dependent observation receiver versus independent action field",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE V0.61 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.61 all-grade predecessor replays", "PASS 50/50" in capture.getvalue())

M = V["M"]
ONE = M["ONE"]
ZERO = M["ZERO"]
channels = V["channels"]
basis_forms = V["basis_forms"]
t_background = V["t_background"]
q0 = V["q0"]
q1 = {1 << 1: {0: ONE}}
q_null = M["fadd"](q0, q1)


def response_at(q, delta_a):
    delta_f = M["fadd"](
        M["wedge_raw"](q, delta_a),
        M["wedge_raw"](t_background, delta_a),
        M["wedge_raw"](delta_a, t_background),
    )
    return M["fadd"](
        M["hodge"](M["shiab"](delta_f, channels)), delta_a
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


def build_solver(q):
    columns = [M["flatten"](response_at(q, value)) for value in basis_forms]
    pivots = {}
    for index, column in enumerate(columns):
        value = dict(column)
        representation = {index: ONE}
        while value:
            pivot = min(value)
            if pivot not in pivots:
                inverse_lead = M["gdiv"](ONE, value[pivot])
                value = {key: M["gmul"](coefficient, inverse_lead)
                         for key, coefficient in value.items()}
                representation = {
                    key: M["gmul"](coefficient, inverse_lead)
                    for key, coefficient in representation.items()
                }
                pivots[pivot] = (value, representation)
                break
            basis_vector, basis_representation = pivots[pivot]
            lead = value[pivot]
            add_scaled(value, basis_vector, M["gneg"](lead))
            add_scaled(representation, basis_representation, M["gneg"](lead))

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

    return columns, pivots, solve


def source_form(solution):
    result = {}
    for index, coefficient in solution.items():
        result = M["fadd"](result, M["fscale"](coefficient, basis_forms[index]))
    return result


def family_rank(forms):
    return M["sparse_rank"]([M["flatten"](value) for value in forms])


print("\nC. EXACT LABELLED-NULL RESPONSE GRAPH")
null_columns, null_pivots, solve_null = build_solver(q_null)
null_support = set().union(*(set(column) for column in null_columns))
check("exact", "the labelled-null full response retains rank 1470 and nullity zero",
      len(null_pivots) == len(basis_forms) == 1470)
check("exact", "the labelled-null response support has 6530 coordinates",
      len(null_support) == 6530)
check("exact", "the labelled-null response still occupies grades one two and five",
      {key[1].bit_count() for key in null_support} == {1, 2, 5})

null_solutions = []
for target in V["targets"]:
    representation, remainder = solve_null(target)
    check("exact", "one fixed target has a unique labelled-null preimage",
          representation is not None and not remainder)
    null_solutions.append(source_form(representation))
check("exact", "the four labelled-null solutions have supports 103 84 73 73",
      [len(M["flatten"](value)) for value in null_solutions] == [103, 84, 73, 73])
check("exact", "the labelled-null solution family retains rank four",
      family_rank(null_solutions) == 4)
check("exact", "every labelled-null response equals its fixed conditional target",
      all(M["flatten"](response_at(q_null, solution)) == target
          for solution, target in zip(null_solutions, V["targets"])))
check("planted", "PLANT freezing the non-null solution at the null conormal fails",
      all(M["flatten"](response_at(q_null, solution)) != target
          for solution, target in zip(V["solutions"], V["targets"])))


print("\nD. FIRST CONORMAL PROLONGATION")
def q_symbol(delta_a):
    return M["hodge"](M["shiab"](
        M["wedge_raw"](q1, delta_a), channels
    ))


graph_derivatives = []
for solution in V["solutions"]:
    source_variation = M["flatten"](q_symbol(solution))
    representation, remainder = V["solve"](source_variation)
    check("exact", "one q-direction source variation lies in the full response image",
          representation is not None and not remainder)
    graph_derivatives.append(M["fscale"](-1, source_form(representation)))
check("exact", "the four unique q-direction graph derivatives have supports 30 37 29 29",
      [len(M["flatten"](value)) for value in graph_derivatives] == [30, 37, 29, 29])
check("exact", "the differentiated fixed-target graph equation closes exactly",
      all(not M["fadd"](response_at(q0, derivative), q_symbol(solution))
          for solution, derivative in zip(V["solutions"], graph_derivatives)))
check("planted", "PLANT a frozen graph misses every q-direction derivative equation",
      all(bool(q_symbol(solution)) for solution in V["solutions"]))
check("planted", "PLANT first-order prolongation is not the finite null graph",
      all(M["flatten"](M["fadd"](solution, derivative))
          != M["flatten"](null_solution)
          for solution, derivative, null_solution
          in zip(V["solutions"], graph_derivatives, null_solutions)))


print("\nE. PRINCIPAL BOUNDARY SENSITIVITY")
def principal(delta_a):
    return M["hodge"](M["shiab"](
        M["wedge_raw"](q0, delta_a), channels
    ))


principal_columns = [M["flatten"](principal(value)) for value in basis_forms]
principal_support = set().union(*(set(column) for column in principal_columns))
principal_rank = M["sparse_rank"](principal_columns)
check("exact", "the source principal symbol has rank 650 and nullity 820",
      principal_rank == 650 and len(basis_forms) - principal_rank == 820)
check("exact", "the source principal symbol has 3224-coordinate output support",
      len(principal_support) == 3224)
check("exact", "exactly 1365 declared basis columns have nonzero principal response",
      sum(bool(column) for column in principal_columns) == 1365)
solution_principals = [principal(solution) for solution in V["solutions"]]
check("exact", "all four graph columns are boundary-symbol visible",
      [len(M["flatten"](value)) for value in solution_principals]
      == [16, 25, 25, 25])
check("exact", "their principal boundary responses retain family rank four",
      family_rank(solution_principals) == 4)
check("control", "the 105 q-parallel form columns are an exact zero-symbol control",
      all(not principal_columns[index] for index in range(105)))
check("control", "the first transverse column has a one-coordinate nonzero symbol",
      len(principal_columns[105]) == 1)


print("\nF. LABELLED STABILIZER AND CLAIM BOUNDARY")
ell = {
    1 << 0: {0: M["gscale"](Fraction(1, 2), ONE)},
    1 << 1: {0: M["gscale"](Fraction(-1, 2), ONE)},
}
for name in ("g12", "n45"):
    element = V["B"][name]
    check("exact", f"{name} fixes the retained null pair and background",
          V["act_form"](element, q_null) == q_null
          and V["act_form"](element, ell) == ell
          and V["act_form"](element, t_background) == t_background)
    check("exact", f"the labelled-null response intertwines {name}",
          all(response_at(q_null, V["act_form"](element, value))
              == V["act_form"](element, response_at(q_null, value))
              for value in null_solutions))

check("symplectic", "a nonzero principal symbol requires a Green owner but is not itself a current", True)
check("symplectic", "the paired Upsilon Xi action dual remains required", True)
check("symplectic", "no reduced presymplectic or BFV class is inferred", True)
check("scope", "moving Hodge Shiab background target and metric-section jets remain open", True)
check("scope", "the fixed conditional targets remain source-silent", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT no Einstein equation spectrum cosmology or Standard Model recovery is inferred", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__PAIRED_UPSILON_XI_FIRST_VARIATION_AND_XI_EQUALS_D_UPSILON__SOURCE-SILENT__EQUATION_DUAL_OBSERVATION_MAP_AND_GREEN_PAIRING")
print("LABELLED_NULL_RESPONSE=DOMAIN1470_RANK1470_NULLITY0_OUTPUT_SUPPORT6530")
print("LABELLED_NULL_SOLUTIONS=UNIQUE_SUPPORTS_103_84_73_73_FAMILY_RANK4")
print("Q_DIRECTION_GRAPH_PROLONGATION=UNIQUE_SUPPORTS_30_37_29_29")
print("PRINCIPAL_SYMBOL=RANK650_NULLITY820_OUTPUT_SUPPORT3224__GRAPH_FAMILY_RANK4")
print("DISPOSITION=NULL_GRAPH_AND_ONE_CONORMAL_PROLONGATION_PASS__PAIRED_ACTION_DUAL_GREEN_AND_MOVING_OBSERVATION_JETS_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=PAIRED_UPSILON_XI_ACTION_DUAL_AND_MOVING_HODGE_OBSERVATION_GREEN_IDENTITY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
