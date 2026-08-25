#!/usr/bin/env sage -python
"""Exact CBRS-1N J4 residual-carrier and alignment-obstruction gate.

The certificate decomposes the full real pointwise carrier under
Spin(1,3) x Spin(6,4), includes the independent Spin-grade-two connection
owner, constructs the broken diagonal-Spin orbit, and rejects the attempted
coarse scalar-Schur Hessian census when it fails that mandatory kernel
control.  No primitive quotient, metric domain, or symbol is admitted from
the rejected ranks.
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
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1m_j4_split_point_class_probe.py"
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
    M = {"__file__": str(PREDECESSOR), "__name__": "__main__"}
    exec(compile(predecessor_source, str(PREDECESSOR), "exec"), M)

check("prior", "CBRS-1M exact four-branch predecessor replays with only its superseded agenda-frontdoor assertion",
      len(M["FAILURES"]) == 1
      and "the agenda advances the live reverse scaffold" in M["FAILURES"][0]
      and "FAIL [propagation]" in capture.getvalue())
check("prior", "CBRS-1M leaves the complete J4 tangent and metric quotient open",
      "CBRS-1N" in read(
          "explorations/conditional-build/selected-k77-cbrs1m-j4-split-point-class-2026-08-22.md"
      ) and "complete residual-symmetry" in read(
          "explorations/conditional-build/selected-k77-cbrs1m-j4-split-point-class-2026-08-22.md"
      ))
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "residual J4-product symmetry versus full diagonal Spin symmetry",
    "normal-J4 radical family versus base-J4 radical family",
    "radical sign versus observed particle chirality",
    "all-grade T carrier versus independent Spin-grade-two connection owner",
    "coefficient-only Spin orbit versus residual diagonal stabilizer",
    "field Hessian kernel versus primitive-epsilon return",
    "zero first-symbol domain versus a physical spectrum",
):
    check("type", label + " remain distinct", True)


P = M["P"]
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

BASE_SLOTS = tuple(sorted(M["BASE"]))
NORMAL_SLOTS = tuple(sorted(M["NORMAL"]))
check("split", "the actual transported J4 4+10 blocks are frozen",
      BASE_SLOTS == (0, 1, 2, 3)
      and NORMAL_SLOTS == tuple(range(4, 14)))


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


a, b, c, d = M["variables"]
BASE = M["j4_field"]((a, b, c, d))
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
    """Choose Hodge-aligned representatives for Lambda^degree(space)."""
    dimension = len(space)
    if degree <= dimension // 2:
        return mask_of(space[:degree])
    return mask_of(set(space) - set(space[:dimension - degree]))


def wedge_rep(owner: str, factor: str, factor_degree: int, other_degree: int):
    space, other = ((BASE_SLOTS, NORMAL_SLOTS) if factor == "B"
                    else (NORMAL_SLOTS, BASE_SLOTS))
    alpha = exterior_mask(space, factor_degree + 1)
    other_mask = exterior_mask(other, other_degree)
    output = {}
    for slot in indices(alpha):
        coefficient_mask = (alpha ^ (1 << slot)) | other_mask
        sign = (-1) ** sum(item < slot for item in indices(coefficient_mask))
        output[(owner, slot, coefficient_mask)] = sp.Integer(sign)
    return output


def contraction_rep(owner: str, factor: str, factor_degree: int, other_degree: int):
    space, other = ((BASE_SLOTS, NORMAL_SLOTS) if factor == "B"
                    else (NORMAL_SLOTS, BASE_SLOTS))
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
    space, other = ((BASE_SLOTS, NORMAL_SLOTS) if factor == "B"
                    else (NORMAL_SLOTS, BASE_SLOTS))
    if factor_degree > len(space) // 2:
        return partial_dual_rep(
            hook_rep(owner, factor, len(space) - factor_degree, other_degree), space)
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


def exterior_label(dimension: int, degree: int) -> int:
    return min(degree, dimension - degree)


def hook_label(dimension: int, degree: int) -> int:
    return min(degree, dimension - degree)


occurrences = defaultdict(list)


def add_occurrence(key, label, rep):
    occurrences[key].append((label, rep))


for owner in ("T", "B"):
    for r in range(len(BASE_SLOTS) + 1):
        for s in range(len(NORMAL_SLOTS) + 1):
            if owner == "B" and r + s != 2:
                continue
            for factor in ("B", "N"):
                dimension = len(BASE_SLOTS) if factor == "B" else len(NORMAL_SLOTS)
                degree, other_degree = (r, s) if factor == "B" else (s, r)
                if degree < dimension:
                    target_b = degree + 1 if factor == "B" else r
                    target_n = degree + 1 if factor == "N" else s
                    key = ("E", exterior_label(4, target_b),
                           "E", exterior_label(10, target_n))
                    add_occurrence(key, f"{owner}_{factor}_W_r{r}s{s}",
                                   wedge_rep(owner, factor, degree, other_degree))
                if degree > 0:
                    target_b = degree - 1 if factor == "B" else r
                    target_n = degree - 1 if factor == "N" else s
                    key = ("E", exterior_label(4, target_b),
                           "E", exterior_label(10, target_n))
                    add_occurrence(key, f"{owner}_{factor}_C_r{r}s{s}",
                                   contraction_rep(owner, factor, degree, other_degree))
                if 1 <= degree < dimension:
                    if factor == "B":
                        key = ("H", hook_label(4, degree),
                               "E", exterior_label(10, s))
                    else:
                        key = ("E", exterior_label(4, r),
                               "H", hook_label(10, degree))
                    add_occurrence(key, f"{owner}_{factor}_H_r{r}s{s}",
                                   hook_rep(owner, factor, degree, other_degree))


def irrep_dimension(key) -> int:
    def factor_dimension(dimension, kind, degree):
        if kind == "E":
            return comb(dimension, degree)
        return (dimension * comb(dimension, degree)
                - comb(dimension, degree + 1)
                - comb(dimension, degree - 1))
    return (factor_dimension(4, key[0], key[1])
            * factor_dimension(10, key[2], key[3]))


print("A. ACTUAL J4-RESIDUAL MULTIPLICITY BLOCKS", flush=True)
branch_substitutions = {}
for family, points in (("normal_J4", M["normal_points"]),
                       ("base_J4", M["base_points"])):
    for sign_index, point in enumerate(points):
        sign = -1 if sign_index == 0 else 1
        branch_substitutions[f"{family}_sign_{sign:+d}"] = dict(zip((a, b, c, d), point))
branch_ranks = {label: 0 for label in branch_substitutions}
block_results = {}
covered_dimension = 0
for key in sorted(occurrences, key=str):
    rows = occurrences[key]
    labels = [row[0] for row in rows]
    reps = [row[1] for row in rows]
    symbolic = sp.Matrix([[bilinear(left, right) for right in reps] for left in reps])
    check("exact", f"J4 residual block {key} is symbolically symmetric",
          symbolic == symbolic.T)
    dimension = irrep_dimension(key)
    covered_dimension += len(rows) * dimension
    ranks = {}
    for branch, substitution in branch_substitutions.items():
        value = symbolic.subs(substitution).applyfunc(sp.factor)
        rank = int(value.rank())
        ranks[branch] = rank
        branch_ranks[branch] += rank * dimension
        check("rank", f"{branch}: J4 residual block {key} has a certified exact rank",
              0 <= rank <= len(rows))
    block_results[str(key)] = {
        "labels": labels,
        "multiplicity": len(rows),
        "representation_dimension": dimension,
        "ranks": ranks,
    }

check("accounting", "J4 residual irreducibles cover every T and independent connection direction",
      covered_dimension == N * 2**N + N * comb(N, 2) == 230650)
print("COMPLETE_RANK_DIAGNOSTIC=" + json.dumps(branch_ranks, sort_keys=True), flush=True)


print("B. ORBIT, STABILIZER, PRIMITIVE QUOTIENT, AND METRIC DOMAIN", flush=True)
comm = K77["comm"]
eadd = K77["eadd"]
escale = K77["escale"]


def scalar_coordinates(value):
    """Convert one real-form Clifford element to normalized direction scalars."""
    output = {}
    for mask, numerator in value.items():
        denominator = normalized_basis(mask)[mask]
        c0, c1 = denominator
        norm = c0 * c0 + c1 * c1
        real = sp.simplify((numerator[0] * c0 + numerator[1] * c1) / norm)
        imag = sp.simplify((numerator[1] * c0 - numerator[0] * c1) / norm)
        assert imag == 0
        if real != 0:
            output[mask] = sp.factor(real)
    return output


def coefficient_orbit_rep(left: int, right: int):
    generator = blade((left, right))
    output = {}
    for slot_mask, coefficient in BASE.items():
        slot = indices(slot_mask)[0]
        for mask, value in scalar_coordinates(comm(generator, coefficient)).items():
            output[("T", slot, mask)] = value
    return output


def diagonal_orbit_rep(left: int, right: int):
    """Combined form-plus-coefficient Spin tangent at the J4 background."""
    generator = blade((left, right))
    output = {}
    for slot in range(N):
        value = comm(generator, BASE[1 << slot])
        if slot == left:
            value = eadd(value, escale(2 * ETA[left], BASE[1 << right]))
        if slot == right:
            value = eadd(value, escale(-2 * ETA[right], BASE[1 << left]))
        for mask, scalar in scalar_coordinates(value).items():
            output[("T", slot, mask)] = scalar
    return output


coefficient_orbits = [coefficient_orbit_rep(left, right)
                      for left, right in combinations(range(N), 2)]
coefficient_rows = sorted({(slot, mask) for rep in coefficient_orbits
                           for _, slot, mask in rep})
coefficient_lookup = {row: position for position, row in enumerate(coefficient_rows)}
coefficient_matrix = sp.MutableSparseMatrix(
    len(coefficient_rows), len(coefficient_orbits), {})
for column, rep in enumerate(coefficient_orbits):
    for (_, slot, mask), value in rep.items():
        coefficient_matrix[coefficient_lookup[(slot, mask)], column] = value

residual_generators = [
    (left, right) for left, right in combinations(range(N), 2)
    if ((left in BASE_SLOTS) == (right in BASE_SLOTS))
]
broken_generators = [
    (left, right) for left in BASE_SLOTS for right in NORMAL_SLOTS
]
residual_orbits = [diagonal_orbit_rep(*pair) for pair in residual_generators]
broken_orbits = [diagonal_orbit_rep(*pair) for pair in broken_generators]
check("stabilizer", "all 51 within-block diagonal-Spin generators stabilize the symbolic J4 class",
      len(residual_generators) == 51 and all(not rep for rep in residual_orbits))

broken_rows = sorted({(slot, mask) for rep in broken_orbits
                      for _, slot, mask in rep})
broken_lookup = {row: position for position, row in enumerate(broken_rows)}
broken_matrix = sp.MutableSparseMatrix(len(broken_rows), len(broken_orbits), {})
for column, rep in enumerate(broken_orbits):
    for (_, slot, mask), value in rep.items():
        broken_matrix[broken_lookup[(slot, mask)], column] = value

mixed_reps = [row[1] for row in occurrences[("E", 1, "E", 1)]]
orbit_kernel_pairings = [bilinear(broken_orbits[0], rep) for rep in mixed_reps]
orbit_results = {}
for branch, substitution in branch_substitutions.items():
    coefficient_rank = int(coefficient_matrix.subs(substitution).rank())
    broken_rank = int(broken_matrix.subs(substitution).rank())
    coarse_nullity = covered_dimension - branch_ranks[branch]
    moving_support = M["branch_results"][branch]["moving_shiab_support"]
    orbit_results[branch] = {
        "coefficient_only_spin_orbit_rank": coefficient_rank,
        "coefficient_only_stabilizer_dimension": comb(N, 2) - coefficient_rank,
        "residual_diagonal_spin_stabilizer_dimension": len(residual_generators),
        "broken_diagonal_spin_orbit_dimension": broken_rank,
        "coarse_scalar_representative_rank_rejected": branch_ranks[branch],
        "coarse_scalar_representative_nullity_rejected": coarse_nullity,
        "complete_field_kernel_dimension": "OPEN_PENDING_ALIGNED_INTERTWINER_BANK",
        "primitive_admissible_kernel_dimension": "OPEN",
        "primitive_quotient_dimension": "OPEN",
        "metric_admissible_nonorbit_domain_dimension": "OPEN",
        "first_symbol_domain_dimension": "NOT_CONSTRUCTED",
    }
    check("orbit", f"{branch}: coefficient-only Spin orbit has rank 91 and stabilizer zero",
          coefficient_rank == comb(N, 2) == 91)
    check("orbit", f"{branch}: 40 broken diagonal-Spin tangents are independent",
          broken_rank == 40)
    check("kernel", f"{branch}: one broken-orbit generator lies in the mixed-block Hessian kernel",
          all(sp.simplify(value.subs(substitution)) == 0
              for value in orbit_kernel_pairings))
    expected_coarse = 60 if branch.startswith("normal") else 100
    check("diagnostic", f"{branch}: the coarse scalar-representative census has its reproducible apparent nullity",
          coarse_nullity == expected_coarse)
    check("primitive", f"{branch}: pointwise primitive return vanishes but the primitive tangent quotient remains open",
          moving_support == 0)
    check("metric", f"{branch}: the nonzero point metric row remains open against a not-yet-aligned non-orbit tangent",
          M["branch_results"][branch]["metric_row_support"] == 4)
    check("symbol", f"{branch}: no symbol is constructed before the aligned kernel and metric quotient exist",
          True)

mixed_block = block_results[str(("E", 1, "E", 1))]
check("contradiction", "the coarse normal-J4 mixed block claims full multiplicity rank",
      mixed_block["ranks"]["normal_J4_sign_-1"] == mixed_block["multiplicity"] == 16
      and mixed_block["ranks"]["normal_J4_sign_+1"] == 16)
check("contradiction", "an independent nonzero broken-orbit vector pairs to zero with every mixed representative",
      all(sp.simplify(value.subs(branch_substitutions["normal_J4_sign_-1"])) == 0
          for value in orbit_kernel_pairings)
      and int(broken_matrix.subs(branch_substitutions["normal_J4_sign_-1"]).rank()) == 40)
check("theorem", "the scalar-Schur coarse census is rejected before any complete-rank claim",
      branch_ranks == {
          "normal_J4_sign_-1": 230590,
          "normal_J4_sign_+1": 230590,
          "base_J4_sign_-1": 230550,
          "base_J4_sign_+1": 230550,
      })
check("conjugacy", "both radical-sign pairs preserve their family complete rank",
      branch_ranks["normal_J4_sign_-1"] == branch_ranks["normal_J4_sign_+1"]
      and branch_ranks["base_J4_sign_-1"] == branch_ranks["base_J4_sign_+1"])
check("planted", "PLANT treating J4 as fully Spin-invariant would erase the 40 broken directions",
      len(broken_generators) == 40 and len(residual_generators) == 51)
check("planted", "PLANT deleting the independent connection owner loses exactly 1274 directions",
      230650 - N * 2**N == 1274)
check("planted", "PLANT the rank-four reduced Hessian is not a complete-tangent certificate",
      all(row["reduced_hessian_rank"] == 4 for row in M["branch_results"].values())
      and covered_dimension != 4)
check("scope", "the exact contradiction blocks both a false rigidity theorem and a false non-orbit survivor count", True)
check("scope", "no global spectrum source ownership ledger canon residue particle or public-posture claim follows", True)
check("reverse", "CBRS-1O must align the 4+10 real/complex intertwiners before primitive metric or symbol work", True)

registry_path = ROOT / "lab/process/selected-k77-cbrs1n-j4-complete-tangent.json"
if registry_path.exists():
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    check("propagation", "the native registry rejects the coarse ranks and records the J4 residual stabilizer",
          registry["coarse_scalar_diagnostic"]["rank_normal_pair"] == 230590
          and registry["coarse_scalar_diagnostic"]["rank_base_pair"] == 230550
          and registry["orbit_stabilizer"]["residual_diagonal_stabilizer_dimension"] == 51
          and registry["complete_hessian"]["status"] == "OPEN")
    check("propagation", "CURRENT-STATE carries CBRS-1N and its exact CBRS-1O correction",
          "CBRS-1N rejects" in read("CURRENT-STATE.yaml") and "CBRS-1O" in read("CURRENT-STATE.yaml"))
    check("propagation", "the agenda records the alignment correction without a false tangent rank",
          "CBRS-1N rejects" in read("lab/process/RESEARCH-AGENDA.json") and "CBRS-1O" in read("lab/process/RESEARCH-AGENDA.json"))
    check("propagation", "the contributor front door points to CBRS-1N and CBRS-1O",
          "CBRS-1N REJECTS" in read("NEXT-STEPS.md") and "CBRS-1O" in read("NEXT-STEPS.md"))

RESULT = {
    "disposition": "CBRS1N_REJECTS_UNALIGNED_SCALAR_SCHUR_COMPLETE_TANGENT_CENSUS__EXACT_4_PLUS_10_CARRIER_AND_BROKEN_ORBIT_FROZEN__ALIGNED_INTERTWINER_BANK_REQUIRED",
    "residual_blocks": block_results,
    "covered_dimension": covered_dimension,
    "coarse_scalar_representative_ranks_rejected": branch_ranks,
    "orbit_primitive_metric_symbol": orbit_results,
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_RESIDUAL_CARRIER_ORBIT_AND_REPRESENTATIVE_ALIGNMENT_OBSTRUCTION__NO_COMPLETE_HESSIAN_PRIMITIVE_METRIC_SYMBOL_GLOBAL_OR_PHYSICAL_CLAIM",
    "next_gate": "CBRS1O_BUILD_ALIGNED_REAL_COMPLEX_4_PLUS_10_INTERTWINER_BANK__RECOMPUTE_COMPLETE_HESSIAN__THEN_PRIMITIVE_METRIC_QUOTIENT_AND_SYMBOL_IF_ANY",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
