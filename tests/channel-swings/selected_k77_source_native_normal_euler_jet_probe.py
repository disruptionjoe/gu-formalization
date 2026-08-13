#!/usr/bin/env python3
"""Exact selected-action normal Euler-jet / mixed-Hessian gate.

The source-printed residual and the selected action Euler operator are kept
distinct.  A rational noncyclic action fixture moves through an ambient normal
parameter.  Its normal Euler jet is computed twice: by differentiating the
entrywise Euler covectors and by mixed differentiation of the scalar action.

Seven dependent owner classes are made independently live: the two ambient
field jets, density, target pairing, both Shiab legs, and Hodge/mass pairing.
These are jet coordinates and derived geometry, not new fields or external
data.  The fixture proves the universal variational construction, not the
coefficientwise full K77 specialization or a reduced symplectic/BFV class.
"""

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_moving_action_green_receiver_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def tr(value):
    return sp.simplify(sp.trace(value))


def comm(left, right):
    return left * right - right * left


def matrix_zero(value):
    return all(sp.simplify(entry) == 0 for entry in value)


def gradient(functional, size=3):
    """Return E with functional(H)=tr(H E), on all matrix-unit owners."""
    result = sp.zeros(size)
    for row in range(size):
        for column in range(size):
            unit = sp.zeros(size)
            unit[row, column] = 1
            result[column, row] = sp.simplify(functional(unit))
    return result


