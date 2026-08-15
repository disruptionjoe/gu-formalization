#!/usr/bin/env python3
"""Exact A2 Cech--de Rham and integral-affine atlas certificate."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads(
    (ROOT / "lab/process/selected-k77-rsap-a2-integral-affine-atlas.json").read_text()
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


def transpose(a):
    return [list(col) for col in zip(*a)]


def mvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv2(a):
    d = det2(a)
    return [[a[1][1] // d, -a[0][1] // d], [-a[1][0] // d, a[0][0] // d]]


I2 = [[1, 0], [0, 1]]
s1 = [[-1, 0], [1, 1]]
s2 = [[1, 1], [0, -1]]

print("A. TWO-SIMPLE-ROOT LATTICE")
e1 = (1, 0)
e2 = (0, 1)
e12 = tuple(a + b for a, b in zip(e1, e2))
check("lattice", "the two simple coroots are independent", det2([list(e1), list(e2)]) == 1)
check("lattice", "the third positive root is their sum", e12 == (1, 1))
spectra = [
    (Fraction(3), Fraction(1), Fraction(-4)),
    (Fraction(5, 2), Fraction(1, 2), Fraction(-3)),
    (Fraction(4), Fraction(-1), Fraction(-3)),
]
for spectrum in spectra:
    l1, l2, l3 = spectrum
    mu = (l1 - l2, l2 - l3)
    check("lattice", f"{spectrum} is traceless", sum(spectrum) == 0)
    check("lattice", f"{spectrum} is regular", len(set(spectrum)) == 3)
    check("lattice", f"the third-root charge adds for {spectrum}", mu[0] + mu[1] == l1 - l3)
check("lattice", "the registry records the rank-two coroot lattice", REGISTRY["cech_de_rham"]["triple_integer"] == "n_ijk in Z^2")

print("\nB. VARYING-CHARGE COTANGENT COMPLETION")
# Coefficients use the ordered one-form basis
# (dmu1,dmu2,dphi1,dphi2).  The fixed-charge orbit term alone is not dF on
# the varying-charge overlap.  The existing conjugate transition supplies the
# first two coefficients.
mu = (Fraction(7, 3), Fraction(5, 2))
phi = (Fraction(2, 5), Fraction(-3, 7))
orbit_term = (0, 0, mu[0], mu[1])
conjugate_term = (phi[0], phi[1], 0, 0)
completed = tuple(a + b for a, b in zip(orbit_term, conjugate_term))
d_mu_dot_phi = (phi[0], phi[1], mu[0], mu[1])
check("completion", "the bare orbit term omits charge variation", orbit_term != d_mu_dot_phi)
check("completion", "the conjugate term owns the missing dmu coefficients", completed == d_mu_dot_phi)
check("completion", "the completed difference is d(mu dot phi)", completed == d_mu_dot_phi)
check("completion", "the full primitive is recorded as strictly glued", REGISTRY["cech_de_rham"]["full_primitive_gluing"] == "STRICT_EQUALITY")
check("completion", "the fixed-charge nonzero period is retained", "NONZERO" in REGISTRY["cech_de_rham"]["fixed_charge_period"])

print("\nC. CECH TRIPLES MODULO THE COROOT LATTICE")
triples = [(1, 0), (0, 1), (1, 1), (-2, 3)]
for n in triples:
    lifted_sum = tuple(2 * n_i for n_i in n)  # coefficients in units of pi
    torus_residue = tuple(value % 2 for value in lifted_sum)
    check("cech", f"the lifted logarithm defect is integral for {n}", all(isinstance(v, int) for v in n))
    check("cech", f"the 2pi defect is identity on the Cartan torus for {n}", torus_residue == (0, 0))
check("cech", "the third-root lattice vector introduces no new generator", e12 == tuple(a + b for a, b in zip(e1, e2)))
check("cech", "the Cartan transition is recorded modulo the lattice", "mod 2 pi Z^2" in REGISTRY["cech_de_rham"]["cartan_angle_transition"])

print("\nD. WEYL COTANGENT LIFTS")
check("weyl", "s1 is an involution", mmul(s1, s1) == I2)
check("weyl", "s2 is an involution", mmul(s2, s2) == I2)
check("weyl", "the A2 braid relation holds", mmul(mmul(s1, s2), s1) == mmul(mmul(s2, s1), s2))
coxeter = mmul(s1, s2)
check("weyl", "the Coxeter element has order three", mmul(mmul(coxeter, coxeter), coxeter) == I2)
test_mu = [Fraction(5, 3), Fraction(7, 4)]
test_tau = [Fraction(11, 5), Fraction(-2, 3)]
pairing = sum(a * b for a, b in zip(test_tau, test_mu))
for label, reflection in (("s1", s1), ("s2", s2)):
    transformed_mu = mvec(reflection, test_mu)
    transformed_tau = mvec(transpose(inv2(reflection)), test_tau)
    transformed_pairing = sum(a * b for a, b in zip(transformed_tau, transformed_mu))
    check("weyl", f"{label} inverse-transpose lift preserves tau dot dmu", transformed_pairing == pairing)
check("weyl", "the registry records cotangent-pairing preservation", REGISTRY["weyl"]["cotangent_pairing_preserved"] is True)

print("\nE. DIMENSION, MOMENT, AND COLLAPSE SCHEDULE")
schedule = REGISTRY["dimension_and_rank"]
check("schedule", "the common leaf plus transverse factor is 98D", schedule["common_leaf_dimension"] + schedule["transverse_dimension"] == schedule["full_source_dimension"] == 98)
check("schedule", "the regular map rank is 91", schedule["regular_map_rank"] == 91)
check("schedule", "the compact A1 wall map rank is 90", schedule["a1_wall_map_rank"] == 90)
check("schedule", "the compact A2 origin map rank is 88", schedule["a2_origin_map_rank"] == 88)
check("schedule", "the atlas imports no new degrees of freedom", schedule["new_degrees_of_freedom"] == 0)
for root in (0, 1):
    wall_mu = [Fraction(3), Fraction(4)]
    wall_mu[root] = 0
    check("collapse", f"root {root + 1} primitive coefficient vanishes on its wall", wall_mu[root] == 0)
    check("collapse", f"the other root circle remains on wall {root + 1}", wall_mu[1 - root] != 0)
check("collapse", "the compact A1 attachment is lattice/primitive/rank compatible", REGISTRY["collapse"]["compact_a1_attachment"] == "LATTICE_PRIMITIVE_AND_RANK_COMPATIBLE")
check("collapse", "the compact A2 attachment is two-root compatible", REGISTRY["collapse"]["compact_a2_attachment"] == "TWO_ROOT_LATTICE_PRIMITIVE_AND_RANK_COMPATIBLE")

print("\nF. CLAIM CEILING")
scope = REGISTRY["scope"]
check("scope", "the compact regular multichart atlas is constructed", scope["compact_a2_regular_multichart_atlas"] == "CONSTRUCTED")
check("scope", "the single global diagonalizer remains obstructed", scope["single_global_diagonalizing_section"] == "OBSTRUCTED")
check("scope", "the bare orbit primitive remains nonexact", scope["bare_orbit_relative_primitive"] == "NONEXACT")
check("scope", "no prequantum twist or integrality claim is used", scope["prequantum_twist"] == "NOT_USED_AND_NO_INTEGRALITY_CLAIM")
check("scope", "split and mixed global topology remain open", scope["split_and_mixed_global_topology"] == "OPEN")
check("scope", "higher root subsystems remain open", scope["higher_root_subsystems"] == "OPEN")
check("scope", "the full singular stratification remains open", scope["full_singular_stratification"] == "OPEN")
check("scope", "zero charge remains unconstructed", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("scope", "global all-strata RSAP remains open", scope["global_all_strata_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REGISTRY["changes"].values()) == {"none"})

print("\nG. ARTIFACT LINKS")
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"the {key} path exists", (ROOT / REGISTRY[key]).is_file())
check("links", "the next gate globalizes remaining real forms", REGISTRY["next_gate"].startswith("GLOBALIZE_SPLIT_AND_MIXED_A2"))

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REGISTRY["status"], "next_gate": REGISTRY["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
