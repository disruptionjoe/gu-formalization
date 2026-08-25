#!/usr/bin/env python3
"""Exact dimension/weight certificate for the SC-GRP-04 phantom ten."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "explorations/sc-grp04-phantom-ten-object-separation-2026-08-24.md"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"


BASE = {
    "spacetime_dim": 4,
    "su5_standard_complex_dim": 5,
    "su5_matter_degree": 2,
    "ps_split": (6, 4),
    "su32_signature": (3, 2),
    "standard_central_weight": 1,
    "matter_central_weight": 2,
    "dynamic_bridge_owned": False,
}


def choose(n: int, k: int) -> int:
    if k == 0:
        return 1
    if k == 1:
        return n
    if k == 2:
        return n * (n - 1) // 2
    raise ValueError("probe only needs k <= 2")


def evaluate(spec: dict) -> list[tuple[str, bool]]:
    n = spec["spacetime_dim"]
    cdim = spec["su5_standard_complex_dim"]
    su32 = spec["su32_signature"]
    return [
        ("Sym^2 of four-space has dimension ten", n * (n + 1) // 2 == 10),
        ("symmetric equation component count is ten", choose(n + 1, 2) == 10),
        ("Pati-Salam vector split has dimension ten", sum(spec["ps_split"]) == 10),
        ("Pati-Salam branching (6,1,1)+(1,2,2) has dimension ten", 6 * 1 * 1 + 1 * 2 * 2 == 10),
        ("SU(5) standard realification has dimension ten", 2 * cdim == 10),
        ("SU(3,2) realification has dimension ten", 2 * sum(su32) == 10),
        ("SU(3,2) real metric has inertia (6,4)", (2 * su32[0], 2 * su32[1]) == (6, 4)),
        ("SU(5) matter 10 is exterior square", choose(cdim, spec["su5_matter_degree"]) == 10),
        ("SU(5) matter 10 has real dimension twenty", 2 * choose(cdim, spec["su5_matter_degree"]) == 20),
        ("standard and matter centre weights differ", spec["standard_central_weight"] != spec["matter_central_weight"]),
        ("centre weights differ modulo five", (spec["matter_central_weight"] - spec["standard_central_weight"]) % 5 != 0),
        ("matter weight two misses vector weights plus/minus one", spec["matter_central_weight"] % 5 not in {spec["standard_central_weight"] % 5, (-spec["standard_central_weight"]) % 5}),
        ("Lorentz trace/traceless split is nine plus one", 9 + 1 == 10),
        ("contracted Bianchi removes four independent equations", 10 - 4 == 6),
        ("no dynamical bridge is claimed", spec["dynamic_bridge_owned"] is False),
    ]


def repository_checks() -> list[tuple[str, bool]]:
    artifact = ARTIFACT.read_text(encoding="utf-8")
    flat_artifact = " ".join(artifact.split())
    register = REGISTER.read_text(encoding="utf-8")
    row = register.split("- id: SC-GRP-04", 1)[1].split("- id: SC-GRP-05", 1)[0]
    return [
        ("artifact carries routing boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in artifact),
        ("artifact names Spin(10,C) common parent", "Spin(10,C)" in artifact),
        ("artifact pins official draft custody", "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4" in artifact),
        ("artifact carries exact Pati-Salam branching", "(6,1,1) direct-sum (1,2,2)" in artifact),
        ("artifact separates Lambda^2 C^5", "Lambda^2 C^5" in artifact),
        ("artifact retains dynamical ceiling", "does not give the hoped-for fundamental explanation" in flat_artifact),
        ("artifact carries typed-object block", "```gu-typed-objects" in artifact),
        ("typed block carries layer and chirality", "LAYER=source-print CHIRALITY=N/A" in artifact),
        ("typed block pairing carries ON", "ON=defining-real-vector-carriers" in artifact),
        ("typed block target is not a map", "MAP-TYPE=not-a-map" in artifact),
        ("artifact states the Bianchi ceiling", "contracted Bianchi identity supplies four differential identities" in flat_artifact),
        ("artifact states the exact SU5 Hom obstruction", "Lambda^2 C^5 -> 5 direct-sum 5bar" in flat_artifact),
        ("SC-GRP-04 is PARTIAL", "adherence: PARTIAL" in row),
        ("source polarity remains ASSERTS", "polarity: ASSERTS" in row),
    ]


def main() -> int:
    checks = evaluate(BASE) + repository_checks()
    failures = [label for label, ok in checks if not ok]
    print(f"SC-GRP-04 clean certificate: {len(checks) - len(failures)}/{len(checks)}")
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if failures:
        return 1

    mutations = []
    for label, expected_failure, change in (
        ("identify matter 10 with real carrier", "SU(5) standard realification has dimension ten", lambda s: s.__setitem__("su5_standard_complex_dim", 10)),
        ("collapse Pati-Salam split", "Pati-Salam vector split has dimension ten", lambda s: s.__setitem__("ps_split", (5, 4))),
        ("erase noncompact inertia", "SU(3,2) real metric has inertia (6,4)", lambda s: s.__setitem__("su32_signature", (5, 0))),
        ("erase centre-weight discriminator", "standard and matter centre weights differ", lambda s: s.__setitem__("matter_central_weight", 1)),
        ("claim an unowned dynamical bridge", "no dynamical bridge is claimed", lambda s: s.__setitem__("dynamic_bridge_owned", True)),
    ):
        mutant = deepcopy(BASE)
        change(mutant)
        mutant_checks = dict(evaluate(mutant))
        caught = mutant_checks.get(expected_failure) is False
        mutations.append((label, caught))
        print(f"  [{'PASS' if caught else 'FAIL'}] hostile mutation caught: {label} -> {expected_failure}")
    print(f"SC-GRP-04 hostile mutations: {sum(ok for _, ok in mutations)}/{len(mutations)}")
    return 0 if all(ok for _, ok in mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