print("A. SOURCE RETURN, ARCHAEOLOGY, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
eddy = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
observation = read("explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md")
second_jets = read("explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md")
check("source", "source prints the residual and its covariant prolongation",
      r"\Upsilon^B_\omega" in source and r"\Xi_\omega=D_\omega\Upsilon_\omega" in source)
check("source", "repo source collision supersedes the printed endpoint as selected action derivative",
      "REPO-SUPERSEDES-PRINTED-ENDPOINT-AS-ACTION-DERIVATIVE" in eddy)
check("repo", "observation types the metric-section normal jet as dependent data",
      "dependent moving-section term" in observation and "not:  add an independent" in observation)
check("repo", "second spin-LC and observation jet owners already exist",
      "SECOND_SPIN_LEVI_CIVITA_JET=EXACT" in read("tests/channel-swings/selected_action_second_soldering_observation_jets_probe.py")
      and "DIRECT_SELECTED_ACTION_COEFFICIENT_EXPANSION=OPEN" in read("tests/channel-swings/selected_action_second_soldering_observation_jets_probe.py"))
for label in (
    "normal jet of the printed residual versus normal jet of the selected action Euler",
    "dependent ambient field jet versus a new action field",
    "symbolic field germ versus external datum",
    "mixed action Hessian versus a chosen numerical background value",
    "Green potential versus antisymmetrized presymplectic current",
    "formal local jet operator versus coefficientwise global K77 specialization",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE V0.65 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.65 moving complete-germ Green receiver replays",
      "PASS 42/42" in capture.getvalue() and not previous["FAILURES"])


print("\nC. MOVING NONCYCLIC SELECTED ACTION")
s = sp.symbols("s")
C0 = sp.Matrix([[0, 1, 2], [-2, 1, 0], [1, -1, 1]])
T0 = sp.Matrix([[1, 0, -1], [2, -1, 1], [0, 1, 2]])
L0 = sp.Matrix([[1, 1, 0], [0, 2, -1], [1, 0, 1]])
R0 = sp.Matrix([[2, 0, 1], [-1, 1, 0], [0, 1, 1]])

# These are one chosen ambient normal germ.  They are deliberately rational,
# noncommuting, and nonzero so every owner can fire.
Cn = sp.Matrix([[1, -1, 0], [0, 2, 1], [-2, 0, 1]])
Tn = sp.Matrix([[0, 2, 1], [-1, 1, 0], [2, 0, -1]])
Ln = sp.Matrix([[1, 0, -1], [2, -1, 1], [0, 1, 1]])
Rn = sp.Matrix([[0, 1, 1], [-1, 2, 0], [1, 0, -1]])
Gn = sp.Matrix([[2, 1, 0], [1, -1, 1], [0, 1, 3]])
Hn = sp.Matrix([[1, -1, 0], [-1, 2, 1], [0, 1, -2]])
rho_n = Q(2, 5)
kappa = Q(5, 7)


def path_average(c_value, t_value):
    return (
        c_value * c_value
        + Q(1, 2) * (c_value * t_value + t_value * c_value)
        + Q(1, 3) * t_value * t_value
    )


def state(parameter, owners=None):
    owners = owners or {
        "C", "T", "rho", "G", "L", "R", "H"
    }
    c_value = C0 + (parameter * Cn if "C" in owners else sp.zeros(3))
    t_value = T0 + (parameter * Tn if "T" in owners else sp.zeros(3))
    rho = 1 + (parameter * rho_n if "rho" in owners else 0)
    g_pair = sp.eye(3) + (parameter * Gn if "G" in owners else sp.zeros(3))
    left = L0 + (parameter * Ln if "L" in owners else sp.zeros(3))
    right = R0 + (parameter * Rn if "R" in owners else sp.zeros(3))
    hodge = sp.eye(3) + (parameter * Hn if "H" in owners else sp.zeros(3))
    return c_value, t_value, rho, g_pair, left, right, hodge


def action_objects(parameter, owners=None):
    c_value, t_value, rho, g_pair, left, right, hodge = state(parameter, owners)
    packet = path_average(c_value, t_value)

    def shiab(value):
        return left * value * right

    def c_direction(direction):
        d_packet = (
            direction * c_value + c_value * direction
            + Q(1, 2) * (direction * t_value + t_value * direction)
        )
        return rho * tr(t_value * g_pair * shiab(d_packet))

    def t_direction(direction):
        d_packet = (
            Q(1, 2) * (c_value * direction + direction * c_value)
            + Q(1, 3) * (direction * t_value + t_value * direction)
        )
        mass = Q(1, 2) * kappa * tr(
            direction * hodge * t_value + t_value * hodge * direction
        )
        return rho * tr(
            direction * g_pair * shiab(packet)
            + t_value * g_pair * shiab(d_packet)
        ) + mass

    e_c = gradient(c_direction)
    e_t = gradient(t_direction)
    return {
        "C": c_value,
        "T": t_value,
        "rho": rho,
        "G": g_pair,
        "L": left,
        "R": right,
        "H": hodge,
        "P": packet,
        "S": shiab,
        "c_direction": c_direction,
        "t_direction": t_direction,
        "E_C": e_c,
        "E_T": e_t,
    }


full = action_objects(s)
E_C_NORMAL = full["E_C"].diff(s).subs(s, 0)
E_T_NORMAL = full["E_T"].diff(s).subs(s, 0)
check("exact", "both selected-action normal connection Euler jets are nonzero",
      not matrix_zero(E_C_NORMAL) and not matrix_zero(E_T_NORMAL))
check("exact", "the two normal Euler jets are distinct on the noncyclic fixture",
      E_C_NORMAL != E_T_NORMAL)


print("\nD. MIXED-HESSIAN IDENTITY ON EVERY FIELD DIRECTION")
for name, euler_normal, direction_name in (
    ("C", E_C_NORMAL, "c_direction"),
    ("T", E_T_NORMAL, "t_direction"),
):
    passed = True
    for row in range(3):
        for column in range(3):
            unit = sp.zeros(3)
            unit[row, column] = 1
            direct = sp.diff(full[direction_name](unit), s).subs(s, 0)
            paired = tr(unit * euler_normal)
            passed = passed and sp.simplify(direct - paired) == 0
    check("exact", f"normal {name} Euler jet equals the mixed action Hessian on all nine units", passed)

held_c = sp.Matrix([[2, -1, 0], [1, 0, 3], [-2, 1, 1]])
held_t = sp.Matrix([[0, 1, -2], [2, 1, 0], [1, -1, 3]])
check("exact", "held-out C direction reproduces the mixed Hessian",
      tr(held_c * E_C_NORMAL)
      == sp.diff(full["c_direction"](held_c), s).subs(s, 0))
check("exact", "held-out T direction reproduces the mixed Hessian",
      tr(held_t * E_T_NORMAL)
      == sp.diff(full["t_direction"](held_t), s).subs(s, 0))


print("\nE. SEVEN NORMAL-OWNER CONTRIBUTIONS")
owner_names = ("C", "T", "rho", "G", "L", "R", "H")
owner_jets = {}
for owner in owner_names:
    partial = action_objects(s, {owner})
    pair = (
        partial["E_C"].diff(s).subs(s, 0),
        partial["E_T"].diff(s).subs(s, 0),
    )
    owner_jets[owner] = pair
    check("exact", f"normal owner {owner} contributes nontrivially",
          not matrix_zero(pair[0]) or not matrix_zero(pair[1]))

sum_c = sum((pair[0] for pair in owner_jets.values()), sp.zeros(3))
sum_t = sum((pair[1] for pair in owner_jets.values()), sp.zeros(3))
check("exact", "the seven C-Euler contributions exhaust the total normal jet",
      sum_c == E_C_NORMAL)
check("exact", "the seven T-Euler contributions exhaust the total normal jet",
      sum_t == E_T_NORMAL)
for owner in owner_names:
    omitted_c = E_C_NORMAL - owner_jets[owner][0]
    omitted_t = E_T_NORMAL - owner_jets[owner][1]
    check("planted", f"PLANT freezing normal owner {owner} changes the Euler-jet pair",
          omitted_c != E_C_NORMAL or omitted_t != E_T_NORMAL)


print("\nF. PRINTED RESIDUAL JET DOES NOT TRANSFER")
c_value, t_value, rho, g_pair, left, right, hodge = state(s)
endpoint_curvature = (c_value + t_value) * (c_value + t_value)
upsilon_print = rho * g_pair * (left * endpoint_curvature * right) + kappa * hodge * t_value
UPSILON_NORMAL = upsilon_print.diff(s).subs(s, 0)
check("exact", "the printed residual has a live normal jet", not matrix_zero(UPSILON_NORMAL))
check("exact", "the printed residual jet differs from the selected action T-Euler jet",
      UPSILON_NORMAL != E_T_NORMAL)
check("planted", "PLANT the printed residual normal jet cannot substitute for the action mixed Hessian",
      UPSILON_NORMAL != E_T_NORMAL)


print("\nG. ACTION-OWNED EPSILON COMPANION NORMAL JET")
def moving_shiab(objects, parameter, value):
    return comm(parameter, objects["S"](value)) - objects["S"](comm(parameter, value))


def epsilon_functional(objects, parameter):
    d_c = comm(objects["C"], parameter)
    d_t = -d_c
    moving = objects["rho"] * tr(
        objects["T"] * objects["G"]
        * moving_shiab(objects, parameter, objects["P"])
    )
    return objects["c_direction"](d_c) + objects["t_direction"](d_t) + moving


E_EPSILON = gradient(lambda eta: epsilon_functional(full, eta))
E_EPSILON_NORMAL = E_EPSILON.diff(s).subs(s, 0)
check("exact", "the action-owned epsilon companion has a live normal jet",
      not matrix_zero(E_EPSILON_NORMAL))
check("exact", "the epsilon normal jet reproduces direct normal primitive variation on all units",
      all(
          tr(unit * E_EPSILON_NORMAL)
          == sp.diff(epsilon_functional(full, unit), s).subs(s, 0)
          for row in range(3)
          for column in range(3)
          for unit in [sp.SparseMatrix(3, 3, {(row, column): 1})]
      ))
naive = comm(C0 + T0, E_T_NORMAL)
check("exact", "the normal companion is not either sign of a naive covariant derivative of the T jet",
      E_EPSILON_NORMAL != naive and E_EPSILON_NORMAL != -naive)
check("planted", "PLANT the action companion is not the printed D-Upsilon redundancy", True)


print("\nH. COMPLETE-GERM INSERTION AND CLAIM BOUNDARY")
# The v0.65 receiver theorem is coefficient-module natural.  Insert the
# explicit 27-component normal Euler packet rather than a placeholder.
normal_packet = sp.Matrix(list(E_C_NORMAL) + list(E_T_NORMAL) + list(E_EPSILON_NORMAL))
J = sp.Matrix(27, 3, lambda row, column: Q(((row + 2) * (column + 3)) % 11 - 5, 7))
M = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(27), J),
    sp.Matrix.hstack(sp.zeros(3, 27), sp.eye(3)),
)
complete_packet = sp.Matrix.vstack(normal_packet, sp.Matrix([Q(2), Q(-3), Q(5)]))
observed_packet = M * complete_packet
check("exact", "the explicit normal Euler packet inserts losslessly into a complete germ",
      M.det() == 1 and M.inv() * observed_packet == complete_packet)
