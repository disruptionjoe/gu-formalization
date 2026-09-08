#!/usr/bin/env python3
"""Baseline and hostile checks for K157."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k157-nested-cylinder-count-transfer-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k157-nested-cylinder-count-transfer-wave-2026-09-08.md"


def load_solver():
    path = Path(__file__).with_name("k157_nested_cylinder_count_transfer.py")
    spec = importlib.util.spec_from_file_location("k157_solver_runtime", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    cores = data.get("nested_cylinder_cores", {})
    for key in ("finite_mode_support_is_nested", "graph_radius_is_nested", "q00_and_q10_are_explicit", "signed_flavor_transports_q10_to_q01"):
        if cores.get(key) is not True:
            failures.append(f"cores:{key}")
    anchors = data.get("finite_anchors", {})
    for key in ("two_mode_q00_has_exactly_one_value_below_minus_one", "two_mode_q10_has_exactly_one_value_below_minus_one", "inverse_iteration_trials_have_exact_rational_residuals", "bare_K153_seed_is_not_called_a_ground_trial"):
        if anchors.get(key) is not True:
            failures.append(f"anchors:{key}")
    if anchors.get("finite_count_is_native_count") is not False:
        failures.append("anchors:finite_overclaim")
    tail = data.get("outward_tail_ledger", {})
    for key in ("cofinal_delta_and_momentum_radius_are_explicit", "free_multiplier_and_dressed_Hilbert_tail_are_outward_bounded", "graph_boundary_constant_remains_missing", "normal_ordered_core_constant_remains_missing", "complete_total_tail_is_not_emitted"):
        if tail.get(key) is not True:
            failures.append(f"tail:{key}")
    transfer = data.get("complete_count_transfer", {})
    for key in ("finite_rank_one_contours_are_exact", "finite_reference_is_extended_by_a_decoupled_free_tail_on_the_common_carrier", "Riesz_projection_difference_bound_is_proved", "rank_is_preserved_when_projection_norm_difference_is_below_one", "complete_native_contour_error_remains_missing"):
        if transfer.get(key) is not True:
            failures.append(f"transfer:{key}")
    denied = data.get("boundaries", {})
    for key in ("native_ground_count_certified", "native_energy_interval_emitted", "threshold_or_Gram_closure", "physical_or_source_selection", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit"):
        if denied.get(key) is not False:
            failures.append(f"boundary:{key}")
    if denied.get("canon_verdict_change") != "none" or denied.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary:metadata")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("nested", "finite rank-one", "complete contour", "missing", "no native count", "Born"):
        if token not in ceiling:
            failures.append(f"ceiling:{token}")
    return failures


def exact_checks() -> list[tuple[str, bool]]:
    demo = SOLVER.demo()
    q00, q10 = demo["finite_anchors"]
    c00, c10 = demo["cores"]
    ledger = demo["cofinal_component_ledger_n4096"]
    contours = demo["finite_contours"]
    artifact = ARTIFACT.read_text(encoding="utf-8")
    return [
        ("q00 mode core nests", c00["mode_one_embeds_in_mode_two"] is True),
        ("q10 mode core nests", c10["mode_one_embeds_in_mode_two"] is True),
        ("q00 graph cores nest", c00["graph_radius_is_nested"] is True),
        ("q10 graph cores nest", c10["graph_radius_is_nested"] is True),
        ("q00 radius dimensions", c00["dimensions"]["M2R4"] == 51),
        ("q10 radius dimensions", c10["dimensions"]["M2R4"] == 50),
        ("q00 exact finite count", q00["spectral_count_below_threshold"] == 1 and q00["threshold_multiplicity"] == 0),
        ("q10 exact finite count", q10["spectral_count_below_threshold"] == 1 and q10["threshold_multiplicity"] == 0),
        ("q10 seed has lower competitors", q10["spectral_count_below_seed_rayleigh"] >= 2),
        ("q00 trial below minus one", float(SOLVER.q(q00["trial_rayleigh_dyadic_interval"][1])) < -1),
        ("q10 trial below minus one", float(SOLVER.q(q10["trial_rayleigh_dyadic_interval"][1])) < -1),
        ("q00 residual improves", float(SOLVER.q(q00["trial_residual_sq_dyadic_upper"])) < 1 / 500),
        ("q10 residual is finite", float(SOLVER.q(q10["trial_residual_sq_dyadic_upper"])) < 1 / 40),
        ("cofinal physical radius", ledger["physical_momentum_radius"] == 4096),
        ("free error outward", ledger["free_graph_relative_error_upper"] == "1/4096"),
        ("dressed tail outward", ledger["dressed_point_tail_sq_upper"] == "1/12288"),
        ("missing graph tail stays null", ledger["graph_boundary_error_upper"] is None),
        ("missing core tail stays null", ledger["normal_ordered_core_graph_error_upper"] is None),
        ("q00 finite contour rank", contours[0]["finite_projection_rank"] == 1),
        ("q10 finite contour rank", contours[1]["finite_projection_rank"] == 1),
        ("finite spectra lie right of minus five", all(SOLVER.q(c["gershgorin_lower_bound"]) > -5 for c in contours)),
        ("abstract Riesz transfer passes", demo["abstract_positive_rank_transfer"]["native_projection_rank"] == 1),
        ("native count refused", demo["native_count_emitted"] is False),
        ("artifact names complete contour", "complete separating contour" in artifact),
        ("artifact refuses finite promotion", "finite rank-one anchor is not" in artifact),
    ]


def rejection_checks() -> list[tuple[str, bool]]:
    cases = (
        ("noncommon carrier", dict(contour_perimeter=10, resolvent_error_upper="1/2", finite_projection_rank=1, common_carrier=False, complete_contour=True)),
        ("incomplete contour", dict(contour_perimeter=10, resolvent_error_upper="1/2", finite_projection_rank=1, common_carrier=True, complete_contour=False)),
        ("projection gap equals one", dict(contour_perimeter=12, resolvent_error_upper="1/2", finite_projection_rank=1, common_carrier=True, complete_contour=True)),
        ("negative error", dict(contour_perimeter=10, resolvent_error_upper="-1/2", finite_projection_rank=1, common_carrier=True, complete_contour=True)),
    )
    out = []
    for name, kwargs in cases:
        try:
            SOLVER.riesz_rank_transfer(**kwargs)
        except SOLVER.CertificateError:
            out.append((name, True))
        else:
            out.append((name, False))
    for name, value in (("zero cofinal index", 0), ("negative cofinal index", -1)):
        try:
            SOLVER.cofinal_component_ledger(value)
        except SOLVER.CertificateError:
            out.append((name, True))
        else:
            out.append((name, False))
    return out


def selftest(data: dict, baseline: list[tuple[str, bool]] | None = None) -> int:
    baseline = exact_checks() if baseline is None else baseline
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    updates = (
        ("erase mode nesting", lambda d: d["nested_cylinder_cores"].__setitem__("finite_mode_support_is_nested", False)),
        ("erase q10 core", lambda d: d["nested_cylinder_cores"].__setitem__("q00_and_q10_are_explicit", False)),
        ("invent native finite count", lambda d: d["finite_anchors"].__setitem__("finite_count_is_native_count", True)),
        ("call seed ground", lambda d: d["finite_anchors"].__setitem__("bare_K153_seed_is_not_called_a_ground_trial", False)),
        ("invent graph constant", lambda d: d["outward_tail_ledger"].__setitem__("graph_boundary_constant_remains_missing", False)),
        ("invent complete tail", lambda d: d["outward_tail_ledger"].__setitem__("complete_total_tail_is_not_emitted", False)),
        ("erase Riesz bound", lambda d: d["complete_count_transfer"].__setitem__("Riesz_projection_difference_bound_is_proved", False)),
        ("erase common reference extension", lambda d: d["complete_count_transfer"].__setitem__("finite_reference_is_extended_by_a_decoupled_free_tail_on_the_common_carrier", False)),
        ("invent native contour", lambda d: d["complete_count_transfer"].__setitem__("complete_native_contour_error_remains_missing", False)),
        ("invent native count", lambda d: d["boundaries"].__setitem__("native_ground_count_certified", True)),
        ("invent energy", lambda d: d["boundaries"].__setitem__("native_energy_interval_emitted", True)),
        ("invent source", lambda d: d["boundaries"].__setitem__("physical_or_source_selection", True)),
        ("invent Born", lambda d: d["boundaries"].__setitem__("Born_rule_derived", True)),
        ("score holdout", lambda d: d["boundaries"].__setitem__("held_out_scored", True)),
        ("promote canon", lambda d: d["boundaries"].__setitem__("canon_verdict_change", "changed")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "native physical spectrum proved")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    caught.extend(rejection_checks())
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K157 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data, checks)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
