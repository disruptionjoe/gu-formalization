#!/usr/bin/env python3
"""Baseline and hostile controls for K159."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k159-fractional-boundary-weyl-resolvent-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k159-fractional-boundary-weyl-resolvent-wave-2026-09-08.md"


def load_solver():
    path = Path(__file__).with_name("k159_fractional_boundary_weyl_resolvent.py")
    spec = importlib.util.spec_from_file_location("k159_solver_runtime", path)
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
    if scope.get("target_claim") != "INTERNAL_TARGET:K158_COMMON_FREE_FORM_OR_BOUNDARY_RESOLVENT_REPAIR":
        failures.append("target")
    if scope.get("target_claim_verdict") != "COMMON_FREE_FORM_ROUTE_KILLED_BOUNDARY_WEYL_ROUTE_NOT_YET_FALSIFIED":
        failures.append("verdict")
    fractional = data.get("fractional_domain", {})
    expected = {
        "sharp_threshold": "s<1/2",
        "Hilbert_s0_member": True,
        "quarter_graph_member": True,
        "free_form_s_half_member": False,
        "free_operator_graph_s1_member": False,
    }
    for key, value in expected.items():
        if fractional.get(key) != value:
            failures.append(f"fractional:{key}")
    boundary = data.get("boundary_weyl_route", {})
    for key in ("operator_valued_denominator_required", "native_denominator_is_operator_valued_on_spectator_Fock_space", "complete_contour_uniformity_required", "abstract_positive_control_passes"):
        if boundary.get(key) is not True:
            failures.append(f"boundary:{key}")
    for key in ("free_graph_chart_error_required", "free_form_chart_error_required", "native_denominator_separation_serialized"):
        if boundary.get(key) is not False:
            failures.append(f"boundary:{key}")
    count = data.get("count_boundary", {})
    for key in ("same_cofinal_reference_rank_required", "native_left_floor_required"):
        if count.get(key) is not True:
            failures.append(f"count:{key}")
    for key in ("same_cofinal_reference_rank_certified", "native_left_floor_certified", "native_rank_one_count_certified"):
        if count.get(key) is not False:
            failures.append(f"count:{key}")
    roles = data.get("normal_ordered_components", {})
    if roles.get("required_for_boundary_weyl_transfer") is not False or roles.get("required_for_regular_representative_or_K152") is not True:
        failures.append("normal_roles")
    denied = data.get("boundaries", {})
    for key in ("native_ground_count_certified", "native_energy_interval_emitted", "threshold_or_Gram_closure", "physical_or_source_selection", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit"):
        if denied.get(key) is not False:
            failures.append(f"denied:{key}")
    if denied.get("canon_verdict_change") != "none" or denied.get("paper_release_or_public_posture_change") != "none":
        failures.append("denied:metadata")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("s<1/2", "form domain", "boundary/Weyl", "cofinal", "left-tail", "No native count", "Born"):
        if token not in ceiling:
            failures.append(f"ceiling:{token}")
    return failures


def exact_checks() -> list[tuple[str, bool]]:
    demo = SOLVER.demo()
    s0, s14, s12, s1 = demo["fractional_domains"]
    ledger = demo["cofinal_fractional_ledger_n4096"]
    control = demo["abstract_boundary_weyl_positive_control"]
    artifact = ARTIFACT.read_text(encoding="utf-8")
    return [
        ("Hilbert membership", s0["sharp_membership"] is True),
        ("quarter membership", s14["sharp_membership"] is True),
        ("form endpoint excluded", s12["sharp_membership"] is False),
        ("operator graph excluded", s1["sharp_membership"] is False),
        ("sharp threshold", s14["threshold"] == "s<1/2"),
        ("Hilbert tail", s0["tail_square_upper"] == "1/12288"),
        ("quarter tail", s14["tail_square_upper"] == "1/96"),
        ("endpoint logarithmic divergence", "logarithmic" in s12["divergence"]),
        ("cofinal delta", ledger["delta"] == "1/4096"),
        ("cofinal quarter tail", ledger["high_momentum_tail_sq_per_channel_upper"] == "1/96"),
        ("cofinal cell bound", ledger["cell_error_sq_per_channel_upper"] == "1/8388608"),
        ("fractional convergence", ledger["converges_to_zero"] is True),
        ("free form not recovered", ledger["free_form_exponent_one_half_available"] is False),
        ("Weyl separation", control["weyl_neumann_parameter"] == "1/500"),
        ("abstract contour closes", control["rank_transfer_certified"] is True),
        ("no graph premise", control["uses_free_graph_chart_error"] is False),
        ("no free form premise", control["uses_free_form_chart_error"] is False),
        ("normal tails role split", demo["normal_ordered_tails_required_for_boundary_weyl_transfer"] is False and demo["normal_ordered_tails_required_for_regular_representative_or_K152_route"] is True),
        ("native count refused", demo["native_count_emitted"] is False),
        ("native interval refused", demo["native_energy_interval_emitted"] is False),
        ("artifact names form obstruction", "free quadratic-form domain" in artifact),
        ("artifact names Weyl repair", "Krein" in artifact and "Weyl" in artifact),
        ("artifact preserves local versus total count", "left of `-5`" in artifact),
        ("artifact refuses source promotion", "Born" in artifact and "source" in artifact),
    ]


def rejection_checks() -> list[tuple[str, bool]]:
    checks: list[tuple[str, bool]] = []
    for name, kwargs in (
        ("Weyl denominator collision", dict(free_resolvent_error=0, gamma_norm_upper=1, gamma_error_upper=0, reference_denominator_inverse_upper=2, weyl_denominator_error_upper="1/2")),
        ("contour gap failure", dict(free_resolvent_error="1/2", gamma_norm_upper=1, gamma_error_upper="1/10", reference_denominator_inverse_upper=1, weyl_denominator_error_upper="1/10", require_rank_transfer=True)),
    ):
        try:
            SOLVER.boundary_weyl_resolvent_budget(**kwargs)
        except SOLVER.CertificateError:
            checks.append((name, True))
        else:
            checks.append((name, False))
    bad_admissions = (
        ("wrong family", dict(same_cofinal_family=False, reference_rank=1, reference_rank_ref="x", complete_contour_error="1/2", native_left_floor=-5, native_left_floor_ref="y")),
        ("missing rank", dict(same_cofinal_family=True, reference_rank=None, reference_rank_ref=None, complete_contour_error="1/2", native_left_floor=-5, native_left_floor_ref="y")),
        ("missing contour", dict(same_cofinal_family=True, reference_rank=1, reference_rank_ref="x", complete_contour_error=None, native_left_floor=-5, native_left_floor_ref="y")),
        ("weak left floor", dict(same_cofinal_family=True, reference_rank=1, reference_rank_ref="x", complete_contour_error="1/2", native_left_floor=-6, native_left_floor_ref="y")),
    )
    for name, kwargs in bad_admissions:
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
        ("invent form membership", lambda d: d["fractional_domain"].__setitem__("free_form_s_half_member", True)),
        ("invent graph membership", lambda d: d["fractional_domain"].__setitem__("free_operator_graph_s1_member", True)),
        ("erase denominator", lambda d: d["boundary_weyl_route"].__setitem__("operator_valued_denominator_required", False)),
        ("collapse native boundary space", lambda d: d["boundary_weyl_route"].__setitem__("native_denominator_is_operator_valued_on_spectator_Fock_space", False)),
        ("invent free-form need", lambda d: d["boundary_weyl_route"].__setitem__("free_form_chart_error_required", True)),
        ("invent native Weyl data", lambda d: d["boundary_weyl_route"].__setitem__("native_denominator_separation_serialized", True)),
        ("invent cofinal rank", lambda d: d["count_boundary"].__setitem__("same_cofinal_reference_rank_certified", True)),
        ("invent left floor", lambda d: d["count_boundary"].__setitem__("native_left_floor_certified", True)),
        ("invent native count", lambda d: d["count_boundary"].__setitem__("native_rank_one_count_certified", True)),
        ("misroute normal tails", lambda d: d["normal_ordered_components"].__setitem__("required_for_boundary_weyl_transfer", True)),
        ("invent energy", lambda d: d["boundaries"].__setitem__("native_energy_interval_emitted", True)),
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
    print(f"K159 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data, checks)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