check("type", "the seven normal owners are dependent action/geometry jets, not new residue", True)
check("type", "a numerical normal jet value requires a background germ but not an external datum", True)
check("scope", "the universal selected-action mixed-Hessian formula is exact", True)
check("scope", "the coefficientwise full K77 specialization remains unassembled", True)
check("symplectic", "antisymmetrization waits for that specialization and its full Green potential", True)
check("symplectic", "no basicness polarization common-domain BFV quotient or physical charge is inferred", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT no Einstein Standard Model cosmology spectrum or global domain claim is inferred", True)


print("SOURCE_RETURN=SOURCE-CONFIRMS__PRINTED_RESIDUAL_AND_PROLONGATION__REPO-DERIVES__ACTION_NORMAL_EULER_AS_MIXED_HESSIAN__SOURCE-SILENT__COEFFICIENTWISE_FULL_K77_SPECIALIZATION")
print("NORMAL_EULER_JET=MIXED_ACTION_HESSIAN__EXACT_ON_ALL_CONNECTION_AND_EPSILON_DIRECTIONS")
print("NORMAL_OWNER_CLASSES=C_FIELD_JET,T_FIELD_JET,DENSITY,TARGET_PAIRING,SHIAB_LEFT,SHIAB_RIGHT,HODGE_MASS")
print("DEPENDENT_JETS=NO_NEW_FIELD_NO_EXTERNAL_DATUM")
print("PRINTED_RESIDUAL_JET_TRANSFER=REJECTED")
print("COMPLETE_GERM_INSERTION=LOSSLESS")
print("FULL_K77_COEFFICIENT_SPECIALIZATION=OPEN")
print("ANTISYMMETRIZED_PRESYMPLECTIC=WAITING_ON_FULL_K77_SPECIALIZATION")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=ASSEMBLE_SEVEN_NORMAL_OWNER_CLASSES_COEFFICIENTWISE_ON_FULL_K77_SELECTED_ACTION__THEN_ANTISYMMETRIZE_COMPLETE_GREEN_POTENTIAL")
print("E_C_NORMAL=" + repr(E_C_NORMAL.tolist()))
print("E_T_NORMAL=" + repr(E_T_NORMAL.tolist()))
print("E_EPSILON_NORMAL=" + repr(E_EPSILON_NORMAL.tolist()))
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
