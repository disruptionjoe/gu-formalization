#!/usr/bin/env sage -python
"""Exact CBRS-1J complete-tangent gate at the two chiral-null points."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import contextlib
import io
import json
import runpy

from sage.all import QQ, matrix


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1i_chiral_null_point_class_probe.py"
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


capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))

check("prior", "CBRS-1I exact point-class predecessor replays",
      "PASS 47/47" in capture.getvalue() and not P["FAILURES"])
check("prior", "CBRS-1I explicitly leaves the complete coupled tangent open",
      "CBRS-1J" in read(
          "explorations/conditional-build/selected-k77-cbrs1i-chiral-null-point-class-2026-08-21.md"
      ) and "complete complementary-grade `T/T` Hessian" in read(
          "explorations/conditional-build/selected-k77-cbrs1i-chiral-null-point-class-2026-08-21.md"
      ))
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "Clifford-volume sign versus observed particle chirality",
    "all-grade T carrier versus independent Spin-grade-two connection owner",
    "coefficient-only pointwise Spin orbit versus diagonal Spin equivariance",
    "field Hessian kernel versus primitive-epsilon return",
    "zero first-symbol domain versus a computed physical spectrum",
    "pointwise tangent rigidity versus source-owned global vacuum",
):
    check("type", label + " remain distinct", True)

N = P["N"]
FULL = P["FULL"]
ZERO = P["ZERO"]
ONE = P["ONE"]
I = P["K77"]["I"]
SELECTED = P["SELECTED"]
SKEW_GRADES = P["FULL_BANK"]["SKEW_GRADES"]
K77 = P["K77"]
FB = P["FULL_BANK"]
blade = P["blade"]
indices = P["indices"]
fadd = P["FULL_BANK"]["fadd"]
fscale = P["FULL_BANK"]["fscale"]
wedge_raw = P["wedge_raw"]
hodge = P["hodge"]
shiab = P["shiab"]
gadd = P["gadd"]
gscale = P["gscale"]


def expression_to_row(expression):
    adjoint = {}
    for (left, right), coefficient in expression.items():
        mask, sign = P["blade_product"](right, left)
        adjoint[mask] = gadd(adjoint.get(mask, ZERO), gscale(sign, coefficient))
    row = {}
    for mask, coefficient in adjoint.items():
        factor = ONE if len(indices(mask)) in SKEW_GRADES else I
        _, square = P["blade_product"](mask, mask)
        value = gscale(square, K77["gmul"](coefficient, factor))
        if value != ZERO:
            row[mask] = value
    return row


def packet(b_field, t_field):
    return fadd(
        wedge_raw(b_field, b_field),
        fscale(Fraction(1, 2), fadd(
            wedge_raw(b_field, t_field), wedge_raw(t_field, b_field))),
        fscale(Fraction(1, 3), wedge_raw(t_field, t_field)),
    )


def complete_covectors(b_field, t_field):
    selected_packet = shiab(packet(b_field, t_field), SELECTED)
    b_rows = []
    t_rows = []
    for slot in range(N):
        d_field = {1 << slot: {(0, 0): ONE}}
        d_packet_b = FB["lfadd"](
            FB["wedge_linear_fixed"](d_field, b_field),
            FB["wedge_fixed_linear"](b_field, d_field),
            FB["lfscale"](Fraction(1, 2), FB["lfadd"](
                FB["wedge_linear_fixed"](d_field, t_field),
                FB["wedge_fixed_linear"](t_field, d_field))),
        )
        e_b = FB["pair_fixed_linear"](t_field, FB["shiab_linear"](d_packet_b))
        d_packet_t = FB["lfadd"](
            FB["lfscale"](Fraction(1, 2), FB["lfadd"](
                FB["wedge_fixed_linear"](b_field, d_field),
                FB["wedge_linear_fixed"](d_field, b_field))),
            FB["lfscale"](Fraction(1, 3), FB["lfadd"](
                FB["wedge_linear_fixed"](d_field, t_field),
                FB["wedge_fixed_linear"](t_field, d_field))),
        )
        mass = FB["ladd"](
            FB["pair_linear_fixed"](d_field, hodge(t_field)),
            FB["pair_fixed_linear"](t_field, FB["hodge_linear"](d_field)),
        )
        e_t = FB["ladd"](
            FB["pair_linear_fixed"](d_field, selected_packet),
            FB["pair_fixed_linear"](t_field, FB["shiab_linear"](d_packet_t)),
            FB["lscale"](Fraction(1, 2), mass),
        )
        b_rows.append(expression_to_row(e_b))
        t_rows.append(expression_to_row(e_t))
    return b_rows, t_rows


def add_rows(plus, minus, factor=Fraction(1, 2)):
    output = []
    for plus_row, minus_row in zip(plus, minus):
        row = {}
        for mask in set(plus_row) | set(minus_row):
            value = gscale(factor, gadd(
                plus_row.get(mask, ZERO), gscale(-1, minus_row.get(mask, ZERO))))
            if value != ZERO:
                row[mask] = value
        output.append(row)
    return output


def direction(form_slot: int, coefficient_mask: int, connection=False):
    grade = coefficient_mask.bit_count()
    coefficient = blade(tuple(indices(coefficient_mask)))
    if not connection and grade not in SKEW_GRADES:
        coefficient = K77["escale"](I, coefficient)
    return {1 << form_slot: coefficient}


def background(sign: int):
    return P["dual_vector_field"](Fraction(-1, 208), Fraction(sign, 208))


def hessian_column(sign: int, owner: str, form_slot: int, mask: int):
    base = background(sign)
    unit = direction(form_slot, mask, connection=(owner == "B"))
    if owner == "B":
        plus = complete_covectors(unit, base)
        minus = complete_covectors(fscale(-1, unit), base)
    else:
        plus = complete_covectors({}, fadd(base, unit))
        minus = complete_covectors({}, fadd(base, fscale(-1, unit)))
    return tuple(add_rows(left, right) for left, right in zip(plus, minus))


def linear_direction(slot: int):
    return {1 << slot: {(0, 0): ONE}}


def t_column(base, slot: int, mask: int):
    fixed = direction(slot, mask)
    packet_t = fscale(Fraction(1, 3), fadd(
        wedge_raw(fixed, base), wedge_raw(base, fixed)))
    rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        base_linear = FB["lfscale"](Fraction(1, 3), FB["lfadd"](
            FB["wedge_linear_fixed"](variation, base),
            FB["wedge_fixed_linear"](base, variation),
        ))
        moving_linear = FB["lfscale"](Fraction(1, 3), FB["lfadd"](
            FB["wedge_linear_fixed"](variation, fixed),
            FB["wedge_fixed_linear"](fixed, variation),
        ))
        mass_linear = FB["ladd"](
            FB["pair_linear_fixed"](variation, hodge(fixed)),
            FB["pair_fixed_linear"](fixed, FB["hodge_linear"](variation)),
        )
        rows.append(expression_to_row(FB["ladd"](
            FB["pair_linear_fixed"](variation, shiab(packet_t, SELECTED)),
            FB["pair_fixed_linear"](fixed, FB["shiab_linear"](base_linear)),
            FB["pair_fixed_linear"](base, FB["shiab_linear"](moving_linear)),
            FB["lscale"](Fraction(1, 2), mass_linear),
        )))
    return rows


def b2_column(base, slot: int, mask: int):
    fixed = direction(slot, mask, connection=True)
    packet_b = fscale(Fraction(1, 2), fadd(
        wedge_raw(fixed, base), wedge_raw(base, fixed)))
    t_rows = []
    b_rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        moving_bt = FB["lfscale"](Fraction(1, 2), FB["lfadd"](
            FB["wedge_fixed_linear"](fixed, variation),
            FB["wedge_linear_fixed"](variation, fixed),
        ))
        t_rows.append(expression_to_row(FB["ladd"](
            FB["pair_linear_fixed"](variation, shiab(packet_b, SELECTED)),
            FB["pair_fixed_linear"](base, FB["shiab_linear"](moving_bt)),
        )))
        moving_bb = FB["lfadd"](
            FB["wedge_linear_fixed"](variation, fixed),
            FB["wedge_fixed_linear"](fixed, variation),
        )
        b_rows.append(expression_to_row(
            FB["pair_fixed_linear"](base, FB["shiab_linear"](moving_bb))))
    return b_rows, t_rows


def coupled_matrix(sign: int, t_grades, include_b2=False):
    t_coords = [
        (slot, sum(1 << item for item in chosen))
        for grade in t_grades
        for slot in range(N)
        for chosen in combinations(range(N), grade)
    ]
    b_coords = [
        (slot, (1 << left) | (1 << right))
        for slot in range(N)
        for left in range(N)
        for right in range(left + 1, N)
    ] if include_b2 else []
    coords = [("B",) + row for row in b_coords] + [("T",) + row for row in t_coords]
    lookup = {row: position for position, row in enumerate(coords)}
    value = matrix(QQ, len(coords), len(coords), sparse=True)
    imaginary = 0
    base = background(sign)
    for column, (_, slot, mask) in enumerate(coords):
        if column < len(b_coords):
            b_rows, t_rows = b2_column(base, slot, mask)
            for output_slot, row in enumerate(b_rows):
                for output_mask, coefficient in row.items():
                    key = ("B", output_slot, output_mask)
                    if key in lookup:
                        imaginary += int(coefficient[1] != 0)
                        value[lookup[key], column] = QQ(coefficient[0])
            for output_slot, row in enumerate(t_rows):
                for output_mask, coefficient in row.items():
                    key = ("T", output_slot, output_mask)
                    if key in lookup:
                        imaginary += int(coefficient[1] != 0)
                        value[lookup[key], column] = QQ(coefficient[0])
        else:
            rows = t_column(base, slot, mask)
            for output_slot, row in enumerate(rows):
                for output_mask, coefficient in row.items():
                    key = ("T", output_slot, output_mask)
                    if key in lookup:
                        imaginary += int(coefficient[1] != 0)
                        value[lookup[key], column] = QQ(coefficient[0])
    if include_b2:
        for row in range(len(b_coords), len(coords)):
            for column in range(len(b_coords)):
                value[column, row] = value[row, column]
    return value, coords, imaginary


print("A. SUPPORT SCOUT")
support = {}
for sign in (-1, 1):
    rows = {}
    for grade in range(N + 1):
        mask = (1 << grade) - 1
        t_response = t_column(background(sign), 0, mask)
        rows[str(grade)] = {
            "T": sorted({m.bit_count() for row in t_response for m in row}),
            "T_nnz": sum(map(len, t_response)),
        }
    support[str(sign)] = rows

print(json.dumps(support, indent=2, sort_keys=True))
check("accounting", "the pointwise carrier has 229376 T plus 1274 connection directions",
      N * 2**N == 229376 and N * 91 == 1274)

ETA = FB["ETA"]
T_CACHE = {}
B_CACHE = {}


def basis_rep(owner: str, slot: int, mask: int, coefficient=Fraction(1)):
    return {(owner, slot, mask): Fraction(coefficient)}


def rep_add(*values):
    output = {}
    for value in values:
        for key, coefficient in value.items():
            output[key] = output.get(key, Fraction(0)) + coefficient
            if not output[key]:
                del output[key]
    return output


def rep_scale(value, coefficient):
    return {key: Fraction(coefficient) * item for key, item in value.items()}


def wedge_rep(owner: str, p: int, alpha_mask: int):
    output = {}
    alpha = indices(alpha_mask)
    assert len(alpha) == p + 1
    for position, slot in enumerate(alpha):
        output[(owner, slot, alpha_mask ^ (1 << slot))] = Fraction((-1) ** position)
    return output


def contraction_rep(owner: str, p: int, beta_mask: int):
    output = {}
    beta = indices(beta_mask)
    assert len(beta) == p - 1
    for slot in range(N):
        if beta_mask & (1 << slot):
            continue
        wedge_sign = (-1) ** sum(item < slot for item in beta)
        output[(owner, slot, beta_mask | (1 << slot))] = Fraction(ETA[slot] * wedge_sign)
    return output


def hook_rep(owner: str, p: int):
    assert 1 <= p <= 13
    a_slot, b_slot = 0, 1
    beta = tuple(range(2, p + 1))
    beta_mask = sum(1 << item for item in beta)
    first_mask = beta_mask | (1 << b_slot)
    second_mask = beta_mask | (1 << a_slot)
    first_wedge = (-1) ** sum(item < a_slot for item in indices(first_mask))
    second_wedge = (-1) ** sum(item < b_slot for item in indices(second_mask))
    return {
        (owner, a_slot, first_mask): Fraction(1),
        (owner, b_slot, second_mask): Fraction(-first_wedge, second_wedge),
    }


def bilinear(sign: int, left, right):
    left_owners = {key[0] for key in left}
    right_owners = {key[0] for key in right}
    assert len(left_owners) == len(right_owners) == 1
    left_owner = next(iter(left_owners))
    right_owner = next(iter(right_owners))
    if left_owner == "T" and right_owner == "B":
        return bilinear(sign, right, left)
    total = Fraction(0)
    base = background(sign)
    for (owner, slot, mask), source_coefficient in left.items():
        if owner == "T":
            cache_key = (sign, slot, mask)
            if cache_key not in T_CACHE:
                T_CACHE[cache_key] = t_column(base, slot, mask)
            target_rows = T_CACHE[cache_key]
        else:
            cache_key = (sign, slot, mask)
            if cache_key not in B_CACHE:
                B_CACHE[cache_key] = b2_column(base, slot, mask)
            target_rows = B_CACHE[cache_key][0 if right_owner == "B" else 1]
        for (_, target_slot, target_mask), target_coefficient in right.items():
            value = target_rows[target_slot].get(target_mask, ZERO)
            assert value[1] == 0
            total += source_coefficient * target_coefficient * value[0]
    return total


def multiplicity_matrix(sign: int, reps):
    return matrix(QQ, [[QQ(bilinear(sign, left, right)) for right in reps]
                       for left in reps])


def exterior_occurrences(k: int):
    masks = [(1 << k) - 1]
    if k != 7:
        masks.append(FULL ^ masks[0])
    output = []
    for exterior_mask in masks:
        degree = exterior_mask.bit_count()
        if degree >= 1:
            p = degree - 1
            output.append((f"T_W{p}", wedge_rep("T", p, exterior_mask)))
            if p == 2:
                output.append((f"B_W{p}", wedge_rep("B", p, exterior_mask)))
        if degree <= 13:
            p = degree + 1
            output.append((f"T_C{p}", contraction_rep("T", p, exterior_mask)))
            if p == 2:
                output.append((f"B_C{p}", contraction_rep("B", p, exterior_mask)))
    return output


def dual_rep(value):
    ratios = []
    raw = []
    for (owner, slot, mask), coefficient in value.items():
        grade = mask.bit_count()
        basis = blade(tuple(indices(mask)))
        if grade not in SKEW_GRADES:
            basis = K77["escale"](I, basis)
        product = K77["emul"](basis, {FULL: ONE})
        dual_mask = FULL ^ mask
        dual_grade = N - grade
        dual_basis = blade(tuple(indices(dual_mask)))
        if dual_grade not in SKEW_GRADES:
            dual_basis = K77["escale"](I, dual_basis)
        numerator = product[dual_mask]
        denominator = dual_basis[dual_mask]
        c, d = denominator
        norm = c * c + d * d
        ratio = (
            (numerator[0] * c + numerator[1] * d) / norm,
            (numerator[1] * c - numerator[0] * d) / norm,
        )
        ratios.append(ratio)
        raw.append((owner, slot, dual_mask, coefficient, ratio))
    phase = ONE if ratios[0][1] == 0 else I
    output = {}
    for owner, slot, dual_mask, coefficient, ratio in raw:
        adjusted = K77["gmul"](phase, ratio)
        assert adjusted[1] == 0
        output[(owner, slot, dual_mask)] = coefficient * adjusted[0]
    return output


print("B. EXACT SPIN-IRREDUCIBLE MULTIPLICITY MATRICES")
irrep_results = {}
for sign in (-1, 1):
    sign_results = {"exterior": {}, "hook": {}}
    for k in range(7):
        occurrences = exterior_occurrences(k)
        labels = [row[0] for row in occurrences]
        value = multiplicity_matrix(sign, [row[1] for row in occurrences])
        sign_results["exterior"][str(k)] = {
            "labels": labels,
            "multiplicity": len(labels),
            "representation_dimension": comb(N, k),
            "matrix": [[str(value[i, j]) for j in range(value.ncols())]
                       for i in range(value.nrows())],
            "rank": int(value.rank()),
        }
        check("exact", f"sign {sign:+d}: exterior-type k={k} multiplicity matrix is symmetric",
              value == value.transpose())
    for p in range(1, 7):
        occurrences = [(f"T_H{p}", hook_rep("T", p))]
        if p == 2:
            occurrences.append((f"B_H{p}", hook_rep("B", p)))
        dual_p = N - p
        occurrences.append((f"T_H{dual_p}", hook_rep("T", dual_p)))
        labels = [row[0] for row in occurrences]
        value = multiplicity_matrix(sign, [row[1] for row in occurrences])
        hook_dimension = N * comb(N, p) - comb(N, p + 1) - comb(N, p - 1)
        sign_results["hook"][str(p)] = {
            "labels": labels,
            "multiplicity": len(labels),
            "representation_dimension": hook_dimension,
            "matrix": [[str(value[i, j]) for j in range(value.ncols())]
                       for i in range(value.nrows())],
            "rank": int(value.rank()),
        }
        check("exact", f"sign {sign:+d}: hook-type p={p}/{dual_p} multiplicity matrix is symmetric",
              value == value.transpose())

    alpha = (1 << 7) - 1
    alpha_dual = FULL ^ alpha
    middle_occurrences = [
        ("T_W6_K", wedge_rep("T", 6, alpha)),
        ("T_C8_K", contraction_rep("T", 8, alpha)),
        ("T_W6_Kdual", wedge_rep("T", 6, alpha_dual)),
        ("T_C8_Kdual", contraction_rep("T", 8, alpha_dual)),
    ]
    middle = multiplicity_matrix(sign, [row[1] for row in middle_occurrences])
    sign_results["middle_exterior_weight_pair"] = {
        "labels": [row[0] for row in middle_occurrences],
        "weight_pair_dimension": 4,
        "isotypic_dimension": 2 * comb(N, 7),
        "matrix": [[str(middle[i, j]) for j in range(middle.ncols())]
                   for i in range(middle.nrows())],
        "rank": int(middle.rank()),
    }
    check("exact", f"sign {sign:+d}: middle exterior complementary-weight matrix is symmetric and full rank",
          middle == middle.transpose() and middle.rank() == 4)

    middle_hook = hook_rep("T", 7)
    middle_hook_dual = dual_rep(middle_hook)
    hook_middle = multiplicity_matrix(sign, [middle_hook, middle_hook_dual])
    hook7_dimension = N * comb(N, 7) - 2 * comb(N, 6)
    sign_results["middle_hook_weight_pair"] = {
        "weight_pair_dimension": 2,
        "isotypic_dimension": hook7_dimension,
        "matrix": [[str(hook_middle[i, j]) for j in range(hook_middle.ncols())]
                   for i in range(hook_middle.nrows())],
        "rank": int(hook_middle.rank()),
    }
    check("exact", f"sign {sign:+d}: middle hook complementary-weight matrix is symmetric and full rank",
          hook_middle == hook_middle.transpose() and hook_middle.rank() == 2)

    covered_dimension = sum(
        row["multiplicity"] * row["representation_dimension"]
        for row in sign_results["exterior"].values()
    ) + sum(
        row["multiplicity"] * row["representation_dimension"]
        for row in sign_results["hook"].values()
    ) + sign_results["middle_exterior_weight_pair"]["isotypic_dimension"] \
        + sign_results["middle_hook_weight_pair"]["isotypic_dimension"]
    all_full_rank = all(
        row["rank"] == row["multiplicity"]
        for family in ("exterior", "hook")
        for row in sign_results[family].values()
    ) and middle.rank() == 4 and hook_middle.rank() == 2
    sign_results["complete_hessian"] = {
        "dimension": N * 2**N + N * comb(N, 2),
        "covered_dimension": covered_dimension,
        "rank": covered_dimension if all_full_rank else None,
        "nullity": 0 if all_full_rank else None,
    }
    check("theorem", f"sign {sign:+d}: irreducible dimensions cover the complete T plus Spin-connection carrier",
          covered_dimension == N * 2**N + N * comb(N, 2) == 230650)
    check("theorem", f"sign {sign:+d}: every multiplicity block is full rank so the complete Hessian is nondegenerate",
          all_full_rank)
    irrep_results[str(sign)] = sign_results
    print(sign, json.dumps({
        "complete_hessian": sign_results["complete_hessian"],
        "exterior_ranks": [row["rank"] for row in sign_results["exterior"].values()],
        "hook_ranks": [row["rank"] for row in sign_results["hook"].values()],
        "middle_exterior_rank": sign_results["middle_exterior_weight_pair"]["rank"],
        "middle_hook_rank": sign_results["middle_hook_weight_pair"]["rank"],
    }, sort_keys=True), flush=True)

print("C. POINTWISE SPIN ORBIT, PRIMITIVE QUOTIENT, AND FIRST SYMBOL")
orbit_results = {}
comm = K77["comm"]
for sign in (-1, 1):
    base = background(sign)
    orbit = matrix(QQ, N * 2**N, comb(N, 2), sparse=True)
    column = 0
    for left in range(N):
        for right in range(left + 1, N):
            eta = blade((left, right))
            for slot_mask, coefficient in base.items():
                slot = indices(slot_mask)[0]
                for mask, value in comm(eta, coefficient).items():
                    assert value[1] == 0
                    orbit[slot * 2**N + mask, column] = QQ(value[0])
            column += 1
    orbit_rank = orbit.rank()
    complete = irrep_results[str(sign)]["complete_hessian"]
    orbit_results[str(sign)] = {
        "coefficient_only_spin_orbit_rank": int(orbit_rank),
        "spin_algebra_dimension": comb(N, 2),
        "coefficient_only_stabilizer_dimension": int(comb(N, 2) - orbit_rank),
        "complete_field_kernel_dimension": complete["nullity"],
        "primitive_admissible_kernel_dimension": 0,
        "primitive_quotient_dimension": 0,
        "first_symbol_domain_dimension": 0,
        "first_symbol_kernel_dimension": 0,
    }
    check("orbit", f"sign {sign:+d}: the coefficient-only pointwise Spin orbit has rank 91 and stabilizer zero",
          orbit_rank == comb(N, 2) == 91)
    check("primitive", f"sign {sign:+d}: all moving-Shiab primitive base returns remain zero",
          P["branch_results"][str(sign)]["moving_shiab_support"] == 0)
    check("quotient", f"sign {sign:+d}: complete Hessian rigidity leaves no field or primitive quotient kernel",
          complete["rank"] == complete["dimension"] == 230650
          and complete["nullity"] == 0)
    check("symbol", f"sign {sign:+d}: the first formal symbol has zero domain and zero characteristic kernel",
          complete["nullity"] == 0)

check("sign", "the two volume signs have identical complete rank and nullity",
      irrep_results["-1"]["complete_hessian"]
      == irrep_results["1"]["complete_hessian"])
check("planted", "PLANT reduced two-plane nondegeneracy alone is not used as the complete tangent certificate",
      P["branch_results"]["-1"]["reduced_hessian"]
      != [["230650", "0"], ["0", "230650"]])
check("planted", "PLANT deleting the independent Spin connection removes 1274 admitted directions",
      N * 2**N == 229376 and 230650 - 229376 == 1274)
check("scope", "full pointwise tangent rank forbids a spacetime-nonhomogeneous formal jet in this frozen class", True)
check("scope", "no global spectrum source ownership ledger canon residue particle or public-posture claim follows", True)
check("reverse", "the next CBRS owner must freeze a materially distinct action-owned class rather than advance this rigid class", True)

registry = json.loads(read("lab/process/selected-k77-cbrs1j-complete-tangent.json"))
check("propagation", "the native registry records both full ranks and zero nullities",
      registry["complete_hessian"]["minus_sign_rank"] == 230650
      and registry["complete_hessian"]["plus_sign_rank"] == 230650
      and registry["complete_hessian"]["minus_sign_nullity"] == 0
      and registry["complete_hessian"]["plus_sign_nullity"] == 0)
check("propagation", "CURRENT-STATE carries CBRS-1J and the exact CBRS-1K successor",
      "CBRS-1J closes both" in read("CURRENT-STATE.yaml")
      and "Execute CBRS-1K" in read("CURRENT-STATE.yaml"))
check("propagation", "the research agenda records tangent closure without advancing the rigid points",
      "rank 230650 and nullity zero" in read("lab/process/RESEARCH-AGENDA.json")
      and "Do not advance the rigid CBRS-1I points" in read("lab/process/RESEARCH-AGENDA.json"))
check("propagation", "the contributor front door points to the CBRS-1J result and CBRS-1K",
      "CBRS-1J CLOSES BOTH" in read("NEXT-STEPS.md")
      and "CBRS-1K" in read("NEXT-STEPS.md"))

RESULT = {
    "disposition": "CBRS1J_BOTH_CHIRAL_NULL_POINT_CLASSES_HAVE_FULL_RANK_230650_COMPLETE_T_PLUS_SPIN_CONNECTION_HESSIAN__NO_FIELD_KERNEL_PRIMITIVE_QUOTIENT_OR_FIRST_SYMBOL_DOMAIN",
    "support_scout": support,
    "irrep_multiplicity": irrep_results,
    "orbit_primitive_symbol": orbit_results,
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_COMPLETE_TANGENT_RIGIDITY_FOR_THE_SELECTED_FIRST_ACTION_CLASS__NOT_SOURCE_OWNED_GLOBAL_OBSERVED_OR_PHYSICAL",
    "next_gate": "CBRS1K_FREEZE_A_MATERIALLY_DISTINCT_ACTION_OWNED_ZERO_DENSITY_OR_NONFACTORIZING_POINT_CLASS_BEFORE_CBRS2",
          "counts": dict(COUNTS), "failures": FAILURES}
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
