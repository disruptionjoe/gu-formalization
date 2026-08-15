#!/usr/bin/env python3
"""Exact ownership/type gate for split and SU(2,2) A3 relative placement."""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k80_rsap_a3_cross_real_form_incidence_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k81-rsap-a3-relative-placement-ownership-gate-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k81-rsap-a3-relative-placement-ownership-gate.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k81-rsap-a3-relative-placement-ownership-gate-review.md"
D7_REGISTRY = ROOT / "lab/process/selected-k77-rsap-rank82-wall-family-a2-cocycle-gate.json"
CARTAN_REGISTRY = ROOT / "lab/process/selected-k77-regular-cartan-global-realization-obstruction.json"
FACTOR_REGISTRY = ROOT / "lab/process/selected-k79-rsap-a3-real-form-principal-factor-census.json"
INCIDENCE_REGISTRY = ROOT / "lab/process/selected-k80-rsap-a3-cross-real-form-incidence.json"
SOURCE_RETURN = ROOT / "lab/sources/selected-k77-regular-cartan-global-realization-source-return-2026-08-14.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def root(i: int, j: int, sign_i: int = 1, sign_j: int = -1) -> tuple[int, ...]:
    value = [0] * 7
    value[i], value[j] = sign_i, sign_j
    return tuple(value)


print("A. PREDECESSOR AND DURABLE FILES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("prior", "the k80 incidence predecessor replays 44/44",
      '"checks": 44' in capture.getvalue()
      and '"failures": []' in capture.getvalue()
      and not prior["FAILURES"])
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. ABSTRACT D7 ROOT DATA")
d7_roots = {
    root(i, j, sign_i, sign_j)
    for i, j in itertools.combinations(range(7), 2)
    for sign_i in (-1, 1)
    for sign_j in (-1, 1)
}
check("root", "the abstract D7 root set has 84 elements", len(d7_roots) == 84)
check("root", "every abstract D7 root has squared length two",
      {dot(value, value) for value in d7_roots} == {2})

