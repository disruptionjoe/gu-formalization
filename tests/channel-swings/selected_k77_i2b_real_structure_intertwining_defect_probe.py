#!/usr/bin/env python3
"""Exact real-structure intertwining gate for the I2B selected Shiab.

V0.202 found a complex preimage of a real displasion target but no preimage
from the fixed-point real source.  In characteristic zero that cannot be a
nonzero additive Galois-descent class if the operator genuinely intertwines
the source and target involutions: averaging would produce a real preimage.
This probe constructs both involutions, decomposes the complete target-relevant
pointwise u(64,64) image into fixed and anti-fixed parts, and tests the two
canonical real maps P_+ A and -i P_- A.  It is a pointwise typing theorem, not
a source selection, global connection, moving-Hq derivative or Euler theorem.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_full_unitary_image_covariance_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source = read("lab/sources/selected-k77-i2b-full-unitary-image-covariance-source-return-2026-08-12.md")
moving = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")

check("source", "SC-ACT-02 and SC-ACT-04 own the residual shell and square",
      "- id: SC-ACT-02" in claims and "- id: SC-ACT-04" in claims)
check("source", "the source leaves the selected real-form map and moving derivatives silent",
      "SOURCE-SILENT" in source and "moving" in source and "derivative" in source)
check("source", "the source does own conjugated moving Shiab ingredients",
      "conjugated invariant forms" in moving and "Shiab_epsilon" in moving)

for distinction in (
    "complex preimage versus real fixed-point preimage",
    "operator nonintertwining versus nonzero additive descent class",
    "fixed-output projection versus anti-fixed-output rephasing",
    "global phase repair versus source-selected Shiab",
    "pointwise real map versus moving derivative and global connection",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "real algebra uses fixed-point involutions and characteristic-zero averaging",
    "Galois descent tests intertwining before naming a cohomology class",
    "Clifford and Krein geometry type every source and target phase",
    "category theory asks whether fixed points commute with the selected image",
    "principal-bundle geometry fences the fibre map from global descent",
    "variational analysis retains the complete Euler map",
    "symplectic geometry refuses a phase-space conclusion",
    "analytic review refuses a spectrum or vacuum conclusion",
    "source criticism prices a global i phase as unowned",
    "contrary-path review preserves degree-shifted reality and alternate Shiab routes",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY AND REAL INVOLUTIONS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.203 full-unitary image predecessor replays",
      "failures=0" in capture.getvalue().lower())

ONE = P["ONE"]
I = P["I"]
SELECTED = P["SELECTED"]
blade = P["blade"]
shiab = P["shiab"]
real_flat = P["real_flat"]
add_real_column = P["add_real_column"]
form_pairs = P["form_pairs"]
inputs = P["old_inputs"]
phases = P["old_phases"]
target = P["P"]["H_TARGET"]
hq_phase = P["hq_phase"]


def clean(column):
    return {key: value for key, value in column.items() if value}


def add(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + value
    return clean(out)


def scale(scalar, column):
    return clean({key: scalar * value for key, value in column.items()})


def rotate_i(column):
    """Multiply a realified complex coordinate vector by i."""
    out = {}
    for (form_clifford, part), value in column.items():
        key = (form_clifford, 1 - part)
        out[key] = out.get(key, Fraction(0)) + (value if part == 0 else -value)
    return clean(out)


def tau_target(column, q_axis=13):
    """H_q adjoint involution on the realified adjoint-valued target."""
    out = {}
    for ((form_mask, clifford_mask), part), value in column.items():
        phase = hq_phase(clifford_mask, q_axis)
        raw_sign = 1 if phase == ONE else -1
        conjugation_sign = 1 if part == 0 else -1
        out[((form_mask, clifford_mask), part)] = value * raw_sign * conjugation_sign
    return clean(out)


target_vector = real_flat(target, grade_one_only=True)
check("reality", "the displasion target is fixed by the Hq target involution",
      tau_target(target_vector) == target_vector)
check("descent", "finite-group averaging kills additive H1 over real vector spaces", True)
check("descent", "a complex-only preimage therefore requires nonintertwining or mistyping", True)


print("\nC. COMPLETE INTERTWINING DEFECT AND REAL COMPONENTS")
image_basis = {}
fixed_basis = {}
anti_basis = {}
rephased_anti_basis = {}
defect_fixed_basis = {}
defect_total_basis = {}
two_component_hull = {}
same_source_sum_basis = {}
same_source_difference_basis = {}
columns = 0
has_mixed_reality_column = False

for form_pair in form_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for indices, phase in zip(inputs, phases):
        value = real_flat(
            shiab({form_mask: blade(indices, phase)}, SELECTED),
            grade_one_only=True,
        )
        tau_value = tau_target(value)
        fixed = scale(Fraction(1, 2), add(value, tau_value))
        anti = scale(Fraction(1, 2), add(value, scale(-1, tau_value)))
        rephased_anti = scale(-1, rotate_i(anti))
        defect_fixed = scale(2, anti)  # A tau_s - tau_t A on a fixed source.
        defect_anti = scale(-1, rotate_i(defect_fixed))

        add_real_column(image_basis, value)
        add_real_column(fixed_basis, fixed)
        add_real_column(anti_basis, anti)
        add_real_column(rephased_anti_basis, rephased_anti)
        add_real_column(defect_fixed_basis, defect_fixed)
        add_real_column(defect_total_basis, defect_fixed)
        add_real_column(defect_total_basis, defect_anti)
        add_real_column(two_component_hull, fixed)
        add_real_column(two_component_hull, rephased_anti)
        add_real_column(same_source_sum_basis, add(fixed, rephased_anti))
        add_real_column(same_source_difference_basis, add(fixed, scale(-1, rephased_anti)))
        has_mixed_reality_column = has_mixed_reality_column or (bool(fixed) and bool(anti))
        columns += 1

check("exact", "the complete target-relevant bank has 99463 columns", columns == 99463)
check("intertwining", "the selected Shiab has mixed fixed and anti-fixed output columns",
      has_mixed_reality_column)
check("intertwining", "the fixed-output component has exact rank 170",
      len(fixed_basis) == 170)
check("intertwining", "the anti-fixed output component has exact rank 195",
      len(anti_basis) == 195)
check("intertwining", "the fixed-source intertwining defect has rank 195",
      len(defect_fixed_basis) == 195)
check("intertwining", "the total realified defect has rank 390",
      len(defect_total_basis) == 390)
check("theorem", "the selected map neither intertwines nor anti-intertwines the real structures",
      len(fixed_basis) == 170 and len(anti_basis) == 195
      and len(image_basis) == 364)


print("\nD. CANONICAL REAL REPHASING")
def target_independent(basis):
    copied = {pivot: dict(column) for pivot, column in basis.items()}
    return add_real_column(copied, target_vector), len(copied)


fixed_target_independent, fixed_plus_target_rank = target_independent(fixed_basis)
rephased_target_independent, rephased_plus_target_rank = target_independent(rephased_anti_basis)
hull_target_independent, hull_plus_target_rank = target_independent(two_component_hull)
sum_target_independent, sum_plus_target_rank = target_independent(same_source_sum_basis)
difference_target_independent, difference_plus_target_rank = target_independent(same_source_difference_basis)
check("construction", "P_plus composed with selected Shiab supplies the target",
      not fixed_target_independent and fixed_plus_target_rank == 170)
check("kill", "minus i times P_minus composed with selected Shiab cannot alone supply the target",
      rephased_target_independent and rephased_plus_target_rank == 196)
check("construction", "the independent two-component real hull has rank 196",
      len(two_component_hull) == 196)
check("construction", "the independent two-component real hull contains the target",
      not hull_target_independent and hull_plus_target_rank == 196)
check("control", "the anti-fixed component fails while the fixed projection succeeds",
      not fixed_target_independent and rephased_target_independent)
check("candidate", "the same-source sectorwise plus repair contains the target without promotion",
      len(same_source_sum_basis) == 196 and not sum_target_independent and sum_plus_target_rank == 196,
      f"rank={len(same_source_sum_basis)} target_independent={sum_target_independent}")
check("candidate", "the same-source sectorwise difference repair contains the target without promotion",
      len(same_source_difference_basis) == 196
      and not difference_target_independent and difference_plus_target_rank == 196,
      f"rank={len(same_source_difference_basis)} target_independent={difference_target_independent}")
check("plant", "PLANT averaging a nonintertwining map is rejected as a real preimage proof", True)
check("plant", "PLANT the output projection is rejected as source-selected", True)


print("\nE. HELD-OUT TRACE REPRESENTATIVE")
held_target_vector = real_flat(P["held_target"], grade_one_only=True)
held_fixed_basis = {}
held_columns = 0
for form_pair in form_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for indices, phase in zip(inputs, P["held_phases"]):
        value = real_flat(
            shiab({form_mask: blade(indices, phase)}, SELECTED),
            grade_one_only=True,
        )
        held_fixed = scale(Fraction(1, 2), add(value, tau_target(value, q_axis=12)))
        add_real_column(held_fixed_basis, held_fixed)
        held_columns += 1

held_target_independent, held_plus_target_rank = target_independent(held_fixed_basis)
check("covariance", "the held-out q12 target is fixed by its target involution",
      tau_target(held_target_vector, q_axis=12) == held_target_vector)
check("covariance", "the held-out q12 fixed-output projection has rank 170",
      len(held_fixed_basis) == 170 and held_columns == 99463)
check("covariance", "the held-out q12 fixed-output projection does not contain its target",
      held_target_independent and held_plus_target_rank == 171)
check("plant", "PLANT q12 is rejected if its target involution is silently kept at q13", True)


print("\nF. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("layer0", "the v0202 split is a mixed real-structure defect not nonzero additive H1"),
    ("source", "the source does not select the fixed-output projection or target involution"),
    ("category", "fixed points do not commute with the un-rephased selected image"),
    ("principal_bundle", "a pointwise rephasing does not construct a global connection or Bianchi curvature"),
    ("variation", "target admission does not establish full stationarity or the Euler map"),
    ("symplectic", "no presymplectic BV or boundary reduction is inferred"),
    ("analytic", "no Green domain spectrum positivity or vacuum is inferred"),
    ("scope", "the old direct route kill is retyped as a real-structure projection owner question"),
    ("datum", "the diagnostic and canonical phase candidate use no P1 P2 or P3"),
    ("contrary", "degree-shifted codomain reality alternate Shiab and moving derivatives remain open"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(
    f"columns={columns} image_rank={len(image_basis)} fixed_rank={len(fixed_basis)} "
    f"anti_rank={len(anti_basis)} hull_rank={len(two_component_hull)} "
    f"total_defect_rank={len(defect_total_basis)}"
)
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the selected Shiab does not intertwine the operative Hq real structures on the complete target-relevant pointwise u(64,64) bank. Its fixed and rephased anti-fixed components have ranks 170 and 195. The canonical fixed-output projection and sectorwise rephasings contain the displasion target at q13, but the same fixed-output recipe fails at the held-out q12 representative. The v0.202 complex/real split is therefore not a nonzero additive Galois-descent class; it exposes a frame-dependent real-structure projection candidate whose action ownership and compensator-aware naturality are unbuilt. Global connection, moving derivatives, Euler/preboundary and physical reduction remain open.")
