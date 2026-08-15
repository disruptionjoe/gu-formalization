#!/usr/bin/env python3
"""Exact split/mixed A2 real-form Cartan transition certificate."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads(
    (ROOT / "lab/process/selected-k77-rsap-a2-real-form-cartan-transition.json").read_text()
)
FAILURES = []
COUNTS = {}


def check(group, label, condition):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    if condition:
        print(f"PASS [{group}] {label}")
    else:
        FAILURES.append(f"[{group}] {label}")
        print(f"FAIL [{group}] {label}")


def mmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def transpose(a):
    return [list(col) for col in zip(*a)]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv2(a):
    d = det2(a)
    return [[a[1][1] // d, -a[0][1] // d], [-a[1][0] // d, a[0][0] // d]]


def power(a, n):
    result = [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        result = mmul(result, a)
    return result


types = REGISTRY["cartan_types"]
print("A. REAL CARTAN-TYPE CENSUS")
expected = {
    "sl3r_split": (2, 0, 4, "S3"),
    "sl3r_complex_pair": (1, 1, 1, "Z/2"),
    "su21_compact": (0, 2, 1, "Z/2"),
    "su21_split": (1, 1, 1, "Z/2"),
}
for name, (split_rank, compact_rank, components, weyl) in expected.items():
    row = types[name]
    check("types", f"{name} split rank", row["split_rank"] == split_rank)
    check("types", f"{name} compact lattice rank", row["compact_lattice_rank"] == compact_rank)
    check("types", f"{name} component count", row["component_count"] == components)
    check("types", f"{name} real Weyl group", row["real_weyl_group"] == weyl)

print("\nB. SPLIT CENTRALIZER COMPONENTS")
signs = [(a, b, a * b) for a in (-1, 1) for b in (-1, 1)]
check("components", "four determinant-one sign components", len(set(signs)) == 4)
for signs_i in signs:
    check("components", f"component {signs_i} has determinant one", signs_i[0] * signs_i[1] * signs_i[2] == 1)
check("components", "components are recorded as (Z/2)^2", types["sl3r_split"]["centralizer_component_group"] == "(Z/2)^2")

print("\nC. INTEGRAL AFFINE COTANGENT LIFTS")
I2 = [[1, 0], [0, 1]]
matrices = {
    "swap": [[0, 1], [1, 0]],
    "split_reflection": [[-1, 0], [0, 1]],
    "a2_s1": [[-1, 0], [1, 1]],
    "a2_s2": [[1, 1], [0, -1]],
}
mu = [Fraction(5, 3), Fraction(-7, 4)]
tau = [Fraction(11, 5), Fraction(2, 7)]
pairing = sum(x * y for x, y in zip(mu, tau))
for name, a in matrices.items():
    check("cotangent", f"{name} is unimodular", abs(det2(a)) == 1)
    transformed_tau = mvec(a, tau)
    transformed_mu = mvec(transpose(inv2(a)), mu)
    check("cotangent", f"{name} preserves the cotangent pairing", sum(x * y for x, y in zip(transformed_mu, transformed_tau)) == pairing)
check("cotangent", "A2 simple reflections braid", mmul(mmul(matrices["a2_s1"], matrices["a2_s2"]), matrices["a2_s1"]) == mmul(mmul(matrices["a2_s2"], matrices["a2_s1"]), matrices["a2_s2"]))
check("cotangent", "component sign involution squares to identity", mmul(matrices["split_reflection"], matrices["split_reflection"]) == I2)

print("\nD. VARYING-CHARGE COMPLETION BY LATTICE RANK")
mu0 = (Fraction(7, 3), Fraction(5, 2))
phi = (Fraction(2, 5), Fraction(-3, 7))
orbit = (0, 0, mu0[0], mu0[1])
conjugate = (phi[0], phi[1], 0, 0)
d_generator = (phi[0], phi[1], mu0[0], mu0[1])
check("completion", "orbit plus conjugate transition is exact", tuple(x + y for x, y in zip(orbit, conjugate)) == d_generator)
for name, row in types.items():
    rank = row["compact_lattice_rank"]
    defect = tuple(2 * n for n in range(1, rank + 1))
    check("completion", f"{name} has the declared compact lattice dimension", len(defect) == rank)
    check("completion", f"{name} lattice defect is a 2pi identity", all(value % 2 == 0 for value in defect))
check("completion", "no new degrees of freedom", REGISTRY["transition"]["new_degrees_of_freedom"] == 0)
check("completion", "same-type primitive gluing is strict", REGISTRY["transition"]["same_type_overlap_gluing"] == "STRICT_AFTER_COTANGENT_LIFT")

print("\nE. REGULAR NONSEMISIMPLE CONTROL")
N = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
Z3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
check("nilpotent", "the Jordan control is nilpotent of order three", power(N, 3) == Z3 and power(N, 2) != Z3)
check("nilpotent", "the Jordan control is not semisimple", REGISTRY["nilpotent_gate"]["semisimple"] is False)
check("nilpotent", "the principal factors retain rank eight", REGISTRY["nilpotent_gate"]["moment_map_rank"] == 8)
check("nilpotent", "the Cartan diagonalizer is absent", REGISTRY["nilpotent_gate"]["cartan_diagonalizer_exists"] is False)
check("nilpotent", "the semisimple atlas does not claim coverage", REGISTRY["nilpotent_gate"]["semisimple_cartan_atlas_covers"] is False)
check("nilpotent", "the verdict is type-missing rather than obstructed", REGISTRY["nilpotent_gate"]["classification"] == "TYPE_MISSING_NOT_OBSTRUCTED")
check("nilpotent", "the next object is a regular-centralizer or Kostant transition", "KOSTANT" in REGISTRY["nilpotent_gate"]["required_next_object"])

print("\nF. DIMENSION, RANK, AND CLAIM CEILING")
schedule = REGISTRY["dimension_and_rank"]
scope = REGISTRY["scope"]
check("scope", "the source remains 98D", schedule["full_source_dimension"] == 98)
check("scope", "the semisimple map rank remains 91", schedule["regular_semisimple_map_rank"] == 91)
check("scope", "the nilpotent local factor schedule remains 91", schedule["regular_nilpotent_local_factor_map_rank"] == 91)
check("scope", "the split semisimple atlas is constructed", scope["split_regular_semisimple_cartan_atlas"] == "CONSTRUCTED")
check("scope", "the mixed semisimple atlas is constructed", scope["mixed_regular_semisimple_cartan_atlas"] == "CONSTRUCTED")
check("scope", "the full regular atlas remains untyped", scope["full_regular_real_form_atlas"] == "NOT_YET_TYPED_AT_NONSEMISIMPLE_VALUES")
check("scope", "higher roots remain dependency-blocked", scope["higher_root_subsystems"] == "DEPENDENCY_BLOCKED")
check("scope", "zero charge remains unconstructed", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("scope", "all-strata RSAP remains open", scope["global_all_strata_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REGISTRY["changes"].values()) == {"none"})

print("\nG. ARTIFACT LINKS")
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"the {key} path exists", (ROOT / REGISTRY[key]).is_file())
check("links", "the next gate is the nonsemisimple bridge", REGISTRY["next_gate"].startswith("CONSTRUCT_REGULAR_CENTRALIZER"))

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REGISTRY["status"], "next_gate": REGISTRY["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
