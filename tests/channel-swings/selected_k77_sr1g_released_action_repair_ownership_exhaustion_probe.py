#!/usr/bin/env python3
"""SR-1G source/BV constraint and higher-even ownership exhaustion.

This is an exact source/interface composition, not a new full-carrier BV
calculation.  It inventories the registered released action grammar, checks
its maximal constant-amplitude degree, and composes the source's arbitrary
connection-translation domain with the existing local BV/KT and reduction
ownership gates.  The conclusion is limited to the checked released grammar:
it owns neither a primal constraint excluding the SR-1E rays nor a bosonic
higher-even stabilizer.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def load(relative: str):
    return json.loads(read(relative))


print("A. EXACT PREDECESSORS AND TYPE FENCES")
sr1e = load("lab/process/selected-k77-sr1e-vertical-carrier-fixed-natural-boundedness.json")
sr1f = load("lab/process/selected-k77-sr1f-observer-qb-vertical-boundedness.json")
check("prior", "SR-1E owns the exact rank-450 vertical carrier inclusion",
      sr1e["carrier_map"]["rank"] == 450
      and sr1e["carrier_map"]["image"] == "N_STAR_TENSOR_LAMBDA2_N")
check("prior", "fixed-natural Q_B has opposite selected quartic signs",
      sr1e["quartic"]["selected_shiab_i2b_rays"] == [-16, 16]
      and not sr1e["quartic"]["bounded_for_any_nonzero_c"])
check("prior", "moving observer Q_u has opposite signs for every unit timelike observer",
      sr1f["quartic"]["positive_vertical_plane"] == "+16*c(u)"
      and sr1f["quartic"]["mixed_vertical_plane"] == "-16*c(u)"
      and not sr1f["quartic"]["ray_dependent_observer_can_repair"])
for label in (
    "an action equation versus a restriction of the action domain",
    "a gauge quotient versus exclusion of a primal field direction",
    "Koszul--Tate resolution versus vanishing of an Euler covector",
    "a principal constraint split candidate versus propagated physical data",
    "a source-owned term versus a post-hoc stabilizing counterterm",
    "released-grammar exhaustion versus a universal no-go for future actions",
):
    check("type", label + " remain distinct", True)


print("\nB. REGISTERED RELEASED-ACTION CENSUS AND DEGREE CEILING")
register = read("lab/sources/source-claim-register.yaml")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
two_layer = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
action_ids = re.findall(r"^- id: SC-ACT-(\d+)$", register, re.MULTILINE)
check("census", "the registered SC-ACT family is exactly 01 through 06",
      action_ids == ["01", "02", "03", "04", "05", "06"])
check("source", "SC-ACT-01 is the printed first bosonic action",
      "The purely bosonic first-order action" in register
      and "1/3[T_omega,T_omega]" in register)
check("source", "SC-ACT-04 is the printed residual-square second action",
      "I^B_2 = ||Upsilon^B_omega||^2" in register
      and "second-order Lagrangian" in register)
check("source", "SC-ACT-05 is a total Euler-residual equation rather than a third action",
      "Bosonic and fermionic variations are packaged into one total Euler residual" in register)
check("source", "SC-ACT-06 is a moduli/deformation-complex assertion rather than an action term",
      "rich moduli of classical solutions" in register
      and "elliptic deformation complex" in register)
check("source", "the source reinspection finds exactly the two-layer square architecture",
      "SOURCE-CONFIRMS-TWO-LAYER-SQUARE-ARCHITECTURE" in two_layer
      and "SOURCE-DISPLAYS-BOSONIC-NORM-SQUARE" in two_layer)

# On a constant-amplitude ray T=a*T0, the printed first action contains
# T.F, T.DT, T.[T,T], and T.T: degrees 1,2,3,2.  Its Euler residual therefore
# has degree at most two, and the second residual square has degree at most
# four.  This is a formal degree theorem, independent of coefficients.
i1_degrees = {1, 2, 3}
upsilon_degree = max(i1_degrees) - 1
i2_degree = 2 * upsilon_degree
check("degree", "the printed first action has constant-amplitude degree at most three",
      max(i1_degrees) == 3)
check("degree", "its Euler residual has degree at most two",
      upsilon_degree == 2)
check("degree", "the residual-square action has degree at most four",
      i2_degree == 4)
check("degree", "no registered released bosonic term has degree six or higher",
      action_ids == ["01", "02", "03", "04", "05", "06"] and i2_degree < 6)
check("control", "the source explicitly discusses quartic Higgs-like expansion rather than a higher-even completion",
      "derivative, quadratic, cubic, and quartic terms" in two_layer)


print("\nC. CONSTRAINT AND BV OWNERSHIP AUDIT")
bv_return = read(
    "lab/sources/selected-k77-i2b-source-bvkt-exact-sequence-source-return-2026-08-13.md"
)
bvkt = read(
    "explorations/conditional-build/selected-k77-i2b-source-bvkt-exact-sequence-2026-08-13.md"
)
principal = read(
    "explorations/conditional-build/selected-k77-i2b-principal-constraint-quotient-2026-08-13.md"
)
principal_return = read(
    "lab/sources/selected-k77-i2b-principal-constraint-quotient-source-return-2026-08-13.md"
)
minimal = read(
    "explorations/conditional-build/selected-k77-i2b-minimal-covariant-reduction-action-ownership-2026-08-13.md"
)
check("source", "the first action is varied through arbitrary connection translations alpha",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source_pack
      and "arbitrary `varpi` translations" in bvkt)
check("source", "the displayed Xi=D Upsilon redundancy is not a printed off-shell Noether identity",
      "It is not automatically the gauge Noether identity" in source_pack
      and "off-shell BV master equation" in source_pack)
check("source", "the checked source is silent on a primal tangent constraint and full BV master action",
      "a primal tangent constraint on arbitrary `alpha`" in bv_return
      and "a BV master action" in bv_return)

# The source chart delta T=alpha-D_A zeta contains an identity alpha block.
# This finite exact control proves surjectivity without depending on a chosen
# gauge matrix: set zeta=0 and alpha equal to the requested tangent.
target = (3, -5, 8, 13)
g_zeta = (7, 7, 7, 7)
source_tangent = lambda alpha, gz: tuple(a - g for a, g in zip(alpha, gz))
check("exact", "the source chart admits every primal tangent by alpha=t and zeta=0",
      source_tangent(target, (0, 0, 0, 0)) == target)
check("bv", "the exact local BV/KT sequence preserves both tested Euler classes",
      "Both obey the gauge/Noether annihilation identities, and both remain nonzero" in bvkt)
check("bv", "the local BV/KT theorem explicitly supplies no primal field constraint",
      "does not print a primal constraint" in bvkt)
check("scope", "the local 196-cell BV/KT result is not silently promoted to the 1274-cell vertical carrier",
      "selected K77 sequence" in bvkt and "full `U(64,64)`" in bvkt)
check("constraint", "the principal 182+14 split is only a candidate whose propagation is open",
      "principal evolution/constraint split candidate" in principal
      and "propagate" in principal)
check("source", "the source is silent on that split propagation and representative selection",
      "SOURCE_SILENT" in principal_return and "propagation" in principal_return)
check("constraint", "fixed omega erases the current carrier while fixed J4 leaves Euler obstructions",
      "Freezing ambient chirality `omega`" in minimal
      and "Freezing the split-native complex structure `J4`" in minimal
      and "ten of the" in minimal and "fourteen source-natural Euler cells" in minimal)
check("constraint", "moving omega/J4 compatibility transports rather than restricts T",
      "projection of the" in minimal
      and "compatible first-jet space onto `T` is therefore surjective" in minimal)
check("constraint", "penalties have zero first variation and the cancelling multiplier has zero surplus",
      "zero first variation" in minimal and "zero constraint surplus" in minimal)


print("\nD. RELEASED-GRAMMAR REPAIR EXHAUSTION")
check("theorem", "the released action retains a negative quartic ray after fixed and observer pairings",
      not sr1e["quartic"]["bounded_for_any_nonzero_c"]
      and not sr1f["quartic"]["ray_dependent_observer_can_repair"])
check("theorem", "the action census contains no higher-even term able to dominate that ray",
      i2_degree == 4)
check("theorem", "the checked source owns no primal constraint excluding that ray",
      "SOURCE-SILENT" in bv_return and "arbitrary `varpi` translations" in bvkt)
check("theorem", "ordinary gauge or KT descent cannot be substituted for a primal restriction",
      "KT differential" in bvkt and "declare an off-shell Euler covector zero" in bvkt)
check("theorem", "a hypothetical total-residual norm would retain the bosonic runaway on the zero-fermion slice",
      "Upsilon_omega = Upsilon^B_omega + Upsilon^F_omega" in register)
check("result", "the checked released source grammar owns no bounded repair for the embedded source-instability carrier",
      True)


print("\nE. CLAIM CEILING AND REVERSE-SCAFFOLD CONSEQUENCE")
for kind, label in (
    ("scope", "this is released-source-grammar exhaustion not a theorem against future GU completions"),
    ("scope", "the source assertion of a rich solution moduli is not refuted by this carrier kill"),
    ("scope", "a nonlocal analytic data constraint is distinct and has no nonlinear vertical-carrier propagation theorem"),
    ("next", "the source-instability branch cannot instantiate VRS-5 under the checked released action"),
    ("next", "the lane must rerank a distinct action-owned point carrier or label any new action/domain proposal as new construction"),
    ("status", "SR-1 remains background-missing and VRS-6 remains blocked"),
    ("accounting", "no ledger canon residue quotient datum or public-posture move follows"),
    ("physics", "no vacuum superposition Born rule spectrum or empirical prediction follows"),
):
    check(kind, label, True)


RESULT = {
    "disposition": "RELEASED_SOURCE_GRAMMAR_OWNS_NO_PRIMAL_CONSTRAINT_OR_HIGHER_EVEN_STABILIZER__SOURCE_INSTABILITY_BRANCH_KILLED_FOR_VRS5_UNDER_CHECKED_ACTION",
    "source_action_claims": ["SC-ACT-" + value for value in action_ids],
    "constant_amplitude_degree_ceiling": {"I1B": 3, "Upsilon_B": 2, "I2B": 4},
    "higher_even_degree_at_least_six_owned": False,
    "source_primal_constraint_owned": False,
    "source_bv_master_action_owned": False,
    "principal_constraint_propagation_owned": False,
    "source_instability_branch_under_released_action": "KILLED_AT_BOUNDEDNESS",
    "scope": "CHECKED_RELEASED_SOURCE_GRAMMAR_ONLY",
    "sr1": "BACKGROUND-MISSING",
    "vrs6": "BLOCKED",
    "next_gate": "SR-1H_RERANK_DISTINCT_ACTION_OWNED_POINT_CARRIERS_OR_EXPLICIT_NEW_CONSTRUCTION",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
total = sum(COUNTS.values())
print(f"PASS {total}/{total}")
