#!/usr/bin/env python3
"""Probe the bounded W154/W229-to-K77 owner qualification result."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/w154-w229-k77-action-owner-qualification.json"
RESULT = ROOT / "explorations/conditional-build/w154-w229-k77-action-owner-qualification-2026-08-24.md"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
STATUS = ROOT / "RESEARCH-STATUS.md"
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
DISPOSITIONS = ROOT / "lab/process/phenomenology-disposition-register-v0.1.json"

EXPECTED_LEDGER_SHA256 = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"
EXPECTED_DISPOSITIONS_SHA256 = "759eb1dcad644a7ed28d7b56d1fbbf43e1d2065af7352105cb02ccde0bf2d728"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "current": CURRENT.read_text(),
        "next": NEXT.read_text(),
        "status": STATUS.read_text(),
        "agenda": json.loads(AGENDA.read_text()),
        "ledger_sha": sha256(LEDGER),
        "dispositions_sha": sha256(DISPOSITIONS),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    data = inputs["data"]
    result = inputs["result"]
    result_flat = " ".join(result.split())
    current = inputs["current"]
    next_text = inputs["next"]
    status_text = inputs["status"]
    agenda = inputs["agenda"]
    assert isinstance(data, dict) and isinstance(agenda, dict)
    assert all(isinstance(x, str) for x in (result, current, next_text, status_text))

    # Positive controls: both filed horns remain valid on their own terms.
    rf = data["real_form_qualification"]
    check(rf["k95"]["vector_form_inertia"] == [9, 5], "K95 inertia positive control")
    check(rf["k77"]["vector_form_inertia"] == [7, 7], "K77 inertia positive control")
    check(64 * 64 * 4 == 128 * 128 == 16384, "real algebra dimension arithmetic")
    check(rf["real_algebra_dimensions_equal"] is True, "equal dimension preserved")
    check(rf["complexifications_equivalent"] is True, "common complexification preserved")

    # The real bridge must nevertheless fail.
    check(rf["real_algebra_types_equal"] is False, "real algebra types distinguished")
    check(rf["vector_forms_congruent_over_R"] is False, "Sylvester inertia obstruction")
    check(rf["complexification_is_real_typed_bridge"] is False, "complexification not a real bridge")
    check(rf["canonical_real_spin_equivariant_action_bridge"] is False, "no canonical real action bridge")
    check(rf["k95"]["irreducible_real_spinor_dimension"] != rf["k77"]["irreducible_real_spinor_dimension"],
          "real spinor module dimensions differ")

    owner = data["configuration_and_owner_inventory"]
    for token in ("V_src(U,epsilon)", "S_cross", "S_bdy"):
        check(token in owner["named_but_not_explicitly_owned_terms"], f"open term retained: {token}")
    for token in ("kappa", "Z_U"):
        check(token in owner["unowned_or_unbuilt_magnitudes"], f"unowned magnitude retained: {token}")
    check(owner["coefficient_complete_before_target_evaluation"] is False, "coefficient completeness refused")
    check(owner["target_blind_pre_density_freeze"] is False, "target-blind freeze refused")

    var = data["variational_role_audit"]
    check(var["w229_explicit_euler_roles"] == ["E_P", "E_U", "E_A"], "displayed Euler roles exact")
    check(len(var["missing_complete_variations"]) >= 5, "missing variation inventory retained")
    check(var["complete_pre_density_euler_map"] is False, "complete Euler map refused")
    check(var["metric_is_integration_variable_in_w154"] is False, "W154 metric role preserved")
    check(var["complete_hilbert_or_intrinsic_METX_variation"] is False, "Hilbert owner refused")
    check(var["n2_metric_stationarity_is_evaluable"] is False, "N2 evaluation blocked before target")

    compat = data["w154_w229_compatibility"]
    check("c_kin=0" in compat["w230_exact_condition"], "W230 zero-stiffness condition")
    check("nonzero Z_U" in compat["w229_completion"], "W229 nonzero stiffness condition")
    check(compat["one_action_realizes_exact_w154_identity_and_genuine_w229_nonlocal_completion"] is False,
          "W154/W229 exact composite incompatibility")

    admission = data["admission_result"]
    for key in ("real_typed_k77_restatement", "coefficient_complete", "complete_euler_roles",
                "complete_hilbert_roles", "target_blind_pre_density", "candidate_admitted",
                "n2_n3_n6_executed"):
        check(admission[key] is False, f"admission refusal: {key}")
    check(admission["preserved_conditions"] == ["N1", "N4", "N5"], "N1 N4 N5 preserved")

    root = data["root_candidate_rebuild"]
    check(root["synthetic_cbrs1ac"] == "FORBIDDEN", "synthetic CBRS-1AC forbidden")
    check(root["other_named_materially_distinct_target_blind_k77_pre_density_action_candidates"] == [],
          "no other named candidate")
    check(root["current_named_root_candidate_set"] == [], "root candidate set empty")
    check(root["state"] == "EMPTY_AT_CURRENT_SOURCE_AND_ACTION_OWNERSHIP", "root state exact")
    check(len(data["reopen_conditions"]) == 3, "three exact reopen conditions")

    # Artifact governance and bounded grammar.
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("Classification: `INTERNAL_STRUCTURAL_ONLY`" in result, "routing classification")
    check("```gu-typed-objects" in result, "typed objects block")
    check("candidate non-admission" in result, "bounded disposition wording")
    check("No `N2`, `N3` or `N6` target test ran" in result_flat, "target tests explicitly absent")
    for forbidden in ("all K77 actions are impossible", "GU is falsified", "W229 is invalid on K95"):
        check(forbidden not in result, f"forbidden overclaim absent: {forbidden}")

    evidence = data["evidence"]
    check(evidence in current, "CURRENT-STATE points to evidence")
    check(evidence in next_text, "NEXT-STEPS points to evidence")
    check(evidence not in status_text, "protected RESEARCH-STATUS remains untouched")
    item = next((x for x in agenda["work_items"] if x["id"] == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD"), None)
    check(isinstance(item, dict), "agenda work item retained")
    latest_result = item.get("latest_result", "") if isinstance(item, dict) else ""
    next_swing = item.get("next_swing", "") if isinstance(item, dict) else ""
    check("W154/W229" in latest_result and "nonadmitted" in latest_result,
          "agenda latest result updated")
    check("repository-wide Progress frontier" in next_swing, "agenda rerank next swing")

    check(inputs["ledger_sha"] == EXPECTED_LEDGER_SHA256, "conditional ledger byte-identical")
    check(inputs["dispositions_sha"] == EXPECTED_DISPOSITIONS_SHA256, "terminal register byte-identical")
    for key in ("ledger_verdict_change", "terminal_disposition_register_change", "source_ownership_change",
                "prediction_or_confirmation_change", "claim_status_change", "canon_verdict_change",
                "public_posture_change"):
        check(data[key] == "none", f"protected effect unchanged: {key}")
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
    changed["data"]["real_form_qualification"]["canonical_real_spin_equivariant_action_bridge"] = True
    mutations.append(("invent-bridge", "no canonical real action bridge", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["real_form_qualification"]["k77"]["vector_form_inertia"] = [9, 5]
    mutations.append(("erase-inertia", "K77 inertia positive control", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["configuration_and_owner_inventory"]["coefficient_complete_before_target_evaluation"] = True
    mutations.append(("invent-coefficients", "coefficient completeness refused", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["variational_role_audit"]["complete_hilbert_or_intrinsic_METX_variation"] = True
    mutations.append(("invent-hilbert", "Hilbert owner refused", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["w154_w229_compatibility"]["one_action_realizes_exact_w154_identity_and_genuine_w229_nonlocal_completion"] = True
    mutations.append(("erase-fork", "W154/W229 exact composite incompatibility", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["admission_result"]["n2_n3_n6_executed"] = True
    mutations.append(("invent-target-test", "admission refusal: n2_n3_n6_executed", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["root_candidate_rebuild"]["current_named_root_candidate_set"] = ["CBRS-1AC"]
    mutations.append(("synthesize-root", "root candidate set empty", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["ledger_verdict_change"] = "moved"
    mutations.append(("move-ledger", "protected effect unchanged: ledger_verdict_change", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace("Classification: `INTERNAL_STRUCTURAL_ONLY`", "")
    mutations.append(("drop-routing-class", "routing classification", changed))

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
