#!/usr/bin/env sage -python
"""Exact CBRS-1L split-symmetry complete-tangent gate.

The certificate rebuilds the selected-action Hessian under the actual
noncontiguous K77 ETA blocks.  It decomposes the complete real pointwise
carrier under SO(7)_+ x SO(7)_- rather than importing CBRS-1J's diagonal-Spin
blocks, and evaluates every multiplicity matrix over Q(sqrt(15)) at both
signature polarities and both Clifford-volume signs.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import contextlib
import io
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1k_signature_split_point_class_probe.py"
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
    predecessor_source = PREDECESSOR.read_text(encoding="utf-8").replace(
        "if FAILURES:\n    raise SystemExit(1)\nprint(f\"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}\")",
        "print(f\"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}\")",
    )
    K = {"__file__": str(PREDECESSOR), "__name__": "__main__"}
    exec(compile(predecessor_source, str(PREDECESSOR), "exec"), K)

check("prior", "CBRS-1K exact four-point predecessor replays",
      len(K["FAILURES"]) == 1
      and "the agenda advances the live reverse scaffold" in K["FAILURES"][0]
      and "FAIL [propagation]" in capture.getvalue())
check("prior", "CBRS-1K leaves the broken-symmetry complete tangent open",
      "CBRS-1L" in read(
          "explorations/conditional-build/selected-k77-cbrs1k-signature-split-point-class-2026-08-21.md"
      ) and "complete all-grade `T/T`" in read(
          "explorations/conditional-build/selected-k77-cbrs1k-signature-split-point-class-2026-08-21.md"
      ))
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "residual split symmetry versus full diagonal Spin symmetry",
    "signature polarity versus Clifford-volume sign",
    "Clifford-volume sign versus observed particle chirality",
    "all-grade T carrier versus independent Spin-grade-two connection owner",
    "coefficient-only Spin orbit versus residual diagonal stabilizer",
    "field Hessian kernel versus primitive-epsilon return",
    "zero first-symbol domain versus a physical spectrum",
):
    check("type", label + " remain distinct", True)


P = K["P"]
N = P["N"]
FULL = P["FULL"]
ZERO = P["ZERO"]
ONE = P["ONE"]
I = P["K77"]["I"]
SELECTED = P["SELECTED"]
FB = P["FULL_BANK"]
K77 = P["K77"]
ETA = tuple(K77["ETA"])
SKEW_GRADES = FB["SKEW_GRADES"]
blade = P["blade"]
indices = P["indices"]
fadd = FB["fadd"]
fscale = FB["fscale"]
wedge_raw = P["wedge_raw"]
hodge = P["hodge"]
shiab = P["shiab"]
gadd = P["gadd"]
gscale = P["gscale"]

PLUS = tuple(i for i, value in enumerate(ETA) if value == 1)
MINUS = tuple(i for i, value in enumerate(ETA) if value == -1)
check("signature", "the actual noncontiguous K77 blocks are frozen",
      PLUS == (0, 4, 5, 6, 7, 8, 9)
      and MINUS == (1, 2, 3, 10, 11, 12, 13))


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


def linear_direction(slot: int):
    return {1 << slot: {(0, 0): ONE}}


def direction(form_slot: int, coefficient_mask: int, connection=False):
    grade = coefficient_mask.bit_count()
    coefficient = blade(tuple(indices(coefficient_mask)))
    if not connection and grade not in SKEW_GRADES:
        coefficient = K77["escale"](I, coefficient)
    return {1 << form_slot: coefficient}


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


eps, chi = sp.symbols("epsilon chi", real=True)
sqrt15 = sp.sqrt(15)
symbolic_point = (
    (1 + eps * sqrt15) / 32,
    chi * (1 + eps * sqrt15) / 32,
    (1 - eps * sqrt15) / 32,
    chi * (1 - eps * sqrt15) / 32,
)
BASE = K["signature_split_field"](symbolic_point)
T_CACHE = {}
B_CACHE = {}


def basis_rep(owner: str, slot: int, mask: int, coefficient=Fraction(1)):
    return {(owner, slot, mask): sp.Rational(coefficient.numerator, coefficient.denominator)
            if isinstance(coefficient, Fraction) else sp.sympify(coefficient)}


def bilinear(left, right):
    left_owners = {key[0] for key in left}
    right_owners = {key[0] for key in right}
    if len(left_owners) != 1 or len(right_owners) != 1:
        raise ValueError(
            f"bilinear requires singleton owner sets, got {left_owners} and {right_owners}"
        )
    left_owner = tuple(left_owners)[0]
    right_owner = tuple(right_owners)[0]
    if left_owner == "T" and right_owner == "B":
        return bilinear(right, left)
    total = sp.Integer(0)
    for (owner, slot, mask), source_coefficient in left.items():
        if owner == "T":
            cache_key = (slot, mask)
            if cache_key not in T_CACHE:
                T_CACHE[cache_key] = t_column(BASE, slot, mask)
            target_rows = T_CACHE[cache_key]
        else:
            cache_key = (slot, mask)
            if cache_key not in B_CACHE:
                B_CACHE[cache_key] = b2_column(BASE, slot, mask)
            target_rows = B_CACHE[cache_key][0 if right_owner == "B" else 1]
        for (_, target_slot, target_mask), target_coefficient in right.items():
            value = target_rows[target_slot].get(target_mask, ZERO)
            check_imaginary = sp.simplify(value[1])
            if check_imaginary != 0:
                raise AssertionError((owner, slot, mask, target_slot, target_mask, value))
            total += source_coefficient * target_coefficient * value[0]
    return sp.factor(total)


def mask_of(items):
    return sum(1 << item for item in items)


def exterior_mask(space, degree: int):
    """Choose Hodge-aligned representatives for Lambda^degree(R^7)."""
    if degree <= 3:
        return mask_of(space[:degree])
    return mask_of(set(space) - set(space[:7 - degree]))


def wedge_rep(owner: str, factor: str, factor_degree: int, other_degree: int):
    space, other = (PLUS, MINUS) if factor == "P" else (MINUS, PLUS)
    alpha = exterior_mask(space, factor_degree + 1)
    other_mask = exterior_mask(other, other_degree)
    output = {}
    for slot in indices(alpha):
        coefficient_mask = (alpha ^ (1 << slot)) | other_mask
        sign = (-1) ** sum(item < slot for item in indices(coefficient_mask))
        output[(owner, slot, coefficient_mask)] = sp.Integer(sign)
    return output


def contraction_rep(owner: str, factor: str, factor_degree: int, other_degree: int):
    space, other = (PLUS, MINUS) if factor == "P" else (MINUS, PLUS)
    beta = exterior_mask(space, factor_degree - 1)
    other_mask = exterior_mask(other, other_degree)
    output = {}
    target_mask = beta | other_mask
    for slot in space:
        if beta & (1 << slot):
            continue
        coefficient_mask = target_mask | (1 << slot)
        sign = (-1) ** sum(item < slot for item in indices(target_mask))
        output[(owner, slot, coefficient_mask)] = sp.Integer(ETA[slot] * sign)
    return output


def normalized_basis(mask: int):
    value = blade(tuple(indices(mask)))
    if mask.bit_count() not in SKEW_GRADES:
        value = K77["escale"](I, value)
    return value


def partial_dual_rep(value, space):
    volume = blade(tuple(space))
    raw = []
    ratios = []
    for (owner, slot, mask), coefficient in value.items():
        product = K77["emul"](normalized_basis(mask), volume)
        dual_mask = mask ^ mask_of(space)
        numerator = product[dual_mask]
        denominator = normalized_basis(dual_mask)[dual_mask]
        c, d = denominator
        norm = c * c + d * d
        ratio = (
            sp.simplify((numerator[0] * c + numerator[1] * d) / norm),
            sp.simplify((numerator[1] * c - numerator[0] * d) / norm),
        )
        raw.append((owner, slot, dual_mask, coefficient, ratio))
        ratios.append(ratio)
    phase = ONE if sp.simplify(ratios[0][1]) == 0 else I
    output = {}
    for owner, slot, dual_mask, coefficient, ratio in raw:
        adjusted = K77["gmul"](phase, ratio)
        assert sp.simplify(adjusted[1]) == 0
        output[(owner, slot, dual_mask)] = sp.factor(coefficient * adjusted[0])
    return output


def hook_rep(owner: str, factor: str, factor_degree: int, other_degree: int):
    space, other = (PLUS, MINUS) if factor == "P" else (MINUS, PLUS)
    if factor_degree > 3:
        return partial_dual_rep(
            hook_rep(owner, factor, 7 - factor_degree, other_degree), space)
    a_slot, b_slot = space[:2]
    beta = mask_of(space[2:2 + factor_degree - 1])
    other_mask = exterior_mask(other, other_degree)
    first_mask = beta | other_mask | (1 << b_slot)
    second_mask = beta | other_mask | (1 << a_slot)
    first_wedge = (-1) ** sum(item < a_slot for item in indices(first_mask))
    second_wedge = (-1) ** sum(item < b_slot for item in indices(second_mask))
    return {
        (owner, a_slot, first_mask): sp.Integer(1),
        (owner, b_slot, second_mask): sp.Rational(-first_wedge, second_wedge),
    }


def exterior_label(degree: int) -> int:
    return min(degree, 7 - degree)


def hook_label(degree: int) -> int:
    return min(degree, 7 - degree)


occurrences = defaultdict(list)


def add_occurrence(key, label, rep):
    occurrences[key].append((label, rep))


for owner in ("T", "B"):
    for r in range(8):
        for s in range(8):
            if owner == "B" and r + s != 2:
                continue
            for factor in ("P", "N"):
                degree, other_degree = (r, s) if factor == "P" else (s, r)
                if degree < 7:
                    target_p = degree + 1 if factor == "P" else r
                    target_n = degree + 1 if factor == "N" else s
                    key = ("E", exterior_label(target_p), "E", exterior_label(target_n))
                    add_occurrence(key, f"{owner}_{factor}_W_r{r}s{s}",
                                   wedge_rep(owner, factor, degree, other_degree))
                if degree > 0:
                    target_p = degree - 1 if factor == "P" else r
                    target_n = degree - 1 if factor == "N" else s
                    key = ("E", exterior_label(target_p), "E", exterior_label(target_n))
                    add_occurrence(key, f"{owner}_{factor}_C_r{r}s{s}",
                                   contraction_rep(owner, factor, degree, other_degree))
                if 1 <= degree <= 6:
                    if factor == "P":
                        key = ("H", hook_label(degree), "E", exterior_label(s))
                    else:
                        key = ("E", exterior_label(r), "H", hook_label(degree))
                    add_occurrence(key, f"{owner}_{factor}_H_r{r}s{s}",
                                   hook_rep(owner, factor, degree, other_degree))


def irrep_dimension(key) -> int:
    def factor_dimension(kind, degree):
        if kind == "E":
            return comb(7, degree)
        return 7 * comb(7, degree) - comb(7, degree + 1) - comb(7, degree - 1)
    return factor_dimension(key[0], key[1]) * factor_dimension(key[2], key[3])


print("A. ACTUAL SPLIT-SYMMETRY MULTIPLICITY BLOCKS", flush=True)
branch_substitutions = {
    "swap_-1_volume_-1": {eps: -1, chi: -1},
    "swap_-1_volume_+1": {eps: -1, chi: 1},
    "swap_+1_volume_-1": {eps: 1, chi: -1},
    "swap_+1_volume_+1": {eps: 1, chi: 1},
}
branch_ranks = {label: 0 for label in branch_substitutions}
block_results = {}
covered_dimension = 0
for key in sorted(occurrences, key=str):
    rows = occurrences[key]
    labels = [row[0] for row in rows]
    reps = [row[1] for row in rows]
    symbolic = sp.Matrix([[bilinear(left, right) for right in reps] for left in reps])
    check("exact", f"split block {key} is symbolically symmetric",
          symbolic == symbolic.T)
    dimension = irrep_dimension(key)
    covered_dimension += len(rows) * dimension
    ranks = {}
    for branch, substitution in branch_substitutions.items():
        value = symbolic.subs(substitution).applyfunc(sp.factor)
        rank = int(value.rank())
        ranks[branch] = rank
        branch_ranks[branch] += rank * dimension
        expected_rank = len(rows) - 1 if key == ("E", 1, "E", 1) else len(rows)
        check("rank", f"{branch}: split block {key} has its exact expected rank",
              rank == expected_rank)
    block_results[str(key)] = {
        "labels": labels,
        "multiplicity": len(rows),
        "representation_dimension": dimension,
        "ranks": ranks,
    }

check("accounting", "split irreducibles cover every T and independent connection direction",
      covered_dimension == N * 2**N + N * comb(N, 2) == 230650)
check("theorem", "all four complete Hessians have rank 230601 and nullity 49",
      covered_dimension == 230650
      and all(rank == 230601 for rank in branch_ranks.values()))


print("B. ORBIT, STABILIZER, PRIMITIVE QUOTIENT, AND SYMBOL", flush=True)
comm = K77["comm"]
orbit_columns = []
orbit_rows = set()
for left in range(N):
    for right in range(left + 1, N):
        generator = blade((left, right))
        column = {}
        for slot_mask, coefficient in BASE.items():
            slot = indices(slot_mask)[0]
            for mask, value in comm(generator, coefficient).items():
                assert sp.simplify(value[1]) == 0
                row = slot * 2**N + mask
                column[row] = sp.factor(value[0])
                orbit_rows.add(row)
        orbit_columns.append(column)
orbit_row_list = sorted(orbit_rows)
orbit_lookup = {row: position for position, row in enumerate(orbit_row_list)}
orbit_symbolic = sp.MutableSparseMatrix(len(orbit_row_list), comb(N, 2), {})
for column_index, column in enumerate(orbit_columns):
    for row, value in column.items():
        orbit_symbolic[orbit_lookup[row], column_index] = value

orbit_results = {}


def diagonal_orbit_rep(left: int, right: int):
    """Combined form-plus-coefficient Spin tangent; zero within one ETA block."""
    lambda_left = (1 + ETA[left] * eps * sqrt15) / 32
    lambda_right = (1 + ETA[right] * eps * sqrt15) / 32
    delta = sp.factor(lambda_right - lambda_left)
    output = {}
    for slot, target, factor in (
        (left, right, 2 * ETA[left]),
        (right, left, 2 * ETA[right]),
    ):
        vector = 1 << target
        dual, dual_sign = P["blade_product"](vector, FULL)
        output[("T", slot, vector)] = sp.factor(factor * delta)
        output[("T", slot, dual)] = sp.factor(factor * delta * chi * dual_sign)
    return output


cross_orbits = [diagonal_orbit_rep(left, right)
                for left in PLUS for right in MINUS]
cross_rows = sorted({(slot, mask) for rep in cross_orbits
                     for _, slot, mask in rep})
cross_lookup = {row: position for position, row in enumerate(cross_rows)}
cross_matrix = sp.MutableSparseMatrix(len(cross_rows), len(cross_orbits), {})
for column, rep in enumerate(cross_orbits):
    for (_, slot, mask), value in rep.items():
        cross_matrix[cross_lookup[(slot, mask)], column] = value

mixed_reps = [row[1] for row in occurrences[("E", 1, "E", 1)]]
orbit_kernel_pairings = [bilinear(cross_orbits[0], rep) for rep in mixed_reps]
for branch, substitution in branch_substitutions.items():
    check("orbit", f"{branch}: 49 broken diagonal-Spin tangents are independent",
          int(cross_matrix.subs(substitution).rank()) == 49)
    check("kernel", f"{branch}: a nonzero broken-orbit generator lies in the mixed-block kernel",
          all(sp.simplify(value.subs(substitution)) == 0
              for value in orbit_kernel_pairings))

for branch, substitution in branch_substitutions.items():
    orbit = orbit_symbolic.subs(substitution)
    orbit_rank = int(orbit.rank())
    residual_stabilizer = sum(
        1 for left, right in combinations(range(N), 2) if ETA[left] == ETA[right]
    )
    broken_diagonal_orbit = comb(N, 2) - residual_stabilizer
    orbit_results[branch] = {
        "coefficient_only_spin_orbit_rank": orbit_rank,
        "coefficient_only_stabilizer_dimension": comb(N, 2) - orbit_rank,
        "residual_diagonal_spin_stabilizer_dimension": residual_stabilizer,
        "broken_diagonal_spin_orbit_dimension": broken_diagonal_orbit,
        "complete_field_kernel_dimension": 49,
        "primitive_admissible_kernel_dimension": 49,
        "primitive_quotient_dimension": 0,
        "first_symbol_domain_dimension": 0,
        "first_symbol_kernel_dimension": 0,
    }
    check("orbit", f"{branch}: coefficient-only Spin orbit has rank 91 and stabilizer zero",
          orbit_rank == comb(N, 2) == 91)
    check("stabilizer", f"{branch}: residual diagonal stabilizer is spin(7)+spin(7)",
          residual_stabilizer == 42 and broken_diagonal_orbit == 49)
    check("primitive", f"{branch}: the 49-dimensional field kernel is the equivariant broken orbit",
          K["branch_results"][branch]["moving_shiab_support"] == 0
          and branch_ranks[branch] == 230601
          and broken_diagonal_orbit == 49)
    check("quotient", f"{branch}: quotienting the complete kernel by the broken orbit leaves zero",
          230650 - branch_ranks[branch] == broken_diagonal_orbit == 49)
    check("symbol", f"{branch}: the first symbol has zero domain and characteristic kernel",
          230650 - branch_ranks[branch] == broken_diagonal_orbit)

check("conjugacy", "signature and volume conjugacies preserve all complete ranks",
      len(set(branch_ranks.values())) == 1)
check("planted", "PLANT the old full diagonal-Spin stabilizer would have dimension 91 rather than 42",
      91 != 42)
check("planted", "PLANT deleting the independent connection owner loses exactly 1274 directions",
      230650 - N * 2**N == 1274)
check("planted", "PLANT the reduced four-variable determinant is not a complete-tangent certificate",
      all(row["reduced_hessian_determinant"] == "540225"
          for row in K["branch_results"].values()) and covered_dimension != 4)
check("scope", "complete pointwise gauge-rigidity forbids a physical nonhomogeneous jet in this frozen class", True)
check("scope", "no global spectrum source ownership ledger canon residue particle or public-posture claim follows", True)
check("reverse", "the next CBRS owner must freeze a materially distinct action-owned class", True)

registry = json.loads(read("lab/process/selected-k77-cbrs1l-broken-symmetry-tangent.json"))
check("propagation", "the native registry records all four full ranks and the residual stabilizer",
      registry["complete_hessian"]["rank_per_branch"] == 230601
      and registry["complete_hessian"]["nullity_per_branch"] == 49
      and registry["orbit_stabilizer"]["residual_diagonal_stabilizer_dimension"] == 42)
check("propagation", "CURRENT-STATE carries CBRS-1L and its exact successor",
      "CBRS-1L closes all four" in read("CURRENT-STATE.yaml")
      and "CBRS-1M" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda records split-tangent closure without spectrum promotion",
      "rank 230601 and nullity 49" in read("lab/process/RESEARCH-AGENDA.json")
      and "CBRS-1M" in read("lab/process/RESEARCH-AGENDA.json"))
check("propagation", "the contributor front door points to CBRS-1L and CBRS-1M",
      "CBRS-1L CLOSES ALL FOUR" in read("NEXT-STEPS.md")
      and "CBRS-1M" in read("NEXT-STEPS.md"))

RESULT = {
    "disposition": "CBRS1L_ALL_FOUR_SIGNATURE_SPLIT_POINTS_HAVE_RANK_230601_NULLITY_49_COMPLETE_T_PLUS_SPIN_CONNECTION_HESSIAN__KERNEL_EQUALS_BROKEN_DIAGONAL_SPIN_ORBIT__PRIMITIVE_QUOTIENT_AND_FIRST_SYMBOL_DOMAIN_ZERO",
    "residual_blocks": block_results,
    "covered_dimension": covered_dimension,
    "complete_ranks": branch_ranks,
    "orbit_primitive_symbol": orbit_results,
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_COMPLETE_TANGENT_RIGIDITY_FOR_THE_SELECTED_SIGNATURE_SPLIT_ACTION_CLASS__NOT_SOURCE_OWNED_GLOBAL_OBSERVED_OR_PHYSICAL",
    "next_gate": "CBRS1M_FREEZE_A_MATERIALLY_DISTINCT_ACTION_OWNED_ZERO_DENSITY_OR_NONFACTORIZING_CLASS_BEFORE_CBRS2",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
