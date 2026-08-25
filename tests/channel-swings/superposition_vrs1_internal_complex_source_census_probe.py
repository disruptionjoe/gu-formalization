#!/usr/bin/env python3
"""Structural verifier for the VRS-1 internal complex-source census.

The finite Clifford and moving-cone calculations remain in the RF-1 and RF-2
probes. This verifier checks that VRS-1 accounts for every presently named
candidate family, preserves the scoped exhaustion quantifiers, and does not
promote a partial component to physical superposition.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


registry = json.loads(read("lab/process/superposition-vrs1-internal-complex-source-census.json"))
result = read(registry["result"])
rf1 = read("explorations/conditional-build/selected-k77-reverse-j-descent-census-2026-08-14.md")
rf2 = read("explorations/conditional-build/selected-k77-moving-j-stueckelberg-cone-2026-08-14.md")
boundary = read("explorations/conditional-build/selected-k77-boundary-stationarity-symplectic-realization-gate-2026-08-14.md")
hessian = read("explorations/conditional-build/selected-k77-stationary-two-layer-hessian-factorization-2026-08-08.md")
twistor = read("explorations/conditional-build/selected-k77-twistor-bv-positive-state-seven-gate-2026-08-13.md")
source_register = read("lab/sources/source-claim-register.yaml")

print("A. REGISTRY AND COMPLETE CURRENT-NAME CENSUS")
check("schema", "the registry identifies VRS-1 and its result", registry["swing"] == "VRS-1" and "vrs1-internal" in registry["result"])
families = registry["candidate_families"]
ids = [family["id"] for family in families]
expected = {
    "CS-EXT", "CS-CL95", "CS-REAL", "CS-FIX", "CS-MOVE", "CS-ORBIT",
    "CS-TW", "CS-BFV", "CS-I2", "CS-MOD", "CS-NL",
}
check("census", "exactly the eleven declared candidate families occur", len(families) == 11 and set(ids) == expected)
check("census", "candidate identifiers are unique", len(ids) == len(set(ids)))
for key in ("name", "owner", "carrier", "status", "reason", "class_exhaustion"):
    check("census", f"every candidate declares {key}", all(family.get(key) for family in families))

print("\nB. QUANTIFIER FENCE")
q = registry["quantifiers"]
check("quantifier", "current repo-named families are accounted for", q["current_repo_named_families_accounted_for"] is True)
check("quantifier", "the fixed split-equivariant family is exhausted", q["complete_fixed_split_equivariant_spinor_family_exhausted"] is True)
check("quantifier", "the natural split-orbit tangent candidate is exhausted", q["natural_split_orbit_tangent_candidate_exhausted"] is True)
check("quantifier", "future action-admissible sources remain unexhausted", q["all_future_action_admissible_complex_sources_exhausted"] is False)
check("quantifier", "H-Q* is not killed", q["intrinsic_superposition_hypothesis_killed"] is False)
check("quantifier", "no action-owned physical J is claimed", q["current_action_owned_physical_complex_structure_constructed"] is False)
check("quantifier", "the result states all three exhaustion levels",
      "Three different exhaustion claims" in " ".join(result.split())
      and "Every non-diagonal, nonlocal" in " ".join(result.split()))

print("\nC. INHERITED EXACT AND TYPE EVIDENCE")
by_id = {family["id"]: family for family in families}
check("fixed", "RF-1 certifies the complete four-member fixed family", "{+J4,-J4,+J10,-J10}" in rf1)
check("fixed", "the fixed family is marked killed rather than globally unique", by_id["CS-FIX"]["status"] == "KILLED_EXACT_FINITE_FAMILY" and "DECLARED_LOCAL" in by_id["CS-FIX"]["class_exhaustion"])
check("moving", "RF-2 owns an exact fibre complex structure", "EXACT FIBRE COMPLEX STRUCTURE" in rf2)
check("moving", "the moving candidate remains partial", by_id["CS-MOVE"]["status"] == "NOT_YET_FALSIFIED_PARTIAL_CONSTRUCTION")
check("orbit", "RF-2 kills the natural invariant orbit complex", "natural invariant complex structure on split orbit" in rf2 and "CANDIDATE KILLED" in rf2)
check("boundary", "boundary evidence is real symplectic but not positive physical cohomology", "symplectic" in boundary and "positive" in boundary and "physical cohomology" in boundary)
check("hessian", "the Hessian evidence distinguishes D Upsilon from the second-action Hessian", "`D Upsilon`" in hessian and "second-action Hessian" in hessian)
check("hessian", "I2 is retyped rather than promoted to J", by_id["CS-I2"]["status"] == "RETYPED_AS_DIFFERENTIAL_OWNER__KILLED_AS_STANDALONE_J")
check("twistor", "the two exact twistor objects remain distinct", "Two twistor objects construct exactly and remain distinct" in twistor)
check("twistor", "the twistor candidate remains an adapter", by_id["CS-TW"]["status"] == "TYPE_MISSING_ADAPTER")
check("source", "SC-ACT-06 asserts rich moduli and Euclidean ellipticity", "id: SC-ACT-06" in source_register and "rich moduli" in source_register and "elliptic" in source_register)
check("source", "the selected Lorentzian program records that moduli claim as untested", "Euclidean ellipticity / rich moduli is untested" in source_register)

print("\nD. SURVIVING COMPOSITE AND HYPOTHESIS UPDATE")
composite = registry["surviving_composite"]
roles = composite["required_roles"]
expected_roles = {"background", "complex_fibre", "differential_owner", "reduction", "pairing", "evolution_adapter"}
check("composite", "the survivor is explicitly unconstructed", composite["status"] == "NOT_YET_FALSIFIED__NOT_CONSTRUCTED")
check("composite", "all six noninterchangeable roles are present", set(roles) == expected_roles)
check("composite", "the moving associated J10 supplies only the complex-fibre role", "associated-spinor J10" in roles["complex_fibre"])
check("composite", "boundary-aware BV/BFV supplies the reduction role", "BFV" in roles["reduction"])
check("composite", "the no-compression rule is explicit", "No one role" in composite["forbidden_compression"])
updates = registry["hypothesis_update"]
check("hypothesis", "H-Q* narrows without promotion", updates["H-Q*"] == "NARROWED_NOT_KILLED")
check("hypothesis", "H0 strengthens without proof", updates["H0"] == "STRENGTHENED_NOT_PROVED")
check("hypothesis", "boundary is promoted to the next reverse test", updates["H-B"] == "PROMOTED_TO_NEXT_REVERSE_TEST")
check("next", "VRS-2 is the next reverse swing", registry["next_reverse_swing"]["id"] == "VRS-2" and "boundary" in registry["next_reverse_swing"]["question"])

print("\nE. CLAIM CEILING")
for phrase in (
    "No currently owned single object is `J_phys`",
    "`H0` is not proved",
    "No complete stationary GU background",
    "No one role may be silently identified with J_phys",
):
    haystack = result if phrase != "No one role may be silently identified with J_phys" else composite["forbidden_compression"]
    check("ceiling", phrase, phrase in haystack)

total = sum(COUNTS.values())
print(f"\nSUMMARY: {total - len(FAILURES)}/{total} checks passed")
if FAILURES:
    raise SystemExit("failed: " + "; ".join(FAILURES))
