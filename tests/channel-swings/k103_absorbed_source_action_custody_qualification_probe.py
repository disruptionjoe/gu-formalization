#!/usr/bin/env python3
"""K103 absorbed source-action custody and completeness qualification."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/k103-absorbed-source-action-custody-qualification-wave.json"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(path: Path) -> dict:
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def valid(data: dict) -> bool:
    denominator = data.get("qualification_denominator", [])
    cells = data.get("cells", {})
    if len(denominator) != 12 or len(set(denominator)) != 12 or set(cells) != set(denominator):
        return False
    if data.get("corpus", {}).get("source_authenticated") is not False:
        return False
    if data.get("corpus", {}).get("external_authorial_action_packet") is not False:
        return False
    if data.get("corpus", {}).get("default_buildbench_candidate_count") != 4:
        return False
    if data.get("candidate_union", {}).get("allowed") is not False:
        return False
    if data.get("result", {}).get("qualified") is not False:
        return False
    if data.get("result", {}).get("first_nonadmission_locus") != "real_coefficient_complete_action":
        return False
    if cells.get("real_coefficient_complete_action", {}).get("state") != "absent":
        return False
    for key in (
        "complete_coefficient_ownership",
        "complete_euler_noether_system",
        "full_hessian_and_formal_adjoint",
        "common_closed_operator_domain",
        "causal_green_boundary_form",
        "families_boundary_dirac_global_objects",
    ):
        if cells.get(key, {}).get("state") != "absent":
            return False
    return all(cell.get("state") in {"partial", "absent"} and cell.get("reason") for cell in cells.values())


data = strict(REGISTRY)
readme = (ROOT / "absorbed/gu-source-action/README.md").read_text()
spec = (ROOT / "absorbed/gu-source-action/SPEC.md").read_text()
buildbench = (ROOT / "absorbed/gu-source-action/lib/source_action_buildbench.py").read_text()
readme_flat = " ".join(readme.split())
spec_flat = " ".join(spec.split())

print("A. POSITIVE CONTROLS")
check("positive", "corpus front door says the action has not yet been built", "It has not yet built one" in readme_flat)
check("positive", "SPEC names the action as the object to construct", "# SPEC — the object to construct" in spec_flat)
check("positive", "security-budget lens does not replace the target", "does **not** relax the target" in spec_flat)
check("positive", "buildbench has four explicit default candidates", buildbench.count("BuildbenchCandidate(") >= 4)

print("\nB. CUSTODY AND QUALIFICATION")
check("custody", "corpus is repository construction evidence", data["corpus"]["custody_grade"] == "repository_absorbed_construction_evidence")
check("custody", "corpus is not source authenticated", data["corpus"]["source_authenticated"] is False)
check("custody", "no external authorial action packet is filed", data["corpus"]["external_authorial_action_packet"] is False)
check("typing", "Cl(9,5) real form is explicit", data["corpus"]["explicit_real_form"] == "Cl(9,5)=M(64,H)")
check("denominator", "twelve unique qualification objects are exact", len(data["qualification_denominator"]) == len(set(data["qualification_denominator"])) == 12)
check("denominator", "every qualification object has one cell", set(data["qualification_denominator"]) == set(data["cells"]))
check("result", "zero corpus packet qualifies", data["result"]["qualified"] is False)
check("result", "first nonadmission is coefficient-complete action ownership", data["result"]["first_nonadmission_locus"] == "real_coefficient_complete_action")
check("result", "candidate union is forbidden", data["candidate_union"]["allowed"] is False)
for key in (
    "real_coefficient_complete_action",
    "complete_coefficient_ownership",
    "complete_euler_noether_system",
    "full_hessian_and_formal_adjoint",
    "common_closed_operator_domain",
    "causal_green_boundary_form",
    "families_boundary_dirac_global_objects",
):
    check("absence", f"{key} remains absent", data["cells"][key]["state"] == "absent")
check("structure", "registry satisfies the complete invariant set", valid(data))

print("\nC. HOSTILE SELFTEST")
mutations = []
for path, value in (
    (("corpus", "source_authenticated"), True),
    (("corpus", "external_authorial_action_packet"), True),
    (("corpus", "default_buildbench_candidate_count"), 3),
    (("candidate_union", "allowed"), True),
    (("result", "qualified"), True),
    (("result", "first_nonadmission_locus"), "full_hessian_and_formal_adjoint"),
    (("cells", "real_coefficient_complete_action", "state"), "qualified"),
    (("cells", "complete_coefficient_ownership", "state"), "partial"),
    (("cells", "complete_euler_noether_system", "state"), "partial"),
    (("cells", "full_hessian_and_formal_adjoint", "state"), "partial"),
    (("cells", "common_closed_operator_domain", "state"), "partial"),
    (("cells", "causal_green_boundary_form", "state"), "partial"),
    (("cells", "families_boundary_dirac_global_objects", "state"), "partial"),
):
    bad = deepcopy(data)
    cursor = bad
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value
    mutations.append(bad)
bad = deepcopy(data)
bad["qualification_denominator"] = bad["qualification_denominator"][:-1]
mutations.append(bad)
for index, bad in enumerate(mutations, 1):
    check("hostile", f"mutation {index} is rejected", not valid(bad))

print(f"\nSUMMARY {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())} passed; hostile {COUNTS['hostile']}/{COUNTS['hostile']} caught")
if FAILURES:
    raise SystemExit(1)
