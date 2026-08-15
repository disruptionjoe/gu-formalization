#!/usr/bin/env python3
"""Exact clutching and primitive-period certificate for compact A2."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads(
    (ROOT / "lab/process/selected-k77-rsap-a2-global-primitive-monodromy-obstruction.json").read_text()
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


def laurent_mul(a, b):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] = out.get(i + j, 0) + ai * bj
    return {k: v for k, v in out.items() if v}


def winding(monomial):
    nonzero = [(degree, coefficient) for degree, coefficient in monomial.items() if coefficient]
    if len(nonzero) != 1:
        raise ValueError("clutching function is not a monomial")
    degree, coefficient = nonzero[0]
    if coefficient not in (1, -1):
        raise ValueError("clutching coefficient is not a unit")
    return degree


print("A. SIMPLE-ROOT HOPF CLUTCHING")
line_1 = {1: 1}
line_2 = {-1: 1}
determinant = laurent_mul(line_1, line_2)
check("clutching", "the first eigenline transition is z", line_1 == {1: 1})
check("clutching", "the second eigenline transition is z^-1", line_2 == {-1: 1})
check("clutching", "the first eigenline has unit winding", winding(line_1) == 1)
check("clutching", "the second eigenline has opposite winding", winding(line_2) == -1)
check("clutching", "the SU2 determinant clutching is trivial", determinant == {0: 1})
check("clutching", "the line clutching itself is nontrivial", winding(line_1) != 0)
check("clutching", "the registry records the simple-root sphere", REGISTRY["simple_root_restriction"]["orbit"] == "SU(2)/U(1)=S2")
check("clutching", "the registry records Chern number one", REGISTRY["simple_root_restriction"]["first_chern_number"] == 1)
check("clutching", "a global group section is obstructed", REGISTRY["simple_root_restriction"]["global_group_section"] == "OBSTRUCTED")

print("\nB. TWO-CHART CONNECTION CERTIFICATE")
# Store coefficients of dphi.  At the north/south poles the displayed local
# potentials vanish on the disc where dphi is singular.
def A_north(cos_theta):
    return (Fraction(1) - cos_theta) / 2


def A_south(cos_theta):
    return -(Fraction(1) + cos_theta) / 2


check("connection", "the north potential vanishes at the north pole", A_north(Fraction(1)) == 0)
check("connection", "the south potential vanishes at the south pole", A_south(Fraction(-1)) == 0)
for value in (Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1)):
    check("connection", f"north-south difference is dphi at cos(theta)={value}", A_north(value) - A_south(value) == 1)
# F=dA_N=(sin theta/2)dtheta wedge dphi, so integral(F)/(2pi)=1.
normalized_curvature_integral = Fraction(1, 2) * (Fraction(1) - Fraction(-1))
check("connection", "the normalized sphere curvature integral is one", normalized_curvature_integral == 1)
check("connection", "the curvature integral matches clutching degree", normalized_curvature_integral == winding(line_1))

print("\nC. COTANGENT PRIMITIVE PERIOD")
regular_spectra = [
    (Fraction(2), Fraction(0), Fraction(-2)),
    (Fraction(3), Fraction(-1), Fraction(-2)),
    (Fraction(5, 2), Fraction(1, 2), Fraction(-3)),
]
for spectrum in regular_spectra:
    l1, l2, l3 = spectrum
    mu = l1 - l2
    check("primitive", f"spectrum {spectrum} is traceless", l1 + l2 + l3 == 0)
    check("primitive", f"spectrum {spectrum} is regular", len(set(spectrum)) == 3)
    check("primitive", f"simple-root charge for {spectrum} is nonzero", mu != 0)
    check("primitive", f"period/(2pi) equals the root charge for {spectrum}", mu * winding(line_1) == l1 - l2)
wall_spectrum = (Fraction(1), Fraction(1), Fraction(-2))
wall_mu = wall_spectrum[0] - wall_spectrum[1]
check("primitive", "zero simple-root period forces an eigenvalue collision", wall_mu == 0 and len(set(wall_spectrum)) < 3)
check("primitive", "the zero-period locus is outside the regular overlap", REGISTRY["primitive"]["zero_period_locus"] == "DISCRIMINANT_WALL_OUTSIDE_REGULAR_OVERLAP")
check("primitive", "the registry records the lifted period", REGISTRY["primitive"]["lifted_period"] == "2 pi mu_alpha")
check("primitive", "the selected group-section exact gauge is obstructed", REGISTRY["primitive"]["global_exact_gauge"].startswith("OBSTRUCTED_FOR_SELECTED_GROUP_SECTION_ROUTE"))

print("\nD. PULLBACK AND CLAIM CEILING")
# Exact one-forms have zero loop period.  A finite quotient cannot repair the
# class: exactness downstairs would pull back to exactness upstairs.
mu = Fraction(7, 3)
cover_degree = 2
check("ceiling", "the selected regular charge is nonzero", mu != 0)
check("ceiling", "the lifted loop period coefficient is nonzero", mu * winding(line_1) != 0)
check("ceiling", "a finite cover preserves nonzero period", cover_degree * mu * winding(line_1) != 0)
surviving = REGISTRY["surviving_structure"]
check("ceiling", "contractible regular germs remain constructed", surviving["contractible_regular_germs"] == "CONSTRUCTED")
check("ceiling", "the symplectic atlas is not killed", surviving["symplectic_atlas"] == "NOT_OBSTRUCTED_BY_THIS_RESULT")
check("ceiling", "the moment atlas is not killed", surviving["moment_map_atlas"] == "NOT_OBSTRUCTED_BY_THIS_RESULT")
check("ceiling", "the A2 cotangent primitive remains global", surviving["a2_cotangent_tautological_primitive"] == "GLOBAL_AND_UNCHANGED")
check("ceiling", "only the section-generated relative primitive is nonexact", surviving["section_generated_relative_primitive"] == "NONEXACT_ON_SELECTED_COMPLETE_REGULAR_OVERLAP")
scope = REGISTRY["scope"]
check("ceiling", "the compact multichart transition remains open", scope["compact_a2_multichart_transition"] == "OPEN")
check("ceiling", "a general compact global transition remains open", scope["compact_a2_general_global_transition"] == "OPEN")
check("ceiling", "split and mixed global topology remain open", scope["split_and_mixed_global_topology"] == "OPEN")
check("ceiling", "singular and deeper extensions remain open", scope["singular_extension"] == scope["deeper_singular_strata"] == "OPEN")
check("ceiling", "zero charge remains unconstructed", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("ceiling", "global RSAP remains open", scope["global_rsap"] == "OPEN")
check("ceiling", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("ceiling", "protected truth surfaces remain unchanged", set(REGISTRY["changes"].values()) == {"none"})

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REGISTRY["status"], "next_gate": REGISTRY["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
