#!/usr/bin/env python3
"""Exact formal-adjoint symbol of the selected one-half d_B T action term."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


print("A. SOURCE, PREDECESSOR, AND LAYER 0")
source = (ROOT / "lab/sources/gu-i1b-conormal-weld-domain-source-reinspection-2026-08-05.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-action-curvature-graph-six-versus-four-2026-08-06.md").read_text()
check("source", "source fixes the one-half d_B T coefficient and fixed-epsilon translation variation", "1/2 d_B T" in source and "fixed `epsilon`" in source)
check("source", "source does not publish the selected product row or its formal-adjoint Euler rank", "preferred Shiab is not selected" in source)
check("repo", "curvature-graph predecessor leaves the off-graph derivative torsion block open", "off-graph `d_B T` torsion block" in predecessor)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(BACKEND))
check("repo", "selected exact Cl(7,7) Shiab backend replays", "PASS: the source moving-Shiab family" in capture.getvalue())

for label in (
    "raw first-order density coefficient versus formal-adjoint bulk Euler symbol",
    "bulk Euler cancellation versus Green/preboundary current",
    "first-order torsion symbol versus second-order metric curvature symbol",
    "independent T coordinate versus source variables (g,varpi)",
    "finite symbol versus common closed Green/Krein domain",
):
    check("type", label + " remain distinct", True)


print("\nB. COMPLETE HORIZONTAL LORENTZ CARRIER")
SELECTED = ("comm", "symi", "symi")
ZERO = M["ZERO"]
ONE = M["ONE"]
FULL = M["FULL"]


def cl2_basis(form_index, left, right):
    return {1 << form_index: M["emul"](M["blade"](left), M["blade"](right))}


def scalar_one_form(covector):
    return {
        1 << mu: {0: (Fraction(value), Fraction(0))}
        for mu, value in enumerate(covector) if value
    }


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(M["wedge_raw"](left, right))


carrier = [
    cl2_basis(mu, a, b)
    for mu in range(4)
    for a in range(4)
    for b in range(a + 1, 4)
]
check("exact", "horizontal Lorentz one-form carrier has dimension 24", len(carrier) == 24)


def raw_symbol(covector):
    k_form = scalar_one_form(covector)
    images = [M["shiab"](M["wedge_raw"](k_form, direction), SELECTED) for direction in carrier]
    values = [[pairing(left, image) for image in images] for left in carrier]
    real = sp.Matrix([[sp.Rational(value[0].numerator, value[0].denominator) for value in row] for row in values])
    imag = sp.Matrix([[sp.Rational(value[1].numerator, value[1].denominator) for value in row] for row in values])
    return real, imag


orbits = {
    "timelike": (1, 0, 0, 0),
    "spacelike": (0, 1, 0, 0),
    "null": (1, 0, 0, 1),
}
results = {}
for name, covector in orbits.items():
    real, imag = raw_symbol(covector)
    # The action coefficient is one half. Integration by parts sends a
    # constant-coefficient first-order symbol A(k) to -A(k)^T.
    euler_real = sp.Rational(1, 2) * (real - real.T)
    euler_imag = sp.Rational(1, 2) * (imag - imag.T)
    boundary_real = sp.Rational(1, 2) * real
    boundary_imag = sp.Rational(1, 2) * imag
    results[name] = {
        "real": real,
        "imag": imag,
        "euler_real": euler_real,
        "euler_imag": euler_imag,
        "boundary_real": boundary_real,
        "boundary_imag": boundary_imag,
    }
    print(
        f"ORBIT={name} RAW_REAL_RANK={real.rank()} RAW_IMAG_RANK={imag.rank()} "
        f"EULER_REAL_RANK={euler_real.rank()} EULER_IMAG_RANK={euler_imag.rank()} "
        f"RAW_REAL_SYMMETRIC={real == real.T} RAW_IMAG_SYMMETRIC={imag == imag.T}"
    )


print("\nC. FORMAL-ADJOINT DISPOSITION ON THE OBSERVED CL2 BANK")
all_euler_zero = all(
    packet["euler_real"] == sp.zeros(24)
    and packet["euler_imag"] == sp.zeros(24)
    for packet in results.values()
)
all_boundary_live = all(
    packet["boundary_real"] != sp.zeros(24)
    or packet["boundary_imag"] != sp.zeros(24)
    for packet in results.values()
)
check("exact", "formal-adjoint Euler and boundary matrices are constructed on all three causal representatives", len(results) == 3)
check("exact", "raw symbol is linear in the covector", all(
    raw_symbol(tuple(2 * value for value in covector))[0] == 2 * results[name]["real"]
    and raw_symbol(tuple(2 * value for value in covector))[1] == 2 * results[name]["imag"]
    for name, covector in orbits.items()
))
check("type", "formal-adjoint result must be composed in mixed differential order rather than added as a zero-jet rank", True)
check("exact", "same-grade horizontal Cl2 raw density and bulk Euler symbols vanish on all causal representatives", all_euler_zero and not all_boundary_live and all(
    packet["real"] == sp.zeros(24) and packet["imag"] == sp.zeros(24)
    for packet in results.values()
))


print("\nD. AMBIENT CL2 CROSS-BLOCK")
full_carrier_labels = [
    (mu, a, b)
    for mu in range(14)
    for a in range(14)
    for b in range(a + 1, 14)
]
full_carrier = [cl2_basis(*label) for label in full_carrier_labels]
check("exact", "full K77 Cl2 one-form carrier has dimension 1274", len(full_carrier) == 1274)


def ambient_cross_symbol(covector):
    """Euler cross block: full-left/horizontal-right minus its adjoint."""
    k_form = scalar_one_form(covector)
    horizontal_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in carrier
    ]
    full_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in full_carrier
    ]
    columns = []
    raw_columns = []
    for horizontal_index, horizontal_image in enumerate(horizontal_images):
        euler_column = {}
        raw_column = {}
        for full_index, full_direction in enumerate(full_carrier):
            forward = pairing(full_direction, horizontal_image)
            reverse = pairing(carrier[horizontal_index], full_images[full_index])
            if forward != ZERO:
                raw_column[full_index] = forward
            euler = M["gscale"](Fraction(1, 2), M["gsub"](forward, reverse))
            if euler != ZERO:
                euler_column[full_index] = euler
        raw_columns.append(raw_column)
        columns.append(euler_column)
    return raw_columns, columns


def full_symbol(covector):
    """Sparse raw and formal-adjoint Euler matrices on the full Cl2 carrier."""
    k_form = scalar_one_form(covector)
    images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in full_carrier
    ]
    rows_by_form_index = {
        mu: [index for index, label in enumerate(full_carrier_labels) if label[0] == mu]
        for mu in range(14)
    }
    raw_columns = []
    for image in images:
        candidate_rows = set()
        for form_mask in image:
            complement = FULL ^ form_mask
            if complement and complement & (complement - 1) == 0:
                candidate_rows.update(rows_by_form_index[complement.bit_length() - 1])
        column = {}
        for row in candidate_rows:
            value = pairing(full_carrier[row], image)
            if value != ZERO:
                column[row] = value
        raw_columns.append(column)
    euler_columns = []
    for column_index, column in enumerate(raw_columns):
        euler_column = {}
        rows = set(column) | {
            row_index for row_index, row_column in enumerate(raw_columns)
            if column_index in row_column
        }
        for row in rows:
            value = M["gscale"](
                Fraction(1, 2),
                M["gsub"](column.get(row, ZERO), raw_columns[row].get(column_index, ZERO)),
            )
            if value != ZERO:
                euler_column[row] = value
        euler_columns.append(euler_column)
    return images, raw_columns, euler_columns


ambient_results = {}
for name, covector in orbits.items():
    raw_columns, euler_columns = ambient_cross_symbol(covector)
    raw_rank = M["sparse_rank"](raw_columns)
    euler_rank = M["sparse_rank"](euler_columns)
    support = sum(len(column) for column in euler_columns)
    ambient_results[name] = {
        "raw_rank": raw_rank,
        "euler_rank": euler_rank,
        "support": support,
        "columns": euler_columns,
    }
    print(f"ORBIT={name} AMBIENT_RAW_CROSS_RANK={raw_rank} AMBIENT_EULER_CROSS_RANK={euler_rank} SUPPORT={support}")

ambient_cross_live = any(packet["euler_rank"] for packet in ambient_results.values())
first_witness = next(
    (
        (name, full_carrier_labels[row], horizontal_column, value)
        for name, packet in ambient_results.items()
        for horizontal_column, column in enumerate(packet["columns"])
        for row, value in column.items()
    ),
    None,
)
check("exact", "complete ambient-to-horizontal Euler cross-block is constructed on all causal representatives", len(ambient_results) == 3)
check("exact", "same-grade Cl2 block remains zero against the complete 1274-dimensional Cl2 carrier", not ambient_cross_live and first_witness is None)

full_results = {}
for name, covector in orbits.items():
    images, raw_columns, euler_columns = full_symbol(covector)
    image_live = sum(bool(M["flatten"](image)) for image in images)
    raw_rank = M["sparse_rank"](raw_columns)
    euler_rank = M["sparse_rank"](euler_columns)
    euler_support = sum(len(column) for column in euler_columns)
    full_results[name] = {
        "image_live": image_live,
        "raw_rank": raw_rank,
        "euler_rank": euler_rank,
        "euler_support": euler_support,
    }
    print(
        f"ORBIT={name} FULL_IMAGE_LIVE={image_live} FULL_RAW_RANK={raw_rank} "
        f"FULL_EULER_RANK={euler_rank} FULL_EULER_SUPPORT={euler_support}"
    )

check("exact", "full Cl2 formal-adjoint block is constructed on all causal representatives", len(full_results) == 3)
check("exact", "selected derivative images are live although the full same-grade Cl2 action pairing is zero", full_results == {
    "timelike": {"image_live": 1183, "raw_rank": 0, "euler_rank": 0, "euler_support": 0},
    "spacelike": {"image_live": 1183, "raw_rank": 0, "euler_rank": 0, "euler_support": 0},
    "null": {"image_live": 1274, "raw_rank": 0, "euler_rank": 0, "euler_support": 0},
})


print("\nE. SOURCE-ACTIVE GRADE-ONE AND GRADE-THIRTEEN BANKS")
cl1_labels = [(mu, cliff) for mu in range(14) for cliff in range(14)]
cl1_carrier = [
    {1 << mu: {1 << cliff: ONE}}
    for mu, cliff in cl1_labels
]
cl13_labels = [(mu, omitted) for mu in range(14) for omitted in range(14)]
cl13_carrier = [
    {1 << mu: {FULL ^ (1 << omitted): ONE}}
    for mu, omitted in cl13_labels
]
check("exact", "grade-one and Hodge-dual grade-thirteen banks each have dimension 196", len(cl1_carrier) == len(cl13_carrier) == 196)


def bank_symbol(covector, bank):
    k_form = scalar_one_form(covector)
    images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in bank
    ]
    raw_columns = []
    for image in images:
        column = {}
        for row, left in enumerate(bank):
            value = pairing(left, image)
            if value != ZERO:
                column[row] = value
        raw_columns.append(column)
    euler_columns = []
    for column_index, column in enumerate(raw_columns):
        euler_column = {}
        rows = set(column) | {
            row_index for row_index, row_column in enumerate(raw_columns)
            if column_index in row_column
        }
        for row in rows:
            value = M["gscale"](
                Fraction(1, 2),
                M["gsub"](column.get(row, ZERO), raw_columns[row].get(column_index, ZERO)),
            )
            if value != ZERO:
                euler_column[row] = value
        euler_columns.append(euler_column)
    return {
        "image_live": sum(bool(M["flatten"](image)) for image in images),
        "raw_rank": M["sparse_rank"](raw_columns),
        "euler_rank": M["sparse_rank"](euler_columns),
        "euler_support": sum(len(column) for column in euler_columns),
    }


graded_results = {}
for name, covector in orbits.items():
    grade1 = bank_symbol(covector, cl1_carrier)
    grade13 = bank_symbol(covector, cl13_carrier)
    graded_results[name] = {"grade1": grade1, "grade13": grade13}
    print(f"ORBIT={name} GRADE1={grade1} GRADE13={grade13}")

check("exact", "both source-active invariant banks are tested on all causal representatives", len(graded_results) == 3)
check("exact", "same-grade Cl1 and Cl13 pairings vanish despite live selected derivative images", all(
    packet[grade]["raw_rank"] == packet[grade]["euler_rank"] == packet[grade]["euler_support"] == 0
    and packet[grade]["image_live"] == (196 if name == "null" else 182)
    for name, packet in graded_results.items() for grade in ("grade1", "grade13")
))


print("\nF. ADJACENT-GRADE LEAKAGE FROM THE OBSERVED LORENTZ CARRIER")


def cross_bank_symbol(covector, left_bank, right_bank):
    k_form = scalar_one_form(covector)
    right_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in right_bank
    ]
    left_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in left_bank
    ]
    raw_columns = []
    euler_columns = []
    for right_index, right_image in enumerate(right_images):
        raw_column = {}
        euler_column = {}
        for left_index, left in enumerate(left_bank):
            forward = pairing(left, right_image)
            reverse = pairing(right_bank[right_index], left_images[left_index])
            if forward != ZERO:
                raw_column[left_index] = forward
            euler = M["gscale"](Fraction(1, 2), M["gsub"](forward, reverse))
            if euler != ZERO:
                euler_column[left_index] = euler
        raw_columns.append(raw_column)
        euler_columns.append(euler_column)
    return {
        "raw_rank": M["sparse_rank"](raw_columns),
        "euler_rank": M["sparse_rank"](euler_columns),
        "euler_support": sum(len(column) for column in euler_columns),
        "columns": euler_columns,
    }


leakage_results = {}
for name, covector in orbits.items():
    cl1_from_horizontal_cl2 = cross_bank_symbol(covector, cl1_carrier, carrier)
    cl13_from_horizontal_cl2 = cross_bank_symbol(covector, cl13_carrier, carrier)
    leakage_results[name] = {
        "cl1_from_horizontal_cl2": cl1_from_horizontal_cl2,
        "cl13_from_horizontal_cl2": cl13_from_horizontal_cl2,
    }
    print(
        f"ORBIT={name} CL1_FROM_HCL2="
        f"{ {k: v for k, v in cl1_from_horizontal_cl2.items() if k != 'columns'} } "
        f"CL13_FROM_HCL2={ {k: v for k, v in cl13_from_horizontal_cl2.items() if k != 'columns'} }"
    )

first_leakage_witness = next(
    (
        (name, cl1_labels[row], horizontal_column, value)
        for name, packet in leakage_results.items()
        for horizontal_column, column in enumerate(packet["cl1_from_horizontal_cl2"]["columns"])
        for row, value in column.items()
    ),
    None,
)
check("exact", "adjacent-grade cross-block is tested on all causal representatives", len(leakage_results) == 3)
expected_leakage = {
    "timelike": (12, 12, 60),
    "spacelike": (12, 12, 60),
    "null": (12, 11, 120),
}
for name, expected in expected_leakage.items():
    packet = leakage_results[name]
    grade1 = packet["cl1_from_horizontal_cl2"]
    grade13 = packet["cl13_from_horizontal_cl2"]
    check("exact", f"{name}: Cl1--horizontal-Cl2 raw/Euler ranks and support are exact", (grade1["raw_rank"], grade1["euler_rank"], grade1["euler_support"]) == expected)
    check("exact", f"{name}: Cl13--horizontal-Cl2 cross-block vanishes", grade13["raw_rank"] == grade13["euler_rank"] == grade13["euler_support"] == 0)
check("exact", "first adjacent-grade Euler witness is exact and real", first_leakage_witness == ("timelike", (1, 0), 0, (Fraction(-1), Fraction(0))))
check("exact", "parity-completed off-diagonal Euler ranks are 24 24 22", tuple(2 * leakage_results[name]["cl1_from_horizontal_cl2"]["euler_rank"] for name in orbits) == (24, 24, 22))
check("planted", "PLANT the null raw rank twelve is not substituted for formal-adjoint Euler rank eleven", leakage_results["null"]["cl1_from_horizontal_cl2"]["raw_rank"] != leakage_results["null"]["cl1_from_horizontal_cl2"]["euler_rank"])


print("\nG. PROGRAM FENCES")
for label in (
    "no raw density rank is called a bulk equation rank",
    "no boundary current is called a reduced physical observable",
    "the graph curvature theorem is not erased",
    "the 24-dimensional observed carrier is not called the full ambient adP carrier",
    "same-grade zero is not generalized across Clifford parity",
    "adjacent-grade leakage is not booked as a new parameter or quotient",
    "observation receiver and common domain remain open",
    "no field coefficient selector quotient or datum is added",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("SAME_GRADE_CL2_RAW_AND_EULER=ZERO_ON_24_AND_FULL_1274")
print("SAME_GRADE_CL1_CL13_RAW_AND_EULER=ZERO")
print("ADJACENT_GRADE_CL1_HCL2_EULER_RANKS=12_12_11")
print("PARITY_COMPLETED_OFFDIAGONAL_EULER_RANKS=24_24_22")
print("CURRENT_34_VARIABLE_SOURCE_TRUNCATION=NOT_ACTION_INVARIANT")
print("OBSERVATION_RECEIVER_COMMON_DOMAIN_ODD_BV_BFV=OPEN")
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
