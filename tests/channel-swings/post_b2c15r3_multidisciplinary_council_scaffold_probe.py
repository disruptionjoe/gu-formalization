#!/usr/bin/env python3
"""Deterministic contract probe for the post-B2C15R3 council scaffold."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/post-b2c15r3-multidisciplinary-council-next-ten-waves.json"
REPORT = ROOT / "explorations/post-b2c15r3-multidisciplinary-council-next-ten-waves-2026-08-02.md"
PW2B = ROOT / "lab/process/pw2b-literal-native-source-port.json"
PW2B_ACTION = ROOT / "lab/process/pw2b-source-composed-action-order-registry.json"
PW2C = ROOT / "lab/process/pw2c-literal-source-jacobian-full-k.json"
PW2C_ACTION = ROOT / "lab/process/pw2c-moving-action-ward-bv-registry.json"
PW2D = ROOT / "lab/process/pw2d-native-transported-shiab-action.json"
PW2D_WARD = ROOT / "lab/process/pw2d-right-tilted-ward-green-registry.json"
PW2E = ROOT / "lab/process/pw2e-finite-native-shiab-descent.json"
PW2E_METRIC = ROOT / "lab/process/pw2e-mixed-metric-frechet-native-ward-registry.json"
PW2F = ROOT / "lab/process/pw2f-native-top-order-metric-ward-registry.json"


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
    if data.get("status") != "PW2F_HOSTILE_CORRECTION_LC_SUBROUTE_PASS_COMPLETE_DELTAK_AND_FULL_Y14_C3_OPEN_PW2F_R_NEXT":
        errors.append("status must record the PW2F hostile correction and PW2F-R next")

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
    expected_statuses = ["CONDITIONAL_PASS_PW2_ENABLED", "PW2F_HOSTILE_CORRECTION_COMPLETE_DELTAK_AND_FULL_Y14_C3_REQUIRED"] + ["BLOCKED_ON_DEPENDENCIES"] * 8
    if [wave.get("status") for wave in waves] != expected_statuses:
        errors.append("wave status frontier must record the hostile-corrected PW2F/PW2F-R gate and keep PW3 blocked")
    pw1_review = waves[0].get("review_receipts", {}) if waves else {}
    if pw1_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW1 pre-assessment receipt incomplete")
    if pw1_review.get("post_review", {}).get("status") != "COMPLETE":
        errors.append("PW1 hostile post-review receipt incomplete")
    if pw1_review.get("post_review", {}).get("must_fix"):
        errors.append("PW1 hostile post-review retains must-fix items")
    if len(pw1_review.get("post_review", {}).get("rerun_digests", [])) < 3:
        errors.append("PW1 hostile post-review rerun receipts missing")
    pw2_review = waves[1].get("review_receipts", {}) if len(waves) > 1 else {}
    if pw2_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW2 pre-assessment receipt incomplete")
    if pw2_review.get("post_review", {}).get("status") != "COMPLETE":
        errors.append("PW2 hostile post-review receipt incomplete")
    if pw2_review.get("post_review", {}).get("must_fix"):
        errors.append("PW2 hostile post-review retains must-fix items")
    if len(pw2_review.get("post_review", {}).get("rerun_receipts", [])) < 3:
        errors.append("PW2 hostile post-review rerun receipts missing")
    pw2a_review = waves[1].get("pw2a_review_receipts", {}) if len(waves) > 1 else {}
    if pw2a_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW2A pre-assessment receipt incomplete")
    if pw2a_review.get("post_review", {}).get("status") != "COMPLETE":
        errors.append("PW2A hostile post-review receipt incomplete")
    if pw2a_review.get("post_review", {}).get("must_fix"):
        errors.append("PW2A hostile post-review retains must-fix items")
    if len(pw2a_review.get("post_review", {}).get("rerun_receipts", [])) < 3:
        errors.append("PW2A hostile post-review rerun receipts missing")
    pw2b_review = waves[1].get("pw2b_review_receipts", {}) if len(waves) > 1 else {}
    if pw2b_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW2B pre-assessment receipt incomplete")
    if pw2b_review.get("post_review", {}).get("status") != "COMPLETE":
        errors.append("PW2B hostile post-review receipt incomplete")
    if pw2b_review.get("post_review", {}).get("must_fix"):
        errors.append("PW2B hostile post-review retains must-fix items")
    if len(pw2b_review.get("post_review", {}).get("rerun_receipts", [])) < 3:
        errors.append("PW2B hostile post-review rerun receipts missing")
    pw2c_review = waves[1].get("pw2c_review_receipts", {}) if len(waves) > 1 else {}
    if pw2c_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW2C pre-assessment receipt incomplete")
    if pw2c_review.get("post_review", {}).get("status") != "COMPLETE":
        errors.append("PW2C hostile post-review receipt incomplete")
    if pw2c_review.get("post_review", {}).get("must_fix"):
        errors.append("PW2C hostile post-review retains must-fix items")
    if len(pw2c_review.get("post_review", {}).get("rerun_receipts", [])) < 3:
        errors.append("PW2C hostile post-review rerun receipts missing")
    pw2d_review = waves[1].get("pw2d_review_receipts", {}) if len(waves) > 1 else {}
    if pw2d_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW2D pre-assessment receipt incomplete")
    if pw2d_review.get("post_review", {}).get("status") != "COMPLETE_AFTER_REPAIR":
        errors.append("PW2D hostile post-review receipt incomplete")
    if pw2d_review.get("post_review", {}).get("must_fix"):
        errors.append("PW2D hostile post-review retains must-fix items")
    if len(pw2d_review.get("post_review", {}).get("rerun_receipts", [])) < 3:
        errors.append("PW2D hostile post-review rerun receipts missing")
    pw2e_review = waves[1].get("pw2e_review_receipts", {}) if len(waves) > 1 else {}
    if pw2e_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW2E pre-assessment receipt incomplete")
    if pw2e_review.get("post_review", {}).get("status") != "COMPLETE_AFTER_REPAIR":
        errors.append("PW2E hostile post-review receipt incomplete")
    if pw2e_review.get("post_review", {}).get("must_fix"):
        errors.append("PW2E hostile post-review retains must-fix items")
    if len(pw2e_review.get("post_review", {}).get("rerun_receipts", [])) < 3:
        errors.append("PW2E hostile post-review rerun receipts missing")
    pw2f_review = waves[1].get("pw2f_review_receipts", {}) if len(waves) > 1 else {}
    if pw2f_review.get("pre_assessment", {}).get("status") != "COMPLETE":
        errors.append("PW2F pre-assessment receipt incomplete")
    if pw2f_review.get("post_review", {}).get("status") not in {"COMPLETE", "COMPLETE_AFTER_REPAIR"}:
        errors.append("PW2F hostile post-review receipt incomplete")
    if pw2f_review.get("post_review", {}).get("must_fix"):
        errors.append("PW2F hostile post-review retains must-fix items")
    if len(pw2f_review.get("post_review", {}).get("rerun_receipts", [])) < 5:
        errors.append("PW2F hostile post-review rerun receipts missing")
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
    if "PW3 plus all later waves remain unexecuted" not in nonclaims:
        errors.append("explicit PW3 execution pause missing")
    return errors


def expect_plant_failure(base: dict[str, object], mutator) -> None:
    planted = copy.deepcopy(base)
    mutator(planted)
    failures = validate(planted)
    if not failures:
        raise AssertionError("planted invalid scaffold was accepted")


def main() -> None:
    data = load_registry()
    pw2b = json.loads(PW2B.read_text(), object_pairs_hook=unique_object)
    action = json.loads(PW2B_ACTION.read_text(), object_pairs_hook=unique_object)
    pw2c = json.loads(PW2C.read_text(), object_pairs_hook=unique_object)
    pw2c_action = json.loads(PW2C_ACTION.read_text(), object_pairs_hook=unique_object)
    pw2d = json.loads(PW2D.read_text(), object_pairs_hook=unique_object)
    pw2d_ward = json.loads(PW2D_WARD.read_text(), object_pairs_hook=unique_object)
    pw2e = json.loads(PW2E.read_text(), object_pairs_hook=unique_object)
    pw2e_metric = json.loads(PW2E_METRIC.read_text(), object_pairs_hook=unique_object)
    pw2f = json.loads(PW2F.read_text(), object_pairs_hook=unique_object)
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
        "PW3 stays blocked",
        "PW2F-R-COMPLETE-DERIVED-K-TOP-ORDER-AND-FULL-Y14-C3-HELMHOLTZ-CLASSIFICATION",
        "P1/P2/P3 remain correctly unused",
        "constraint surplus",
    ]:
        if token not in report:
            raise AssertionError(f"report token missing: {token}")
        exact_checks += 1

    exact_checks += 1  # strict registry validator
    if not pw2b["status"].startswith("PW2B_ACTIVE_REAL_FORM_BRIDGE_ADMISSIBILITY"):
        raise AssertionError("PW2B active-real-form scope drifted")
    if not action["status"].startswith("SOURCE_ORBIT_VARPI_ORDER2_ATTAINABLE"):
        raise AssertionError("PW2B action attainability scope drifted")
    if pw2b["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED":
        raise AssertionError("PW2B spent the external datum")
    if not pw2c["status"].startswith("PW2C_FIXED_QG_ACTIVE_SOURCE_ROOT"):
        raise AssertionError("PW2C source-Jacobian scope drifted")
    if not pw2c_action["status"].startswith("PW2C_STRUCTURAL_SOURCE_PULLBACK"):
        raise AssertionError("PW2C moving-action scope drifted")
    if pw2c["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED":
        raise AssertionError("PW2C spent the external datum")
    if pw2c_action["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED":
        raise AssertionError("PW2C action spent the external datum")
    if not pw2d["status"].startswith("PW2D_PARTIAL_FIXED_METRIC"):
        raise AssertionError("PW2D fixed-metric/partial scope drifted")
    if pw2d["transported_shiab"]["explicit_transported_projector_live_branches"] != 0:
        raise AssertionError("PW2D resurrected the killed projector-motion claim")
    if pw2d["native_action_jet"]["full_quadratic_responses"] != [0, "3/8+kappa1", "3/8+kappa1", 0, 0]:
        raise AssertionError("PW2D full distortion-norm-plus-curvature response drifted")
    if pw2d["metric_owner_bank"]["action_or_euler_metric_rank"] != "NOT_COMPUTED":
        raise AssertionError("PW2D promoted coefficient rank to action/Euler rank")
    if not pw2d_ward["status"].startswith("PW2D_STRUCTURAL_RESIDUAL_RIGHT_TILTED"):
        raise AssertionError("PW2D structural Ward scope drifted")
    if pw2d_ward["frechet_green"]["endpoint"] != "243073/216000":
        raise AssertionError("PW2D repaired total preboundary endpoint drifted")
    if pw2d["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED" or pw2d_ward["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED":
        raise AssertionError("PW2D spent the external datum")
    if not pw2e["status"].startswith("PW2E_FINITE_ACTIVE_NATIVE_OPERATOR"):
        raise AssertionError("PW2E finite active scope drifted")
    if pw2e["projector_correction"]["correct_result"].find("rank-8256") < 0:
        raise AssertionError("PW2E projector correction drifted")
    if not pw2e_metric["status"].startswith("PW2E_MIXED_OWNER_INVENTORY"):
        raise AssertionError("PW2E metric-owner scope drifted")
    if "may cancel" not in pw2e_metric["jet_determinacy"]["interpretation"]:
        raise AssertionError("PW2E promoted possible fourth-jet sensitivity")
    if not pw2e["external_datum"].startswith("P1/P2/P3 UNCHANGED AND UNUSED") or not pw2e_metric["external_datum"].startswith("P1/P2/P3 UNCHANGED AND UNUSED"):
        raise AssertionError("PW2E spent the external datum")
    if not pw2f["status"].startswith("PW2F_HOSTILE_REVIEW_CORRECTION"):
        raise AssertionError("PW2F hostile-corrected scope drifted")
    if not pw2f["result"]["base_fourth_metric_coefficient"].startswith("OPEN_AFTER_HOSTILE_REVIEW"):
        raise AssertionError("PW2F fourth-order open boundary drifted")
    if "RANK10" not in pw2f["result"]["held_out_metric_third_contributions"]:
        raise AssertionError("PW2F held-out vertical C3 witness drifted")
    if pw2f["result"]["selected_curvature_input_bank"]["exact_rank"] != 7:
        raise AssertionError("PW2F selected C2 rank drifted")
    if pw2f["result"]["moving_shiab_coefficient_bank"]["exact_rank"] != 10:
        raise AssertionError("PW2F moving coefficient rank drifted")
    if pw2f["diffeomorphism_ward"]["status"] != "STRUCTURAL_1D_FORMAL_NATURAL_LIFT_NOETHER_AND_GREEN_SCHEMA_PASS_NATIVE_EVALUATION_OPEN":
        raise AssertionError("PW2F Ward scope drifted")
    if pw2f["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED":
        raise AssertionError("PW2F spent the external datum")
    exact_checks += 25
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
        lambda d: d["waves"][1]["review_receipts"]["post_review"].update(must_fix=["live blocker"]),
        lambda d: d["waves"][1]["pw2a_review_receipts"]["post_review"].update(must_fix=["live blocker"]),
        lambda d: d["waves"][1]["pw2b_review_receipts"]["post_review"].update(must_fix=["live blocker"]),
        lambda d: d["waves"][1]["pw2c_review_receipts"]["post_review"].update(must_fix=["live blocker"]),
        lambda d: d["waves"][1]["pw2d_review_receipts"]["post_review"].update(must_fix=["live blocker"]),
        lambda d: d["waves"][1]["pw2e_review_receipts"]["post_review"].update(must_fix=["live blocker"]),
        lambda d: d["waves"][1]["pw2f_review_receipts"]["post_review"].update(must_fix=["live blocker"]),
    ]
    for plant in plants:
        expect_plant_failure(data, plant)

    print(
        f"PASS: {exact_checks} exact scaffold checks + "
        f"{len(plants)} planted rejections = {exact_checks + len(plants)}"
    )


if __name__ == "__main__":
    main()
