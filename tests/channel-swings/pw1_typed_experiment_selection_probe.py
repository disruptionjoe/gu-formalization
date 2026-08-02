#!/usr/bin/env python3
"""Fail-closed exact algorithm scaffold for PW1 experiment selection."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/pw1-typed-experiment-registry.json"
RESULT = ROOT / "lab/process/pw1-source-native-port-superig-interface.json"


class DuplicateKeyError(ValueError):
    pass


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def load() -> dict[str, object]:
    return json.loads(REGISTRY.read_text(), object_pairs_hook=unique_object)


def exact_rank(rows: list[list[int | Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(value) for value in row] for row in rows]
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    pivot_row = 0
    for col in range(n_cols):
        pivot = next((row for row in range(pivot_row, n_rows) if matrix[row][col]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row or matrix[row][col] == 0:
                continue
            factor = matrix[row][col]
            matrix[row] = [left - factor * right for left, right in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
    return pivot_row


def separated_pairs(rows: list[list[int]], candidate: list[int]) -> int:
    augmented = rows + [candidate]
    columns = list(zip(*augmented))
    return sum(columns[left] != columns[right] for left in range(len(columns)) for right in range(left + 1, len(columns)))


def select(fixtures: list[dict[str, object]]) -> list[str]:
    discovery = [fixture for fixture in fixtures if fixture["role"] == "DISCOVERY"]
    selected: list[dict[str, object]] = []
    current_rows: list[list[int]] = []
    current_rank = 0
    while True:
        scored: list[tuple[int, int, str, dict[str, object]]] = []
        for fixture in discovery:
            if fixture in selected:
                continue
            response = fixture["response"]
            gain = exact_rank(current_rows + [response]) - current_rank
            separation = separated_pairs(current_rows, response)
            scored.append((-gain, -separation, fixture["id"], fixture))
        if not scored:
            break
        _, _, _, winner = min(scored)
        response = winner["response"]
        new_rank = exact_rank(current_rows + [response])
        if new_rank == current_rank:
            break
        selected.append(winner)
        current_rows.append(response)
        current_rank = new_rank
    return [fixture["id"] for fixture in selected]


def validate(data: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if data.get("status") != "EXACT_SELECTOR_ALGORITHM_SCAFFOLD":
        errors.append("selector scaffold status changed")
    if data.get("artifact_role") != "SEARCH_SCHEDULER_NOT_SCIENTIFIC_EVIDENCE":
        errors.append("selector was promoted to evidence")
    if data.get("candidate_kinds") != ["PORT", "ALT", "ACTION_INTERFACE"]:
        errors.append("candidate kind schema changed")
    if data.get("disposition_vocabulary") != [
        "REJECTED_TYPE",
        "EXACT_COUNTEREXAMPLE",
        "SURVIVES_FINITE_FIXTURES",
        "NOT_EVALUABLE",
    ]:
        errors.append("fail-closed imported-disposition vocabulary changed")
    if data.get("response_axis_schema") != [
        "synthetic_type_axis",
        "synthetic_curvature_axis",
        "synthetic_bracket_axis",
        "synthetic_affine_axis",
    ]:
        errors.append("synthetic response-axis schema changed")
    if "do not correspond" not in data.get("response_boundary", ""):
        errors.append("synthetic response boundary missing")

    candidates = data.get("candidates", [])
    candidate_ids = [candidate.get("id") for candidate in candidates]
    if len(candidate_ids) != len(set(candidate_ids)):
        errors.append("duplicate candidate ID")
    for candidate in candidates:
        for field in ["kind", "domain", "codomain", "structure", "owners", "coefficients", "obligations", "imported_disposition", "evidence_ref"]:
            if field not in candidate:
                errors.append(f"candidate {candidate.get('id')} lacks {field}")
        if candidate.get("imported_disposition") not in data.get("disposition_vocabulary", []):
            errors.append(f"candidate {candidate.get('id')} has an illegal imported disposition")
        if not candidate.get("evidence_ref"):
            errors.append(f"candidate {candidate.get('id')} lacks evidence reference")

    fixtures = data.get("fixtures", [])
    fixture_ids = [fixture.get("id") for fixture in fixtures]
    fixture_hashes = [fixture.get("content_digest") for fixture in fixtures]
    if len(fixture_ids) != len(set(fixture_ids)):
        errors.append("duplicate fixture ID")
    if len(fixture_hashes) != len(set(fixture_hashes)):
        errors.append("duplicate fixture hash")
    widths = {len(fixture.get("response", [])) for fixture in fixtures}
    if widths != {4}:
        errors.append("fixture response width changed")
    roles = {fixture.get("role") for fixture in fixtures}
    if roles != {"DISCOVERY", "RESERVED_CONTROL"}:
        errors.append("fixture role schema changed")

    recomputed_digests: list[str] = []
    for fixture in fixtures:
        response = fixture.get("response", [])
        if any(type(value) is not int for value in response):
            errors.append(f"fixture {fixture.get('id')} contains a nonintegral exact scalar")
        digest = hashlib.sha256(
            json.dumps({"response": response}, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        recomputed_digests.append(digest)
        if fixture.get("content_digest") != digest:
            errors.append(f"fixture {fixture.get('id')} content digest mismatch")
    if len(recomputed_digests) != len(set(recomputed_digests)):
        errors.append("duplicate fixture content across roles or IDs")

    discovery_hashes = {fixture["content_digest"] for fixture in fixtures if fixture["role"] == "DISCOVERY"}
    reserved_hashes = {fixture["content_digest"] for fixture in fixtures if fixture["role"] == "RESERVED_CONTROL"}
    if discovery_hashes & reserved_hashes:
        errors.append("reserved-control leakage by content")
    if widths == {4}:
        selected = select(fixtures)
        if selected != data.get("selected_discovery_fixtures"):
            errors.append(f"frozen exact selection differs: {selected}")
        if any(fixture_id.startswith("R-") for fixture_id in selected):
            errors.append("reserved control leaked into selection")
        if exact_rank([next(f["response"] for f in fixtures if f["id"] == fixture_id) for fixture_id in selected]) != 4:
            errors.append("selected discovery set lacks full exact rank")

    if "exact replay" not in data.get("reconstruction_rule", ""):
        errors.append("exact reconstruction replay missing")
    if len(data.get("future_executable_plant_backlog", [])) < 18:
        errors.append("future plant backlog incomplete")
    if len(data.get("executed_mutation_plants", [])) < 10:
        errors.append("executed mutation inventory incomplete")
    return errors


def expect_failure(base: dict[str, object], mutator) -> None:
    planted = copy.deepcopy(base)
    mutator(planted)
    if not validate(planted):
        raise AssertionError("planted invalid experiment registry was accepted")


def main() -> None:
    data = load()
    failures = validate(data)
    if failures:
        raise AssertionError("\n".join(failures))

    exact_checks = 12 + len(data["candidates"]) + len(data["fixtures"])
    canonical_digest = hashlib.sha256(REGISTRY.read_bytes()).hexdigest()
    result = json.loads(RESULT.read_text(), object_pairs_hook=unique_object)
    assert result["pw1_c_experiment_harness"]["registry_sha256"] == canonical_digest
    exact_checks += 1

    plants = [
        lambda d: d.update(status="SCIENTIFICALLY_CERTIFIED"),
        lambda d: d.update(artifact_role="SCIENTIFIC_CERTIFICATE"),
        lambda d: d.update(disposition_vocabulary=d["disposition_vocabulary"] + ["CERTIFIED"]),
        lambda d: d["candidates"][0].pop("owners"),
        lambda d: d["candidates"][0].update(imported_disposition="PROBABLY_TRUE"),
        lambda d: d["fixtures"][5].update(content_digest=d["fixtures"][0]["content_digest"]),
        lambda d: d["fixtures"][5].update(response=d["fixtures"][0]["response"]),
        lambda d: d["fixtures"][0].update(response=[1.0, 0, 0, 0]),
        lambda d: d.update(selected_discovery_fixtures=["R-01-MOVING"]),
        lambda d: d.update(reconstruction_rule="accept floating fit"),
        lambda d: d.update(future_executable_plant_backlog=[]),
    ]
    for plant in plants:
        expect_failure(data, plant)

    print(f"PASS: {exact_checks} exact + {len(plants)} planted = {exact_checks + len(plants)}")


if __name__ == "__main__":
    main()
