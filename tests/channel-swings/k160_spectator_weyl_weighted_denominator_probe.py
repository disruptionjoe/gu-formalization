#!/usr/bin/env python3
"""Baseline-first and hostile controls for K160."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k160-spectator-weyl-weighted-denominator-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k160-spectator-weyl-weighted-denominator-wave-2026-09-08.md"


def load_solver():
    path = Path(__file__).with_name("k160_spectator_weyl_weighted_denominator.py")
    spec = importlib.util.spec_from_file_location("k160_solver_runtime", path)
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
    scope = data.get("scope", {})
    if scope.get("target_claim") != "INTERNAL_TARGET:K159_UNWEIGHTED_SPECTATOR_WEYL_CONVERGENCE":
        failures.append("target")
    if scope.get("target_claim_verdict") != "ORDINARY_OPERATOR_NORM_ROUTE_KILLED_WEIGHTED_ROUTE_NOT_YET_FALSIFIED":
        failures.append("verdict")
    unweighted = data.get("unweighted_spectator_tail", {})
    for key in ("matched_counterterm_coordinate_retained", "fixed_spectator_energy_convergence", "spectator_energy_spectrum_unbounded"):
        if unweighted.get(key) is not True:
            failures.append(f"unweighted:{key}")
    for key in ("ordinary_operator_norm_cutoff_error_finite", "ordinary_operator_norm_Weyl_convergence", "K159_unweighted_native_dm_available", "finite_impurity_matrix_substitution_allowed"):
        if unweighted.get(key) is not False:
            failures.append(f"unweighted:{key}")
    weighted = data.get("weighted_diagonal_route", {})
    if weighted.get("weight") != "(1+S)^(-1)" or weighted.get("n4096_outward_upper") != "1049/49152":
        failures.append("weighted:exact")
    if weighted.get("complete_K157_rectangle_covered") is not True:
        failures.append("weighted:contour")
    for key in ("Pauli_and_exchange_components_serialized", "complete_native_weighted_denominator_error_serialized"):
        if weighted.get(key) is not False:
            failures.append(f"weighted:{key}")
    compiler = data.get("weighted_inverse_compiler", {})
    for key in ("complete_weighted_error_required", "reference_inverse_smoothing_required", "low_energy_denominator_separation_required", "abstract_positive_control_passes"):
        if compiler.get(key) is not True:
            failures.append(f"compiler:{key}")
    for key in ("ordinary_unweighted_dm_required", "native_inverse_smoothing_serialized", "native_complete_contour_error_serialized"):
        if compiler.get(key) is not False:
            failures.append(f"compiler:{key}")
    count = data.get("count_boundary", {})
    for key in ("same_cofinal_reference_rank_required", "native_left_floor_required", "signed_charge_intertwiner_required"):
        if count.get(key) is not True:
            failures.append(f"count:{key}")
    for key in ("same_cofinal_reference_rank_certified", "native_left_floor_certified", "native_rank_one_count_certified"):
        if count.get(key) is not False:
            failures.append(f"count:{key}")
    denied = data.get("boundaries", {})
    for key in ("native_ground_count_certified", "native_energy_interval_emitted", "threshold_or_Gram_closure", "full_Fock_scattering_or_NESS", "physical_or_source_selection", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit"):
        if denied.get(key) is not False:
            failures.append(f"denied:{key}")
    if denied.get("canon_verdict_change") != "none" or denied.get("paper_release_or_public_posture_change") != "none":
        failures.append("denied:metadata")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("infinite ordinary operator norm", "(1+S)^(-1)", "Pauli/exchange", "inverse-smoothing", "left-tail", "No native count", "Born"):
        if token not in ceiling:
            failures.append(f"ceiling:{token}")
    return failures


def exact_checks() -> list[tuple[str, bool]]:
    demo = SOLVER.demo()
    obstruction = demo["unweighted_tail_obstruction_n4096"]
    weighted4 = demo["weighted_diagonal_tail_n4096"]
    weighted16 = demo["weighted_diagonal_tail_n65536"]
    control = demo["abstract_weighted_resolvent_positive_control"]
    artifact = ARTIFACT.read_text(encoding="utf-8")
    return [
        ("cutoff retained", obstruction["cutoff"] == 4096),
        ("matched shift retained", obstruction["matched_subtraction_shift"] == "256"),
        ("pivot exact", obstruction["pivot_P"] == 4096),
        ("fixed fibers converge", obstruction["fixed_s_tail_converges"] is True),
        ("operator tail infinite", obstruction["ordinary_operator_norm_tail_is_finite"] is False),
        ("ordinary norm route killed", obstruction["ordinary_operator_norm_convergence"] is False),
        ("native dm refused", obstruction["native_unweighted_dm_available"] is False),
        ("one-energy weight", weighted4["weight"] == "(1+S)^(-1)"),
        ("n4096 exact", weighted4["diagonal_weighted_tail_upper"] == "1049/49152"),
        ("n65536 exact", weighted16["diagonal_weighted_tail_upper"] == "1049/786432"),
        ("weighted convergence", weighted4["converges_to_zero"] is True),
        ("complete denominator refused", weighted4["complete_native_weighted_denominator_error_emitted"] is False),
        ("Pauli exchange not smuggled", weighted4["Pauli_and_exchange_components_included"] is False),
        ("weighted theta", control["weighted_neumann_parameter"] == "1/500"),
        ("approximant inverse", control["approximant_denominator_inverse_upper"] == "1000/499"),
        ("inverse difference", control["denominator_inverse_error_upper"] == "2/499"),
        ("resolvent total", control["complete_resolvent_error_upper"] == "4497/499000"),
        ("abstract rank transfer", control["rank_transfer_certified"] is True),
        ("weighted premise required", control["complete_weighted_denominator_error_required"] is True),
        ("inverse smoothing required", control["reference_inverse_smoothing_required"] is True),
        ("native count refused", demo["native_count_emitted"] is False),
        ("native interval refused", demo["native_energy_interval_emitted"] is False),
        ("artifact proves logarithmic obstruction", "log(s/(4P))" in artifact and "fiberwise cutoff convergence" in artifact),
        ("artifact preserves operator-valued space", "finite impurity matrix" in artifact and "spectator-Fock" in artifact),
        ("artifact types weighted repair", "weighted Neumann" in artifact and "inverse-smoothing" in artifact),
        ("artifact refuses source promotion", "Born" in artifact and "source" in artifact),
    ]


def rejection_checks() -> list[tuple[str, bool]]:
    checks: list[tuple[str, bool]] = []
    bad_weighted = (
        ("zero weight", dict(cutoff=4096, weight_exponent=0)),
        ("nonexact cutoff", dict(cutoff=4095, weight_exponent="1/2")),
    )
    for name, kwargs in bad_weighted:
        try:
            SOLVER.weighted_diagonal_tail_bound(**kwargs)
        except SOLVER.CertificateError:
            checks.append((name, True))
        else:
            checks.append((name, False))
    for name, kwargs in (
        ("weighted collision", dict(free_resolvent_error=0, gamma_norm_upper=1, gamma_error_upper=0, reference_denominator_inverse_upper=1, weighted_denominator_error_upper="1/2", reference_inverse_smoothing_upper=2)),
        ("weighted contour gap", dict(free_resolvent_error="1/2", gamma_norm_upper=1, gamma_error_upper="1/10", reference_denominator_inverse_upper=1, weighted_denominator_error_upper="1/10", reference_inverse_smoothing_upper=1, require_rank_transfer=True)),
    ):
        try:
            SOLVER.weighted_denominator_resolvent_budget(**kwargs)
        except SOLVER.CertificateError:
            checks.append((name, True))
        else:
            checks.append((name, False))
    base = dict(
        complete_weighted_denominator_ref="weighted",
        inverse_smoothing_ref="smooth",
        low_energy_denominator_ref="low",
        same_cofinal_rank=1,
        same_cofinal_rank_ref="rank",
        complete_contour_error="1/2",
        native_left_floor=-5,
        native_left_floor_ref="floor",
        signed_charge_intertwiner_ref="charge",
    )
    variants = (
        ("missing weighted reference", "complete_weighted_denominator_ref", None),
        ("missing inverse smoothing", "inverse_smoothing_ref", None),
        ("missing low energy", "low_energy_denominator_ref", None),
        ("missing cofinal rank", "same_cofinal_rank_ref", None),
        ("weak contour", "complete_contour_error", "3/5"),
        ("weak left floor", "native_left_floor", -6),
        ("missing charge", "signed_charge_intertwiner_ref", None),
    )
    for name, key, value in variants:
        kwargs = dict(base)
        kwargs[key] = value
        try:
            SOLVER.native_count_admission(**kwargs)
        except SOLVER.CertificateError:
            checks.append((name, True))
        else:
            checks.append((name, False))
    return checks


def selftest(data: dict, baseline: list[tuple[str, bool]]) -> int:
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    updates = (
        ("invent finite norm", lambda d: d["unweighted_spectator_tail"].__setitem__("ordinary_operator_norm_cutoff_error_finite", True)),
        ("invent norm convergence", lambda d: d["unweighted_spectator_tail"].__setitem__("ordinary_operator_norm_Weyl_convergence", True)),
        ("invent native dm", lambda d: d["unweighted_spectator_tail"].__setitem__("K159_unweighted_native_dm_available", True)),
        ("allow finite matrix collapse", lambda d: d["unweighted_spectator_tail"].__setitem__("finite_impurity_matrix_substitution_allowed", True)),
        ("erase weighted contour", lambda d: d["weighted_diagonal_route"].__setitem__("complete_K157_rectangle_covered", False)),
        ("invent Pauli exchange", lambda d: d["weighted_diagonal_route"].__setitem__("Pauli_and_exchange_components_serialized", True)),
        ("invent complete denominator", lambda d: d["weighted_diagonal_route"].__setitem__("complete_native_weighted_denominator_error_serialized", True)),
        ("erase smoothing need", lambda d: d["weighted_inverse_compiler"].__setitem__("reference_inverse_smoothing_required", False)),
        ("invent native smoothing", lambda d: d["weighted_inverse_compiler"].__setitem__("native_inverse_smoothing_serialized", True)),
        ("invent contour error", lambda d: d["weighted_inverse_compiler"].__setitem__("native_complete_contour_error_serialized", True)),
        ("invent cofinal rank", lambda d: d["count_boundary"].__setitem__("same_cofinal_reference_rank_certified", True)),
        ("invent left floor", lambda d: d["count_boundary"].__setitem__("native_left_floor_certified", True)),
        ("invent native count", lambda d: d["count_boundary"].__setitem__("native_rank_one_count_certified", True)),
        ("invent interval", lambda d: d["boundaries"].__setitem__("native_energy_interval_emitted", True)),
        ("invent source", lambda d: d["boundaries"].__setitem__("physical_or_source_selection", True)),
        ("invent Born", lambda d: d["boundaries"].__setitem__("Born_rule_derived", True)),
        ("score holdout", lambda d: d["boundaries"].__setitem__("held_out_scored", True)),
        ("promote canon", lambda d: d["boundaries"].__setitem__("canon_verdict_change", "changed")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "native physical prediction proved")),
    )
    caught: list[tuple[str, bool]] = []
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
    print(f"K160 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data, checks)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
