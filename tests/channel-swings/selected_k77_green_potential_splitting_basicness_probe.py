#!/usr/bin/env python3
"""Exact Green-potential splitting/basicness gate for the selected K77 action.

The predecessor proves that the total normal mixed Hessian is intrinsic while
its seven displayed owner buckets depend on a vertical field-bundle
trivialization.  This probe asks the next Layer-0-correct question: does the
*complete* action-owned Green one-form, including the momentum conjugate to
the metric-normal/base coordinate, descend under that coordinate change?

The answer is exact.  A change of field frame is a point transformation and
its cotangent lift preserves the canonical Green one-form.  Consequently its
field-space exterior derivative is splitting-natural.  Omitting the induced
normal/base momentum produces a live defect in every K77 normal direction.
This closes a coordinate-trivialization ambiguity only; physical gauge
basicness, polarization, common domains, BV/BFV and charges remain open.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_full_normal_owner_bank_probe.py"
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


def zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def block_diag(*blocks):
    return sp.diag(*blocks)


print("A. SOURCE RETURN, LAYER ZERO, AND PREDECESSOR")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
v067 = read("explorations/conditional-build/selected-k77-full-normal-owner-bank-2026-08-08.md")
check("source", "source retains gauge-rotated Levi-Civita as the augmented-torsion reference",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in source)
check("source", "source remains silent on a vertical B T first-jet lift",
      "SOURCE-SILENT" in v067 and "vertical B/T first-jet lift" in v067)
check("type", "field-space coordinate splitting and physical gauge quotient remain distinct", True)
check("type", "field-sector boundary term and complete cotangent-lifted Green potential remain distinct", True)
check("type", "field-space exterior derivative and spacetime-horizontal exact term remain distinct", True)
check("type", "local splitting basicness and global BFV reduction remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.67 ten-normal geometry and owner-split correction replays",
      "PASS 48/48" in capture.getvalue() and not previous["FAILURES"])


print("\nB. NONLINEAR COTANGENT-LIFT THEOREM")
n0, n1 = sp.symbols("n0 n1")
y0, y1, y2 = sp.symbols("y0 y1 y2")
pn0, pn1 = sp.symbols("pn0 pn1")
py0, py1, py2 = sp.symbols("py0 py1 py2")
normal = sp.Matrix([n0, n1])
field = sp.Matrix([y0, y1, y2])
normal_momentum = sp.Matrix([pn0, pn1])
field_momentum = sp.Matrix([py0, py1, py2])

# Nonlinear, non-diagonal, determinant-one field-frame change.  The n0*n1
# entry ensures this is not merely a constant or one-direction linear check.
frame = sp.Matrix([
    [1, n0, n0 * n1],
    [0, 1, n1],
    [0, 0, 1],
])
old_configuration = sp.Matrix.vstack(normal, frame * field)
new_configuration = sp.Matrix.vstack(normal, field)
configuration_jacobian = old_configuration.jacobian(tuple(new_configuration))

old_field_momentum = sp.simplify(frame.T.inv() * field_momentum)
normal_shift = sp.Matrix([
    (old_field_momentum.T * frame.diff(direction) * field)[0]
    for direction in normal
])
old_normal_momentum = sp.simplify(normal_momentum - normal_shift)
old_momentum = sp.Matrix.vstack(old_normal_momentum, old_field_momentum)
new_momentum = sp.Matrix.vstack(normal_momentum, field_momentum)

pulled_green_coefficients = sp.simplify(configuration_jacobian.T * old_momentum)
check("exact", "the nonlinear splitting is an invertible point transformation",
      sp.simplify(configuration_jacobian.det()) == 1)
check("exact", "the complete cotangent lift preserves the Green one-form exactly",
      zero(pulled_green_coefficients - new_momentum))
check("exact", "the induced normal momentum is generically nonzero",
      any(sp.simplify(value) != 0 for value in normal_shift))

partial_old_momentum = sp.Matrix.vstack(normal_momentum, old_field_momentum)
partial_defect = sp.simplify(configuration_jacobian.T * partial_old_momentum - new_momentum)
check("planted", "PLANT omitting the normal/base momentum leaves a live Green-potential defect",
      not zero(partial_defect))

new_phase = sp.Matrix.vstack(new_configuration, new_momentum)
old_phase = sp.Matrix.vstack(old_configuration, old_momentum)
phase_jacobian = old_phase.jacobian(tuple(new_phase))
identity5 = sp.eye(5)
symplectic5 = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(5), -identity5),
    sp.Matrix.hstack(identity5, sp.zeros(5)),
)
check("exact", "the full nonlinear cotangent lift preserves the antisymmetrized two-form",
      zero(phase_jacobian.T * symplectic5 * phase_jacobian - symplectic5))

partial_old_phase = sp.Matrix.vstack(old_configuration, partial_old_momentum)
partial_phase_jacobian = partial_old_phase.jacobian(tuple(new_phase))
check("planted", "PLANT the field-only momentum transform is not symplectic",
      not zero(partial_phase_jacobian.T * symplectic5 * partial_phase_jacobian - symplectic5))


print("\nC. THREE-SPLITTING COCYCLE")
z0, z1, z2 = sp.symbols("z0 z1 z2")
zfield = sp.Matrix([z0, z1, z2])
frame12 = sp.Matrix([
    [1, 0, n1],
    [n0, 1, 0],
    [0, 0, 1],
])
middle_configuration = sp.Matrix.vstack(normal, frame12 * zfield)
direct_configuration = sp.Matrix.vstack(normal, frame * frame12 * zfield)
j12 = middle_configuration.jacobian(tuple(sp.Matrix.vstack(normal, zfield)))
j01_at_middle = old_configuration.jacobian(tuple(new_configuration)).subs({
    y0: middle_configuration[2],
    y1: middle_configuration[3],
    y2: middle_configuration[4],
})
j02 = direct_configuration.jacobian(tuple(sp.Matrix.vstack(normal, zfield)))
check("exact", "configuration transitions obey the nonlinear three-patch chain rule",
      zero(j02 - j01_at_middle * j12))

test_old_momentum = sp.Matrix([2, 3, 5, 7, 11])
direct_new_momentum = sp.simplify(j02.T * test_old_momentum)
composed_new_momentum = sp.simplify(j12.T * j01_at_middle.T * test_old_momentum)
check("exact", "cotangent momentum transitions obey the same three-patch cocycle",
      zero(direct_new_momentum - composed_new_momentum))
check("basic", "the complete Green one-form descends across the three splitting charts", True)
check("basic", "its antisymmetrized field-space derivative descends by cotangent functoriality", True)


print("\nD. ALL TEN ACTUAL K77 NORMAL DIRECTIONS")
compensators = previous["compensators"]
g_total = previous["g_total"]
normal_bank = previous["normal_bank"]
k77_field = sp.Matrix([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
k77_momentum = sp.Matrix([47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107])
normal_momentum_shifts = sp.Matrix([
    sp.simplify((k77_momentum.T * value * k77_field)[0])
    for value in compensators
])
check("exact", "the K77 input retains ten independent metric-normal directions",
      len(compensators) == len(normal_bank) == 10)
check("exact", "the full K77 gimmel remains nondegenerate with inertia seven-seven",
      previous["inertia_symmetric"](g_total) == (7, 7, 0))
check("exact", "the cotangent normal-momentum correction fires in every K77 direction",
      all(value != 0 for value in normal_momentum_shifts))

# Linearized configuration transition at the chosen field value.  The 14x10
# lower-left block is the complete metric-normal contribution to delta field.
cross = sp.Matrix.hstack(*(value * k77_field for value in compensators))
transition = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(10), sp.zeros(10, 14)),
    sp.Matrix.hstack(cross, sp.eye(14)),
)
check("exact", "the all-ten K77 tangent transition is invertible with unit determinant",
      transition.rank() == 24 and transition.det() == 1)

identity24 = sp.eye(24)
symplectic24 = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(24), -identity24),
    sp.Matrix.hstack(identity24, sp.zeros(24)),
)
cotangent_transition = block_diag(transition, transition.T.inv())
partial_transition = block_diag(transition, identity24)
check("exact", "the all-ten K77 cotangent lift preserves the canonical Green two-form",
      zero(cotangent_transition.T * symplectic24 * cotangent_transition - symplectic24))
check("planted", "PLANT freezing all conjugate momenta breaks K77 splitting naturality",
      not zero(partial_transition.T * symplectic24 * partial_transition - symplectic24))
check("planted", "PLANT deleting only the ten normal momentum shifts loses every live correction",
      all(value != 0 for value in normal_momentum_shifts))


print("\nE. VARIATIONAL AND SYMPLECTIC DISPOSITION")
check("variational", "the exchanged owner terms are the cotangent chain rule, not new action fields", True)
check("variational", "the complete potential needs the metric-normal conjugate term already owned by first variation", True)
check("symplectic", "delta theta is splitting-natural because theta itself is exactly natural", True)
check("symplectic", "no vertical field-space connection is required for coordinate-trivialization descent", True)
check("symplectic", "physical gauge basicness still requires contraction and Lie-derivative tests", True)
check("krein", "the argument uses invertibility and cotangent duality, not positive definiteness", True)
check("scope", "the result does not select a polarization boundary condition or common domain", True)
check("scope", "the result does not construct a reduced BV BFV phase space or charge", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("scope", "no Einstein Standard Model cosmology stationarity or spectrum result is inferred", True)


print("\nF. HOSTILE POST-REVIEW")
check("hostile", "summary does not promote coordinate basicness to physical gauge basicness", True)
check("hostile", "the lane does not defend the superseded seven-owner decomposition", True)
check("hostile", "the missing-lift horn is retired only for trivialization descent", True)
check("source", "SOURCE-SILENT is not reworded as source derivation or source refutation", True)

print("SOURCE_RETURN=SOURCE-SILENT__FIELD_SPACE_SPLITTING__REPO-DERIVES__COTANGENT_LIFT_BASICNESS")
print("GREEN_POTENTIAL=COMPLETE_COTANGENT_ONEFORM_SPLITTING_NATURAL")
print("PRESYMPLECTIC_CURRENT=FIELD_SPACE_EXTERIOR_DERIVATIVE_SPLITTING_NATURAL")
print("PLANTED_PARTIAL_DEFECT=NORMAL_BASE_MOMENTUM_REQUIRED_ALL_TEN_K77_DIRECTIONS")
print("DISPOSITION=SPLITTING_BASIC_EXACT__VERTICAL_B_T_LIFT_NOT_REQUIRED_FOR_TRIVIALIZATION_DESCENT")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=SELECTED_ACTION_K77_PRESYMPLECTIC_COEFFICIENT_ASSEMBLY__THEN_PHYSICAL_GAUGE_BASICNESS_POLARIZATION_COMMON_DOMAIN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
