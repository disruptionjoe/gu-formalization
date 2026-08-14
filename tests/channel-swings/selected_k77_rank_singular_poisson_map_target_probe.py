#!/usr/bin/env python3
"""Exact target-class gate for a weaker rank-singular all-charge Poisson map."""

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


target = strict("lab/process/selected-k77-rank-singular-poisson-map-target.json")
prior = strict("lab/process/selected-k77-all-charge-poisson-submersion-minimum.json")
atlas = strict("lab/process/selected-k77-regular-semisimple-cartan-atlas-realization.json")

print("A. TARGET CLASS")
spec = target["target"]
check("type", "RSAP has one smooth symplectic domain", spec["domain"] == "ONE_SMOOTH_SYMPLECTIC_MANIFOLD" and spec["stratified_domain"] is False)
check("type", "RSAP is smooth surjective and Poisson", spec["map"] == "SMOOTH_SURJECTIVE_POISSON")
check("type", "RSAP is submersive on the regular locus", spec["regular_locus"] == "SUBMERSION")
check("type", "RSAP may lose rank on singular strata", spec["singular_strata"] == "RANK_LOSS_ALLOWED")
check("scope", "the existing regular atlas is not mislabeled all-charge", target["existing_regular_atlas"]["all_charge"] is False)
check("scope", "the existing regular atlas is not yet an RSAP candidate", target["existing_regular_atlas"]["rsap_candidate"] is False)

print("\nB. EXACT DIMENSION BOUNDS")
dims = target["dimensions"]
check("prior", "the target dimension remains 91", dims["target"] == prior["result"]["target_dimension"] == 91)
check("prior", "the regular Poisson rank remains 84", dims["regular_poisson_rank"] == prior["result"]["regular_poisson_rank"] == 84)
check("exact", "regular corank is seven", dims["target"] - dims["regular_poisson_rank"] == dims["regular_corank"] == 7)
check("theorem", "regular submersivity forces dimension at least 98", dims["target"] + dims["regular_corank"] == dims["lower_bound"] == 98)
check("prior", "the all-charge submersion minimum remains 182", dims["all_charge_submersion_minimum"] == prior["result"]["all_charge_poisson_submersion_minimum"] == 182)
check("scope", "the weaker candidate interval is exactly [98,182)", dims["smaller_candidate_interval"] == "[98,182)")
check("atlas", "the existing atlas attains the regular lower bound", atlas["component"]["dimension"] == dims["lower_bound"])
check("atlas", "the existing atlas covers only the regular-semisimple locus", "REGULAR" in target["existing_regular_atlas"]["coverage"])

print("\nC. SURJECTIVE IS NOT SUBMERSIVE CONTROL")
toy = target["toy_control"]
q_values = [-2, -1, 0, 1, 2]
images = [q**3 for q in q_values]
derivatives = [3 * q**2 for q in q_values]
check("planted", "the cube control preserves order and both signs", images == [-8, -1, 0, 1, 8])
check("planted", "the cube derivative vanishes exactly at zero", derivatives[2] == 0 and all(value > 0 for index, value in enumerate(derivatives) if index != 2))
check("planted", "the registry marks the cube map surjective and critical", toy["surjective"] is True and toy["critical_at_zero"] is True)
check("scope", "the cube is not claimed as an so(7,7) construction", toy["scope"].startswith("HYPOTHESIS_CONTROL"))

print("\nD. FIRST CONSTRUCTION GATE")
check("next", "the first gate is one codimension-one discriminant wall", "CODIMENSION_ONE_DISCRIMINANT_WALL" in target["first_gate"])
check("scope", "no RSAP existence is claimed", "NO_RSAP_EXISTENCE" in target["claim_ceiling"])
check("accounting", "no ledger canon residue quotient datum or posture move occurs", set(target["changes"].values()) == {"none"})

print(json.dumps({"counts": dict(COUNTS), "failures": FAILURES, "status": target["status"], "first_gate": target["first_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