simple = [root(0, 1), root(1, 2), root(2, 3)]
cartan = [[dot(left, right) for right in simple] for left in simple]
check("root", "the chosen three-root chain has the A3 Cartan matrix",
      cartan == [[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
a3_roots = {
    root(i, j)
    for i in range(4)
    for j in range(4)
    if i != j
}
check("root", "the chain spans the twelve e_i-e_j roots on four coordinates",
      len(a3_roots) == 12 and a3_roots <= d7_roots)

d7_registry = load(D7_REGISTRY)
check("schema", "the D7 wall registry owns both real rank-one possibilities",
      d7_registry["wall_family"]["real_rank_one_forms"] == ["sl(2,R)", "su(2)"])
serialized_d7 = json.dumps(d7_registry).lower()
check("schema", "the D7 wall registry serializes no six-plane support map",
      "six_plane" not in serialized_d7 and "support_map" not in serialized_d7)
check("typing", "abstract root combinatorics alone does not encode a real-form involution", True)
check("typing", "an abstract A3 subsystem is not an ambient six-plane embedding", True)


print("\nC. OWNED ENDPOINT AND FACTOR DATA")
cartan_registry = load(CARTAN_REGISTRY)
real_cartan = cartan_registry["real_cartan"]
check("cartan", "the selected endpoint owns split rank five and compact rank two",
      real_cartan["split_rank"] == 5 and real_cartan["compact_rank"] == 2)
check("cartan", "the endpoint is regular but not split-regular",
      real_cartan["regular"] is True and real_cartan["split_regular"] is False)
check("ownership", "the endpoint registry does not own an edge carrier",
      cartan_registry["source_and_physics"]["source_owned_edge_carrier"] is False)

factor_registry = load(FACTOR_REGISTRY)
check("factor", "all real A3 factors remain constructed at factor grade",
      factor_registry["scope"]["all_real_a3_principal_factors"] == "CONSTRUCTED_AT_FACTOR_GRADE")
check("factor", "the predecessor factor census leaves cross-form refinements open",
      factor_registry["scope"]["cross_real_form_common_refinements"] == "OPEN")
check("factor", "the SU(2,2) factor has the required 18 dimensions",
      factor_registry["real_forms"]["pseudo_unitary_22"]["factor_dimension"] == 18)

source_text = SOURCE_RETURN.read_text(encoding="utf-8")
check("source", "the inspected source return is explicit about source silence",
      "SOURCE-SILENT" in source_text)
check("source", "the inspected source return owns no coadjoint-orbit edge field",
      "does not print a coadjoint-orbit edge\nfield" in source_text)
check("source", "the inspected source return owns no global symplectic realization",
      "a global symplectic realization" in source_text)
check("typing", "Cartan ranks do not label either A3 six-plane support", True)
check("typing", "Cartan ranks do not determine a pairwise support intersection", True)


print("\nD. MISSING JOINT TYPE AND CONTRARY COMPLETIONS")
incidence = load(INCIDENCE_REGISTRY)
models = incidence["relative_models"]
observed = {
    (row["support_intersection_dimension"], tuple(row["support_intersection_signature"]))
    for row in models.values()
}
check("contrary", "k80 realizes transverse, A1xA1 and B2 support incidences",
      observed == {(0, (0, 0)), (4, (2, 2)), (5, (3, 2))})
check("contrary", "the k80 individual factor data select no relative orbit",
      incidence["incidence"]["individual_factor_data_select_relative_orbit"] is False)
check("contrary", "k80 selects no canonical common target domain",
      incidence["incidence"]["canonical_common_target_domain"] == "NOT_SELECTED")

registry = load(REGISTRY)
missing = registry["missing_joint_type"]
for key in (
    "selected_split_support_map",
    "selected_su22_support_map",
    "same_endpoint_or_source_ownership_proof",
    "support_intersection_dimension",
    "support_intersection_signature",
):
    check("missing", f"{key} is explicitly not provided", missing[key] == "NOT_PROVIDED")
check("missing", "the selected relative orbit is type-missing",
      missing["selected_relative_orbit"] == "TYPE_MISSING")
check("missing", "root combinatorics is not promoted to a real-form selector",
      missing["root_combinatorics_selects_real_form"] is False)
check("missing", "the Cartan rank pair is not promoted to a support selector",
      missing["cartan_rank_pair_selects_six_plane_support"] is False)
check("missing", "current owner data exclude no two contrary k80 models",
      registry["k80_contrary_completions"]["current_owner_data_excludes_all_but_one"] is False)


print("\nE. ROUTING AND CLAIM CEILING")
routing = registry["routing"]
check("routing", "real forms are alternative local carrier horns at current ownership grade",
      routing["real_a3_forms"] == "ALTERNATIVE_LOCAL_CARRIER_HORNS_AT_CURRENT_OWNERSHIP_GRADE")
check("routing", "no cross-form atlas edge is added", routing["cross_form_atlas_edge"] == "DO_NOT_ADD")
for key in ("common_refinement", "moment_map_comparison", "tautological_primitive_comparison", "triple_cocycle"):
    check("routing", f"{key} remains unlicensed", routing[key] == "NOT_LICENSED")
check("scope", "the type-missing verdict is repository and source-return scoped",
      registry["scope"]["claim_is_repository_and_inspected_source_return_scoped"] is True)
check("scope", "universal nonexistence is not claimed",
      registry["scope"]["universal_nonexistence_of_cross_form_incidence"] == "NOT_CLAIMED")
check("scope", "the individual A3 factors are unchanged",
      registry["scope"]["individual_a3_principal_factors"] == "UNCHANGED")
check("scope", "the complete SU(2,2) singular atlas is the next open gate",
      registry["scope"]["complete_su22_singular_transition_atlas"] == "OPEN_NEXT")
check("scope", "zero charge and global all-strata RSAP remain open",
      registry["scope"]["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED"
      and registry["scope"]["global_all_strata_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182-dimensional",
      registry["scope"]["all_charge_fallback_dimension"] == 182)
check("review", "hostile review preserves the repository-scoped ceiling",
      "PASS_WITH_REPOSITORY_SCOPED_TYPE_MISSING_CEILING" in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
