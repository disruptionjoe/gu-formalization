#!/usr/bin/env python3
"""Deterministic contract probe for the post-B2C15R3 council scaffold."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/post-b2c15r3-multidisciplinary-council-next-ten-waves.json"
REPORT = ROOT / "explorations/post-b2c15r3-multidisciplinary-council-next-ten-waves-2026-08-02.md"


class DuplicateKeyError(ValueError):
    pass


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def load_registry() -> dict[str, object]:
    return json.loads(REGISTRY.read_text(), object_pairs_hook=unique_object)


def validate(data: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if data.get("status") != "PW1_CONDITIONAL_PASS_PW2_ENABLED":
        errors.append("status must be PW1_CONDITIONAL_PASS_PW2_ENABLED")

    layer0 = data.get("layer0_distinctions", [])
    if len(layer0) < 8:
        errors.append("at least eight Layer-0 distinctions are required")

    lanes = data.get("lanes", [])
    lane_ids = [lane.get("id") for lane in lanes]
    if lane_ids != ["INDEPENDENT_NATIVE", "ERIC_GUIDED", "CURT_COMPARATOR"]:
        errors.append("lane separation or ordering changed")
    curt = next((lane for lane in lanes if lane.get("id") == "CURT_COMPARATOR"), {})
    if "TG-1 AND TG-2 AND TG-3" not in curt.get("rule", ""):
        errors.append("conjunctive Curt promotion guard missing")

    specialists = data.get("specialist_lenses", [])
    if len(specialists) < 10:
        errors.append("fewer than ten specialist lenses")
    specialist_ids = [item.get("id") for item in specialists]
    if len(specialist_ids) != len(set(specialist_ids)):
        errors.append("duplicate specialist lens id")
    specialist_blob = json.dumps(specialists)
    for token in [
        "symplectic",
        "hyperbolic",
        "ZK",
        "distributed",
        "neural",
        "statistics",
        "counterfactual",
    ]:
        if token.lower() not in specialist_blob.lower():
            errors.append(f"required specialist token missing: {token}")

    engineers = data.get("engineering_personas", [])
    if len(engineers) != 10:
        errors.append("exactly ten engineering personas are required")
    engineer_ids = [item.get("id") for item in engineers]
    if len(engineer_ids) != len(set(engineer_ids)):
        errors.append("duplicate engineering persona id")
    for engineer in engineers:
        for field in ["persona", "shop_floor_view", "sees_missing", "would_do", "tripwire"]:
            if not engineer.get(field):
                errors.append(f"engineering persona {engineer.get('id')} lacks {field}")

    waves = data.get("waves", [])
    if len(waves) != 10:
        errors.append("exactly ten waves are required")
    wave_ids = [wave.get("id") for wave in waves]
    if wave_ids != [f"PW{i}" for i in range(1, 11)]:
        errors.append("wave IDs or execution order changed")
    if data.get("execution_order") != wave_ids:
        errors.append("execution_order must equal wave order")
    expected_statuses = ["CONDITIONAL_PASS_PW2_ENABLED", "NEXT"] + ["BLOCKED_ON_DEPENDENCIES"] * 8
    if [wave.get("status") for wave in waves] != expected_statuses:
        errors.append("wave status frontier must be PW1 conditional-pass and PW2 next")
    pw1_review = waves[0].get("review_receipts", {}) if waves else {}
    if pw1_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW1 pre-assessment receipt incomplete")
    if pw1_review.get("post_review", {}).get("status") != "COMPLETE":
        errors.append("PW1 hostile post-review receipt incomplete")
    if pw1_review.get("post_review", {}).get("must_fix"):
        errors.append("PW1 hostile post-review retains must-fix items")
    if len(pw1_review.get("post_review", {}).get("rerun_digests", [])) < 3:
        errors.append("PW1 hostile post-review rerun receipts missing")
    seen: set[str] = set()
    for wave in waves:
        wave_id = wave.get("id", "UNKNOWN")
        for field in [
            "title",
            "objective",
            "deliverables",
            "information_gain_question",
            "parallel_swings",
            "kill_conditions",
            "route_if_killed",
            "ml_role",
            "exit",
        ]:
            if not wave.get(field):
                errors.append(f"{wave_id} lacks {field}")
        deps = wave.get("depends_on", [])
        for dep in deps:
            if dep not in seen:
                errors.append(f"{wave_id} has forward or missing dependency {dep}")
        seen.add(wave_id)

    if "gauge" not in data.get("constraint_surplus_rule", "").lower():
        errors.append("constraint surplus is not gauge-quotiented")
    pipeline = data.get("ml_verification_pipeline", [])
    if len(pipeline) != 5 or "certificate" not in pipeline[-1].lower():
        errors.append("ML verification pipeline does not terminate in a certificate")
    datum_rule = data.get("datum_rule", "")
    for token in ["bundle port", "jet owner", "observation projector", "domain"]:
        if token not in datum_rule:
            errors.append(f"datum anti-smuggling token missing: {token}")

    review = data.get("wave_review_protocol", {})
    if review.get("required") is not True:
        errors.append("two-sided specialist review is not mandatory")
    if "divergent" not in review.get("pre_assessment", ""):
        errors.append("divergent pre-assessment missing")
    if "hostile" not in review.get("post_review", ""):
        errors.append("hostile post-review missing")
    if len(review.get("minimum_lenses", [])) < 5:
        errors.append("review lens floor missing")

    nonclaims = " ".join(data.get("nonclaims", []))
    if "PW2 and all later waves remain unexecuted" not in nonclaims:
        errors.append("explicit PW2 execution pause missing")
    return errors


def expect_plant_failure(base: dict[str, object], mutator) -> None:
    planted = copy.deepcopy(base)
    mutator(planted)
    failures = validate(planted)
    if not failures:
        raise AssertionError("planted invalid scaffold was accepted")


def main() -> None:
    data = load_registry()
    failures = validate(data)
    if failures:
        raise AssertionError("\n".join(failures))

    report = REPORT.read_text()
    exact_checks = 0
    for token in [
        "## Ten inline engineering personas",
        "### 4. Pressure-vessel and structural-integrity engineer",
        "### 6. Distributed-systems and site-reliability engineer",
        "### 7. ZK protocol and proof-circuit engineer",
        "### 10. Systems-integration and verification engineer",
        "## The next ten big waves",
        "## Mandatory review protocol for every wave",
        "divergent specialist pre-assessment",
        "hostile specialist post-review",
        "## Execution checkpoint",
        "No PW2 or later wave",
        "P1/P2/P3 remain correctly unused",
        "constraint surplus",
    ]:
        if token not in report:
            raise AssertionError(f"report token missing: {token}")
        exact_checks += 1

    exact_checks += 1  # strict registry validator
    exact_checks += len(data["specialist_lenses"])
    exact_checks += len(data["engineering_personas"])
    exact_checks += len(data["waves"])

    plants = [
        lambda d: d.update(status="EXECUTED"),
        lambda d: d["engineering_personas"].pop(),
        lambda d: d["waves"].pop(),
        lambda d: d["waves"][3].update(depends_on=["PW10"]),
        lambda d: d["waves"][1].update(kill_conditions=[]),
        lambda d: d.update(ml_verification_pipeline=["neural verdict"]),
        lambda d: d.update(datum_rule="P1 selects everything"),
        lambda d: d["lanes"][2].update(rule="promote on TG-1"),
        lambda d: d["waves"][1].update(status="COMPLETE"),
        lambda d: d["wave_review_protocol"].update(required=False),
        lambda d: d["waves"][0]["review_receipts"]["post_review"].update(must_fix=["live blocker"]),
    ]
    for plant in plants:
        expect_plant_failure(data, plant)

    print(
        f"PASS: {exact_checks} exact scaffold checks + "
        f"{len(plants)} planted rejections = {exact_checks + len(plants)}"
    )


if __name__ == "__main__":
    main()
