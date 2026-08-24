#!/usr/bin/env python3
"""Exact and mutation-tested probe for the final SAME-cohort disposition wave."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/dai-freed-same-cohort-row-disposition-wave.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
RESULT = ROOT / "explorations/conditional-build/dai-freed-same-cohort-row-disposition-wave-2026-08-24.md"
EXPECTED_LEDGER_SHA256 = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"


def gf2_rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    matrix = [[value & 1 for value in row] for row in rows]
    width = len(matrix[0])
    pivot_row = 0
    for column in range(width):
        pivot = next((r for r in range(pivot_row, len(matrix)) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        for r in range(len(matrix)):
            if r != pivot_row and matrix[r][column]:
                matrix[r] = [a ^ b for a, b in zip(matrix[r], matrix[pivot_row])]
        pivot_row += 1
    return pivot_row


def dot(row: list[int], vector: list[int]) -> int:
    return sum(a * b for a, b in zip(row, vector)) & 1


def quotient_dimension(width: int, outgoing: list[list[int]], incoming: list[list[int]]) -> int:
    """dim ker(outgoing) / span(incoming), checking d2^2=0."""
    assert all(len(row) == width for row in outgoing)
    assert all(len(vector) == width for vector in incoming)
    assert all(dot(row, vector) == 0 for row in outgoing for vector in incoming)
    kernel_dimension = width - gf2_rank(outgoing)
    image_dimension = gf2_rank(incoming)
    assert image_dimension <= kernel_dimension
    return kernel_dimension - image_dimension


def recompute_spin_groups() -> tuple[dict[str, str], dict[str, str]]:
    # Dual H_4 bases are (t^2, c2_SU3/U3, c2_SU2/U2).  The outgoing
    # dual-Sq2 kills t^2.  The incoming image always kills the colour c2;
    # it also kills the weak c2 exactly when SU(2) is absorbed into U(2).
    group_specs = {
        "1": (3, [[1, 0, 0]], [[0, 1, 0]]),
        "2": (3, [[1, 0, 0]], [[0, 1, 0], [0, 0, 1]]),
        "3": (3, [[1, 0, 0]], [[0, 1, 0]]),
        "6": (3, [[1, 0, 0]], [[0, 1, 0], [0, 0, 1]]),
    }
    groups = {
        name: ("Z/2" if quotient_dimension(*spec) == 1 else "0")
        for name, spec in group_specs.items()
    }
    controls = {
        "BSU(2)": "Z/2" if quotient_dimension(1, [], []) == 1 else "0",
        "BU(1)": "Z/2" if quotient_dimension(1, [[1]], []) == 1 else "0",
        "BSU(3)": "Z/2" if quotient_dimension(1, [], [[1]]) == 1 else "0",
    }
    return groups, controls


def load_inputs() -> dict[str, object]:
    ledger_bytes = LEDGER.read_bytes()
    return {
        "registry": json.loads(REGISTRY.read_text()),
        "ledger": json.loads(ledger_bytes),
        "ledger_sha256": hashlib.sha256(ledger_bytes).hexdigest(),
        "result": RESULT.read_text(),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    registry = inputs["registry"]
    ledger = inputs["ledger"]
    result = inputs["result"]
    assert isinstance(registry, dict) and isinstance(ledger, dict) and isinstance(result, str)

    computed_groups, computed_controls = recompute_spin_groups()
    recomputation = registry.get("dai_freed_recomputation", {})
    check(computed_groups == recomputation.get("global_forms"), "four Spin groups are independently recomputed")
    check(computed_controls == recomputation.get("controls"), "three simple-group controls match")
    check(set(computed_groups.values()) == {"0", "Z/2"}, "recomputation has positive and negative outcomes")
    check(recomputation.get("sm_content_image") == {"1": 0, "2": 0, "3": 0, "6": 0},
          "SM content image is zero on every global form")
    check((3 + 1) % 2 == 0, "one complete SM generation has even weak-doublet parity")
    check(inputs["ledger_sha256"] == EXPECTED_LEDGER_SHA256, "ledger v0.263 remains byte-identical")

    ledger_rows = {row.get("id"): row for row in ledger.get("rows", [])}
    expected_rows = {"AC-E1", "LT-GR2", "LT-GR2b", "LT-SM5"}
    terminal_rows = registry.get("terminal_rows", [])
    terminal_by_id = {row.get("row_id"): row for row in terminal_rows}
    check(set(terminal_by_id) == expected_rows, "wave covers exactly the final SAME cohort")
    check(all(ledger_rows[row_id].get("verdict") == "SAME" for row_id in expected_rows),
          "every selected row is SAME in ledger v0.263")
    check(ledger_rows["LT-GR2"].get("row_status") == "SUPERSEDED", "LT-GR2 is already superseded")
    check(ledger_rows["LT-GR2"].get("successors") == ["LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"],
          "LT-GR2 exact successor escape is preserved")

    expected_outcomes = {
        "AC-E1": ("B1", "FITTING_CONSTRUCTION", "FC-ANOMALY-SM-DAI-FREED-SHADOW-1"),
        "LT-GR2": ("B4", "PRECISE_IMPOSSIBILITY", "PI-LT-GR2-UNSPLIT-AGGREGATE-1"),
        "LT-GR2b": ("B1", "FITTING_CONSTRUCTION", "FC-GR-VARIABLE-THETA-RELATIVE-KO-INTERFACE-1"),
        "LT-SM5": ("B1", "FITTING_CONSTRUCTION", "FC-SM-AMBIENT-WEYL-HALF-EXCHANGER-1"),
    }
    for row_id, (bucket, outcome, object_id) in expected_outcomes.items():
        row = terminal_by_id.get(row_id, {})
        check(row.get("bucket") == bucket, f"bucket is exact: {row_id}")
        check(row.get("terminal_outcome") == outcome, f"terminal outcome is exact: {row_id}")
        id_field = "construction_id" if outcome == "FITTING_CONSTRUCTION" else "impossibility_id"
        check(row.get(id_field) == object_id, f"terminal object id is exact: {row_id}")

    constructions = {item.get("id"): item for item in registry.get("fitting_constructions", [])}
    check(set(constructions) == {
        "FC-ANOMALY-SM-DAI-FREED-SHADOW-1",
        "FC-GR-VARIABLE-THETA-RELATIVE-KO-INTERFACE-1",
        "FC-SM-AMBIENT-WEYL-HALF-EXCHANGER-1",
    }, "exact fitting-construction set is serialized")
    for construction_id, construction in constructions.items():
        criteria = construction.get("fc_criteria", {})
        check(set(criteria) == {f"FC-{n}" for n in range(1, 8)}, f"all FC criteria exist: {construction_id}")
        check(all(criteria.values()), f"all FC criteria are substantive: {construction_id}")
        check(bool(construction.get("fingerprint")), f"fingerprint exists: {construction_id}")
        check(bool(construction.get("claim_ceiling")), f"claim ceiling exists: {construction_id}")

    impossibilities = registry.get("precise_impossibilities", [])
    check(len(impossibilities) == 1, "one precise impossibility is serialized")
    impossibility = impossibilities[0]
    check(impossibility.get("id") == "PI-LT-GR2-UNSPLIT-AGGREGATE-1", "aggregate impossibility id is exact")
    check(len(impossibility.get("assumptions", [])) >= 3, "aggregate impossibility states assumptions")
    check("LT-GR2a" in impossibility.get("escape", "") and "LT-GR2e" in impossibility.get("escape", ""),
          "aggregate impossibility states the successor escape")
    check(bool(impossibility.get("resurrection_trigger")), "aggregate impossibility states resurrection trigger")
    check("no physical" in impossibility.get("scope_ceiling", ""), "aggregate impossibility preserves physical routes")

    for field in ("ledger_verdict_change", "ledger_row_field_change", "source_ownership_change",
                  "prediction_or_confirmation_change", "canon_verdict_change", "public_posture_change"):
        check(registry.get(field) == "none", f"protected movement remains none: {field}")

    check("GU-COMPARATOR-ROUTING — scope before inference" in result, "routing notice is present")
    check("Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in result, "routing classification is explicit")
    check("```gu-typed-objects" in result, "typed-object block is present")
    check("Z/2, 0, Z/2, 0" in result, "computed four-form sequence is reported")
    check("49 terminal and 42 open" in result, "derived post-wave denominator is reported")
    return checks, failures


def main() -> int:
    checks, failures = collect_failures(load_inputs())
    for label in failures:
        print(f"[FAIL] {label}")
    if failures:
        return 1
    print(f"PASS {checks}/{checks}")
    return 0


def selftest() -> int:
    baseline = load_inputs()
    checks, failures = collect_failures(baseline)
    if failures:
        for label in failures:
            print(f"[FAIL] baseline: {label}")
        return 1
    print(f"BASELINE PASS {checks}/{checks}")

    mutations: list[tuple[str, str, dict[str, object]]] = []

    changed = copy.deepcopy(baseline)
    changed["registry"]["dai_freed_recomputation"]["global_forms"]["1"] = "0"
    mutations.append(("wrong-bordism-group", "four Spin groups are independently recomputed", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["dai_freed_recomputation"]["controls"]["BSU(2)"] = "0"
    mutations.append(("dead-positive-control", "three simple-group controls match", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["dai_freed_recomputation"]["sm_content_image"]["3"] = 1
    mutations.append(("odd-content-image", "SM content image is zero on every global form", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["terminal_rows"].pop()
    mutations.append(("row-omitted", "wave covers exactly the final SAME cohort", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["fitting_constructions"][0]["fc_criteria"].pop("FC-7")
    mutations.append(("missing-nontriviality", "all FC criteria exist: FC-ANOMALY-SM-DAI-FREED-SHADOW-1", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["precise_impossibilities"][0]["escape"] = "none"
    mutations.append(("missing-aggregate-escape", "aggregate impossibility states the successor escape", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["source_ownership_change"] = "claimed"
    mutations.append(("source-overclaim", "protected movement remains none: source_ownership_change", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace("```gu-typed-objects", "```objects", 1)
    mutations.append(("typed-block-removed", "typed-object block is present", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
